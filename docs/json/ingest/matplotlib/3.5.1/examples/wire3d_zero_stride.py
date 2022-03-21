������������bsdx�"""
===================================
3D wireframe plots in one direction
===================================

Demonstrates that setting rstride or cstride to 0 causes wires to not be
generated in the corresponding direction.
"""���`a
���`a
���bkndfrom���`a ���bnnlmpl_toolkits���bnna.���bnngmplot3d���`a ���bknfimport���`a ���`faxes3d���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���`a
���`a
���`cfig���`a,���`a ���`a(���`cax1���`a,���`a ���`cax2���`a)���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`a
���`d    ���bmia2���`a,���`a ���bmia1���`a,���`a ���`gfigsize���aoa=���`a(���bmia8���`a,���`a ���bmib12���`a)���`a,���`a ���`jsubplot_kw���aoa=���`a{���bs1a'���bs1jprojection���bs1a'���`a:���`a ���bs1a'���bs1b3d���bs1a'���`a}���`a)���`a
���`a
���bc1s# Get the test data���`a
���`aX���`a,���`a ���`aY���`a,���`a ���`aZ���`a ���aoa=���`a ���`faxes3d���aoa.���`mget_test_data���`a(���bmfd0.05���`a)���`a
���`a
���bc1x7# Give the first plot only wireframes of the type y = c���`a
���`cax1���aoa.���`nplot_wireframe���`a(���`aX���`a,���`a ���`aY���`a,���`a ���`aZ���`a,���`a ���`grstride���aoa=���bmib10���`a,���`a ���`gcstride���aoa=���bmia0���`a)���`a
���`cax1���aoa.���`iset_title���`a(���bs2a"���bs2xColumn (x) stride set to 0���bs2a"���`a)���`a
���`a
���bc1x8# Give the second plot only wireframes of the type x = c���`a
���`cax2���aoa.���`nplot_wireframe���`a(���`aX���`a,���`a ���`aY���`a,���`a ���`aZ���`a,���`a ���`grstride���aoa=���bmia0���`a,���`a ���`gcstride���aoa=���bmib10���`a)���`a
���`cax2���aoa.���`iset_title���`a(���bs2a"���bs2wRow (y) stride set to 0���bs2a"���`a)���`a
���`a
���`cplt���aoa.���`ltight_layout���`a(���`a)���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
`dNone�