Ù¯‚Ù´ƒ™/Ù±‚bsdxğ"""
======================
Style sheets reference
======================

This script demonstrates the different available style sheets on a
common set of example plots: scatter plot, image, bar graph, patches,
line plot and histogram,

"""Ù±‚`a
Ù±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„enumpyÙ „enumpyf1.22.3fmoduleenumpyfmoduleõÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnnbnpÙ±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnnfpyplotÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnncpltÙ±‚`a
Ù±‚`a
Ù±‚bc1x)# Fixing random state for reproducibilityÙ±‚`a
Ù±‚`bnpÙ±‚aoa.Ù±‚`frandomÙ±‚aoa.Ù±‚`dseedÙ±‚`a(Ù±‚bmih19680801Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚akcdefÙ±‚`a Ù±‚bnflplot_scatterÙ±‚`a(Ù±‚`baxÙ±‚`a,Ù±‚`a Ù±‚`dprngÙ±‚`a,Ù±‚`a Ù±‚`jnb_samplesÙ±‚aoa=Ù±‚bmic100Ù±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`d    Ù±‚bsds"""Scatter plot."""Ù±‚`a
Ù±‚`d    Ù±‚akcforÙ±‚`a Ù±‚`bmuÙ±‚`a,Ù±‚`a Ù±‚`esigmaÙ±‚`a,Ù±‚`a Ù±‚`fmarkerÙ±‚`a Ù±‚bowbinÙ±‚`a Ù±‚`a[Ù±‚`a(Ù±‚aoa-Ù±‚bmfb.5Ù±‚`a,Ù±‚`a Ù±‚bmfd0.75Ù±‚`a,Ù±‚`a Ù±‚bs1a'Ù±‚bs1aoÙ±‚bs1a'Ù±‚`a)Ù±‚`a,Ù±‚`a Ù±‚`a(Ù±‚bmfd0.75Ù±‚`a,Ù±‚`a Ù±‚bmfb1.Ù±‚`a,Ù±‚`a Ù±‚bs1a'Ù±‚bs1asÙ±‚bs1a'Ù±‚`a)Ù±‚`a]Ù±‚`a:Ù±‚`a
Ù±‚`h        Ù±‚`axÙ±‚`a,Ù±‚`a Ù±‚`ayÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`dprngÙ±‚aoa.Ù±‚`fnormalÙ±‚`a(Ù±‚`clocÙ±‚aoa=Ù±‚`bmuÙ±‚`a,Ù±‚`a Ù±‚`escaleÙ±‚aoa=Ù±‚`esigmaÙ±‚`a,Ù±‚`a Ù±‚`dsizeÙ±‚aoa=Ù±‚`a(Ù±‚bmia2Ù±‚`a,Ù±‚`a Ù±‚`jnb_samplesÙ±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚`baxÙ±‚aoa.Ù±‚`dplotÙ±‚`a(Ù±‚`axÙ±‚`a,Ù±‚`a Ù±‚`ayÙ±‚`a,Ù±‚`a Ù±‚`blsÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1dnoneÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`fmarkerÙ±‚aoa=Ù±‚`fmarkerÙ±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`baxÙ±‚aoa.Ù±‚`jset_xlabelÙ±‚`a(Ù±‚bs1a'Ù±‚bs1gX-labelÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`baxÙ±‚aoa.Ù±‚`iset_titleÙ±‚`a(Ù±‚bs1a'Ù±‚bs1jAxes titleÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚akfreturnÙ±‚`a Ù±‚`baxÙ±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚akcdefÙ±‚`a Ù±‚bnfxplot_colored_sinusoidal_linesÙ±‚`a(Ù±‚`baxÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`d    Ù±‚bsdxH"""Plot sinusoidal lines with colors following the style color cycle."""Ù±‚`a
Ù±‚`d    Ù±‚`aLÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bmia2Ù±‚`a Ù±‚aoa*Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`bpiÙ±‚`a
Ù±‚`d    Ù±‚`axÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`hlinspaceÙ±‚`a(Ù±‚bmia0Ù±‚`a,Ù±‚`a Ù±‚`aLÙ±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`inb_colorsÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bnbclenÙ±‚`a(Ù±‚`cpltÙ±‚aoa.Ù±‚`hrcParamsÙ±‚`a[Ù±‚bs1a'Ù±‚bs1oaxes.prop_cycleÙ±‚bs1a'Ù±‚`a]Ù±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`eshiftÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`hlinspaceÙ±‚`a(Ù±‚bmia0Ù±‚`a,Ù±‚`a Ù±‚`aLÙ±‚`a,Ù±‚`a Ù±‚`inb_colorsÙ±‚`a,Ù±‚`a Ù±‚`hendpointÙ±‚aoa=Ù±‚bkceFalseÙ±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚akcforÙ±‚`a Ù±‚`asÙ±‚`a Ù±‚bowbinÙ±‚`a Ù±‚`eshiftÙ±‚`a:Ù±‚`a
Ù±‚`h        Ù±‚`baxÙ±‚aoa.Ù±‚`dplotÙ±‚`a(Ù±‚`axÙ±‚`a,Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`csinÙ±‚`a(Ù±‚`axÙ±‚`a Ù±‚aoa+Ù±‚`a Ù±‚`asÙ±‚`a)Ù±‚`a,Ù±‚`a Ù±‚bs1a'Ù±‚bs1a-Ù±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`baxÙ±‚aoa.Ù±‚`hset_xlimÙ±‚`a(Ù±‚`a[Ù±‚`axÙ±‚`a[Ù±‚bmia0Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`axÙ±‚`a[Ù±‚aoa-Ù±‚bmia1Ù±‚`a]Ù±‚`a]Ù±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚akfreturnÙ±‚`a Ù±‚`baxÙ±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚akcdefÙ±‚`a Ù±‚bnfoplot_bar_graphsÙ±‚`a(Ù±‚`baxÙ±‚`a,Ù±‚`a Ù±‚`dprngÙ±‚`a,Ù±‚`a Ù±‚`imin_valueÙ±‚aoa=Ù±‚bmia5Ù±‚`a,Ù±‚`a Ù±‚`imax_valueÙ±‚aoa=Ù±‚bmib25Ù±‚`a,Ù±‚`a Ù±‚`jnb_samplesÙ±‚aoa=Ù±‚bmia5Ù±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`d    Ù±‚bsdxF"""Plot two bar graphs side by side, with letters as x-tick labels."""Ù±‚`a
Ù±‚`d    Ù±‚`axÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`farangeÙ±‚`a(Ù±‚`jnb_samplesÙ±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`byaÙ±‚`a,Ù±‚`a Ù±‚`bybÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`dprngÙ±‚aoa.Ù±‚`grandintÙ±‚`a(Ù±‚`imin_valueÙ±‚`a,Ù±‚`a Ù±‚`imax_valueÙ±‚`a,Ù±‚`a Ù±‚`dsizeÙ±‚aoa=Ù±‚`a(Ù±‚bmia2Ù±‚`a,Ù±‚`a Ù±‚`jnb_samplesÙ±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`ewidthÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bmfd0.25Ù±‚`a
Ù±‚`d    Ù±‚`baxÙ±‚aoa.Ù±‚`cbarÙ±‚`a(Ù±‚`axÙ±‚`a,Ù±‚`a Ù±‚`byaÙ±‚`a,Ù±‚`a Ù±‚`ewidthÙ±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`baxÙ±‚aoa.Ù±‚`cbarÙ±‚`a(Ù±‚`axÙ±‚`a Ù±‚aoa+Ù±‚`a Ù±‚`ewidthÙ±‚`a,Ù±‚`a Ù±‚`bybÙ±‚`a,Ù±‚`a Ù±‚`ewidthÙ±‚`a,Ù±‚`a Ù±‚`ecolorÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1bC2Ù±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`baxÙ±‚aoa.Ù±‚`jset_xticksÙ±‚`a(Ù±‚`axÙ±‚`a Ù±‚aoa+Ù±‚`a Ù±‚`ewidthÙ±‚`a,Ù±‚`a Ù±‚`flabelsÙ±‚aoa=Ù±‚`a[Ù±‚bs1a'Ù±‚bs1aaÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚bs1a'Ù±‚bs1abÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚bs1a'Ù±‚bs1acÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚bs1a'Ù±‚bs1adÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚bs1a'Ù±‚bs1aeÙ±‚bs1a'Ù±‚`a]Ù±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚akfreturnÙ±‚`a Ù±‚`baxÙ±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚akcdefÙ±‚`a Ù±‚bnftplot_colored_circlesÙ±‚`a(Ù±‚`baxÙ±‚`a,Ù±‚`a Ù±‚`dprngÙ±‚`a,Ù±‚`a Ù±‚`jnb_samplesÙ±‚aoa=Ù±‚bmib15Ù±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`d    Ù±‚bsdxÆ"""
    Plot circle patches.

    NB: draws a fixed amount of samples, rather than using the length of
    the color cycle, because different styles may have different numbers
    of colors.
    """Ù±‚`a
Ù±‚`d    Ù±‚akcforÙ±‚`a Ù±‚`hsty_dictÙ±‚`a,Ù±‚`a Ù±‚`ajÙ±‚`a Ù±‚bowbinÙ±‚`a Ù±‚bnbczipÙ±‚`a(Ù±‚`cpltÙ±‚aoa.Ù±‚`hrcParamsÙ±‚`a[Ù±‚bs1a'Ù±‚bs1oaxes.prop_cycleÙ±‚bs1a'Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚bnberangeÙ±‚`a(Ù±‚`jnb_samplesÙ±‚`a)Ù±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`h        Ù±‚`baxÙ±‚aoa.Ù±‚`iadd_patchÙ±‚`a(Ù±‚`cpltÙ±‚aoa.Ù±‚`fCircleÙ±‚`a(Ù±‚`dprngÙ±‚aoa.Ù±‚`fnormalÙ±‚`a(Ù±‚`escaleÙ±‚aoa=Ù±‚bmia3Ù±‚`a,Ù±‚`a Ù±‚`dsizeÙ±‚aoa=Ù±‚bmia2Ù±‚`a)Ù±‚`a,Ù±‚`a
Ù±‚`x                                 Ù±‚`fradiusÙ±‚aoa=Ù±‚bmfc1.0Ù±‚`a,Ù±‚`a Ù±‚`ecolorÙ±‚aoa=Ù±‚`hsty_dictÙ±‚`a[Ù±‚bs1a'Ù±‚bs1ecolorÙ±‚bs1a'Ù±‚`a]Ù±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚bc1xF# Force the limits to be the same across the styles (because differentÙ±‚`a
Ù±‚`d    Ù±‚bc1x9# styles may have different numbers of available colors).Ù±‚`a
Ù±‚`d    Ù±‚`baxÙ±‚aoa.Ù±‚`hset_xlimÙ±‚`a(Ù±‚`a[Ù±‚aoa-Ù±‚bmia4Ù±‚`a,Ù±‚`a Ù±‚bmia8Ù±‚`a]Ù±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`baxÙ±‚aoa.Ù±‚`hset_ylimÙ±‚`a(Ù±‚`a[Ù±‚aoa-Ù±‚bmia5Ù±‚`a,Ù±‚`a Ù±‚bmia6Ù±‚`a]Ù±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`baxÙ±‚aoa.Ù±‚`jset_aspectÙ±‚`a(Ù±‚bs1a'Ù±‚bs1eequalÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`jadjustableÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1cboxÙ±‚bs1a'Ù±‚`a)Ù±‚`b  Ù±‚bc1x# to plot circles as circlesÙ±‚`a
Ù±‚`d    Ù±‚akfreturnÙ±‚`a Ù±‚`baxÙ±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚akcdefÙ±‚`a Ù±‚bnftplot_image_and_patchÙ±‚`a(Ù±‚`baxÙ±‚`a,Ù±‚`a Ù±‚`dprngÙ±‚`a,Ù±‚`a Ù±‚`dsizeÙ±‚aoa=Ù±‚`a(Ù±‚bmib20Ù±‚`a,Ù±‚`a Ù±‚bmib20Ù±‚`a)Ù±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`d    Ù±‚bsdxH"""Plot an image with random values and superimpose a circular patch."""Ù±‚`a
Ù±‚`d    Ù±‚`fvaluesÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`dprngÙ±‚aoa.Ù±‚`mrandom_sampleÙ±‚`a(Ù±‚`dsizeÙ±‚aoa=Ù±‚`dsizeÙ±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`baxÙ±‚aoa.Ù±‚`fimshowÙ±‚`a(Ù±‚`fvaluesÙ±‚`a,Ù±‚`a Ù±‚`minterpolationÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1dnoneÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`acÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cpltÙ±‚aoa.Ù±‚`fCircleÙ±‚`a(Ù±‚`a(Ù±‚bmia5Ù±‚`a,Ù±‚`a Ù±‚bmia5Ù±‚`a)Ù±‚`a,Ù±‚`a Ù±‚`fradiusÙ±‚aoa=Ù±‚bmia5Ù±‚`a,Ù±‚`a Ù±‚`elabelÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1epatchÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`baxÙ±‚aoa.Ù±‚`iadd_patchÙ±‚`a(Ù±‚`acÙ±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚bc1n# Remove ticksÙ±‚`a
Ù±‚`d    Ù±‚`baxÙ±‚aoa.Ù±‚`jset_xticksÙ±‚`a(Ù±‚`a[Ù±‚`a]Ù±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`baxÙ±‚aoa.Ù±‚`jset_yticksÙ±‚`a(Ù±‚`a[Ù±‚`a]Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚akcdefÙ±‚`a Ù±‚bnfoplot_histogramsÙ±‚`a(Ù±‚`baxÙ±‚`a,Ù±‚`a Ù±‚`dprngÙ±‚`a,Ù±‚`a Ù±‚`jnb_samplesÙ±‚aoa=Ù±‚bmie10000Ù±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`d    Ù±‚bsdx."""Plot 4 histograms and a text annotation."""Ù±‚`a
Ù±‚`d    Ù±‚`fparamsÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`a(Ù±‚`a(Ù±‚bmib10Ù±‚`a,Ù±‚`a Ù±‚bmib10Ù±‚`a)Ù±‚`a,Ù±‚`a Ù±‚`a(Ù±‚bmia4Ù±‚`a,Ù±‚`a Ù±‚bmib12Ù±‚`a)Ù±‚`a,Ù±‚`a Ù±‚`a(Ù±‚bmib50Ù±‚`a,Ù±‚`a Ù±‚bmib12Ù±‚`a)Ù±‚`a,Ù±‚`a Ù±‚`a(Ù±‚bmia6Ù±‚`a,Ù±‚`a Ù±‚bmib55Ù±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚akcforÙ±‚`a Ù±‚`aaÙ±‚`a,Ù±‚`a Ù±‚`abÙ±‚`a Ù±‚bowbinÙ±‚`a Ù±‚`fparamsÙ±‚`a:Ù±‚`a
Ù±‚`h        Ù±‚`fvaluesÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`dprngÙ±‚aoa.Ù±‚`dbetaÙ±‚`a(Ù±‚`aaÙ±‚`a,Ù±‚`a Ù±‚`abÙ±‚`a,Ù±‚`a Ù±‚`dsizeÙ±‚aoa=Ù±‚`jnb_samplesÙ±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚`baxÙ±‚aoa.Ù±‚`dhistÙ±‚`a(Ù±‚`fvaluesÙ±‚`a,Ù±‚`a Ù±‚`hhisttypeÙ±‚aoa=Ù±‚bs2a"Ù±‚bs2jstepfilledÙ±‚bs2a"Ù±‚`a,Ù±‚`a Ù±‚`dbinsÙ±‚aoa=Ù±‚bmib30Ù±‚`a,Ù±‚`a
Ù±‚`p                Ù±‚`ealphaÙ±‚aoa=Ù±‚bmfc0.8Ù±‚`a,Ù±‚`a Ù±‚`gdensityÙ±‚aoa=Ù±‚bkcdTrueÙ±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚bc1x# Add a small annotation.Ù±‚`a
Ù±‚`d    Ù±‚`baxÙ±‚aoa.Ù±‚`hannotateÙ±‚`a(Ù±‚bs1a'Ù±‚bs1jAnnotationÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`bxyÙ±‚aoa=Ù±‚`a(Ù±‚bmfd0.25Ù±‚`a,Ù±‚`a Ù±‚bmfd4.25Ù±‚`a)Ù±‚`a,Ù±‚`a
Ù±‚`p                Ù±‚`fxytextÙ±‚aoa=Ù±‚`a(Ù±‚bmfc0.9Ù±‚`a,Ù±‚`a Ù±‚bmfc0.9Ù±‚`a)Ù±‚`a,Ù±‚`a Ù±‚`jtextcoordsÙ±‚aoa=Ù±‚`baxÙ±‚aoa.Ù±‚`itransAxesÙ±‚`a,Ù±‚`a
Ù±‚`p                Ù±‚`bvaÙ±‚aoa=Ù±‚bs2a"Ù±‚bs2ctopÙ±‚bs2a"Ù±‚`a,Ù±‚`a Ù±‚`bhaÙ±‚aoa=Ù±‚bs2a"Ù±‚bs2erightÙ±‚bs2a"Ù±‚`a,Ù±‚`a
Ù±‚`p                Ù±‚`dbboxÙ±‚aoa=Ù±‚bnbddictÙ±‚`a(Ù±‚`hboxstyleÙ±‚aoa=Ù±‚bs2a"Ù±‚bs2eroundÙ±‚bs2a"Ù±‚`a,Ù±‚`a Ù±‚`ealphaÙ±‚aoa=Ù±‚bmfc0.2Ù±‚`a)Ù±‚`a,Ù±‚`a
Ù±‚`p                Ù±‚`jarrowpropsÙ±‚aoa=Ù±‚bnbddictÙ±‚`a(Ù±‚`a
Ù±‚`x                          Ù±‚`jarrowstyleÙ±‚aoa=Ù±‚bs2a"Ù±‚bs2b->Ù±‚bs2a"Ù±‚`a,Ù±‚`a
Ù±‚`x                          Ù±‚`oconnectionstyleÙ±‚aoa=Ù±‚bs2a"Ù±‚bs2x!angle,angleA=-95,angleB=35,rad=10Ù±‚bs2a"Ù±‚`a)Ù±‚`a,Ù±‚`a
Ù±‚`p                Ù±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚akfreturnÙ±‚`a Ù±‚`baxÙ±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚akcdefÙ±‚`a Ù±‚bnfkplot_figureÙ±‚`a(Ù±‚`kstyle_labelÙ±‚aoa=Ù±‚bs2a"Ù±‚bs2a"Ù±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`d    Ù±‚bsdxA"""Setup and plot the demonstration figure with a given style."""Ù±‚`a
Ù±‚`d    Ù±‚bc1xG# Use a dedicated RandomState instance to draw the same "random" valuesÙ±‚`a
Ù±‚`d    Ù±‚bc1x# across the different figures.Ù±‚`a
Ù±‚`d    Ù±‚`dprngÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`frandomÙ±‚aoa.Ù±‚`kRandomStateÙ±‚`a(Ù±‚bmih96917002Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚bc1xH# Tweak the figure size to be better suited for a row of numerous plots:Ù±‚`a
Ù±‚`d    Ù±‚bc1xI# double the width and halve the height. NB: use relative changes becauseÙ±‚`a
Ù±‚`d    Ù±‚bc1xD# some styles may have a figure size different from the default one.Ù±‚`a
Ù±‚`d    Ù±‚`a(Ù±‚`ifig_widthÙ±‚`a,Ù±‚`a Ù±‚`jfig_heightÙ±‚`a)Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cpltÙ±‚aoa.Ù±‚`hrcParamsÙ±‚`a[Ù±‚bs1a'Ù±‚bs1nfigure.figsizeÙ±‚bs1a'Ù±‚`a]Ù±‚`a
Ù±‚`d    Ù±‚`hfig_sizeÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`a[Ù±‚`ifig_widthÙ±‚`a Ù±‚aoa*Ù±‚`a Ù±‚bmia2Ù±‚`a,Ù±‚`a Ù±‚`jfig_heightÙ±‚`a Ù±‚aoa/Ù±‚`a Ù±‚bmia2Ù±‚`a]Ù±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚`cfigÙ±‚`a,Ù±‚`a Ù±‚`caxsÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cpltÙ±‚aoa.Ù±‚`hsubplotsÙ±‚`a(Ù±‚`encolsÙ±‚aoa=Ù±‚bmia6Ù±‚`a,Ù±‚`a Ù±‚`enrowsÙ±‚aoa=Ù±‚bmia1Ù±‚`a,Ù±‚`a Ù±‚`cnumÙ±‚aoa=Ù±‚`kstyle_labelÙ±‚`a,Ù±‚`a
Ù±‚`x                            Ù±‚`gfigsizeÙ±‚aoa=Ù±‚`hfig_sizeÙ±‚`a,Ù±‚`a Ù±‚`gsqueezeÙ±‚aoa=Ù±‚bkcdTrueÙ±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`caxsÙ±‚`a[Ù±‚bmia0Ù±‚`a]Ù±‚aoa.Ù±‚`jset_ylabelÙ±‚`a(Ù±‚`kstyle_labelÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚`lplot_scatterÙ±‚`a(Ù±‚`caxsÙ±‚`a[Ù±‚bmia0Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`dprngÙ±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`tplot_image_and_patchÙ±‚`a(Ù±‚`caxsÙ±‚`a[Ù±‚bmia1Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`dprngÙ±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`oplot_bar_graphsÙ±‚`a(Ù±‚`caxsÙ±‚`a[Ù±‚bmia2Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`dprngÙ±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`tplot_colored_circlesÙ±‚`a(Ù±‚`caxsÙ±‚`a[Ù±‚bmia3Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`dprngÙ±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`xplot_colored_sinusoidal_linesÙ±‚`a(Ù±‚`caxsÙ±‚`a[Ù±‚bmia4Ù±‚`a]Ù±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`oplot_histogramsÙ±‚`a(Ù±‚`caxsÙ±‚`a[Ù±‚bmia5Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`dprngÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚`cfigÙ±‚aoa.Ù±‚`ltight_layoutÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚akfreturnÙ±‚`a Ù±‚`cfigÙ±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚akbifÙ±‚`a Ù±‚bvmh__name__Ù±‚`a Ù±‚aob==Ù±‚`a Ù±‚bs2a"Ù±‚bs2h__main__Ù±‚bs2a"Ù±‚`a:Ù±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚bc1xA# Setup a list of all available styles, in alphabetical order butÙ±‚`a
Ù±‚`d    Ù±‚bc1xA# the `default` and `classic` ones, which will be forced resp. inÙ±‚`a
Ù±‚`d    Ù±‚bc1x# first and second position.Ù±‚`a
Ù±‚`d    Ù±‚`jstyle_listÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`a[Ù±‚bs1a'Ù±‚bs1gdefaultÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚bs1a'Ù±‚bs1gclassicÙ±‚bs1a'Ù±‚`a]Ù±‚`a Ù±‚aoa+Ù±‚`a Ù±‚bnbfsortedÙ±‚`a(Ù±‚`a
Ù±‚`h        Ù±‚`estyleÙ±‚`a Ù±‚akcforÙ±‚`a Ù±‚`estyleÙ±‚`a Ù±‚bowbinÙ±‚`a Ù±‚`cpltÙ±‚aoa.Ù±‚`estyleÙ±‚aoa.Ù±‚`iavailableÙ±‚`a Ù±‚akbifÙ±‚`a Ù±‚`estyleÙ±‚`a Ù±‚aob!=Ù±‚`a Ù±‚bs1a'Ù±‚bs1gclassicÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚bc1x># Plot a demonstration figure for every available style sheet.Ù±‚`a
Ù±‚`d    Ù±‚akcforÙ±‚`a Ù±‚`kstyle_labelÙ±‚`a Ù±‚bowbinÙ±‚`a Ù±‚`jstyle_listÙ±‚`a:Ù±‚`a
Ù±‚`h        Ù±‚akdwithÙ±‚`a Ù±‚`cpltÙ±‚aoa.Ù±‚`jrc_contextÙ±‚`a(Ù±‚`a{Ù±‚bs2a"Ù±‚bs2wfigure.max_open_warningÙ±‚bs2a"Ù±‚`a:Ù±‚`a Ù±‚bnbclenÙ±‚`a(Ù±‚`jstyle_listÙ±‚`a)Ù±‚`a}Ù±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`l            Ù±‚akdwithÙ±‚`a Ù±‚`cpltÙ±‚aoa.Ù±‚`estyleÙ±‚aoa.Ù±‚`gcontextÙ±‚`a(Ù±‚`kstyle_labelÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`p                Ù±‚`cfigÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`kplot_figureÙ±‚`a(Ù±‚`kstyle_labelÙ±‚aoa=Ù±‚`kstyle_labelÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚`cpltÙ±‚aoa.Ù±‚`dshowÙ±‚`a(Ù±‚`a)Ù±‚`a
`dNoneö