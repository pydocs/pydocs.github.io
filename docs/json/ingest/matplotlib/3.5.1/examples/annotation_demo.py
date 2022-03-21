��������+���bsdy�"""
================
Annotating Plots
================

The following examples show how it is possible to annotate plots in Matplotlib.
This includes highlighting specific points of interest and using various
visual tools to call attention to this point. For a more complete and in-depth
description of the annotation and text tools in Matplotlib, see the
:doc:`tutorial on annotation </tutorials/text/annotations>`.
"""���`a
���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���bkndfrom���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnngpatches���`a ���bknfimport���`a ���`gEllipse���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���bkndfrom���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnndtext���`a ���bknfimport���`a ���`jOffsetFrom���`a
���`a
���`a
���bc1xO###############################################################################���`a
���bc1x.# Specifying text points and annotation points���`a
���bc1x.# --------------------------------------------���`a
���bc1a#���`a
���bc1xL# You must specify an annotation point ``xy=(x, y)`` to annotate this point.���`a
���bc1xO# Additionally, you may specify a text point ``xytext=(x, y)`` for the location���`a
���bc1xN# of the text for this annotation.  Optionally, you can specify the coordinate���`a
���bc1xN# system of *xy* and *xytext* with one of the following strings for *xycoords*���`a
���bc1x(# and *textcoords* (default is 'data')::���`a
���bc1a#���`a
���bc1xF#  'figure points'   : points from the lower left corner of the figure���`a
���bc1xF#  'figure pixels'   : pixels from the lower left corner of the figure���`a
���bc1xO#  'figure fraction' : (0, 0) is lower left of figure and (1, 1) is upper right���`a
���bc1x<#  'axes points'     : points from lower left corner of axes���`a
���bc1x<#  'axes pixels'     : pixels from lower left corner of axes���`a
���bc1xM#  'axes fraction'   : (0, 0) is lower left of axes and (1, 1) is upper right���`a
���bc1xF#  'offset points'   : Specify an offset (in points) from the xy value���`a
���bc1xF#  'offset pixels'   : Specify an offset (in pixels) from the xy value���`a
���bc1x:#  'data'            : use the axes data coordinate system���`a
���bc1a#���`a
���bc1xL# Note: for physical coordinate systems (points or pixels) the origin is the���`a
���bc1x'# (bottom, left) of the figure or axes.���`a
���bc1a#���`a
���bc1xD# Optionally, you can specify arrow properties which draws and arrow���`a
���bc1xF# from the text to the annotated point by giving a dictionary of arrow���`a
���bc1l# properties���`a
���bc1a#���`a
���bc1r# Valid keys are::���`a
���bc1a#���`a
���bc1x,#   width : the width of the arrow in points���`a
���bc1xA#   frac  : the fraction of the arrow length occupied by the head���`a
���bc1xA#   headwidth : the width of the base of the arrow head in points���`a
���bc1x=#   shrink : move the tip and base some percent away from the���`a
���bc1x%#            annotated point and text���`a
���bc1x=#   any key for matplotlib.patches.polygon  (e.g., facecolor)���`a
���`a
���bc1x3# Create our figure and data we'll use for plotting���`a
���`cfig���`a,���`a ���`bax���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`gfigsize���aoa=���`a(���bmia3���`a,���`a ���bmia3���`a)���`a)���`a
���`a
���`at���`a ���aoa=���`a ���`bnp���aoa.���`farange���`a(���bmfc0.0���`a,���`a ���bmfc5.0���`a,���`a ���bmfd0.01���`a)���`a
���`as���`a ���aoa=���`a ���`bnp���aoa.���`ccos���`a(���bmia2���aoa*���`bnp���aoa.���`bpi���aoa*���`at���`a)���`a
���`a
���bc1x-# Plot a line and add some simple annotations���`a
���`dline���`a,���`a ���aoa=���`a ���`bax���aoa.���`dplot���`a(���`at���`a,���`a ���`as���`a)���`a
���`bax���aoa.���`hannotate���`a(���bs1a'���bs1mfigure pixels���bs1a'���`a,���`a
���`l            ���`bxy���aoa=���`a(���bmib10���`a,���`a ���bmib10���`a)���`a,���`a ���`hxycoords���aoa=���bs1a'���bs1mfigure pixels���bs1a'���`a)���`a
���`bax���aoa.���`hannotate���`a(���bs1a'���bs1mfigure points���bs1a'���`a,���`a
���`l            ���`bxy���aoa=���`a(���bmib80���`a,���`a ���bmib80���`a)���`a,���`a ���`hxycoords���aoa=���bs1a'���bs1mfigure points���bs1a'���`a)���`a
���`bax���aoa.���`hannotate���`a(���bs1a'���bs1ofigure fraction���bs1a'���`a,���`a
���`l            ���`bxy���aoa=���`a(���bmfd.025���`a,���`a ���bmfd.975���`a)���`a,���`a ���`hxycoords���aoa=���bs1a'���bs1ofigure fraction���bs1a'���`a,���`a
���`l            ���`shorizontalalignment���aoa=���bs1a'���bs1dleft���bs1a'���`a,���`a ���`qverticalalignment���aoa=���bs1a'���bs1ctop���bs1a'���`a,���`a
���`l            ���`hfontsize���aoa=���bmib20���`a)���`a
���`a
���bc1x=# The following examples show off how these arrows are drawn.���`a
���`a
���`bax���aoa.���`hannotate���`a(���bs1a'���bs1vpoint offset from data���bs1a'���`a,���`a
���`l            ���`bxy���aoa=���`a(���bmia2���`a,���`a ���bmia1���`a)���`a,���`a ���`hxycoords���aoa=���bs1a'���bs1ddata���bs1a'���`a,���`a
���`l            ���`fxytext���aoa=���`a(���aoa-���bmib15���`a,���`a ���bmib25���`a)���`a,���`a ���`jtextcoords���aoa=���bs1a'���bs1moffset points���bs1a'���`a,���`a
���`l            ���`jarrowprops���aoa=���bnbddict���`a(���`ifacecolor���aoa=���bs1a'���bs1eblack���bs1a'���`a,���`a ���`fshrink���aoa=���bmfd0.05���`a)���`a,���`a
���`l            ���`shorizontalalignment���aoa=���bs1a'���bs1eright���bs1a'���`a,���`a ���`qverticalalignment���aoa=���bs1a'���bs1fbottom���bs1a'���`a)���`a
���`a
���`bax���aoa.���`hannotate���`a(���bs1a'���bs1maxes fraction���bs1a'���`a,���`a
���`l            ���`bxy���aoa=���`a(���bmia3���`a,���`a ���bmia1���`a)���`a,���`a ���`hxycoords���aoa=���bs1a'���bs1ddata���bs1a'���`a,���`a
���`l            ���`fxytext���aoa=���`a(���bmfc0.8���`a,���`a ���bmfd0.95���`a)���`a,���`a ���`jtextcoords���aoa=���bs1a'���bs1maxes fraction���bs1a'���`a,���`a
���`l            ���`jarrowprops���aoa=���bnbddict���`a(���`ifacecolor���aoa=���bs1a'���bs1eblack���bs1a'���`a,���`a ���`fshrink���aoa=���bmfd0.05���`a)���`a,���`a
���`l            ���`shorizontalalignment���aoa=���bs1a'���bs1eright���bs1a'���`a,���`a ���`qverticalalignment���aoa=���bs1a'���bs1ctop���bs1a'���`a)���`a
���`a
���bc1xJ# You may also use negative points or pixels to specify from (right, top).���`a
���bc1xO# E.g., (-10, 10) is 10 points to the left of the right side of the axes and 10���`a
���bc1x# points above the bottom���`a
���`a
���`bax���aoa.���`hannotate���`a(���bs1a'���bs1xpixel offset from axes fraction���bs1a'���`a,���`a
���`l            ���`bxy���aoa=���`a(���bmia1���`a,���`a ���bmia0���`a)���`a,���`a ���`hxycoords���aoa=���bs1a'���bs1maxes fraction���bs1a'���`a,���`a
���`l            ���`fxytext���aoa=���`a(���aoa-���bmib20���`a,���`a ���bmib20���`a)���`a,���`a ���`jtextcoords���aoa=���bs1a'���bs1moffset pixels���bs1a'���`a,���`a
���`l            ���`shorizontalalignment���aoa=���bs1a'���bs1eright���bs1a'���`a,���`a
���`l            ���`qverticalalignment���aoa=���bs1a'���bs1fbottom���bs1a'���`a)���`a
���`a
���`bax���aoa.���`cset���`a(���`dxlim���aoa=���`a(���aoa-���bmia1���`a,���`a ���bmia5���`a)���`a,���`a ���`dylim���aoa=���`a(���aoa-���bmia3���`a,���`a ���bmia5���`a)���`a)���`a
���`a
���`a
���bc1xO###############################################################################���`a
���bc1x2# Using multiple coordinate systems and axis types���`a
���bc1x2# ------------------------------------------------���`a
���bc1a#���`a
���bc1xK# You can specify the *xypoint* and the *xytext* in different positions and���`a
���bc1xK# coordinate systems, and optionally turn on a connecting line and mark the���`a
���bc1x;# point with a marker.  Annotations work on polar axes too.���`a
���bc1a#���`a
���bc1xK# In the example below, the *xy* point is in native coordinates (*xycoords*���`a
���bc1xK# defaults to 'data').  For a polar axes, this is in (theta, radius) space.���`a
���bc1xO# The text in the example is placed in the fractional figure coordinate system.���`a
���bc1xN# Text keyword arguments like horizontal and vertical alignment are respected.���`a
���`a
���`cfig���`a,���`a ���`bax���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`jsubplot_kw���aoa=���bnbddict���`a(���`jprojection���aoa=���bs1a'���bs1epolar���bs1a'���`a)���`a,���`a ���`gfigsize���aoa=���`a(���bmia3���`a,���`a ���bmia3���`a)���`a)���`a
���`ar���`a ���aoa=���`a ���`bnp���aoa.���`farange���`a(���bmia0���`a,���`a ���bmia1���`a,���`a ���bmfe0.001���`a)���`a
���`etheta���`a ���aoa=���`a ���bmia2���aoa*���bmia2���aoa*���`bnp���aoa.���`bpi���aoa*���`ar���`a
���`dline���`a,���`a ���aoa=���`a ���`bax���aoa.���`dplot���`a(���`etheta���`a,���`a ���`ar���`a)���`a
���`a
���`cind���`a ���aoa=���`a ���bmic800���`a
���`ethisr���`a,���`a ���`ithistheta���`a ���aoa=���`a ���`ar���`a[���`cind���`a]���`a,���`a ���`etheta���`a[���`cind���`a]���`a
���`bax���aoa.���`dplot���`a(���`a[���`ithistheta���`a]���`a,���`a ���`a[���`ethisr���`a]���`a,���`a ���bs1a'���bs1ao���bs1a'���`a)���`a
���`bax���aoa.���`hannotate���`a(���bs1a'���bs1ra polar annotation���bs1a'���`a,���`a
���`l            ���`bxy���aoa=���`a(���`ithistheta���`a,���`a ���`ethisr���`a)���`a,���`b  ���bc1o# theta, radius���`a
���`l            ���`fxytext���aoa=���`a(���bmfd0.05���`a,���`a ���bmfd0.05���`a)���`a,���`d    ���bc1t# fraction, fraction���`a
���`l            ���`jtextcoords���aoa=���bs1a'���bs1ofigure fraction���bs1a'���`a,���`a
���`l            ���`jarrowprops���aoa=���bnbddict���`a(���`ifacecolor���aoa=���bs1a'���bs1eblack���bs1a'���`a,���`a ���`fshrink���aoa=���bmfd0.05���`a)���`a,���`a
���`l            ���`shorizontalalignment���aoa=���bs1a'���bs1dleft���bs1a'���`a,���`a
���`l            ���`qverticalalignment���aoa=���bs1a'���bs1fbottom���bs1a'���`a)���`a
���`a
���bc1xM#############################################################################���`a
���bc1xG# You can also use polar notation on a cartesian axes.  Here the native���`a
���bc1xE# coordinate system ('data') is cartesian, so you need to specify the���`a
���bc1xH# xycoords and textcoords as 'polar' if you want to use (theta, radius).���`a
���`a
���`bel���`a ���aoa=���`a ���`gEllipse���`a(���`a(���bmia0���`a,���`a ���bmia0���`a)���`a,���`a ���bmib10���`a,���`a ���bmib20���`a,���`a ���`ifacecolor���aoa=���bs1a'���bs1ar���bs1a'���`a,���`a ���`ealpha���aoa=���bmfc0.5���`a)���`a
���`a
���`cfig���`a,���`a ���`bax���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`jsubplot_kw���aoa=���bnbddict���`a(���`faspect���aoa=���bs1a'���bs1eequal���bs1a'���`a)���`a)���`a
���`bax���aoa.���`jadd_artist���`a(���`bel���`a)���`a
���`bel���aoa.���`lset_clip_box���`a(���`bax���aoa.���`dbbox���`a)���`a
���`bax���aoa.���`hannotate���`a(���bs1a'���bs1gthe top���bs1a'���`a,���`a
���`l            ���`bxy���aoa=���`a(���`bnp���aoa.���`bpi���aoa/���bmfb2.���`a,���`a ���bmfc10.���`a)���`a,���`f      ���bc1o# theta, radius���`a
���`l            ���`fxytext���aoa=���`a(���`bnp���aoa.���`bpi���aoa/���bmia3���`a,���`a ���bmfc20.���`a)���`a,���`c   ���bc1o# theta, radius���`a
���`l            ���`hxycoords���aoa=���bs1a'���bs1epolar���bs1a'���`a,���`a
���`l            ���`jtextcoords���aoa=���bs1a'���bs1epolar���bs1a'���`a,���`a
���`l            ���`jarrowprops���aoa=���bnbddict���`a(���`ifacecolor���aoa=���bs1a'���bs1eblack���bs1a'���`a,���`a ���`fshrink���aoa=���bmfd0.05���`a)���`a,���`a
���`l            ���`shorizontalalignment���aoa=���bs1a'���bs1dleft���bs1a'���`a,���`a
���`l            ���`qverticalalignment���aoa=���bs1a'���bs1fbottom���bs1a'���`a,���`a
���`l            ���`gclip_on���aoa=���bkcdTrue���`a)���`b  ���bc1x# clip to the axes bounding box���`a
���`a
���`bax���aoa.���`cset���`a(���`dxlim���aoa=���`a[���aoa-���bmib20���`a,���`a ���bmib20���`a]���`a,���`a ���`dylim���aoa=���`a[���aoa-���bmib20���`a,���`a ���bmib20���`a]���`a)���`a
���`a
���`a
���bc1xO###############################################################################���`a
���bc1x%# Customizing arrow and bubble styles���`a
���bc1x%# -----------------------------------���`a
���bc1a#���`a
���bc1xL# The arrow between *xytext* and the annotation point, as well as the bubble���`a
���bc1xK# that covers the annotation text, are highly customizable. Below are a few���`a
���bc1x6# parameter options as well as their resulting output.���`a
���`a
���`cfig���`a,���`a ���`bax���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`gfigsize���aoa=���`a(���bmia8���`a,���`a ���bmia5���`a)���`a)���`a
���`a
���`at���`a ���aoa=���`a ���`bnp���aoa.���`farange���`a(���bmfc0.0���`a,���`a ���bmfc5.0���`a,���`a ���bmfd0.01���`a)���`a
���`as���`a ���aoa=���`a ���`bnp���aoa.���`ccos���`a(���bmia2���aoa*���`bnp���aoa.���`bpi���aoa*���`at���`a)���`a
���`dline���`a,���`a ���aoa=���`a ���`bax���aoa.���`dplot���`a(���`at���`a,���`a ���`as���`a,���`a ���`blw���aoa=���bmia3���`a)���`a
���`a
���`bax���aoa.���`hannotate���`a(���`a
���`d    ���bs1a'���bs1hstraight���bs1a'���`a,���`a
���`d    ���`bxy���aoa=���`a(���bmia0���`a,���`a ���bmia1���`a)���`a,���`a ���`hxycoords���aoa=���bs1a'���bs1ddata���bs1a'���`a,���`a
���`d    ���`fxytext���aoa=���`a(���aoa-���bmib50���`a,���`a ���bmib30���`a)���`a,���`a ���`jtextcoords���aoa=���bs1a'���bs1moffset points���bs1a'���`a,���`a
���`d    ���`jarrowprops���aoa=���bnbddict���`a(���`jarrowstyle���aoa=���bs2a"���bs2b->���bs2a"���`a)���`a)���`a
���`bax���aoa.���`hannotate���`a(���`a
���`d    ���bs1a'���bs1earc3,���bseb\n���bs1grad 0.2���bs1a'���`a,���`a
���`d    ���`bxy���aoa=���`a(���bmfc0.5���`a,���`a ���aoa-���bmia1���`a)���`a,���`a ���`hxycoords���aoa=���bs1a'���bs1ddata���bs1a'���`a,���`a
���`d    ���`fxytext���aoa=���`a(���aoa-���bmib80���`a,���`a ���aoa-���bmib60���`a)���`a,���`a ���`jtextcoords���aoa=���bs1a'���bs1moffset points���bs1a'���`a,���`a
���`d    ���`jarrowprops���aoa=���bnbddict���`a(���`jarrowstyle���aoa=���bs2a"���bs2b->���bs2a"���`a,���`a
���`t                    ���`oconnectionstyle���aoa=���bs2a"���bs2karc3,rad=.2���bs2a"���`a)���`a)���`a
���`bax���aoa.���`hannotate���`a(���`a
���`d    ���bs1a'���bs1darc,���bseb\n���bs1hangle 50���bs1a'���`a,���`a
���`d    ���`bxy���aoa=���`a(���bmfb1.���`a,���`a ���bmia1���`a)���`a,���`a ���`hxycoords���aoa=���bs1a'���bs1ddata���bs1a'���`a,���`a
���`d    ���`fxytext���aoa=���`a(���aoa-���bmib90���`a,���`a ���bmib50���`a)���`a,���`a ���`jtextcoords���aoa=���bs1a'���bs1moffset points���bs1a'���`a,���`a
���`d    ���`jarrowprops���aoa=���bnbddict���`a(���`jarrowstyle���aoa=���bs2a"���bs2b->���bs2a"���`a,���`a
���`t                    ���`oconnectionstyle���aoa=���bs2a"���bs2xarc,angleA=0,armA=50,rad=10���bs2a"���`a)���`a)���`a
���`bax���aoa.���`hannotate���`a(���`a
���`d    ���bs1a'���bs1darc,���bseb\n���bs1darms���bs1a'���`a,���`a
���`d    ���`bxy���aoa=���`a(���bmfc1.5���`a,���`a ���aoa-���bmia1���`a)���`a,���`a ���`hxycoords���aoa=���bs1a'���bs1ddata���bs1a'���`a,���`a
���`d    ���`fxytext���aoa=���`a(���aoa-���bmib80���`a,���`a ���aoa-���bmib60���`a)���`a,���`a ���`jtextcoords���aoa=���bs1a'���bs1moffset points���bs1a'���`a,���`a
���`d    ���`jarrowprops���aoa=���bnbddict���`a(���`a
���`h        ���`jarrowstyle���aoa=���bs2a"���bs2b->���bs2a"���`a,���`a
���`h        ���`oconnectionstyle���aoa=���bs2a"���bs2x-arc,angleA=0,armA=40,angleB=-90,armB=30,rad=7���bs2a"���`a)���`a)���`a
���`bax���aoa.���`hannotate���`a(���`a
���`d    ���bs1a'���bs1fangle,���bseb\n���bs1hangle 90���bs1a'���`a,���`a
���`d    ���`bxy���aoa=���`a(���bmfb2.���`a,���`a ���bmia1���`a)���`a,���`a ���`hxycoords���aoa=���bs1a'���bs1ddata���bs1a'���`a,���`a
���`d    ���`fxytext���aoa=���`a(���aoa-���bmib70���`a,���`a ���bmib30���`a)���`a,���`a ���`jtextcoords���aoa=���bs1a'���bs1moffset points���bs1a'���`a,���`a
���`d    ���`jarrowprops���aoa=���bnbddict���`a(���`jarrowstyle���aoa=���bs2a"���bs2b->���bs2a"���`a,���`a
���`t                    ���`oconnectionstyle���aoa=���bs2a"���bs2xangle,angleA=0,angleB=90,rad=10���bs2a"���`a)���`a)���`a
���`bax���aoa.���`hannotate���`a(���`a
���`d    ���bs1a'���bs1gangle3,���bseb\n���bs1iangle -90���bs1a'���`a,���`a
���`d    ���`bxy���aoa=���`a(���bmfc2.5���`a,���`a ���aoa-���bmia1���`a)���`a,���`a ���`hxycoords���aoa=���bs1a'���bs1ddata���bs1a'���`a,���`a
���`d    ���`fxytext���aoa=���`a(���aoa-���bmib80���`a,���`a ���aoa-���bmib60���`a)���`a,���`a ���`jtextcoords���aoa=���bs1a'���bs1moffset points���bs1a'���`a,���`a
���`d    ���`jarrowprops���aoa=���bnbddict���`a(���`jarrowstyle���aoa=���bs2a"���bs2b->���bs2a"���`a,���`a
���`t                    ���`oconnectionstyle���aoa=���bs2a"���bs2xangle3,angleA=0,angleB=-90���bs2a"���`a)���`a)���`a
���`bax���aoa.���`hannotate���`a(���`a
���`d    ���bs1a'���bs1fangle,���bseb\n���bs1eround���bs1a'���`a,���`a
���`d    ���`bxy���aoa=���`a(���bmfb3.���`a,���`a ���bmia1���`a)���`a,���`a ���`hxycoords���aoa=���bs1a'���bs1ddata���bs1a'���`a,���`a
���`d    ���`fxytext���aoa=���`a(���aoa-���bmib60���`a,���`a ���bmib30���`a)���`a,���`a ���`jtextcoords���aoa=���bs1a'���bs1moffset points���bs1a'���`a,���`a
���`d    ���`dbbox���aoa=���bnbddict���`a(���`hboxstyle���aoa=���bs2a"���bs2eround���bs2a"���`a,���`a ���`bfc���aoa=���bs2a"���bs2c0.8���bs2a"���`a)���`a,���`a
���`d    ���`jarrowprops���aoa=���bnbddict���`a(���`jarrowstyle���aoa=���bs2a"���bs2b->���bs2a"���`a,���`a
���`t                    ���`oconnectionstyle���aoa=���bs2a"���bs2xangle,angleA=0,angleB=90,rad=10���bs2a"���`a)���`a)���`a
���`bax���aoa.���`hannotate���`a(���`a
���`d    ���bs1a'���bs1fangle,���bseb\n���bs1fround4���bs1a'���`a,���`a
���`d    ���`bxy���aoa=���`a(���bmfc3.5���`a,���`a ���aoa-���bmia1���`a)���`a,���`a ���`hxycoords���aoa=���bs1a'���bs1ddata���bs1a'���`a,���`a
���`d    ���`fxytext���aoa=���`a(���aoa-���bmib70���`a,���`a ���aoa-���bmib80���`a)���`a,���`a ���`jtextcoords���aoa=���bs1a'���bs1moffset points���bs1a'���`a,���`a
���`d    ���`dsize���aoa=���bmib20���`a,���`a
���`d    ���`dbbox���aoa=���bnbddict���`a(���`hboxstyle���aoa=���bs2a"���bs2mround4,pad=.5���bs2a"���`a,���`a ���`bfc���aoa=���bs2a"���bs2c0.8���bs2a"���`a)���`a,���`a
���`d    ���`jarrowprops���aoa=���bnbddict���`a(���`jarrowstyle���aoa=���bs2a"���bs2b->���bs2a"���`a,���`a
���`t                    ���`oconnectionstyle���aoa=���bs2a"���bs2x angle,angleA=0,angleB=-90,rad=10���bs2a"���`a)���`a)���`a
���`bax���aoa.���`hannotate���`a(���`a
���`d    ���bs1a'���bs1fangle,���bseb\n���bs1fshrink���bs1a'���`a,���`a
���`d    ���`bxy���aoa=���`a(���bmfb4.���`a,���`a ���bmia1���`a)���`a,���`a ���`hxycoords���aoa=���bs1a'���bs1ddata���bs1a'���`a,���`a
���`d    ���`fxytext���aoa=���`a(���aoa-���bmib60���`a,���`a ���bmib30���`a)���`a,���`a ���`jtextcoords���aoa=���bs1a'���bs1moffset points���bs1a'���`a,���`a
���`d    ���`dbbox���aoa=���bnbddict���`a(���`hboxstyle���aoa=���bs2a"���bs2eround���bs2a"���`a,���`a ���`bfc���aoa=���bs2a"���bs2c0.8���bs2a"���`a)���`a,���`a
���`d    ���`jarrowprops���aoa=���bnbddict���`a(���`jarrowstyle���aoa=���bs2a"���bs2b->���bs2a"���`a,���`a
���`t                    ���`gshrinkA���aoa=���bmia0���`a,���`a ���`gshrinkB���aoa=���bmib10���`a,���`a
���`t                    ���`oconnectionstyle���aoa=���bs2a"���bs2xangle,angleA=0,angleB=90,rad=10���bs2a"���`a)���`a)���`a
���bc1xE# You can pass an empty string to get only annotation arrows rendered���`a
���`bax���aoa.���`hannotate���`a(���bs1a'���bs1a'���`a,���`a ���`bxy���aoa=���`a(���bmfb4.���`a,���`a ���bmfb1.���`a)���`a,���`a ���`hxycoords���aoa=���bs1a'���bs1ddata���bs1a'���`a,���`a
���`l            ���`fxytext���aoa=���`a(���bmfc4.5���`a,���`a ���aoa-���bmia1���`a)���`a,���`a ���`jtextcoords���aoa=���bs1a'���bs1ddata���bs1a'���`a,���`a
���`l            ���`jarrowprops���aoa=���bnbddict���`a(���`jarrowstyle���aoa=���bs2a"���bs2c<->���bs2a"���`a,���`a
���`x                            ���`oconnectionstyle���aoa=���bs2a"���bs2cbar���bs2a"���`a,���`a
���`x                            ���`bec���aoa=���bs2a"���bs2ak���bs2a"���`a,���`a
���`x                            ���`gshrinkA���aoa=���bmia5���`a,���`a ���`gshrinkB���aoa=���bmia5���`a)���`a)���`a
���`a
���`bax���aoa.���`cset���`a(���`dxlim���aoa=���`a(���aoa-���bmia1���`a,���`a ���bmia5���`a)���`a,���`a ���`dylim���aoa=���`a(���aoa-���bmia4���`a,���`a ���bmia3���`a)���`a)���`a
���`a
���bc1xM#############################################################################���`a
���bc1xB# We'll create another figure so that it doesn't get too cluttered���`a
���`cfig���`a,���`a ���`bax���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`a)���`a
���`a
���`bel���`a ���aoa=���`a ���`gEllipse���`a(���`a(���bmia2���`a,���`a ���aoa-���bmia1���`a)���`a,���`a ���bmfc0.5���`a,���`a ���bmfc0.5���`a)���`a
���`bax���aoa.���`iadd_patch���`a(���`bel���`a)���`a
���`a
���`bax���aoa.���`hannotate���`a(���bs1a'���bs1d$->$���bs1a'���`a,���`a
���`l            ���`bxy���aoa=���`a(���bmfb2.���`a,���`a ���aoa-���bmia1���`a)���`a,���`a ���`hxycoords���aoa=���bs1a'���bs1ddata���bs1a'���`a,���`a
���`l            ���`fxytext���aoa=���`a(���aoa-���bmic150���`a,���`a ���aoa-���bmic140���`a)���`a,���`a ���`jtextcoords���aoa=���bs1a'���bs1moffset points���bs1a'���`a,���`a
���`l            ���`dbbox���aoa=���bnbddict���`a(���`hboxstyle���aoa=���bs2a"���bs2eround���bs2a"���`a,���`a ���`bfc���aoa=���bs2a"���bs2c0.8���bs2a"���`a)���`a,���`a
���`l            ���`jarrowprops���aoa=���bnbddict���`a(���`jarrowstyle���aoa=���bs2a"���bs2b->���bs2a"���`a,���`a
���`x                            ���`fpatchB���aoa=���`bel���`a,���`a
���`x                            ���`oconnectionstyle���aoa=���bs2a"���bs2xangle,angleA=90,angleB=0,rad=10���bs2a"���`a)���`a)���`a
���`bax���aoa.���`hannotate���`a(���bs1a'���bs1earrow���bseb\n���bs1efancy���bs1a'���`a,���`a
���`l            ���`bxy���aoa=���`a(���bmfb2.���`a,���`a ���aoa-���bmia1���`a)���`a,���`a ���`hxycoords���aoa=���bs1a'���bs1ddata���bs1a'���`a,���`a
���`l            ���`fxytext���aoa=���`a(���aoa-���bmic100���`a,���`a ���bmib60���`a)���`a,���`a ���`jtextcoords���aoa=���bs1a'���bs1moffset points���bs1a'���`a,���`a
���`l            ���`dsize���aoa=���bmib20���`a,���`a
���`l            ���bc1x(# bbox=dict(boxstyle="round", fc="0.8"),���`a
���`l            ���`jarrowprops���aoa=���bnbddict���`a(���`jarrowstyle���aoa=���bs2a"���bs2efancy���bs2a"���`a,���`a
���`x                            ���`bfc���aoa=���bs2a"���bs2c0.6���bs2a"���`a,���`a ���`bec���aoa=���bs2a"���bs2dnone���bs2a"���`a,���`a
���`x                            ���`fpatchB���aoa=���`bel���`a,���`a
���`x                            ���`oconnectionstyle���aoa=���bs2a"���bs2xangle3,angleA=0,angleB=-90���bs2a"���`a)���`a)���`a
���`bax���aoa.���`hannotate���`a(���bs1a'���bs1earrow���bseb\n���bs1fsimple���bs1a'���`a,���`a
���`l            ���`bxy���aoa=���`a(���bmfb2.���`a,���`a ���aoa-���bmia1���`a)���`a,���`a ���`hxycoords���aoa=���bs1a'���bs1ddata���bs1a'���`a,���`a
���`l            ���`fxytext���aoa=���`a(���bmic100���`a,���`a ���bmib60���`a)���`a,���`a ���`jtextcoords���aoa=���bs1a'���bs1moffset points���bs1a'���`a,���`a
���`l            ���`dsize���aoa=���bmib20���`a,���`a
���`l            ���bc1x(# bbox=dict(boxstyle="round", fc="0.8"),���`a
���`l            ���`jarrowprops���aoa=���bnbddict���`a(���`jarrowstyle���aoa=���bs2a"���bs2fsimple���bs2a"���`a,���`a
���`x                            ���`bfc���aoa=���bs2a"���bs2c0.6���bs2a"���`a,���`a ���`bec���aoa=���bs2a"���bs2dnone���bs2a"���`a,���`a
���`x                            ���`fpatchB���aoa=���`bel���`a,���`a
���`x                            ���`oconnectionstyle���aoa=���bs2a"���bs2larc3,rad=0.3���bs2a"���`a)���`a)���`a
���`bax���aoa.���`hannotate���`a(���bs1a'���bs1ewedge���bs1a'���`a,���`a
���`l            ���`bxy���aoa=���`a(���bmfb2.���`a,���`a ���aoa-���bmia1���`a)���`a,���`a ���`hxycoords���aoa=���bs1a'���bs1ddata���bs1a'���`a,���`a
���`l            ���`fxytext���aoa=���`a(���aoa-���bmic100���`a,���`a ���aoa-���bmic100���`a)���`a,���`a ���`jtextcoords���aoa=���bs1a'���bs1moffset points���bs1a'���`a,���`a
���`l            ���`dsize���aoa=���bmib20���`a,���`a
���`l            ���bc1x(# bbox=dict(boxstyle="round", fc="0.8"),���`a
���`l            ���`jarrowprops���aoa=���bnbddict���`a(���`jarrowstyle���aoa=���bs2a"���bs2twedge,tail_width=0.7���bs2a"���`a,���`a
���`x                            ���`bfc���aoa=���bs2a"���bs2c0.6���bs2a"���`a,���`a ���`bec���aoa=���bs2a"���bs2dnone���bs2a"���`a,���`a
���`x                            ���`fpatchB���aoa=���`bel���`a,���`a
���`x                            ���`oconnectionstyle���aoa=���bs2a"���bs2marc3,rad=-0.3���bs2a"���`a)���`a)���`a
���`bax���aoa.���`hannotate���`a(���bs1a'���bs1gbubble,���bseb\n���bs1hcontours���bs1a'���`a,���`a
���`l            ���`bxy���aoa=���`a(���bmfb2.���`a,���`a ���aoa-���bmia1���`a)���`a,���`a ���`hxycoords���aoa=���bs1a'���bs1ddata���bs1a'���`a,���`a
���`l            ���`fxytext���aoa=���`a(���bmia0���`a,���`a ���aoa-���bmib70���`a)���`a,���`a ���`jtextcoords���aoa=���bs1a'���bs1moffset points���bs1a'���`a,���`a
���`l            ���`dsize���aoa=���bmib20���`a,���`a
���`l            ���`dbbox���aoa=���bnbddict���`a(���`hboxstyle���aoa=���bs2a"���bs2eround���bs2a"���`a,���`a
���`v                      ���`bfc���aoa=���`a(���bmfc1.0���`a,���`a ���bmfc0.7���`a,���`a ���bmfc0.7���`a)���`a,���`a
���`v                      ���`bec���aoa=���`a(���bmfb1.���`a,���`a ���bmfb.5���`a,���`a ���bmfb.5���`a)���`a)���`a,���`a
���`l            ���`jarrowprops���aoa=���bnbddict���`a(���`jarrowstyle���aoa=���bs2a"���bs2swedge,tail_width=1.���bs2a"���`a,���`a
���`x                            ���`bfc���aoa=���`a(���bmfc1.0���`a,���`a ���bmfc0.7���`a,���`a ���bmfc0.7���`a)���`a,���`a ���`bec���aoa=���`a(���bmfb1.���`a,���`a ���bmfb.5���`a,���`a ���bmfb.5���`a)���`a,���`a
���`x                            ���`fpatchA���aoa=���bkcdNone���`a,���`a
���`x                            ���`fpatchB���aoa=���`bel���`a,���`a
���`x                            ���`frelpos���aoa=���`a(���bmfc0.2���`a,���`a ���bmfc0.8���`a)���`a,���`a
���`x                            ���`oconnectionstyle���aoa=���bs2a"���bs2marc3,rad=-0.1���bs2a"���`a)���`a)���`a
���`bax���aoa.���`hannotate���`a(���bs1a'���bs1fbubble���bs1a'���`a,���`a
���`l            ���`bxy���aoa=���`a(���bmfb2.���`a,���`a ���aoa-���bmia1���`a)���`a,���`a ���`hxycoords���aoa=���bs1a'���bs1ddata���bs1a'���`a,���`a
���`l            ���`fxytext���aoa=���`a(���bmib55���`a,���`a ���bmia0���`a)���`a,���`a ���`jtextcoords���aoa=���bs1a'���bs1moffset points���bs1a'���`a,���`a
���`l            ���`dsize���aoa=���bmib20���`a,���`a ���`bva���aoa=���bs2a"���bs2fcenter���bs2a"���`a,���`a
���`l            ���`dbbox���aoa=���bnbddict���`a(���`hboxstyle���aoa=���bs2a"���bs2eround���bs2a"���`a,���`a ���`bfc���aoa=���`a(���bmfc1.0���`a,���`a ���bmfc0.7���`a,���`a ���bmfc0.7���`a)���`a,���`a ���`bec���aoa=���bs2a"���bs2dnone���bs2a"���`a)���`a,���`a
���`l            ���`jarrowprops���aoa=���bnbddict���`a(���`jarrowstyle���aoa=���bs2a"���bs2swedge,tail_width=1.���bs2a"���`a,���`a
���`x                            ���`bfc���aoa=���`a(���bmfc1.0���`a,���`a ���bmfc0.7���`a,���`a ���bmfc0.7���`a)���`a,���`a ���`bec���aoa=���bs2a"���bs2dnone���bs2a"���`a,���`a
���`x                            ���`fpatchA���aoa=���bkcdNone���`a,���`a
���`x                            ���`fpatchB���aoa=���`bel���`a,���`a
���`x                            ���`frelpos���aoa=���`a(���bmfc0.2���`a,���`a ���bmfc0.5���`a)���`a)���`a)���`a
���`a
���`bax���aoa.���`cset���`a(���`dxlim���aoa=���`a(���aoa-���bmia1���`a,���`a ���bmia5���`a)���`a,���`a ���`dylim���aoa=���`a(���aoa-���bmia5���`a,���`a ���bmia3���`a)���`a)���`a
���`a
���bc1xO###############################################################################���`a
���bc1x%# More examples of coordinate systems���`a
���bc1x%# -----------------------------------���`a
���bc1a#���`a
���bc1xH# Below we'll show a few more examples of coordinate systems and how the���`a
���bc1x+# location of annotations may be specified.���`a
���`a
���`cfig���`a,���`a ���`a(���`cax1���`a,���`a ���`cax2���`a)���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���bmia1���`a,���`a ���bmia2���`a)���`a
���`a
���`ibbox_args���`a ���aoa=���`a ���bnbddict���`a(���`hboxstyle���aoa=���bs2a"���bs2eround���bs2a"���`a,���`a ���`bfc���aoa=���bs2a"���bs2c0.8���bs2a"���`a)���`a
���`jarrow_args���`a ���aoa=���`a ���bnbddict���`a(���`jarrowstyle���aoa=���bs2a"���bs2b->���bs2a"���`a)���`a
���`a
���bc1xE# Here we'll demonstrate the extents of the coordinate system and how���`a
���bc1x# we place annotating text.���`a
���`a
���`cax1���aoa.���`hannotate���`a(���bs1a'���bs1vfigure fraction : 0, 0���bs1a'���`a,���`a ���`bxy���aoa=���`a(���bmia0���`a,���`a ���bmia0���`a)���`a,���`a ���`hxycoords���aoa=���bs1a'���bs1ofigure fraction���bs1a'���`a,���`a
���`m             ���`fxytext���aoa=���`a(���bmib20���`a,���`a ���bmib20���`a)���`a,���`a ���`jtextcoords���aoa=���bs1a'���bs1moffset points���bs1a'���`a,���`a
���`m             ���`bha���aoa=���bs2a"���bs2dleft���bs2a"���`a,���`a ���`bva���aoa=���bs2a"���bs2fbottom���bs2a"���`a,���`a
���`m             ���`dbbox���aoa=���`ibbox_args���`a,���`a
���`m             ���`jarrowprops���aoa=���`jarrow_args���`a)���`a
���`a
���`cax1���aoa.���`hannotate���`a(���bs1a'���bs1vfigure fraction : 1, 1���bs1a'���`a,���`a ���`bxy���aoa=���`a(���bmia1���`a,���`a ���bmia1���`a)���`a,���`a ���`hxycoords���aoa=���bs1a'���bs1ofigure fraction���bs1a'���`a,���`a
���`m             ���`fxytext���aoa=���`a(���aoa-���bmib20���`a,���`a ���aoa-���bmib20���`a)���`a,���`a ���`jtextcoords���aoa=���bs1a'���bs1moffset points���bs1a'���`a,���`a
���`m             ���`bha���aoa=���bs2a"���bs2eright���bs2a"���`a,���`a ���`bva���aoa=���bs2a"���bs2ctop���bs2a"���`a,���`a
���`m             ���`dbbox���aoa=���`ibbox_args���`a,���`a
���`m             ���`jarrowprops���aoa=���`jarrow_args���`a)���`a
���`a
���`cax1���aoa.���`hannotate���`a(���bs1a'���bs1taxes fraction : 0, 0���bs1a'���`a,���`a ���`bxy���aoa=���`a(���bmia0���`a,���`a ���bmia0���`a)���`a,���`a ���`hxycoords���aoa=���bs1a'���bs1maxes fraction���bs1a'���`a,���`a
���`m             ���`fxytext���aoa=���`a(���bmib20���`a,���`a ���bmib20���`a)���`a,���`a ���`jtextcoords���aoa=���bs1a'���bs1moffset points���bs1a'���`a,���`a
���`m             ���`bha���aoa=���bs2a"���bs2dleft���bs2a"���`a,���`a ���`bva���aoa=���bs2a"���bs2fbottom���bs2a"���`a,���`a
���`m             ���`dbbox���aoa=���`ibbox_args���`a,���`a
���`m             ���`jarrowprops���aoa=���`jarrow_args���`a)���`a
���`a
���`cax1���aoa.���`hannotate���`a(���bs1a'���bs1taxes fraction : 1, 1���bs1a'���`a,���`a ���`bxy���aoa=���`a(���bmia1���`a,���`a ���bmia1���`a)���`a,���`a ���`hxycoords���aoa=���bs1a'���bs1maxes fraction���bs1a'���`a,���`a
���`m             ���`fxytext���aoa=���`a(���aoa-���bmib20���`a,���`a ���aoa-���bmib20���`a)���`a,���`a ���`jtextcoords���aoa=���bs1a'���bs1moffset points���bs1a'���`a,���`a
���`m             ���`bha���aoa=���bs2a"���bs2eright���bs2a"���`a,���`a ���`bva���aoa=���bs2a"���bs2ctop���bs2a"���`a,���`a
���`m             ���`dbbox���aoa=���`ibbox_args���`a,���`a
���`m             ���`jarrowprops���aoa=���`jarrow_args���`a)���`a
���`a
���bc1x7# It is also possible to generate draggable annotations���`a
���`a
���`can1���`a ���aoa=���`a ���`cax1���aoa.���`hannotate���`a(���bs1a'���bs1iDrag me 1���bs1a'���`a,���`a ���`bxy���aoa=���`a(���bmfb.5���`a,���`a ���bmfb.7���`a)���`a,���`a ���`hxycoords���aoa=���bs1a'���bs1ddata���bs1a'���`a,���`a
���`s                   ���`bha���aoa=���bs2a"���bs2fcenter���bs2a"���`a,���`a ���`bva���aoa=���bs2a"���bs2fcenter���bs2a"���`a,���`a
���`s                   ���`dbbox���aoa=���`ibbox_args���`a)���`a
���`a
���`can2���`a ���aoa=���`a ���`cax1���aoa.���`hannotate���`a(���bs1a'���bs1iDrag me 2���bs1a'���`a,���`a ���`bxy���aoa=���`a(���bmfb.5���`a,���`a ���bmfb.5���`a)���`a,���`a ���`hxycoords���aoa=���`can1���`a,���`a
���`s                   ���`fxytext���aoa=���`a(���bmfb.5���`a,���`a ���bmfb.3���`a)���`a,���`a ���`jtextcoords���aoa=���bs1a'���bs1maxes fraction���bs1a'���`a,���`a
���`s                   ���`bha���aoa=���bs2a"���bs2fcenter���bs2a"���`a,���`a ���`bva���aoa=���bs2a"���bs2fcenter���bs2a"���`a,���`a
���`s                   ���`dbbox���aoa=���`ibbox_args���`a,���`a
���`s                   ���`jarrowprops���aoa=���bnbddict���`a(���`fpatchB���aoa=���`can1���aoa.���`nget_bbox_patch���`a(���`a)���`a,���`a
���`x#                                   ���`oconnectionstyle���aoa=���bs2a"���bs2larc3,rad=0.2���bs2a"���`a,���`a
���`x#                                   ���aoa*���aoa*���`jarrow_args���`a)���`a)���`a
���`can1���aoa.���`idraggable���`a(���`a)���`a
���`can2���aoa.���`idraggable���`a(���`a)���`a
���`a
���`can3���`a ���aoa=���`a ���`cax1���aoa.���`hannotate���`a(���bs1a'���bs1a'���`a,���`a ���`bxy���aoa=���`a(���bmfb.5���`a,���`a ���bmfb.5���`a)���`a,���`a ���`hxycoords���aoa=���`can2���`a,���`a
���`s                   ���`fxytext���aoa=���`a(���bmfb.5���`a,���`a ���bmfb.5���`a)���`a,���`a ���`jtextcoords���aoa=���`can1���`a,���`a
���`s                   ���`bha���aoa=���bs2a"���bs2fcenter���bs2a"���`a,���`a ���`bva���aoa=���bs2a"���bs2fcenter���bs2a"���`a,���`a
���`s                   ���`dbbox���aoa=���`ibbox_args���`a,���`a
���`s                   ���`jarrowprops���aoa=���bnbddict���`a(���`fpatchA���aoa=���`can1���aoa.���`nget_bbox_patch���`a(���`a)���`a,���`a
���`x#                                   ���`fpatchB���aoa=���`can2���aoa.���`nget_bbox_patch���`a(���`a)���`a,���`a
���`x#                                   ���`oconnectionstyle���aoa=���bs2a"���bs2larc3,rad=0.2���bs2a"���`a,���`a
���`x#                                   ���aoa*���aoa*���`jarrow_args���`a)���`a)���`a
���`a
���bc1xC# Finally we'll show off some more complex annotation and placement���`a
���`a
���`dtext���`a ���aoa=���`a ���`cax2���aoa.���`hannotate���`a(���bs1a'���bs1ixy=(0, 1)���bseb\n���bs1jxycoords=(���bs1a"���bs1ddata���bs1a"���bs1b, ���bs1a"���bs1maxes fraction���bs1a"���bs1a)���bs1a'���`a,���`a
���`t                    ���`bxy���aoa=���`a(���bmia0���`a,���`a ���bmia1���`a)���`a,���`a ���`hxycoords���aoa=���`a(���bs2a"���bs2ddata���bs2a"���`a,���`a ���bs1a'���bs1maxes fraction���bs1a'���`a)���`a,���`a
���`t                    ���`fxytext���aoa=���`a(���bmia0���`a,���`a ���aoa-���bmib20���`a)���`a,���`a ���`jtextcoords���aoa=���bs1a'���bs1moffset points���bs1a'���`a,���`a
���`t                    ���`bha���aoa=���bs2a"���bs2fcenter���bs2a"���`a,���`a ���`bva���aoa=���bs2a"���bs2ctop���bs2a"���`a,���`a
���`t                    ���`dbbox���aoa=���`ibbox_args���`a,���`a
���`t                    ���`jarrowprops���aoa=���`jarrow_args���`a)���`a
���`a
���`cax2���aoa.���`hannotate���`a(���bs1a'���bs1kxy=(0.5, 0)���bseb\n���bs1oxycoords=artist���bs1a'���`a,���`a
���`m             ���`bxy���aoa=���`a(���bmfc0.5���`a,���`a ���bmfb0.���`a)���`a,���`a ���`hxycoords���aoa=���`dtext���`a,���`a
���`m             ���`fxytext���aoa=���`a(���bmia0���`a,���`a ���aoa-���bmib20���`a)���`a,���`a ���`jtextcoords���aoa=���bs1a'���bs1moffset points���bs1a'���`a,���`a
���`m             ���`bha���aoa=���bs2a"���bs2fcenter���bs2a"���`a,���`a ���`bva���aoa=���bs2a"���bs2ctop���bs2a"���`a,���`a
���`m             ���`dbbox���aoa=���`ibbox_args���`a,���`a
���`m             ���`jarrowprops���aoa=���`jarrow_args���`a)���`a
���`a
���`cax2���aoa.���`hannotate���`a(���bs1a'���bs1mxy=(0.8, 0.5)���bseb\n���bs1vxycoords=ax1.transData���bs1a'���`a,���`a
���`m             ���`bxy���aoa=���`a(���bmfc0.8���`a,���`a ���bmfc0.5���`a)���`a,���`a ���`hxycoords���aoa=���`cax1���aoa.���`itransData���`a,���`a
���`m             ���`fxytext���aoa=���`a(���bmib10���`a,���`a ���bmib10���`a)���`a,���`a
���`m             ���`jtextcoords���aoa=���`jOffsetFrom���`a(���`cax2���aoa.���`dbbox���`a,���`a ���`a(���bmia0���`a,���`a ���bmia0���`a)���`a,���`a ���bs2a"���bs2fpoints���bs2a"���`a)���`a,���`a
���`m             ���`bha���aoa=���bs2a"���bs2dleft���bs2a"���`a,���`a ���`bva���aoa=���bs2a"���bs2fbottom���bs2a"���`a,���`a
���`m             ���`dbbox���aoa=���`ibbox_args���`a,���`a
���`m             ���`jarrowprops���aoa=���`jarrow_args���`a)���`a
���`a
���`cax2���aoa.���`cset���`a(���`dxlim���aoa=���`a[���aoa-���bmia2���`a,���`a ���bmia2���`a]���`a,���`a ���`dylim���aoa=���`a[���aoa-���bmia2���`a,���`a ���bmia2���`a]���`a)���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
`dNone�