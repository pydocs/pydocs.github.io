������������bsdx�"""
=================================
2D and 3D *Axes* in same *Figure*
=================================

This example shows a how to plot a 2D and 3D plot on the same figure.
"""���`a
���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���`a
���`a
���akcdef���`a ���bnfaf���`a(���`at���`a)���`a:���`a
���`d    ���akfreturn���`a ���`bnp���aoa.���`ccos���`a(���bmia2���aoa*���`bnp���aoa.���`bpi���aoa*���`at���`a)���`a ���aoa*���`a ���`bnp���aoa.���`cexp���`a(���aoa-���`at���`a)���`a
���`a
���`a
���bc1x-# Set up a figure twice as tall as it is wide���`a
���`cfig���`a ���aoa=���`a ���`cplt���aoa.���`ffigure���`a(���`gfigsize���aoa=���`cplt���aoa.���`ifigaspect���`a(���bmfb2.���`a)���`a)���`a
���`cfig���aoa.���`hsuptitle���`a(���bs1a'���bs1tA tale of 2 subplots���bs1a'���`a)���`a
���`a
���bc1o# First subplot���`a
���`bax���`a ���aoa=���`a ���`cfig���aoa.���`kadd_subplot���`a(���bmia2���`a,���`a ���bmia1���`a,���`a ���bmia1���`a)���`a
���`a
���`bt1���`a ���aoa=���`a ���`bnp���aoa.���`farange���`a(���bmfc0.0���`a,���`a ���bmfc5.0���`a,���`a ���bmfc0.1���`a)���`a
���`bt2���`a ���aoa=���`a ���`bnp���aoa.���`farange���`a(���bmfc0.0���`a,���`a ���bmfc5.0���`a,���`a ���bmfd0.02���`a)���`a
���`bt3���`a ���aoa=���`a ���`bnp���aoa.���`farange���`a(���bmfc0.0���`a,���`a ���bmfc2.0���`a,���`a ���bmfd0.01���`a)���`a
���`a
���`bax���aoa.���`dplot���`a(���`bt1���`a,���`a ���`af���`a(���`bt1���`a)���`a,���`a ���bs1a'���bs1bbo���bs1a'���`a,���`a
���`h        ���`bt2���`a,���`a ���`af���`a(���`bt2���`a)���`a,���`a ���bs1a'���bs1ck--���bs1a'���`a,���`a ���`omarkerfacecolor���aoa=���bs1a'���bs1egreen���bs1a'���`a)���`a
���`bax���aoa.���`dgrid���`a(���bkcdTrue���`a)���`a
���`bax���aoa.���`jset_ylabel���`a(���bs1a'���bs1rDamped oscillation���bs1a'���`a)���`a
���`a
���bc1p# Second subplot���`a
���`bax���`a ���aoa=���`a ���`cfig���aoa.���`kadd_subplot���`a(���bmia2���`a,���`a ���bmia1���`a,���`a ���bmia2���`a,���`a ���`jprojection���aoa=���bs1a'���bs1b3d���bs1a'���`a)���`a
���`a
���`aX���`a ���aoa=���`a ���`bnp���aoa.���`farange���`a(���aoa-���bmia5���`a,���`a ���bmia5���`a,���`a ���bmfd0.25���`a)���`a
���`aY���`a ���aoa=���`a ���`bnp���aoa.���`farange���`a(���aoa-���bmia5���`a,���`a ���bmia5���`a,���`a ���bmfd0.25���`a)���`a
���`aX���`a,���`a ���`aY���`a ���aoa=���`a ���`bnp���aoa.���`hmeshgrid���`a(���`aX���`a,���`a ���`aY���`a)���`a
���`aR���`a ���aoa=���`a ���`bnp���aoa.���`dsqrt���`a(���`aX���aoa*���aoa*���bmia2���`a ���aoa+���`a ���`aY���aoa*���aoa*���bmia2���`a)���`a
���`aZ���`a ���aoa=���`a ���`bnp���aoa.���`csin���`a(���`aR���`a)���`a
���`a
���`dsurf���`a ���aoa=���`a ���`bax���aoa.���`lplot_surface���`a(���`aX���`a,���`a ���`aY���`a,���`a ���`aZ���`a,���`a ���`grstride���aoa=���bmia1���`a,���`a ���`gcstride���aoa=���bmia1���`a,���`a
���`w                       ���`ilinewidth���aoa=���bmia0���`a,���`a ���`kantialiased���aoa=���bkceFalse���`a)���`a
���`bax���aoa.���`hset_zlim���`a(���aoa-���bmia1���`a,���`a ���bmia1���`a)���`a
���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
`dNone�