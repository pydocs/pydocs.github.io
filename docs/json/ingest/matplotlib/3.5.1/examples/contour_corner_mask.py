Ù¯‚Ù´ƒ™nÙ±‚bsdx¯"""
===================
Contour Corner Mask
===================

Illustrate the difference between ``corner_mask=False`` and
``corner_mask=True`` for masked contour plots.
"""Ù±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnnfpyplotÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnncpltÙ±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„enumpyÙ „enumpyf1.22.3fmoduleenumpyfmoduleõÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnnbnpÙ±‚`a
Ù±‚`a
Ù±‚bc1o# Data to plot.Ù±‚`a
Ù±‚`axÙ±‚`a,Ù±‚`a Ù±‚`ayÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`hmeshgridÙ±‚`a(Ù±‚`bnpÙ±‚aoa.Ù±‚`farangeÙ±‚`a(Ù±‚bmia7Ù±‚`a)Ù±‚`a,Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`farangeÙ±‚`a(Ù±‚bmib10Ù±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`azÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`csinÙ±‚`a(Ù±‚bmfc0.5Ù±‚`a Ù±‚aoa*Ù±‚`a Ù±‚`axÙ±‚`a)Ù±‚`a Ù±‚aoa*Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`ccosÙ±‚`a(Ù±‚bmfd0.52Ù±‚`a Ù±‚aoa*Ù±‚`a Ù±‚`ayÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚bc1x# Mask various z values.Ù±‚`a
Ù±‚`dmaskÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`jzeros_likeÙ±‚`a(Ù±‚`azÙ±‚`a,Ù±‚`a Ù±‚`edtypeÙ±‚aoa=Ù±‚bnbdboolÙ±‚`a)Ù±‚`a
Ù±‚`dmaskÙ±‚`a[Ù±‚bmia2Ù±‚`a,Ù±‚`a Ù±‚bmia3Ù±‚`a:Ù±‚bmia5Ù±‚`a]Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bkcdTrueÙ±‚`a
Ù±‚`dmaskÙ±‚`a[Ù±‚bmia3Ù±‚`a:Ù±‚bmia5Ù±‚`a,Ù±‚`a Ù±‚bmia4Ù±‚`a]Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bkcdTrueÙ±‚`a
Ù±‚`dmaskÙ±‚`a[Ù±‚bmia7Ù±‚`a,Ù±‚`a Ù±‚bmia2Ù±‚`a]Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bkcdTrueÙ±‚`a
Ù±‚`dmaskÙ±‚`a[Ù±‚bmia5Ù±‚`a,Ù±‚`a Ù±‚bmia0Ù±‚`a]Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bkcdTrueÙ±‚`a
Ù±‚`dmaskÙ±‚`a[Ù±‚bmia0Ù±‚`a,Ù±‚`a Ù±‚bmia6Ù±‚`a]Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bkcdTrueÙ±‚`a
Ù±‚`azÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`bmaÙ±‚aoa.Ù±‚`earrayÙ±‚`a(Ù±‚`azÙ±‚`a,Ù±‚`a Ù±‚`dmaskÙ±‚aoa=Ù±‚`dmaskÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`lcorner_masksÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`a[Ù±‚bkceFalseÙ±‚`a,Ù±‚`a Ù±‚bkcdTrueÙ±‚`a]Ù±‚`a
Ù±‚`cfigÙ±‚`a,Ù±‚`a Ù±‚`caxsÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cpltÙ±‚aoa.Ù±‚`hsubplotsÙ±‚`a(Ù±‚`encolsÙ±‚aoa=Ù±‚bmia2Ù±‚`a)Ù±‚`a
Ù±‚akcforÙ±‚`a Ù±‚`baxÙ±‚`a,Ù±‚`a Ù±‚`kcorner_maskÙ±‚`a Ù±‚bowbinÙ±‚`a Ù±‚bnbczipÙ±‚`a(Ù±‚`caxsÙ±‚`a,Ù±‚`a Ù±‚`lcorner_masksÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`d    Ù±‚`bcsÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`baxÙ±‚aoa.Ù±‚`hcontourfÙ±‚`a(Ù±‚`axÙ±‚`a,Ù±‚`a Ù±‚`ayÙ±‚`a,Ù±‚`a Ù±‚`azÙ±‚`a,Ù±‚`a Ù±‚`kcorner_maskÙ±‚aoa=Ù±‚`kcorner_maskÙ±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`baxÙ±‚aoa.Ù±‚`gcontourÙ±‚`a(Ù±‚`bcsÙ±‚`a,Ù±‚`a Ù±‚`fcolorsÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1akÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`baxÙ±‚aoa.Ù±‚`iset_titleÙ±‚`a(Ù±‚bs1a'Ù±‚bs1ncorner_mask = Ù±‚bsic{0}Ù±‚bs1a'Ù±‚aoa.Ù±‚`fformatÙ±‚`a(Ù±‚`kcorner_maskÙ±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚bc1l# Plot grid.Ù±‚`a
Ù±‚`d    Ù±‚`baxÙ±‚aoa.Ù±‚`dgridÙ±‚`a(Ù±‚`acÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1akÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`blsÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1a-Ù±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`ealphaÙ±‚aoa=Ù±‚bmfc0.3Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚bc1x*# Indicate masked points with red circles.Ù±‚`a
Ù±‚`d    Ù±‚`baxÙ±‚aoa.Ù±‚`dplotÙ±‚`a(Ù±‚`bnpÙ±‚aoa.Ù±‚`bmaÙ±‚aoa.Ù±‚`earrayÙ±‚`a(Ù±‚`axÙ±‚`a,Ù±‚`a Ù±‚`dmaskÙ±‚aoa=Ù±‚aoa~Ù±‚`dmaskÙ±‚`a)Ù±‚`a,Ù±‚`a Ù±‚`ayÙ±‚`a,Ù±‚`a Ù±‚bs1a'Ù±‚bs1broÙ±‚bs1a'Ù±‚`a)Ù±‚`a
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
Ù±‚bc1xC#    - `matplotlib.axes.Axes.contour` / `matplotlib.pyplot.contour`Ù±‚`a
Ù±‚bc1xE#    - `matplotlib.axes.Axes.contourf` / `matplotlib.pyplot.contourf`Ù±‚`a
`dNoneö