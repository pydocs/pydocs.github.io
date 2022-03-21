������������bsdx["""
==================
Simple axes labels
==================

Label the axes of a plot.
"""���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���`a
���`cfig���`a ���aoa=���`a ���`cplt���aoa.���`ffigure���`a(���`a)���`a
���`cfig���aoa.���`osubplots_adjust���`a(���`ctop���aoa=���bmfc0.8���`a)���`a
���`cax1���`a ���aoa=���`a ���`cfig���aoa.���`kadd_subplot���`a(���bmic211���`a)���`a
���`cax1���aoa.���`jset_ylabel���`a(���bs1a'���bs1evolts���bs1a'���`a)���`a
���`cax1���aoa.���`iset_title���`a(���bs1a'���bs1ka sine wave���bs1a'���`a)���`a
���`a
���`at���`a ���aoa=���`a ���`bnp���aoa.���`farange���`a(���bmfc0.0���`a,���`a ���bmfc1.0���`a,���`a ���bmfd0.01���`a)���`a
���`as���`a ���aoa=���`a ���`bnp���aoa.���`csin���`a(���bmia2���`a ���aoa*���`a ���`bnp���aoa.���`bpi���`a ���aoa*���`a ���`at���`a)���`a
���`dline���`a,���`a ���aoa=���`a ���`cax1���aoa.���`dplot���`a(���`at���`a,���`a ���`as���`a,���`a ���`blw���aoa=���bmia2���`a)���`a
���`a
���bc1x)# Fixing random state for reproducibility���`a
���`bnp���aoa.���`frandom���aoa.���`dseed���`a(���bmih19680801���`a)���`a
���`a
���`cax2���`a ���aoa=���`a ���`cfig���aoa.���`hadd_axes���`a(���`a[���bmfd0.15���`a,���`a ���bmfc0.1���`a,���`a ���bmfc0.7���`a,���`a ���bmfc0.3���`a]���`a)���`a
���`an���`a,���`a ���`dbins���`a,���`a ���`gpatches���`a ���aoa=���`a ���`cax2���aoa.���`dhist���`a(���`bnp���aoa.���`frandom���aoa.���`erandn���`a(���bmid1000���`a)���`a,���`a ���bmib50���`a)���`a
���`cax2���aoa.���`jset_xlabel���`a(���bs1a'���bs1htime (s)���bs1a'���`a)���`a
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
���bc1x(#    - `matplotlib.axes.Axes.set_xlabel`���`a
���bc1x(#    - `matplotlib.axes.Axes.set_ylabel`���`a
���bc1x'#    - `matplotlib.axes.Axes.set_title`���`a
���bc1x"#    - `matplotlib.axes.Axes.plot`���`a
���bc1x"#    - `matplotlib.axes.Axes.hist`���`a
���bc1x*#    - `matplotlib.figure.Figure.add_axes`���`a
`dNone�