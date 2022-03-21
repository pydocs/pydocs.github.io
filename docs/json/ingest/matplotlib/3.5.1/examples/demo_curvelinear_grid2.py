Ù¯‚Ù´ƒ™?Ù±‚bsdy3"""
======================
Demo CurveLinear Grid2
======================

Custom grid and ticklines.

This example demonstrates how to use GridHelperCurveLinear to define
custom grids and ticklines by applying a transformation on the grid.
As showcase on the plot, a 5x5 matrix is displayed on the axes.
"""Ù±‚`a
Ù±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„enumpyÙ „enumpyf1.22.3fmoduleenumpyfmoduleõÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnnbnpÙ±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnnfpyplotÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnncpltÙ±‚`a
Ù±‚`a
Ù±‚bkndfromÙ±‚`a Ù±‚bnnlmpl_toolkitsÙ±‚bnna.Ù±‚bnnjaxisartistÙ±‚bnna.Ù±‚bnnwgrid_helper_curvelinearÙ±‚`a Ù±‚bknfimportÙ±‚`a Ù±‚`a(Ù±‚`a
Ù±‚`d    Ù±‚`uGridHelperCurveLinearÙ±‚`a)Ù±‚`a
Ù±‚bkndfromÙ±‚`a Ù±‚bnnlmpl_toolkitsÙ±‚bnna.Ù±‚bnnjaxisartistÙ±‚bnna.Ù±‚bnnkgrid_finderÙ±‚`a Ù±‚bknfimportÙ±‚`a Ù±‚`a(Ù±‚`a
Ù±‚`d    Ù±‚`sExtremeFinderSimpleÙ±‚`a,Ù±‚`a Ù±‚`kMaxNLocatorÙ±‚`a)Ù±‚`a
Ù±‚bkndfromÙ±‚`a Ù±‚bnnlmpl_toolkitsÙ±‚bnna.Ù±‚bnnjaxisartistÙ±‚bnna.Ù±‚bnniaxislinesÙ±‚`a Ù±‚bknfimportÙ±‚`a Ù±‚`dAxesÙ±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚akcdefÙ±‚`a Ù±‚bnfqcurvelinear_test1Ù±‚`a(Ù±‚`cfigÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`d    Ù±‚bsdx """Grid for custom transform."""Ù±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚akcdefÙ±‚`a Ù±‚bnfbtrÙ±‚`a(Ù±‚`axÙ±‚`a,Ù±‚`a Ù±‚`ayÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`h        Ù±‚akfreturnÙ±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`dsignÙ±‚`a(Ù±‚`axÙ±‚`a)Ù±‚aoa*Ù±‚bnbcabsÙ±‚`a(Ù±‚`axÙ±‚`a)Ù±‚aoa*Ù±‚aoa*Ù±‚bmfb.5Ù±‚`a,Ù±‚`a Ù±‚`ayÙ±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚akcdefÙ±‚`a Ù±‚bnffinv_trÙ±‚`a(Ù±‚`axÙ±‚`a,Ù±‚`a Ù±‚`ayÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`h        Ù±‚akfreturnÙ±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`dsignÙ±‚`a(Ù±‚`axÙ±‚`a)Ù±‚aoa*Ù±‚`axÙ±‚aoa*Ù±‚aoa*Ù±‚bmia2Ù±‚`a,Ù±‚`a Ù±‚`ayÙ±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚`kgrid_helperÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`uGridHelperCurveLinearÙ±‚`a(Ù±‚`a
Ù±‚`h        Ù±‚`a(Ù±‚`btrÙ±‚`a,Ù±‚`a Ù±‚`finv_trÙ±‚`a)Ù±‚`a,Ù±‚`a
Ù±‚`h        Ù±‚`nextreme_finderÙ±‚aoa=Ù±‚`sExtremeFinderSimpleÙ±‚`a(Ù±‚bmib20Ù±‚`a,Ù±‚`a Ù±‚bmib20Ù±‚`a)Ù±‚`a,Ù±‚`a
Ù±‚`h        Ù±‚bc1u# better tick densityÙ±‚`a
Ù±‚`h        Ù±‚`mgrid_locator1Ù±‚aoa=Ù±‚`kMaxNLocatorÙ±‚`a(Ù±‚`enbinsÙ±‚aoa=Ù±‚bmia6Ù±‚`a)Ù±‚`a,Ù±‚`a Ù±‚`mgrid_locator2Ù±‚aoa=Ù±‚`kMaxNLocatorÙ±‚`a(Ù±‚`enbinsÙ±‚aoa=Ù±‚bmia6Ù±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚`cax1Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cfigÙ±‚aoa.Ù±‚`kadd_subplotÙ±‚`a(Ù±‚`jaxes_classÙ±‚aoa=Ù±‚`dAxesÙ±‚`a,Ù±‚`a Ù±‚`kgrid_helperÙ±‚aoa=Ù±‚`kgrid_helperÙ±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚bc1x:# ax1 will have a ticks and gridlines defined by the givenÙ±‚`a
Ù±‚`d    Ù±‚bc1xJ# transform (+ transData of the Axes). Note that the transform of the AxesÙ±‚`a
Ù±‚`d    Ù±‚bc1xB# itself (i.e., transData) is not affected by the given transform.Ù±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚`cax1Ù±‚aoa.Ù±‚`fimshowÙ±‚`a(Ù±‚`bnpÙ±‚aoa.Ù±‚`farangeÙ±‚`a(Ù±‚bmib25Ù±‚`a)Ù±‚aoa.Ù±‚`greshapeÙ±‚`a(Ù±‚bmia5Ù±‚`a,Ù±‚`a Ù±‚bmia5Ù±‚`a)Ù±‚`a,Ù±‚`a
Ù±‚`o               Ù±‚`dvmaxÙ±‚aoa=Ù±‚bmib50Ù±‚`a,Ù±‚`a Ù±‚`dcmapÙ±‚aoa=Ù±‚`cpltÙ±‚aoa.Ù±‚`bcmÙ±‚aoa.Ù±‚`fgray_rÙ±‚`a,Ù±‚`a Ù±‚`foriginÙ±‚aoa=Ù±‚bs2a"Ù±‚bs2elowerÙ±‚bs2a"Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚akbifÙ±‚`a Ù±‚bvmh__name__Ù±‚`a Ù±‚aob==Ù±‚`a Ù±‚bs2a"Ù±‚bs2h__main__Ù±‚bs2a"Ù±‚`a:Ù±‚`a
Ù±‚`d    Ù±‚`cfigÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cpltÙ±‚aoa.Ù±‚`ffigureÙ±‚`a(Ù±‚`gfigsizeÙ±‚aoa=Ù±‚`a(Ù±‚bmia7Ù±‚`a,Ù±‚`a Ù±‚bmia4Ù±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`qcurvelinear_test1Ù±‚`a(Ù±‚`cfigÙ±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`cpltÙ±‚aoa.Ù±‚`dshowÙ±‚`a(Ù±‚`a)Ù±‚`a
`dNoneö