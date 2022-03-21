������������bsdyC"""
===========================
More triangular 3D surfaces
===========================

Two additional examples of plotting surfaces with triangular mesh.

The first demonstrates use of plot_trisurf's triangles argument, and the
second sets a Triangulation object's mask and passes the object directly
to plot_trisurf.
"""���`a
���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnctri���`a ���akbas���`a ���bnndmtri���`a
���`a
���`a
���`cfig���`a ���aoa=���`a ���`cplt���aoa.���`ffigure���`a(���`gfigsize���aoa=���`cplt���aoa.���`ifigaspect���`a(���bmfc0.5���`a)���`a)���`a
���`a
���bc1l# ==========���`a
���bc1l# First plot���`a
���bc1l# ==========���`a
���`a
���bc1x@# Make a mesh in the space of parameterisation variables u and v���`a
���`au���`a ���aoa=���`a ���`bnp���aoa.���`hlinspace���`a(���bmia0���`a,���`a ���bmfc2.0���`a ���aoa*���`a ���`bnp���aoa.���`bpi���`a,���`a ���`hendpoint���aoa=���bkcdTrue���`a,���`a ���`cnum���aoa=���bmib50���`a)���`a
���`av���`a ���aoa=���`a ���`bnp���aoa.���`hlinspace���`a(���aoa-���bmfc0.5���`a,���`a ���bmfc0.5���`a,���`a ���`hendpoint���aoa=���bkcdTrue���`a,���`a ���`cnum���aoa=���bmib10���`a)���`a
���`au���`a,���`a ���`av���`a ���aoa=���`a ���`bnp���aoa.���`hmeshgrid���`a(���`au���`a,���`a ���`av���`a)���`a
���`au���`a,���`a ���`av���`a ���aoa=���`a ���`au���aoa.���`gflatten���`a(���`a)���`a,���`a ���`av���aoa.���`gflatten���`a(���`a)���`a
���`a
���bc1xI# This is the Mobius mapping, taking a u, v pair and returning an x, y, z���`a
���bc1h# triple���`a
���`ax���`a ���aoa=���`a ���`a(���bmia1���`a ���aoa+���`a ���bmfc0.5���`a ���aoa*���`a ���`av���`a ���aoa*���`a ���`bnp���aoa.���`ccos���`a(���`au���`a ���aoa/���`a ���bmfc2.0���`a)���`a)���`a ���aoa*���`a ���`bnp���aoa.���`ccos���`a(���`au���`a)���`a
���`ay���`a ���aoa=���`a ���`a(���bmia1���`a ���aoa+���`a ���bmfc0.5���`a ���aoa*���`a ���`av���`a ���aoa*���`a ���`bnp���aoa.���`ccos���`a(���`au���`a ���aoa/���`a ���bmfc2.0���`a)���`a)���`a ���aoa*���`a ���`bnp���aoa.���`csin���`a(���`au���`a)���`a
���`az���`a ���aoa=���`a ���bmfc0.5���`a ���aoa*���`a ���`av���`a ���aoa*���`a ���`bnp���aoa.���`csin���`a(���`au���`a ���aoa/���`a ���bmfc2.0���`a)���`a
���`a
���bc1x8# Triangulate parameter space to determine the triangles���`a
���`ctri���`a ���aoa=���`a ���`dmtri���aoa.���`mTriangulation���`a(���`au���`a,���`a ���`av���`a)���`a
���`a
���bc1xM# Plot the surface.  The triangles in parameter space determine which x, y, z���`a
���bc1x"# points are connected by an edge.���`a
���`bax���`a ���aoa=���`a ���`cfig���aoa.���`kadd_subplot���`a(���bmia1���`a,���`a ���bmia2���`a,���`a ���bmia1���`a,���`a ���`jprojection���aoa=���bs1a'���bs1b3d���bs1a'���`a)���`a
���`bax���aoa.���`lplot_trisurf���`a(���`ax���`a,���`a ���`ay���`a,���`a ���`az���`a,���`a ���`itriangles���aoa=���`ctri���aoa.���`itriangles���`a,���`a ���`dcmap���aoa=���`cplt���aoa.���`bcm���aoa.���`hSpectral���`a)���`a
���`bax���aoa.���`hset_zlim���`a(���aoa-���bmia1���`a,���`a ���bmia1���`a)���`a
���`a
���`a
���bc1m# ===========���`a
���bc1m# Second plot���`a
���bc1m# ===========���`a
���`a
���bc1x)# Make parameter spaces radii and angles.���`a
���`hn_angles���`a ���aoa=���`a ���bmib36���`a
���`gn_radii���`a ���aoa=���`a ���bmia8���`a
���`jmin_radius���`a ���aoa=���`a ���bmfd0.25���`a
���`eradii���`a ���aoa=���`a ���`bnp���aoa.���`hlinspace���`a(���`jmin_radius���`a,���`a ���bmfd0.95���`a,���`a ���`gn_radii���`a)���`a
���`a
���`fangles���`a ���aoa=���`a ���`bnp���aoa.���`hlinspace���`a(���bmia0���`a,���`a ���bmia2���aoa*���`bnp���aoa.���`bpi���`a,���`a ���`hn_angles���`a,���`a ���`hendpoint���aoa=���bkceFalse���`a)���`a
���`fangles���`a ���aoa=���`a ���`bnp���aoa.���`frepeat���`a(���`fangles���`a[���aoa.���aoa.���aoa.���`a,���`a ���`bnp���aoa.���`gnewaxis���`a]���`a,���`a ���`gn_radii���`a,���`a ���`daxis���aoa=���bmia1���`a)���`a
���`fangles���`a[���`a:���`a,���`a ���bmia1���`a:���`a:���bmia2���`a]���`a ���aoa+���aoa=���`a ���`bnp���aoa.���`bpi���aoa/���`hn_angles���`a
���`a
���bc1x,# Map radius, angle pairs to x, y, z points.���`a
���`ax���`a ���aoa=���`a ���`a(���`eradii���aoa*���`bnp���aoa.���`ccos���`a(���`fangles���`a)���`a)���aoa.���`gflatten���`a(���`a)���`a
���`ay���`a ���aoa=���`a ���`a(���`eradii���aoa*���`bnp���aoa.���`csin���`a(���`fangles���`a)���`a)���aoa.���`gflatten���`a(���`a)���`a
���`az���`a ���aoa=���`a ���`a(���`bnp���aoa.���`ccos���`a(���`eradii���`a)���aoa*���`bnp���aoa.���`ccos���`a(���bmia3���aoa*���`fangles���`a)���`a)���aoa.���`gflatten���`a(���`a)���`a
���`a
���bc1xK# Create the Triangulation; no triangles so Delaunay triangulation created.���`a
���`ftriang���`a ���aoa=���`a ���`dmtri���aoa.���`mTriangulation���`a(���`ax���`a,���`a ���`ay���`a)���`a
���`a
���bc1x# Mask off unwanted triangles.���`a
���`dxmid���`a ���aoa=���`a ���`ax���`a[���`ftriang���aoa.���`itriangles���`a]���aoa.���`dmean���`a(���`daxis���aoa=���bmia1���`a)���`a
���`dymid���`a ���aoa=���`a ���`ay���`a[���`ftriang���aoa.���`itriangles���`a]���aoa.���`dmean���`a(���`daxis���aoa=���bmia1���`a)���`a
���`dmask���`a ���aoa=���`a ���`dxmid���aoa*���aoa*���bmia2���`a ���aoa+���`a ���`dymid���aoa*���aoa*���bmia2���`a ���aoa<���`a ���`jmin_radius���aoa*���aoa*���bmia2���`a
���`ftriang���aoa.���`hset_mask���`a(���`dmask���`a)���`a
���`a
���bc1s# Plot the surface.���`a
���`bax���`a ���aoa=���`a ���`cfig���aoa.���`kadd_subplot���`a(���bmia1���`a,���`a ���bmia2���`a,���`a ���bmia2���`a,���`a ���`jprojection���aoa=���bs1a'���bs1b3d���bs1a'���`a)���`a
���`bax���aoa.���`lplot_trisurf���`a(���`ftriang���`a,���`a ���`az���`a,���`a ���`dcmap���aoa=���`cplt���aoa.���`bcm���aoa.���`fCMRmap���`a)���`a
���`a
���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
`dNone�