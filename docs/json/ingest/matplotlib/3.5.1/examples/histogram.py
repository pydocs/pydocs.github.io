������������bsdx�"""
===========================
Frontpage histogram example
===========================

This example reproduces the frontpage histogram example.
"""���`a
���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���`a
���`a
���`lrandom_state���`a ���aoa=���`a ���`bnp���aoa.���`frandom���aoa.���`kRandomState���`a(���bmih19680801���`a)���`a
���`aX���`a ���aoa=���`a ���`lrandom_state���aoa.���`erandn���`a(���bmie10000���`a)���`a
���`a
���`cfig���`a,���`a ���`bax���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`a)���`a
���`bax���aoa.���`dhist���`a(���`aX���`a,���`a ���`dbins���aoa=���bmib25���`a,���`a ���`gdensity���aoa=���bkcdTrue���`a)���`a
���`ax���`a ���aoa=���`a ���`bnp���aoa.���`hlinspace���`a(���aoa-���bmia5���`a,���`a ���bmia5���`a,���`a ���bmid1000���`a)���`a
���`bax���aoa.���`dplot���`a(���`ax���`a,���`a ���bmia1���`a ���aoa/���`a ���`bnp���aoa.���`dsqrt���`a(���bmia2���aoa*���`bnp���aoa.���`bpi���`a)���`a ���aoa*���`a ���`bnp���aoa.���`cexp���`a(���aoa-���`a(���`ax���aoa*���aoa*���bmia2���`a)���aoa/���bmia2���`a)���`a,���`a ���`ilinewidth���aoa=���bmia4���`a)���`a
���`bax���aoa.���`jset_xticks���`a(���`a[���`a]���`a)���`a
���`bax���aoa.���`jset_yticks���`a(���`a[���`a]���`a)���`a
���`cfig���aoa.���`gsavefig���`a(���bs2a"���bs2whistogram_frontpage.png���bs2a"���`a,���`a ���`cdpi���aoa=���bmib25���`a)���`b  ���bc1x# results in 160x120 px image���`a
`dNone�