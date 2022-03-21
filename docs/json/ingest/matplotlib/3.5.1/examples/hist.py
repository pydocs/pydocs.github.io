ŸØÇÅŸ¥ÉôRŸ±ÇbsdxQ"""
==========
Histograms
==========

How to plot histograms with Matplotlib.
"""Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±ÇbknfimportŸ±Ç`a Ÿ±ÇbnnŸ¢ÑjmatplotlibŸ†Ñjmatplotlibe3.5.1fmodulejmatplotlibfmoduleıŸ±Çbnna.Ÿ±ÇbnnfpyplotŸ±Ç`a Ÿ±ÇakbasŸ±Ç`a Ÿ±ÇbnncpltŸ±Ç`a
Ÿ±ÇbknfimportŸ±Ç`a Ÿ±ÇbnnŸ¢ÑenumpyŸ†Ñenumpyf1.22.3fmoduleenumpyfmoduleıŸ±Ç`a Ÿ±ÇakbasŸ±Ç`a Ÿ±ÇbnnbnpŸ±Ç`a
Ÿ±ÇbkndfromŸ±Ç`a Ÿ±ÇbnnŸ¢ÑjmatplotlibŸ†Ñjmatplotlibe3.5.1fmodulejmatplotlibfmoduleıŸ±Ç`a Ÿ±ÇbknfimportŸ±Ç`a Ÿ±Ç`fcolorsŸ±Ç`a
Ÿ±ÇbkndfromŸ±Ç`a Ÿ±ÇbnnŸ¢ÑjmatplotlibŸ†Ñjmatplotlibe3.5.1fmodulejmatplotlibfmoduleıŸ±Çbnna.Ÿ±ÇbnnftickerŸ±Ç`a Ÿ±ÇbknfimportŸ±Ç`a Ÿ±Ç`pPercentFormatterŸ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1xH# Create a random number generator with a fixed seed for reproducibilityŸ±Ç`a
Ÿ±Ç`crngŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`frandomŸ±Çaoa.Ÿ±Ç`kdefault_rngŸ±Ç`a(Ÿ±Çbmih19680801Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1xO###############################################################################Ÿ±Ç`a
Ÿ±Çbc1x+# Generate data and plot a simple histogramŸ±Ç`a
Ÿ±Çbc1x+# -----------------------------------------Ÿ±Ç`a
Ÿ±Çbc1a#Ÿ±Ç`a
Ÿ±Çbc1xN# To generate a 1D histogram we only need a single vector of numbers. For a 2DŸ±Ç`a
Ÿ±Çbc1xK# histogram we'll need a second vector. We'll generate both below, and showŸ±Ç`a
Ÿ±Çbc1x # the histogram for each vector.Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`hN_pointsŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Çbmif100000Ÿ±Ç`a
Ÿ±Ç`fn_binsŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Çbmib20Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1x## Generate two normal distributionsŸ±Ç`a
Ÿ±Ç`edist1Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`crngŸ±Çaoa.Ÿ±Ç`ostandard_normalŸ±Ç`a(Ÿ±Ç`hN_pointsŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`edist2Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Çbmfc0.4Ÿ±Ç`a Ÿ±Çaoa*Ÿ±Ç`a Ÿ±Ç`crngŸ±Çaoa.Ÿ±Ç`ostandard_normalŸ±Ç`a(Ÿ±Ç`hN_pointsŸ±Ç`a)Ÿ±Ç`a Ÿ±Çaoa+Ÿ±Ç`a Ÿ±Çbmia5Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`cfigŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`caxsŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`hsubplotsŸ±Ç`a(Ÿ±Çbmia1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia2Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`fshareyŸ±Çaoa=Ÿ±ÇbkcdTrueŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ltight_layoutŸ±Çaoa=Ÿ±ÇbkcdTrueŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1xA# We can set the number of bins with the *bins* keyword argument.Ÿ±Ç`a
Ÿ±Ç`caxsŸ±Ç`a[Ÿ±Çbmia0Ÿ±Ç`a]Ÿ±Çaoa.Ÿ±Ç`dhistŸ±Ç`a(Ÿ±Ç`edist1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dbinsŸ±Çaoa=Ÿ±Ç`fn_binsŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`caxsŸ±Ç`a[Ÿ±Çbmia1Ÿ±Ç`a]Ÿ±Çaoa.Ÿ±Ç`dhistŸ±Ç`a(Ÿ±Ç`edist2Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dbinsŸ±Çaoa=Ÿ±Ç`fn_binsŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1xO###############################################################################Ÿ±Ç`a
Ÿ±Çbc1x# Updating histogram colorsŸ±Ç`a
Ÿ±Çbc1x# -------------------------Ÿ±Ç`a
Ÿ±Çbc1a#Ÿ±Ç`a
Ÿ±Çbc1xN# The histogram method returns (among other things) a ``patches`` object. ThisŸ±Ç`a
Ÿ±Çbc1xL# gives us access to the properties of the objects drawn. Using this, we canŸ±Ç`a
Ÿ±Çbc1xF# edit the histogram to our liking. Let's change the color of each barŸ±Ç`a
Ÿ±Çbc1w# based on its y value.Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`cfigŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`caxsŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`hsubplotsŸ±Ç`a(Ÿ±Çbmia1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia2Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ltight_layoutŸ±Çaoa=Ÿ±ÇbkcdTrueŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1x@# N is the count in each bin, bins is the lower-limit of the binŸ±Ç`a
Ÿ±Ç`aNŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dbinsŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`gpatchesŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`caxsŸ±Ç`a[Ÿ±Çbmia0Ÿ±Ç`a]Ÿ±Çaoa.Ÿ±Ç`dhistŸ±Ç`a(Ÿ±Ç`edist1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dbinsŸ±Çaoa=Ÿ±Ç`fn_binsŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1x:# We'll color code by height, but you could use any scalarŸ±Ç`a
Ÿ±Ç`efracsŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`aNŸ±Ç`a Ÿ±Çaoa/Ÿ±Ç`a Ÿ±Ç`aNŸ±Çaoa.Ÿ±Ç`cmaxŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1xJ# we need to normalize the data to 0..1 for the full range of the colormapŸ±Ç`a
Ÿ±Ç`dnormŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`fcolorsŸ±Çaoa.Ÿ±Ç`iNormalizeŸ±Ç`a(Ÿ±Ç`efracsŸ±Çaoa.Ÿ±Ç`cminŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`efracsŸ±Çaoa.Ÿ±Ç`cmaxŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1xK# Now, we'll loop through our objects and set the color of each accordinglyŸ±Ç`a
Ÿ±ÇakcforŸ±Ç`a Ÿ±Ç`hthisfracŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ithispatchŸ±Ç`a Ÿ±ÇbowbinŸ±Ç`a Ÿ±ÇbnbczipŸ±Ç`a(Ÿ±Ç`efracsŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`gpatchesŸ±Ç`a)Ÿ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`ecolorŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`bcmŸ±Çaoa.Ÿ±Ç`gviridisŸ±Ç`a(Ÿ±Ç`dnormŸ±Ç`a(Ÿ±Ç`hthisfracŸ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`ithispatchŸ±Çaoa.Ÿ±Ç`mset_facecolorŸ±Ç`a(Ÿ±Ç`ecolorŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1x@# We can also normalize our inputs by the total number of countsŸ±Ç`a
Ÿ±Ç`caxsŸ±Ç`a[Ÿ±Çbmia1Ÿ±Ç`a]Ÿ±Çaoa.Ÿ±Ç`dhistŸ±Ç`a(Ÿ±Ç`edist1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dbinsŸ±Çaoa=Ÿ±Ç`fn_binsŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`gdensityŸ±Çaoa=Ÿ±ÇbkcdTrueŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1x0# Now we format the y-axis to display percentageŸ±Ç`a
Ÿ±Ç`caxsŸ±Ç`a[Ÿ±Çbmia1Ÿ±Ç`a]Ÿ±Çaoa.Ÿ±Ç`eyaxisŸ±Çaoa.Ÿ±Ç`sset_major_formatterŸ±Ç`a(Ÿ±Ç`pPercentFormatterŸ±Ç`a(Ÿ±Ç`dxmaxŸ±Çaoa=Ÿ±Çbmia1Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1xO###############################################################################Ÿ±Ç`a
Ÿ±Çbc1u# Plot a 2D histogramŸ±Ç`a
Ÿ±Çbc1u# -------------------Ÿ±Ç`a
Ÿ±Çbc1a#Ÿ±Ç`a
Ÿ±Çbc1xH# To plot a 2D histogram, one only needs two vectors of the same length,Ÿ±Ç`a
Ÿ±Çbc1x.# corresponding to each axis of the histogram.Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`cfigŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`baxŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`hsubplotsŸ±Ç`a(Ÿ±Ç`ltight_layoutŸ±Çaoa=Ÿ±ÇbkcdTrueŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`dhistŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`fhist2dŸ±Ç`a(Ÿ±Ç`edist1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`edist2Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1xO###############################################################################Ÿ±Ç`a
Ÿ±Çbc1x# Customizing your histogramŸ±Ç`a
Ÿ±Çbc1x# --------------------------Ÿ±Ç`a
Ÿ±Çbc1a#Ÿ±Ç`a
Ÿ±Çbc1xG# Customizing a 2D histogram is similar to the 1D case, you can controlŸ±Ç`a
Ÿ±Çbc1x@# visual components such as the bin size or color normalization.Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`cfigŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`caxsŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`hsubplotsŸ±Ç`a(Ÿ±Çbmia3Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`gfigsizeŸ±Çaoa=Ÿ±Ç`a(Ÿ±Çbmia5Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmib15Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`fsharexŸ±Çaoa=Ÿ±ÇbkcdTrueŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`fshareyŸ±Çaoa=Ÿ±ÇbkcdTrueŸ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`x                        Ÿ±Ç`ltight_layoutŸ±Çaoa=Ÿ±ÇbkcdTrueŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1x1# We can increase the number of bins on each axisŸ±Ç`a
Ÿ±Ç`caxsŸ±Ç`a[Ÿ±Çbmia0Ÿ±Ç`a]Ÿ±Çaoa.Ÿ±Ç`fhist2dŸ±Ç`a(Ÿ±Ç`edist1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`edist2Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dbinsŸ±Çaoa=Ÿ±Çbmib40Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1x/# As well as define normalization of the colorsŸ±Ç`a
Ÿ±Ç`caxsŸ±Ç`a[Ÿ±Çbmia1Ÿ±Ç`a]Ÿ±Çaoa.Ÿ±Ç`fhist2dŸ±Ç`a(Ÿ±Ç`edist1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`edist2Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dbinsŸ±Çaoa=Ÿ±Çbmib40Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dnormŸ±Çaoa=Ÿ±Ç`fcolorsŸ±Çaoa.Ÿ±Ç`gLogNormŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1x9# We can also define custom numbers of bins for each axisŸ±Ç`a
Ÿ±Ç`caxsŸ±Ç`a[Ÿ±Çbmia2Ÿ±Ç`a]Ÿ±Çaoa.Ÿ±Ç`fhist2dŸ±Ç`a(Ÿ±Ç`edist1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`edist2Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dbinsŸ±Çaoa=Ÿ±Ç`a(Ÿ±Çbmib80Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmib10Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dnormŸ±Çaoa=Ÿ±Ç`fcolorsŸ±Çaoa.Ÿ±Ç`gLogNormŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`dshowŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1xM#############################################################################Ÿ±Ç`a
Ÿ±Çbc1a#Ÿ±Ç`a
Ÿ±Çbc1x# .. admonition:: ReferencesŸ±Ç`a
Ÿ±Çbc1a#Ÿ±Ç`a
Ÿ±Çbc1xN#    The use of the following functions, methods, classes and modules is shownŸ±Ç`a
Ÿ±Çbc1u#    in this example:Ÿ±Ç`a
Ÿ±Çbc1a#Ÿ±Ç`a
Ÿ±Çbc1x=#    - `matplotlib.axes.Axes.hist` / `matplotlib.pyplot.hist`Ÿ±Ç`a
Ÿ±Çbc1x!#    - `matplotlib.pyplot.hist2d`Ÿ±Ç`a
Ÿ±Çbc1x+#    - `matplotlib.ticker.PercentFormatter`Ÿ±Ç`a
`dNoneˆ