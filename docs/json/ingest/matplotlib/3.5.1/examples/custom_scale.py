Ù¯‚Ù´ƒ™;Ù±‚bsdy±"""
============
Custom scale
============

Create a custom scale, by implementing the scaling use for latitude data in a
Mercator Projection.

Unless you are making special use of the `.Transform` class, you probably
don't need to use this verbose method, and instead can use `~.scale.FuncScale`
and the ``'function'`` option of `~.Axes.set_xscale` and `~.Axes.set_yscale`.
See the last example in :doc:`/gallery/scales/scales`.
"""Ù±‚`a
Ù±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„enumpyÙ „enumpyf1.22.3fmoduleenumpyfmoduleõÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnnbnpÙ±‚`a
Ù±‚bkndfromÙ±‚`a Ù±‚bnnÙ¢„enumpyÙ „enumpyf1.22.3fmoduleenumpyfmoduleõÙ±‚`a Ù±‚bknfimportÙ±‚`a Ù±‚`bmaÙ±‚`a
Ù±‚bkndfromÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚`a Ù±‚bknfimportÙ±‚`a Ù±‚`escaleÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚`fmscaleÙ±‚`a
Ù±‚bkndfromÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚`a Ù±‚bknfimportÙ±‚`a Ù±‚`jtransformsÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚`kmtransformsÙ±‚`a
Ù±‚bkndfromÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnnftickerÙ±‚`a Ù±‚bknfimportÙ±‚`a Ù±‚`lFixedLocatorÙ±‚`a,Ù±‚`a Ù±‚`mFuncFormatterÙ±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚akeclassÙ±‚`a Ù±‚bncuMercatorLatitudeScaleÙ±‚`a(Ù±‚`fmscaleÙ±‚aoa.Ù±‚`iScaleBaseÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`d    Ù±‚bsdyî"""
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
    """Ù±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚bc1xJ# The scale class must have a member ``name`` that defines the string usedÙ±‚`a
Ù±‚`d    Ù±‚bc1xK# to select the scale.  For example, ``ax.set_yscale("mercator")`` would beÙ±‚`a
Ù±‚`d    Ù±‚bc1x# used to select this scale.Ù±‚`a
Ù±‚`d    Ù±‚`dnameÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bs1a'Ù±‚bs1hmercatorÙ±‚bs1a'Ù±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚akcdefÙ±‚`a Ù±‚bfmh__init__Ù±‚`a(Ù±‚bbpdselfÙ±‚`a,Ù±‚`a Ù±‚`daxisÙ±‚`a,Ù±‚`a Ù±‚aoa*Ù±‚`a,Ù±‚`a Ù±‚`fthreshÙ±‚aoa=Ù±‚`bnpÙ±‚aoa.Ù±‚`gdeg2radÙ±‚`a(Ù±‚bmib85Ù±‚`a)Ù±‚`a,Ù±‚`a Ù±‚aoa*Ù±‚aoa*Ù±‚`fkwargsÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`h        Ù±‚bsdxÌ"""
        Any keyword arguments passed to ``set_xscale`` and ``set_yscale`` will
        be passed along to the scale's constructor.

        thresh: The degree above which to crop the data.
        """Ù±‚`a
Ù±‚`h        Ù±‚bnbesuperÙ±‚`a(Ù±‚`a)Ù±‚aoa.Ù±‚bfmh__init__Ù±‚`a(Ù±‚`daxisÙ±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚akbifÙ±‚`a Ù±‚`fthreshÙ±‚`a Ù±‚aoa>Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`bpiÙ±‚`a Ù±‚aoa/Ù±‚`a Ù±‚bmia2Ù±‚`a:Ù±‚`a
Ù±‚`l            Ù±‚akeraiseÙ±‚`a Ù±‚bnejValueErrorÙ±‚`a(Ù±‚bs2a"Ù±‚bs2xthresh must be less than pi/2Ù±‚bs2a"Ù±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`fthreshÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`fthreshÙ±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚akcdefÙ±‚`a Ù±‚bnfmget_transformÙ±‚`a(Ù±‚bbpdselfÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`h        Ù±‚bsdxã"""
        Override this method to return a new instance that does the
        actual transformation of the data.

        The MercatorLatitudeTransform class is defined below as a
        nested class of this one.
        """Ù±‚`a
Ù±‚`h        Ù±‚akfreturnÙ±‚`a Ù±‚bbpdselfÙ±‚aoa.Ù±‚`xMercatorLatitudeTransformÙ±‚`a(Ù±‚bbpdselfÙ±‚aoa.Ù±‚`fthreshÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚akcdefÙ±‚`a Ù±‚bnfx#set_default_locators_and_formattersÙ±‚`a(Ù±‚bbpdselfÙ±‚`a,Ù±‚`a Ù±‚`daxisÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`h        Ù±‚bsdy"""
        Override to set up the locators and formatters to use with the
        scale.  This is only required if the scale requires custom
        locators and formatters.  Writing custom locators and
        formatters is rather outside the scope of this example, but
        there are many helpful examples in :mod:`.ticker`.

        In our case, the Mercator example uses a fixed locator from -90 to 90
        degrees and a custom formatter to convert the radians to degrees and
        put a degree symbol after the value.
        """Ù±‚`a
Ù±‚`h        Ù±‚`cfmtÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`mFuncFormatterÙ±‚`a(Ù±‚`a
Ù±‚`l            Ù±‚akflambdaÙ±‚`a Ù±‚`axÙ±‚`a,Ù±‚`a Ù±‚`cposÙ±‚aoa=Ù±‚bkcdNoneÙ±‚`a:Ù±‚`a Ù±‚bsaafÙ±‚bs2a"Ù±‚bsia{Ù±‚`bnpÙ±‚aoa.Ù±‚`gdegreesÙ±‚`a(Ù±‚`axÙ±‚`a)Ù±‚bsia:Ù±‚bs2c.0fÙ±‚bsia}Ù±‚bseo\N{DEGREE SIGN}Ù±‚bs2a"Ù±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚`daxisÙ±‚aoa.Ù±‚`csetÙ±‚`a(Ù±‚`mmajor_locatorÙ±‚aoa=Ù±‚`lFixedLocatorÙ±‚`a(Ù±‚`bnpÙ±‚aoa.Ù±‚`gradiansÙ±‚`a(Ù±‚bnberangeÙ±‚`a(Ù±‚aoa-Ù±‚bmib90Ù±‚`a,Ù±‚`a Ù±‚bmib90Ù±‚`a,Ù±‚`a Ù±‚bmib10Ù±‚`a)Ù±‚`a)Ù±‚`a)Ù±‚`a,Ù±‚`a
Ù±‚`q                 Ù±‚`omajor_formatterÙ±‚aoa=Ù±‚`cfmtÙ±‚`a,Ù±‚`a Ù±‚`ominor_formatterÙ±‚aoa=Ù±‚`cfmtÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚akcdefÙ±‚`a Ù±‚bnfulimit_range_for_scaleÙ±‚`a(Ù±‚bbpdselfÙ±‚`a,Ù±‚`a Ù±‚`dvminÙ±‚`a,Ù±‚`a Ù±‚`dvmaxÙ±‚`a,Ù±‚`a Ù±‚`fminposÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`h        Ù±‚bsdy»"""
        Override to limit the bounds of the axis to the domain of the
        transform.  In the case of Mercator, the bounds should be
        limited to the threshold that was passed in.  Unlike the
        autoscaling provided by the tick locators, this range limiting
        will always be adhered to, whether the axis range is set
        manually, determined automatically or changed through panning
        and zooming.
        """Ù±‚`a
Ù±‚`h        Ù±‚akfreturnÙ±‚`a Ù±‚bnbcmaxÙ±‚`a(Ù±‚`dvminÙ±‚`a,Ù±‚`a Ù±‚aoa-Ù±‚bbpdselfÙ±‚aoa.Ù±‚`fthreshÙ±‚`a)Ù±‚`a,Ù±‚`a Ù±‚bnbcminÙ±‚`a(Ù±‚`dvmaxÙ±‚`a,Ù±‚`a Ù±‚bbpdselfÙ±‚aoa.Ù±‚`fthreshÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚akeclassÙ±‚`a Ù±‚bncxMercatorLatitudeTransformÙ±‚`a(Ù±‚`kmtransformsÙ±‚aoa.Ù±‚`iTransformÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`h        Ù±‚bc1x3# There are two value members that must be defined.Ù±‚`a
Ù±‚`h        Ù±‚bc1x<# ``input_dims`` and ``output_dims`` specify number of inputÙ±‚`a
Ù±‚`h        Ù±‚bc1x9# dimensions and output dimensions to the transformation.Ù±‚`a
Ù±‚`h        Ù±‚bc1x;# These are used by the transformation framework to do someÙ±‚`a
Ù±‚`h        Ù±‚bc1x># error checking and prevent incompatible transformations fromÙ±‚`a
Ù±‚`h        Ù±‚bc1x;# being connected together.  When defining transforms for aÙ±‚`a
Ù±‚`h        Ù±‚bc1x># scale, which are, by definition, separable and have only oneÙ±‚`a
Ù±‚`h        Ù±‚bc1x5# dimension, these members should always be set to 1.Ù±‚`a
Ù±‚`h        Ù±‚`jinput_dimsÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`koutput_dimsÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bmia1Ù±‚`a
Ù±‚`a
Ù±‚`h        Ù±‚akcdefÙ±‚`a Ù±‚bfmh__init__Ù±‚`a(Ù±‚bbpdselfÙ±‚`a,Ù±‚`a Ù±‚`fthreshÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`l            Ù±‚`kmtransformsÙ±‚aoa.Ù±‚`iTransformÙ±‚aoa.Ù±‚bfmh__init__Ù±‚`a(Ù±‚bbpdselfÙ±‚`a)Ù±‚`a
Ù±‚`l            Ù±‚bbpdselfÙ±‚aoa.Ù±‚`fthreshÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`fthreshÙ±‚`a
Ù±‚`a
Ù±‚`h        Ù±‚akcdefÙ±‚`a Ù±‚bnfttransform_non_affineÙ±‚`a(Ù±‚bbpdselfÙ±‚`a,Ù±‚`a Ù±‚`aaÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`l            Ù±‚bsdy:"""
            This transform takes a numpy array and returns a transformed copy.
            Since the range of the Mercator scale is limited by the
            user-specified threshold, the input array must be masked to
            contain only valid values.  Matplotlib will handle masked arrays
            and remove the out-of-range data from the plot.  However, the
            returned array *must* have the same shape as the input array, since
            these values need to remain synchronized with values in the other
            dimension.
            """Ù±‚`a
Ù±‚`l            Ù±‚`fmaskedÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bmaÙ±‚aoa.Ù±‚`lmasked_whereÙ±‚`a(Ù±‚`a(Ù±‚`aaÙ±‚`a Ù±‚aoa<Ù±‚`a Ù±‚aoa-Ù±‚bbpdselfÙ±‚aoa.Ù±‚`fthreshÙ±‚`a)Ù±‚`a Ù±‚aoa|Ù±‚`a Ù±‚`a(Ù±‚`aaÙ±‚`a Ù±‚aoa>Ù±‚`a Ù±‚bbpdselfÙ±‚aoa.Ù±‚`fthreshÙ±‚`a)Ù±‚`a,Ù±‚`a Ù±‚`aaÙ±‚`a)Ù±‚`a
Ù±‚`l            Ù±‚akbifÙ±‚`a Ù±‚`fmaskedÙ±‚aoa.Ù±‚`dmaskÙ±‚aoa.Ù±‚`canyÙ±‚`a(Ù±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`p                Ù±‚akfreturnÙ±‚`a Ù±‚`bmaÙ±‚aoa.Ù±‚`clogÙ±‚`a(Ù±‚`bnpÙ±‚aoa.Ù±‚`cabsÙ±‚`a(Ù±‚`bmaÙ±‚aoa.Ù±‚`ctanÙ±‚`a(Ù±‚`fmaskedÙ±‚`a)Ù±‚`a Ù±‚aoa+Ù±‚`a Ù±‚bmia1Ù±‚`a Ù±‚aoa/Ù±‚`a Ù±‚`bmaÙ±‚aoa.Ù±‚`ccosÙ±‚`a(Ù±‚`fmaskedÙ±‚`a)Ù±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`l            Ù±‚akdelseÙ±‚`a:Ù±‚`a
Ù±‚`p                Ù±‚akfreturnÙ±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`clogÙ±‚`a(Ù±‚`bnpÙ±‚aoa.Ù±‚`cabsÙ±‚`a(Ù±‚`bnpÙ±‚aoa.Ù±‚`ctanÙ±‚`a(Ù±‚`aaÙ±‚`a)Ù±‚`a Ù±‚aoa+Ù±‚`a Ù±‚bmia1Ù±‚`a Ù±‚aoa/Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`ccosÙ±‚`a(Ù±‚`aaÙ±‚`a)Ù±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`h        Ù±‚akcdefÙ±‚`a Ù±‚bnfhinvertedÙ±‚`a(Ù±‚bbpdselfÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`l            Ù±‚bsdx‰"""
            Override this method so Matplotlib knows how to get the
            inverse transform for this transform.
            """Ù±‚`a
Ù±‚`l            Ù±‚akfreturnÙ±‚`a Ù±‚`uMercatorLatitudeScaleÙ±‚aoa.Ù±‚`x!InvertedMercatorLatitudeTransformÙ±‚`a(Ù±‚`a
Ù±‚`p                Ù±‚bbpdselfÙ±‚aoa.Ù±‚`fthreshÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚akeclassÙ±‚`a Ù±‚bncx!InvertedMercatorLatitudeTransformÙ±‚`a(Ù±‚`kmtransformsÙ±‚aoa.Ù±‚`iTransformÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`h        Ù±‚`jinput_dimsÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`koutput_dimsÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bmia1Ù±‚`a
Ù±‚`a
Ù±‚`h        Ù±‚akcdefÙ±‚`a Ù±‚bfmh__init__Ù±‚`a(Ù±‚bbpdselfÙ±‚`a,Ù±‚`a Ù±‚`fthreshÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`l            Ù±‚`kmtransformsÙ±‚aoa.Ù±‚`iTransformÙ±‚aoa.Ù±‚bfmh__init__Ù±‚`a(Ù±‚bbpdselfÙ±‚`a)Ù±‚`a
Ù±‚`l            Ù±‚bbpdselfÙ±‚aoa.Ù±‚`fthreshÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`fthreshÙ±‚`a
Ù±‚`a
Ù±‚`h        Ù±‚akcdefÙ±‚`a Ù±‚bnfttransform_non_affineÙ±‚`a(Ù±‚bbpdselfÙ±‚`a,Ù±‚`a Ù±‚`aaÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`l            Ù±‚akfreturnÙ±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`farctanÙ±‚`a(Ù±‚`bnpÙ±‚aoa.Ù±‚`dsinhÙ±‚`a(Ù±‚`aaÙ±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`h        Ù±‚akcdefÙ±‚`a Ù±‚bnfhinvertedÙ±‚`a(Ù±‚bbpdselfÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`l            Ù±‚akfreturnÙ±‚`a Ù±‚`uMercatorLatitudeScaleÙ±‚aoa.Ù±‚`xMercatorLatitudeTransformÙ±‚`a(Ù±‚bbpdselfÙ±‚aoa.Ù±‚`fthreshÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚bc1xE# Now that the Scale class has been defined, it must be registered soÙ±‚`a
Ù±‚bc1x# that Matplotlib can find it.Ù±‚`a
Ù±‚`fmscaleÙ±‚aoa.Ù±‚`nregister_scaleÙ±‚`a(Ù±‚`uMercatorLatitudeScaleÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚akbifÙ±‚`a Ù±‚bvmh__name__Ù±‚`a Ù±‚aob==Ù±‚`a Ù±‚bs1a'Ù±‚bs1h__main__Ù±‚bs1a'Ù±‚`a:Ù±‚`a
Ù±‚`d    Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnnfpyplotÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnncpltÙ±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚`atÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`farangeÙ±‚`a(Ù±‚aoa-Ù±‚bmfe180.0Ù±‚`a,Ù±‚`a Ù±‚bmfe180.0Ù±‚`a,Ù±‚`a Ù±‚bmfc0.1Ù±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`asÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`gradiansÙ±‚`a(Ù±‚`atÙ±‚`a)Ù±‚aoa/Ù±‚bmfb2.Ù±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚`cpltÙ±‚aoa.Ù±‚`dplotÙ±‚`a(Ù±‚`atÙ±‚`a,Ù±‚`a Ù±‚`asÙ±‚`a,Ù±‚`a Ù±‚bs1a'Ù±‚bs1a-Ù±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`blwÙ±‚aoa=Ù±‚bmia2Ù±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`cpltÙ±‚aoa.Ù±‚`fyscaleÙ±‚`a(Ù±‚bs1a'Ù±‚bs1hmercatorÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚`cpltÙ±‚aoa.Ù±‚`fxlabelÙ±‚`a(Ù±‚bs1a'Ù±‚bs1iLongitudeÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`cpltÙ±‚aoa.Ù±‚`fylabelÙ±‚`a(Ù±‚bs1a'Ù±‚bs1hLatitudeÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`cpltÙ±‚aoa.Ù±‚`etitleÙ±‚`a(Ù±‚bs1a'Ù±‚bs1sMercator projectionÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`cpltÙ±‚aoa.Ù±‚`dgridÙ±‚`a(Ù±‚bkcdTrueÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚`cpltÙ±‚aoa.Ù±‚`dshowÙ±‚`a(Ù±‚`a)Ù±‚`a
`dNoneö