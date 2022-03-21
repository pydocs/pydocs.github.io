Ù¯‚Ù´ƒ™×Ù±‚bsdy"""
========================
Spectrum Representations
========================

The plots show different spectrum representations of a sine signal with
additive noise. A (frequency) spectrum of a discrete-time signal is calculated
by utilizing the fast Fourier transform (FFT).
"""Ù±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnnfpyplotÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnncpltÙ±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„enumpyÙ „enumpyf1.22.3fmoduleenumpyfmoduleõÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnnbnpÙ±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚`bnpÙ±‚aoa.Ù±‚`frandomÙ±‚aoa.Ù±‚`dseedÙ±‚`a(Ù±‚bmia0Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`bdtÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bmfd0.01Ù±‚`b  Ù±‚bc1s# sampling intervalÙ±‚`a
Ù±‚`bFsÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bmia1Ù±‚`a Ù±‚aoa/Ù±‚`a Ù±‚`bdtÙ±‚`b  Ù±‚bc1t# sampling frequencyÙ±‚`a
Ù±‚`atÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`farangeÙ±‚`a(Ù±‚bmia0Ù±‚`a,Ù±‚`a Ù±‚bmib10Ù±‚`a,Ù±‚`a Ù±‚`bdtÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚bc1q# generate noise:Ù±‚`a
Ù±‚`cnseÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`frandomÙ±‚aoa.Ù±‚`erandnÙ±‚`a(Ù±‚bnbclenÙ±‚`a(Ù±‚`atÙ±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`arÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`cexpÙ±‚`a(Ù±‚aoa-Ù±‚`atÙ±‚`a Ù±‚aoa/Ù±‚`a Ù±‚bmfd0.05Ù±‚`a)Ù±‚`a
Ù±‚`dcnseÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`hconvolveÙ±‚`a(Ù±‚`cnseÙ±‚`a,Ù±‚`a Ù±‚`arÙ±‚`a)Ù±‚`a Ù±‚aoa*Ù±‚`a Ù±‚`bdtÙ±‚`a
Ù±‚`dcnseÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`dcnseÙ±‚`a[Ù±‚`a:Ù±‚bnbclenÙ±‚`a(Ù±‚`atÙ±‚`a)Ù±‚`a]Ù±‚`a
Ù±‚`a
Ù±‚`asÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bmfc0.1Ù±‚`a Ù±‚aoa*Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`csinÙ±‚`a(Ù±‚bmia4Ù±‚`a Ù±‚aoa*Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`bpiÙ±‚`a Ù±‚aoa*Ù±‚`a Ù±‚`atÙ±‚`a)Ù±‚`a Ù±‚aoa+Ù±‚`a Ù±‚`dcnseÙ±‚`b  Ù±‚bc1l# the signalÙ±‚`a
Ù±‚`a
Ù±‚`cfigÙ±‚`a,Ù±‚`a Ù±‚`caxsÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cpltÙ±‚aoa.Ù±‚`hsubplotsÙ±‚`a(Ù±‚`enrowsÙ±‚aoa=Ù±‚bmia3Ù±‚`a,Ù±‚`a Ù±‚`encolsÙ±‚aoa=Ù±‚bmia2Ù±‚`a,Ù±‚`a Ù±‚`gfigsizeÙ±‚aoa=Ù±‚`a(Ù±‚bmia7Ù±‚`a,Ù±‚`a Ù±‚bmia7Ù±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚bc1s# plot time signal:Ù±‚`a
Ù±‚`caxsÙ±‚`a[Ù±‚bmia0Ù±‚`a,Ù±‚`a Ù±‚bmia0Ù±‚`a]Ù±‚aoa.Ù±‚`iset_titleÙ±‚`a(Ù±‚bs2a"Ù±‚bs2fSignalÙ±‚bs2a"Ù±‚`a)Ù±‚`a
Ù±‚`caxsÙ±‚`a[Ù±‚bmia0Ù±‚`a,Ù±‚`a Ù±‚bmia0Ù±‚`a]Ù±‚aoa.Ù±‚`dplotÙ±‚`a(Ù±‚`atÙ±‚`a,Ù±‚`a Ù±‚`asÙ±‚`a,Ù±‚`a Ù±‚`ecolorÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1bC0Ù±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`caxsÙ±‚`a[Ù±‚bmia0Ù±‚`a,Ù±‚`a Ù±‚bmia0Ù±‚`a]Ù±‚aoa.Ù±‚`jset_xlabelÙ±‚`a(Ù±‚bs2a"Ù±‚bs2dTimeÙ±‚bs2a"Ù±‚`a)Ù±‚`a
Ù±‚`caxsÙ±‚`a[Ù±‚bmia0Ù±‚`a,Ù±‚`a Ù±‚bmia0Ù±‚`a]Ù±‚aoa.Ù±‚`jset_ylabelÙ±‚`a(Ù±‚bs2a"Ù±‚bs2iAmplitudeÙ±‚bs2a"Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚bc1x # plot different spectrum types:Ù±‚`a
Ù±‚`caxsÙ±‚`a[Ù±‚bmia1Ù±‚`a,Ù±‚`a Ù±‚bmia0Ù±‚`a]Ù±‚aoa.Ù±‚`iset_titleÙ±‚`a(Ù±‚bs2a"Ù±‚bs2rMagnitude SpectrumÙ±‚bs2a"Ù±‚`a)Ù±‚`a
Ù±‚`caxsÙ±‚`a[Ù±‚bmia1Ù±‚`a,Ù±‚`a Ù±‚bmia0Ù±‚`a]Ù±‚aoa.Ù±‚`rmagnitude_spectrumÙ±‚`a(Ù±‚`asÙ±‚`a,Ù±‚`a Ù±‚`bFsÙ±‚aoa=Ù±‚`bFsÙ±‚`a,Ù±‚`a Ù±‚`ecolorÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1bC1Ù±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`caxsÙ±‚`a[Ù±‚bmia1Ù±‚`a,Ù±‚`a Ù±‚bmia1Ù±‚`a]Ù±‚aoa.Ù±‚`iset_titleÙ±‚`a(Ù±‚bs2a"Ù±‚bs2wLog. Magnitude SpectrumÙ±‚bs2a"Ù±‚`a)Ù±‚`a
Ù±‚`caxsÙ±‚`a[Ù±‚bmia1Ù±‚`a,Ù±‚`a Ù±‚bmia1Ù±‚`a]Ù±‚aoa.Ù±‚`rmagnitude_spectrumÙ±‚`a(Ù±‚`asÙ±‚`a,Ù±‚`a Ù±‚`bFsÙ±‚aoa=Ù±‚`bFsÙ±‚`a,Ù±‚`a Ù±‚`escaleÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1bdBÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`ecolorÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1bC1Ù±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`caxsÙ±‚`a[Ù±‚bmia2Ù±‚`a,Ù±‚`a Ù±‚bmia0Ù±‚`a]Ù±‚aoa.Ù±‚`iset_titleÙ±‚`a(Ù±‚bs2a"Ù±‚bs2oPhase Spectrum Ù±‚bs2a"Ù±‚`a)Ù±‚`a
Ù±‚`caxsÙ±‚`a[Ù±‚bmia2Ù±‚`a,Ù±‚`a Ù±‚bmia0Ù±‚`a]Ù±‚aoa.Ù±‚`nphase_spectrumÙ±‚`a(Ù±‚`asÙ±‚`a,Ù±‚`a Ù±‚`bFsÙ±‚aoa=Ù±‚`bFsÙ±‚`a,Ù±‚`a Ù±‚`ecolorÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1bC2Ù±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`caxsÙ±‚`a[Ù±‚bmia2Ù±‚`a,Ù±‚`a Ù±‚bmia1Ù±‚`a]Ù±‚aoa.Ù±‚`iset_titleÙ±‚`a(Ù±‚bs2a"Ù±‚bs2nAngle SpectrumÙ±‚bs2a"Ù±‚`a)Ù±‚`a
Ù±‚`caxsÙ±‚`a[Ù±‚bmia2Ù±‚`a,Ù±‚`a Ù±‚bmia1Ù±‚`a]Ù±‚aoa.Ù±‚`nangle_spectrumÙ±‚`a(Ù±‚`asÙ±‚`a,Ù±‚`a Ù±‚`bFsÙ±‚aoa=Ù±‚`bFsÙ±‚`a,Ù±‚`a Ù±‚`ecolorÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1bC2Ù±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`caxsÙ±‚`a[Ù±‚bmia0Ù±‚`a,Ù±‚`a Ù±‚bmia1Ù±‚`a]Ù±‚aoa.Ù±‚`fremoveÙ±‚`a(Ù±‚`a)Ù±‚`b  Ù±‚bc1x# don't display empty axÙ±‚`a
Ù±‚`a
Ù±‚`cfigÙ±‚aoa.Ù±‚`ltight_layoutÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`cpltÙ±‚aoa.Ù±‚`dshowÙ±‚`a(Ù±‚`a)Ù±‚`a
`dNoneö