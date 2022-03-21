������������bsdy """
Fill Between and Alpha
======================

The `~matplotlib.axes.Axes.fill_between` function generates a shaded
region between a min and max boundary that is useful for illustrating ranges.
It has a very handy ``where`` argument to combine filling with logical ranges,
e.g., to just fill in a curve over some threshold value.

At its most basic level, ``fill_between`` can be use to enhance a graphs visual
appearance. Let's compare two graphs of a financial times with a simple line
plot on the left and a filled line on the right.
"""���`a
���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnecbook���`a ���akbas���`a ���bnnecbook���`a
���`a
���`a
���bc1x$# load up some sample financial data���`a
���`ar���`a ���aoa=���`a ���`a(���`ecbook���aoa.���`oget_sample_data���`a(���bs1a'���bs1hgoog.npz���bs1a'���`a,���`a ���`gnp_load���aoa=���bkcdTrue���`a)���`a[���bs1a'���bs1jprice_data���bs1a'���`a]���`a
���`e     ���aoa.���`dview���`a(���`bnp���aoa.���`hrecarray���`a)���`a)���`a
���bc1x2# create two subplots with the shared x and y axes���`a
���`cfig���`a,���`a ���`a(���`cax1���`a,���`a ���`cax2���`a)���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���bmia1���`a,���`a ���bmia2���`a,���`a ���`fsharex���aoa=���bkcdTrue���`a,���`a ���`fsharey���aoa=���bkcdTrue���`a)���`a
���`a
���`hpricemin���`a ���aoa=���`a ���`ar���aoa.���`eclose���aoa.���`cmin���`a(���`a)���`a
���`a
���`cax1���aoa.���`dplot���`a(���`ar���aoa.���`ddate���`a,���`a ���`ar���aoa.���`eclose���`a,���`a ���`blw���aoa=���bmia2���`a)���`a
���`cax2���aoa.���`lfill_between���`a(���`ar���aoa.���`ddate���`a,���`a ���`hpricemin���`a,���`a ���`ar���aoa.���`eclose���`a,���`a ���`ealpha���aoa=���bmfc0.7���`a)���`a
���`a
���akcfor���`a ���`bax���`a ���bowbin���`a ���`cax1���`a,���`a ���`cax2���`a:���`a
���`d    ���`bax���aoa.���`dgrid���`a(���bkcdTrue���`a)���`a
���`a
���`cax1���aoa.���`jset_ylabel���`a(���bs1a'���bs1eprice���bs1a'���`a)���`a
���akcfor���`a ���`elabel���`a ���bowbin���`a ���`cax2���aoa.���`oget_yticklabels���`a(���`a)���`a:���`a
���`d    ���`elabel���aoa.���`kset_visible���`a(���bkceFalse���`a)���`a
���`a
���`cfig���aoa.���`hsuptitle���`a(���bs1a'���bs1x!Google (GOOG) daily closing price���bs1a'���`a)���`a
���`cfig���aoa.���`mautofmt_xdate���`a(���`a)���`a
���`a
���bc1xO###############################################################################���`a
���bc1xG# The alpha channel is not necessary here, but it can be used to soften���`a
���bc1xH# colors for more visually appealing plots.  In other examples, as we'll���`a
���bc1xC# see below, the alpha channel is functionally useful as the shaded���`a
���bc1xF# regions can overlap and alpha allows you to see both.  Note that the���`a
���bc1x@# postscript format does not support alpha (this is a postscript���`a
���bc1xD# limitation, not a matplotlib limitation), so when using alpha save���`a
���bc1x"# your figures in PNG, PDF or SVG.���`a
���bc1a#���`a
���bc1xD# Our next example computes two populations of random walkers with a���`a
���bc1xH# different mean and standard deviation of the normal distributions from���`a
���bc1xC# which the steps are drawn.  We use filled regions to plot +/- one���`a
���bc1xF# standard deviation of the mean position of the population.  Here the���`a
���bc1x.# alpha channel is useful, not just aesthetic.���`a
���`a
���bc1x)# Fixing random state for reproducibility���`a
���`bnp���aoa.���`frandom���aoa.���`dseed���`a(���bmih19680801���`a)���`a
���`a
���`fNsteps���`a,���`a ���`hNwalkers���`a ���aoa=���`a ���bmic100���`a,���`a ���bmic250���`a
���`at���`a ���aoa=���`a ���`bnp���aoa.���`farange���`a(���`fNsteps���`a)���`a
���`a
���bc1x3# an (Nsteps x Nwalkers) array of random walk steps���`a
���`bS1���`a ���aoa=���`a ���bmfe0.004���`a ���aoa+���`a ���bmfd0.02���aoa*���`bnp���aoa.���`frandom���aoa.���`erandn���`a(���`fNsteps���`a,���`a ���`hNwalkers���`a)���`a
���`bS2���`a ���aoa=���`a ���bmfe0.002���`a ���aoa+���`a ���bmfd0.01���aoa*���`bnp���aoa.���`frandom���aoa.���`erandn���`a(���`fNsteps���`a,���`a ���`hNwalkers���`a)���`a
���`a
���bc1x9# an (Nsteps x Nwalkers) array of random walker positions���`a
���`bX1���`a ���aoa=���`a ���`bS1���aoa.���`fcumsum���`a(���`daxis���aoa=���bmia0���`a)���`a
���`bX2���`a ���aoa=���`a ���`bS2���aoa.���`fcumsum���`a(���`daxis���aoa=���bmia0���`a)���`a
���`a
���`a
���bc1xF# Nsteps length arrays empirical means and standard deviations of both���`a
���bc1w# populations over time���`a
���`cmu1���`a ���aoa=���`a ���`bX1���aoa.���`dmean���`a(���`daxis���aoa=���bmia1���`a)���`a
���`fsigma1���`a ���aoa=���`a ���`bX1���aoa.���`cstd���`a(���`daxis���aoa=���bmia1���`a)���`a
���`cmu2���`a ���aoa=���`a ���`bX2���aoa.���`dmean���`a(���`daxis���aoa=���bmia1���`a)���`a
���`fsigma2���`a ���aoa=���`a ���`bX2���aoa.���`cstd���`a(���`daxis���aoa=���bmia1���`a)���`a
���`a
���bc1j# plot it!���`a
���`cfig���`a,���`a ���`bax���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���bmia1���`a)���`a
���`bax���aoa.���`dplot���`a(���`at���`a,���`a ���`cmu1���`a,���`a ���`blw���aoa=���bmia2���`a,���`a ���`elabel���aoa=���bs1a'���bs1qmean population 1���bs1a'���`a)���`a
���`bax���aoa.���`dplot���`a(���`at���`a,���`a ���`cmu2���`a,���`a ���`blw���aoa=���bmia2���`a,���`a ���`elabel���aoa=���bs1a'���bs1qmean population 2���bs1a'���`a)���`a
���`bax���aoa.���`lfill_between���`a(���`at���`a,���`a ���`cmu1���aoa+���`fsigma1���`a,���`a ���`cmu1���aoa-���`fsigma1���`a,���`a ���`ifacecolor���aoa=���bs1a'���bs1bC0���bs1a'���`a,���`a ���`ealpha���aoa=���bmfc0.4���`a)���`a
���`bax���aoa.���`lfill_between���`a(���`at���`a,���`a ���`cmu2���aoa+���`fsigma2���`a,���`a ���`cmu2���aoa-���`fsigma2���`a,���`a ���`ifacecolor���aoa=���bs1a'���bs1bC1���bs1a'���`a,���`a ���`ealpha���aoa=���bmfc0.4���`a)���`a
���`bax���aoa.���`iset_title���`a(���bsaar���bs1a'���bs1xrandom walkers empirical $���bs1a\���bs1imu$ and $���bs1a\���bs1cpm ���bs1a\���bs1osigma$ interval���bs1a'���`a)���`a
���`bax���aoa.���`flegend���`a(���`cloc���aoa=���bs1a'���bs1jupper left���bs1a'���`a)���`a
���`bax���aoa.���`jset_xlabel���`a(���bs1a'���bs1inum steps���bs1a'���`a)���`a
���`bax���aoa.���`jset_ylabel���`a(���bs1a'���bs1hposition���bs1a'���`a)���`a
���`bax���aoa.���`dgrid���`a(���`a)���`a
���`a
���bc1xO###############################################################################���`a
���bc1xG# The ``where`` keyword argument is very handy for highlighting certain���`a
���bc1xG# regions of the graph.  ``where`` takes a boolean mask the same length���`a
���bc1xG# as the x, ymin and ymax arguments, and only fills in the region where���`a
���bc1xG# the boolean mask is True.  In the example below, we simulate a single���`a
���bc1xG# random walker and compute the analytic mean and standard deviation of���`a
���bc1xG# the population positions.  The population mean is shown as the dashed���`a
���bc1xE# line, and the plus/minus one sigma deviation from the mean is shown���`a
���bc1xE# as the filled region.  We use the where mask ``X > upper_bound`` to���`a
���bc1xE# find the region where the walker is outside the one sigma boundary,���`a
���bc1x# and shade that region red.���`a
���`a
���bc1x)# Fixing random state for reproducibility���`a
���`bnp���aoa.���`frandom���aoa.���`dseed���`a(���bmia1���`a)���`a
���`a
���`fNsteps���`a ���aoa=���`a ���bmic500���`a
���`at���`a ���aoa=���`a ���`bnp���aoa.���`farange���`a(���`fNsteps���`a)���`a
���`a
���`bmu���`a ���aoa=���`a ���bmfe0.002���`a
���`esigma���`a ���aoa=���`a ���bmfd0.01���`a
���`a
���bc1x# the steps and position���`a
���`aS���`a ���aoa=���`a ���`bmu���`a ���aoa+���`a ���`esigma���aoa*���`bnp���aoa.���`frandom���aoa.���`erandn���`a(���`fNsteps���`a)���`a
���`aX���`a ���aoa=���`a ���`aS���aoa.���`fcumsum���`a(���`a)���`a
���`a
���bc1x8# the 1 sigma upper and lower analytic population bounds���`a
���`klower_bound���`a ���aoa=���`a ���`bmu���aoa*���`at���`a ���aoa-���`a ���`esigma���aoa*���`bnp���aoa.���`dsqrt���`a(���`at���`a)���`a
���`kupper_bound���`a ���aoa=���`a ���`bmu���aoa*���`at���`a ���aoa+���`a ���`esigma���aoa*���`bnp���aoa.���`dsqrt���`a(���`at���`a)���`a
���`a
���`cfig���`a,���`a ���`bax���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���bmia1���`a)���`a
���`bax���aoa.���`dplot���`a(���`at���`a,���`a ���`aX���`a,���`a ���`blw���aoa=���bmia2���`a,���`a ���`elabel���aoa=���bs1a'���bs1owalker position���bs1a'���`a)���`a
���`bax���aoa.���`dplot���`a(���`at���`a,���`a ���`bmu���aoa*���`at���`a,���`a ���`blw���aoa=���bmia1���`a,���`a ���`elabel���aoa=���bs1a'���bs1opopulation mean���bs1a'���`a,���`a ���`ecolor���aoa=���bs1a'���bs1bC0���bs1a'���`a,���`a ���`bls���aoa=���bs1a'���bs1b--���bs1a'���`a)���`a
���`bax���aoa.���`lfill_between���`a(���`at���`a,���`a ���`klower_bound���`a,���`a ���`kupper_bound���`a,���`a ���`ifacecolor���aoa=���bs1a'���bs1bC0���bs1a'���`a,���`a ���`ealpha���aoa=���bmfc0.4���`a,���`a
���`p                ���`elabel���aoa=���bs1a'���bs1m1 sigma range���bs1a'���`a)���`a
���`bax���aoa.���`flegend���`a(���`cloc���aoa=���bs1a'���bs1jupper left���bs1a'���`a)���`a
���`a
���bc1xB# here we use the where argument to only fill the region where the���`a
���bc1x1# walker is above the population 1 sigma boundary���`a
���`bax���aoa.���`lfill_between���`a(���`at���`a,���`a ���`kupper_bound���`a,���`a ���`aX���`a,���`a ���`ewhere���aoa=���`aX���`a ���aoa>���`a ���`kupper_bound���`a,���`a ���`bfc���aoa=���bs1a'���bs1cred���bs1a'���`a,���`a ���`ealpha���aoa=���bmfc0.4���`a)���`a
���`bax���aoa.���`lfill_between���`a(���`at���`a,���`a ���`klower_bound���`a,���`a ���`aX���`a,���`a ���`ewhere���aoa=���`aX���`a ���aoa<���`a ���`klower_bound���`a,���`a ���`bfc���aoa=���bs1a'���bs1cred���bs1a'���`a,���`a ���`ealpha���aoa=���bmfc0.4���`a)���`a
���`bax���aoa.���`jset_xlabel���`a(���bs1a'���bs1inum steps���bs1a'���`a)���`a
���`bax���aoa.���`jset_ylabel���`a(���bs1a'���bs1hposition���bs1a'���`a)���`a
���`bax���aoa.���`dgrid���`a(���`a)���`a
���`a
���bc1xO###############################################################################���`a
���bc1xL# Another handy use of filled regions is to highlight horizontal or vertical���`a
���bc1xB# spans of an axes -- for that Matplotlib has the helper functions���`a
���bc1xK# `~matplotlib.axes.Axes.axhspan` and `~matplotlib.axes.Axes.axvspan`.  See���`a
���bc1x9# :doc:`/gallery/subplots_axes_and_figures/axhspan_demo`.���`a
���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
`dNone�