��������9���bsdx�"""
=========================
Frontpage contour example
=========================

This example reproduces the frontpage contour example.
"""���`a
���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���bkndfrom���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����`a ���bknfimport���`a ���`bcm���`a
���`a
���`fextent���`a ���aoa=���`a ���`a(���aoa-���bmia3���`a,���`a ���bmia3���`a,���`a ���aoa-���bmia3���`a,���`a ���bmia3���`a)���`a
���`a
���`edelta���`a ���aoa=���`a ���bmfc0.5���`a
���`ax���`a ���aoa=���`a ���`bnp���aoa.���`farange���`a(���aoa-���bmfc3.0���`a,���`a ���bmfe4.001���`a,���`a ���`edelta���`a)���`a
���`ay���`a ���aoa=���`a ���`bnp���aoa.���`farange���`a(���aoa-���bmfc4.0���`a,���`a ���bmfe3.001���`a,���`a ���`edelta���`a)���`a
���`aX���`a,���`a ���`aY���`a ���aoa=���`a ���`bnp���aoa.���`hmeshgrid���`a(���`ax���`a,���`a ���`ay���`a)���`a
���`bZ1���`a ���aoa=���`a ���`bnp���aoa.���`cexp���`a(���aoa-���`aX���aoa*���aoa*���bmia2���`a ���aoa-���`a ���`aY���aoa*���aoa*���bmia2���`a)���`a
���`bZ2���`a ���aoa=���`a ���`bnp���aoa.���`cexp���`a(���aoa-���`a(���`aX���`a ���aoa-���`a ���bmia1���`a)���aoa*���aoa*���bmia2���`a ���aoa-���`a ���`a(���`aY���`a ���aoa-���`a ���bmia1���`a)���aoa*���aoa*���bmia2���`a)���`a
���`aZ���`a ���aoa=���`a ���`bZ1���`a ���aoa-���`a ���`bZ2���`a
���`a
���`dnorm���`a ���aoa=���`a ���`bcm���aoa.���`fcolors���aoa.���`iNormalize���`a(���`dvmax���aoa=���bnbcabs���`a(���`aZ���`a)���aoa.���`cmax���`a(���`a)���`a,���`a ���`dvmin���aoa=���aoa-���bnbcabs���`a(���`aZ���`a)���aoa.���`cmax���`a(���`a)���`a)���`a
���`a
���`cfig���`a,���`a ���`bax���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`a)���`a
���`ecset1���`a ���aoa=���`a ���`bax���aoa.���`hcontourf���`a(���`a
���`d    ���`aX���`a,���`a ���`aY���`a,���`a ���`aZ���`a,���`a ���bmib40���`a,���`a
���`d    ���`dnorm���aoa=���`dnorm���`a)���`a
���`bax���aoa.���`hset_xlim���`a(���aoa-���bmia2���`a,���`a ���bmia2���`a)���`a
���`bax���aoa.���`hset_ylim���`a(���aoa-���bmia2���`a,���`a ���bmia2���`a)���`a
���`bax���aoa.���`jset_xticks���`a(���`a[���`a]���`a)���`a
���`bax���aoa.���`jset_yticks���`a(���`a[���`a]���`a)���`a
���`cfig���aoa.���`gsavefig���`a(���bs2a"���bs2ucontour_frontpage.png���bs2a"���`a,���`a ���`cdpi���aoa=���bmib25���`a)���`b  ���bc1x# results in 160x120 px image���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
`dNone�