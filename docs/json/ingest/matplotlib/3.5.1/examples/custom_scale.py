��������;���bsdy�"""
============
Custom scale
============

Create a custom scale, by implementing the scaling use for latitude data in a
Mercator Projection.

Unless you are making special use of the `.Transform` class, you probably
don't need to use this verbose method, and instead can use `~.scale.FuncScale`
and the ``'function'`` option of `~.Axes.set_xscale` and `~.Axes.set_yscale`.
See the last example in :doc:`/gallery/scales/scales`.
"""���`a
���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���bkndfrom���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���bknfimport���`a ���`bma���`a
���bkndfrom���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����`a ���bknfimport���`a ���`escale���`a ���akbas���`a ���`fmscale���`a
���bkndfrom���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����`a ���bknfimport���`a ���`jtransforms���`a ���akbas���`a ���`kmtransforms���`a
���bkndfrom���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfticker���`a ���bknfimport���`a ���`lFixedLocator���`a,���`a ���`mFuncFormatter���`a
���`a
���`a
���akeclass���`a ���bncuMercatorLatitudeScale���`a(���`fmscale���aoa.���`iScaleBase���`a)���`a:���`a
���`d    ���bsdy�"""
    Scales data in range -pi/2 to pi/2 (-90 to 90 degrees) using
    the system used to scale latitudes in a Mercator__ projection.

    The scale function:
      ln(tan(y) + sec(y))

    The inverse scale function:
      atan(sinh(y))

    Since the Mercator scale tends to infinity at +/- 90 degrees,
    there is user-defined threshold, above and below which nothing
    will be plotted.  This defaults to +/- 85 degrees.

    __ https://en.wikipedia.org/wiki/Mercator_projection
    """���`a
���`a
���`d    ���bc1xJ# The scale class must have a member ``name`` that defines the string used���`a
���`d    ���bc1xK# to select the scale.  For example, ``ax.set_yscale("mercator")`` would be���`a
���`d    ���bc1x# used to select this scale.���`a
���`d    ���`dname���`a ���aoa=���`a ���bs1a'���bs1hmercator���bs1a'���`a
���`a
���`d    ���akcdef���`a ���bfmh__init__���`a(���bbpdself���`a,���`a ���`daxis���`a,���`a ���aoa*���`a,���`a ���`fthresh���aoa=���`bnp���aoa.���`gdeg2rad���`a(���bmib85���`a)���`a,���`a ���aoa*���aoa*���`fkwargs���`a)���`a:���`a
���`h        ���bsdx�"""
        Any keyword arguments passed to ``set_xscale`` and ``set_yscale`` will
        be passed along to the scale's constructor.

        thresh: The degree above which to crop the data.
        """���`a
���`h        ���bnbesuper���`a(���`a)���aoa.���bfmh__init__���`a(���`daxis���`a)���`a
���`h        ���akbif���`a ���`fthresh���`a ���aoa>���aoa=���`a ���`bnp���aoa.���`bpi���`a ���aoa/���`a ���bmia2���`a:���`a
���`l            ���akeraise���`a ���bnejValueError���`a(���bs2a"���bs2xthresh must be less than pi/2���bs2a"���`a)���`a
���`h        ���bbpdself���aoa.���`fthresh���`a ���aoa=���`a ���`fthresh���`a
���`a
���`d    ���akcdef���`a ���bnfmget_transform���`a(���bbpdself���`a)���`a:���`a
���`h        ���bsdx�"""
        Override this method to return a new instance that does the
        actual transformation of the data.

        The MercatorLatitudeTransform class is defined below as a
        nested class of this one.
        """���`a
���`h        ���akfreturn���`a ���bbpdself���aoa.���`xMercatorLatitudeTransform���`a(���bbpdself���aoa.���`fthresh���`a)���`a
���`a
���`d    ���akcdef���`a ���bnfx#set_default_locators_and_formatters���`a(���bbpdself���`a,���`a ���`daxis���`a)���`a:���`a
���`h        ���bsdy"""
        Override to set up the locators and formatters to use with the
        scale.  This is only required if the scale requires custom
        locators and formatters.  Writing custom locators and
        formatters is rather outside the scope of this example, but
        there are many helpful examples in :mod:`.ticker`.

        In our case, the Mercator example uses a fixed locator from -90 to 90
        degrees and a custom formatter to convert the radians to degrees and
        put a degree symbol after the value.
        """���`a
���`h        ���`cfmt���`a ���aoa=���`a ���`mFuncFormatter���`a(���`a
���`l            ���akflambda���`a ���`ax���`a,���`a ���`cpos���aoa=���bkcdNone���`a:���`a ���bsaaf���bs2a"���bsia{���`bnp���aoa.���`gdegrees���`a(���`ax���`a)���bsia:���bs2c.0f���bsia}���bseo\N{DEGREE SIGN}���bs2a"���`a)���`a
���`h        ���`daxis���aoa.���`cset���`a(���`mmajor_locator���aoa=���`lFixedLocator���`a(���`bnp���aoa.���`gradians���`a(���bnberange���`a(���aoa-���bmib90���`a,���`a ���bmib90���`a,���`a ���bmib10���`a)���`a)���`a)���`a,���`a
���`q                 ���`omajor_formatter���aoa=���`cfmt���`a,���`a ���`ominor_formatter���aoa=���`cfmt���`a)���`a
���`a
���`d    ���akcdef���`a ���bnfulimit_range_for_scale���`a(���bbpdself���`a,���`a ���`dvmin���`a,���`a ���`dvmax���`a,���`a ���`fminpos���`a)���`a:���`a
���`h        ���bsdy�"""
        Override to limit the bounds of the axis to the domain of the
        transform.  In the case of Mercator, the bounds should be
        limited to the threshold that was passed in.  Unlike the
        autoscaling provided by the tick locators, this range limiting
        will always be adhered to, whether the axis range is set
        manually, determined automatically or changed through panning
        and zooming.
        """���`a
���`h        ���akfreturn���`a ���bnbcmax���`a(���`dvmin���`a,���`a ���aoa-���bbpdself���aoa.���`fthresh���`a)���`a,���`a ���bnbcmin���`a(���`dvmax���`a,���`a ���bbpdself���aoa.���`fthresh���`a)���`a
���`a
���`d    ���akeclass���`a ���bncxMercatorLatitudeTransform���`a(���`kmtransforms���aoa.���`iTransform���`a)���`a:���`a
���`h        ���bc1x3# There are two value members that must be defined.���`a
���`h        ���bc1x<# ``input_dims`` and ``output_dims`` specify number of input���`a
���`h        ���bc1x9# dimensions and output dimensions to the transformation.���`a
���`h        ���bc1x;# These are used by the transformation framework to do some���`a
���`h        ���bc1x># error checking and prevent incompatible transformations from���`a
���`h        ���bc1x;# being connected together.  When defining transforms for a���`a
���`h        ���bc1x># scale, which are, by definition, separable and have only one���`a
���`h        ���bc1x5# dimension, these members should always be set to 1.���`a
���`h        ���`jinput_dims���`a ���aoa=���`a ���`koutput_dims���`a ���aoa=���`a ���bmia1���`a
���`a
���`h        ���akcdef���`a ���bfmh__init__���`a(���bbpdself���`a,���`a ���`fthresh���`a)���`a:���`a
���`l            ���`kmtransforms���aoa.���`iTransform���aoa.���bfmh__init__���`a(���bbpdself���`a)���`a
���`l            ���bbpdself���aoa.���`fthresh���`a ���aoa=���`a ���`fthresh���`a
���`a
���`h        ���akcdef���`a ���bnfttransform_non_affine���`a(���bbpdself���`a,���`a ���`aa���`a)���`a:���`a
���`l            ���bsdy:"""
            This transform takes a numpy array and returns a transformed copy.
            Since the range of the Mercator scale is limited by the
            user-specified threshold, the input array must be masked to
            contain only valid values.  Matplotlib will handle masked arrays
            and remove the out-of-range data from the plot.  However, the
            returned array *must* have the same shape as the input array, since
            these values need to remain synchronized with values in the other
            dimension.
            """���`a
���`l            ���`fmasked���`a ���aoa=���`a ���`bma���aoa.���`lmasked_where���`a(���`a(���`aa���`a ���aoa<���`a ���aoa-���bbpdself���aoa.���`fthresh���`a)���`a ���aoa|���`a ���`a(���`aa���`a ���aoa>���`a ���bbpdself���aoa.���`fthresh���`a)���`a,���`a ���`aa���`a)���`a
���`l            ���akbif���`a ���`fmasked���aoa.���`dmask���aoa.���`cany���`a(���`a)���`a:���`a
���`p                ���akfreturn���`a ���`bma���aoa.���`clog���`a(���`bnp���aoa.���`cabs���`a(���`bma���aoa.���`ctan���`a(���`fmasked���`a)���`a ���aoa+���`a ���bmia1���`a ���aoa/���`a ���`bma���aoa.���`ccos���`a(���`fmasked���`a)���`a)���`a)���`a
���`l            ���akdelse���`a:���`a
���`p                ���akfreturn���`a ���`bnp���aoa.���`clog���`a(���`bnp���aoa.���`cabs���`a(���`bnp���aoa.���`ctan���`a(���`aa���`a)���`a ���aoa+���`a ���bmia1���`a ���aoa/���`a ���`bnp���aoa.���`ccos���`a(���`aa���`a)���`a)���`a)���`a
���`a
���`h        ���akcdef���`a ���bnfhinverted���`a(���bbpdself���`a)���`a:���`a
���`l            ���bsdx�"""
            Override this method so Matplotlib knows how to get the
            inverse transform for this transform.
            """���`a
���`l            ���akfreturn���`a ���`uMercatorLatitudeScale���aoa.���`x!InvertedMercatorLatitudeTransform���`a(���`a
���`p                ���bbpdself���aoa.���`fthresh���`a)���`a
���`a
���`d    ���akeclass���`a ���bncx!InvertedMercatorLatitudeTransform���`a(���`kmtransforms���aoa.���`iTransform���`a)���`a:���`a
���`h        ���`jinput_dims���`a ���aoa=���`a ���`koutput_dims���`a ���aoa=���`a ���bmia1���`a
���`a
���`h        ���akcdef���`a ���bfmh__init__���`a(���bbpdself���`a,���`a ���`fthresh���`a)���`a:���`a
���`l            ���`kmtransforms���aoa.���`iTransform���aoa.���bfmh__init__���`a(���bbpdself���`a)���`a
���`l            ���bbpdself���aoa.���`fthresh���`a ���aoa=���`a ���`fthresh���`a
���`a
���`h        ���akcdef���`a ���bnfttransform_non_affine���`a(���bbpdself���`a,���`a ���`aa���`a)���`a:���`a
���`l            ���akfreturn���`a ���`bnp���aoa.���`farctan���`a(���`bnp���aoa.���`dsinh���`a(���`aa���`a)���`a)���`a
���`a
���`h        ���akcdef���`a ���bnfhinverted���`a(���bbpdself���`a)���`a:���`a
���`l            ���akfreturn���`a ���`uMercatorLatitudeScale���aoa.���`xMercatorLatitudeTransform���`a(���bbpdself���aoa.���`fthresh���`a)���`a
���`a
���`a
���bc1xE# Now that the Scale class has been defined, it must be registered so���`a
���bc1x# that Matplotlib can find it.���`a
���`fmscale���aoa.���`nregister_scale���`a(���`uMercatorLatitudeScale���`a)���`a
���`a
���`a
���akbif���`a ���bvmh__name__���`a ���aob==���`a ���bs1a'���bs1h__main__���bs1a'���`a:���`a
���`d    ���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���`a
���`d    ���`at���`a ���aoa=���`a ���`bnp���aoa.���`farange���`a(���aoa-���bmfe180.0���`a,���`a ���bmfe180.0���`a,���`a ���bmfc0.1���`a)���`a
���`d    ���`as���`a ���aoa=���`a ���`bnp���aoa.���`gradians���`a(���`at���`a)���aoa/���bmfb2.���`a
���`a
���`d    ���`cplt���aoa.���`dplot���`a(���`at���`a,���`a ���`as���`a,���`a ���bs1a'���bs1a-���bs1a'���`a,���`a ���`blw���aoa=���bmia2���`a)���`a
���`d    ���`cplt���aoa.���`fyscale���`a(���bs1a'���bs1hmercator���bs1a'���`a)���`a
���`a
���`d    ���`cplt���aoa.���`fxlabel���`a(���bs1a'���bs1iLongitude���bs1a'���`a)���`a
���`d    ���`cplt���aoa.���`fylabel���`a(���bs1a'���bs1hLatitude���bs1a'���`a)���`a
���`d    ���`cplt���aoa.���`etitle���`a(���bs1a'���bs1sMercator projection���bs1a'���`a)���`a
���`d    ���`cplt���aoa.���`dgrid���`a(���bkcdTrue���`a)���`a
���`a
���`d    ���`cplt���aoa.���`dshow���`a(���`a)���`a
`dNone�