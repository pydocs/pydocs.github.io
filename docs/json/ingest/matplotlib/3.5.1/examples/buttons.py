Ù¯‚Ù´ƒ™¦Ù±‚bsdx´"""
=======
Buttons
=======

Constructing a simple button GUI to modify a sine wave.

The ``next`` and ``previous`` button widget helps visualize the wave with
new frequencies.
"""Ù±‚`a
Ù±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„enumpyÙ „enumpyf1.22.3fmoduleenumpyfmoduleõÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnnbnpÙ±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnnfpyplotÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnncpltÙ±‚`a
Ù±‚bkndfromÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnngwidgetsÙ±‚`a Ù±‚bknfimportÙ±‚`a Ù±‚`fButtonÙ±‚`a
Ù±‚`a
Ù±‚`efreqsÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`farangeÙ±‚`a(Ù±‚bmia2Ù±‚`a,Ù±‚`a Ù±‚bmib20Ù±‚`a,Ù±‚`a Ù±‚bmia3Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`cfigÙ±‚`a,Ù±‚`a Ù±‚`baxÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cpltÙ±‚aoa.Ù±‚`hsubplotsÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`cpltÙ±‚aoa.Ù±‚`osubplots_adjustÙ±‚`a(Ù±‚`fbottomÙ±‚aoa=Ù±‚bmfc0.2Ù±‚`a)Ù±‚`a
Ù±‚`atÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`farangeÙ±‚`a(Ù±‚bmfc0.0Ù±‚`a,Ù±‚`a Ù±‚bmfc1.0Ù±‚`a,Ù±‚`a Ù±‚bmfe0.001Ù±‚`a)Ù±‚`a
Ù±‚`asÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`csinÙ±‚`a(Ù±‚bmia2Ù±‚aoa*Ù±‚`bnpÙ±‚aoa.Ù±‚`bpiÙ±‚aoa*Ù±‚`efreqsÙ±‚`a[Ù±‚bmia0Ù±‚`a]Ù±‚aoa*Ù±‚`atÙ±‚`a)Ù±‚`a
Ù±‚`alÙ±‚`a,Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cpltÙ±‚aoa.Ù±‚`dplotÙ±‚`a(Ù±‚`atÙ±‚`a,Ù±‚`a Ù±‚`asÙ±‚`a,Ù±‚`a Ù±‚`blwÙ±‚aoa=Ù±‚bmia2Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚akeclassÙ±‚`a Ù±‚bnceIndexÙ±‚`a:Ù±‚`a
Ù±‚`d    Ù±‚`cindÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bmia0Ù±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚akcdefÙ±‚`a Ù±‚bnfdnextÙ±‚`a(Ù±‚bbpdselfÙ±‚`a,Ù±‚`a Ù±‚`eeventÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`cindÙ±‚`a Ù±‚aoa+Ù±‚aoa=Ù±‚`a Ù±‚bmia1Ù±‚`a
Ù±‚`h        Ù±‚`aiÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bbpdselfÙ±‚aoa.Ù±‚`cindÙ±‚`a Ù±‚aoa%Ù±‚`a Ù±‚bnbclenÙ±‚`a(Ù±‚`efreqsÙ±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚`eydataÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`csinÙ±‚`a(Ù±‚bmia2Ù±‚aoa*Ù±‚`bnpÙ±‚aoa.Ù±‚`bpiÙ±‚aoa*Ù±‚`efreqsÙ±‚`a[Ù±‚`aiÙ±‚`a]Ù±‚aoa*Ù±‚`atÙ±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚`alÙ±‚aoa.Ù±‚`iset_ydataÙ±‚`a(Ù±‚`eydataÙ±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚`cpltÙ±‚aoa.Ù±‚`ddrawÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚akcdefÙ±‚`a Ù±‚bnfdprevÙ±‚`a(Ù±‚bbpdselfÙ±‚`a,Ù±‚`a Ù±‚`eeventÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`cindÙ±‚`a Ù±‚aoa-Ù±‚aoa=Ù±‚`a Ù±‚bmia1Ù±‚`a
Ù±‚`h        Ù±‚`aiÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bbpdselfÙ±‚aoa.Ù±‚`cindÙ±‚`a Ù±‚aoa%Ù±‚`a Ù±‚bnbclenÙ±‚`a(Ù±‚`efreqsÙ±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚`eydataÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`csinÙ±‚`a(Ù±‚bmia2Ù±‚aoa*Ù±‚`bnpÙ±‚aoa.Ù±‚`bpiÙ±‚aoa*Ù±‚`efreqsÙ±‚`a[Ù±‚`aiÙ±‚`a]Ù±‚aoa*Ù±‚`atÙ±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚`alÙ±‚aoa.Ù±‚`iset_ydataÙ±‚`a(Ù±‚`eydataÙ±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚`cpltÙ±‚aoa.Ù±‚`ddrawÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`hcallbackÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`eIndexÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`faxprevÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cpltÙ±‚aoa.Ù±‚`daxesÙ±‚`a(Ù±‚`a[Ù±‚bmfc0.7Ù±‚`a,Ù±‚`a Ù±‚bmfd0.05Ù±‚`a,Ù±‚`a Ù±‚bmfc0.1Ù±‚`a,Ù±‚`a Ù±‚bmfe0.075Ù±‚`a]Ù±‚`a)Ù±‚`a
Ù±‚`faxnextÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cpltÙ±‚aoa.Ù±‚`daxesÙ±‚`a(Ù±‚`a[Ù±‚bmfd0.81Ù±‚`a,Ù±‚`a Ù±‚bmfd0.05Ù±‚`a,Ù±‚`a Ù±‚bmfc0.1Ù±‚`a,Ù±‚`a Ù±‚bmfe0.075Ù±‚`a]Ù±‚`a)Ù±‚`a
Ù±‚`ebnextÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`fButtonÙ±‚`a(Ù±‚`faxnextÙ±‚`a,Ù±‚`a Ù±‚bs1a'Ù±‚bs1dNextÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`ebnextÙ±‚aoa.Ù±‚`jon_clickedÙ±‚`a(Ù±‚`hcallbackÙ±‚aoa.Ù±‚`dnextÙ±‚`a)Ù±‚`a
Ù±‚`ebprevÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`fButtonÙ±‚`a(Ù±‚`faxprevÙ±‚`a,Ù±‚`a Ù±‚bs1a'Ù±‚bs1hPreviousÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`ebprevÙ±‚aoa.Ù±‚`jon_clickedÙ±‚`a(Ù±‚`hcallbackÙ±‚aoa.Ù±‚`dprevÙ±‚`a)Ù±‚`a
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
`dNoneö