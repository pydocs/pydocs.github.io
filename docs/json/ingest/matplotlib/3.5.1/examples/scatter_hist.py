ŸØÇÅŸ¥Éô∫Ÿ±Çbsdy"""
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
"""Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±ÇbknfimportŸ±Ç`a Ÿ±ÇbnnŸ¢ÑenumpyŸ†Ñenumpyf1.22.3fmoduleenumpyfmoduleıŸ±Ç`a Ÿ±ÇakbasŸ±Ç`a Ÿ±ÇbnnbnpŸ±Ç`a
Ÿ±ÇbknfimportŸ±Ç`a Ÿ±ÇbnnŸ¢ÑjmatplotlibŸ†Ñjmatplotlibe3.5.1fmodulejmatplotlibfmoduleıŸ±Çbnna.Ÿ±ÇbnnfpyplotŸ±Ç`a Ÿ±ÇakbasŸ±Ç`a Ÿ±ÇbnncpltŸ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1x)# Fixing random state for reproducibilityŸ±Ç`a
Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`frandomŸ±Çaoa.Ÿ±Ç`dseedŸ±Ç`a(Ÿ±Çbmih19680801Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1r# some random dataŸ±Ç`a
Ÿ±Ç`axŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`frandomŸ±Çaoa.Ÿ±Ç`erandnŸ±Ç`a(Ÿ±Çbmid1000Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`ayŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`frandomŸ±Çaoa.Ÿ±Ç`erandnŸ±Ç`a(Ÿ±Çbmid1000Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±ÇakcdefŸ±Ç`a Ÿ±Çbnflscatter_histŸ±Ç`a(Ÿ±Ç`axŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ayŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`baxŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`hax_histxŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`hax_histyŸ±Ç`a)Ÿ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Çbc1k# no labelsŸ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`hax_histxŸ±Çaoa.Ÿ±Ç`ktick_paramsŸ±Ç`a(Ÿ±Ç`daxisŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2axŸ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`klabelbottomŸ±Çaoa=Ÿ±ÇbkceFalseŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`hax_histyŸ±Çaoa.Ÿ±Ç`ktick_paramsŸ±Ç`a(Ÿ±Ç`daxisŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2ayŸ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ilabelleftŸ±Çaoa=Ÿ±ÇbkceFalseŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Çbc1s# the scatter plot:Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`gscatterŸ±Ç`a(Ÿ±Ç`axŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ayŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Çbc1x$# now determine nice limits by hand:Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`hbinwidthŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Çbmfd0.25Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`exymaxŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±ÇbnbcmaxŸ±Ç`a(Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`cmaxŸ±Ç`a(Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`cabsŸ±Ç`a(Ÿ±Ç`axŸ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`cmaxŸ±Ç`a(Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`cabsŸ±Ç`a(Ÿ±Ç`ayŸ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`climŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`a(Ÿ±ÇbnbcintŸ±Ç`a(Ÿ±Ç`exymaxŸ±Çaoa/Ÿ±Ç`hbinwidthŸ±Ç`a)Ÿ±Ç`a Ÿ±Çaoa+Ÿ±Ç`a Ÿ±Çbmia1Ÿ±Ç`a)Ÿ±Ç`a Ÿ±Çaoa*Ÿ±Ç`a Ÿ±Ç`hbinwidthŸ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`dbinsŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`farangeŸ±Ç`a(Ÿ±Çaoa-Ÿ±Ç`climŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`climŸ±Ç`a Ÿ±Çaoa+Ÿ±Ç`a Ÿ±Ç`hbinwidthŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`hbinwidthŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`hax_histxŸ±Çaoa.Ÿ±Ç`dhistŸ±Ç`a(Ÿ±Ç`axŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dbinsŸ±Çaoa=Ÿ±Ç`dbinsŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`hax_histyŸ±Çaoa.Ÿ±Ç`dhistŸ±Ç`a(Ÿ±Ç`ayŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dbinsŸ±Çaoa=Ÿ±Ç`dbinsŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`korientationŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1jhorizontalŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1xM#############################################################################Ÿ±Ç`a
Ÿ±Çbc1a#Ÿ±Ç`a
Ÿ±Çbc1x# Axes in figure coordinatesŸ±Ç`a
Ÿ±Çbc1x# --------------------------Ÿ±Ç`a
Ÿ±Çbc1a#Ÿ±Ç`a
Ÿ±Çbc1xO# To define the axes positions, `.Figure.add_axes` is provided with a rectangleŸ±Ç`a
Ÿ±Çbc1xL# ``[left, bottom, width, height]`` in figure coordinates. The marginal axesŸ±Ç`a
Ÿ±Çbc1x)# share one dimension with the main axes.Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1x# definitions for the axesŸ±Ç`a
Ÿ±Ç`dleftŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ewidthŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Çbmfc0.1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd0.65Ÿ±Ç`a
Ÿ±Ç`fbottomŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`fheightŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Çbmfc0.1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd0.65Ÿ±Ç`a
Ÿ±Ç`gspacingŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Çbmfe0.005Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`lrect_scatterŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`a[Ÿ±Ç`dleftŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`fbottomŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ewidthŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`fheightŸ±Ç`a]Ÿ±Ç`a
Ÿ±Ç`jrect_histxŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`a[Ÿ±Ç`dleftŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`fbottomŸ±Ç`a Ÿ±Çaoa+Ÿ±Ç`a Ÿ±Ç`fheightŸ±Ç`a Ÿ±Çaoa+Ÿ±Ç`a Ÿ±Ç`gspacingŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ewidthŸ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfc0.2Ÿ±Ç`a]Ÿ±Ç`a
Ÿ±Ç`jrect_histyŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`a[Ÿ±Ç`dleftŸ±Ç`a Ÿ±Çaoa+Ÿ±Ç`a Ÿ±Ç`ewidthŸ±Ç`a Ÿ±Çaoa+Ÿ±Ç`a Ÿ±Ç`gspacingŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`fbottomŸ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfc0.2Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`fheightŸ±Ç`a]Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1x# start with a square FigureŸ±Ç`a
Ÿ±Ç`cfigŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`ffigureŸ±Ç`a(Ÿ±Ç`gfigsizeŸ±Çaoa=Ÿ±Ç`a(Ÿ±Çbmia8Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia8Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`baxŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cfigŸ±Çaoa.Ÿ±Ç`hadd_axesŸ±Ç`a(Ÿ±Ç`lrect_scatterŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`hax_histxŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cfigŸ±Çaoa.Ÿ±Ç`hadd_axesŸ±Ç`a(Ÿ±Ç`jrect_histxŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`fsharexŸ±Çaoa=Ÿ±Ç`baxŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`hax_histyŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cfigŸ±Çaoa.Ÿ±Ç`hadd_axesŸ±Ç`a(Ÿ±Ç`jrect_histyŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`fshareyŸ±Çaoa=Ÿ±Ç`baxŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1x%# use the previously defined functionŸ±Ç`a
Ÿ±Ç`lscatter_histŸ±Ç`a(Ÿ±Ç`axŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ayŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`baxŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`hax_histxŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`hax_histyŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`dshowŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1xM#############################################################################Ÿ±Ç`a
Ÿ±Çbc1a#Ÿ±Ç`a
Ÿ±Çbc1r# Using a gridspecŸ±Ç`a
Ÿ±Çbc1r# ----------------Ÿ±Ç`a
Ÿ±Çbc1a#Ÿ±Ç`a
Ÿ±Çbc1xK# We may equally define a gridspec with unequal width- and height-ratios toŸ±Ç`a
Ÿ±Çbc1x&# achieve desired layout. Also see theŸ±Ç`a
Ÿ±Çbc1x9# :doc:`/tutorials/intermediate/arranging_axes` tutorial.Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1x# start with a square FigureŸ±Ç`a
Ÿ±Ç`cfigŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`ffigureŸ±Ç`a(Ÿ±Ç`gfigsizeŸ±Çaoa=Ÿ±Ç`a(Ÿ±Çbmia8Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia8Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1xL# Add a gridspec with two rows and two columns and a ratio of 2 to 7 betweenŸ±Ç`a
Ÿ±Çbc1xE# the size of the marginal axes and the main axes in both directions.Ÿ±Ç`a
Ÿ±Çbc1x7# Also adjust the subplot parameters for a square plot.Ÿ±Ç`a
Ÿ±Ç`bgsŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cfigŸ±Çaoa.Ÿ±Ç`ladd_gridspecŸ±Ç`a(Ÿ±Çbmia2Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia2Ÿ±Ç`a,Ÿ±Ç`b  Ÿ±Ç`lwidth_ratiosŸ±Çaoa=Ÿ±Ç`a(Ÿ±Çbmia7Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia2Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`mheight_ratiosŸ±Çaoa=Ÿ±Ç`a(Ÿ±Çbmia2Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia7Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`v                      Ÿ±Ç`dleftŸ±Çaoa=Ÿ±Çbmfc0.1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`erightŸ±Çaoa=Ÿ±Çbmfc0.9Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`fbottomŸ±Çaoa=Ÿ±Çbmfc0.1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ctopŸ±Çaoa=Ÿ±Çbmfc0.9Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`v                      Ÿ±Ç`fwspaceŸ±Çaoa=Ÿ±Çbmfd0.05Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`fhspaceŸ±Çaoa=Ÿ±Çbmfd0.05Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`baxŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cfigŸ±Çaoa.Ÿ±Ç`kadd_subplotŸ±Ç`a(Ÿ±Ç`bgsŸ±Ç`a[Ÿ±Çbmia1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia0Ÿ±Ç`a]Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`hax_histxŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cfigŸ±Çaoa.Ÿ±Ç`kadd_subplotŸ±Ç`a(Ÿ±Ç`bgsŸ±Ç`a[Ÿ±Çbmia0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia0Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`fsharexŸ±Çaoa=Ÿ±Ç`baxŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`hax_histyŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cfigŸ±Çaoa.Ÿ±Ç`kadd_subplotŸ±Ç`a(Ÿ±Ç`bgsŸ±Ç`a[Ÿ±Çbmia1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia1Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`fshareyŸ±Çaoa=Ÿ±Ç`baxŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1x%# use the previously defined functionŸ±Ç`a
Ÿ±Ç`lscatter_histŸ±Ç`a(Ÿ±Ç`axŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ayŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`baxŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`hax_histxŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`hax_histyŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`dshowŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1xM#############################################################################Ÿ±Ç`a
Ÿ±Çbc1a#Ÿ±Ç`a
Ÿ±Çbc1x# .. admonition:: ReferencesŸ±Ç`a
Ÿ±Çbc1a#Ÿ±Ç`a
Ÿ±Çbc1xN#    The use of the following functions, methods, classes and modules is shownŸ±Ç`a
Ÿ±Çbc1u#    in this example:Ÿ±Ç`a
Ÿ±Çbc1a#Ÿ±Ç`a
Ÿ±Çbc1x*#    - `matplotlib.figure.Figure.add_axes`Ÿ±Ç`a
Ÿ±Çbc1x-#    - `matplotlib.figure.Figure.add_subplot`Ÿ±Ç`a
Ÿ±Çbc1x.#    - `matplotlib.figure.Figure.add_gridspec`Ÿ±Ç`a
Ÿ±Çbc1x%#    - `matplotlib.axes.Axes.scatter`Ÿ±Ç`a
Ÿ±Çbc1x"#    - `matplotlib.axes.Axes.hist`Ÿ±Ç`a
`dNoneˆ