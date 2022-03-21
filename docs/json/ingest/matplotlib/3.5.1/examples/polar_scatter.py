ŸØÇÅŸ¥ÉôÉŸ±Çbsdx‹"""
==========================
Scatter plot on polar axis
==========================

Size increases radially in this example and color increases with angle
(just to verify the symbols are being scattered correctly).
"""Ÿ±Ç`a
Ÿ±ÇbknfimportŸ±Ç`a Ÿ±ÇbnnŸ¢ÑenumpyŸ†Ñenumpyf1.22.3fmoduleenumpyfmoduleıŸ±Ç`a Ÿ±ÇakbasŸ±Ç`a Ÿ±ÇbnnbnpŸ±Ç`a
Ÿ±ÇbknfimportŸ±Ç`a Ÿ±ÇbnnŸ¢ÑjmatplotlibŸ†Ñjmatplotlibe3.5.1fmodulejmatplotlibfmoduleıŸ±Çbnna.Ÿ±ÇbnnfpyplotŸ±Ç`a Ÿ±ÇakbasŸ±Ç`a Ÿ±ÇbnncpltŸ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1x)# Fixing random state for reproducibilityŸ±Ç`a
Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`frandomŸ±Çaoa.Ÿ±Ç`dseedŸ±Ç`a(Ÿ±Çbmih19680801Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1x# Compute areas and colorsŸ±Ç`a
Ÿ±Ç`aNŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Çbmic150Ÿ±Ç`a
Ÿ±Ç`arŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Çbmia2Ÿ±Ç`a Ÿ±Çaoa*Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`frandomŸ±Çaoa.Ÿ±Ç`drandŸ±Ç`a(Ÿ±Ç`aNŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`ethetaŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Çbmia2Ÿ±Ç`a Ÿ±Çaoa*Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`bpiŸ±Ç`a Ÿ±Çaoa*Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`frandomŸ±Çaoa.Ÿ±Ç`drandŸ±Ç`a(Ÿ±Ç`aNŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`dareaŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Çbmic200Ÿ±Ç`a Ÿ±Çaoa*Ÿ±Ç`a Ÿ±Ç`arŸ±Çaoa*Ÿ±Çaoa*Ÿ±Çbmia2Ÿ±Ç`a
Ÿ±Ç`fcolorsŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`ethetaŸ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`cfigŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`ffigureŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`baxŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cfigŸ±Çaoa.Ÿ±Ç`kadd_subplotŸ±Ç`a(Ÿ±Ç`jprojectionŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1epolarŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`acŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`gscatterŸ±Ç`a(Ÿ±Ç`ethetaŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`arŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`acŸ±Çaoa=Ÿ±Ç`fcolorsŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`asŸ±Çaoa=Ÿ±Ç`dareaŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dcmapŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1chsvŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ealphaŸ±Çaoa=Ÿ±Çbmfd0.75Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1xO###############################################################################Ÿ±Ç`a
Ÿ±Çbc1x0# Scatter plot on polar axis, with offset originŸ±Ç`a
Ÿ±Çbc1x0# ----------------------------------------------Ÿ±Ç`a
Ÿ±Çbc1a#Ÿ±Ç`a
Ÿ±Çbc1xO# The main difference with the previous plot is the configuration of the originŸ±Ç`a
Ÿ±Çbc1xO# radius, producing an annulus. Additionally, the theta zero location is set toŸ±Ç`a
Ÿ±Çbc1r# rotate the plot.Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`cfigŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`ffigureŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`baxŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cfigŸ±Çaoa.Ÿ±Ç`kadd_subplotŸ±Ç`a(Ÿ±Ç`jprojectionŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1epolarŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`acŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`gscatterŸ±Ç`a(Ÿ±Ç`ethetaŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`arŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`acŸ±Çaoa=Ÿ±Ç`fcolorsŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`asŸ±Çaoa=Ÿ±Ç`dareaŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dcmapŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1chsvŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ealphaŸ±Çaoa=Ÿ±Çbmfd0.75Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`kset_roriginŸ±Ç`a(Ÿ±Çaoa-Ÿ±Çbmfc2.5Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`wset_theta_zero_locationŸ±Ç`a(Ÿ±Çbs1a'Ÿ±Çbs1aWŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`foffsetŸ±Çaoa=Ÿ±Çbmib10Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1xO###############################################################################Ÿ±Ç`a
Ÿ±Çbc1x1# Scatter plot on polar axis confined to a sectorŸ±Ç`a
Ÿ±Çbc1x1# -----------------------------------------------Ÿ±Ç`a
Ÿ±Çbc1a#Ÿ±Ç`a
Ÿ±Çbc1xI# The main difference with the previous plots is the configuration of theŸ±Ç`a
Ÿ±Çbc1xJ# theta start and end limits, producing a sector instead of a full circle.Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`cfigŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`ffigureŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`baxŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cfigŸ±Çaoa.Ÿ±Ç`kadd_subplotŸ±Ç`a(Ÿ±Ç`jprojectionŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1epolarŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`acŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`gscatterŸ±Ç`a(Ÿ±Ç`ethetaŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`arŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`acŸ±Çaoa=Ÿ±Ç`fcolorsŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`asŸ±Çaoa=Ÿ±Ç`dareaŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dcmapŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1chsvŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ealphaŸ±Çaoa=Ÿ±Çbmfd0.75Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`lset_thetaminŸ±Ç`a(Ÿ±Çbmib45Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`lset_thetamaxŸ±Ç`a(Ÿ±Çbmic135Ÿ±Ç`a)Ÿ±Ç`a
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
Ÿ±Çbc1xC#    - `matplotlib.axes.Axes.scatter` / `matplotlib.pyplot.scatter`Ÿ±Ç`a
Ÿ±Çbc1x%#    - `matplotlib.projections.polar`Ÿ±Ç`a
Ÿ±Çbc1x;#    - `matplotlib.projections.polar.PolarAxes.set_rorigin`Ÿ±Ç`a
Ÿ±Çbc1xG#    - `matplotlib.projections.polar.PolarAxes.set_theta_zero_location`Ÿ±Ç`a
Ÿ±Çbc1x<#    - `matplotlib.projections.polar.PolarAxes.set_thetamin`Ÿ±Ç`a
Ÿ±Çbc1x<#    - `matplotlib.projections.polar.PolarAxes.set_thetamax`Ÿ±Ç`a
`dNoneˆ