Ù¯‚Ù´ƒ™şÙ±‚bsdy"""
================
The Bayes update
================

This animation displays the posterior estimate updates as it is refitted when
new data arrives.
The vertical line represents the theoretical value to which the plotted
distribution should converge.
"""Ù±‚`a
Ù±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnndmathÙ±‚`a
Ù±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„enumpyÙ „enumpyf1.22.3fmoduleenumpyfmoduleõÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnnbnpÙ±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnnfpyplotÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnncpltÙ±‚`a
Ù±‚bkndfromÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnnianimationÙ±‚`a Ù±‚bknfimportÙ±‚`a Ù±‚`mFuncAnimationÙ±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚akcdefÙ±‚`a Ù±‚bnfhbeta_pdfÙ±‚`a(Ù±‚`axÙ±‚`a,Ù±‚`a Ù±‚`aaÙ±‚`a,Ù±‚`a Ù±‚`abÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`d    Ù±‚akfreturnÙ±‚`a Ù±‚`a(Ù±‚`axÙ±‚aoa*Ù±‚aoa*Ù±‚`a(Ù±‚`aaÙ±‚aoa-Ù±‚bmia1Ù±‚`a)Ù±‚`a Ù±‚aoa*Ù±‚`a Ù±‚`a(Ù±‚bmia1Ù±‚aoa-Ù±‚`axÙ±‚`a)Ù±‚aoa*Ù±‚aoa*Ù±‚`a(Ù±‚`abÙ±‚aoa-Ù±‚bmia1Ù±‚`a)Ù±‚`a Ù±‚aoa*Ù±‚`a Ù±‚`dmathÙ±‚aoa.Ù±‚`egammaÙ±‚`a(Ù±‚`aaÙ±‚`a Ù±‚aoa+Ù±‚`a Ù±‚`abÙ±‚`a)Ù±‚`a
Ù±‚`l            Ù±‚aoa/Ù±‚`a Ù±‚`a(Ù±‚`dmathÙ±‚aoa.Ù±‚`egammaÙ±‚`a(Ù±‚`aaÙ±‚`a)Ù±‚`a Ù±‚aoa*Ù±‚`a Ù±‚`dmathÙ±‚aoa.Ù±‚`egammaÙ±‚`a(Ù±‚`abÙ±‚`a)Ù±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚akeclassÙ±‚`a Ù±‚bncjUpdateDistÙ±‚`a:Ù±‚`a
Ù±‚`d    Ù±‚akcdefÙ±‚`a Ù±‚bfmh__init__Ù±‚`a(Ù±‚bbpdselfÙ±‚`a,Ù±‚`a Ù±‚`baxÙ±‚`a,Ù±‚`a Ù±‚`dprobÙ±‚aoa=Ù±‚bmfc0.5Ù±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`gsuccessÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bmia0Ù±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`dprobÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`dprobÙ±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`dlineÙ±‚`a,Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`baxÙ±‚aoa.Ù±‚`dplotÙ±‚`a(Ù±‚`a[Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`a[Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚bs1a'Ù±‚bs1bk-Ù±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`axÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`hlinspaceÙ±‚`a(Ù±‚bmia0Ù±‚`a,Ù±‚`a Ù±‚bmia1Ù±‚`a,Ù±‚`a Ù±‚bmic200Ù±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`baxÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`baxÙ±‚`a
Ù±‚`a
Ù±‚`h        Ù±‚bc1x# Set up plot parametersÙ±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`baxÙ±‚aoa.Ù±‚`hset_xlimÙ±‚`a(Ù±‚bmia0Ù±‚`a,Ù±‚`a Ù±‚bmia1Ù±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`baxÙ±‚aoa.Ù±‚`hset_ylimÙ±‚`a(Ù±‚bmia0Ù±‚`a,Ù±‚`a Ù±‚bmib10Ù±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`baxÙ±‚aoa.Ù±‚`dgridÙ±‚`a(Ù±‚bkcdTrueÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`h        Ù±‚bc1x9# This vertical line represents the theoretical value, toÙ±‚`a
Ù±‚`h        Ù±‚bc1x1# which the plotted distribution should converge.Ù±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`baxÙ±‚aoa.Ù±‚`gaxvlineÙ±‚`a(Ù±‚`dprobÙ±‚`a,Ù±‚`a Ù±‚`ilinestyleÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1b--Ù±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`ecolorÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1eblackÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚akcdefÙ±‚`a Ù±‚bfmh__call__Ù±‚`a(Ù±‚bbpdselfÙ±‚`a,Ù±‚`a Ù±‚`aiÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`h        Ù±‚bc1x9# This way the plot can continuously run and we just keepÙ±‚`a
Ù±‚`h        Ù±‚bc1x*# watching new realizations of the processÙ±‚`a
Ù±‚`h        Ù±‚akbifÙ±‚`a Ù±‚`aiÙ±‚`a Ù±‚aob==Ù±‚`a Ù±‚bmia0Ù±‚`a:Ù±‚`a
Ù±‚`l            Ù±‚bbpdselfÙ±‚aoa.Ù±‚`gsuccessÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bmia0Ù±‚`a
Ù±‚`l            Ù±‚bbpdselfÙ±‚aoa.Ù±‚`dlineÙ±‚aoa.Ù±‚`hset_dataÙ±‚`a(Ù±‚`a[Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`a[Ù±‚`a]Ù±‚`a)Ù±‚`a
Ù±‚`l            Ù±‚akfreturnÙ±‚`a Ù±‚bbpdselfÙ±‚aoa.Ù±‚`dlineÙ±‚`a,Ù±‚`a
Ù±‚`a
Ù±‚`h        Ù±‚bc1x@# Choose success based on exceed a threshold with a uniform pickÙ±‚`a
Ù±‚`h        Ù±‚akbifÙ±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`frandomÙ±‚aoa.Ù±‚`drandÙ±‚`a(Ù±‚bmia1Ù±‚`a,Ù±‚`a)Ù±‚`a Ù±‚aoa<Ù±‚`a Ù±‚bbpdselfÙ±‚aoa.Ù±‚`dprobÙ±‚`a:Ù±‚`a
Ù±‚`l            Ù±‚bbpdselfÙ±‚aoa.Ù±‚`gsuccessÙ±‚`a Ù±‚aoa+Ù±‚aoa=Ù±‚`a Ù±‚bmia1Ù±‚`a
Ù±‚`h        Ù±‚`ayÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`hbeta_pdfÙ±‚`a(Ù±‚bbpdselfÙ±‚aoa.Ù±‚`axÙ±‚`a,Ù±‚`a Ù±‚bbpdselfÙ±‚aoa.Ù±‚`gsuccessÙ±‚`a Ù±‚aoa+Ù±‚`a Ù±‚bmia1Ù±‚`a,Ù±‚`a Ù±‚`a(Ù±‚`aiÙ±‚`a Ù±‚aoa-Ù±‚`a Ù±‚bbpdselfÙ±‚aoa.Ù±‚`gsuccessÙ±‚`a)Ù±‚`a Ù±‚aoa+Ù±‚`a Ù±‚bmia1Ù±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`dlineÙ±‚aoa.Ù±‚`hset_dataÙ±‚`a(Ù±‚bbpdselfÙ±‚aoa.Ù±‚`axÙ±‚`a,Ù±‚`a Ù±‚`ayÙ±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚akfreturnÙ±‚`a Ù±‚bbpdselfÙ±‚aoa.Ù±‚`dlineÙ±‚`a,Ù±‚`a
Ù±‚`a
Ù±‚bc1x)# Fixing random state for reproducibilityÙ±‚`a
Ù±‚`bnpÙ±‚aoa.Ù±‚`frandomÙ±‚aoa.Ù±‚`dseedÙ±‚`a(Ù±‚bmih19680801Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚`cfigÙ±‚`a,Ù±‚`a Ù±‚`baxÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cpltÙ±‚aoa.Ù±‚`hsubplotsÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`budÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`jUpdateDistÙ±‚`a(Ù±‚`baxÙ±‚`a,Ù±‚`a Ù±‚`dprobÙ±‚aoa=Ù±‚bmfc0.7Ù±‚`a)Ù±‚`a
Ù±‚`danimÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`mFuncAnimationÙ±‚`a(Ù±‚`cfigÙ±‚`a,Ù±‚`a Ù±‚`budÙ±‚`a,Ù±‚`a Ù±‚`fframesÙ±‚aoa=Ù±‚bmic100Ù±‚`a,Ù±‚`a Ù±‚`hintervalÙ±‚aoa=Ù±‚bmic100Ù±‚`a,Ù±‚`a Ù±‚`dblitÙ±‚aoa=Ù±‚bkcdTrueÙ±‚`a)Ù±‚`a
Ù±‚`cpltÙ±‚aoa.Ù±‚`dshowÙ±‚`a(Ù±‚`a)Ù±‚`a
`dNoneö