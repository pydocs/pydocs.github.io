������������bsdxN"""
==========
Polar plot
==========

Demo of a line plot on a polar axis.
"""���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���`a
���`a
���`ar���`a ���aoa=���`a ���`bnp���aoa.���`farange���`a(���bmia0���`a,���`a ���bmia2���`a,���`a ���bmfd0.01���`a)���`a
���`etheta���`a ���aoa=���`a ���bmia2���`a ���aoa*���`a ���`bnp���aoa.���`bpi���`a ���aoa*���`a ���`ar���`a
���`a
���`cfig���`a,���`a ���`bax���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`jsubplot_kw���aoa=���`a{���bs1a'���bs1jprojection���bs1a'���`a:���`a ���bs1a'���bs1epolar���bs1a'���`a}���`a)���`a
���`bax���aoa.���`dplot���`a(���`etheta���`a,���`a ���`ar���`a)���`a
���`bax���aoa.���`hset_rmax���`a(���bmia2���`a)���`a
���`bax���aoa.���`jset_rticks���`a(���`a[���bmfc0.5���`a,���`a ���bmia1���`a,���`a ���bmfc1.5���`a,���`a ���bmia2���`a]���`a)���`b  ���bc1s# Less radial ticks���`a
���`bax���aoa.���`sset_rlabel_position���`a(���aoa-���bmfd22.5���`a)���`b  ���bc1x+# Move radial labels away from plotted line���`a
���`bax���aoa.���`dgrid���`a(���bkcdTrue���`a)���`a
���`a
���`bax���aoa.���`iset_title���`a(���bs2a"���bs2xA line plot on a polar axis���bs2a"���`a,���`a ���`bva���aoa=���bs1a'���bs1fbottom���bs1a'���`a)���`a
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
���bc1x%#    - `matplotlib.projections.polar`���`a
���bc1x/#    - `matplotlib.projections.polar.PolarAxes`���`a
���bc1x:#    - `matplotlib.projections.polar.PolarAxes.set_rticks`���`a
���bc1x8#    - `matplotlib.projections.polar.PolarAxes.set_rmax`���`a
���bc1xC#    - `matplotlib.projections.polar.PolarAxes.set_rlabel_position`���`a
`dNone�