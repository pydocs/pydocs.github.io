��������d���bsdyb"""
============================================================================
Demonstrates plotting contour (level) curves in 3D using the extend3d option
============================================================================

This modification of the contour3d_demo example uses extend3d=True to
extend the curves vertically into 'ribbons'.
"""���`a
���`a
���bkndfrom���`a ���bnnlmpl_toolkits���bnna.���bnngmplot3d���`a ���bknfimport���`a ���`faxes3d���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���bkndfrom���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����`a ���bknfimport���`a ���`bcm���`a
���`a
���`bax���`a ���aoa=���`a ���`cplt���aoa.���`ffigure���`a(���`a)���aoa.���`kadd_subplot���`a(���`jprojection���aoa=���bs1a'���bs1b3d���bs1a'���`a)���`a
���`aX���`a,���`a ���`aY���`a,���`a ���`aZ���`a ���aoa=���`a ���`faxes3d���aoa.���`mget_test_data���`a(���bmfd0.05���`a)���`a
���`bax���aoa.���`gcontour���`a(���`aX���`a,���`a ���`aY���`a,���`a ���`aZ���`a,���`a ���`hextend3d���aoa=���bkcdTrue���`a,���`a ���`dcmap���aoa=���`bcm���aoa.���`hcoolwarm���`a)���`a
���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
`dNone�