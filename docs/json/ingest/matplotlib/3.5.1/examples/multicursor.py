������������bsdx�"""
===========
Multicursor
===========

Showing a cursor on multiple plots simultaneously.

This example generates two subplots and on hovering the cursor over data in one
subplot, the values of that datapoint are shown in both respectively.
"""���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���bkndfrom���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnngwidgets���`a ���bknfimport���`a ���`kMultiCursor���`a
���`a
���`at���`a ���aoa=���`a ���`bnp���aoa.���`farange���`a(���bmfc0.0���`a,���`a ���bmfc2.0���`a,���`a ���bmfd0.01���`a)���`a
���`bs1���`a ���aoa=���`a ���`bnp���aoa.���`csin���`a(���bmia2���aoa*���`bnp���aoa.���`bpi���aoa*���`at���`a)���`a
���`bs2���`a ���aoa=���`a ���`bnp���aoa.���`csin���`a(���bmia4���aoa*���`bnp���aoa.���`bpi���aoa*���`at���`a)���`a
���`a
���`cfig���`a,���`a ���`a(���`cax1���`a,���`a ���`cax2���`a)���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���bmia2���`a,���`a ���`fsharex���aoa=���bkcdTrue���`a)���`a
���`cax1���aoa.���`dplot���`a(���`at���`a,���`a ���`bs1���`a)���`a
���`cax2���aoa.���`dplot���`a(���`at���`a,���`a ���`bs2���`a)���`a
���`a
���`emulti���`a ���aoa=���`a ���`kMultiCursor���`a(���`cfig���aoa.���`fcanvas���`a,���`a ���`a(���`cax1���`a,���`a ���`cax2���`a)���`a,���`a ���`ecolor���aoa=���bs1a'���bs1ar���bs1a'���`a,���`a ���`blw���aoa=���bmia1���`a)���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
���`a
���bc1xM#############################################################################���`a
���bc1a#���`a
���bc1x# .. admonition:: References���`a
���bc1a#���`a
���bc1xN#    The use of the following functions, methods, classes and modules is shown���`a
���bc1u#    in this example:���`a
���bc1a#���`a
���bc1x'#    - `matplotlib.widgets.MultiCursor`���`a
`dNone�