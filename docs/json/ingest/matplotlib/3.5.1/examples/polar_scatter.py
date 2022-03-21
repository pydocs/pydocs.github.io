������������bsdx�"""
==========================
Scatter plot on polar axis
==========================

Size increases radially in this example and color increases with angle
(just to verify the symbols are being scattered correctly).
"""���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���`a
���`a
���bc1x)# Fixing random state for reproducibility���`a
���`bnp���aoa.���`frandom���aoa.���`dseed���`a(���bmih19680801���`a)���`a
���`a
���bc1x# Compute areas and colors���`a
���`aN���`a ���aoa=���`a ���bmic150���`a
���`ar���`a ���aoa=���`a ���bmia2���`a ���aoa*���`a ���`bnp���aoa.���`frandom���aoa.���`drand���`a(���`aN���`a)���`a
���`etheta���`a ���aoa=���`a ���bmia2���`a ���aoa*���`a ���`bnp���aoa.���`bpi���`a ���aoa*���`a ���`bnp���aoa.���`frandom���aoa.���`drand���`a(���`aN���`a)���`a
���`darea���`a ���aoa=���`a ���bmic200���`a ���aoa*���`a ���`ar���aoa*���aoa*���bmia2���`a
���`fcolors���`a ���aoa=���`a ���`etheta���`a
���`a
���`cfig���`a ���aoa=���`a ���`cplt���aoa.���`ffigure���`a(���`a)���`a
���`bax���`a ���aoa=���`a ���`cfig���aoa.���`kadd_subplot���`a(���`jprojection���aoa=���bs1a'���bs1epolar���bs1a'���`a)���`a
���`ac���`a ���aoa=���`a ���`bax���aoa.���`gscatter���`a(���`etheta���`a,���`a ���`ar���`a,���`a ���`ac���aoa=���`fcolors���`a,���`a ���`as���aoa=���`darea���`a,���`a ���`dcmap���aoa=���bs1a'���bs1chsv���bs1a'���`a,���`a ���`ealpha���aoa=���bmfd0.75���`a)���`a
���`a
���bc1xO###############################################################################���`a
���bc1x0# Scatter plot on polar axis, with offset origin���`a
���bc1x0# ----------------------------------------------���`a
���bc1a#���`a
���bc1xO# The main difference with the previous plot is the configuration of the origin���`a
���bc1xO# radius, producing an annulus. Additionally, the theta zero location is set to���`a
���bc1r# rotate the plot.���`a
���`a
���`cfig���`a ���aoa=���`a ���`cplt���aoa.���`ffigure���`a(���`a)���`a
���`bax���`a ���aoa=���`a ���`cfig���aoa.���`kadd_subplot���`a(���`jprojection���aoa=���bs1a'���bs1epolar���bs1a'���`a)���`a
���`ac���`a ���aoa=���`a ���`bax���aoa.���`gscatter���`a(���`etheta���`a,���`a ���`ar���`a,���`a ���`ac���aoa=���`fcolors���`a,���`a ���`as���aoa=���`darea���`a,���`a ���`dcmap���aoa=���bs1a'���bs1chsv���bs1a'���`a,���`a ���`ealpha���aoa=���bmfd0.75���`a)���`a
���`a
���`bax���aoa.���`kset_rorigin���`a(���aoa-���bmfc2.5���`a)���`a
���`bax���aoa.���`wset_theta_zero_location���`a(���bs1a'���bs1aW���bs1a'���`a,���`a ���`foffset���aoa=���bmib10���`a)���`a
���`a
���bc1xO###############################################################################���`a
���bc1x1# Scatter plot on polar axis confined to a sector���`a
���bc1x1# -----------------------------------------------���`a
���bc1a#���`a
���bc1xI# The main difference with the previous plots is the configuration of the���`a
���bc1xJ# theta start and end limits, producing a sector instead of a full circle.���`a
���`a
���`cfig���`a ���aoa=���`a ���`cplt���aoa.���`ffigure���`a(���`a)���`a
���`bax���`a ���aoa=���`a ���`cfig���aoa.���`kadd_subplot���`a(���`jprojection���aoa=���bs1a'���bs1epolar���bs1a'���`a)���`a
���`ac���`a ���aoa=���`a ���`bax���aoa.���`gscatter���`a(���`etheta���`a,���`a ���`ar���`a,���`a ���`ac���aoa=���`fcolors���`a,���`a ���`as���aoa=���`darea���`a,���`a ���`dcmap���aoa=���bs1a'���bs1chsv���bs1a'���`a,���`a ���`ealpha���aoa=���bmfd0.75���`a)���`a
���`a
���`bax���aoa.���`lset_thetamin���`a(���bmib45���`a)���`a
���`bax���aoa.���`lset_thetamax���`a(���bmic135���`a)���`a
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
���bc1xC#    - `matplotlib.axes.Axes.scatter` / `matplotlib.pyplot.scatter`���`a
���bc1x%#    - `matplotlib.projections.polar`���`a
���bc1x;#    - `matplotlib.projections.polar.PolarAxes.set_rorigin`���`a
���bc1xG#    - `matplotlib.projections.polar.PolarAxes.set_theta_zero_location`���`a
���bc1x<#    - `matplotlib.projections.polar.PolarAxes.set_thetamin`���`a
���bc1x<#    - `matplotlib.projections.polar.PolarAxes.set_thetamax`���`a
`dNone�