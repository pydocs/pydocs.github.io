������������bsdy"""
========================
Spectrum Representations
========================

The plots show different spectrum representations of a sine signal with
additive noise. A (frequency) spectrum of a discrete-time signal is calculated
by utilizing the fast Fourier transform (FFT).
"""���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���`a
���`a
���`bnp���aoa.���`frandom���aoa.���`dseed���`a(���bmia0���`a)���`a
���`a
���`bdt���`a ���aoa=���`a ���bmfd0.01���`b  ���bc1s# sampling interval���`a
���`bFs���`a ���aoa=���`a ���bmia1���`a ���aoa/���`a ���`bdt���`b  ���bc1t# sampling frequency���`a
���`at���`a ���aoa=���`a ���`bnp���aoa.���`farange���`a(���bmia0���`a,���`a ���bmib10���`a,���`a ���`bdt���`a)���`a
���`a
���bc1q# generate noise:���`a
���`cnse���`a ���aoa=���`a ���`bnp���aoa.���`frandom���aoa.���`erandn���`a(���bnbclen���`a(���`at���`a)���`a)���`a
���`ar���`a ���aoa=���`a ���`bnp���aoa.���`cexp���`a(���aoa-���`at���`a ���aoa/���`a ���bmfd0.05���`a)���`a
���`dcnse���`a ���aoa=���`a ���`bnp���aoa.���`hconvolve���`a(���`cnse���`a,���`a ���`ar���`a)���`a ���aoa*���`a ���`bdt���`a
���`dcnse���`a ���aoa=���`a ���`dcnse���`a[���`a:���bnbclen���`a(���`at���`a)���`a]���`a
���`a
���`as���`a ���aoa=���`a ���bmfc0.1���`a ���aoa*���`a ���`bnp���aoa.���`csin���`a(���bmia4���`a ���aoa*���`a ���`bnp���aoa.���`bpi���`a ���aoa*���`a ���`at���`a)���`a ���aoa+���`a ���`dcnse���`b  ���bc1l# the signal���`a
���`a
���`cfig���`a,���`a ���`caxs���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`enrows���aoa=���bmia3���`a,���`a ���`encols���aoa=���bmia2���`a,���`a ���`gfigsize���aoa=���`a(���bmia7���`a,���`a ���bmia7���`a)���`a)���`a
���`a
���bc1s# plot time signal:���`a
���`caxs���`a[���bmia0���`a,���`a ���bmia0���`a]���aoa.���`iset_title���`a(���bs2a"���bs2fSignal���bs2a"���`a)���`a
���`caxs���`a[���bmia0���`a,���`a ���bmia0���`a]���aoa.���`dplot���`a(���`at���`a,���`a ���`as���`a,���`a ���`ecolor���aoa=���bs1a'���bs1bC0���bs1a'���`a)���`a
���`caxs���`a[���bmia0���`a,���`a ���bmia0���`a]���aoa.���`jset_xlabel���`a(���bs2a"���bs2dTime���bs2a"���`a)���`a
���`caxs���`a[���bmia0���`a,���`a ���bmia0���`a]���aoa.���`jset_ylabel���`a(���bs2a"���bs2iAmplitude���bs2a"���`a)���`a
���`a
���bc1x # plot different spectrum types:���`a
���`caxs���`a[���bmia1���`a,���`a ���bmia0���`a]���aoa.���`iset_title���`a(���bs2a"���bs2rMagnitude Spectrum���bs2a"���`a)���`a
���`caxs���`a[���bmia1���`a,���`a ���bmia0���`a]���aoa.���`rmagnitude_spectrum���`a(���`as���`a,���`a ���`bFs���aoa=���`bFs���`a,���`a ���`ecolor���aoa=���bs1a'���bs1bC1���bs1a'���`a)���`a
���`a
���`caxs���`a[���bmia1���`a,���`a ���bmia1���`a]���aoa.���`iset_title���`a(���bs2a"���bs2wLog. Magnitude Spectrum���bs2a"���`a)���`a
���`caxs���`a[���bmia1���`a,���`a ���bmia1���`a]���aoa.���`rmagnitude_spectrum���`a(���`as���`a,���`a ���`bFs���aoa=���`bFs���`a,���`a ���`escale���aoa=���bs1a'���bs1bdB���bs1a'���`a,���`a ���`ecolor���aoa=���bs1a'���bs1bC1���bs1a'���`a)���`a
���`a
���`caxs���`a[���bmia2���`a,���`a ���bmia0���`a]���aoa.���`iset_title���`a(���bs2a"���bs2oPhase Spectrum ���bs2a"���`a)���`a
���`caxs���`a[���bmia2���`a,���`a ���bmia0���`a]���aoa.���`nphase_spectrum���`a(���`as���`a,���`a ���`bFs���aoa=���`bFs���`a,���`a ���`ecolor���aoa=���bs1a'���bs1bC2���bs1a'���`a)���`a
���`a
���`caxs���`a[���bmia2���`a,���`a ���bmia1���`a]���aoa.���`iset_title���`a(���bs2a"���bs2nAngle Spectrum���bs2a"���`a)���`a
���`caxs���`a[���bmia2���`a,���`a ���bmia1���`a]���aoa.���`nangle_spectrum���`a(���`as���`a,���`a ���`bFs���aoa=���`bFs���`a,���`a ���`ecolor���aoa=���bs1a'���bs1bC2���bs1a'���`a)���`a
���`a
���`caxs���`a[���bmia0���`a,���`a ���bmia1���`a]���aoa.���`fremove���`a(���`a)���`b  ���bc1x# don't display empty ax���`a
���`a
���`cfig���aoa.���`ltight_layout���`a(���`a)���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
`dNone�