��������T���bsdx�"""
========
Viewlims
========

Creates two identical panels.  Zooming in on the right panel will show
a rectangle in the first panel, denoting the zoomed region.
"""���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���bkndfrom���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnngpatches���`a ���bknfimport���`a ���`iRectangle���`a
���`a
���`a
���bc1xB# We just subclass Rectangle so that it can be called with an Axes���`a
���bc1xB# instance, causing the rectangle to update its shape to match the���`a
���bc1t# bounds of the Axes���`a
���akeclass���`a ���bnclUpdatingRect���`a(���`iRectangle���`a)���`a:���`a
���`d    ���akcdef���`a ���bfmh__call__���`a(���bbpdself���`a,���`a ���`bax���`a)���`a:���`a
���`h        ���bbpdself���aoa.���`jset_bounds���`a(���aoa*���`bax���aoa.���`gviewLim���aoa.���`fbounds���`a)���`a
���`h        ���`bax���aoa.���`ffigure���aoa.���`fcanvas���aoa.���`idraw_idle���`a(���`a)���`a
���`a
���`a
���bc1xG# A class that will regenerate a fractal set as we zoom in, so that you���`a
���bc1xL# can actually see the increasing detail.  A box in the left panel will show���`a
���bc1x"# the area to which we are zoomed.���`a
���akeclass���`a ���bncqMandelbrotDisplay���`a:���`a
���`d    ���akcdef���`a ���bfmh__init__���`a(���bbpdself���`a,���`a ���`ah���aoa=���bmic500���`a,���`a ���`aw���aoa=���bmic500���`a,���`a ���`eniter���aoa=���bmib50���`a,���`a ���`fradius���aoa=���bmfb2.���`a,���`a ���`epower���aoa=���bmia2���`a)���`a:���`a
���`h        ���bbpdself���aoa.���`fheight���`a ���aoa=���`a ���`ah���`a
���`h        ���bbpdself���aoa.���`ewidth���`a ���aoa=���`a ���`aw���`a
���`h        ���bbpdself���aoa.���`eniter���`a ���aoa=���`a ���`eniter���`a
���`h        ���bbpdself���aoa.���`fradius���`a ���aoa=���`a ���`fradius���`a
���`h        ���bbpdself���aoa.���`epower���`a ���aoa=���`a ���`epower���`a
���`a
���`d    ���akcdef���`a ���bnfmcompute_image���`a(���bbpdself���`a,���`a ���`fxstart���`a,���`a ���`dxend���`a,���`a ���`fystart���`a,���`a ���`dyend���`a)���`a:���`a
���`h        ���bbpdself���aoa.���`ax���`a ���aoa=���`a ���`bnp���aoa.���`hlinspace���`a(���`fxstart���`a,���`a ���`dxend���`a,���`a ���bbpdself���aoa.���`ewidth���`a)���`a
���`h        ���bbpdself���aoa.���`ay���`a ���aoa=���`a ���`bnp���aoa.���`hlinspace���`a(���`fystart���`a,���`a ���`dyend���`a,���`a ���bbpdself���aoa.���`fheight���`a)���aoa.���`greshape���`a(���aoa-���bmia1���`a,���`a ���bmia1���`a)���`a
���`h        ���`ac���`a ���aoa=���`a ���bbpdself���aoa.���`ax���`a ���aoa+���`a ���bmfc1.0���`aj���`a ���aoa*���`a ���bbpdself���aoa.���`ay���`a
���`h        ���`nthreshold_time���`a ���aoa=���`a ���`bnp���aoa.���`ezeros���`a(���`a(���bbpdself���aoa.���`fheight���`a,���`a ���bbpdself���aoa.���`ewidth���`a)���`a)���`a
���`h        ���`az���`a ���aoa=���`a ���`bnp���aoa.���`ezeros���`a(���`nthreshold_time���aoa.���`eshape���`a,���`a ���`edtype���aoa=���bnbgcomplex���`a)���`a
���`h        ���`dmask���`a ���aoa=���`a ���`bnp���aoa.���`dones���`a(���`nthreshold_time���aoa.���`eshape���`a,���`a ���`edtype���aoa=���bnbdbool���`a)���`a
���`h        ���akcfor���`a ���`ai���`a ���bowbin���`a ���bnberange���`a(���bbpdself���aoa.���`eniter���`a)���`a:���`a
���`l            ���`az���`a[���`dmask���`a]���`a ���aoa=���`a ���`az���`a[���`dmask���`a]���aoa*���aoa*���bbpdself���aoa.���`epower���`a ���aoa+���`a ���`ac���`a[���`dmask���`a]���`a
���`l            ���`dmask���`a ���aoa=���`a ���`a(���`bnp���aoa.���`cabs���`a(���`az���`a)���`a ���aoa<���`a ���bbpdself���aoa.���`fradius���`a)���`a
���`l            ���`nthreshold_time���`a ���aoa+���aoa=���`a ���`dmask���`a
���`h        ���akfreturn���`a ���`nthreshold_time���`a
���`a
���`d    ���akcdef���`a ���bnfiax_update���`a(���bbpdself���`a,���`a ���`bax���`a)���`a:���`a
���`h        ���`bax���aoa.���`pset_autoscale_on���`a(���bkceFalse���`a)���`b  ���bc1x# Otherwise, infinite loop���`a
���`h        ���bc1xB# Get the number of points from the number of pixels in the window���`a
���`h        ���bbpdself���aoa.���`ewidth���`a,���`a ���bbpdself���aoa.���`fheight���`a ���aoa=���`a ���`b\
���`l            ���`bnp���aoa.���`eround���`a(���`bax���aoa.���`epatch���aoa.���`qget_window_extent���`a(���`a)���aoa.���`dsize���`a)���aoa.���`fastype���`a(���bnbcint���`a)���`a
���`h        ���bc1x # Get the range for the new area���`a
���`h        ���`bvl���`a ���aoa=���`a ���`bax���aoa.���`gviewLim���`a
���`h        ���`fextent���`a ���aoa=���`a ���`bvl���aoa.���`bx0���`a,���`a ���`bvl���aoa.���`bx1���`a,���`a ���`bvl���aoa.���`by0���`a,���`a ���`bvl���aoa.���`by1���`a
���`h        ���bc1x6# Update the image object with our new data and extent���`a
���`h        ���`bim���`a ���aoa=���`a ���`bax���aoa.���`fimages���`a[���aoa-���bmia1���`a]���`a
���`h        ���`bim���aoa.���`hset_data���`a(���bbpdself���aoa.���`mcompute_image���`a(���aoa*���`fextent���`a)���`a)���`a
���`h        ���`bim���aoa.���`jset_extent���`a(���`fextent���`a)���`a
���`h        ���`bax���aoa.���`ffigure���aoa.���`fcanvas���aoa.���`idraw_idle���`a(���`a)���`a
���`a
���`a
���`bmd���`a ���aoa=���`a ���`qMandelbrotDisplay���`a(���`a)���`a
���`aZ���`a ���aoa=���`a ���`bmd���aoa.���`mcompute_image���`a(���aoa-���bmfb2.���`a,���`a ���bmfc0.5���`a,���`a ���aoa-���bmfd1.25���`a,���`a ���bmfd1.25���`a)���`a
���`a
���`dfig1���`a,���`a ���`a(���`cax1���`a,���`a ���`cax2���`a)���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���bmia1���`a,���`a ���bmia2���`a)���`a
���`cax1���aoa.���`fimshow���`a(���`aZ���`a,���`a ���`forigin���aoa=���bs1a'���bs1elower���bs1a'���`a,���`a
���`k           ���`fextent���aoa=���`a(���`bmd���aoa.���`ax���aoa.���`cmin���`a(���`a)���`a,���`a ���`bmd���aoa.���`ax���aoa.���`cmax���`a(���`a)���`a,���`a ���`bmd���aoa.���`ay���aoa.���`cmin���`a(���`a)���`a,���`a ���`bmd���aoa.���`ay���aoa.���`cmax���`a(���`a)���`a)���`a)���`a
���`cax2���aoa.���`fimshow���`a(���`aZ���`a,���`a ���`forigin���aoa=���bs1a'���bs1elower���bs1a'���`a,���`a
���`k           ���`fextent���aoa=���`a(���`bmd���aoa.���`ax���aoa.���`cmin���`a(���`a)���`a,���`a ���`bmd���aoa.���`ax���aoa.���`cmax���`a(���`a)���`a,���`a ���`bmd���aoa.���`ay���aoa.���`cmin���`a(���`a)���`a,���`a ���`bmd���aoa.���`ay���aoa.���`cmax���`a(���`a)���`a)���`a)���`a
���`a
���`drect���`a ���aoa=���`a ���`lUpdatingRect���`a(���`a
���`d    ���`a[���bmia0���`a,���`a ���bmia0���`a]���`a,���`a ���bmia0���`a,���`a ���bmia0���`a,���`a ���`ifacecolor���aoa=���bs1a'���bs1dnone���bs1a'���`a,���`a ���`iedgecolor���aoa=���bs1a'���bs1eblack���bs1a'���`a,���`a ���`ilinewidth���aoa=���bmfc1.0���`a)���`a
���`drect���aoa.���`jset_bounds���`a(���aoa*���`cax2���aoa.���`gviewLim���aoa.���`fbounds���`a)���`a
���`cax1���aoa.���`iadd_patch���`a(���`drect���`a)���`a
���`a
���bc1x&# Connect for changing the view limits���`a
���`cax2���aoa.���`icallbacks���aoa.���`gconnect���`a(���bs1a'���bs1lxlim_changed���bs1a'���`a,���`a ���`drect���`a)���`a
���`cax2���aoa.���`icallbacks���aoa.���`gconnect���`a(���bs1a'���bs1lylim_changed���bs1a'���`a,���`a ���`drect���`a)���`a
���`a
���`cax2���aoa.���`icallbacks���aoa.���`gconnect���`a(���bs1a'���bs1lxlim_changed���bs1a'���`a,���`a ���`bmd���aoa.���`iax_update���`a)���`a
���`cax2���aoa.���`icallbacks���aoa.���`gconnect���`a(���bs1a'���bs1lylim_changed���bs1a'���`a,���`a ���`bmd���aoa.���`iax_update���`a)���`a
���`cax2���aoa.���`iset_title���`a(���bs2a"���bs2iZoom here���bs2a"���`a)���`a
���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
`dNone�