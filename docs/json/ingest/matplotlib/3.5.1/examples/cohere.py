Ù¯‚Ù´ƒ™%Ù±‚bsdx·"""
=====================================
Plotting the coherence of two signals
=====================================

An example showing how to plot the coherence of two signals.
"""Ù±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„enumpyÙ „enumpyf1.22.3fmoduleenumpyfmoduleõÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnnbnpÙ±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnnfpyplotÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnncpltÙ±‚`a
Ù±‚`a
Ù±‚bc1x)# Fixing random state for reproducibilityÙ±‚`a
Ù±‚`bnpÙ±‚aoa.Ù±‚`frandomÙ±‚aoa.Ù±‚`dseedÙ±‚`a(Ù±‚bmih19680801Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`bdtÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bmfd0.01Ù±‚`a
Ù±‚`atÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`farangeÙ±‚`a(Ù±‚bmia0Ù±‚`a,Ù±‚`a Ù±‚bmib30Ù±‚`a,Ù±‚`a Ù±‚`bdtÙ±‚`a)Ù±‚`a
Ù±‚`dnse1Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`frandomÙ±‚aoa.Ù±‚`erandnÙ±‚`a(Ù±‚bnbclenÙ±‚`a(Ù±‚`atÙ±‚`a)Ù±‚`a)Ù±‚`q                 Ù±‚bc1o# white noise 1Ù±‚`a
Ù±‚`dnse2Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`frandomÙ±‚aoa.Ù±‚`erandnÙ±‚`a(Ù±‚bnbclenÙ±‚`a(Ù±‚`atÙ±‚`a)Ù±‚`a)Ù±‚`q                 Ù±‚bc1o# white noise 2Ù±‚`a
Ù±‚`a
Ù±‚bc1x<# Two signals with a coherent part at 10Hz and a random partÙ±‚`a
Ù±‚`bs1Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`csinÙ±‚`a(Ù±‚bmia2Ù±‚`a Ù±‚aoa*Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`bpiÙ±‚`a Ù±‚aoa*Ù±‚`a Ù±‚bmib10Ù±‚`a Ù±‚aoa*Ù±‚`a Ù±‚`atÙ±‚`a)Ù±‚`a Ù±‚aoa+Ù±‚`a Ù±‚`dnse1Ù±‚`a
Ù±‚`bs2Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`csinÙ±‚`a(Ù±‚bmia2Ù±‚`a Ù±‚aoa*Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`bpiÙ±‚`a Ù±‚aoa*Ù±‚`a Ù±‚bmib10Ù±‚`a Ù±‚aoa*Ù±‚`a Ù±‚`atÙ±‚`a)Ù±‚`a Ù±‚aoa+Ù±‚`a Ù±‚`dnse2Ù±‚`a
Ù±‚`a
Ù±‚`cfigÙ±‚`a,Ù±‚`a Ù±‚`caxsÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cpltÙ±‚aoa.Ù±‚`hsubplotsÙ±‚`a(Ù±‚bmia2Ù±‚`a,Ù±‚`a Ù±‚bmia1Ù±‚`a)Ù±‚`a
Ù±‚`caxsÙ±‚`a[Ù±‚bmia0Ù±‚`a]Ù±‚aoa.Ù±‚`dplotÙ±‚`a(Ù±‚`atÙ±‚`a,Ù±‚`a Ù±‚`bs1Ù±‚`a,Ù±‚`a Ù±‚`atÙ±‚`a,Ù±‚`a Ù±‚`bs2Ù±‚`a)Ù±‚`a
Ù±‚`caxsÙ±‚`a[Ù±‚bmia0Ù±‚`a]Ù±‚aoa.Ù±‚`hset_xlimÙ±‚`a(Ù±‚bmia0Ù±‚`a,Ù±‚`a Ù±‚bmia2Ù±‚`a)Ù±‚`a
Ù±‚`caxsÙ±‚`a[Ù±‚bmia0Ù±‚`a]Ù±‚aoa.Ù±‚`jset_xlabelÙ±‚`a(Ù±‚bs1a'Ù±‚bs1dtimeÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`caxsÙ±‚`a[Ù±‚bmia0Ù±‚`a]Ù±‚aoa.Ù±‚`jset_ylabelÙ±‚`a(Ù±‚bs1a'Ù±‚bs1is1 and s2Ù±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`caxsÙ±‚`a[Ù±‚bmia0Ù±‚`a]Ù±‚aoa.Ù±‚`dgridÙ±‚`a(Ù±‚bkcdTrueÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`ccxyÙ±‚`a,Ù±‚`a Ù±‚`afÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`caxsÙ±‚`a[Ù±‚bmia1Ù±‚`a]Ù±‚aoa.Ù±‚`fcohereÙ±‚`a(Ù±‚`bs1Ù±‚`a,Ù±‚`a Ù±‚`bs2Ù±‚`a,Ù±‚`a Ù±‚bmic256Ù±‚`a,Ù±‚`a Ù±‚bmfb1.Ù±‚`a Ù±‚aoa/Ù±‚`a Ù±‚`bdtÙ±‚`a)Ù±‚`a
Ù±‚`caxsÙ±‚`a[Ù±‚bmia1Ù±‚`a]Ù±‚aoa.Ù±‚`jset_ylabelÙ±‚`a(Ù±‚bs1a'Ù±‚bs1icoherenceÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`cfigÙ±‚aoa.Ù±‚`ltight_layoutÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`cpltÙ±‚aoa.Ù±‚`dshowÙ±‚`a(Ù±‚`a)Ù±‚`a
`dNoneö