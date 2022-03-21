Ù¯‚Ù´ƒ™óÙ±‚bsdyT"""
===================================
Snapping Sliders to Discrete Values
===================================

You can snap slider values to discrete values using the ``valstep`` argument.

In this example the Freq slider is constrained to be multiples of pi, and the
Amp slider uses an array as the ``valstep`` argument to more densely sample
the first part of its range.

See :doc:`/gallery/widgets/slider_demo` for an example of using
a ``Slider`` to control a single float.

See :doc:`/gallery/widgets/range_slider` for an example of using
a ``RangeSlider`` to define a range of values.
"""Ù±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„enumpyÙ „enumpyf1.22.3fmoduleenumpyfmoduleõÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnnbnpÙ±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnnfpyplotÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnncpltÙ±‚`a
Ù±‚bkndfromÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnngwidgetsÙ±‚`a Ù±‚bknfimportÙ±‚`a Ù±‚`fSliderÙ±‚`a,Ù±‚`a Ù±‚`fButtonÙ±‚`a
Ù±‚`a
Ù±‚`atÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`farangeÙ±‚`a(Ù±‚bmfc0.0Ù±‚`a,Ù±‚`a Ù±‚bmfc1.0Ù±‚`a,Ù±‚`a Ù±‚bmfe0.001Ù±‚`a)Ù±‚`a
Ù±‚`ba0Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bmia5Ù±‚`a
Ù±‚`bf0Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bmia3Ù±‚`a
Ù±‚`asÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`ba0Ù±‚`a Ù±‚aoa*Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`csinÙ±‚`a(Ù±‚bmia2Ù±‚`a Ù±‚aoa*Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`bpiÙ±‚`a Ù±‚aoa*Ù±‚`a Ù±‚`bf0Ù±‚`a Ù±‚aoa*Ù±‚`a Ù±‚`atÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`cfigÙ±‚`a,Ù±‚`a Ù±‚`baxÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cpltÙ±‚aoa.Ù±‚`hsubplotsÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`cpltÙ±‚aoa.Ù±‚`osubplots_adjustÙ±‚`a(Ù±‚`fbottomÙ±‚aoa=Ù±‚bmfd0.25Ù±‚`a)Ù±‚`a
Ù±‚`alÙ±‚`a,Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cpltÙ±‚aoa.Ù±‚`dplotÙ±‚`a(Ù±‚`atÙ±‚`a,Ù±‚`a Ù±‚`asÙ±‚`a,Ù±‚`a Ù±‚`blwÙ±‚aoa=Ù±‚bmia2Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`gax_freqÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cpltÙ±‚aoa.Ù±‚`daxesÙ±‚`a(Ù±‚`a[Ù±‚bmfd0.25Ù±‚`a,Ù±‚`a Ù±‚bmfc0.1Ù±‚`a,Ù±‚`a Ù±‚bmfd0.65Ù±‚`a,Ù±‚`a Ù±‚bmfd0.03Ù±‚`a]Ù±‚`a)Ù±‚`a
Ù±‚`fax_ampÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cpltÙ±‚aoa.Ù±‚`daxesÙ±‚`a(Ù±‚`a[Ù±‚bmfd0.25Ù±‚`a,Ù±‚`a Ù±‚bmfd0.15Ù±‚`a,Ù±‚`a Ù±‚bmfd0.65Ù±‚`a,Ù±‚`a Ù±‚bmfd0.03Ù±‚`a]Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚bc1x'# define the values to use for snappingÙ±‚`a
Ù±‚`rallowed_amplitudesÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`kconcatenateÙ±‚`a(Ù±‚`a[Ù±‚`bnpÙ±‚aoa.Ù±‚`hlinspaceÙ±‚`a(Ù±‚bmfb.1Ù±‚`a,Ù±‚`a Ù±‚bmia5Ù±‚`a,Ù±‚`a Ù±‚bmic100Ù±‚`a)Ù±‚`a,Ù±‚`a Ù±‚`a[Ù±‚bmia6Ù±‚`a,Ù±‚`a Ù±‚bmia7Ù±‚`a,Ù±‚`a Ù±‚bmia8Ù±‚`a,Ù±‚`a Ù±‚bmia9Ù±‚`a]Ù±‚`a]Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚bc1t# create the slidersÙ±‚`a
Ù±‚`dsampÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`fSliderÙ±‚`a(Ù±‚`a
Ù±‚`d    Ù±‚`fax_ampÙ±‚`a,Ù±‚`a Ù±‚bs2a"Ù±‚bs2cAmpÙ±‚bs2a"Ù±‚`a,Ù±‚`a Ù±‚bmfc0.1Ù±‚`a,Ù±‚`a Ù±‚bmfc9.0Ù±‚`a,Ù±‚`a
Ù±‚`d    Ù±‚`gvalinitÙ±‚aoa=Ù±‚`ba0Ù±‚`a,Ù±‚`a Ù±‚`gvalstepÙ±‚aoa=Ù±‚`rallowed_amplitudesÙ±‚`a,Ù±‚`a
Ù±‚`d    Ù±‚`ecolorÙ±‚aoa=Ù±‚bs2a"Ù±‚bs2egreenÙ±‚bs2a"Ù±‚`a
Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`esfreqÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`fSliderÙ±‚`a(Ù±‚`a
Ù±‚`d    Ù±‚`gax_freqÙ±‚`a,Ù±‚`a Ù±‚bs2a"Ù±‚bs2dFreqÙ±‚bs2a"Ù±‚`a,Ù±‚`a Ù±‚bmia0Ù±‚`a,Ù±‚`a Ù±‚bmib10Ù±‚aoa*Ù±‚`bnpÙ±‚aoa.Ù±‚`bpiÙ±‚`a,Ù±‚`a
Ù±‚`d    Ù±‚`gvalinitÙ±‚aoa=Ù±‚bmia2Ù±‚aoa*Ù±‚`bnpÙ±‚aoa.Ù±‚`bpiÙ±‚`a,Ù±‚`a Ù±‚`gvalstepÙ±‚aoa=Ù±‚`bnpÙ±‚aoa.Ù±‚`bpiÙ±‚`a,Ù±‚`a
Ù±‚`d    Ù±‚`iinitcolorÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1dnoneÙ±‚bs1a'Ù±‚`b  Ù±‚bc1x/# Remove the line marking the valinit position.Ù±‚`a
Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚akcdefÙ±‚`a Ù±‚bnffupdateÙ±‚`a(Ù±‚`cvalÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`d    Ù±‚`campÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`dsampÙ±‚aoa.Ù±‚`cvalÙ±‚`a
Ù±‚`d    Ù±‚`dfreqÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`esfreqÙ±‚aoa.Ù±‚`cvalÙ±‚`a
Ù±‚`d    Ù±‚`alÙ±‚aoa.Ù±‚`iset_ydataÙ±‚`a(Ù±‚`campÙ±‚aoa*Ù±‚`bnpÙ±‚aoa.Ù±‚`csinÙ±‚`a(Ù±‚bmia2Ù±‚aoa*Ù±‚`bnpÙ±‚aoa.Ù±‚`bpiÙ±‚aoa*Ù±‚`dfreqÙ±‚aoa*Ù±‚`atÙ±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`cfigÙ±‚aoa.Ù±‚`fcanvasÙ±‚aoa.Ù±‚`idraw_idleÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚`esfreqÙ±‚aoa.Ù±‚`jon_changedÙ±‚`a(Ù±‚`fupdateÙ±‚`a)Ù±‚`a
Ù±‚`dsampÙ±‚aoa.Ù±‚`jon_changedÙ±‚`a(Ù±‚`fupdateÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`hax_resetÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cpltÙ±‚aoa.Ù±‚`daxesÙ±‚`a(Ù±‚`a[Ù±‚bmfc0.8Ù±‚`a,Ù±‚`a Ù±‚bmfe0.025Ù±‚`a,Ù±‚`a Ù±‚bmfc0.1Ù±‚`a,Ù±‚`a Ù±‚bmfd0.04Ù±‚`a]Ù±‚`a)Ù±‚`a
Ù±‚`fbuttonÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`fButtonÙ±‚`a(Ù±‚`hax_resetÙ±‚`a,Ù±‚`a Ù±‚bs1a'Ù±‚bs1eResetÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`jhovercolorÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1e0.975Ù±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚akcdefÙ±‚`a Ù±‚bnferesetÙ±‚`a(Ù±‚`eeventÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`d    Ù±‚`esfreqÙ±‚aoa.Ù±‚`eresetÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`dsampÙ±‚aoa.Ù±‚`eresetÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`fbuttonÙ±‚aoa.Ù±‚`jon_clickedÙ±‚`a(Ù±‚`eresetÙ±‚`a)Ù±‚`a
Ù±‚`a
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
Ù±‚bc1x"#    - `matplotlib.widgets.Slider`Ù±‚`a
Ù±‚bc1x"#    - `matplotlib.widgets.Button`Ù±‚`a
`dNoneö