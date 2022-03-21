�����������bsdy\"""
===============
Aligning Labels
===============

Aligning xlabel and ylabel using `.Figure.align_xlabels` and
`.Figure.align_ylabels`

`.Figure.align_labels` wraps these two functions.

Note that the xlabel "XLabel1 1" would normally be much closer to the
x-axis, and "YLabel1 0" would be much closer to the y-axis of their
respective axes.
"""���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnhgridspec���`a ���akbas���`a ���bnnhgridspec���`a
���`a
���`cfig���`a ���aoa=���`a ���`cplt���aoa.���`ffigure���`a(���`ltight_layout���aoa=���bkcdTrue���`a)���`a
���`bgs���`a ���aoa=���`a ���`hgridspec���aoa.���`hGridSpec���`a(���bmia2���`a,���`a ���bmia2���`a)���`a
���`a
���`bax���`a ���aoa=���`a ���`cfig���aoa.���`kadd_subplot���`a(���`bgs���`a[���bmia0���`a,���`a ���`a:���`a]���`a)���`a
���`bax���aoa.���`dplot���`a(���`bnp���aoa.���`farange���`a(���bmia0���`a,���`a ���bmfc1e6���`a,���`a ���bmid1000���`a)���`a)���`a
���`bax���aoa.���`jset_ylabel���`a(���bs1a'���bs1gYLabel0���bs1a'���`a)���`a
���`bax���aoa.���`jset_xlabel���`a(���bs1a'���bs1gXLabel0���bs1a'���`a)���`a
���`a
���akcfor���`a ���`ai���`a ���bowbin���`a ���bnberange���`a(���bmia2���`a)���`a:���`a
���`d    ���`bax���`a ���aoa=���`a ���`cfig���aoa.���`kadd_subplot���`a(���`bgs���`a[���bmia1���`a,���`a ���`ai���`a]���`a)���`a
���`d    ���`bax���aoa.���`dplot���`a(���`bnp���aoa.���`farange���`a(���bmfb1.���`a,���`a ���bmfb0.���`a,���`a ���aoa-���bmfc0.1���`a)���`a ���aoa*���`a ���bmfe2000.���`a,���`a ���`bnp���aoa.���`farange���`a(���bmfb1.���`a,���`a ���bmfb0.���`a,���`a ���aoa-���bmfc0.1���`a)���`a)���`a
���`d    ���`bax���aoa.���`jset_ylabel���`a(���bs1a'���bs1hYLabel1 ���bsib%d���bs1a'���`a ���aoa%���`a ���`ai���`a)���`a
���`d    ���`bax���aoa.���`jset_xlabel���`a(���bs1a'���bs1hXLabel1 ���bsib%d���bs1a'���`a ���aoa%���`a ���`ai���`a)���`a
���`d    ���akbif���`a ���`ai���`a ���aob==���`a ���bmia0���`a:���`a
���`h        ���akcfor���`a ���`dtick���`a ���bowbin���`a ���`bax���aoa.���`oget_xticklabels���`a(���`a)���`a:���`a
���`l            ���`dtick���aoa.���`lset_rotation���`a(���bmib55���`a)���`a
���`cfig���aoa.���`lalign_labels���`a(���`a)���`b  ���bc1x2# same as fig.align_xlabels(); fig.align_ylabels()���`a
���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
`dNone�