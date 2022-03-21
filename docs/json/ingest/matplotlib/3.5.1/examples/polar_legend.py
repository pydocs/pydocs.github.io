�����������bsdxV"""
============
Polar Legend
============

Demo of a legend on a polar-axis plot.
"""���`a
���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���`a
���`cfig���`a ���aoa=���`a ���`cplt���aoa.���`ffigure���`a(���`a)���`a
���`bax���`a ���aoa=���`a ���`cfig���aoa.���`kadd_subplot���`a(���`jprojection���aoa=���bs2a"���bs2epolar���bs2a"���`a,���`a ���`ifacecolor���aoa=���bs2a"���bs2tlightgoldenrodyellow���bs2a"���`a)���`a
���`a
���`ar���`a ���aoa=���`a ���`bnp���aoa.���`hlinspace���`a(���bmia0���`a,���`a ���bmia3���`a,���`a ���bmic301���`a)���`a
���`etheta���`a ���aoa=���`a ���bmia2���`a ���aoa*���`a ���`bnp���aoa.���`bpi���`a ���aoa*���`a ���`ar���`a
���`bax���aoa.���`dplot���`a(���`etheta���`a,���`a ���`ar���`a,���`a ���`ecolor���aoa=���bs2a"���bs2jtab:orange���bs2a"���`a,���`a ���`blw���aoa=���bmia3���`a,���`a ���`elabel���aoa=���bs2a"���bs2fa line���bs2a"���`a)���`a
���`bax���aoa.���`dplot���`a(���bmfc0.5���`a ���aoa*���`a ���`etheta���`a,���`a ���`ar���`a,���`a ���`ecolor���aoa=���bs2a"���bs2htab:blue���bs2a"���`a,���`a ���`bls���aoa=���bs2a"���bs2b--���bs2a"���`a,���`a ���`blw���aoa=���bmia3���`a,���`a ���`elabel���aoa=���bs2a"���bs2lanother line���bs2a"���`a)���`a
���`bax���aoa.���`ktick_params���`a(���`jgrid_color���aoa=���bs2a"���bs2mpalegoldenrod���bs2a"���`a)���`a
���bc1xL# For polar axes, it may be useful to move the legend slightly away from the���`a
���bc1xO# axes center, to avoid overlap between the legend and the axes.  The following���`a
���bc1xN# snippet places the legend's lower left corner just outside of the polar axes���`a
���bc1x3# at an angle of 67.5 degrees in polar coordinates.���`a
���`eangle���`a ���aoa=���`a ���`bnp���aoa.���`gdeg2rad���`a(���bmfd67.5���`a)���`a
���`bax���aoa.���`flegend���`a(���`cloc���aoa=���bs2a"���bs2jlower left���bs2a"���`a,���`a
���`j          ���`nbbox_to_anchor���aoa=���`a(���bmfb.5���`a ���aoa+���`a ���`bnp���aoa.���`ccos���`a(���`eangle���`a)���aoa/���bmia2���`a,���`a ���bmfb.5���`a ���aoa+���`a ���`bnp���aoa.���`csin���`a(���`eangle���`a)���aoa/���bmia2���`a)���`a)���`a
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
���bc1x=#    - `matplotlib.axes.Axes.plot` / `matplotlib.pyplot.plot`���`a
���bc1xA#    - `matplotlib.axes.Axes.legend` / `matplotlib.pyplot.legend`���`a
���bc1x%#    - `matplotlib.projections.polar`���`a
���bc1x/#    - `matplotlib.projections.polar.PolarAxes`���`a
`dNone�