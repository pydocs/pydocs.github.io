������������bsdx�"""
==================
Simple ImageGrid 2
==================

Align multiple images of different sizes using
`~mpl_toolkits.axes_grid1.axes_grid.ImageGrid`.
"""���`a
���`a
���bkndfrom���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����`a ���bknfimport���`a ���`ecbook���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���bkndfrom���`a ���bnnlmpl_toolkits���bnna.���bnnjaxes_grid1���`a ���bknfimport���`a ���`iImageGrid���`a
���`a
���`a
���`cfig���`a ���aoa=���`a ���`cplt���aoa.���`ffigure���`a(���`gfigsize���aoa=���`a(���bmfc5.5���`a,���`a ���bmfc3.5���`a)���`a)���`a
���`dgrid���`a ���aoa=���`a ���`iImageGrid���`a(���`cfig���`a,���`a ���bmic111���`a,���`b  ���bc1x# similar to subplot(111)���`a
���`q                 ���`knrows_ncols���aoa=���`a(���bmia1���`a,���`a ���bmia3���`a)���`a,���`a
���`q                 ���`haxes_pad���aoa=���bmfc0.1���`a,���`a
���`q                 ���`jlabel_mode���aoa=���bs2a"���bs2aL���bs2a"���`a,���`a
���`q                 ���`a)���`a
���`a
���bc1l# demo image���`a
���`aZ���`a ���aoa=���`a ���`ecbook���aoa.���`oget_sample_data���`a(���bs2a"���bs2xaxes_grid/bivariate_normal.npy���bs2a"���`a,���`a ���`gnp_load���aoa=���bkcdTrue���`a)���`a
���`cim1���`a ���aoa=���`a ���`aZ���`a
���`cim2���`a ���aoa=���`a ���`aZ���`a[���`a:���`a,���`a ���`a:���bmib10���`a]���`a
���`cim3���`a ���aoa=���`a ���`aZ���`a[���`a:���`a,���`a ���bmib10���`a:���`a]���`a
���`dvmin���`a,���`a ���`dvmax���`a ���aoa=���`a ���`aZ���aoa.���`cmin���`a(���`a)���`a,���`a ���`aZ���aoa.���`cmax���`a(���`a)���`a
���akcfor���`a ���`bax���`a,���`a ���`bim���`a ���bowbin���`a ���bnbczip���`a(���`dgrid���`a,���`a ���`a[���`cim1���`a,���`a ���`cim2���`a,���`a ���`cim3���`a]���`a)���`a:���`a
���`d    ���`bax���aoa.���`fimshow���`a(���`bim���`a,���`a ���`forigin���aoa=���bs2a"���bs2elower���bs2a"���`a,���`a ���`dvmin���aoa=���`dvmin���`a,���`a ���`dvmax���aoa=���`dvmax���`a)���`a
���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
`dNone�