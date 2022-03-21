������������bsdy�"""
==============
Custom Ticker1
==============

The new ticker code was designed to explicitly support user customized
ticking. The documentation of :mod:`matplotlib.ticker` details this
process.  That code defines a lot of preset tickers but was primarily
designed to be user extensible.

In this example a user defined function is used to format the ticks in
millions of dollars on the y axis.
"""���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���`a
���`emoney���`a ���aoa=���`a ���`a[���bmfe1.5e5���`a,���`a ���bmfe2.5e6���`a,���`a ���bmfe5.5e6���`a,���`a ���bmfe2.0e7���`a]���`a
���`a
���`a
���akcdef���`a ���bnfhmillions���`a(���`ax���`a,���`a ���`cpos���`a)���`a:���`a
���`d    ���bsdx8"""The two arguments are the value and tick position."""���`a
���`d    ���akfreturn���`a ���bs1a'���bs1a$���bsig{:1.1f}���bs1aM���bs1a'���aoa.���`fformat���`a(���`ax���aoa*���bmfd1e-6���`a)���`a
���`a
���`cfig���`a,���`a ���`bax���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`a)���`a
���bc1x&# Use automatic FuncFormatter creation���`a
���`bax���aoa.���`eyaxis���aoa.���`sset_major_formatter���`a(���`hmillions���`a)���`a
���`bax���aoa.���`cbar���`a(���`a[���bs1a'���bs1dBill���bs1a'���`a,���`a ���bs1a'���bs1dFred���bs1a'���`a,���`a ���bs1a'���bs1dMary���bs1a'���`a,���`a ���bs1a'���bs1cSue���bs1a'���`a]���`a,���`a ���`emoney���`a)���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
���`a
���bc1xM#############################################################################���`a
���bc1a#���`a
���bc1x# .. admonition:: References���`a
���bc1a#���`a
���bc1xN#    The use of the following functions, methods, classes and modules is shown���`a
���bc1u#    in this example:���`a
���bc1a#���`a
���bc1x##    - `matplotlib.pyplot.subplots`���`a
���bc1x1#    - `matplotlib.axis.Axis.set_major_formatter`���`a
���bc1x(#    - `matplotlib.ticker.FuncFormatter`���`a
`dNone�