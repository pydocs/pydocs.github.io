ŸØÇÅŸ¥ÉôÑŸ±Çbsdx‰"""
=========
Pie Demo2
=========

Make a pie charts using `~.axes.Axes.pie`.

This example demonstrates some pie chart features like labels, varying size,
autolabeling the percentage, offsetting a slice and adding a shadow.
"""Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±ÇbknfimportŸ±Ç`a Ÿ±ÇbnnŸ¢ÑjmatplotlibŸ†Ñjmatplotlibe3.5.1fmodulejmatplotlibfmoduleıŸ±Çbnna.Ÿ±ÇbnnfpyplotŸ±Ç`a Ÿ±ÇakbasŸ±Ç`a Ÿ±ÇbnncpltŸ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1k# Some dataŸ±Ç`a
Ÿ±Ç`flabelsŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1eFrogsŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1dHogsŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1dDogsŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1dLogsŸ±Çbs1a'Ÿ±Ç`a
Ÿ±Ç`efracsŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`a[Ÿ±Çbmib15Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmib30Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmib45Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmib10Ÿ±Ç`a]Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1v# Make figure and axesŸ±Ç`a
Ÿ±Ç`cfigŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`caxsŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`hsubplotsŸ±Ç`a(Ÿ±Çbmia2Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia2Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1u# A standard pie plotŸ±Ç`a
Ÿ±Ç`caxsŸ±Ç`a[Ÿ±Çbmia0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia0Ÿ±Ç`a]Ÿ±Çaoa.Ÿ±Ç`cpieŸ±Ç`a(Ÿ±Ç`efracsŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`flabelsŸ±Çaoa=Ÿ±Ç`flabelsŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`gautopctŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbsie%1.1fŸ±Çbsib%%Ÿ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`fshadowŸ±Çaoa=Ÿ±ÇbkcdTrueŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1x&# Shift the second slice using explodeŸ±Ç`a
Ÿ±Ç`caxsŸ±Ç`a[Ÿ±Çbmia0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia1Ÿ±Ç`a]Ÿ±Çaoa.Ÿ±Ç`cpieŸ±Ç`a(Ÿ±Ç`efracsŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`flabelsŸ±Çaoa=Ÿ±Ç`flabelsŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`gautopctŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbsid%.0fŸ±Çbsib%%Ÿ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`fshadowŸ±Çaoa=Ÿ±ÇbkcdTrueŸ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`n              Ÿ±Ç`gexplodeŸ±Çaoa=Ÿ±Ç`a(Ÿ±Çbmia0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfc0.1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia0Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1x.# Adapt radius and text size for a smaller pieŸ±Ç`a
Ÿ±Ç`gpatchesŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`etextsŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`iautotextsŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`caxsŸ±Ç`a[Ÿ±Çbmia1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia0Ÿ±Ç`a]Ÿ±Çaoa.Ÿ±Ç`cpieŸ±Ç`a(Ÿ±Ç`efracsŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`flabelsŸ±Çaoa=Ÿ±Ç`flabelsŸ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`x*                                          Ÿ±Ç`gautopctŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbsid%.0fŸ±Çbsib%%Ÿ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`x*                                          Ÿ±Ç`itextpropsŸ±Çaoa=Ÿ±Ç`a{Ÿ±Çbs1a'Ÿ±Çbs1dsizeŸ±Çbs1a'Ÿ±Ç`a:Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1gsmallerŸ±Çbs1a'Ÿ±Ç`a}Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`x*                                          Ÿ±Ç`fshadowŸ±Çaoa=Ÿ±ÇbkcdTrueŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`fradiusŸ±Çaoa=Ÿ±Çbmfc0.5Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Çbc1x!# Make percent texts even smallerŸ±Ç`a
Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`dsetpŸ±Ç`a(Ÿ±Ç`iautotextsŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dsizeŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1gx-smallŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`iautotextsŸ±Ç`a[Ÿ±Çbmia0Ÿ±Ç`a]Ÿ±Çaoa.Ÿ±Ç`iset_colorŸ±Ç`a(Ÿ±Çbs1a'Ÿ±Çbs1ewhiteŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1xD# Use a smaller explode and turn of the shadow for better visibilityŸ±Ç`a
Ÿ±Ç`gpatchesŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`etextsŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`iautotextsŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`caxsŸ±Ç`a[Ÿ±Çbmia1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia1Ÿ±Ç`a]Ÿ±Çaoa.Ÿ±Ç`cpieŸ±Ç`a(Ÿ±Ç`efracsŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`flabelsŸ±Çaoa=Ÿ±Ç`flabelsŸ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`x*                                          Ÿ±Ç`gautopctŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbsid%.0fŸ±Çbsib%%Ÿ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`x*                                          Ÿ±Ç`itextpropsŸ±Çaoa=Ÿ±Ç`a{Ÿ±Çbs1a'Ÿ±Çbs1dsizeŸ±Çbs1a'Ÿ±Ç`a:Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1gsmallerŸ±Çbs1a'Ÿ±Ç`a}Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`x*                                          Ÿ±Ç`fshadowŸ±Çaoa=Ÿ±ÇbkceFalseŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`fradiusŸ±Çaoa=Ÿ±Çbmfc0.5Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`x*                                          Ÿ±Ç`gexplodeŸ±Çaoa=Ÿ±Ç`a(Ÿ±Çbmia0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd0.05Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia0Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`dsetpŸ±Ç`a(Ÿ±Ç`iautotextsŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dsizeŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1gx-smallŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`iautotextsŸ±Ç`a[Ÿ±Çbmia0Ÿ±Ç`a]Ÿ±Çaoa.Ÿ±Ç`iset_colorŸ±Ç`a(Ÿ±Çbs1a'Ÿ±Çbs1ewhiteŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
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