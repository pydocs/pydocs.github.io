�����������bsdy"""
=====================
Grayscale style sheet
=====================

This example demonstrates the "grayscale" style sheet, which changes all colors
that are defined as `.rcParams` to grayscale. Note, however, that not all
plot elements respect `.rcParams`.
"""���`a
���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���`a
���bc1x)# Fixing random state for reproducibility���`a
���`bnp���aoa.���`frandom���aoa.���`dseed���`a(���bmih19680801���`a)���`a
���`a
���`a
���akcdef���`a ���bnfscolor_cycle_example���`a(���`bax���`a)���`a:���`a
���`d    ���`aL���`a ���aoa=���`a ���bmia6���`a
���`d    ���`ax���`a ���aoa=���`a ���`bnp���aoa.���`hlinspace���`a(���bmia0���`a,���`a ���`aL���`a)���`a
���`d    ���`gncolors���`a ���aoa=���`a ���bnbclen���`a(���`cplt���aoa.���`hrcParams���`a[���bs1a'���bs1oaxes.prop_cycle���bs1a'���`a]���`a)���`a
���`d    ���`eshift���`a ���aoa=���`a ���`bnp���aoa.���`hlinspace���`a(���bmia0���`a,���`a ���`aL���`a,���`a ���`gncolors���`a,���`a ���`hendpoint���aoa=���bkceFalse���`a)���`a
���`d    ���akcfor���`a ���`as���`a ���bowbin���`a ���`eshift���`a:���`a
���`h        ���`bax���aoa.���`dplot���`a(���`ax���`a,���`a ���`bnp���aoa.���`csin���`a(���`ax���`a ���aoa+���`a ���`as���`a)���`a,���`a ���bs1a'���bs1bo-���bs1a'���`a)���`a
���`a
���`a
���akcdef���`a ���bnfwimage_and_patch_example���`a(���`bax���`a)���`a:���`a
���`d    ���`bax���aoa.���`fimshow���`a(���`bnp���aoa.���`frandom���aoa.���`frandom���`a(���`dsize���aoa=���`a(���bmib20���`a,���`a ���bmib20���`a)���`a)���`a,���`a ���`minterpolation���aoa=���bs1a'���bs1dnone���bs1a'���`a)���`a
���`d    ���`ac���`a ���aoa=���`a ���`cplt���aoa.���`fCircle���`a(���`a(���bmia5���`a,���`a ���bmia5���`a)���`a,���`a ���`fradius���aoa=���bmia5���`a,���`a ���`elabel���aoa=���bs1a'���bs1epatch���bs1a'���`a)���`a
���`d    ���`bax���aoa.���`iadd_patch���`a(���`ac���`a)���`a
���`a
���`a
���`cplt���aoa.���`estyle���aoa.���`cuse���`a(���bs1a'���bs1igrayscale���bs1a'���`a)���`a
���`a
���`cfig���`a,���`a ���`a(���`cax1���`a,���`a ���`cax2���`a)���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`encols���aoa=���bmia2���`a)���`a
���`cfig���aoa.���`hsuptitle���`a(���bs2a"���bs2a'���bs2igrayscale���bs2a'���bs2l style sheet���bs2a"���`a)���`a
���`a
���`scolor_cycle_example���`a(���`cax1���`a)���`a
���`wimage_and_patch_example���`a(���`cax2���`a)���`a
���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
`dNone�