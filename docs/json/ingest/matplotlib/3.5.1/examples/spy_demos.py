������������bsdxK"""
=========
Spy Demos
=========

Plot the sparsity pattern of arrays.
"""���`a
���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���`a
���`a
���bc1x)# Fixing random state for reproducibility���`a
���`bnp���aoa.���`frandom���aoa.���`dseed���`a(���bmih19680801���`a)���`a
���`a
���`cfig���`a,���`a ���`caxs���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���bmia2���`a,���`a ���bmia2���`a)���`a
���`cax1���`a ���aoa=���`a ���`caxs���`a[���bmia0���`a,���`a ���bmia0���`a]���`a
���`cax2���`a ���aoa=���`a ���`caxs���`a[���bmia0���`a,���`a ���bmia1���`a]���`a
���`cax3���`a ���aoa=���`a ���`caxs���`a[���bmia1���`a,���`a ���bmia0���`a]���`a
���`cax4���`a ���aoa=���`a ���`caxs���`a[���bmia1���`a,���`a ���bmia1���`a]���`a
���`a
���`ax���`a ���aoa=���`a ���`bnp���aoa.���`frandom���aoa.���`erandn���`a(���bmib20���`a,���`a ���bmib20���`a)���`a
���`ax���`a[���bmia5���`a,���`a ���`a:���`a]���`a ���aoa=���`a ���bmfb0.���`a
���`ax���`a[���`a:���`a,���`a ���bmib12���`a]���`a ���aoa=���`a ���bmfb0.���`a
���`a
���`cax1���aoa.���`cspy���`a(���`ax���`a,���`a ���`jmarkersize���aoa=���bmia5���`a)���`a
���`cax2���aoa.���`cspy���`a(���`ax���`a,���`a ���`iprecision���aoa=���bmfc0.1���`a,���`a ���`jmarkersize���aoa=���bmia5���`a)���`a
���`a
���`cax3���aoa.���`cspy���`a(���`ax���`a)���`a
���`cax4���aoa.���`cspy���`a(���`ax���`a,���`a ���`iprecision���aoa=���bmfc0.1���`a)���`a
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
���bc1x;#    - `matplotlib.axes.Axes.spy` / `matplotlib.pyplot.spy`���`a
`dNone�