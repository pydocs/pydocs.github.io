��������:���bsdx�"""
=======================
Colorbar Tick Labelling
=======================

Produce custom labelling for a colorbar.

Contributed by Scott Sinclair
"""���`a
���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���bkndfrom���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����`a ���bknfimport���`a ���`bcm���`a
���bkndfrom���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����bnna.���bnnfrandom���`a ���bknfimport���`a ���`erandn���`a
���`a
���`a
���bc1x)# Fixing random state for reproducibility���`a
���`bnp���aoa.���`frandom���aoa.���`dseed���`a(���bmih19680801���`a)���`a
���`a
���bc1xO###############################################################################���`a
���bc1x,# Make plot with vertical (default) colorbar���`a
���`a
���`cfig���`a,���`a ���`bax���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`a)���`a
���`a
���`ddata���`a ���aoa=���`a ���`bnp���aoa.���`dclip���`a(���`erandn���`a(���bmic250���`a,���`a ���bmic250���`a)���`a,���`a ���aoa-���bmia1���`a,���`a ���bmia1���`a)���`a
���`a
���`ccax���`a ���aoa=���`a ���`bax���aoa.���`fimshow���`a(���`ddata���`a,���`a ���`dcmap���aoa=���`bcm���aoa.���`hcoolwarm���`a)���`a
���`bax���aoa.���`iset_title���`a(���bs1a'���bs1x%Gaussian noise with vertical colorbar���bs1a'���`a)���`a
���`a
���bc1xO# Add colorbar, make sure to specify tick locations to match desired ticklabels���`a
���`dcbar���`a ���aoa=���`a ���`cfig���aoa.���`hcolorbar���`a(���`ccax���`a,���`a ���`eticks���aoa=���`a[���aoa-���bmia1���`a,���`a ���bmia0���`a,���`a ���bmia1���`a]���`a)���`a
���`dcbar���aoa.���`bax���aoa.���`oset_yticklabels���`a(���`a[���bs1a'���bs1d< -1���bs1a'���`a,���`a ���bs1a'���bs1a0���bs1a'���`a,���`a ���bs1a'���bs1c> 1���bs1a'���`a]���`a)���`b  ���bc1x# vertically oriented colorbar���`a
���`a
���bc1xO###############################################################################���`a
���bc1x$# Make plot with horizontal colorbar���`a
���`a
���`cfig���`a,���`a ���`bax���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`a)���`a
���`a
���`ddata���`a ���aoa=���`a ���`bnp���aoa.���`dclip���`a(���`erandn���`a(���bmic250���`a,���`a ���bmic250���`a)���`a,���`a ���aoa-���bmia1���`a,���`a ���bmia1���`a)���`a
���`a
���`ccax���`a ���aoa=���`a ���`bax���aoa.���`fimshow���`a(���`ddata���`a,���`a ���`dcmap���aoa=���`bcm���aoa.���`fafmhot���`a)���`a
���`bax���aoa.���`iset_title���`a(���bs1a'���bs1x'Gaussian noise with horizontal colorbar���bs1a'���`a)���`a
���`a
���`dcbar���`a ���aoa=���`a ���`cfig���aoa.���`hcolorbar���`a(���`ccax���`a,���`a ���`eticks���aoa=���`a[���aoa-���bmia1���`a,���`a ���bmia0���`a,���`a ���bmia1���`a]���`a,���`a ���`korientation���aoa=���bs1a'���bs1jhorizontal���bs1a'���`a)���`a
���`dcbar���aoa.���`bax���aoa.���`oset_xticklabels���`a(���`a[���bs1a'���bs1cLow���bs1a'���`a,���`a ���bs1a'���bs1fMedium���bs1a'���`a,���`a ���bs1a'���bs1dHigh���bs1a'���`a]���`a)���`b  ���bc1u# horizontal colorbar���`a
���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
`dNone�