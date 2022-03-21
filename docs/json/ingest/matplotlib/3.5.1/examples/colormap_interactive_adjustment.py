Ù¯‚Ù´ƒ˜“Ù±‚bsdyJ"""
========================================
Interactive Adjustment of Colormap Range
========================================

Demonstration of how a colorbar can be used to interactively adjust the
range of colormapping on an image. To use the interactive feature, you must
be in either zoom mode (magnifying glass toolbar button) or
pan mode (4-way arrow toolbar button) and click inside the colorbar.

When zooming, the bounding box of the zoom region defines the new vmin and
vmax of the norm. Zooming using the right mouse button will expand the
vmin and vmax proportionally to the selected region, in the same manner that
one can zoom out on an axis. When panning, the vmin and vmax of the norm are
both shifted according to the direction of movement. The
Home/Back/Forward buttons can also be used to get back to a previous state.
"""Ù±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnnfpyplotÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnncpltÙ±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„enumpyÙ „enumpyf1.22.3fmoduleenumpyfmoduleõÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnnbnpÙ±‚`a
Ù±‚`a
Ù±‚`atÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`hlinspaceÙ±‚`a(Ù±‚bmia0Ù±‚`a,Ù±‚`a Ù±‚bmia2Ù±‚`a Ù±‚aoa*Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`bpiÙ±‚`a,Ù±‚`a Ù±‚bmid1024Ù±‚`a)Ù±‚`a
Ù±‚`fdata2dÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`csinÙ±‚`a(Ù±‚`atÙ±‚`a)Ù±‚`a[Ù±‚`a:Ù±‚`a,Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`gnewaxisÙ±‚`a]Ù±‚`a Ù±‚aoa*Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`ccosÙ±‚`a(Ù±‚`atÙ±‚`a)Ù±‚`a[Ù±‚`bnpÙ±‚aoa.Ù±‚`gnewaxisÙ±‚`a,Ù±‚`a Ù±‚`a:Ù±‚`a]Ù±‚`a
Ù±‚`a
Ù±‚`cfigÙ±‚`a,Ù±‚`a Ù±‚`baxÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cpltÙ±‚aoa.Ù±‚`hsubplotsÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`bimÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`baxÙ±‚aoa.Ù±‚`fimshowÙ±‚`a(Ù±‚`fdata2dÙ±‚`a)Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`iset_titleÙ±‚`a(Ù±‚bs1a'Ù±‚bs1x.Pan on the colorbar to shift the color mappingÙ±‚bseb\nÙ±‚bs1a'Ù±‚`a
Ù±‚`m             Ù±‚bs1a'Ù±‚bs1x/Zoom on the colorbar to scale the color mappingÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`cfigÙ±‚aoa.Ù±‚`hcolorbarÙ±‚`a(Ù±‚`bimÙ±‚`a,Ù±‚`a Ù±‚`baxÙ±‚aoa=Ù±‚`baxÙ±‚`a,Ù±‚`a Ù±‚`elabelÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1tInteractive colorbarÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`cpltÙ±‚aoa.Ù±‚`dshowÙ±‚`a(Ù±‚`a)Ù±‚`a
`dNoneö