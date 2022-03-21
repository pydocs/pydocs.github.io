��������O���bsdy("""
=================================
Triangular 3D filled contour plot
=================================

Filled contour plots of unstructured triangular grids.

The data used is the same as in the second plot of trisurf3d_demo2.
tricontour3d_demo shows the unfilled version of this example.
"""���`a
���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnctri���`a ���akbas���`a ���bnnctri���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���`a
���bc1x5# First create the x, y, z coordinates of the points.���`a
���`hn_angles���`a ���aoa=���`a ���bmib48���`a
���`gn_radii���`a ���aoa=���`a ���bmia8���`a
���`jmin_radius���`a ���aoa=���`a ���bmfd0.25���`a
���`a
���bc1x;# Create the mesh in polar coordinates and compute x, y, z.���`a
���`eradii���`a ���aoa=���`a ���`bnp���aoa.���`hlinspace���`a(���`jmin_radius���`a,���`a ���bmfd0.95���`a,���`a ���`gn_radii���`a)���`a
���`fangles���`a ���aoa=���`a ���`bnp���aoa.���`hlinspace���`a(���bmia0���`a,���`a ���bmia2���aoa*���`bnp���aoa.���`bpi���`a,���`a ���`hn_angles���`a,���`a ���`hendpoint���aoa=���bkceFalse���`a)���`a
���`fangles���`a ���aoa=���`a ���`bnp���aoa.���`frepeat���`a(���`fangles���`a[���aoa.���aoa.���aoa.���`a,���`a ���`bnp���aoa.���`gnewaxis���`a]���`a,���`a ���`gn_radii���`a,���`a ���`daxis���aoa=���bmia1���`a)���`a
���`fangles���`a[���`a:���`a,���`a ���bmia1���`a:���`a:���bmia2���`a]���`a ���aoa+���aoa=���`a ���`bnp���aoa.���`bpi���aoa/���`hn_angles���`a
���`a
���`ax���`a ���aoa=���`a ���`a(���`eradii���aoa*���`bnp���aoa.���`ccos���`a(���`fangles���`a)���`a)���aoa.���`gflatten���`a(���`a)���`a
���`ay���`a ���aoa=���`a ���`a(���`eradii���aoa*���`bnp���aoa.���`csin���`a(���`fangles���`a)���`a)���aoa.���`gflatten���`a(���`a)���`a
���`az���`a ���aoa=���`a ���`a(���`bnp���aoa.���`ccos���`a(���`eradii���`a)���aoa*���`bnp���aoa.���`ccos���`a(���bmia3���aoa*���`fangles���`a)���`a)���aoa.���`gflatten���`a(���`a)���`a
���`a
���bc1x # Create a custom triangulation.���`a
���`ftriang���`a ���aoa=���`a ���`ctri���aoa.���`mTriangulation���`a(���`ax���`a,���`a ���`ay���`a)���`a
���`a
���bc1x# Mask off unwanted triangles.���`a
���`ftriang���aoa.���`hset_mask���`a(���`bnp���aoa.���`ehypot���`a(���`ax���`a[���`ftriang���aoa.���`itriangles���`a]���aoa.���`dmean���`a(���`daxis���aoa=���bmia1���`a)���`a,���`a
���`x                         ���`ay���`a[���`ftriang���aoa.���`itriangles���`a]���aoa.���`dmean���`a(���`daxis���aoa=���bmia1���`a)���`a)���`a
���`p                ���aoa<���`a ���`jmin_radius���`a)���`a
���`a
���`bax���`a ���aoa=���`a ���`cplt���aoa.���`ffigure���`a(���`a)���aoa.���`kadd_subplot���`a(���`jprojection���aoa=���bs1a'���bs1b3d���bs1a'���`a)���`a
���`bax���aoa.���`ktricontourf���`a(���`ftriang���`a,���`a ���`az���`a,���`a ���`dcmap���aoa=���`cplt���aoa.���`bcm���aoa.���`fCMRmap���`a)���`a
���`a
���bc1xA# Customize the view angle so it's easier to understand the plot.���`a
���`bax���aoa.���`iview_init���`a(���`delev���aoa=���bmfc45.���`a)���`a
���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
`dNone�