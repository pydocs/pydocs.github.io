Ù¯‚Ù´ƒ™Ù±‚bsdxu"""
============
3D errorbars
============

An example of using errorbars with upper and lower limits in mplot3d.
"""Ù±‚`a
Ù±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnnfpyplotÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnncpltÙ±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„enumpyÙ „enumpyf1.22.3fmoduleenumpyfmoduleõÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnnbnpÙ±‚`a
Ù±‚`a
Ù±‚`baxÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cpltÙ±‚aoa.Ù±‚`ffigureÙ±‚`a(Ù±‚`a)Ù±‚aoa.Ù±‚`kadd_subplotÙ±‚`a(Ù±‚`jprojectionÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1b3dÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚bc1x# setting up a parametric curveÙ±‚`a
Ù±‚`atÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`farangeÙ±‚`a(Ù±‚bmia0Ù±‚`a,Ù±‚`a Ù±‚bmia2Ù±‚aoa*Ù±‚`bnpÙ±‚aoa.Ù±‚`bpiÙ±‚aoa+Ù±‚bmfb.1Ù±‚`a,Ù±‚`a Ù±‚bmfd0.01Ù±‚`a)Ù±‚`a
Ù±‚`axÙ±‚`a,Ù±‚`a Ù±‚`ayÙ±‚`a,Ù±‚`a Ù±‚`azÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`csinÙ±‚`a(Ù±‚`atÙ±‚`a)Ù±‚`a,Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`ccosÙ±‚`a(Ù±‚bmia3Ù±‚aoa*Ù±‚`atÙ±‚`a)Ù±‚`a,Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`csinÙ±‚`a(Ù±‚bmia5Ù±‚aoa*Ù±‚`atÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`eestepÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bmib15Ù±‚`a
Ù±‚`aiÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`farangeÙ±‚`a(Ù±‚`atÙ±‚aoa.Ù±‚`dsizeÙ±‚`a)Ù±‚`a
Ù±‚`gzuplimsÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`a(Ù±‚`aiÙ±‚`a Ù±‚aoa%Ù±‚`a Ù±‚`eestepÙ±‚`a Ù±‚aob==Ù±‚`a Ù±‚bmia0Ù±‚`a)Ù±‚`a Ù±‚aoa&Ù±‚`a Ù±‚`a(Ù±‚`aiÙ±‚`a Ù±‚aoa/Ù±‚aoa/Ù±‚`a Ù±‚`eestepÙ±‚`a Ù±‚aoa%Ù±‚`a Ù±‚bmia3Ù±‚`a Ù±‚aob==Ù±‚`a Ù±‚bmia0Ù±‚`a)Ù±‚`a
Ù±‚`gzlolimsÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`a(Ù±‚`aiÙ±‚`a Ù±‚aoa%Ù±‚`a Ù±‚`eestepÙ±‚`a Ù±‚aob==Ù±‚`a Ù±‚bmia0Ù±‚`a)Ù±‚`a Ù±‚aoa&Ù±‚`a Ù±‚`a(Ù±‚`aiÙ±‚`a Ù±‚aoa/Ù±‚aoa/Ù±‚`a Ù±‚`eestepÙ±‚`a Ù±‚aoa%Ù±‚`a Ù±‚bmia3Ù±‚`a Ù±‚aob==Ù±‚`a Ù±‚bmia2Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`herrorbarÙ±‚`a(Ù±‚`axÙ±‚`a,Ù±‚`a Ù±‚`ayÙ±‚`a,Ù±‚`a Ù±‚`azÙ±‚`a,Ù±‚`a Ù±‚bmfc0.2Ù±‚`a,Ù±‚`a Ù±‚`gzuplimsÙ±‚aoa=Ù±‚`gzuplimsÙ±‚`a,Ù±‚`a Ù±‚`gzlolimsÙ±‚aoa=Ù±‚`gzlolimsÙ±‚`a,Ù±‚`a Ù±‚`jerroreveryÙ±‚aoa=Ù±‚`eestepÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`jset_xlabelÙ±‚`a(Ù±‚bs2a"Ù±‚bs2gX labelÙ±‚bs2a"Ù±‚`a)Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`jset_ylabelÙ±‚`a(Ù±‚bs2a"Ù±‚bs2gY labelÙ±‚bs2a"Ù±‚`a)Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`jset_zlabelÙ±‚`a(Ù±‚bs2a"Ù±‚bs2gZ labelÙ±‚bs2a"Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`cpltÙ±‚aoa.Ù±‚`dshowÙ±‚`a(Ù±‚`a)Ù±‚`a
`dNoneö