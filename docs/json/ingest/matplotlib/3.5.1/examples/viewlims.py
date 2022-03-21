Ù¯‚Ù´ƒ™TÙ±‚bsdx¦"""
========
Viewlims
========

Creates two identical panels.  Zooming in on the right panel will show
a rectangle in the first panel, denoting the zoomed region.
"""Ù±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„enumpyÙ „enumpyf1.22.3fmoduleenumpyfmoduleõÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnnbnpÙ±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnnfpyplotÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnncpltÙ±‚`a
Ù±‚bkndfromÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnngpatchesÙ±‚`a Ù±‚bknfimportÙ±‚`a Ù±‚`iRectangleÙ±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚bc1xB# We just subclass Rectangle so that it can be called with an AxesÙ±‚`a
Ù±‚bc1xB# instance, causing the rectangle to update its shape to match theÙ±‚`a
Ù±‚bc1t# bounds of the AxesÙ±‚`a
Ù±‚akeclassÙ±‚`a Ù±‚bnclUpdatingRectÙ±‚`a(Ù±‚`iRectangleÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`d    Ù±‚akcdefÙ±‚`a Ù±‚bfmh__call__Ù±‚`a(Ù±‚bbpdselfÙ±‚`a,Ù±‚`a Ù±‚`baxÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`jset_boundsÙ±‚`a(Ù±‚aoa*Ù±‚`baxÙ±‚aoa.Ù±‚`gviewLimÙ±‚aoa.Ù±‚`fboundsÙ±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚`baxÙ±‚aoa.Ù±‚`ffigureÙ±‚aoa.Ù±‚`fcanvasÙ±‚aoa.Ù±‚`idraw_idleÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚bc1xG# A class that will regenerate a fractal set as we zoom in, so that youÙ±‚`a
Ù±‚bc1xL# can actually see the increasing detail.  A box in the left panel will showÙ±‚`a
Ù±‚bc1x"# the area to which we are zoomed.Ù±‚`a
Ù±‚akeclassÙ±‚`a Ù±‚bncqMandelbrotDisplayÙ±‚`a:Ù±‚`a
Ù±‚`d    Ù±‚akcdefÙ±‚`a Ù±‚bfmh__init__Ù±‚`a(Ù±‚bbpdselfÙ±‚`a,Ù±‚`a Ù±‚`ahÙ±‚aoa=Ù±‚bmic500Ù±‚`a,Ù±‚`a Ù±‚`awÙ±‚aoa=Ù±‚bmic500Ù±‚`a,Ù±‚`a Ù±‚`eniterÙ±‚aoa=Ù±‚bmib50Ù±‚`a,Ù±‚`a Ù±‚`fradiusÙ±‚aoa=Ù±‚bmfb2.Ù±‚`a,Ù±‚`a Ù±‚`epowerÙ±‚aoa=Ù±‚bmia2Ù±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`fheightÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`ahÙ±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`ewidthÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`awÙ±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`eniterÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`eniterÙ±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`fradiusÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`fradiusÙ±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`epowerÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`epowerÙ±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚akcdefÙ±‚`a Ù±‚bnfmcompute_imageÙ±‚`a(Ù±‚bbpdselfÙ±‚`a,Ù±‚`a Ù±‚`fxstartÙ±‚`a,Ù±‚`a Ù±‚`dxendÙ±‚`a,Ù±‚`a Ù±‚`fystartÙ±‚`a,Ù±‚`a Ù±‚`dyendÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`axÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`hlinspaceÙ±‚`a(Ù±‚`fxstartÙ±‚`a,Ù±‚`a Ù±‚`dxendÙ±‚`a,Ù±‚`a Ù±‚bbpdselfÙ±‚aoa.Ù±‚`ewidthÙ±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`ayÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`hlinspaceÙ±‚`a(Ù±‚`fystartÙ±‚`a,Ù±‚`a Ù±‚`dyendÙ±‚`a,Ù±‚`a Ù±‚bbpdselfÙ±‚aoa.Ù±‚`fheightÙ±‚`a)Ù±‚aoa.Ù±‚`greshapeÙ±‚`a(Ù±‚aoa-Ù±‚bmia1Ù±‚`a,Ù±‚`a Ù±‚bmia1Ù±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚`acÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bbpdselfÙ±‚aoa.Ù±‚`axÙ±‚`a Ù±‚aoa+Ù±‚`a Ù±‚bmfc1.0Ù±‚`ajÙ±‚`a Ù±‚aoa*Ù±‚`a Ù±‚bbpdselfÙ±‚aoa.Ù±‚`ayÙ±‚`a
Ù±‚`h        Ù±‚`nthreshold_timeÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`ezerosÙ±‚`a(Ù±‚`a(Ù±‚bbpdselfÙ±‚aoa.Ù±‚`fheightÙ±‚`a,Ù±‚`a Ù±‚bbpdselfÙ±‚aoa.Ù±‚`ewidthÙ±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚`azÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`ezerosÙ±‚`a(Ù±‚`nthreshold_timeÙ±‚aoa.Ù±‚`eshapeÙ±‚`a,Ù±‚`a Ù±‚`edtypeÙ±‚aoa=Ù±‚bnbgcomplexÙ±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚`dmaskÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`donesÙ±‚`a(Ù±‚`nthreshold_timeÙ±‚aoa.Ù±‚`eshapeÙ±‚`a,Ù±‚`a Ù±‚`edtypeÙ±‚aoa=Ù±‚bnbdboolÙ±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚akcforÙ±‚`a Ù±‚`aiÙ±‚`a Ù±‚bowbinÙ±‚`a Ù±‚bnberangeÙ±‚`a(Ù±‚bbpdselfÙ±‚aoa.Ù±‚`eniterÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`l            Ù±‚`azÙ±‚`a[Ù±‚`dmaskÙ±‚`a]Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`azÙ±‚`a[Ù±‚`dmaskÙ±‚`a]Ù±‚aoa*Ù±‚aoa*Ù±‚bbpdselfÙ±‚aoa.Ù±‚`epowerÙ±‚`a Ù±‚aoa+Ù±‚`a Ù±‚`acÙ±‚`a[Ù±‚`dmaskÙ±‚`a]Ù±‚`a
Ù±‚`l            Ù±‚`dmaskÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`a(Ù±‚`bnpÙ±‚aoa.Ù±‚`cabsÙ±‚`a(Ù±‚`azÙ±‚`a)Ù±‚`a Ù±‚aoa<Ù±‚`a Ù±‚bbpdselfÙ±‚aoa.Ù±‚`fradiusÙ±‚`a)Ù±‚`a
Ù±‚`l            Ù±‚`nthreshold_timeÙ±‚`a Ù±‚aoa+Ù±‚aoa=Ù±‚`a Ù±‚`dmaskÙ±‚`a
Ù±‚`h        Ù±‚akfreturnÙ±‚`a Ù±‚`nthreshold_timeÙ±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚akcdefÙ±‚`a Ù±‚bnfiax_updateÙ±‚`a(Ù±‚bbpdselfÙ±‚`a,Ù±‚`a Ù±‚`baxÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`h        Ù±‚`baxÙ±‚aoa.Ù±‚`pset_autoscale_onÙ±‚`a(Ù±‚bkceFalseÙ±‚`a)Ù±‚`b  Ù±‚bc1x# Otherwise, infinite loopÙ±‚`a
Ù±‚`h        Ù±‚bc1xB# Get the number of points from the number of pixels in the windowÙ±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`ewidthÙ±‚`a,Ù±‚`a Ù±‚bbpdselfÙ±‚aoa.Ù±‚`fheightÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`b\
Ù±‚`l            Ù±‚`bnpÙ±‚aoa.Ù±‚`eroundÙ±‚`a(Ù±‚`baxÙ±‚aoa.Ù±‚`epatchÙ±‚aoa.Ù±‚`qget_window_extentÙ±‚`a(Ù±‚`a)Ù±‚aoa.Ù±‚`dsizeÙ±‚`a)Ù±‚aoa.Ù±‚`fastypeÙ±‚`a(Ù±‚bnbcintÙ±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚bc1x # Get the range for the new areaÙ±‚`a
Ù±‚`h        Ù±‚`bvlÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`baxÙ±‚aoa.Ù±‚`gviewLimÙ±‚`a
Ù±‚`h        Ù±‚`fextentÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bvlÙ±‚aoa.Ù±‚`bx0Ù±‚`a,Ù±‚`a Ù±‚`bvlÙ±‚aoa.Ù±‚`bx1Ù±‚`a,Ù±‚`a Ù±‚`bvlÙ±‚aoa.Ù±‚`by0Ù±‚`a,Ù±‚`a Ù±‚`bvlÙ±‚aoa.Ù±‚`by1Ù±‚`a
Ù±‚`h        Ù±‚bc1x6# Update the image object with our new data and extentÙ±‚`a
Ù±‚`h        Ù±‚`bimÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`baxÙ±‚aoa.Ù±‚`fimagesÙ±‚`a[Ù±‚aoa-Ù±‚bmia1Ù±‚`a]Ù±‚`a
Ù±‚`h        Ù±‚`bimÙ±‚aoa.Ù±‚`hset_dataÙ±‚`a(Ù±‚bbpdselfÙ±‚aoa.Ù±‚`mcompute_imageÙ±‚`a(Ù±‚aoa*Ù±‚`fextentÙ±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚`bimÙ±‚aoa.Ù±‚`jset_extentÙ±‚`a(Ù±‚`fextentÙ±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚`baxÙ±‚aoa.Ù±‚`ffigureÙ±‚aoa.Ù±‚`fcanvasÙ±‚aoa.Ù±‚`idraw_idleÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚`bmdÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`qMandelbrotDisplayÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`aZÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bmdÙ±‚aoa.Ù±‚`mcompute_imageÙ±‚`a(Ù±‚aoa-Ù±‚bmfb2.Ù±‚`a,Ù±‚`a Ù±‚bmfc0.5Ù±‚`a,Ù±‚`a Ù±‚aoa-Ù±‚bmfd1.25Ù±‚`a,Ù±‚`a Ù±‚bmfd1.25Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`dfig1Ù±‚`a,Ù±‚`a Ù±‚`a(Ù±‚`cax1Ù±‚`a,Ù±‚`a Ù±‚`cax2Ù±‚`a)Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cpltÙ±‚aoa.Ù±‚`hsubplotsÙ±‚`a(Ù±‚bmia1Ù±‚`a,Ù±‚`a Ù±‚bmia2Ù±‚`a)Ù±‚`a
Ù±‚`cax1Ù±‚aoa.Ù±‚`fimshowÙ±‚`a(Ù±‚`aZÙ±‚`a,Ù±‚`a Ù±‚`foriginÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1elowerÙ±‚bs1a'Ù±‚`a,Ù±‚`a
Ù±‚`k           Ù±‚`fextentÙ±‚aoa=Ù±‚`a(Ù±‚`bmdÙ±‚aoa.Ù±‚`axÙ±‚aoa.Ù±‚`cminÙ±‚`a(Ù±‚`a)Ù±‚`a,Ù±‚`a Ù±‚`bmdÙ±‚aoa.Ù±‚`axÙ±‚aoa.Ù±‚`cmaxÙ±‚`a(Ù±‚`a)Ù±‚`a,Ù±‚`a Ù±‚`bmdÙ±‚aoa.Ù±‚`ayÙ±‚aoa.Ù±‚`cminÙ±‚`a(Ù±‚`a)Ù±‚`a,Ù±‚`a Ù±‚`bmdÙ±‚aoa.Ù±‚`ayÙ±‚aoa.Ù±‚`cmaxÙ±‚`a(Ù±‚`a)Ù±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`cax2Ù±‚aoa.Ù±‚`fimshowÙ±‚`a(Ù±‚`aZÙ±‚`a,Ù±‚`a Ù±‚`foriginÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1elowerÙ±‚bs1a'Ù±‚`a,Ù±‚`a
Ù±‚`k           Ù±‚`fextentÙ±‚aoa=Ù±‚`a(Ù±‚`bmdÙ±‚aoa.Ù±‚`axÙ±‚aoa.Ù±‚`cminÙ±‚`a(Ù±‚`a)Ù±‚`a,Ù±‚`a Ù±‚`bmdÙ±‚aoa.Ù±‚`axÙ±‚aoa.Ù±‚`cmaxÙ±‚`a(Ù±‚`a)Ù±‚`a,Ù±‚`a Ù±‚`bmdÙ±‚aoa.Ù±‚`ayÙ±‚aoa.Ù±‚`cminÙ±‚`a(Ù±‚`a)Ù±‚`a,Ù±‚`a Ù±‚`bmdÙ±‚aoa.Ù±‚`ayÙ±‚aoa.Ù±‚`cmaxÙ±‚`a(Ù±‚`a)Ù±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`drectÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`lUpdatingRectÙ±‚`a(Ù±‚`a
Ù±‚`d    Ù±‚`a[Ù±‚bmia0Ù±‚`a,Ù±‚`a Ù±‚bmia0Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚bmia0Ù±‚`a,Ù±‚`a Ù±‚bmia0Ù±‚`a,Ù±‚`a Ù±‚`ifacecolorÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1dnoneÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`iedgecolorÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1eblackÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`ilinewidthÙ±‚aoa=Ù±‚bmfc1.0Ù±‚`a)Ù±‚`a
Ù±‚`drectÙ±‚aoa.Ù±‚`jset_boundsÙ±‚`a(Ù±‚aoa*Ù±‚`cax2Ù±‚aoa.Ù±‚`gviewLimÙ±‚aoa.Ù±‚`fboundsÙ±‚`a)Ù±‚`a
Ù±‚`cax1Ù±‚aoa.Ù±‚`iadd_patchÙ±‚`a(Ù±‚`drectÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚bc1x&# Connect for changing the view limitsÙ±‚`a
Ù±‚`cax2Ù±‚aoa.Ù±‚`icallbacksÙ±‚aoa.Ù±‚`gconnectÙ±‚`a(Ù±‚bs1a'Ù±‚bs1lxlim_changedÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`drectÙ±‚`a)Ù±‚`a
Ù±‚`cax2Ù±‚aoa.Ù±‚`icallbacksÙ±‚aoa.Ù±‚`gconnectÙ±‚`a(Ù±‚bs1a'Ù±‚bs1lylim_changedÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`drectÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`cax2Ù±‚aoa.Ù±‚`icallbacksÙ±‚aoa.Ù±‚`gconnectÙ±‚`a(Ù±‚bs1a'Ù±‚bs1lxlim_changedÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`bmdÙ±‚aoa.Ù±‚`iax_updateÙ±‚`a)Ù±‚`a
Ù±‚`cax2Ù±‚aoa.Ù±‚`icallbacksÙ±‚aoa.Ù±‚`gconnectÙ±‚`a(Ù±‚bs1a'Ù±‚bs1lylim_changedÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`bmdÙ±‚aoa.Ù±‚`iax_updateÙ±‚`a)Ù±‚`a
Ù±‚`cax2Ù±‚aoa.Ù±‚`iset_titleÙ±‚`a(Ù±‚bs2a"Ù±‚bs2iZoom hereÙ±‚bs2a"Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`cpltÙ±‚aoa.Ù±‚`dshowÙ±‚`a(Ù±‚`a)Ù±‚`a
`dNoneö