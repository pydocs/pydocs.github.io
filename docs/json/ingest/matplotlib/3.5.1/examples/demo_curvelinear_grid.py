Ù¯‚Ù´ƒ™‚Ù±‚bsdyn"""
=====================
Curvilinear grid demo
=====================

Custom grid and ticklines.

This example demonstrates how to use
`~.grid_helper_curvelinear.GridHelperCurveLinear` to define custom grids and
ticklines by applying a transformation on the grid.  This can be used, as
shown on the second plot, to create polar projections in a rectangular box.
"""Ù±‚`a
Ù±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„enumpyÙ „enumpyf1.22.3fmoduleenumpyfmoduleõÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnnbnpÙ±‚`a
Ù±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnnfpyplotÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnncpltÙ±‚`a
Ù±‚bkndfromÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnnkprojectionsÙ±‚`a Ù±‚bknfimportÙ±‚`a Ù±‚`iPolarAxesÙ±‚`a
Ù±‚bkndfromÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnnjtransformsÙ±‚`a Ù±‚bknfimportÙ±‚`a Ù±‚`hAffine2DÙ±‚`a
Ù±‚`a
Ù±‚bkndfromÙ±‚`a Ù±‚bnnlmpl_toolkitsÙ±‚bnna.Ù±‚bnnjaxisartistÙ±‚`a Ù±‚bknfimportÙ±‚`a Ù±‚`langle_helperÙ±‚`a,Ù±‚`a Ù±‚`dAxesÙ±‚`a,Ù±‚`a Ù±‚`hHostAxesÙ±‚`a
Ù±‚bkndfromÙ±‚`a Ù±‚bnnlmpl_toolkitsÙ±‚bnna.Ù±‚bnnjaxisartistÙ±‚bnna.Ù±‚bnnwgrid_helper_curvelinearÙ±‚`a Ù±‚bknfimportÙ±‚`a Ù±‚`a(Ù±‚`a
Ù±‚`d    Ù±‚`uGridHelperCurveLinearÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚akcdefÙ±‚`a Ù±‚bnfqcurvelinear_test1Ù±‚`a(Ù±‚`cfigÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`d    Ù±‚bsdx*"""
    Grid for custom transform.
    """Ù±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚akcdefÙ±‚`a Ù±‚bnfbtrÙ±‚`a(Ù±‚`axÙ±‚`a,Ù±‚`a Ù±‚`ayÙ±‚`a)Ù±‚`a:Ù±‚`a Ù±‚akfreturnÙ±‚`a Ù±‚`axÙ±‚`a,Ù±‚`a Ù±‚`ayÙ±‚`a Ù±‚aoa-Ù±‚`a Ù±‚`axÙ±‚`a
Ù±‚`d    Ù±‚akcdefÙ±‚`a Ù±‚bnffinv_trÙ±‚`a(Ù±‚`axÙ±‚`a,Ù±‚`a Ù±‚`ayÙ±‚`a)Ù±‚`a:Ù±‚`a Ù±‚akfreturnÙ±‚`a Ù±‚`axÙ±‚`a,Ù±‚`a Ù±‚`ayÙ±‚`a Ù±‚aoa+Ù±‚`a Ù±‚`axÙ±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚`kgrid_helperÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`uGridHelperCurveLinearÙ±‚`a(Ù±‚`a(Ù±‚`btrÙ±‚`a,Ù±‚`a Ù±‚`finv_trÙ±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚`cax1Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cfigÙ±‚aoa.Ù±‚`kadd_subplotÙ±‚`a(Ù±‚bmia1Ù±‚`a,Ù±‚`a Ù±‚bmia2Ù±‚`a,Ù±‚`a Ù±‚bmia1Ù±‚`a,Ù±‚`a Ù±‚`jaxes_classÙ±‚aoa=Ù±‚`dAxesÙ±‚`a,Ù±‚`a Ù±‚`kgrid_helperÙ±‚aoa=Ù±‚`kgrid_helperÙ±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚bc1xE# ax1 will have ticks and gridlines defined by the given transform (+Ù±‚`a
Ù±‚`d    Ù±‚bc1xE# transData of the Axes).  Note that the transform of the Axes itselfÙ±‚`a
Ù±‚`d    Ù±‚bc1x;# (i.e., transData) is not affected by the given transform.Ù±‚`a
Ù±‚`d    Ù±‚`bxxÙ±‚`a,Ù±‚`a Ù±‚`byyÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`btrÙ±‚`a(Ù±‚`bnpÙ±‚aoa.Ù±‚`earrayÙ±‚`a(Ù±‚`a[Ù±‚bmia3Ù±‚`a,Ù±‚`a Ù±‚bmia6Ù±‚`a]Ù±‚`a)Ù±‚`a,Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`earrayÙ±‚`a(Ù±‚`a[Ù±‚bmia5Ù±‚`a,Ù±‚`a Ù±‚bmib10Ù±‚`a]Ù±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`cax1Ù±‚aoa.Ù±‚`dplotÙ±‚`a(Ù±‚`bxxÙ±‚`a,Ù±‚`a Ù±‚`byyÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚`cax1Ù±‚aoa.Ù±‚`jset_aspectÙ±‚`a(Ù±‚bmia1Ù±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`cax1Ù±‚aoa.Ù±‚`hset_xlimÙ±‚`a(Ù±‚bmia0Ù±‚`a,Ù±‚`a Ù±‚bmib10Ù±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`cax1Ù±‚aoa.Ù±‚`hset_ylimÙ±‚`a(Ù±‚bmia0Ù±‚`a,Ù±‚`a Ù±‚bmib10Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚`cax1Ù±‚aoa.Ù±‚`daxisÙ±‚`a[Ù±‚bs2a"Ù±‚bs2atÙ±‚bs2a"Ù±‚`a]Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cax1Ù±‚aoa.Ù±‚`qnew_floating_axisÙ±‚`a(Ù±‚bmia0Ù±‚`a,Ù±‚`a Ù±‚bmia3Ù±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`cax1Ù±‚aoa.Ù±‚`daxisÙ±‚`a[Ù±‚bs2a"Ù±‚bs2bt2Ù±‚bs2a"Ù±‚`a]Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cax1Ù±‚aoa.Ù±‚`qnew_floating_axisÙ±‚`a(Ù±‚bmia1Ù±‚`a,Ù±‚`a Ù±‚bmia7Ù±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`cax1Ù±‚aoa.Ù±‚`dgridÙ±‚`a(Ù±‚bkcdTrueÙ±‚`a,Ù±‚`a Ù±‚`fzorderÙ±‚aoa=Ù±‚bmia0Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚akcdefÙ±‚`a Ù±‚bnfqcurvelinear_test2Ù±‚`a(Ù±‚`cfigÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`d    Ù±‚bsdx;"""
    Polar projection, but in a rectangular box.
    """Ù±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚bc1xH# PolarAxes.PolarTransform takes radian. However, we want our coordinateÙ±‚`a
Ù±‚`d    Ù±‚bc1r# system in degreeÙ±‚`a
Ù±‚`d    Ù±‚`btrÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`hAffine2DÙ±‚`a(Ù±‚`a)Ù±‚aoa.Ù±‚`escaleÙ±‚`a(Ù±‚`bnpÙ±‚aoa.Ù±‚`bpiÙ±‚aoa/Ù±‚bmic180Ù±‚`a,Ù±‚`a Ù±‚bmia1Ù±‚`a)Ù±‚`a Ù±‚aoa+Ù±‚`a Ù±‚`iPolarAxesÙ±‚aoa.Ù±‚`nPolarTransformÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚bc1x@# Polar projection, which involves cycle, and also has limits inÙ±‚`a
Ù±‚`d    Ù±‚bc1x># its coordinates, needs a special method to find the extremesÙ±‚`a
Ù±‚`d    Ù±‚bc1x/# (min, max of the coordinate within the view).Ù±‚`a
Ù±‚`d    Ù±‚`nextreme_finderÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`langle_helperÙ±‚aoa.Ù±‚`rExtremeFinderCycleÙ±‚`a(Ù±‚`a
Ù±‚`h        Ù±‚`bnxÙ±‚aoa=Ù±‚bmib20Ù±‚`a,Ù±‚`a Ù±‚`bnyÙ±‚aoa=Ù±‚bmib20Ù±‚`a,Ù±‚`b  Ù±‚bc1x.# Number of sampling points in each direction.Ù±‚`a
Ù±‚`h        Ù±‚`ilon_cycleÙ±‚aoa=Ù±‚bmic360Ù±‚`a,Ù±‚`a Ù±‚`ilat_cycleÙ±‚aoa=Ù±‚bkcdNoneÙ±‚`a,Ù±‚`a
Ù±‚`h        Ù±‚`jlon_minmaxÙ±‚aoa=Ù±‚bkcdNoneÙ±‚`a,Ù±‚`a Ù±‚`jlat_minmaxÙ±‚aoa=Ù±‚`a(Ù±‚bmia0Ù±‚`a,Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`cinfÙ±‚`a)Ù±‚`a,Ù±‚`a
Ù±‚`d    Ù±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚bc1xK# Find grid values appropriate for the coordinate (degree, minute, second).Ù±‚`a
Ù±‚`d    Ù±‚`mgrid_locator1Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`langle_helperÙ±‚aoa.Ù±‚`jLocatorDMSÙ±‚`a(Ù±‚bmib12Ù±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚bc1xE# Use an appropriate formatter.  Note that the acceptable Locator andÙ±‚`a
Ù±‚`d    Ù±‚bc1xF# Formatter classes are a bit different than that of Matplotlib, whichÙ±‚`a
Ù±‚`d    Ù±‚bc1xD# cannot directly be used here (this may be possible in the future).Ù±‚`a
Ù±‚`d    Ù±‚`otick_formatter1Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`langle_helperÙ±‚aoa.Ù±‚`lFormatterDMSÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚`kgrid_helperÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`uGridHelperCurveLinearÙ±‚`a(Ù±‚`a
Ù±‚`h        Ù±‚`btrÙ±‚`a,Ù±‚`a Ù±‚`nextreme_finderÙ±‚aoa=Ù±‚`nextreme_finderÙ±‚`a,Ù±‚`a
Ù±‚`h        Ù±‚`mgrid_locator1Ù±‚aoa=Ù±‚`mgrid_locator1Ù±‚`a,Ù±‚`a Ù±‚`otick_formatter1Ù±‚aoa=Ù±‚`otick_formatter1Ù±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`cax1Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cfigÙ±‚aoa.Ù±‚`kadd_subplotÙ±‚`a(Ù±‚`a
Ù±‚`h        Ù±‚bmia1Ù±‚`a,Ù±‚`a Ù±‚bmia2Ù±‚`a,Ù±‚`a Ù±‚bmia2Ù±‚`a,Ù±‚`a Ù±‚`jaxes_classÙ±‚aoa=Ù±‚`hHostAxesÙ±‚`a,Ù±‚`a Ù±‚`kgrid_helperÙ±‚aoa=Ù±‚`kgrid_helperÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚bc1x0# make ticklabels of right and top axis visible.Ù±‚`a
Ù±‚`d    Ù±‚`cax1Ù±‚aoa.Ù±‚`daxisÙ±‚`a[Ù±‚bs2a"Ù±‚bs2erightÙ±‚bs2a"Ù±‚`a]Ù±‚aoa.Ù±‚`pmajor_ticklabelsÙ±‚aoa.Ù±‚`kset_visibleÙ±‚`a(Ù±‚bkcdTrueÙ±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`cax1Ù±‚aoa.Ù±‚`daxisÙ±‚`a[Ù±‚bs2a"Ù±‚bs2ctopÙ±‚bs2a"Ù±‚`a]Ù±‚aoa.Ù±‚`pmajor_ticklabelsÙ±‚aoa.Ù±‚`kset_visibleÙ±‚`a(Ù±‚bkcdTrueÙ±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚bc1x<# let right axis shows ticklabels for 1st coordinate (angle)Ù±‚`a
Ù±‚`d    Ù±‚`cax1Ù±‚aoa.Ù±‚`daxisÙ±‚`a[Ù±‚bs2a"Ù±‚bs2erightÙ±‚bs2a"Ù±‚`a]Ù±‚aoa.Ù±‚`jget_helperÙ±‚`a(Ù±‚`a)Ù±‚aoa.Ù±‚`onth_coord_ticksÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bmia0Ù±‚`a
Ù±‚`d    Ù±‚bc1x># let bottom axis shows ticklabels for 2nd coordinate (radius)Ù±‚`a
Ù±‚`d    Ù±‚`cax1Ù±‚aoa.Ù±‚`daxisÙ±‚`a[Ù±‚bs2a"Ù±‚bs2fbottomÙ±‚bs2a"Ù±‚`a]Ù±‚aoa.Ù±‚`jget_helperÙ±‚`a(Ù±‚`a)Ù±‚aoa.Ù±‚`onth_coord_ticksÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bmia1Ù±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚`cax1Ù±‚aoa.Ù±‚`jset_aspectÙ±‚`a(Ù±‚bmia1Ù±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`cax1Ù±‚aoa.Ù±‚`hset_xlimÙ±‚`a(Ù±‚aoa-Ù±‚bmia5Ù±‚`a,Ù±‚`a Ù±‚bmib12Ù±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`cax1Ù±‚aoa.Ù±‚`hset_ylimÙ±‚`a(Ù±‚aoa-Ù±‚bmia5Ù±‚`a,Ù±‚`a Ù±‚bmib10Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚`cax1Ù±‚aoa.Ù±‚`dgridÙ±‚`a(Ù±‚bkcdTrueÙ±‚`a,Ù±‚`a Ù±‚`fzorderÙ±‚aoa=Ù±‚bmia0Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚bc1x&# A parasite axes with given transformÙ±‚`a
Ù±‚`d    Ù±‚`cax2Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cax1Ù±‚aoa.Ù±‚`lget_aux_axesÙ±‚`a(Ù±‚`btrÙ±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚bc1x/# note that ax2.transData == tr + ax1.transDataÙ±‚`a
Ù±‚`d    Ù±‚bc1xA# Anything you draw in ax2 will match the ticks and grids of ax1.Ù±‚`a
Ù±‚`d    Ù±‚`cax1Ù±‚aoa.Ù±‚`iparasitesÙ±‚aoa.Ù±‚`fappendÙ±‚`a(Ù±‚`cax2Ù±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`cax2Ù±‚aoa.Ù±‚`dplotÙ±‚`a(Ù±‚`bnpÙ±‚aoa.Ù±‚`hlinspaceÙ±‚`a(Ù±‚bmia0Ù±‚`a,Ù±‚`a Ù±‚bmib30Ù±‚`a,Ù±‚`a Ù±‚bmib51Ù±‚`a)Ù±‚`a,Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`hlinspaceÙ±‚`a(Ù±‚bmib10Ù±‚`a,Ù±‚`a Ù±‚bmib10Ù±‚`a,Ù±‚`a Ù±‚bmib51Ù±‚`a)Ù±‚`a,Ù±‚`a Ù±‚`ilinewidthÙ±‚aoa=Ù±‚bmia2Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚`cax2Ù±‚aoa.Ù±‚`fpcolorÙ±‚`a(Ù±‚`bnpÙ±‚aoa.Ù±‚`hlinspaceÙ±‚`a(Ù±‚bmia0Ù±‚`a,Ù±‚`a Ù±‚bmib90Ù±‚`a,Ù±‚`a Ù±‚bmia4Ù±‚`a)Ù±‚`a,Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`hlinspaceÙ±‚`a(Ù±‚bmia0Ù±‚`a,Ù±‚`a Ù±‚bmib10Ù±‚`a,Ù±‚`a Ù±‚bmia4Ù±‚`a)Ù±‚`a,Ù±‚`a
Ù±‚`o               Ù±‚`bnpÙ±‚aoa.Ù±‚`farangeÙ±‚`a(Ù±‚bmia9Ù±‚`a)Ù±‚aoa.Ù±‚`greshapeÙ±‚`a(Ù±‚`a(Ù±‚bmia3Ù±‚`a,Ù±‚`a Ù±‚bmia3Ù±‚`a)Ù±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`cax2Ù±‚aoa.Ù±‚`gcontourÙ±‚`a(Ù±‚`bnpÙ±‚aoa.Ù±‚`hlinspaceÙ±‚`a(Ù±‚bmia0Ù±‚`a,Ù±‚`a Ù±‚bmib90Ù±‚`a,Ù±‚`a Ù±‚bmia4Ù±‚`a)Ù±‚`a,Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`hlinspaceÙ±‚`a(Ù±‚bmia0Ù±‚`a,Ù±‚`a Ù±‚bmib10Ù±‚`a,Ù±‚`a Ù±‚bmia4Ù±‚`a)Ù±‚`a,Ù±‚`a
Ù±‚`p                Ù±‚`bnpÙ±‚aoa.Ù±‚`farangeÙ±‚`a(Ù±‚bmib16Ù±‚`a)Ù±‚aoa.Ù±‚`greshapeÙ±‚`a(Ù±‚`a(Ù±‚bmia4Ù±‚`a,Ù±‚`a Ù±‚bmia4Ù±‚`a)Ù±‚`a)Ù±‚`a,Ù±‚`a Ù±‚`fcolorsÙ±‚aoa=Ù±‚bs2a"Ù±‚bs2akÙ±‚bs2a"Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚akbifÙ±‚`a Ù±‚bvmh__name__Ù±‚`a Ù±‚aob==Ù±‚`a Ù±‚bs2a"Ù±‚bs2h__main__Ù±‚bs2a"Ù±‚`a:Ù±‚`a
Ù±‚`d    Ù±‚`cfigÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cpltÙ±‚aoa.Ù±‚`ffigureÙ±‚`a(Ù±‚`gfigsizeÙ±‚aoa=Ù±‚`a(Ù±‚bmia7Ù±‚`a,Ù±‚`a Ù±‚bmia4Ù±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚`qcurvelinear_test1Ù±‚`a(Ù±‚`cfigÙ±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`qcurvelinear_test2Ù±‚`a(Ù±‚`cfigÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚`cpltÙ±‚aoa.Ù±‚`dshowÙ±‚`a(Ù±‚`a)Ù±‚`a
`dNoneö