Ù¯‚Ù´ƒ˜óÙ±‚bsdx»"""
===========================
Mouse move and click events
===========================

An example of how to interact with the plotting canvas by connecting to move
and click events.
"""Ù±‚`a
Ù±‚`a
Ù±‚bkndfromÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnnmbackend_basesÙ±‚`a Ù±‚bknfimportÙ±‚`a Ù±‚`kMouseButtonÙ±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnnfpyplotÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnncpltÙ±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„enumpyÙ „enumpyf1.22.3fmoduleenumpyfmoduleõÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnnbnpÙ±‚`a
Ù±‚`a
Ù±‚`atÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`farangeÙ±‚`a(Ù±‚bmfc0.0Ù±‚`a,Ù±‚`a Ù±‚bmfc1.0Ù±‚`a,Ù±‚`a Ù±‚bmfd0.01Ù±‚`a)Ù±‚`a
Ù±‚`asÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`csinÙ±‚`a(Ù±‚bmia2Ù±‚`a Ù±‚aoa*Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`bpiÙ±‚`a Ù±‚aoa*Ù±‚`a Ù±‚`atÙ±‚`a)Ù±‚`a
Ù±‚`cfigÙ±‚`a,Ù±‚`a Ù±‚`baxÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cpltÙ±‚aoa.Ù±‚`hsubplotsÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`dplotÙ±‚`a(Ù±‚`atÙ±‚`a,Ù±‚`a Ù±‚`asÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚akcdefÙ±‚`a Ù±‚bnfgon_moveÙ±‚`a(Ù±‚`eeventÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`d    Ù±‚bc1x# get the x and y pixel coordsÙ±‚`a
Ù±‚`d    Ù±‚`axÙ±‚`a,Ù±‚`a Ù±‚`ayÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`eeventÙ±‚aoa.Ù±‚`axÙ±‚`a,Ù±‚`a Ù±‚`eeventÙ±‚aoa.Ù±‚`ayÙ±‚`a
Ù±‚`d    Ù±‚akbifÙ±‚`a Ù±‚`eeventÙ±‚aoa.Ù±‚`finaxesÙ±‚`a:Ù±‚`a
Ù±‚`h        Ù±‚`baxÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`eeventÙ±‚aoa.Ù±‚`finaxesÙ±‚`b  Ù±‚bc1s# the axes instanceÙ±‚`a
Ù±‚`h        Ù±‚bnbeprintÙ±‚`a(Ù±‚bs1a'Ù±‚bs1ldata coords Ù±‚bsib%fÙ±‚bs1a Ù±‚bsib%fÙ±‚bs1a'Ù±‚`a Ù±‚aoa%Ù±‚`a Ù±‚`a(Ù±‚`eeventÙ±‚aoa.Ù±‚`exdataÙ±‚`a,Ù±‚`a Ù±‚`eeventÙ±‚aoa.Ù±‚`eydataÙ±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚akcdefÙ±‚`a Ù±‚bnfhon_clickÙ±‚`a(Ù±‚`eeventÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`d    Ù±‚akbifÙ±‚`a Ù±‚`eeventÙ±‚aoa.Ù±‚`fbuttonÙ±‚`a Ù±‚bowbisÙ±‚`a Ù±‚`kMouseButtonÙ±‚aoa.Ù±‚`dLEFTÙ±‚`a:Ù±‚`a
Ù±‚`h        Ù±‚bnbeprintÙ±‚`a(Ù±‚bs1a'Ù±‚bs1vdisconnecting callbackÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚`cpltÙ±‚aoa.Ù±‚`jdisconnectÙ±‚`a(Ù±‚`jbinding_idÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚`jbinding_idÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cpltÙ±‚aoa.Ù±‚`gconnectÙ±‚`a(Ù±‚bs1a'Ù±‚bs1smotion_notify_eventÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`gon_moveÙ±‚`a)Ù±‚`a
Ù±‚`cpltÙ±‚aoa.Ù±‚`gconnectÙ±‚`a(Ù±‚bs1a'Ù±‚bs1rbutton_press_eventÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`hon_clickÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`cpltÙ±‚aoa.Ù±‚`dshowÙ±‚`a(Ù±‚`a)Ù±‚`a
`dNoneö