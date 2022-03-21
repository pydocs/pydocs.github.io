��������/���bsdx�"""
===============
Resampling Data
===============

Downsampling lowers the sample rate or sample size of a signal. In
this tutorial, the signal is downsampled when the plot is adjusted
through dragging and zooming.
"""���`a
���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���`a
���`a
���bc1xB# A class that will downsample the data and recompute when zoomed.���`a
���akeclass���`a ���bncvDataDisplayDownsampler���`a:���`a
���`d    ���akcdef���`a ���bfmh__init__���`a(���bbpdself���`a,���`a ���`exdata���`a,���`a ���`eydata���`a)���`a:���`a
���`h        ���bbpdself���aoa.���`iorigYData���`a ���aoa=���`a ���`eydata���`a
���`h        ���bbpdself���aoa.���`iorigXData���`a ���aoa=���`a ���`exdata���`a
���`h        ���bbpdself���aoa.���`jmax_points���`a ���aoa=���`a ���bmib50���`a
���`h        ���bbpdself���aoa.���`edelta���`a ���aoa=���`a ���`exdata���`a[���aoa-���bmia1���`a]���`a ���aoa-���`a ���`exdata���`a[���bmia0���`a]���`a
���`a
���`d    ���akcdef���`a ���bnfjdownsample���`a(���bbpdself���`a,���`a ���`fxstart���`a,���`a ���`dxend���`a)���`a:���`a
���`h        ���bc1x"# get the points in the view range���`a
���`h        ���`dmask���`a ���aoa=���`a ���`a(���bbpdself���aoa.���`iorigXData���`a ���aoa>���`a ���`fxstart���`a)���`a ���aoa&���`a ���`a(���bbpdself���aoa.���`iorigXData���`a ���aoa<���`a ���`dxend���`a)���`a
���`h        ���bc1x9# dilate the mask by one to catch the points just outside���`a
���`h        ���bc1x,# of the view range to not truncate the line���`a
���`h        ���`dmask���`a ���aoa=���`a ���`bnp���aoa.���`hconvolve���`a(���`a[���bmia1���`a,���`a ���bmia1���`a,���`a ���bmia1���`a]���`a,���`a ���`dmask���`a,���`a ���`dmode���aoa=���bs1a'���bs1dsame���bs1a'���`a)���aoa.���`fastype���`a(���bnbdbool���`a)���`a
���`h        ���bc1x"# sort out how many points to drop���`a
���`h        ���`eratio���`a ���aoa=���`a ���bnbcmax���`a(���`bnp���aoa.���`csum���`a(���`dmask���`a)���`a ���aoa/���aoa/���`a ���bbpdself���aoa.���`jmax_points���`a,���`a ���bmia1���`a)���`a
���`a
���`h        ���bc1k# mask data���`a
���`h        ���`exdata���`a ���aoa=���`a ���bbpdself���aoa.���`iorigXData���`a[���`dmask���`a]���`a
���`h        ���`eydata���`a ���aoa=���`a ���bbpdself���aoa.���`iorigYData���`a[���`dmask���`a]���`a
���`a
���`h        ���bc1q# downsample data���`a
���`h        ���`exdata���`a ���aoa=���`a ���`exdata���`a[���`a:���`a:���`eratio���`a]���`a
���`h        ���`eydata���`a ���aoa=���`a ���`eydata���`a[���`a:���`a:���`eratio���`a]���`a
���`a
���`h        ���bnbeprint���`a(���bs2a"���bs2fusing ���bsib{}���bs2d of ���bsib{}���bs2o visible points���bs2a"���aoa.���`fformat���`a(���bnbclen���`a(���`eydata���`a)���`a,���`a ���`bnp���aoa.���`csum���`a(���`dmask���`a)���`a)���`a)���`a
���`a
���`h        ���akfreturn���`a ���`exdata���`a,���`a ���`eydata���`a
���`a
���`d    ���akcdef���`a ���bnffupdate���`a(���bbpdself���`a,���`a ���`bax���`a)���`a:���`a
���`h        ���bc1q# Update the line���`a
���`h        ���`dlims���`a ���aoa=���`a ���`bax���aoa.���`gviewLim���`a
���`h        ���akbif���`a ���bnbcabs���`a(���`dlims���aoa.���`ewidth���`a ���aoa-���`a ���bbpdself���aoa.���`edelta���`a)���`a ���aoa>���`a ���bmfd1e-8���`a:���`a
���`l            ���bbpdself���aoa.���`edelta���`a ���aoa=���`a ���`dlims���aoa.���`ewidth���`a
���`l            ���`fxstart���`a,���`a ���`dxend���`a ���aoa=���`a ���`dlims���aoa.���`iintervalx���`a
���`l            ���bbpdself���aoa.���`dline���aoa.���`hset_data���`a(���aoa*���bbpdself���aoa.���`jdownsample���`a(���`fxstart���`a,���`a ���`dxend���`a)���`a)���`a
���`l            ���`bax���aoa.���`ffigure���aoa.���`fcanvas���aoa.���`idraw_idle���`a(���`a)���`a
���`a
���`a
���bc1q# Create a signal���`a
���`exdata���`a ���aoa=���`a ���`bnp���aoa.���`hlinspace���`a(���bmib16���`a,���`a ���bmic365���`a,���`a ���`a(���bmic365���aoa-���bmib16���`a)���aoa*���bmia4���`a)���`a
���`eydata���`a ���aoa=���`a ���`bnp���aoa.���`csin���`a(���bmia2���aoa*���`bnp���aoa.���`bpi���aoa*���`exdata���aoa/���bmic153���`a)���`a ���aoa+���`a ���`bnp���aoa.���`ccos���`a(���bmia2���aoa*���`bnp���aoa.���`bpi���aoa*���`exdata���aoa/���bmic127���`a)���`a
���`a
���`ad���`a ���aoa=���`a ���`vDataDisplayDownsampler���`a(���`exdata���`a,���`a ���`eydata���`a)���`a
���`a
���`cfig���`a,���`a ���`bax���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`a)���`a
���`a
���bc1r# Hook up the line���`a
���`ad���aoa.���`dline���`a,���`a ���aoa=���`a ���`bax���aoa.���`dplot���`a(���`exdata���`a,���`a ���`eydata���`a,���`a ���bs1a'���bs1bo-���bs1a'���`a)���`a
���`bax���aoa.���`pset_autoscale_on���`a(���bkceFalse���`a)���`b  ���bc1x# Otherwise, infinite loop���`a
���`a
���bc1x&# Connect for changing the view limits���`a
���`bax���aoa.���`icallbacks���aoa.���`gconnect���`a(���bs1a'���bs1lxlim_changed���bs1a'���`a,���`a ���`ad���aoa.���`fupdate���`a)���`a
���`bax���aoa.���`hset_xlim���`a(���bmib16���`a,���`a ���bmic365���`a)���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
`dNone�