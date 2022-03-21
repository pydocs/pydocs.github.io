Ù¯‚Ù´ƒ™‘Ù±‚bsdy'"""
================
Anchored Artists
================

This example illustrates the use of the anchored objects without the
helper classes found in :mod:`mpl_toolkits.axes_grid1`. This version
of the figure is similar to the one found in
:doc:`/gallery/axes_grid1/simple_anchored_artists`, but it is
implemented using only the matplotlib namespace, without the help
of additional toolkits.

.. redirect-from:: /gallery/userdemo/anchored_box01
.. redirect-from:: /gallery/userdemo/anchored_box02
.. redirect-from:: /gallery/userdemo/anchored_box03
"""Ù±‚`a
Ù±‚`a
Ù±‚bkndfromÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚`a Ù±‚bknfimportÙ±‚`a Ù±‚`fpyplotÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚`cpltÙ±‚`a
Ù±‚bkndfromÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnnelinesÙ±‚`a Ù±‚bknfimportÙ±‚`a Ù±‚`fLine2DÙ±‚`a
Ù±‚bkndfromÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnngpatchesÙ±‚`a Ù±‚bknfimportÙ±‚`a Ù±‚`fCircleÙ±‚`a,Ù±‚`a Ù±‚`gEllipseÙ±‚`a
Ù±‚bkndfromÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnnioffsetboxÙ±‚`a Ù±‚bknfimportÙ±‚`a Ù±‚`a(Ù±‚`a
Ù±‚`d    Ù±‚`qAnchoredOffsetboxÙ±‚`a,Ù±‚`a Ù±‚`oAuxTransformBoxÙ±‚`a,Ù±‚`a Ù±‚`kDrawingAreaÙ±‚`a,Ù±‚`a Ù±‚`hTextAreaÙ±‚`a,Ù±‚`a Ù±‚`gVPackerÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚akcdefÙ±‚`a Ù±‚bnfidraw_textÙ±‚`a(Ù±‚`baxÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`d    Ù±‚bsdxF"""Draw a text-box anchored to the upper-left corner of the figure."""Ù±‚`a
Ù±‚`d    Ù±‚`cboxÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`qAnchoredOffsetboxÙ±‚`a(Ù±‚`echildÙ±‚aoa=Ù±‚`hTextAreaÙ±‚`a(Ù±‚bs2a"Ù±‚bs2iFigure 1aÙ±‚bs2a"Ù±‚`a)Ù±‚`a,Ù±‚`a
Ù±‚`x                            Ù±‚`clocÙ±‚aoa=Ù±‚bs2a"Ù±‚bs2jupper leftÙ±‚bs2a"Ù±‚`a,Ù±‚`a Ù±‚`gframeonÙ±‚aoa=Ù±‚bkcdTrueÙ±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`cboxÙ±‚aoa.Ù±‚`epatchÙ±‚aoa.Ù±‚`lset_boxstyleÙ±‚`a(Ù±‚bs2a"Ù±‚bs2xround,pad=0.,rounding_size=0.2Ù±‚bs2a"Ù±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`baxÙ±‚aoa.Ù±‚`jadd_artistÙ±‚`a(Ù±‚`cboxÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚akcdefÙ±‚`a Ù±‚bnfldraw_circlesÙ±‚`a(Ù±‚`baxÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`d    Ù±‚bsdx'"""Draw circles in axes coordinates."""Ù±‚`a
Ù±‚`d    Ù±‚`dareaÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`kDrawingAreaÙ±‚`a(Ù±‚bmib40Ù±‚`a,Ù±‚`a Ù±‚bmib20Ù±‚`a,Ù±‚`a Ù±‚bmia0Ù±‚`a,Ù±‚`a Ù±‚bmia0Ù±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`dareaÙ±‚aoa.Ù±‚`jadd_artistÙ±‚`a(Ù±‚`fCircleÙ±‚`a(Ù±‚`a(Ù±‚bmib10Ù±‚`a,Ù±‚`a Ù±‚bmib10Ù±‚`a)Ù±‚`a,Ù±‚`a Ù±‚bmib10Ù±‚`a,Ù±‚`a Ù±‚`bfcÙ±‚aoa=Ù±‚bs2a"Ù±‚bs2htab:blueÙ±‚bs2a"Ù±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`dareaÙ±‚aoa.Ù±‚`jadd_artistÙ±‚`a(Ù±‚`fCircleÙ±‚`a(Ù±‚`a(Ù±‚bmib30Ù±‚`a,Ù±‚`a Ù±‚bmib10Ù±‚`a)Ù±‚`a,Ù±‚`a Ù±‚bmia5Ù±‚`a,Ù±‚`a Ù±‚`bfcÙ±‚aoa=Ù±‚bs2a"Ù±‚bs2gtab:redÙ±‚bs2a"Ù±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`cboxÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`qAnchoredOffsetboxÙ±‚`a(Ù±‚`a
Ù±‚`h        Ù±‚`echildÙ±‚aoa=Ù±‚`dareaÙ±‚`a,Ù±‚`a Ù±‚`clocÙ±‚aoa=Ù±‚bs2a"Ù±‚bs2kupper rightÙ±‚bs2a"Ù±‚`a,Ù±‚`a Ù±‚`cpadÙ±‚aoa=Ù±‚bmia0Ù±‚`a,Ù±‚`a Ù±‚`gframeonÙ±‚aoa=Ù±‚bkceFalseÙ±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`baxÙ±‚aoa.Ù±‚`jadd_artistÙ±‚`a(Ù±‚`cboxÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚akcdefÙ±‚`a Ù±‚bnfldraw_ellipseÙ±‚`a(Ù±‚`baxÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`d    Ù±‚bsdxD"""Draw an ellipse of width=0.1, height=0.15 in data coordinates."""Ù±‚`a
Ù±‚`d    Ù±‚`jaux_tr_boxÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`oAuxTransformBoxÙ±‚`a(Ù±‚`baxÙ±‚aoa.Ù±‚`itransDataÙ±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`jaux_tr_boxÙ±‚aoa.Ù±‚`jadd_artistÙ±‚`a(Ù±‚`gEllipseÙ±‚`a(Ù±‚`a(Ù±‚bmia0Ù±‚`a,Ù±‚`a Ù±‚bmia0Ù±‚`a)Ù±‚`a,Ù±‚`a Ù±‚`ewidthÙ±‚aoa=Ù±‚bmfc0.1Ù±‚`a,Ù±‚`a Ù±‚`fheightÙ±‚aoa=Ù±‚bmfd0.15Ù±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`cboxÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`qAnchoredOffsetboxÙ±‚`a(Ù±‚`echildÙ±‚aoa=Ù±‚`jaux_tr_boxÙ±‚`a,Ù±‚`a Ù±‚`clocÙ±‚aoa=Ù±‚bs2a"Ù±‚bs2jlower leftÙ±‚bs2a"Ù±‚`a,Ù±‚`a Ù±‚`gframeonÙ±‚aoa=Ù±‚bkcdTrueÙ±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`baxÙ±‚aoa.Ù±‚`jadd_artistÙ±‚`a(Ù±‚`cboxÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚akeclassÙ±‚`a Ù±‚bncoAnchoredSizeBarÙ±‚`a(Ù±‚`qAnchoredOffsetboxÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`d    Ù±‚akcdefÙ±‚`a Ù±‚bfmh__init__Ù±‚`a(Ù±‚bbpdselfÙ±‚`a,Ù±‚`a Ù±‚`itransformÙ±‚`a,Ù±‚`a Ù±‚`dsizeÙ±‚`a,Ù±‚`a Ù±‚`elabelÙ±‚`a,Ù±‚`a Ù±‚`clocÙ±‚`a,Ù±‚`a
Ù±‚`q                 Ù±‚`cpadÙ±‚aoa=Ù±‚bmfc0.1Ù±‚`a,Ù±‚`a Ù±‚`iborderpadÙ±‚aoa=Ù±‚bmfc0.1Ù±‚`a,Ù±‚`a Ù±‚`csepÙ±‚aoa=Ù±‚bmia2Ù±‚`a,Ù±‚`a Ù±‚`dpropÙ±‚aoa=Ù±‚bkcdNoneÙ±‚`a,Ù±‚`a Ù±‚`gframeonÙ±‚aoa=Ù±‚bkcdTrueÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`h        Ù±‚bsdxù"""
        Draw a horizontal bar with the size in data coordinate of the given
        axes. A label will be drawn underneath (center-aligned).

        pad, borderpad in fraction of the legend font size (or prop)
        sep in points.
        """Ù±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`hsize_barÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`oAuxTransformBoxÙ±‚`a(Ù±‚`itransformÙ±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`hsize_barÙ±‚aoa.Ù±‚`jadd_artistÙ±‚`a(Ù±‚`fLine2DÙ±‚`a(Ù±‚`a[Ù±‚bmia0Ù±‚`a,Ù±‚`a Ù±‚`dsizeÙ±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`a[Ù±‚bmia0Ù±‚`a,Ù±‚`a Ù±‚bmia0Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`ecolorÙ±‚aoa=Ù±‚bs2a"Ù±‚bs2eblackÙ±‚bs2a"Ù±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`itxt_labelÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`hTextAreaÙ±‚`a(Ù±‚`elabelÙ±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`d_boxÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`gVPackerÙ±‚`a(Ù±‚`hchildrenÙ±‚aoa=Ù±‚`a[Ù±‚bbpdselfÙ±‚aoa.Ù±‚`hsize_barÙ±‚`a,Ù±‚`a Ù±‚bbpdselfÙ±‚aoa.Ù±‚`itxt_labelÙ±‚`a]Ù±‚`a,Ù±‚`a
Ù±‚`x                            Ù±‚`ealignÙ±‚aoa=Ù±‚bs2a"Ù±‚bs2fcenterÙ±‚bs2a"Ù±‚`a,Ù±‚`a
Ù±‚`x                            Ù±‚`cpadÙ±‚aoa=Ù±‚bmia0Ù±‚`a,Ù±‚`a Ù±‚`csepÙ±‚aoa=Ù±‚`csepÙ±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚bnbesuperÙ±‚`a(Ù±‚`a)Ù±‚aoa.Ù±‚bfmh__init__Ù±‚`a(Ù±‚`clocÙ±‚`a,Ù±‚`a Ù±‚`cpadÙ±‚aoa=Ù±‚`cpadÙ±‚`a,Ù±‚`a Ù±‚`iborderpadÙ±‚aoa=Ù±‚`iborderpadÙ±‚`a,Ù±‚`a
Ù±‚`x                         Ù±‚`echildÙ±‚aoa=Ù±‚bbpdselfÙ±‚aoa.Ù±‚`d_boxÙ±‚`a,Ù±‚`a Ù±‚`dpropÙ±‚aoa=Ù±‚`dpropÙ±‚`a,Ù±‚`a Ù±‚`gframeonÙ±‚aoa=Ù±‚`gframeonÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚akcdefÙ±‚`a Ù±‚bnfldraw_sizebarÙ±‚`a(Ù±‚`baxÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`d    Ù±‚bsdxp"""
    Draw a horizontal bar with length of 0.1 in data coordinates,
    with a fixed label underneath.
    """Ù±‚`a
Ù±‚`d    Ù±‚`casbÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`oAnchoredSizeBarÙ±‚`a(Ù±‚`baxÙ±‚aoa.Ù±‚`itransDataÙ±‚`a,Ù±‚`a
Ù±‚`x                          Ù±‚bmfc0.1Ù±‚`a,Ù±‚`a
Ù±‚`x                          Ù±‚bsaarÙ±‚bs2a"Ù±‚bs2c1$^Ù±‚bs2a{Ù±‚bs2a\Ù±‚bs2gprime}$Ù±‚bs2a"Ù±‚`a,Ù±‚`a
Ù±‚`x                          Ù±‚`clocÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1llower centerÙ±‚bs1a'Ù±‚`a,Ù±‚`a
Ù±‚`x                          Ù±‚`cpadÙ±‚aoa=Ù±‚bmfc0.1Ù±‚`a,Ù±‚`a Ù±‚`iborderpadÙ±‚aoa=Ù±‚bmfc0.5Ù±‚`a,Ù±‚`a Ù±‚`csepÙ±‚aoa=Ù±‚bmia5Ù±‚`a,Ù±‚`a
Ù±‚`x                          Ù±‚`gframeonÙ±‚aoa=Ù±‚bkceFalseÙ±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`baxÙ±‚aoa.Ù±‚`jadd_artistÙ±‚`a(Ù±‚`casbÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚`cfigÙ±‚`a,Ù±‚`a Ù±‚`baxÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cpltÙ±‚aoa.Ù±‚`hsubplotsÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`jset_aspectÙ±‚`a(Ù±‚bmia1Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`idraw_textÙ±‚`a(Ù±‚`baxÙ±‚`a)Ù±‚`a
Ù±‚`ldraw_circlesÙ±‚`a(Ù±‚`baxÙ±‚`a)Ù±‚`a
Ù±‚`ldraw_ellipseÙ±‚`a(Ù±‚`baxÙ±‚`a)Ù±‚`a
Ù±‚`ldraw_sizebarÙ±‚`a(Ù±‚`baxÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`cpltÙ±‚aoa.Ù±‚`dshowÙ±‚`a(Ù±‚`a)Ù±‚`a
`dNoneö