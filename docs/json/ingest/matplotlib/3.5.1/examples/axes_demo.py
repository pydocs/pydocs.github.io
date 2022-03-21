Ù¯‚Ù´ƒ™sÙ±‚bsdyn"""
=========
Axes Demo
=========

Example use of ``fig.add_axes`` to create inset axes within the main plot axes.

Please see also the :ref:`axes_grid_examples` section, and the following three
examples:

- :doc:`/gallery/subplots_axes_and_figures/zoom_inset_axes`
- :doc:`/gallery/axes_grid1/inset_locator_demo`
- :doc:`/gallery/axes_grid1/inset_locator_demo2`
"""Ù±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnnfpyplotÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnncpltÙ±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„enumpyÙ „enumpyf1.22.3fmoduleenumpyfmoduleõÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnnbnpÙ±‚`a
Ù±‚`a
Ù±‚`bnpÙ±‚aoa.Ù±‚`frandomÙ±‚aoa.Ù±‚`dseedÙ±‚`a(Ù±‚bmih19680801Ù±‚`a)Ù±‚`b  Ù±‚bc1x*# Fixing random state for reproducibility.Ù±‚`a
Ù±‚`a
Ù±‚bc1x&# create some data to use for the plotÙ±‚`a
Ù±‚`bdtÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bmfe0.001Ù±‚`a
Ù±‚`atÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`farangeÙ±‚`a(Ù±‚bmfc0.0Ù±‚`a,Ù±‚`a Ù±‚bmfd10.0Ù±‚`a,Ù±‚`a Ù±‚`bdtÙ±‚`a)Ù±‚`a
Ù±‚`arÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`cexpÙ±‚`a(Ù±‚aoa-Ù±‚`atÙ±‚`a[Ù±‚`a:Ù±‚bmid1000Ù±‚`a]Ù±‚`a Ù±‚aoa/Ù±‚`a Ù±‚bmfd0.05Ù±‚`a)Ù±‚`b  Ù±‚bc1r# impulse responseÙ±‚`a
Ù±‚`axÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`frandomÙ±‚aoa.Ù±‚`erandnÙ±‚`a(Ù±‚bnbclenÙ±‚`a(Ù±‚`atÙ±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`asÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`hconvolveÙ±‚`a(Ù±‚`axÙ±‚`a,Ù±‚`a Ù±‚`arÙ±‚`a)Ù±‚`a[Ù±‚`a:Ù±‚bnbclenÙ±‚`a(Ù±‚`axÙ±‚`a)Ù±‚`a]Ù±‚`a Ù±‚aoa*Ù±‚`a Ù±‚`bdtÙ±‚`b  Ù±‚bc1o# colored noiseÙ±‚`a
Ù±‚`a
Ù±‚`cfigÙ±‚`a,Ù±‚`a Ù±‚`gmain_axÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cpltÙ±‚aoa.Ù±‚`hsubplotsÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`gmain_axÙ±‚aoa.Ù±‚`dplotÙ±‚`a(Ù±‚`atÙ±‚`a,Ù±‚`a Ù±‚`asÙ±‚`a)Ù±‚`a
Ù±‚`gmain_axÙ±‚aoa.Ù±‚`hset_xlimÙ±‚`a(Ù±‚bmia0Ù±‚`a,Ù±‚`a Ù±‚bmia1Ù±‚`a)Ù±‚`a
Ù±‚`gmain_axÙ±‚aoa.Ù±‚`hset_ylimÙ±‚`a(Ù±‚bmfc1.1Ù±‚`a Ù±‚aoa*Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`cminÙ±‚`a(Ù±‚`asÙ±‚`a)Ù±‚`a,Ù±‚`a Ù±‚bmia2Ù±‚`a Ù±‚aoa*Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`cmaxÙ±‚`a(Ù±‚`asÙ±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`gmain_axÙ±‚aoa.Ù±‚`jset_xlabelÙ±‚`a(Ù±‚bs1a'Ù±‚bs1htime (s)Ù±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`gmain_axÙ±‚aoa.Ù±‚`jset_ylabelÙ±‚`a(Ù±‚bs1a'Ù±‚bs1lcurrent (nA)Ù±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`gmain_axÙ±‚aoa.Ù±‚`iset_titleÙ±‚`a(Ù±‚bs1a'Ù±‚bs1vGaussian colored noiseÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚bc1x*# this is an inset axes over the main axesÙ±‚`a
Ù±‚`nright_inset_axÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cfigÙ±‚aoa.Ù±‚`hadd_axesÙ±‚`a(Ù±‚`a[Ù±‚bmfc.65Ù±‚`a,Ù±‚`a Ù±‚bmfb.6Ù±‚`a,Ù±‚`a Ù±‚bmfb.2Ù±‚`a,Ù±‚`a Ù±‚bmfb.2Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`ifacecolorÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1akÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`nright_inset_axÙ±‚aoa.Ù±‚`dhistÙ±‚`a(Ù±‚`asÙ±‚`a,Ù±‚`a Ù±‚bmic400Ù±‚`a,Ù±‚`a Ù±‚`gdensityÙ±‚aoa=Ù±‚bkcdTrueÙ±‚`a)Ù±‚`a
Ù±‚`nright_inset_axÙ±‚aoa.Ù±‚`csetÙ±‚`a(Ù±‚`etitleÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1kProbabilityÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`fxticksÙ±‚aoa=Ù±‚`a[Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`fyticksÙ±‚aoa=Ù±‚`a[Ù±‚`a]Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚bc1x/# this is another inset axes over the main axesÙ±‚`a
Ù±‚`mleft_inset_axÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cfigÙ±‚aoa.Ù±‚`hadd_axesÙ±‚`a(Ù±‚`a[Ù±‚bmfb.2Ù±‚`a,Ù±‚`a Ù±‚bmfb.6Ù±‚`a,Ù±‚`a Ù±‚bmfb.2Ù±‚`a,Ù±‚`a Ù±‚bmfb.2Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`ifacecolorÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1akÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`mleft_inset_axÙ±‚aoa.Ù±‚`dplotÙ±‚`a(Ù±‚`atÙ±‚`a[Ù±‚`a:Ù±‚bnbclenÙ±‚`a(Ù±‚`arÙ±‚`a)Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`arÙ±‚`a)Ù±‚`a
Ù±‚`mleft_inset_axÙ±‚aoa.Ù±‚`csetÙ±‚`a(Ù±‚`etitleÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1pImpulse responseÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`dxlimÙ±‚aoa=Ù±‚`a(Ù±‚bmia0Ù±‚`a,Ù±‚`a Ù±‚bmfb.2Ù±‚`a)Ù±‚`a,Ù±‚`a Ù±‚`fxticksÙ±‚aoa=Ù±‚`a[Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`fyticksÙ±‚aoa=Ù±‚`a[Ù±‚`a]Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`cpltÙ±‚aoa.Ù±‚`dshowÙ±‚`a(Ù±‚`a)Ù±‚`a
`dNoneö