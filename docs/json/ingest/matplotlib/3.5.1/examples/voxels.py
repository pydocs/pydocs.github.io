Ù¯‚Ù´ƒ™Ù±‚bsdxœ"""
==========================
3D voxel / volumetric plot
==========================

Demonstrates plotting 3D volumetric objects with `.Axes3D.voxels`.
"""Ù±‚`a
Ù±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnnfpyplotÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnncpltÙ±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„enumpyÙ „enumpyf1.22.3fmoduleenumpyfmoduleõÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnnbnpÙ±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚bc1x# prepare some coordinatesÙ±‚`a
Ù±‚`axÙ±‚`a,Ù±‚`a Ù±‚`ayÙ±‚`a,Ù±‚`a Ù±‚`azÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`gindicesÙ±‚`a(Ù±‚`a(Ù±‚bmia8Ù±‚`a,Ù±‚`a Ù±‚bmia8Ù±‚`a,Ù±‚`a Ù±‚bmia8Ù±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚bc1xK# draw cuboids in the top left and bottom right corners, and a link betweenÙ±‚`a
Ù±‚bc1f# themÙ±‚`a
Ù±‚`ecube1Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`a(Ù±‚`axÙ±‚`a Ù±‚aoa<Ù±‚`a Ù±‚bmia3Ù±‚`a)Ù±‚`a Ù±‚aoa&Ù±‚`a Ù±‚`a(Ù±‚`ayÙ±‚`a Ù±‚aoa<Ù±‚`a Ù±‚bmia3Ù±‚`a)Ù±‚`a Ù±‚aoa&Ù±‚`a Ù±‚`a(Ù±‚`azÙ±‚`a Ù±‚aoa<Ù±‚`a Ù±‚bmia3Ù±‚`a)Ù±‚`a
Ù±‚`ecube2Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`a(Ù±‚`axÙ±‚`a Ù±‚aoa>Ù±‚aoa=Ù±‚`a Ù±‚bmia5Ù±‚`a)Ù±‚`a Ù±‚aoa&Ù±‚`a Ù±‚`a(Ù±‚`ayÙ±‚`a Ù±‚aoa>Ù±‚aoa=Ù±‚`a Ù±‚bmia5Ù±‚`a)Ù±‚`a Ù±‚aoa&Ù±‚`a Ù±‚`a(Ù±‚`azÙ±‚`a Ù±‚aoa>Ù±‚aoa=Ù±‚`a Ù±‚bmia5Ù±‚`a)Ù±‚`a
Ù±‚`dlinkÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bnbcabsÙ±‚`a(Ù±‚`axÙ±‚`a Ù±‚aoa-Ù±‚`a Ù±‚`ayÙ±‚`a)Ù±‚`a Ù±‚aoa+Ù±‚`a Ù±‚bnbcabsÙ±‚`a(Ù±‚`ayÙ±‚`a Ù±‚aoa-Ù±‚`a Ù±‚`azÙ±‚`a)Ù±‚`a Ù±‚aoa+Ù±‚`a Ù±‚bnbcabsÙ±‚`a(Ù±‚`azÙ±‚`a Ù±‚aoa-Ù±‚`a Ù±‚`axÙ±‚`a)Ù±‚`a Ù±‚aoa<Ù±‚aoa=Ù±‚`a Ù±‚bmia2Ù±‚`a
Ù±‚`a
Ù±‚bc1x1# combine the objects into a single boolean arrayÙ±‚`a
Ù±‚`jvoxelarrayÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`ecube1Ù±‚`a Ù±‚aoa|Ù±‚`a Ù±‚`ecube2Ù±‚`a Ù±‚aoa|Ù±‚`a Ù±‚`dlinkÙ±‚`a
Ù±‚`a
Ù±‚bc1x# set the colors of each objectÙ±‚`a
Ù±‚`fcolorsÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`eemptyÙ±‚`a(Ù±‚`jvoxelarrayÙ±‚aoa.Ù±‚`eshapeÙ±‚`a,Ù±‚`a Ù±‚`edtypeÙ±‚aoa=Ù±‚bnbfobjectÙ±‚`a)Ù±‚`a
Ù±‚`fcolorsÙ±‚`a[Ù±‚`dlinkÙ±‚`a]Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bs1a'Ù±‚bs1credÙ±‚bs1a'Ù±‚`a
Ù±‚`fcolorsÙ±‚`a[Ù±‚`ecube1Ù±‚`a]Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bs1a'Ù±‚bs1dblueÙ±‚bs1a'Ù±‚`a
Ù±‚`fcolorsÙ±‚`a[Ù±‚`ecube2Ù±‚`a]Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bs1a'Ù±‚bs1egreenÙ±‚bs1a'Ù±‚`a
Ù±‚`a
Ù±‚bc1u# and plot everythingÙ±‚`a
Ù±‚`baxÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cpltÙ±‚aoa.Ù±‚`ffigureÙ±‚`a(Ù±‚`a)Ù±‚aoa.Ù±‚`kadd_subplotÙ±‚`a(Ù±‚`jprojectionÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1b3dÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`fvoxelsÙ±‚`a(Ù±‚`jvoxelarrayÙ±‚`a,Ù±‚`a Ù±‚`jfacecolorsÙ±‚aoa=Ù±‚`fcolorsÙ±‚`a,Ù±‚`a Ù±‚`iedgecolorÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1akÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`cpltÙ±‚aoa.Ù±‚`dshowÙ±‚`a(Ù±‚`a)Ù±‚`a
`dNoneö