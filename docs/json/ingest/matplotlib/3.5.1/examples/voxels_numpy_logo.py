ЩЇ‚ЃЩґѓ™ЮЩ±‚bsdxҐ"""
===============================
3D voxel plot of the numpy logo
===============================

Demonstrates using `.Axes3D.voxels` with uneven coordinates.
"""Щ±‚`a
Щ±‚`a
Щ±‚bknfimportЩ±‚`a Щ±‚bnnЩў„jmatplotlibЩ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleхЩ±‚bnna.Щ±‚bnnfpyplotЩ±‚`a Щ±‚akbasЩ±‚`a Щ±‚bnncpltЩ±‚`a
Щ±‚bknfimportЩ±‚`a Щ±‚bnnЩў„enumpyЩ „enumpyf1.22.3fmoduleenumpyfmoduleхЩ±‚`a Щ±‚akbasЩ±‚`a Щ±‚bnnbnpЩ±‚`a
Щ±‚`a
Щ±‚`a
Щ±‚akcdefЩ±‚`a Щ±‚bnfgexplodeЩ±‚`a(Щ±‚`ddataЩ±‚`a)Щ±‚`a:Щ±‚`a
Щ±‚`d    Щ±‚`dsizeЩ±‚`a Щ±‚aoa=Щ±‚`a Щ±‚`bnpЩ±‚aoa.Щ±‚`earrayЩ±‚`a(Щ±‚`ddataЩ±‚aoa.Щ±‚`eshapeЩ±‚`a)Щ±‚aoa*Щ±‚bmia2Щ±‚`a
Щ±‚`d    Щ±‚`fdata_eЩ±‚`a Щ±‚aoa=Щ±‚`a Щ±‚`bnpЩ±‚aoa.Щ±‚`ezerosЩ±‚`a(Щ±‚`dsizeЩ±‚`a Щ±‚aoa-Щ±‚`a Щ±‚bmia1Щ±‚`a,Щ±‚`a Щ±‚`edtypeЩ±‚aoa=Щ±‚`ddataЩ±‚aoa.Щ±‚`edtypeЩ±‚`a)Щ±‚`a
Щ±‚`d    Щ±‚`fdata_eЩ±‚`a[Щ±‚`a:Щ±‚`a:Щ±‚bmia2Щ±‚`a,Щ±‚`a Щ±‚`a:Щ±‚`a:Щ±‚bmia2Щ±‚`a,Щ±‚`a Щ±‚`a:Щ±‚`a:Щ±‚bmia2Щ±‚`a]Щ±‚`a Щ±‚aoa=Щ±‚`a Щ±‚`ddataЩ±‚`a
Щ±‚`d    Щ±‚akfreturnЩ±‚`a Щ±‚`fdata_eЩ±‚`a
Щ±‚`a
Щ±‚bc1x# build up the numpy logoЩ±‚`a
Щ±‚`hn_voxelsЩ±‚`a Щ±‚aoa=Щ±‚`a Щ±‚`bnpЩ±‚aoa.Щ±‚`ezerosЩ±‚`a(Щ±‚`a(Щ±‚bmia4Щ±‚`a,Щ±‚`a Щ±‚bmia3Щ±‚`a,Щ±‚`a Щ±‚bmia4Щ±‚`a)Щ±‚`a,Щ±‚`a Щ±‚`edtypeЩ±‚aoa=Щ±‚bnbdboolЩ±‚`a)Щ±‚`a
Щ±‚`hn_voxelsЩ±‚`a[Щ±‚bmia0Щ±‚`a,Щ±‚`a Щ±‚bmia0Щ±‚`a,Щ±‚`a Щ±‚`a:Щ±‚`a]Щ±‚`a Щ±‚aoa=Щ±‚`a Щ±‚bkcdTrueЩ±‚`a
Щ±‚`hn_voxelsЩ±‚`a[Щ±‚aoa-Щ±‚bmia1Щ±‚`a,Щ±‚`a Щ±‚bmia0Щ±‚`a,Щ±‚`a Щ±‚`a:Щ±‚`a]Щ±‚`a Щ±‚aoa=Щ±‚`a Щ±‚bkcdTrueЩ±‚`a
Щ±‚`hn_voxelsЩ±‚`a[Щ±‚bmia1Щ±‚`a,Щ±‚`a Щ±‚bmia0Щ±‚`a,Щ±‚`a Щ±‚bmia2Щ±‚`a]Щ±‚`a Щ±‚aoa=Щ±‚`a Щ±‚bkcdTrueЩ±‚`a
Щ±‚`hn_voxelsЩ±‚`a[Щ±‚bmia2Щ±‚`a,Щ±‚`a Щ±‚bmia0Щ±‚`a,Щ±‚`a Щ±‚bmia1Щ±‚`a]Щ±‚`a Щ±‚aoa=Щ±‚`a Щ±‚bkcdTrueЩ±‚`a
Щ±‚`jfacecolorsЩ±‚`a Щ±‚aoa=Щ±‚`a Щ±‚`bnpЩ±‚aoa.Щ±‚`ewhereЩ±‚`a(Щ±‚`hn_voxelsЩ±‚`a,Щ±‚`a Щ±‚bs1a'Щ±‚bs1i#FFD65DC0Щ±‚bs1a'Щ±‚`a,Щ±‚`a Щ±‚bs1a'Щ±‚bs1i#7A88CCC0Щ±‚bs1a'Щ±‚`a)Щ±‚`a
Щ±‚`jedgecolorsЩ±‚`a Щ±‚aoa=Щ±‚`a Щ±‚`bnpЩ±‚aoa.Щ±‚`ewhereЩ±‚`a(Щ±‚`hn_voxelsЩ±‚`a,Щ±‚`a Щ±‚bs1a'Щ±‚bs1g#BFAB6EЩ±‚bs1a'Щ±‚`a,Щ±‚`a Щ±‚bs1a'Щ±‚bs1g#7D84A6Щ±‚bs1a'Щ±‚`a)Щ±‚`a
Щ±‚`ffilledЩ±‚`a Щ±‚aoa=Щ±‚`a Щ±‚`bnpЩ±‚aoa.Щ±‚`donesЩ±‚`a(Щ±‚`hn_voxelsЩ±‚aoa.Щ±‚`eshapeЩ±‚`a)Щ±‚`a
Щ±‚`a
Щ±‚bc1x-# upscale the above voxel image, leaving gapsЩ±‚`a
Щ±‚`hfilled_2Щ±‚`a Щ±‚aoa=Щ±‚`a Щ±‚`gexplodeЩ±‚`a(Щ±‚`ffilledЩ±‚`a)Щ±‚`a
Щ±‚`ifcolors_2Щ±‚`a Щ±‚aoa=Щ±‚`a Щ±‚`gexplodeЩ±‚`a(Щ±‚`jfacecolorsЩ±‚`a)Щ±‚`a
Щ±‚`iecolors_2Щ±‚`a Щ±‚aoa=Щ±‚`a Щ±‚`gexplodeЩ±‚`a(Щ±‚`jedgecolorsЩ±‚`a)Щ±‚`a
Щ±‚`a
Щ±‚bc1q# Shrink the gapsЩ±‚`a
Щ±‚`axЩ±‚`a,Щ±‚`a Щ±‚`ayЩ±‚`a,Щ±‚`a Щ±‚`azЩ±‚`a Щ±‚aoa=Щ±‚`a Щ±‚`bnpЩ±‚aoa.Щ±‚`gindicesЩ±‚`a(Щ±‚`bnpЩ±‚aoa.Щ±‚`earrayЩ±‚`a(Щ±‚`hfilled_2Щ±‚aoa.Щ±‚`eshapeЩ±‚`a)Щ±‚`a Щ±‚aoa+Щ±‚`a Щ±‚bmia1Щ±‚`a)Щ±‚aoa.Щ±‚`fastypeЩ±‚`a(Щ±‚bnbefloatЩ±‚`a)Щ±‚`a Щ±‚aoa/Щ±‚aoa/Щ±‚`a Щ±‚bmia2Щ±‚`a
Щ±‚`axЩ±‚`a[Щ±‚bmia0Щ±‚`a:Щ±‚`a:Щ±‚bmia2Щ±‚`a,Щ±‚`a Щ±‚`a:Щ±‚`a,Щ±‚`a Щ±‚`a:Щ±‚`a]Щ±‚`a Щ±‚aoa+Щ±‚aoa=Щ±‚`a Щ±‚bmfd0.05Щ±‚`a
Щ±‚`ayЩ±‚`a[Щ±‚`a:Щ±‚`a,Щ±‚`a Щ±‚bmia0Щ±‚`a:Щ±‚`a:Щ±‚bmia2Щ±‚`a,Щ±‚`a Щ±‚`a:Щ±‚`a]Щ±‚`a Щ±‚aoa+Щ±‚aoa=Щ±‚`a Щ±‚bmfd0.05Щ±‚`a
Щ±‚`azЩ±‚`a[Щ±‚`a:Щ±‚`a,Щ±‚`a Щ±‚`a:Щ±‚`a,Щ±‚`a Щ±‚bmia0Щ±‚`a:Щ±‚`a:Щ±‚bmia2Щ±‚`a]Щ±‚`a Щ±‚aoa+Щ±‚aoa=Щ±‚`a Щ±‚bmfd0.05Щ±‚`a
Щ±‚`axЩ±‚`a[Щ±‚bmia1Щ±‚`a:Щ±‚`a:Щ±‚bmia2Щ±‚`a,Щ±‚`a Щ±‚`a:Щ±‚`a,Щ±‚`a Щ±‚`a:Щ±‚`a]Щ±‚`a Щ±‚aoa+Щ±‚aoa=Щ±‚`a Щ±‚bmfd0.95Щ±‚`a
Щ±‚`ayЩ±‚`a[Щ±‚`a:Щ±‚`a,Щ±‚`a Щ±‚bmia1Щ±‚`a:Щ±‚`a:Щ±‚bmia2Щ±‚`a,Щ±‚`a Щ±‚`a:Щ±‚`a]Щ±‚`a Щ±‚aoa+Щ±‚aoa=Щ±‚`a Щ±‚bmfd0.95Щ±‚`a
Щ±‚`azЩ±‚`a[Щ±‚`a:Щ±‚`a,Щ±‚`a Щ±‚`a:Щ±‚`a,Щ±‚`a Щ±‚bmia1Щ±‚`a:Щ±‚`a:Щ±‚bmia2Щ±‚`a]Щ±‚`a Щ±‚aoa+Щ±‚aoa=Щ±‚`a Щ±‚bmfd0.95Щ±‚`a
Щ±‚`a
Щ±‚`baxЩ±‚`a Щ±‚aoa=Щ±‚`a Щ±‚`cpltЩ±‚aoa.Щ±‚`ffigureЩ±‚`a(Щ±‚`a)Щ±‚aoa.Щ±‚`kadd_subplotЩ±‚`a(Щ±‚`jprojectionЩ±‚aoa=Щ±‚bs1a'Щ±‚bs1b3dЩ±‚bs1a'Щ±‚`a)Щ±‚`a
Щ±‚`baxЩ±‚aoa.Щ±‚`fvoxelsЩ±‚`a(Щ±‚`axЩ±‚`a,Щ±‚`a Щ±‚`ayЩ±‚`a,Щ±‚`a Щ±‚`azЩ±‚`a,Щ±‚`a Щ±‚`hfilled_2Щ±‚`a,Щ±‚`a Щ±‚`jfacecolorsЩ±‚aoa=Щ±‚`ifcolors_2Щ±‚`a,Щ±‚`a Щ±‚`jedgecolorsЩ±‚aoa=Щ±‚`iecolors_2Щ±‚`a)Щ±‚`a
Щ±‚`a
Щ±‚`cpltЩ±‚aoa.Щ±‚`dshowЩ±‚`a(Щ±‚`a)Щ±‚`a
`dNoneц