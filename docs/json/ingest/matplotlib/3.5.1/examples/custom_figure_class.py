Ù¯‚Ù´ƒ™+Ù±‚bsdyù"""
========================
Custom Figure subclasses
========================

You can pass a `.Figure` subclass to `.pyplot.figure` if you want to change
the default behavior of the figure.

This example defines a `.Figure` subclass ``WatermarkFigure`` that accepts an
additional parameter ``watermark`` to display a custom watermark text. The
figure is created using the ``FigureClass`` parameter of `.pyplot.figure`.
The additional ``watermark`` parameter is passed on to the subclass
constructor.
"""Ù±‚`a
Ù±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnnfpyplotÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnncpltÙ±‚`a
Ù±‚bkndfromÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnnffigureÙ±‚`a Ù±‚bknfimportÙ±‚`a Ù±‚`fFigureÙ±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„enumpyÙ „enumpyf1.22.3fmoduleenumpyfmoduleõÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnnbnpÙ±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚akeclassÙ±‚`a Ù±‚bncoWatermarkFigureÙ±‚`a(Ù±‚`fFigureÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`d    Ù±‚bsdx%"""A figure with a text watermark."""Ù±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚akcdefÙ±‚`a Ù±‚bfmh__init__Ù±‚`a(Ù±‚bbpdselfÙ±‚`a,Ù±‚`a Ù±‚aoa*Ù±‚`dargsÙ±‚`a,Ù±‚`a Ù±‚`iwatermarkÙ±‚aoa=Ù±‚bkcdNoneÙ±‚`a,Ù±‚`a Ù±‚aoa*Ù±‚aoa*Ù±‚`fkwargsÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`h        Ù±‚bnbesuperÙ±‚`a(Ù±‚`a)Ù±‚aoa.Ù±‚bfmh__init__Ù±‚`a(Ù±‚aoa*Ù±‚`dargsÙ±‚`a,Ù±‚`a Ù±‚aoa*Ù±‚aoa*Ù±‚`fkwargsÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`h        Ù±‚akbifÙ±‚`a Ù±‚`iwatermarkÙ±‚`a Ù±‚bowbisÙ±‚`a Ù±‚bowcnotÙ±‚`a Ù±‚bkcdNoneÙ±‚`a:Ù±‚`a
Ù±‚`l            Ù±‚`dbboxÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bnbddictÙ±‚`a(Ù±‚`hboxstyleÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1fsquareÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`blwÙ±‚aoa=Ù±‚bmia3Ù±‚`a,Ù±‚`a Ù±‚`becÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1dgrayÙ±‚bs1a'Ù±‚`a,Ù±‚`a
Ù±‚`x                        Ù±‚`bfcÙ±‚aoa=Ù±‚`a(Ù±‚bmfc0.9Ù±‚`a,Ù±‚`a Ù±‚bmfc0.9Ù±‚`a,Ù±‚`a Ù±‚bmfb.9Ù±‚`a,Ù±‚`a Ù±‚bmfb.5Ù±‚`a)Ù±‚`a,Ù±‚`a Ù±‚`ealphaÙ±‚aoa=Ù±‚bmfc0.5Ù±‚`a)Ù±‚`a
Ù±‚`l            Ù±‚bbpdselfÙ±‚aoa.Ù±‚`dtextÙ±‚`a(Ù±‚bmfc0.5Ù±‚`a,Ù±‚`a Ù±‚bmfc0.5Ù±‚`a,Ù±‚`a Ù±‚`iwatermarkÙ±‚`a,Ù±‚`a
Ù±‚`v                      Ù±‚`bhaÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1fcenterÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`bvaÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1fcenterÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`hrotationÙ±‚aoa=Ù±‚bmib30Ù±‚`a,Ù±‚`a
Ù±‚`v                      Ù±‚`hfontsizeÙ±‚aoa=Ù±‚bmib40Ù±‚`a,Ù±‚`a Ù±‚`ecolorÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1dgrayÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`ealphaÙ±‚aoa=Ù±‚bmfc0.5Ù±‚`a,Ù±‚`a Ù±‚`dbboxÙ±‚aoa=Ù±‚`dbboxÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚`axÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`hlinspaceÙ±‚`a(Ù±‚aoa-Ù±‚bmia3Ù±‚`a,Ù±‚`a Ù±‚bmia3Ù±‚`a,Ù±‚`a Ù±‚bmic201Ù±‚`a)Ù±‚`a
Ù±‚`ayÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`dtanhÙ±‚`a(Ù±‚`axÙ±‚`a)Ù±‚`a Ù±‚aoa+Ù±‚`a Ù±‚bmfc0.1Ù±‚`a Ù±‚aoa*Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`ccosÙ±‚`a(Ù±‚bmia5Ù±‚`a Ù±‚aoa*Ù±‚`a Ù±‚`axÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`cpltÙ±‚aoa.Ù±‚`ffigureÙ±‚`a(Ù±‚`kFigureClassÙ±‚aoa=Ù±‚`oWatermarkFigureÙ±‚`a,Ù±‚`a Ù±‚`iwatermarkÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1edraftÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`cpltÙ±‚aoa.Ù±‚`dplotÙ±‚`a(Ù±‚`axÙ±‚`a,Ù±‚`a Ù±‚`ayÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚bc1xM#############################################################################Ù±‚`a
Ù±‚bc1a#Ù±‚`a
Ù±‚bc1x# .. admonition:: ReferencesÙ±‚`a
Ù±‚bc1a#Ù±‚`a
Ù±‚bc1xN#    The use of the following functions, methods, classes and modules is shownÙ±‚`a
Ù±‚bc1u#    in this example:Ù±‚`a
Ù±‚bc1a#Ù±‚`a
Ù±‚bc1x!#    - `matplotlib.pyplot.figure`Ù±‚`a
Ù±‚bc1x!#    - `matplotlib.figure.Figure`Ù±‚`a
Ù±‚bc1x&#    - `matplotlib.figure.Figure.text`Ù±‚`a
`dNoneö