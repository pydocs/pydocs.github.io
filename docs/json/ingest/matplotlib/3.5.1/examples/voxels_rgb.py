ŸØÇÅŸ¥ÉôéŸ±Çbsdx“"""
==========================================
3D voxel / volumetric plot with rgb colors
==========================================

Demonstrates using `.Axes3D.voxels` to visualize parts of a color space.
"""Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±ÇbknfimportŸ±Ç`a Ÿ±ÇbnnŸ¢ÑjmatplotlibŸ†Ñjmatplotlibe3.5.1fmodulejmatplotlibfmoduleıŸ±Çbnna.Ÿ±ÇbnnfpyplotŸ±Ç`a Ÿ±ÇakbasŸ±Ç`a Ÿ±ÇbnncpltŸ±Ç`a
Ÿ±ÇbknfimportŸ±Ç`a Ÿ±ÇbnnŸ¢ÑenumpyŸ†Ñenumpyf1.22.3fmoduleenumpyfmoduleıŸ±Ç`a Ÿ±ÇakbasŸ±Ç`a Ÿ±ÇbnnbnpŸ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±ÇakcdefŸ±Ç`a Ÿ±ÇbnfimidpointsŸ±Ç`a(Ÿ±Ç`axŸ±Ç`a)Ÿ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`bslŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±ÇakcforŸ±Ç`a Ÿ±Ç`aiŸ±Ç`a Ÿ±ÇbowbinŸ±Ç`a Ÿ±ÇbnberangeŸ±Ç`a(Ÿ±Ç`axŸ±Çaoa.Ÿ±Ç`dndimŸ±Ç`a)Ÿ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±Ç`axŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`a(Ÿ±Ç`axŸ±Ç`a[Ÿ±Ç`bslŸ±Ç`a Ÿ±Çaoa+Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`iindex_expŸ±Ç`a[Ÿ±Ç`a:Ÿ±Çaoa-Ÿ±Çbmia1Ÿ±Ç`a]Ÿ±Ç`a]Ÿ±Ç`a Ÿ±Çaoa+Ÿ±Ç`a Ÿ±Ç`axŸ±Ç`a[Ÿ±Ç`bslŸ±Ç`a Ÿ±Çaoa+Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`iindex_expŸ±Ç`a[Ÿ±Çbmia1Ÿ±Ç`a:Ÿ±Ç`a]Ÿ±Ç`a]Ÿ±Ç`a)Ÿ±Ç`a Ÿ±Çaoa/Ÿ±Ç`a Ÿ±Çbmfc2.0Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±Ç`bslŸ±Ç`a Ÿ±Çaoa+Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`iindex_expŸ±Ç`a[Ÿ±Ç`a:Ÿ±Ç`a]Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±ÇakfreturnŸ±Ç`a Ÿ±Ç`axŸ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1x9# prepare some coordinates, and attach rgb values to eachŸ±Ç`a
Ÿ±Ç`arŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`agŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`abŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`gindicesŸ±Ç`a(Ÿ±Ç`a(Ÿ±Çbmib17Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmib17Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmib17Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a Ÿ±Çaoa/Ÿ±Ç`a Ÿ±Çbmfd16.0Ÿ±Ç`a
Ÿ±Ç`brcŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`imidpointsŸ±Ç`a(Ÿ±Ç`arŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`bgcŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`imidpointsŸ±Ç`a(Ÿ±Ç`agŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`bbcŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`imidpointsŸ±Ç`a(Ÿ±Ç`abŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1x'# define a sphere about [0.5, 0.5, 0.5]Ÿ±Ç`a
Ÿ±Ç`fsphereŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`a(Ÿ±Ç`brcŸ±Ç`a Ÿ±Çaoa-Ÿ±Ç`a Ÿ±Çbmfc0.5Ÿ±Ç`a)Ÿ±Çaoa*Ÿ±Çaoa*Ÿ±Çbmia2Ÿ±Ç`a Ÿ±Çaoa+Ÿ±Ç`a Ÿ±Ç`a(Ÿ±Ç`bgcŸ±Ç`a Ÿ±Çaoa-Ÿ±Ç`a Ÿ±Çbmfc0.5Ÿ±Ç`a)Ÿ±Çaoa*Ÿ±Çaoa*Ÿ±Çbmia2Ÿ±Ç`a Ÿ±Çaoa+Ÿ±Ç`a Ÿ±Ç`a(Ÿ±Ç`bbcŸ±Ç`a Ÿ±Çaoa-Ÿ±Ç`a Ÿ±Çbmfc0.5Ÿ±Ç`a)Ÿ±Çaoa*Ÿ±Çaoa*Ÿ±Çbmia2Ÿ±Ç`a Ÿ±Çaoa<Ÿ±Ç`a Ÿ±Çbmfc0.5Ÿ±Çaoa*Ÿ±Çaoa*Ÿ±Çbmia2Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1x# combine the color componentsŸ±Ç`a
Ÿ±Ç`fcolorsŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`ezerosŸ±Ç`a(Ÿ±Ç`fsphereŸ±Çaoa.Ÿ±Ç`eshapeŸ±Ç`a Ÿ±Çaoa+Ÿ±Ç`a Ÿ±Ç`a(Ÿ±Çbmia3Ÿ±Ç`a,Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`fcolorsŸ±Ç`a[Ÿ±Çaoa.Ÿ±Çaoa.Ÿ±Çaoa.Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia0Ÿ±Ç`a]Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`brcŸ±Ç`a
Ÿ±Ç`fcolorsŸ±Ç`a[Ÿ±Çaoa.Ÿ±Çaoa.Ÿ±Çaoa.Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia1Ÿ±Ç`a]Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bgcŸ±Ç`a
Ÿ±Ç`fcolorsŸ±Ç`a[Ÿ±Çaoa.Ÿ±Çaoa.Ÿ±Çaoa.Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia2Ÿ±Ç`a]Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bbcŸ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1u# and plot everythingŸ±Ç`a
Ÿ±Ç`baxŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`ffigureŸ±Ç`a(Ÿ±Ç`a)Ÿ±Çaoa.Ÿ±Ç`kadd_subplotŸ±Ç`a(Ÿ±Ç`jprojectionŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1b3dŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`fvoxelsŸ±Ç`a(Ÿ±Ç`arŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`agŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`abŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`fsphereŸ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`j          Ÿ±Ç`jfacecolorsŸ±Çaoa=Ÿ±Ç`fcolorsŸ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`j          Ÿ±Ç`jedgecolorsŸ±Çaoa=Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`dclipŸ±Ç`a(Ÿ±Çbmia2Ÿ±Çaoa*Ÿ±Ç`fcolorsŸ±Ç`a Ÿ±Çaoa-Ÿ±Ç`a Ÿ±Çbmfc0.5Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia1Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`b  Ÿ±Çbc1j# brighterŸ±Ç`a
Ÿ±Ç`j          Ÿ±Ç`ilinewidthŸ±Çaoa=Ÿ±Çbmfc0.5Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`csetŸ±Ç`a(Ÿ±Ç`fxlabelŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1arŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`fylabelŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1agŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`fzlabelŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1abŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`dshowŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
`dNoneˆ