Ù¯‚Ù´ƒ˜ùÙ±‚bsdyÏ"""
Placing text boxes
==================

When decorating axes with text boxes, two useful tricks are to place the text
in axes coordinates (see :doc:`/tutorials/advanced/transforms_tutorial`),
so the text doesn't move around with changes in x or y limits.  You
can also use the ``bbox`` property of text to surround the text with a
`~matplotlib.patches.Patch` instance -- the ``bbox`` keyword argument takes a
dictionary with keys that are Patch properties.
"""Ù±‚`a
Ù±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„enumpyÙ „enumpyf1.22.3fmoduleenumpyfmoduleõÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnnbnpÙ±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnnfpyplotÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnncpltÙ±‚`a
Ù±‚`a
Ù±‚`bnpÙ±‚aoa.Ù±‚`frandomÙ±‚aoa.Ù±‚`dseedÙ±‚`a(Ù±‚bmih19680801Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`cfigÙ±‚`a,Ù±‚`a Ù±‚`baxÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cpltÙ±‚aoa.Ù±‚`hsubplotsÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`axÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bmib30Ù±‚aoa*Ù±‚`bnpÙ±‚aoa.Ù±‚`frandomÙ±‚aoa.Ù±‚`erandnÙ±‚`a(Ù±‚bmie10000Ù±‚`a)Ù±‚`a
Ù±‚`bmuÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`axÙ±‚aoa.Ù±‚`dmeanÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`fmedianÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`fmedianÙ±‚`a(Ù±‚`axÙ±‚`a)Ù±‚`a
Ù±‚`esigmaÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`axÙ±‚aoa.Ù±‚`cstdÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`gtextstrÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bs1a'Ù±‚bseb\nÙ±‚bs1a'Ù±‚aoa.Ù±‚`djoinÙ±‚`a(Ù±‚`a(Ù±‚`a
Ù±‚`d    Ù±‚bsaarÙ±‚bs1a'Ù±‚bs1a$Ù±‚bs1a\Ù±‚bs1cmu=Ù±‚bsid%.2fÙ±‚bs1a$Ù±‚bs1a'Ù±‚`a Ù±‚aoa%Ù±‚`a Ù±‚`a(Ù±‚`bmuÙ±‚`a,Ù±‚`a Ù±‚`a)Ù±‚`a,Ù±‚`a
Ù±‚`d    Ù±‚bsaarÙ±‚bs1a'Ù±‚bs1a$Ù±‚bs1a\Ù±‚bs1fmathrmÙ±‚bsih{median}Ù±‚bs1a=Ù±‚bsid%.2fÙ±‚bs1a$Ù±‚bs1a'Ù±‚`a Ù±‚aoa%Ù±‚`a Ù±‚`a(Ù±‚`fmedianÙ±‚`a,Ù±‚`a Ù±‚`a)Ù±‚`a,Ù±‚`a
Ù±‚`d    Ù±‚bsaarÙ±‚bs1a'Ù±‚bs1a$Ù±‚bs1a\Ù±‚bs1fsigma=Ù±‚bsid%.2fÙ±‚bs1a$Ù±‚bs1a'Ù±‚`a Ù±‚aoa%Ù±‚`a Ù±‚`a(Ù±‚`esigmaÙ±‚`a,Ù±‚`a Ù±‚`a)Ù±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`dhistÙ±‚`a(Ù±‚`axÙ±‚`a,Ù±‚`a Ù±‚bmib50Ù±‚`a)Ù±‚`a
Ù±‚bc1x-# these are matplotlib.patch.Patch propertiesÙ±‚`a
Ù±‚`epropsÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bnbddictÙ±‚`a(Ù±‚`hboxstyleÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1eroundÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`ifacecolorÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1ewheatÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`ealphaÙ±‚aoa=Ù±‚bmfc0.5Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚bc1x/# place a text box in upper left in axes coordsÙ±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`dtextÙ±‚`a(Ù±‚bmfd0.05Ù±‚`a,Ù±‚`a Ù±‚bmfd0.95Ù±‚`a,Ù±‚`a Ù±‚`gtextstrÙ±‚`a,Ù±‚`a Ù±‚`itransformÙ±‚aoa=Ù±‚`baxÙ±‚aoa.Ù±‚`itransAxesÙ±‚`a,Ù±‚`a Ù±‚`hfontsizeÙ±‚aoa=Ù±‚bmib14Ù±‚`a,Ù±‚`a
Ù±‚`h        Ù±‚`qverticalalignmentÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1ctopÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`dbboxÙ±‚aoa=Ù±‚`epropsÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`cpltÙ±‚aoa.Ù±‚`dshowÙ±‚`a(Ù±‚`a)Ù±‚`a
`dNoneö