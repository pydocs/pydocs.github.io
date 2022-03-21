Ù¯‚Ù´ƒ˜ÍÙ±‚bsdx~"""
================
Color by y-value
================

Use masked arrays to plot a line with different colors by y-value.
"""Ù±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„enumpyÙ „enumpyf1.22.3fmoduleenumpyfmoduleõÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnnbnpÙ±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnnfpyplotÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnncpltÙ±‚`a
Ù±‚`a
Ù±‚`atÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`farangeÙ±‚`a(Ù±‚bmfc0.0Ù±‚`a,Ù±‚`a Ù±‚bmfc2.0Ù±‚`a,Ù±‚`a Ù±‚bmfd0.01Ù±‚`a)Ù±‚`a
Ù±‚`asÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`csinÙ±‚`a(Ù±‚bmia2Ù±‚`a Ù±‚aoa*Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`bpiÙ±‚`a Ù±‚aoa*Ù±‚`a Ù±‚`atÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`eupperÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bmfd0.77Ù±‚`a
Ù±‚`elowerÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚aoa-Ù±‚bmfd0.77Ù±‚`a
Ù±‚`a
Ù±‚`fsupperÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`bmaÙ±‚aoa.Ù±‚`lmasked_whereÙ±‚`a(Ù±‚`asÙ±‚`a Ù±‚aoa<Ù±‚`a Ù±‚`eupperÙ±‚`a,Ù±‚`a Ù±‚`asÙ±‚`a)Ù±‚`a
Ù±‚`fslowerÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`bmaÙ±‚aoa.Ù±‚`lmasked_whereÙ±‚`a(Ù±‚`asÙ±‚`a Ù±‚aoa>Ù±‚`a Ù±‚`elowerÙ±‚`a,Ù±‚`a Ù±‚`asÙ±‚`a)Ù±‚`a
Ù±‚`gsmiddleÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`bmaÙ±‚aoa.Ù±‚`lmasked_whereÙ±‚`a(Ù±‚`a(Ù±‚`asÙ±‚`a Ù±‚aoa<Ù±‚`a Ù±‚`elowerÙ±‚`a)Ù±‚`a Ù±‚aoa|Ù±‚`a Ù±‚`a(Ù±‚`asÙ±‚`a Ù±‚aoa>Ù±‚`a Ù±‚`eupperÙ±‚`a)Ù±‚`a,Ù±‚`a Ù±‚`asÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`cfigÙ±‚`a,Ù±‚`a Ù±‚`baxÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cpltÙ±‚aoa.Ù±‚`hsubplotsÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`dplotÙ±‚`a(Ù±‚`atÙ±‚`a,Ù±‚`a Ù±‚`gsmiddleÙ±‚`a,Ù±‚`a Ù±‚`atÙ±‚`a,Ù±‚`a Ù±‚`fslowerÙ±‚`a,Ù±‚`a Ù±‚`atÙ±‚`a,Ù±‚`a Ù±‚`fsupperÙ±‚`a)Ù±‚`a
Ù±‚`cpltÙ±‚aoa.Ù±‚`dshowÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚bc1xM#############################################################################Ù±‚`a
Ù±‚bc1a#Ù±‚`a
Ù±‚bc1x# .. admonition:: ReferencesÙ±‚`a
Ù±‚bc1a#Ù±‚`a
Ù±‚bc1xN#    The use of the following functions, methods, classes and modules is shownÙ±‚`a
Ù±‚bc1u#    in this example:Ù±‚`a
Ù±‚bc1a#Ù±‚`a
Ù±‚bc1x=#    - `matplotlib.axes.Axes.plot` / `matplotlib.pyplot.plot`Ù±‚`a
`dNoneö