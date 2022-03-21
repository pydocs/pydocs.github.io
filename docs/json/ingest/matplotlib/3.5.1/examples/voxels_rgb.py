������������bsdx�"""
==========================================
3D voxel / volumetric plot with rgb colors
==========================================

Demonstrates using `.Axes3D.voxels` to visualize parts of a color space.
"""���`a
���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���`a
���`a
���akcdef���`a ���bnfimidpoints���`a(���`ax���`a)���`a:���`a
���`d    ���`bsl���`a ���aoa=���`a ���`a(���`a)���`a
���`d    ���akcfor���`a ���`ai���`a ���bowbin���`a ���bnberange���`a(���`ax���aoa.���`dndim���`a)���`a:���`a
���`h        ���`ax���`a ���aoa=���`a ���`a(���`ax���`a[���`bsl���`a ���aoa+���`a ���`bnp���aoa.���`iindex_exp���`a[���`a:���aoa-���bmia1���`a]���`a]���`a ���aoa+���`a ���`ax���`a[���`bsl���`a ���aoa+���`a ���`bnp���aoa.���`iindex_exp���`a[���bmia1���`a:���`a]���`a]���`a)���`a ���aoa/���`a ���bmfc2.0���`a
���`h        ���`bsl���`a ���aoa+���aoa=���`a ���`bnp���aoa.���`iindex_exp���`a[���`a:���`a]���`a
���`d    ���akfreturn���`a ���`ax���`a
���`a
���bc1x9# prepare some coordinates, and attach rgb values to each���`a
���`ar���`a,���`a ���`ag���`a,���`a ���`ab���`a ���aoa=���`a ���`bnp���aoa.���`gindices���`a(���`a(���bmib17���`a,���`a ���bmib17���`a,���`a ���bmib17���`a)���`a)���`a ���aoa/���`a ���bmfd16.0���`a
���`brc���`a ���aoa=���`a ���`imidpoints���`a(���`ar���`a)���`a
���`bgc���`a ���aoa=���`a ���`imidpoints���`a(���`ag���`a)���`a
���`bbc���`a ���aoa=���`a ���`imidpoints���`a(���`ab���`a)���`a
���`a
���bc1x'# define a sphere about [0.5, 0.5, 0.5]���`a
���`fsphere���`a ���aoa=���`a ���`a(���`brc���`a ���aoa-���`a ���bmfc0.5���`a)���aoa*���aoa*���bmia2���`a ���aoa+���`a ���`a(���`bgc���`a ���aoa-���`a ���bmfc0.5���`a)���aoa*���aoa*���bmia2���`a ���aoa+���`a ���`a(���`bbc���`a ���aoa-���`a ���bmfc0.5���`a)���aoa*���aoa*���bmia2���`a ���aoa<���`a ���bmfc0.5���aoa*���aoa*���bmia2���`a
���`a
���bc1x# combine the color components���`a
���`fcolors���`a ���aoa=���`a ���`bnp���aoa.���`ezeros���`a(���`fsphere���aoa.���`eshape���`a ���aoa+���`a ���`a(���bmia3���`a,���`a)���`a)���`a
���`fcolors���`a[���aoa.���aoa.���aoa.���`a,���`a ���bmia0���`a]���`a ���aoa=���`a ���`brc���`a
���`fcolors���`a[���aoa.���aoa.���aoa.���`a,���`a ���bmia1���`a]���`a ���aoa=���`a ���`bgc���`a
���`fcolors���`a[���aoa.���aoa.���aoa.���`a,���`a ���bmia2���`a]���`a ���aoa=���`a ���`bbc���`a
���`a
���bc1u# and plot everything���`a
���`bax���`a ���aoa=���`a ���`cplt���aoa.���`ffigure���`a(���`a)���aoa.���`kadd_subplot���`a(���`jprojection���aoa=���bs1a'���bs1b3d���bs1a'���`a)���`a
���`bax���aoa.���`fvoxels���`a(���`ar���`a,���`a ���`ag���`a,���`a ���`ab���`a,���`a ���`fsphere���`a,���`a
���`j          ���`jfacecolors���aoa=���`fcolors���`a,���`a
���`j          ���`jedgecolors���aoa=���`bnp���aoa.���`dclip���`a(���bmia2���aoa*���`fcolors���`a ���aoa-���`a ���bmfc0.5���`a,���`a ���bmia0���`a,���`a ���bmia1���`a)���`a,���`b  ���bc1j# brighter���`a
���`j          ���`ilinewidth���aoa=���bmfc0.5���`a)���`a
���`bax���aoa.���`cset���`a(���`fxlabel���aoa=���bs1a'���bs1ar���bs1a'���`a,���`a ���`fylabel���aoa=���bs1a'���bs1ag���bs1a'���`a,���`a ���`fzlabel���aoa=���bs1a'���bs1ab���bs1a'���`a)���`a
���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
`dNone�