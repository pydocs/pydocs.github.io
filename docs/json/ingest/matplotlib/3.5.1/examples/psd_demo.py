Ù¯‚Ù´ƒ™»Ù±‚bsdy'"""
========
Psd Demo
========

Plotting Power Spectral Density (PSD) in Matplotlib.

The PSD is a common plot in the field of signal processing. NumPy has
many useful libraries for computing a PSD. Below we demo a few examples
of how this can be accomplished and visualized with Matplotlib.
"""Ù±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnnfpyplotÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnncpltÙ±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„enumpyÙ „enumpyf1.22.3fmoduleenumpyfmoduleõÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnnbnpÙ±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnndmlabÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnndmlabÙ±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnnhgridspecÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnnhgridspecÙ±‚`a
Ù±‚`a
Ù±‚bc1x)# Fixing random state for reproducibilityÙ±‚`a
Ù±‚`bnpÙ±‚aoa.Ù±‚`frandomÙ±‚aoa.Ù±‚`dseedÙ±‚`a(Ù±‚bmih19680801Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`bdtÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bmfd0.01Ù±‚`a
Ù±‚`atÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`farangeÙ±‚`a(Ù±‚bmia0Ù±‚`a,Ù±‚`a Ù±‚bmib10Ù±‚`a,Ù±‚`a Ù±‚`bdtÙ±‚`a)Ù±‚`a
Ù±‚`cnseÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`frandomÙ±‚aoa.Ù±‚`erandnÙ±‚`a(Ù±‚bnbclenÙ±‚`a(Ù±‚`atÙ±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`arÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`cexpÙ±‚`a(Ù±‚aoa-Ù±‚`atÙ±‚`a Ù±‚aoa/Ù±‚`a Ù±‚bmfd0.05Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`dcnseÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`hconvolveÙ±‚`a(Ù±‚`cnseÙ±‚`a,Ù±‚`a Ù±‚`arÙ±‚`a)Ù±‚`a Ù±‚aoa*Ù±‚`a Ù±‚`bdtÙ±‚`a
Ù±‚`dcnseÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`dcnseÙ±‚`a[Ù±‚`a:Ù±‚bnbclenÙ±‚`a(Ù±‚`atÙ±‚`a)Ù±‚`a]Ù±‚`a
Ù±‚`asÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bmfc0.1Ù±‚`a Ù±‚aoa*Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`csinÙ±‚`a(Ù±‚bmia2Ù±‚`a Ù±‚aoa*Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`bpiÙ±‚`a Ù±‚aoa*Ù±‚`a Ù±‚`atÙ±‚`a)Ù±‚`a Ù±‚aoa+Ù±‚`a Ù±‚`dcnseÙ±‚`a
Ù±‚`a
Ù±‚`cfigÙ±‚`a,Ù±‚`a Ù±‚`a(Ù±‚`cax0Ù±‚`a,Ù±‚`a Ù±‚`cax1Ù±‚`a)Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cpltÙ±‚aoa.Ù±‚`hsubplotsÙ±‚`a(Ù±‚bmia2Ù±‚`a,Ù±‚`a Ù±‚bmia1Ù±‚`a)Ù±‚`a
Ù±‚`cax0Ù±‚aoa.Ù±‚`dplotÙ±‚`a(Ù±‚`atÙ±‚`a,Ù±‚`a Ù±‚`asÙ±‚`a)Ù±‚`a
Ù±‚`cax1Ù±‚aoa.Ù±‚`cpsdÙ±‚`a(Ù±‚`asÙ±‚`a,Ù±‚`a Ù±‚bmic512Ù±‚`a,Ù±‚`a Ù±‚bmia1Ù±‚`a Ù±‚aoa/Ù±‚`a Ù±‚`bdtÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`cpltÙ±‚aoa.Ù±‚`dshowÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚bc1xO###############################################################################Ù±‚`a
Ù±‚bc1xM# Compare this with the equivalent Matlab code to accomplish the same thing::Ù±‚`a
Ù±‚bc1a#Ù±‚`a
Ù±‚bc1p#     dt = 0.01;Ù±‚`a
Ù±‚bc1t#     t = [0:dt:10];Ù±‚`a
Ù±‚bc1x#     nse = randn(size(t));Ù±‚`a
Ù±‚bc1w#     r = exp(-t/0.05);Ù±‚`a
Ù±‚bc1x#     cnse = conv(nse, r)*dt;Ù±‚`a
Ù±‚bc1x#     cnse = cnse(1:length(t));Ù±‚`a
Ù±‚bc1x!#     s = 0.1*sin(2*pi*t) + cnse;Ù±‚`a
Ù±‚bc1a#Ù±‚`a
Ù±‚bc1r#     subplot(211)Ù±‚`a
Ù±‚bc1p#     plot(t, s)Ù±‚`a
Ù±‚bc1r#     subplot(212)Ù±‚`a
Ù±‚bc1w#     psd(s, 512, 1/dt)Ù±‚`a
Ù±‚bc1a#Ù±‚`a
Ù±‚bc1xD# Below we'll show a slightly more complex example that demonstratesÙ±‚`a
Ù±‚bc1x(# how padding affects the resulting PSD.Ù±‚`a
Ù±‚`a
Ù±‚`bdtÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`bpiÙ±‚`a Ù±‚aoa/Ù±‚`a Ù±‚bmfd100.Ù±‚`a
Ù±‚`bfsÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bmfb1.Ù±‚`a Ù±‚aoa/Ù±‚`a Ù±‚`bdtÙ±‚`a
Ù±‚`atÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`farangeÙ±‚`a(Ù±‚bmia0Ù±‚`a,Ù±‚`a Ù±‚bmia8Ù±‚`a,Ù±‚`a Ù±‚`bdtÙ±‚`a)Ù±‚`a
Ù±‚`ayÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bmfc10.Ù±‚`a Ù±‚aoa*Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`csinÙ±‚`a(Ù±‚bmia2Ù±‚`a Ù±‚aoa*Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`bpiÙ±‚`a Ù±‚aoa*Ù±‚`a Ù±‚bmia4Ù±‚`a Ù±‚aoa*Ù±‚`a Ù±‚`atÙ±‚`a)Ù±‚`a Ù±‚aoa+Ù±‚`a Ù±‚bmfb5.Ù±‚`a Ù±‚aoa*Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`csinÙ±‚`a(Ù±‚bmia2Ù±‚`a Ù±‚aoa*Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`bpiÙ±‚`a Ù±‚aoa*Ù±‚`a Ù±‚bmfd4.25Ù±‚`a Ù±‚aoa*Ù±‚`a Ù±‚`atÙ±‚`a)Ù±‚`a
Ù±‚`ayÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`ayÙ±‚`a Ù±‚aoa+Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`frandomÙ±‚aoa.Ù±‚`erandnÙ±‚`a(Ù±‚aoa*Ù±‚`atÙ±‚aoa.Ù±‚`eshapeÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚bc1x# Plot the raw time seriesÙ±‚`a
Ù±‚`cfigÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cpltÙ±‚aoa.Ù±‚`ffigureÙ±‚`a(Ù±‚`rconstrained_layoutÙ±‚aoa=Ù±‚bkcdTrueÙ±‚`a)Ù±‚`a
Ù±‚`bgsÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`hgridspecÙ±‚aoa.Ù±‚`hGridSpecÙ±‚`a(Ù±‚bmia2Ù±‚`a,Ù±‚`a Ù±‚bmia3Ù±‚`a,Ù±‚`a Ù±‚`ffigureÙ±‚aoa=Ù±‚`cfigÙ±‚`a)Ù±‚`a
Ù±‚`baxÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cfigÙ±‚aoa.Ù±‚`kadd_subplotÙ±‚`a(Ù±‚`bgsÙ±‚`a[Ù±‚bmia0Ù±‚`a,Ù±‚`a Ù±‚`a:Ù±‚`a]Ù±‚`a)Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`dplotÙ±‚`a(Ù±‚`atÙ±‚`a,Ù±‚`a Ù±‚`ayÙ±‚`a)Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`jset_xlabelÙ±‚`a(Ù±‚bs1a'Ù±‚bs1htime [s]Ù±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`jset_ylabelÙ±‚`a(Ù±‚bs1a'Ù±‚bs1fsignalÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚bc1xK# Plot the PSD with different amounts of zero padding. This uses the entireÙ±‚`a
Ù±‚bc1u# time series at onceÙ±‚`a
Ù±‚`cax2Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cfigÙ±‚aoa.Ù±‚`kadd_subplotÙ±‚`a(Ù±‚`bgsÙ±‚`a[Ù±‚bmia1Ù±‚`a,Ù±‚`a Ù±‚bmia0Ù±‚`a]Ù±‚`a)Ù±‚`a
Ù±‚`cax2Ù±‚aoa.Ù±‚`cpsdÙ±‚`a(Ù±‚`ayÙ±‚`a,Ù±‚`a Ù±‚`dNFFTÙ±‚aoa=Ù±‚bnbclenÙ±‚`a(Ù±‚`atÙ±‚`a)Ù±‚`a,Ù±‚`a Ù±‚`fpad_toÙ±‚aoa=Ù±‚bnbclenÙ±‚`a(Ù±‚`atÙ±‚`a)Ù±‚`a,Ù±‚`a Ù±‚`bFsÙ±‚aoa=Ù±‚`bfsÙ±‚`a)Ù±‚`a
Ù±‚`cax2Ù±‚aoa.Ù±‚`cpsdÙ±‚`a(Ù±‚`ayÙ±‚`a,Ù±‚`a Ù±‚`dNFFTÙ±‚aoa=Ù±‚bnbclenÙ±‚`a(Ù±‚`atÙ±‚`a)Ù±‚`a,Ù±‚`a Ù±‚`fpad_toÙ±‚aoa=Ù±‚bnbclenÙ±‚`a(Ù±‚`atÙ±‚`a)Ù±‚`a Ù±‚aoa*Ù±‚`a Ù±‚bmia2Ù±‚`a,Ù±‚`a Ù±‚`bFsÙ±‚aoa=Ù±‚`bfsÙ±‚`a)Ù±‚`a
Ù±‚`cax2Ù±‚aoa.Ù±‚`cpsdÙ±‚`a(Ù±‚`ayÙ±‚`a,Ù±‚`a Ù±‚`dNFFTÙ±‚aoa=Ù±‚bnbclenÙ±‚`a(Ù±‚`atÙ±‚`a)Ù±‚`a,Ù±‚`a Ù±‚`fpad_toÙ±‚aoa=Ù±‚bnbclenÙ±‚`a(Ù±‚`atÙ±‚`a)Ù±‚`a Ù±‚aoa*Ù±‚`a Ù±‚bmia4Ù±‚`a,Ù±‚`a Ù±‚`bFsÙ±‚aoa=Ù±‚`bfsÙ±‚`a)Ù±‚`a
Ù±‚`cax2Ù±‚aoa.Ù±‚`iset_titleÙ±‚`a(Ù±‚bs1a'Ù±‚bs1lzero paddingÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚bc1xH# Plot the PSD with different block sizes, Zero pad to the length of theÙ±‚`a
Ù±‚bc1x# original data sequence.Ù±‚`a
Ù±‚`cax3Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cfigÙ±‚aoa.Ù±‚`kadd_subplotÙ±‚`a(Ù±‚`bgsÙ±‚`a[Ù±‚bmia1Ù±‚`a,Ù±‚`a Ù±‚bmia1Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`fsharexÙ±‚aoa=Ù±‚`cax2Ù±‚`a,Ù±‚`a Ù±‚`fshareyÙ±‚aoa=Ù±‚`cax2Ù±‚`a)Ù±‚`a
Ù±‚`cax3Ù±‚aoa.Ù±‚`cpsdÙ±‚`a(Ù±‚`ayÙ±‚`a,Ù±‚`a Ù±‚`dNFFTÙ±‚aoa=Ù±‚bnbclenÙ±‚`a(Ù±‚`atÙ±‚`a)Ù±‚`a,Ù±‚`a Ù±‚`fpad_toÙ±‚aoa=Ù±‚bnbclenÙ±‚`a(Ù±‚`atÙ±‚`a)Ù±‚`a,Ù±‚`a Ù±‚`bFsÙ±‚aoa=Ù±‚`bfsÙ±‚`a)Ù±‚`a
Ù±‚`cax3Ù±‚aoa.Ù±‚`cpsdÙ±‚`a(Ù±‚`ayÙ±‚`a,Ù±‚`a Ù±‚`dNFFTÙ±‚aoa=Ù±‚bnbclenÙ±‚`a(Ù±‚`atÙ±‚`a)Ù±‚`a Ù±‚aoa/Ù±‚aoa/Ù±‚`a Ù±‚bmia2Ù±‚`a,Ù±‚`a Ù±‚`fpad_toÙ±‚aoa=Ù±‚bnbclenÙ±‚`a(Ù±‚`atÙ±‚`a)Ù±‚`a,Ù±‚`a Ù±‚`bFsÙ±‚aoa=Ù±‚`bfsÙ±‚`a)Ù±‚`a
Ù±‚`cax3Ù±‚aoa.Ù±‚`cpsdÙ±‚`a(Ù±‚`ayÙ±‚`a,Ù±‚`a Ù±‚`dNFFTÙ±‚aoa=Ù±‚bnbclenÙ±‚`a(Ù±‚`atÙ±‚`a)Ù±‚`a Ù±‚aoa/Ù±‚aoa/Ù±‚`a Ù±‚bmia4Ù±‚`a,Ù±‚`a Ù±‚`fpad_toÙ±‚aoa=Ù±‚bnbclenÙ±‚`a(Ù±‚`atÙ±‚`a)Ù±‚`a,Ù±‚`a Ù±‚`bFsÙ±‚aoa=Ù±‚`bfsÙ±‚`a)Ù±‚`a
Ù±‚`cax3Ù±‚aoa.Ù±‚`jset_ylabelÙ±‚`a(Ù±‚bs1a'Ù±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`cax3Ù±‚aoa.Ù±‚`iset_titleÙ±‚`a(Ù±‚bs1a'Ù±‚bs1jblock sizeÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚bc1x?# Plot the PSD with different amounts of overlap between blocksÙ±‚`a
Ù±‚`cax4Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cfigÙ±‚aoa.Ù±‚`kadd_subplotÙ±‚`a(Ù±‚`bgsÙ±‚`a[Ù±‚bmia1Ù±‚`a,Ù±‚`a Ù±‚bmia2Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`fsharexÙ±‚aoa=Ù±‚`cax2Ù±‚`a,Ù±‚`a Ù±‚`fshareyÙ±‚aoa=Ù±‚`cax2Ù±‚`a)Ù±‚`a
Ù±‚`cax4Ù±‚aoa.Ù±‚`cpsdÙ±‚`a(Ù±‚`ayÙ±‚`a,Ù±‚`a Ù±‚`dNFFTÙ±‚aoa=Ù±‚bnbclenÙ±‚`a(Ù±‚`atÙ±‚`a)Ù±‚`a Ù±‚aoa/Ù±‚aoa/Ù±‚`a Ù±‚bmia2Ù±‚`a,Ù±‚`a Ù±‚`fpad_toÙ±‚aoa=Ù±‚bnbclenÙ±‚`a(Ù±‚`atÙ±‚`a)Ù±‚`a,Ù±‚`a Ù±‚`hnoverlapÙ±‚aoa=Ù±‚bmia0Ù±‚`a,Ù±‚`a Ù±‚`bFsÙ±‚aoa=Ù±‚`bfsÙ±‚`a)Ù±‚`a
Ù±‚`cax4Ù±‚aoa.Ù±‚`cpsdÙ±‚`a(Ù±‚`ayÙ±‚`a,Ù±‚`a Ù±‚`dNFFTÙ±‚aoa=Ù±‚bnbclenÙ±‚`a(Ù±‚`atÙ±‚`a)Ù±‚`a Ù±‚aoa/Ù±‚aoa/Ù±‚`a Ù±‚bmia2Ù±‚`a,Ù±‚`a Ù±‚`fpad_toÙ±‚aoa=Ù±‚bnbclenÙ±‚`a(Ù±‚`atÙ±‚`a)Ù±‚`a,Ù±‚`a
Ù±‚`h        Ù±‚`hnoverlapÙ±‚aoa=Ù±‚bnbcintÙ±‚`a(Ù±‚bmfd0.05Ù±‚`a Ù±‚aoa*Ù±‚`a Ù±‚bnbclenÙ±‚`a(Ù±‚`atÙ±‚`a)Ù±‚`a Ù±‚aoa/Ù±‚`a Ù±‚bmfb2.Ù±‚`a)Ù±‚`a,Ù±‚`a Ù±‚`bFsÙ±‚aoa=Ù±‚`bfsÙ±‚`a)Ù±‚`a
Ù±‚`cax4Ù±‚aoa.Ù±‚`cpsdÙ±‚`a(Ù±‚`ayÙ±‚`a,Ù±‚`a Ù±‚`dNFFTÙ±‚aoa=Ù±‚bnbclenÙ±‚`a(Ù±‚`atÙ±‚`a)Ù±‚`a Ù±‚aoa/Ù±‚aoa/Ù±‚`a Ù±‚bmia2Ù±‚`a,Ù±‚`a Ù±‚`fpad_toÙ±‚aoa=Ù±‚bnbclenÙ±‚`a(Ù±‚`atÙ±‚`a)Ù±‚`a,Ù±‚`a
Ù±‚`h        Ù±‚`hnoverlapÙ±‚aoa=Ù±‚bnbcintÙ±‚`a(Ù±‚bmfc0.2Ù±‚`a Ù±‚aoa*Ù±‚`a Ù±‚bnbclenÙ±‚`a(Ù±‚`atÙ±‚`a)Ù±‚`a Ù±‚aoa/Ù±‚`a Ù±‚bmfb2.Ù±‚`a)Ù±‚`a,Ù±‚`a Ù±‚`bFsÙ±‚aoa=Ù±‚`bfsÙ±‚`a)Ù±‚`a
Ù±‚`cax4Ù±‚aoa.Ù±‚`jset_ylabelÙ±‚`a(Ù±‚bs1a'Ù±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`cax4Ù±‚aoa.Ù±‚`iset_titleÙ±‚`a(Ù±‚bs1a'Ù±‚bs1goverlapÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`cpltÙ±‚aoa.Ù±‚`dshowÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚bc1xO###############################################################################Ù±‚`a
Ù±‚bc1x># This is a ported version of a MATLAB example from the signalÙ±‚`a
Ù±‚bc1xD# processing toolbox that showed some difference at one time betweenÙ±‚`a
Ù±‚bc1x/# Matplotlib's and MATLAB's scaling of the PSD.Ù±‚`a
Ù±‚`a
Ù±‚`bfsÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bmid1000Ù±‚`a
Ù±‚`atÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`hlinspaceÙ±‚`a(Ù±‚bmia0Ù±‚`a,Ù±‚`a Ù±‚bmfc0.3Ù±‚`a,Ù±‚`a Ù±‚bmic301Ù±‚`a)Ù±‚`a
Ù±‚`aAÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`earrayÙ±‚`a(Ù±‚`a[Ù±‚bmia2Ù±‚`a,Ù±‚`a Ù±‚bmia8Ù±‚`a]Ù±‚`a)Ù±‚aoa.Ù±‚`greshapeÙ±‚`a(Ù±‚aoa-Ù±‚bmia1Ù±‚`a,Ù±‚`a Ù±‚bmia1Ù±‚`a)Ù±‚`a
Ù±‚`afÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`earrayÙ±‚`a(Ù±‚`a[Ù±‚bmic150Ù±‚`a,Ù±‚`a Ù±‚bmic140Ù±‚`a]Ù±‚`a)Ù±‚aoa.Ù±‚`greshapeÙ±‚`a(Ù±‚aoa-Ù±‚bmia1Ù±‚`a,Ù±‚`a Ù±‚bmia1Ù±‚`a)Ù±‚`a
Ù±‚`bxnÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`a(Ù±‚`aAÙ±‚`a Ù±‚aoa*Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`csinÙ±‚`a(Ù±‚bmia2Ù±‚`a Ù±‚aoa*Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`bpiÙ±‚`a Ù±‚aoa*Ù±‚`a Ù±‚`afÙ±‚`a Ù±‚aoa*Ù±‚`a Ù±‚`atÙ±‚`a)Ù±‚`a)Ù±‚aoa.Ù±‚`csumÙ±‚`a(Ù±‚`daxisÙ±‚aoa=Ù±‚bmia0Ù±‚`a)Ù±‚`a
Ù±‚`bxnÙ±‚`a Ù±‚aoa+Ù±‚aoa=Ù±‚`a Ù±‚bmia5Ù±‚`a Ù±‚aoa*Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`frandomÙ±‚aoa.Ù±‚`erandnÙ±‚`a(Ù±‚aoa*Ù±‚`atÙ±‚aoa.Ù±‚`eshapeÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`cfigÙ±‚`a,Ù±‚`a Ù±‚`a(Ù±‚`cax0Ù±‚`a,Ù±‚`a Ù±‚`cax1Ù±‚`a)Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cpltÙ±‚aoa.Ù±‚`hsubplotsÙ±‚`a(Ù±‚`encolsÙ±‚aoa=Ù±‚bmia2Ù±‚`a,Ù±‚`a Ù±‚`rconstrained_layoutÙ±‚aoa=Ù±‚bkcdTrueÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`fyticksÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`farangeÙ±‚`a(Ù±‚aoa-Ù±‚bmib50Ù±‚`a,Ù±‚`a Ù±‚bmib30Ù±‚`a,Ù±‚`a Ù±‚bmib10Ù±‚`a)Ù±‚`a
Ù±‚`fyrangeÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`a(Ù±‚`fyticksÙ±‚`a[Ù±‚bmia0Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`fyticksÙ±‚`a[Ù±‚aoa-Ù±‚bmia1Ù±‚`a]Ù±‚`a)Ù±‚`a
Ù±‚`fxticksÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`farangeÙ±‚`a(Ù±‚bmia0Ù±‚`a,Ù±‚`a Ù±‚bmic550Ù±‚`a,Ù±‚`a Ù±‚bmic100Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`cax0Ù±‚aoa.Ù±‚`cpsdÙ±‚`a(Ù±‚`bxnÙ±‚`a,Ù±‚`a Ù±‚`dNFFTÙ±‚aoa=Ù±‚bmic301Ù±‚`a,Ù±‚`a Ù±‚`bFsÙ±‚aoa=Ù±‚`bfsÙ±‚`a,Ù±‚`a Ù±‚`fwindowÙ±‚aoa=Ù±‚`dmlabÙ±‚aoa.Ù±‚`kwindow_noneÙ±‚`a,Ù±‚`a Ù±‚`fpad_toÙ±‚aoa=Ù±‚bmid1024Ù±‚`a,Ù±‚`a
Ù±‚`h        Ù±‚`mscale_by_freqÙ±‚aoa=Ù±‚bkcdTrueÙ±‚`a)Ù±‚`a
Ù±‚`cax0Ù±‚aoa.Ù±‚`iset_titleÙ±‚`a(Ù±‚bs1a'Ù±‚bs1kPeriodogramÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`cax0Ù±‚aoa.Ù±‚`jset_yticksÙ±‚`a(Ù±‚`fyticksÙ±‚`a)Ù±‚`a
Ù±‚`cax0Ù±‚aoa.Ù±‚`jset_xticksÙ±‚`a(Ù±‚`fxticksÙ±‚`a)Ù±‚`a
Ù±‚`cax0Ù±‚aoa.Ù±‚`dgridÙ±‚`a(Ù±‚bkcdTrueÙ±‚`a)Ù±‚`a
Ù±‚`cax0Ù±‚aoa.Ù±‚`hset_ylimÙ±‚`a(Ù±‚`fyrangeÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`cax1Ù±‚aoa.Ù±‚`cpsdÙ±‚`a(Ù±‚`bxnÙ±‚`a,Ù±‚`a Ù±‚`dNFFTÙ±‚aoa=Ù±‚bmic150Ù±‚`a,Ù±‚`a Ù±‚`bFsÙ±‚aoa=Ù±‚`bfsÙ±‚`a,Ù±‚`a Ù±‚`fwindowÙ±‚aoa=Ù±‚`dmlabÙ±‚aoa.Ù±‚`kwindow_noneÙ±‚`a,Ù±‚`a Ù±‚`fpad_toÙ±‚aoa=Ù±‚bmic512Ù±‚`a,Ù±‚`a Ù±‚`hnoverlapÙ±‚aoa=Ù±‚bmib75Ù±‚`a,Ù±‚`a
Ù±‚`h        Ù±‚`mscale_by_freqÙ±‚aoa=Ù±‚bkcdTrueÙ±‚`a)Ù±‚`a
Ù±‚`cax1Ù±‚aoa.Ù±‚`iset_titleÙ±‚`a(Ù±‚bs1a'Ù±‚bs1eWelchÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`cax1Ù±‚aoa.Ù±‚`jset_xticksÙ±‚`a(Ù±‚`fxticksÙ±‚`a)Ù±‚`a
Ù±‚`cax1Ù±‚aoa.Ù±‚`jset_yticksÙ±‚`a(Ù±‚`fyticksÙ±‚`a)Ù±‚`a
Ù±‚`cax1Ù±‚aoa.Ù±‚`jset_ylabelÙ±‚`a(Ù±‚bs1a'Ù±‚bs1a'Ù±‚`a)Ù±‚`b  Ù±‚bc1x&# overwrite the y-label added by `psd`Ù±‚`a
Ù±‚`cax1Ù±‚aoa.Ù±‚`dgridÙ±‚`a(Ù±‚bkcdTrueÙ±‚`a)Ù±‚`a
Ù±‚`cax1Ù±‚aoa.Ù±‚`hset_ylimÙ±‚`a(Ù±‚`fyrangeÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`cpltÙ±‚aoa.Ù±‚`dshowÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚bc1xO###############################################################################Ù±‚`a
Ù±‚bc1x># This is a ported version of a MATLAB example from the signalÙ±‚`a
Ù±‚bc1xD# processing toolbox that showed some difference at one time betweenÙ±‚`a
Ù±‚bc1x/# Matplotlib's and MATLAB's scaling of the PSD.Ù±‚`a
Ù±‚bc1a#Ù±‚`a
Ù±‚bc1xJ# It uses a complex signal so we can see that complex PSD's work properly.Ù±‚`a
Ù±‚`a
Ù±‚`dprngÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`frandomÙ±‚aoa.Ù±‚`kRandomStateÙ±‚`a(Ù±‚bmih19680801Ù±‚`a)Ù±‚`b  Ù±‚bc1x# to ensure reproducibilityÙ±‚`a
Ù±‚`a
Ù±‚`bfsÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bmid1000Ù±‚`a
Ù±‚`atÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`hlinspaceÙ±‚`a(Ù±‚bmia0Ù±‚`a,Ù±‚`a Ù±‚bmfc0.3Ù±‚`a,Ù±‚`a Ù±‚bmic301Ù±‚`a)Ù±‚`a
Ù±‚`aAÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`earrayÙ±‚`a(Ù±‚`a[Ù±‚bmia2Ù±‚`a,Ù±‚`a Ù±‚bmia8Ù±‚`a]Ù±‚`a)Ù±‚aoa.Ù±‚`greshapeÙ±‚`a(Ù±‚aoa-Ù±‚bmia1Ù±‚`a,Ù±‚`a Ù±‚bmia1Ù±‚`a)Ù±‚`a
Ù±‚`afÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`earrayÙ±‚`a(Ù±‚`a[Ù±‚bmic150Ù±‚`a,Ù±‚`a Ù±‚bmic140Ù±‚`a]Ù±‚`a)Ù±‚aoa.Ù±‚`greshapeÙ±‚`a(Ù±‚aoa-Ù±‚bmia1Ù±‚`a,Ù±‚`a Ù±‚bmia1Ù±‚`a)Ù±‚`a
Ù±‚`bxnÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`a(Ù±‚`aAÙ±‚`a Ù±‚aoa*Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`cexpÙ±‚`a(Ù±‚bmia2Ù±‚`ajÙ±‚`a Ù±‚aoa*Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`bpiÙ±‚`a Ù±‚aoa*Ù±‚`a Ù±‚`afÙ±‚`a Ù±‚aoa*Ù±‚`a Ù±‚`atÙ±‚`a)Ù±‚`a)Ù±‚aoa.Ù±‚`csumÙ±‚`a(Ù±‚`daxisÙ±‚aoa=Ù±‚bmia0Ù±‚`a)Ù±‚`a Ù±‚aoa+Ù±‚`a Ù±‚bmia5Ù±‚`a Ù±‚aoa*Ù±‚`a Ù±‚`dprngÙ±‚aoa.Ù±‚`erandnÙ±‚`a(Ù±‚aoa*Ù±‚`atÙ±‚aoa.Ù±‚`eshapeÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`cfigÙ±‚`a,Ù±‚`a Ù±‚`a(Ù±‚`cax0Ù±‚`a,Ù±‚`a Ù±‚`cax1Ù±‚`a)Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cpltÙ±‚aoa.Ù±‚`hsubplotsÙ±‚`a(Ù±‚`encolsÙ±‚aoa=Ù±‚bmia2Ù±‚`a,Ù±‚`a Ù±‚`rconstrained_layoutÙ±‚aoa=Ù±‚bkcdTrueÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`fyticksÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`farangeÙ±‚`a(Ù±‚aoa-Ù±‚bmib50Ù±‚`a,Ù±‚`a Ù±‚bmib30Ù±‚`a,Ù±‚`a Ù±‚bmib10Ù±‚`a)Ù±‚`a
Ù±‚`fyrangeÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`a(Ù±‚`fyticksÙ±‚`a[Ù±‚bmia0Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`fyticksÙ±‚`a[Ù±‚aoa-Ù±‚bmia1Ù±‚`a]Ù±‚`a)Ù±‚`a
Ù±‚`fxticksÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`farangeÙ±‚`a(Ù±‚aoa-Ù±‚bmic500Ù±‚`a,Ù±‚`a Ù±‚bmic550Ù±‚`a,Ù±‚`a Ù±‚bmic200Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`cax0Ù±‚aoa.Ù±‚`cpsdÙ±‚`a(Ù±‚`bxnÙ±‚`a,Ù±‚`a Ù±‚`dNFFTÙ±‚aoa=Ù±‚bmic301Ù±‚`a,Ù±‚`a Ù±‚`bFsÙ±‚aoa=Ù±‚`bfsÙ±‚`a,Ù±‚`a Ù±‚`fwindowÙ±‚aoa=Ù±‚`dmlabÙ±‚aoa.Ù±‚`kwindow_noneÙ±‚`a,Ù±‚`a Ù±‚`fpad_toÙ±‚aoa=Ù±‚bmid1024Ù±‚`a,Ù±‚`a
Ù±‚`h        Ù±‚`mscale_by_freqÙ±‚aoa=Ù±‚bkcdTrueÙ±‚`a)Ù±‚`a
Ù±‚`cax0Ù±‚aoa.Ù±‚`iset_titleÙ±‚`a(Ù±‚bs1a'Ù±‚bs1kPeriodogramÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`cax0Ù±‚aoa.Ù±‚`jset_yticksÙ±‚`a(Ù±‚`fyticksÙ±‚`a)Ù±‚`a
Ù±‚`cax0Ù±‚aoa.Ù±‚`jset_xticksÙ±‚`a(Ù±‚`fxticksÙ±‚`a)Ù±‚`a
Ù±‚`cax0Ù±‚aoa.Ù±‚`dgridÙ±‚`a(Ù±‚bkcdTrueÙ±‚`a)Ù±‚`a
Ù±‚`cax0Ù±‚aoa.Ù±‚`hset_ylimÙ±‚`a(Ù±‚`fyrangeÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`cax1Ù±‚aoa.Ù±‚`cpsdÙ±‚`a(Ù±‚`bxnÙ±‚`a,Ù±‚`a Ù±‚`dNFFTÙ±‚aoa=Ù±‚bmic150Ù±‚`a,Ù±‚`a Ù±‚`bFsÙ±‚aoa=Ù±‚`bfsÙ±‚`a,Ù±‚`a Ù±‚`fwindowÙ±‚aoa=Ù±‚`dmlabÙ±‚aoa.Ù±‚`kwindow_noneÙ±‚`a,Ù±‚`a Ù±‚`fpad_toÙ±‚aoa=Ù±‚bmic512Ù±‚`a,Ù±‚`a Ù±‚`hnoverlapÙ±‚aoa=Ù±‚bmib75Ù±‚`a,Ù±‚`a
Ù±‚`h        Ù±‚`mscale_by_freqÙ±‚aoa=Ù±‚bkcdTrueÙ±‚`a)Ù±‚`a
Ù±‚`cax1Ù±‚aoa.Ù±‚`iset_titleÙ±‚`a(Ù±‚bs1a'Ù±‚bs1eWelchÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`cax1Ù±‚aoa.Ù±‚`jset_xticksÙ±‚`a(Ù±‚`fxticksÙ±‚`a)Ù±‚`a
Ù±‚`cax1Ù±‚aoa.Ù±‚`jset_yticksÙ±‚`a(Ù±‚`fyticksÙ±‚`a)Ù±‚`a
Ù±‚`cax1Ù±‚aoa.Ù±‚`jset_ylabelÙ±‚`a(Ù±‚bs1a'Ù±‚bs1a'Ù±‚`a)Ù±‚`b  Ù±‚bc1x&# overwrite the y-label added by `psd`Ù±‚`a
Ù±‚`cax1Ù±‚aoa.Ù±‚`dgridÙ±‚`a(Ù±‚bkcdTrueÙ±‚`a)Ù±‚`a
Ù±‚`cax1Ù±‚aoa.Ù±‚`hset_ylimÙ±‚`a(Ù±‚`fyrangeÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`cpltÙ±‚aoa.Ù±‚`dshowÙ±‚`a(Ù±‚`a)Ù±‚`a
`dNoneö