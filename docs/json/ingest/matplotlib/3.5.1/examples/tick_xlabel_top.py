��������{���bsdyn"""
==========================================
Set default x-axis tick labels on the top
==========================================

We can use :rc:`xtick.labeltop` and :rc:`xtick.top` and :rc:`xtick.labelbottom`
and :rc:`xtick.bottom` to control where on the axes ticks and their labels
appear.

These properties can also be set in ``.matplotlib/matplotlibrc``.
"""���`a
���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���`a
���`a
���`cplt���aoa.���`hrcParams���`a[���bs1a'���bs1lxtick.bottom���bs1a'���`a]���`a ���aoa=���`a ���`cplt���aoa.���`hrcParams���`a[���bs1a'���bs1qxtick.labelbottom���bs1a'���`a]���`a ���aoa=���`a ���bkceFalse���`a
���`cplt���aoa.���`hrcParams���`a[���bs1a'���bs1ixtick.top���bs1a'���`a]���`a ���aoa=���`a ���`cplt���aoa.���`hrcParams���`a[���bs1a'���bs1nxtick.labeltop���bs1a'���`a]���`a ���aoa=���`a ���bkcdTrue���`a
���`a
���`ax���`a ���aoa=���`a ���`bnp���aoa.���`farange���`a(���bmib10���`a)���`a
���`a
���`cfig���`a,���`a ���`bax���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`a)���`a
���`a
���`bax���aoa.���`dplot���`a(���`ax���`a)���`a
���`bax���aoa.���`iset_title���`a(���bs1a'���bs1jxlabel top���bs1a'���`a)���`b  ���bc1x)# Note title moves to make room for ticks���`a
���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
`dNone�