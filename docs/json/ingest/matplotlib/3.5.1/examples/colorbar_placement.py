������������bsdy"""
=================
Placing Colorbars
=================

Colorbars indicate the quantitative extent of image data.  Placing in
a figure is non-trivial because room needs to be made for them.

The simplest case is just attaching a colorbar to each axes:
"""���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���`a
���`a
���bc1x)# Fixing random state for reproducibility���`a
���`bnp���aoa.���`frandom���aoa.���`dseed���`a(���bmih19680801���`a)���`a
���`a
���`cfig���`a,���`a ���`caxs���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���bmia2���`a,���`a ���bmia2���`a)���`a
���`ecmaps���`a ���aoa=���`a ���`a[���bs1a'���bs1fRdBu_r���bs1a'���`a,���`a ���bs1a'���bs1gviridis���bs1a'���`a]���`a
���akcfor���`a ���`ccol���`a ���bowbin���`a ���bnberange���`a(���bmia2���`a)���`a:���`a
���`d    ���akcfor���`a ���`crow���`a ���bowbin���`a ���bnberange���`a(���bmia2���`a)���`a:���`a
���`h        ���`bax���`a ���aoa=���`a ���`caxs���`a[���`crow���`a,���`a ���`ccol���`a]���`a
���`h        ���`cpcm���`a ���aoa=���`a ���`bax���aoa.���`jpcolormesh���`a(���`bnp���aoa.���`frandom���aoa.���`frandom���`a(���`a(���bmib20���`a,���`a ���bmib20���`a)���`a)���`a ���aoa*���`a ���`a(���`ccol���`a ���aoa+���`a ���bmia1���`a)���`a,���`a
���`x                            ���`dcmap���aoa=���`ecmaps���`a[���`ccol���`a]���`a)���`a
���`h        ���`cfig���aoa.���`hcolorbar���`a(���`cpcm���`a,���`a ���`bax���aoa=���`bax���`a)���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
���`a
���bc1xF######################################################################���`a
���bc1xD# The first column has the same type of data in both rows, so it may���`a
���bc1x=# be desirable to combine the colorbar which we do by calling���`a
���bc1xB# `.Figure.colorbar` with a list of axes instead of a single axes.���`a
���`a
���`cfig���`a,���`a ���`caxs���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���bmia2���`a,���`a ���bmia2���`a)���`a
���`ecmaps���`a ���aoa=���`a ���`a[���bs1a'���bs1fRdBu_r���bs1a'���`a,���`a ���bs1a'���bs1gviridis���bs1a'���`a]���`a
���akcfor���`a ���`ccol���`a ���bowbin���`a ���bnberange���`a(���bmia2���`a)���`a:���`a
���`d    ���akcfor���`a ���`crow���`a ���bowbin���`a ���bnberange���`a(���bmia2���`a)���`a:���`a
���`h        ���`bax���`a ���aoa=���`a ���`caxs���`a[���`crow���`a,���`a ���`ccol���`a]���`a
���`h        ���`cpcm���`a ���aoa=���`a ���`bax���aoa.���`jpcolormesh���`a(���`bnp���aoa.���`frandom���aoa.���`frandom���`a(���`a(���bmib20���`a,���`a ���bmib20���`a)���`a)���`a ���aoa*���`a ���`a(���`ccol���`a ���aoa+���`a ���bmia1���`a)���`a,���`a
���`x                            ���`dcmap���aoa=���`ecmaps���`a[���`ccol���`a]���`a)���`a
���`d    ���`cfig���aoa.���`hcolorbar���`a(���`cpcm���`a,���`a ���`bax���aoa=���`caxs���`a[���`a:���`a,���`a ���`ccol���`a]���`a,���`a ���`fshrink���aoa=���bmfc0.6���`a)���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
���`a
���bc1xF######################################################################���`a
���bc1xA# Relatively complicated colorbar layouts are possible using this���`a
���bc1x9# paradigm.  Note that this example works far better with���`a
���bc1x# ``constrained_layout=True``���`a
���`a
���`cfig���`a,���`a ���`caxs���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���bmia3���`a,���`a ���bmia3���`a,���`a ���`rconstrained_layout���aoa=���bkcdTrue���`a)���`a
���akcfor���`a ���`bax���`a ���bowbin���`a ���`caxs���aoa.���`dflat���`a:���`a
���`d    ���`cpcm���`a ���aoa=���`a ���`bax���aoa.���`jpcolormesh���`a(���`bnp���aoa.���`frandom���aoa.���`frandom���`a(���`a(���bmib20���`a,���`a ���bmib20���`a)���`a)���`a)���`a
���`a
���`cfig���aoa.���`hcolorbar���`a(���`cpcm���`a,���`a ���`bax���aoa=���`caxs���`a[���bmia0���`a,���`a ���`a:���bmia2���`a]���`a,���`a ���`fshrink���aoa=���bmfc0.6���`a,���`a ���`hlocation���aoa=���bs1a'���bs1fbottom���bs1a'���`a)���`a
���`cfig���aoa.���`hcolorbar���`a(���`cpcm���`a,���`a ���`bax���aoa=���`a[���`caxs���`a[���bmia0���`a,���`a ���bmia2���`a]���`a]���`a,���`a ���`hlocation���aoa=���bs1a'���bs1fbottom���bs1a'���`a)���`a
���`cfig���aoa.���`hcolorbar���`a(���`cpcm���`a,���`a ���`bax���aoa=���`caxs���`a[���bmia1���`a:���`a,���`a ���`a:���`a]���`a,���`a ���`hlocation���aoa=���bs1a'���bs1eright���bs1a'���`a,���`a ���`fshrink���aoa=���bmfc0.6���`a)���`a
���`cfig���aoa.���`hcolorbar���`a(���`cpcm���`a,���`a ���`bax���aoa=���`a[���`caxs���`a[���bmia2���`a,���`a ���bmia1���`a]���`a]���`a,���`a ���`hlocation���aoa=���bs1a'���bs1dleft���bs1a'���`a)���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
���`a
���bc1xF######################################################################���`a
���bc1x(# Colorbars with fixed-aspect-ratio axes���`a
���bc1x(# ======================================���`a
���bc1a#���`a
���bc1xH# Placing colorbars for axes with a fixed aspect ratio pose a particular���`a
���bc1xG# challenge as the parent axes changes size depending on the data view.���`a
���`a
���`cfig���`a,���`a ���`caxs���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���bmia2���`a,���`a ���bmia2���`a,���`b  ���`rconstrained_layout���aoa=���bkcdTrue���`a)���`a
���`ecmaps���`a ���aoa=���`a ���`a[���bs1a'���bs1fRdBu_r���bs1a'���`a,���`a ���bs1a'���bs1gviridis���bs1a'���`a]���`a
���akcfor���`a ���`ccol���`a ���bowbin���`a ���bnberange���`a(���bmia2���`a)���`a:���`a
���`d    ���akcfor���`a ���`crow���`a ���bowbin���`a ���bnberange���`a(���bmia2���`a)���`a:���`a
���`h        ���`bax���`a ���aoa=���`a ���`caxs���`a[���`crow���`a,���`a ���`ccol���`a]���`a
���`h        ���`cpcm���`a ���aoa=���`a ���`bax���aoa.���`jpcolormesh���`a(���`bnp���aoa.���`frandom���aoa.���`frandom���`a(���`a(���bmib20���`a,���`a ���bmib20���`a)���`a)���`a ���aoa*���`a ���`a(���`ccol���`a ���aoa+���`a ���bmia1���`a)���`a,���`a
���`x                            ���`dcmap���aoa=���`ecmaps���`a[���`ccol���`a]���`a)���`a
���`h        ���akbif���`a ���`ccol���`a ���aob==���`a ���bmia0���`a:���`a
���`l            ���`bax���aoa.���`jset_aspect���`a(���bmia2���`a)���`a
���`h        ���akdelse���`a:���`a
���`l            ���`bax���aoa.���`jset_aspect���`a(���bmia1���aoa/���bmia2���`a)���`a
���`h        ���akbif���`a ���`crow���`a ���aob==���`a ���bmia1���`a:���`a
���`l            ���`cfig���aoa.���`hcolorbar���`a(���`cpcm���`a,���`a ���`bax���aoa=���`bax���`a,���`a ���`fshrink���aoa=���bmfc0.6���`a)���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
���`a
���bc1xF######################################################################���`a
���bc1xI# One way around this issue is to use an `.Axes.inset_axes` to locate the���`a
���bc1xF# axes in axes coordinates.  Note that if you zoom in on the axes, and���`a
���bc1xG# change the shape of the axes, the colorbar will also change position.���`a
���`a
���`cfig���`a,���`a ���`caxs���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���bmia2���`a,���`a ���bmia2���`a,���`a ���`rconstrained_layout���aoa=���bkcdTrue���`a)���`a
���`ecmaps���`a ���aoa=���`a ���`a[���bs1a'���bs1fRdBu_r���bs1a'���`a,���`a ���bs1a'���bs1gviridis���bs1a'���`a]���`a
���akcfor���`a ���`ccol���`a ���bowbin���`a ���bnberange���`a(���bmia2���`a)���`a:���`a
���`d    ���akcfor���`a ���`crow���`a ���bowbin���`a ���bnberange���`a(���bmia2���`a)���`a:���`a
���`h        ���`bax���`a ���aoa=���`a ���`caxs���`a[���`crow���`a,���`a ���`ccol���`a]���`a
���`h        ���`cpcm���`a ���aoa=���`a ���`bax���aoa.���`jpcolormesh���`a(���`bnp���aoa.���`frandom���aoa.���`frandom���`a(���`a(���bmib20���`a,���`a ���bmib20���`a)���`a)���`a ���aoa*���`a ���`a(���`ccol���`a ���aoa+���`a ���bmia1���`a)���`a,���`a
���`x                            ���`dcmap���aoa=���`ecmaps���`a[���`ccol���`a]���`a)���`a
���`h        ���akbif���`a ���`ccol���`a ���aob==���`a ���bmia0���`a:���`a
���`l            ���`bax���aoa.���`jset_aspect���`a(���bmia2���`a)���`a
���`h        ���akdelse���`a:���`a
���`l            ���`bax���aoa.���`jset_aspect���`a(���bmia1���aoa/���bmia2���`a)���`a
���`h        ���akbif���`a ���`crow���`a ���aob==���`a ���bmia1���`a:���`a
���`l            ���`ccax���`a ���aoa=���`a ���`bax���aoa.���`jinset_axes���`a(���`a[���bmfd1.04���`a,���`a ���bmfc0.2���`a,���`a ���bmfd0.05���`a,���`a ���bmfc0.6���`a]���`a,���`a ���`itransform���aoa=���`bax���aoa.���`itransAxes���`a)���`a
���`l            ���`cfig���aoa.���`hcolorbar���`a(���`cpcm���`a,���`a ���`bax���aoa=���`bax���`a,���`a ���`ccax���aoa=���`ccax���`a)���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
`dNone�