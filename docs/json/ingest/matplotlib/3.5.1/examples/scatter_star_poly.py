ЩЇ‚ЃЩґѓ™лЩ±‚bsdxґ"""
===============
Marker examples
===============

Example with different ways to specify markers.

For a list of all markers see also the `matplotlib.markers` documentation.
"""Щ±‚`a
Щ±‚bknfimportЩ±‚`a Щ±‚bnnЩў„enumpyЩ „enumpyf1.22.3fmoduleenumpyfmoduleхЩ±‚`a Щ±‚akbasЩ±‚`a Щ±‚bnnbnpЩ±‚`a
Щ±‚bknfimportЩ±‚`a Щ±‚bnnЩў„jmatplotlibЩ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleхЩ±‚bnna.Щ±‚bnnfpyplotЩ±‚`a Щ±‚akbasЩ±‚`a Щ±‚bnncpltЩ±‚`a
Щ±‚`a
Щ±‚bc1x)# Fixing random state for reproducibilityЩ±‚`a
Щ±‚`bnpЩ±‚aoa.Щ±‚`frandomЩ±‚aoa.Щ±‚`dseedЩ±‚`a(Щ±‚bmih19680801Щ±‚`a)Щ±‚`a
Щ±‚`a
Щ±‚`axЩ±‚`a Щ±‚aoa=Щ±‚`a Щ±‚`bnpЩ±‚aoa.Щ±‚`frandomЩ±‚aoa.Щ±‚`drandЩ±‚`a(Щ±‚bmib10Щ±‚`a)Щ±‚`a
Щ±‚`ayЩ±‚`a Щ±‚aoa=Щ±‚`a Щ±‚`bnpЩ±‚aoa.Щ±‚`frandomЩ±‚aoa.Щ±‚`drandЩ±‚`a(Щ±‚bmib10Щ±‚`a)Щ±‚`a
Щ±‚`azЩ±‚`a Щ±‚aoa=Щ±‚`a Щ±‚`bnpЩ±‚aoa.Щ±‚`dsqrtЩ±‚`a(Щ±‚`axЩ±‚aoa*Щ±‚aoa*Щ±‚bmia2Щ±‚`a Щ±‚aoa+Щ±‚`a Щ±‚`ayЩ±‚aoa*Щ±‚aoa*Щ±‚bmia2Щ±‚`a)Щ±‚`a
Щ±‚`a
Щ±‚`cfigЩ±‚`a,Щ±‚`a Щ±‚`caxsЩ±‚`a Щ±‚aoa=Щ±‚`a Щ±‚`cpltЩ±‚aoa.Щ±‚`hsubplotsЩ±‚`a(Щ±‚bmia2Щ±‚`a,Щ±‚`a Щ±‚bmia3Щ±‚`a,Щ±‚`a Щ±‚`fsharexЩ±‚aoa=Щ±‚bkcdTrueЩ±‚`a,Щ±‚`a Щ±‚`fshareyЩ±‚aoa=Щ±‚bkcdTrueЩ±‚`a)Щ±‚`a
Щ±‚`a
Щ±‚bc1o# marker symbolЩ±‚`a
Щ±‚`caxsЩ±‚`a[Щ±‚bmia0Щ±‚`a,Щ±‚`a Щ±‚bmia0Щ±‚`a]Щ±‚aoa.Щ±‚`gscatterЩ±‚`a(Щ±‚`axЩ±‚`a,Щ±‚`a Щ±‚`ayЩ±‚`a,Щ±‚`a Щ±‚`asЩ±‚aoa=Щ±‚bmib80Щ±‚`a,Щ±‚`a Щ±‚`acЩ±‚aoa=Щ±‚`azЩ±‚`a,Щ±‚`a Щ±‚`fmarkerЩ±‚aoa=Щ±‚bs2a"Щ±‚bs2a>Щ±‚bs2a"Щ±‚`a)Щ±‚`a
Щ±‚`caxsЩ±‚`a[Щ±‚bmia0Щ±‚`a,Щ±‚`a Щ±‚bmia0Щ±‚`a]Щ±‚aoa.Щ±‚`iset_titleЩ±‚`a(Щ±‚bs2a"Щ±‚bs2gmarker=Щ±‚bs2a'Щ±‚bs2a>Щ±‚bs2a'Щ±‚bs2a"Щ±‚`a)Щ±‚`a
Щ±‚`a
Щ±‚bc1q# marker from TeXЩ±‚`a
Щ±‚`caxsЩ±‚`a[Щ±‚bmia0Щ±‚`a,Щ±‚`a Щ±‚bmia1Щ±‚`a]Щ±‚aoa.Щ±‚`gscatterЩ±‚`a(Щ±‚`axЩ±‚`a,Щ±‚`a Щ±‚`ayЩ±‚`a,Щ±‚`a Щ±‚`asЩ±‚aoa=Щ±‚bmib80Щ±‚`a,Щ±‚`a Щ±‚`acЩ±‚aoa=Щ±‚`azЩ±‚`a,Щ±‚`a Щ±‚`fmarkerЩ±‚aoa=Щ±‚bsaarЩ±‚bs1a'Щ±‚bs1a$Щ±‚bs1a\Щ±‚bs1falpha$Щ±‚bs1a'Щ±‚`a)Щ±‚`a
Щ±‚`caxsЩ±‚`a[Щ±‚bmia0Щ±‚`a,Щ±‚`a Щ±‚bmia1Щ±‚`a]Щ±‚aoa.Щ±‚`iset_titleЩ±‚`a(Щ±‚bsaarЩ±‚bs2a"Щ±‚bs2hmarker=rЩ±‚bs2a'Щ±‚bs2a\Щ±‚bs2a$Щ±‚bs2a\Щ±‚bs2ealphaЩ±‚bs2a\Щ±‚bs2a$Щ±‚bs2a'Щ±‚bs2a"Щ±‚`a)Щ±‚`a
Щ±‚`a
Щ±‚bc1r# marker from pathЩ±‚`a
Щ±‚`evertsЩ±‚`a Щ±‚aoa=Щ±‚`a Щ±‚`a[Щ±‚`a[Щ±‚aoa-Щ±‚bmia1Щ±‚`a,Щ±‚`a Щ±‚aoa-Щ±‚bmia1Щ±‚`a]Щ±‚`a,Щ±‚`a Щ±‚`a[Щ±‚bmia1Щ±‚`a,Щ±‚`a Щ±‚aoa-Щ±‚bmia1Щ±‚`a]Щ±‚`a,Щ±‚`a Щ±‚`a[Щ±‚bmia1Щ±‚`a,Щ±‚`a Щ±‚bmia1Щ±‚`a]Щ±‚`a,Щ±‚`a Щ±‚`a[Щ±‚aoa-Щ±‚bmia1Щ±‚`a,Щ±‚`a Щ±‚aoa-Щ±‚bmia1Щ±‚`a]Щ±‚`a]Щ±‚`a
Щ±‚`caxsЩ±‚`a[Щ±‚bmia0Щ±‚`a,Щ±‚`a Щ±‚bmia2Щ±‚`a]Щ±‚aoa.Щ±‚`gscatterЩ±‚`a(Щ±‚`axЩ±‚`a,Щ±‚`a Щ±‚`ayЩ±‚`a,Щ±‚`a Щ±‚`asЩ±‚aoa=Щ±‚bmib80Щ±‚`a,Щ±‚`a Щ±‚`acЩ±‚aoa=Щ±‚`azЩ±‚`a,Щ±‚`a Щ±‚`fmarkerЩ±‚aoa=Щ±‚`evertsЩ±‚`a)Щ±‚`a
Щ±‚`caxsЩ±‚`a[Щ±‚bmia0Щ±‚`a,Щ±‚`a Щ±‚bmia2Щ±‚`a]Щ±‚aoa.Щ±‚`iset_titleЩ±‚`a(Щ±‚bs2a"Щ±‚bs2lmarker=vertsЩ±‚bs2a"Щ±‚`a)Щ±‚`a
Щ±‚`a
Щ±‚bc1x# regular polygon markerЩ±‚`a
Щ±‚`caxsЩ±‚`a[Щ±‚bmia1Щ±‚`a,Щ±‚`a Щ±‚bmia0Щ±‚`a]Щ±‚aoa.Щ±‚`gscatterЩ±‚`a(Щ±‚`axЩ±‚`a,Щ±‚`a Щ±‚`ayЩ±‚`a,Щ±‚`a Щ±‚`asЩ±‚aoa=Щ±‚bmib80Щ±‚`a,Щ±‚`a Щ±‚`acЩ±‚aoa=Щ±‚`azЩ±‚`a,Щ±‚`a Щ±‚`fmarkerЩ±‚aoa=Щ±‚`a(Щ±‚bmia5Щ±‚`a,Щ±‚`a Щ±‚bmia0Щ±‚`a)Щ±‚`a)Щ±‚`a
Щ±‚`caxsЩ±‚`a[Щ±‚bmia1Щ±‚`a,Щ±‚`a Щ±‚bmia0Щ±‚`a]Щ±‚aoa.Щ±‚`iset_titleЩ±‚`a(Щ±‚bs2a"Щ±‚bs2mmarker=(5, 0)Щ±‚bs2a"Щ±‚`a)Щ±‚`a
Щ±‚`a
Щ±‚bc1u# regular star markerЩ±‚`a
Щ±‚`caxsЩ±‚`a[Щ±‚bmia1Щ±‚`a,Щ±‚`a Щ±‚bmia1Щ±‚`a]Щ±‚aoa.Щ±‚`gscatterЩ±‚`a(Щ±‚`axЩ±‚`a,Щ±‚`a Щ±‚`ayЩ±‚`a,Щ±‚`a Щ±‚`asЩ±‚aoa=Щ±‚bmib80Щ±‚`a,Щ±‚`a Щ±‚`acЩ±‚aoa=Щ±‚`azЩ±‚`a,Щ±‚`a Щ±‚`fmarkerЩ±‚aoa=Щ±‚`a(Щ±‚bmia5Щ±‚`a,Щ±‚`a Щ±‚bmia1Щ±‚`a)Щ±‚`a)Щ±‚`a
Щ±‚`caxsЩ±‚`a[Щ±‚bmia1Щ±‚`a,Щ±‚`a Щ±‚bmia1Щ±‚`a]Щ±‚aoa.Щ±‚`iset_titleЩ±‚`a(Щ±‚bs2a"Щ±‚bs2mmarker=(5, 1)Щ±‚bs2a"Щ±‚`a)Щ±‚`a
Щ±‚`a
Щ±‚bc1x# regular asterisk markerЩ±‚`a
Щ±‚`caxsЩ±‚`a[Щ±‚bmia1Щ±‚`a,Щ±‚`a Щ±‚bmia2Щ±‚`a]Щ±‚aoa.Щ±‚`gscatterЩ±‚`a(Щ±‚`axЩ±‚`a,Щ±‚`a Щ±‚`ayЩ±‚`a,Щ±‚`a Щ±‚`asЩ±‚aoa=Щ±‚bmib80Щ±‚`a,Щ±‚`a Щ±‚`acЩ±‚aoa=Щ±‚`azЩ±‚`a,Щ±‚`a Щ±‚`fmarkerЩ±‚aoa=Щ±‚`a(Щ±‚bmia5Щ±‚`a,Щ±‚`a Щ±‚bmia2Щ±‚`a)Щ±‚`a)Щ±‚`a
Щ±‚`caxsЩ±‚`a[Щ±‚bmia1Щ±‚`a,Щ±‚`a Щ±‚bmia2Щ±‚`a]Щ±‚aoa.Щ±‚`iset_titleЩ±‚`a(Щ±‚bs2a"Щ±‚bs2mmarker=(5, 2)Щ±‚bs2a"Щ±‚`a)Щ±‚`a
Щ±‚`a
Щ±‚`cpltЩ±‚aoa.Щ±‚`ltight_layoutЩ±‚`a(Щ±‚`a)Щ±‚`a
Щ±‚`cpltЩ±‚aoa.Щ±‚`dshowЩ±‚`a(Щ±‚`a)Щ±‚`a
`dNoneц