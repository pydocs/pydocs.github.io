�����������bsdy�"""
==============================================
Some features of the histogram (hist) function
==============================================

In addition to the basic histogram, this demo shows a few optional features:

* Setting the number of data bins.
* The *density* parameter, which normalizes bin heights so that the integral of
  the histogram is 1. The resulting histogram is an approximation of the
  probability density function.

Selecting different bin counts and sizes can significantly affect the shape
of a histogram. The Astropy docs have a great section_ on how to select these
parameters.

.. _section: http://docs.astropy.org/en/stable/visualization/histogram.html
"""���`a
���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���`a
���`bnp���aoa.���`frandom���aoa.���`dseed���`a(���bmih19680801���`a)���`a
���`a
���bc1n# example data���`a
���`bmu���`a ���aoa=���`a ���bmic100���`b  ���bc1v# mean of distribution���`a
���`esigma���`a ���aoa=���`a ���bmib15���`b  ���bc1x$# standard deviation of distribution���`a
���`ax���`a ���aoa=���`a ���`bmu���`a ���aoa+���`a ���`esigma���`a ���aoa*���`a ���`bnp���aoa.���`frandom���aoa.���`erandn���`a(���bmic437���`a)���`a
���`a
���`hnum_bins���`a ���aoa=���`a ���bmib50���`a
���`a
���`cfig���`a,���`a ���`bax���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`a)���`a
���`a
���bc1x# the histogram of the data���`a
���`an���`a,���`a ���`dbins���`a,���`a ���`gpatches���`a ���aoa=���`a ���`bax���aoa.���`dhist���`a(���`ax���`a,���`a ���`hnum_bins���`a,���`a ���`gdensity���aoa=���bkcdTrue���`a)���`a
���`a
���bc1w# add a 'best fit' line���`a
���`ay���`a ���aoa=���`a ���`a(���`a(���bmia1���`a ���aoa/���`a ���`a(���`bnp���aoa.���`dsqrt���`a(���bmia2���`a ���aoa*���`a ���`bnp���aoa.���`bpi���`a)���`a ���aoa*���`a ���`esigma���`a)���`a)���`a ���aoa*���`a
���`e     ���`bnp���aoa.���`cexp���`a(���aoa-���bmfc0.5���`a ���aoa*���`a ���`a(���bmia1���`a ���aoa/���`a ���`esigma���`a ���aoa*���`a ���`a(���`dbins���`a ���aoa-���`a ���`bmu���`a)���`a)���aoa*���aoa*���bmia2���`a)���`a)���`a
���`bax���aoa.���`dplot���`a(���`dbins���`a,���`a ���`ay���`a,���`a ���bs1a'���bs1b--���bs1a'���`a)���`a
���`bax���aoa.���`jset_xlabel���`a(���bs1a'���bs1fSmarts���bs1a'���`a)���`a
���`bax���aoa.���`jset_ylabel���`a(���bs1a'���bs1sProbability density���bs1a'���`a)���`a
���`bax���aoa.���`iset_title���`a(���bsaar���bs1a'���bs1rHistogram of IQ: $���bs1a\���bs1jmu=100$, $���bs1a\���bs1isigma=15$���bs1a'���`a)���`a
���`a
���bc1x-# Tweak spacing to prevent clipping of ylabel���`a
���`cfig���aoa.���`ltight_layout���`a(���`a)���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
���`a
���bc1xM#############################################################################���`a
���bc1a#���`a
���bc1x# .. admonition:: References���`a
���bc1a#���`a
���bc1xN#    The use of the following functions, methods, classes and modules is shown���`a
���bc1u#    in this example:���`a
���bc1a#���`a
���bc1x=#    - `matplotlib.axes.Axes.hist` / `matplotlib.pyplot.hist`���`a
���bc1x'#    - `matplotlib.axes.Axes.set_title`���`a
���bc1x(#    - `matplotlib.axes.Axes.set_xlabel`���`a
���bc1x(#    - `matplotlib.axes.Axes.set_ylabel`���`a
`dNone�