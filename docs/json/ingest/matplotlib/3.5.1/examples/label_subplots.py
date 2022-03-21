Ù¯‚Ù´ƒ™Ù±‚bsdyì"""
==================
Labelling subplots
==================

Labelling subplots is relatively straightforward, and varies,
so Matplotlib does not have a general method for doing this.

Simplest is putting the label inside the axes.  Note, here
we use `.pyplot.subplot_mosaic`, and use the subplot labels
as keys for the subplots, which is a nice convenience.  However,
the same method works with `.pyplot.subplots` or keys that are
different than what you want to label the subplot with.
"""Ù±‚`a
Ù±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnnfpyplotÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnncpltÙ±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnnjtransformsÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnnkmtransformsÙ±‚`a
Ù±‚`a
Ù±‚`cfigÙ±‚`a,Ù±‚`a Ù±‚`caxsÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cpltÙ±‚aoa.Ù±‚`nsubplot_mosaicÙ±‚`a(Ù±‚`a[Ù±‚`a[Ù±‚bs1a'Ù±‚bs1ba)Ù±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚bs1a'Ù±‚bs1bc)Ù±‚bs1a'Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`a[Ù±‚bs1a'Ù±‚bs1bb)Ù±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚bs1a'Ù±‚bs1bc)Ù±‚bs1a'Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`a[Ù±‚bs1a'Ù±‚bs1bd)Ù±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚bs1a'Ù±‚bs1bd)Ù±‚bs1a'Ù±‚`a]Ù±‚`a]Ù±‚`a,Ù±‚`a
Ù±‚`x                              Ù±‚`rconstrained_layoutÙ±‚aoa=Ù±‚bkcdTrueÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚akcforÙ±‚`a Ù±‚`elabelÙ±‚`a,Ù±‚`a Ù±‚`baxÙ±‚`a Ù±‚bowbinÙ±‚`a Ù±‚`caxsÙ±‚aoa.Ù±‚`eitemsÙ±‚`a(Ù±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`d    Ù±‚bc1x&# label physical distance in and down:Ù±‚`a
Ù±‚`d    Ù±‚`etransÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`kmtransformsÙ±‚aoa.Ù±‚`qScaledTranslationÙ±‚`a(Ù±‚bmib10Ù±‚aoa/Ù±‚bmib72Ù±‚`a,Ù±‚`a Ù±‚aoa-Ù±‚bmia5Ù±‚aoa/Ù±‚bmib72Ù±‚`a,Ù±‚`a Ù±‚`cfigÙ±‚aoa.Ù±‚`odpi_scale_transÙ±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`baxÙ±‚aoa.Ù±‚`dtextÙ±‚`a(Ù±‚bmfc0.0Ù±‚`a,Ù±‚`a Ù±‚bmfc1.0Ù±‚`a,Ù±‚`a Ù±‚`elabelÙ±‚`a,Ù±‚`a Ù±‚`itransformÙ±‚aoa=Ù±‚`baxÙ±‚aoa.Ù±‚`itransAxesÙ±‚`a Ù±‚aoa+Ù±‚`a Ù±‚`etransÙ±‚`a,Ù±‚`a
Ù±‚`l            Ù±‚`hfontsizeÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1fmediumÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`qverticalalignmentÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1ctopÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`jfontfamilyÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1eserifÙ±‚bs1a'Ù±‚`a,Ù±‚`a
Ù±‚`l            Ù±‚`dbboxÙ±‚aoa=Ù±‚bnbddictÙ±‚`a(Ù±‚`ifacecolorÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1c0.7Ù±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`iedgecolorÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1dnoneÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`cpadÙ±‚aoa=Ù±‚bmfc3.0Ù±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`cpltÙ±‚aoa.Ù±‚`dshowÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚bc1xN##############################################################################Ù±‚`a
Ù±‚bc1x># We may prefer the labels outside the axes, but still alignedÙ±‚`a
Ù±‚bc1xG# with each other, in which case we use a slightly different transform:Ù±‚`a
Ù±‚`a
Ù±‚`cfigÙ±‚`a,Ù±‚`a Ù±‚`caxsÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cpltÙ±‚aoa.Ù±‚`nsubplot_mosaicÙ±‚`a(Ù±‚`a[Ù±‚`a[Ù±‚bs1a'Ù±‚bs1ba)Ù±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚bs1a'Ù±‚bs1bc)Ù±‚bs1a'Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`a[Ù±‚bs1a'Ù±‚bs1bb)Ù±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚bs1a'Ù±‚bs1bc)Ù±‚bs1a'Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`a[Ù±‚bs1a'Ù±‚bs1bd)Ù±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚bs1a'Ù±‚bs1bd)Ù±‚bs1a'Ù±‚`a]Ù±‚`a]Ù±‚`a,Ù±‚`a
Ù±‚`x                              Ù±‚`rconstrained_layoutÙ±‚aoa=Ù±‚bkcdTrueÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚akcforÙ±‚`a Ù±‚`elabelÙ±‚`a,Ù±‚`a Ù±‚`baxÙ±‚`a Ù±‚bowbinÙ±‚`a Ù±‚`caxsÙ±‚aoa.Ù±‚`eitemsÙ±‚`a(Ù±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`d    Ù±‚bc1x-# label physical distance to the left and up:Ù±‚`a
Ù±‚`d    Ù±‚`etransÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`kmtransformsÙ±‚aoa.Ù±‚`qScaledTranslationÙ±‚`a(Ù±‚aoa-Ù±‚bmib20Ù±‚aoa/Ù±‚bmib72Ù±‚`a,Ù±‚`a Ù±‚bmia7Ù±‚aoa/Ù±‚bmib72Ù±‚`a,Ù±‚`a Ù±‚`cfigÙ±‚aoa.Ù±‚`odpi_scale_transÙ±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`baxÙ±‚aoa.Ù±‚`dtextÙ±‚`a(Ù±‚bmfc0.0Ù±‚`a,Ù±‚`a Ù±‚bmfc1.0Ù±‚`a,Ù±‚`a Ù±‚`elabelÙ±‚`a,Ù±‚`a Ù±‚`itransformÙ±‚aoa=Ù±‚`baxÙ±‚aoa.Ù±‚`itransAxesÙ±‚`a Ù±‚aoa+Ù±‚`a Ù±‚`etransÙ±‚`a,Ù±‚`a
Ù±‚`l            Ù±‚`hfontsizeÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1fmediumÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`bvaÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1fbottomÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`jfontfamilyÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1eserifÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`cpltÙ±‚aoa.Ù±‚`dshowÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚bc1xN##############################################################################Ù±‚`a
Ù±‚bc1xJ# If we want it aligned with the title, either incorporate in the title orÙ±‚`a
Ù±‚bc1x!# use the *loc* keyword argument:Ù±‚`a
Ù±‚`a
Ù±‚`cfigÙ±‚`a,Ù±‚`a Ù±‚`caxsÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cpltÙ±‚aoa.Ù±‚`nsubplot_mosaicÙ±‚`a(Ù±‚`a[Ù±‚`a[Ù±‚bs1a'Ù±‚bs1ba)Ù±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚bs1a'Ù±‚bs1bc)Ù±‚bs1a'Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`a[Ù±‚bs1a'Ù±‚bs1bb)Ù±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚bs1a'Ù±‚bs1bc)Ù±‚bs1a'Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`a[Ù±‚bs1a'Ù±‚bs1bd)Ù±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚bs1a'Ù±‚bs1bd)Ù±‚bs1a'Ù±‚`a]Ù±‚`a]Ù±‚`a,Ù±‚`a
Ù±‚`x                              Ù±‚`rconstrained_layoutÙ±‚aoa=Ù±‚bkcdTrueÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚akcforÙ±‚`a Ù±‚`elabelÙ±‚`a,Ù±‚`a Ù±‚`baxÙ±‚`a Ù±‚bowbinÙ±‚`a Ù±‚`caxsÙ±‚aoa.Ù±‚`eitemsÙ±‚`a(Ù±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`d    Ù±‚`baxÙ±‚aoa.Ù±‚`iset_titleÙ±‚`a(Ù±‚bs1a'Ù±‚bs1lNormal TitleÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`ifontstyleÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1fitalicÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`baxÙ±‚aoa.Ù±‚`iset_titleÙ±‚`a(Ù±‚`elabelÙ±‚`a,Ù±‚`a Ù±‚`jfontfamilyÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1eserifÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`clocÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1dleftÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`hfontsizeÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1fmediumÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`cpltÙ±‚aoa.Ù±‚`dshowÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚bc1xM#############################################################################Ù±‚`a
Ù±‚bc1a#Ù±‚`a
Ù±‚bc1x# .. admonition:: ReferencesÙ±‚`a
Ù±‚bc1a#Ù±‚`a
Ù±‚bc1xN#    The use of the following functions, methods, classes and modules is shownÙ±‚`a
Ù±‚bc1u#    in this example:Ù±‚`a
Ù±‚bc1a#Ù±‚`a
Ù±‚bc1x2#    - `matplotlib.figure.Figure.subplot_mosaic` /Ù±‚`a
Ù±‚bc1x)#      `matplotlib.pyplot.subplot_mosaic`Ù±‚`a
Ù±‚bc1x'#    - `matplotlib.axes.Axes.set_title`Ù±‚`a
Ù±‚bc1x"#    - `matplotlib.axes.Axes.text`Ù±‚`a
Ù±‚bc1x0#    - `matplotlib.transforms.ScaledTranslation`Ù±‚`a
`dNoneö