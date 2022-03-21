Ù¯‚Ù´ƒ™Ù±‚bsdxI"""
============
Oscilloscope
============

Emulates an oscilloscope.
"""Ù±‚`a
Ù±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„enumpyÙ „enumpyf1.22.3fmoduleenumpyfmoduleõÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnnbnpÙ±‚`a
Ù±‚bkndfromÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnnelinesÙ±‚`a Ù±‚bknfimportÙ±‚`a Ù±‚`fLine2DÙ±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnnfpyplotÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnncpltÙ±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnnianimationÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnnianimationÙ±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚akeclassÙ±‚`a Ù±‚bnceScopeÙ±‚`a:Ù±‚`a
Ù±‚`d    Ù±‚akcdefÙ±‚`a Ù±‚bfmh__init__Ù±‚`a(Ù±‚bbpdselfÙ±‚`a,Ù±‚`a Ù±‚`baxÙ±‚`a,Ù±‚`a Ù±‚`dmaxtÙ±‚aoa=Ù±‚bmia2Ù±‚`a,Ù±‚`a Ù±‚`bdtÙ±‚aoa=Ù±‚bmfd0.02Ù±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`baxÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`baxÙ±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`bdtÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bdtÙ±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`dmaxtÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`dmaxtÙ±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`etdataÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`a[Ù±‚bmia0Ù±‚`a]Ù±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`eydataÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`a[Ù±‚bmia0Ù±‚`a]Ù±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`dlineÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`fLine2DÙ±‚`a(Ù±‚bbpdselfÙ±‚aoa.Ù±‚`etdataÙ±‚`a,Ù±‚`a Ù±‚bbpdselfÙ±‚aoa.Ù±‚`eydataÙ±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`baxÙ±‚aoa.Ù±‚`hadd_lineÙ±‚`a(Ù±‚bbpdselfÙ±‚aoa.Ù±‚`dlineÙ±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`baxÙ±‚aoa.Ù±‚`hset_ylimÙ±‚`a(Ù±‚aoa-Ù±‚bmfb.1Ù±‚`a,Ù±‚`a Ù±‚bmfc1.1Ù±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`baxÙ±‚aoa.Ù±‚`hset_xlimÙ±‚`a(Ù±‚bmia0Ù±‚`a,Ù±‚`a Ù±‚bbpdselfÙ±‚aoa.Ù±‚`dmaxtÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚akcdefÙ±‚`a Ù±‚bnffupdateÙ±‚`a(Ù±‚bbpdselfÙ±‚`a,Ù±‚`a Ù±‚`ayÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`h        Ù±‚`elasttÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bbpdselfÙ±‚aoa.Ù±‚`etdataÙ±‚`a[Ù±‚aoa-Ù±‚bmia1Ù±‚`a]Ù±‚`a
Ù±‚`h        Ù±‚akbifÙ±‚`a Ù±‚`elasttÙ±‚`a Ù±‚aoa>Ù±‚`a Ù±‚bbpdselfÙ±‚aoa.Ù±‚`etdataÙ±‚`a[Ù±‚bmia0Ù±‚`a]Ù±‚`a Ù±‚aoa+Ù±‚`a Ù±‚bbpdselfÙ±‚aoa.Ù±‚`dmaxtÙ±‚`a:Ù±‚`b  Ù±‚bc1r# reset the arraysÙ±‚`a
Ù±‚`l            Ù±‚bbpdselfÙ±‚aoa.Ù±‚`etdataÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`a[Ù±‚bbpdselfÙ±‚aoa.Ù±‚`etdataÙ±‚`a[Ù±‚aoa-Ù±‚bmia1Ù±‚`a]Ù±‚`a]Ù±‚`a
Ù±‚`l            Ù±‚bbpdselfÙ±‚aoa.Ù±‚`eydataÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`a[Ù±‚bbpdselfÙ±‚aoa.Ù±‚`eydataÙ±‚`a[Ù±‚aoa-Ù±‚bmia1Ù±‚`a]Ù±‚`a]Ù±‚`a
Ù±‚`l            Ù±‚bbpdselfÙ±‚aoa.Ù±‚`baxÙ±‚aoa.Ù±‚`hset_xlimÙ±‚`a(Ù±‚bbpdselfÙ±‚aoa.Ù±‚`etdataÙ±‚`a[Ù±‚bmia0Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚bbpdselfÙ±‚aoa.Ù±‚`etdataÙ±‚`a[Ù±‚bmia0Ù±‚`a]Ù±‚`a Ù±‚aoa+Ù±‚`a Ù±‚bbpdselfÙ±‚aoa.Ù±‚`dmaxtÙ±‚`a)Ù±‚`a
Ù±‚`l            Ù±‚bbpdselfÙ±‚aoa.Ù±‚`baxÙ±‚aoa.Ù±‚`ffigureÙ±‚aoa.Ù±‚`fcanvasÙ±‚aoa.Ù±‚`ddrawÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`h        Ù±‚`atÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bbpdselfÙ±‚aoa.Ù±‚`etdataÙ±‚`a[Ù±‚aoa-Ù±‚bmia1Ù±‚`a]Ù±‚`a Ù±‚aoa+Ù±‚`a Ù±‚bbpdselfÙ±‚aoa.Ù±‚`bdtÙ±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`etdataÙ±‚aoa.Ù±‚`fappendÙ±‚`a(Ù±‚`atÙ±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`eydataÙ±‚aoa.Ù±‚`fappendÙ±‚`a(Ù±‚`ayÙ±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`dlineÙ±‚aoa.Ù±‚`hset_dataÙ±‚`a(Ù±‚bbpdselfÙ±‚aoa.Ù±‚`etdataÙ±‚`a,Ù±‚`a Ù±‚bbpdselfÙ±‚aoa.Ù±‚`eydataÙ±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚akfreturnÙ±‚`a Ù±‚bbpdselfÙ±‚aoa.Ù±‚`dlineÙ±‚`a,Ù±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚akcdefÙ±‚`a Ù±‚bnfgemitterÙ±‚`a(Ù±‚`apÙ±‚aoa=Ù±‚bmfc0.1Ù±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`d    Ù±‚bsdxA"""Return a random value in [0, 1) with probability p, else 0."""Ù±‚`a
Ù±‚`d    Ù±‚akewhileÙ±‚`a Ù±‚bkcdTrueÙ±‚`a:Ù±‚`a
Ù±‚`h        Ù±‚`avÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`frandomÙ±‚aoa.Ù±‚`drandÙ±‚`a(Ù±‚bmia1Ù±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚akbifÙ±‚`a Ù±‚`avÙ±‚`a Ù±‚aoa>Ù±‚`a Ù±‚`apÙ±‚`a:Ù±‚`a
Ù±‚`l            Ù±‚akeyieldÙ±‚`a Ù±‚bmfb0.Ù±‚`a
Ù±‚`h        Ù±‚akdelseÙ±‚`a:Ù±‚`a
Ù±‚`l            Ù±‚akeyieldÙ±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`frandomÙ±‚aoa.Ù±‚`drandÙ±‚`a(Ù±‚bmia1Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚bc1x)# Fixing random state for reproducibilityÙ±‚`a
Ù±‚`bnpÙ±‚aoa.Ù±‚`frandomÙ±‚aoa.Ù±‚`dseedÙ±‚`a(Ù±‚bmih19680801Ù±‚`a Ù±‚aoa/Ù±‚aoa/Ù±‚`a Ù±‚bmib10Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚`cfigÙ±‚`a,Ù±‚`a Ù±‚`baxÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cpltÙ±‚aoa.Ù±‚`hsubplotsÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`escopeÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`eScopeÙ±‚`a(Ù±‚`baxÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚bc1xC# pass a generator in "emitter" to produce data for the update funcÙ±‚`a
Ù±‚`caniÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`ianimationÙ±‚aoa.Ù±‚`mFuncAnimationÙ±‚`a(Ù±‚`cfigÙ±‚`a,Ù±‚`a Ù±‚`escopeÙ±‚aoa.Ù±‚`fupdateÙ±‚`a,Ù±‚`a Ù±‚`gemitterÙ±‚`a,Ù±‚`a Ù±‚`hintervalÙ±‚aoa=Ù±‚bmib50Ù±‚`a,Ù±‚`a
Ù±‚`x                              Ù±‚`dblitÙ±‚aoa=Ù±‚bkcdTrueÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`cpltÙ±‚aoa.Ù±‚`dshowÙ±‚`a(Ù±‚`a)Ù±‚`a
`dNoneö