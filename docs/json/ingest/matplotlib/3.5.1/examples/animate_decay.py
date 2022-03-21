Ù¯‚Ù´ƒ™kÙ±‚bsdxŠ"""
=====
Decay
=====

This example showcases:

- using a generator to drive an animation,
- changing axes limits during an animation.
"""Ù±‚`a
Ù±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnniitertoolsÙ±‚`a
Ù±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„enumpyÙ „enumpyf1.22.3fmoduleenumpyfmoduleõÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnnbnpÙ±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnnfpyplotÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnncpltÙ±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnnianimationÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnnianimationÙ±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚akcdefÙ±‚`a Ù±‚bnfhdata_genÙ±‚`a(Ù±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`d    Ù±‚akcforÙ±‚`a Ù±‚`ccntÙ±‚`a Ù±‚bowbinÙ±‚`a Ù±‚`iitertoolsÙ±‚aoa.Ù±‚`ecountÙ±‚`a(Ù±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`h        Ù±‚`atÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`ccntÙ±‚`a Ù±‚aoa/Ù±‚`a Ù±‚bmib10Ù±‚`a
Ù±‚`h        Ù±‚akeyieldÙ±‚`a Ù±‚`atÙ±‚`a,Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`csinÙ±‚`a(Ù±‚bmia2Ù±‚aoa*Ù±‚`bnpÙ±‚aoa.Ù±‚`bpiÙ±‚aoa*Ù±‚`atÙ±‚`a)Ù±‚`a Ù±‚aoa*Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`cexpÙ±‚`a(Ù±‚aoa-Ù±‚`atÙ±‚aoa/Ù±‚bmfc10.Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚akcdefÙ±‚`a Ù±‚bnfdinitÙ±‚`a(Ù±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`d    Ù±‚`baxÙ±‚aoa.Ù±‚`hset_ylimÙ±‚`a(Ù±‚aoa-Ù±‚bmfc1.1Ù±‚`a,Ù±‚`a Ù±‚bmfc1.1Ù±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`baxÙ±‚aoa.Ù±‚`hset_xlimÙ±‚`a(Ù±‚bmia0Ù±‚`a,Ù±‚`a Ù±‚bmib10Ù±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚akcdelÙ±‚`a Ù±‚`exdataÙ±‚`a[Ù±‚`a:Ù±‚`a]Ù±‚`a
Ù±‚`d    Ù±‚akcdelÙ±‚`a Ù±‚`eydataÙ±‚`a[Ù±‚`a:Ù±‚`a]Ù±‚`a
Ù±‚`d    Ù±‚`dlineÙ±‚aoa.Ù±‚`hset_dataÙ±‚`a(Ù±‚`exdataÙ±‚`a,Ù±‚`a Ù±‚`eydataÙ±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚akfreturnÙ±‚`a Ù±‚`dlineÙ±‚`a,Ù±‚`a
Ù±‚`a
Ù±‚`cfigÙ±‚`a,Ù±‚`a Ù±‚`baxÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cpltÙ±‚aoa.Ù±‚`hsubplotsÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`dlineÙ±‚`a,Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`baxÙ±‚aoa.Ù±‚`dplotÙ±‚`a(Ù±‚`a[Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`a[Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`blwÙ±‚aoa=Ù±‚bmia2Ù±‚`a)Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`dgridÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`exdataÙ±‚`a,Ù±‚`a Ù±‚`eydataÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`a[Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`a[Ù±‚`a]Ù±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚akcdefÙ±‚`a Ù±‚bnfcrunÙ±‚`a(Ù±‚`ddataÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`d    Ù±‚bc1q# update the dataÙ±‚`a
Ù±‚`d    Ù±‚`atÙ±‚`a,Ù±‚`a Ù±‚`ayÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`ddataÙ±‚`a
Ù±‚`d    Ù±‚`exdataÙ±‚aoa.Ù±‚`fappendÙ±‚`a(Ù±‚`atÙ±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`eydataÙ±‚aoa.Ù±‚`fappendÙ±‚`a(Ù±‚`ayÙ±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`dxminÙ±‚`a,Ù±‚`a Ù±‚`dxmaxÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`baxÙ±‚aoa.Ù±‚`hget_xlimÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚akbifÙ±‚`a Ù±‚`atÙ±‚`a Ù±‚aoa>Ù±‚aoa=Ù±‚`a Ù±‚`dxmaxÙ±‚`a:Ù±‚`a
Ù±‚`h        Ù±‚`baxÙ±‚aoa.Ù±‚`hset_xlimÙ±‚`a(Ù±‚`dxminÙ±‚`a,Ù±‚`a Ù±‚bmia2Ù±‚aoa*Ù±‚`dxmaxÙ±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚`baxÙ±‚aoa.Ù±‚`ffigureÙ±‚aoa.Ù±‚`fcanvasÙ±‚aoa.Ù±‚`ddrawÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`dlineÙ±‚aoa.Ù±‚`hset_dataÙ±‚`a(Ù±‚`exdataÙ±‚`a,Ù±‚`a Ù±‚`eydataÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚akfreturnÙ±‚`a Ù±‚`dlineÙ±‚`a,Ù±‚`a
Ù±‚`a
Ù±‚`caniÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`ianimationÙ±‚aoa.Ù±‚`mFuncAnimationÙ±‚`a(Ù±‚`cfigÙ±‚`a,Ù±‚`a Ù±‚`crunÙ±‚`a,Ù±‚`a Ù±‚`hdata_genÙ±‚`a,Ù±‚`a Ù±‚`hintervalÙ±‚aoa=Ù±‚bmib10Ù±‚`a,Ù±‚`a Ù±‚`iinit_funcÙ±‚aoa=Ù±‚`dinitÙ±‚`a)Ù±‚`a
Ù±‚`cpltÙ±‚aoa.Ù±‚`dshowÙ±‚`a(Ù±‚`a)Ù±‚`a
`dNoneö