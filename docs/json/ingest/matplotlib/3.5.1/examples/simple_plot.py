������������bsdxB"""
===========
Simple Plot
===========

Create a simple plot.
"""���`a
���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���`a
���bc1s# Data for plotting���`a
���`at���`a ���aoa=���`a ���`bnp���aoa.���`farange���`a(���bmfc0.0���`a,���`a ���bmfc2.0���`a,���`a ���bmfd0.01���`a)���`a
���`as���`a ���aoa=���`a ���bmia1���`a ���aoa+���`a ���`bnp���aoa.���`csin���`a(���bmia2���`a ���aoa*���`a ���`bnp���aoa.���`bpi���`a ���aoa*���`a ���`at���`a)���`a
���`a
���`cfig���`a,���`a ���`bax���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`a)���`a
���`bax���aoa.���`dplot���`a(���`at���`a,���`a ���`as���`a)���`a
���`a
���`bax���aoa.���`cset���`a(���`fxlabel���aoa=���bs1a'���bs1htime (s)���bs1a'���`a,���`a ���`fylabel���aoa=���bs1a'���bs1lvoltage (mV)���bs1a'���`a,���`a
���`g       ���`etitle���aoa=���bs1a'���bs1x!About as simple as it gets, folks���bs1a'���`a)���`a
���`bax���aoa.���`dgrid���`a(���`a)���`a
���`a
���`cfig���aoa.���`gsavefig���`a(���bs2a"���bs2htest.png���bs2a"���`a)���`a
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
���bc1x##    - `matplotlib.pyplot.subplots`���`a
���bc1x)#    - `matplotlib.figure.Figure.savefig`���`a
`dNone�