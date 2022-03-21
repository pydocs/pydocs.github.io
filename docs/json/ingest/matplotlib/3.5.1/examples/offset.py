Ù¯‚Ù´ƒ˜¾Ù±‚bsdyÃ"""
=========================
Automatic Text Offsetting
=========================

This example demonstrates mplot3d's offset text display.
As one rotates the 3D figure, the offsets should remain oriented the
same way as the axis label, and should also be located "away"
from the center of the plot.

This demo triggers the display of the offset text for the x and
y axis by adding 1e5 to X and Y. Anything less would not
automatically trigger it.
"""Ù±‚`a
Ù±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnnfpyplotÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnncpltÙ±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„enumpyÙ „enumpyf1.22.3fmoduleenumpyfmoduleõÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnnbnpÙ±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚`baxÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cpltÙ±‚aoa.Ù±‚`ffigureÙ±‚`a(Ù±‚`a)Ù±‚aoa.Ù±‚`kadd_subplotÙ±‚`a(Ù±‚`jprojectionÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1b3dÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`aXÙ±‚`a,Ù±‚`a Ù±‚`aYÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`emgridÙ±‚`a[Ù±‚bmia0Ù±‚`a:Ù±‚bmia6Ù±‚aoa*Ù±‚`bnpÙ±‚aoa.Ù±‚`bpiÙ±‚`a:Ù±‚bmfd0.25Ù±‚`a,Ù±‚`a Ù±‚bmia0Ù±‚`a:Ù±‚bmia4Ù±‚aoa*Ù±‚`bnpÙ±‚aoa.Ù±‚`bpiÙ±‚`a:Ù±‚bmfd0.25Ù±‚`a]Ù±‚`a
Ù±‚`aZÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`dsqrtÙ±‚`a(Ù±‚`bnpÙ±‚aoa.Ù±‚`cabsÙ±‚`a(Ù±‚`bnpÙ±‚aoa.Ù±‚`ccosÙ±‚`a(Ù±‚`aXÙ±‚`a)Ù±‚`a Ù±‚aoa+Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`ccosÙ±‚`a(Ù±‚`aYÙ±‚`a)Ù±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`lplot_surfaceÙ±‚`a(Ù±‚`aXÙ±‚`a Ù±‚aoa+Ù±‚`a Ù±‚bmfc1e5Ù±‚`a,Ù±‚`a Ù±‚`aYÙ±‚`a Ù±‚aoa+Ù±‚`a Ù±‚bmfc1e5Ù±‚`a,Ù±‚`a Ù±‚`aZÙ±‚`a,Ù±‚`a Ù±‚`dcmapÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1fautumnÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`gcstrideÙ±‚aoa=Ù±‚bmia2Ù±‚`a,Ù±‚`a Ù±‚`grstrideÙ±‚aoa=Ù±‚bmia2Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`jset_xlabelÙ±‚`a(Ù±‚bs2a"Ù±‚bs2gX labelÙ±‚bs2a"Ù±‚`a)Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`jset_ylabelÙ±‚`a(Ù±‚bs2a"Ù±‚bs2gY labelÙ±‚bs2a"Ù±‚`a)Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`jset_zlabelÙ±‚`a(Ù±‚bs2a"Ù±‚bs2gZ labelÙ±‚bs2a"Ù±‚`a)Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`hset_zlimÙ±‚`a(Ù±‚bmia0Ù±‚`a,Ù±‚`a Ù±‚bmia2Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`cpltÙ±‚aoa.Ù±‚`dshowÙ±‚`a(Ù±‚`a)Ù±‚`a
`dNoneö