������������bsdy"""
============================
Scatter plot with histograms
============================

Show the marginal distributions of a scatter as histograms at the sides of
the plot.

For a nice alignment of the main axes with the marginals, two options are shown
below.

* the axes positions are defined in terms of rectangles in figure coordinates
* the axes positions are defined via a gridspec

An alternative method to produce a similar figure using the ``axes_grid1``
toolkit is shown in the
:doc:`/gallery/axes_grid1/scatter_hist_locatable_axes` example.

Let us first define a function that takes x and y data as input, as well
as three axes, the main axes for the scatter, and two marginal axes. It will
then create the scatter and histograms inside the provided axes.
"""���`a
���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���`a
���bc1x)# Fixing random state for reproducibility���`a
���`bnp���aoa.���`frandom���aoa.���`dseed���`a(���bmih19680801���`a)���`a
���`a
���bc1r# some random data���`a
���`ax���`a ���aoa=���`a ���`bnp���aoa.���`frandom���aoa.���`erandn���`a(���bmid1000���`a)���`a
���`ay���`a ���aoa=���`a ���`bnp���aoa.���`frandom���aoa.���`erandn���`a(���bmid1000���`a)���`a
���`a
���`a
���akcdef���`a ���bnflscatter_hist���`a(���`ax���`a,���`a ���`ay���`a,���`a ���`bax���`a,���`a ���`hax_histx���`a,���`a ���`hax_histy���`a)���`a:���`a
���`d    ���bc1k# no labels���`a
���`d    ���`hax_histx���aoa.���`ktick_params���`a(���`daxis���aoa=���bs2a"���bs2ax���bs2a"���`a,���`a ���`klabelbottom���aoa=���bkceFalse���`a)���`a
���`d    ���`hax_histy���aoa.���`ktick_params���`a(���`daxis���aoa=���bs2a"���bs2ay���bs2a"���`a,���`a ���`ilabelleft���aoa=���bkceFalse���`a)���`a
���`a
���`d    ���bc1s# the scatter plot:���`a
���`d    ���`bax���aoa.���`gscatter���`a(���`ax���`a,���`a ���`ay���`a)���`a
���`a
���`d    ���bc1x$# now determine nice limits by hand:���`a
���`d    ���`hbinwidth���`a ���aoa=���`a ���bmfd0.25���`a
���`d    ���`exymax���`a ���aoa=���`a ���bnbcmax���`a(���`bnp���aoa.���`cmax���`a(���`bnp���aoa.���`cabs���`a(���`ax���`a)���`a)���`a,���`a ���`bnp���aoa.���`cmax���`a(���`bnp���aoa.���`cabs���`a(���`ay���`a)���`a)���`a)���`a
���`d    ���`clim���`a ���aoa=���`a ���`a(���bnbcint���`a(���`exymax���aoa/���`hbinwidth���`a)���`a ���aoa+���`a ���bmia1���`a)���`a ���aoa*���`a ���`hbinwidth���`a
���`a
���`d    ���`dbins���`a ���aoa=���`a ���`bnp���aoa.���`farange���`a(���aoa-���`clim���`a,���`a ���`clim���`a ���aoa+���`a ���`hbinwidth���`a,���`a ���`hbinwidth���`a)���`a
���`d    ���`hax_histx���aoa.���`dhist���`a(���`ax���`a,���`a ���`dbins���aoa=���`dbins���`a)���`a
���`d    ���`hax_histy���aoa.���`dhist���`a(���`ay���`a,���`a ���`dbins���aoa=���`dbins���`a,���`a ���`korientation���aoa=���bs1a'���bs1jhorizontal���bs1a'���`a)���`a
���`a
���`a
���bc1xM#############################################################################���`a
���bc1a#���`a
���bc1x# Axes in figure coordinates���`a
���bc1x# --------------------------���`a
���bc1a#���`a
���bc1xO# To define the axes positions, `.Figure.add_axes` is provided with a rectangle���`a
���bc1xL# ``[left, bottom, width, height]`` in figure coordinates. The marginal axes���`a
���bc1x)# share one dimension with the main axes.���`a
���`a
���bc1x# definitions for the axes���`a
���`dleft���`a,���`a ���`ewidth���`a ���aoa=���`a ���bmfc0.1���`a,���`a ���bmfd0.65���`a
���`fbottom���`a,���`a ���`fheight���`a ���aoa=���`a ���bmfc0.1���`a,���`a ���bmfd0.65���`a
���`gspacing���`a ���aoa=���`a ���bmfe0.005���`a
���`a
���`a
���`lrect_scatter���`a ���aoa=���`a ���`a[���`dleft���`a,���`a ���`fbottom���`a,���`a ���`ewidth���`a,���`a ���`fheight���`a]���`a
���`jrect_histx���`a ���aoa=���`a ���`a[���`dleft���`a,���`a ���`fbottom���`a ���aoa+���`a ���`fheight���`a ���aoa+���`a ���`gspacing���`a,���`a ���`ewidth���`a,���`a ���bmfc0.2���`a]���`a
���`jrect_histy���`a ���aoa=���`a ���`a[���`dleft���`a ���aoa+���`a ���`ewidth���`a ���aoa+���`a ���`gspacing���`a,���`a ���`fbottom���`a,���`a ���bmfc0.2���`a,���`a ���`fheight���`a]���`a
���`a
���bc1x# start with a square Figure���`a
���`cfig���`a ���aoa=���`a ���`cplt���aoa.���`ffigure���`a(���`gfigsize���aoa=���`a(���bmia8���`a,���`a ���bmia8���`a)���`a)���`a
���`a
���`bax���`a ���aoa=���`a ���`cfig���aoa.���`hadd_axes���`a(���`lrect_scatter���`a)���`a
���`hax_histx���`a ���aoa=���`a ���`cfig���aoa.���`hadd_axes���`a(���`jrect_histx���`a,���`a ���`fsharex���aoa=���`bax���`a)���`a
���`hax_histy���`a ���aoa=���`a ���`cfig���aoa.���`hadd_axes���`a(���`jrect_histy���`a,���`a ���`fsharey���aoa=���`bax���`a)���`a
���`a
���bc1x%# use the previously defined function���`a
���`lscatter_hist���`a(���`ax���`a,���`a ���`ay���`a,���`a ���`bax���`a,���`a ���`hax_histx���`a,���`a ���`hax_histy���`a)���`a
���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
���`a
���`a
���bc1xM#############################################################################���`a
���bc1a#���`a
���bc1r# Using a gridspec���`a
���bc1r# ----------------���`a
���bc1a#���`a
���bc1xK# We may equally define a gridspec with unequal width- and height-ratios to���`a
���bc1x&# achieve desired layout. Also see the���`a
���bc1x9# :doc:`/tutorials/intermediate/arranging_axes` tutorial.���`a
���`a
���bc1x# start with a square Figure���`a
���`cfig���`a ���aoa=���`a ���`cplt���aoa.���`ffigure���`a(���`gfigsize���aoa=���`a(���bmia8���`a,���`a ���bmia8���`a)���`a)���`a
���`a
���bc1xL# Add a gridspec with two rows and two columns and a ratio of 2 to 7 between���`a
���bc1xE# the size of the marginal axes and the main axes in both directions.���`a
���bc1x7# Also adjust the subplot parameters for a square plot.���`a
���`bgs���`a ���aoa=���`a ���`cfig���aoa.���`ladd_gridspec���`a(���bmia2���`a,���`a ���bmia2���`a,���`b  ���`lwidth_ratios���aoa=���`a(���bmia7���`a,���`a ���bmia2���`a)���`a,���`a ���`mheight_ratios���aoa=���`a(���bmia2���`a,���`a ���bmia7���`a)���`a,���`a
���`v                      ���`dleft���aoa=���bmfc0.1���`a,���`a ���`eright���aoa=���bmfc0.9���`a,���`a ���`fbottom���aoa=���bmfc0.1���`a,���`a ���`ctop���aoa=���bmfc0.9���`a,���`a
���`v                      ���`fwspace���aoa=���bmfd0.05���`a,���`a ���`fhspace���aoa=���bmfd0.05���`a)���`a
���`a
���`bax���`a ���aoa=���`a ���`cfig���aoa.���`kadd_subplot���`a(���`bgs���`a[���bmia1���`a,���`a ���bmia0���`a]���`a)���`a
���`hax_histx���`a ���aoa=���`a ���`cfig���aoa.���`kadd_subplot���`a(���`bgs���`a[���bmia0���`a,���`a ���bmia0���`a]���`a,���`a ���`fsharex���aoa=���`bax���`a)���`a
���`hax_histy���`a ���aoa=���`a ���`cfig���aoa.���`kadd_subplot���`a(���`bgs���`a[���bmia1���`a,���`a ���bmia1���`a]���`a,���`a ���`fsharey���aoa=���`bax���`a)���`a
���`a
���bc1x%# use the previously defined function���`a
���`lscatter_hist���`a(���`ax���`a,���`a ���`ay���`a,���`a ���`bax���`a,���`a ���`hax_histx���`a,���`a ���`hax_histy���`a)���`a
���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
���`a
���`a
���bc1xM#############################################################################���`a
���bc1a#���`a
���bc1x# .. admonition:: References���`a
���bc1a#���`a
���bc1xN#    The use of the following functions, methods, classes and modules is shown���`a
���bc1u#    in this example:���`a
���bc1a#���`a
���bc1x*#    - `matplotlib.figure.Figure.add_axes`���`a
���bc1x-#    - `matplotlib.figure.Figure.add_subplot`���`a
���bc1x.#    - `matplotlib.figure.Figure.add_gridspec`���`a
���bc1x%#    - `matplotlib.axes.Axes.scatter`���`a
���bc1x"#    - `matplotlib.axes.Axes.hist`���`a
`dNone�