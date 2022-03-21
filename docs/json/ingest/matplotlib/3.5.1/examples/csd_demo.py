��������l���bsdxU"""
========
CSD Demo
========

Compute the cross spectral density of two signals
"""���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���`a
���`a
���`cfig���`a,���`a ���`a(���`cax1���`a,���`a ���`cax2���`a)���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���bmia2���`a,���`a ���bmia1���`a)���`a
���bc1x0# make a little extra space between the subplots���`a
���`cfig���aoa.���`osubplots_adjust���`a(���`fhspace���aoa=���bmfc0.5���`a)���`a
���`a
���`bdt���`a ���aoa=���`a ���bmfd0.01���`a
���`at���`a ���aoa=���`a ���`bnp���aoa.���`farange���`a(���bmia0���`a,���`a ���bmib30���`a,���`a ���`bdt���`a)���`a
���`a
���bc1x)# Fixing random state for reproducibility���`a
���`bnp���aoa.���`frandom���aoa.���`dseed���`a(���bmih19680801���`a)���`a
���`a
���`a
���`dnse1���`a ���aoa=���`a ���`bnp���aoa.���`frandom���aoa.���`erandn���`a(���bnbclen���`a(���`at���`a)���`a)���`q                 ���bc1o# white noise 1���`a
���`dnse2���`a ���aoa=���`a ���`bnp���aoa.���`frandom���aoa.���`erandn���`a(���bnbclen���`a(���`at���`a)���`a)���`q                 ���bc1o# white noise 2���`a
���`ar���`a ���aoa=���`a ���`bnp���aoa.���`cexp���`a(���aoa-���`at���`a ���aoa/���`a ���bmfd0.05���`a)���`a
���`a
���`ecnse1���`a ���aoa=���`a ���`bnp���aoa.���`hconvolve���`a(���`dnse1���`a,���`a ���`ar���`a,���`a ���`dmode���aoa=���bs1a'���bs1dsame���bs1a'���`a)���`a ���aoa*���`a ���`bdt���`c   ���bc1q# colored noise 1���`a
���`ecnse2���`a ���aoa=���`a ���`bnp���aoa.���`hconvolve���`a(���`dnse2���`a,���`a ���`ar���`a,���`a ���`dmode���aoa=���bs1a'���bs1dsame���bs1a'���`a)���`a ���aoa*���`a ���`bdt���`c   ���bc1q# colored noise 2���`a
���`a
���bc1x4# two signals with a coherent part and a random part���`a
���`bs1���`a ���aoa=���`a ���bmfd0.01���`a ���aoa*���`a ���`bnp���aoa.���`csin���`a(���bmia2���`a ���aoa*���`a ���`bnp���aoa.���`bpi���`a ���aoa*���`a ���bmib10���`a ���aoa*���`a ���`at���`a)���`a ���aoa+���`a ���`ecnse1���`a
���`bs2���`a ���aoa=���`a ���bmfd0.01���`a ���aoa*���`a ���`bnp���aoa.���`csin���`a(���bmia2���`a ���aoa*���`a ���`bnp���aoa.���`bpi���`a ���aoa*���`a ���bmib10���`a ���aoa*���`a ���`at���`a)���`a ���aoa+���`a ���`ecnse2���`a
���`a
���`cax1���aoa.���`dplot���`a(���`at���`a,���`a ���`bs1���`a,���`a ���`at���`a,���`a ���`bs2���`a)���`a
���`cax1���aoa.���`hset_xlim���`a(���bmia0���`a,���`a ���bmia5���`a)���`a
���`cax1���aoa.���`jset_xlabel���`a(���bs1a'���bs1dtime���bs1a'���`a)���`a
���`cax1���aoa.���`jset_ylabel���`a(���bs1a'���bs1is1 and s2���bs1a'���`a)���`a
���`cax1���aoa.���`dgrid���`a(���bkcdTrue���`a)���`a
���`a
���`ccxy���`a,���`a ���`af���`a ���aoa=���`a ���`cax2���aoa.���`ccsd���`a(���`bs1���`a,���`a ���`bs2���`a,���`a ���bmic256���`a,���`a ���bmfb1.���`a ���aoa/���`a ���`bdt���`a)���`a
���`cax2���aoa.���`jset_ylabel���`a(���bs1a'���bs1hCSD (db)���bs1a'���`a)���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
`dNone�