ŸØÇÅŸ¥Éô⁄Ÿ±Çbsdyf"""
===========
Arrow guide
===========

Adding arrow patches to plots.

Arrows are often used to annotate plots. This tutorial shows how to plot arrows
that behave differently when the data limits on a plot are changed. In general,
points on a plot can either be fixed in "data space" or "display space".
Something plotted in data space moves when the data limits are altered - an
example would be the points in a scatter plot. Something plotted in display
space stays static when data limits are altered - an example would be a
figure title or the axis labels.

Arrows consist of a head (and possibly a tail) and a stem drawn between a
start point and end point, called 'anchor points' from now on.
Here we show three use cases for plotting arrows, depending on whether the
head or anchor points need to be fixed in data or display space:

1. Head shape fixed in display space, anchor points fixed in data space
2. Head shape and anchor points fixed in display space
3. Entire patch fixed in data space

Below each use case is presented in turn.

.. redirect-from:: /gallery/text_labels_and_annotations/arrow_simple_demo
"""Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±ÇbknfimportŸ±Ç`a Ÿ±ÇbnnŸ¢ÑjmatplotlibŸ†Ñjmatplotlibe3.5.1fmodulejmatplotlibfmoduleıŸ±Çbnna.Ÿ±ÇbnngpatchesŸ±Ç`a Ÿ±ÇakbasŸ±Ç`a Ÿ±ÇbnnhmpatchesŸ±Ç`a
Ÿ±ÇbknfimportŸ±Ç`a Ÿ±ÇbnnŸ¢ÑjmatplotlibŸ†Ñjmatplotlibe3.5.1fmodulejmatplotlibfmoduleıŸ±Çbnna.Ÿ±ÇbnnfpyplotŸ±Ç`a Ÿ±ÇakbasŸ±Ç`a Ÿ±ÇbnncpltŸ±Ç`a
Ÿ±Ç`fx_tailŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Çbmfc0.1Ÿ±Ç`a
Ÿ±Ç`fy_tailŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Çbmfc0.5Ÿ±Ç`a
Ÿ±Ç`fx_headŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Çbmfc0.9Ÿ±Ç`a
Ÿ±Ç`fy_headŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Çbmfc0.8Ÿ±Ç`a
Ÿ±Ç`bdxŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`fx_headŸ±Ç`a Ÿ±Çaoa-Ÿ±Ç`a Ÿ±Ç`fx_tailŸ±Ç`a
Ÿ±Ç`bdyŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`fy_headŸ±Ç`a Ÿ±Çaoa-Ÿ±Ç`a Ÿ±Ç`fy_tailŸ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1xO###############################################################################Ÿ±Ç`a
Ÿ±Çbc1xI# Head shape fixed in display space and anchor points fixed in data spaceŸ±Ç`a
Ÿ±Çbc1xI# -----------------------------------------------------------------------Ÿ±Ç`a
Ÿ±Çbc1a#Ÿ±Ç`a
Ÿ±Çbc1xJ# This is useful if you are annotating a plot, and don't want the arrow toŸ±Ç`a
Ÿ±Çbc1x;# to change shape or position if you pan or scale the plot.Ÿ±Ç`a
Ÿ±Çbc1a#Ÿ±Ç`a
Ÿ±Çbc1x1# In this case we use `.patches.FancyArrowPatch`.Ÿ±Ç`a
Ÿ±Çbc1a#Ÿ±Ç`a
Ÿ±Çbc1xM# Note that when the axis limits are changed, the arrow shape stays the same,Ÿ±Ç`a
Ÿ±Çbc1x# but the anchor points move.Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`cfigŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`caxsŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`hsubplotsŸ±Ç`a(Ÿ±Ç`enrowsŸ±Çaoa=Ÿ±Çbmia2Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`earrowŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`hmpatchesŸ±Çaoa.Ÿ±Ç`oFancyArrowPatchŸ±Ç`a(Ÿ±Ç`a(Ÿ±Ç`fx_tailŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`fy_tailŸ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`a(Ÿ±Ç`fx_headŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`fy_headŸ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`x!                                 Ÿ±Ç`nmutation_scaleŸ±Çaoa=Ÿ±Çbmic100Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`caxsŸ±Ç`a[Ÿ±Çbmia0Ÿ±Ç`a]Ÿ±Çaoa.Ÿ±Ç`iadd_patchŸ±Ç`a(Ÿ±Ç`earrowŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`earrowŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`hmpatchesŸ±Çaoa.Ÿ±Ç`oFancyArrowPatchŸ±Ç`a(Ÿ±Ç`a(Ÿ±Ç`fx_tailŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`fy_tailŸ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`a(Ÿ±Ç`fx_headŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`fy_headŸ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`x!                                 Ÿ±Ç`nmutation_scaleŸ±Çaoa=Ÿ±Çbmic100Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`caxsŸ±Ç`a[Ÿ±Çbmia1Ÿ±Ç`a]Ÿ±Çaoa.Ÿ±Ç`iadd_patchŸ±Ç`a(Ÿ±Ç`earrowŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`caxsŸ±Ç`a[Ÿ±Çbmia1Ÿ±Ç`a]Ÿ±Çaoa.Ÿ±Ç`csetŸ±Ç`a(Ÿ±Ç`dxlimŸ±Çaoa=Ÿ±Ç`a(Ÿ±Çbmia0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia2Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dylimŸ±Çaoa=Ÿ±Ç`a(Ÿ±Çbmia0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia2Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1xO###############################################################################Ÿ±Ç`a
Ÿ±Çbc1x5# Head shape and anchor points fixed in display spaceŸ±Ç`a
Ÿ±Çbc1x5# ---------------------------------------------------Ÿ±Ç`a
Ÿ±Çbc1a#Ÿ±Ç`a
Ÿ±Çbc1xJ# This is useful if you are annotating a plot, and don't want the arrow toŸ±Ç`a
Ÿ±Çbc1x8# change shape or position if you pan or scale the plot.Ÿ±Ç`a
Ÿ±Çbc1a#Ÿ±Ç`a
Ÿ±Çbc1xO# In this case we use `.patches.FancyArrowPatch`, and pass the keyword argumentŸ±Ç`a
Ÿ±Çbc1xM# ``transform=ax.transAxes`` where ``ax`` is the axes we are adding the patchŸ±Ç`a
Ÿ±Çbc1e# to.Ÿ±Ç`a
Ÿ±Çbc1a#Ÿ±Ç`a
Ÿ±Çbc1xJ# Note that when the axis limits are changed, the arrow shape and locationŸ±Ç`a
Ÿ±Çbc1p# stay the same.Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`cfigŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`caxsŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`hsubplotsŸ±Ç`a(Ÿ±Ç`enrowsŸ±Çaoa=Ÿ±Çbmia2Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`earrowŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`hmpatchesŸ±Çaoa.Ÿ±Ç`oFancyArrowPatchŸ±Ç`a(Ÿ±Ç`a(Ÿ±Ç`fx_tailŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`fy_tailŸ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`a(Ÿ±Ç`fx_headŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`fy_headŸ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`x!                                 Ÿ±Ç`nmutation_scaleŸ±Çaoa=Ÿ±Çbmic100Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`x!                                 Ÿ±Ç`itransformŸ±Çaoa=Ÿ±Ç`caxsŸ±Ç`a[Ÿ±Çbmia0Ÿ±Ç`a]Ÿ±Çaoa.Ÿ±Ç`itransAxesŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`caxsŸ±Ç`a[Ÿ±Çbmia0Ÿ±Ç`a]Ÿ±Çaoa.Ÿ±Ç`iadd_patchŸ±Ç`a(Ÿ±Ç`earrowŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`earrowŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`hmpatchesŸ±Çaoa.Ÿ±Ç`oFancyArrowPatchŸ±Ç`a(Ÿ±Ç`a(Ÿ±Ç`fx_tailŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`fy_tailŸ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`a(Ÿ±Ç`fx_headŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`fy_headŸ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`x!                                 Ÿ±Ç`nmutation_scaleŸ±Çaoa=Ÿ±Çbmic100Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`x!                                 Ÿ±Ç`itransformŸ±Çaoa=Ÿ±Ç`caxsŸ±Ç`a[Ÿ±Çbmia1Ÿ±Ç`a]Ÿ±Çaoa.Ÿ±Ç`itransAxesŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`caxsŸ±Ç`a[Ÿ±Çbmia1Ÿ±Ç`a]Ÿ±Çaoa.Ÿ±Ç`iadd_patchŸ±Ç`a(Ÿ±Ç`earrowŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`caxsŸ±Ç`a[Ÿ±Çbmia1Ÿ±Ç`a]Ÿ±Çaoa.Ÿ±Ç`csetŸ±Ç`a(Ÿ±Ç`dxlimŸ±Çaoa=Ÿ±Ç`a(Ÿ±Çbmia0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia2Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dylimŸ±Çaoa=Ÿ±Ç`a(Ÿ±Çbmia0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia2Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1xO###############################################################################Ÿ±Ç`a
Ÿ±Çbc1x2# Head shape and anchor points fixed in data spaceŸ±Ç`a
Ÿ±Çbc1x2# ------------------------------------------------Ÿ±Ç`a
Ÿ±Çbc1a#Ÿ±Ç`a
Ÿ±Çbc1xO# In this case we use `.patches.Arrow`, or `.patches.FancyArrow` (the latter isŸ±Ç`a
Ÿ±Çbc1m# in orange).Ÿ±Ç`a
Ÿ±Çbc1a#Ÿ±Ç`a
Ÿ±Çbc1xJ# Note that when the axis limits are changed, the arrow shape and locationŸ±Ç`a
Ÿ±Çbc1i# change.Ÿ±Ç`a
Ÿ±Çbc1a#Ÿ±Ç`a
Ÿ±Çbc1xO# `.FancyArrow`'s API is relatively awkward, and requires in particular passingŸ±Ç`a
Ÿ±Çbc1xL# ``length_includes_head=True`` so that the arrow *tip* is ``(dx, dy)`` awayŸ±Ç`a
Ÿ±Çbc1xL# from the arrow start.  It is only included in this reference because it isŸ±Ç`a
Ÿ±Çbc1x7# the arrow class returned by `.Axes.arrow` (in green).Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`cfigŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`caxsŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`hsubplotsŸ±Ç`a(Ÿ±Ç`enrowsŸ±Çaoa=Ÿ±Çbmia2Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`earrowŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`hmpatchesŸ±Çaoa.Ÿ±Ç`eArrowŸ±Ç`a(Ÿ±Ç`fx_tailŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`fy_tailŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`bdxŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`bdyŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`caxsŸ±Ç`a[Ÿ±Çbmia0Ÿ±Ç`a]Ÿ±Çaoa.Ÿ±Ç`iadd_patchŸ±Ç`a(Ÿ±Ç`earrowŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`earrowŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`hmpatchesŸ±Çaoa.Ÿ±Ç`jFancyArrowŸ±Ç`a(Ÿ±Ç`fx_tailŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`fy_tailŸ±Ç`a Ÿ±Çaoa-Ÿ±Ç`a Ÿ±Çbmfb.4Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`bdxŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`bdyŸ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`x                            Ÿ±Ç`ewidthŸ±Çaoa=Ÿ±Çbmfb.1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`tlength_includes_headŸ±Çaoa=Ÿ±ÇbkcdTrueŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ecolorŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2bC1Ÿ±Çbs2a"Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`caxsŸ±Ç`a[Ÿ±Çbmia0Ÿ±Ç`a]Ÿ±Çaoa.Ÿ±Ç`iadd_patchŸ±Ç`a(Ÿ±Ç`earrowŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`caxsŸ±Ç`a[Ÿ±Çbmia0Ÿ±Ç`a]Ÿ±Çaoa.Ÿ±Ç`earrowŸ±Ç`a(Ÿ±Ç`fx_tailŸ±Ç`a Ÿ±Çaoa+Ÿ±Ç`a Ÿ±Çbmia1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`fy_tailŸ±Ç`a Ÿ±Çaoa-Ÿ±Ç`a Ÿ±Çbmfb.4Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`bdxŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`bdyŸ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`m             Ÿ±Ç`ewidthŸ±Çaoa=Ÿ±Çbmfb.1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`tlength_includes_headŸ±Çaoa=Ÿ±ÇbkcdTrueŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ecolorŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2bC2Ÿ±Çbs2a"Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`earrowŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`hmpatchesŸ±Çaoa.Ÿ±Ç`eArrowŸ±Ç`a(Ÿ±Ç`fx_tailŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`fy_tailŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`bdxŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`bdyŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`caxsŸ±Ç`a[Ÿ±Çbmia1Ÿ±Ç`a]Ÿ±Çaoa.Ÿ±Ç`iadd_patchŸ±Ç`a(Ÿ±Ç`earrowŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`earrowŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`hmpatchesŸ±Çaoa.Ÿ±Ç`jFancyArrowŸ±Ç`a(Ÿ±Ç`fx_tailŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`fy_tailŸ±Ç`a Ÿ±Çaoa-Ÿ±Ç`a Ÿ±Çbmfb.4Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`bdxŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`bdyŸ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`x                            Ÿ±Ç`ewidthŸ±Çaoa=Ÿ±Çbmfb.1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`tlength_includes_headŸ±Çaoa=Ÿ±ÇbkcdTrueŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ecolorŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2bC1Ÿ±Çbs2a"Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`caxsŸ±Ç`a[Ÿ±Çbmia1Ÿ±Ç`a]Ÿ±Çaoa.Ÿ±Ç`iadd_patchŸ±Ç`a(Ÿ±Ç`earrowŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`caxsŸ±Ç`a[Ÿ±Çbmia1Ÿ±Ç`a]Ÿ±Çaoa.Ÿ±Ç`earrowŸ±Ç`a(Ÿ±Ç`fx_tailŸ±Ç`a Ÿ±Çaoa+Ÿ±Ç`a Ÿ±Çbmia1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`fy_tailŸ±Ç`a Ÿ±Çaoa-Ÿ±Ç`a Ÿ±Çbmfb.4Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`bdxŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`bdyŸ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`m             Ÿ±Ç`ewidthŸ±Çaoa=Ÿ±Çbmfb.1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`tlength_includes_headŸ±Çaoa=Ÿ±ÇbkcdTrueŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ecolorŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2bC2Ÿ±Çbs2a"Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`caxsŸ±Ç`a[Ÿ±Çbmia1Ÿ±Ç`a]Ÿ±Çaoa.Ÿ±Ç`csetŸ±Ç`a(Ÿ±Ç`dxlimŸ±Çaoa=Ÿ±Ç`a(Ÿ±Çbmia0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia2Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dylimŸ±Çaoa=Ÿ±Ç`a(Ÿ±Çbmia0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia2Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1xO###############################################################################Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`dshowŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
`dNoneˆ