������������bsdx8"""
===============
Simple Legend02
===============

"""���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���`a
���`cfig���`a,���`a ���`bax���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`a)���`a
���`a
���`eline1���`a,���`a ���aoa=���`a ���`bax���aoa.���`dplot���`a(���`a[���bmia1���`a,���`a ���bmia2���`a,���`a ���bmia3���`a]���`a,���`a ���`elabel���aoa=���bs2a"���bs2fLine 1���bs2a"���`a,���`a ���`ilinestyle���aoa=���bs1a'���bs1b--���bs1a'���`a)���`a
���`eline2���`a,���`a ���aoa=���`a ���`bax���aoa.���`dplot���`a(���`a[���bmia3���`a,���`a ���bmia2���`a,���`a ���bmia1���`a]���`a,���`a ���`elabel���aoa=���bs2a"���bs2fLine 2���bs2a"���`a,���`a ���`ilinewidth���aoa=���bmia4���`a)���`a
���`a
���bc1x%# Create a legend for the first line.���`a
���`lfirst_legend���`a ���aoa=���`a ���`bax���aoa.���`flegend���`a(���`ghandles���aoa=���`a[���`eline1���`a]���`a,���`a ���`cloc���aoa=���bs1a'���bs1kupper right���bs1a'���`a)���`a
���`a
���bc1x.# Add the legend manually to the current Axes.���`a
���`bax���aoa.���`jadd_artist���`a(���`lfirst_legend���`a)���`a
���`a
���bc1x,# Create another legend for the second line.���`a
���`bax���aoa.���`flegend���`a(���`ghandles���aoa=���`a[���`eline2���`a]���`a,���`a ���`cloc���aoa=���bs1a'���bs1klower right���bs1a'���`a)���`a
���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
`dNone�