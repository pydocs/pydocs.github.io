Ù¯‚Ù´ƒ™Ù±‚bsdy'"""
===========================================
Changing colors of lines intersecting a box
===========================================

The lines intersecting the rectangle are colored in red, while the others
are left as blue lines. This example showcases the `.intersects_bbox` function.

"""Ù±‚`a
Ù±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„enumpyÙ „enumpyf1.22.3fmoduleenumpyfmoduleõÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnnbnpÙ±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnnfpyplotÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnncpltÙ±‚`a
Ù±‚bkndfromÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnnjtransformsÙ±‚`a Ù±‚bknfimportÙ±‚`a Ù±‚`dBboxÙ±‚`a
Ù±‚bkndfromÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnndpathÙ±‚`a Ù±‚bknfimportÙ±‚`a Ù±‚`dPathÙ±‚`a
Ù±‚`a
Ù±‚bc1x)# Fixing random state for reproducibilityÙ±‚`a
Ù±‚`bnpÙ±‚aoa.Ù±‚`frandomÙ±‚aoa.Ù±‚`dseedÙ±‚`a(Ù±‚bmih19680801Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚`dleftÙ±‚`a,Ù±‚`a Ù±‚`fbottomÙ±‚`a,Ù±‚`a Ù±‚`ewidthÙ±‚`a,Ù±‚`a Ù±‚`fheightÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`a(Ù±‚aoa-Ù±‚bmia1Ù±‚`a,Ù±‚`a Ù±‚aoa-Ù±‚bmia1Ù±‚`a,Ù±‚`a Ù±‚bmia2Ù±‚`a,Ù±‚`a Ù±‚bmia2Ù±‚`a)Ù±‚`a
Ù±‚`drectÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cpltÙ±‚aoa.Ù±‚`iRectangleÙ±‚`a(Ù±‚`a(Ù±‚`dleftÙ±‚`a,Ù±‚`a Ù±‚`fbottomÙ±‚`a)Ù±‚`a,Ù±‚`a Ù±‚`ewidthÙ±‚`a,Ù±‚`a Ù±‚`fheightÙ±‚`a,Ù±‚`a
Ù±‚`u                     Ù±‚`ifacecolorÙ±‚aoa=Ù±‚bs2a"Ù±‚bs2eblackÙ±‚bs2a"Ù±‚`a,Ù±‚`a Ù±‚`ealphaÙ±‚aoa=Ù±‚bmfc0.1Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`cfigÙ±‚`a,Ù±‚`a Ù±‚`baxÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cpltÙ±‚aoa.Ù±‚`hsubplotsÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`iadd_patchÙ±‚`a(Ù±‚`drectÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`dbboxÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`dBboxÙ±‚aoa.Ù±‚`kfrom_boundsÙ±‚`a(Ù±‚`dleftÙ±‚`a,Ù±‚`a Ù±‚`fbottomÙ±‚`a,Ù±‚`a Ù±‚`ewidthÙ±‚`a,Ù±‚`a Ù±‚`fheightÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚akcforÙ±‚`a Ù±‚`aiÙ±‚`a Ù±‚bowbinÙ±‚`a Ù±‚bnberangeÙ±‚`a(Ù±‚bmib12Ù±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`d    Ù±‚`hverticesÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`a(Ù±‚`bnpÙ±‚aoa.Ù±‚`frandomÙ±‚aoa.Ù±‚`frandomÙ±‚`a(Ù±‚`a(Ù±‚bmia2Ù±‚`a,Ù±‚`a Ù±‚bmia2Ù±‚`a)Ù±‚`a)Ù±‚`a Ù±‚aoa-Ù±‚`a Ù±‚bmfc0.5Ù±‚`a)Ù±‚`a Ù±‚aoa*Ù±‚`a Ù±‚bmfc6.0Ù±‚`a
Ù±‚`d    Ù±‚`dpathÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`dPathÙ±‚`a(Ù±‚`hverticesÙ±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚akbifÙ±‚`a Ù±‚`dpathÙ±‚aoa.Ù±‚`ointersects_bboxÙ±‚`a(Ù±‚`dbboxÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`h        Ù±‚`ecolorÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bs1a'Ù±‚bs1arÙ±‚bs1a'Ù±‚`a
Ù±‚`d    Ù±‚akdelseÙ±‚`a:Ù±‚`a
Ù±‚`h        Ù±‚`ecolorÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bs1a'Ù±‚bs1abÙ±‚bs1a'Ù±‚`a
Ù±‚`d    Ù±‚`baxÙ±‚aoa.Ù±‚`dplotÙ±‚`a(Ù±‚`hverticesÙ±‚`a[Ù±‚`a:Ù±‚`a,Ù±‚`a Ù±‚bmia0Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`hverticesÙ±‚`a[Ù±‚`a:Ù±‚`a,Ù±‚`a Ù±‚bmia1Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`ecolorÙ±‚aoa=Ù±‚`ecolorÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`cpltÙ±‚aoa.Ù±‚`dshowÙ±‚`a(Ù±‚`a)Ù±‚`a
`dNoneö