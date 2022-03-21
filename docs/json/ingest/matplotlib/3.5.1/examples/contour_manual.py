Ù¯‚Ù´ƒ™~Ù±‚bsdx"""
==============
Manual Contour
==============

Example of displaying your own contour lines and polygons using ContourSet.
"""Ù±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnnfpyplotÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnncpltÙ±‚`a
Ù±‚bkndfromÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnngcontourÙ±‚`a Ù±‚bknfimportÙ±‚`a Ù±‚`jContourSetÙ±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnnbcmÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnnbcmÙ±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚bc1xO###############################################################################Ù±‚`a
Ù±‚bc1x<# Contour lines for each level are a list/tuple of polygons.Ù±‚`a
Ù±‚`flines0Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`a[Ù±‚`a[Ù±‚`a[Ù±‚bmia0Ù±‚`a,Ù±‚`a Ù±‚bmia0Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`a[Ù±‚bmia0Ù±‚`a,Ù±‚`a Ù±‚bmia4Ù±‚`a]Ù±‚`a]Ù±‚`a]Ù±‚`a
Ù±‚`flines1Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`a[Ù±‚`a[Ù±‚`a[Ù±‚bmia2Ù±‚`a,Ù±‚`a Ù±‚bmia0Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`a[Ù±‚bmia1Ù±‚`a,Ù±‚`a Ù±‚bmia2Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`a[Ù±‚bmia1Ù±‚`a,Ù±‚`a Ù±‚bmia3Ù±‚`a]Ù±‚`a]Ù±‚`a]Ù±‚`a
Ù±‚`flines2Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`a[Ù±‚`a[Ù±‚`a[Ù±‚bmia3Ù±‚`a,Ù±‚`a Ù±‚bmia0Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`a[Ù±‚bmia3Ù±‚`a,Ù±‚`a Ù±‚bmia2Ù±‚`a]Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`a[Ù±‚`a[Ù±‚bmia3Ù±‚`a,Ù±‚`a Ù±‚bmia3Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`a[Ù±‚bmia3Ù±‚`a,Ù±‚`a Ù±‚bmia4Ù±‚`a]Ù±‚`a]Ù±‚`a]Ù±‚`b  Ù±‚bc1q# Note two lines.Ù±‚`a
Ù±‚`a
Ù±‚bc1xO###############################################################################Ù±‚`a
Ù±‚bc1xG# Filled contours between two levels are also a list/tuple of polygons.Ù±‚`a
Ù±‚bc1x3# Points can be ordered clockwise or anticlockwise.Ù±‚`a
Ù±‚`hfilled01Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`a[Ù±‚`a[Ù±‚`a[Ù±‚bmia0Ù±‚`a,Ù±‚`a Ù±‚bmia0Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`a[Ù±‚bmia0Ù±‚`a,Ù±‚`a Ù±‚bmia4Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`a[Ù±‚bmia1Ù±‚`a,Ù±‚`a Ù±‚bmia3Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`a[Ù±‚bmia1Ù±‚`a,Ù±‚`a Ù±‚bmia2Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`a[Ù±‚bmia2Ù±‚`a,Ù±‚`a Ù±‚bmia0Ù±‚`a]Ù±‚`a]Ù±‚`a]Ù±‚`a
Ù±‚`hfilled12Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`a[Ù±‚`a[Ù±‚`a[Ù±‚bmia2Ù±‚`a,Ù±‚`a Ù±‚bmia0Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`a[Ù±‚bmia3Ù±‚`a,Ù±‚`a Ù±‚bmia0Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`a[Ù±‚bmia3Ù±‚`a,Ù±‚`a Ù±‚bmia2Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`a[Ù±‚bmia1Ù±‚`a,Ù±‚`a Ù±‚bmia3Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`a[Ù±‚bmia1Ù±‚`a,Ù±‚`a Ù±‚bmia2Ù±‚`a]Ù±‚`a]Ù±‚`a,Ù±‚`c   Ù±‚bc1t# Note two polygons.Ù±‚`a
Ù±‚`l            Ù±‚`a[Ù±‚`a[Ù±‚bmia1Ù±‚`a,Ù±‚`a Ù±‚bmia4Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`a[Ù±‚bmia3Ù±‚`a,Ù±‚`a Ù±‚bmia4Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`a[Ù±‚bmia3Ù±‚`a,Ù±‚`a Ù±‚bmia3Ù±‚`a]Ù±‚`a]Ù±‚`a]Ù±‚`a
Ù±‚`a
Ù±‚bc1xO###############################################################################Ù±‚`a
Ù±‚`a
Ù±‚`cfigÙ±‚`a,Ù±‚`a Ù±‚`baxÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cpltÙ±‚aoa.Ù±‚`hsubplotsÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚bc1x$# Filled contours using filled=True.Ù±‚`a
Ù±‚`bcsÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`jContourSetÙ±‚`a(Ù±‚`baxÙ±‚`a,Ù±‚`a Ù±‚`a[Ù±‚bmia0Ù±‚`a,Ù±‚`a Ù±‚bmia1Ù±‚`a,Ù±‚`a Ù±‚bmia2Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`a[Ù±‚`hfilled01Ù±‚`a,Ù±‚`a Ù±‚`hfilled12Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`ffilledÙ±‚aoa=Ù±‚bkcdTrueÙ±‚`a,Ù±‚`a Ù±‚`dcmapÙ±‚aoa=Ù±‚`bcmÙ±‚aoa.Ù±‚`dboneÙ±‚`a)Ù±‚`a
Ù±‚`dcbarÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cfigÙ±‚aoa.Ù±‚`hcolorbarÙ±‚`a(Ù±‚`bcsÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚bc1x# Contour lines (non-filled).Ù±‚`a
Ù±‚`elinesÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`jContourSetÙ±‚`a(Ù±‚`a
Ù±‚`d    Ù±‚`baxÙ±‚`a,Ù±‚`a Ù±‚`a[Ù±‚bmia0Ù±‚`a,Ù±‚`a Ù±‚bmia1Ù±‚`a,Ù±‚`a Ù±‚bmia2Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`a[Ù±‚`flines0Ù±‚`a,Ù±‚`a Ù±‚`flines1Ù±‚`a,Ù±‚`a Ù±‚`flines2Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`dcmapÙ±‚aoa=Ù±‚`bcmÙ±‚aoa.Ù±‚`dcoolÙ±‚`a,Ù±‚`a Ù±‚`jlinewidthsÙ±‚aoa=Ù±‚bmia3Ù±‚`a)Ù±‚`a
Ù±‚`dcbarÙ±‚aoa.Ù±‚`iadd_linesÙ±‚`a(Ù±‚`elinesÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`csetÙ±‚`a(Ù±‚`dxlimÙ±‚aoa=Ù±‚`a(Ù±‚aoa-Ù±‚bmfc0.5Ù±‚`a,Ù±‚`a Ù±‚bmfc3.5Ù±‚`a)Ù±‚`a,Ù±‚`a Ù±‚`dylimÙ±‚aoa=Ù±‚`a(Ù±‚aoa-Ù±‚bmfc0.5Ù±‚`a,Ù±‚`a Ù±‚bmfc4.5Ù±‚`a)Ù±‚`a,Ù±‚`a
Ù±‚`g       Ù±‚`etitleÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1wUser-specified contoursÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚bc1xO###############################################################################Ù±‚`a
Ù±‚bc1xL# Multiple filled contour lines can be specified in a single list of polygonÙ±‚`a
Ù±‚bc1xM# vertices along with a list of vertex kinds (code types) as described in theÙ±‚`a
Ù±‚bc1xC# Path class.  This is particularly useful for polygons with holes.Ù±‚`a
Ù±‚bc1x7# Here a code type of 1 is a MOVETO, and 2 is a LINETO.Ù±‚`a
Ù±‚`a
Ù±‚`cfigÙ±‚`a,Ù±‚`a Ù±‚`baxÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cpltÙ±‚aoa.Ù±‚`hsubplotsÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`hfilled01Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`a[Ù±‚`a[Ù±‚`a[Ù±‚bmia0Ù±‚`a,Ù±‚`a Ù±‚bmia0Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`a[Ù±‚bmia3Ù±‚`a,Ù±‚`a Ù±‚bmia0Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`a[Ù±‚bmia3Ù±‚`a,Ù±‚`a Ù±‚bmia3Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`a[Ù±‚bmia0Ù±‚`a,Ù±‚`a Ù±‚bmia3Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`a[Ù±‚bmia1Ù±‚`a,Ù±‚`a Ù±‚bmia1Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`a[Ù±‚bmia1Ù±‚`a,Ù±‚`a Ù±‚bmia2Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`a[Ù±‚bmia2Ù±‚`a,Ù±‚`a Ù±‚bmia2Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`a[Ù±‚bmia2Ù±‚`a,Ù±‚`a Ù±‚bmia1Ù±‚`a]Ù±‚`a]Ù±‚`a]Ù±‚`a
Ù±‚`gkinds01Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`a[Ù±‚`a[Ù±‚bmia1Ù±‚`a,Ù±‚`a Ù±‚bmia2Ù±‚`a,Ù±‚`a Ù±‚bmia2Ù±‚`a,Ù±‚`a Ù±‚bmia2Ù±‚`a,Ù±‚`a Ù±‚bmia1Ù±‚`a,Ù±‚`a Ù±‚bmia2Ù±‚`a,Ù±‚`a Ù±‚bmia2Ù±‚`a,Ù±‚`a Ù±‚bmia2Ù±‚`a]Ù±‚`a]Ù±‚`a
Ù±‚`bcsÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`jContourSetÙ±‚`a(Ù±‚`baxÙ±‚`a,Ù±‚`a Ù±‚`a[Ù±‚bmia0Ù±‚`a,Ù±‚`a Ù±‚bmia1Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`a[Ù±‚`hfilled01Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`a[Ù±‚`gkinds01Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`ffilledÙ±‚aoa=Ù±‚bkcdTrueÙ±‚`a)Ù±‚`a
Ù±‚`dcbarÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cfigÙ±‚aoa.Ù±‚`hcolorbarÙ±‚`a(Ù±‚`bcsÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`csetÙ±‚`a(Ù±‚`dxlimÙ±‚aoa=Ù±‚`a(Ù±‚aoa-Ù±‚bmfc0.5Ù±‚`a,Ù±‚`a Ù±‚bmfc3.5Ù±‚`a)Ù±‚`a,Ù±‚`a Ù±‚`dylimÙ±‚aoa=Ù±‚`a(Ù±‚aoa-Ù±‚bmfc0.5Ù±‚`a,Ù±‚`a Ù±‚bmfc3.5Ù±‚`a)Ù±‚`a,Ù±‚`a
Ù±‚`g       Ù±‚`etitleÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1x)User specified filled contours with holesÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`cpltÙ±‚aoa.Ù±‚`dshowÙ±‚`a(Ù±‚`a)Ù±‚`a
`dNoneö