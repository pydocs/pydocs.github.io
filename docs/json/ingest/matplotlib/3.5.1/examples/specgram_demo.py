Ù¯‚Ù´ƒ™0Ù±‚bsdxp"""
================
Spectrogram Demo
================

Demo of a spectrogram plot (`~.axes.Axes.specgram`).
"""Ù±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnnfpyplotÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnncpltÙ±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„enumpyÙ „enumpyf1.22.3fmoduleenumpyfmoduleõÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnnbnpÙ±‚`a
Ù±‚`a
Ù±‚bc1x)# Fixing random state for reproducibilityÙ±‚`a
Ù±‚`bnpÙ±‚aoa.Ù±‚`frandomÙ±‚aoa.Ù±‚`dseedÙ±‚`a(Ù±‚bmih19680801Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`bdtÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bmff0.0005Ù±‚`a
Ù±‚`atÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`farangeÙ±‚`a(Ù±‚bmfc0.0Ù±‚`a,Ù±‚`a Ù±‚bmfd20.0Ù±‚`a,Ù±‚`a Ù±‚`bdtÙ±‚`a)Ù±‚`a
Ù±‚`bs1Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`csinÙ±‚`a(Ù±‚bmia2Ù±‚`a Ù±‚aoa*Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`bpiÙ±‚`a Ù±‚aoa*Ù±‚`a Ù±‚bmic100Ù±‚`a Ù±‚aoa*Ù±‚`a Ù±‚`atÙ±‚`a)Ù±‚`a
Ù±‚`bs2Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bmia2Ù±‚`a Ù±‚aoa*Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`csinÙ±‚`a(Ù±‚bmia2Ù±‚`a Ù±‚aoa*Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`bpiÙ±‚`a Ù±‚aoa*Ù±‚`a Ù±‚bmic400Ù±‚`a Ù±‚aoa*Ù±‚`a Ù±‚`atÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚bc1x# create a transient "chirp"Ù±‚`a
Ù±‚`bs2Ù±‚`a[Ù±‚`atÙ±‚`a Ù±‚aoa<Ù±‚aoa=Ù±‚`a Ù±‚bmib10Ù±‚`a]Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bs2Ù±‚`a[Ù±‚bmib12Ù±‚`a Ù±‚aoa<Ù±‚aoa=Ù±‚`a Ù±‚`atÙ±‚`a]Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bmia0Ù±‚`a
Ù±‚`a
Ù±‚bc1x# add some noise into the mixÙ±‚`a
Ù±‚`cnseÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bmfd0.01Ù±‚`a Ù±‚aoa*Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`frandomÙ±‚aoa.Ù±‚`frandomÙ±‚`a(Ù±‚`dsizeÙ±‚aoa=Ù±‚bnbclenÙ±‚`a(Ù±‚`atÙ±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`axÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bs1Ù±‚`a Ù±‚aoa+Ù±‚`a Ù±‚`bs2Ù±‚`a Ù±‚aoa+Ù±‚`a Ù±‚`cnseÙ±‚`b  Ù±‚bc1l# the signalÙ±‚`a
Ù±‚`dNFFTÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bmid1024Ù±‚`b  Ù±‚bc1x&# the length of the windowing segmentsÙ±‚`a
Ù±‚`bFsÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bnbcintÙ±‚`a(Ù±‚bmfc1.0Ù±‚`a Ù±‚aoa/Ù±‚`a Ù±‚`bdtÙ±‚`a)Ù±‚`b  Ù±‚bc1x# the sampling frequencyÙ±‚`a
Ù±‚`a
Ù±‚`cfigÙ±‚`a,Ù±‚`a Ù±‚`a(Ù±‚`cax1Ù±‚`a,Ù±‚`a Ù±‚`cax2Ù±‚`a)Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cpltÙ±‚aoa.Ù±‚`hsubplotsÙ±‚`a(Ù±‚`enrowsÙ±‚aoa=Ù±‚bmia2Ù±‚`a)Ù±‚`a
Ù±‚`cax1Ù±‚aoa.Ù±‚`dplotÙ±‚`a(Ù±‚`atÙ±‚`a,Ù±‚`a Ù±‚`axÙ±‚`a)Ù±‚`a
Ù±‚`cPxxÙ±‚`a,Ù±‚`a Ù±‚`efreqsÙ±‚`a,Ù±‚`a Ù±‚`dbinsÙ±‚`a,Ù±‚`a Ù±‚`bimÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cax2Ù±‚aoa.Ù±‚`hspecgramÙ±‚`a(Ù±‚`axÙ±‚`a,Ù±‚`a Ù±‚`dNFFTÙ±‚aoa=Ù±‚`dNFFTÙ±‚`a,Ù±‚`a Ù±‚`bFsÙ±‚aoa=Ù±‚`bFsÙ±‚`a,Ù±‚`a Ù±‚`hnoverlapÙ±‚aoa=Ù±‚bmic900Ù±‚`a)Ù±‚`a
Ù±‚bc1x4# The `specgram` method returns 4 objects. They are:Ù±‚`a
Ù±‚bc1x# - Pxx: the periodogramÙ±‚`a
Ù±‚bc1x# - freqs: the frequency vectorÙ±‚`a
Ù±‚bc1x&# - bins: the centers of the time binsÙ±‚`a
Ù±‚bc1xG# - im: the .image.AxesImage instance representing the data in the plotÙ±‚`a
Ù±‚`cpltÙ±‚aoa.Ù±‚`dshowÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚bc1xM#############################################################################Ù±‚`a
Ù±‚bc1a#Ù±‚`a
Ù±‚bc1x# .. admonition:: ReferencesÙ±‚`a
Ù±‚bc1a#Ù±‚`a
Ù±‚bc1xN#    The use of the following functions, methods, classes and modules is shownÙ±‚`a
Ù±‚bc1u#    in this example:Ù±‚`a
Ù±‚bc1a#Ù±‚`a
Ù±‚bc1xE#    - `matplotlib.axes.Axes.specgram` / `matplotlib.pyplot.specgram`Ù±‚`a
`dNoneö