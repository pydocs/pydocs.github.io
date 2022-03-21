Ù¯‚Ù´ƒ™%Ù±‚bsdy%"""
==========
AGG filter
==========

Most pixel-based backends in Matplotlib use `Anti-Grain Geometry (AGG)`_ for
rendering. You can modify the rendering of Artists by applying a filter via
`.Artist.set_agg_filter`.

.. _Anti-Grain Geometry (AGG): http://agg.sourceforge.net/antigrain.com
"""Ù±‚`a
Ù±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnnbcmÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnnbcmÙ±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnnfpyplotÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnncpltÙ±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnnjtransformsÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnnkmtransformsÙ±‚`a
Ù±‚bkndfromÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnnfcolorsÙ±‚`a Ù±‚bknfimportÙ±‚`a Ù±‚`kLightSourceÙ±‚`a
Ù±‚bkndfromÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnnfartistÙ±‚`a Ù±‚bknfimportÙ±‚`a Ù±‚`fArtistÙ±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„enumpyÙ „enumpyf1.22.3fmoduleenumpyfmoduleõÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnnbnpÙ±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚akcdefÙ±‚`a Ù±‚bnfhsmooth1dÙ±‚`a(Ù±‚`axÙ±‚`a,Ù±‚`a Ù±‚`jwindow_lenÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`d    Ù±‚bc1xK# copied from https://scipy-cookbook.readthedocs.io/items/SignalSmooth.htmlÙ±‚`a
Ù±‚`d    Ù±‚`asÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`br_Ù±‚`a[Ù±‚bmia2Ù±‚aoa*Ù±‚`axÙ±‚`a[Ù±‚bmia0Ù±‚`a]Ù±‚`a Ù±‚aoa-Ù±‚`a Ù±‚`axÙ±‚`a[Ù±‚`jwindow_lenÙ±‚`a:Ù±‚bmia1Ù±‚`a:Ù±‚aoa-Ù±‚bmia1Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`axÙ±‚`a,Ù±‚`a Ù±‚bmia2Ù±‚aoa*Ù±‚`axÙ±‚`a[Ù±‚aoa-Ù±‚bmia1Ù±‚`a]Ù±‚`a Ù±‚aoa-Ù±‚`a Ù±‚`axÙ±‚`a[Ù±‚aoa-Ù±‚bmia1Ù±‚`a:Ù±‚aoa-Ù±‚`jwindow_lenÙ±‚`a:Ù±‚aoa-Ù±‚bmia1Ù±‚`a]Ù±‚`a]Ù±‚`a
Ù±‚`d    Ù±‚`awÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`ghanningÙ±‚`a(Ù±‚`jwindow_lenÙ±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`ayÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`hconvolveÙ±‚`a(Ù±‚`awÙ±‚aoa/Ù±‚`awÙ±‚aoa.Ù±‚`csumÙ±‚`a(Ù±‚`a)Ù±‚`a,Ù±‚`a Ù±‚`asÙ±‚`a,Ù±‚`a Ù±‚`dmodeÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1dsameÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚akfreturnÙ±‚`a Ù±‚`ayÙ±‚`a[Ù±‚`jwindow_lenÙ±‚aoa-Ù±‚bmia1Ù±‚`a:Ù±‚aoa-Ù±‚`jwindow_lenÙ±‚aoa+Ù±‚bmia1Ù±‚`a]Ù±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚akcdefÙ±‚`a Ù±‚bnfhsmooth2dÙ±‚`a(Ù±‚`aAÙ±‚`a,Ù±‚`a Ù±‚`esigmaÙ±‚aoa=Ù±‚bmia3Ù±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`d    Ù±‚`jwindow_lenÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bnbcmaxÙ±‚`a(Ù±‚bnbcintÙ±‚`a(Ù±‚`esigmaÙ±‚`a)Ù±‚`a,Ù±‚`a Ù±‚bmia3Ù±‚`a)Ù±‚`a Ù±‚aoa*Ù±‚`a Ù±‚bmia2Ù±‚`a Ù±‚aoa+Ù±‚`a Ù±‚bmia1Ù±‚`a
Ù±‚`d    Ù±‚`aAÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`papply_along_axisÙ±‚`a(Ù±‚`hsmooth1dÙ±‚`a,Ù±‚`a Ù±‚bmia0Ù±‚`a,Ù±‚`a Ù±‚`aAÙ±‚`a,Ù±‚`a Ù±‚`jwindow_lenÙ±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`aAÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`papply_along_axisÙ±‚`a(Ù±‚`hsmooth1dÙ±‚`a,Ù±‚`a Ù±‚bmia1Ù±‚`a,Ù±‚`a Ù±‚`aAÙ±‚`a,Ù±‚`a Ù±‚`jwindow_lenÙ±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚akfreturnÙ±‚`a Ù±‚`aAÙ±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚akeclassÙ±‚`a Ù±‚bncjBaseFilterÙ±‚`a:Ù±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚akcdefÙ±‚`a Ù±‚bnfgget_padÙ±‚`a(Ù±‚bbpdselfÙ±‚`a,Ù±‚`a Ù±‚`cdpiÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`h        Ù±‚akfreturnÙ±‚`a Ù±‚bmia0Ù±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚akcdefÙ±‚`a Ù±‚bnfmprocess_imageÙ±‚`a(Ù±‚`jpadded_srcÙ±‚`a,Ù±‚`a Ù±‚`cdpiÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`h        Ù±‚akeraiseÙ±‚`a Ù±‚bnesNotImplementedErrorÙ±‚`a(Ù±‚bs2a"Ù±‚bs2x"Should be overridden by subclassesÙ±‚bs2a"Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚akcdefÙ±‚`a Ù±‚bfmh__call__Ù±‚`a(Ù±‚bbpdselfÙ±‚`a,Ù±‚`a Ù±‚`bimÙ±‚`a,Ù±‚`a Ù±‚`cdpiÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`h        Ù±‚`cpadÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bbpdselfÙ±‚aoa.Ù±‚`gget_padÙ±‚`a(Ù±‚`cdpiÙ±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚`jpadded_srcÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`cpadÙ±‚`a(Ù±‚`bimÙ±‚`a,Ù±‚`a Ù±‚`a[Ù±‚`a(Ù±‚`cpadÙ±‚`a,Ù±‚`a Ù±‚`cpadÙ±‚`a)Ù±‚`a,Ù±‚`a Ù±‚`a(Ù±‚`cpadÙ±‚`a,Ù±‚`a Ù±‚`cpadÙ±‚`a)Ù±‚`a,Ù±‚`a Ù±‚`a(Ù±‚bmia0Ù±‚`a,Ù±‚`a Ù±‚bmia0Ù±‚`a)Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚bs2a"Ù±‚bs2hconstantÙ±‚bs2a"Ù±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚`itgt_imageÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bbpdselfÙ±‚aoa.Ù±‚`mprocess_imageÙ±‚`a(Ù±‚`jpadded_srcÙ±‚`a,Ù±‚`a Ù±‚`cdpiÙ±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚akfreturnÙ±‚`a Ù±‚`itgt_imageÙ±‚`a,Ù±‚`a Ù±‚aoa-Ù±‚`cpadÙ±‚`a,Ù±‚`a Ù±‚aoa-Ù±‚`cpadÙ±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚akeclassÙ±‚`a Ù±‚bnclOffsetFilterÙ±‚`a(Ù±‚`jBaseFilterÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚akcdefÙ±‚`a Ù±‚bfmh__init__Ù±‚`a(Ù±‚bbpdselfÙ±‚`a,Ù±‚`a Ù±‚`goffsetsÙ±‚aoa=Ù±‚`a(Ù±‚bmia0Ù±‚`a,Ù±‚`a Ù±‚bmia0Ù±‚`a)Ù±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`goffsetsÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`goffsetsÙ±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚akcdefÙ±‚`a Ù±‚bnfgget_padÙ±‚`a(Ù±‚bbpdselfÙ±‚`a,Ù±‚`a Ù±‚`cdpiÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`h        Ù±‚akfreturnÙ±‚`a Ù±‚bnbcintÙ±‚`a(Ù±‚bnbcmaxÙ±‚`a(Ù±‚bbpdselfÙ±‚aoa.Ù±‚`goffsetsÙ±‚`a)Ù±‚`a Ù±‚aoa/Ù±‚`a Ù±‚bmib72Ù±‚`a Ù±‚aoa*Ù±‚`a Ù±‚`cdpiÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚akcdefÙ±‚`a Ù±‚bnfmprocess_imageÙ±‚`a(Ù±‚bbpdselfÙ±‚`a,Ù±‚`a Ù±‚`jpadded_srcÙ±‚`a,Ù±‚`a Ù±‚`cdpiÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`h        Ù±‚`boxÙ±‚`a,Ù±‚`a Ù±‚`boyÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bbpdselfÙ±‚aoa.Ù±‚`goffsetsÙ±‚`a
Ù±‚`h        Ù±‚`ba1Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`drollÙ±‚`a(Ù±‚`jpadded_srcÙ±‚`a,Ù±‚`a Ù±‚bnbcintÙ±‚`a(Ù±‚`boxÙ±‚`a Ù±‚aoa/Ù±‚`a Ù±‚bmib72Ù±‚`a Ù±‚aoa*Ù±‚`a Ù±‚`cdpiÙ±‚`a)Ù±‚`a,Ù±‚`a Ù±‚`daxisÙ±‚aoa=Ù±‚bmia1Ù±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚`ba2Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`drollÙ±‚`a(Ù±‚`ba1Ù±‚`a,Ù±‚`a Ù±‚aoa-Ù±‚bnbcintÙ±‚`a(Ù±‚`boyÙ±‚`a Ù±‚aoa/Ù±‚`a Ù±‚bmib72Ù±‚`a Ù±‚aoa*Ù±‚`a Ù±‚`cdpiÙ±‚`a)Ù±‚`a,Ù±‚`a Ù±‚`daxisÙ±‚aoa=Ù±‚bmia0Ù±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚akfreturnÙ±‚`a Ù±‚`ba2Ù±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚akeclassÙ±‚`a Ù±‚bncnGaussianFilterÙ±‚`a(Ù±‚`jBaseFilterÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`d    Ù±‚bsdx"""Simple Gaussian filter."""Ù±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚akcdefÙ±‚`a Ù±‚bfmh__init__Ù±‚`a(Ù±‚bbpdselfÙ±‚`a,Ù±‚`a Ù±‚`esigmaÙ±‚`a,Ù±‚`a Ù±‚`ealphaÙ±‚aoa=Ù±‚bmfc0.5Ù±‚`a,Ù±‚`a Ù±‚`ecolorÙ±‚aoa=Ù±‚`a(Ù±‚bmia0Ù±‚`a,Ù±‚`a Ù±‚bmia0Ù±‚`a,Ù±‚`a Ù±‚bmia0Ù±‚`a)Ù±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`esigmaÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`esigmaÙ±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`ealphaÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`ealphaÙ±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`ecolorÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`ecolorÙ±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚akcdefÙ±‚`a Ù±‚bnfgget_padÙ±‚`a(Ù±‚bbpdselfÙ±‚`a,Ù±‚`a Ù±‚`cdpiÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`h        Ù±‚akfreturnÙ±‚`a Ù±‚bnbcintÙ±‚`a(Ù±‚bbpdselfÙ±‚aoa.Ù±‚`esigmaÙ±‚aoa*Ù±‚bmia3Ù±‚`a Ù±‚aoa/Ù±‚`a Ù±‚bmib72Ù±‚`a Ù±‚aoa*Ù±‚`a Ù±‚`cdpiÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚akcdefÙ±‚`a Ù±‚bnfmprocess_imageÙ±‚`a(Ù±‚bbpdselfÙ±‚`a,Ù±‚`a Ù±‚`jpadded_srcÙ±‚`a,Ù±‚`a Ù±‚`cdpiÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`h        Ù±‚`itgt_imageÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`jempty_likeÙ±‚`a(Ù±‚`jpadded_srcÙ±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚`itgt_imageÙ±‚`a[Ù±‚`a:Ù±‚`a,Ù±‚`a Ù±‚`a:Ù±‚`a,Ù±‚`a Ù±‚`a:Ù±‚bmia3Ù±‚`a]Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bbpdselfÙ±‚aoa.Ù±‚`ecolorÙ±‚`a
Ù±‚`h        Ù±‚`itgt_imageÙ±‚`a[Ù±‚`a:Ù±‚`a,Ù±‚`a Ù±‚`a:Ù±‚`a,Ù±‚`a Ù±‚bmia3Ù±‚`a]Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`hsmooth2dÙ±‚`a(Ù±‚`jpadded_srcÙ±‚`a[Ù±‚`a:Ù±‚`a,Ù±‚`a Ù±‚`a:Ù±‚`a,Ù±‚`a Ù±‚bmia3Ù±‚`a]Ù±‚`a Ù±‚aoa*Ù±‚`a Ù±‚bbpdselfÙ±‚aoa.Ù±‚`ealphaÙ±‚`a,Ù±‚`a
Ù±‚`x&                                      Ù±‚bbpdselfÙ±‚aoa.Ù±‚`esigmaÙ±‚`a Ù±‚aoa/Ù±‚`a Ù±‚bmib72Ù±‚`a Ù±‚aoa*Ù±‚`a Ù±‚`cdpiÙ±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚akfreturnÙ±‚`a Ù±‚`itgt_imageÙ±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚akeclassÙ±‚`a Ù±‚bncpDropShadowFilterÙ±‚`a(Ù±‚`jBaseFilterÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚akcdefÙ±‚`a Ù±‚bfmh__init__Ù±‚`a(Ù±‚bbpdselfÙ±‚`a,Ù±‚`a Ù±‚`esigmaÙ±‚`a,Ù±‚`a Ù±‚`ealphaÙ±‚aoa=Ù±‚bmfc0.3Ù±‚`a,Ù±‚`a Ù±‚`ecolorÙ±‚aoa=Ù±‚`a(Ù±‚bmia0Ù±‚`a,Ù±‚`a Ù±‚bmia0Ù±‚`a,Ù±‚`a Ù±‚bmia0Ù±‚`a)Ù±‚`a,Ù±‚`a Ù±‚`goffsetsÙ±‚aoa=Ù±‚`a(Ù±‚bmia0Ù±‚`a,Ù±‚`a Ù±‚bmia0Ù±‚`a)Ù±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`lgauss_filterÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`nGaussianFilterÙ±‚`a(Ù±‚`esigmaÙ±‚`a,Ù±‚`a Ù±‚`ealphaÙ±‚`a,Ù±‚`a Ù±‚`ecolorÙ±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`moffset_filterÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`lOffsetFilterÙ±‚`a(Ù±‚`goffsetsÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚akcdefÙ±‚`a Ù±‚bnfgget_padÙ±‚`a(Ù±‚bbpdselfÙ±‚`a,Ù±‚`a Ù±‚`cdpiÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`h        Ù±‚akfreturnÙ±‚`a Ù±‚bnbcmaxÙ±‚`a(Ù±‚bbpdselfÙ±‚aoa.Ù±‚`lgauss_filterÙ±‚aoa.Ù±‚`gget_padÙ±‚`a(Ù±‚`cdpiÙ±‚`a)Ù±‚`a,Ù±‚`a
Ù±‚`s                   Ù±‚bbpdselfÙ±‚aoa.Ù±‚`moffset_filterÙ±‚aoa.Ù±‚`gget_padÙ±‚`a(Ù±‚`cdpiÙ±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚akcdefÙ±‚`a Ù±‚bnfmprocess_imageÙ±‚`a(Ù±‚bbpdselfÙ±‚`a,Ù±‚`a Ù±‚`jpadded_srcÙ±‚`a,Ù±‚`a Ù±‚`cdpiÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`h        Ù±‚`bt1Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bbpdselfÙ±‚aoa.Ù±‚`lgauss_filterÙ±‚aoa.Ù±‚`mprocess_imageÙ±‚`a(Ù±‚`jpadded_srcÙ±‚`a,Ù±‚`a Ù±‚`cdpiÙ±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚`bt2Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bbpdselfÙ±‚aoa.Ù±‚`moffset_filterÙ±‚aoa.Ù±‚`mprocess_imageÙ±‚`a(Ù±‚`bt1Ù±‚`a,Ù±‚`a Ù±‚`cdpiÙ±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚akfreturnÙ±‚`a Ù±‚`bt2Ù±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚akeclassÙ±‚`a Ù±‚bnckLightFilterÙ±‚`a(Ù±‚`jBaseFilterÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚akcdefÙ±‚`a Ù±‚bfmh__init__Ù±‚`a(Ù±‚bbpdselfÙ±‚`a,Ù±‚`a Ù±‚`esigmaÙ±‚`a,Ù±‚`a Ù±‚`hfractionÙ±‚aoa=Ù±‚bmfc0.5Ù±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`lgauss_filterÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`nGaussianFilterÙ±‚`a(Ù±‚`esigmaÙ±‚`a,Ù±‚`a Ù±‚`ealphaÙ±‚aoa=Ù±‚bmia1Ù±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`llight_sourceÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`kLightSourceÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`hfractionÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`hfractionÙ±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚akcdefÙ±‚`a Ù±‚bnfgget_padÙ±‚`a(Ù±‚bbpdselfÙ±‚`a,Ù±‚`a Ù±‚`cdpiÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`h        Ù±‚akfreturnÙ±‚`a Ù±‚bbpdselfÙ±‚aoa.Ù±‚`lgauss_filterÙ±‚aoa.Ù±‚`gget_padÙ±‚`a(Ù±‚`cdpiÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚akcdefÙ±‚`a Ù±‚bnfmprocess_imageÙ±‚`a(Ù±‚bbpdselfÙ±‚`a,Ù±‚`a Ù±‚`jpadded_srcÙ±‚`a,Ù±‚`a Ù±‚`cdpiÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`h        Ù±‚`bt1Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bbpdselfÙ±‚aoa.Ù±‚`lgauss_filterÙ±‚aoa.Ù±‚`mprocess_imageÙ±‚`a(Ù±‚`jpadded_srcÙ±‚`a,Ù±‚`a Ù±‚`cdpiÙ±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚`ielevationÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bt1Ù±‚`a[Ù±‚`a:Ù±‚`a,Ù±‚`a Ù±‚`a:Ù±‚`a,Ù±‚`a Ù±‚bmia3Ù±‚`a]Ù±‚`a
Ù±‚`h        Ù±‚`crgbÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`jpadded_srcÙ±‚`a[Ù±‚`a:Ù±‚`a,Ù±‚`a Ù±‚`a:Ù±‚`a,Ù±‚`a Ù±‚`a:Ù±‚bmia3Ù±‚`a]Ù±‚`a
Ù±‚`h        Ù±‚`ealphaÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`jpadded_srcÙ±‚`a[Ù±‚`a:Ù±‚`a,Ù±‚`a Ù±‚`a:Ù±‚`a,Ù±‚`a Ù±‚bmia3Ù±‚`a:Ù±‚`a]Ù±‚`a
Ù±‚`h        Ù±‚`drgb2Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bbpdselfÙ±‚aoa.Ù±‚`llight_sourceÙ±‚aoa.Ù±‚`ishade_rgbÙ±‚`a(Ù±‚`crgbÙ±‚`a,Ù±‚`a Ù±‚`ielevationÙ±‚`a,Ù±‚`a
Ù±‚`x+                                           Ù±‚`hfractionÙ±‚aoa=Ù±‚bbpdselfÙ±‚aoa.Ù±‚`hfractionÙ±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚akfreturnÙ±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`kconcatenateÙ±‚`a(Ù±‚`a[Ù±‚`drgb2Ù±‚`a,Ù±‚`a Ù±‚`ealphaÙ±‚`a]Ù±‚`a,Ù±‚`a Ù±‚aoa-Ù±‚bmia1Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚akeclassÙ±‚`a Ù±‚bncjGrowFilterÙ±‚`a(Ù±‚`jBaseFilterÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`d    Ù±‚bsdw"""Enlarge the area."""Ù±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚akcdefÙ±‚`a Ù±‚bfmh__init__Ù±‚`a(Ù±‚bbpdselfÙ±‚`a,Ù±‚`a Ù±‚`fpixelsÙ±‚`a,Ù±‚`a Ù±‚`ecolorÙ±‚aoa=Ù±‚`a(Ù±‚bmia1Ù±‚`a,Ù±‚`a Ù±‚bmia1Ù±‚`a,Ù±‚`a Ù±‚bmia1Ù±‚`a)Ù±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`fpixelsÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`fpixelsÙ±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`ecolorÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`ecolorÙ±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚akcdefÙ±‚`a Ù±‚bfmh__call__Ù±‚`a(Ù±‚bbpdselfÙ±‚`a,Ù±‚`a Ù±‚`bimÙ±‚`a,Ù±‚`a Ù±‚`cdpiÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`h        Ù±‚`ealphaÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`cpadÙ±‚`a(Ù±‚`bimÙ±‚`a[Ù±‚aoa.Ù±‚aoa.Ù±‚aoa.Ù±‚`a,Ù±‚`a Ù±‚bmia3Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚bbpdselfÙ±‚aoa.Ù±‚`fpixelsÙ±‚`a,Ù±‚`a Ù±‚bs2a"Ù±‚bs2hconstantÙ±‚bs2a"Ù±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚`falpha2Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`dclipÙ±‚`a(Ù±‚`hsmooth2dÙ±‚`a(Ù±‚`ealphaÙ±‚`a,Ù±‚`a Ù±‚bbpdselfÙ±‚aoa.Ù±‚`fpixelsÙ±‚`a Ù±‚aoa/Ù±‚`a Ù±‚bmib72Ù±‚`a Ù±‚aoa*Ù±‚`a Ù±‚`cdpiÙ±‚`a)Ù±‚`a Ù±‚aoa*Ù±‚`a Ù±‚bmia5Ù±‚`a,Ù±‚`a Ù±‚bmia0Ù±‚`a,Ù±‚`a Ù±‚bmia1Ù±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚`fnew_imÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`eemptyÙ±‚`a(Ù±‚`a(Ù±‚aoa*Ù±‚`falpha2Ù±‚aoa.Ù±‚`eshapeÙ±‚`a,Ù±‚`a Ù±‚bmia4Ù±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚`fnew_imÙ±‚`a[Ù±‚`a:Ù±‚`a,Ù±‚`a Ù±‚`a:Ù±‚`a,Ù±‚`a Ù±‚`a:Ù±‚bmia3Ù±‚`a]Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bbpdselfÙ±‚aoa.Ù±‚`ecolorÙ±‚`a
Ù±‚`h        Ù±‚`fnew_imÙ±‚`a[Ù±‚`a:Ù±‚`a,Ù±‚`a Ù±‚`a:Ù±‚`a,Ù±‚`a Ù±‚bmia3Ù±‚`a]Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`falpha2Ù±‚`a
Ù±‚`h        Ù±‚`goffsetxÙ±‚`a,Ù±‚`a Ù±‚`goffsetyÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚aoa-Ù±‚bbpdselfÙ±‚aoa.Ù±‚`fpixelsÙ±‚`a,Ù±‚`a Ù±‚aoa-Ù±‚bbpdselfÙ±‚aoa.Ù±‚`fpixelsÙ±‚`a
Ù±‚`h        Ù±‚akfreturnÙ±‚`a Ù±‚`fnew_imÙ±‚`a,Ù±‚`a Ù±‚`goffsetxÙ±‚`a,Ù±‚`a Ù±‚`goffsetyÙ±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚akeclassÙ±‚`a Ù±‚bncrFilteredArtistListÙ±‚`a(Ù±‚`fArtistÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`d    Ù±‚bsdx<"""A simple container to filter multiple artists at once."""Ù±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚akcdefÙ±‚`a Ù±‚bfmh__init__Ù±‚`a(Ù±‚bbpdselfÙ±‚`a,Ù±‚`a Ù±‚`kartist_listÙ±‚`a,Ù±‚`a Ù±‚bnbffilterÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`h        Ù±‚bnbesuperÙ±‚`a(Ù±‚`a)Ù±‚aoa.Ù±‚bfmh__init__Ù±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`l_artist_listÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`kartist_listÙ±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`g_filterÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bnbffilterÙ±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚akcdefÙ±‚`a Ù±‚bnfddrawÙ±‚`a(Ù±‚bbpdselfÙ±‚`a,Ù±‚`a Ù±‚`hrendererÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`h        Ù±‚`hrendererÙ±‚aoa.Ù±‚`qstart_rasterizingÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚`hrendererÙ±‚aoa.Ù±‚`lstart_filterÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚akcforÙ±‚`a Ù±‚`aaÙ±‚`a Ù±‚bowbinÙ±‚`a Ù±‚bbpdselfÙ±‚aoa.Ù±‚`l_artist_listÙ±‚`a:Ù±‚`a
Ù±‚`l            Ù±‚`aaÙ±‚aoa.Ù±‚`ddrawÙ±‚`a(Ù±‚`hrendererÙ±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚`hrendererÙ±‚aoa.Ù±‚`kstop_filterÙ±‚`a(Ù±‚bbpdselfÙ±‚aoa.Ù±‚`g_filterÙ±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚`hrendererÙ±‚aoa.Ù±‚`pstop_rasterizingÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚akcdefÙ±‚`a Ù±‚bnfmfiltered_textÙ±‚`a(Ù±‚`baxÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`d    Ù±‚bc1x$# mostly copied from contour_demo.pyÙ±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚bc1o# prepare imageÙ±‚`a
Ù±‚`d    Ù±‚`edeltaÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bmfe0.025Ù±‚`a
Ù±‚`d    Ù±‚`axÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`farangeÙ±‚`a(Ù±‚aoa-Ù±‚bmfc3.0Ù±‚`a,Ù±‚`a Ù±‚bmfc3.0Ù±‚`a,Ù±‚`a Ù±‚`edeltaÙ±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`ayÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`farangeÙ±‚`a(Ù±‚aoa-Ù±‚bmfc2.0Ù±‚`a,Ù±‚`a Ù±‚bmfc2.0Ù±‚`a,Ù±‚`a Ù±‚`edeltaÙ±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`aXÙ±‚`a,Ù±‚`a Ù±‚`aYÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`hmeshgridÙ±‚`a(Ù±‚`axÙ±‚`a,Ù±‚`a Ù±‚`ayÙ±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`bZ1Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`cexpÙ±‚`a(Ù±‚aoa-Ù±‚`aXÙ±‚aoa*Ù±‚aoa*Ù±‚bmia2Ù±‚`a Ù±‚aoa-Ù±‚`a Ù±‚`aYÙ±‚aoa*Ù±‚aoa*Ù±‚bmia2Ù±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`bZ2Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`cexpÙ±‚`a(Ù±‚aoa-Ù±‚`a(Ù±‚`aXÙ±‚`a Ù±‚aoa-Ù±‚`a Ù±‚bmia1Ù±‚`a)Ù±‚aoa*Ù±‚aoa*Ù±‚bmia2Ù±‚`a Ù±‚aoa-Ù±‚`a Ù±‚`a(Ù±‚`aYÙ±‚`a Ù±‚aoa-Ù±‚`a Ù±‚bmia1Ù±‚`a)Ù±‚aoa*Ù±‚aoa*Ù±‚bmia2Ù±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`aZÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`a(Ù±‚`bZ1Ù±‚`a Ù±‚aoa-Ù±‚`a Ù±‚`bZ2Ù±‚`a)Ù±‚`a Ù±‚aoa*Ù±‚`a Ù±‚bmia2Ù±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚bc1f# drawÙ±‚`a
Ù±‚`d    Ù±‚`baxÙ±‚aoa.Ù±‚`fimshowÙ±‚`a(Ù±‚`aZÙ±‚`a,Ù±‚`a Ù±‚`minterpolationÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1hbilinearÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`foriginÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1elowerÙ±‚bs1a'Ù±‚`a,Ù±‚`a
Ù±‚`n              Ù±‚`dcmapÙ±‚aoa=Ù±‚`bcmÙ±‚aoa.Ù±‚`dgrayÙ±‚`a,Ù±‚`a Ù±‚`fextentÙ±‚aoa=Ù±‚`a(Ù±‚aoa-Ù±‚bmia3Ù±‚`a,Ù±‚`a Ù±‚bmia3Ù±‚`a,Ù±‚`a Ù±‚aoa-Ù±‚bmia2Ù±‚`a,Ù±‚`a Ù±‚bmia2Ù±‚`a)Ù±‚`a,Ù±‚`a Ù±‚`faspectÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1dautoÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`flevelsÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`farangeÙ±‚`a(Ù±‚aoa-Ù±‚bmfc1.2Ù±‚`a,Ù±‚`a Ù±‚bmfc1.6Ù±‚`a,Ù±‚`a Ù±‚bmfc0.2Ù±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`bCSÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`baxÙ±‚aoa.Ù±‚`gcontourÙ±‚`a(Ù±‚`aZÙ±‚`a,Ù±‚`a Ù±‚`flevelsÙ±‚`a,Ù±‚`a
Ù±‚`t                    Ù±‚`foriginÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1elowerÙ±‚bs1a'Ù±‚`a,Ù±‚`a
Ù±‚`t                    Ù±‚`jlinewidthsÙ±‚aoa=Ù±‚bmia2Ù±‚`a,Ù±‚`a
Ù±‚`t                    Ù±‚`fextentÙ±‚aoa=Ù±‚`a(Ù±‚aoa-Ù±‚bmia3Ù±‚`a,Ù±‚`a Ù±‚bmia3Ù±‚`a,Ù±‚`a Ù±‚aoa-Ù±‚bmia2Ù±‚`a,Ù±‚`a Ù±‚bmia2Ù±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚bc1o# contour labelÙ±‚`a
Ù±‚`d    Ù±‚`bclÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`baxÙ±‚aoa.Ù±‚`fclabelÙ±‚`a(Ù±‚`bCSÙ±‚`a,Ù±‚`a Ù±‚`flevelsÙ±‚`a[Ù±‚bmia1Ù±‚`a:Ù±‚`a:Ù±‚bmia2Ù±‚`a]Ù±‚`a,Ù±‚`b  Ù±‚bc1x# label every second levelÙ±‚`a
Ù±‚`s                   Ù±‚`finlineÙ±‚aoa=Ù±‚bkcdTrueÙ±‚`a,Ù±‚`a
Ù±‚`s                   Ù±‚`cfmtÙ±‚aoa=Ù±‚bs1a'Ù±‚bsie%1.1fÙ±‚bs1a'Ù±‚`a,Ù±‚`a
Ù±‚`s                   Ù±‚`hfontsizeÙ±‚aoa=Ù±‚bmib11Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚bc1x# change clabel color to blackÙ±‚`a
Ù±‚`d    Ù±‚bkndfromÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnnkpatheffectsÙ±‚`a Ù±‚bknfimportÙ±‚`a Ù±‚`fNormalÙ±‚`a
Ù±‚`d    Ù±‚akcforÙ±‚`a Ù±‚`atÙ±‚`a Ù±‚bowbinÙ±‚`a Ù±‚`bclÙ±‚`a:Ù±‚`a
Ù±‚`h        Ù±‚`atÙ±‚aoa.Ù±‚`iset_colorÙ±‚`a(Ù±‚bs2a"Ù±‚bs2akÙ±‚bs2a"Ù±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚bc1x5# to force TextPath (i.e., same font in all backends)Ù±‚`a
Ù±‚`h        Ù±‚`atÙ±‚aoa.Ù±‚`pset_path_effectsÙ±‚`a(Ù±‚`a[Ù±‚`fNormalÙ±‚`a(Ù±‚`a)Ù±‚`a]Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚bc1x2# Add white glows to improve visibility of labels.Ù±‚`a
Ù±‚`d    Ù±‚`kwhite_glowsÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`rFilteredArtistListÙ±‚`a(Ù±‚`bclÙ±‚`a,Ù±‚`a Ù±‚`jGrowFilterÙ±‚`a(Ù±‚bmia3Ù±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`baxÙ±‚aoa.Ù±‚`jadd_artistÙ±‚`a(Ù±‚`kwhite_glowsÙ±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`kwhite_glowsÙ±‚aoa.Ù±‚`jset_zorderÙ±‚`a(Ù±‚`bclÙ±‚`a[Ù±‚bmia0Ù±‚`a]Ù±‚aoa.Ù±‚`jget_zorderÙ±‚`a(Ù±‚`a)Ù±‚`a Ù±‚aoa-Ù±‚`a Ù±‚bmfc0.1Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚`baxÙ±‚aoa.Ù±‚`exaxisÙ±‚aoa.Ù±‚`kset_visibleÙ±‚`a(Ù±‚bkceFalseÙ±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`baxÙ±‚aoa.Ù±‚`eyaxisÙ±‚aoa.Ù±‚`kset_visibleÙ±‚`a(Ù±‚bkceFalseÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚akcdefÙ±‚`a Ù±‚bnfpdrop_shadow_lineÙ±‚`a(Ù±‚`baxÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`d    Ù±‚bc1x.# copied from examples/misc/svg_filter_line.pyÙ±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚bc1l# draw linesÙ±‚`a
Ù±‚`d    Ù±‚`bl1Ù±‚`a,Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`baxÙ±‚aoa.Ù±‚`dplotÙ±‚`a(Ù±‚`a[Ù±‚bmfc0.1Ù±‚`a,Ù±‚`a Ù±‚bmfc0.5Ù±‚`a,Ù±‚`a Ù±‚bmfc0.9Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`a[Ù±‚bmfc0.1Ù±‚`a,Ù±‚`a Ù±‚bmfc0.9Ù±‚`a,Ù±‚`a Ù±‚bmfc0.5Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚bs2a"Ù±‚bs2cbo-Ù±‚bs2a"Ù±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`bl2Ù±‚`a,Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`baxÙ±‚aoa.Ù±‚`dplotÙ±‚`a(Ù±‚`a[Ù±‚bmfc0.1Ù±‚`a,Ù±‚`a Ù±‚bmfc0.5Ù±‚`a,Ù±‚`a Ù±‚bmfc0.9Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`a[Ù±‚bmfc0.5Ù±‚`a,Ù±‚`a Ù±‚bmfc0.2Ù±‚`a,Ù±‚`a Ù±‚bmfc0.7Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚bs2a"Ù±‚bs2cro-Ù±‚bs2a"Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚`egaussÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`pDropShadowFilterÙ±‚`a(Ù±‚bmia4Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚akcforÙ±‚`a Ù±‚`alÙ±‚`a Ù±‚bowbinÙ±‚`a Ù±‚`a[Ù±‚`bl1Ù±‚`a,Ù±‚`a Ù±‚`bl2Ù±‚`a]Ù±‚`a:Ù±‚`a
Ù±‚`a
Ù±‚`h        Ù±‚bc1x2# draw shadows with same lines with slight offset.Ù±‚`a
Ù±‚`h        Ù±‚`bxxÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`alÙ±‚aoa.Ù±‚`iget_xdataÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚`byyÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`alÙ±‚aoa.Ù±‚`iget_ydataÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚`fshadowÙ±‚`a,Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`baxÙ±‚aoa.Ù±‚`dplotÙ±‚`a(Ù±‚`bxxÙ±‚`a,Ù±‚`a Ù±‚`byyÙ±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚`fshadowÙ±‚aoa.Ù±‚`kupdate_fromÙ±‚`a(Ù±‚`alÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`h        Ù±‚bc1r# offset transformÙ±‚`a
Ù±‚`h        Ù±‚`botÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`kmtransformsÙ±‚aoa.Ù±‚`koffset_copyÙ±‚`a(Ù±‚`alÙ±‚aoa.Ù±‚`mget_transformÙ±‚`a(Ù±‚`a)Ù±‚`a,Ù±‚`a Ù±‚`baxÙ±‚aoa.Ù±‚`ffigureÙ±‚`a,Ù±‚`a
Ù±‚`x%                                     Ù±‚`axÙ±‚aoa=Ù±‚bmfc4.0Ù±‚`a,Ù±‚`a Ù±‚`ayÙ±‚aoa=Ù±‚aoa-Ù±‚bmfc6.0Ù±‚`a,Ù±‚`a Ù±‚`eunitsÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1fpointsÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`h        Ù±‚`fshadowÙ±‚aoa.Ù±‚`mset_transformÙ±‚`a(Ù±‚`botÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`h        Ù±‚bc1xA# adjust zorder of the shadow lines so that it is drawn below theÙ±‚`a
Ù±‚`h        Ù±‚bc1p# original linesÙ±‚`a
Ù±‚`h        Ù±‚`fshadowÙ±‚aoa.Ù±‚`jset_zorderÙ±‚`a(Ù±‚`alÙ±‚aoa.Ù±‚`jget_zorderÙ±‚`a(Ù±‚`a)Ù±‚`a Ù±‚aoa-Ù±‚`a Ù±‚bmfc0.5Ù±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚`fshadowÙ±‚aoa.Ù±‚`nset_agg_filterÙ±‚`a(Ù±‚`egaussÙ±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚`fshadowÙ±‚aoa.Ù±‚`nset_rasterizedÙ±‚`a(Ù±‚bkcdTrueÙ±‚`a)Ù±‚`b  Ù±‚bc1x!# to support mixed-mode renderersÙ±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚`baxÙ±‚aoa.Ù±‚`hset_xlimÙ±‚`a(Ù±‚bmfb0.Ù±‚`a,Ù±‚`a Ù±‚bmfb1.Ù±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`baxÙ±‚aoa.Ù±‚`hset_ylimÙ±‚`a(Ù±‚bmfb0.Ù±‚`a,Ù±‚`a Ù±‚bmfb1.Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚`baxÙ±‚aoa.Ù±‚`exaxisÙ±‚aoa.Ù±‚`kset_visibleÙ±‚`a(Ù±‚bkceFalseÙ±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`baxÙ±‚aoa.Ù±‚`eyaxisÙ±‚aoa.Ù±‚`kset_visibleÙ±‚`a(Ù±‚bkceFalseÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚akcdefÙ±‚`a Ù±‚bnfsdrop_shadow_patchesÙ±‚`a(Ù±‚`baxÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`d    Ù±‚bc1x# Copied from barchart_demo.pyÙ±‚`a
Ù±‚`d    Ù±‚`aNÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bmia5Ù±‚`a
Ù±‚`d    Ù±‚`imen_meansÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`a[Ù±‚bmib20Ù±‚`a,Ù±‚`a Ù±‚bmib35Ù±‚`a,Ù±‚`a Ù±‚bmib30Ù±‚`a,Ù±‚`a Ù±‚bmib35Ù±‚`a,Ù±‚`a Ù±‚bmib27Ù±‚`a]Ù±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚`cindÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`farangeÙ±‚`a(Ù±‚`aNÙ±‚`a)Ù±‚`b  Ù±‚bc1x # the x locations for the groupsÙ±‚`a
Ù±‚`d    Ù±‚`ewidthÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bmfd0.35Ù±‚`b  Ù±‚bc1w# the width of the barsÙ±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚`frects1Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`baxÙ±‚aoa.Ù±‚`cbarÙ±‚`a(Ù±‚`cindÙ±‚`a,Ù±‚`a Ù±‚`imen_meansÙ±‚`a,Ù±‚`a Ù±‚`ewidthÙ±‚`a,Ù±‚`a Ù±‚`ecolorÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1arÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`becÙ±‚aoa=Ù±‚bs2a"Ù±‚bs2awÙ±‚bs2a"Ù±‚`a,Ù±‚`a Ù±‚`blwÙ±‚aoa=Ù±‚bmia2Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚`kwomen_meansÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`a[Ù±‚bmib25Ù±‚`a,Ù±‚`a Ù±‚bmib32Ù±‚`a,Ù±‚`a Ù±‚bmib34Ù±‚`a,Ù±‚`a Ù±‚bmib20Ù±‚`a,Ù±‚`a Ù±‚bmib25Ù±‚`a]Ù±‚`a
Ù±‚`d    Ù±‚`frects2Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`baxÙ±‚aoa.Ù±‚`cbarÙ±‚`a(Ù±‚`cindÙ±‚`a Ù±‚aoa+Ù±‚`a Ù±‚`ewidthÙ±‚`a Ù±‚aoa+Ù±‚`a Ù±‚bmfc0.1Ù±‚`a,Ù±‚`a Ù±‚`kwomen_meansÙ±‚`a,Ù±‚`a Ù±‚`ewidthÙ±‚`a,Ù±‚`a
Ù±‚`t                    Ù±‚`ecolorÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1ayÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`becÙ±‚aoa=Ù±‚bs2a"Ù±‚bs2awÙ±‚bs2a"Ù±‚`a,Ù±‚`a Ù±‚`blwÙ±‚aoa=Ù±‚bmia2Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚bc1x-# gauss = GaussianFilter(1.5, offsets=(1, 1))Ù±‚`a
Ù±‚`d    Ù±‚`egaussÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`pDropShadowFilterÙ±‚`a(Ù±‚bmia5Ù±‚`a,Ù±‚`a Ù±‚`goffsetsÙ±‚aoa=Ù±‚`a(Ù±‚bmia1Ù±‚`a,Ù±‚`a Ù±‚bmia1Ù±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`fshadowÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`rFilteredArtistListÙ±‚`a(Ù±‚`frects1Ù±‚`a Ù±‚aoa+Ù±‚`a Ù±‚`frects2Ù±‚`a,Ù±‚`a Ù±‚`egaussÙ±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`baxÙ±‚aoa.Ù±‚`jadd_artistÙ±‚`a(Ù±‚`fshadowÙ±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`fshadowÙ±‚aoa.Ù±‚`jset_zorderÙ±‚`a(Ù±‚`frects1Ù±‚`a[Ù±‚bmia0Ù±‚`a]Ù±‚aoa.Ù±‚`jget_zorderÙ±‚`a(Ù±‚`a)Ù±‚`a Ù±‚aoa-Ù±‚`a Ù±‚bmfc0.1Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚`baxÙ±‚aoa.Ù±‚`hset_ylimÙ±‚`a(Ù±‚bmia0Ù±‚`a,Ù±‚`a Ù±‚bmib40Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚`baxÙ±‚aoa.Ù±‚`exaxisÙ±‚aoa.Ù±‚`kset_visibleÙ±‚`a(Ù±‚bkceFalseÙ±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`baxÙ±‚aoa.Ù±‚`eyaxisÙ±‚aoa.Ù±‚`kset_visibleÙ±‚`a(Ù±‚bkceFalseÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚akcdefÙ±‚`a Ù±‚bnfplight_filter_pieÙ±‚`a(Ù±‚`baxÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`d    Ù±‚`efracsÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`a[Ù±‚bmib15Ù±‚`a,Ù±‚`a Ù±‚bmib30Ù±‚`a,Ù±‚`a Ù±‚bmib45Ù±‚`a,Ù±‚`a Ù±‚bmib10Ù±‚`a]Ù±‚`a
Ù±‚`d    Ù±‚`gexplodeÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`a(Ù±‚bmia0Ù±‚`a,Ù±‚`a Ù±‚bmfd0.05Ù±‚`a,Ù±‚`a Ù±‚bmia0Ù±‚`a,Ù±‚`a Ù±‚bmia0Ù±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`dpiesÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`baxÙ±‚aoa.Ù±‚`cpieÙ±‚`a(Ù±‚`efracsÙ±‚`a,Ù±‚`a Ù±‚`gexplodeÙ±‚aoa=Ù±‚`gexplodeÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚`llight_filterÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`kLightFilterÙ±‚`a(Ù±‚bmia9Ù±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚akcforÙ±‚`a Ù±‚`apÙ±‚`a Ù±‚bowbinÙ±‚`a Ù±‚`dpiesÙ±‚`a[Ù±‚bmia0Ù±‚`a]Ù±‚`a:Ù±‚`a
Ù±‚`h        Ù±‚`apÙ±‚aoa.Ù±‚`nset_agg_filterÙ±‚`a(Ù±‚`llight_filterÙ±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚`apÙ±‚aoa.Ù±‚`nset_rasterizedÙ±‚`a(Ù±‚bkcdTrueÙ±‚`a)Ù±‚`b  Ù±‚bc1x!# to support mixed-mode renderersÙ±‚`a
Ù±‚`h        Ù±‚`apÙ±‚aoa.Ù±‚`csetÙ±‚`a(Ù±‚`becÙ±‚aoa=Ù±‚bs2a"Ù±‚bs2dnoneÙ±‚bs2a"Ù±‚`a,Ù±‚`a
Ù±‚`n              Ù±‚`blwÙ±‚aoa=Ù±‚bmia2Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚`egaussÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`pDropShadowFilterÙ±‚`a(Ù±‚bmia9Ù±‚`a,Ù±‚`a Ù±‚`goffsetsÙ±‚aoa=Ù±‚`a(Ù±‚bmia3Ù±‚`a,Ù±‚`a Ù±‚bmia4Ù±‚`a)Ù±‚`a,Ù±‚`a Ù±‚`ealphaÙ±‚aoa=Ù±‚bmfc0.7Ù±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`fshadowÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`rFilteredArtistListÙ±‚`a(Ù±‚`dpiesÙ±‚`a[Ù±‚bmia0Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`egaussÙ±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`baxÙ±‚aoa.Ù±‚`jadd_artistÙ±‚`a(Ù±‚`fshadowÙ±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`fshadowÙ±‚aoa.Ù±‚`jset_zorderÙ±‚`a(Ù±‚`dpiesÙ±‚`a[Ù±‚bmia0Ù±‚`a]Ù±‚`a[Ù±‚bmia0Ù±‚`a]Ù±‚aoa.Ù±‚`jget_zorderÙ±‚`a(Ù±‚`a)Ù±‚`a Ù±‚aoa-Ù±‚`a Ù±‚bmfc0.1Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚akbifÙ±‚`a Ù±‚bvmh__name__Ù±‚`a Ù±‚aob==Ù±‚`a Ù±‚bs2a"Ù±‚bs2h__main__Ù±‚bs2a"Ù±‚`a:Ù±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚`cfixÙ±‚`a,Ù±‚`a Ù±‚`caxsÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cpltÙ±‚aoa.Ù±‚`hsubplotsÙ±‚`a(Ù±‚bmia2Ù±‚`a,Ù±‚`a Ù±‚bmia2Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚`mfiltered_textÙ±‚`a(Ù±‚`caxsÙ±‚`a[Ù±‚bmia0Ù±‚`a,Ù±‚`a Ù±‚bmia0Ù±‚`a]Ù±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`pdrop_shadow_lineÙ±‚`a(Ù±‚`caxsÙ±‚`a[Ù±‚bmia0Ù±‚`a,Ù±‚`a Ù±‚bmia1Ù±‚`a]Ù±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`sdrop_shadow_patchesÙ±‚`a(Ù±‚`caxsÙ±‚`a[Ù±‚bmia1Ù±‚`a,Ù±‚`a Ù±‚bmia0Ù±‚`a]Ù±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`plight_filter_pieÙ±‚`a(Ù±‚`caxsÙ±‚`a[Ù±‚bmia1Ù±‚`a,Ù±‚`a Ù±‚bmia1Ù±‚`a]Ù±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`caxsÙ±‚`a[Ù±‚bmia1Ù±‚`a,Ù±‚`a Ù±‚bmia1Ù±‚`a]Ù±‚aoa.Ù±‚`lset_frame_onÙ±‚`a(Ù±‚bkcdTrueÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚`cpltÙ±‚aoa.Ù±‚`dshowÙ±‚`a(Ù±‚`a)Ù±‚`a
`dNoneö