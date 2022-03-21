Ù¯‚Ù´ƒ™iÙ±‚bsdxª"""
=======================
Plot 2D data on 3D plot
=======================

Demonstrates using ax.plot's zdir keyword to plot 2D data on
selective axes of a 3D plot.
"""Ù±‚`a
Ù±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„enumpyÙ „enumpyf1.22.3fmoduleenumpyfmoduleõÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnnbnpÙ±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnnfpyplotÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnncpltÙ±‚`a
Ù±‚`a
Ù±‚`baxÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cpltÙ±‚aoa.Ù±‚`ffigureÙ±‚`a(Ù±‚`a)Ù±‚aoa.Ù±‚`kadd_subplotÙ±‚`a(Ù±‚`jprojectionÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1b3dÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚bc1x*# Plot a sin curve using the x and y axes.Ù±‚`a
Ù±‚`axÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`hlinspaceÙ±‚`a(Ù±‚bmia0Ù±‚`a,Ù±‚`a Ù±‚bmia1Ù±‚`a,Ù±‚`a Ù±‚bmic100Ù±‚`a)Ù±‚`a
Ù±‚`ayÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`csinÙ±‚`a(Ù±‚`axÙ±‚`a Ù±‚aoa*Ù±‚`a Ù±‚bmia2Ù±‚`a Ù±‚aoa*Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`bpiÙ±‚`a)Ù±‚`a Ù±‚aoa/Ù±‚`a Ù±‚bmia2Ù±‚`a Ù±‚aoa+Ù±‚`a Ù±‚bmfc0.5Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`dplotÙ±‚`a(Ù±‚`axÙ±‚`a,Ù±‚`a Ù±‚`ayÙ±‚`a,Ù±‚`a Ù±‚`bzsÙ±‚aoa=Ù±‚bmia0Ù±‚`a,Ù±‚`a Ù±‚`dzdirÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1azÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`elabelÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1ocurve in (x, y)Ù±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚bc1xF# Plot scatterplot data (20 2D points per colour) on the x and z axes.Ù±‚`a
Ù±‚`fcolorsÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`a(Ù±‚bs1a'Ù±‚bs1arÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚bs1a'Ù±‚bs1agÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚bs1a'Ù±‚bs1abÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚bs1a'Ù±‚bs1akÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚bc1x)# Fixing random state for reproducibilityÙ±‚`a
Ù±‚`bnpÙ±‚aoa.Ù±‚`frandomÙ±‚aoa.Ù±‚`dseedÙ±‚`a(Ù±‚bmih19680801Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`axÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`frandomÙ±‚aoa.Ù±‚`fsampleÙ±‚`a(Ù±‚bmib20Ù±‚`a Ù±‚aoa*Ù±‚`a Ù±‚bnbclenÙ±‚`a(Ù±‚`fcolorsÙ±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`ayÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`frandomÙ±‚aoa.Ù±‚`fsampleÙ±‚`a(Ù±‚bmib20Ù±‚`a Ù±‚aoa*Ù±‚`a Ù±‚bnbclenÙ±‚`a(Ù±‚`fcolorsÙ±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`fc_listÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`a[Ù±‚`a]Ù±‚`a
Ù±‚akcforÙ±‚`a Ù±‚`acÙ±‚`a Ù±‚bowbinÙ±‚`a Ù±‚`fcolorsÙ±‚`a:Ù±‚`a
Ù±‚`d    Ù±‚`fc_listÙ±‚aoa.Ù±‚`fextendÙ±‚`a(Ù±‚`a[Ù±‚`acÙ±‚`a]Ù±‚`a Ù±‚aoa*Ù±‚`a Ù±‚bmib20Ù±‚`a)Ù±‚`a
Ù±‚bc1xK# By using zdir='y', the y value of these points is fixed to the zs value 0Ù±‚`a
Ù±‚bc1x8# and the (x, y) points are plotted on the x and z axes.Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`gscatterÙ±‚`a(Ù±‚`axÙ±‚`a,Ù±‚`a Ù±‚`ayÙ±‚`a,Ù±‚`a Ù±‚`bzsÙ±‚aoa=Ù±‚bmia0Ù±‚`a,Ù±‚`a Ù±‚`dzdirÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1ayÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`acÙ±‚aoa=Ù±‚`fc_listÙ±‚`a,Ù±‚`a Ù±‚`elabelÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1ppoints in (x, z)Ù±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚bc1x)# Make legend, set axes limits and labelsÙ±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`flegendÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`hset_xlimÙ±‚`a(Ù±‚bmia0Ù±‚`a,Ù±‚`a Ù±‚bmia1Ù±‚`a)Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`hset_ylimÙ±‚`a(Ù±‚bmia0Ù±‚`a,Ù±‚`a Ù±‚bmia1Ù±‚`a)Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`hset_zlimÙ±‚`a(Ù±‚bmia0Ù±‚`a,Ù±‚`a Ù±‚bmia1Ù±‚`a)Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`jset_xlabelÙ±‚`a(Ù±‚bs1a'Ù±‚bs1aXÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`jset_ylabelÙ±‚`a(Ù±‚bs1a'Ù±‚bs1aYÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`jset_zlabelÙ±‚`a(Ù±‚bs1a'Ù±‚bs1aZÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚bc1xL# Customize the view angle so it's easier to see that the scatter points lieÙ±‚`a
Ù±‚bc1r# on the plane y=0Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`iview_initÙ±‚`a(Ù±‚`delevÙ±‚aoa=Ù±‚bmfc20.Ù±‚`a,Ù±‚`a Ù±‚`dazimÙ±‚aoa=Ù±‚aoa-Ù±‚bmib35Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`cpltÙ±‚aoa.Ù±‚`dshowÙ±‚`a(Ù±‚`a)Ù±‚`a
`dNoneö