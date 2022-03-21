Ù¯‚Ù´ƒ™WÙ±‚bsdy="""
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
"""Ù±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚bc1xN##############################################################################Ù±‚`a
Ù±‚bc1a#Ù±‚`a
Ù±‚bc1x# A simple categorical heatmapÙ±‚`a
Ù±‚bc1x# ----------------------------Ù±‚`a
Ù±‚bc1a#Ù±‚`a
Ù±‚bc1xH# We may start by defining some data. What we need is a 2D list or arrayÙ±‚`a
Ù±‚bc1xM# which defines the data to color code. We then also need two lists or arraysÙ±‚`a
Ù±‚bc1x@# of categories; of course the number of elements in those listsÙ±‚`a
Ù±‚bc1x3# need to match the data along the respective axes.Ù±‚`a
Ù±‚bc1x># The heatmap itself is an `~matplotlib.axes.Axes.imshow` plotÙ±‚`a
Ù±‚bc1x0# with the labels set to the categories we have.Ù±‚`a
Ù±‚bc1x;# Note that it is important to set both, the tick locationsÙ±‚`a
Ù±‚bc1x5# (`~matplotlib.axes.Axes.set_xticks`) as well as theÙ±‚`a
Ù±‚bc1x8# tick labels (`~matplotlib.axes.Axes.set_xticklabels`),Ù±‚`a
Ù±‚bc1xA# otherwise they would become out of sync. The locations are justÙ±‚`a
Ù±‚bc1xM# the ascending integer numbers, while the ticklabels are the labels to show.Ù±‚`a
Ù±‚bc1xL# Finally we can label the data itself by creating a `~matplotlib.text.Text`Ù±‚`a
Ù±‚bc1x2# within each cell showing the value of that cell.Ù±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„enumpyÙ „enumpyf1.22.3fmoduleenumpyfmoduleõÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnnbnpÙ±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnnfpyplotÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnncpltÙ±‚`a
Ù±‚bc1x%# sphinx_gallery_thumbnail_number = 2Ù±‚`a
Ù±‚`a
Ù±‚`jvegetablesÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`a[Ù±‚bs2a"Ù±‚bs2hcucumberÙ±‚bs2a"Ù±‚`a,Ù±‚`a Ù±‚bs2a"Ù±‚bs2ftomatoÙ±‚bs2a"Ù±‚`a,Ù±‚`a Ù±‚bs2a"Ù±‚bs2glettuceÙ±‚bs2a"Ù±‚`a,Ù±‚`a Ù±‚bs2a"Ù±‚bs2iasparagusÙ±‚bs2a"Ù±‚`a,Ù±‚`a
Ù±‚`n              Ù±‚bs2a"Ù±‚bs2fpotatoÙ±‚bs2a"Ù±‚`a,Ù±‚`a Ù±‚bs2a"Ù±‚bs2ewheatÙ±‚bs2a"Ù±‚`a,Ù±‚`a Ù±‚bs2a"Ù±‚bs2fbarleyÙ±‚bs2a"Ù±‚`a]Ù±‚`a
Ù±‚`gfarmersÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`a[Ù±‚bs2a"Ù±‚bs2jFarmer JoeÙ±‚bs2a"Ù±‚`a,Ù±‚`a Ù±‚bs2a"Ù±‚bs2lUpland Bros.Ù±‚bs2a"Ù±‚`a,Ù±‚`a Ù±‚bs2a"Ù±‚bs2oSmith GardeningÙ±‚bs2a"Ù±‚`a,Ù±‚`a
Ù±‚`k           Ù±‚bs2a"Ù±‚bs2gAgrifunÙ±‚bs2a"Ù±‚`a,Ù±‚`a Ù±‚bs2a"Ù±‚bs2mOrganicultureÙ±‚bs2a"Ù±‚`a,Ù±‚`a Ù±‚bs2a"Ù±‚bs2mBioGoods Ltd.Ù±‚bs2a"Ù±‚`a,Ù±‚`a Ù±‚bs2a"Ù±‚bs2nCornylee Corp.Ù±‚bs2a"Ù±‚`a]Ù±‚`a
Ù±‚`a
Ù±‚`gharvestÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`earrayÙ±‚`a(Ù±‚`a[Ù±‚`a[Ù±‚bmfc0.8Ù±‚`a,Ù±‚`a Ù±‚bmfc2.4Ù±‚`a,Ù±‚`a Ù±‚bmfc2.5Ù±‚`a,Ù±‚`a Ù±‚bmfc3.9Ù±‚`a,Ù±‚`a Ù±‚bmfc0.0Ù±‚`a,Ù±‚`a Ù±‚bmfc4.0Ù±‚`a,Ù±‚`a Ù±‚bmfc0.0Ù±‚`a]Ù±‚`a,Ù±‚`a
Ù±‚`t                    Ù±‚`a[Ù±‚bmfc2.4Ù±‚`a,Ù±‚`a Ù±‚bmfc0.0Ù±‚`a,Ù±‚`a Ù±‚bmfc4.0Ù±‚`a,Ù±‚`a Ù±‚bmfc1.0Ù±‚`a,Ù±‚`a Ù±‚bmfc2.7Ù±‚`a,Ù±‚`a Ù±‚bmfc0.0Ù±‚`a,Ù±‚`a Ù±‚bmfc0.0Ù±‚`a]Ù±‚`a,Ù±‚`a
Ù±‚`t                    Ù±‚`a[Ù±‚bmfc1.1Ù±‚`a,Ù±‚`a Ù±‚bmfc2.4Ù±‚`a,Ù±‚`a Ù±‚bmfc0.8Ù±‚`a,Ù±‚`a Ù±‚bmfc4.3Ù±‚`a,Ù±‚`a Ù±‚bmfc1.9Ù±‚`a,Ù±‚`a Ù±‚bmfc4.4Ù±‚`a,Ù±‚`a Ù±‚bmfc0.0Ù±‚`a]Ù±‚`a,Ù±‚`a
Ù±‚`t                    Ù±‚`a[Ù±‚bmfc0.6Ù±‚`a,Ù±‚`a Ù±‚bmfc0.0Ù±‚`a,Ù±‚`a Ù±‚bmfc0.3Ù±‚`a,Ù±‚`a Ù±‚bmfc0.0Ù±‚`a,Ù±‚`a Ù±‚bmfc3.1Ù±‚`a,Ù±‚`a Ù±‚bmfc0.0Ù±‚`a,Ù±‚`a Ù±‚bmfc0.0Ù±‚`a]Ù±‚`a,Ù±‚`a
Ù±‚`t                    Ù±‚`a[Ù±‚bmfc0.7Ù±‚`a,Ù±‚`a Ù±‚bmfc1.7Ù±‚`a,Ù±‚`a Ù±‚bmfc0.6Ù±‚`a,Ù±‚`a Ù±‚bmfc2.6Ù±‚`a,Ù±‚`a Ù±‚bmfc2.2Ù±‚`a,Ù±‚`a Ù±‚bmfc6.2Ù±‚`a,Ù±‚`a Ù±‚bmfc0.0Ù±‚`a]Ù±‚`a,Ù±‚`a
Ù±‚`t                    Ù±‚`a[Ù±‚bmfc1.3Ù±‚`a,Ù±‚`a Ù±‚bmfc1.2Ù±‚`a,Ù±‚`a Ù±‚bmfc0.0Ù±‚`a,Ù±‚`a Ù±‚bmfc0.0Ù±‚`a,Ù±‚`a Ù±‚bmfc0.0Ù±‚`a,Ù±‚`a Ù±‚bmfc3.2Ù±‚`a,Ù±‚`a Ù±‚bmfc5.1Ù±‚`a]Ù±‚`a,Ù±‚`a
Ù±‚`t                    Ù±‚`a[Ù±‚bmfc0.1Ù±‚`a,Ù±‚`a Ù±‚bmfc2.0Ù±‚`a,Ù±‚`a Ù±‚bmfc0.0Ù±‚`a,Ù±‚`a Ù±‚bmfc1.4Ù±‚`a,Ù±‚`a Ù±‚bmfc0.0Ù±‚`a,Ù±‚`a Ù±‚bmfc1.9Ù±‚`a,Ù±‚`a Ù±‚bmfc6.3Ù±‚`a]Ù±‚`a]Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚`cfigÙ±‚`a,Ù±‚`a Ù±‚`baxÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cpltÙ±‚aoa.Ù±‚`hsubplotsÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`bimÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`baxÙ±‚aoa.Ù±‚`fimshowÙ±‚`a(Ù±‚`gharvestÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚bc1x@# Show all ticks and label them with the respective list entriesÙ±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`jset_xticksÙ±‚`a(Ù±‚`bnpÙ±‚aoa.Ù±‚`farangeÙ±‚`a(Ù±‚bnbclenÙ±‚`a(Ù±‚`gfarmersÙ±‚`a)Ù±‚`a)Ù±‚`a,Ù±‚`a Ù±‚`flabelsÙ±‚aoa=Ù±‚`gfarmersÙ±‚`a)Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`jset_yticksÙ±‚`a(Ù±‚`bnpÙ±‚aoa.Ù±‚`farangeÙ±‚`a(Ù±‚bnbclenÙ±‚`a(Ù±‚`jvegetablesÙ±‚`a)Ù±‚`a)Ù±‚`a,Ù±‚`a Ù±‚`flabelsÙ±‚aoa=Ù±‚`jvegetablesÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚bc1x1# Rotate the tick labels and set their alignment.Ù±‚`a
Ù±‚`cpltÙ±‚aoa.Ù±‚`dsetpÙ±‚`a(Ù±‚`baxÙ±‚aoa.Ù±‚`oget_xticklabelsÙ±‚`a(Ù±‚`a)Ù±‚`a,Ù±‚`a Ù±‚`hrotationÙ±‚aoa=Ù±‚bmib45Ù±‚`a,Ù±‚`a Ù±‚`bhaÙ±‚aoa=Ù±‚bs2a"Ù±‚bs2erightÙ±‚bs2a"Ù±‚`a,Ù±‚`a
Ù±‚`i         Ù±‚`mrotation_modeÙ±‚aoa=Ù±‚bs2a"Ù±‚bs2fanchorÙ±‚bs2a"Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚bc1x8# Loop over data dimensions and create text annotations.Ù±‚`a
Ù±‚akcforÙ±‚`a Ù±‚`aiÙ±‚`a Ù±‚bowbinÙ±‚`a Ù±‚bnberangeÙ±‚`a(Ù±‚bnbclenÙ±‚`a(Ù±‚`jvegetablesÙ±‚`a)Ù±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`d    Ù±‚akcforÙ±‚`a Ù±‚`ajÙ±‚`a Ù±‚bowbinÙ±‚`a Ù±‚bnberangeÙ±‚`a(Ù±‚bnbclenÙ±‚`a(Ù±‚`gfarmersÙ±‚`a)Ù±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`h        Ù±‚`dtextÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`baxÙ±‚aoa.Ù±‚`dtextÙ±‚`a(Ù±‚`ajÙ±‚`a,Ù±‚`a Ù±‚`aiÙ±‚`a,Ù±‚`a Ù±‚`gharvestÙ±‚`a[Ù±‚`aiÙ±‚`a,Ù±‚`a Ù±‚`ajÙ±‚`a]Ù±‚`a,Ù±‚`a
Ù±‚`w                       Ù±‚`bhaÙ±‚aoa=Ù±‚bs2a"Ù±‚bs2fcenterÙ±‚bs2a"Ù±‚`a,Ù±‚`a Ù±‚`bvaÙ±‚aoa=Ù±‚bs2a"Ù±‚bs2fcenterÙ±‚bs2a"Ù±‚`a,Ù±‚`a Ù±‚`ecolorÙ±‚aoa=Ù±‚bs2a"Ù±‚bs2awÙ±‚bs2a"Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`iset_titleÙ±‚`a(Ù±‚bs2a"Ù±‚bs2x'Harvest of local farmers (in tons/year)Ù±‚bs2a"Ù±‚`a)Ù±‚`a
Ù±‚`cfigÙ±‚aoa.Ù±‚`ltight_layoutÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`cpltÙ±‚aoa.Ù±‚`dshowÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚bc1xM#############################################################################Ù±‚`a
Ù±‚bc1x&# Using the helper function code styleÙ±‚`a
Ù±‚bc1x&# ------------------------------------Ù±‚`a
Ù±‚bc1a#Ù±‚`a
Ù±‚bc1x:# As discussed in the :ref:`Coding styles <coding_styles>`Ù±‚`a
Ù±‚bc1xB# one might want to reuse such code to create some kind of heatmapÙ±‚`a
Ù±‚bc1x4# for different input data and/or on different axes.Ù±‚`a
Ù±‚bc1xK# We create a function that takes the data and the row and column labels asÙ±‚`a
Ù±‚bc1xA# input, and allows arguments that are used to customize the plotÙ±‚`a
Ù±‚bc1a#Ù±‚`a
Ù±‚bc1xF# Here, in addition to the above we also want to create a colorbar andÙ±‚`a
Ù±‚bc1x?# position the labels above of the heatmap instead of below it.Ù±‚`a
Ù±‚bc1xE# The annotations shall get different colors depending on a thresholdÙ±‚`a
Ù±‚bc1x.# for better contrast against the pixel color.Ù±‚`a
Ù±‚bc1x=# Finally, we turn the surrounding axes spines off and createÙ±‚`a
Ù±‚bc1x.# a grid of white lines to separate the cells.Ù±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚akcdefÙ±‚`a Ù±‚bnfgheatmapÙ±‚`a(Ù±‚`ddataÙ±‚`a,Ù±‚`a Ù±‚`jrow_labelsÙ±‚`a,Ù±‚`a Ù±‚`jcol_labelsÙ±‚`a,Ù±‚`a Ù±‚`baxÙ±‚aoa=Ù±‚bkcdNoneÙ±‚`a,Ù±‚`a
Ù±‚`l            Ù±‚`gcbar_kwÙ±‚aoa=Ù±‚`a{Ù±‚`a}Ù±‚`a,Ù±‚`a Ù±‚`icbarlabelÙ±‚aoa=Ù±‚bs2a"Ù±‚bs2a"Ù±‚`a,Ù±‚`a Ù±‚aoa*Ù±‚aoa*Ù±‚`fkwargsÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`d    Ù±‚bsdy½"""
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
    """Ù±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚akbifÙ±‚`a Ù±‚bowcnotÙ±‚`a Ù±‚`baxÙ±‚`a:Ù±‚`a
Ù±‚`h        Ù±‚`baxÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cpltÙ±‚aoa.Ù±‚`cgcaÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚bc1r# Plot the heatmapÙ±‚`a
Ù±‚`d    Ù±‚`bimÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`baxÙ±‚aoa.Ù±‚`fimshowÙ±‚`a(Ù±‚`ddataÙ±‚`a,Ù±‚`a Ù±‚aoa*Ù±‚aoa*Ù±‚`fkwargsÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚bc1q# Create colorbarÙ±‚`a
Ù±‚`d    Ù±‚`dcbarÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`baxÙ±‚aoa.Ù±‚`ffigureÙ±‚aoa.Ù±‚`hcolorbarÙ±‚`a(Ù±‚`bimÙ±‚`a,Ù±‚`a Ù±‚`baxÙ±‚aoa=Ù±‚`baxÙ±‚`a,Ù±‚`a Ù±‚aoa*Ù±‚aoa*Ù±‚`gcbar_kwÙ±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`dcbarÙ±‚aoa.Ù±‚`baxÙ±‚aoa.Ù±‚`jset_ylabelÙ±‚`a(Ù±‚`icbarlabelÙ±‚`a,Ù±‚`a Ù±‚`hrotationÙ±‚aoa=Ù±‚aoa-Ù±‚bmib90Ù±‚`a,Ù±‚`a Ù±‚`bvaÙ±‚aoa=Ù±‚bs2a"Ù±‚bs2fbottomÙ±‚bs2a"Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚bc1xA# Show all ticks and label them with the respective list entries.Ù±‚`a
Ù±‚`d    Ù±‚`baxÙ±‚aoa.Ù±‚`jset_xticksÙ±‚`a(Ù±‚`bnpÙ±‚aoa.Ù±‚`farangeÙ±‚`a(Ù±‚`ddataÙ±‚aoa.Ù±‚`eshapeÙ±‚`a[Ù±‚bmia1Ù±‚`a]Ù±‚`a)Ù±‚`a,Ù±‚`a Ù±‚`flabelsÙ±‚aoa=Ù±‚`jcol_labelsÙ±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`baxÙ±‚aoa.Ù±‚`jset_yticksÙ±‚`a(Ù±‚`bnpÙ±‚aoa.Ù±‚`farangeÙ±‚`a(Ù±‚`ddataÙ±‚aoa.Ù±‚`eshapeÙ±‚`a[Ù±‚bmia0Ù±‚`a]Ù±‚`a)Ù±‚`a,Ù±‚`a Ù±‚`flabelsÙ±‚aoa=Ù±‚`jrow_labelsÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚bc1x1# Let the horizontal axes labeling appear on top.Ù±‚`a
Ù±‚`d    Ù±‚`baxÙ±‚aoa.Ù±‚`ktick_paramsÙ±‚`a(Ù±‚`ctopÙ±‚aoa=Ù±‚bkcdTrueÙ±‚`a,Ù±‚`a Ù±‚`fbottomÙ±‚aoa=Ù±‚bkceFalseÙ±‚`a,Ù±‚`a
Ù±‚`s                   Ù±‚`hlabeltopÙ±‚aoa=Ù±‚bkcdTrueÙ±‚`a,Ù±‚`a Ù±‚`klabelbottomÙ±‚aoa=Ù±‚bkceFalseÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚bc1x1# Rotate the tick labels and set their alignment.Ù±‚`a
Ù±‚`d    Ù±‚`cpltÙ±‚aoa.Ù±‚`dsetpÙ±‚`a(Ù±‚`baxÙ±‚aoa.Ù±‚`oget_xticklabelsÙ±‚`a(Ù±‚`a)Ù±‚`a,Ù±‚`a Ù±‚`hrotationÙ±‚aoa=Ù±‚aoa-Ù±‚bmib30Ù±‚`a,Ù±‚`a Ù±‚`bhaÙ±‚aoa=Ù±‚bs2a"Ù±‚bs2erightÙ±‚bs2a"Ù±‚`a,Ù±‚`a
Ù±‚`m             Ù±‚`mrotation_modeÙ±‚aoa=Ù±‚bs2a"Ù±‚bs2fanchorÙ±‚bs2a"Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚bc1x(# Turn spines off and create white grid.Ù±‚`a
Ù±‚`d    Ù±‚`baxÙ±‚aoa.Ù±‚`fspinesÙ±‚`a[Ù±‚`a:Ù±‚`a]Ù±‚aoa.Ù±‚`kset_visibleÙ±‚`a(Ù±‚bkceFalseÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚`baxÙ±‚aoa.Ù±‚`jset_xticksÙ±‚`a(Ù±‚`bnpÙ±‚aoa.Ù±‚`farangeÙ±‚`a(Ù±‚`ddataÙ±‚aoa.Ù±‚`eshapeÙ±‚`a[Ù±‚bmia1Ù±‚`a]Ù±‚aoa+Ù±‚bmia1Ù±‚`a)Ù±‚aoa-Ù±‚bmfb.5Ù±‚`a,Ù±‚`a Ù±‚`eminorÙ±‚aoa=Ù±‚bkcdTrueÙ±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`baxÙ±‚aoa.Ù±‚`jset_yticksÙ±‚`a(Ù±‚`bnpÙ±‚aoa.Ù±‚`farangeÙ±‚`a(Ù±‚`ddataÙ±‚aoa.Ù±‚`eshapeÙ±‚`a[Ù±‚bmia0Ù±‚`a]Ù±‚aoa+Ù±‚bmia1Ù±‚`a)Ù±‚aoa-Ù±‚bmfb.5Ù±‚`a,Ù±‚`a Ù±‚`eminorÙ±‚aoa=Ù±‚bkcdTrueÙ±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`baxÙ±‚aoa.Ù±‚`dgridÙ±‚`a(Ù±‚`ewhichÙ±‚aoa=Ù±‚bs2a"Ù±‚bs2eminorÙ±‚bs2a"Ù±‚`a,Ù±‚`a Ù±‚`ecolorÙ±‚aoa=Ù±‚bs2a"Ù±‚bs2awÙ±‚bs2a"Ù±‚`a,Ù±‚`a Ù±‚`ilinestyleÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1a-Ù±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`ilinewidthÙ±‚aoa=Ù±‚bmia3Ù±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`baxÙ±‚aoa.Ù±‚`ktick_paramsÙ±‚`a(Ù±‚`ewhichÙ±‚aoa=Ù±‚bs2a"Ù±‚bs2eminorÙ±‚bs2a"Ù±‚`a,Ù±‚`a Ù±‚`fbottomÙ±‚aoa=Ù±‚bkceFalseÙ±‚`a,Ù±‚`a Ù±‚`dleftÙ±‚aoa=Ù±‚bkceFalseÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚akfreturnÙ±‚`a Ù±‚`bimÙ±‚`a,Ù±‚`a Ù±‚`dcbarÙ±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚akcdefÙ±‚`a Ù±‚bnfpannotate_heatmapÙ±‚`a(Ù±‚`bimÙ±‚`a,Ù±‚`a Ù±‚`ddataÙ±‚aoa=Ù±‚bkcdNoneÙ±‚`a,Ù±‚`a Ù±‚`fvalfmtÙ±‚aoa=Ù±‚bs2a"Ù±‚bsig{x:.2f}Ù±‚bs2a"Ù±‚`a,Ù±‚`a
Ù±‚`u                     Ù±‚`jtextcolorsÙ±‚aoa=Ù±‚`a(Ù±‚bs2a"Ù±‚bs2eblackÙ±‚bs2a"Ù±‚`a,Ù±‚`a Ù±‚bs2a"Ù±‚bs2ewhiteÙ±‚bs2a"Ù±‚`a)Ù±‚`a,Ù±‚`a
Ù±‚`u                     Ù±‚`ithresholdÙ±‚aoa=Ù±‚bkcdNoneÙ±‚`a,Ù±‚`a Ù±‚aoa*Ù±‚aoa*Ù±‚`ftextkwÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`d    Ù±‚bsdyc"""
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
    """Ù±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚akbifÙ±‚`a Ù±‚bowcnotÙ±‚`a Ù±‚bnbjisinstanceÙ±‚`a(Ù±‚`ddataÙ±‚`a,Ù±‚`a Ù±‚`a(Ù±‚bnbdlistÙ±‚`a,Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`gndarrayÙ±‚`a)Ù±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`h        Ù±‚`ddataÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bimÙ±‚aoa.Ù±‚`iget_arrayÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚bc1x4# Normalize the threshold to the images color range.Ù±‚`a
Ù±‚`d    Ù±‚akbifÙ±‚`a Ù±‚`ithresholdÙ±‚`a Ù±‚bowbisÙ±‚`a Ù±‚bowcnotÙ±‚`a Ù±‚bkcdNoneÙ±‚`a:Ù±‚`a
Ù±‚`h        Ù±‚`ithresholdÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bimÙ±‚aoa.Ù±‚`dnormÙ±‚`a(Ù±‚`ithresholdÙ±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚akdelseÙ±‚`a:Ù±‚`a
Ù±‚`h        Ù±‚`ithresholdÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bimÙ±‚aoa.Ù±‚`dnormÙ±‚`a(Ù±‚`ddataÙ±‚aoa.Ù±‚`cmaxÙ±‚`a(Ù±‚`a)Ù±‚`a)Ù±‚aoa/Ù±‚bmfb2.Ù±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚bc1x5# Set default alignment to center, but allow it to beÙ±‚`a
Ù±‚`d    Ù±‚bc1x# overwritten by textkw.Ù±‚`a
Ù±‚`d    Ù±‚`bkwÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bnbddictÙ±‚`a(Ù±‚`shorizontalalignmentÙ±‚aoa=Ù±‚bs2a"Ù±‚bs2fcenterÙ±‚bs2a"Ù±‚`a,Ù±‚`a
Ù±‚`n              Ù±‚`qverticalalignmentÙ±‚aoa=Ù±‚bs2a"Ù±‚bs2fcenterÙ±‚bs2a"Ù±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`bkwÙ±‚aoa.Ù±‚`fupdateÙ±‚`a(Ù±‚`ftextkwÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚bc1x0# Get the formatter in case a string is suppliedÙ±‚`a
Ù±‚`d    Ù±‚akbifÙ±‚`a Ù±‚bnbjisinstanceÙ±‚`a(Ù±‚`fvalfmtÙ±‚`a,Ù±‚`a Ù±‚bnbcstrÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`h        Ù±‚`fvalfmtÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`Ù¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚aoa.Ù±‚`ftickerÙ±‚aoa.Ù±‚`rStrMethodFormatterÙ±‚`a(Ù±‚`fvalfmtÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚bc1x:# Loop over the data and create a `Text` for each "pixel".Ù±‚`a
Ù±‚`d    Ù±‚bc1x0# Change the text's color depending on the data.Ù±‚`a
Ù±‚`d    Ù±‚`etextsÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`a[Ù±‚`a]Ù±‚`a
Ù±‚`d    Ù±‚akcforÙ±‚`a Ù±‚`aiÙ±‚`a Ù±‚bowbinÙ±‚`a Ù±‚bnberangeÙ±‚`a(Ù±‚`ddataÙ±‚aoa.Ù±‚`eshapeÙ±‚`a[Ù±‚bmia0Ù±‚`a]Ù±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`h        Ù±‚akcforÙ±‚`a Ù±‚`ajÙ±‚`a Ù±‚bowbinÙ±‚`a Ù±‚bnberangeÙ±‚`a(Ù±‚`ddataÙ±‚aoa.Ù±‚`eshapeÙ±‚`a[Ù±‚bmia1Ù±‚`a]Ù±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`l            Ù±‚`bkwÙ±‚aoa.Ù±‚`fupdateÙ±‚`a(Ù±‚`ecolorÙ±‚aoa=Ù±‚`jtextcolorsÙ±‚`a[Ù±‚bnbcintÙ±‚`a(Ù±‚`bimÙ±‚aoa.Ù±‚`dnormÙ±‚`a(Ù±‚`ddataÙ±‚`a[Ù±‚`aiÙ±‚`a,Ù±‚`a Ù±‚`ajÙ±‚`a]Ù±‚`a)Ù±‚`a Ù±‚aoa>Ù±‚`a Ù±‚`ithresholdÙ±‚`a)Ù±‚`a]Ù±‚`a)Ù±‚`a
Ù±‚`l            Ù±‚`dtextÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bimÙ±‚aoa.Ù±‚`daxesÙ±‚aoa.Ù±‚`dtextÙ±‚`a(Ù±‚`ajÙ±‚`a,Ù±‚`a Ù±‚`aiÙ±‚`a,Ù±‚`a Ù±‚`fvalfmtÙ±‚`a(Ù±‚`ddataÙ±‚`a[Ù±‚`aiÙ±‚`a,Ù±‚`a Ù±‚`ajÙ±‚`a]Ù±‚`a,Ù±‚`a Ù±‚bkcdNoneÙ±‚`a)Ù±‚`a,Ù±‚`a Ù±‚aoa*Ù±‚aoa*Ù±‚`bkwÙ±‚`a)Ù±‚`a
Ù±‚`l            Ù±‚`etextsÙ±‚aoa.Ù±‚`fappendÙ±‚`a(Ù±‚`dtextÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚akfreturnÙ±‚`a Ù±‚`etextsÙ±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚bc1xJ##########################################################################Ù±‚`a
Ù±‚bc1xJ# The above now allows us to keep the actual plot creation pretty compact.Ù±‚`a
Ù±‚bc1a#Ù±‚`a
Ù±‚`a
Ù±‚`cfigÙ±‚`a,Ù±‚`a Ù±‚`baxÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cpltÙ±‚aoa.Ù±‚`hsubplotsÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`bimÙ±‚`a,Ù±‚`a Ù±‚`dcbarÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`gheatmapÙ±‚`a(Ù±‚`gharvestÙ±‚`a,Ù±‚`a Ù±‚`jvegetablesÙ±‚`a,Ù±‚`a Ù±‚`gfarmersÙ±‚`a,Ù±‚`a Ù±‚`baxÙ±‚aoa=Ù±‚`baxÙ±‚`a,Ù±‚`a
Ù±‚`s                   Ù±‚`dcmapÙ±‚aoa=Ù±‚bs2a"Ù±‚bs2dYlGnÙ±‚bs2a"Ù±‚`a,Ù±‚`a Ù±‚`icbarlabelÙ±‚aoa=Ù±‚bs2a"Ù±‚bs2pharvest [t/year]Ù±‚bs2a"Ù±‚`a)Ù±‚`a
Ù±‚`etextsÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`pannotate_heatmapÙ±‚`a(Ù±‚`bimÙ±‚`a,Ù±‚`a Ù±‚`fvalfmtÙ±‚aoa=Ù±‚bs2a"Ù±‚bsig{x:.1f}Ù±‚bs2b tÙ±‚bs2a"Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`cfigÙ±‚aoa.Ù±‚`ltight_layoutÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`cpltÙ±‚aoa.Ù±‚`dshowÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚bc1xM#############################################################################Ù±‚`a
Ù±‚bc1x$# Some more complex heatmap examplesÙ±‚`a
Ù±‚bc1x$# ----------------------------------Ù±‚`a
Ù±‚bc1a#Ù±‚`a
Ù±‚bc1xD# In the following we show the versatility of the previously createdÙ±‚`a
Ù±‚bc1xL# functions by applying it in different cases and using different arguments.Ù±‚`a
Ù±‚bc1a#Ù±‚`a
Ù±‚`a
Ù±‚`bnpÙ±‚aoa.Ù±‚`frandomÙ±‚aoa.Ù±‚`dseedÙ±‚`a(Ù±‚bmih19680801Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`cfigÙ±‚`a,Ù±‚`a Ù±‚`a(Ù±‚`a(Ù±‚`baxÙ±‚`a,Ù±‚`a Ù±‚`cax2Ù±‚`a)Ù±‚`a,Ù±‚`a Ù±‚`a(Ù±‚`cax3Ù±‚`a,Ù±‚`a Ù±‚`cax4Ù±‚`a)Ù±‚`a)Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cpltÙ±‚aoa.Ù±‚`hsubplotsÙ±‚`a(Ù±‚bmia2Ù±‚`a,Ù±‚`a Ù±‚bmia2Ù±‚`a,Ù±‚`a Ù±‚`gfigsizeÙ±‚aoa=Ù±‚`a(Ù±‚bmia8Ù±‚`a,Ù±‚`a Ù±‚bmia6Ù±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚bc1xF# Replicate the above example with a different font size and colormap.Ù±‚`a
Ù±‚`a
Ù±‚`bimÙ±‚`a,Ù±‚`a Ù±‚`a_Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`gheatmapÙ±‚`a(Ù±‚`gharvestÙ±‚`a,Ù±‚`a Ù±‚`jvegetablesÙ±‚`a,Ù±‚`a Ù±‚`gfarmersÙ±‚`a,Ù±‚`a Ù±‚`baxÙ±‚aoa=Ù±‚`baxÙ±‚`a,Ù±‚`a
Ù±‚`p                Ù±‚`dcmapÙ±‚aoa=Ù±‚bs2a"Ù±‚bs2fWistiaÙ±‚bs2a"Ù±‚`a,Ù±‚`a Ù±‚`icbarlabelÙ±‚aoa=Ù±‚bs2a"Ù±‚bs2pharvest [t/year]Ù±‚bs2a"Ù±‚`a)Ù±‚`a
Ù±‚`pannotate_heatmapÙ±‚`a(Ù±‚`bimÙ±‚`a,Ù±‚`a Ù±‚`fvalfmtÙ±‚aoa=Ù±‚bs2a"Ù±‚bsig{x:.1f}Ù±‚bs2a"Ù±‚`a,Ù±‚`a Ù±‚`dsizeÙ±‚aoa=Ù±‚bmia7Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚bc1x@# Create some new data, give further arguments to imshow (vmin),Ù±‚`a
Ù±‚bc1xC# use an integer format on the annotations and provide some colors.Ù±‚`a
Ù±‚`a
Ù±‚`ddataÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`frandomÙ±‚aoa.Ù±‚`grandintÙ±‚`a(Ù±‚bmia2Ù±‚`a,Ù±‚`a Ù±‚bmic100Ù±‚`a,Ù±‚`a Ù±‚`dsizeÙ±‚aoa=Ù±‚`a(Ù±‚bmia7Ù±‚`a,Ù±‚`a Ù±‚bmia7Ù±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`ayÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`a[Ù±‚bs2a"Ù±‚bs2eBook Ù±‚bsib{}Ù±‚bs2a"Ù±‚aoa.Ù±‚`fformatÙ±‚`a(Ù±‚`aiÙ±‚`a)Ù±‚`a Ù±‚akcforÙ±‚`a Ù±‚`aiÙ±‚`a Ù±‚bowbinÙ±‚`a Ù±‚bnberangeÙ±‚`a(Ù±‚bmia1Ù±‚`a,Ù±‚`a Ù±‚bmia8Ù±‚`a)Ù±‚`a]Ù±‚`a
Ù±‚`axÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`a[Ù±‚bs2a"Ù±‚bs2fStore Ù±‚bsib{}Ù±‚bs2a"Ù±‚aoa.Ù±‚`fformatÙ±‚`a(Ù±‚`aiÙ±‚`a)Ù±‚`a Ù±‚akcforÙ±‚`a Ù±‚`aiÙ±‚`a Ù±‚bowbinÙ±‚`a Ù±‚bnbdlistÙ±‚`a(Ù±‚bs2a"Ù±‚bs2gABCDEFGÙ±‚bs2a"Ù±‚`a)Ù±‚`a]Ù±‚`a
Ù±‚`bimÙ±‚`a,Ù±‚`a Ù±‚`a_Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`gheatmapÙ±‚`a(Ù±‚`ddataÙ±‚`a,Ù±‚`a Ù±‚`ayÙ±‚`a,Ù±‚`a Ù±‚`axÙ±‚`a,Ù±‚`a Ù±‚`baxÙ±‚aoa=Ù±‚`cax2Ù±‚`a,Ù±‚`a Ù±‚`dvminÙ±‚aoa=Ù±‚bmia0Ù±‚`a,Ù±‚`a
Ù±‚`p                Ù±‚`dcmapÙ±‚aoa=Ù±‚bs2a"Ù±‚bs2gmagma_rÙ±‚bs2a"Ù±‚`a,Ù±‚`a Ù±‚`icbarlabelÙ±‚aoa=Ù±‚bs2a"Ù±‚bs2rweekly sold copiesÙ±‚bs2a"Ù±‚`a)Ù±‚`a
Ù±‚`pannotate_heatmapÙ±‚`a(Ù±‚`bimÙ±‚`a,Ù±‚`a Ù±‚`fvalfmtÙ±‚aoa=Ù±‚bs2a"Ù±‚bsie{x:d}Ù±‚bs2a"Ù±‚`a,Ù±‚`a Ù±‚`dsizeÙ±‚aoa=Ù±‚bmia7Ù±‚`a,Ù±‚`a Ù±‚`ithresholdÙ±‚aoa=Ù±‚bmib20Ù±‚`a,Ù±‚`a
Ù±‚`q                 Ù±‚`jtextcolorsÙ±‚aoa=Ù±‚`a(Ù±‚bs2a"Ù±‚bs2credÙ±‚bs2a"Ù±‚`a,Ù±‚`a Ù±‚bs2a"Ù±‚bs2ewhiteÙ±‚bs2a"Ù±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚bc1x># Sometimes even the data itself is categorical. Here we use aÙ±‚`a
Ù±‚bc1x?# `matplotlib.colors.BoundaryNorm` to get the data into classesÙ±‚`a
Ù±‚bc1xA# and use this to colorize the plot, but also to obtain the classÙ±‚`a
Ù±‚bc1x"# labels from an array of classes.Ù±‚`a
Ù±‚`a
Ù±‚`ddataÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`frandomÙ±‚aoa.Ù±‚`erandnÙ±‚`a(Ù±‚bmia6Ù±‚`a,Ù±‚`a Ù±‚bmia6Ù±‚`a)Ù±‚`a
Ù±‚`ayÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`a[Ù±‚bs2a"Ù±‚bs2fProd. Ù±‚bsib{}Ù±‚bs2a"Ù±‚aoa.Ù±‚`fformatÙ±‚`a(Ù±‚`aiÙ±‚`a)Ù±‚`a Ù±‚akcforÙ±‚`a Ù±‚`aiÙ±‚`a Ù±‚bowbinÙ±‚`a Ù±‚bnberangeÙ±‚`a(Ù±‚bmib10Ù±‚`a,Ù±‚`a Ù±‚bmib70Ù±‚`a,Ù±‚`a Ù±‚bmib10Ù±‚`a)Ù±‚`a]Ù±‚`a
Ù±‚`axÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`a[Ù±‚bs2a"Ù±‚bs2fCycle Ù±‚bsib{}Ù±‚bs2a"Ù±‚aoa.Ù±‚`fformatÙ±‚`a(Ù±‚`aiÙ±‚`a)Ù±‚`a Ù±‚akcforÙ±‚`a Ù±‚`aiÙ±‚`a Ù±‚bowbinÙ±‚`a Ù±‚bnberangeÙ±‚`a(Ù±‚bmia1Ù±‚`a,Ù±‚`a Ù±‚bmia7Ù±‚`a)Ù±‚`a]Ù±‚`a
Ù±‚`a
Ù±‚`fqratesÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bnbdlistÙ±‚`a(Ù±‚bs2a"Ù±‚bs2gABCDEFGÙ±‚bs2a"Ù±‚`a)Ù±‚`a
Ù±‚`dnormÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`Ù¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚aoa.Ù±‚`fcolorsÙ±‚aoa.Ù±‚`lBoundaryNormÙ±‚`a(Ù±‚`bnpÙ±‚aoa.Ù±‚`hlinspaceÙ±‚`a(Ù±‚aoa-Ù±‚bmfc3.5Ù±‚`a,Ù±‚`a Ù±‚bmfc3.5Ù±‚`a,Ù±‚`a Ù±‚bmia8Ù±‚`a)Ù±‚`a,Ù±‚`a Ù±‚bmia7Ù±‚`a)Ù±‚`a
Ù±‚`cfmtÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`Ù¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚aoa.Ù±‚`ftickerÙ±‚aoa.Ù±‚`mFuncFormatterÙ±‚`a(Ù±‚akflambdaÙ±‚`a Ù±‚`axÙ±‚`a,Ù±‚`a Ù±‚`cposÙ±‚`a:Ù±‚`a Ù±‚`fqratesÙ±‚`a[Ù±‚`a:Ù±‚`a:Ù±‚aoa-Ù±‚bmia1Ù±‚`a]Ù±‚`a[Ù±‚`dnormÙ±‚`a(Ù±‚`axÙ±‚`a)Ù±‚`a]Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`bimÙ±‚`a,Ù±‚`a Ù±‚`a_Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`gheatmapÙ±‚`a(Ù±‚`ddataÙ±‚`a,Ù±‚`a Ù±‚`ayÙ±‚`a,Ù±‚`a Ù±‚`axÙ±‚`a,Ù±‚`a Ù±‚`baxÙ±‚aoa=Ù±‚`cax3Ù±‚`a,Ù±‚`a
Ù±‚`p                Ù±‚`dcmapÙ±‚aoa=Ù±‚`cpltÙ±‚aoa.Ù±‚`hget_cmapÙ±‚`a(Ù±‚bs2a"Ù±‚bs2dPiYGÙ±‚bs2a"Ù±‚`a,Ù±‚`a Ù±‚bmia7Ù±‚`a)Ù±‚`a,Ù±‚`a Ù±‚`dnormÙ±‚aoa=Ù±‚`dnormÙ±‚`a,Ù±‚`a
Ù±‚`p                Ù±‚`gcbar_kwÙ±‚aoa=Ù±‚bnbddictÙ±‚`a(Ù±‚`eticksÙ±‚aoa=Ù±‚`bnpÙ±‚aoa.Ù±‚`farangeÙ±‚`a(Ù±‚aoa-Ù±‚bmia3Ù±‚`a,Ù±‚`a Ù±‚bmia4Ù±‚`a)Ù±‚`a,Ù±‚`a Ù±‚bnbfformatÙ±‚aoa=Ù±‚`cfmtÙ±‚`a)Ù±‚`a,Ù±‚`a
Ù±‚`p                Ù±‚`icbarlabelÙ±‚aoa=Ù±‚bs2a"Ù±‚bs2nQuality RatingÙ±‚bs2a"Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`pannotate_heatmapÙ±‚`a(Ù±‚`bimÙ±‚`a,Ù±‚`a Ù±‚`fvalfmtÙ±‚aoa=Ù±‚`cfmtÙ±‚`a,Ù±‚`a Ù±‚`dsizeÙ±‚aoa=Ù±‚bmia9Ù±‚`a,Ù±‚`a Ù±‚`jfontweightÙ±‚aoa=Ù±‚bs2a"Ù±‚bs2dboldÙ±‚bs2a"Ù±‚`a,Ù±‚`a Ù±‚`ithresholdÙ±‚aoa=Ù±‚aoa-Ù±‚bmia1Ù±‚`a,Ù±‚`a
Ù±‚`q                 Ù±‚`jtextcolorsÙ±‚aoa=Ù±‚`a(Ù±‚bs2a"Ù±‚bs2credÙ±‚bs2a"Ù±‚`a,Ù±‚`a Ù±‚bs2a"Ù±‚bs2eblackÙ±‚bs2a"Ù±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚bc1xK# We can nicely plot a correlation matrix. Since this is bound by -1 and 1,Ù±‚`a
Ù±‚bc1xJ# we use those as vmin and vmax. We may also remove leading zeros and hideÙ±‚`a
Ù±‚bc1x4# the diagonal elements (which are all 1) by using aÙ±‚`a
Ù±‚bc1x$# `matplotlib.ticker.FuncFormatter`.Ù±‚`a
Ù±‚`a
Ù±‚`kcorr_matrixÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`hcorrcoefÙ±‚`a(Ù±‚`gharvestÙ±‚`a)Ù±‚`a
Ù±‚`bimÙ±‚`a,Ù±‚`a Ù±‚`a_Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`gheatmapÙ±‚`a(Ù±‚`kcorr_matrixÙ±‚`a,Ù±‚`a Ù±‚`jvegetablesÙ±‚`a,Ù±‚`a Ù±‚`jvegetablesÙ±‚`a,Ù±‚`a Ù±‚`baxÙ±‚aoa=Ù±‚`cax4Ù±‚`a,Ù±‚`a
Ù±‚`p                Ù±‚`dcmapÙ±‚aoa=Ù±‚bs2a"Ù±‚bs2dPuOrÙ±‚bs2a"Ù±‚`a,Ù±‚`a Ù±‚`dvminÙ±‚aoa=Ù±‚aoa-Ù±‚bmia1Ù±‚`a,Ù±‚`a Ù±‚`dvmaxÙ±‚aoa=Ù±‚bmia1Ù±‚`a,Ù±‚`a
Ù±‚`p                Ù±‚`icbarlabelÙ±‚aoa=Ù±‚bs2a"Ù±‚bs2rcorrelation coeff.Ù±‚bs2a"Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚akcdefÙ±‚`a Ù±‚bnfdfuncÙ±‚`a(Ù±‚`axÙ±‚`a,Ù±‚`a Ù±‚`cposÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`d    Ù±‚akfreturnÙ±‚`a Ù±‚bs2a"Ù±‚bsif{:.2f}Ù±‚bs2a"Ù±‚aoa.Ù±‚`fformatÙ±‚`a(Ù±‚`axÙ±‚`a)Ù±‚aoa.Ù±‚`greplaceÙ±‚`a(Ù±‚bs2a"Ù±‚bs2b0.Ù±‚bs2a"Ù±‚`a,Ù±‚`a Ù±‚bs2a"Ù±‚bs2a.Ù±‚bs2a"Ù±‚`a)Ù±‚aoa.Ù±‚`greplaceÙ±‚`a(Ù±‚bs2a"Ù±‚bs2d1.00Ù±‚bs2a"Ù±‚`a,Ù±‚`a Ù±‚bs2a"Ù±‚bs2a"Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`pannotate_heatmapÙ±‚`a(Ù±‚`bimÙ±‚`a,Ù±‚`a Ù±‚`fvalfmtÙ±‚aoa=Ù±‚`Ù¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚aoa.Ù±‚`ftickerÙ±‚aoa.Ù±‚`mFuncFormatterÙ±‚`a(Ù±‚`dfuncÙ±‚`a)Ù±‚`a,Ù±‚`a Ù±‚`dsizeÙ±‚aoa=Ù±‚bmia7Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚`cpltÙ±‚aoa.Ù±‚`ltight_layoutÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`cpltÙ±‚aoa.Ù±‚`dshowÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚bc1xM#############################################################################Ù±‚`a
Ù±‚bc1a#Ù±‚`a
Ù±‚bc1x# .. admonition:: ReferencesÙ±‚`a
Ù±‚bc1a#Ù±‚`a
Ù±‚bc1xN#    The use of the following functions, methods, classes and modules is shownÙ±‚`a
Ù±‚bc1u#    in this example:Ù±‚`a
Ù±‚bc1a#Ù±‚`a
Ù±‚bc1xA#    - `matplotlib.axes.Axes.imshow` / `matplotlib.pyplot.imshow`Ù±‚`a
Ù±‚bc1xI#    - `matplotlib.figure.Figure.colorbar` / `matplotlib.pyplot.colorbar`Ù±‚`a
`dNoneö