������������bsdx�"""
================
Simple ImageGrid
================

Align multiple images using `~mpl_toolkits.axes_grid1.axes_grid.ImageGrid`.
"""���`a
���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���bkndfrom���`a ���bnnlmpl_toolkits���bnna.���bnnjaxes_grid1���`a ���bknfimport���`a ���`iImageGrid���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���`a
���`cim1���`a ���aoa=���`a ���`bnp���aoa.���`farange���`a(���bmic100���`a)���aoa.���`greshape���`a(���`a(���bmib10���`a,���`a ���bmib10���`a)���`a)���`a
���`cim2���`a ���aoa=���`a ���`cim1���aoa.���`aT���`a
���`cim3���`a ���aoa=���`a ���`bnp���aoa.���`fflipud���`a(���`cim1���`a)���`a
���`cim4���`a ���aoa=���`a ���`bnp���aoa.���`ffliplr���`a(���`cim2���`a)���`a
���`a
���`cfig���`a ���aoa=���`a ���`cplt���aoa.���`ffigure���`a(���`gfigsize���aoa=���`a(���bmfb4.���`a,���`a ���bmfb4.���`a)���`a)���`a
���`dgrid���`a ���aoa=���`a ���`iImageGrid���`a(���`cfig���`a,���`a ���bmic111���`a,���`b  ���bc1x# similar to subplot(111)���`a
���`q                 ���`knrows_ncols���aoa=���`a(���bmia2���`a,���`a ���bmia2���`a)���`a,���`b  ���bc1x# creates 2x2 grid of axes���`a
���`q                 ���`haxes_pad���aoa=���bmfc0.1���`a,���`b  ���bc1x# pad between axes in inch.���`a
���`q                 ���`a)���`a
���`a
���akcfor���`a ���`bax���`a,���`a ���`bim���`a ���bowbin���`a ���bnbczip���`a(���`dgrid���`a,���`a ���`a[���`cim1���`a,���`a ���`cim2���`a,���`a ���`cim3���`a,���`a ���`cim4���`a]���`a)���`a:���`a
���`d    ���bc1x+# Iterating over the grid returns the Axes.���`a
���`d    ���`bax���aoa.���`fimshow���`a(���`bim���`a)���`a
���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
`dNone�