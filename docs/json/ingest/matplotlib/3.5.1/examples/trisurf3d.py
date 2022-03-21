������������bsdxw"""
======================
Triangular 3D surfaces
======================

Plot a 3D surface with a triangular mesh.
"""���`a
���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���`a
���`a
���`gn_radii���`a ���aoa=���`a ���bmia8���`a
���`hn_angles���`a ���aoa=���`a ���bmib36���`a
���`a
���bc1xM# Make radii and angles spaces (radius r=0 omitted to eliminate duplication).���`a
���`eradii���`a ���aoa=���`a ���`bnp���aoa.���`hlinspace���`a(���bmfe0.125���`a,���`a ���bmfc1.0���`a,���`a ���`gn_radii���`a)���`a
���`fangles���`a ���aoa=���`a ���`bnp���aoa.���`hlinspace���`a(���bmia0���`a,���`a ���bmia2���aoa*���`bnp���aoa.���`bpi���`a,���`a ���`hn_angles���`a,���`a ���`hendpoint���aoa=���bkceFalse���`a)���`a[���aoa.���aoa.���aoa.���`a,���`a ���`bnp���aoa.���`gnewaxis���`a]���`a
���`a
���bc1xB# Convert polar (radii, angles) coords to cartesian (x, y) coords.���`a
���bc1xH# (0, 0) is manually added at this stage,  so there will be no duplicate���`a
���bc1x# points in the (x, y) plane.���`a
���`ax���`a ���aoa=���`a ���`bnp���aoa.���`fappend���`a(���bmia0���`a,���`a ���`a(���`eradii���aoa*���`bnp���aoa.���`ccos���`a(���`fangles���`a)���`a)���aoa.���`gflatten���`a(���`a)���`a)���`a
���`ay���`a ���aoa=���`a ���`bnp���aoa.���`fappend���`a(���bmia0���`a,���`a ���`a(���`eradii���aoa*���`bnp���aoa.���`csin���`a(���`fangles���`a)���`a)���aoa.���`gflatten���`a(���`a)���`a)���`a
���`a
���bc1x(# Compute z to make the pringle surface.���`a
���`az���`a ���aoa=���`a ���`bnp���aoa.���`csin���`a(���aoa-���`ax���aoa*���`ay���`a)���`a
���`a
���`bax���`a ���aoa=���`a ���`cplt���aoa.���`ffigure���`a(���`a)���aoa.���`kadd_subplot���`a(���`jprojection���aoa=���bs1a'���bs1b3d���bs1a'���`a)���`a
���`a
���`bax���aoa.���`lplot_trisurf���`a(���`ax���`a,���`a ���`ay���`a,���`a ���`az���`a,���`a ���`ilinewidth���aoa=���bmfc0.2���`a,���`a ���`kantialiased���aoa=���bkcdTrue���`a)���`a
���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
`dNone�