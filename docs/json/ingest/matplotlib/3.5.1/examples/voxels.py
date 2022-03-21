�����������bsdx�"""
==========================
3D voxel / volumetric plot
==========================

Demonstrates plotting 3D volumetric objects with `.Axes3D.voxels`.
"""���`a
���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���`a
���`a
���bc1x# prepare some coordinates���`a
���`ax���`a,���`a ���`ay���`a,���`a ���`az���`a ���aoa=���`a ���`bnp���aoa.���`gindices���`a(���`a(���bmia8���`a,���`a ���bmia8���`a,���`a ���bmia8���`a)���`a)���`a
���`a
���bc1xK# draw cuboids in the top left and bottom right corners, and a link between���`a
���bc1f# them���`a
���`ecube1���`a ���aoa=���`a ���`a(���`ax���`a ���aoa<���`a ���bmia3���`a)���`a ���aoa&���`a ���`a(���`ay���`a ���aoa<���`a ���bmia3���`a)���`a ���aoa&���`a ���`a(���`az���`a ���aoa<���`a ���bmia3���`a)���`a
���`ecube2���`a ���aoa=���`a ���`a(���`ax���`a ���aoa>���aoa=���`a ���bmia5���`a)���`a ���aoa&���`a ���`a(���`ay���`a ���aoa>���aoa=���`a ���bmia5���`a)���`a ���aoa&���`a ���`a(���`az���`a ���aoa>���aoa=���`a ���bmia5���`a)���`a
���`dlink���`a ���aoa=���`a ���bnbcabs���`a(���`ax���`a ���aoa-���`a ���`ay���`a)���`a ���aoa+���`a ���bnbcabs���`a(���`ay���`a ���aoa-���`a ���`az���`a)���`a ���aoa+���`a ���bnbcabs���`a(���`az���`a ���aoa-���`a ���`ax���`a)���`a ���aoa<���aoa=���`a ���bmia2���`a
���`a
���bc1x1# combine the objects into a single boolean array���`a
���`jvoxelarray���`a ���aoa=���`a ���`ecube1���`a ���aoa|���`a ���`ecube2���`a ���aoa|���`a ���`dlink���`a
���`a
���bc1x# set the colors of each object���`a
���`fcolors���`a ���aoa=���`a ���`bnp���aoa.���`eempty���`a(���`jvoxelarray���aoa.���`eshape���`a,���`a ���`edtype���aoa=���bnbfobject���`a)���`a
���`fcolors���`a[���`dlink���`a]���`a ���aoa=���`a ���bs1a'���bs1cred���bs1a'���`a
���`fcolors���`a[���`ecube1���`a]���`a ���aoa=���`a ���bs1a'���bs1dblue���bs1a'���`a
���`fcolors���`a[���`ecube2���`a]���`a ���aoa=���`a ���bs1a'���bs1egreen���bs1a'���`a
���`a
���bc1u# and plot everything���`a
���`bax���`a ���aoa=���`a ���`cplt���aoa.���`ffigure���`a(���`a)���aoa.���`kadd_subplot���`a(���`jprojection���aoa=���bs1a'���bs1b3d���bs1a'���`a)���`a
���`bax���aoa.���`fvoxels���`a(���`jvoxelarray���`a,���`a ���`jfacecolors���aoa=���`fcolors���`a,���`a ���`iedgecolor���aoa=���bs1a'���bs1ak���bs1a'���`a)���`a
���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
`dNone�