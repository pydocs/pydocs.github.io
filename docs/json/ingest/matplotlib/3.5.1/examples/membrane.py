������������bsdx�"""
======================
Frontpage plot example
======================

This example reproduces the frontpage simple plot example.
"""���`a
���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnecbook���`a ���akbas���`a ���bnnecbook���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���`a
���`a
���akdwith���`a ���`ecbook���aoa.���`oget_sample_data���`a(���bs1a'���bs1lmembrane.dat���bs1a'���`a)���`a ���akbas���`a ���`hdatafile���`a:���`a
���`d    ���`ax���`a ���aoa=���`a ���`bnp���aoa.���`hfromfile���`a(���`hdatafile���`a,���`a ���`bnp���aoa.���`gfloat32���`a)���`a
���bc1x# 0.0005 is the sample interval���`a
���`a
���`cfig���`a,���`a ���`bax���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`a)���`a
���`bax���aoa.���`dplot���`a(���`ax���`a,���`a ���`ilinewidth���aoa=���bmia4���`a)���`a
���`bax���aoa.���`hset_xlim���`a(���bmid5000���`a,���`a ���bmid6000���`a)���`a
���`bax���aoa.���`hset_ylim���`a(���aoa-���bmfc0.6���`a,���`a ���bmfc0.1���`a)���`a
���`bax���aoa.���`jset_xticks���`a(���`a[���`a]���`a)���`a
���`bax���aoa.���`jset_yticks���`a(���`a[���`a]���`a)���`a
���`cfig���aoa.���`gsavefig���`a(���bs2a"���bs2vmembrane_frontpage.png���bs2a"���`a,���`a ���`cdpi���aoa=���bmib25���`a)���`b  ���bc1x# results in 160x120 px image���`a
`dNone�