������������bsdxr"""
=======================
Bar chart on polar axis
=======================

Demo of bar plot on a polar axis.
"""���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���`a
���`a
���bc1x)# Fixing random state for reproducibility���`a
���`bnp���aoa.���`frandom���aoa.���`dseed���`a(���bmih19680801���`a)���`a
���`a
���bc1t# Compute pie slices���`a
���`aN���`a ���aoa=���`a ���bmib20���`a
���`etheta���`a ���aoa=���`a ���`bnp���aoa.���`hlinspace���`a(���bmfc0.0���`a,���`a ���bmia2���`a ���aoa*���`a ���`bnp���aoa.���`bpi���`a,���`a ���`aN���`a,���`a ���`hendpoint���aoa=���bkceFalse���`a)���`a
���`eradii���`a ���aoa=���`a ���bmib10���`a ���aoa*���`a ���`bnp���aoa.���`frandom���aoa.���`drand���`a(���`aN���`a)���`a
���`ewidth���`a ���aoa=���`a ���`bnp���aoa.���`bpi���`a ���aoa/���`a ���bmia4���`a ���aoa*���`a ���`bnp���aoa.���`frandom���aoa.���`drand���`a(���`aN���`a)���`a
���`fcolors���`a ���aoa=���`a ���`cplt���aoa.���`bcm���aoa.���`gviridis���`a(���`eradii���`a ���aoa/���`a ���bmfc10.���`a)���`a
���`a
���`bax���`a ���aoa=���`a ���`cplt���aoa.���`gsubplot���`a(���`jprojection���aoa=���bs1a'���bs1epolar���bs1a'���`a)���`a
���`bax���aoa.���`cbar���`a(���`etheta���`a,���`a ���`eradii���`a,���`a ���`ewidth���aoa=���`ewidth���`a,���`a ���`fbottom���aoa=���bmfc0.0���`a,���`a ���`ecolor���aoa=���`fcolors���`a,���`a ���`ealpha���aoa=���bmfc0.5���`a)���`a
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
���bc1x;#    - `matplotlib.axes.Axes.bar` / `matplotlib.pyplot.bar`���`a
���bc1x%#    - `matplotlib.projections.polar`���`a
`dNone�