ŸØÇÅŸ¥Éô$Ÿ±Çbsdxf"""
==============
Triinterp Demo
==============

Interpolation from triangular grid to quad grid.
"""Ÿ±Ç`a
Ÿ±ÇbknfimportŸ±Ç`a Ÿ±ÇbnnŸ¢ÑjmatplotlibŸ†Ñjmatplotlibe3.5.1fmodulejmatplotlibfmoduleıŸ±Çbnna.Ÿ±ÇbnnfpyplotŸ±Ç`a Ÿ±ÇakbasŸ±Ç`a Ÿ±ÇbnncpltŸ±Ç`a
Ÿ±ÇbknfimportŸ±Ç`a Ÿ±ÇbnnŸ¢ÑjmatplotlibŸ†Ñjmatplotlibe3.5.1fmodulejmatplotlibfmoduleıŸ±Çbnna.Ÿ±ÇbnnctriŸ±Ç`a Ÿ±ÇakbasŸ±Ç`a Ÿ±ÇbnndmtriŸ±Ç`a
Ÿ±ÇbknfimportŸ±Ç`a Ÿ±ÇbnnŸ¢ÑenumpyŸ†Ñenumpyf1.22.3fmoduleenumpyfmoduleıŸ±Ç`a Ÿ±ÇakbasŸ±Ç`a Ÿ±ÇbnnbnpŸ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1w# Create triangulation.Ÿ±Ç`a
Ÿ±Ç`axŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`gasarrayŸ±Ç`a(Ÿ±Ç`a[Ÿ±Çbmia0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia2Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia3Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfc0.5Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfc1.5Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfc2.5Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia2Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfc1.5Ÿ±Ç`a]Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`ayŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`gasarrayŸ±Ç`a(Ÿ±Ç`a[Ÿ±Çbmia0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfc1.0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfc1.0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfc1.0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia2Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia2Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfc3.0Ÿ±Ç`a]Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`itrianglesŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`a[Ÿ±Ç`a[Ÿ±Çbmia0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia4Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`a[Ÿ±Çbmia1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia2Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia5Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`a[Ÿ±Çbmia2Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia3Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia6Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`a[Ÿ±Çbmia1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia5Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia4Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`a[Ÿ±Çbmia2Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia6Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia5Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`a[Ÿ±Çbmia4Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia5Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia7Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`m             Ÿ±Ç`a[Ÿ±Çbmia5Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia6Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia8Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`a[Ÿ±Çbmia5Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia8Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia7Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`a[Ÿ±Çbmia7Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia8Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia9Ÿ±Ç`a]Ÿ±Ç`a]Ÿ±Ç`a
Ÿ±Ç`ftriangŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`dmtriŸ±Çaoa.Ÿ±Ç`mTriangulationŸ±Ç`a(Ÿ±Ç`axŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ayŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`itrianglesŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1x,# Interpolate to regularly-spaced quad grid.Ÿ±Ç`a
Ÿ±Ç`azŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`ccosŸ±Ç`a(Ÿ±Çbmfc1.5Ÿ±Ç`a Ÿ±Çaoa*Ÿ±Ç`a Ÿ±Ç`axŸ±Ç`a)Ÿ±Ç`a Ÿ±Çaoa*Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`ccosŸ±Ç`a(Ÿ±Çbmfc1.5Ÿ±Ç`a Ÿ±Çaoa*Ÿ±Ç`a Ÿ±Ç`ayŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`bxiŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`byiŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`hmeshgridŸ±Ç`a(Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`hlinspaceŸ±Ç`a(Ÿ±Çbmia0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia3Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmib20Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`hlinspaceŸ±Ç`a(Ÿ±Çbmia0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia3Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmib20Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`jinterp_linŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`dmtriŸ±Çaoa.Ÿ±Ç`uLinearTriInterpolatorŸ±Ç`a(Ÿ±Ç`ftriangŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`azŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`fzi_linŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`jinterp_linŸ±Ç`a(Ÿ±Ç`bxiŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`byiŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`qinterp_cubic_geomŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`dmtriŸ±Çaoa.Ÿ±Ç`tCubicTriInterpolatorŸ±Ç`a(Ÿ±Ç`ftriangŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`azŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dkindŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1dgeomŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`mzi_cubic_geomŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`qinterp_cubic_geomŸ±Ç`a(Ÿ±Ç`bxiŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`byiŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`rinterp_cubic_min_EŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`dmtriŸ±Çaoa.Ÿ±Ç`tCubicTriInterpolatorŸ±Ç`a(Ÿ±Ç`ftriangŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`azŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dkindŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1emin_EŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`nzi_cubic_min_EŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`rinterp_cubic_min_EŸ±Ç`a(Ÿ±Ç`bxiŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`byiŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1s# Set up the figureŸ±Ç`a
Ÿ±Ç`cfigŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`caxsŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`hsubplotsŸ±Ç`a(Ÿ±Ç`enrowsŸ±Çaoa=Ÿ±Çbmia2Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`encolsŸ±Çaoa=Ÿ±Çbmia2Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`caxsŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`caxsŸ±Çaoa.Ÿ±Ç`gflattenŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1x# Plot the triangulation.Ÿ±Ç`a
Ÿ±Ç`caxsŸ±Ç`a[Ÿ±Çbmia0Ÿ±Ç`a]Ÿ±Çaoa.Ÿ±Ç`ktricontourfŸ±Ç`a(Ÿ±Ç`ftriangŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`azŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`caxsŸ±Ç`a[Ÿ±Çbmia0Ÿ±Ç`a]Ÿ±Çaoa.Ÿ±Ç`gtriplotŸ±Ç`a(Ÿ±Ç`ftriangŸ±Ç`a,Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1cko-Ÿ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`caxsŸ±Ç`a[Ÿ±Çbmia0Ÿ±Ç`a]Ÿ±Çaoa.Ÿ±Ç`iset_titleŸ±Ç`a(Ÿ±Çbs1a'Ÿ±Çbs1oTriangular gridŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1x)# Plot linear interpolation to quad grid.Ÿ±Ç`a
Ÿ±Ç`caxsŸ±Ç`a[Ÿ±Çbmia1Ÿ±Ç`a]Ÿ±Çaoa.Ÿ±Ç`hcontourfŸ±Ç`a(Ÿ±Ç`bxiŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`byiŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`fzi_linŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`caxsŸ±Ç`a[Ÿ±Çbmia1Ÿ±Ç`a]Ÿ±Çaoa.Ÿ±Ç`dplotŸ±Ç`a(Ÿ±Ç`bxiŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`byiŸ±Ç`a,Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1bk-Ÿ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`blwŸ±Çaoa=Ÿ±Çbmfc0.5Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ealphaŸ±Çaoa=Ÿ±Çbmfc0.5Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`caxsŸ±Ç`a[Ÿ±Çbmia1Ÿ±Ç`a]Ÿ±Çaoa.Ÿ±Ç`dplotŸ±Ç`a(Ÿ±Ç`bxiŸ±Çaoa.Ÿ±Ç`aTŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`byiŸ±Çaoa.Ÿ±Ç`aTŸ±Ç`a,Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1bk-Ÿ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`blwŸ±Çaoa=Ÿ±Çbmfc0.5Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ealphaŸ±Çaoa=Ÿ±Çbmfc0.5Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`caxsŸ±Ç`a[Ÿ±Çbmia1Ÿ±Ç`a]Ÿ±Çaoa.Ÿ±Ç`iset_titleŸ±Ç`a(Ÿ±Çbs2a"Ÿ±Çbs2tLinear interpolationŸ±Çbs2a"Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1x2# Plot cubic interpolation to quad grid, kind=geomŸ±Ç`a
Ÿ±Ç`caxsŸ±Ç`a[Ÿ±Çbmia2Ÿ±Ç`a]Ÿ±Çaoa.Ÿ±Ç`hcontourfŸ±Ç`a(Ÿ±Ç`bxiŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`byiŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`mzi_cubic_geomŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`caxsŸ±Ç`a[Ÿ±Çbmia2Ÿ±Ç`a]Ÿ±Çaoa.Ÿ±Ç`dplotŸ±Ç`a(Ÿ±Ç`bxiŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`byiŸ±Ç`a,Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1bk-Ÿ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`blwŸ±Çaoa=Ÿ±Çbmfc0.5Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ealphaŸ±Çaoa=Ÿ±Çbmfc0.5Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`caxsŸ±Ç`a[Ÿ±Çbmia2Ÿ±Ç`a]Ÿ±Çaoa.Ÿ±Ç`dplotŸ±Ç`a(Ÿ±Ç`bxiŸ±Çaoa.Ÿ±Ç`aTŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`byiŸ±Çaoa.Ÿ±Ç`aTŸ±Ç`a,Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1bk-Ÿ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`blwŸ±Çaoa=Ÿ±Çbmfc0.5Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ealphaŸ±Çaoa=Ÿ±Çbmfc0.5Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`caxsŸ±Ç`a[Ÿ±Çbmia2Ÿ±Ç`a]Ÿ±Çaoa.Ÿ±Ç`iset_titleŸ±Ç`a(Ÿ±Çbs2a"Ÿ±Çbs2tCubic interpolation,Ÿ±Çbseb\nŸ±Çbs2ekind=Ÿ±Çbs2a'Ÿ±Çbs2dgeomŸ±Çbs2a'Ÿ±Çbs2a"Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1x3# Plot cubic interpolation to quad grid, kind=min_EŸ±Ç`a
Ÿ±Ç`caxsŸ±Ç`a[Ÿ±Çbmia3Ÿ±Ç`a]Ÿ±Çaoa.Ÿ±Ç`hcontourfŸ±Ç`a(Ÿ±Ç`bxiŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`byiŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`nzi_cubic_min_EŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`caxsŸ±Ç`a[Ÿ±Çbmia3Ÿ±Ç`a]Ÿ±Çaoa.Ÿ±Ç`dplotŸ±Ç`a(Ÿ±Ç`bxiŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`byiŸ±Ç`a,Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1bk-Ÿ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`blwŸ±Çaoa=Ÿ±Çbmfc0.5Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ealphaŸ±Çaoa=Ÿ±Çbmfc0.5Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`caxsŸ±Ç`a[Ÿ±Çbmia3Ÿ±Ç`a]Ÿ±Çaoa.Ÿ±Ç`dplotŸ±Ç`a(Ÿ±Ç`bxiŸ±Çaoa.Ÿ±Ç`aTŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`byiŸ±Çaoa.Ÿ±Ç`aTŸ±Ç`a,Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1bk-Ÿ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`blwŸ±Çaoa=Ÿ±Çbmfc0.5Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ealphaŸ±Çaoa=Ÿ±Çbmfc0.5Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`caxsŸ±Ç`a[Ÿ±Çbmia3Ÿ±Ç`a]Ÿ±Çaoa.Ÿ±Ç`iset_titleŸ±Ç`a(Ÿ±Çbs2a"Ÿ±Çbs2tCubic interpolation,Ÿ±Çbseb\nŸ±Çbs2ekind=Ÿ±Çbs2a'Ÿ±Çbs2emin_EŸ±Çbs2a'Ÿ±Çbs2a"Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`cfigŸ±Çaoa.Ÿ±Ç`ltight_layoutŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`dshowŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1xM#############################################################################Ÿ±Ç`a
Ÿ±Çbc1a#Ÿ±Ç`a
Ÿ±Çbc1x# .. admonition:: ReferencesŸ±Ç`a
Ÿ±Çbc1a#Ÿ±Ç`a
Ÿ±Çbc1xN#    The use of the following functions, methods, classes and modules is shownŸ±Ç`a
Ÿ±Çbc1u#    in this example:Ÿ±Ç`a
Ÿ±Çbc1a#Ÿ±Ç`a
Ÿ±Çbc1xK#    - `matplotlib.axes.Axes.tricontourf` / `matplotlib.pyplot.tricontourf`Ÿ±Ç`a
Ÿ±Çbc1xC#    - `matplotlib.axes.Axes.triplot` / `matplotlib.pyplot.triplot`Ÿ±Ç`a
Ÿ±Çbc1xE#    - `matplotlib.axes.Axes.contourf` / `matplotlib.pyplot.contourf`Ÿ±Ç`a
Ÿ±Çbc1x=#    - `matplotlib.axes.Axes.plot` / `matplotlib.pyplot.plot`Ÿ±Ç`a
Ÿ±Çbc1w#    - `matplotlib.tri`Ÿ±Ç`a
Ÿ±Çbc1x-#    - `matplotlib.tri.LinearTriInterpolator`Ÿ±Ç`a
Ÿ±Çbc1x,#    - `matplotlib.tri.CubicTriInterpolator`Ÿ±Ç`a
Ÿ±Çbc1x%#    - `matplotlib.tri.Triangulation`Ÿ±Ç`a
`dNoneˆ