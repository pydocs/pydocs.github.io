Ù¯‚Ù´ƒ™jÙ±‚bsdx›"""
=======================
Colormap Normalizations
=======================

Demonstration of using norm to map colormaps onto data in non-linear ways.
"""Ù±‚`a
Ù±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„enumpyÙ „enumpyf1.22.3fmoduleenumpyfmoduleõÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnnbnpÙ±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnnfpyplotÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnncpltÙ±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnnfcolorsÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnnfcolorsÙ±‚`a
Ù±‚`a
Ù±‚bc1xO###############################################################################Ù±‚`a
Ù±‚bc1xG# Lognorm: Instead of pcolor log10(Z1) you can have colorbars that haveÙ±‚`a
Ù±‚bc1x&# the exponential labels using a norm.Ù±‚`a
Ù±‚`a
Ù±‚`aNÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bmic100Ù±‚`a
Ù±‚`aXÙ±‚`a,Ù±‚`a Ù±‚`aYÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`emgridÙ±‚`a[Ù±‚aoa-Ù±‚bmia3Ù±‚`a:Ù±‚bmia3Ù±‚`a:Ù±‚bnbgcomplexÙ±‚`a(Ù±‚bmia0Ù±‚`a,Ù±‚`a Ù±‚`aNÙ±‚`a)Ù±‚`a,Ù±‚`a Ù±‚aoa-Ù±‚bmia2Ù±‚`a:Ù±‚bmia2Ù±‚`a:Ù±‚bnbgcomplexÙ±‚`a(Ù±‚bmia0Ù±‚`a,Ù±‚`a Ù±‚`aNÙ±‚`a)Ù±‚`a]Ù±‚`a
Ù±‚`a
Ù±‚bc1x?# A low hump with a spike coming out of the top.  Needs to haveÙ±‚`a
Ù±‚bc1xE# z/colour axis on a log scale so we see both hump and spike.  linearÙ±‚`a
Ù±‚bc1x# scale only shows the spike.Ù±‚`a
Ù±‚`a
Ù±‚`bZ1Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`cexpÙ±‚`a(Ù±‚aoa-Ù±‚`aXÙ±‚aoa*Ù±‚aoa*Ù±‚bmia2Ù±‚`a Ù±‚aoa-Ù±‚`a Ù±‚`aYÙ±‚aoa*Ù±‚aoa*Ù±‚bmia2Ù±‚`a)Ù±‚`a
Ù±‚`bZ2Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`cexpÙ±‚`a(Ù±‚aoa-Ù±‚`a(Ù±‚`aXÙ±‚`a Ù±‚aoa*Ù±‚`a Ù±‚bmib10Ù±‚`a)Ù±‚aoa*Ù±‚aoa*Ù±‚bmia2Ù±‚`a Ù±‚aoa-Ù±‚`a Ù±‚`a(Ù±‚`aYÙ±‚`a Ù±‚aoa*Ù±‚`a Ù±‚bmib10Ù±‚`a)Ù±‚aoa*Ù±‚aoa*Ù±‚bmia2Ù±‚`a)Ù±‚`a
Ù±‚`aZÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bZ1Ù±‚`a Ù±‚aoa+Ù±‚`a Ù±‚bmib50Ù±‚`a Ù±‚aoa*Ù±‚`a Ù±‚`bZ2Ù±‚`a
Ù±‚`a
Ù±‚`cfigÙ±‚`a,Ù±‚`a Ù±‚`baxÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cpltÙ±‚aoa.Ù±‚`hsubplotsÙ±‚`a(Ù±‚bmia2Ù±‚`a,Ù±‚`a Ù±‚bmia1Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`cpcmÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`baxÙ±‚`a[Ù±‚bmia0Ù±‚`a]Ù±‚aoa.Ù±‚`fpcolorÙ±‚`a(Ù±‚`aXÙ±‚`a,Ù±‚`a Ù±‚`aYÙ±‚`a,Ù±‚`a Ù±‚`aZÙ±‚`a,Ù±‚`a
Ù±‚`s                   Ù±‚`dnormÙ±‚aoa=Ù±‚`fcolorsÙ±‚aoa.Ù±‚`gLogNormÙ±‚`a(Ù±‚`dvminÙ±‚aoa=Ù±‚`aZÙ±‚aoa.Ù±‚`cminÙ±‚`a(Ù±‚`a)Ù±‚`a,Ù±‚`a Ù±‚`dvmaxÙ±‚aoa=Ù±‚`aZÙ±‚aoa.Ù±‚`cmaxÙ±‚`a(Ù±‚`a)Ù±‚`a)Ù±‚`a,Ù±‚`a
Ù±‚`s                   Ù±‚`dcmapÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1fPuBu_rÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`gshadingÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1gnearestÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`cfigÙ±‚aoa.Ù±‚`hcolorbarÙ±‚`a(Ù±‚`cpcmÙ±‚`a,Ù±‚`a Ù±‚`baxÙ±‚aoa=Ù±‚`baxÙ±‚`a[Ù±‚bmia0Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`fextendÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1cmaxÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`cpcmÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`baxÙ±‚`a[Ù±‚bmia1Ù±‚`a]Ù±‚aoa.Ù±‚`fpcolorÙ±‚`a(Ù±‚`aXÙ±‚`a,Ù±‚`a Ù±‚`aYÙ±‚`a,Ù±‚`a Ù±‚`aZÙ±‚`a,Ù±‚`a Ù±‚`dcmapÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1fPuBu_rÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`gshadingÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1gnearestÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`cfigÙ±‚aoa.Ù±‚`hcolorbarÙ±‚`a(Ù±‚`cpcmÙ±‚`a,Ù±‚`a Ù±‚`baxÙ±‚aoa=Ù±‚`baxÙ±‚`a[Ù±‚bmia1Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`fextendÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1cmaxÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚bc1xO###############################################################################Ù±‚`a
Ù±‚bc1xG# PowerNorm: Here a power-law trend in X partially obscures a rectifiedÙ±‚`a
Ù±‚bc1x@# sine wave in Y. We can remove the power law using a PowerNorm.Ù±‚`a
Ù±‚`a
Ù±‚`aXÙ±‚`a,Ù±‚`a Ù±‚`aYÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`emgridÙ±‚`a[Ù±‚bmia0Ù±‚`a:Ù±‚bmia3Ù±‚`a:Ù±‚bnbgcomplexÙ±‚`a(Ù±‚bmia0Ù±‚`a,Ù±‚`a Ù±‚`aNÙ±‚`a)Ù±‚`a,Ù±‚`a Ù±‚bmia0Ù±‚`a:Ù±‚bmia2Ù±‚`a:Ù±‚bnbgcomplexÙ±‚`a(Ù±‚bmia0Ù±‚`a,Ù±‚`a Ù±‚`aNÙ±‚`a)Ù±‚`a]Ù±‚`a
Ù±‚`bZ1Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`a(Ù±‚bmia1Ù±‚`a Ù±‚aoa+Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`csinÙ±‚`a(Ù±‚`aYÙ±‚`a Ù±‚aoa*Ù±‚`a Ù±‚bmfc10.Ù±‚`a)Ù±‚`a)Ù±‚`a Ù±‚aoa*Ù±‚`a Ù±‚`aXÙ±‚aoa*Ù±‚aoa*Ù±‚bmia2Ù±‚`a
Ù±‚`a
Ù±‚`cfigÙ±‚`a,Ù±‚`a Ù±‚`baxÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cpltÙ±‚aoa.Ù±‚`hsubplotsÙ±‚`a(Ù±‚bmia2Ù±‚`a,Ù±‚`a Ù±‚bmia1Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`cpcmÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`baxÙ±‚`a[Ù±‚bmia0Ù±‚`a]Ù±‚aoa.Ù±‚`jpcolormeshÙ±‚`a(Ù±‚`aXÙ±‚`a,Ù±‚`a Ù±‚`aYÙ±‚`a,Ù±‚`a Ù±‚`bZ1Ù±‚`a,Ù±‚`a Ù±‚`dnormÙ±‚aoa=Ù±‚`fcolorsÙ±‚aoa.Ù±‚`iPowerNormÙ±‚`a(Ù±‚`egammaÙ±‚aoa=Ù±‚bmfb1.Ù±‚`a Ù±‚aoa/Ù±‚`a Ù±‚bmfb2.Ù±‚`a)Ù±‚`a,Ù±‚`a
Ù±‚`w                       Ù±‚`dcmapÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1fPuBu_rÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`gshadingÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1gnearestÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`cfigÙ±‚aoa.Ù±‚`hcolorbarÙ±‚`a(Ù±‚`cpcmÙ±‚`a,Ù±‚`a Ù±‚`baxÙ±‚aoa=Ù±‚`baxÙ±‚`a[Ù±‚bmia0Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`fextendÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1cmaxÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`cpcmÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`baxÙ±‚`a[Ù±‚bmia1Ù±‚`a]Ù±‚aoa.Ù±‚`jpcolormeshÙ±‚`a(Ù±‚`aXÙ±‚`a,Ù±‚`a Ù±‚`aYÙ±‚`a,Ù±‚`a Ù±‚`bZ1Ù±‚`a,Ù±‚`a Ù±‚`dcmapÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1fPuBu_rÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`gshadingÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1gnearestÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`cfigÙ±‚aoa.Ù±‚`hcolorbarÙ±‚`a(Ù±‚`cpcmÙ±‚`a,Ù±‚`a Ù±‚`baxÙ±‚aoa=Ù±‚`baxÙ±‚`a[Ù±‚bmia1Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`fextendÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1cmaxÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚bc1xO###############################################################################Ù±‚`a
Ù±‚bc1xD# SymLogNorm: two humps, one negative and one positive, The positiveÙ±‚`a
Ù±‚bc1xD# with 5-times the amplitude. Linearly, you cannot see detail in theÙ±‚`a
Ù±‚bc1x@# negative hump.  Here we logarithmically scale the positive andÙ±‚`a
Ù±‚bc1x# negative data separately.Ù±‚`a
Ù±‚bc1a#Ù±‚`a
Ù±‚bc1x># Note that colorbar labels do not come out looking very good.Ù±‚`a
Ù±‚`a
Ù±‚`aXÙ±‚`a,Ù±‚`a Ù±‚`aYÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`emgridÙ±‚`a[Ù±‚aoa-Ù±‚bmia3Ù±‚`a:Ù±‚bmia3Ù±‚`a:Ù±‚bnbgcomplexÙ±‚`a(Ù±‚bmia0Ù±‚`a,Ù±‚`a Ù±‚`aNÙ±‚`a)Ù±‚`a,Ù±‚`a Ù±‚aoa-Ù±‚bmia2Ù±‚`a:Ù±‚bmia2Ù±‚`a:Ù±‚bnbgcomplexÙ±‚`a(Ù±‚bmia0Ù±‚`a,Ù±‚`a Ù±‚`aNÙ±‚`a)Ù±‚`a]Ù±‚`a
Ù±‚`bZ1Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bmia5Ù±‚`a Ù±‚aoa*Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`cexpÙ±‚`a(Ù±‚aoa-Ù±‚`aXÙ±‚aoa*Ù±‚aoa*Ù±‚bmia2Ù±‚`a Ù±‚aoa-Ù±‚`a Ù±‚`aYÙ±‚aoa*Ù±‚aoa*Ù±‚bmia2Ù±‚`a)Ù±‚`a
Ù±‚`bZ2Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`cexpÙ±‚`a(Ù±‚aoa-Ù±‚`a(Ù±‚`aXÙ±‚`a Ù±‚aoa-Ù±‚`a Ù±‚bmia1Ù±‚`a)Ù±‚aoa*Ù±‚aoa*Ù±‚bmia2Ù±‚`a Ù±‚aoa-Ù±‚`a Ù±‚`a(Ù±‚`aYÙ±‚`a Ù±‚aoa-Ù±‚`a Ù±‚bmia1Ù±‚`a)Ù±‚aoa*Ù±‚aoa*Ù±‚bmia2Ù±‚`a)Ù±‚`a
Ù±‚`aZÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`a(Ù±‚`bZ1Ù±‚`a Ù±‚aoa-Ù±‚`a Ù±‚`bZ2Ù±‚`a)Ù±‚`a Ù±‚aoa*Ù±‚`a Ù±‚bmia2Ù±‚`a
Ù±‚`a
Ù±‚`cfigÙ±‚`a,Ù±‚`a Ù±‚`baxÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cpltÙ±‚aoa.Ù±‚`hsubplotsÙ±‚`a(Ù±‚bmia2Ù±‚`a,Ù±‚`a Ù±‚bmia1Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`cpcmÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`baxÙ±‚`a[Ù±‚bmia0Ù±‚`a]Ù±‚aoa.Ù±‚`jpcolormeshÙ±‚`a(Ù±‚`aXÙ±‚`a,Ù±‚`a Ù±‚`aYÙ±‚`a,Ù±‚`a Ù±‚`bZ1Ù±‚`a,Ù±‚`a
Ù±‚`w                       Ù±‚`dnormÙ±‚aoa=Ù±‚`fcolorsÙ±‚aoa.Ù±‚`jSymLogNormÙ±‚`a(Ù±‚`ilinthreshÙ±‚aoa=Ù±‚bmfd0.03Ù±‚`a,Ù±‚`a Ù±‚`hlinscaleÙ±‚aoa=Ù±‚bmfd0.03Ù±‚`a,Ù±‚`a
Ù±‚`x.                                              Ù±‚`dvminÙ±‚aoa=Ù±‚aoa-Ù±‚bmfc1.0Ù±‚`a,Ù±‚`a Ù±‚`dvmaxÙ±‚aoa=Ù±‚bmfc1.0Ù±‚`a,Ù±‚`a Ù±‚`dbaseÙ±‚aoa=Ù±‚bmib10Ù±‚`a)Ù±‚`a,Ù±‚`a
Ù±‚`w                       Ù±‚`dcmapÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1fRdBu_rÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`gshadingÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1gnearestÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`cfigÙ±‚aoa.Ù±‚`hcolorbarÙ±‚`a(Ù±‚`cpcmÙ±‚`a,Ù±‚`a Ù±‚`baxÙ±‚aoa=Ù±‚`baxÙ±‚`a[Ù±‚bmia0Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`fextendÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1dbothÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`cpcmÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`baxÙ±‚`a[Ù±‚bmia1Ù±‚`a]Ù±‚aoa.Ù±‚`jpcolormeshÙ±‚`a(Ù±‚`aXÙ±‚`a,Ù±‚`a Ù±‚`aYÙ±‚`a,Ù±‚`a Ù±‚`bZ1Ù±‚`a,Ù±‚`a Ù±‚`dcmapÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1fRdBu_rÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`dvminÙ±‚aoa=Ù±‚aoa-Ù±‚`bnpÙ±‚aoa.Ù±‚`cmaxÙ±‚`a(Ù±‚`bZ1Ù±‚`a)Ù±‚`a,Ù±‚`a
Ù±‚`w                       Ù±‚`gshadingÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1gnearestÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`cfigÙ±‚aoa.Ù±‚`hcolorbarÙ±‚`a(Ù±‚`cpcmÙ±‚`a,Ù±‚`a Ù±‚`baxÙ±‚aoa=Ù±‚`baxÙ±‚`a[Ù±‚bmia1Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`fextendÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1dbothÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚bc1xO###############################################################################Ù±‚`a
Ù±‚bc1xD# Custom Norm: An example with a customized normalization.  This oneÙ±‚`a
Ù±‚bc1xF# uses the example above, and normalizes the negative data differentlyÙ±‚`a
Ù±‚bc1t# from the positive.Ù±‚`a
Ù±‚`a
Ù±‚`aXÙ±‚`a,Ù±‚`a Ù±‚`aYÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`emgridÙ±‚`a[Ù±‚aoa-Ù±‚bmia3Ù±‚`a:Ù±‚bmia3Ù±‚`a:Ù±‚bnbgcomplexÙ±‚`a(Ù±‚bmia0Ù±‚`a,Ù±‚`a Ù±‚`aNÙ±‚`a)Ù±‚`a,Ù±‚`a Ù±‚aoa-Ù±‚bmia2Ù±‚`a:Ù±‚bmia2Ù±‚`a:Ù±‚bnbgcomplexÙ±‚`a(Ù±‚bmia0Ù±‚`a,Ù±‚`a Ù±‚`aNÙ±‚`a)Ù±‚`a]Ù±‚`a
Ù±‚`bZ1Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`cexpÙ±‚`a(Ù±‚aoa-Ù±‚`aXÙ±‚aoa*Ù±‚aoa*Ù±‚bmia2Ù±‚`a Ù±‚aoa-Ù±‚`a Ù±‚`aYÙ±‚aoa*Ù±‚aoa*Ù±‚bmia2Ù±‚`a)Ù±‚`a
Ù±‚`bZ2Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`cexpÙ±‚`a(Ù±‚aoa-Ù±‚`a(Ù±‚`aXÙ±‚`a Ù±‚aoa-Ù±‚`a Ù±‚bmia1Ù±‚`a)Ù±‚aoa*Ù±‚aoa*Ù±‚bmia2Ù±‚`a Ù±‚aoa-Ù±‚`a Ù±‚`a(Ù±‚`aYÙ±‚`a Ù±‚aoa-Ù±‚`a Ù±‚bmia1Ù±‚`a)Ù±‚aoa*Ù±‚aoa*Ù±‚bmia2Ù±‚`a)Ù±‚`a
Ù±‚`aZÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`a(Ù±‚`bZ1Ù±‚`a Ù±‚aoa-Ù±‚`a Ù±‚`bZ2Ù±‚`a)Ù±‚`a Ù±‚aoa*Ù±‚`a Ù±‚bmia2Ù±‚`a
Ù±‚`a
Ù±‚bc1x?# Example of making your own norm.  Also see matplotlib.colors.Ù±‚`a
Ù±‚bc1x># From Joe Kington: This one gives two different linear ramps:Ù±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚akeclassÙ±‚`a Ù±‚bncqMidpointNormalizeÙ±‚`a(Ù±‚`fcolorsÙ±‚aoa.Ù±‚`iNormalizeÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`d    Ù±‚akcdefÙ±‚`a Ù±‚bfmh__init__Ù±‚`a(Ù±‚bbpdselfÙ±‚`a,Ù±‚`a Ù±‚`dvminÙ±‚aoa=Ù±‚bkcdNoneÙ±‚`a,Ù±‚`a Ù±‚`dvmaxÙ±‚aoa=Ù±‚bkcdNoneÙ±‚`a,Ù±‚`a Ù±‚`hmidpointÙ±‚aoa=Ù±‚bkcdNoneÙ±‚`a,Ù±‚`a Ù±‚`dclipÙ±‚aoa=Ù±‚bkceFalseÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`hmidpointÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`hmidpointÙ±‚`a
Ù±‚`h        Ù±‚bnbesuperÙ±‚`a(Ù±‚`a)Ù±‚aoa.Ù±‚bfmh__init__Ù±‚`a(Ù±‚`dvminÙ±‚`a,Ù±‚`a Ù±‚`dvmaxÙ±‚`a,Ù±‚`a Ù±‚`dclipÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚akcdefÙ±‚`a Ù±‚bfmh__call__Ù±‚`a(Ù±‚bbpdselfÙ±‚`a,Ù±‚`a Ù±‚`evalueÙ±‚`a,Ù±‚`a Ù±‚`dclipÙ±‚aoa=Ù±‚bkcdNoneÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`h        Ù±‚bc1xB# I'm ignoring masked values and all kinds of edge cases to make aÙ±‚`a
Ù±‚`h        Ù±‚bc1s# simple example...Ù±‚`a
Ù±‚`h        Ù±‚`axÙ±‚`a,Ù±‚`a Ù±‚`ayÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`a[Ù±‚bbpdselfÙ±‚aoa.Ù±‚`dvminÙ±‚`a,Ù±‚`a Ù±‚bbpdselfÙ±‚aoa.Ù±‚`hmidpointÙ±‚`a,Ù±‚`a Ù±‚bbpdselfÙ±‚aoa.Ù±‚`dvmaxÙ±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`a[Ù±‚bmia0Ù±‚`a,Ù±‚`a Ù±‚bmfc0.5Ù±‚`a,Ù±‚`a Ù±‚bmia1Ù±‚`a]Ù±‚`a
Ù±‚`h        Ù±‚akfreturnÙ±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`bmaÙ±‚aoa.Ù±‚`lmasked_arrayÙ±‚`a(Ù±‚`bnpÙ±‚aoa.Ù±‚`finterpÙ±‚`a(Ù±‚`evalueÙ±‚`a,Ù±‚`a Ù±‚`axÙ±‚`a,Ù±‚`a Ù±‚`ayÙ±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚bc1e#####Ù±‚`a
Ù±‚`cfigÙ±‚`a,Ù±‚`a Ù±‚`baxÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cpltÙ±‚aoa.Ù±‚`hsubplotsÙ±‚`a(Ù±‚bmia2Ù±‚`a,Ù±‚`a Ù±‚bmia1Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`cpcmÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`baxÙ±‚`a[Ù±‚bmia0Ù±‚`a]Ù±‚aoa.Ù±‚`jpcolormeshÙ±‚`a(Ù±‚`aXÙ±‚`a,Ù±‚`a Ù±‚`aYÙ±‚`a,Ù±‚`a Ù±‚`aZÙ±‚`a,Ù±‚`a
Ù±‚`w                       Ù±‚`dnormÙ±‚aoa=Ù±‚`qMidpointNormalizeÙ±‚`a(Ù±‚`hmidpointÙ±‚aoa=Ù±‚bmfb0.Ù±‚`a)Ù±‚`a,Ù±‚`a
Ù±‚`w                       Ù±‚`dcmapÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1fRdBu_rÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`gshadingÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1gnearestÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`cfigÙ±‚aoa.Ù±‚`hcolorbarÙ±‚`a(Ù±‚`cpcmÙ±‚`a,Ù±‚`a Ù±‚`baxÙ±‚aoa=Ù±‚`baxÙ±‚`a[Ù±‚bmia0Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`fextendÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1dbothÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`cpcmÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`baxÙ±‚`a[Ù±‚bmia1Ù±‚`a]Ù±‚aoa.Ù±‚`jpcolormeshÙ±‚`a(Ù±‚`aXÙ±‚`a,Ù±‚`a Ù±‚`aYÙ±‚`a,Ù±‚`a Ù±‚`aZÙ±‚`a,Ù±‚`a Ù±‚`dcmapÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1fRdBu_rÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`dvminÙ±‚aoa=Ù±‚aoa-Ù±‚`bnpÙ±‚aoa.Ù±‚`cmaxÙ±‚`a(Ù±‚`aZÙ±‚`a)Ù±‚`a,Ù±‚`a
Ù±‚`w                       Ù±‚`gshadingÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1gnearestÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`cfigÙ±‚aoa.Ù±‚`hcolorbarÙ±‚`a(Ù±‚`cpcmÙ±‚`a,Ù±‚`a Ù±‚`baxÙ±‚aoa=Ù±‚`baxÙ±‚`a[Ù±‚bmia1Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`fextendÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1dbothÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚bc1xO###############################################################################Ù±‚`a
Ù±‚bc1xH# BoundaryNorm: For this one you provide the boundaries for your colors,Ù±‚`a
Ù±‚bc1xB# and the Norm puts the first color in between the first pair, theÙ±‚`a
Ù±‚bc1x,# second color between the second pair, etc.Ù±‚`a
Ù±‚`a
Ù±‚`cfigÙ±‚`a,Ù±‚`a Ù±‚`baxÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cpltÙ±‚aoa.Ù±‚`hsubplotsÙ±‚`a(Ù±‚bmia3Ù±‚`a,Ù±‚`a Ù±‚bmia1Ù±‚`a,Ù±‚`a Ù±‚`gfigsizeÙ±‚aoa=Ù±‚`a(Ù±‚bmia8Ù±‚`a,Ù±‚`a Ù±‚bmia8Ù±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`baxÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`baxÙ±‚aoa.Ù±‚`gflattenÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚bc1x)# even bounds gives a contour-like effectÙ±‚`a
Ù±‚`fboundsÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`hlinspaceÙ±‚`a(Ù±‚aoa-Ù±‚bmia1Ù±‚`a,Ù±‚`a Ù±‚bmia1Ù±‚`a,Ù±‚`a Ù±‚bmib10Ù±‚`a)Ù±‚`a
Ù±‚`dnormÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`fcolorsÙ±‚aoa.Ù±‚`lBoundaryNormÙ±‚`a(Ù±‚`jboundariesÙ±‚aoa=Ù±‚`fboundsÙ±‚`a,Ù±‚`a Ù±‚`gncolorsÙ±‚aoa=Ù±‚bmic256Ù±‚`a)Ù±‚`a
Ù±‚`cpcmÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`baxÙ±‚`a[Ù±‚bmia0Ù±‚`a]Ù±‚aoa.Ù±‚`jpcolormeshÙ±‚`a(Ù±‚`aXÙ±‚`a,Ù±‚`a Ù±‚`aYÙ±‚`a,Ù±‚`a Ù±‚`aZÙ±‚`a,Ù±‚`a
Ù±‚`w                       Ù±‚`dnormÙ±‚aoa=Ù±‚`dnormÙ±‚`a,Ù±‚`a
Ù±‚`w                       Ù±‚`dcmapÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1fRdBu_rÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`gshadingÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1gnearestÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`cfigÙ±‚aoa.Ù±‚`hcolorbarÙ±‚`a(Ù±‚`cpcmÙ±‚`a,Ù±‚`a Ù±‚`baxÙ±‚aoa=Ù±‚`baxÙ±‚`a[Ù±‚bmia0Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`fextendÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1dbothÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`korientationÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1hverticalÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚bc1x)# uneven bounds changes the colormapping:Ù±‚`a
Ù±‚`fboundsÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`earrayÙ±‚`a(Ù±‚`a[Ù±‚aoa-Ù±‚bmfd0.25Ù±‚`a,Ù±‚`a Ù±‚aoa-Ù±‚bmfe0.125Ù±‚`a,Ù±‚`a Ù±‚bmia0Ù±‚`a,Ù±‚`a Ù±‚bmfc0.5Ù±‚`a,Ù±‚`a Ù±‚bmia1Ù±‚`a]Ù±‚`a)Ù±‚`a
Ù±‚`dnormÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`fcolorsÙ±‚aoa.Ù±‚`lBoundaryNormÙ±‚`a(Ù±‚`jboundariesÙ±‚aoa=Ù±‚`fboundsÙ±‚`a,Ù±‚`a Ù±‚`gncolorsÙ±‚aoa=Ù±‚bmic256Ù±‚`a)Ù±‚`a
Ù±‚`cpcmÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`baxÙ±‚`a[Ù±‚bmia1Ù±‚`a]Ù±‚aoa.Ù±‚`jpcolormeshÙ±‚`a(Ù±‚`aXÙ±‚`a,Ù±‚`a Ù±‚`aYÙ±‚`a,Ù±‚`a Ù±‚`aZÙ±‚`a,Ù±‚`a Ù±‚`dnormÙ±‚aoa=Ù±‚`dnormÙ±‚`a,Ù±‚`a Ù±‚`dcmapÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1fRdBu_rÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`gshadingÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1gnearestÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`cfigÙ±‚aoa.Ù±‚`hcolorbarÙ±‚`a(Ù±‚`cpcmÙ±‚`a,Ù±‚`a Ù±‚`baxÙ±‚aoa=Ù±‚`baxÙ±‚`a[Ù±‚bmia1Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`fextendÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1dbothÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`korientationÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1hverticalÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`cpcmÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`baxÙ±‚`a[Ù±‚bmia2Ù±‚`a]Ù±‚aoa.Ù±‚`jpcolormeshÙ±‚`a(Ù±‚`aXÙ±‚`a,Ù±‚`a Ù±‚`aYÙ±‚`a,Ù±‚`a Ù±‚`aZÙ±‚`a,Ù±‚`a Ù±‚`dcmapÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1fRdBu_rÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`dvminÙ±‚aoa=Ù±‚aoa-Ù±‚`bnpÙ±‚aoa.Ù±‚`cmaxÙ±‚`a(Ù±‚`bZ1Ù±‚`a)Ù±‚`a,Ù±‚`a
Ù±‚`w                       Ù±‚`gshadingÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1gnearestÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`cfigÙ±‚aoa.Ù±‚`hcolorbarÙ±‚`a(Ù±‚`cpcmÙ±‚`a,Ù±‚`a Ù±‚`baxÙ±‚aoa=Ù±‚`baxÙ±‚`a[Ù±‚bmia2Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`fextendÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1dbothÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`korientationÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1hverticalÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`cpltÙ±‚aoa.Ù±‚`dshowÙ±‚`a(Ù±‚`a)Ù±‚`a
`dNoneö