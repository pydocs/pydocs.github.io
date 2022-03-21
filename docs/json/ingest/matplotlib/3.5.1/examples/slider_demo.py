Ù¯‚Ù´ƒ™åÙ±‚bsdyV"""
======
Slider
======

In this example, sliders are used to control the frequency and amplitude of
a sine wave.

See :doc:`/gallery/widgets/slider_snap_demo` for an example of having
the ``Slider`` snap to discrete values.

See :doc:`/gallery/widgets/range_slider` for an example of using
a ``RangeSlider`` to define a range of values.
"""Ù±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„enumpyÙ „enumpyf1.22.3fmoduleenumpyfmoduleõÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnnbnpÙ±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnnfpyplotÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnncpltÙ±‚`a
Ù±‚bkndfromÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnngwidgetsÙ±‚`a Ù±‚bknfimportÙ±‚`a Ù±‚`fSliderÙ±‚`a,Ù±‚`a Ù±‚`fButtonÙ±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚bc1x)# The parametrized function to be plottedÙ±‚`a
Ù±‚akcdefÙ±‚`a Ù±‚bnfafÙ±‚`a(Ù±‚`atÙ±‚`a,Ù±‚`a Ù±‚`iamplitudeÙ±‚`a,Ù±‚`a Ù±‚`ifrequencyÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`d    Ù±‚akfreturnÙ±‚`a Ù±‚`iamplitudeÙ±‚`a Ù±‚aoa*Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`csinÙ±‚`a(Ù±‚bmia2Ù±‚`a Ù±‚aoa*Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`bpiÙ±‚`a Ù±‚aoa*Ù±‚`a Ù±‚`ifrequencyÙ±‚`a Ù±‚aoa*Ù±‚`a Ù±‚`atÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`atÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`hlinspaceÙ±‚`a(Ù±‚bmia0Ù±‚`a,Ù±‚`a Ù±‚bmia1Ù±‚`a,Ù±‚`a Ù±‚bmid1000Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚bc1x# Define initial parametersÙ±‚`a
Ù±‚`ninit_amplitudeÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bmia5Ù±‚`a
Ù±‚`ninit_frequencyÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bmia3Ù±‚`a
Ù±‚`a
Ù±‚bc1x8# Create the figure and the line that we will manipulateÙ±‚`a
Ù±‚`cfigÙ±‚`a,Ù±‚`a Ù±‚`baxÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cpltÙ±‚aoa.Ù±‚`hsubplotsÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`dlineÙ±‚`a,Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cpltÙ±‚aoa.Ù±‚`dplotÙ±‚`a(Ù±‚`atÙ±‚`a,Ù±‚`a Ù±‚`afÙ±‚`a(Ù±‚`atÙ±‚`a,Ù±‚`a Ù±‚`ninit_amplitudeÙ±‚`a,Ù±‚`a Ù±‚`ninit_frequencyÙ±‚`a)Ù±‚`a,Ù±‚`a Ù±‚`blwÙ±‚aoa=Ù±‚bmia2Ù±‚`a)Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`jset_xlabelÙ±‚`a(Ù±‚bs1a'Ù±‚bs1hTime [s]Ù±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚bc1x3# adjust the main plot to make room for the slidersÙ±‚`a
Ù±‚`cpltÙ±‚aoa.Ù±‚`osubplots_adjustÙ±‚`a(Ù±‚`dleftÙ±‚aoa=Ù±‚bmfd0.25Ù±‚`a,Ù±‚`a Ù±‚`fbottomÙ±‚aoa=Ù±‚bmfd0.25Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚bc1x4# Make a horizontal slider to control the frequency.Ù±‚`a
Ù±‚`faxfreqÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cpltÙ±‚aoa.Ù±‚`daxesÙ±‚`a(Ù±‚`a[Ù±‚bmfd0.25Ù±‚`a,Ù±‚`a Ù±‚bmfc0.1Ù±‚`a,Ù±‚`a Ù±‚bmfd0.65Ù±‚`a,Ù±‚`a Ù±‚bmfd0.03Ù±‚`a]Ù±‚`a)Ù±‚`a
Ù±‚`kfreq_sliderÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`fSliderÙ±‚`a(Ù±‚`a
Ù±‚`d    Ù±‚`baxÙ±‚aoa=Ù±‚`faxfreqÙ±‚`a,Ù±‚`a
Ù±‚`d    Ù±‚`elabelÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1nFrequency [Hz]Ù±‚bs1a'Ù±‚`a,Ù±‚`a
Ù±‚`d    Ù±‚`fvalminÙ±‚aoa=Ù±‚bmfc0.1Ù±‚`a,Ù±‚`a
Ù±‚`d    Ù±‚`fvalmaxÙ±‚aoa=Ù±‚bmib30Ù±‚`a,Ù±‚`a
Ù±‚`d    Ù±‚`gvalinitÙ±‚aoa=Ù±‚`ninit_frequencyÙ±‚`a,Ù±‚`a
Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚bc1x<# Make a vertically oriented slider to control the amplitudeÙ±‚`a
Ù±‚`eaxampÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cpltÙ±‚aoa.Ù±‚`daxesÙ±‚`a(Ù±‚`a[Ù±‚bmfc0.1Ù±‚`a,Ù±‚`a Ù±‚bmfd0.25Ù±‚`a,Ù±‚`a Ù±‚bmff0.0225Ù±‚`a,Ù±‚`a Ù±‚bmfd0.63Ù±‚`a]Ù±‚`a)Ù±‚`a
Ù±‚`jamp_sliderÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`fSliderÙ±‚`a(Ù±‚`a
Ù±‚`d    Ù±‚`baxÙ±‚aoa=Ù±‚`eaxampÙ±‚`a,Ù±‚`a
Ù±‚`d    Ù±‚`elabelÙ±‚aoa=Ù±‚bs2a"Ù±‚bs2iAmplitudeÙ±‚bs2a"Ù±‚`a,Ù±‚`a
Ù±‚`d    Ù±‚`fvalminÙ±‚aoa=Ù±‚bmia0Ù±‚`a,Ù±‚`a
Ù±‚`d    Ù±‚`fvalmaxÙ±‚aoa=Ù±‚bmib10Ù±‚`a,Ù±‚`a
Ù±‚`d    Ù±‚`gvalinitÙ±‚aoa=Ù±‚`ninit_amplitudeÙ±‚`a,Ù±‚`a
Ù±‚`d    Ù±‚`korientationÙ±‚aoa=Ù±‚bs2a"Ù±‚bs2hverticalÙ±‚bs2a"Ù±‚`a
Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚bc1x<# The function to be called anytime a slider's value changesÙ±‚`a
Ù±‚akcdefÙ±‚`a Ù±‚bnffupdateÙ±‚`a(Ù±‚`cvalÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`d    Ù±‚`dlineÙ±‚aoa.Ù±‚`iset_ydataÙ±‚`a(Ù±‚`afÙ±‚`a(Ù±‚`atÙ±‚`a,Ù±‚`a Ù±‚`jamp_sliderÙ±‚aoa.Ù±‚`cvalÙ±‚`a,Ù±‚`a Ù±‚`kfreq_sliderÙ±‚aoa.Ù±‚`cvalÙ±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`cfigÙ±‚aoa.Ù±‚`fcanvasÙ±‚aoa.Ù±‚`idraw_idleÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚bc1x/# register the update function with each sliderÙ±‚`a
Ù±‚`kfreq_sliderÙ±‚aoa.Ù±‚`jon_changedÙ±‚`a(Ù±‚`fupdateÙ±‚`a)Ù±‚`a
Ù±‚`jamp_sliderÙ±‚aoa.Ù±‚`jon_changedÙ±‚`a(Ù±‚`fupdateÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚bc1xN# Create a `matplotlib.widgets.Button` to reset the sliders to initial values.Ù±‚`a
Ù±‚`gresetaxÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cpltÙ±‚aoa.Ù±‚`daxesÙ±‚`a(Ù±‚`a[Ù±‚bmfc0.8Ù±‚`a,Ù±‚`a Ù±‚bmfe0.025Ù±‚`a,Ù±‚`a Ù±‚bmfc0.1Ù±‚`a,Ù±‚`a Ù±‚bmfd0.04Ù±‚`a]Ù±‚`a)Ù±‚`a
Ù±‚`fbuttonÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`fButtonÙ±‚`a(Ù±‚`gresetaxÙ±‚`a,Ù±‚`a Ù±‚bs1a'Ù±‚bs1eResetÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`jhovercolorÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1e0.975Ù±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚akcdefÙ±‚`a Ù±‚bnferesetÙ±‚`a(Ù±‚`eeventÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`d    Ù±‚`kfreq_sliderÙ±‚aoa.Ù±‚`eresetÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`jamp_sliderÙ±‚aoa.Ù±‚`eresetÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`fbuttonÙ±‚aoa.Ù±‚`jon_clickedÙ±‚`a(Ù±‚`eresetÙ±‚`a)Ù±‚`a
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
Ù±‚bc1x"#    - `matplotlib.widgets.Button`Ù±‚`a
Ù±‚bc1x"#    - `matplotlib.widgets.Slider`Ù±‚`a
`dNoneö