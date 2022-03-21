Ù¯‚Ù´ƒ™ÞÙ±‚bsdy™"""
==============================================
Contouring the solution space of optimizations
==============================================

Contour plotting is particularly handy when illustrating the solution
space of optimization problems.  Not only can `.axes.Axes.contour` be
used to represent the topography of the objective function, it can be
used to generate boundary curves of the constraint functions.  The
constraint lines can be drawn with
`~matplotlib.patheffects.TickedStroke` to distinguish the valid and
invalid sides of the constraint boundaries.

`.axes.Axes.contour` generates curves with larger values to the left
of the contour.  The angle parameter is measured zero ahead with
increasing values to the left.  Consequently, when using
`~matplotlib.patheffects.TickedStroke` to illustrate a constraint in
a typical optimization problem, the angle should be set between
zero and 180 degrees.

"""Ù±‚`a
Ù±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„enumpyÙ „enumpyf1.22.3fmoduleenumpyfmoduleõÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnnbnpÙ±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnnfpyplotÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnncpltÙ±‚`a
Ù±‚bkndfromÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚`a Ù±‚bknfimportÙ±‚`a Ù±‚`kpatheffectsÙ±‚`a
Ù±‚`a
Ù±‚`cfigÙ±‚`a,Ù±‚`a Ù±‚`baxÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cpltÙ±‚aoa.Ù±‚`hsubplotsÙ±‚`a(Ù±‚`gfigsizeÙ±‚aoa=Ù±‚`a(Ù±‚bmia6Ù±‚`a,Ù±‚`a Ù±‚bmia6Ù±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`bnxÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bmic101Ù±‚`a
Ù±‚`bnyÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bmic105Ù±‚`a
Ù±‚`a
Ù±‚bc1w# Set up survey vectorsÙ±‚`a
Ù±‚`dxvecÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`hlinspaceÙ±‚`a(Ù±‚bmfe0.001Ù±‚`a,Ù±‚`a Ù±‚bmfc4.0Ù±‚`a,Ù±‚`a Ù±‚`bnxÙ±‚`a)Ù±‚`a
Ù±‚`dyvecÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`hlinspaceÙ±‚`a(Ù±‚bmfe0.001Ù±‚`a,Ù±‚`a Ù±‚bmfc4.0Ù±‚`a,Ù±‚`a Ù±‚`bnyÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚bc1x># Set up survey matrices.  Design disk loading and gear ratio.Ù±‚`a
Ù±‚`bx1Ù±‚`a,Ù±‚`a Ù±‚`bx2Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`hmeshgridÙ±‚`a(Ù±‚`dxvecÙ±‚`a,Ù±‚`a Ù±‚`dyvecÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚bc1x# Evaluate some stuff to plotÙ±‚`a
Ù±‚`cobjÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bx1Ù±‚aoa*Ù±‚aoa*Ù±‚bmia2Ù±‚`a Ù±‚aoa+Ù±‚`a Ù±‚`bx2Ù±‚aoa*Ù±‚aoa*Ù±‚bmia2Ù±‚`a Ù±‚aoa-Ù±‚`a Ù±‚bmia2Ù±‚aoa*Ù±‚`bx1Ù±‚`a Ù±‚aoa-Ù±‚`a Ù±‚bmia2Ù±‚aoa*Ù±‚`bx2Ù±‚`a Ù±‚aoa+Ù±‚`a Ù±‚bmia2Ù±‚`a
Ù±‚`bg1Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚aoa-Ù±‚`a(Ù±‚bmia3Ù±‚aoa*Ù±‚`bx1Ù±‚`a Ù±‚aoa+Ù±‚`a Ù±‚`bx2Ù±‚`a Ù±‚aoa-Ù±‚`a Ù±‚bmfc5.5Ù±‚`a)Ù±‚`a
Ù±‚`bg2Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚aoa-Ù±‚`a(Ù±‚`bx1Ù±‚`a Ù±‚aoa+Ù±‚`a Ù±‚bmia2Ù±‚aoa*Ù±‚`bx2Ù±‚`a Ù±‚aoa-Ù±‚`a Ù±‚bmfc4.5Ù±‚`a)Ù±‚`a
Ù±‚`bg3Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bmfc0.8Ù±‚`a Ù±‚aoa+Ù±‚`a Ù±‚`bx1Ù±‚aoa*Ù±‚aoa*Ù±‚aoa-Ù±‚bmia3Ù±‚`a Ù±‚aoa-Ù±‚`a Ù±‚`bx2Ù±‚`a
Ù±‚`a
Ù±‚`dcntrÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`baxÙ±‚aoa.Ù±‚`gcontourÙ±‚`a(Ù±‚`bx1Ù±‚`a,Ù±‚`a Ù±‚`bx2Ù±‚`a,Ù±‚`a Ù±‚`cobjÙ±‚`a,Ù±‚`a Ù±‚`a[Ù±‚bmfd0.01Ù±‚`a,Ù±‚`a Ù±‚bmfc0.1Ù±‚`a,Ù±‚`a Ù±‚bmfc0.5Ù±‚`a,Ù±‚`a Ù±‚bmia1Ù±‚`a,Ù±‚`a Ù±‚bmia2Ù±‚`a,Ù±‚`a Ù±‚bmia4Ù±‚`a,Ù±‚`a Ù±‚bmia8Ù±‚`a,Ù±‚`a Ù±‚bmib16Ù±‚`a]Ù±‚`a,Ù±‚`a
Ù±‚`r                  Ù±‚`fcolorsÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1eblackÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`fclabelÙ±‚`a(Ù±‚`dcntrÙ±‚`a,Ù±‚`a Ù±‚`cfmtÙ±‚aoa=Ù±‚bs2a"Ù±‚bsie%2.1fÙ±‚bs2a"Ù±‚`a,Ù±‚`a Ù±‚`nuse_clabeltextÙ±‚aoa=Ù±‚bkcdTrueÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`ccg1Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`baxÙ±‚aoa.Ù±‚`gcontourÙ±‚`a(Ù±‚`bx1Ù±‚`a,Ù±‚`a Ù±‚`bx2Ù±‚`a,Ù±‚`a Ù±‚`bg1Ù±‚`a,Ù±‚`a Ù±‚`a[Ù±‚bmia0Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`fcolorsÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1jsandybrownÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`cpltÙ±‚aoa.Ù±‚`dsetpÙ±‚`a(Ù±‚`ccg1Ù±‚aoa.Ù±‚`kcollectionsÙ±‚`a,Ù±‚`a
Ù±‚`i         Ù±‚`lpath_effectsÙ±‚aoa=Ù±‚`a[Ù±‚`kpatheffectsÙ±‚aoa.Ù±‚`pwithTickedStrokeÙ±‚`a(Ù±‚`eangleÙ±‚aoa=Ù±‚bmic135Ù±‚`a)Ù±‚`a]Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`ccg2Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`baxÙ±‚aoa.Ù±‚`gcontourÙ±‚`a(Ù±‚`bx1Ù±‚`a,Ù±‚`a Ù±‚`bx2Ù±‚`a,Ù±‚`a Ù±‚`bg2Ù±‚`a,Ù±‚`a Ù±‚`a[Ù±‚bmia0Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`fcolorsÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1iorangeredÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`cpltÙ±‚aoa.Ù±‚`dsetpÙ±‚`a(Ù±‚`ccg2Ù±‚aoa.Ù±‚`kcollectionsÙ±‚`a,Ù±‚`a
Ù±‚`i         Ù±‚`lpath_effectsÙ±‚aoa=Ù±‚`a[Ù±‚`kpatheffectsÙ±‚aoa.Ù±‚`pwithTickedStrokeÙ±‚`a(Ù±‚`eangleÙ±‚aoa=Ù±‚bmib60Ù±‚`a,Ù±‚`a Ù±‚`flengthÙ±‚aoa=Ù±‚bmia2Ù±‚`a)Ù±‚`a]Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`ccg3Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`baxÙ±‚aoa.Ù±‚`gcontourÙ±‚`a(Ù±‚`bx1Ù±‚`a,Ù±‚`a Ù±‚`bx2Ù±‚`a,Ù±‚`a Ù±‚`bg3Ù±‚`a,Ù±‚`a Ù±‚`a[Ù±‚bmia0Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`fcolorsÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1jmediumblueÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`cpltÙ±‚aoa.Ù±‚`dsetpÙ±‚`a(Ù±‚`ccg3Ù±‚aoa.Ù±‚`kcollectionsÙ±‚`a,Ù±‚`a
Ù±‚`i         Ù±‚`lpath_effectsÙ±‚aoa=Ù±‚`a[Ù±‚`kpatheffectsÙ±‚aoa.Ù±‚`pwithTickedStrokeÙ±‚`a(Ù±‚`gspacingÙ±‚aoa=Ù±‚bmia7Ù±‚`a)Ù±‚`a]Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`hset_xlimÙ±‚`a(Ù±‚bmia0Ù±‚`a,Ù±‚`a Ù±‚bmia4Ù±‚`a)Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`hset_ylimÙ±‚`a(Ù±‚bmia0Ù±‚`a,Ù±‚`a Ù±‚bmia4Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`cpltÙ±‚aoa.Ù±‚`dshowÙ±‚`a(Ù±‚`a)Ù±‚`a
`dNoneö