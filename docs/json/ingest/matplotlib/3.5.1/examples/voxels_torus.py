������������bsdx�"""
=======================================================
3D voxel / volumetric plot with cylindrical coordinates
=======================================================

Demonstrates using the *x*, *y*, *z* parameters of `.Axes3D.voxels`.
"""���`a
���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfcolors���`a
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
���`ar���`a,���`a ���`etheta���`a,���`a ���`az���`a ���aoa=���`a ���`bnp���aoa.���`emgrid���`a[���bmia0���`a:���bmia1���`a:���bmib11���`aj���`a,���`a ���bmia0���`a:���`bnp���aoa.���`bpi���aoa*���bmia2���`a:���bmib25���`aj���`a,���`a ���aoa-���bmfc0.5���`a:���bmfc0.5���`a:���bmib11���`aj���`a]���`a
���`ax���`a ���aoa=���`a ���`ar���aoa*���`bnp���aoa.���`ccos���`a(���`etheta���`a)���`a
���`ay���`a ���aoa=���`a ���`ar���aoa*���`bnp���aoa.���`csin���`a(���`etheta���`a)���`a
���`a
���`brc���`a,���`a ���`fthetac���`a,���`a ���`bzc���`a ���aoa=���`a ���`imidpoints���`a(���`ar���`a)���`a,���`a ���`imidpoints���`a(���`etheta���`a)���`a,���`a ���`imidpoints���`a(���`az���`a)���`a
���`a
���bc1x)# define a wobbly torus about [0.7, *, 0]���`a
���`fsphere���`a ���aoa=���`a ���`a(���`brc���`a ���aoa-���`a ���bmfc0.7���`a)���aoa*���aoa*���bmia2���`a ���aoa+���`a ���`a(���`bzc���`a ���aoa+���`a ���bmfc0.2���aoa*���`bnp���aoa.���`ccos���`a(���`fthetac���aoa*���bmia2���`a)���`a)���aoa*���aoa*���bmia2���`a ���aoa<���`a ���bmfc0.2���aoa*���aoa*���bmia2���`a
���`a
���bc1x# combine the color components���`a
���`chsv���`a ���aoa=���`a ���`bnp���aoa.���`ezeros���`a(���`fsphere���aoa.���`eshape���`a ���aoa+���`a ���`a(���bmia3���`a,���`a)���`a)���`a
���`chsv���`a[���aoa.���aoa.���aoa.���`a,���`a ���bmia0���`a]���`a ���aoa=���`a ���`fthetac���`a ���aoa/���`a ���`a(���`bnp���aoa.���`bpi���aoa*���bmia2���`a)���`a
���`chsv���`a[���aoa.���aoa.���aoa.���`a,���`a ���bmia1���`a]���`a ���aoa=���`a ���`brc���`a
���`chsv���`a[���aoa.���aoa.���aoa.���`a,���`a ���bmia2���`a]���`a ���aoa=���`a ���`bzc���`a ���aoa+���`a ���bmfc0.5���`a
���`fcolors���`a ���aoa=���`a ���`���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����aoa.���`fcolors���aoa.���`jhsv_to_rgb���`a(���`chsv���`a)���`a
���`a
���bc1u# and plot everything���`a
���`bax���`a ���aoa=���`a ���`cplt���aoa.���`ffigure���`a(���`a)���aoa.���`kadd_subplot���`a(���`jprojection���aoa=���bs1a'���bs1b3d���bs1a'���`a)���`a
���`bax���aoa.���`fvoxels���`a(���`ax���`a,���`a ���`ay���`a,���`a ���`az���`a,���`a ���`fsphere���`a,���`a
���`j          ���`jfacecolors���aoa=���`fcolors���`a,���`a
���`j          ���`jedgecolors���aoa=���`bnp���aoa.���`dclip���`a(���bmia2���aoa*���`fcolors���`a ���aoa-���`a ���bmfc0.5���`a,���`a ���bmia0���`a,���`a ���bmia1���`a)���`a,���`b  ���bc1j# brighter���`a
���`j          ���`ilinewidth���aoa=���bmfc0.5���`a)���`a
���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
`dNone�