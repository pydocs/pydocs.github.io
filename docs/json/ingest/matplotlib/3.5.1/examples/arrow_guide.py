������������bsdyf"""
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
"""���`a
���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnngpatches���`a ���akbas���`a ���bnnhmpatches���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���`fx_tail���`a ���aoa=���`a ���bmfc0.1���`a
���`fy_tail���`a ���aoa=���`a ���bmfc0.5���`a
���`fx_head���`a ���aoa=���`a ���bmfc0.9���`a
���`fy_head���`a ���aoa=���`a ���bmfc0.8���`a
���`bdx���`a ���aoa=���`a ���`fx_head���`a ���aoa-���`a ���`fx_tail���`a
���`bdy���`a ���aoa=���`a ���`fy_head���`a ���aoa-���`a ���`fy_tail���`a
���`a
���`a
���bc1xO###############################################################################���`a
���bc1xI# Head shape fixed in display space and anchor points fixed in data space���`a
���bc1xI# -----------------------------------------------------------------------���`a
���bc1a#���`a
���bc1xJ# This is useful if you are annotating a plot, and don't want the arrow to���`a
���bc1x;# to change shape or position if you pan or scale the plot.���`a
���bc1a#���`a
���bc1x1# In this case we use `.patches.FancyArrowPatch`.���`a
���bc1a#���`a
���bc1xM# Note that when the axis limits are changed, the arrow shape stays the same,���`a
���bc1x# but the anchor points move.���`a
���`a
���`cfig���`a,���`a ���`caxs���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`enrows���aoa=���bmia2���`a)���`a
���`earrow���`a ���aoa=���`a ���`hmpatches���aoa.���`oFancyArrowPatch���`a(���`a(���`fx_tail���`a,���`a ���`fy_tail���`a)���`a,���`a ���`a(���`fx_head���`a,���`a ���`fy_head���`a)���`a,���`a
���`x!                                 ���`nmutation_scale���aoa=���bmic100���`a)���`a
���`caxs���`a[���bmia0���`a]���aoa.���`iadd_patch���`a(���`earrow���`a)���`a
���`a
���`earrow���`a ���aoa=���`a ���`hmpatches���aoa.���`oFancyArrowPatch���`a(���`a(���`fx_tail���`a,���`a ���`fy_tail���`a)���`a,���`a ���`a(���`fx_head���`a,���`a ���`fy_head���`a)���`a,���`a
���`x!                                 ���`nmutation_scale���aoa=���bmic100���`a)���`a
���`caxs���`a[���bmia1���`a]���aoa.���`iadd_patch���`a(���`earrow���`a)���`a
���`caxs���`a[���bmia1���`a]���aoa.���`cset���`a(���`dxlim���aoa=���`a(���bmia0���`a,���`a ���bmia2���`a)���`a,���`a ���`dylim���aoa=���`a(���bmia0���`a,���`a ���bmia2���`a)���`a)���`a
���`a
���bc1xO###############################################################################���`a
���bc1x5# Head shape and anchor points fixed in display space���`a
���bc1x5# ---------------------------------------------------���`a
���bc1a#���`a
���bc1xJ# This is useful if you are annotating a plot, and don't want the arrow to���`a
���bc1x8# change shape or position if you pan or scale the plot.���`a
���bc1a#���`a
���bc1xO# In this case we use `.patches.FancyArrowPatch`, and pass the keyword argument���`a
���bc1xM# ``transform=ax.transAxes`` where ``ax`` is the axes we are adding the patch���`a
���bc1e# to.���`a
���bc1a#���`a
���bc1xJ# Note that when the axis limits are changed, the arrow shape and location���`a
���bc1p# stay the same.���`a
���`a
���`cfig���`a,���`a ���`caxs���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`enrows���aoa=���bmia2���`a)���`a
���`earrow���`a ���aoa=���`a ���`hmpatches���aoa.���`oFancyArrowPatch���`a(���`a(���`fx_tail���`a,���`a ���`fy_tail���`a)���`a,���`a ���`a(���`fx_head���`a,���`a ���`fy_head���`a)���`a,���`a
���`x!                                 ���`nmutation_scale���aoa=���bmic100���`a,���`a
���`x!                                 ���`itransform���aoa=���`caxs���`a[���bmia0���`a]���aoa.���`itransAxes���`a)���`a
���`caxs���`a[���bmia0���`a]���aoa.���`iadd_patch���`a(���`earrow���`a)���`a
���`a
���`earrow���`a ���aoa=���`a ���`hmpatches���aoa.���`oFancyArrowPatch���`a(���`a(���`fx_tail���`a,���`a ���`fy_tail���`a)���`a,���`a ���`a(���`fx_head���`a,���`a ���`fy_head���`a)���`a,���`a
���`x!                                 ���`nmutation_scale���aoa=���bmic100���`a,���`a
���`x!                                 ���`itransform���aoa=���`caxs���`a[���bmia1���`a]���aoa.���`itransAxes���`a)���`a
���`caxs���`a[���bmia1���`a]���aoa.���`iadd_patch���`a(���`earrow���`a)���`a
���`caxs���`a[���bmia1���`a]���aoa.���`cset���`a(���`dxlim���aoa=���`a(���bmia0���`a,���`a ���bmia2���`a)���`a,���`a ���`dylim���aoa=���`a(���bmia0���`a,���`a ���bmia2���`a)���`a)���`a
���`a
���`a
���bc1xO###############################################################################���`a
���bc1x2# Head shape and anchor points fixed in data space���`a
���bc1x2# ------------------------------------------------���`a
���bc1a#���`a
���bc1xO# In this case we use `.patches.Arrow`, or `.patches.FancyArrow` (the latter is���`a
���bc1m# in orange).���`a
���bc1a#���`a
���bc1xJ# Note that when the axis limits are changed, the arrow shape and location���`a
���bc1i# change.���`a
���bc1a#���`a
���bc1xO# `.FancyArrow`'s API is relatively awkward, and requires in particular passing���`a
���bc1xL# ``length_includes_head=True`` so that the arrow *tip* is ``(dx, dy)`` away���`a
���bc1xL# from the arrow start.  It is only included in this reference because it is���`a
���bc1x7# the arrow class returned by `.Axes.arrow` (in green).���`a
���`a
���`cfig���`a,���`a ���`caxs���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`enrows���aoa=���bmia2���`a)���`a
���`a
���`earrow���`a ���aoa=���`a ���`hmpatches���aoa.���`eArrow���`a(���`fx_tail���`a,���`a ���`fy_tail���`a,���`a ���`bdx���`a,���`a ���`bdy���`a)���`a
���`caxs���`a[���bmia0���`a]���aoa.���`iadd_patch���`a(���`earrow���`a)���`a
���`earrow���`a ���aoa=���`a ���`hmpatches���aoa.���`jFancyArrow���`a(���`fx_tail���`a,���`a ���`fy_tail���`a ���aoa-���`a ���bmfb.4���`a,���`a ���`bdx���`a,���`a ���`bdy���`a,���`a
���`x                            ���`ewidth���aoa=���bmfb.1���`a,���`a ���`tlength_includes_head���aoa=���bkcdTrue���`a,���`a ���`ecolor���aoa=���bs2a"���bs2bC1���bs2a"���`a)���`a
���`caxs���`a[���bmia0���`a]���aoa.���`iadd_patch���`a(���`earrow���`a)���`a
���`caxs���`a[���bmia0���`a]���aoa.���`earrow���`a(���`fx_tail���`a ���aoa+���`a ���bmia1���`a,���`a ���`fy_tail���`a ���aoa-���`a ���bmfb.4���`a,���`a ���`bdx���`a,���`a ���`bdy���`a,���`a
���`m             ���`ewidth���aoa=���bmfb.1���`a,���`a ���`tlength_includes_head���aoa=���bkcdTrue���`a,���`a ���`ecolor���aoa=���bs2a"���bs2bC2���bs2a"���`a)���`a
���`a
���`earrow���`a ���aoa=���`a ���`hmpatches���aoa.���`eArrow���`a(���`fx_tail���`a,���`a ���`fy_tail���`a,���`a ���`bdx���`a,���`a ���`bdy���`a)���`a
���`caxs���`a[���bmia1���`a]���aoa.���`iadd_patch���`a(���`earrow���`a)���`a
���`earrow���`a ���aoa=���`a ���`hmpatches���aoa.���`jFancyArrow���`a(���`fx_tail���`a,���`a ���`fy_tail���`a ���aoa-���`a ���bmfb.4���`a,���`a ���`bdx���`a,���`a ���`bdy���`a,���`a
���`x                            ���`ewidth���aoa=���bmfb.1���`a,���`a ���`tlength_includes_head���aoa=���bkcdTrue���`a,���`a ���`ecolor���aoa=���bs2a"���bs2bC1���bs2a"���`a)���`a
���`caxs���`a[���bmia1���`a]���aoa.���`iadd_patch���`a(���`earrow���`a)���`a
���`caxs���`a[���bmia1���`a]���aoa.���`earrow���`a(���`fx_tail���`a ���aoa+���`a ���bmia1���`a,���`a ���`fy_tail���`a ���aoa-���`a ���bmfb.4���`a,���`a ���`bdx���`a,���`a ���`bdy���`a,���`a
���`m             ���`ewidth���aoa=���bmfb.1���`a,���`a ���`tlength_includes_head���aoa=���bkcdTrue���`a,���`a ���`ecolor���aoa=���bs2a"���bs2bC2���bs2a"���`a)���`a
���`caxs���`a[���bmia1���`a]���aoa.���`cset���`a(���`dxlim���aoa=���`a(���bmia0���`a,���`a ���bmia2���`a)���`a,���`a ���`dylim���aoa=���`a(���bmia0���`a,���`a ���bmia2���`a)���`a)���`a
���`a
���bc1xO###############################################################################���`a
���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
`dNone�