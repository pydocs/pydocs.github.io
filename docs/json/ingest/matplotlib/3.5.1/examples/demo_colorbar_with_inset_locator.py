��������4���bsdy%"""
==============================================================
Controlling the position and size of colorbars with Inset Axes
==============================================================

This example shows how to control the position, height, and width of
colorbars using `~mpl_toolkits.axes_grid1.inset_locator.inset_axes`.

Controlling the placement of the inset axes is done similarly as that of the
legend: either by providing a location option ("upper right", "best", ...), or
by providing a locator with respect to the parent bbox.

"""���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���`a
���bkndfrom���`a ���bnnlmpl_toolkits���bnna.���bnnjaxes_grid1���bnna.���bnnminset_locator���`a ���bknfimport���`a ���`jinset_axes���`a
���`a
���`cfig���`a,���`a ���`a(���`cax1���`a,���`a ���`cax2���`a)���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���bmia1���`a,���`a ���bmia2���`a,���`a ���`gfigsize���aoa=���`a[���bmia6���`a,���`a ���bmia3���`a]���`a)���`a
���`a
���`faxins1���`a ���aoa=���`a ���`jinset_axes���`a(���`cax1���`a,���`a
���`t                    ���`ewidth���aoa=���bs2a"���bs2b50���bs2a%���bs2a"���`a,���`b  ���bc1x"# width = 50% of parent_bbox width���`a
���`t                    ���`fheight���aoa=���bs2a"���bs2a5���bs2a%���bs2a"���`a,���`b  ���bc1m# height : 5%���`a
���`t                    ���`cloc���aoa=���bs1a'���bs1kupper right���bs1a'���`a)���`a
���`a
���`cim1���`a ���aoa=���`a ���`cax1���aoa.���`fimshow���`a(���`a[���`a[���bmia1���`a,���`a ���bmia2���`a]���`a,���`a ���`a[���bmia2���`a,���`a ���bmia3���`a]���`a]���`a)���`a
���`cfig���aoa.���`hcolorbar���`a(���`cim1���`a,���`a ���`ccax���aoa=���`faxins1���`a,���`a ���`korientation���aoa=���bs2a"���bs2jhorizontal���bs2a"���`a,���`a ���`eticks���aoa=���`a[���bmia1���`a,���`a ���bmia2���`a,���`a ���bmia3���`a]���`a)���`a
���`faxins1���aoa.���`exaxis���aoa.���`rset_ticks_position���`a(���bs2a"���bs2fbottom���bs2a"���`a)���`a
���`a
���`eaxins���`a ���aoa=���`a ���`jinset_axes���`a(���`cax2���`a,���`a
���`s                   ���`ewidth���aoa=���bs2a"���bs2a5���bs2a%���bs2a"���`a,���`b  ���bc1x!# width = 5% of parent_bbox width���`a
���`s                   ���`fheight���aoa=���bs2a"���bs2b50���bs2a%���bs2a"���`a,���`b  ���bc1n# height : 50%���`a
���`s                   ���`cloc���aoa=���bs1a'���bs1jlower left���bs1a'���`a,���`a
���`s                   ���`nbbox_to_anchor���aoa=���`a(���bmfd1.05���`a,���`a ���bmfb0.���`a,���`a ���bmia1���`a,���`a ���bmia1���`a)���`a,���`a
���`s                   ���`nbbox_transform���aoa=���`cax2���aoa.���`itransAxes���`a,���`a
���`s                   ���`iborderpad���aoa=���bmia0���`a,���`a
���`s                   ���`a)���`a
���`a
���bc1xG# Controlling the placement of the inset axes is basically same as that���`a
���bc1xC# of the legend.  you may want to play with the borderpad value and���`a
���bc1x # the bbox_to_anchor coordinate.���`a
���`a
���`bim���`a ���aoa=���`a ���`cax2���aoa.���`fimshow���`a(���`a[���`a[���bmia1���`a,���`a ���bmia2���`a]���`a,���`a ���`a[���bmia2���`a,���`a ���bmia3���`a]���`a]���`a)���`a
���`cfig���aoa.���`hcolorbar���`a(���`bim���`a,���`a ���`ccax���aoa=���`eaxins���`a,���`a ���`eticks���aoa=���`a[���bmia1���`a,���`a ���bmia2���`a,���`a ���bmia3���`a]���`a)���`a
���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
`dNone�