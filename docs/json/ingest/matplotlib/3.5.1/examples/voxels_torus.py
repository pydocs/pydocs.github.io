Ù¯‚Ù´ƒ™»Ù±‚bsdxõ"""
=======================================================
3D voxel / volumetric plot with cylindrical coordinates
=======================================================

Demonstrates using the *x*, *y*, *z* parameters of `.Axes3D.voxels`.
"""Ù±‚`a
Ù±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnnfpyplotÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnncpltÙ±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnnfcolorsÙ±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„enumpyÙ „enumpyf1.22.3fmoduleenumpyfmoduleõÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnnbnpÙ±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚akcdefÙ±‚`a Ù±‚bnfimidpointsÙ±‚`a(Ù±‚`axÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`d    Ù±‚`bslÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚akcforÙ±‚`a Ù±‚`aiÙ±‚`a Ù±‚bowbinÙ±‚`a Ù±‚bnberangeÙ±‚`a(Ù±‚`axÙ±‚aoa.Ù±‚`dndimÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`h        Ù±‚`axÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`a(Ù±‚`axÙ±‚`a[Ù±‚`bslÙ±‚`a Ù±‚aoa+Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`iindex_expÙ±‚`a[Ù±‚`a:Ù±‚aoa-Ù±‚bmia1Ù±‚`a]Ù±‚`a]Ù±‚`a Ù±‚aoa+Ù±‚`a Ù±‚`axÙ±‚`a[Ù±‚`bslÙ±‚`a Ù±‚aoa+Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`iindex_expÙ±‚`a[Ù±‚bmia1Ù±‚`a:Ù±‚`a]Ù±‚`a]Ù±‚`a)Ù±‚`a Ù±‚aoa/Ù±‚`a Ù±‚bmfc2.0Ù±‚`a
Ù±‚`h        Ù±‚`bslÙ±‚`a Ù±‚aoa+Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`iindex_expÙ±‚`a[Ù±‚`a:Ù±‚`a]Ù±‚`a
Ù±‚`d    Ù±‚akfreturnÙ±‚`a Ù±‚`axÙ±‚`a
Ù±‚`a
Ù±‚bc1x9# prepare some coordinates, and attach rgb values to eachÙ±‚`a
Ù±‚`arÙ±‚`a,Ù±‚`a Ù±‚`ethetaÙ±‚`a,Ù±‚`a Ù±‚`azÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`emgridÙ±‚`a[Ù±‚bmia0Ù±‚`a:Ù±‚bmia1Ù±‚`a:Ù±‚bmib11Ù±‚`ajÙ±‚`a,Ù±‚`a Ù±‚bmia0Ù±‚`a:Ù±‚`bnpÙ±‚aoa.Ù±‚`bpiÙ±‚aoa*Ù±‚bmia2Ù±‚`a:Ù±‚bmib25Ù±‚`ajÙ±‚`a,Ù±‚`a Ù±‚aoa-Ù±‚bmfc0.5Ù±‚`a:Ù±‚bmfc0.5Ù±‚`a:Ù±‚bmib11Ù±‚`ajÙ±‚`a]Ù±‚`a
Ù±‚`axÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`arÙ±‚aoa*Ù±‚`bnpÙ±‚aoa.Ù±‚`ccosÙ±‚`a(Ù±‚`ethetaÙ±‚`a)Ù±‚`a
Ù±‚`ayÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`arÙ±‚aoa*Ù±‚`bnpÙ±‚aoa.Ù±‚`csinÙ±‚`a(Ù±‚`ethetaÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`brcÙ±‚`a,Ù±‚`a Ù±‚`fthetacÙ±‚`a,Ù±‚`a Ù±‚`bzcÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`imidpointsÙ±‚`a(Ù±‚`arÙ±‚`a)Ù±‚`a,Ù±‚`a Ù±‚`imidpointsÙ±‚`a(Ù±‚`ethetaÙ±‚`a)Ù±‚`a,Ù±‚`a Ù±‚`imidpointsÙ±‚`a(Ù±‚`azÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚bc1x)# define a wobbly torus about [0.7, *, 0]Ù±‚`a
Ù±‚`fsphereÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`a(Ù±‚`brcÙ±‚`a Ù±‚aoa-Ù±‚`a Ù±‚bmfc0.7Ù±‚`a)Ù±‚aoa*Ù±‚aoa*Ù±‚bmia2Ù±‚`a Ù±‚aoa+Ù±‚`a Ù±‚`a(Ù±‚`bzcÙ±‚`a Ù±‚aoa+Ù±‚`a Ù±‚bmfc0.2Ù±‚aoa*Ù±‚`bnpÙ±‚aoa.Ù±‚`ccosÙ±‚`a(Ù±‚`fthetacÙ±‚aoa*Ù±‚bmia2Ù±‚`a)Ù±‚`a)Ù±‚aoa*Ù±‚aoa*Ù±‚bmia2Ù±‚`a Ù±‚aoa<Ù±‚`a Ù±‚bmfc0.2Ù±‚aoa*Ù±‚aoa*Ù±‚bmia2Ù±‚`a
Ù±‚`a
Ù±‚bc1x# combine the color componentsÙ±‚`a
Ù±‚`chsvÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`ezerosÙ±‚`a(Ù±‚`fsphereÙ±‚aoa.Ù±‚`eshapeÙ±‚`a Ù±‚aoa+Ù±‚`a Ù±‚`a(Ù±‚bmia3Ù±‚`a,Ù±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`chsvÙ±‚`a[Ù±‚aoa.Ù±‚aoa.Ù±‚aoa.Ù±‚`a,Ù±‚`a Ù±‚bmia0Ù±‚`a]Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`fthetacÙ±‚`a Ù±‚aoa/Ù±‚`a Ù±‚`a(Ù±‚`bnpÙ±‚aoa.Ù±‚`bpiÙ±‚aoa*Ù±‚bmia2Ù±‚`a)Ù±‚`a
Ù±‚`chsvÙ±‚`a[Ù±‚aoa.Ù±‚aoa.Ù±‚aoa.Ù±‚`a,Ù±‚`a Ù±‚bmia1Ù±‚`a]Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`brcÙ±‚`a
Ù±‚`chsvÙ±‚`a[Ù±‚aoa.Ù±‚aoa.Ù±‚aoa.Ù±‚`a,Ù±‚`a Ù±‚bmia2Ù±‚`a]Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bzcÙ±‚`a Ù±‚aoa+Ù±‚`a Ù±‚bmfc0.5Ù±‚`a
Ù±‚`fcolorsÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`Ù¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚aoa.Ù±‚`fcolorsÙ±‚aoa.Ù±‚`jhsv_to_rgbÙ±‚`a(Ù±‚`chsvÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚bc1u# and plot everythingÙ±‚`a
Ù±‚`baxÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cpltÙ±‚aoa.Ù±‚`ffigureÙ±‚`a(Ù±‚`a)Ù±‚aoa.Ù±‚`kadd_subplotÙ±‚`a(Ù±‚`jprojectionÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1b3dÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`fvoxelsÙ±‚`a(Ù±‚`axÙ±‚`a,Ù±‚`a Ù±‚`ayÙ±‚`a,Ù±‚`a Ù±‚`azÙ±‚`a,Ù±‚`a Ù±‚`fsphereÙ±‚`a,Ù±‚`a
Ù±‚`j          Ù±‚`jfacecolorsÙ±‚aoa=Ù±‚`fcolorsÙ±‚`a,Ù±‚`a
Ù±‚`j          Ù±‚`jedgecolorsÙ±‚aoa=Ù±‚`bnpÙ±‚aoa.Ù±‚`dclipÙ±‚`a(Ù±‚bmia2Ù±‚aoa*Ù±‚`fcolorsÙ±‚`a Ù±‚aoa-Ù±‚`a Ù±‚bmfc0.5Ù±‚`a,Ù±‚`a Ù±‚bmia0Ù±‚`a,Ù±‚`a Ù±‚bmia1Ù±‚`a)Ù±‚`a,Ù±‚`b  Ù±‚bc1j# brighterÙ±‚`a
Ù±‚`j          Ù±‚`ilinewidthÙ±‚aoa=Ù±‚bmfc0.5Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`cpltÙ±‚aoa.Ù±‚`dshowÙ±‚`a(Ù±‚`a)Ù±‚`a
`dNoneö