��������s���bsdy�"""
==================================================
Using histograms to plot a cumulative distribution
==================================================

This shows how to plot a cumulative, normalized histogram as a
step function in order to visualize the empirical cumulative
distribution function (CDF) of a sample. We also show the theoretical CDF.

A couple of other options to the ``hist`` function are demonstrated. Namely, we
use the *normed* parameter to normalize the histogram and a couple of different
options to the *cumulative* parameter. The *normed* parameter takes a boolean
value. When ``True``, the bin heights are scaled such that the total area of
the histogram is 1. The *cumulative* keyword argument is a little more nuanced.
Like *normed*, you can pass it True or False, but you can also pass it -1 to
reverse the distribution.

Since we're showing a normalized and cumulative histogram, these curves
are effectively the cumulative distribution functions (CDFs) of the
samples. In engineering, empirical CDFs are sometimes called
"non-exceedance" curves. In other words, you can look at the
y-value for a given-x-value to get the probability of and observation
from the sample not exceeding that x-value. For example, the value of
225 on the x-axis corresponds to about 0.85 on the y-axis, so there's an
85% chance that an observation in the sample does not exceed 225.
Conversely, setting, ``cumulative`` to -1 as is done in the
last series for this example, creates a "exceedance" curve.

Selecting different bin counts and sizes can significantly affect the
shape of a histogram. The Astropy docs have a great section on how to
select these parameters:
http://docs.astropy.org/en/stable/visualization/histogram.html

"""���`a
���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���`a
���`bnp���aoa.���`frandom���aoa.���`dseed���`a(���bmih19680801���`a)���`a
���`a
���`bmu���`a ���aoa=���`a ���bmic200���`a
���`esigma���`a ���aoa=���`a ���bmib25���`a
���`fn_bins���`a ���aoa=���`a ���bmib50���`a
���`ax���`a ���aoa=���`a ���`bnp���aoa.���`frandom���aoa.���`fnormal���`a(���`bmu���`a,���`a ���`esigma���`a,���`a ���`dsize���aoa=���bmic100���`a)���`a
���`a
���`cfig���`a,���`a ���`bax���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`gfigsize���aoa=���`a(���bmia8���`a,���`a ���bmia4���`a)���`a)���`a
���`a
���bc1x# plot the cumulative histogram���`a
���`an���`a,���`a ���`dbins���`a,���`a ���`gpatches���`a ���aoa=���`a ���`bax���aoa.���`dhist���`a(���`ax���`a,���`a ���`fn_bins���`a,���`a ���`gdensity���aoa=���bkcdTrue���`a,���`a ���`hhisttype���aoa=���bs1a'���bs1dstep���bs1a'���`a,���`a
���`x                           ���`jcumulative���aoa=���bkcdTrue���`a,���`a ���`elabel���aoa=���bs1a'���bs1iEmpirical���bs1a'���`a)���`a
���`a
���bc1x/# Add a line showing the expected distribution.���`a
���`ay���`a ���aoa=���`a ���`a(���`a(���bmia1���`a ���aoa/���`a ���`a(���`bnp���aoa.���`dsqrt���`a(���bmia2���`a ���aoa*���`a ���`bnp���aoa.���`bpi���`a)���`a ���aoa*���`a ���`esigma���`a)���`a)���`a ���aoa*���`a
���`e     ���`bnp���aoa.���`cexp���`a(���aoa-���bmfc0.5���`a ���aoa*���`a ���`a(���bmia1���`a ���aoa/���`a ���`esigma���`a ���aoa*���`a ���`a(���`dbins���`a ���aoa-���`a ���`bmu���`a)���`a)���aoa*���aoa*���bmia2���`a)���`a)���`a
���`ay���`a ���aoa=���`a ���`ay���aoa.���`fcumsum���`a(���`a)���`a
���`ay���`a ���aoa/���aoa=���`a ���`ay���`a[���aoa-���bmia1���`a]���`a
���`a
���`bax���aoa.���`dplot���`a(���`dbins���`a,���`a ���`ay���`a,���`a ���bs1a'���bs1ck--���bs1a'���`a,���`a ���`ilinewidth���aoa=���bmfc1.5���`a,���`a ���`elabel���aoa=���bs1a'���bs1kTheoretical���bs1a'���`a)���`a
���`a
���bc1x*# Overlay a reversed cumulative histogram.���`a
���`bax���aoa.���`dhist���`a(���`ax���`a,���`a ���`dbins���aoa=���`dbins���`a,���`a ���`gdensity���aoa=���bkcdTrue���`a,���`a ���`hhisttype���aoa=���bs1a'���bs1dstep���bs1a'���`a,���`a ���`jcumulative���aoa=���aoa-���bmia1���`a,���`a
���`h        ���`elabel���aoa=���bs1a'���bs1mReversed emp.���bs1a'���`a)���`a
���`a
���bc1t# tidy up the figure���`a
���`bax���aoa.���`dgrid���`a(���bkcdTrue���`a)���`a
���`bax���aoa.���`flegend���`a(���`cloc���aoa=���bs1a'���bs1eright���bs1a'���`a)���`a
���`bax���aoa.���`iset_title���`a(���bs1a'���bs1xCumulative step histograms���bs1a'���`a)���`a
���`bax���aoa.���`jset_xlabel���`a(���bs1a'���bs1tAnnual rainfall (mm)���bs1a'���`a)���`a
���`bax���aoa.���`jset_ylabel���`a(���bs1a'���bs1xLikelihood of occurrence���bs1a'���`a)���`a
���`a
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
`dNone�