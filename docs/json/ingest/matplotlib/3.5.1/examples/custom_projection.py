Ù¯‚Ù´ƒ™Ù±‚bsdx…"""
=================
Custom projection
=================

Showcase Hammer projection by alleviating many features of Matplotlib.
"""Ù±‚`a
Ù±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚`a
Ù±‚bkndfromÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnndaxesÙ±‚`a Ù±‚bknfimportÙ±‚`a Ù±‚`dAxesÙ±‚`a
Ù±‚bkndfromÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnngpatchesÙ±‚`a Ù±‚bknfimportÙ±‚`a Ù±‚`fCircleÙ±‚`a
Ù±‚bkndfromÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnndpathÙ±‚`a Ù±‚bknfimportÙ±‚`a Ù±‚`dPathÙ±‚`a
Ù±‚bkndfromÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnnftickerÙ±‚`a Ù±‚bknfimportÙ±‚`a Ù±‚`kNullLocatorÙ±‚`a,Ù±‚`a Ù±‚`iFormatterÙ±‚`a,Ù±‚`a Ù±‚`lFixedLocatorÙ±‚`a
Ù±‚bkndfromÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnnjtransformsÙ±‚`a Ù±‚bknfimportÙ±‚`a Ù±‚`hAffine2DÙ±‚`a,Ù±‚`a Ù±‚`oBboxTransformToÙ±‚`a,Ù±‚`a Ù±‚`iTransformÙ±‚`a
Ù±‚bkndfromÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnnkprojectionsÙ±‚`a Ù±‚bknfimportÙ±‚`a Ù±‚`sregister_projectionÙ±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnnfspinesÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnngmspinesÙ±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnndaxisÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnnemaxisÙ±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„enumpyÙ „enumpyf1.22.3fmoduleenumpyfmoduleõÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnnbnpÙ±‚`a
Ù±‚`a
Ù±‚`hrcParamsÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`Ù¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚aoa.Ù±‚`hrcParamsÙ±‚`a
Ù±‚`a
Ù±‚bc1xE# This example projection class is rather long, but it is designed toÙ±‚`a
Ù±‚bc1xE# illustrate many features, not all of which will be used every time.Ù±‚`a
Ù±‚bc1xD# It is also common to factor out a lot of these methods into commonÙ±‚`a
Ù±‚bc1xC# code used by a number of projections with similar characteristicsÙ±‚`a
Ù±‚bc1o# (see geo.py).Ù±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚akeclassÙ±‚`a Ù±‚bncgGeoAxesÙ±‚`a(Ù±‚`dAxesÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`d    Ù±‚bsdxA"""
    An abstract base class for geographic projections
    """Ù±‚`a
Ù±‚`d    Ù±‚akeclassÙ±‚`a Ù±‚bncnThetaFormatterÙ±‚`a(Ù±‚`iFormatterÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`h        Ù±‚bsdx‘"""
        Used to format the theta tick labels.  Converts the native
        unit of radians into degrees and adds a degree symbol.
        """Ù±‚`a
Ù±‚`h        Ù±‚akcdefÙ±‚`a Ù±‚bfmh__init__Ù±‚`a(Ù±‚bbpdselfÙ±‚`a,Ù±‚`a Ù±‚`hround_toÙ±‚aoa=Ù±‚bmfc1.0Ù±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`l            Ù±‚bbpdselfÙ±‚aoa.Ù±‚`i_round_toÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`hround_toÙ±‚`a
Ù±‚`a
Ù±‚`h        Ù±‚akcdefÙ±‚`a Ù±‚bfmh__call__Ù±‚`a(Ù±‚bbpdselfÙ±‚`a,Ù±‚`a Ù±‚`axÙ±‚`a,Ù±‚`a Ù±‚`cposÙ±‚aoa=Ù±‚bkcdNoneÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`l            Ù±‚`gdegreesÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bnberoundÙ±‚`a(Ù±‚`bnpÙ±‚aoa.Ù±‚`grad2degÙ±‚`a(Ù±‚`axÙ±‚`a)Ù±‚`a Ù±‚aoa/Ù±‚`a Ù±‚bbpdselfÙ±‚aoa.Ù±‚`i_round_toÙ±‚`a)Ù±‚`a Ù±‚aoa*Ù±‚`a Ù±‚bbpdselfÙ±‚aoa.Ù±‚`i_round_toÙ±‚`a
Ù±‚`l            Ù±‚akfreturnÙ±‚`a Ù±‚bsaafÙ±‚bs2a"Ù±‚bsia{Ù±‚`gdegreesÙ±‚bsia:Ù±‚bs2d0.0fÙ±‚bsia}Ù±‚bseo\N{DEGREE SIGN}Ù±‚bs2a"Ù±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚`jRESOLUTIONÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bmib75Ù±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚akcdefÙ±‚`a Ù±‚bnfj_init_axisÙ±‚`a(Ù±‚bbpdselfÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`exaxisÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`emaxisÙ±‚aoa.Ù±‚`eXAxisÙ±‚`a(Ù±‚bbpdselfÙ±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`eyaxisÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`emaxisÙ±‚aoa.Ù±‚`eYAxisÙ±‚`a(Ù±‚bbpdselfÙ±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚bc1x:# Do not register xaxis or yaxis with spines -- as done inÙ±‚`a
Ù±‚`h        Ù±‚bc1x9# Axes._init_axis() -- until GeoAxes.xaxis.clear() works.Ù±‚`a
Ù±‚`h        Ù±‚bc1x.# self.spines['geo'].register_axis(self.yaxis)Ù±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`r_update_transScaleÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚akcdefÙ±‚`a Ù±‚bnfcclaÙ±‚`a(Ù±‚bbpdselfÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`h        Ù±‚bnbesuperÙ±‚`a(Ù±‚`a)Ù±‚aoa.Ù±‚`cclaÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`rset_longitude_gridÙ±‚`a(Ù±‚bmib30Ù±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`qset_latitude_gridÙ±‚`a(Ù±‚bmib15Ù±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`wset_longitude_grid_endsÙ±‚`a(Ù±‚bmib75Ù±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`exaxisÙ±‚aoa.Ù±‚`qset_minor_locatorÙ±‚`a(Ù±‚`kNullLocatorÙ±‚`a(Ù±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`eyaxisÙ±‚aoa.Ù±‚`qset_minor_locatorÙ±‚`a(Ù±‚`kNullLocatorÙ±‚`a(Ù±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`exaxisÙ±‚aoa.Ù±‚`rset_ticks_positionÙ±‚`a(Ù±‚bs1a'Ù±‚bs1dnoneÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`eyaxisÙ±‚aoa.Ù±‚`rset_ticks_positionÙ±‚`a(Ù±‚bs1a'Ù±‚bs1dnoneÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`eyaxisÙ±‚aoa.Ù±‚`oset_tick_paramsÙ±‚`a(Ù±‚`hlabel1OnÙ±‚aoa=Ù±‚bkcdTrueÙ±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚bc1x2# Why do we need to turn on yaxis tick labels, butÙ±‚`a
Ù±‚`h        Ù±‚bc1x## xaxis tick labels are already on?Ù±‚`a
Ù±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`dgridÙ±‚`a(Ù±‚`hrcParamsÙ±‚`a[Ù±‚bs1a'Ù±‚bs1iaxes.gridÙ±‚bs1a'Ù±‚`a]Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`h        Ù±‚`dAxesÙ±‚aoa.Ù±‚`hset_xlimÙ±‚`a(Ù±‚bbpdselfÙ±‚`a,Ù±‚`a Ù±‚aoa-Ù±‚`bnpÙ±‚aoa.Ù±‚`bpiÙ±‚`a,Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`bpiÙ±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚`dAxesÙ±‚aoa.Ù±‚`hset_ylimÙ±‚`a(Ù±‚bbpdselfÙ±‚`a,Ù±‚`a Ù±‚aoa-Ù±‚`bnpÙ±‚aoa.Ù±‚`bpiÙ±‚`a Ù±‚aoa/Ù±‚`a Ù±‚bmfc2.0Ù±‚`a,Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`bpiÙ±‚`a Ù±‚aoa/Ù±‚`a Ù±‚bmfc2.0Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚akcdefÙ±‚`a Ù±‚bnfw_set_lim_and_transformsÙ±‚`a(Ù±‚bbpdselfÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`h        Ù±‚bc1xA# A (possibly non-linear) projection on the (already scaled) dataÙ±‚`a
Ù±‚`a
Ù±‚`h        Ù±‚bc1x<# There are three important coordinate spaces going on here:Ù±‚`a
Ù±‚`h        Ù±‚bc1a#Ù±‚`a
Ù±‚`h        Ù±‚bc1x-# 1. Data space: The space of the data itselfÙ±‚`a
Ù±‚`h        Ù±‚bc1a#Ù±‚`a
Ù±‚`h        Ù±‚bc1x4# 2. Axes space: The unit rectangle (0, 0) to (1, 1)Ù±‚`a
Ù±‚`h        Ù±‚bc1x##    covering the entire plot area.Ù±‚`a
Ù±‚`h        Ù±‚bc1a#Ù±‚`a
Ù±‚`h        Ù±‚bc1x;# 3. Display space: The coordinates of the resulting image,Ù±‚`a
Ù±‚`h        Ù±‚bc1x!#    often in pixels or dpi/inch.Ù±‚`a
Ù±‚`a
Ù±‚`h        Ù±‚bc1x;# This function makes heavy use of the Transform classes inÙ±‚`a
Ù±‚`h        Ù±‚bc1x=# ``lib/matplotlib/transforms.py.`` For more information, seeÙ±‚`a
Ù±‚`h        Ù±‚bc1x!# the inline documentation there.Ù±‚`a
Ù±‚`a
Ù±‚`h        Ù±‚bc1x># The goal of the first two transformations is to get from theÙ±‚`a
Ù±‚`h        Ù±‚bc1x:# data space (in this case longitude and latitude) to axesÙ±‚`a
Ù±‚`h        Ù±‚bc1x># space.  It is separated into a non-affine and affine part soÙ±‚`a
Ù±‚`h        Ù±‚bc1x># that the non-affine part does not have to be recomputed whenÙ±‚`a
Ù±‚`h        Ù±‚bc1x=# a simple affine change to the figure has been made (such asÙ±‚`a
Ù±‚`h        Ù±‚bc1x+# resizing the window or changing the dpi).Ù±‚`a
Ù±‚`a
Ù±‚`h        Ù±‚bc1x1# 1) The core transformation from data space intoÙ±‚`a
Ù±‚`h        Ù±‚bc1x9# rectilinear space defined in the HammerTransform class.Ù±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`otransProjectionÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bbpdselfÙ±‚aoa.Ù±‚`s_get_core_transformÙ±‚`a(Ù±‚bbpdselfÙ±‚aoa.Ù±‚`jRESOLUTIONÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`h        Ù±‚bc1x:# 2) The above has an output range that is not in the unitÙ±‚`a
Ù±‚`h        Ù±‚bc1x;# rectangle, so scale and translate it so it fits correctlyÙ±‚`a
Ù±‚`h        Ù±‚bc1x;# within the axes.  The peculiar calculations of xscale andÙ±‚`a
Ù±‚`h        Ù±‚bc1x=# yscale are specific to a Aitoff-Hammer projection, so don'tÙ±‚`a
Ù±‚`h        Ù±‚bc1x# worry about them too much.Ù±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`ktransAffineÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bbpdselfÙ±‚aoa.Ù±‚`u_get_affine_transformÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`h        Ù±‚bc1x:# 3) This is the transformation from axes space to displayÙ±‚`a
Ù±‚`h        Ù±‚bc1h# space.Ù±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`itransAxesÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`oBboxTransformToÙ±‚`a(Ù±‚bbpdselfÙ±‚aoa.Ù±‚`dbboxÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`h        Ù±‚bc1x># Now put these 3 transforms together -- from data all the wayÙ±‚`a
Ù±‚`h        Ù±‚bc1x8# to display coordinates.  Using the '+' operator, theseÙ±‚`a
Ù±‚`h        Ù±‚bc1x<# transforms will be applied "in order".  The transforms areÙ±‚`a
Ù±‚`h        Ù±‚bc1x:# automatically simplified, if possible, by the underlyingÙ±‚`a
Ù±‚`h        Ù±‚bc1x# transformation framework.Ù±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`itransDataÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`b\
Ù±‚`l            Ù±‚bbpdselfÙ±‚aoa.Ù±‚`otransProjectionÙ±‚`a Ù±‚aoa+Ù±‚`a Ù±‚`b\
Ù±‚`l            Ù±‚bbpdselfÙ±‚aoa.Ù±‚`ktransAffineÙ±‚`a Ù±‚aoa+Ù±‚`a Ù±‚`b\
Ù±‚`l            Ù±‚bbpdselfÙ±‚aoa.Ù±‚`itransAxesÙ±‚`a
Ù±‚`a
Ù±‚`h        Ù±‚bc1x8# The main data transformation is set up.  Now deal withÙ±‚`a
Ù±‚`h        Ù±‚bc1x# gridlines and tick labels.Ù±‚`a
Ù±‚`a
Ù±‚`h        Ù±‚bc1x9# Longitude gridlines and ticklabels.  The input to theseÙ±‚`a
Ù±‚`h        Ù±‚bc1x;# transforms are in display space in x and axes space in y.Ù±‚`a
Ù±‚`h        Ù±‚bc1x:# Therefore, the input values will be in range (-xmin, 0),Ù±‚`a
Ù±‚`h        Ù±‚bc1x=# (xmax, 1).  The goal of these transforms is to go from thatÙ±‚`a
Ù±‚`h        Ù±‚bc1x;# space to display space.  The tick labels will be offset 4Ù±‚`a
Ù±‚`h        Ù±‚bc1x# pixels from the equator.Ù±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`s_xaxis_pretransformÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`b\
Ù±‚`l            Ù±‚`hAffine2DÙ±‚`a(Ù±‚`a)Ù±‚`a Ù±‚`b\
Ù±‚`l            Ù±‚aoa.Ù±‚`escaleÙ±‚`a(Ù±‚bmfc1.0Ù±‚`a,Ù±‚`a Ù±‚bbpdselfÙ±‚aoa.Ù±‚`n_longitude_capÙ±‚`a Ù±‚aoa*Ù±‚`a Ù±‚bmfc2.0Ù±‚`a)Ù±‚`a Ù±‚`b\
Ù±‚`l            Ù±‚aoa.Ù±‚`itranslateÙ±‚`a(Ù±‚bmfc0.0Ù±‚`a,Ù±‚`a Ù±‚aoa-Ù±‚bbpdselfÙ±‚aoa.Ù±‚`n_longitude_capÙ±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`p_xaxis_transformÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`b\
Ù±‚`l            Ù±‚bbpdselfÙ±‚aoa.Ù±‚`s_xaxis_pretransformÙ±‚`a Ù±‚aoa+Ù±‚`a Ù±‚`b\
Ù±‚`l            Ù±‚bbpdselfÙ±‚aoa.Ù±‚`itransDataÙ±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`v_xaxis_text1_transformÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`b\
Ù±‚`l            Ù±‚`hAffine2DÙ±‚`a(Ù±‚`a)Ù±‚aoa.Ù±‚`escaleÙ±‚`a(Ù±‚bmfc1.0Ù±‚`a,Ù±‚`a Ù±‚bmfc0.0Ù±‚`a)Ù±‚`a Ù±‚aoa+Ù±‚`a Ù±‚`b\
Ù±‚`l            Ù±‚bbpdselfÙ±‚aoa.Ù±‚`itransDataÙ±‚`a Ù±‚aoa+Ù±‚`a Ù±‚`b\
Ù±‚`l            Ù±‚`hAffine2DÙ±‚`a(Ù±‚`a)Ù±‚aoa.Ù±‚`itranslateÙ±‚`a(Ù±‚bmfc0.0Ù±‚`a,Ù±‚`a Ù±‚bmfc4.0Ù±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`v_xaxis_text2_transformÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`b\
Ù±‚`l            Ù±‚`hAffine2DÙ±‚`a(Ù±‚`a)Ù±‚aoa.Ù±‚`escaleÙ±‚`a(Ù±‚bmfc1.0Ù±‚`a,Ù±‚`a Ù±‚bmfc0.0Ù±‚`a)Ù±‚`a Ù±‚aoa+Ù±‚`a Ù±‚`b\
Ù±‚`l            Ù±‚bbpdselfÙ±‚aoa.Ù±‚`itransDataÙ±‚`a Ù±‚aoa+Ù±‚`a Ù±‚`b\
Ù±‚`l            Ù±‚`hAffine2DÙ±‚`a(Ù±‚`a)Ù±‚aoa.Ù±‚`itranslateÙ±‚`a(Ù±‚bmfc0.0Ù±‚`a,Ù±‚`a Ù±‚aoa-Ù±‚bmfc4.0Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`h        Ù±‚bc1xA# Now set up the transforms for the latitude ticks.  The input toÙ±‚`a
Ù±‚`h        Ù±‚bc1x># these transforms are in axes space in x and display space inÙ±‚`a
Ù±‚`h        Ù±‚bc1x># y.  Therefore, the input values will be in range (0, -ymin),Ù±‚`a
Ù±‚`h        Ù±‚bc1x=# (1, ymax).  The goal of these transforms is to go from thatÙ±‚`a
Ù±‚`h        Ù±‚bc1x;# space to display space.  The tick labels will be offset 4Ù±‚`a
Ù±‚`h        Ù±‚bc1x+# pixels from the edge of the axes ellipse.Ù±‚`a
Ù±‚`h        Ù±‚`myaxis_stretchÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`hAffine2DÙ±‚`a(Ù±‚`a)Ù±‚aoa.Ù±‚`escaleÙ±‚`a(Ù±‚`bnpÙ±‚aoa.Ù±‚`bpiÙ±‚aoa*Ù±‚bmia2Ù±‚`a,Ù±‚`a Ù±‚bmia1Ù±‚`a)Ù±‚aoa.Ù±‚`itranslateÙ±‚`a(Ù±‚aoa-Ù±‚`bnpÙ±‚aoa.Ù±‚`bpiÙ±‚`a,Ù±‚`a Ù±‚bmia0Ù±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚`kyaxis_spaceÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`hAffine2DÙ±‚`a(Ù±‚`a)Ù±‚aoa.Ù±‚`escaleÙ±‚`a(Ù±‚bmfc1.0Ù±‚`a,Ù±‚`a Ù±‚bmfc1.1Ù±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`p_yaxis_transformÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`b\
Ù±‚`l            Ù±‚`myaxis_stretchÙ±‚`a Ù±‚aoa+Ù±‚`a Ù±‚`b\
Ù±‚`l            Ù±‚bbpdselfÙ±‚aoa.Ù±‚`itransDataÙ±‚`a
Ù±‚`h        Ù±‚`oyaxis_text_baseÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`b\
Ù±‚`l            Ù±‚`myaxis_stretchÙ±‚`a Ù±‚aoa+Ù±‚`a Ù±‚`b\
Ù±‚`l            Ù±‚bbpdselfÙ±‚aoa.Ù±‚`otransProjectionÙ±‚`a Ù±‚aoa+Ù±‚`a Ù±‚`b\
Ù±‚`l            Ù±‚`a(Ù±‚`kyaxis_spaceÙ±‚`a Ù±‚aoa+Ù±‚`a
Ù±‚`m             Ù±‚bbpdselfÙ±‚aoa.Ù±‚`ktransAffineÙ±‚`a Ù±‚aoa+Ù±‚`a
Ù±‚`m             Ù±‚bbpdselfÙ±‚aoa.Ù±‚`itransAxesÙ±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`v_yaxis_text1_transformÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`b\
Ù±‚`l            Ù±‚`oyaxis_text_baseÙ±‚`a Ù±‚aoa+Ù±‚`a Ù±‚`b\
Ù±‚`l            Ù±‚`hAffine2DÙ±‚`a(Ù±‚`a)Ù±‚aoa.Ù±‚`itranslateÙ±‚`a(Ù±‚aoa-Ù±‚bmfc8.0Ù±‚`a,Ù±‚`a Ù±‚bmfc0.0Ù±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`v_yaxis_text2_transformÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`b\
Ù±‚`l            Ù±‚`oyaxis_text_baseÙ±‚`a Ù±‚aoa+Ù±‚`a Ù±‚`b\
Ù±‚`l            Ù±‚`hAffine2DÙ±‚`a(Ù±‚`a)Ù±‚aoa.Ù±‚`itranslateÙ±‚`a(Ù±‚bmfc8.0Ù±‚`a,Ù±‚`a Ù±‚bmfc0.0Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚akcdefÙ±‚`a Ù±‚bnfu_get_affine_transformÙ±‚`a(Ù±‚bbpdselfÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`h        Ù±‚`itransformÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bbpdselfÙ±‚aoa.Ù±‚`s_get_core_transformÙ±‚`a(Ù±‚bmia1Ù±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚`fxscaleÙ±‚`a,Ù±‚`a Ù±‚`a_Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`itransformÙ±‚aoa.Ù±‚`itransformÙ±‚`a(Ù±‚`a(Ù±‚`bnpÙ±‚aoa.Ù±‚`bpiÙ±‚`a,Ù±‚`a Ù±‚bmia0Ù±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚`a_Ù±‚`a,Ù±‚`a Ù±‚`fyscaleÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`itransformÙ±‚aoa.Ù±‚`itransformÙ±‚`a(Ù±‚`a(Ù±‚bmia0Ù±‚`a,Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`bpiÙ±‚aoa/Ù±‚bmia2Ù±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚akfreturnÙ±‚`a Ù±‚`hAffine2DÙ±‚`a(Ù±‚`a)Ù±‚`a Ù±‚`b\
Ù±‚`l            Ù±‚aoa.Ù±‚`escaleÙ±‚`a(Ù±‚bmfc0.5Ù±‚`a Ù±‚aoa/Ù±‚`a Ù±‚`fxscaleÙ±‚`a,Ù±‚`a Ù±‚bmfc0.5Ù±‚`a Ù±‚aoa/Ù±‚`a Ù±‚`fyscaleÙ±‚`a)Ù±‚`a Ù±‚`b\
Ù±‚`l            Ù±‚aoa.Ù±‚`itranslateÙ±‚`a(Ù±‚bmfc0.5Ù±‚`a,Ù±‚`a Ù±‚bmfc0.5Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚akcdefÙ±‚`a Ù±‚bnfsget_xaxis_transformÙ±‚`a(Ù±‚bbpdselfÙ±‚`a,Ù±‚`a Ù±‚`ewhichÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1dgridÙ±‚bs1a'Ù±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`h        Ù±‚bsdx­"""
        Override this method to provide a transformation for the
        x-axis tick labels.

        Returns a tuple of the form (transform, valign, halign)
        """Ù±‚`a
Ù±‚`h        Ù±‚akbifÙ±‚`a Ù±‚`ewhichÙ±‚`a Ù±‚bowcnotÙ±‚`a Ù±‚bowbinÙ±‚`a Ù±‚`a[Ù±‚bs1a'Ù±‚bs1etick1Ù±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚bs1a'Ù±‚bs1etick2Ù±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚bs1a'Ù±‚bs1dgridÙ±‚bs1a'Ù±‚`a]Ù±‚`a:Ù±‚`a
Ù±‚`l            Ù±‚akeraiseÙ±‚`a Ù±‚bnejValueErrorÙ±‚`a(Ù±‚`a
Ù±‚`p                Ù±‚bs2a"Ù±‚bs2a'Ù±‚bs2ewhichÙ±‚bs2a'Ù±‚bs2p must be one of Ù±‚bs2a'Ù±‚bs2etick1Ù±‚bs2a'Ù±‚bs2b, Ù±‚bs2a'Ù±‚bs2etick2Ù±‚bs2a'Ù±‚bs2e, or Ù±‚bs2a'Ù±‚bs2dgridÙ±‚bs2a'Ù±‚bs2a"Ù±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚akfreturnÙ±‚`a Ù±‚bbpdselfÙ±‚aoa.Ù±‚`p_xaxis_transformÙ±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚akcdefÙ±‚`a Ù±‚bnfxget_xaxis_text1_transformÙ±‚`a(Ù±‚bbpdselfÙ±‚`a,Ù±‚`a Ù±‚`cpadÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`h        Ù±‚akfreturnÙ±‚`a Ù±‚bbpdselfÙ±‚aoa.Ù±‚`v_xaxis_text1_transformÙ±‚`a,Ù±‚`a Ù±‚bs1a'Ù±‚bs1fbottomÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚bs1a'Ù±‚bs1fcenterÙ±‚bs1a'Ù±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚akcdefÙ±‚`a Ù±‚bnfxget_xaxis_text2_transformÙ±‚`a(Ù±‚bbpdselfÙ±‚`a,Ù±‚`a Ù±‚`cpadÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`h        Ù±‚bsdx·"""
        Override this method to provide a transformation for the
        secondary x-axis tick labels.

        Returns a tuple of the form (transform, valign, halign)
        """Ù±‚`a
Ù±‚`h        Ù±‚akfreturnÙ±‚`a Ù±‚bbpdselfÙ±‚aoa.Ù±‚`v_xaxis_text2_transformÙ±‚`a,Ù±‚`a Ù±‚bs1a'Ù±‚bs1ctopÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚bs1a'Ù±‚bs1fcenterÙ±‚bs1a'Ù±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚akcdefÙ±‚`a Ù±‚bnfsget_yaxis_transformÙ±‚`a(Ù±‚bbpdselfÙ±‚`a,Ù±‚`a Ù±‚`ewhichÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1dgridÙ±‚bs1a'Ù±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`h        Ù±‚bsdxo"""
        Override this method to provide a transformation for the
        y-axis grid and ticks.
        """Ù±‚`a
Ù±‚`h        Ù±‚akbifÙ±‚`a Ù±‚`ewhichÙ±‚`a Ù±‚bowcnotÙ±‚`a Ù±‚bowbinÙ±‚`a Ù±‚`a[Ù±‚bs1a'Ù±‚bs1etick1Ù±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚bs1a'Ù±‚bs1etick2Ù±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚bs1a'Ù±‚bs1dgridÙ±‚bs1a'Ù±‚`a]Ù±‚`a:Ù±‚`a
Ù±‚`l            Ù±‚akeraiseÙ±‚`a Ù±‚bnejValueErrorÙ±‚`a(Ù±‚`a
Ù±‚`p                Ù±‚bs2a"Ù±‚bs2a'Ù±‚bs2ewhichÙ±‚bs2a'Ù±‚bs2p must be one of Ù±‚bs2a'Ù±‚bs2etick1Ù±‚bs2a'Ù±‚bs2b, Ù±‚bs2a'Ù±‚bs2etick2Ù±‚bs2a'Ù±‚bs2e, or Ù±‚bs2a'Ù±‚bs2dgridÙ±‚bs2a'Ù±‚bs2a"Ù±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚akfreturnÙ±‚`a Ù±‚bbpdselfÙ±‚aoa.Ù±‚`p_yaxis_transformÙ±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚akcdefÙ±‚`a Ù±‚bnfxget_yaxis_text1_transformÙ±‚`a(Ù±‚bbpdselfÙ±‚`a,Ù±‚`a Ù±‚`cpadÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`h        Ù±‚bsdx­"""
        Override this method to provide a transformation for the
        y-axis tick labels.

        Returns a tuple of the form (transform, valign, halign)
        """Ù±‚`a
Ù±‚`h        Ù±‚akfreturnÙ±‚`a Ù±‚bbpdselfÙ±‚aoa.Ù±‚`v_yaxis_text1_transformÙ±‚`a,Ù±‚`a Ù±‚bs1a'Ù±‚bs1fcenterÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚bs1a'Ù±‚bs1erightÙ±‚bs1a'Ù±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚akcdefÙ±‚`a Ù±‚bnfxget_yaxis_text2_transformÙ±‚`a(Ù±‚bbpdselfÙ±‚`a,Ù±‚`a Ù±‚`cpadÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`h        Ù±‚bsdx·"""
        Override this method to provide a transformation for the
        secondary y-axis tick labels.

        Returns a tuple of the form (transform, valign, halign)
        """Ù±‚`a
Ù±‚`h        Ù±‚akfreturnÙ±‚`a Ù±‚bbpdselfÙ±‚aoa.Ù±‚`v_yaxis_text2_transformÙ±‚`a,Ù±‚`a Ù±‚bs1a'Ù±‚bs1fcenterÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚bs1a'Ù±‚bs1dleftÙ±‚bs1a'Ù±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚akcdefÙ±‚`a Ù±‚bnfo_gen_axes_patchÙ±‚`a(Ù±‚bbpdselfÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`h        Ù±‚bsdyA"""
        Override this method to define the shape that is used for the
        background of the plot.  It should be a subclass of Patch.

        In this case, it is a Circle (that may be warped by the axes
        transform into an ellipse).  Any data and gridlines will be
        clipped to this shape.
        """Ù±‚`a
Ù±‚`h        Ù±‚akfreturnÙ±‚`a Ù±‚`fCircleÙ±‚`a(Ù±‚`a(Ù±‚bmfc0.5Ù±‚`a,Ù±‚`a Ù±‚bmfc0.5Ù±‚`a)Ù±‚`a,Ù±‚`a Ù±‚bmfc0.5Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚akcdefÙ±‚`a Ù±‚bnfp_gen_axes_spinesÙ±‚`a(Ù±‚bbpdselfÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`h        Ù±‚akfreturnÙ±‚`a Ù±‚`a{Ù±‚bs1a'Ù±‚bs1cgeoÙ±‚bs1a'Ù±‚`a:Ù±‚`a Ù±‚`gmspinesÙ±‚aoa.Ù±‚`eSpineÙ±‚aoa.Ù±‚`ncircular_spineÙ±‚`a(Ù±‚bbpdselfÙ±‚`a,Ù±‚`a Ù±‚`a(Ù±‚bmfc0.5Ù±‚`a,Ù±‚`a Ù±‚bmfc0.5Ù±‚`a)Ù±‚`a,Ù±‚`a Ù±‚bmfc0.5Ù±‚`a)Ù±‚`a}Ù±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚akcdefÙ±‚`a Ù±‚bnfjset_yscaleÙ±‚`a(Ù±‚bbpdselfÙ±‚`a,Ù±‚`a Ù±‚aoa*Ù±‚`dargsÙ±‚`a,Ù±‚`a Ù±‚aoa*Ù±‚aoa*Ù±‚`fkwargsÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`h        Ù±‚akbifÙ±‚`a Ù±‚`dargsÙ±‚`a[Ù±‚bmia0Ù±‚`a]Ù±‚`a Ù±‚aob!=Ù±‚`a Ù±‚bs1a'Ù±‚bs1flinearÙ±‚bs1a'Ù±‚`a:Ù±‚`a
Ù±‚`l            Ù±‚akeraiseÙ±‚`a Ù±‚bnesNotImplementedErrorÙ±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚bc1x=# Prevent the user from applying scales to one or both of theÙ±‚`a
Ù±‚`d    Ù±‚bc1x@# axes.  In this particular case, scaling the axes wouldn't makeÙ±‚`a
Ù±‚`d    Ù±‚bc1x# sense, so we don't allow it.Ù±‚`a
Ù±‚`d    Ù±‚`jset_xscaleÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`jset_yscaleÙ±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚bc1xB# Prevent the user from changing the axes limits.  In our case, weÙ±‚`a
Ù±‚`d    Ù±‚bc1x?# want to display the whole sphere all the time, so we overrideÙ±‚`a
Ù±‚`d    Ù±‚bc1xB# set_xlim and set_ylim to ignore any input.  This also applies toÙ±‚`a
Ù±‚`d    Ù±‚bc1x8# interactive panning and zooming in the GUI interfaces.Ù±‚`a
Ù±‚`d    Ù±‚akcdefÙ±‚`a Ù±‚bnfhset_xlimÙ±‚`a(Ù±‚bbpdselfÙ±‚`a,Ù±‚`a Ù±‚aoa*Ù±‚`dargsÙ±‚`a,Ù±‚`a Ù±‚aoa*Ù±‚aoa*Ù±‚`fkwargsÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`h        Ù±‚akeraiseÙ±‚`a Ù±‚bneiTypeErrorÙ±‚`a(Ù±‚bs2a"Ù±‚bs2x3Changing axes limits of a geographic projection is Ù±‚bs2a"Ù±‚`a
Ù±‚`x                        Ù±‚bs2a"Ù±‚bs2x.not supported.  Please consider using Cartopy.Ù±‚bs2a"Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚`hset_ylimÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`hset_xlimÙ±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚akcdefÙ±‚`a Ù±‚bnflformat_coordÙ±‚`a(Ù±‚bbpdselfÙ±‚`a,Ù±‚`a Ù±‚`clonÙ±‚`a,Ù±‚`a Ù±‚`clatÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`h        Ù±‚bsdx¶"""
        Override this method to change how the values are displayed in
        the status bar.

        In this case, we want them to be displayed in degrees N/S/E/W.
        """Ù±‚`a
Ù±‚`h        Ù±‚`clonÙ±‚`a,Ù±‚`a Ù±‚`clatÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`grad2degÙ±‚`a(Ù±‚`a[Ù±‚`clonÙ±‚`a,Ù±‚`a Ù±‚`clatÙ±‚`a]Ù±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚akbifÙ±‚`a Ù±‚`clatÙ±‚`a Ù±‚aoa>Ù±‚aoa=Ù±‚`a Ù±‚bmfc0.0Ù±‚`a:Ù±‚`a
Ù±‚`l            Ù±‚`bnsÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bs1a'Ù±‚bs1aNÙ±‚bs1a'Ù±‚`a
Ù±‚`h        Ù±‚akdelseÙ±‚`a:Ù±‚`a
Ù±‚`l            Ù±‚`bnsÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bs1a'Ù±‚bs1aSÙ±‚bs1a'Ù±‚`a
Ù±‚`h        Ù±‚akbifÙ±‚`a Ù±‚`clonÙ±‚`a Ù±‚aoa>Ù±‚aoa=Ù±‚`a Ù±‚bmfc0.0Ù±‚`a:Ù±‚`a
Ù±‚`l            Ù±‚`bewÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bs1a'Ù±‚bs1aEÙ±‚bs1a'Ù±‚`a
Ù±‚`h        Ù±‚akdelseÙ±‚`a:Ù±‚`a
Ù±‚`l            Ù±‚`bewÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bs1a'Ù±‚bs1aWÙ±‚bs1a'Ù±‚`a
Ù±‚`h        Ù±‚akfreturnÙ±‚`a Ù±‚`a(Ù±‚bs1a'Ù±‚bsib%fÙ±‚bseo\N{DEGREE SIGN}Ù±‚bsib%sÙ±‚bs1b, Ù±‚bsib%fÙ±‚bseo\N{DEGREE SIGN}Ù±‚bsib%sÙ±‚bs1a'Ù±‚`a
Ù±‚`p                Ù±‚aoa%Ù±‚`a Ù±‚`a(Ù±‚bnbcabsÙ±‚`a(Ù±‚`clatÙ±‚`a)Ù±‚`a,Ù±‚`a Ù±‚`bnsÙ±‚`a,Ù±‚`a Ù±‚bnbcabsÙ±‚`a(Ù±‚`clonÙ±‚`a)Ù±‚`a,Ù±‚`a Ù±‚`bewÙ±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚akcdefÙ±‚`a Ù±‚bnfrset_longitude_gridÙ±‚`a(Ù±‚bbpdselfÙ±‚`a,Ù±‚`a Ù±‚`gdegreesÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`h        Ù±‚bsdy """
        Set the number of degrees between each longitude grid.

        This is an example method that is specific to this projection
        class -- it provides a more convenient interface to set the
        ticking than set_xticks would.
        """Ù±‚`a
Ù±‚`h        Ù±‚bc1x0# Skip -180 and 180, which are the fixed limits.Ù±‚`a
Ù±‚`h        Ù±‚`dgridÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`farangeÙ±‚`a(Ù±‚aoa-Ù±‚bmic180Ù±‚`a Ù±‚aoa+Ù±‚`a Ù±‚`gdegreesÙ±‚`a,Ù±‚`a Ù±‚bmic180Ù±‚`a,Ù±‚`a Ù±‚`gdegreesÙ±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`exaxisÙ±‚aoa.Ù±‚`qset_major_locatorÙ±‚`a(Ù±‚`lFixedLocatorÙ±‚`a(Ù±‚`bnpÙ±‚aoa.Ù±‚`gdeg2radÙ±‚`a(Ù±‚`dgridÙ±‚`a)Ù±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`exaxisÙ±‚aoa.Ù±‚`sset_major_formatterÙ±‚`a(Ù±‚bbpdselfÙ±‚aoa.Ù±‚`nThetaFormatterÙ±‚`a(Ù±‚`gdegreesÙ±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚akcdefÙ±‚`a Ù±‚bnfqset_latitude_gridÙ±‚`a(Ù±‚bbpdselfÙ±‚`a,Ù±‚`a Ù±‚`gdegreesÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`h        Ù±‚bsdxí"""
        Set the number of degrees between each longitude grid.

        This is an example method that is specific to this projection
        class -- it provides a more convenient interface than
        set_yticks would.
        """Ù±‚`a
Ù±‚`h        Ù±‚bc1x.# Skip -90 and 90, which are the fixed limits.Ù±‚`a
Ù±‚`h        Ù±‚`dgridÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`farangeÙ±‚`a(Ù±‚aoa-Ù±‚bmib90Ù±‚`a Ù±‚aoa+Ù±‚`a Ù±‚`gdegreesÙ±‚`a,Ù±‚`a Ù±‚bmib90Ù±‚`a,Ù±‚`a Ù±‚`gdegreesÙ±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`eyaxisÙ±‚aoa.Ù±‚`qset_major_locatorÙ±‚`a(Ù±‚`lFixedLocatorÙ±‚`a(Ù±‚`bnpÙ±‚aoa.Ù±‚`gdeg2radÙ±‚`a(Ù±‚`dgridÙ±‚`a)Ù±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`eyaxisÙ±‚aoa.Ù±‚`sset_major_formatterÙ±‚`a(Ù±‚bbpdselfÙ±‚aoa.Ù±‚`nThetaFormatterÙ±‚`a(Ù±‚`gdegreesÙ±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚akcdefÙ±‚`a Ù±‚bnfwset_longitude_grid_endsÙ±‚`a(Ù±‚bbpdselfÙ±‚`a,Ù±‚`a Ù±‚`gdegreesÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`h        Ù±‚bsdyÚ"""
        Set the latitude(s) at which to stop drawing the longitude grids.

        Often, in geographic projections, you wouldn't want to draw
        longitude gridlines near the poles.  This allows the user to
        specify the degree at which to stop drawing longitude grids.

        This is an example method that is specific to this projection
        class -- it provides an interface to something that has no
        analogy in the base Axes class.
        """Ù±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`n_longitude_capÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`gdeg2radÙ±‚`a(Ù±‚`gdegreesÙ±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`s_xaxis_pretransformÙ±‚`a Ù±‚`b\
Ù±‚`l            Ù±‚aoa.Ù±‚`eclearÙ±‚`a(Ù±‚`a)Ù±‚`a Ù±‚`b\
Ù±‚`l            Ù±‚aoa.Ù±‚`escaleÙ±‚`a(Ù±‚bmfc1.0Ù±‚`a,Ù±‚`a Ù±‚bbpdselfÙ±‚aoa.Ù±‚`n_longitude_capÙ±‚`a Ù±‚aoa*Ù±‚`a Ù±‚bmfc2.0Ù±‚`a)Ù±‚`a Ù±‚`b\
Ù±‚`l            Ù±‚aoa.Ù±‚`itranslateÙ±‚`a(Ù±‚bmfc0.0Ù±‚`a,Ù±‚`a Ù±‚aoa-Ù±‚bbpdselfÙ±‚aoa.Ù±‚`n_longitude_capÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚akcdefÙ±‚`a Ù±‚bnfnget_data_ratioÙ±‚`a(Ù±‚bbpdselfÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`h        Ù±‚bsdxŸ"""
        Return the aspect ratio of the data itself.

        This method should be overridden by any Axes that have a
        fixed data ratio.
        """Ù±‚`a
Ù±‚`h        Ù±‚akfreturnÙ±‚`a Ù±‚bmfc1.0Ù±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚bc1xH# Interactive panning and zooming is not supported with this projection,Ù±‚`a
Ù±‚`d    Ù±‚bc1x<# so we override all of the following methods to disable it.Ù±‚`a
Ù±‚`d    Ù±‚akcdefÙ±‚`a Ù±‚bnfhcan_zoomÙ±‚`a(Ù±‚bbpdselfÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`h        Ù±‚bsdx"""
        Return whether this axes supports the zoom box button functionality.

        This axes object does not support interactive zoom box.
        """Ù±‚`a
Ù±‚`h        Ù±‚akfreturnÙ±‚`a Ù±‚bkceFalseÙ±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚akcdefÙ±‚`a Ù±‚bnfgcan_panÙ±‚`a(Ù±‚bbpdselfÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`h        Ù±‚bsdx"""
        Return whether this axes supports the pan/zoom button functionality.

        This axes object does not support interactive pan/zoom.
        """Ù±‚`a
Ù±‚`h        Ù±‚akfreturnÙ±‚`a Ù±‚bkceFalseÙ±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚akcdefÙ±‚`a Ù±‚bnfistart_panÙ±‚`a(Ù±‚bbpdselfÙ±‚`a,Ù±‚`a Ù±‚`axÙ±‚`a,Ù±‚`a Ù±‚`ayÙ±‚`a,Ù±‚`a Ù±‚`fbuttonÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`h        Ù±‚akdpassÙ±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚akcdefÙ±‚`a Ù±‚bnfgend_panÙ±‚`a(Ù±‚bbpdselfÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`h        Ù±‚akdpassÙ±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚akcdefÙ±‚`a Ù±‚bnfhdrag_panÙ±‚`a(Ù±‚bbpdselfÙ±‚`a,Ù±‚`a Ù±‚`fbuttonÙ±‚`a,Ù±‚`a Ù±‚`ckeyÙ±‚`a,Ù±‚`a Ù±‚`axÙ±‚`a,Ù±‚`a Ù±‚`ayÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`h        Ù±‚akdpassÙ±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚akeclassÙ±‚`a Ù±‚bncjHammerAxesÙ±‚`a(Ù±‚`gGeoAxesÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`d    Ù±‚bsdx—"""
    A custom class for the Aitoff-Hammer projection, an equal-area map
    projection.

    https://en.wikipedia.org/wiki/Hammer_projection
    """Ù±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚bc1x># The projection must specify a name. This will be used by theÙ±‚`a
Ù±‚`d    Ù±‚bc1x # user to select the projection,Ù±‚`a
Ù±‚`d    Ù±‚bc1x/# i.e. ``subplot(projection='custom_hammer')``.Ù±‚`a
Ù±‚`d    Ù±‚`dnameÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bs1a'Ù±‚bs1mcustom_hammerÙ±‚bs1a'Ù±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚akeclassÙ±‚`a Ù±‚bncoHammerTransformÙ±‚`a(Ù±‚`iTransformÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`h        Ù±‚bsdx """The base Hammer transform."""Ù±‚`a
Ù±‚`h        Ù±‚`jinput_dimsÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`koutput_dimsÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bmia2Ù±‚`a
Ù±‚`a
Ù±‚`h        Ù±‚akcdefÙ±‚`a Ù±‚bfmh__init__Ù±‚`a(Ù±‚bbpdselfÙ±‚`a,Ù±‚`a Ù±‚`jresolutionÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`l            Ù±‚bsdxØ"""
            Create a new Hammer transform.  Resolution is the number of steps
            to interpolate between each input line segment to approximate its
            path in curved Hammer space.
            """Ù±‚`a
Ù±‚`l            Ù±‚`iTransformÙ±‚aoa.Ù±‚bfmh__init__Ù±‚`a(Ù±‚bbpdselfÙ±‚`a)Ù±‚`a
Ù±‚`l            Ù±‚bbpdselfÙ±‚aoa.Ù±‚`k_resolutionÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`jresolutionÙ±‚`a
Ù±‚`a
Ù±‚`h        Ù±‚akcdefÙ±‚`a Ù±‚bnfttransform_non_affineÙ±‚`a(Ù±‚bbpdselfÙ±‚`a,Ù±‚`a Ù±‚`bllÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`l            Ù±‚`ilongitudeÙ±‚`a,Ù±‚`a Ù±‚`hlatitudeÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bllÙ±‚aoa.Ù±‚`aTÙ±‚`a
Ù±‚`a
Ù±‚`l            Ù±‚bc1x# Pre-compute some valuesÙ±‚`a
Ù±‚`l            Ù±‚`ihalf_longÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`ilongitudeÙ±‚`a Ù±‚aoa/Ù±‚`a Ù±‚bmia2Ù±‚`a
Ù±‚`l            Ù±‚`lcos_latitudeÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`ccosÙ±‚`a(Ù±‚`hlatitudeÙ±‚`a)Ù±‚`a
Ù±‚`l            Ù±‚`esqrt2Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`dsqrtÙ±‚`a(Ù±‚bmia2Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`l            Ù±‚`ealphaÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`dsqrtÙ±‚`a(Ù±‚bmia1Ù±‚`a Ù±‚aoa+Ù±‚`a Ù±‚`lcos_latitudeÙ±‚`a Ù±‚aoa*Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`ccosÙ±‚`a(Ù±‚`ihalf_longÙ±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`l            Ù±‚`axÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`a(Ù±‚bmia2Ù±‚`a Ù±‚aoa*Ù±‚`a Ù±‚`esqrt2Ù±‚`a)Ù±‚`a Ù±‚aoa*Ù±‚`a Ù±‚`a(Ù±‚`lcos_latitudeÙ±‚`a Ù±‚aoa*Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`csinÙ±‚`a(Ù±‚`ihalf_longÙ±‚`a)Ù±‚`a)Ù±‚`a Ù±‚aoa/Ù±‚`a Ù±‚`ealphaÙ±‚`a
Ù±‚`l            Ù±‚`ayÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`a(Ù±‚`esqrt2Ù±‚`a Ù±‚aoa*Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`csinÙ±‚`a(Ù±‚`hlatitudeÙ±‚`a)Ù±‚`a)Ù±‚`a Ù±‚aoa/Ù±‚`a Ù±‚`ealphaÙ±‚`a
Ù±‚`l            Ù±‚akfreturnÙ±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`lcolumn_stackÙ±‚`a(Ù±‚`a[Ù±‚`axÙ±‚`a,Ù±‚`a Ù±‚`ayÙ±‚`a]Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`h        Ù±‚akcdefÙ±‚`a Ù±‚bnfxtransform_path_non_affineÙ±‚`a(Ù±‚bbpdselfÙ±‚`a,Ù±‚`a Ù±‚`dpathÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`l            Ù±‚bc1x# vertices = path.verticesÙ±‚`a
Ù±‚`l            Ù±‚`eipathÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`dpathÙ±‚aoa.Ù±‚`linterpolatedÙ±‚`a(Ù±‚bbpdselfÙ±‚aoa.Ù±‚`k_resolutionÙ±‚`a)Ù±‚`a
Ù±‚`l            Ù±‚akfreturnÙ±‚`a Ù±‚`dPathÙ±‚`a(Ù±‚bbpdselfÙ±‚aoa.Ù±‚`itransformÙ±‚`a(Ù±‚`eipathÙ±‚aoa.Ù±‚`hverticesÙ±‚`a)Ù±‚`a,Ù±‚`a Ù±‚`eipathÙ±‚aoa.Ù±‚`ecodesÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`h        Ù±‚akcdefÙ±‚`a Ù±‚bnfhinvertedÙ±‚`a(Ù±‚bbpdselfÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`l            Ù±‚akfreturnÙ±‚`a Ù±‚`jHammerAxesÙ±‚aoa.Ù±‚`wInvertedHammerTransformÙ±‚`a(Ù±‚bbpdselfÙ±‚aoa.Ù±‚`k_resolutionÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚akeclassÙ±‚`a Ù±‚bncwInvertedHammerTransformÙ±‚`a(Ù±‚`iTransformÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`h        Ù±‚`jinput_dimsÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`koutput_dimsÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bmia2Ù±‚`a
Ù±‚`a
Ù±‚`h        Ù±‚akcdefÙ±‚`a Ù±‚bfmh__init__Ù±‚`a(Ù±‚bbpdselfÙ±‚`a,Ù±‚`a Ù±‚`jresolutionÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`l            Ù±‚`iTransformÙ±‚aoa.Ù±‚bfmh__init__Ù±‚`a(Ù±‚bbpdselfÙ±‚`a)Ù±‚`a
Ù±‚`l            Ù±‚bbpdselfÙ±‚aoa.Ù±‚`k_resolutionÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`jresolutionÙ±‚`a
Ù±‚`a
Ù±‚`h        Ù±‚akcdefÙ±‚`a Ù±‚bnfttransform_non_affineÙ±‚`a(Ù±‚bbpdselfÙ±‚`a,Ù±‚`a Ù±‚`bxyÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`l            Ù±‚`axÙ±‚`a,Ù±‚`a Ù±‚`ayÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bxyÙ±‚aoa.Ù±‚`aTÙ±‚`a
Ù±‚`l            Ù±‚`azÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`dsqrtÙ±‚`a(Ù±‚bmia1Ù±‚`a Ù±‚aoa-Ù±‚`a Ù±‚`a(Ù±‚`axÙ±‚`a Ù±‚aoa/Ù±‚`a Ù±‚bmia4Ù±‚`a)Ù±‚`a Ù±‚aoa*Ù±‚aoa*Ù±‚`a Ù±‚bmia2Ù±‚`a Ù±‚aoa-Ù±‚`a Ù±‚`a(Ù±‚`ayÙ±‚`a Ù±‚aoa/Ù±‚`a Ù±‚bmia2Ù±‚`a)Ù±‚`a Ù±‚aoa*Ù±‚aoa*Ù±‚`a Ù±‚bmia2Ù±‚`a)Ù±‚`a
Ù±‚`l            Ù±‚`ilongitudeÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bmia2Ù±‚`a Ù±‚aoa*Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`farctanÙ±‚`a(Ù±‚`a(Ù±‚`azÙ±‚`a Ù±‚aoa*Ù±‚`a Ù±‚`axÙ±‚`a)Ù±‚`a Ù±‚aoa/Ù±‚`a Ù±‚`a(Ù±‚bmia2Ù±‚`a Ù±‚aoa*Ù±‚`a Ù±‚`a(Ù±‚bmia2Ù±‚`a Ù±‚aoa*Ù±‚`a Ù±‚`azÙ±‚`a Ù±‚aoa*Ù±‚aoa*Ù±‚`a Ù±‚bmia2Ù±‚`a Ù±‚aoa-Ù±‚`a Ù±‚bmia1Ù±‚`a)Ù±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`l            Ù±‚`hlatitudeÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`farcsinÙ±‚`a(Ù±‚`ayÙ±‚aoa*Ù±‚`azÙ±‚`a)Ù±‚`a
Ù±‚`l            Ù±‚akfreturnÙ±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`lcolumn_stackÙ±‚`a(Ù±‚`a[Ù±‚`ilongitudeÙ±‚`a,Ù±‚`a Ù±‚`hlatitudeÙ±‚`a]Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`h        Ù±‚akcdefÙ±‚`a Ù±‚bnfhinvertedÙ±‚`a(Ù±‚bbpdselfÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`l            Ù±‚akfreturnÙ±‚`a Ù±‚`jHammerAxesÙ±‚aoa.Ù±‚`oHammerTransformÙ±‚`a(Ù±‚bbpdselfÙ±‚aoa.Ù±‚`k_resolutionÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚akcdefÙ±‚`a Ù±‚bfmh__init__Ù±‚`a(Ù±‚bbpdselfÙ±‚`a,Ù±‚`a Ù±‚aoa*Ù±‚`dargsÙ±‚`a,Ù±‚`a Ù±‚aoa*Ù±‚aoa*Ù±‚`fkwargsÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`n_longitude_capÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`bpiÙ±‚`a Ù±‚aoa/Ù±‚`a Ù±‚bmfc2.0Ù±‚`a
Ù±‚`h        Ù±‚bnbesuperÙ±‚`a(Ù±‚`a)Ù±‚aoa.Ù±‚bfmh__init__Ù±‚`a(Ù±‚aoa*Ù±‚`dargsÙ±‚`a,Ù±‚`a Ù±‚aoa*Ù±‚aoa*Ù±‚`fkwargsÙ±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`jset_aspectÙ±‚`a(Ù±‚bmfc0.5Ù±‚`a,Ù±‚`a Ù±‚`jadjustableÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1cboxÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`fanchorÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1aCÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`cclaÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚akcdefÙ±‚`a Ù±‚bnfs_get_core_transformÙ±‚`a(Ù±‚bbpdselfÙ±‚`a,Ù±‚`a Ù±‚`jresolutionÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`h        Ù±‚akfreturnÙ±‚`a Ù±‚bbpdselfÙ±‚aoa.Ù±‚`oHammerTransformÙ±‚`a(Ù±‚`jresolutionÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚bc1xH# Now register the projection with Matplotlib so the user can select it.Ù±‚`a
Ù±‚`sregister_projectionÙ±‚`a(Ù±‚`jHammerAxesÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚akbifÙ±‚`a Ù±‚bvmh__name__Ù±‚`a Ù±‚aob==Ù±‚`a Ù±‚bs1a'Ù±‚bs1h__main__Ù±‚bs1a'Ù±‚`a:Ù±‚`a
Ù±‚`d    Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnnfpyplotÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnncpltÙ±‚`a
Ù±‚`d    Ù±‚bc1x8# Now make a simple example using the custom projection.Ù±‚`a
Ù±‚`d    Ù±‚`cfigÙ±‚`a,Ù±‚`a Ù±‚`baxÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cpltÙ±‚aoa.Ù±‚`hsubplotsÙ±‚`a(Ù±‚`jsubplot_kwÙ±‚aoa=Ù±‚`a{Ù±‚bs1a'Ù±‚bs1jprojectionÙ±‚bs1a'Ù±‚`a:Ù±‚`a Ù±‚bs1a'Ù±‚bs1mcustom_hammerÙ±‚bs1a'Ù±‚`a}Ù±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`baxÙ±‚aoa.Ù±‚`dplotÙ±‚`a(Ù±‚`a[Ù±‚aoa-Ù±‚bmia1Ù±‚`a,Ù±‚`a Ù±‚bmia1Ù±‚`a,Ù±‚`a Ù±‚bmia1Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`a[Ù±‚aoa-Ù±‚bmia1Ù±‚`a,Ù±‚`a Ù±‚aoa-Ù±‚bmia1Ù±‚`a,Ù±‚`a Ù±‚bmia1Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚bs2a"Ù±‚bs2bo-Ù±‚bs2a"Ù±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`baxÙ±‚aoa.Ù±‚`dgridÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚`cpltÙ±‚aoa.Ù±‚`dshowÙ±‚`a(Ù±‚`a)Ù±‚`a
`dNoneö