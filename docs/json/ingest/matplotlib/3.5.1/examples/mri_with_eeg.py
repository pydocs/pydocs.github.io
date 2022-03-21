Ù¯‚Ù´ƒ™œÙ±‚bsdxŠ"""
============
MRI With EEG
============

Displays a set of subplots with an MRI image, its intensity
histogram and some EEG traces.
"""Ù±‚`a
Ù±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„enumpyÙ „enumpyf1.22.3fmoduleenumpyfmoduleõÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnnbnpÙ±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnnfpyplotÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnncpltÙ±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnnecbookÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnnecbookÙ±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnnbcmÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnnbcmÙ±‚`a
Ù±‚`a
Ù±‚bkndfromÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnnkcollectionsÙ±‚`a Ù±‚bknfimportÙ±‚`a Ù±‚`nLineCollectionÙ±‚`a
Ù±‚bkndfromÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnnftickerÙ±‚`a Ù±‚bknfimportÙ±‚`a Ù±‚`oMultipleLocatorÙ±‚`a
Ù±‚`a
Ù±‚`cfigÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cpltÙ±‚aoa.Ù±‚`ffigureÙ±‚`a(Ù±‚bs2a"Ù±‚bs2lMRI_with_EEGÙ±‚bs2a"Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚bc1x-# Load the MRI data (256x256 16 bit integers)Ù±‚`a
Ù±‚akdwithÙ±‚`a Ù±‚`ecbookÙ±‚aoa.Ù±‚`oget_sample_dataÙ±‚`a(Ù±‚bs1a'Ù±‚bs1ls1045.ima.gzÙ±‚bs1a'Ù±‚`a)Ù±‚`a Ù±‚akbasÙ±‚`a Ù±‚`edfileÙ±‚`a:Ù±‚`a
Ù±‚`d    Ù±‚`bimÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`jfrombufferÙ±‚`a(Ù±‚`edfileÙ±‚aoa.Ù±‚`dreadÙ±‚`a(Ù±‚`a)Ù±‚`a,Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`fuint16Ù±‚`a)Ù±‚aoa.Ù±‚`greshapeÙ±‚`a(Ù±‚`a(Ù±‚bmic256Ù±‚`a,Ù±‚`a Ù±‚bmic256Ù±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚bc1t# Plot the MRI imageÙ±‚`a
Ù±‚`cax0Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cfigÙ±‚aoa.Ù±‚`kadd_subplotÙ±‚`a(Ù±‚bmia2Ù±‚`a,Ù±‚`a Ù±‚bmia2Ù±‚`a,Ù±‚`a Ù±‚bmia1Ù±‚`a)Ù±‚`a
Ù±‚`cax0Ù±‚aoa.Ù±‚`fimshowÙ±‚`a(Ù±‚`bimÙ±‚`a,Ù±‚`a Ù±‚`dcmapÙ±‚aoa=Ù±‚`bcmÙ±‚aoa.Ù±‚`dgrayÙ±‚`a)Ù±‚`a
Ù±‚`cax0Ù±‚aoa.Ù±‚`daxisÙ±‚`a(Ù±‚bs1a'Ù±‚bs1coffÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚bc1x%# Plot the histogram of MRI intensityÙ±‚`a
Ù±‚`cax1Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cfigÙ±‚aoa.Ù±‚`kadd_subplotÙ±‚`a(Ù±‚bmia2Ù±‚`a,Ù±‚`a Ù±‚bmia2Ù±‚`a,Ù±‚`a Ù±‚bmia2Ù±‚`a)Ù±‚`a
Ù±‚`bimÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`eravelÙ±‚`a(Ù±‚`bimÙ±‚`a)Ù±‚`a
Ù±‚`bimÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bimÙ±‚`a[Ù±‚`bnpÙ±‚aoa.Ù±‚`gnonzeroÙ±‚`a(Ù±‚`bimÙ±‚`a)Ù±‚`a]Ù±‚`b  Ù±‚bc1w# Ignore the backgroundÙ±‚`a
Ù±‚`bimÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bimÙ±‚`a Ù±‚aoa/Ù±‚`a Ù±‚`a(Ù±‚bmia2Ù±‚aoa*Ù±‚aoa*Ù±‚bmib16Ù±‚`a Ù±‚aoa-Ù±‚`a Ù±‚bmia1Ù±‚`a)Ù±‚`b  Ù±‚bc1k# NormalizeÙ±‚`a
Ù±‚`cax1Ù±‚aoa.Ù±‚`dhistÙ±‚`a(Ù±‚`bimÙ±‚`a,Ù±‚`a Ù±‚`dbinsÙ±‚aoa=Ù±‚bmic100Ù±‚`a)Ù±‚`a
Ù±‚`cax1Ù±‚aoa.Ù±‚`exaxisÙ±‚aoa.Ù±‚`qset_major_locatorÙ±‚`a(Ù±‚`oMultipleLocatorÙ±‚`a(Ù±‚bmfc0.4Ù±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`cax1Ù±‚aoa.Ù±‚`mminorticks_onÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`cax1Ù±‚aoa.Ù±‚`jset_yticksÙ±‚`a(Ù±‚`a[Ù±‚`a]Ù±‚`a)Ù±‚`a
Ù±‚`cax1Ù±‚aoa.Ù±‚`jset_xlabelÙ±‚`a(Ù±‚bs1a'Ù±‚bs1pIntensity (a.u.)Ù±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`cax1Ù±‚aoa.Ù±‚`jset_ylabelÙ±‚`a(Ù±‚bs1a'Ù±‚bs1kMRI densityÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚bc1s# Load the EEG dataÙ±‚`a
Ù±‚`in_samplesÙ±‚`a,Ù±‚`a Ù±‚`fn_rowsÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bmic800Ù±‚`a,Ù±‚`a Ù±‚bmia4Ù±‚`a
Ù±‚akdwithÙ±‚`a Ù±‚`ecbookÙ±‚aoa.Ù±‚`oget_sample_dataÙ±‚`a(Ù±‚bs1a'Ù±‚bs1geeg.datÙ±‚bs1a'Ù±‚`a)Ù±‚`a Ù±‚akbasÙ±‚`a Ù±‚`geegfileÙ±‚`a:Ù±‚`a
Ù±‚`d    Ù±‚`ddataÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`hfromfileÙ±‚`a(Ù±‚`geegfileÙ±‚`a,Ù±‚`a Ù±‚`edtypeÙ±‚aoa=Ù±‚bnbefloatÙ±‚`a)Ù±‚aoa.Ù±‚`greshapeÙ±‚`a(Ù±‚`a(Ù±‚`in_samplesÙ±‚`a,Ù±‚`a Ù±‚`fn_rowsÙ±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`atÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bmib10Ù±‚`a Ù±‚aoa*Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`farangeÙ±‚`a(Ù±‚`in_samplesÙ±‚`a)Ù±‚`a Ù±‚aoa/Ù±‚`a Ù±‚`in_samplesÙ±‚`a
Ù±‚`a
Ù±‚bc1n# Plot the EEGÙ±‚`a
Ù±‚`hticklocsÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`a[Ù±‚`a]Ù±‚`a
Ù±‚`cax2Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cfigÙ±‚aoa.Ù±‚`kadd_subplotÙ±‚`a(Ù±‚bmia2Ù±‚`a,Ù±‚`a Ù±‚bmia1Ù±‚`a,Ù±‚`a Ù±‚bmia2Ù±‚`a)Ù±‚`a
Ù±‚`cax2Ù±‚aoa.Ù±‚`hset_xlimÙ±‚`a(Ù±‚bmia0Ù±‚`a,Ù±‚`a Ù±‚bmib10Ù±‚`a)Ù±‚`a
Ù±‚`cax2Ù±‚aoa.Ù±‚`jset_xticksÙ±‚`a(Ù±‚`bnpÙ±‚aoa.Ù±‚`farangeÙ±‚`a(Ù±‚bmib10Ù±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`ddminÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`ddataÙ±‚aoa.Ù±‚`cminÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`ddmaxÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`ddataÙ±‚aoa.Ù±‚`cmaxÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`bdrÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`a(Ù±‚`ddmaxÙ±‚`a Ù±‚aoa-Ù±‚`a Ù±‚`ddminÙ±‚`a)Ù±‚`a Ù±‚aoa*Ù±‚`a Ù±‚bmfc0.7Ù±‚`b  Ù±‚bc1s# Crowd them a bit.Ù±‚`a
Ù±‚`by0Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`ddminÙ±‚`a
Ù±‚`by1Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`a(Ù±‚`fn_rowsÙ±‚`a Ù±‚aoa-Ù±‚`a Ù±‚bmia1Ù±‚`a)Ù±‚`a Ù±‚aoa*Ù±‚`a Ù±‚`bdrÙ±‚`a Ù±‚aoa+Ù±‚`a Ù±‚`ddmaxÙ±‚`a
Ù±‚`cax2Ù±‚aoa.Ù±‚`hset_ylimÙ±‚`a(Ù±‚`by0Ù±‚`a,Ù±‚`a Ù±‚`by1Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`dsegsÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`a[Ù±‚`a]Ù±‚`a
Ù±‚akcforÙ±‚`a Ù±‚`aiÙ±‚`a Ù±‚bowbinÙ±‚`a Ù±‚bnberangeÙ±‚`a(Ù±‚`fn_rowsÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`d    Ù±‚`dsegsÙ±‚aoa.Ù±‚`fappendÙ±‚`a(Ù±‚`bnpÙ±‚aoa.Ù±‚`lcolumn_stackÙ±‚`a(Ù±‚`a(Ù±‚`atÙ±‚`a,Ù±‚`a Ù±‚`ddataÙ±‚`a[Ù±‚`a:Ù±‚`a,Ù±‚`a Ù±‚`aiÙ±‚`a]Ù±‚`a)Ù±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`hticklocsÙ±‚aoa.Ù±‚`fappendÙ±‚`a(Ù±‚`aiÙ±‚`a Ù±‚aoa*Ù±‚`a Ù±‚`bdrÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`goffsetsÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`ezerosÙ±‚`a(Ù±‚`a(Ù±‚`fn_rowsÙ±‚`a,Ù±‚`a Ù±‚bmia2Ù±‚`a)Ù±‚`a,Ù±‚`a Ù±‚`edtypeÙ±‚aoa=Ù±‚bnbefloatÙ±‚`a)Ù±‚`a
Ù±‚`goffsetsÙ±‚`a[Ù±‚`a:Ù±‚`a,Ù±‚`a Ù±‚bmia1Ù±‚`a]Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`hticklocsÙ±‚`a
Ù±‚`a
Ù±‚`elinesÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`nLineCollectionÙ±‚`a(Ù±‚`dsegsÙ±‚`a,Ù±‚`a Ù±‚`goffsetsÙ±‚aoa=Ù±‚`goffsetsÙ±‚`a,Ù±‚`a Ù±‚`ktransOffsetÙ±‚aoa=Ù±‚bkcdNoneÙ±‚`a)Ù±‚`a
Ù±‚`cax2Ù±‚aoa.Ù±‚`nadd_collectionÙ±‚`a(Ù±‚`elinesÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚bc1x6# Set the yticks to use axes coordinates on the y axisÙ±‚`a
Ù±‚`cax2Ù±‚aoa.Ù±‚`jset_yticksÙ±‚`a(Ù±‚`hticklocsÙ±‚`a,Ù±‚`a Ù±‚`flabelsÙ±‚aoa=Ù±‚`a[Ù±‚bs1a'Ù±‚bs1cPG3Ù±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚bs1a'Ù±‚bs1cPG5Ù±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚bs1a'Ù±‚bs1cPG7Ù±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚bs1a'Ù±‚bs1cPG9Ù±‚bs1a'Ù±‚`a]Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`cax2Ù±‚aoa.Ù±‚`jset_xlabelÙ±‚`a(Ù±‚bs1a'Ù±‚bs1hTime (s)Ù±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚`cpltÙ±‚aoa.Ù±‚`ltight_layoutÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`cpltÙ±‚aoa.Ù±‚`dshowÙ±‚`a(Ù±‚`a)Ù±‚`a
`dNoneö