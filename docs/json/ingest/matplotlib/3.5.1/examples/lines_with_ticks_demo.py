Ù¯‚Ù´ƒ˜·Ù±‚bsdyI"""
==============================
Lines with a ticked patheffect
==============================

Ticks can be added along a line to mark one side as a barrier using
`~matplotlib.patheffects.TickedStroke`.  You can control the angle,
spacing, and length of the ticks.

The ticks will also appear appropriately in the legend.

"""Ù±‚`a
Ù±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„enumpyÙ „enumpyf1.22.3fmoduleenumpyfmoduleõÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnnbnpÙ±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnnfpyplotÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnncpltÙ±‚`a
Ù±‚bkndfromÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚`a Ù±‚bknfimportÙ±‚`a Ù±‚`kpatheffectsÙ±‚`a
Ù±‚`a
Ù±‚`cfigÙ±‚`a,Ù±‚`a Ù±‚`baxÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cpltÙ±‚aoa.Ù±‚`hsubplotsÙ±‚`a(Ù±‚`gfigsizeÙ±‚aoa=Ù±‚`a(Ù±‚bmia6Ù±‚`a,Ù±‚`a Ù±‚bmia6Ù±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`dplotÙ±‚`a(Ù±‚`a[Ù±‚bmia0Ù±‚`a,Ù±‚`a Ù±‚bmia1Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`a[Ù±‚bmia0Ù±‚`a,Ù±‚`a Ù±‚bmia1Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`elabelÙ±‚aoa=Ù±‚bs2a"Ù±‚bs2dLineÙ±‚bs2a"Ù±‚`a,Ù±‚`a
Ù±‚`h        Ù±‚`lpath_effectsÙ±‚aoa=Ù±‚`a[Ù±‚`kpatheffectsÙ±‚aoa.Ù±‚`pwithTickedStrokeÙ±‚`a(Ù±‚`gspacingÙ±‚aoa=Ù±‚bmia7Ù±‚`a,Ù±‚`a Ù±‚`eangleÙ±‚aoa=Ù±‚bmic135Ù±‚`a)Ù±‚`a]Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`bnxÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bmic101Ù±‚`a
Ù±‚`axÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`hlinspaceÙ±‚`a(Ù±‚bmfc0.0Ù±‚`a,Ù±‚`a Ù±‚bmfc1.0Ù±‚`a,Ù±‚`a Ù±‚`bnxÙ±‚`a)Ù±‚`a
Ù±‚`ayÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bmfc0.3Ù±‚aoa*Ù±‚`bnpÙ±‚aoa.Ù±‚`csinÙ±‚`a(Ù±‚`axÙ±‚aoa*Ù±‚bmia8Ù±‚`a)Ù±‚`a Ù±‚aoa+Ù±‚`a Ù±‚bmfc0.4Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`dplotÙ±‚`a(Ù±‚`axÙ±‚`a,Ù±‚`a Ù±‚`ayÙ±‚`a,Ù±‚`a Ù±‚`elabelÙ±‚aoa=Ù±‚bs2a"Ù±‚bs2eCurveÙ±‚bs2a"Ù±‚`a,Ù±‚`a Ù±‚`lpath_effectsÙ±‚aoa=Ù±‚`a[Ù±‚`kpatheffectsÙ±‚aoa.Ù±‚`pwithTickedStrokeÙ±‚`a(Ù±‚`a)Ù±‚`a]Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`flegendÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`cpltÙ±‚aoa.Ù±‚`dshowÙ±‚`a(Ù±‚`a)Ù±‚`a
`dNoneö