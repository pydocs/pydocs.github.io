������������bsdx]"""
============
Scatter plot
============

This example showcases a simple scatter plot.
"""���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���`a
���bc1x)# Fixing random state for reproducibility���`a
���`bnp���aoa.���`frandom���aoa.���`dseed���`a(���bmih19680801���`a)���`a
���`a
���`a
���`aN���`a ���aoa=���`a ���bmib50���`a
���`ax���`a ���aoa=���`a ���`bnp���aoa.���`frandom���aoa.���`drand���`a(���`aN���`a)���`a
���`ay���`a ���aoa=���`a ���`bnp���aoa.���`frandom���aoa.���`drand���`a(���`aN���`a)���`a
���`fcolors���`a ���aoa=���`a ���`bnp���aoa.���`frandom���aoa.���`drand���`a(���`aN���`a)���`a
���`darea���`a ���aoa=���`a ���`a(���bmib30���`a ���aoa*���`a ���`bnp���aoa.���`frandom���aoa.���`drand���`a(���`aN���`a)���`a)���aoa*���aoa*���bmia2���`b  ���bc1u# 0 to 15 point radii���`a
���`a
���`cplt���aoa.���`gscatter���`a(���`ax���`a,���`a ���`ay���`a,���`a ���`as���aoa=���`darea���`a,���`a ���`ac���aoa=���`fcolors���`a,���`a ���`ealpha���aoa=���bmfc0.5���`a)���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
���`a
���bc1xM#############################################################################���`a
���bc1a#���`a
���bc1x# .. admonition:: References���`a
���bc1a#���`a
���bc1xN#    The use of the following functions, methods, classes and modules is shown���`a
���bc1u#    in this example:���`a
���bc1a#���`a
���bc1xC#    - `matplotlib.axes.Axes.scatter` / `matplotlib.pyplot.scatter`���`a
`dNone�