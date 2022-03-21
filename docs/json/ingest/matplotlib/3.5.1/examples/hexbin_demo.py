��������J���bsdx�"""
=====================
Hexagonal binned plot
=====================

`~.Axes.hexbin` is a 2D histogram plot, in which the bins are hexagons and
the color represents the number of data points within each bin.
"""���`a
���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���`a
���bc1x)# Fixing random state for reproducibility���`a
���`bnp���aoa.���`frandom���aoa.���`dseed���`a(���bmih19680801���`a)���`a
���`a
���`an���`a ���aoa=���`a ���bmig100_000���`a
���`ax���`a ���aoa=���`a ���`bnp���aoa.���`frandom���aoa.���`ostandard_normal���`a(���`an���`a)���`a
���`ay���`a ���aoa=���`a ���bmfc2.0���`a ���aoa+���`a ���bmfc3.0���`a ���aoa*���`a ���`ax���`a ���aoa+���`a ���bmfc4.0���`a ���aoa*���`a ���`bnp���aoa.���`frandom���aoa.���`ostandard_normal���`a(���`an���`a)���`a
���`dxlim���`a ���aoa=���`a ���`ax���aoa.���`cmin���`a(���`a)���`a,���`a ���`ax���aoa.���`cmax���`a(���`a)���`a
���`dylim���`a ���aoa=���`a ���`ay���aoa.���`cmin���`a(���`a)���`a,���`a ���`ay���aoa.���`cmax���`a(���`a)���`a
���`a
���`cfig���`a,���`a ���`a(���`cax0���`a,���`a ���`cax1���`a)���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`encols���aoa=���bmia2���`a,���`a ���`fsharey���aoa=���bkcdTrue���`a,���`a ���`gfigsize���aoa=���`a(���bmia9���`a,���`a ���bmia4���`a)���`a)���`a
���`a
���`bhb���`a ���aoa=���`a ���`cax0���aoa.���`fhexbin���`a(���`ax���`a,���`a ���`ay���`a,���`a ���`hgridsize���aoa=���bmib50���`a,���`a ���`dcmap���aoa=���bs1a'���bs1ginferno���bs1a'���`a)���`a
���`cax0���aoa.���`cset���`a(���`dxlim���aoa=���`dxlim���`a,���`a ���`dylim���aoa=���`dylim���`a)���`a
���`cax0���aoa.���`iset_title���`a(���bs2a"���bs2oHexagon binning���bs2a"���`a)���`a
���`bcb���`a ���aoa=���`a ���`cfig���aoa.���`hcolorbar���`a(���`bhb���`a,���`a ���`bax���aoa=���`cax0���`a,���`a ���`elabel���aoa=���bs1a'���bs1fcounts���bs1a'���`a)���`a
���`a
���`bhb���`a ���aoa=���`a ���`cax1���aoa.���`fhexbin���`a(���`ax���`a,���`a ���`ay���`a,���`a ���`hgridsize���aoa=���bmib50���`a,���`a ���`dbins���aoa=���bs1a'���bs1clog���bs1a'���`a,���`a ���`dcmap���aoa=���bs1a'���bs1ginferno���bs1a'���`a)���`a
���`cax1���aoa.���`cset���`a(���`dxlim���aoa=���`dxlim���`a,���`a ���`dylim���aoa=���`dylim���`a)���`a
���`cax1���aoa.���`iset_title���`a(���bs2a"���bs2vWith a log color scale���bs2a"���`a)���`a
���`bcb���`a ���aoa=���`a ���`cfig���aoa.���`hcolorbar���`a(���`bhb���`a,���`a ���`bax���aoa=���`cax1���`a,���`a ���`elabel���aoa=���bs1a'���bs1hlog10(N)���bs1a'���`a)���`a
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
���bc1xA#    - `matplotlib.axes.Axes.hexbin` / `matplotlib.pyplot.hexbin`���`a
`dNone�