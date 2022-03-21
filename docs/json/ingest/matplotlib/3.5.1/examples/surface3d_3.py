Ù¯‚Ù´ƒ™9Ù±‚bsdxœ"""
=========================
3D surface (checkerboard)
=========================

Demonstrates plotting a 3D surface colored in a checkerboard pattern.
"""Ù±‚`a
Ù±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnnfpyplotÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnncpltÙ±‚`a
Ù±‚bkndfromÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnnftickerÙ±‚`a Ù±‚bknfimportÙ±‚`a Ù±‚`mLinearLocatorÙ±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„enumpyÙ „enumpyf1.22.3fmoduleenumpyfmoduleõÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnnbnpÙ±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚`baxÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cpltÙ±‚aoa.Ù±‚`ffigureÙ±‚`a(Ù±‚`a)Ù±‚aoa.Ù±‚`kadd_subplotÙ±‚`a(Ù±‚`jprojectionÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1b3dÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚bc1l# Make data.Ù±‚`a
Ù±‚`aXÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`farangeÙ±‚`a(Ù±‚aoa-Ù±‚bmia5Ù±‚`a,Ù±‚`a Ù±‚bmia5Ù±‚`a,Ù±‚`a Ù±‚bmfd0.25Ù±‚`a)Ù±‚`a
Ù±‚`dxlenÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bnbclenÙ±‚`a(Ù±‚`aXÙ±‚`a)Ù±‚`a
Ù±‚`aYÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`farangeÙ±‚`a(Ù±‚aoa-Ù±‚bmia5Ù±‚`a,Ù±‚`a Ù±‚bmia5Ù±‚`a,Ù±‚`a Ù±‚bmfd0.25Ù±‚`a)Ù±‚`a
Ù±‚`dylenÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bnbclenÙ±‚`a(Ù±‚`aYÙ±‚`a)Ù±‚`a
Ù±‚`aXÙ±‚`a,Ù±‚`a Ù±‚`aYÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`hmeshgridÙ±‚`a(Ù±‚`aXÙ±‚`a,Ù±‚`a Ù±‚`aYÙ±‚`a)Ù±‚`a
Ù±‚`aRÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`dsqrtÙ±‚`a(Ù±‚`aXÙ±‚aoa*Ù±‚aoa*Ù±‚bmia2Ù±‚`a Ù±‚aoa+Ù±‚`a Ù±‚`aYÙ±‚aoa*Ù±‚aoa*Ù±‚bmia2Ù±‚`a)Ù±‚`a
Ù±‚`aZÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`csinÙ±‚`a(Ù±‚`aRÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚bc1xK# Create an empty array of strings with the same shape as the meshgrid, andÙ±‚`a
Ù±‚bc1x8# populate it with two colors in a checkerboard pattern.Ù±‚`a
Ù±‚`jcolortupleÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`a(Ù±‚bs1a'Ù±‚bs1ayÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚bs1a'Ù±‚bs1abÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`fcolorsÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`eemptyÙ±‚`a(Ù±‚`aXÙ±‚aoa.Ù±‚`eshapeÙ±‚`a,Ù±‚`a Ù±‚`edtypeÙ±‚aoa=Ù±‚bnbcstrÙ±‚`a)Ù±‚`a
Ù±‚akcforÙ±‚`a Ù±‚`ayÙ±‚`a Ù±‚bowbinÙ±‚`a Ù±‚bnberangeÙ±‚`a(Ù±‚`dylenÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`d    Ù±‚akcforÙ±‚`a Ù±‚`axÙ±‚`a Ù±‚bowbinÙ±‚`a Ù±‚bnberangeÙ±‚`a(Ù±‚`dxlenÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`h        Ù±‚`fcolorsÙ±‚`a[Ù±‚`ayÙ±‚`a,Ù±‚`a Ù±‚`axÙ±‚`a]Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`jcolortupleÙ±‚`a[Ù±‚`a(Ù±‚`axÙ±‚`a Ù±‚aoa+Ù±‚`a Ù±‚`ayÙ±‚`a)Ù±‚`a Ù±‚aoa%Ù±‚`a Ù±‚bnbclenÙ±‚`a(Ù±‚`jcolortupleÙ±‚`a)Ù±‚`a]Ù±‚`a
Ù±‚`a
Ù±‚bc1xA# Plot the surface with face colors taken from the array we made.Ù±‚`a
Ù±‚`dsurfÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`baxÙ±‚aoa.Ù±‚`lplot_surfaceÙ±‚`a(Ù±‚`aXÙ±‚`a,Ù±‚`a Ù±‚`aYÙ±‚`a,Ù±‚`a Ù±‚`aZÙ±‚`a,Ù±‚`a Ù±‚`jfacecolorsÙ±‚aoa=Ù±‚`fcolorsÙ±‚`a,Ù±‚`a Ù±‚`ilinewidthÙ±‚aoa=Ù±‚bmia0Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚bc1w# Customize the z axis.Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`hset_zlimÙ±‚`a(Ù±‚aoa-Ù±‚bmia1Ù±‚`a,Ù±‚`a Ù±‚bmia1Ù±‚`a)Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`ezaxisÙ±‚aoa.Ù±‚`qset_major_locatorÙ±‚`a(Ù±‚`mLinearLocatorÙ±‚`a(Ù±‚bmia6Ù±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`cpltÙ±‚aoa.Ù±‚`dshowÙ±‚`a(Ù±‚`a)Ù±‚`a
`dNoneö