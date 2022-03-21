Ù¯‚Ù´ƒ™‰Ù±‚bsdys"""
======================================
Thresholding an Image with RangeSlider
======================================

Using the RangeSlider widget to control the thresholding of an image.

The RangeSlider widget can be used similarly to the `.widgets.Slider`
widget. The major difference is that RangeSlider's ``val`` attribute
is a tuple of floats ``(lower val, upper val)`` rather than a single float.

See :doc:`/gallery/widgets/slider_demo` for an example of using
a ``Slider`` to control a single float.

See :doc:`/gallery/widgets/slider_snap_demo` for an example of having
the ``Slider`` snap to discrete values.
"""Ù±‚`a
Ù±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„enumpyÙ „enumpyf1.22.3fmoduleenumpyfmoduleõÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnnbnpÙ±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnnfpyplotÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnncpltÙ±‚`a
Ù±‚bkndfromÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnngwidgetsÙ±‚`a Ù±‚bknfimportÙ±‚`a Ù±‚`kRangeSliderÙ±‚`a
Ù±‚`a
Ù±‚bc1w# generate a fake imageÙ±‚`a
Ù±‚`bnpÙ±‚aoa.Ù±‚`frandomÙ±‚aoa.Ù±‚`dseedÙ±‚`a(Ù±‚bmih19680801Ù±‚`a)Ù±‚`a
Ù±‚`aNÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bmic128Ù±‚`a
Ù±‚`cimgÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`frandomÙ±‚aoa.Ù±‚`erandnÙ±‚`a(Ù±‚`aNÙ±‚`a,Ù±‚`a Ù±‚`aNÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`cfigÙ±‚`a,Ù±‚`a Ù±‚`caxsÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cpltÙ±‚aoa.Ù±‚`hsubplotsÙ±‚`a(Ù±‚bmia1Ù±‚`a,Ù±‚`a Ù±‚bmia2Ù±‚`a,Ù±‚`a Ù±‚`gfigsizeÙ±‚aoa=Ù±‚`a(Ù±‚bmib10Ù±‚`a,Ù±‚`a Ù±‚bmia5Ù±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`cpltÙ±‚aoa.Ù±‚`osubplots_adjustÙ±‚`a(Ù±‚`fbottomÙ±‚aoa=Ù±‚bmfd0.25Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`bimÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`caxsÙ±‚`a[Ù±‚bmia0Ù±‚`a]Ù±‚aoa.Ù±‚`fimshowÙ±‚`a(Ù±‚`cimgÙ±‚`a)Ù±‚`a
Ù±‚`caxsÙ±‚`a[Ù±‚bmia1Ù±‚`a]Ù±‚aoa.Ù±‚`dhistÙ±‚`a(Ù±‚`cimgÙ±‚aoa.Ù±‚`gflattenÙ±‚`a(Ù±‚`a)Ù±‚`a,Ù±‚`a Ù±‚`dbinsÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1dautoÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`caxsÙ±‚`a[Ù±‚bmia1Ù±‚`a]Ù±‚aoa.Ù±‚`iset_titleÙ±‚`a(Ù±‚bs1a'Ù±‚bs1xHistogram of pixel intensitiesÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚bc1x# Create the RangeSliderÙ±‚`a
Ù±‚`islider_axÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cpltÙ±‚aoa.Ù±‚`daxesÙ±‚`a(Ù±‚`a[Ù±‚bmfd0.20Ù±‚`a,Ù±‚`a Ù±‚bmfc0.1Ù±‚`a,Ù±‚`a Ù±‚bmfd0.60Ù±‚`a,Ù±‚`a Ù±‚bmfd0.03Ù±‚`a]Ù±‚`a)Ù±‚`a
Ù±‚`fsliderÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`kRangeSliderÙ±‚`a(Ù±‚`islider_axÙ±‚`a,Ù±‚`a Ù±‚bs2a"Ù±‚bs2iThresholdÙ±‚bs2a"Ù±‚`a,Ù±‚`a Ù±‚`cimgÙ±‚aoa.Ù±‚`cminÙ±‚`a(Ù±‚`a)Ù±‚`a,Ù±‚`a Ù±‚`cimgÙ±‚aoa.Ù±‚`cmaxÙ±‚`a(Ù±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚bc1x,# Create the Vertical lines on the histogramÙ±‚`a
Ù±‚`plower_limit_lineÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`caxsÙ±‚`a[Ù±‚bmia1Ù±‚`a]Ù±‚aoa.Ù±‚`gaxvlineÙ±‚`a(Ù±‚`fsliderÙ±‚aoa.Ù±‚`cvalÙ±‚`a[Ù±‚bmia0Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`ecolorÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1akÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`pupper_limit_lineÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`caxsÙ±‚`a[Ù±‚bmia1Ù±‚`a]Ù±‚aoa.Ù±‚`gaxvlineÙ±‚`a(Ù±‚`fsliderÙ±‚aoa.Ù±‚`cvalÙ±‚`a[Ù±‚bmia1Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`ecolorÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1akÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚akcdefÙ±‚`a Ù±‚bnffupdateÙ±‚`a(Ù±‚`cvalÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`d    Ù±‚bc1x6# The val passed to a callback by the RangeSlider willÙ±‚`a
Ù±‚`d    Ù±‚bc1x# be a tuple of (min, max)Ù±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚bc1x# Update the image's colormapÙ±‚`a
Ù±‚`d    Ù±‚`bimÙ±‚aoa.Ù±‚`dnormÙ±‚aoa.Ù±‚`dvminÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cvalÙ±‚`a[Ù±‚bmia0Ù±‚`a]Ù±‚`a
Ù±‚`d    Ù±‚`bimÙ±‚aoa.Ù±‚`dnormÙ±‚aoa.Ù±‚`dvmaxÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cvalÙ±‚`a[Ù±‚bmia1Ù±‚`a]Ù±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚bc1x+# Update the position of the vertical linesÙ±‚`a
Ù±‚`d    Ù±‚`plower_limit_lineÙ±‚aoa.Ù±‚`iset_xdataÙ±‚`a(Ù±‚`a[Ù±‚`cvalÙ±‚`a[Ù±‚bmia0Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`cvalÙ±‚`a[Ù±‚bmia0Ù±‚`a]Ù±‚`a]Ù±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`pupper_limit_lineÙ±‚aoa.Ù±‚`iset_xdataÙ±‚`a(Ù±‚`a[Ù±‚`cvalÙ±‚`a[Ù±‚bmia1Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`cvalÙ±‚`a[Ù±‚bmia1Ù±‚`a]Ù±‚`a]Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚bc1x(# Redraw the figure to ensure it updatesÙ±‚`a
Ù±‚`d    Ù±‚`cfigÙ±‚aoa.Ù±‚`fcanvasÙ±‚aoa.Ù±‚`idraw_idleÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚`fsliderÙ±‚aoa.Ù±‚`jon_changedÙ±‚`a(Ù±‚`fupdateÙ±‚`a)Ù±‚`a
Ù±‚`cpltÙ±‚aoa.Ù±‚`dshowÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚bc1xM#############################################################################Ù±‚`a
Ù±‚bc1a#Ù±‚`a
Ù±‚bc1x# .. admonition:: ReferencesÙ±‚`a
Ù±‚bc1a#Ù±‚`a
Ù±‚bc1xN#    The use of the following functions, methods, classes and modules is shownÙ±‚`a
Ù±‚bc1u#    in this example:Ù±‚`a
Ù±‚bc1a#Ù±‚`a
Ù±‚bc1x'#    - `matplotlib.widgets.RangeSlider`Ù±‚`a
`dNoneö