������������bsdx�"""
=======
Buttons
=======

Constructing a simple button GUI to modify a sine wave.

The ``next`` and ``previous`` button widget helps visualize the wave with
new frequencies.
"""���`a
���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���bkndfrom���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnngwidgets���`a ���bknfimport���`a ���`fButton���`a
���`a
���`efreqs���`a ���aoa=���`a ���`bnp���aoa.���`farange���`a(���bmia2���`a,���`a ���bmib20���`a,���`a ���bmia3���`a)���`a
���`a
���`cfig���`a,���`a ���`bax���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`a)���`a
���`cplt���aoa.���`osubplots_adjust���`a(���`fbottom���aoa=���bmfc0.2���`a)���`a
���`at���`a ���aoa=���`a ���`bnp���aoa.���`farange���`a(���bmfc0.0���`a,���`a ���bmfc1.0���`a,���`a ���bmfe0.001���`a)���`a
���`as���`a ���aoa=���`a ���`bnp���aoa.���`csin���`a(���bmia2���aoa*���`bnp���aoa.���`bpi���aoa*���`efreqs���`a[���bmia0���`a]���aoa*���`at���`a)���`a
���`al���`a,���`a ���aoa=���`a ���`cplt���aoa.���`dplot���`a(���`at���`a,���`a ���`as���`a,���`a ���`blw���aoa=���bmia2���`a)���`a
���`a
���`a
���akeclass���`a ���bnceIndex���`a:���`a
���`d    ���`cind���`a ���aoa=���`a ���bmia0���`a
���`a
���`d    ���akcdef���`a ���bnfdnext���`a(���bbpdself���`a,���`a ���`eevent���`a)���`a:���`a
���`h        ���bbpdself���aoa.���`cind���`a ���aoa+���aoa=���`a ���bmia1���`a
���`h        ���`ai���`a ���aoa=���`a ���bbpdself���aoa.���`cind���`a ���aoa%���`a ���bnbclen���`a(���`efreqs���`a)���`a
���`h        ���`eydata���`a ���aoa=���`a ���`bnp���aoa.���`csin���`a(���bmia2���aoa*���`bnp���aoa.���`bpi���aoa*���`efreqs���`a[���`ai���`a]���aoa*���`at���`a)���`a
���`h        ���`al���aoa.���`iset_ydata���`a(���`eydata���`a)���`a
���`h        ���`cplt���aoa.���`ddraw���`a(���`a)���`a
���`a
���`d    ���akcdef���`a ���bnfdprev���`a(���bbpdself���`a,���`a ���`eevent���`a)���`a:���`a
���`h        ���bbpdself���aoa.���`cind���`a ���aoa-���aoa=���`a ���bmia1���`a
���`h        ���`ai���`a ���aoa=���`a ���bbpdself���aoa.���`cind���`a ���aoa%���`a ���bnbclen���`a(���`efreqs���`a)���`a
���`h        ���`eydata���`a ���aoa=���`a ���`bnp���aoa.���`csin���`a(���bmia2���aoa*���`bnp���aoa.���`bpi���aoa*���`efreqs���`a[���`ai���`a]���aoa*���`at���`a)���`a
���`h        ���`al���aoa.���`iset_ydata���`a(���`eydata���`a)���`a
���`h        ���`cplt���aoa.���`ddraw���`a(���`a)���`a
���`a
���`hcallback���`a ���aoa=���`a ���`eIndex���`a(���`a)���`a
���`faxprev���`a ���aoa=���`a ���`cplt���aoa.���`daxes���`a(���`a[���bmfc0.7���`a,���`a ���bmfd0.05���`a,���`a ���bmfc0.1���`a,���`a ���bmfe0.075���`a]���`a)���`a
���`faxnext���`a ���aoa=���`a ���`cplt���aoa.���`daxes���`a(���`a[���bmfd0.81���`a,���`a ���bmfd0.05���`a,���`a ���bmfc0.1���`a,���`a ���bmfe0.075���`a]���`a)���`a
���`ebnext���`a ���aoa=���`a ���`fButton���`a(���`faxnext���`a,���`a ���bs1a'���bs1dNext���bs1a'���`a)���`a
���`ebnext���aoa.���`jon_clicked���`a(���`hcallback���aoa.���`dnext���`a)���`a
���`ebprev���`a ���aoa=���`a ���`fButton���`a(���`faxprev���`a,���`a ���bs1a'���bs1hPrevious���bs1a'���`a)���`a
���`ebprev���aoa.���`jon_clicked���`a(���`hcallback���aoa.���`dprev���`a)���`a
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
���bc1x"#    - `matplotlib.widgets.Button`���`a
`dNone�