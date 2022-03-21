��������%���bsdx�"""
=====================================
Plotting the coherence of two signals
=====================================

An example showing how to plot the coherence of two signals.
"""���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���`a
���bc1x)# Fixing random state for reproducibility���`a
���`bnp���aoa.���`frandom���aoa.���`dseed���`a(���bmih19680801���`a)���`a
���`a
���`bdt���`a ���aoa=���`a ���bmfd0.01���`a
���`at���`a ���aoa=���`a ���`bnp���aoa.���`farange���`a(���bmia0���`a,���`a ���bmib30���`a,���`a ���`bdt���`a)���`a
���`dnse1���`a ���aoa=���`a ���`bnp���aoa.���`frandom���aoa.���`erandn���`a(���bnbclen���`a(���`at���`a)���`a)���`q                 ���bc1o# white noise 1���`a
���`dnse2���`a ���aoa=���`a ���`bnp���aoa.���`frandom���aoa.���`erandn���`a(���bnbclen���`a(���`at���`a)���`a)���`q                 ���bc1o# white noise 2���`a
���`a
���bc1x<# Two signals with a coherent part at 10Hz and a random part���`a
���`bs1���`a ���aoa=���`a ���`bnp���aoa.���`csin���`a(���bmia2���`a ���aoa*���`a ���`bnp���aoa.���`bpi���`a ���aoa*���`a ���bmib10���`a ���aoa*���`a ���`at���`a)���`a ���aoa+���`a ���`dnse1���`a
���`bs2���`a ���aoa=���`a ���`bnp���aoa.���`csin���`a(���bmia2���`a ���aoa*���`a ���`bnp���aoa.���`bpi���`a ���aoa*���`a ���bmib10���`a ���aoa*���`a ���`at���`a)���`a ���aoa+���`a ���`dnse2���`a
���`a
���`cfig���`a,���`a ���`caxs���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���bmia2���`a,���`a ���bmia1���`a)���`a
���`caxs���`a[���bmia0���`a]���aoa.���`dplot���`a(���`at���`a,���`a ���`bs1���`a,���`a ���`at���`a,���`a ���`bs2���`a)���`a
���`caxs���`a[���bmia0���`a]���aoa.���`hset_xlim���`a(���bmia0���`a,���`a ���bmia2���`a)���`a
���`caxs���`a[���bmia0���`a]���aoa.���`jset_xlabel���`a(���bs1a'���bs1dtime���bs1a'���`a)���`a
���`caxs���`a[���bmia0���`a]���aoa.���`jset_ylabel���`a(���bs1a'���bs1is1 and s2���bs1a'���`a)���`a
���`caxs���`a[���bmia0���`a]���aoa.���`dgrid���`a(���bkcdTrue���`a)���`a
���`a
���`ccxy���`a,���`a ���`af���`a ���aoa=���`a ���`caxs���`a[���bmia1���`a]���aoa.���`fcohere���`a(���`bs1���`a,���`a ���`bs2���`a,���`a ���bmic256���`a,���`a ���bmfb1.���`a ���aoa/���`a ���`bdt���`a)���`a
���`caxs���`a[���bmia1���`a]���aoa.���`jset_ylabel���`a(���bs1a'���bs1icoherence���bs1a'���`a)���`a
���`a
���`cfig���aoa.���`ltight_layout���`a(���`a)���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
`dNone�