�����������bsdx�"""
======================
Tricontour Smooth User
======================

Demonstrates high-resolution tricontouring on user-defined triangular grids
with `matplotlib.tri.UniformTriRefiner`.
"""���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnctri���`a ���akbas���`a ���bnnctri���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���`a
���`a
���bc1xN# ----------------------------------------------------------------------------���`a
���bc1x# Analytical test function���`a
���bc1xN# ----------------------------------------------------------------------------���`a
���akcdef���`a ���bnfjfunction_z���`a(���`ax���`a,���`a ���`ay���`a)���`a:���`a
���`d    ���`br1���`a ���aoa=���`a ���`bnp���aoa.���`dsqrt���`a(���`a(���bmfc0.5���`a ���aoa-���`a ���`ax���`a)���aoa*���aoa*���bmia2���`a ���aoa+���`a ���`a(���bmfc0.5���`a ���aoa-���`a ���`ay���`a)���aoa*���aoa*���bmia2���`a)���`a
���`d    ���`ftheta1���`a ���aoa=���`a ���`bnp���aoa.���`garctan2���`a(���bmfc0.5���`a ���aoa-���`a ���`ax���`a,���`a ���bmfc0.5���`a ���aoa-���`a ���`ay���`a)���`a
���`d    ���`br2���`a ���aoa=���`a ���`bnp���aoa.���`dsqrt���`a(���`a(���aoa-���`ax���`a ���aoa-���`a ���bmfc0.2���`a)���aoa*���aoa*���bmia2���`a ���aoa+���`a ���`a(���aoa-���`ay���`a ���aoa-���`a ���bmfc0.2���`a)���aoa*���aoa*���bmia2���`a)���`a
���`d    ���`ftheta2���`a ���aoa=���`a ���`bnp���aoa.���`garctan2���`a(���aoa-���`ax���`a ���aoa-���`a ���bmfc0.2���`a,���`a ���aoa-���`ay���`a ���aoa-���`a ���bmfc0.2���`a)���`a
���`d    ���`az���`a ���aoa=���`a ���aoa-���`a(���bmia2���`a ���aoa*���`a ���`a(���`bnp���aoa.���`cexp���`a(���`a(���`br1���`a ���aoa/���`a ���bmib10���`a)���aoa*���aoa*���bmia2���`a)���`a ���aoa-���`a ���bmia1���`a)���`a ���aoa*���`a ���bmfc30.���`a ���aoa*���`a ���`bnp���aoa.���`ccos���`a(���bmfb7.���`a ���aoa*���`a ���`ftheta1���`a)���`a ���aoa+���`a
���`j          ���`a(���`bnp���aoa.���`cexp���`a(���`a(���`br2���`a ���aoa/���`a ���bmib10���`a)���aoa*���aoa*���bmia2���`a)���`a ���aoa-���`a ���bmia1���`a)���`a ���aoa*���`a ���bmfc30.���`a ���aoa*���`a ���`bnp���aoa.���`ccos���`a(���bmfc11.���`a ���aoa*���`a ���`ftheta2���`a)���`a ���aoa+���`a
���`j          ���bmfc0.7���`a ���aoa*���`a ���`a(���`ax���aoa*���aoa*���bmia2���`a ���aoa+���`a ���`ay���aoa*���aoa*���bmia2���`a)���`a)���`a
���`d    ���akfreturn���`a ���`a(���`bnp���aoa.���`cmax���`a(���`az���`a)���`a ���aoa-���`a ���`az���`a)���`a ���aoa/���`a ���`a(���`bnp���aoa.���`cmax���`a(���`az���`a)���`a ���aoa-���`a ���`bnp���aoa.���`cmin���`a(���`az���`a)���`a)���`a
���`a
���bc1xN# ----------------------------------------------------------------------------���`a
���bc1x# Creating a Triangulation���`a
���bc1xN# ----------------------------------------------------------------------------���`a
���bc1x5# First create the x and y coordinates of the points.���`a
���`hn_angles���`a ���aoa=���`a ���bmib20���`a
���`gn_radii���`a ���aoa=���`a ���bmib10���`a
���`jmin_radius���`a ���aoa=���`a ���bmfd0.15���`a
���`eradii���`a ���aoa=���`a ���`bnp���aoa.���`hlinspace���`a(���`jmin_radius���`a,���`a ���bmfd0.95���`a,���`a ���`gn_radii���`a)���`a
���`a
���`fangles���`a ���aoa=���`a ���`bnp���aoa.���`hlinspace���`a(���bmia0���`a,���`a ���bmia2���`a ���aoa*���`a ���`bnp���aoa.���`bpi���`a,���`a ���`hn_angles���`a,���`a ���`hendpoint���aoa=���bkceFalse���`a)���`a
���`fangles���`a ���aoa=���`a ���`bnp���aoa.���`frepeat���`a(���`fangles���`a[���aoa.���aoa.���aoa.���`a,���`a ���`bnp���aoa.���`gnewaxis���`a]���`a,���`a ���`gn_radii���`a,���`a ���`daxis���aoa=���bmia1���`a)���`a
���`fangles���`a[���`a:���`a,���`a ���bmia1���`a:���`a:���bmia2���`a]���`a ���aoa+���aoa=���`a ���`bnp���aoa.���`bpi���`a ���aoa/���`a ���`hn_angles���`a
���`a
���`ax���`a ���aoa=���`a ���`a(���`eradii���`a ���aoa*���`a ���`bnp���aoa.���`ccos���`a(���`fangles���`a)���`a)���aoa.���`gflatten���`a(���`a)���`a
���`ay���`a ���aoa=���`a ���`a(���`eradii���`a ���aoa*���`a ���`bnp���aoa.���`csin���`a(���`fangles���`a)���`a)���aoa.���`gflatten���`a(���`a)���`a
���`az���`a ���aoa=���`a ���`jfunction_z���`a(���`ax���`a,���`a ���`ay���`a)���`a
���`a
���bc1x# Now create the Triangulation.���`a
���bc1xK# (Creating a Triangulation without specifying the triangles results in the���`a
���bc1x(# Delaunay triangulation of the points.)���`a
���`ftriang���`a ���aoa=���`a ���`ctri���aoa.���`mTriangulation���`a(���`ax���`a,���`a ���`ay���`a)���`a
���`a
���bc1x# Mask off unwanted triangles.���`a
���`ftriang���aoa.���`hset_mask���`a(���`bnp���aoa.���`ehypot���`a(���`ax���`a[���`ftriang���aoa.���`itriangles���`a]���aoa.���`dmean���`a(���`daxis���aoa=���bmia1���`a)���`a,���`a
���`x                         ���`ay���`a[���`ftriang���aoa.���`itriangles���`a]���aoa.���`dmean���`a(���`daxis���aoa=���bmia1���`a)���`a)���`a
���`p                ���aoa<���`a ���`jmin_radius���`a)���`a
���`a
���bc1xN# ----------------------------------------------------------------------------���`a
���bc1m# Refine data���`a
���bc1xN# ----------------------------------------------------------------------------���`a
���`grefiner���`a ���aoa=���`a ���`ctri���aoa.���`qUniformTriRefiner���`a(���`ftriang���`a)���`a
���`htri_refi���`a,���`a ���`kz_test_refi���`a ���aoa=���`a ���`grefiner���aoa.���`lrefine_field���`a(���`az���`a,���`a ���`fsubdiv���aoa=���bmia3���`a)���`a
���`a
���bc1xN# ----------------------------------------------------------------------------���`a
���bc1x6# Plot the triangulation and the high-res iso-contours���`a
���bc1xN# ----------------------------------------------------------------------------���`a
���`cfig���`a,���`a ���`bax���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`a)���`a
���`bax���aoa.���`jset_aspect���`a(���bs1a'���bs1eequal���bs1a'���`a)���`a
���`bax���aoa.���`gtriplot���`a(���`ftriang���`a,���`a ���`blw���aoa=���bmfc0.5���`a,���`a ���`ecolor���aoa=���bs1a'���bs1ewhite���bs1a'���`a)���`a
���`a
���`flevels���`a ���aoa=���`a ���`bnp���aoa.���`farange���`a(���bmfb0.���`a,���`a ���bmfb1.���`a,���`a ���bmfe0.025���`a)���`a
���`bax���aoa.���`ktricontourf���`a(���`htri_refi���`a,���`a ���`kz_test_refi���`a,���`a ���`flevels���aoa=���`flevels���`a,���`a ���`dcmap���aoa=���bs1a'���bs1gterrain���bs1a'���`a)���`a
���`bax���aoa.���`jtricontour���`a(���`htri_refi���`a,���`a ���`kz_test_refi���`a,���`a ���`flevels���aoa=���`flevels���`a,���`a
���`n              ���`fcolors���aoa=���`a[���bs1a'���bs1d0.25���bs1a'���`a,���`a ���bs1a'���bs1c0.5���bs1a'���`a,���`a ���bs1a'���bs1c0.5���bs1a'���`a,���`a ���bs1a'���bs1c0.5���bs1a'���`a,���`a ���bs1a'���bs1c0.5���bs1a'���`a]���`a,���`a
���`n              ���`jlinewidths���aoa=���`a[���bmfc1.0���`a,���`a ���bmfc0.5���`a,���`a ���bmfc0.5���`a,���`a ���bmfc0.5���`a,���`a ���bmfc0.5���`a]���`a)���`a
���`a
���`bax���aoa.���`iset_title���`a(���bs2a"���bs2xHigh-resolution tricontouring���bs2a"���`a)���`a
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
���bc1w#    - `matplotlib.tri`���`a
���bc1x%#    - `matplotlib.tri.Triangulation`���`a
���bc1x)#    - `matplotlib.tri.UniformTriRefiner`���`a
`dNone�