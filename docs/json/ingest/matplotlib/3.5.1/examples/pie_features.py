ŸØÇÅŸ¥ÉòüŸ±ÇbsdyQ"""
===============
Basic pie chart
===============

Demo of a basic pie chart plus a few additional features.

In addition to the basic pie chart, this demo shows a few optional features:

* slice labels
* auto-labeling the percentage
* offsetting a slice with "explode"
* drop-shadow
* custom start angle

Note about the custom start angle:

The default ``startangle`` is 0, which would start the "Frogs" slice on the
positive x-axis. This example sets ``startangle = 90`` such that everything is
rotated counter-clockwise by 90 degrees, and the frog slice starts on the
positive y-axis.
"""Ÿ±Ç`a
Ÿ±ÇbknfimportŸ±Ç`a Ÿ±ÇbnnŸ¢ÑjmatplotlibŸ†Ñjmatplotlibe3.5.1fmodulejmatplotlibfmoduleıŸ±Çbnna.Ÿ±ÇbnnfpyplotŸ±Ç`a Ÿ±ÇakbasŸ±Ç`a Ÿ±ÇbnncpltŸ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1xL# Pie chart, where the slices will be ordered and plotted counter-clockwise:Ÿ±Ç`a
Ÿ±Ç`flabelsŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1eFrogsŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1dHogsŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1dDogsŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1dLogsŸ±Çbs1a'Ÿ±Ç`a
Ÿ±Ç`esizesŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`a[Ÿ±Çbmib15Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmib30Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmib45Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmib10Ÿ±Ç`a]Ÿ±Ç`a
Ÿ±Ç`gexplodeŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`a(Ÿ±Çbmia0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfc0.1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia0Ÿ±Ç`a)Ÿ±Ç`b  Ÿ±Çbc1x,# only "explode" the 2nd slice (i.e. 'Hogs')Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`dfig1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`cax1Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`hsubplotsŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cax1Ÿ±Çaoa.Ÿ±Ç`cpieŸ±Ç`a(Ÿ±Ç`esizesŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`gexplodeŸ±Çaoa=Ÿ±Ç`gexplodeŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`flabelsŸ±Çaoa=Ÿ±Ç`flabelsŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`gautopctŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbsie%1.1fŸ±Çbsib%%Ÿ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±Ç`fshadowŸ±Çaoa=Ÿ±ÇbkcdTrueŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`jstartangleŸ±Çaoa=Ÿ±Çbmib90Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cax1Ÿ±Çaoa.Ÿ±Ç`daxisŸ±Ç`a(Ÿ±Çbs1a'Ÿ±Çbs1eequalŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`b  Ÿ±Çbc1x;# Equal aspect ratio ensures that pie is drawn as a circle.Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`dshowŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1xM#############################################################################Ÿ±Ç`a
Ÿ±Çbc1a#Ÿ±Ç`a
Ÿ±Çbc1x# .. admonition:: ReferencesŸ±Ç`a
Ÿ±Çbc1a#Ÿ±Ç`a
Ÿ±Çbc1xN#    The use of the following functions, methods, classes and modules is shownŸ±Ç`a
Ÿ±Çbc1u#    in this example:Ÿ±Ç`a
Ÿ±Çbc1a#Ÿ±Ç`a
Ÿ±Çbc1x;#    - `matplotlib.axes.Axes.pie` / `matplotlib.pyplot.pie`Ÿ±Ç`a
`dNoneˆ