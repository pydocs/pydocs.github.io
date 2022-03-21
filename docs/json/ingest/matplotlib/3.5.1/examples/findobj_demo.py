Ù¯‚Ù´ƒ™FÙ±‚bsdxe"""
============
Findobj Demo
============

Recursively find all objects that match some criteria
"""Ù±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„enumpyÙ „enumpyf1.22.3fmoduleenumpyfmoduleõÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnnbnpÙ±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnnfpyplotÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnncpltÙ±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnndtextÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnndtextÙ±‚`a
Ù±‚`a
Ù±‚`aaÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`farangeÙ±‚`a(Ù±‚bmia0Ù±‚`a,Ù±‚`a Ù±‚bmia3Ù±‚`a,Ù±‚`a Ù±‚bmfc.02Ù±‚`a)Ù±‚`a
Ù±‚`abÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`farangeÙ±‚`a(Ù±‚bmia0Ù±‚`a,Ù±‚`a Ù±‚bmia3Ù±‚`a,Ù±‚`a Ù±‚bmfc.02Ù±‚`a)Ù±‚`a
Ù±‚`acÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`cexpÙ±‚`a(Ù±‚`aaÙ±‚`a)Ù±‚`a
Ù±‚`adÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`acÙ±‚`a[Ù±‚`a:Ù±‚`a:Ù±‚aoa-Ù±‚bmia1Ù±‚`a]Ù±‚`a
Ù±‚`a
Ù±‚`cfigÙ±‚`a,Ù±‚`a Ù±‚`baxÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cpltÙ±‚aoa.Ù±‚`hsubplotsÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`cpltÙ±‚aoa.Ù±‚`dplotÙ±‚`a(Ù±‚`aaÙ±‚`a,Ù±‚`a Ù±‚`acÙ±‚`a,Ù±‚`a Ù±‚bs1a'Ù±‚bs1ck--Ù±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`aaÙ±‚`a,Ù±‚`a Ù±‚`adÙ±‚`a,Ù±‚`a Ù±‚bs1a'Ù±‚bs1bk:Ù±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`aaÙ±‚`a,Ù±‚`a Ù±‚`acÙ±‚`a Ù±‚aoa+Ù±‚`a Ù±‚`adÙ±‚`a,Ù±‚`a Ù±‚bs1a'Ù±‚bs1akÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`cpltÙ±‚aoa.Ù±‚`flegendÙ±‚`a(Ù±‚`a(Ù±‚bs1a'Ù±‚bs1lModel lengthÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚bs1a'Ù±‚bs1kData lengthÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚bs1a'Ù±‚bs1tTotal message lengthÙ±‚bs1a'Ù±‚`a)Ù±‚`a,Ù±‚`a
Ù±‚`k           Ù±‚`clocÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1lupper centerÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`fshadowÙ±‚aoa=Ù±‚bkcdTrueÙ±‚`a)Ù±‚`a
Ù±‚`cpltÙ±‚aoa.Ù±‚`dylimÙ±‚`a(Ù±‚`a[Ù±‚aoa-Ù±‚bmia1Ù±‚`a,Ù±‚`a Ù±‚bmib20Ù±‚`a]Ù±‚`a)Ù±‚`a
Ù±‚`cpltÙ±‚aoa.Ù±‚`dgridÙ±‚`a(Ù±‚bkceFalseÙ±‚`a)Ù±‚`a
Ù±‚`cpltÙ±‚aoa.Ù±‚`fxlabelÙ±‚`a(Ù±‚bs1a'Ù±‚bs1uModel complexity --->Ù±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`cpltÙ±‚aoa.Ù±‚`fylabelÙ±‚`a(Ù±‚bs1a'Ù±‚bs1sMessage length --->Ù±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`cpltÙ±‚aoa.Ù±‚`etitleÙ±‚`a(Ù±‚bs1a'Ù±‚bs1vMinimum Message LengthÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚bc1x# match on arbitrary functionÙ±‚`a
Ù±‚akcdefÙ±‚`a Ù±‚bnffmyfuncÙ±‚`a(Ù±‚`axÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`d    Ù±‚akfreturnÙ±‚`a Ù±‚bnbghasattrÙ±‚`a(Ù±‚`axÙ±‚`a,Ù±‚`a Ù±‚bs1a'Ù±‚bs1iset_colorÙ±‚bs1a'Ù±‚`a)Ù±‚`a Ù±‚bowcandÙ±‚`a Ù±‚bowcnotÙ±‚`a Ù±‚bnbghasattrÙ±‚`a(Ù±‚`axÙ±‚`a,Ù±‚`a Ù±‚bs1a'Ù±‚bs1mset_facecolorÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚akcforÙ±‚`a Ù±‚`aoÙ±‚`a Ù±‚bowbinÙ±‚`a Ù±‚`cfigÙ±‚aoa.Ù±‚`gfindobjÙ±‚`a(Ù±‚`fmyfuncÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`d    Ù±‚`aoÙ±‚aoa.Ù±‚`iset_colorÙ±‚`a(Ù±‚bs1a'Ù±‚bs1dblueÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚bc1x# match on class instancesÙ±‚`a
Ù±‚akcforÙ±‚`a Ù±‚`aoÙ±‚`a Ù±‚bowbinÙ±‚`a Ù±‚`cfigÙ±‚aoa.Ù±‚`gfindobjÙ±‚`a(Ù±‚`dtextÙ±‚aoa.Ù±‚`dTextÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`d    Ù±‚`aoÙ±‚aoa.Ù±‚`mset_fontstyleÙ±‚`a(Ù±‚bs1a'Ù±‚bs1fitalicÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚`cpltÙ±‚aoa.Ù±‚`dshowÙ±‚`a(Ù±‚`a)Ù±‚`a
`dNoneö