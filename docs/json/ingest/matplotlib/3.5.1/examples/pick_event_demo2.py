Ù¯‚Ù´ƒ™TÙ±‚bsdy"""
================
Pick Event Demo2
================

Compute the mean (mu) and standard deviation (sigma) of 100 data sets and plot
mu vs. sigma.  When you click on one of the (mu, sigma) points, plot the raw
data from the dataset that generated this point.
"""Ù±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„enumpyÙ „enumpyf1.22.3fmoduleenumpyfmoduleõÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnnbnpÙ±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnnfpyplotÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnncpltÙ±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚bc1x)# Fixing random state for reproducibilityÙ±‚`a
Ù±‚`bnpÙ±‚aoa.Ù±‚`frandomÙ±‚aoa.Ù±‚`dseedÙ±‚`a(Ù±‚bmih19680801Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`aXÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`frandomÙ±‚aoa.Ù±‚`drandÙ±‚`a(Ù±‚bmic100Ù±‚`a,Ù±‚`a Ù±‚bmid1000Ù±‚`a)Ù±‚`a
Ù±‚`bxsÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`dmeanÙ±‚`a(Ù±‚`aXÙ±‚`a,Ù±‚`a Ù±‚`daxisÙ±‚aoa=Ù±‚bmia1Ù±‚`a)Ù±‚`a
Ù±‚`bysÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`cstdÙ±‚`a(Ù±‚`aXÙ±‚`a,Ù±‚`a Ù±‚`daxisÙ±‚aoa=Ù±‚bmia1Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`cfigÙ±‚`a,Ù±‚`a Ù±‚`baxÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cpltÙ±‚aoa.Ù±‚`hsubplotsÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`iset_titleÙ±‚`a(Ù±‚bs1a'Ù±‚bs1x"click on point to plot time seriesÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`dlineÙ±‚`a,Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`baxÙ±‚aoa.Ù±‚`dplotÙ±‚`a(Ù±‚`bxsÙ±‚`a,Ù±‚`a Ù±‚`bysÙ±‚`a,Ù±‚`a Ù±‚bs1a'Ù±‚bs1aoÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`fpickerÙ±‚aoa=Ù±‚bkcdTrueÙ±‚`a,Ù±‚`a Ù±‚`jpickradiusÙ±‚aoa=Ù±‚bmia5Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚akcdefÙ±‚`a Ù±‚bnffonpickÙ±‚`a(Ù±‚`eeventÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚akbifÙ±‚`a Ù±‚`eeventÙ±‚aoa.Ù±‚`fartistÙ±‚`a Ù±‚aob!=Ù±‚`a Ù±‚`dlineÙ±‚`a:Ù±‚`a
Ù±‚`h        Ù±‚akfreturnÙ±‚`a Ù±‚bkcdTrueÙ±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚`aNÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bnbclenÙ±‚`a(Ù±‚`eeventÙ±‚aoa.Ù±‚`cindÙ±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚akbifÙ±‚`a Ù±‚bowcnotÙ±‚`a Ù±‚`aNÙ±‚`a:Ù±‚`a
Ù±‚`h        Ù±‚akfreturnÙ±‚`a Ù±‚bkcdTrueÙ±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚`dfigiÙ±‚`a,Ù±‚`a Ù±‚`caxsÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cpltÙ±‚aoa.Ù±‚`hsubplotsÙ±‚`a(Ù±‚`aNÙ±‚`a,Ù±‚`a Ù±‚`gsqueezeÙ±‚aoa=Ù±‚bkceFalseÙ±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚akcforÙ±‚`a Ù±‚`baxÙ±‚`a,Ù±‚`a Ù±‚`gdataindÙ±‚`a Ù±‚bowbinÙ±‚`a Ù±‚bnbczipÙ±‚`a(Ù±‚`caxsÙ±‚aoa.Ù±‚`dflatÙ±‚`a,Ù±‚`a Ù±‚`eeventÙ±‚aoa.Ù±‚`cindÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`h        Ù±‚`baxÙ±‚aoa.Ù±‚`dplotÙ±‚`a(Ù±‚`aXÙ±‚`a[Ù±‚`gdataindÙ±‚`a]Ù±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚`baxÙ±‚aoa.Ù±‚`dtextÙ±‚`a(Ù±‚bmfc.05Ù±‚`a,Ù±‚`a Ù±‚bmfb.9Ù±‚`a,Ù±‚`a Ù±‚bs1a'Ù±‚bs1cmu=Ù±‚bsie%1.3fÙ±‚bseb\nÙ±‚bs1fsigma=Ù±‚bsie%1.3fÙ±‚bs1a'Ù±‚`a Ù±‚aoa%Ù±‚`a Ù±‚`a(Ù±‚`bxsÙ±‚`a[Ù±‚`gdataindÙ±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`bysÙ±‚`a[Ù±‚`gdataindÙ±‚`a]Ù±‚`a)Ù±‚`a,Ù±‚`a
Ù±‚`p                Ù±‚`itransformÙ±‚aoa=Ù±‚`baxÙ±‚aoa.Ù±‚`itransAxesÙ±‚`a,Ù±‚`a Ù±‚`bvaÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1ctopÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚`baxÙ±‚aoa.Ù±‚`hset_ylimÙ±‚`a(Ù±‚aoa-Ù±‚bmfc0.5Ù±‚`a,Ù±‚`a Ù±‚bmfc1.5Ù±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`dfigiÙ±‚aoa.Ù±‚`dshowÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚akfreturnÙ±‚`a Ù±‚bkcdTrueÙ±‚`a
Ù±‚`a
Ù±‚`cfigÙ±‚aoa.Ù±‚`fcanvasÙ±‚aoa.Ù±‚`kmpl_connectÙ±‚`a(Ù±‚bs1a'Ù±‚bs1jpick_eventÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`fonpickÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`cpltÙ±‚aoa.Ù±‚`dshowÙ±‚`a(Ù±‚`a)Ù±‚`a
`dNoneö