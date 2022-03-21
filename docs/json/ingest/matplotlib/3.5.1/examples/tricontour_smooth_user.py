ŸØÇÅŸ¥ÉôŸ±Çbsdx¬"""
======================
Tricontour Smooth User
======================

Demonstrates high-resolution tricontouring on user-defined triangular grids
with `matplotlib.tri.UniformTriRefiner`.
"""Ÿ±Ç`a
Ÿ±ÇbknfimportŸ±Ç`a Ÿ±ÇbnnŸ¢ÑjmatplotlibŸ†Ñjmatplotlibe3.5.1fmodulejmatplotlibfmoduleıŸ±Çbnna.Ÿ±ÇbnnctriŸ±Ç`a Ÿ±ÇakbasŸ±Ç`a Ÿ±ÇbnnctriŸ±Ç`a
Ÿ±ÇbknfimportŸ±Ç`a Ÿ±ÇbnnŸ¢ÑjmatplotlibŸ†Ñjmatplotlibe3.5.1fmodulejmatplotlibfmoduleıŸ±Çbnna.Ÿ±ÇbnnfpyplotŸ±Ç`a Ÿ±ÇakbasŸ±Ç`a Ÿ±ÇbnncpltŸ±Ç`a
Ÿ±ÇbknfimportŸ±Ç`a Ÿ±ÇbnnŸ¢ÑenumpyŸ†Ñenumpyf1.22.3fmoduleenumpyfmoduleıŸ±Ç`a Ÿ±ÇakbasŸ±Ç`a Ÿ±ÇbnnbnpŸ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1xN# ----------------------------------------------------------------------------Ÿ±Ç`a
Ÿ±Çbc1x# Analytical test functionŸ±Ç`a
Ÿ±Çbc1xN# ----------------------------------------------------------------------------Ÿ±Ç`a
Ÿ±ÇakcdefŸ±Ç`a Ÿ±Çbnfjfunction_zŸ±Ç`a(Ÿ±Ç`axŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ayŸ±Ç`a)Ÿ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`br1Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`dsqrtŸ±Ç`a(Ÿ±Ç`a(Ÿ±Çbmfc0.5Ÿ±Ç`a Ÿ±Çaoa-Ÿ±Ç`a Ÿ±Ç`axŸ±Ç`a)Ÿ±Çaoa*Ÿ±Çaoa*Ÿ±Çbmia2Ÿ±Ç`a Ÿ±Çaoa+Ÿ±Ç`a Ÿ±Ç`a(Ÿ±Çbmfc0.5Ÿ±Ç`a Ÿ±Çaoa-Ÿ±Ç`a Ÿ±Ç`ayŸ±Ç`a)Ÿ±Çaoa*Ÿ±Çaoa*Ÿ±Çbmia2Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`ftheta1Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`garctan2Ÿ±Ç`a(Ÿ±Çbmfc0.5Ÿ±Ç`a Ÿ±Çaoa-Ÿ±Ç`a Ÿ±Ç`axŸ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfc0.5Ÿ±Ç`a Ÿ±Çaoa-Ÿ±Ç`a Ÿ±Ç`ayŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`br2Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`dsqrtŸ±Ç`a(Ÿ±Ç`a(Ÿ±Çaoa-Ÿ±Ç`axŸ±Ç`a Ÿ±Çaoa-Ÿ±Ç`a Ÿ±Çbmfc0.2Ÿ±Ç`a)Ÿ±Çaoa*Ÿ±Çaoa*Ÿ±Çbmia2Ÿ±Ç`a Ÿ±Çaoa+Ÿ±Ç`a Ÿ±Ç`a(Ÿ±Çaoa-Ÿ±Ç`ayŸ±Ç`a Ÿ±Çaoa-Ÿ±Ç`a Ÿ±Çbmfc0.2Ÿ±Ç`a)Ÿ±Çaoa*Ÿ±Çaoa*Ÿ±Çbmia2Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`ftheta2Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`garctan2Ÿ±Ç`a(Ÿ±Çaoa-Ÿ±Ç`axŸ±Ç`a Ÿ±Çaoa-Ÿ±Ç`a Ÿ±Çbmfc0.2Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çaoa-Ÿ±Ç`ayŸ±Ç`a Ÿ±Çaoa-Ÿ±Ç`a Ÿ±Çbmfc0.2Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`azŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Çaoa-Ÿ±Ç`a(Ÿ±Çbmia2Ÿ±Ç`a Ÿ±Çaoa*Ÿ±Ç`a Ÿ±Ç`a(Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`cexpŸ±Ç`a(Ÿ±Ç`a(Ÿ±Ç`br1Ÿ±Ç`a Ÿ±Çaoa/Ÿ±Ç`a Ÿ±Çbmib10Ÿ±Ç`a)Ÿ±Çaoa*Ÿ±Çaoa*Ÿ±Çbmia2Ÿ±Ç`a)Ÿ±Ç`a Ÿ±Çaoa-Ÿ±Ç`a Ÿ±Çbmia1Ÿ±Ç`a)Ÿ±Ç`a Ÿ±Çaoa*Ÿ±Ç`a Ÿ±Çbmfc30.Ÿ±Ç`a Ÿ±Çaoa*Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`ccosŸ±Ç`a(Ÿ±Çbmfb7.Ÿ±Ç`a Ÿ±Çaoa*Ÿ±Ç`a Ÿ±Ç`ftheta1Ÿ±Ç`a)Ÿ±Ç`a Ÿ±Çaoa+Ÿ±Ç`a
Ÿ±Ç`j          Ÿ±Ç`a(Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`cexpŸ±Ç`a(Ÿ±Ç`a(Ÿ±Ç`br2Ÿ±Ç`a Ÿ±Çaoa/Ÿ±Ç`a Ÿ±Çbmib10Ÿ±Ç`a)Ÿ±Çaoa*Ÿ±Çaoa*Ÿ±Çbmia2Ÿ±Ç`a)Ÿ±Ç`a Ÿ±Çaoa-Ÿ±Ç`a Ÿ±Çbmia1Ÿ±Ç`a)Ÿ±Ç`a Ÿ±Çaoa*Ÿ±Ç`a Ÿ±Çbmfc30.Ÿ±Ç`a Ÿ±Çaoa*Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`ccosŸ±Ç`a(Ÿ±Çbmfc11.Ÿ±Ç`a Ÿ±Çaoa*Ÿ±Ç`a Ÿ±Ç`ftheta2Ÿ±Ç`a)Ÿ±Ç`a Ÿ±Çaoa+Ÿ±Ç`a
Ÿ±Ç`j          Ÿ±Çbmfc0.7Ÿ±Ç`a Ÿ±Çaoa*Ÿ±Ç`a Ÿ±Ç`a(Ÿ±Ç`axŸ±Çaoa*Ÿ±Çaoa*Ÿ±Çbmia2Ÿ±Ç`a Ÿ±Çaoa+Ÿ±Ç`a Ÿ±Ç`ayŸ±Çaoa*Ÿ±Çaoa*Ÿ±Çbmia2Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±ÇakfreturnŸ±Ç`a Ÿ±Ç`a(Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`cmaxŸ±Ç`a(Ÿ±Ç`azŸ±Ç`a)Ÿ±Ç`a Ÿ±Çaoa-Ÿ±Ç`a Ÿ±Ç`azŸ±Ç`a)Ÿ±Ç`a Ÿ±Çaoa/Ÿ±Ç`a Ÿ±Ç`a(Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`cmaxŸ±Ç`a(Ÿ±Ç`azŸ±Ç`a)Ÿ±Ç`a Ÿ±Çaoa-Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`cminŸ±Ç`a(Ÿ±Ç`azŸ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1xN# ----------------------------------------------------------------------------Ÿ±Ç`a
Ÿ±Çbc1x# Creating a TriangulationŸ±Ç`a
Ÿ±Çbc1xN# ----------------------------------------------------------------------------Ÿ±Ç`a
Ÿ±Çbc1x5# First create the x and y coordinates of the points.Ÿ±Ç`a
Ÿ±Ç`hn_anglesŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Çbmib20Ÿ±Ç`a
Ÿ±Ç`gn_radiiŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Çbmib10Ÿ±Ç`a
Ÿ±Ç`jmin_radiusŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Çbmfd0.15Ÿ±Ç`a
Ÿ±Ç`eradiiŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`hlinspaceŸ±Ç`a(Ÿ±Ç`jmin_radiusŸ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd0.95Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`gn_radiiŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`fanglesŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`hlinspaceŸ±Ç`a(Ÿ±Çbmia0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia2Ÿ±Ç`a Ÿ±Çaoa*Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`bpiŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`hn_anglesŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`hendpointŸ±Çaoa=Ÿ±ÇbkceFalseŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`fanglesŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`frepeatŸ±Ç`a(Ÿ±Ç`fanglesŸ±Ç`a[Ÿ±Çaoa.Ÿ±Çaoa.Ÿ±Çaoa.Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`gnewaxisŸ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`gn_radiiŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`daxisŸ±Çaoa=Ÿ±Çbmia1Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`fanglesŸ±Ç`a[Ÿ±Ç`a:Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia1Ÿ±Ç`a:Ÿ±Ç`a:Ÿ±Çbmia2Ÿ±Ç`a]Ÿ±Ç`a Ÿ±Çaoa+Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`bpiŸ±Ç`a Ÿ±Çaoa/Ÿ±Ç`a Ÿ±Ç`hn_anglesŸ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`axŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`a(Ÿ±Ç`eradiiŸ±Ç`a Ÿ±Çaoa*Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`ccosŸ±Ç`a(Ÿ±Ç`fanglesŸ±Ç`a)Ÿ±Ç`a)Ÿ±Çaoa.Ÿ±Ç`gflattenŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`ayŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`a(Ÿ±Ç`eradiiŸ±Ç`a Ÿ±Çaoa*Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`csinŸ±Ç`a(Ÿ±Ç`fanglesŸ±Ç`a)Ÿ±Ç`a)Ÿ±Çaoa.Ÿ±Ç`gflattenŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`azŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`jfunction_zŸ±Ç`a(Ÿ±Ç`axŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ayŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1x# Now create the Triangulation.Ÿ±Ç`a
Ÿ±Çbc1xK# (Creating a Triangulation without specifying the triangles results in theŸ±Ç`a
Ÿ±Çbc1x(# Delaunay triangulation of the points.)Ÿ±Ç`a
Ÿ±Ç`ftriangŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`ctriŸ±Çaoa.Ÿ±Ç`mTriangulationŸ±Ç`a(Ÿ±Ç`axŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ayŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1x# Mask off unwanted triangles.Ÿ±Ç`a
Ÿ±Ç`ftriangŸ±Çaoa.Ÿ±Ç`hset_maskŸ±Ç`a(Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`ehypotŸ±Ç`a(Ÿ±Ç`axŸ±Ç`a[Ÿ±Ç`ftriangŸ±Çaoa.Ÿ±Ç`itrianglesŸ±Ç`a]Ÿ±Çaoa.Ÿ±Ç`dmeanŸ±Ç`a(Ÿ±Ç`daxisŸ±Çaoa=Ÿ±Çbmia1Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`x                         Ÿ±Ç`ayŸ±Ç`a[Ÿ±Ç`ftriangŸ±Çaoa.Ÿ±Ç`itrianglesŸ±Ç`a]Ÿ±Çaoa.Ÿ±Ç`dmeanŸ±Ç`a(Ÿ±Ç`daxisŸ±Çaoa=Ÿ±Çbmia1Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`p                Ÿ±Çaoa<Ÿ±Ç`a Ÿ±Ç`jmin_radiusŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1xN# ----------------------------------------------------------------------------Ÿ±Ç`a
Ÿ±Çbc1m# Refine dataŸ±Ç`a
Ÿ±Çbc1xN# ----------------------------------------------------------------------------Ÿ±Ç`a
Ÿ±Ç`grefinerŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`ctriŸ±Çaoa.Ÿ±Ç`qUniformTriRefinerŸ±Ç`a(Ÿ±Ç`ftriangŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`htri_refiŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`kz_test_refiŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`grefinerŸ±Çaoa.Ÿ±Ç`lrefine_fieldŸ±Ç`a(Ÿ±Ç`azŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`fsubdivŸ±Çaoa=Ÿ±Çbmia3Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1xN# ----------------------------------------------------------------------------Ÿ±Ç`a
Ÿ±Çbc1x6# Plot the triangulation and the high-res iso-contoursŸ±Ç`a
Ÿ±Çbc1xN# ----------------------------------------------------------------------------Ÿ±Ç`a
Ÿ±Ç`cfigŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`baxŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`hsubplotsŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`jset_aspectŸ±Ç`a(Ÿ±Çbs1a'Ÿ±Çbs1eequalŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`gtriplotŸ±Ç`a(Ÿ±Ç`ftriangŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`blwŸ±Çaoa=Ÿ±Çbmfc0.5Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ecolorŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1ewhiteŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`flevelsŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`farangeŸ±Ç`a(Ÿ±Çbmfb0.Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfb1.Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfe0.025Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`ktricontourfŸ±Ç`a(Ÿ±Ç`htri_refiŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`kz_test_refiŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`flevelsŸ±Çaoa=Ÿ±Ç`flevelsŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dcmapŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1gterrainŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`jtricontourŸ±Ç`a(Ÿ±Ç`htri_refiŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`kz_test_refiŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`flevelsŸ±Çaoa=Ÿ±Ç`flevelsŸ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`n              Ÿ±Ç`fcolorsŸ±Çaoa=Ÿ±Ç`a[Ÿ±Çbs1a'Ÿ±Çbs1d0.25Ÿ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1c0.5Ÿ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1c0.5Ÿ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1c0.5Ÿ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1c0.5Ÿ±Çbs1a'Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`n              Ÿ±Ç`jlinewidthsŸ±Çaoa=Ÿ±Ç`a[Ÿ±Çbmfc1.0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfc0.5Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfc0.5Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfc0.5Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfc0.5Ÿ±Ç`a]Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`iset_titleŸ±Ç`a(Ÿ±Çbs2a"Ÿ±Çbs2xHigh-resolution tricontouringŸ±Çbs2a"Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`dshowŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1xM#############################################################################Ÿ±Ç`a
Ÿ±Çbc1a#Ÿ±Ç`a
Ÿ±Çbc1x# .. admonition:: ReferencesŸ±Ç`a
Ÿ±Çbc1a#Ÿ±Ç`a
Ÿ±Çbc1xN#    The use of the following functions, methods, classes and modules is shownŸ±Ç`a
Ÿ±Çbc1u#    in this example:Ÿ±Ç`a
Ÿ±Çbc1a#Ÿ±Ç`a
Ÿ±Çbc1xI#    - `matplotlib.axes.Axes.tricontour` / `matplotlib.pyplot.tricontour`Ÿ±Ç`a
Ÿ±Çbc1xK#    - `matplotlib.axes.Axes.tricontourf` / `matplotlib.pyplot.tricontourf`Ÿ±Ç`a
Ÿ±Çbc1w#    - `matplotlib.tri`Ÿ±Ç`a
Ÿ±Çbc1x%#    - `matplotlib.tri.Triangulation`Ÿ±Ç`a
Ÿ±Çbc1x)#    - `matplotlib.tri.UniformTriRefiner`Ÿ±Ç`a
`dNoneˆ