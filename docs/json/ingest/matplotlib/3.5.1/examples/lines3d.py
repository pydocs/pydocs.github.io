������������bsdxx"""
================
Parametric Curve
================

This example demonstrates plotting a parametric curve in 3D.
"""���`a
���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���`a
���`a
���`bax���`a ���aoa=���`a ���`cplt���aoa.���`ffigure���`a(���`a)���aoa.���`kadd_subplot���`a(���`jprojection���aoa=���bs1a'���bs1b3d���bs1a'���`a)���`a
���`a
���bc1x# Prepare arrays x, y, z���`a
���`etheta���`a ���aoa=���`a ���`bnp���aoa.���`hlinspace���`a(���aoa-���bmia4���`a ���aoa*���`a ���`bnp���aoa.���`bpi���`a,���`a ���bmia4���`a ���aoa*���`a ���`bnp���aoa.���`bpi���`a,���`a ���bmic100���`a)���`a
���`az���`a ���aoa=���`a ���`bnp���aoa.���`hlinspace���`a(���aoa-���bmia2���`a,���`a ���bmia2���`a,���`a ���bmic100���`a)���`a
���`ar���`a ���aoa=���`a ���`az���aoa*���aoa*���bmia2���`a ���aoa+���`a ���bmia1���`a
���`ax���`a ���aoa=���`a ���`ar���`a ���aoa*���`a ���`bnp���aoa.���`csin���`a(���`etheta���`a)���`a
���`ay���`a ���aoa=���`a ���`ar���`a ���aoa*���`a ���`bnp���aoa.���`ccos���`a(���`etheta���`a)���`a
���`a
���`bax���aoa.���`dplot���`a(���`ax���`a,���`a ���`ay���`a,���`a ���`az���`a,���`a ���`elabel���aoa=���bs1a'���bs1pparametric curve���bs1a'���`a)���`a
���`bax���aoa.���`flegend���`a(���`a)���`a
���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
`dNone�