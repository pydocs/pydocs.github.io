Ù¯‚Ù´ƒ™/Ù±‚bsdxÜ"""
===============
Resampling Data
===============

Downsampling lowers the sample rate or sample size of a signal. In
this tutorial, the signal is downsampled when the plot is adjusted
through dragging and zooming.
"""Ù±‚`a
Ù±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„enumpyÙ „enumpyf1.22.3fmoduleenumpyfmoduleõÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnnbnpÙ±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnnfpyplotÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnncpltÙ±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚bc1xB# A class that will downsample the data and recompute when zoomed.Ù±‚`a
Ù±‚akeclassÙ±‚`a Ù±‚bncvDataDisplayDownsamplerÙ±‚`a:Ù±‚`a
Ù±‚`d    Ù±‚akcdefÙ±‚`a Ù±‚bfmh__init__Ù±‚`a(Ù±‚bbpdselfÙ±‚`a,Ù±‚`a Ù±‚`exdataÙ±‚`a,Ù±‚`a Ù±‚`eydataÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`iorigYDataÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`eydataÙ±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`iorigXDataÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`exdataÙ±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`jmax_pointsÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bmib50Ù±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`edeltaÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`exdataÙ±‚`a[Ù±‚aoa-Ù±‚bmia1Ù±‚`a]Ù±‚`a Ù±‚aoa-Ù±‚`a Ù±‚`exdataÙ±‚`a[Ù±‚bmia0Ù±‚`a]Ù±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚akcdefÙ±‚`a Ù±‚bnfjdownsampleÙ±‚`a(Ù±‚bbpdselfÙ±‚`a,Ù±‚`a Ù±‚`fxstartÙ±‚`a,Ù±‚`a Ù±‚`dxendÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`h        Ù±‚bc1x"# get the points in the view rangeÙ±‚`a
Ù±‚`h        Ù±‚`dmaskÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`a(Ù±‚bbpdselfÙ±‚aoa.Ù±‚`iorigXDataÙ±‚`a Ù±‚aoa>Ù±‚`a Ù±‚`fxstartÙ±‚`a)Ù±‚`a Ù±‚aoa&Ù±‚`a Ù±‚`a(Ù±‚bbpdselfÙ±‚aoa.Ù±‚`iorigXDataÙ±‚`a Ù±‚aoa<Ù±‚`a Ù±‚`dxendÙ±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚bc1x9# dilate the mask by one to catch the points just outsideÙ±‚`a
Ù±‚`h        Ù±‚bc1x,# of the view range to not truncate the lineÙ±‚`a
Ù±‚`h        Ù±‚`dmaskÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`hconvolveÙ±‚`a(Ù±‚`a[Ù±‚bmia1Ù±‚`a,Ù±‚`a Ù±‚bmia1Ù±‚`a,Ù±‚`a Ù±‚bmia1Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`dmaskÙ±‚`a,Ù±‚`a Ù±‚`dmodeÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1dsameÙ±‚bs1a'Ù±‚`a)Ù±‚aoa.Ù±‚`fastypeÙ±‚`a(Ù±‚bnbdboolÙ±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚bc1x"# sort out how many points to dropÙ±‚`a
Ù±‚`h        Ù±‚`eratioÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bnbcmaxÙ±‚`a(Ù±‚`bnpÙ±‚aoa.Ù±‚`csumÙ±‚`a(Ù±‚`dmaskÙ±‚`a)Ù±‚`a Ù±‚aoa/Ù±‚aoa/Ù±‚`a Ù±‚bbpdselfÙ±‚aoa.Ù±‚`jmax_pointsÙ±‚`a,Ù±‚`a Ù±‚bmia1Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`h        Ù±‚bc1k# mask dataÙ±‚`a
Ù±‚`h        Ù±‚`exdataÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bbpdselfÙ±‚aoa.Ù±‚`iorigXDataÙ±‚`a[Ù±‚`dmaskÙ±‚`a]Ù±‚`a
Ù±‚`h        Ù±‚`eydataÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bbpdselfÙ±‚aoa.Ù±‚`iorigYDataÙ±‚`a[Ù±‚`dmaskÙ±‚`a]Ù±‚`a
Ù±‚`a
Ù±‚`h        Ù±‚bc1q# downsample dataÙ±‚`a
Ù±‚`h        Ù±‚`exdataÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`exdataÙ±‚`a[Ù±‚`a:Ù±‚`a:Ù±‚`eratioÙ±‚`a]Ù±‚`a
Ù±‚`h        Ù±‚`eydataÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`eydataÙ±‚`a[Ù±‚`a:Ù±‚`a:Ù±‚`eratioÙ±‚`a]Ù±‚`a
Ù±‚`a
Ù±‚`h        Ù±‚bnbeprintÙ±‚`a(Ù±‚bs2a"Ù±‚bs2fusing Ù±‚bsib{}Ù±‚bs2d of Ù±‚bsib{}Ù±‚bs2o visible pointsÙ±‚bs2a"Ù±‚aoa.Ù±‚`fformatÙ±‚`a(Ù±‚bnbclenÙ±‚`a(Ù±‚`eydataÙ±‚`a)Ù±‚`a,Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`csumÙ±‚`a(Ù±‚`dmaskÙ±‚`a)Ù±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`h        Ù±‚akfreturnÙ±‚`a Ù±‚`exdataÙ±‚`a,Ù±‚`a Ù±‚`eydataÙ±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚akcdefÙ±‚`a Ù±‚bnffupdateÙ±‚`a(Ù±‚bbpdselfÙ±‚`a,Ù±‚`a Ù±‚`baxÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`h        Ù±‚bc1q# Update the lineÙ±‚`a
Ù±‚`h        Ù±‚`dlimsÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`baxÙ±‚aoa.Ù±‚`gviewLimÙ±‚`a
Ù±‚`h        Ù±‚akbifÙ±‚`a Ù±‚bnbcabsÙ±‚`a(Ù±‚`dlimsÙ±‚aoa.Ù±‚`ewidthÙ±‚`a Ù±‚aoa-Ù±‚`a Ù±‚bbpdselfÙ±‚aoa.Ù±‚`edeltaÙ±‚`a)Ù±‚`a Ù±‚aoa>Ù±‚`a Ù±‚bmfd1e-8Ù±‚`a:Ù±‚`a
Ù±‚`l            Ù±‚bbpdselfÙ±‚aoa.Ù±‚`edeltaÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`dlimsÙ±‚aoa.Ù±‚`ewidthÙ±‚`a
Ù±‚`l            Ù±‚`fxstartÙ±‚`a,Ù±‚`a Ù±‚`dxendÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`dlimsÙ±‚aoa.Ù±‚`iintervalxÙ±‚`a
Ù±‚`l            Ù±‚bbpdselfÙ±‚aoa.Ù±‚`dlineÙ±‚aoa.Ù±‚`hset_dataÙ±‚`a(Ù±‚aoa*Ù±‚bbpdselfÙ±‚aoa.Ù±‚`jdownsampleÙ±‚`a(Ù±‚`fxstartÙ±‚`a,Ù±‚`a Ù±‚`dxendÙ±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`l            Ù±‚`baxÙ±‚aoa.Ù±‚`ffigureÙ±‚aoa.Ù±‚`fcanvasÙ±‚aoa.Ù±‚`idraw_idleÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚bc1q# Create a signalÙ±‚`a
Ù±‚`exdataÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`hlinspaceÙ±‚`a(Ù±‚bmib16Ù±‚`a,Ù±‚`a Ù±‚bmic365Ù±‚`a,Ù±‚`a Ù±‚`a(Ù±‚bmic365Ù±‚aoa-Ù±‚bmib16Ù±‚`a)Ù±‚aoa*Ù±‚bmia4Ù±‚`a)Ù±‚`a
Ù±‚`eydataÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`csinÙ±‚`a(Ù±‚bmia2Ù±‚aoa*Ù±‚`bnpÙ±‚aoa.Ù±‚`bpiÙ±‚aoa*Ù±‚`exdataÙ±‚aoa/Ù±‚bmic153Ù±‚`a)Ù±‚`a Ù±‚aoa+Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`ccosÙ±‚`a(Ù±‚bmia2Ù±‚aoa*Ù±‚`bnpÙ±‚aoa.Ù±‚`bpiÙ±‚aoa*Ù±‚`exdataÙ±‚aoa/Ù±‚bmic127Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`adÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`vDataDisplayDownsamplerÙ±‚`a(Ù±‚`exdataÙ±‚`a,Ù±‚`a Ù±‚`eydataÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`cfigÙ±‚`a,Ù±‚`a Ù±‚`baxÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cpltÙ±‚aoa.Ù±‚`hsubplotsÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚bc1r# Hook up the lineÙ±‚`a
Ù±‚`adÙ±‚aoa.Ù±‚`dlineÙ±‚`a,Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`baxÙ±‚aoa.Ù±‚`dplotÙ±‚`a(Ù±‚`exdataÙ±‚`a,Ù±‚`a Ù±‚`eydataÙ±‚`a,Ù±‚`a Ù±‚bs1a'Ù±‚bs1bo-Ù±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`pset_autoscale_onÙ±‚`a(Ù±‚bkceFalseÙ±‚`a)Ù±‚`b  Ù±‚bc1x# Otherwise, infinite loopÙ±‚`a
Ù±‚`a
Ù±‚bc1x&# Connect for changing the view limitsÙ±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`icallbacksÙ±‚aoa.Ù±‚`gconnectÙ±‚`a(Ù±‚bs1a'Ù±‚bs1lxlim_changedÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`adÙ±‚aoa.Ù±‚`fupdateÙ±‚`a)Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`hset_xlimÙ±‚`a(Ù±‚bmib16Ù±‚`a,Ù±‚`a Ù±‚bmic365Ù±‚`a)Ù±‚`a
Ù±‚`cpltÙ±‚aoa.Ù±‚`dshowÙ±‚`a(Ù±‚`a)Ù±‚`a
`dNoneö