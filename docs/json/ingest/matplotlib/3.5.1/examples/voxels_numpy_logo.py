������������bsdx�"""
===============================
3D voxel plot of the numpy logo
===============================

Demonstrates using `.Axes3D.voxels` with uneven coordinates.
"""���`a
���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���`a
���`a
���akcdef���`a ���bnfgexplode���`a(���`ddata���`a)���`a:���`a
���`d    ���`dsize���`a ���aoa=���`a ���`bnp���aoa.���`earray���`a(���`ddata���aoa.���`eshape���`a)���aoa*���bmia2���`a
���`d    ���`fdata_e���`a ���aoa=���`a ���`bnp���aoa.���`ezeros���`a(���`dsize���`a ���aoa-���`a ���bmia1���`a,���`a ���`edtype���aoa=���`ddata���aoa.���`edtype���`a)���`a
���`d    ���`fdata_e���`a[���`a:���`a:���bmia2���`a,���`a ���`a:���`a:���bmia2���`a,���`a ���`a:���`a:���bmia2���`a]���`a ���aoa=���`a ���`ddata���`a
���`d    ���akfreturn���`a ���`fdata_e���`a
���`a
���bc1x# build up the numpy logo���`a
���`hn_voxels���`a ���aoa=���`a ���`bnp���aoa.���`ezeros���`a(���`a(���bmia4���`a,���`a ���bmia3���`a,���`a ���bmia4���`a)���`a,���`a ���`edtype���aoa=���bnbdbool���`a)���`a
���`hn_voxels���`a[���bmia0���`a,���`a ���bmia0���`a,���`a ���`a:���`a]���`a ���aoa=���`a ���bkcdTrue���`a
���`hn_voxels���`a[���aoa-���bmia1���`a,���`a ���bmia0���`a,���`a ���`a:���`a]���`a ���aoa=���`a ���bkcdTrue���`a
���`hn_voxels���`a[���bmia1���`a,���`a ���bmia0���`a,���`a ���bmia2���`a]���`a ���aoa=���`a ���bkcdTrue���`a
���`hn_voxels���`a[���bmia2���`a,���`a ���bmia0���`a,���`a ���bmia1���`a]���`a ���aoa=���`a ���bkcdTrue���`a
���`jfacecolors���`a ���aoa=���`a ���`bnp���aoa.���`ewhere���`a(���`hn_voxels���`a,���`a ���bs1a'���bs1i#FFD65DC0���bs1a'���`a,���`a ���bs1a'���bs1i#7A88CCC0���bs1a'���`a)���`a
���`jedgecolors���`a ���aoa=���`a ���`bnp���aoa.���`ewhere���`a(���`hn_voxels���`a,���`a ���bs1a'���bs1g#BFAB6E���bs1a'���`a,���`a ���bs1a'���bs1g#7D84A6���bs1a'���`a)���`a
���`ffilled���`a ���aoa=���`a ���`bnp���aoa.���`dones���`a(���`hn_voxels���aoa.���`eshape���`a)���`a
���`a
���bc1x-# upscale the above voxel image, leaving gaps���`a
���`hfilled_2���`a ���aoa=���`a ���`gexplode���`a(���`ffilled���`a)���`a
���`ifcolors_2���`a ���aoa=���`a ���`gexplode���`a(���`jfacecolors���`a)���`a
���`iecolors_2���`a ���aoa=���`a ���`gexplode���`a(���`jedgecolors���`a)���`a
���`a
���bc1q# Shrink the gaps���`a
���`ax���`a,���`a ���`ay���`a,���`a ���`az���`a ���aoa=���`a ���`bnp���aoa.���`gindices���`a(���`bnp���aoa.���`earray���`a(���`hfilled_2���aoa.���`eshape���`a)���`a ���aoa+���`a ���bmia1���`a)���aoa.���`fastype���`a(���bnbefloat���`a)���`a ���aoa/���aoa/���`a ���bmia2���`a
���`ax���`a[���bmia0���`a:���`a:���bmia2���`a,���`a ���`a:���`a,���`a ���`a:���`a]���`a ���aoa+���aoa=���`a ���bmfd0.05���`a
���`ay���`a[���`a:���`a,���`a ���bmia0���`a:���`a:���bmia2���`a,���`a ���`a:���`a]���`a ���aoa+���aoa=���`a ���bmfd0.05���`a
���`az���`a[���`a:���`a,���`a ���`a:���`a,���`a ���bmia0���`a:���`a:���bmia2���`a]���`a ���aoa+���aoa=���`a ���bmfd0.05���`a
���`ax���`a[���bmia1���`a:���`a:���bmia2���`a,���`a ���`a:���`a,���`a ���`a:���`a]���`a ���aoa+���aoa=���`a ���bmfd0.95���`a
���`ay���`a[���`a:���`a,���`a ���bmia1���`a:���`a:���bmia2���`a,���`a ���`a:���`a]���`a ���aoa+���aoa=���`a ���bmfd0.95���`a
���`az���`a[���`a:���`a,���`a ���`a:���`a,���`a ���bmia1���`a:���`a:���bmia2���`a]���`a ���aoa+���aoa=���`a ���bmfd0.95���`a
���`a
���`bax���`a ���aoa=���`a ���`cplt���aoa.���`ffigure���`a(���`a)���aoa.���`kadd_subplot���`a(���`jprojection���aoa=���bs1a'���bs1b3d���bs1a'���`a)���`a
���`bax���aoa.���`fvoxels���`a(���`ax���`a,���`a ���`ay���`a,���`a ���`az���`a,���`a ���`hfilled_2���`a,���`a ���`jfacecolors���aoa=���`ifcolors_2���`a,���`a ���`jedgecolors���aoa=���`iecolors_2���`a)���`a
���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
`dNone�