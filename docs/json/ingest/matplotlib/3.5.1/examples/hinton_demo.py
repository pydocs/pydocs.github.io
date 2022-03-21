Ù¯‚Ù´ƒ™eÙ±‚bsdyk"""
===============
Hinton diagrams
===============

Hinton diagrams are useful for visualizing the values of a 2D array (e.g.
a weight matrix): Positive and negative values are represented by white and
black squares, respectively, and the size of each square represents the
magnitude of each value.

Initial idea from David Warde-Farley on the SciPy Cookbook
"""Ù±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„enumpyÙ „enumpyf1.22.3fmoduleenumpyfmoduleõÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnnbnpÙ±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnnfpyplotÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnncpltÙ±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚akcdefÙ±‚`a Ù±‚bnffhintonÙ±‚`a(Ù±‚`fmatrixÙ±‚`a,Ù±‚`a Ù±‚`jmax_weightÙ±‚aoa=Ù±‚bkcdNoneÙ±‚`a,Ù±‚`a Ù±‚`baxÙ±‚aoa=Ù±‚bkcdNoneÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`d    Ù±‚bsdx:"""Draw Hinton diagram for visualizing a weight matrix."""Ù±‚`a
Ù±‚`d    Ù±‚`baxÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`baxÙ±‚`a Ù±‚akbifÙ±‚`a Ù±‚`baxÙ±‚`a Ù±‚bowbisÙ±‚`a Ù±‚bowcnotÙ±‚`a Ù±‚bkcdNoneÙ±‚`a Ù±‚akdelseÙ±‚`a Ù±‚`cpltÙ±‚aoa.Ù±‚`cgcaÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚akbifÙ±‚`a Ù±‚bowcnotÙ±‚`a Ù±‚`jmax_weightÙ±‚`a:Ù±‚`a
Ù±‚`h        Ù±‚`jmax_weightÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bmia2Ù±‚`a Ù±‚aoa*Ù±‚aoa*Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`dceilÙ±‚`a(Ù±‚`bnpÙ±‚aoa.Ù±‚`dlog2Ù±‚`a(Ù±‚`bnpÙ±‚aoa.Ù±‚`cabsÙ±‚`a(Ù±‚`fmatrixÙ±‚`a)Ù±‚aoa.Ù±‚`cmaxÙ±‚`a(Ù±‚`a)Ù±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚`baxÙ±‚aoa.Ù±‚`epatchÙ±‚aoa.Ù±‚`mset_facecolorÙ±‚`a(Ù±‚bs1a'Ù±‚bs1dgrayÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`baxÙ±‚aoa.Ù±‚`jset_aspectÙ±‚`a(Ù±‚bs1a'Ù±‚bs1eequalÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚bs1a'Ù±‚bs1cboxÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`baxÙ±‚aoa.Ù±‚`exaxisÙ±‚aoa.Ù±‚`qset_major_locatorÙ±‚`a(Ù±‚`cpltÙ±‚aoa.Ù±‚`kNullLocatorÙ±‚`a(Ù±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`baxÙ±‚aoa.Ù±‚`eyaxisÙ±‚aoa.Ù±‚`qset_major_locatorÙ±‚`a(Ù±‚`cpltÙ±‚aoa.Ù±‚`kNullLocatorÙ±‚`a(Ù±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚akcforÙ±‚`a Ù±‚`a(Ù±‚`axÙ±‚`a,Ù±‚`a Ù±‚`ayÙ±‚`a)Ù±‚`a,Ù±‚`a Ù±‚`awÙ±‚`a Ù±‚bowbinÙ±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`kndenumerateÙ±‚`a(Ù±‚`fmatrixÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`h        Ù±‚`ecolorÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bs1a'Ù±‚bs1ewhiteÙ±‚bs1a'Ù±‚`a Ù±‚akbifÙ±‚`a Ù±‚`awÙ±‚`a Ù±‚aoa>Ù±‚`a Ù±‚bmia0Ù±‚`a Ù±‚akdelseÙ±‚`a Ù±‚bs1a'Ù±‚bs1eblackÙ±‚bs1a'Ù±‚`a
Ù±‚`h        Ù±‚`dsizeÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`dsqrtÙ±‚`a(Ù±‚bnbcabsÙ±‚`a(Ù±‚`awÙ±‚`a)Ù±‚`a Ù±‚aoa/Ù±‚`a Ù±‚`jmax_weightÙ±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚`drectÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cpltÙ±‚aoa.Ù±‚`iRectangleÙ±‚`a(Ù±‚`a[Ù±‚`axÙ±‚`a Ù±‚aoa-Ù±‚`a Ù±‚`dsizeÙ±‚`a Ù±‚aoa/Ù±‚`a Ù±‚bmia2Ù±‚`a,Ù±‚`a Ù±‚`ayÙ±‚`a Ù±‚aoa-Ù±‚`a Ù±‚`dsizeÙ±‚`a Ù±‚aoa/Ù±‚`a Ù±‚bmia2Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`dsizeÙ±‚`a,Ù±‚`a Ù±‚`dsizeÙ±‚`a,Ù±‚`a
Ù±‚`x                             Ù±‚`ifacecolorÙ±‚aoa=Ù±‚`ecolorÙ±‚`a,Ù±‚`a Ù±‚`iedgecolorÙ±‚aoa=Ù±‚`ecolorÙ±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚`baxÙ±‚aoa.Ù±‚`iadd_patchÙ±‚`a(Ù±‚`drectÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚`baxÙ±‚aoa.Ù±‚`nautoscale_viewÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`baxÙ±‚aoa.Ù±‚`linvert_yaxisÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚akbifÙ±‚`a Ù±‚bvmh__name__Ù±‚`a Ù±‚aob==Ù±‚`a Ù±‚bs1a'Ù±‚bs1h__main__Ù±‚bs1a'Ù±‚`a:Ù±‚`a
Ù±‚`d    Ù±‚bc1x)# Fixing random state for reproducibilityÙ±‚`a
Ù±‚`d    Ù±‚`bnpÙ±‚aoa.Ù±‚`frandomÙ±‚aoa.Ù±‚`dseedÙ±‚`a(Ù±‚bmih19680801Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚`fhintonÙ±‚`a(Ù±‚`bnpÙ±‚aoa.Ù±‚`frandomÙ±‚aoa.Ù±‚`drandÙ±‚`a(Ù±‚bmib20Ù±‚`a,Ù±‚`a Ù±‚bmib20Ù±‚`a)Ù±‚`a Ù±‚aoa-Ù±‚`a Ù±‚bmfc0.5Ù±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`cpltÙ±‚aoa.Ù±‚`dshowÙ±‚`a(Ù±‚`a)Ù±‚`a
`dNoneö