Ù¯‚Ù´ƒ™Ù±‚bsdxŞ"""
========================================
Create 2D bar graphs in different planes
========================================

Demonstrates making a 3D plot which has 2D bar graphs projected onto
planes y=0, y=1, etc.
"""Ù±‚`a
Ù±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnnfpyplotÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnncpltÙ±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„enumpyÙ „enumpyf1.22.3fmoduleenumpyfmoduleõÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnnbnpÙ±‚`a
Ù±‚`a
Ù±‚bc1x)# Fixing random state for reproducibilityÙ±‚`a
Ù±‚`bnpÙ±‚aoa.Ù±‚`frandomÙ±‚aoa.Ù±‚`dseedÙ±‚`a(Ù±‚bmih19680801Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚`cfigÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cpltÙ±‚aoa.Ù±‚`ffigureÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`baxÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cfigÙ±‚aoa.Ù±‚`kadd_subplotÙ±‚`a(Ù±‚`jprojectionÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1b3dÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`fcolorsÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`a[Ù±‚bs1a'Ù±‚bs1arÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚bs1a'Ù±‚bs1agÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚bs1a'Ù±‚bs1abÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚bs1a'Ù±‚bs1ayÙ±‚bs1a'Ù±‚`a]Ù±‚`a
Ù±‚`fyticksÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`a[Ù±‚bmia3Ù±‚`a,Ù±‚`a Ù±‚bmia2Ù±‚`a,Ù±‚`a Ù±‚bmia1Ù±‚`a,Ù±‚`a Ù±‚bmia0Ù±‚`a]Ù±‚`a
Ù±‚akcforÙ±‚`a Ù±‚`acÙ±‚`a,Ù±‚`a Ù±‚`akÙ±‚`a Ù±‚bowbinÙ±‚`a Ù±‚bnbczipÙ±‚`a(Ù±‚`fcolorsÙ±‚`a,Ù±‚`a Ù±‚`fyticksÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`d    Ù±‚bc1x/# Generate the random data for the y=k 'layer'.Ù±‚`a
Ù±‚`d    Ù±‚`bxsÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`farangeÙ±‚`a(Ù±‚bmib20Ù±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`bysÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`frandomÙ±‚aoa.Ù±‚`drandÙ±‚`a(Ù±‚bmib20Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚bc1xK# You can provide either a single color or an array with the same length asÙ±‚`a
Ù±‚`d    Ù±‚bc1xJ# xs and ys. To demonstrate this, we color the first bar of each set cyan.Ù±‚`a
Ù±‚`d    Ù±‚`bcsÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`a[Ù±‚`acÙ±‚`a]Ù±‚`a Ù±‚aoa*Ù±‚`a Ù±‚bnbclenÙ±‚`a(Ù±‚`bxsÙ±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`bcsÙ±‚`a[Ù±‚bmia0Ù±‚`a]Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bs1a'Ù±‚bs1acÙ±‚bs1a'Ù±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚bc1xJ# Plot the bar graph given by xs and ys on the plane y=k with 80% opacity.Ù±‚`a
Ù±‚`d    Ù±‚`baxÙ±‚aoa.Ù±‚`cbarÙ±‚`a(Ù±‚`bxsÙ±‚`a,Ù±‚`a Ù±‚`bysÙ±‚`a,Ù±‚`a Ù±‚`bzsÙ±‚aoa=Ù±‚`akÙ±‚`a,Ù±‚`a Ù±‚`dzdirÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1ayÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`ecolorÙ±‚aoa=Ù±‚`bcsÙ±‚`a,Ù±‚`a Ù±‚`ealphaÙ±‚aoa=Ù±‚bmfc0.8Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`jset_xlabelÙ±‚`a(Ù±‚bs1a'Ù±‚bs1aXÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`jset_ylabelÙ±‚`a(Ù±‚bs1a'Ù±‚bs1aYÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`jset_zlabelÙ±‚`a(Ù±‚bs1a'Ù±‚bs1aZÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚bc1xK# On the y axis let's only label the discrete values that we have data for.Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`jset_yticksÙ±‚`a(Ù±‚`fyticksÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`cpltÙ±‚aoa.Ù±‚`dshowÙ±‚`a(Ù±‚`a)Ù±‚`a
`dNoneö