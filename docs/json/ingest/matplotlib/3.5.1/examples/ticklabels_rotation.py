������������bsdx�"""
===========================
Rotating custom tick labels
===========================

Demo of custom tick-labels with user-defined rotation.
"""���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���`a
���`a
���`ax���`a ���aoa=���`a ���`a[���bmia1���`a,���`a ���bmia2���`a,���`a ���bmia3���`a,���`a ���bmia4���`a]���`a
���`ay���`a ���aoa=���`a ���`a[���bmia1���`a,���`a ���bmia4���`a,���`a ���bmia9���`a,���`a ���bmia6���`a]���`a
���`flabels���`a ���aoa=���`a ���`a[���bs1a'���bs1eFrogs���bs1a'���`a,���`a ���bs1a'���bs1dHogs���bs1a'���`a,���`a ���bs1a'���bs1dBogs���bs1a'���`a,���`a ���bs1a'���bs1eSlogs���bs1a'���`a]���`a
���`a
���`cplt���aoa.���`dplot���`a(���`ax���`a,���`a ���`ay���`a)���`a
���bc1xM# You can specify a rotation for the tick labels in degrees or with keywords.���`a
���`cplt���aoa.���`fxticks���`a(���`ax���`a,���`a ���`flabels���`a,���`a ���`hrotation���aoa=���bs1a'���bs1hvertical���bs1a'���`a)���`a
���bc1x;# Pad margins so that markers don't get clipped by the axes���`a
���`cplt���aoa.���`gmargins���`a(���bmfc0.2���`a)���`a
���bc1x2# Tweak spacing to prevent clipping of tick-labels���`a
���`cplt���aoa.���`osubplots_adjust���`a(���`fbottom���aoa=���bmfd0.15���`a)���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
`dNone�