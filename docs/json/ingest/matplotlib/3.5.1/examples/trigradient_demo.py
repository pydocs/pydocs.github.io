������������bsdx�"""
================
Trigradient Demo
================

Demonstrates computation of gradient with
`matplotlib.tri.CubicTriInterpolator`.
"""���`a
���bkndfrom���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnctri���`a ���bknfimport���`a ���`a(���`a
���`d    ���`mTriangulation���`a,���`a ���`qUniformTriRefiner���`a,���`a ���`tCubicTriInterpolator���`a)���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���`a
���`a
���bc1xN# ----------------------------------------------------------------------------���`a
���bc1x"# Electrical potential of a dipole���`a
���bc1xN# ----------------------------------------------------------------------------���`a
���akcdef���`a ���bnfpdipole_potential���`a(���`ax���`a,���`a ���`ay���`a)���`a:���`a
���`d    ���bsdx<"""The electric dipole potential V, at position *x*, *y*."""���`a
���`d    ���`dr_sq���`a ���aoa=���`a ���`ax���aoa*���aoa*���bmia2���`a ���aoa+���`a ���`ay���aoa*���aoa*���bmia2���`a
���`d    ���`etheta���`a ���aoa=���`a ���`bnp���aoa.���`garctan2���`a(���`ay���`a,���`a ���`ax���`a)���`a
���`d    ���`az���`a ���aoa=���`a ���`bnp���aoa.���`ccos���`a(���`etheta���`a)���aoa/���`dr_sq���`a
���`d    ���akfreturn���`a ���`a(���`bnp���aoa.���`cmax���`a(���`az���`a)���`a ���aoa-���`a ���`az���`a)���`a ���aoa/���`a ���`a(���`bnp���aoa.���`cmax���`a(���`az���`a)���`a ���aoa-���`a ���`bnp���aoa.���`cmin���`a(���`az���`a)���`a)���`a
���`a
���`a
���bc1xN# ----------------------------------------------------------------------------���`a
���bc1x# Creating a Triangulation���`a
���bc1xN# ----------------------------------------------------------------------------���`a
���bc1x5# First create the x and y coordinates of the points.���`a
���`hn_angles���`a ���aoa=���`a ���bmib30���`a
���`gn_radii���`a ���aoa=���`a ���bmib10���`a
���`jmin_radius���`a ���aoa=���`a ���bmfc0.2���`a
���`eradii���`a ���aoa=���`a ���`bnp���aoa.���`hlinspace���`a(���`jmin_radius���`a,���`a ���bmfd0.95���`a,���`a ���`gn_radii���`a)���`a
���`a
���`fangles���`a ���aoa=���`a ���`bnp���aoa.���`hlinspace���`a(���bmia0���`a,���`a ���bmia2���`a ���aoa*���`a ���`bnp���aoa.���`bpi���`a,���`a ���`hn_angles���`a,���`a ���`hendpoint���aoa=���bkceFalse���`a)���`a
���`fangles���`a ���aoa=���`a ���`bnp���aoa.���`frepeat���`a(���`fangles���`a[���aoa.���aoa.���aoa.���`a,���`a ���`bnp���aoa.���`gnewaxis���`a]���`a,���`a ���`gn_radii���`a,���`a ���`daxis���aoa=���bmia1���`a)���`a
���`fangles���`a[���`a:���`a,���`a ���bmia1���`a:���`a:���bmia2���`a]���`a ���aoa+���aoa=���`a ���`bnp���aoa.���`bpi���`a ���aoa/���`a ���`hn_angles���`a
���`a
���`ax���`a ���aoa=���`a ���`a(���`eradii���aoa*���`bnp���aoa.���`ccos���`a(���`fangles���`a)���`a)���aoa.���`gflatten���`a(���`a)���`a
���`ay���`a ���aoa=���`a ���`a(���`eradii���aoa*���`bnp���aoa.���`csin���`a(���`fangles���`a)���`a)���aoa.���`gflatten���`a(���`a)���`a
���`aV���`a ���aoa=���`a ���`pdipole_potential���`a(���`ax���`a,���`a ���`ay���`a)���`a
���`a
���bc1xL# Create the Triangulation; no triangles specified so Delaunay triangulation���`a
���bc1j# created.���`a
���`ftriang���`a ���aoa=���`a ���`mTriangulation���`a(���`ax���`a,���`a ���`ay���`a)���`a
���`a
���bc1x# Mask off unwanted triangles.���`a
���`ftriang���aoa.���`hset_mask���`a(���`bnp���aoa.���`ehypot���`a(���`ax���`a[���`ftriang���aoa.���`itriangles���`a]���aoa.���`dmean���`a(���`daxis���aoa=���bmia1���`a)���`a,���`a
���`x                         ���`ay���`a[���`ftriang���aoa.���`itriangles���`a]���aoa.���`dmean���`a(���`daxis���aoa=���bmia1���`a)���`a)���`a
���`p                ���aoa<���`a ���`jmin_radius���`a)���`a
���`a
���bc1xN# ----------------------------------------------------------------------------���`a
���bc1x7# Refine data - interpolates the electrical potential V���`a
���bc1xN# ----------------------------------------------------------------------------���`a
���`grefiner���`a ���aoa=���`a ���`qUniformTriRefiner���`a(���`ftriang���`a)���`a
���`htri_refi���`a,���`a ���`kz_test_refi���`a ���aoa=���`a ���`grefiner���aoa.���`lrefine_field���`a(���`aV���`a,���`a ���`fsubdiv���aoa=���bmia3���`a)���`a
���`a
���bc1xN# ----------------------------------------------------------------------------���`a
���bc1xL# Computes the electrical field (Ex, Ey) as gradient of electrical potential���`a
���bc1xN# ----------------------------------------------------------------------------���`a
���`ctci���`a ���aoa=���`a ���`tCubicTriInterpolator���`a(���`ftriang���`a,���`a ���aoa-���`aV���`a)���`a
���bc1xG# Gradient requested here at the mesh nodes but could be anywhere else:���`a
���`a(���`bEx���`a,���`a ���`bEy���`a)���`a ���aoa=���`a ���`ctci���aoa.���`hgradient���`a(���`ftriang���aoa.���`ax���`a,���`a ���`ftriang���aoa.���`ay���`a)���`a
���`fE_norm���`a ���aoa=���`a ���`bnp���aoa.���`dsqrt���`a(���`bEx���aoa*���aoa*���bmia2���`a ���aoa+���`a ���`bEy���aoa*���aoa*���bmia2���`a)���`a
���`a
���bc1xN# ----------------------------------------------------------------------------���`a
���bc1xI# Plot the triangulation, the potential iso-contours and the vector field���`a
���bc1xN# ----------------------------------------------------------------------------���`a
���`cfig���`a,���`a ���`bax���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`a)���`a
���`bax���aoa.���`jset_aspect���`a(���bs1a'���bs1eequal���bs1a'���`a)���`a
���bc1xE# Enforce the margins, and enlarge them to give room for the vectors.���`a
���`bax���aoa.���`puse_sticky_edges���`a ���aoa=���`a ���bkceFalse���`a
���`bax���aoa.���`gmargins���`a(���bmfd0.07���`a)���`a
���`a
���`bax���aoa.���`gtriplot���`a(���`ftriang���`a,���`a ���`ecolor���aoa=���bs1a'���bs1c0.8���bs1a'���`a)���`a
���`a
���`flevels���`a ���aoa=���`a ���`bnp���aoa.���`farange���`a(���bmfb0.���`a,���`a ���bmfb1.���`a,���`a ���bmfd0.01���`a)���`a
���`bax���aoa.���`jtricontour���`a(���`htri_refi���`a,���`a ���`kz_test_refi���`a,���`a ���`flevels���aoa=���`flevels���`a,���`a ���`dcmap���aoa=���bs1a'���bs1chot���bs1a'���`a,���`a
���`n              ���`jlinewidths���aoa=���`a[���bmfc2.0���`a,���`a ���bmfc1.0���`a,���`a ���bmfc1.0���`a,���`a ���bmfc1.0���`a]���`a)���`a
���bc1x0# Plots direction of the electrical vector field���`a
���`bax���aoa.���`fquiver���`a(���`ftriang���aoa.���`ax���`a,���`a ���`ftriang���aoa.���`ay���`a,���`a ���`bEx���aoa/���`fE_norm���`a,���`a ���`bEy���aoa/���`fE_norm���`a,���`a
���`j          ���`eunits���aoa=���bs1a'���bs1bxy���bs1a'���`a,���`a ���`escale���aoa=���bmfc10.���`a,���`a ���`fzorder���aoa=���bmia3���`a,���`a ���`ecolor���aoa=���bs1a'���bs1dblue���bs1a'���`a,���`a
���`j          ���`ewidth���aoa=���bmfe0.007���`a,���`a ���`iheadwidth���aoa=���bmfb3.���`a,���`a ���`jheadlength���aoa=���bmfb4.���`a)���`a
���`a
���`bax���aoa.���`iset_title���`a(���bs1a'���bs1x#Gradient plot: an electrical dipole���bs1a'���`a)���`a
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
���bc1xC#    - `matplotlib.axes.Axes.triplot` / `matplotlib.pyplot.triplot`���`a
���bc1w#    - `matplotlib.tri`���`a
���bc1x%#    - `matplotlib.tri.Triangulation`���`a
���bc1x,#    - `matplotlib.tri.CubicTriInterpolator`���`a
���bc1x5#    - `matplotlib.tri.CubicTriInterpolator.gradient`���`a
���bc1x)#    - `matplotlib.tri.UniformTriRefiner`���`a
���bc1xA#    - `matplotlib.axes.Axes.quiver` / `matplotlib.pyplot.quiver`���`a
`dNone�