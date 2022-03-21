��������_���bsdy5"""
===============
Filled contours
===============

contourf differs from contour in that it creates filled contours, ie.
a discrete number of colours are used to shade the domain.

This is like a contourf plot in 2D except that the shaded region corresponding
to the level c is graphed on the plane z=c.
"""���`a
���`a
���bkndfrom���`a ���bnnlmpl_toolkits���bnna.���bnngmplot3d���`a ���bknfimport���`a ���`faxes3d���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���bkndfrom���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����`a ���bknfimport���`a ���`bcm���`a
���`a
���`bax���`a ���aoa=���`a ���`cplt���aoa.���`ffigure���`a(���`a)���aoa.���`kadd_subplot���`a(���`jprojection���aoa=���bs1a'���bs1b3d���bs1a'���`a)���`a
���`aX���`a,���`a ���`aY���`a,���`a ���`aZ���`a ���aoa=���`a ���`faxes3d���aoa.���`mget_test_data���`a(���bmfd0.05���`a)���`a
���`bax���aoa.���`hcontourf���`a(���`aX���`a,���`a ���`aY���`a,���`a ���`aZ���`a,���`a ���`dcmap���aoa=���`bcm���aoa.���`hcoolwarm���`a)���`a
���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
`dNone�