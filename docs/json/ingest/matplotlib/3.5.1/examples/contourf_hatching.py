������������bsdxo"""
=================
Contourf Hatching
=================

Demo filled contour plots with hatched patterns.
"""���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���`a
���bc1x=# invent some numbers, turning the x and y arrays into simple���`a
���bc1x7# 2d arrays, which make combining them together easier.���`a
���`ax���`a ���aoa=���`a ���`bnp���aoa.���`hlinspace���`a(���aoa-���bmia3���`a,���`a ���bmia5���`a,���`a ���bmic150���`a)���aoa.���`greshape���`a(���bmia1���`a,���`a ���aoa-���bmia1���`a)���`a
���`ay���`a ���aoa=���`a ���`bnp���aoa.���`hlinspace���`a(���aoa-���bmia3���`a,���`a ���bmia5���`a,���`a ���bmic120���`a)���aoa.���`greshape���`a(���aoa-���bmia1���`a,���`a ���bmia1���`a)���`a
���`az���`a ���aoa=���`a ���`bnp���aoa.���`ccos���`a(���`ax���`a)���`a ���aoa+���`a ���`bnp���aoa.���`csin���`a(���`ay���`a)���`a
���`a
���bc1xA# we no longer need x and y to be 2 dimensional, so flatten them.���`a
���`ax���`a,���`a ���`ay���`a ���aoa=���`a ���`ax���aoa.���`gflatten���`a(���`a)���`a,���`a ���`ay���aoa.���`gflatten���`a(���`a)���`a
���`a
���bc1xO###############################################################################���`a
���bc1x3# Plot 1: the simplest hatched plot with a colorbar���`a
���`a
���`dfig1���`a,���`a ���`cax1���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`a)���`a
���`bcs���`a ���aoa=���`a ���`cax1���aoa.���`hcontourf���`a(���`ax���`a,���`a ���`ay���`a,���`a ���`az���`a,���`a ���`ghatches���aoa=���`a[���bs1a'���bs1a-���bs1a'���`a,���`a ���bs1a'���bs1a/���bs1a'���`a,���`a ���bs1a'���bseb\\���bs1a'���`a,���`a ���bs1a'���bs1b//���bs1a'���`a]���`a,���`a
���`r                  ���`dcmap���aoa=���bs1a'���bs1dgray���bs1a'���`a,���`a ���`fextend���aoa=���bs1a'���bs1dboth���bs1a'���`a,���`a ���`ealpha���aoa=���bmfc0.5���`a)���`a
���`dfig1���aoa.���`hcolorbar���`a(���`bcs���`a)���`a
���`a
���bc1xO###############################################################################���`a
���bc1x7# Plot 2: a plot of hatches without color with a legend���`a
���`a
���`dfig2���`a,���`a ���`cax2���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`a)���`a
���`hn_levels���`a ���aoa=���`a ���bmia6���`a
���`cax2���aoa.���`gcontour���`a(���`ax���`a,���`a ���`ay���`a,���`a ���`az���`a,���`a ���`hn_levels���`a,���`a ���`fcolors���aoa=���bs1a'���bs1eblack���bs1a'���`a,���`a ���`jlinestyles���aoa=���bs1a'���bs1a-���bs1a'���`a)���`a
���`bcs���`a ���aoa=���`a ���`cax2���aoa.���`hcontourf���`a(���`ax���`a,���`a ���`ay���`a,���`a ���`az���`a,���`a ���`hn_levels���`a,���`a ���`fcolors���aoa=���bs1a'���bs1dnone���bs1a'���`a,���`a
���`r                  ���`ghatches���aoa=���`a[���bs1a'���bs1a.���bs1a'���`a,���`a ���bs1a'���bs1a/���bs1a'���`a,���`a ���bs1a'���bseb\\���bs1a'���`a,���`a ���bkcdNone���`a,���`a ���bs1a'���bseb\\���bseb\\���bs1a'���`a,���`a ���bs1a'���bs1a*���bs1a'���`a]���`a,���`a
���`r                  ���`fextend���aoa=���bs1a'���bs1elower���bs1a'���`a)���`a
���`a
���bc1x%# create a legend for the contour set���`a
���`gartists���`a,���`a ���`flabels���`a ���aoa=���`a ���`bcs���aoa.���`olegend_elements���`a(���`jstr_format���aoa=���bs1a'���bsig{:2.1f}���bs1a'���aoa.���`fformat���`a)���`a
���`cax2���aoa.���`flegend���`a(���`gartists���`a,���`a ���`flabels���`a,���`a ���`lhandleheight���aoa=���bmia2���`a,���`a ���`jframealpha���aoa=���bmia1���`a)���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
���`a
���bc1xM#############################################################################���`a
���bc1a#���`a
���bc1x# .. admonition:: References���`a
���bc1a#���`a
���bc1xN#    The use of the following functions, methods, classes and modules is shown���`a
���bc1u#    in this example:���`a
���bc1a#���`a
���bc1xC#    - `matplotlib.axes.Axes.contour` / `matplotlib.pyplot.contour`���`a
���bc1xE#    - `matplotlib.axes.Axes.contourf` / `matplotlib.pyplot.contourf`���`a
���bc1xI#    - `matplotlib.figure.Figure.colorbar` / `matplotlib.pyplot.colorbar`���`a
���bc1xA#    - `matplotlib.axes.Axes.legend` / `matplotlib.pyplot.legend`���`a
���bc1x&#    - `matplotlib.contour.ContourSet`���`a
���bc1x6#    - `matplotlib.contour.ContourSet.legend_elements`���`a
`dNone�