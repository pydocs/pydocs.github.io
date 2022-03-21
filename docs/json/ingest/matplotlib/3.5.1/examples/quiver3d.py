��������2���bsdxz"""
==============
3D quiver plot
==============

Demonstrates plotting directional arrows at points on a 3D meshgrid.
"""���`a
���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���`a
���`bax���`a ���aoa=���`a ���`cplt���aoa.���`ffigure���`a(���`a)���aoa.���`kadd_subplot���`a(���`jprojection���aoa=���bs1a'���bs1b3d���bs1a'���`a)���`a
���`a
���bc1o# Make the grid���`a
���`ax���`a,���`a ���`ay���`a,���`a ���`az���`a ���aoa=���`a ���`bnp���aoa.���`hmeshgrid���`a(���`bnp���aoa.���`farange���`a(���aoa-���bmfc0.8���`a,���`a ���bmia1���`a,���`a ���bmfc0.2���`a)���`a,���`a
���`v                      ���`bnp���aoa.���`farange���`a(���aoa-���bmfc0.8���`a,���`a ���bmia1���`a,���`a ���bmfc0.2���`a)���`a,���`a
���`v                      ���`bnp���aoa.���`farange���`a(���aoa-���bmfc0.8���`a,���`a ���bmia1���`a,���`a ���bmfc0.8���`a)���`a)���`a
���`a
���bc1x(# Make the direction data for the arrows���`a
���`au���`a ���aoa=���`a ���`bnp���aoa.���`csin���`a(���`bnp���aoa.���`bpi���`a ���aoa*���`a ���`ax���`a)���`a ���aoa*���`a ���`bnp���aoa.���`ccos���`a(���`bnp���aoa.���`bpi���`a ���aoa*���`a ���`ay���`a)���`a ���aoa*���`a ���`bnp���aoa.���`ccos���`a(���`bnp���aoa.���`bpi���`a ���aoa*���`a ���`az���`a)���`a
���`av���`a ���aoa=���`a ���aoa-���`bnp���aoa.���`ccos���`a(���`bnp���aoa.���`bpi���`a ���aoa*���`a ���`ax���`a)���`a ���aoa*���`a ���`bnp���aoa.���`csin���`a(���`bnp���aoa.���`bpi���`a ���aoa*���`a ���`ay���`a)���`a ���aoa*���`a ���`bnp���aoa.���`ccos���`a(���`bnp���aoa.���`bpi���`a ���aoa*���`a ���`az���`a)���`a
���`aw���`a ���aoa=���`a ���`a(���`bnp���aoa.���`dsqrt���`a(���bmfc2.0���`a ���aoa/���`a ���bmfc3.0���`a)���`a ���aoa*���`a ���`bnp���aoa.���`ccos���`a(���`bnp���aoa.���`bpi���`a ���aoa*���`a ���`ax���`a)���`a ���aoa*���`a ���`bnp���aoa.���`ccos���`a(���`bnp���aoa.���`bpi���`a ���aoa*���`a ���`ay���`a)���`a ���aoa*���`a
���`e     ���`bnp���aoa.���`csin���`a(���`bnp���aoa.���`bpi���`a ���aoa*���`a ���`az���`a)���`a)���`a
���`a
���`bax���aoa.���`fquiver���`a(���`ax���`a,���`a ���`ay���`a,���`a ���`az���`a,���`a ���`au���`a,���`a ���`av���`a,���`a ���`aw���`a,���`a ���`flength���aoa=���bmfc0.1���`a,���`a ���`inormalize���aoa=���bkcdTrue���`a)���`a
���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
`dNone�