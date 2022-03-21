Ù¯‚Ù´ƒ™µÙ±‚bsdx³"""
=============
Span Selector
=============

The SpanSelector is a mouse widget to select a xmin/xmax range and plot the
detail view of the selected region in the lower axes
"""Ù±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„enumpyÙ „enumpyf1.22.3fmoduleenumpyfmoduleõÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnnbnpÙ±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnnfpyplotÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnncpltÙ±‚`a
Ù±‚bkndfromÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnngwidgetsÙ±‚`a Ù±‚bknfimportÙ±‚`a Ù±‚`lSpanSelectorÙ±‚`a
Ù±‚`a
Ù±‚bc1x)# Fixing random state for reproducibilityÙ±‚`a
Ù±‚`bnpÙ±‚aoa.Ù±‚`frandomÙ±‚aoa.Ù±‚`dseedÙ±‚`a(Ù±‚bmih19680801Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`cfigÙ±‚`a,Ù±‚`a Ù±‚`a(Ù±‚`cax1Ù±‚`a,Ù±‚`a Ù±‚`cax2Ù±‚`a)Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cpltÙ±‚aoa.Ù±‚`hsubplotsÙ±‚`a(Ù±‚bmia2Ù±‚`a,Ù±‚`a Ù±‚`gfigsizeÙ±‚aoa=Ù±‚`a(Ù±‚bmia8Ù±‚`a,Ù±‚`a Ù±‚bmia6Ù±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`axÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`farangeÙ±‚`a(Ù±‚bmfc0.0Ù±‚`a,Ù±‚`a Ù±‚bmfc5.0Ù±‚`a,Ù±‚`a Ù±‚bmfd0.01Ù±‚`a)Ù±‚`a
Ù±‚`ayÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`csinÙ±‚`a(Ù±‚bmia2Ù±‚`a Ù±‚aoa*Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`bpiÙ±‚`a Ù±‚aoa*Ù±‚`a Ù±‚`axÙ±‚`a)Ù±‚`a Ù±‚aoa+Ù±‚`a Ù±‚bmfc0.5Ù±‚`a Ù±‚aoa*Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`frandomÙ±‚aoa.Ù±‚`erandnÙ±‚`a(Ù±‚bnbclenÙ±‚`a(Ù±‚`axÙ±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`cax1Ù±‚aoa.Ù±‚`dplotÙ±‚`a(Ù±‚`axÙ±‚`a,Ù±‚`a Ù±‚`ayÙ±‚`a)Ù±‚`a
Ù±‚`cax1Ù±‚aoa.Ù±‚`hset_ylimÙ±‚`a(Ù±‚aoa-Ù±‚bmia2Ù±‚`a,Ù±‚`a Ù±‚bmia2Ù±‚`a)Ù±‚`a
Ù±‚`cax1Ù±‚aoa.Ù±‚`iset_titleÙ±‚`a(Ù±‚bs1a'Ù±‚bs1x!Press left mouse button and drag Ù±‚bs1a'Ù±‚`a
Ù±‚`n              Ù±‚bs1a'Ù±‚bs1x#to select a region in the top graphÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`eline2Ù±‚`a,Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cax2Ù±‚aoa.Ù±‚`dplotÙ±‚`a(Ù±‚`a[Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`a[Ù±‚`a]Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚akcdefÙ±‚`a Ù±‚bnfhonselectÙ±‚`a(Ù±‚`dxminÙ±‚`a,Ù±‚`a Ù±‚`dxmaxÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`d    Ù±‚`findminÙ±‚`a,Ù±‚`a Ù±‚`findmaxÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`lsearchsortedÙ±‚`a(Ù±‚`axÙ±‚`a,Ù±‚`a Ù±‚`a(Ù±‚`dxminÙ±‚`a,Ù±‚`a Ù±‚`dxmaxÙ±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`findmaxÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bnbcminÙ±‚`a(Ù±‚bnbclenÙ±‚`a(Ù±‚`axÙ±‚`a)Ù±‚`a Ù±‚aoa-Ù±‚`a Ù±‚bmia1Ù±‚`a,Ù±‚`a Ù±‚`findmaxÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚`hregion_xÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`axÙ±‚`a[Ù±‚`findminÙ±‚`a:Ù±‚`findmaxÙ±‚`a]Ù±‚`a
Ù±‚`d    Ù±‚`hregion_yÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`ayÙ±‚`a[Ù±‚`findminÙ±‚`a:Ù±‚`findmaxÙ±‚`a]Ù±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚akbifÙ±‚`a Ù±‚bnbclenÙ±‚`a(Ù±‚`hregion_xÙ±‚`a)Ù±‚`a Ù±‚aoa>Ù±‚aoa=Ù±‚`a Ù±‚bmia2Ù±‚`a:Ù±‚`a
Ù±‚`h        Ù±‚`eline2Ù±‚aoa.Ù±‚`hset_dataÙ±‚`a(Ù±‚`hregion_xÙ±‚`a,Ù±‚`a Ù±‚`hregion_yÙ±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚`cax2Ù±‚aoa.Ù±‚`hset_xlimÙ±‚`a(Ù±‚`hregion_xÙ±‚`a[Ù±‚bmia0Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`hregion_xÙ±‚`a[Ù±‚aoa-Ù±‚bmia1Ù±‚`a]Ù±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚`cax2Ù±‚aoa.Ù±‚`hset_ylimÙ±‚`a(Ù±‚`hregion_yÙ±‚aoa.Ù±‚`cminÙ±‚`a(Ù±‚`a)Ù±‚`a,Ù±‚`a Ù±‚`hregion_yÙ±‚aoa.Ù±‚`cmaxÙ±‚`a(Ù±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚`cfigÙ±‚aoa.Ù±‚`fcanvasÙ±‚aoa.Ù±‚`idraw_idleÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚bc1xM#############################################################################Ù±‚`a
Ù±‚bc1k# .. note::Ù±‚`a
Ù±‚bc1a#Ù±‚`a
Ù±‚bc1xF#    If the SpanSelector object is garbage collected you will lose theÙ±‚`a
Ù±‚bc1xJ#    interactivity.  You must keep a hard reference to it to prevent this.Ù±‚`a
Ù±‚bc1a#Ù±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚`dspanÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`lSpanSelectorÙ±‚`a(Ù±‚`a
Ù±‚`d    Ù±‚`cax1Ù±‚`a,Ù±‚`a
Ù±‚`d    Ù±‚`honselectÙ±‚`a,Ù±‚`a
Ù±‚`d    Ù±‚bs2a"Ù±‚bs2jhorizontalÙ±‚bs2a"Ù±‚`a,Ù±‚`a
Ù±‚`d    Ù±‚`guseblitÙ±‚aoa=Ù±‚bkcdTrueÙ±‚`a,Ù±‚`a
Ù±‚`d    Ù±‚`epropsÙ±‚aoa=Ù±‚bnbddictÙ±‚`a(Ù±‚`ealphaÙ±‚aoa=Ù±‚bmfc0.5Ù±‚`a,Ù±‚`a Ù±‚`ifacecolorÙ±‚aoa=Ù±‚bs2a"Ù±‚bs2htab:blueÙ±‚bs2a"Ù±‚`a)Ù±‚`a,Ù±‚`a
Ù±‚`d    Ù±‚`kinteractiveÙ±‚aoa=Ù±‚bkcdTrueÙ±‚`a,Ù±‚`a
Ù±‚`d    Ù±‚`rdrag_from_anywhereÙ±‚aoa=Ù±‚bkcdTrueÙ±‚`a
Ù±‚`a)Ù±‚`a
Ù±‚bc1x=# Set useblit=True on most backends for enhanced performance.Ù±‚`a
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
Ù±‚bc1x(#    - `matplotlib.widgets.SpanSelector`Ù±‚`a
`dNoneö