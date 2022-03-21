������������bsdy """
==========================
Tricontour Smooth Delaunay
==========================

Demonstrates high-resolution tricontouring of a random set of points;
a `matplotlib.tri.TriAnalyzer` is used to improve the plot quality.

The initial data points and triangular grid for this demo are:

- a set of random points is instantiated, inside [-1, 1] x [-1, 1] square
- A Delaunay triangulation of these points is then computed, of which a
  random subset of triangles is masked out by the user (based on
  *init_mask_frac* parameter). This simulates invalidated data.

The proposed generic procedure to obtain a high resolution contouring of such
a data set is the following:

1. Compute an extended mask with a `matplotlib.tri.TriAnalyzer`, which will
   exclude badly shaped (flat) triangles from the border of the
   triangulation. Apply the mask to the triangulation (using set_mask).
2. Refine and interpolate the data using a `matplotlib.tri.UniformTriRefiner`.
3. Plot the refined data with `~.axes.Axes.tricontour`.

"""���`a
���bkndfrom���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnctri���`a ���bknfimport���`a ���`mTriangulation���`a,���`a ���`kTriAnalyzer���`a,���`a ���`qUniformTriRefiner���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���`a
���`a
���bc1xN# ----------------------------------------------------------------------------���`a
���bc1x# Analytical test function���`a
���bc1xN# ----------------------------------------------------------------------------���`a
���akcdef���`a ���bnfnexperiment_res���`a(���`ax���`a,���`a ���`ay���`a)���`a:���`a
���`d    ���bsdx;"""An analytic function representing experiment results."""���`a
���`d    ���`ax���`a ���aoa=���`a ���bmia2���`a ���aoa*���`a ���`ax���`a
���`d    ���`br1���`a ���aoa=���`a ���`bnp���aoa.���`dsqrt���`a(���`a(���bmfc0.5���`a ���aoa-���`a ���`ax���`a)���aoa*���aoa*���bmia2���`a ���aoa+���`a ���`a(���bmfc0.5���`a ���aoa-���`a ���`ay���`a)���aoa*���aoa*���bmia2���`a)���`a
���`d    ���`ftheta1���`a ���aoa=���`a ���`bnp���aoa.���`garctan2���`a(���bmfc0.5���`a ���aoa-���`a ���`ax���`a,���`a ���bmfc0.5���`a ���aoa-���`a ���`ay���`a)���`a
���`d    ���`br2���`a ���aoa=���`a ���`bnp���aoa.���`dsqrt���`a(���`a(���aoa-���`ax���`a ���aoa-���`a ���bmfc0.2���`a)���aoa*���aoa*���bmia2���`a ���aoa+���`a ���`a(���aoa-���`ay���`a ���aoa-���`a ���bmfc0.2���`a)���aoa*���aoa*���bmia2���`a)���`a
���`d    ���`ftheta2���`a ���aoa=���`a ���`bnp���aoa.���`garctan2���`a(���aoa-���`ax���`a ���aoa-���`a ���bmfc0.2���`a,���`a ���aoa-���`ay���`a ���aoa-���`a ���bmfc0.2���`a)���`a
���`d    ���`az���`a ���aoa=���`a ���`a(���bmia4���`a ���aoa*���`a ���`a(���`bnp���aoa.���`cexp���`a(���`a(���`br1���aoa/���bmib10���`a)���aoa*���aoa*���bmia2���`a)���`a ���aoa-���`a ���bmia1���`a)���`a ���aoa*���`a ���bmib30���`a ���aoa*���`a ���`bnp���aoa.���`ccos���`a(���bmia3���`a ���aoa*���`a ���`ftheta1���`a)���`a ���aoa+���`a
���`i         ���`a(���`bnp���aoa.���`cexp���`a(���`a(���`br2���aoa/���bmib10���`a)���aoa*���aoa*���bmia2���`a)���`a ���aoa-���`a ���bmia1���`a)���`a ���aoa*���`a ���bmib30���`a ���aoa*���`a ���`bnp���aoa.���`ccos���`a(���bmia5���`a ���aoa*���`a ���`ftheta2���`a)���`a ���aoa+���`a
���`i         ���bmia2���`a ���aoa*���`a ���`a(���`ax���aoa*���aoa*���bmia2���`a ���aoa+���`a ���`ay���aoa*���aoa*���bmia2���`a)���`a)���`a
���`d    ���akfreturn���`a ���`a(���`bnp���aoa.���`cmax���`a(���`az���`a)���`a ���aoa-���`a ���`az���`a)���`a ���aoa/���`a ���`a(���`bnp���aoa.���`cmax���`a(���`az���`a)���`a ���aoa-���`a ���`bnp���aoa.���`cmin���`a(���`az���`a)���`a)���`a
���`a
���bc1xN# ----------------------------------------------------------------------------���`a
���bc1xH# Generating the initial data test points and triangulation for the demo���`a
���bc1xN# ----------------------------------------------------------------------------���`a
���bc1x&# User parameters for data test points���`a
���`a
���bc1x@# Number of test data points, tested from 3 to 5000 for subdiv=3���`a
���`fn_test���`a ���aoa=���`a ���bmic200���`a
���`a
���bc1xH# Number of recursive subdivisions of the initial mesh for smooth plots.���`a
���bc1xJ# Values >3 might result in a very high number of triangles for the refine���`a
���bc1x2# mesh: new triangles numbering = (4**subdiv)*ntri���`a
���`fsubdiv���`a ���aoa=���`a ���bmia3���`a
���`a
���bc1xO# Float > 0. adjusting the proportion of (invalid) initial triangles which will���`a
���bc1x%# be masked out. Enter 0 for no mask.���`a
���`ninit_mask_frac���`a ���aoa=���`a ���bmfc0.0���`a
���`a
���bc1xN# Minimum circle ratio - border triangles with circle ratio below this will be���`a
���bc1xI# masked if they touch a border. Suggested value 0.01; use -1 to keep all���`a
���bc1l# triangles.���`a
���`pmin_circle_ratio���`a ���aoa=���`a ���bmfc.01���`a
���`a
���bc1o# Random points���`a
���`jrandom_gen���`a ���aoa=���`a ���`bnp���aoa.���`frandom���aoa.���`kRandomState���`a(���`dseed���aoa=���bmih19680801���`a)���`a
���`fx_test���`a ���aoa=���`a ���`jrandom_gen���aoa.���`guniform���`a(���aoa-���bmfb1.���`a,���`a ���bmfb1.���`a,���`a ���`dsize���aoa=���`fn_test���`a)���`a
���`fy_test���`a ���aoa=���`a ���`jrandom_gen���aoa.���`guniform���`a(���aoa-���bmfb1.���`a,���`a ���bmfb1.���`a,���`a ���`dsize���aoa=���`fn_test���`a)���`a
���`fz_test���`a ���aoa=���`a ���`nexperiment_res���`a(���`fx_test���`a,���`a ���`fy_test���`a)���`a
���`a
���bc1x%# meshing with Delaunay triangulation���`a
���`ctri���`a ���aoa=���`a ���`mTriangulation���`a(���`fx_test���`a,���`a ���`fy_test���`a)���`a
���`dntri���`a ���aoa=���`a ���`ctri���aoa.���`itriangles���aoa.���`eshape���`a[���bmia0���`a]���`a
���`a
���bc1x"# Some invalid data are masked out���`a
���`imask_init���`a ���aoa=���`a ���`bnp���aoa.���`ezeros���`a(���`dntri���`a,���`a ���`edtype���aoa=���bnbdbool���`a)���`a
���`jmasked_tri���`a ���aoa=���`a ���`jrandom_gen���aoa.���`grandint���`a(���bmia0���`a,���`a ���`dntri���`a,���`a ���bnbcint���`a(���`dntri���`a ���aoa*���`a ���`ninit_mask_frac���`a)���`a)���`a
���`imask_init���`a[���`jmasked_tri���`a]���`a ���aoa=���`a ���bkcdTrue���`a
���`ctri���aoa.���`hset_mask���`a(���`imask_init���`a)���`a
���`a
���`a
���bc1xN# ----------------------------------------------------------------------------���`a
���bc1xL# Improving the triangulation before high-res plots: removing flat triangles���`a
���bc1xN# ----------------------------------------------------------------------------���`a
���bc1xF# masking badly shaped triangles at the border of the triangular mesh.���`a
���`dmask���`a ���aoa=���`a ���`kTriAnalyzer���`a(���`ctri���`a)���aoa.���`qget_flat_tri_mask���`a(���`pmin_circle_ratio���`a)���`a
���`ctri���aoa.���`hset_mask���`a(���`dmask���`a)���`a
���`a
���bc1s# refining the data���`a
���`grefiner���`a ���aoa=���`a ���`qUniformTriRefiner���`a(���`ctri���`a)���`a
���`htri_refi���`a,���`a ���`kz_test_refi���`a ���aoa=���`a ���`grefiner���aoa.���`lrefine_field���`a(���`fz_test���`a,���`a ���`fsubdiv���aoa=���`fsubdiv���`a)���`a
���`a
���bc1x%# analytical 'results' for comparison���`a
���`jz_expected���`a ���aoa=���`a ���`nexperiment_res���`a(���`htri_refi���aoa.���`ax���`a,���`a ���`htri_refi���aoa.���`ay���`a)���`a
���`a
���bc1x5# for the demo: loading the 'flat' triangles for plot���`a
���`hflat_tri���`a ���aoa=���`a ���`mTriangulation���`a(���`fx_test���`a,���`a ���`fy_test���`a)���`a
���`hflat_tri���aoa.���`hset_mask���`a(���aoa~���`dmask���`a)���`a
���`a
���`a
���bc1xN# ----------------------------------------------------------------------------���`a
���bc1o# Now the plots���`a
���bc1xN# ----------------------------------------------------------------------------���`a
���bc1x# User options for plots���`a
���`hplot_tri���`a ���aoa=���`a ���bkcdTrue���`j          ���bc1x# plot of base triangulation���`a
���`oplot_masked_tri���`a ���aoa=���`a ���bkcdTrue���`c   ���bc1x-# plot of excessively flat excluded triangles���`a
���`mplot_refi_tri���`a ���aoa=���`a ���bkceFalse���`d    ���bc1x# plot of refined triangulation���`a
���`mplot_expected���`a ���aoa=���`a ���bkceFalse���`d    ���bc1x3# plot of analytical function values for comparison���`a
���`a
���`a
���bc1x%# Graphical options for tricontouring���`a
���`flevels���`a ���aoa=���`a ���`bnp���aoa.���`farange���`a(���bmfb0.���`a,���`a ���bmfb1.���`a,���`a ���bmfe0.025���`a)���`a
���`a
���`cfig���`a,���`a ���`bax���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`a)���`a
���`bax���aoa.���`jset_aspect���`a(���bs1a'���bs1eequal���bs1a'���`a)���`a
���`bax���aoa.���`iset_title���`a(���bs2a"���bs2xFiltering a Delaunay mesh���bseb\n���bs2a"���`a
���`m             ���bs2a"���bs2x.(application to high-resolution tricontouring)���bs2a"���`a)���`a
���`a
���bc1x2# 1) plot of the refined (computed) data contours:���`a
���`bax���aoa.���`jtricontour���`a(���`htri_refi���`a,���`a ���`kz_test_refi���`a,���`a ���`flevels���aoa=���`flevels���`a,���`a ���`dcmap���aoa=���bs1a'���bs1eBlues���bs1a'���`a,���`a
���`n              ���`jlinewidths���aoa=���`a[���bmfc2.0���`a,���`a ���bmfc0.5���`a,���`a ���bmfc1.0���`a,���`a ���bmfc0.5���`a]���`a)���`a
���bc1x># 2) plot of the expected (analytical) data contours (dashed):���`a
���akbif���`a ���`mplot_expected���`a:���`a
���`d    ���`bax���aoa.���`jtricontour���`a(���`htri_refi���`a,���`a ���`jz_expected���`a,���`a ���`flevels���aoa=���`flevels���`a,���`a ���`dcmap���aoa=���bs1a'���bs1eBlues���bs1a'���`a,���`a
���`r                  ���`jlinestyles���aoa=���bs1a'���bs1b--���bs1a'���`a)���`a
���bc1x;# 3) plot of the fine mesh on which interpolation was done:���`a
���akbif���`a ���`mplot_refi_tri���`a:���`a
���`d    ���`bax���aoa.���`gtriplot���`a(���`htri_refi���`a,���`a ���`ecolor���aoa=���bs1a'���bs1d0.97���bs1a'���`a)���`a
���bc1x'# 4) plot of the initial 'coarse' mesh:���`a
���akbif���`a ���`hplot_tri���`a:���`a
���`d    ���`bax���aoa.���`gtriplot���`a(���`ctri���`a,���`a ���`ecolor���aoa=���bs1a'���bs1c0.7���bs1a'���`a)���`a
���bc1xI# 4) plot of the unvalidated triangles from naive Delaunay Triangulation:���`a
���akbif���`a ���`oplot_masked_tri���`a:���`a
���`d    ���`bax���aoa.���`gtriplot���`a(���`hflat_tri���`a,���`a ���`ecolor���aoa=���bs1a'���bs1cred���bs1a'���`a)���`a
���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
���`a
���bc1xM#############################################################################���`a
���bc1a#���`a
���bc1x# .. admonition:: References���`a
���bc1a#���`a
���bc1xN#    The use of the following functions, methods, classes and modules is shown���`a
���bc1u#    in this example:���`a
���bc1a#���`a
���bc1xI#    - `matplotlib.axes.Axes.tricontour` / `matplotlib.pyplot.tricontour`���`a
���bc1xK#    - `matplotlib.axes.Axes.tricontourf` / `matplotlib.pyplot.tricontourf`���`a
���bc1xC#    - `matplotlib.axes.Axes.triplot` / `matplotlib.pyplot.triplot`���`a
���bc1w#    - `matplotlib.tri`���`a
���bc1x%#    - `matplotlib.tri.Triangulation`���`a
���bc1x##    - `matplotlib.tri.TriAnalyzer`���`a
���bc1x)#    - `matplotlib.tri.UniformTriRefiner`���`a
`dNone�