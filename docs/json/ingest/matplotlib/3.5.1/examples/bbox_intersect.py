�����������bsdy'"""
===========================================
Changing colors of lines intersecting a box
===========================================

The lines intersecting the rectangle are colored in red, while the others
are left as blue lines. This example showcases the `.intersects_bbox` function.

"""���`a
���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���bkndfrom���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnjtransforms���`a ���bknfimport���`a ���`dBbox���`a
���bkndfrom���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnndpath���`a ���bknfimport���`a ���`dPath���`a
���`a
���bc1x)# Fixing random state for reproducibility���`a
���`bnp���aoa.���`frandom���aoa.���`dseed���`a(���bmih19680801���`a)���`a
���`a
���`a
���`dleft���`a,���`a ���`fbottom���`a,���`a ���`ewidth���`a,���`a ���`fheight���`a ���aoa=���`a ���`a(���aoa-���bmia1���`a,���`a ���aoa-���bmia1���`a,���`a ���bmia2���`a,���`a ���bmia2���`a)���`a
���`drect���`a ���aoa=���`a ���`cplt���aoa.���`iRectangle���`a(���`a(���`dleft���`a,���`a ���`fbottom���`a)���`a,���`a ���`ewidth���`a,���`a ���`fheight���`a,���`a
���`u                     ���`ifacecolor���aoa=���bs2a"���bs2eblack���bs2a"���`a,���`a ���`ealpha���aoa=���bmfc0.1���`a)���`a
���`a
���`cfig���`a,���`a ���`bax���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`a)���`a
���`bax���aoa.���`iadd_patch���`a(���`drect���`a)���`a
���`a
���`dbbox���`a ���aoa=���`a ���`dBbox���aoa.���`kfrom_bounds���`a(���`dleft���`a,���`a ���`fbottom���`a,���`a ���`ewidth���`a,���`a ���`fheight���`a)���`a
���`a
���akcfor���`a ���`ai���`a ���bowbin���`a ���bnberange���`a(���bmib12���`a)���`a:���`a
���`d    ���`hvertices���`a ���aoa=���`a ���`a(���`bnp���aoa.���`frandom���aoa.���`frandom���`a(���`a(���bmia2���`a,���`a ���bmia2���`a)���`a)���`a ���aoa-���`a ���bmfc0.5���`a)���`a ���aoa*���`a ���bmfc6.0���`a
���`d    ���`dpath���`a ���aoa=���`a ���`dPath���`a(���`hvertices���`a)���`a
���`d    ���akbif���`a ���`dpath���aoa.���`ointersects_bbox���`a(���`dbbox���`a)���`a:���`a
���`h        ���`ecolor���`a ���aoa=���`a ���bs1a'���bs1ar���bs1a'���`a
���`d    ���akdelse���`a:���`a
���`h        ���`ecolor���`a ���aoa=���`a ���bs1a'���bs1ab���bs1a'���`a
���`d    ���`bax���aoa.���`dplot���`a(���`hvertices���`a[���`a:���`a,���`a ���bmia0���`a]���`a,���`a ���`hvertices���`a[���`a:���`a,���`a ���bmia1���`a]���`a,���`a ���`ecolor���aoa=���`ecolor���`a)���`a
���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
`dNone�