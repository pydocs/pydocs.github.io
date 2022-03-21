������������bsdy�"""
==================
ggplot style sheet
==================

This example demonstrates the "ggplot" style, which adjusts the style to
emulate ggplot_ (a popular plotting package for R_).

These settings were shamelessly stolen from [1]_ (with permission).

.. [1] https://everyhue.me/posts/sane-color-scheme-for-matplotlib/

.. _ggplot: https://ggplot2.tidyverse.org/
.. _R: https://www.r-project.org/

"""���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���`a
���`cplt���aoa.���`estyle���aoa.���`cuse���`a(���bs1a'���bs1fggplot���bs1a'���`a)���`a
���`a
���bc1x)# Fixing random state for reproducibility���`a
���`bnp���aoa.���`frandom���aoa.���`dseed���`a(���bmih19680801���`a)���`a
���`a
���`cfig���`a,���`a ���`caxs���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`encols���aoa=���bmia2���`a,���`a ���`enrows���aoa=���bmia2���`a)���`a
���`cax1���`a,���`a ���`cax2���`a,���`a ���`cax3���`a,���`a ���`cax4���`a ���aoa=���`a ���`caxs���aoa.���`dflat���`a
���`a
���bc1x?# scatter plot (Note: `plt.scatter` doesn't use default colors)���`a
���`ax���`a,���`a ���`ay���`a ���aoa=���`a ���`bnp���aoa.���`frandom���aoa.���`fnormal���`a(���`dsize���aoa=���`a(���bmia2���`a,���`a ���bmic200���`a)���`a)���`a
���`cax1���aoa.���`dplot���`a(���`ax���`a,���`a ���`ay���`a,���`a ���bs1a'���bs1ao���bs1a'���`a)���`a
���`a
���bc1x7# sinusoidal lines with colors from default color cycle���`a
���`aL���`a ���aoa=���`a ���bmia2���aoa*���`bnp���aoa.���`bpi���`a
���`ax���`a ���aoa=���`a ���`bnp���aoa.���`hlinspace���`a(���bmia0���`a,���`a ���`aL���`a)���`a
���`gncolors���`a ���aoa=���`a ���bnbclen���`a(���`cplt���aoa.���`hrcParams���`a[���bs1a'���bs1oaxes.prop_cycle���bs1a'���`a]���`a)���`a
���`eshift���`a ���aoa=���`a ���`bnp���aoa.���`hlinspace���`a(���bmia0���`a,���`a ���`aL���`a,���`a ���`gncolors���`a,���`a ���`hendpoint���aoa=���bkceFalse���`a)���`a
���akcfor���`a ���`as���`a ���bowbin���`a ���`eshift���`a:���`a
���`d    ���`cax2���aoa.���`dplot���`a(���`ax���`a,���`a ���`bnp���aoa.���`csin���`a(���`ax���`a ���aoa+���`a ���`as���`a)���`a,���`a ���bs1a'���bs1a-���bs1a'���`a)���`a
���`cax2���aoa.���`gmargins���`a(���bmia0���`a)���`a
���`a
���bc1l# bar graphs���`a
���`ax���`a ���aoa=���`a ���`bnp���aoa.���`farange���`a(���bmia5���`a)���`a
���`by1���`a,���`a ���`by2���`a ���aoa=���`a ���`bnp���aoa.���`frandom���aoa.���`grandint���`a(���bmia1���`a,���`a ���bmib25���`a,���`a ���`dsize���aoa=���`a(���bmia2���`a,���`a ���bmia5���`a)���`a)���`a
���`ewidth���`a ���aoa=���`a ���bmfd0.25���`a
���`cax3���aoa.���`cbar���`a(���`ax���`a,���`a ���`by1���`a,���`a ���`ewidth���`a)���`a
���`cax3���aoa.���`cbar���`a(���`ax���`a ���aoa+���`a ���`ewidth���`a,���`a ���`by2���`a,���`a ���`ewidth���`a,���`a
���`h        ���`ecolor���aoa=���bnbdlist���`a(���`cplt���aoa.���`hrcParams���`a[���bs1a'���bs1oaxes.prop_cycle���bs1a'���`a]���`a)���`a[���bmia2���`a]���`a[���bs1a'���bs1ecolor���bs1a'���`a]���`a)���`a
���`cax3���aoa.���`jset_xticks���`a(���`ax���`a ���aoa+���`a ���`ewidth���`a,���`a ���`flabels���aoa=���`a[���bs1a'���bs1aa���bs1a'���`a,���`a ���bs1a'���bs1ab���bs1a'���`a,���`a ���bs1a'���bs1ac���bs1a'���`a,���`a ���bs1a'���bs1ad���bs1a'���`a,���`a ���bs1a'���bs1ae���bs1a'���`a]���`a)���`a
���`a
���bc1x.# circles with colors from default color cycle���`a
���akcfor���`a ���`ai���`a,���`a ���`ecolor���`a ���bowbin���`a ���bnbienumerate���`a(���`cplt���aoa.���`hrcParams���`a[���bs1a'���bs1oaxes.prop_cycle���bs1a'���`a]���`a)���`a:���`a
���`d    ���`bxy���`a ���aoa=���`a ���`bnp���aoa.���`frandom���aoa.���`fnormal���`a(���`dsize���aoa=���bmia2���`a)���`a
���`d    ���`cax4���aoa.���`iadd_patch���`a(���`cplt���aoa.���`fCircle���`a(���`bxy���`a,���`a ���`fradius���aoa=���bmfc0.3���`a,���`a ���`ecolor���aoa=���`ecolor���`a[���bs1a'���bs1ecolor���bs1a'���`a]���`a)���`a)���`a
���`cax4���aoa.���`daxis���`a(���bs1a'���bs1eequal���bs1a'���`a)���`a
���`cax4���aoa.���`gmargins���`a(���bmia0���`a)���`a
���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
`dNone�