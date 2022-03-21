ŸØÇÅŸ¥Éô+Ÿ±Çbsdy§"""
================
Annotating Plots
================

The following examples show how it is possible to annotate plots in Matplotlib.
This includes highlighting specific points of interest and using various
visual tools to call attention to this point. For a more complete and in-depth
description of the annotation and text tools in Matplotlib, see the
:doc:`tutorial on annotation </tutorials/text/annotations>`.
"""Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±ÇbknfimportŸ±Ç`a Ÿ±ÇbnnŸ¢ÑjmatplotlibŸ†Ñjmatplotlibe3.5.1fmodulejmatplotlibfmoduleıŸ±Çbnna.Ÿ±ÇbnnfpyplotŸ±Ç`a Ÿ±ÇakbasŸ±Ç`a Ÿ±ÇbnncpltŸ±Ç`a
Ÿ±ÇbkndfromŸ±Ç`a Ÿ±ÇbnnŸ¢ÑjmatplotlibŸ†Ñjmatplotlibe3.5.1fmodulejmatplotlibfmoduleıŸ±Çbnna.Ÿ±ÇbnngpatchesŸ±Ç`a Ÿ±ÇbknfimportŸ±Ç`a Ÿ±Ç`gEllipseŸ±Ç`a
Ÿ±ÇbknfimportŸ±Ç`a Ÿ±ÇbnnŸ¢ÑenumpyŸ†Ñenumpyf1.22.3fmoduleenumpyfmoduleıŸ±Ç`a Ÿ±ÇakbasŸ±Ç`a Ÿ±ÇbnnbnpŸ±Ç`a
Ÿ±ÇbkndfromŸ±Ç`a Ÿ±ÇbnnŸ¢ÑjmatplotlibŸ†Ñjmatplotlibe3.5.1fmodulejmatplotlibfmoduleıŸ±Çbnna.Ÿ±ÇbnndtextŸ±Ç`a Ÿ±ÇbknfimportŸ±Ç`a Ÿ±Ç`jOffsetFromŸ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1xO###############################################################################Ÿ±Ç`a
Ÿ±Çbc1x.# Specifying text points and annotation pointsŸ±Ç`a
Ÿ±Çbc1x.# --------------------------------------------Ÿ±Ç`a
Ÿ±Çbc1a#Ÿ±Ç`a
Ÿ±Çbc1xL# You must specify an annotation point ``xy=(x, y)`` to annotate this point.Ÿ±Ç`a
Ÿ±Çbc1xO# Additionally, you may specify a text point ``xytext=(x, y)`` for the locationŸ±Ç`a
Ÿ±Çbc1xN# of the text for this annotation.  Optionally, you can specify the coordinateŸ±Ç`a
Ÿ±Çbc1xN# system of *xy* and *xytext* with one of the following strings for *xycoords*Ÿ±Ç`a
Ÿ±Çbc1x(# and *textcoords* (default is 'data')::Ÿ±Ç`a
Ÿ±Çbc1a#Ÿ±Ç`a
Ÿ±Çbc1xF#  'figure points'   : points from the lower left corner of the figureŸ±Ç`a
Ÿ±Çbc1xF#  'figure pixels'   : pixels from the lower left corner of the figureŸ±Ç`a
Ÿ±Çbc1xO#  'figure fraction' : (0, 0) is lower left of figure and (1, 1) is upper rightŸ±Ç`a
Ÿ±Çbc1x<#  'axes points'     : points from lower left corner of axesŸ±Ç`a
Ÿ±Çbc1x<#  'axes pixels'     : pixels from lower left corner of axesŸ±Ç`a
Ÿ±Çbc1xM#  'axes fraction'   : (0, 0) is lower left of axes and (1, 1) is upper rightŸ±Ç`a
Ÿ±Çbc1xF#  'offset points'   : Specify an offset (in points) from the xy valueŸ±Ç`a
Ÿ±Çbc1xF#  'offset pixels'   : Specify an offset (in pixels) from the xy valueŸ±Ç`a
Ÿ±Çbc1x:#  'data'            : use the axes data coordinate systemŸ±Ç`a
Ÿ±Çbc1a#Ÿ±Ç`a
Ÿ±Çbc1xL# Note: for physical coordinate systems (points or pixels) the origin is theŸ±Ç`a
Ÿ±Çbc1x'# (bottom, left) of the figure or axes.Ÿ±Ç`a
Ÿ±Çbc1a#Ÿ±Ç`a
Ÿ±Çbc1xD# Optionally, you can specify arrow properties which draws and arrowŸ±Ç`a
Ÿ±Çbc1xF# from the text to the annotated point by giving a dictionary of arrowŸ±Ç`a
Ÿ±Çbc1l# propertiesŸ±Ç`a
Ÿ±Çbc1a#Ÿ±Ç`a
Ÿ±Çbc1r# Valid keys are::Ÿ±Ç`a
Ÿ±Çbc1a#Ÿ±Ç`a
Ÿ±Çbc1x,#   width : the width of the arrow in pointsŸ±Ç`a
Ÿ±Çbc1xA#   frac  : the fraction of the arrow length occupied by the headŸ±Ç`a
Ÿ±Çbc1xA#   headwidth : the width of the base of the arrow head in pointsŸ±Ç`a
Ÿ±Çbc1x=#   shrink : move the tip and base some percent away from theŸ±Ç`a
Ÿ±Çbc1x%#            annotated point and textŸ±Ç`a
Ÿ±Çbc1x=#   any key for matplotlib.patches.polygon  (e.g., facecolor)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1x3# Create our figure and data we'll use for plottingŸ±Ç`a
Ÿ±Ç`cfigŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`baxŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`hsubplotsŸ±Ç`a(Ÿ±Ç`gfigsizeŸ±Çaoa=Ÿ±Ç`a(Ÿ±Çbmia3Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia3Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`atŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`farangeŸ±Ç`a(Ÿ±Çbmfc0.0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfc5.0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd0.01Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`asŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`ccosŸ±Ç`a(Ÿ±Çbmia2Ÿ±Çaoa*Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`bpiŸ±Çaoa*Ÿ±Ç`atŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1x-# Plot a line and add some simple annotationsŸ±Ç`a
Ÿ±Ç`dlineŸ±Ç`a,Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`dplotŸ±Ç`a(Ÿ±Ç`atŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`asŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`hannotateŸ±Ç`a(Ÿ±Çbs1a'Ÿ±Çbs1mfigure pixelsŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`l            Ÿ±Ç`bxyŸ±Çaoa=Ÿ±Ç`a(Ÿ±Çbmib10Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmib10Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`hxycoordsŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1mfigure pixelsŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`hannotateŸ±Ç`a(Ÿ±Çbs1a'Ÿ±Çbs1mfigure pointsŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`l            Ÿ±Ç`bxyŸ±Çaoa=Ÿ±Ç`a(Ÿ±Çbmib80Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmib80Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`hxycoordsŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1mfigure pointsŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`hannotateŸ±Ç`a(Ÿ±Çbs1a'Ÿ±Çbs1ofigure fractionŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`l            Ÿ±Ç`bxyŸ±Çaoa=Ÿ±Ç`a(Ÿ±Çbmfd.025Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd.975Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`hxycoordsŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1ofigure fractionŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`l            Ÿ±Ç`shorizontalalignmentŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1dleftŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`qverticalalignmentŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1ctopŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`l            Ÿ±Ç`hfontsizeŸ±Çaoa=Ÿ±Çbmib20Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1x=# The following examples show off how these arrows are drawn.Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`hannotateŸ±Ç`a(Ÿ±Çbs1a'Ÿ±Çbs1vpoint offset from dataŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`l            Ÿ±Ç`bxyŸ±Çaoa=Ÿ±Ç`a(Ÿ±Çbmia2Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia1Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`hxycoordsŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1ddataŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`l            Ÿ±Ç`fxytextŸ±Çaoa=Ÿ±Ç`a(Ÿ±Çaoa-Ÿ±Çbmib15Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmib25Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`jtextcoordsŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1moffset pointsŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`l            Ÿ±Ç`jarrowpropsŸ±Çaoa=Ÿ±ÇbnbddictŸ±Ç`a(Ÿ±Ç`ifacecolorŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1eblackŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`fshrinkŸ±Çaoa=Ÿ±Çbmfd0.05Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`l            Ÿ±Ç`shorizontalalignmentŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1erightŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`qverticalalignmentŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1fbottomŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`hannotateŸ±Ç`a(Ÿ±Çbs1a'Ÿ±Çbs1maxes fractionŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`l            Ÿ±Ç`bxyŸ±Çaoa=Ÿ±Ç`a(Ÿ±Çbmia3Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia1Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`hxycoordsŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1ddataŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`l            Ÿ±Ç`fxytextŸ±Çaoa=Ÿ±Ç`a(Ÿ±Çbmfc0.8Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd0.95Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`jtextcoordsŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1maxes fractionŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`l            Ÿ±Ç`jarrowpropsŸ±Çaoa=Ÿ±ÇbnbddictŸ±Ç`a(Ÿ±Ç`ifacecolorŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1eblackŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`fshrinkŸ±Çaoa=Ÿ±Çbmfd0.05Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`l            Ÿ±Ç`shorizontalalignmentŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1erightŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`qverticalalignmentŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1ctopŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1xJ# You may also use negative points or pixels to specify from (right, top).Ÿ±Ç`a
Ÿ±Çbc1xO# E.g., (-10, 10) is 10 points to the left of the right side of the axes and 10Ÿ±Ç`a
Ÿ±Çbc1x# points above the bottomŸ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`hannotateŸ±Ç`a(Ÿ±Çbs1a'Ÿ±Çbs1xpixel offset from axes fractionŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`l            Ÿ±Ç`bxyŸ±Çaoa=Ÿ±Ç`a(Ÿ±Çbmia1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia0Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`hxycoordsŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1maxes fractionŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`l            Ÿ±Ç`fxytextŸ±Çaoa=Ÿ±Ç`a(Ÿ±Çaoa-Ÿ±Çbmib20Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmib20Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`jtextcoordsŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1moffset pixelsŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`l            Ÿ±Ç`shorizontalalignmentŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1erightŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`l            Ÿ±Ç`qverticalalignmentŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1fbottomŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`csetŸ±Ç`a(Ÿ±Ç`dxlimŸ±Çaoa=Ÿ±Ç`a(Ÿ±Çaoa-Ÿ±Çbmia1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia5Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dylimŸ±Çaoa=Ÿ±Ç`a(Ÿ±Çaoa-Ÿ±Çbmia3Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia5Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1xO###############################################################################Ÿ±Ç`a
Ÿ±Çbc1x2# Using multiple coordinate systems and axis typesŸ±Ç`a
Ÿ±Çbc1x2# ------------------------------------------------Ÿ±Ç`a
Ÿ±Çbc1a#Ÿ±Ç`a
Ÿ±Çbc1xK# You can specify the *xypoint* and the *xytext* in different positions andŸ±Ç`a
Ÿ±Çbc1xK# coordinate systems, and optionally turn on a connecting line and mark theŸ±Ç`a
Ÿ±Çbc1x;# point with a marker.  Annotations work on polar axes too.Ÿ±Ç`a
Ÿ±Çbc1a#Ÿ±Ç`a
Ÿ±Çbc1xK# In the example below, the *xy* point is in native coordinates (*xycoords*Ÿ±Ç`a
Ÿ±Çbc1xK# defaults to 'data').  For a polar axes, this is in (theta, radius) space.Ÿ±Ç`a
Ÿ±Çbc1xO# The text in the example is placed in the fractional figure coordinate system.Ÿ±Ç`a
Ÿ±Çbc1xN# Text keyword arguments like horizontal and vertical alignment are respected.Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`cfigŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`baxŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`hsubplotsŸ±Ç`a(Ÿ±Ç`jsubplot_kwŸ±Çaoa=Ÿ±ÇbnbddictŸ±Ç`a(Ÿ±Ç`jprojectionŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1epolarŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`gfigsizeŸ±Çaoa=Ÿ±Ç`a(Ÿ±Çbmia3Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia3Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`arŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`farangeŸ±Ç`a(Ÿ±Çbmia0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfe0.001Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`ethetaŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Çbmia2Ÿ±Çaoa*Ÿ±Çbmia2Ÿ±Çaoa*Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`bpiŸ±Çaoa*Ÿ±Ç`arŸ±Ç`a
Ÿ±Ç`dlineŸ±Ç`a,Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`dplotŸ±Ç`a(Ÿ±Ç`ethetaŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`arŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`cindŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Çbmic800Ÿ±Ç`a
Ÿ±Ç`ethisrŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ithisthetaŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`arŸ±Ç`a[Ÿ±Ç`cindŸ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ethetaŸ±Ç`a[Ÿ±Ç`cindŸ±Ç`a]Ÿ±Ç`a
Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`dplotŸ±Ç`a(Ÿ±Ç`a[Ÿ±Ç`ithisthetaŸ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`a[Ÿ±Ç`ethisrŸ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1aoŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`hannotateŸ±Ç`a(Ÿ±Çbs1a'Ÿ±Çbs1ra polar annotationŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`l            Ÿ±Ç`bxyŸ±Çaoa=Ÿ±Ç`a(Ÿ±Ç`ithisthetaŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ethisrŸ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`b  Ÿ±Çbc1o# theta, radiusŸ±Ç`a
Ÿ±Ç`l            Ÿ±Ç`fxytextŸ±Çaoa=Ÿ±Ç`a(Ÿ±Çbmfd0.05Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd0.05Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`d    Ÿ±Çbc1t# fraction, fractionŸ±Ç`a
Ÿ±Ç`l            Ÿ±Ç`jtextcoordsŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1ofigure fractionŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`l            Ÿ±Ç`jarrowpropsŸ±Çaoa=Ÿ±ÇbnbddictŸ±Ç`a(Ÿ±Ç`ifacecolorŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1eblackŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`fshrinkŸ±Çaoa=Ÿ±Çbmfd0.05Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`l            Ÿ±Ç`shorizontalalignmentŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1dleftŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`l            Ÿ±Ç`qverticalalignmentŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1fbottomŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1xM#############################################################################Ÿ±Ç`a
Ÿ±Çbc1xG# You can also use polar notation on a cartesian axes.  Here the nativeŸ±Ç`a
Ÿ±Çbc1xE# coordinate system ('data') is cartesian, so you need to specify theŸ±Ç`a
Ÿ±Çbc1xH# xycoords and textcoords as 'polar' if you want to use (theta, radius).Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`belŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`gEllipseŸ±Ç`a(Ÿ±Ç`a(Ÿ±Çbmia0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia0Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmib10Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmib20Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ifacecolorŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1arŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ealphaŸ±Çaoa=Ÿ±Çbmfc0.5Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`cfigŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`baxŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`hsubplotsŸ±Ç`a(Ÿ±Ç`jsubplot_kwŸ±Çaoa=Ÿ±ÇbnbddictŸ±Ç`a(Ÿ±Ç`faspectŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1eequalŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`jadd_artistŸ±Ç`a(Ÿ±Ç`belŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`belŸ±Çaoa.Ÿ±Ç`lset_clip_boxŸ±Ç`a(Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`dbboxŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`hannotateŸ±Ç`a(Ÿ±Çbs1a'Ÿ±Çbs1gthe topŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`l            Ÿ±Ç`bxyŸ±Çaoa=Ÿ±Ç`a(Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`bpiŸ±Çaoa/Ÿ±Çbmfb2.Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfc10.Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`f      Ÿ±Çbc1o# theta, radiusŸ±Ç`a
Ÿ±Ç`l            Ÿ±Ç`fxytextŸ±Çaoa=Ÿ±Ç`a(Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`bpiŸ±Çaoa/Ÿ±Çbmia3Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfc20.Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`c   Ÿ±Çbc1o# theta, radiusŸ±Ç`a
Ÿ±Ç`l            Ÿ±Ç`hxycoordsŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1epolarŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`l            Ÿ±Ç`jtextcoordsŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1epolarŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`l            Ÿ±Ç`jarrowpropsŸ±Çaoa=Ÿ±ÇbnbddictŸ±Ç`a(Ÿ±Ç`ifacecolorŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1eblackŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`fshrinkŸ±Çaoa=Ÿ±Çbmfd0.05Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`l            Ÿ±Ç`shorizontalalignmentŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1dleftŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`l            Ÿ±Ç`qverticalalignmentŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1fbottomŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`l            Ÿ±Ç`gclip_onŸ±Çaoa=Ÿ±ÇbkcdTrueŸ±Ç`a)Ÿ±Ç`b  Ÿ±Çbc1x# clip to the axes bounding boxŸ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`csetŸ±Ç`a(Ÿ±Ç`dxlimŸ±Çaoa=Ÿ±Ç`a[Ÿ±Çaoa-Ÿ±Çbmib20Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmib20Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dylimŸ±Çaoa=Ÿ±Ç`a[Ÿ±Çaoa-Ÿ±Çbmib20Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmib20Ÿ±Ç`a]Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1xO###############################################################################Ÿ±Ç`a
Ÿ±Çbc1x%# Customizing arrow and bubble stylesŸ±Ç`a
Ÿ±Çbc1x%# -----------------------------------Ÿ±Ç`a
Ÿ±Çbc1a#Ÿ±Ç`a
Ÿ±Çbc1xL# The arrow between *xytext* and the annotation point, as well as the bubbleŸ±Ç`a
Ÿ±Çbc1xK# that covers the annotation text, are highly customizable. Below are a fewŸ±Ç`a
Ÿ±Çbc1x6# parameter options as well as their resulting output.Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`cfigŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`baxŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`hsubplotsŸ±Ç`a(Ÿ±Ç`gfigsizeŸ±Çaoa=Ÿ±Ç`a(Ÿ±Çbmia8Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia5Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`atŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`farangeŸ±Ç`a(Ÿ±Çbmfc0.0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfc5.0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd0.01Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`asŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`ccosŸ±Ç`a(Ÿ±Çbmia2Ÿ±Çaoa*Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`bpiŸ±Çaoa*Ÿ±Ç`atŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`dlineŸ±Ç`a,Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`dplotŸ±Ç`a(Ÿ±Ç`atŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`asŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`blwŸ±Çaoa=Ÿ±Çbmia3Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`hannotateŸ±Ç`a(Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Çbs1a'Ÿ±Çbs1hstraightŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`bxyŸ±Çaoa=Ÿ±Ç`a(Ÿ±Çbmia0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia1Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`hxycoordsŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1ddataŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`fxytextŸ±Çaoa=Ÿ±Ç`a(Ÿ±Çaoa-Ÿ±Çbmib50Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmib30Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`jtextcoordsŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1moffset pointsŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`jarrowpropsŸ±Çaoa=Ÿ±ÇbnbddictŸ±Ç`a(Ÿ±Ç`jarrowstyleŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2b->Ÿ±Çbs2a"Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`hannotateŸ±Ç`a(Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Çbs1a'Ÿ±Çbs1earc3,Ÿ±Çbseb\nŸ±Çbs1grad 0.2Ÿ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`bxyŸ±Çaoa=Ÿ±Ç`a(Ÿ±Çbmfc0.5Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çaoa-Ÿ±Çbmia1Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`hxycoordsŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1ddataŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`fxytextŸ±Çaoa=Ÿ±Ç`a(Ÿ±Çaoa-Ÿ±Çbmib80Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çaoa-Ÿ±Çbmib60Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`jtextcoordsŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1moffset pointsŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`jarrowpropsŸ±Çaoa=Ÿ±ÇbnbddictŸ±Ç`a(Ÿ±Ç`jarrowstyleŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2b->Ÿ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`t                    Ÿ±Ç`oconnectionstyleŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2karc3,rad=.2Ÿ±Çbs2a"Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`hannotateŸ±Ç`a(Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Çbs1a'Ÿ±Çbs1darc,Ÿ±Çbseb\nŸ±Çbs1hangle 50Ÿ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`bxyŸ±Çaoa=Ÿ±Ç`a(Ÿ±Çbmfb1.Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia1Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`hxycoordsŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1ddataŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`fxytextŸ±Çaoa=Ÿ±Ç`a(Ÿ±Çaoa-Ÿ±Çbmib90Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmib50Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`jtextcoordsŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1moffset pointsŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`jarrowpropsŸ±Çaoa=Ÿ±ÇbnbddictŸ±Ç`a(Ÿ±Ç`jarrowstyleŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2b->Ÿ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`t                    Ÿ±Ç`oconnectionstyleŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2xarc,angleA=0,armA=50,rad=10Ÿ±Çbs2a"Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`hannotateŸ±Ç`a(Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Çbs1a'Ÿ±Çbs1darc,Ÿ±Çbseb\nŸ±Çbs1darmsŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`bxyŸ±Çaoa=Ÿ±Ç`a(Ÿ±Çbmfc1.5Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çaoa-Ÿ±Çbmia1Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`hxycoordsŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1ddataŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`fxytextŸ±Çaoa=Ÿ±Ç`a(Ÿ±Çaoa-Ÿ±Çbmib80Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çaoa-Ÿ±Çbmib60Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`jtextcoordsŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1moffset pointsŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`jarrowpropsŸ±Çaoa=Ÿ±ÇbnbddictŸ±Ç`a(Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±Ç`jarrowstyleŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2b->Ÿ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±Ç`oconnectionstyleŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2x-arc,angleA=0,armA=40,angleB=-90,armB=30,rad=7Ÿ±Çbs2a"Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`hannotateŸ±Ç`a(Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Çbs1a'Ÿ±Çbs1fangle,Ÿ±Çbseb\nŸ±Çbs1hangle 90Ÿ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`bxyŸ±Çaoa=Ÿ±Ç`a(Ÿ±Çbmfb2.Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia1Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`hxycoordsŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1ddataŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`fxytextŸ±Çaoa=Ÿ±Ç`a(Ÿ±Çaoa-Ÿ±Çbmib70Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmib30Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`jtextcoordsŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1moffset pointsŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`jarrowpropsŸ±Çaoa=Ÿ±ÇbnbddictŸ±Ç`a(Ÿ±Ç`jarrowstyleŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2b->Ÿ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`t                    Ÿ±Ç`oconnectionstyleŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2xangle,angleA=0,angleB=90,rad=10Ÿ±Çbs2a"Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`hannotateŸ±Ç`a(Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Çbs1a'Ÿ±Çbs1gangle3,Ÿ±Çbseb\nŸ±Çbs1iangle -90Ÿ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`bxyŸ±Çaoa=Ÿ±Ç`a(Ÿ±Çbmfc2.5Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çaoa-Ÿ±Çbmia1Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`hxycoordsŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1ddataŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`fxytextŸ±Çaoa=Ÿ±Ç`a(Ÿ±Çaoa-Ÿ±Çbmib80Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çaoa-Ÿ±Çbmib60Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`jtextcoordsŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1moffset pointsŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`jarrowpropsŸ±Çaoa=Ÿ±ÇbnbddictŸ±Ç`a(Ÿ±Ç`jarrowstyleŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2b->Ÿ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`t                    Ÿ±Ç`oconnectionstyleŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2xangle3,angleA=0,angleB=-90Ÿ±Çbs2a"Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`hannotateŸ±Ç`a(Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Çbs1a'Ÿ±Çbs1fangle,Ÿ±Çbseb\nŸ±Çbs1eroundŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`bxyŸ±Çaoa=Ÿ±Ç`a(Ÿ±Çbmfb3.Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia1Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`hxycoordsŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1ddataŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`fxytextŸ±Çaoa=Ÿ±Ç`a(Ÿ±Çaoa-Ÿ±Çbmib60Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmib30Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`jtextcoordsŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1moffset pointsŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`dbboxŸ±Çaoa=Ÿ±ÇbnbddictŸ±Ç`a(Ÿ±Ç`hboxstyleŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2eroundŸ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`bfcŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2c0.8Ÿ±Çbs2a"Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`jarrowpropsŸ±Çaoa=Ÿ±ÇbnbddictŸ±Ç`a(Ÿ±Ç`jarrowstyleŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2b->Ÿ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`t                    Ÿ±Ç`oconnectionstyleŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2xangle,angleA=0,angleB=90,rad=10Ÿ±Çbs2a"Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`hannotateŸ±Ç`a(Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Çbs1a'Ÿ±Çbs1fangle,Ÿ±Çbseb\nŸ±Çbs1fround4Ÿ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`bxyŸ±Çaoa=Ÿ±Ç`a(Ÿ±Çbmfc3.5Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çaoa-Ÿ±Çbmia1Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`hxycoordsŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1ddataŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`fxytextŸ±Çaoa=Ÿ±Ç`a(Ÿ±Çaoa-Ÿ±Çbmib70Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çaoa-Ÿ±Çbmib80Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`jtextcoordsŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1moffset pointsŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`dsizeŸ±Çaoa=Ÿ±Çbmib20Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`dbboxŸ±Çaoa=Ÿ±ÇbnbddictŸ±Ç`a(Ÿ±Ç`hboxstyleŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2mround4,pad=.5Ÿ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`bfcŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2c0.8Ÿ±Çbs2a"Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`jarrowpropsŸ±Çaoa=Ÿ±ÇbnbddictŸ±Ç`a(Ÿ±Ç`jarrowstyleŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2b->Ÿ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`t                    Ÿ±Ç`oconnectionstyleŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2x angle,angleA=0,angleB=-90,rad=10Ÿ±Çbs2a"Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`hannotateŸ±Ç`a(Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Çbs1a'Ÿ±Çbs1fangle,Ÿ±Çbseb\nŸ±Çbs1fshrinkŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`bxyŸ±Çaoa=Ÿ±Ç`a(Ÿ±Çbmfb4.Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia1Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`hxycoordsŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1ddataŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`fxytextŸ±Çaoa=Ÿ±Ç`a(Ÿ±Çaoa-Ÿ±Çbmib60Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmib30Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`jtextcoordsŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1moffset pointsŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`dbboxŸ±Çaoa=Ÿ±ÇbnbddictŸ±Ç`a(Ÿ±Ç`hboxstyleŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2eroundŸ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`bfcŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2c0.8Ÿ±Çbs2a"Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`jarrowpropsŸ±Çaoa=Ÿ±ÇbnbddictŸ±Ç`a(Ÿ±Ç`jarrowstyleŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2b->Ÿ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`t                    Ÿ±Ç`gshrinkAŸ±Çaoa=Ÿ±Çbmia0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`gshrinkBŸ±Çaoa=Ÿ±Çbmib10Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`t                    Ÿ±Ç`oconnectionstyleŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2xangle,angleA=0,angleB=90,rad=10Ÿ±Çbs2a"Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Çbc1xE# You can pass an empty string to get only annotation arrows renderedŸ±Ç`a
Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`hannotateŸ±Ç`a(Ÿ±Çbs1a'Ÿ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`bxyŸ±Çaoa=Ÿ±Ç`a(Ÿ±Çbmfb4.Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfb1.Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`hxycoordsŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1ddataŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`l            Ÿ±Ç`fxytextŸ±Çaoa=Ÿ±Ç`a(Ÿ±Çbmfc4.5Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çaoa-Ÿ±Çbmia1Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`jtextcoordsŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1ddataŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`l            Ÿ±Ç`jarrowpropsŸ±Çaoa=Ÿ±ÇbnbddictŸ±Ç`a(Ÿ±Ç`jarrowstyleŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2c<->Ÿ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`x                            Ÿ±Ç`oconnectionstyleŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2cbarŸ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`x                            Ÿ±Ç`becŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2akŸ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`x                            Ÿ±Ç`gshrinkAŸ±Çaoa=Ÿ±Çbmia5Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`gshrinkBŸ±Çaoa=Ÿ±Çbmia5Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`csetŸ±Ç`a(Ÿ±Ç`dxlimŸ±Çaoa=Ÿ±Ç`a(Ÿ±Çaoa-Ÿ±Çbmia1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia5Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dylimŸ±Çaoa=Ÿ±Ç`a(Ÿ±Çaoa-Ÿ±Çbmia4Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia3Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1xM#############################################################################Ÿ±Ç`a
Ÿ±Çbc1xB# We'll create another figure so that it doesn't get too clutteredŸ±Ç`a
Ÿ±Ç`cfigŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`baxŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`hsubplotsŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`belŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`gEllipseŸ±Ç`a(Ÿ±Ç`a(Ÿ±Çbmia2Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çaoa-Ÿ±Çbmia1Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfc0.5Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfc0.5Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`iadd_patchŸ±Ç`a(Ÿ±Ç`belŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`hannotateŸ±Ç`a(Ÿ±Çbs1a'Ÿ±Çbs1d$->$Ÿ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`l            Ÿ±Ç`bxyŸ±Çaoa=Ÿ±Ç`a(Ÿ±Çbmfb2.Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çaoa-Ÿ±Çbmia1Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`hxycoordsŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1ddataŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`l            Ÿ±Ç`fxytextŸ±Çaoa=Ÿ±Ç`a(Ÿ±Çaoa-Ÿ±Çbmic150Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çaoa-Ÿ±Çbmic140Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`jtextcoordsŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1moffset pointsŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`l            Ÿ±Ç`dbboxŸ±Çaoa=Ÿ±ÇbnbddictŸ±Ç`a(Ÿ±Ç`hboxstyleŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2eroundŸ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`bfcŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2c0.8Ÿ±Çbs2a"Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`l            Ÿ±Ç`jarrowpropsŸ±Çaoa=Ÿ±ÇbnbddictŸ±Ç`a(Ÿ±Ç`jarrowstyleŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2b->Ÿ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`x                            Ÿ±Ç`fpatchBŸ±Çaoa=Ÿ±Ç`belŸ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`x                            Ÿ±Ç`oconnectionstyleŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2xangle,angleA=90,angleB=0,rad=10Ÿ±Çbs2a"Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`hannotateŸ±Ç`a(Ÿ±Çbs1a'Ÿ±Çbs1earrowŸ±Çbseb\nŸ±Çbs1efancyŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`l            Ÿ±Ç`bxyŸ±Çaoa=Ÿ±Ç`a(Ÿ±Çbmfb2.Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çaoa-Ÿ±Çbmia1Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`hxycoordsŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1ddataŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`l            Ÿ±Ç`fxytextŸ±Çaoa=Ÿ±Ç`a(Ÿ±Çaoa-Ÿ±Çbmic100Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmib60Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`jtextcoordsŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1moffset pointsŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`l            Ÿ±Ç`dsizeŸ±Çaoa=Ÿ±Çbmib20Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`l            Ÿ±Çbc1x(# bbox=dict(boxstyle="round", fc="0.8"),Ÿ±Ç`a
Ÿ±Ç`l            Ÿ±Ç`jarrowpropsŸ±Çaoa=Ÿ±ÇbnbddictŸ±Ç`a(Ÿ±Ç`jarrowstyleŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2efancyŸ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`x                            Ÿ±Ç`bfcŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2c0.6Ÿ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`becŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2dnoneŸ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`x                            Ÿ±Ç`fpatchBŸ±Çaoa=Ÿ±Ç`belŸ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`x                            Ÿ±Ç`oconnectionstyleŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2xangle3,angleA=0,angleB=-90Ÿ±Çbs2a"Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`hannotateŸ±Ç`a(Ÿ±Çbs1a'Ÿ±Çbs1earrowŸ±Çbseb\nŸ±Çbs1fsimpleŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`l            Ÿ±Ç`bxyŸ±Çaoa=Ÿ±Ç`a(Ÿ±Çbmfb2.Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çaoa-Ÿ±Çbmia1Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`hxycoordsŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1ddataŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`l            Ÿ±Ç`fxytextŸ±Çaoa=Ÿ±Ç`a(Ÿ±Çbmic100Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmib60Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`jtextcoordsŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1moffset pointsŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`l            Ÿ±Ç`dsizeŸ±Çaoa=Ÿ±Çbmib20Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`l            Ÿ±Çbc1x(# bbox=dict(boxstyle="round", fc="0.8"),Ÿ±Ç`a
Ÿ±Ç`l            Ÿ±Ç`jarrowpropsŸ±Çaoa=Ÿ±ÇbnbddictŸ±Ç`a(Ÿ±Ç`jarrowstyleŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2fsimpleŸ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`x                            Ÿ±Ç`bfcŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2c0.6Ÿ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`becŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2dnoneŸ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`x                            Ÿ±Ç`fpatchBŸ±Çaoa=Ÿ±Ç`belŸ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`x                            Ÿ±Ç`oconnectionstyleŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2larc3,rad=0.3Ÿ±Çbs2a"Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`hannotateŸ±Ç`a(Ÿ±Çbs1a'Ÿ±Çbs1ewedgeŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`l            Ÿ±Ç`bxyŸ±Çaoa=Ÿ±Ç`a(Ÿ±Çbmfb2.Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çaoa-Ÿ±Çbmia1Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`hxycoordsŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1ddataŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`l            Ÿ±Ç`fxytextŸ±Çaoa=Ÿ±Ç`a(Ÿ±Çaoa-Ÿ±Çbmic100Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çaoa-Ÿ±Çbmic100Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`jtextcoordsŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1moffset pointsŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`l            Ÿ±Ç`dsizeŸ±Çaoa=Ÿ±Çbmib20Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`l            Ÿ±Çbc1x(# bbox=dict(boxstyle="round", fc="0.8"),Ÿ±Ç`a
Ÿ±Ç`l            Ÿ±Ç`jarrowpropsŸ±Çaoa=Ÿ±ÇbnbddictŸ±Ç`a(Ÿ±Ç`jarrowstyleŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2twedge,tail_width=0.7Ÿ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`x                            Ÿ±Ç`bfcŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2c0.6Ÿ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`becŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2dnoneŸ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`x                            Ÿ±Ç`fpatchBŸ±Çaoa=Ÿ±Ç`belŸ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`x                            Ÿ±Ç`oconnectionstyleŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2marc3,rad=-0.3Ÿ±Çbs2a"Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`hannotateŸ±Ç`a(Ÿ±Çbs1a'Ÿ±Çbs1gbubble,Ÿ±Çbseb\nŸ±Çbs1hcontoursŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`l            Ÿ±Ç`bxyŸ±Çaoa=Ÿ±Ç`a(Ÿ±Çbmfb2.Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çaoa-Ÿ±Çbmia1Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`hxycoordsŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1ddataŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`l            Ÿ±Ç`fxytextŸ±Çaoa=Ÿ±Ç`a(Ÿ±Çbmia0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çaoa-Ÿ±Çbmib70Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`jtextcoordsŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1moffset pointsŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`l            Ÿ±Ç`dsizeŸ±Çaoa=Ÿ±Çbmib20Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`l            Ÿ±Ç`dbboxŸ±Çaoa=Ÿ±ÇbnbddictŸ±Ç`a(Ÿ±Ç`hboxstyleŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2eroundŸ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`v                      Ÿ±Ç`bfcŸ±Çaoa=Ÿ±Ç`a(Ÿ±Çbmfc1.0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfc0.7Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfc0.7Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`v                      Ÿ±Ç`becŸ±Çaoa=Ÿ±Ç`a(Ÿ±Çbmfb1.Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfb.5Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfb.5Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`l            Ÿ±Ç`jarrowpropsŸ±Çaoa=Ÿ±ÇbnbddictŸ±Ç`a(Ÿ±Ç`jarrowstyleŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2swedge,tail_width=1.Ÿ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`x                            Ÿ±Ç`bfcŸ±Çaoa=Ÿ±Ç`a(Ÿ±Çbmfc1.0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfc0.7Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfc0.7Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`becŸ±Çaoa=Ÿ±Ç`a(Ÿ±Çbmfb1.Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfb.5Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfb.5Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`x                            Ÿ±Ç`fpatchAŸ±Çaoa=Ÿ±ÇbkcdNoneŸ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`x                            Ÿ±Ç`fpatchBŸ±Çaoa=Ÿ±Ç`belŸ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`x                            Ÿ±Ç`frelposŸ±Çaoa=Ÿ±Ç`a(Ÿ±Çbmfc0.2Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfc0.8Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`x                            Ÿ±Ç`oconnectionstyleŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2marc3,rad=-0.1Ÿ±Çbs2a"Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`hannotateŸ±Ç`a(Ÿ±Çbs1a'Ÿ±Çbs1fbubbleŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`l            Ÿ±Ç`bxyŸ±Çaoa=Ÿ±Ç`a(Ÿ±Çbmfb2.Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çaoa-Ÿ±Çbmia1Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`hxycoordsŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1ddataŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`l            Ÿ±Ç`fxytextŸ±Çaoa=Ÿ±Ç`a(Ÿ±Çbmib55Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia0Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`jtextcoordsŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1moffset pointsŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`l            Ÿ±Ç`dsizeŸ±Çaoa=Ÿ±Çbmib20Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`bvaŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2fcenterŸ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`l            Ÿ±Ç`dbboxŸ±Çaoa=Ÿ±ÇbnbddictŸ±Ç`a(Ÿ±Ç`hboxstyleŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2eroundŸ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`bfcŸ±Çaoa=Ÿ±Ç`a(Ÿ±Çbmfc1.0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfc0.7Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfc0.7Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`becŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2dnoneŸ±Çbs2a"Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`l            Ÿ±Ç`jarrowpropsŸ±Çaoa=Ÿ±ÇbnbddictŸ±Ç`a(Ÿ±Ç`jarrowstyleŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2swedge,tail_width=1.Ÿ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`x                            Ÿ±Ç`bfcŸ±Çaoa=Ÿ±Ç`a(Ÿ±Çbmfc1.0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfc0.7Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfc0.7Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`becŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2dnoneŸ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`x                            Ÿ±Ç`fpatchAŸ±Çaoa=Ÿ±ÇbkcdNoneŸ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`x                            Ÿ±Ç`fpatchBŸ±Çaoa=Ÿ±Ç`belŸ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`x                            Ÿ±Ç`frelposŸ±Çaoa=Ÿ±Ç`a(Ÿ±Çbmfc0.2Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfc0.5Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`csetŸ±Ç`a(Ÿ±Ç`dxlimŸ±Çaoa=Ÿ±Ç`a(Ÿ±Çaoa-Ÿ±Çbmia1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia5Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dylimŸ±Çaoa=Ÿ±Ç`a(Ÿ±Çaoa-Ÿ±Çbmia5Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia3Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1xO###############################################################################Ÿ±Ç`a
Ÿ±Çbc1x%# More examples of coordinate systemsŸ±Ç`a
Ÿ±Çbc1x%# -----------------------------------Ÿ±Ç`a
Ÿ±Çbc1a#Ÿ±Ç`a
Ÿ±Çbc1xH# Below we'll show a few more examples of coordinate systems and how theŸ±Ç`a
Ÿ±Çbc1x+# location of annotations may be specified.Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`cfigŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`a(Ÿ±Ç`cax1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`cax2Ÿ±Ç`a)Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`hsubplotsŸ±Ç`a(Ÿ±Çbmia1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia2Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`ibbox_argsŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±ÇbnbddictŸ±Ç`a(Ÿ±Ç`hboxstyleŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2eroundŸ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`bfcŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2c0.8Ÿ±Çbs2a"Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`jarrow_argsŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±ÇbnbddictŸ±Ç`a(Ÿ±Ç`jarrowstyleŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2b->Ÿ±Çbs2a"Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1xE# Here we'll demonstrate the extents of the coordinate system and howŸ±Ç`a
Ÿ±Çbc1x# we place annotating text.Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`cax1Ÿ±Çaoa.Ÿ±Ç`hannotateŸ±Ç`a(Ÿ±Çbs1a'Ÿ±Çbs1vfigure fraction : 0, 0Ÿ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`bxyŸ±Çaoa=Ÿ±Ç`a(Ÿ±Çbmia0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia0Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`hxycoordsŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1ofigure fractionŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`m             Ÿ±Ç`fxytextŸ±Çaoa=Ÿ±Ç`a(Ÿ±Çbmib20Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmib20Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`jtextcoordsŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1moffset pointsŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`m             Ÿ±Ç`bhaŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2dleftŸ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`bvaŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2fbottomŸ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`m             Ÿ±Ç`dbboxŸ±Çaoa=Ÿ±Ç`ibbox_argsŸ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`m             Ÿ±Ç`jarrowpropsŸ±Çaoa=Ÿ±Ç`jarrow_argsŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`cax1Ÿ±Çaoa.Ÿ±Ç`hannotateŸ±Ç`a(Ÿ±Çbs1a'Ÿ±Çbs1vfigure fraction : 1, 1Ÿ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`bxyŸ±Çaoa=Ÿ±Ç`a(Ÿ±Çbmia1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia1Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`hxycoordsŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1ofigure fractionŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`m             Ÿ±Ç`fxytextŸ±Çaoa=Ÿ±Ç`a(Ÿ±Çaoa-Ÿ±Çbmib20Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çaoa-Ÿ±Çbmib20Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`jtextcoordsŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1moffset pointsŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`m             Ÿ±Ç`bhaŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2erightŸ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`bvaŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2ctopŸ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`m             Ÿ±Ç`dbboxŸ±Çaoa=Ÿ±Ç`ibbox_argsŸ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`m             Ÿ±Ç`jarrowpropsŸ±Çaoa=Ÿ±Ç`jarrow_argsŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`cax1Ÿ±Çaoa.Ÿ±Ç`hannotateŸ±Ç`a(Ÿ±Çbs1a'Ÿ±Çbs1taxes fraction : 0, 0Ÿ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`bxyŸ±Çaoa=Ÿ±Ç`a(Ÿ±Çbmia0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia0Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`hxycoordsŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1maxes fractionŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`m             Ÿ±Ç`fxytextŸ±Çaoa=Ÿ±Ç`a(Ÿ±Çbmib20Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmib20Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`jtextcoordsŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1moffset pointsŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`m             Ÿ±Ç`bhaŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2dleftŸ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`bvaŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2fbottomŸ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`m             Ÿ±Ç`dbboxŸ±Çaoa=Ÿ±Ç`ibbox_argsŸ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`m             Ÿ±Ç`jarrowpropsŸ±Çaoa=Ÿ±Ç`jarrow_argsŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`cax1Ÿ±Çaoa.Ÿ±Ç`hannotateŸ±Ç`a(Ÿ±Çbs1a'Ÿ±Çbs1taxes fraction : 1, 1Ÿ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`bxyŸ±Çaoa=Ÿ±Ç`a(Ÿ±Çbmia1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia1Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`hxycoordsŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1maxes fractionŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`m             Ÿ±Ç`fxytextŸ±Çaoa=Ÿ±Ç`a(Ÿ±Çaoa-Ÿ±Çbmib20Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çaoa-Ÿ±Çbmib20Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`jtextcoordsŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1moffset pointsŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`m             Ÿ±Ç`bhaŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2erightŸ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`bvaŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2ctopŸ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`m             Ÿ±Ç`dbboxŸ±Çaoa=Ÿ±Ç`ibbox_argsŸ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`m             Ÿ±Ç`jarrowpropsŸ±Çaoa=Ÿ±Ç`jarrow_argsŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1x7# It is also possible to generate draggable annotationsŸ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`can1Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cax1Ÿ±Çaoa.Ÿ±Ç`hannotateŸ±Ç`a(Ÿ±Çbs1a'Ÿ±Çbs1iDrag me 1Ÿ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`bxyŸ±Çaoa=Ÿ±Ç`a(Ÿ±Çbmfb.5Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfb.7Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`hxycoordsŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1ddataŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`s                   Ÿ±Ç`bhaŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2fcenterŸ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`bvaŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2fcenterŸ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`s                   Ÿ±Ç`dbboxŸ±Çaoa=Ÿ±Ç`ibbox_argsŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`can2Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cax1Ÿ±Çaoa.Ÿ±Ç`hannotateŸ±Ç`a(Ÿ±Çbs1a'Ÿ±Çbs1iDrag me 2Ÿ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`bxyŸ±Çaoa=Ÿ±Ç`a(Ÿ±Çbmfb.5Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfb.5Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`hxycoordsŸ±Çaoa=Ÿ±Ç`can1Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`s                   Ÿ±Ç`fxytextŸ±Çaoa=Ÿ±Ç`a(Ÿ±Çbmfb.5Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfb.3Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`jtextcoordsŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1maxes fractionŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`s                   Ÿ±Ç`bhaŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2fcenterŸ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`bvaŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2fcenterŸ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`s                   Ÿ±Ç`dbboxŸ±Çaoa=Ÿ±Ç`ibbox_argsŸ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`s                   Ÿ±Ç`jarrowpropsŸ±Çaoa=Ÿ±ÇbnbddictŸ±Ç`a(Ÿ±Ç`fpatchBŸ±Çaoa=Ÿ±Ç`can1Ÿ±Çaoa.Ÿ±Ç`nget_bbox_patchŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`x#                                   Ÿ±Ç`oconnectionstyleŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2larc3,rad=0.2Ÿ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`x#                                   Ÿ±Çaoa*Ÿ±Çaoa*Ÿ±Ç`jarrow_argsŸ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`can1Ÿ±Çaoa.Ÿ±Ç`idraggableŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`can2Ÿ±Çaoa.Ÿ±Ç`idraggableŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`can3Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cax1Ÿ±Çaoa.Ÿ±Ç`hannotateŸ±Ç`a(Ÿ±Çbs1a'Ÿ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`bxyŸ±Çaoa=Ÿ±Ç`a(Ÿ±Çbmfb.5Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfb.5Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`hxycoordsŸ±Çaoa=Ÿ±Ç`can2Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`s                   Ÿ±Ç`fxytextŸ±Çaoa=Ÿ±Ç`a(Ÿ±Çbmfb.5Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfb.5Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`jtextcoordsŸ±Çaoa=Ÿ±Ç`can1Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`s                   Ÿ±Ç`bhaŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2fcenterŸ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`bvaŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2fcenterŸ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`s                   Ÿ±Ç`dbboxŸ±Çaoa=Ÿ±Ç`ibbox_argsŸ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`s                   Ÿ±Ç`jarrowpropsŸ±Çaoa=Ÿ±ÇbnbddictŸ±Ç`a(Ÿ±Ç`fpatchAŸ±Çaoa=Ÿ±Ç`can1Ÿ±Çaoa.Ÿ±Ç`nget_bbox_patchŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`x#                                   Ÿ±Ç`fpatchBŸ±Çaoa=Ÿ±Ç`can2Ÿ±Çaoa.Ÿ±Ç`nget_bbox_patchŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`x#                                   Ÿ±Ç`oconnectionstyleŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2larc3,rad=0.2Ÿ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`x#                                   Ÿ±Çaoa*Ÿ±Çaoa*Ÿ±Ç`jarrow_argsŸ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1xC# Finally we'll show off some more complex annotation and placementŸ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`dtextŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cax2Ÿ±Çaoa.Ÿ±Ç`hannotateŸ±Ç`a(Ÿ±Çbs1a'Ÿ±Çbs1ixy=(0, 1)Ÿ±Çbseb\nŸ±Çbs1jxycoords=(Ÿ±Çbs1a"Ÿ±Çbs1ddataŸ±Çbs1a"Ÿ±Çbs1b, Ÿ±Çbs1a"Ÿ±Çbs1maxes fractionŸ±Çbs1a"Ÿ±Çbs1a)Ÿ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`t                    Ÿ±Ç`bxyŸ±Çaoa=Ÿ±Ç`a(Ÿ±Çbmia0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia1Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`hxycoordsŸ±Çaoa=Ÿ±Ç`a(Ÿ±Çbs2a"Ÿ±Çbs2ddataŸ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1maxes fractionŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`t                    Ÿ±Ç`fxytextŸ±Çaoa=Ÿ±Ç`a(Ÿ±Çbmia0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çaoa-Ÿ±Çbmib20Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`jtextcoordsŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1moffset pointsŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`t                    Ÿ±Ç`bhaŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2fcenterŸ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`bvaŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2ctopŸ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`t                    Ÿ±Ç`dbboxŸ±Çaoa=Ÿ±Ç`ibbox_argsŸ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`t                    Ÿ±Ç`jarrowpropsŸ±Çaoa=Ÿ±Ç`jarrow_argsŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`cax2Ÿ±Çaoa.Ÿ±Ç`hannotateŸ±Ç`a(Ÿ±Çbs1a'Ÿ±Çbs1kxy=(0.5, 0)Ÿ±Çbseb\nŸ±Çbs1oxycoords=artistŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`m             Ÿ±Ç`bxyŸ±Çaoa=Ÿ±Ç`a(Ÿ±Çbmfc0.5Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfb0.Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`hxycoordsŸ±Çaoa=Ÿ±Ç`dtextŸ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`m             Ÿ±Ç`fxytextŸ±Çaoa=Ÿ±Ç`a(Ÿ±Çbmia0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çaoa-Ÿ±Çbmib20Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`jtextcoordsŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1moffset pointsŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`m             Ÿ±Ç`bhaŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2fcenterŸ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`bvaŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2ctopŸ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`m             Ÿ±Ç`dbboxŸ±Çaoa=Ÿ±Ç`ibbox_argsŸ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`m             Ÿ±Ç`jarrowpropsŸ±Çaoa=Ÿ±Ç`jarrow_argsŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`cax2Ÿ±Çaoa.Ÿ±Ç`hannotateŸ±Ç`a(Ÿ±Çbs1a'Ÿ±Çbs1mxy=(0.8, 0.5)Ÿ±Çbseb\nŸ±Çbs1vxycoords=ax1.transDataŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`m             Ÿ±Ç`bxyŸ±Çaoa=Ÿ±Ç`a(Ÿ±Çbmfc0.8Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfc0.5Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`hxycoordsŸ±Çaoa=Ÿ±Ç`cax1Ÿ±Çaoa.Ÿ±Ç`itransDataŸ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`m             Ÿ±Ç`fxytextŸ±Çaoa=Ÿ±Ç`a(Ÿ±Çbmib10Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmib10Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`m             Ÿ±Ç`jtextcoordsŸ±Çaoa=Ÿ±Ç`jOffsetFromŸ±Ç`a(Ÿ±Ç`cax2Ÿ±Çaoa.Ÿ±Ç`dbboxŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`a(Ÿ±Çbmia0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia0Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs2a"Ÿ±Çbs2fpointsŸ±Çbs2a"Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`m             Ÿ±Ç`bhaŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2dleftŸ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`bvaŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2fbottomŸ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`m             Ÿ±Ç`dbboxŸ±Çaoa=Ÿ±Ç`ibbox_argsŸ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`m             Ÿ±Ç`jarrowpropsŸ±Çaoa=Ÿ±Ç`jarrow_argsŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`cax2Ÿ±Çaoa.Ÿ±Ç`csetŸ±Ç`a(Ÿ±Ç`dxlimŸ±Çaoa=Ÿ±Ç`a[Ÿ±Çaoa-Ÿ±Çbmia2Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia2Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dylimŸ±Çaoa=Ÿ±Ç`a[Ÿ±Çaoa-Ÿ±Çbmia2Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia2Ÿ±Ç`a]Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`dshowŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
`dNoneˆ