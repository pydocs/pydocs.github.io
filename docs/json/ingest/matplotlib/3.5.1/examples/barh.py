������������bsdx}"""
====================
Horizontal bar chart
====================

This example showcases a simple horizontal bar chart.
"""���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���`a
���bc1x)# Fixing random state for reproducibility���`a
���`bnp���aoa.���`frandom���aoa.���`dseed���`a(���bmih19680801���`a)���`a
���`a
���`a
���`cplt���aoa.���`jrcdefaults���`a(���`a)���`a
���`cfig���`a,���`a ���`bax���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`a)���`a
���`a
���bc1n# Example data���`a
���`fpeople���`a ���aoa=���`a ���`a(���bs1a'���bs1cTom���bs1a'���`a,���`a ���bs1a'���bs1dDick���bs1a'���`a,���`a ���bs1a'���bs1eHarry���bs1a'���`a,���`a ���bs1a'���bs1dSlim���bs1a'���`a,���`a ���bs1a'���bs1cJim���bs1a'���`a)���`a
���`ey_pos���`a ���aoa=���`a ���`bnp���aoa.���`farange���`a(���bnbclen���`a(���`fpeople���`a)���`a)���`a
���`kperformance���`a ���aoa=���`a ���bmia3���`a ���aoa+���`a ���bmib10���`a ���aoa*���`a ���`bnp���aoa.���`frandom���aoa.���`drand���`a(���bnbclen���`a(���`fpeople���`a)���`a)���`a
���`eerror���`a ���aoa=���`a ���`bnp���aoa.���`frandom���aoa.���`drand���`a(���bnbclen���`a(���`fpeople���`a)���`a)���`a
���`a
���`bax���aoa.���`dbarh���`a(���`ey_pos���`a,���`a ���`kperformance���`a,���`a ���`dxerr���aoa=���`eerror���`a,���`a ���`ealign���aoa=���bs1a'���bs1fcenter���bs1a'���`a)���`a
���`bax���aoa.���`jset_yticks���`a(���`ey_pos���`a,���`a ���`flabels���aoa=���`fpeople���`a)���`a
���`bax���aoa.���`linvert_yaxis���`a(���`a)���`b  ���bc1x# labels read top-to-bottom���`a
���`bax���aoa.���`jset_xlabel���`a(���bs1a'���bs1kPerformance���bs1a'���`a)���`a
���`bax���aoa.���`iset_title���`a(���bs1a'���bs1x!How fast do you want to go today?���bs1a'���`a)���`a
���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
`dNone�