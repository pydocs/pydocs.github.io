ŸØÇÅŸ¥ÉôŸ±Çbsdx˚"""
================
Annotation Polar
================

This example shows how to create an annotation on a polar graph.

For a complete overview of the annotation capabilities, also see the
:doc:`annotation tutorial</tutorials/text/annotations>`.
"""Ÿ±Ç`a
Ÿ±ÇbknfimportŸ±Ç`a Ÿ±ÇbnnŸ¢ÑenumpyŸ†Ñenumpyf1.22.3fmoduleenumpyfmoduleıŸ±Ç`a Ÿ±ÇakbasŸ±Ç`a Ÿ±ÇbnnbnpŸ±Ç`a
Ÿ±ÇbknfimportŸ±Ç`a Ÿ±ÇbnnŸ¢ÑjmatplotlibŸ†Ñjmatplotlibe3.5.1fmodulejmatplotlibfmoduleıŸ±Çbnna.Ÿ±ÇbnnfpyplotŸ±Ç`a Ÿ±ÇakbasŸ±Ç`a Ÿ±ÇbnncpltŸ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`cfigŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`ffigureŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`baxŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cfigŸ±Çaoa.Ÿ±Ç`kadd_subplotŸ±Ç`a(Ÿ±Ç`jprojectionŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1epolarŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`arŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`farangeŸ±Ç`a(Ÿ±Çbmia0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfe0.001Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`ethetaŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Çbmia2Ÿ±Ç`a Ÿ±Çaoa*Ÿ±Ç`a Ÿ±Çbmia2Ÿ±Çaoa*Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`bpiŸ±Ç`a Ÿ±Çaoa*Ÿ±Ç`a Ÿ±Ç`arŸ±Ç`a
Ÿ±Ç`dlineŸ±Ç`a,Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`dplotŸ±Ç`a(Ÿ±Ç`ethetaŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`arŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ecolorŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1g#ee8d18Ÿ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`blwŸ±Çaoa=Ÿ±Çbmia3Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`cindŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Çbmic800Ÿ±Ç`a
Ÿ±Ç`ethisrŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ithisthetaŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`arŸ±Ç`a[Ÿ±Ç`cindŸ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ethetaŸ±Ç`a[Ÿ±Ç`cindŸ±Ç`a]Ÿ±Ç`a
Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`dplotŸ±Ç`a(Ÿ±Ç`a[Ÿ±Ç`ithisthetaŸ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`a[Ÿ±Ç`ethisrŸ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1aoŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`hannotateŸ±Ç`a(Ÿ±Çbs1a'Ÿ±Çbs1ra polar annotationŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`l            Ÿ±Ç`bxyŸ±Çaoa=Ÿ±Ç`a(Ÿ±Ç`ithisthetaŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ethisrŸ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`b  Ÿ±Çbc1o# theta, radiusŸ±Ç`a
Ÿ±Ç`l            Ÿ±Ç`fxytextŸ±Çaoa=Ÿ±Ç`a(Ÿ±Çbmfd0.05Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd0.05Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`d    Ÿ±Çbc1t# fraction, fractionŸ±Ç`a
Ÿ±Ç`l            Ÿ±Ç`jtextcoordsŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1ofigure fractionŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`l            Ÿ±Ç`jarrowpropsŸ±Çaoa=Ÿ±ÇbnbddictŸ±Ç`a(Ÿ±Ç`ifacecolorŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1eblackŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`fshrinkŸ±Çaoa=Ÿ±Çbmfd0.05Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`l            Ÿ±Ç`shorizontalalignmentŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1dleftŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`l            Ÿ±Ç`qverticalalignmentŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1fbottomŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`l            Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`dshowŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1xM#############################################################################Ÿ±Ç`a
Ÿ±Çbc1a#Ÿ±Ç`a
Ÿ±Çbc1x# .. admonition:: ReferencesŸ±Ç`a
Ÿ±Çbc1a#Ÿ±Ç`a
Ÿ±Çbc1xN#    The use of the following functions, methods, classes and modules is shownŸ±Ç`a
Ÿ±Çbc1u#    in this example:Ÿ±Ç`a
Ÿ±Çbc1a#Ÿ±Ç`a
Ÿ±Çbc1x%#    - `matplotlib.projections.polar`Ÿ±Ç`a
Ÿ±Çbc1xE#    - `matplotlib.axes.Axes.annotate` / `matplotlib.pyplot.annotate`Ÿ±Ç`a
`dNoneˆ