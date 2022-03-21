������������bsdx�"""
=============
Span Selector
=============

The SpanSelector is a mouse widget to select a xmin/xmax range and plot the
detail view of the selected region in the lower axes
"""���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���bkndfrom���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnngwidgets���`a ���bknfimport���`a ���`lSpanSelector���`a
���`a
���bc1x)# Fixing random state for reproducibility���`a
���`bnp���aoa.���`frandom���aoa.���`dseed���`a(���bmih19680801���`a)���`a
���`a
���`cfig���`a,���`a ���`a(���`cax1���`a,���`a ���`cax2���`a)���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���bmia2���`a,���`a ���`gfigsize���aoa=���`a(���bmia8���`a,���`a ���bmia6���`a)���`a)���`a
���`a
���`ax���`a ���aoa=���`a ���`bnp���aoa.���`farange���`a(���bmfc0.0���`a,���`a ���bmfc5.0���`a,���`a ���bmfd0.01���`a)���`a
���`ay���`a ���aoa=���`a ���`bnp���aoa.���`csin���`a(���bmia2���`a ���aoa*���`a ���`bnp���aoa.���`bpi���`a ���aoa*���`a ���`ax���`a)���`a ���aoa+���`a ���bmfc0.5���`a ���aoa*���`a ���`bnp���aoa.���`frandom���aoa.���`erandn���`a(���bnbclen���`a(���`ax���`a)���`a)���`a
���`a
���`cax1���aoa.���`dplot���`a(���`ax���`a,���`a ���`ay���`a)���`a
���`cax1���aoa.���`hset_ylim���`a(���aoa-���bmia2���`a,���`a ���bmia2���`a)���`a
���`cax1���aoa.���`iset_title���`a(���bs1a'���bs1x!Press left mouse button and drag ���bs1a'���`a
���`n              ���bs1a'���bs1x#to select a region in the top graph���bs1a'���`a)���`a
���`a
���`eline2���`a,���`a ���aoa=���`a ���`cax2���aoa.���`dplot���`a(���`a[���`a]���`a,���`a ���`a[���`a]���`a)���`a
���`a
���`a
���akcdef���`a ���bnfhonselect���`a(���`dxmin���`a,���`a ���`dxmax���`a)���`a:���`a
���`d    ���`findmin���`a,���`a ���`findmax���`a ���aoa=���`a ���`bnp���aoa.���`lsearchsorted���`a(���`ax���`a,���`a ���`a(���`dxmin���`a,���`a ���`dxmax���`a)���`a)���`a
���`d    ���`findmax���`a ���aoa=���`a ���bnbcmin���`a(���bnbclen���`a(���`ax���`a)���`a ���aoa-���`a ���bmia1���`a,���`a ���`findmax���`a)���`a
���`a
���`d    ���`hregion_x���`a ���aoa=���`a ���`ax���`a[���`findmin���`a:���`findmax���`a]���`a
���`d    ���`hregion_y���`a ���aoa=���`a ���`ay���`a[���`findmin���`a:���`findmax���`a]���`a
���`a
���`d    ���akbif���`a ���bnbclen���`a(���`hregion_x���`a)���`a ���aoa>���aoa=���`a ���bmia2���`a:���`a
���`h        ���`eline2���aoa.���`hset_data���`a(���`hregion_x���`a,���`a ���`hregion_y���`a)���`a
���`h        ���`cax2���aoa.���`hset_xlim���`a(���`hregion_x���`a[���bmia0���`a]���`a,���`a ���`hregion_x���`a[���aoa-���bmia1���`a]���`a)���`a
���`h        ���`cax2���aoa.���`hset_ylim���`a(���`hregion_y���aoa.���`cmin���`a(���`a)���`a,���`a ���`hregion_y���aoa.���`cmax���`a(���`a)���`a)���`a
���`h        ���`cfig���aoa.���`fcanvas���aoa.���`idraw_idle���`a(���`a)���`a
���`a
���`a
���bc1xM#############################################################################���`a
���bc1k# .. note::���`a
���bc1a#���`a
���bc1xF#    If the SpanSelector object is garbage collected you will lose the���`a
���bc1xJ#    interactivity.  You must keep a hard reference to it to prevent this.���`a
���bc1a#���`a
���`a
���`a
���`dspan���`a ���aoa=���`a ���`lSpanSelector���`a(���`a
���`d    ���`cax1���`a,���`a
���`d    ���`honselect���`a,���`a
���`d    ���bs2a"���bs2jhorizontal���bs2a"���`a,���`a
���`d    ���`guseblit���aoa=���bkcdTrue���`a,���`a
���`d    ���`eprops���aoa=���bnbddict���`a(���`ealpha���aoa=���bmfc0.5���`a,���`a ���`ifacecolor���aoa=���bs2a"���bs2htab:blue���bs2a"���`a)���`a,���`a
���`d    ���`kinteractive���aoa=���bkcdTrue���`a,���`a
���`d    ���`rdrag_from_anywhere���aoa=���bkcdTrue���`a
���`a)���`a
���bc1x=# Set useblit=True on most backends for enhanced performance.���`a
���`a
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
���bc1x(#    - `matplotlib.widgets.SpanSelector`���`a
`dNone�