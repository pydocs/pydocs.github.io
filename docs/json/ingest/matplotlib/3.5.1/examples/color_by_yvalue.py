������������bsdx~"""
================
Color by y-value
================

Use masked arrays to plot a line with different colors by y-value.
"""���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���`a
���`at���`a ���aoa=���`a ���`bnp���aoa.���`farange���`a(���bmfc0.0���`a,���`a ���bmfc2.0���`a,���`a ���bmfd0.01���`a)���`a
���`as���`a ���aoa=���`a ���`bnp���aoa.���`csin���`a(���bmia2���`a ���aoa*���`a ���`bnp���aoa.���`bpi���`a ���aoa*���`a ���`at���`a)���`a
���`a
���`eupper���`a ���aoa=���`a ���bmfd0.77���`a
���`elower���`a ���aoa=���`a ���aoa-���bmfd0.77���`a
���`a
���`fsupper���`a ���aoa=���`a ���`bnp���aoa.���`bma���aoa.���`lmasked_where���`a(���`as���`a ���aoa<���`a ���`eupper���`a,���`a ���`as���`a)���`a
���`fslower���`a ���aoa=���`a ���`bnp���aoa.���`bma���aoa.���`lmasked_where���`a(���`as���`a ���aoa>���`a ���`elower���`a,���`a ���`as���`a)���`a
���`gsmiddle���`a ���aoa=���`a ���`bnp���aoa.���`bma���aoa.���`lmasked_where���`a(���`a(���`as���`a ���aoa<���`a ���`elower���`a)���`a ���aoa|���`a ���`a(���`as���`a ���aoa>���`a ���`eupper���`a)���`a,���`a ���`as���`a)���`a
���`a
���`cfig���`a,���`a ���`bax���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`a)���`a
���`bax���aoa.���`dplot���`a(���`at���`a,���`a ���`gsmiddle���`a,���`a ���`at���`a,���`a ���`fslower���`a,���`a ���`at���`a,���`a ���`fsupper���`a)���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
���`a
���bc1xM#############################################################################���`a
���bc1a#���`a
���bc1x# .. admonition:: References���`a
���bc1a#���`a
���bc1xN#    The use of the following functions, methods, classes and modules is shown���`a
���bc1u#    in this example:���`a
���bc1a#���`a
���bc1x=#    - `matplotlib.axes.Axes.plot` / `matplotlib.pyplot.plot`���`a
`dNone�