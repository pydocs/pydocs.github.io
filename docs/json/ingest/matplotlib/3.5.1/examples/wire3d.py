��������g���bsdxn"""
=================
3D wireframe plot
=================

A very basic demonstration of a wireframe plot.
"""���`a
���`a
���bkndfrom���`a ���bnnlmpl_toolkits���bnna.���bnngmplot3d���`a ���bknfimport���`a ���`faxes3d���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���`a
���`a
���`cfig���`a ���aoa=���`a ���`cplt���aoa.���`ffigure���`a(���`a)���`a
���`bax���`a ���aoa=���`a ���`cfig���aoa.���`kadd_subplot���`a(���`jprojection���aoa=���bs1a'���bs1b3d���bs1a'���`a)���`a
���`a
���bc1v# Grab some test data.���`a
���`aX���`a,���`a ���`aY���`a,���`a ���`aZ���`a ���aoa=���`a ���`faxes3d���aoa.���`mget_test_data���`a(���bmfd0.05���`a)���`a
���`a
���bc1x# Plot a basic wireframe.���`a
���`bax���aoa.���`nplot_wireframe���`a(���`aX���`a,���`a ���`aY���`a,���`a ���`aZ���`a,���`a ���`grstride���aoa=���bmib10���`a,���`a ���`gcstride���aoa=���bmib10���`a)���`a
���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
`dNone�