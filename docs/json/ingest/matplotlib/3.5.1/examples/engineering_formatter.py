��������(���bsdx�"""
=========================================
Labeling ticks using engineering notation
=========================================

Use of the engineering Formatter.
"""���`a
���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���`a
���bkndfrom���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfticker���`a ���bknfimport���`a ���`lEngFormatter���`a
���`a
���bc1x)# Fixing random state for reproducibility���`a
���`dprng���`a ���aoa=���`a ���`bnp���aoa.���`frandom���aoa.���`kRandomState���`a(���bmih19680801���`a)���`a
���`a
���bc1x!# Create artificial data to plot.���`a
���bc1xJ# The x data span over several decades to demonstrate several SI prefixes.���`a
���`bxs���`a ���aoa=���`a ���`bnp���aoa.���`hlogspace���`a(���bmia1���`a,���`a ���bmia9���`a,���`a ���bmic100���`a)���`a
���`bys���`a ���aoa=���`a ���`a(���bmfc0.8���`a ���aoa+���`a ���bmfc0.4���`a ���aoa*���`a ���`dprng���aoa.���`guniform���`a(���`dsize���aoa=���bmic100���`a)���`a)���`a ���aoa*���`a ���`bnp���aoa.���`elog10���`a(���`bxs���`a)���aoa*���aoa*���bmia2���`a
���`a
���bc1xL# Figure width is doubled (2*6.4) to display nicely 2 subplots side by side.���`a
���`cfig���`a,���`a ���`a(���`cax0���`a,���`a ���`cax1���`a)���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`enrows���aoa=���bmia2���`a,���`a ���`gfigsize���aoa=���`a(���bmia7���`a,���`a ���bmfc9.6���`a)���`a)���`a
���akcfor���`a ���`bax���`a ���bowbin���`a ���`a(���`cax0���`a,���`a ���`cax1���`a)���`a:���`a
���`d    ���`bax���aoa.���`jset_xscale���`a(���bs1a'���bs1clog���bs1a'���`a)���`a
���`a
���bc1x?# Demo of the default settings, with a user-defined unit label.���`a
���`cax0���aoa.���`iset_title���`a(���bs1a'���bs1x<Full unit ticklabels, w/ default precision & space separator���bs1a'���`a)���`a
���`jformatter0���`a ���aoa=���`a ���`lEngFormatter���`a(���`dunit���aoa=���bs1a'���bs1bHz���bs1a'���`a)���`a
���`cax0���aoa.���`exaxis���aoa.���`sset_major_formatter���`a(���`jformatter0���`a)���`a
���`cax0���aoa.���`dplot���`a(���`bxs���`a,���`a ���`bys���`a)���`a
���`cax0���aoa.���`jset_xlabel���`a(���bs1a'���bs1iFrequency���bs1a'���`a)���`a
���`a
���bc1xH# Demo of the options `places` (number of digit after decimal point) and���`a
���bc1x;# `sep` (separator between the number and the prefix/unit).���`a
���`cax1���aoa.���`iset_title���`a(���bs1a'���bs1x/SI-prefix only ticklabels, 1-digit precision & ���bs1a'���`a
���`n              ���bs1a'���bs1tthin space separator���bs1a'���`a)���`a
���`jformatter1���`a ���aoa=���`a ���`lEngFormatter���`a(���`fplaces���aoa=���bmia1���`a,���`a ���`csep���aoa=���bs2a"���bsen\N{THIN SPACE}���bs2a"���`a)���`b  ���bc1h# U+2009���`a
���`cax1���aoa.���`exaxis���aoa.���`sset_major_formatter���`a(���`jformatter1���`a)���`a
���`cax1���aoa.���`dplot���`a(���`bxs���`a,���`a ���`bys���`a)���`a
���`cax1���aoa.���`jset_xlabel���`a(���bs1a'���bs1nFrequency [Hz]���bs1a'���`a)���`a
���`a
���`cplt���aoa.���`ltight_layout���`a(���`a)���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
`dNone�