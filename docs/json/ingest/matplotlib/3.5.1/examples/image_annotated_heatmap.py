��������W���bsdy="""
===========================
Creating annotated heatmaps
===========================

It is often desirable to show data which depends on two independent
variables as a color coded image plot. This is often referred to as a
heatmap. If the data is categorical, this would be called a categorical
heatmap.

Matplotlib's `~matplotlib.axes.Axes.imshow` function makes
production of such plots particularly easy.

The following examples show how to create a heatmap with annotations.
We will start with an easy example and expand it to be usable as a
universal function.
"""���`a
���`a
���`a
���bc1xN##############################################################################���`a
���bc1a#���`a
���bc1x# A simple categorical heatmap���`a
���bc1x# ----------------------------���`a
���bc1a#���`a
���bc1xH# We may start by defining some data. What we need is a 2D list or array���`a
���bc1xM# which defines the data to color code. We then also need two lists or arrays���`a
���bc1x@# of categories; of course the number of elements in those lists���`a
���bc1x3# need to match the data along the respective axes.���`a
���bc1x># The heatmap itself is an `~matplotlib.axes.Axes.imshow` plot���`a
���bc1x0# with the labels set to the categories we have.���`a
���bc1x;# Note that it is important to set both, the tick locations���`a
���bc1x5# (`~matplotlib.axes.Axes.set_xticks`) as well as the���`a
���bc1x8# tick labels (`~matplotlib.axes.Axes.set_xticklabels`),���`a
���bc1xA# otherwise they would become out of sync. The locations are just���`a
���bc1xM# the ascending integer numbers, while the ticklabels are the labels to show.���`a
���bc1xL# Finally we can label the data itself by creating a `~matplotlib.text.Text`���`a
���bc1x2# within each cell showing the value of that cell.���`a
���`a
���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���bc1x%# sphinx_gallery_thumbnail_number = 2���`a
���`a
���`jvegetables���`a ���aoa=���`a ���`a[���bs2a"���bs2hcucumber���bs2a"���`a,���`a ���bs2a"���bs2ftomato���bs2a"���`a,���`a ���bs2a"���bs2glettuce���bs2a"���`a,���`a ���bs2a"���bs2iasparagus���bs2a"���`a,���`a
���`n              ���bs2a"���bs2fpotato���bs2a"���`a,���`a ���bs2a"���bs2ewheat���bs2a"���`a,���`a ���bs2a"���bs2fbarley���bs2a"���`a]���`a
���`gfarmers���`a ���aoa=���`a ���`a[���bs2a"���bs2jFarmer Joe���bs2a"���`a,���`a ���bs2a"���bs2lUpland Bros.���bs2a"���`a,���`a ���bs2a"���bs2oSmith Gardening���bs2a"���`a,���`a
���`k           ���bs2a"���bs2gAgrifun���bs2a"���`a,���`a ���bs2a"���bs2mOrganiculture���bs2a"���`a,���`a ���bs2a"���bs2mBioGoods Ltd.���bs2a"���`a,���`a ���bs2a"���bs2nCornylee Corp.���bs2a"���`a]���`a
���`a
���`gharvest���`a ���aoa=���`a ���`bnp���aoa.���`earray���`a(���`a[���`a[���bmfc0.8���`a,���`a ���bmfc2.4���`a,���`a ���bmfc2.5���`a,���`a ���bmfc3.9���`a,���`a ���bmfc0.0���`a,���`a ���bmfc4.0���`a,���`a ���bmfc0.0���`a]���`a,���`a
���`t                    ���`a[���bmfc2.4���`a,���`a ���bmfc0.0���`a,���`a ���bmfc4.0���`a,���`a ���bmfc1.0���`a,���`a ���bmfc2.7���`a,���`a ���bmfc0.0���`a,���`a ���bmfc0.0���`a]���`a,���`a
���`t                    ���`a[���bmfc1.1���`a,���`a ���bmfc2.4���`a,���`a ���bmfc0.8���`a,���`a ���bmfc4.3���`a,���`a ���bmfc1.9���`a,���`a ���bmfc4.4���`a,���`a ���bmfc0.0���`a]���`a,���`a
���`t                    ���`a[���bmfc0.6���`a,���`a ���bmfc0.0���`a,���`a ���bmfc0.3���`a,���`a ���bmfc0.0���`a,���`a ���bmfc3.1���`a,���`a ���bmfc0.0���`a,���`a ���bmfc0.0���`a]���`a,���`a
���`t                    ���`a[���bmfc0.7���`a,���`a ���bmfc1.7���`a,���`a ���bmfc0.6���`a,���`a ���bmfc2.6���`a,���`a ���bmfc2.2���`a,���`a ���bmfc6.2���`a,���`a ���bmfc0.0���`a]���`a,���`a
���`t                    ���`a[���bmfc1.3���`a,���`a ���bmfc1.2���`a,���`a ���bmfc0.0���`a,���`a ���bmfc0.0���`a,���`a ���bmfc0.0���`a,���`a ���bmfc3.2���`a,���`a ���bmfc5.1���`a]���`a,���`a
���`t                    ���`a[���bmfc0.1���`a,���`a ���bmfc2.0���`a,���`a ���bmfc0.0���`a,���`a ���bmfc1.4���`a,���`a ���bmfc0.0���`a,���`a ���bmfc1.9���`a,���`a ���bmfc6.3���`a]���`a]���`a)���`a
���`a
���`a
���`cfig���`a,���`a ���`bax���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`a)���`a
���`bim���`a ���aoa=���`a ���`bax���aoa.���`fimshow���`a(���`gharvest���`a)���`a
���`a
���bc1x@# Show all ticks and label them with the respective list entries���`a
���`bax���aoa.���`jset_xticks���`a(���`bnp���aoa.���`farange���`a(���bnbclen���`a(���`gfarmers���`a)���`a)���`a,���`a ���`flabels���aoa=���`gfarmers���`a)���`a
���`bax���aoa.���`jset_yticks���`a(���`bnp���aoa.���`farange���`a(���bnbclen���`a(���`jvegetables���`a)���`a)���`a,���`a ���`flabels���aoa=���`jvegetables���`a)���`a
���`a
���bc1x1# Rotate the tick labels and set their alignment.���`a
���`cplt���aoa.���`dsetp���`a(���`bax���aoa.���`oget_xticklabels���`a(���`a)���`a,���`a ���`hrotation���aoa=���bmib45���`a,���`a ���`bha���aoa=���bs2a"���bs2eright���bs2a"���`a,���`a
���`i         ���`mrotation_mode���aoa=���bs2a"���bs2fanchor���bs2a"���`a)���`a
���`a
���bc1x8# Loop over data dimensions and create text annotations.���`a
���akcfor���`a ���`ai���`a ���bowbin���`a ���bnberange���`a(���bnbclen���`a(���`jvegetables���`a)���`a)���`a:���`a
���`d    ���akcfor���`a ���`aj���`a ���bowbin���`a ���bnberange���`a(���bnbclen���`a(���`gfarmers���`a)���`a)���`a:���`a
���`h        ���`dtext���`a ���aoa=���`a ���`bax���aoa.���`dtext���`a(���`aj���`a,���`a ���`ai���`a,���`a ���`gharvest���`a[���`ai���`a,���`a ���`aj���`a]���`a,���`a
���`w                       ���`bha���aoa=���bs2a"���bs2fcenter���bs2a"���`a,���`a ���`bva���aoa=���bs2a"���bs2fcenter���bs2a"���`a,���`a ���`ecolor���aoa=���bs2a"���bs2aw���bs2a"���`a)���`a
���`a
���`bax���aoa.���`iset_title���`a(���bs2a"���bs2x'Harvest of local farmers (in tons/year)���bs2a"���`a)���`a
���`cfig���aoa.���`ltight_layout���`a(���`a)���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
���`a
���`a
���bc1xM#############################################################################���`a
���bc1x&# Using the helper function code style���`a
���bc1x&# ------------------------------------���`a
���bc1a#���`a
���bc1x:# As discussed in the :ref:`Coding styles <coding_styles>`���`a
���bc1xB# one might want to reuse such code to create some kind of heatmap���`a
���bc1x4# for different input data and/or on different axes.���`a
���bc1xK# We create a function that takes the data and the row and column labels as���`a
���bc1xA# input, and allows arguments that are used to customize the plot���`a
���bc1a#���`a
���bc1xF# Here, in addition to the above we also want to create a colorbar and���`a
���bc1x?# position the labels above of the heatmap instead of below it.���`a
���bc1xE# The annotations shall get different colors depending on a threshold���`a
���bc1x.# for better contrast against the pixel color.���`a
���bc1x=# Finally, we turn the surrounding axes spines off and create���`a
���bc1x.# a grid of white lines to separate the cells.���`a
���`a
���`a
���akcdef���`a ���bnfgheatmap���`a(���`ddata���`a,���`a ���`jrow_labels���`a,���`a ���`jcol_labels���`a,���`a ���`bax���aoa=���bkcdNone���`a,���`a
���`l            ���`gcbar_kw���aoa=���`a{���`a}���`a,���`a ���`icbarlabel���aoa=���bs2a"���bs2a"���`a,���`a ���aoa*���aoa*���`fkwargs���`a)���`a:���`a
���`d    ���bsdy�"""
    Create a heatmap from a numpy array and two lists of labels.

    Parameters
    ----------
    data
        A 2D numpy array of shape (M, N).
    row_labels
        A list or array of length M with the labels for the rows.
    col_labels
        A list or array of length N with the labels for the columns.
    ax
        A `matplotlib.axes.Axes` instance to which the heatmap is plotted.  If
        not provided, use current axes or create a new one.  Optional.
    cbar_kw
        A dictionary with arguments to `matplotlib.Figure.colorbar`.  Optional.
    cbarlabel
        The label for the colorbar.  Optional.
    **kwargs
        All other arguments are forwarded to `imshow`.
    """���`a
���`a
���`d    ���akbif���`a ���bowcnot���`a ���`bax���`a:���`a
���`h        ���`bax���`a ���aoa=���`a ���`cplt���aoa.���`cgca���`a(���`a)���`a
���`a
���`d    ���bc1r# Plot the heatmap���`a
���`d    ���`bim���`a ���aoa=���`a ���`bax���aoa.���`fimshow���`a(���`ddata���`a,���`a ���aoa*���aoa*���`fkwargs���`a)���`a
���`a
���`d    ���bc1q# Create colorbar���`a
���`d    ���`dcbar���`a ���aoa=���`a ���`bax���aoa.���`ffigure���aoa.���`hcolorbar���`a(���`bim���`a,���`a ���`bax���aoa=���`bax���`a,���`a ���aoa*���aoa*���`gcbar_kw���`a)���`a
���`d    ���`dcbar���aoa.���`bax���aoa.���`jset_ylabel���`a(���`icbarlabel���`a,���`a ���`hrotation���aoa=���aoa-���bmib90���`a,���`a ���`bva���aoa=���bs2a"���bs2fbottom���bs2a"���`a)���`a
���`a
���`d    ���bc1xA# Show all ticks and label them with the respective list entries.���`a
���`d    ���`bax���aoa.���`jset_xticks���`a(���`bnp���aoa.���`farange���`a(���`ddata���aoa.���`eshape���`a[���bmia1���`a]���`a)���`a,���`a ���`flabels���aoa=���`jcol_labels���`a)���`a
���`d    ���`bax���aoa.���`jset_yticks���`a(���`bnp���aoa.���`farange���`a(���`ddata���aoa.���`eshape���`a[���bmia0���`a]���`a)���`a,���`a ���`flabels���aoa=���`jrow_labels���`a)���`a
���`a
���`d    ���bc1x1# Let the horizontal axes labeling appear on top.���`a
���`d    ���`bax���aoa.���`ktick_params���`a(���`ctop���aoa=���bkcdTrue���`a,���`a ���`fbottom���aoa=���bkceFalse���`a,���`a
���`s                   ���`hlabeltop���aoa=���bkcdTrue���`a,���`a ���`klabelbottom���aoa=���bkceFalse���`a)���`a
���`a
���`d    ���bc1x1# Rotate the tick labels and set their alignment.���`a
���`d    ���`cplt���aoa.���`dsetp���`a(���`bax���aoa.���`oget_xticklabels���`a(���`a)���`a,���`a ���`hrotation���aoa=���aoa-���bmib30���`a,���`a ���`bha���aoa=���bs2a"���bs2eright���bs2a"���`a,���`a
���`m             ���`mrotation_mode���aoa=���bs2a"���bs2fanchor���bs2a"���`a)���`a
���`a
���`d    ���bc1x(# Turn spines off and create white grid.���`a
���`d    ���`bax���aoa.���`fspines���`a[���`a:���`a]���aoa.���`kset_visible���`a(���bkceFalse���`a)���`a
���`a
���`d    ���`bax���aoa.���`jset_xticks���`a(���`bnp���aoa.���`farange���`a(���`ddata���aoa.���`eshape���`a[���bmia1���`a]���aoa+���bmia1���`a)���aoa-���bmfb.5���`a,���`a ���`eminor���aoa=���bkcdTrue���`a)���`a
���`d    ���`bax���aoa.���`jset_yticks���`a(���`bnp���aoa.���`farange���`a(���`ddata���aoa.���`eshape���`a[���bmia0���`a]���aoa+���bmia1���`a)���aoa-���bmfb.5���`a,���`a ���`eminor���aoa=���bkcdTrue���`a)���`a
���`d    ���`bax���aoa.���`dgrid���`a(���`ewhich���aoa=���bs2a"���bs2eminor���bs2a"���`a,���`a ���`ecolor���aoa=���bs2a"���bs2aw���bs2a"���`a,���`a ���`ilinestyle���aoa=���bs1a'���bs1a-���bs1a'���`a,���`a ���`ilinewidth���aoa=���bmia3���`a)���`a
���`d    ���`bax���aoa.���`ktick_params���`a(���`ewhich���aoa=���bs2a"���bs2eminor���bs2a"���`a,���`a ���`fbottom���aoa=���bkceFalse���`a,���`a ���`dleft���aoa=���bkceFalse���`a)���`a
���`a
���`d    ���akfreturn���`a ���`bim���`a,���`a ���`dcbar���`a
���`a
���`a
���akcdef���`a ���bnfpannotate_heatmap���`a(���`bim���`a,���`a ���`ddata���aoa=���bkcdNone���`a,���`a ���`fvalfmt���aoa=���bs2a"���bsig{x:.2f}���bs2a"���`a,���`a
���`u                     ���`jtextcolors���aoa=���`a(���bs2a"���bs2eblack���bs2a"���`a,���`a ���bs2a"���bs2ewhite���bs2a"���`a)���`a,���`a
���`u                     ���`ithreshold���aoa=���bkcdNone���`a,���`a ���aoa*���aoa*���`ftextkw���`a)���`a:���`a
���`d    ���bsdyc"""
    A function to annotate a heatmap.

    Parameters
    ----------
    im
        The AxesImage to be labeled.
    data
        Data used to annotate.  If None, the image's data is used.  Optional.
    valfmt
        The format of the annotations inside the heatmap.  This should either
        use the string format method, e.g. "$ {x:.2f}", or be a
        `matplotlib.ticker.Formatter`.  Optional.
    textcolors
        A pair of colors.  The first is used for values below a threshold,
        the second for those above.  Optional.
    threshold
        Value in data units according to which the colors from textcolors are
        applied.  If None (the default) uses the middle of the colormap as
        separation.  Optional.
    **kwargs
        All other arguments are forwarded to each call to `text` used to create
        the text labels.
    """���`a
���`a
���`d    ���akbif���`a ���bowcnot���`a ���bnbjisinstance���`a(���`ddata���`a,���`a ���`a(���bnbdlist���`a,���`a ���`bnp���aoa.���`gndarray���`a)���`a)���`a:���`a
���`h        ���`ddata���`a ���aoa=���`a ���`bim���aoa.���`iget_array���`a(���`a)���`a
���`a
���`d    ���bc1x4# Normalize the threshold to the images color range.���`a
���`d    ���akbif���`a ���`ithreshold���`a ���bowbis���`a ���bowcnot���`a ���bkcdNone���`a:���`a
���`h        ���`ithreshold���`a ���aoa=���`a ���`bim���aoa.���`dnorm���`a(���`ithreshold���`a)���`a
���`d    ���akdelse���`a:���`a
���`h        ���`ithreshold���`a ���aoa=���`a ���`bim���aoa.���`dnorm���`a(���`ddata���aoa.���`cmax���`a(���`a)���`a)���aoa/���bmfb2.���`a
���`a
���`d    ���bc1x5# Set default alignment to center, but allow it to be���`a
���`d    ���bc1x# overwritten by textkw.���`a
���`d    ���`bkw���`a ���aoa=���`a ���bnbddict���`a(���`shorizontalalignment���aoa=���bs2a"���bs2fcenter���bs2a"���`a,���`a
���`n              ���`qverticalalignment���aoa=���bs2a"���bs2fcenter���bs2a"���`a)���`a
���`d    ���`bkw���aoa.���`fupdate���`a(���`ftextkw���`a)���`a
���`a
���`d    ���bc1x0# Get the formatter in case a string is supplied���`a
���`d    ���akbif���`a ���bnbjisinstance���`a(���`fvalfmt���`a,���`a ���bnbcstr���`a)���`a:���`a
���`h        ���`fvalfmt���`a ���aoa=���`a ���`���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����aoa.���`fticker���aoa.���`rStrMethodFormatter���`a(���`fvalfmt���`a)���`a
���`a
���`d    ���bc1x:# Loop over the data and create a `Text` for each "pixel".���`a
���`d    ���bc1x0# Change the text's color depending on the data.���`a
���`d    ���`etexts���`a ���aoa=���`a ���`a[���`a]���`a
���`d    ���akcfor���`a ���`ai���`a ���bowbin���`a ���bnberange���`a(���`ddata���aoa.���`eshape���`a[���bmia0���`a]���`a)���`a:���`a
���`h        ���akcfor���`a ���`aj���`a ���bowbin���`a ���bnberange���`a(���`ddata���aoa.���`eshape���`a[���bmia1���`a]���`a)���`a:���`a
���`l            ���`bkw���aoa.���`fupdate���`a(���`ecolor���aoa=���`jtextcolors���`a[���bnbcint���`a(���`bim���aoa.���`dnorm���`a(���`ddata���`a[���`ai���`a,���`a ���`aj���`a]���`a)���`a ���aoa>���`a ���`ithreshold���`a)���`a]���`a)���`a
���`l            ���`dtext���`a ���aoa=���`a ���`bim���aoa.���`daxes���aoa.���`dtext���`a(���`aj���`a,���`a ���`ai���`a,���`a ���`fvalfmt���`a(���`ddata���`a[���`ai���`a,���`a ���`aj���`a]���`a,���`a ���bkcdNone���`a)���`a,���`a ���aoa*���aoa*���`bkw���`a)���`a
���`l            ���`etexts���aoa.���`fappend���`a(���`dtext���`a)���`a
���`a
���`d    ���akfreturn���`a ���`etexts���`a
���`a
���`a
���bc1xJ##########################################################################���`a
���bc1xJ# The above now allows us to keep the actual plot creation pretty compact.���`a
���bc1a#���`a
���`a
���`cfig���`a,���`a ���`bax���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`a)���`a
���`a
���`bim���`a,���`a ���`dcbar���`a ���aoa=���`a ���`gheatmap���`a(���`gharvest���`a,���`a ���`jvegetables���`a,���`a ���`gfarmers���`a,���`a ���`bax���aoa=���`bax���`a,���`a
���`s                   ���`dcmap���aoa=���bs2a"���bs2dYlGn���bs2a"���`a,���`a ���`icbarlabel���aoa=���bs2a"���bs2pharvest [t/year]���bs2a"���`a)���`a
���`etexts���`a ���aoa=���`a ���`pannotate_heatmap���`a(���`bim���`a,���`a ���`fvalfmt���aoa=���bs2a"���bsig{x:.1f}���bs2b t���bs2a"���`a)���`a
���`a
���`cfig���aoa.���`ltight_layout���`a(���`a)���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
���`a
���`a
���bc1xM#############################################################################���`a
���bc1x$# Some more complex heatmap examples���`a
���bc1x$# ----------------------------------���`a
���bc1a#���`a
���bc1xD# In the following we show the versatility of the previously created���`a
���bc1xL# functions by applying it in different cases and using different arguments.���`a
���bc1a#���`a
���`a
���`bnp���aoa.���`frandom���aoa.���`dseed���`a(���bmih19680801���`a)���`a
���`a
���`cfig���`a,���`a ���`a(���`a(���`bax���`a,���`a ���`cax2���`a)���`a,���`a ���`a(���`cax3���`a,���`a ���`cax4���`a)���`a)���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���bmia2���`a,���`a ���bmia2���`a,���`a ���`gfigsize���aoa=���`a(���bmia8���`a,���`a ���bmia6���`a)���`a)���`a
���`a
���bc1xF# Replicate the above example with a different font size and colormap.���`a
���`a
���`bim���`a,���`a ���`a_���`a ���aoa=���`a ���`gheatmap���`a(���`gharvest���`a,���`a ���`jvegetables���`a,���`a ���`gfarmers���`a,���`a ���`bax���aoa=���`bax���`a,���`a
���`p                ���`dcmap���aoa=���bs2a"���bs2fWistia���bs2a"���`a,���`a ���`icbarlabel���aoa=���bs2a"���bs2pharvest [t/year]���bs2a"���`a)���`a
���`pannotate_heatmap���`a(���`bim���`a,���`a ���`fvalfmt���aoa=���bs2a"���bsig{x:.1f}���bs2a"���`a,���`a ���`dsize���aoa=���bmia7���`a)���`a
���`a
���bc1x@# Create some new data, give further arguments to imshow (vmin),���`a
���bc1xC# use an integer format on the annotations and provide some colors.���`a
���`a
���`ddata���`a ���aoa=���`a ���`bnp���aoa.���`frandom���aoa.���`grandint���`a(���bmia2���`a,���`a ���bmic100���`a,���`a ���`dsize���aoa=���`a(���bmia7���`a,���`a ���bmia7���`a)���`a)���`a
���`ay���`a ���aoa=���`a ���`a[���bs2a"���bs2eBook ���bsib{}���bs2a"���aoa.���`fformat���`a(���`ai���`a)���`a ���akcfor���`a ���`ai���`a ���bowbin���`a ���bnberange���`a(���bmia1���`a,���`a ���bmia8���`a)���`a]���`a
���`ax���`a ���aoa=���`a ���`a[���bs2a"���bs2fStore ���bsib{}���bs2a"���aoa.���`fformat���`a(���`ai���`a)���`a ���akcfor���`a ���`ai���`a ���bowbin���`a ���bnbdlist���`a(���bs2a"���bs2gABCDEFG���bs2a"���`a)���`a]���`a
���`bim���`a,���`a ���`a_���`a ���aoa=���`a ���`gheatmap���`a(���`ddata���`a,���`a ���`ay���`a,���`a ���`ax���`a,���`a ���`bax���aoa=���`cax2���`a,���`a ���`dvmin���aoa=���bmia0���`a,���`a
���`p                ���`dcmap���aoa=���bs2a"���bs2gmagma_r���bs2a"���`a,���`a ���`icbarlabel���aoa=���bs2a"���bs2rweekly sold copies���bs2a"���`a)���`a
���`pannotate_heatmap���`a(���`bim���`a,���`a ���`fvalfmt���aoa=���bs2a"���bsie{x:d}���bs2a"���`a,���`a ���`dsize���aoa=���bmia7���`a,���`a ���`ithreshold���aoa=���bmib20���`a,���`a
���`q                 ���`jtextcolors���aoa=���`a(���bs2a"���bs2cred���bs2a"���`a,���`a ���bs2a"���bs2ewhite���bs2a"���`a)���`a)���`a
���`a
���bc1x># Sometimes even the data itself is categorical. Here we use a���`a
���bc1x?# `matplotlib.colors.BoundaryNorm` to get the data into classes���`a
���bc1xA# and use this to colorize the plot, but also to obtain the class���`a
���bc1x"# labels from an array of classes.���`a
���`a
���`ddata���`a ���aoa=���`a ���`bnp���aoa.���`frandom���aoa.���`erandn���`a(���bmia6���`a,���`a ���bmia6���`a)���`a
���`ay���`a ���aoa=���`a ���`a[���bs2a"���bs2fProd. ���bsib{}���bs2a"���aoa.���`fformat���`a(���`ai���`a)���`a ���akcfor���`a ���`ai���`a ���bowbin���`a ���bnberange���`a(���bmib10���`a,���`a ���bmib70���`a,���`a ���bmib10���`a)���`a]���`a
���`ax���`a ���aoa=���`a ���`a[���bs2a"���bs2fCycle ���bsib{}���bs2a"���aoa.���`fformat���`a(���`ai���`a)���`a ���akcfor���`a ���`ai���`a ���bowbin���`a ���bnberange���`a(���bmia1���`a,���`a ���bmia7���`a)���`a]���`a
���`a
���`fqrates���`a ���aoa=���`a ���bnbdlist���`a(���bs2a"���bs2gABCDEFG���bs2a"���`a)���`a
���`dnorm���`a ���aoa=���`a ���`���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����aoa.���`fcolors���aoa.���`lBoundaryNorm���`a(���`bnp���aoa.���`hlinspace���`a(���aoa-���bmfc3.5���`a,���`a ���bmfc3.5���`a,���`a ���bmia8���`a)���`a,���`a ���bmia7���`a)���`a
���`cfmt���`a ���aoa=���`a ���`���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����aoa.���`fticker���aoa.���`mFuncFormatter���`a(���akflambda���`a ���`ax���`a,���`a ���`cpos���`a:���`a ���`fqrates���`a[���`a:���`a:���aoa-���bmia1���`a]���`a[���`dnorm���`a(���`ax���`a)���`a]���`a)���`a
���`a
���`bim���`a,���`a ���`a_���`a ���aoa=���`a ���`gheatmap���`a(���`ddata���`a,���`a ���`ay���`a,���`a ���`ax���`a,���`a ���`bax���aoa=���`cax3���`a,���`a
���`p                ���`dcmap���aoa=���`cplt���aoa.���`hget_cmap���`a(���bs2a"���bs2dPiYG���bs2a"���`a,���`a ���bmia7���`a)���`a,���`a ���`dnorm���aoa=���`dnorm���`a,���`a
���`p                ���`gcbar_kw���aoa=���bnbddict���`a(���`eticks���aoa=���`bnp���aoa.���`farange���`a(���aoa-���bmia3���`a,���`a ���bmia4���`a)���`a,���`a ���bnbfformat���aoa=���`cfmt���`a)���`a,���`a
���`p                ���`icbarlabel���aoa=���bs2a"���bs2nQuality Rating���bs2a"���`a)���`a
���`a
���`pannotate_heatmap���`a(���`bim���`a,���`a ���`fvalfmt���aoa=���`cfmt���`a,���`a ���`dsize���aoa=���bmia9���`a,���`a ���`jfontweight���aoa=���bs2a"���bs2dbold���bs2a"���`a,���`a ���`ithreshold���aoa=���aoa-���bmia1���`a,���`a
���`q                 ���`jtextcolors���aoa=���`a(���bs2a"���bs2cred���bs2a"���`a,���`a ���bs2a"���bs2eblack���bs2a"���`a)���`a)���`a
���`a
���bc1xK# We can nicely plot a correlation matrix. Since this is bound by -1 and 1,���`a
���bc1xJ# we use those as vmin and vmax. We may also remove leading zeros and hide���`a
���bc1x4# the diagonal elements (which are all 1) by using a���`a
���bc1x$# `matplotlib.ticker.FuncFormatter`.���`a
���`a
���`kcorr_matrix���`a ���aoa=���`a ���`bnp���aoa.���`hcorrcoef���`a(���`gharvest���`a)���`a
���`bim���`a,���`a ���`a_���`a ���aoa=���`a ���`gheatmap���`a(���`kcorr_matrix���`a,���`a ���`jvegetables���`a,���`a ���`jvegetables���`a,���`a ���`bax���aoa=���`cax4���`a,���`a
���`p                ���`dcmap���aoa=���bs2a"���bs2dPuOr���bs2a"���`a,���`a ���`dvmin���aoa=���aoa-���bmia1���`a,���`a ���`dvmax���aoa=���bmia1���`a,���`a
���`p                ���`icbarlabel���aoa=���bs2a"���bs2rcorrelation coeff.���bs2a"���`a)���`a
���`a
���`a
���akcdef���`a ���bnfdfunc���`a(���`ax���`a,���`a ���`cpos���`a)���`a:���`a
���`d    ���akfreturn���`a ���bs2a"���bsif{:.2f}���bs2a"���aoa.���`fformat���`a(���`ax���`a)���aoa.���`greplace���`a(���bs2a"���bs2b0.���bs2a"���`a,���`a ���bs2a"���bs2a.���bs2a"���`a)���aoa.���`greplace���`a(���bs2a"���bs2d1.00���bs2a"���`a,���`a ���bs2a"���bs2a"���`a)���`a
���`a
���`pannotate_heatmap���`a(���`bim���`a,���`a ���`fvalfmt���aoa=���`���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����aoa.���`fticker���aoa.���`mFuncFormatter���`a(���`dfunc���`a)���`a,���`a ���`dsize���aoa=���bmia7���`a)���`a
���`a
���`a
���`cplt���aoa.���`ltight_layout���`a(���`a)���`a
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
���bc1xA#    - `matplotlib.axes.Axes.imshow` / `matplotlib.pyplot.imshow`���`a
���bc1xI#    - `matplotlib.figure.Figure.colorbar` / `matplotlib.pyplot.colorbar`���`a
`dNone�