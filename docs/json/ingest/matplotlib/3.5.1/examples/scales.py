Ù¯‚Ù´ƒ™(Ù±‚bsdxû"""
======
Scales
======

Illustrate the scale transformations applied to axes, e.g. log, symlog, logit.

The last two examples are examples of using the ``'function'`` scale by
supplying forward and inverse functions for the scale transformation.
"""Ù±‚`a
Ù±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„enumpyÙ „enumpyf1.22.3fmoduleenumpyfmoduleõÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnnbnpÙ±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnnfpyplotÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnncpltÙ±‚`a
Ù±‚bkndfromÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnnftickerÙ±‚`a Ù±‚bknfimportÙ±‚`a Ù±‚`mNullFormatterÙ±‚`a,Ù±‚`a Ù±‚`lFixedLocatorÙ±‚`a
Ù±‚`a
Ù±‚bc1x)# Fixing random state for reproducibilityÙ±‚`a
Ù±‚`bnpÙ±‚aoa.Ù±‚`frandomÙ±‚aoa.Ù±‚`dseedÙ±‚`a(Ù±‚bmih19680801Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚bc1x*# make up some data in the interval ]0, 1[Ù±‚`a
Ù±‚`ayÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`frandomÙ±‚aoa.Ù±‚`fnormalÙ±‚`a(Ù±‚`clocÙ±‚aoa=Ù±‚bmfc0.5Ù±‚`a,Ù±‚`a Ù±‚`escaleÙ±‚aoa=Ù±‚bmfc0.4Ù±‚`a,Ù±‚`a Ù±‚`dsizeÙ±‚aoa=Ù±‚bmid1000Ù±‚`a)Ù±‚`a
Ù±‚`ayÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`ayÙ±‚`a[Ù±‚`a(Ù±‚`ayÙ±‚`a Ù±‚aoa>Ù±‚`a Ù±‚bmia0Ù±‚`a)Ù±‚`a Ù±‚aoa&Ù±‚`a Ù±‚`a(Ù±‚`ayÙ±‚`a Ù±‚aoa<Ù±‚`a Ù±‚bmia1Ù±‚`a)Ù±‚`a]Ù±‚`a
Ù±‚`ayÙ±‚aoa.Ù±‚`dsortÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`axÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`farangeÙ±‚`a(Ù±‚bnbclenÙ±‚`a(Ù±‚`ayÙ±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚bc1x# plot with various axes scalesÙ±‚`a
Ù±‚`cfigÙ±‚`a,Ù±‚`a Ù±‚`caxsÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cpltÙ±‚aoa.Ù±‚`hsubplotsÙ±‚`a(Ù±‚bmia3Ù±‚`a,Ù±‚`a Ù±‚bmia2Ù±‚`a,Ù±‚`a Ù±‚`gfigsizeÙ±‚aoa=Ù±‚`a(Ù±‚bmia6Ù±‚`a,Ù±‚`a Ù±‚bmia8Ù±‚`a)Ù±‚`a,Ù±‚`a
Ù±‚`x                        Ù±‚`rconstrained_layoutÙ±‚aoa=Ù±‚bkcdTrueÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚bc1h# linearÙ±‚`a
Ù±‚`baxÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`caxsÙ±‚`a[Ù±‚bmia0Ù±‚`a,Ù±‚`a Ù±‚bmia0Ù±‚`a]Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`dplotÙ±‚`a(Ù±‚`axÙ±‚`a,Ù±‚`a Ù±‚`ayÙ±‚`a)Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`jset_yscaleÙ±‚`a(Ù±‚bs1a'Ù±‚bs1flinearÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`iset_titleÙ±‚`a(Ù±‚bs1a'Ù±‚bs1flinearÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`dgridÙ±‚`a(Ù±‚bkcdTrueÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚bc1e# logÙ±‚`a
Ù±‚`baxÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`caxsÙ±‚`a[Ù±‚bmia0Ù±‚`a,Ù±‚`a Ù±‚bmia1Ù±‚`a]Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`dplotÙ±‚`a(Ù±‚`axÙ±‚`a,Ù±‚`a Ù±‚`ayÙ±‚`a)Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`jset_yscaleÙ±‚`a(Ù±‚bs1a'Ù±‚bs1clogÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`iset_titleÙ±‚`a(Ù±‚bs1a'Ù±‚bs1clogÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`dgridÙ±‚`a(Ù±‚bkcdTrueÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚bc1o# symmetric logÙ±‚`a
Ù±‚`baxÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`caxsÙ±‚`a[Ù±‚bmia1Ù±‚`a,Ù±‚`a Ù±‚bmia1Ù±‚`a]Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`dplotÙ±‚`a(Ù±‚`axÙ±‚`a,Ù±‚`a Ù±‚`ayÙ±‚`a Ù±‚aoa-Ù±‚`a Ù±‚`ayÙ±‚aoa.Ù±‚`dmeanÙ±‚`a(Ù±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`jset_yscaleÙ±‚`a(Ù±‚bs1a'Ù±‚bs1fsymlogÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`ilinthreshÙ±‚aoa=Ù±‚bmfd0.02Ù±‚`a)Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`iset_titleÙ±‚`a(Ù±‚bs1a'Ù±‚bs1fsymlogÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`dgridÙ±‚`a(Ù±‚bkcdTrueÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚bc1g# logitÙ±‚`a
Ù±‚`baxÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`caxsÙ±‚`a[Ù±‚bmia1Ù±‚`a,Ù±‚`a Ù±‚bmia0Ù±‚`a]Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`dplotÙ±‚`a(Ù±‚`axÙ±‚`a,Ù±‚`a Ù±‚`ayÙ±‚`a)Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`jset_yscaleÙ±‚`a(Ù±‚bs1a'Ù±‚bs1elogitÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`iset_titleÙ±‚`a(Ù±‚bs1a'Ù±‚bs1elogitÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`dgridÙ±‚`a(Ù±‚bkcdTrueÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚bc1s# Function x**(1/2)Ù±‚`a
Ù±‚akcdefÙ±‚`a Ù±‚bnfgforwardÙ±‚`a(Ù±‚`axÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`d    Ù±‚akfreturnÙ±‚`a Ù±‚`axÙ±‚aoa*Ù±‚aoa*Ù±‚`a(Ù±‚bmia1Ù±‚aoa/Ù±‚bmia2Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚akcdefÙ±‚`a Ù±‚bnfginverseÙ±‚`a(Ù±‚`axÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`d    Ù±‚akfreturnÙ±‚`a Ù±‚`axÙ±‚aoa*Ù±‚aoa*Ù±‚bmia2Ù±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚`baxÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`caxsÙ±‚`a[Ù±‚bmia2Ù±‚`a,Ù±‚`a Ù±‚bmia0Ù±‚`a]Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`dplotÙ±‚`a(Ù±‚`axÙ±‚`a,Ù±‚`a Ù±‚`ayÙ±‚`a)Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`jset_yscaleÙ±‚`a(Ù±‚bs1a'Ù±‚bs1hfunctionÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`ifunctionsÙ±‚aoa=Ù±‚`a(Ù±‚`gforwardÙ±‚`a,Ù±‚`a Ù±‚`ginverseÙ±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`iset_titleÙ±‚`a(Ù±‚bs1a'Ù±‚bs1mfunction: $x^Ù±‚bs1a{Ù±‚bs1e1/2}$Ù±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`dgridÙ±‚`a(Ù±‚bkcdTrueÙ±‚`a)Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`eyaxisÙ±‚aoa.Ù±‚`qset_major_locatorÙ±‚`a(Ù±‚`lFixedLocatorÙ±‚`a(Ù±‚`bnpÙ±‚aoa.Ù±‚`farangeÙ±‚`a(Ù±‚bmia0Ù±‚`a,Ù±‚`a Ù±‚bmia1Ù±‚`a,Ù±‚`a Ù±‚bmfc0.2Ù±‚`a)Ù±‚aoa*Ù±‚aoa*Ù±‚bmia2Ù±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`eyaxisÙ±‚aoa.Ù±‚`qset_major_locatorÙ±‚`a(Ù±‚`lFixedLocatorÙ±‚`a(Ù±‚`bnpÙ±‚aoa.Ù±‚`farangeÙ±‚`a(Ù±‚bmia0Ù±‚`a,Ù±‚`a Ù±‚bmia1Ù±‚`a,Ù±‚`a Ù±‚bmfc0.2Ù±‚`a)Ù±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚bc1x# Function Mercator transformÙ±‚`a
Ù±‚akcdefÙ±‚`a Ù±‚bnfgforwardÙ±‚`a(Ù±‚`aaÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`d    Ù±‚`aaÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`gdeg2radÙ±‚`a(Ù±‚`aaÙ±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚akfreturnÙ±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`grad2degÙ±‚`a(Ù±‚`bnpÙ±‚aoa.Ù±‚`clogÙ±‚`a(Ù±‚`bnpÙ±‚aoa.Ù±‚`cabsÙ±‚`a(Ù±‚`bnpÙ±‚aoa.Ù±‚`ctanÙ±‚`a(Ù±‚`aaÙ±‚`a)Ù±‚`a Ù±‚aoa+Ù±‚`a Ù±‚bmfc1.0Ù±‚`a Ù±‚aoa/Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`ccosÙ±‚`a(Ù±‚`aaÙ±‚`a)Ù±‚`a)Ù±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚akcdefÙ±‚`a Ù±‚bnfginverseÙ±‚`a(Ù±‚`aaÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`d    Ù±‚`aaÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`gdeg2radÙ±‚`a(Ù±‚`aaÙ±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚akfreturnÙ±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`grad2degÙ±‚`a(Ù±‚`bnpÙ±‚aoa.Ù±‚`farctanÙ±‚`a(Ù±‚`bnpÙ±‚aoa.Ù±‚`dsinhÙ±‚`a(Ù±‚`aaÙ±‚`a)Ù±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`baxÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`caxsÙ±‚`a[Ù±‚bmia2Ù±‚`a,Ù±‚`a Ù±‚bmia1Ù±‚`a]Ù±‚`a
Ù±‚`a
Ù±‚`atÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`farangeÙ±‚`a(Ù±‚bmia0Ù±‚`a,Ù±‚`a Ù±‚bmfe170.0Ù±‚`a,Ù±‚`a Ù±‚bmfc0.1Ù±‚`a)Ù±‚`a
Ù±‚`asÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`atÙ±‚`a Ù±‚aoa/Ù±‚`a Ù±‚bmfb2.Ù±‚`a
Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`dplotÙ±‚`a(Ù±‚`atÙ±‚`a,Ù±‚`a Ù±‚`asÙ±‚`a,Ù±‚`a Ù±‚bs1a'Ù±‚bs1a-Ù±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`blwÙ±‚aoa=Ù±‚bmia2Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`jset_yscaleÙ±‚`a(Ù±‚bs1a'Ù±‚bs1hfunctionÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`ifunctionsÙ±‚aoa=Ù±‚`a(Ù±‚`gforwardÙ±‚`a,Ù±‚`a Ù±‚`ginverseÙ±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`iset_titleÙ±‚`a(Ù±‚bs1a'Ù±‚bs1rfunction: MercatorÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`dgridÙ±‚`a(Ù±‚bkcdTrueÙ±‚`a)Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`hset_xlimÙ±‚`a(Ù±‚`a[Ù±‚bmia0Ù±‚`a,Ù±‚`a Ù±‚bmic180Ù±‚`a]Ù±‚`a)Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`eyaxisÙ±‚aoa.Ù±‚`sset_minor_formatterÙ±‚`a(Ù±‚`mNullFormatterÙ±‚`a(Ù±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`eyaxisÙ±‚aoa.Ù±‚`qset_major_locatorÙ±‚`a(Ù±‚`lFixedLocatorÙ±‚`a(Ù±‚`bnpÙ±‚aoa.Ù±‚`farangeÙ±‚`a(Ù±‚bmia0Ù±‚`a,Ù±‚`a Ù±‚bmib90Ù±‚`a,Ù±‚`a Ù±‚bmib10Ù±‚`a)Ù±‚`a)Ù±‚`a)Ù±‚`a
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
Ù±‚bc1x(#    - `matplotlib.axes.Axes.set_xscale`Ù±‚`a
Ù±‚bc1x(#    - `matplotlib.axes.Axes.set_yscale`Ù±‚`a
Ù±‚bc1x/#    - `matplotlib.axis.Axis.set_major_locator`Ù±‚`a
Ù±‚bc1x%#    - `matplotlib.scale.LinearScale`Ù±‚`a
Ù±‚bc1x"#    - `matplotlib.scale.LogScale`Ù±‚`a
Ù±‚bc1x-#    - `matplotlib.scale.SymmetricalLogScale`Ù±‚`a
Ù±‚bc1x$#    - `matplotlib.scale.LogitScale`Ù±‚`a
Ù±‚bc1x##    - `matplotlib.scale.FuncScale`Ù±‚`a
`dNoneö