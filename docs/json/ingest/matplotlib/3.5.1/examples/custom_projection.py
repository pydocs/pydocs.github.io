�����������bsdx�"""
=================
Custom projection
=================

Showcase Hammer projection by alleviating many features of Matplotlib.
"""���`a
���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����`a
���bkndfrom���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnndaxes���`a ���bknfimport���`a ���`dAxes���`a
���bkndfrom���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnngpatches���`a ���bknfimport���`a ���`fCircle���`a
���bkndfrom���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnndpath���`a ���bknfimport���`a ���`dPath���`a
���bkndfrom���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfticker���`a ���bknfimport���`a ���`kNullLocator���`a,���`a ���`iFormatter���`a,���`a ���`lFixedLocator���`a
���bkndfrom���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnjtransforms���`a ���bknfimport���`a ���`hAffine2D���`a,���`a ���`oBboxTransformTo���`a,���`a ���`iTransform���`a
���bkndfrom���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnkprojections���`a ���bknfimport���`a ���`sregister_projection���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfspines���`a ���akbas���`a ���bnngmspines���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnndaxis���`a ���akbas���`a ���bnnemaxis���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���`a
���`hrcParams���`a ���aoa=���`a ���`���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����aoa.���`hrcParams���`a
���`a
���bc1xE# This example projection class is rather long, but it is designed to���`a
���bc1xE# illustrate many features, not all of which will be used every time.���`a
���bc1xD# It is also common to factor out a lot of these methods into common���`a
���bc1xC# code used by a number of projections with similar characteristics���`a
���bc1o# (see geo.py).���`a
���`a
���`a
���akeclass���`a ���bncgGeoAxes���`a(���`dAxes���`a)���`a:���`a
���`d    ���bsdxA"""
    An abstract base class for geographic projections
    """���`a
���`d    ���akeclass���`a ���bncnThetaFormatter���`a(���`iFormatter���`a)���`a:���`a
���`h        ���bsdx�"""
        Used to format the theta tick labels.  Converts the native
        unit of radians into degrees and adds a degree symbol.
        """���`a
���`h        ���akcdef���`a ���bfmh__init__���`a(���bbpdself���`a,���`a ���`hround_to���aoa=���bmfc1.0���`a)���`a:���`a
���`l            ���bbpdself���aoa.���`i_round_to���`a ���aoa=���`a ���`hround_to���`a
���`a
���`h        ���akcdef���`a ���bfmh__call__���`a(���bbpdself���`a,���`a ���`ax���`a,���`a ���`cpos���aoa=���bkcdNone���`a)���`a:���`a
���`l            ���`gdegrees���`a ���aoa=���`a ���bnberound���`a(���`bnp���aoa.���`grad2deg���`a(���`ax���`a)���`a ���aoa/���`a ���bbpdself���aoa.���`i_round_to���`a)���`a ���aoa*���`a ���bbpdself���aoa.���`i_round_to���`a
���`l            ���akfreturn���`a ���bsaaf���bs2a"���bsia{���`gdegrees���bsia:���bs2d0.0f���bsia}���bseo\N{DEGREE SIGN}���bs2a"���`a
���`a
���`d    ���`jRESOLUTION���`a ���aoa=���`a ���bmib75���`a
���`a
���`d    ���akcdef���`a ���bnfj_init_axis���`a(���bbpdself���`a)���`a:���`a
���`h        ���bbpdself���aoa.���`exaxis���`a ���aoa=���`a ���`emaxis���aoa.���`eXAxis���`a(���bbpdself���`a)���`a
���`h        ���bbpdself���aoa.���`eyaxis���`a ���aoa=���`a ���`emaxis���aoa.���`eYAxis���`a(���bbpdself���`a)���`a
���`h        ���bc1x:# Do not register xaxis or yaxis with spines -- as done in���`a
���`h        ���bc1x9# Axes._init_axis() -- until GeoAxes.xaxis.clear() works.���`a
���`h        ���bc1x.# self.spines['geo'].register_axis(self.yaxis)���`a
���`h        ���bbpdself���aoa.���`r_update_transScale���`a(���`a)���`a
���`a
���`d    ���akcdef���`a ���bnfccla���`a(���bbpdself���`a)���`a:���`a
���`h        ���bnbesuper���`a(���`a)���aoa.���`ccla���`a(���`a)���`a
���`a
���`h        ���bbpdself���aoa.���`rset_longitude_grid���`a(���bmib30���`a)���`a
���`h        ���bbpdself���aoa.���`qset_latitude_grid���`a(���bmib15���`a)���`a
���`h        ���bbpdself���aoa.���`wset_longitude_grid_ends���`a(���bmib75���`a)���`a
���`h        ���bbpdself���aoa.���`exaxis���aoa.���`qset_minor_locator���`a(���`kNullLocator���`a(���`a)���`a)���`a
���`h        ���bbpdself���aoa.���`eyaxis���aoa.���`qset_minor_locator���`a(���`kNullLocator���`a(���`a)���`a)���`a
���`h        ���bbpdself���aoa.���`exaxis���aoa.���`rset_ticks_position���`a(���bs1a'���bs1dnone���bs1a'���`a)���`a
���`h        ���bbpdself���aoa.���`eyaxis���aoa.���`rset_ticks_position���`a(���bs1a'���bs1dnone���bs1a'���`a)���`a
���`h        ���bbpdself���aoa.���`eyaxis���aoa.���`oset_tick_params���`a(���`hlabel1On���aoa=���bkcdTrue���`a)���`a
���`h        ���bc1x2# Why do we need to turn on yaxis tick labels, but���`a
���`h        ���bc1x## xaxis tick labels are already on?���`a
���`a
���`h        ���bbpdself���aoa.���`dgrid���`a(���`hrcParams���`a[���bs1a'���bs1iaxes.grid���bs1a'���`a]���`a)���`a
���`a
���`h        ���`dAxes���aoa.���`hset_xlim���`a(���bbpdself���`a,���`a ���aoa-���`bnp���aoa.���`bpi���`a,���`a ���`bnp���aoa.���`bpi���`a)���`a
���`h        ���`dAxes���aoa.���`hset_ylim���`a(���bbpdself���`a,���`a ���aoa-���`bnp���aoa.���`bpi���`a ���aoa/���`a ���bmfc2.0���`a,���`a ���`bnp���aoa.���`bpi���`a ���aoa/���`a ���bmfc2.0���`a)���`a
���`a
���`d    ���akcdef���`a ���bnfw_set_lim_and_transforms���`a(���bbpdself���`a)���`a:���`a
���`h        ���bc1xA# A (possibly non-linear) projection on the (already scaled) data���`a
���`a
���`h        ���bc1x<# There are three important coordinate spaces going on here:���`a
���`h        ���bc1a#���`a
���`h        ���bc1x-# 1. Data space: The space of the data itself���`a
���`h        ���bc1a#���`a
���`h        ���bc1x4# 2. Axes space: The unit rectangle (0, 0) to (1, 1)���`a
���`h        ���bc1x##    covering the entire plot area.���`a
���`h        ���bc1a#���`a
���`h        ���bc1x;# 3. Display space: The coordinates of the resulting image,���`a
���`h        ���bc1x!#    often in pixels or dpi/inch.���`a
���`a
���`h        ���bc1x;# This function makes heavy use of the Transform classes in���`a
���`h        ���bc1x=# ``lib/matplotlib/transforms.py.`` For more information, see���`a
���`h        ���bc1x!# the inline documentation there.���`a
���`a
���`h        ���bc1x># The goal of the first two transformations is to get from the���`a
���`h        ���bc1x:# data space (in this case longitude and latitude) to axes���`a
���`h        ���bc1x># space.  It is separated into a non-affine and affine part so���`a
���`h        ���bc1x># that the non-affine part does not have to be recomputed when���`a
���`h        ���bc1x=# a simple affine change to the figure has been made (such as���`a
���`h        ���bc1x+# resizing the window or changing the dpi).���`a
���`a
���`h        ���bc1x1# 1) The core transformation from data space into���`a
���`h        ���bc1x9# rectilinear space defined in the HammerTransform class.���`a
���`h        ���bbpdself���aoa.���`otransProjection���`a ���aoa=���`a ���bbpdself���aoa.���`s_get_core_transform���`a(���bbpdself���aoa.���`jRESOLUTION���`a)���`a
���`a
���`h        ���bc1x:# 2) The above has an output range that is not in the unit���`a
���`h        ���bc1x;# rectangle, so scale and translate it so it fits correctly���`a
���`h        ���bc1x;# within the axes.  The peculiar calculations of xscale and���`a
���`h        ���bc1x=# yscale are specific to a Aitoff-Hammer projection, so don't���`a
���`h        ���bc1x# worry about them too much.���`a
���`h        ���bbpdself���aoa.���`ktransAffine���`a ���aoa=���`a ���bbpdself���aoa.���`u_get_affine_transform���`a(���`a)���`a
���`a
���`h        ���bc1x:# 3) This is the transformation from axes space to display���`a
���`h        ���bc1h# space.���`a
���`h        ���bbpdself���aoa.���`itransAxes���`a ���aoa=���`a ���`oBboxTransformTo���`a(���bbpdself���aoa.���`dbbox���`a)���`a
���`a
���`h        ���bc1x># Now put these 3 transforms together -- from data all the way���`a
���`h        ���bc1x8# to display coordinates.  Using the '+' operator, these���`a
���`h        ���bc1x<# transforms will be applied "in order".  The transforms are���`a
���`h        ���bc1x:# automatically simplified, if possible, by the underlying���`a
���`h        ���bc1x# transformation framework.���`a
���`h        ���bbpdself���aoa.���`itransData���`a ���aoa=���`a ���`b\
���`l            ���bbpdself���aoa.���`otransProjection���`a ���aoa+���`a ���`b\
���`l            ���bbpdself���aoa.���`ktransAffine���`a ���aoa+���`a ���`b\
���`l            ���bbpdself���aoa.���`itransAxes���`a
���`a
���`h        ���bc1x8# The main data transformation is set up.  Now deal with���`a
���`h        ���bc1x# gridlines and tick labels.���`a
���`a
���`h        ���bc1x9# Longitude gridlines and ticklabels.  The input to these���`a
���`h        ���bc1x;# transforms are in display space in x and axes space in y.���`a
���`h        ���bc1x:# Therefore, the input values will be in range (-xmin, 0),���`a
���`h        ���bc1x=# (xmax, 1).  The goal of these transforms is to go from that���`a
���`h        ���bc1x;# space to display space.  The tick labels will be offset 4���`a
���`h        ���bc1x# pixels from the equator.���`a
���`h        ���bbpdself���aoa.���`s_xaxis_pretransform���`a ���aoa=���`a ���`b\
���`l            ���`hAffine2D���`a(���`a)���`a ���`b\
���`l            ���aoa.���`escale���`a(���bmfc1.0���`a,���`a ���bbpdself���aoa.���`n_longitude_cap���`a ���aoa*���`a ���bmfc2.0���`a)���`a ���`b\
���`l            ���aoa.���`itranslate���`a(���bmfc0.0���`a,���`a ���aoa-���bbpdself���aoa.���`n_longitude_cap���`a)���`a
���`h        ���bbpdself���aoa.���`p_xaxis_transform���`a ���aoa=���`a ���`b\
���`l            ���bbpdself���aoa.���`s_xaxis_pretransform���`a ���aoa+���`a ���`b\
���`l            ���bbpdself���aoa.���`itransData���`a
���`h        ���bbpdself���aoa.���`v_xaxis_text1_transform���`a ���aoa=���`a ���`b\
���`l            ���`hAffine2D���`a(���`a)���aoa.���`escale���`a(���bmfc1.0���`a,���`a ���bmfc0.0���`a)���`a ���aoa+���`a ���`b\
���`l            ���bbpdself���aoa.���`itransData���`a ���aoa+���`a ���`b\
���`l            ���`hAffine2D���`a(���`a)���aoa.���`itranslate���`a(���bmfc0.0���`a,���`a ���bmfc4.0���`a)���`a
���`h        ���bbpdself���aoa.���`v_xaxis_text2_transform���`a ���aoa=���`a ���`b\
���`l            ���`hAffine2D���`a(���`a)���aoa.���`escale���`a(���bmfc1.0���`a,���`a ���bmfc0.0���`a)���`a ���aoa+���`a ���`b\
���`l            ���bbpdself���aoa.���`itransData���`a ���aoa+���`a ���`b\
���`l            ���`hAffine2D���`a(���`a)���aoa.���`itranslate���`a(���bmfc0.0���`a,���`a ���aoa-���bmfc4.0���`a)���`a
���`a
���`h        ���bc1xA# Now set up the transforms for the latitude ticks.  The input to���`a
���`h        ���bc1x># these transforms are in axes space in x and display space in���`a
���`h        ���bc1x># y.  Therefore, the input values will be in range (0, -ymin),���`a
���`h        ���bc1x=# (1, ymax).  The goal of these transforms is to go from that���`a
���`h        ���bc1x;# space to display space.  The tick labels will be offset 4���`a
���`h        ���bc1x+# pixels from the edge of the axes ellipse.���`a
���`h        ���`myaxis_stretch���`a ���aoa=���`a ���`hAffine2D���`a(���`a)���aoa.���`escale���`a(���`bnp���aoa.���`bpi���aoa*���bmia2���`a,���`a ���bmia1���`a)���aoa.���`itranslate���`a(���aoa-���`bnp���aoa.���`bpi���`a,���`a ���bmia0���`a)���`a
���`h        ���`kyaxis_space���`a ���aoa=���`a ���`hAffine2D���`a(���`a)���aoa.���`escale���`a(���bmfc1.0���`a,���`a ���bmfc1.1���`a)���`a
���`h        ���bbpdself���aoa.���`p_yaxis_transform���`a ���aoa=���`a ���`b\
���`l            ���`myaxis_stretch���`a ���aoa+���`a ���`b\
���`l            ���bbpdself���aoa.���`itransData���`a
���`h        ���`oyaxis_text_base���`a ���aoa=���`a ���`b\
���`l            ���`myaxis_stretch���`a ���aoa+���`a ���`b\
���`l            ���bbpdself���aoa.���`otransProjection���`a ���aoa+���`a ���`b\
���`l            ���`a(���`kyaxis_space���`a ���aoa+���`a
���`m             ���bbpdself���aoa.���`ktransAffine���`a ���aoa+���`a
���`m             ���bbpdself���aoa.���`itransAxes���`a)���`a
���`h        ���bbpdself���aoa.���`v_yaxis_text1_transform���`a ���aoa=���`a ���`b\
���`l            ���`oyaxis_text_base���`a ���aoa+���`a ���`b\
���`l            ���`hAffine2D���`a(���`a)���aoa.���`itranslate���`a(���aoa-���bmfc8.0���`a,���`a ���bmfc0.0���`a)���`a
���`h        ���bbpdself���aoa.���`v_yaxis_text2_transform���`a ���aoa=���`a ���`b\
���`l            ���`oyaxis_text_base���`a ���aoa+���`a ���`b\
���`l            ���`hAffine2D���`a(���`a)���aoa.���`itranslate���`a(���bmfc8.0���`a,���`a ���bmfc0.0���`a)���`a
���`a
���`d    ���akcdef���`a ���bnfu_get_affine_transform���`a(���bbpdself���`a)���`a:���`a
���`h        ���`itransform���`a ���aoa=���`a ���bbpdself���aoa.���`s_get_core_transform���`a(���bmia1���`a)���`a
���`h        ���`fxscale���`a,���`a ���`a_���`a ���aoa=���`a ���`itransform���aoa.���`itransform���`a(���`a(���`bnp���aoa.���`bpi���`a,���`a ���bmia0���`a)���`a)���`a
���`h        ���`a_���`a,���`a ���`fyscale���`a ���aoa=���`a ���`itransform���aoa.���`itransform���`a(���`a(���bmia0���`a,���`a ���`bnp���aoa.���`bpi���aoa/���bmia2���`a)���`a)���`a
���`h        ���akfreturn���`a ���`hAffine2D���`a(���`a)���`a ���`b\
���`l            ���aoa.���`escale���`a(���bmfc0.5���`a ���aoa/���`a ���`fxscale���`a,���`a ���bmfc0.5���`a ���aoa/���`a ���`fyscale���`a)���`a ���`b\
���`l            ���aoa.���`itranslate���`a(���bmfc0.5���`a,���`a ���bmfc0.5���`a)���`a
���`a
���`d    ���akcdef���`a ���bnfsget_xaxis_transform���`a(���bbpdself���`a,���`a ���`ewhich���aoa=���bs1a'���bs1dgrid���bs1a'���`a)���`a:���`a
���`h        ���bsdx�"""
        Override this method to provide a transformation for the
        x-axis tick labels.

        Returns a tuple of the form (transform, valign, halign)
        """���`a
���`h        ���akbif���`a ���`ewhich���`a ���bowcnot���`a ���bowbin���`a ���`a[���bs1a'���bs1etick1���bs1a'���`a,���`a ���bs1a'���bs1etick2���bs1a'���`a,���`a ���bs1a'���bs1dgrid���bs1a'���`a]���`a:���`a
���`l            ���akeraise���`a ���bnejValueError���`a(���`a
���`p                ���bs2a"���bs2a'���bs2ewhich���bs2a'���bs2p must be one of ���bs2a'���bs2etick1���bs2a'���bs2b, ���bs2a'���bs2etick2���bs2a'���bs2e, or ���bs2a'���bs2dgrid���bs2a'���bs2a"���`a)���`a
���`h        ���akfreturn���`a ���bbpdself���aoa.���`p_xaxis_transform���`a
���`a
���`d    ���akcdef���`a ���bnfxget_xaxis_text1_transform���`a(���bbpdself���`a,���`a ���`cpad���`a)���`a:���`a
���`h        ���akfreturn���`a ���bbpdself���aoa.���`v_xaxis_text1_transform���`a,���`a ���bs1a'���bs1fbottom���bs1a'���`a,���`a ���bs1a'���bs1fcenter���bs1a'���`a
���`a
���`d    ���akcdef���`a ���bnfxget_xaxis_text2_transform���`a(���bbpdself���`a,���`a ���`cpad���`a)���`a:���`a
���`h        ���bsdx�"""
        Override this method to provide a transformation for the
        secondary x-axis tick labels.

        Returns a tuple of the form (transform, valign, halign)
        """���`a
���`h        ���akfreturn���`a ���bbpdself���aoa.���`v_xaxis_text2_transform���`a,���`a ���bs1a'���bs1ctop���bs1a'���`a,���`a ���bs1a'���bs1fcenter���bs1a'���`a
���`a
���`d    ���akcdef���`a ���bnfsget_yaxis_transform���`a(���bbpdself���`a,���`a ���`ewhich���aoa=���bs1a'���bs1dgrid���bs1a'���`a)���`a:���`a
���`h        ���bsdxo"""
        Override this method to provide a transformation for the
        y-axis grid and ticks.
        """���`a
���`h        ���akbif���`a ���`ewhich���`a ���bowcnot���`a ���bowbin���`a ���`a[���bs1a'���bs1etick1���bs1a'���`a,���`a ���bs1a'���bs1etick2���bs1a'���`a,���`a ���bs1a'���bs1dgrid���bs1a'���`a]���`a:���`a
���`l            ���akeraise���`a ���bnejValueError���`a(���`a
���`p                ���bs2a"���bs2a'���bs2ewhich���bs2a'���bs2p must be one of ���bs2a'���bs2etick1���bs2a'���bs2b, ���bs2a'���bs2etick2���bs2a'���bs2e, or ���bs2a'���bs2dgrid���bs2a'���bs2a"���`a)���`a
���`h        ���akfreturn���`a ���bbpdself���aoa.���`p_yaxis_transform���`a
���`a
���`d    ���akcdef���`a ���bnfxget_yaxis_text1_transform���`a(���bbpdself���`a,���`a ���`cpad���`a)���`a:���`a
���`h        ���bsdx�"""
        Override this method to provide a transformation for the
        y-axis tick labels.

        Returns a tuple of the form (transform, valign, halign)
        """���`a
���`h        ���akfreturn���`a ���bbpdself���aoa.���`v_yaxis_text1_transform���`a,���`a ���bs1a'���bs1fcenter���bs1a'���`a,���`a ���bs1a'���bs1eright���bs1a'���`a
���`a
���`d    ���akcdef���`a ���bnfxget_yaxis_text2_transform���`a(���bbpdself���`a,���`a ���`cpad���`a)���`a:���`a
���`h        ���bsdx�"""
        Override this method to provide a transformation for the
        secondary y-axis tick labels.

        Returns a tuple of the form (transform, valign, halign)
        """���`a
���`h        ���akfreturn���`a ���bbpdself���aoa.���`v_yaxis_text2_transform���`a,���`a ���bs1a'���bs1fcenter���bs1a'���`a,���`a ���bs1a'���bs1dleft���bs1a'���`a
���`a
���`d    ���akcdef���`a ���bnfo_gen_axes_patch���`a(���bbpdself���`a)���`a:���`a
���`h        ���bsdyA"""
        Override this method to define the shape that is used for the
        background of the plot.  It should be a subclass of Patch.

        In this case, it is a Circle (that may be warped by the axes
        transform into an ellipse).  Any data and gridlines will be
        clipped to this shape.
        """���`a
���`h        ���akfreturn���`a ���`fCircle���`a(���`a(���bmfc0.5���`a,���`a ���bmfc0.5���`a)���`a,���`a ���bmfc0.5���`a)���`a
���`a
���`d    ���akcdef���`a ���bnfp_gen_axes_spines���`a(���bbpdself���`a)���`a:���`a
���`h        ���akfreturn���`a ���`a{���bs1a'���bs1cgeo���bs1a'���`a:���`a ���`gmspines���aoa.���`eSpine���aoa.���`ncircular_spine���`a(���bbpdself���`a,���`a ���`a(���bmfc0.5���`a,���`a ���bmfc0.5���`a)���`a,���`a ���bmfc0.5���`a)���`a}���`a
���`a
���`d    ���akcdef���`a ���bnfjset_yscale���`a(���bbpdself���`a,���`a ���aoa*���`dargs���`a,���`a ���aoa*���aoa*���`fkwargs���`a)���`a:���`a
���`h        ���akbif���`a ���`dargs���`a[���bmia0���`a]���`a ���aob!=���`a ���bs1a'���bs1flinear���bs1a'���`a:���`a
���`l            ���akeraise���`a ���bnesNotImplementedError���`a
���`a
���`d    ���bc1x=# Prevent the user from applying scales to one or both of the���`a
���`d    ���bc1x@# axes.  In this particular case, scaling the axes wouldn't make���`a
���`d    ���bc1x# sense, so we don't allow it.���`a
���`d    ���`jset_xscale���`a ���aoa=���`a ���`jset_yscale���`a
���`a
���`d    ���bc1xB# Prevent the user from changing the axes limits.  In our case, we���`a
���`d    ���bc1x?# want to display the whole sphere all the time, so we override���`a
���`d    ���bc1xB# set_xlim and set_ylim to ignore any input.  This also applies to���`a
���`d    ���bc1x8# interactive panning and zooming in the GUI interfaces.���`a
���`d    ���akcdef���`a ���bnfhset_xlim���`a(���bbpdself���`a,���`a ���aoa*���`dargs���`a,���`a ���aoa*���aoa*���`fkwargs���`a)���`a:���`a
���`h        ���akeraise���`a ���bneiTypeError���`a(���bs2a"���bs2x3Changing axes limits of a geographic projection is ���bs2a"���`a
���`x                        ���bs2a"���bs2x.not supported.  Please consider using Cartopy.���bs2a"���`a)���`a
���`a
���`d    ���`hset_ylim���`a ���aoa=���`a ���`hset_xlim���`a
���`a
���`d    ���akcdef���`a ���bnflformat_coord���`a(���bbpdself���`a,���`a ���`clon���`a,���`a ���`clat���`a)���`a:���`a
���`h        ���bsdx�"""
        Override this method to change how the values are displayed in
        the status bar.

        In this case, we want them to be displayed in degrees N/S/E/W.
        """���`a
���`h        ���`clon���`a,���`a ���`clat���`a ���aoa=���`a ���`bnp���aoa.���`grad2deg���`a(���`a[���`clon���`a,���`a ���`clat���`a]���`a)���`a
���`h        ���akbif���`a ���`clat���`a ���aoa>���aoa=���`a ���bmfc0.0���`a:���`a
���`l            ���`bns���`a ���aoa=���`a ���bs1a'���bs1aN���bs1a'���`a
���`h        ���akdelse���`a:���`a
���`l            ���`bns���`a ���aoa=���`a ���bs1a'���bs1aS���bs1a'���`a
���`h        ���akbif���`a ���`clon���`a ���aoa>���aoa=���`a ���bmfc0.0���`a:���`a
���`l            ���`bew���`a ���aoa=���`a ���bs1a'���bs1aE���bs1a'���`a
���`h        ���akdelse���`a:���`a
���`l            ���`bew���`a ���aoa=���`a ���bs1a'���bs1aW���bs1a'���`a
���`h        ���akfreturn���`a ���`a(���bs1a'���bsib%f���bseo\N{DEGREE SIGN}���bsib%s���bs1b, ���bsib%f���bseo\N{DEGREE SIGN}���bsib%s���bs1a'���`a
���`p                ���aoa%���`a ���`a(���bnbcabs���`a(���`clat���`a)���`a,���`a ���`bns���`a,���`a ���bnbcabs���`a(���`clon���`a)���`a,���`a ���`bew���`a)���`a)���`a
���`a
���`d    ���akcdef���`a ���bnfrset_longitude_grid���`a(���bbpdself���`a,���`a ���`gdegrees���`a)���`a:���`a
���`h        ���bsdy """
        Set the number of degrees between each longitude grid.

        This is an example method that is specific to this projection
        class -- it provides a more convenient interface to set the
        ticking than set_xticks would.
        """���`a
���`h        ���bc1x0# Skip -180 and 180, which are the fixed limits.���`a
���`h        ���`dgrid���`a ���aoa=���`a ���`bnp���aoa.���`farange���`a(���aoa-���bmic180���`a ���aoa+���`a ���`gdegrees���`a,���`a ���bmic180���`a,���`a ���`gdegrees���`a)���`a
���`h        ���bbpdself���aoa.���`exaxis���aoa.���`qset_major_locator���`a(���`lFixedLocator���`a(���`bnp���aoa.���`gdeg2rad���`a(���`dgrid���`a)���`a)���`a)���`a
���`h        ���bbpdself���aoa.���`exaxis���aoa.���`sset_major_formatter���`a(���bbpdself���aoa.���`nThetaFormatter���`a(���`gdegrees���`a)���`a)���`a
���`a
���`d    ���akcdef���`a ���bnfqset_latitude_grid���`a(���bbpdself���`a,���`a ���`gdegrees���`a)���`a:���`a
���`h        ���bsdx�"""
        Set the number of degrees between each longitude grid.

        This is an example method that is specific to this projection
        class -- it provides a more convenient interface than
        set_yticks would.
        """���`a
���`h        ���bc1x.# Skip -90 and 90, which are the fixed limits.���`a
���`h        ���`dgrid���`a ���aoa=���`a ���`bnp���aoa.���`farange���`a(���aoa-���bmib90���`a ���aoa+���`a ���`gdegrees���`a,���`a ���bmib90���`a,���`a ���`gdegrees���`a)���`a
���`h        ���bbpdself���aoa.���`eyaxis���aoa.���`qset_major_locator���`a(���`lFixedLocator���`a(���`bnp���aoa.���`gdeg2rad���`a(���`dgrid���`a)���`a)���`a)���`a
���`h        ���bbpdself���aoa.���`eyaxis���aoa.���`sset_major_formatter���`a(���bbpdself���aoa.���`nThetaFormatter���`a(���`gdegrees���`a)���`a)���`a
���`a
���`d    ���akcdef���`a ���bnfwset_longitude_grid_ends���`a(���bbpdself���`a,���`a ���`gdegrees���`a)���`a:���`a
���`h        ���bsdy�"""
        Set the latitude(s) at which to stop drawing the longitude grids.

        Often, in geographic projections, you wouldn't want to draw
        longitude gridlines near the poles.  This allows the user to
        specify the degree at which to stop drawing longitude grids.

        This is an example method that is specific to this projection
        class -- it provides an interface to something that has no
        analogy in the base Axes class.
        """���`a
���`h        ���bbpdself���aoa.���`n_longitude_cap���`a ���aoa=���`a ���`bnp���aoa.���`gdeg2rad���`a(���`gdegrees���`a)���`a
���`h        ���bbpdself���aoa.���`s_xaxis_pretransform���`a ���`b\
���`l            ���aoa.���`eclear���`a(���`a)���`a ���`b\
���`l            ���aoa.���`escale���`a(���bmfc1.0���`a,���`a ���bbpdself���aoa.���`n_longitude_cap���`a ���aoa*���`a ���bmfc2.0���`a)���`a ���`b\
���`l            ���aoa.���`itranslate���`a(���bmfc0.0���`a,���`a ���aoa-���bbpdself���aoa.���`n_longitude_cap���`a)���`a
���`a
���`d    ���akcdef���`a ���bnfnget_data_ratio���`a(���bbpdself���`a)���`a:���`a
���`h        ���bsdx�"""
        Return the aspect ratio of the data itself.

        This method should be overridden by any Axes that have a
        fixed data ratio.
        """���`a
���`h        ���akfreturn���`a ���bmfc1.0���`a
���`a
���`d    ���bc1xH# Interactive panning and zooming is not supported with this projection,���`a
���`d    ���bc1x<# so we override all of the following methods to disable it.���`a
���`d    ���akcdef���`a ���bnfhcan_zoom���`a(���bbpdself���`a)���`a:���`a
���`h        ���bsdx�"""
        Return whether this axes supports the zoom box button functionality.

        This axes object does not support interactive zoom box.
        """���`a
���`h        ���akfreturn���`a ���bkceFalse���`a
���`a
���`d    ���akcdef���`a ���bnfgcan_pan���`a(���bbpdself���`a)���`a:���`a
���`h        ���bsdx�"""
        Return whether this axes supports the pan/zoom button functionality.

        This axes object does not support interactive pan/zoom.
        """���`a
���`h        ���akfreturn���`a ���bkceFalse���`a
���`a
���`d    ���akcdef���`a ���bnfistart_pan���`a(���bbpdself���`a,���`a ���`ax���`a,���`a ���`ay���`a,���`a ���`fbutton���`a)���`a:���`a
���`h        ���akdpass���`a
���`a
���`d    ���akcdef���`a ���bnfgend_pan���`a(���bbpdself���`a)���`a:���`a
���`h        ���akdpass���`a
���`a
���`d    ���akcdef���`a ���bnfhdrag_pan���`a(���bbpdself���`a,���`a ���`fbutton���`a,���`a ���`ckey���`a,���`a ���`ax���`a,���`a ���`ay���`a)���`a:���`a
���`h        ���akdpass���`a
���`a
���`a
���akeclass���`a ���bncjHammerAxes���`a(���`gGeoAxes���`a)���`a:���`a
���`d    ���bsdx�"""
    A custom class for the Aitoff-Hammer projection, an equal-area map
    projection.

    https://en.wikipedia.org/wiki/Hammer_projection
    """���`a
���`a
���`d    ���bc1x># The projection must specify a name. This will be used by the���`a
���`d    ���bc1x # user to select the projection,���`a
���`d    ���bc1x/# i.e. ``subplot(projection='custom_hammer')``.���`a
���`d    ���`dname���`a ���aoa=���`a ���bs1a'���bs1mcustom_hammer���bs1a'���`a
���`a
���`d    ���akeclass���`a ���bncoHammerTransform���`a(���`iTransform���`a)���`a:���`a
���`h        ���bsdx """The base Hammer transform."""���`a
���`h        ���`jinput_dims���`a ���aoa=���`a ���`koutput_dims���`a ���aoa=���`a ���bmia2���`a
���`a
���`h        ���akcdef���`a ���bfmh__init__���`a(���bbpdself���`a,���`a ���`jresolution���`a)���`a:���`a
���`l            ���bsdx�"""
            Create a new Hammer transform.  Resolution is the number of steps
            to interpolate between each input line segment to approximate its
            path in curved Hammer space.
            """���`a
���`l            ���`iTransform���aoa.���bfmh__init__���`a(���bbpdself���`a)���`a
���`l            ���bbpdself���aoa.���`k_resolution���`a ���aoa=���`a ���`jresolution���`a
���`a
���`h        ���akcdef���`a ���bnfttransform_non_affine���`a(���bbpdself���`a,���`a ���`bll���`a)���`a:���`a
���`l            ���`ilongitude���`a,���`a ���`hlatitude���`a ���aoa=���`a ���`bll���aoa.���`aT���`a
���`a
���`l            ���bc1x# Pre-compute some values���`a
���`l            ���`ihalf_long���`a ���aoa=���`a ���`ilongitude���`a ���aoa/���`a ���bmia2���`a
���`l            ���`lcos_latitude���`a ���aoa=���`a ���`bnp���aoa.���`ccos���`a(���`hlatitude���`a)���`a
���`l            ���`esqrt2���`a ���aoa=���`a ���`bnp���aoa.���`dsqrt���`a(���bmia2���`a)���`a
���`a
���`l            ���`ealpha���`a ���aoa=���`a ���`bnp���aoa.���`dsqrt���`a(���bmia1���`a ���aoa+���`a ���`lcos_latitude���`a ���aoa*���`a ���`bnp���aoa.���`ccos���`a(���`ihalf_long���`a)���`a)���`a
���`l            ���`ax���`a ���aoa=���`a ���`a(���bmia2���`a ���aoa*���`a ���`esqrt2���`a)���`a ���aoa*���`a ���`a(���`lcos_latitude���`a ���aoa*���`a ���`bnp���aoa.���`csin���`a(���`ihalf_long���`a)���`a)���`a ���aoa/���`a ���`ealpha���`a
���`l            ���`ay���`a ���aoa=���`a ���`a(���`esqrt2���`a ���aoa*���`a ���`bnp���aoa.���`csin���`a(���`hlatitude���`a)���`a)���`a ���aoa/���`a ���`ealpha���`a
���`l            ���akfreturn���`a ���`bnp���aoa.���`lcolumn_stack���`a(���`a[���`ax���`a,���`a ���`ay���`a]���`a)���`a
���`a
���`h        ���akcdef���`a ���bnfxtransform_path_non_affine���`a(���bbpdself���`a,���`a ���`dpath���`a)���`a:���`a
���`l            ���bc1x# vertices = path.vertices���`a
���`l            ���`eipath���`a ���aoa=���`a ���`dpath���aoa.���`linterpolated���`a(���bbpdself���aoa.���`k_resolution���`a)���`a
���`l            ���akfreturn���`a ���`dPath���`a(���bbpdself���aoa.���`itransform���`a(���`eipath���aoa.���`hvertices���`a)���`a,���`a ���`eipath���aoa.���`ecodes���`a)���`a
���`a
���`h        ���akcdef���`a ���bnfhinverted���`a(���bbpdself���`a)���`a:���`a
���`l            ���akfreturn���`a ���`jHammerAxes���aoa.���`wInvertedHammerTransform���`a(���bbpdself���aoa.���`k_resolution���`a)���`a
���`a
���`d    ���akeclass���`a ���bncwInvertedHammerTransform���`a(���`iTransform���`a)���`a:���`a
���`h        ���`jinput_dims���`a ���aoa=���`a ���`koutput_dims���`a ���aoa=���`a ���bmia2���`a
���`a
���`h        ���akcdef���`a ���bfmh__init__���`a(���bbpdself���`a,���`a ���`jresolution���`a)���`a:���`a
���`l            ���`iTransform���aoa.���bfmh__init__���`a(���bbpdself���`a)���`a
���`l            ���bbpdself���aoa.���`k_resolution���`a ���aoa=���`a ���`jresolution���`a
���`a
���`h        ���akcdef���`a ���bnfttransform_non_affine���`a(���bbpdself���`a,���`a ���`bxy���`a)���`a:���`a
���`l            ���`ax���`a,���`a ���`ay���`a ���aoa=���`a ���`bxy���aoa.���`aT���`a
���`l            ���`az���`a ���aoa=���`a ���`bnp���aoa.���`dsqrt���`a(���bmia1���`a ���aoa-���`a ���`a(���`ax���`a ���aoa/���`a ���bmia4���`a)���`a ���aoa*���aoa*���`a ���bmia2���`a ���aoa-���`a ���`a(���`ay���`a ���aoa/���`a ���bmia2���`a)���`a ���aoa*���aoa*���`a ���bmia2���`a)���`a
���`l            ���`ilongitude���`a ���aoa=���`a ���bmia2���`a ���aoa*���`a ���`bnp���aoa.���`farctan���`a(���`a(���`az���`a ���aoa*���`a ���`ax���`a)���`a ���aoa/���`a ���`a(���bmia2���`a ���aoa*���`a ���`a(���bmia2���`a ���aoa*���`a ���`az���`a ���aoa*���aoa*���`a ���bmia2���`a ���aoa-���`a ���bmia1���`a)���`a)���`a)���`a
���`l            ���`hlatitude���`a ���aoa=���`a ���`bnp���aoa.���`farcsin���`a(���`ay���aoa*���`az���`a)���`a
���`l            ���akfreturn���`a ���`bnp���aoa.���`lcolumn_stack���`a(���`a[���`ilongitude���`a,���`a ���`hlatitude���`a]���`a)���`a
���`a
���`h        ���akcdef���`a ���bnfhinverted���`a(���bbpdself���`a)���`a:���`a
���`l            ���akfreturn���`a ���`jHammerAxes���aoa.���`oHammerTransform���`a(���bbpdself���aoa.���`k_resolution���`a)���`a
���`a
���`d    ���akcdef���`a ���bfmh__init__���`a(���bbpdself���`a,���`a ���aoa*���`dargs���`a,���`a ���aoa*���aoa*���`fkwargs���`a)���`a:���`a
���`h        ���bbpdself���aoa.���`n_longitude_cap���`a ���aoa=���`a ���`bnp���aoa.���`bpi���`a ���aoa/���`a ���bmfc2.0���`a
���`h        ���bnbesuper���`a(���`a)���aoa.���bfmh__init__���`a(���aoa*���`dargs���`a,���`a ���aoa*���aoa*���`fkwargs���`a)���`a
���`h        ���bbpdself���aoa.���`jset_aspect���`a(���bmfc0.5���`a,���`a ���`jadjustable���aoa=���bs1a'���bs1cbox���bs1a'���`a,���`a ���`fanchor���aoa=���bs1a'���bs1aC���bs1a'���`a)���`a
���`h        ���bbpdself���aoa.���`ccla���`a(���`a)���`a
���`a
���`d    ���akcdef���`a ���bnfs_get_core_transform���`a(���bbpdself���`a,���`a ���`jresolution���`a)���`a:���`a
���`h        ���akfreturn���`a ���bbpdself���aoa.���`oHammerTransform���`a(���`jresolution���`a)���`a
���`a
���`a
���bc1xH# Now register the projection with Matplotlib so the user can select it.���`a
���`sregister_projection���`a(���`jHammerAxes���`a)���`a
���`a
���`a
���akbif���`a ���bvmh__name__���`a ���aob==���`a ���bs1a'���bs1h__main__���bs1a'���`a:���`a
���`d    ���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���`d    ���bc1x8# Now make a simple example using the custom projection.���`a
���`d    ���`cfig���`a,���`a ���`bax���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`jsubplot_kw���aoa=���`a{���bs1a'���bs1jprojection���bs1a'���`a:���`a ���bs1a'���bs1mcustom_hammer���bs1a'���`a}���`a)���`a
���`d    ���`bax���aoa.���`dplot���`a(���`a[���aoa-���bmia1���`a,���`a ���bmia1���`a,���`a ���bmia1���`a]���`a,���`a ���`a[���aoa-���bmia1���`a,���`a ���aoa-���bmia1���`a,���`a ���bmia1���`a]���`a,���`a ���bs2a"���bs2bo-���bs2a"���`a)���`a
���`d    ���`bax���aoa.���`dgrid���`a(���`a)���`a
���`a
���`d    ���`cplt���aoa.���`dshow���`a(���`a)���`a
`dNone�