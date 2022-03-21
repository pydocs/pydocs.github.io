��������Q���bsdx�"""
======================
Zoom region inset axes
======================

Example of an inset axes and a rectangle showing where the zoom is located.
"""���`a
���`a
���bkndfrom���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����`a ���bknfimport���`a ���`ecbook���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���`a
���`a
���akcdef���`a ���bnfnget_demo_image���`a(���`a)���`a:���`a
���`d    ���`az���`a ���aoa=���`a ���`ecbook���aoa.���`oget_sample_data���`a(���bs2a"���bs2xaxes_grid/bivariate_normal.npy���bs2a"���`a,���`a ���`gnp_load���aoa=���bkcdTrue���`a)���`a
���`d    ���bc1x# z is a numpy array of 15x15���`a
���`d    ���akfreturn���`a ���`az���`a,���`a ���`a(���aoa-���bmia3���`a,���`a ���bmia4���`a,���`a ���aoa-���bmia4���`a,���`a ���bmia3���`a)���`a
���`a
���`cfig���`a,���`a ���`bax���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`gfigsize���aoa=���`a[���bmia5���`a,���`a ���bmia4���`a]���`a)���`a
���`a
���bc1k# make data���`a
���`aZ���`a,���`a ���`fextent���`a ���aoa=���`a ���`nget_demo_image���`a(���`a)���`a
���`bZ2���`a ���aoa=���`a ���`bnp���aoa.���`ezeros���`a(���`a(���bmic150���`a,���`a ���bmic150���`a)���`a)���`a
���`bny���`a,���`a ���`bnx���`a ���aoa=���`a ���`aZ���aoa.���`eshape���`a
���`bZ2���`a[���bmib30���`a:���bmib30���aoa+���`bny���`a,���`a ���bmib30���`a:���bmib30���aoa+���`bnx���`a]���`a ���aoa=���`a ���`aZ���`a
���`a
���`bax���aoa.���`fimshow���`a(���`bZ2���`a,���`a ���`fextent���aoa=���`fextent���`a,���`a ���`forigin���aoa=���bs2a"���bs2elower���bs2a"���`a)���`a
���`a
���bc1p# inset axes....���`a
���`eaxins���`a ���aoa=���`a ���`bax���aoa.���`jinset_axes���`a(���`a[���bmfc0.5���`a,���`a ���bmfc0.5���`a,���`a ���bmfd0.47���`a,���`a ���bmfd0.47���`a]���`a)���`a
���`eaxins���aoa.���`fimshow���`a(���`bZ2���`a,���`a ���`fextent���aoa=���`fextent���`a,���`a ���`forigin���aoa=���bs2a"���bs2elower���bs2a"���`a)���`a
���bc1x"# sub region of the original image���`a
���`bx1���`a,���`a ���`bx2���`a,���`a ���`by1���`a,���`a ���`by2���`a ���aoa=���`a ���aoa-���bmfc1.5���`a,���`a ���aoa-���bmfc0.9���`a,���`a ���aoa-���bmfc2.5���`a,���`a ���aoa-���bmfc1.9���`a
���`eaxins���aoa.���`hset_xlim���`a(���`bx1���`a,���`a ���`bx2���`a)���`a
���`eaxins���aoa.���`hset_ylim���`a(���`by1���`a,���`a ���`by2���`a)���`a
���`eaxins���aoa.���`oset_xticklabels���`a(���`a[���`a]���`a)���`a
���`eaxins���aoa.���`oset_yticklabels���`a(���`a[���`a]���`a)���`a
���`a
���`bax���aoa.���`sindicate_inset_zoom���`a(���`eaxins���`a,���`a ���`iedgecolor���aoa=���bs2a"���bs2eblack���bs2a"���`a)���`a
���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
���`a
���bc1xM#############################################################################���`a
���bc1a#���`a
���bc1x# .. admonition:: References���`a
���bc1a#���`a
���bc1xN#    The use of the following functions, methods, classes and modules is shown���`a
���bc1u#    in this example:���`a
���bc1a#���`a
���bc1x(#    - `matplotlib.axes.Axes.inset_axes`���`a
���bc1x1#    - `matplotlib.axes.Axes.indicate_inset_zoom`���`a
���bc1x$#    - `matplotlib.axes.Axes.imshow`���`a
`dNone�