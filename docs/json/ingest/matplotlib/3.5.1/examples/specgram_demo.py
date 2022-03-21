��������0���bsdxp"""
================
Spectrogram Demo
================

Demo of a spectrogram plot (`~.axes.Axes.specgram`).
"""���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���`a
���bc1x)# Fixing random state for reproducibility���`a
���`bnp���aoa.���`frandom���aoa.���`dseed���`a(���bmih19680801���`a)���`a
���`a
���`bdt���`a ���aoa=���`a ���bmff0.0005���`a
���`at���`a ���aoa=���`a ���`bnp���aoa.���`farange���`a(���bmfc0.0���`a,���`a ���bmfd20.0���`a,���`a ���`bdt���`a)���`a
���`bs1���`a ���aoa=���`a ���`bnp���aoa.���`csin���`a(���bmia2���`a ���aoa*���`a ���`bnp���aoa.���`bpi���`a ���aoa*���`a ���bmic100���`a ���aoa*���`a ���`at���`a)���`a
���`bs2���`a ���aoa=���`a ���bmia2���`a ���aoa*���`a ���`bnp���aoa.���`csin���`a(���bmia2���`a ���aoa*���`a ���`bnp���aoa.���`bpi���`a ���aoa*���`a ���bmic400���`a ���aoa*���`a ���`at���`a)���`a
���`a
���bc1x# create a transient "chirp"���`a
���`bs2���`a[���`at���`a ���aoa<���aoa=���`a ���bmib10���`a]���`a ���aoa=���`a ���`bs2���`a[���bmib12���`a ���aoa<���aoa=���`a ���`at���`a]���`a ���aoa=���`a ���bmia0���`a
���`a
���bc1x# add some noise into the mix���`a
���`cnse���`a ���aoa=���`a ���bmfd0.01���`a ���aoa*���`a ���`bnp���aoa.���`frandom���aoa.���`frandom���`a(���`dsize���aoa=���bnbclen���`a(���`at���`a)���`a)���`a
���`a
���`ax���`a ���aoa=���`a ���`bs1���`a ���aoa+���`a ���`bs2���`a ���aoa+���`a ���`cnse���`b  ���bc1l# the signal���`a
���`dNFFT���`a ���aoa=���`a ���bmid1024���`b  ���bc1x&# the length of the windowing segments���`a
���`bFs���`a ���aoa=���`a ���bnbcint���`a(���bmfc1.0���`a ���aoa/���`a ���`bdt���`a)���`b  ���bc1x# the sampling frequency���`a
���`a
���`cfig���`a,���`a ���`a(���`cax1���`a,���`a ���`cax2���`a)���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`enrows���aoa=���bmia2���`a)���`a
���`cax1���aoa.���`dplot���`a(���`at���`a,���`a ���`ax���`a)���`a
���`cPxx���`a,���`a ���`efreqs���`a,���`a ���`dbins���`a,���`a ���`bim���`a ���aoa=���`a ���`cax2���aoa.���`hspecgram���`a(���`ax���`a,���`a ���`dNFFT���aoa=���`dNFFT���`a,���`a ���`bFs���aoa=���`bFs���`a,���`a ���`hnoverlap���aoa=���bmic900���`a)���`a
���bc1x4# The `specgram` method returns 4 objects. They are:���`a
���bc1x# - Pxx: the periodogram���`a
���bc1x# - freqs: the frequency vector���`a
���bc1x&# - bins: the centers of the time bins���`a
���bc1xG# - im: the .image.AxesImage instance representing the data in the plot���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
���`a
���bc1xM#############################################################################���`a
���bc1a#���`a
���bc1x# .. admonition:: References���`a
���bc1a#���`a
���bc1xN#    The use of the following functions, methods, classes and modules is shown���`a
���bc1u#    in this example:���`a
���bc1a#���`a
���bc1xE#    - `matplotlib.axes.Axes.specgram` / `matplotlib.pyplot.specgram`���`a
`dNone�