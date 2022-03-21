Ù¯‚Ù´ƒ™JÙ±‚bsdxÕ"""
=====================
Hexagonal binned plot
=====================

`~.Axes.hexbin` is a 2D histogram plot, in which the bins are hexagons and
the color represents the number of data points within each bin.
"""Ù±‚`a
Ù±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„enumpyÙ „enumpyf1.22.3fmoduleenumpyfmoduleõÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnnbnpÙ±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnnfpyplotÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnncpltÙ±‚`a
Ù±‚`a
Ù±‚bc1x)# Fixing random state for reproducibilityÙ±‚`a
Ù±‚`bnpÙ±‚aoa.Ù±‚`frandomÙ±‚aoa.Ù±‚`dseedÙ±‚`a(Ù±‚bmih19680801Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`anÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bmig100_000Ù±‚`a
Ù±‚`axÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`frandomÙ±‚aoa.Ù±‚`ostandard_normalÙ±‚`a(Ù±‚`anÙ±‚`a)Ù±‚`a
Ù±‚`ayÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bmfc2.0Ù±‚`a Ù±‚aoa+Ù±‚`a Ù±‚bmfc3.0Ù±‚`a Ù±‚aoa*Ù±‚`a Ù±‚`axÙ±‚`a Ù±‚aoa+Ù±‚`a Ù±‚bmfc4.0Ù±‚`a Ù±‚aoa*Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`frandomÙ±‚aoa.Ù±‚`ostandard_normalÙ±‚`a(Ù±‚`anÙ±‚`a)Ù±‚`a
Ù±‚`dxlimÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`axÙ±‚aoa.Ù±‚`cminÙ±‚`a(Ù±‚`a)Ù±‚`a,Ù±‚`a Ù±‚`axÙ±‚aoa.Ù±‚`cmaxÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`dylimÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`ayÙ±‚aoa.Ù±‚`cminÙ±‚`a(Ù±‚`a)Ù±‚`a,Ù±‚`a Ù±‚`ayÙ±‚aoa.Ù±‚`cmaxÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`cfigÙ±‚`a,Ù±‚`a Ù±‚`a(Ù±‚`cax0Ù±‚`a,Ù±‚`a Ù±‚`cax1Ù±‚`a)Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cpltÙ±‚aoa.Ù±‚`hsubplotsÙ±‚`a(Ù±‚`encolsÙ±‚aoa=Ù±‚bmia2Ù±‚`a,Ù±‚`a Ù±‚`fshareyÙ±‚aoa=Ù±‚bkcdTrueÙ±‚`a,Ù±‚`a Ù±‚`gfigsizeÙ±‚aoa=Ù±‚`a(Ù±‚bmia9Ù±‚`a,Ù±‚`a Ù±‚bmia4Ù±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`bhbÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cax0Ù±‚aoa.Ù±‚`fhexbinÙ±‚`a(Ù±‚`axÙ±‚`a,Ù±‚`a Ù±‚`ayÙ±‚`a,Ù±‚`a Ù±‚`hgridsizeÙ±‚aoa=Ù±‚bmib50Ù±‚`a,Ù±‚`a Ù±‚`dcmapÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1ginfernoÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`cax0Ù±‚aoa.Ù±‚`csetÙ±‚`a(Ù±‚`dxlimÙ±‚aoa=Ù±‚`dxlimÙ±‚`a,Ù±‚`a Ù±‚`dylimÙ±‚aoa=Ù±‚`dylimÙ±‚`a)Ù±‚`a
Ù±‚`cax0Ù±‚aoa.Ù±‚`iset_titleÙ±‚`a(Ù±‚bs2a"Ù±‚bs2oHexagon binningÙ±‚bs2a"Ù±‚`a)Ù±‚`a
Ù±‚`bcbÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cfigÙ±‚aoa.Ù±‚`hcolorbarÙ±‚`a(Ù±‚`bhbÙ±‚`a,Ù±‚`a Ù±‚`baxÙ±‚aoa=Ù±‚`cax0Ù±‚`a,Ù±‚`a Ù±‚`elabelÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1fcountsÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`bhbÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cax1Ù±‚aoa.Ù±‚`fhexbinÙ±‚`a(Ù±‚`axÙ±‚`a,Ù±‚`a Ù±‚`ayÙ±‚`a,Ù±‚`a Ù±‚`hgridsizeÙ±‚aoa=Ù±‚bmib50Ù±‚`a,Ù±‚`a Ù±‚`dbinsÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1clogÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`dcmapÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1ginfernoÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`cax1Ù±‚aoa.Ù±‚`csetÙ±‚`a(Ù±‚`dxlimÙ±‚aoa=Ù±‚`dxlimÙ±‚`a,Ù±‚`a Ù±‚`dylimÙ±‚aoa=Ù±‚`dylimÙ±‚`a)Ù±‚`a
Ù±‚`cax1Ù±‚aoa.Ù±‚`iset_titleÙ±‚`a(Ù±‚bs2a"Ù±‚bs2vWith a log color scaleÙ±‚bs2a"Ù±‚`a)Ù±‚`a
Ù±‚`bcbÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cfigÙ±‚aoa.Ù±‚`hcolorbarÙ±‚`a(Ù±‚`bhbÙ±‚`a,Ù±‚`a Ù±‚`baxÙ±‚aoa=Ù±‚`cax1Ù±‚`a,Ù±‚`a Ù±‚`elabelÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1hlog10(N)Ù±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`cpltÙ±‚aoa.Ù±‚`dshowÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚bc1xM#############################################################################Ù±‚`a
Ù±‚bc1a#Ù±‚`a
Ù±‚bc1x# .. admonition:: ReferencesÙ±‚`a
Ù±‚bc1a#Ù±‚`a
Ù±‚bc1xN#    The use of the following functions, methods, classes and modules is shownÙ±‚`a
Ù±‚bc1u#    in this example:Ù±‚`a
Ù±‚bc1a#Ù±‚`a
Ù±‚bc1xA#    - `matplotlib.axes.Axes.hexbin` / `matplotlib.pyplot.hexbin`Ù±‚`a
`dNoneö