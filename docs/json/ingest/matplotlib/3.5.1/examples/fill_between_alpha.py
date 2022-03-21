Ù¯‚Ù´ƒ™ÈÙ±‚bsdy """
Fill Between and Alpha
======================

The `~matplotlib.axes.Axes.fill_between` function generates a shaded
region between a min and max boundary that is useful for illustrating ranges.
It has a very handy ``where`` argument to combine filling with logical ranges,
e.g., to just fill in a curve over some threshold value.

At its most basic level, ``fill_between`` can be use to enhance a graphs visual
appearance. Let's compare two graphs of a financial times with a simple line
plot on the left and a filled line on the right.
"""Ù±‚`a
Ù±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnnfpyplotÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnncpltÙ±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„enumpyÙ „enumpyf1.22.3fmoduleenumpyfmoduleõÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnnbnpÙ±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnnecbookÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnnecbookÙ±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚bc1x$# load up some sample financial dataÙ±‚`a
Ù±‚`arÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`a(Ù±‚`ecbookÙ±‚aoa.Ù±‚`oget_sample_dataÙ±‚`a(Ù±‚bs1a'Ù±‚bs1hgoog.npzÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`gnp_loadÙ±‚aoa=Ù±‚bkcdTrueÙ±‚`a)Ù±‚`a[Ù±‚bs1a'Ù±‚bs1jprice_dataÙ±‚bs1a'Ù±‚`a]Ù±‚`a
Ù±‚`e     Ù±‚aoa.Ù±‚`dviewÙ±‚`a(Ù±‚`bnpÙ±‚aoa.Ù±‚`hrecarrayÙ±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚bc1x2# create two subplots with the shared x and y axesÙ±‚`a
Ù±‚`cfigÙ±‚`a,Ù±‚`a Ù±‚`a(Ù±‚`cax1Ù±‚`a,Ù±‚`a Ù±‚`cax2Ù±‚`a)Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cpltÙ±‚aoa.Ù±‚`hsubplotsÙ±‚`a(Ù±‚bmia1Ù±‚`a,Ù±‚`a Ù±‚bmia2Ù±‚`a,Ù±‚`a Ù±‚`fsharexÙ±‚aoa=Ù±‚bkcdTrueÙ±‚`a,Ù±‚`a Ù±‚`fshareyÙ±‚aoa=Ù±‚bkcdTrueÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`hpriceminÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`arÙ±‚aoa.Ù±‚`ecloseÙ±‚aoa.Ù±‚`cminÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`cax1Ù±‚aoa.Ù±‚`dplotÙ±‚`a(Ù±‚`arÙ±‚aoa.Ù±‚`ddateÙ±‚`a,Ù±‚`a Ù±‚`arÙ±‚aoa.Ù±‚`ecloseÙ±‚`a,Ù±‚`a Ù±‚`blwÙ±‚aoa=Ù±‚bmia2Ù±‚`a)Ù±‚`a
Ù±‚`cax2Ù±‚aoa.Ù±‚`lfill_betweenÙ±‚`a(Ù±‚`arÙ±‚aoa.Ù±‚`ddateÙ±‚`a,Ù±‚`a Ù±‚`hpriceminÙ±‚`a,Ù±‚`a Ù±‚`arÙ±‚aoa.Ù±‚`ecloseÙ±‚`a,Ù±‚`a Ù±‚`ealphaÙ±‚aoa=Ù±‚bmfc0.7Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚akcforÙ±‚`a Ù±‚`baxÙ±‚`a Ù±‚bowbinÙ±‚`a Ù±‚`cax1Ù±‚`a,Ù±‚`a Ù±‚`cax2Ù±‚`a:Ù±‚`a
Ù±‚`d    Ù±‚`baxÙ±‚aoa.Ù±‚`dgridÙ±‚`a(Ù±‚bkcdTrueÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`cax1Ù±‚aoa.Ù±‚`jset_ylabelÙ±‚`a(Ù±‚bs1a'Ù±‚bs1epriceÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚akcforÙ±‚`a Ù±‚`elabelÙ±‚`a Ù±‚bowbinÙ±‚`a Ù±‚`cax2Ù±‚aoa.Ù±‚`oget_yticklabelsÙ±‚`a(Ù±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`d    Ù±‚`elabelÙ±‚aoa.Ù±‚`kset_visibleÙ±‚`a(Ù±‚bkceFalseÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`cfigÙ±‚aoa.Ù±‚`hsuptitleÙ±‚`a(Ù±‚bs1a'Ù±‚bs1x!Google (GOOG) daily closing priceÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`cfigÙ±‚aoa.Ù±‚`mautofmt_xdateÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚bc1xO###############################################################################Ù±‚`a
Ù±‚bc1xG# The alpha channel is not necessary here, but it can be used to softenÙ±‚`a
Ù±‚bc1xH# colors for more visually appealing plots.  In other examples, as we'llÙ±‚`a
Ù±‚bc1xC# see below, the alpha channel is functionally useful as the shadedÙ±‚`a
Ù±‚bc1xF# regions can overlap and alpha allows you to see both.  Note that theÙ±‚`a
Ù±‚bc1x@# postscript format does not support alpha (this is a postscriptÙ±‚`a
Ù±‚bc1xD# limitation, not a matplotlib limitation), so when using alpha saveÙ±‚`a
Ù±‚bc1x"# your figures in PNG, PDF or SVG.Ù±‚`a
Ù±‚bc1a#Ù±‚`a
Ù±‚bc1xD# Our next example computes two populations of random walkers with aÙ±‚`a
Ù±‚bc1xH# different mean and standard deviation of the normal distributions fromÙ±‚`a
Ù±‚bc1xC# which the steps are drawn.  We use filled regions to plot +/- oneÙ±‚`a
Ù±‚bc1xF# standard deviation of the mean position of the population.  Here theÙ±‚`a
Ù±‚bc1x.# alpha channel is useful, not just aesthetic.Ù±‚`a
Ù±‚`a
Ù±‚bc1x)# Fixing random state for reproducibilityÙ±‚`a
Ù±‚`bnpÙ±‚aoa.Ù±‚`frandomÙ±‚aoa.Ù±‚`dseedÙ±‚`a(Ù±‚bmih19680801Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`fNstepsÙ±‚`a,Ù±‚`a Ù±‚`hNwalkersÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bmic100Ù±‚`a,Ù±‚`a Ù±‚bmic250Ù±‚`a
Ù±‚`atÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`farangeÙ±‚`a(Ù±‚`fNstepsÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚bc1x3# an (Nsteps x Nwalkers) array of random walk stepsÙ±‚`a
Ù±‚`bS1Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bmfe0.004Ù±‚`a Ù±‚aoa+Ù±‚`a Ù±‚bmfd0.02Ù±‚aoa*Ù±‚`bnpÙ±‚aoa.Ù±‚`frandomÙ±‚aoa.Ù±‚`erandnÙ±‚`a(Ù±‚`fNstepsÙ±‚`a,Ù±‚`a Ù±‚`hNwalkersÙ±‚`a)Ù±‚`a
Ù±‚`bS2Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bmfe0.002Ù±‚`a Ù±‚aoa+Ù±‚`a Ù±‚bmfd0.01Ù±‚aoa*Ù±‚`bnpÙ±‚aoa.Ù±‚`frandomÙ±‚aoa.Ù±‚`erandnÙ±‚`a(Ù±‚`fNstepsÙ±‚`a,Ù±‚`a Ù±‚`hNwalkersÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚bc1x9# an (Nsteps x Nwalkers) array of random walker positionsÙ±‚`a
Ù±‚`bX1Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bS1Ù±‚aoa.Ù±‚`fcumsumÙ±‚`a(Ù±‚`daxisÙ±‚aoa=Ù±‚bmia0Ù±‚`a)Ù±‚`a
Ù±‚`bX2Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bS2Ù±‚aoa.Ù±‚`fcumsumÙ±‚`a(Ù±‚`daxisÙ±‚aoa=Ù±‚bmia0Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚bc1xF# Nsteps length arrays empirical means and standard deviations of bothÙ±‚`a
Ù±‚bc1w# populations over timeÙ±‚`a
Ù±‚`cmu1Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bX1Ù±‚aoa.Ù±‚`dmeanÙ±‚`a(Ù±‚`daxisÙ±‚aoa=Ù±‚bmia1Ù±‚`a)Ù±‚`a
Ù±‚`fsigma1Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bX1Ù±‚aoa.Ù±‚`cstdÙ±‚`a(Ù±‚`daxisÙ±‚aoa=Ù±‚bmia1Ù±‚`a)Ù±‚`a
Ù±‚`cmu2Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bX2Ù±‚aoa.Ù±‚`dmeanÙ±‚`a(Ù±‚`daxisÙ±‚aoa=Ù±‚bmia1Ù±‚`a)Ù±‚`a
Ù±‚`fsigma2Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bX2Ù±‚aoa.Ù±‚`cstdÙ±‚`a(Ù±‚`daxisÙ±‚aoa=Ù±‚bmia1Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚bc1j# plot it!Ù±‚`a
Ù±‚`cfigÙ±‚`a,Ù±‚`a Ù±‚`baxÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cpltÙ±‚aoa.Ù±‚`hsubplotsÙ±‚`a(Ù±‚bmia1Ù±‚`a)Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`dplotÙ±‚`a(Ù±‚`atÙ±‚`a,Ù±‚`a Ù±‚`cmu1Ù±‚`a,Ù±‚`a Ù±‚`blwÙ±‚aoa=Ù±‚bmia2Ù±‚`a,Ù±‚`a Ù±‚`elabelÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1qmean population 1Ù±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`dplotÙ±‚`a(Ù±‚`atÙ±‚`a,Ù±‚`a Ù±‚`cmu2Ù±‚`a,Ù±‚`a Ù±‚`blwÙ±‚aoa=Ù±‚bmia2Ù±‚`a,Ù±‚`a Ù±‚`elabelÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1qmean population 2Ù±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`lfill_betweenÙ±‚`a(Ù±‚`atÙ±‚`a,Ù±‚`a Ù±‚`cmu1Ù±‚aoa+Ù±‚`fsigma1Ù±‚`a,Ù±‚`a Ù±‚`cmu1Ù±‚aoa-Ù±‚`fsigma1Ù±‚`a,Ù±‚`a Ù±‚`ifacecolorÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1bC0Ù±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`ealphaÙ±‚aoa=Ù±‚bmfc0.4Ù±‚`a)Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`lfill_betweenÙ±‚`a(Ù±‚`atÙ±‚`a,Ù±‚`a Ù±‚`cmu2Ù±‚aoa+Ù±‚`fsigma2Ù±‚`a,Ù±‚`a Ù±‚`cmu2Ù±‚aoa-Ù±‚`fsigma2Ù±‚`a,Ù±‚`a Ù±‚`ifacecolorÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1bC1Ù±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`ealphaÙ±‚aoa=Ù±‚bmfc0.4Ù±‚`a)Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`iset_titleÙ±‚`a(Ù±‚bsaarÙ±‚bs1a'Ù±‚bs1xrandom walkers empirical $Ù±‚bs1a\Ù±‚bs1imu$ and $Ù±‚bs1a\Ù±‚bs1cpm Ù±‚bs1a\Ù±‚bs1osigma$ intervalÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`flegendÙ±‚`a(Ù±‚`clocÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1jupper leftÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`jset_xlabelÙ±‚`a(Ù±‚bs1a'Ù±‚bs1inum stepsÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`jset_ylabelÙ±‚`a(Ù±‚bs1a'Ù±‚bs1hpositionÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`dgridÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚bc1xO###############################################################################Ù±‚`a
Ù±‚bc1xG# The ``where`` keyword argument is very handy for highlighting certainÙ±‚`a
Ù±‚bc1xG# regions of the graph.  ``where`` takes a boolean mask the same lengthÙ±‚`a
Ù±‚bc1xG# as the x, ymin and ymax arguments, and only fills in the region whereÙ±‚`a
Ù±‚bc1xG# the boolean mask is True.  In the example below, we simulate a singleÙ±‚`a
Ù±‚bc1xG# random walker and compute the analytic mean and standard deviation ofÙ±‚`a
Ù±‚bc1xG# the population positions.  The population mean is shown as the dashedÙ±‚`a
Ù±‚bc1xE# line, and the plus/minus one sigma deviation from the mean is shownÙ±‚`a
Ù±‚bc1xE# as the filled region.  We use the where mask ``X > upper_bound`` toÙ±‚`a
Ù±‚bc1xE# find the region where the walker is outside the one sigma boundary,Ù±‚`a
Ù±‚bc1x# and shade that region red.Ù±‚`a
Ù±‚`a
Ù±‚bc1x)# Fixing random state for reproducibilityÙ±‚`a
Ù±‚`bnpÙ±‚aoa.Ù±‚`frandomÙ±‚aoa.Ù±‚`dseedÙ±‚`a(Ù±‚bmia1Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`fNstepsÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bmic500Ù±‚`a
Ù±‚`atÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`farangeÙ±‚`a(Ù±‚`fNstepsÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`bmuÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bmfe0.002Ù±‚`a
Ù±‚`esigmaÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bmfd0.01Ù±‚`a
Ù±‚`a
Ù±‚bc1x# the steps and positionÙ±‚`a
Ù±‚`aSÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bmuÙ±‚`a Ù±‚aoa+Ù±‚`a Ù±‚`esigmaÙ±‚aoa*Ù±‚`bnpÙ±‚aoa.Ù±‚`frandomÙ±‚aoa.Ù±‚`erandnÙ±‚`a(Ù±‚`fNstepsÙ±‚`a)Ù±‚`a
Ù±‚`aXÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`aSÙ±‚aoa.Ù±‚`fcumsumÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚bc1x8# the 1 sigma upper and lower analytic population boundsÙ±‚`a
Ù±‚`klower_boundÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bmuÙ±‚aoa*Ù±‚`atÙ±‚`a Ù±‚aoa-Ù±‚`a Ù±‚`esigmaÙ±‚aoa*Ù±‚`bnpÙ±‚aoa.Ù±‚`dsqrtÙ±‚`a(Ù±‚`atÙ±‚`a)Ù±‚`a
Ù±‚`kupper_boundÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bmuÙ±‚aoa*Ù±‚`atÙ±‚`a Ù±‚aoa+Ù±‚`a Ù±‚`esigmaÙ±‚aoa*Ù±‚`bnpÙ±‚aoa.Ù±‚`dsqrtÙ±‚`a(Ù±‚`atÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`cfigÙ±‚`a,Ù±‚`a Ù±‚`baxÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cpltÙ±‚aoa.Ù±‚`hsubplotsÙ±‚`a(Ù±‚bmia1Ù±‚`a)Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`dplotÙ±‚`a(Ù±‚`atÙ±‚`a,Ù±‚`a Ù±‚`aXÙ±‚`a,Ù±‚`a Ù±‚`blwÙ±‚aoa=Ù±‚bmia2Ù±‚`a,Ù±‚`a Ù±‚`elabelÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1owalker positionÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`dplotÙ±‚`a(Ù±‚`atÙ±‚`a,Ù±‚`a Ù±‚`bmuÙ±‚aoa*Ù±‚`atÙ±‚`a,Ù±‚`a Ù±‚`blwÙ±‚aoa=Ù±‚bmia1Ù±‚`a,Ù±‚`a Ù±‚`elabelÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1opopulation meanÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`ecolorÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1bC0Ù±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`blsÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1b--Ù±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`lfill_betweenÙ±‚`a(Ù±‚`atÙ±‚`a,Ù±‚`a Ù±‚`klower_boundÙ±‚`a,Ù±‚`a Ù±‚`kupper_boundÙ±‚`a,Ù±‚`a Ù±‚`ifacecolorÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1bC0Ù±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`ealphaÙ±‚aoa=Ù±‚bmfc0.4Ù±‚`a,Ù±‚`a
Ù±‚`p                Ù±‚`elabelÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1m1 sigma rangeÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`flegendÙ±‚`a(Ù±‚`clocÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1jupper leftÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚bc1xB# here we use the where argument to only fill the region where theÙ±‚`a
Ù±‚bc1x1# walker is above the population 1 sigma boundaryÙ±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`lfill_betweenÙ±‚`a(Ù±‚`atÙ±‚`a,Ù±‚`a Ù±‚`kupper_boundÙ±‚`a,Ù±‚`a Ù±‚`aXÙ±‚`a,Ù±‚`a Ù±‚`ewhereÙ±‚aoa=Ù±‚`aXÙ±‚`a Ù±‚aoa>Ù±‚`a Ù±‚`kupper_boundÙ±‚`a,Ù±‚`a Ù±‚`bfcÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1credÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`ealphaÙ±‚aoa=Ù±‚bmfc0.4Ù±‚`a)Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`lfill_betweenÙ±‚`a(Ù±‚`atÙ±‚`a,Ù±‚`a Ù±‚`klower_boundÙ±‚`a,Ù±‚`a Ù±‚`aXÙ±‚`a,Ù±‚`a Ù±‚`ewhereÙ±‚aoa=Ù±‚`aXÙ±‚`a Ù±‚aoa<Ù±‚`a Ù±‚`klower_boundÙ±‚`a,Ù±‚`a Ù±‚`bfcÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1credÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`ealphaÙ±‚aoa=Ù±‚bmfc0.4Ù±‚`a)Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`jset_xlabelÙ±‚`a(Ù±‚bs1a'Ù±‚bs1inum stepsÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`jset_ylabelÙ±‚`a(Ù±‚bs1a'Ù±‚bs1hpositionÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`dgridÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚bc1xO###############################################################################Ù±‚`a
Ù±‚bc1xL# Another handy use of filled regions is to highlight horizontal or verticalÙ±‚`a
Ù±‚bc1xB# spans of an axes -- for that Matplotlib has the helper functionsÙ±‚`a
Ù±‚bc1xK# `~matplotlib.axes.Axes.axhspan` and `~matplotlib.axes.Axes.axvspan`.  SeeÙ±‚`a
Ù±‚bc1x9# :doc:`/gallery/subplots_axes_and_figures/axhspan_demo`.Ù±‚`a
Ù±‚`a
Ù±‚`cpltÙ±‚aoa.Ù±‚`dshowÙ±‚`a(Ù±‚`a)Ù±‚`a
`dNoneö