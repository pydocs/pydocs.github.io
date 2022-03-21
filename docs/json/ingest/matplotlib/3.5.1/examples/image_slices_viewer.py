Ù¯‚Ù´ƒ™‘Ù±‚bsdxr"""
===================
Image Slices Viewer
===================

Scroll through 2D image slices of a 3D array.
"""Ù±‚`a
Ù±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„enumpyÙ „enumpyf1.22.3fmoduleenumpyfmoduleõÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnnbnpÙ±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnnfpyplotÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnncpltÙ±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚bc1x)# Fixing random state for reproducibilityÙ±‚`a
Ù±‚`bnpÙ±‚aoa.Ù±‚`frandomÙ±‚aoa.Ù±‚`dseedÙ±‚`a(Ù±‚bmih19680801Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚akeclassÙ±‚`a Ù±‚bnclIndexTrackerÙ±‚`a:Ù±‚`a
Ù±‚`d    Ù±‚akcdefÙ±‚`a Ù±‚bfmh__init__Ù±‚`a(Ù±‚bbpdselfÙ±‚`a,Ù±‚`a Ù±‚`baxÙ±‚`a,Ù±‚`a Ù±‚`aXÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`baxÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`baxÙ±‚`a
Ù±‚`h        Ù±‚`baxÙ±‚aoa.Ù±‚`iset_titleÙ±‚`a(Ù±‚bs1a'Ù±‚bs1x#use scroll wheel to navigate imagesÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`aXÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`aXÙ±‚`a
Ù±‚`h        Ù±‚`drowsÙ±‚`a,Ù±‚`a Ù±‚`dcolsÙ±‚`a,Ù±‚`a Ù±‚bbpdselfÙ±‚aoa.Ù±‚`fslicesÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`aXÙ±‚aoa.Ù±‚`eshapeÙ±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`cindÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bbpdselfÙ±‚aoa.Ù±‚`fslicesÙ±‚aoa/Ù±‚aoa/Ù±‚bmia2Ù±‚`a
Ù±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`bimÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`baxÙ±‚aoa.Ù±‚`fimshowÙ±‚`a(Ù±‚bbpdselfÙ±‚aoa.Ù±‚`aXÙ±‚`a[Ù±‚`a:Ù±‚`a,Ù±‚`a Ù±‚`a:Ù±‚`a,Ù±‚`a Ù±‚bbpdselfÙ±‚aoa.Ù±‚`cindÙ±‚`a]Ù±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`fupdateÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚akcdefÙ±‚`a Ù±‚bnfion_scrollÙ±‚`a(Ù±‚bbpdselfÙ±‚`a,Ù±‚`a Ù±‚`eeventÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`h        Ù±‚bnbeprintÙ±‚`a(Ù±‚bs2a"Ù±‚bsib%sÙ±‚bs2a Ù±‚bsib%sÙ±‚bs2a"Ù±‚`a Ù±‚aoa%Ù±‚`a Ù±‚`a(Ù±‚`eeventÙ±‚aoa.Ù±‚`fbuttonÙ±‚`a,Ù±‚`a Ù±‚`eeventÙ±‚aoa.Ù±‚`dstepÙ±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚akbifÙ±‚`a Ù±‚`eeventÙ±‚aoa.Ù±‚`fbuttonÙ±‚`a Ù±‚aob==Ù±‚`a Ù±‚bs1a'Ù±‚bs1bupÙ±‚bs1a'Ù±‚`a:Ù±‚`a
Ù±‚`l            Ù±‚bbpdselfÙ±‚aoa.Ù±‚`cindÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`a(Ù±‚bbpdselfÙ±‚aoa.Ù±‚`cindÙ±‚`a Ù±‚aoa+Ù±‚`a Ù±‚bmia1Ù±‚`a)Ù±‚`a Ù±‚aoa%Ù±‚`a Ù±‚bbpdselfÙ±‚aoa.Ù±‚`fslicesÙ±‚`a
Ù±‚`h        Ù±‚akdelseÙ±‚`a:Ù±‚`a
Ù±‚`l            Ù±‚bbpdselfÙ±‚aoa.Ù±‚`cindÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`a(Ù±‚bbpdselfÙ±‚aoa.Ù±‚`cindÙ±‚`a Ù±‚aoa-Ù±‚`a Ù±‚bmia1Ù±‚`a)Ù±‚`a Ù±‚aoa%Ù±‚`a Ù±‚bbpdselfÙ±‚aoa.Ù±‚`fslicesÙ±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`fupdateÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚akcdefÙ±‚`a Ù±‚bnffupdateÙ±‚`a(Ù±‚bbpdselfÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`bimÙ±‚aoa.Ù±‚`hset_dataÙ±‚`a(Ù±‚bbpdselfÙ±‚aoa.Ù±‚`aXÙ±‚`a[Ù±‚`a:Ù±‚`a,Ù±‚`a Ù±‚`a:Ù±‚`a,Ù±‚`a Ù±‚bbpdselfÙ±‚aoa.Ù±‚`cindÙ±‚`a]Ù±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`baxÙ±‚aoa.Ù±‚`jset_ylabelÙ±‚`a(Ù±‚bs1a'Ù±‚bs1fslice Ù±‚bsib%sÙ±‚bs1a'Ù±‚`a Ù±‚aoa%Ù±‚`a Ù±‚bbpdselfÙ±‚aoa.Ù±‚`cindÙ±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`bimÙ±‚aoa.Ù±‚`daxesÙ±‚aoa.Ù±‚`ffigureÙ±‚aoa.Ù±‚`fcanvasÙ±‚aoa.Ù±‚`ddrawÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚`cfigÙ±‚`a,Ù±‚`a Ù±‚`baxÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cpltÙ±‚aoa.Ù±‚`hsubplotsÙ±‚`a(Ù±‚bmia1Ù±‚`a,Ù±‚`a Ù±‚bmia1Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`aXÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`frandomÙ±‚aoa.Ù±‚`drandÙ±‚`a(Ù±‚bmib20Ù±‚`a,Ù±‚`a Ù±‚bmib20Ù±‚`a,Ù±‚`a Ù±‚bmib40Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`gtrackerÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`lIndexTrackerÙ±‚`a(Ù±‚`baxÙ±‚`a,Ù±‚`a Ù±‚`aXÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚`cfigÙ±‚aoa.Ù±‚`fcanvasÙ±‚aoa.Ù±‚`kmpl_connectÙ±‚`a(Ù±‚bs1a'Ù±‚bs1lscroll_eventÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`gtrackerÙ±‚aoa.Ù±‚`ion_scrollÙ±‚`a)Ù±‚`a
Ù±‚`cpltÙ±‚aoa.Ù±‚`dshowÙ±‚`a(Ù±‚`a)Ù±‚`a
`dNoneö