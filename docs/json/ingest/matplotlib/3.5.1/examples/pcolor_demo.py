ŸØÇÅŸ¥Éô÷Ÿ±ÇbsdxΩ"""
===========
Pcolor Demo
===========

Generating images with `~.axes.Axes.pcolor`.

Pcolor allows you to generate 2D image-style plots. Below we will show how
to do so in Matplotlib.
"""Ÿ±Ç`a
Ÿ±ÇbknfimportŸ±Ç`a Ÿ±ÇbnnŸ¢ÑjmatplotlibŸ†Ñjmatplotlibe3.5.1fmodulejmatplotlibfmoduleıŸ±Çbnna.Ÿ±ÇbnnfpyplotŸ±Ç`a Ÿ±ÇakbasŸ±Ç`a Ÿ±ÇbnncpltŸ±Ç`a
Ÿ±ÇbknfimportŸ±Ç`a Ÿ±ÇbnnŸ¢ÑenumpyŸ†Ñenumpyf1.22.3fmoduleenumpyfmoduleıŸ±Ç`a Ÿ±ÇakbasŸ±Ç`a Ÿ±ÇbnnbnpŸ±Ç`a
Ÿ±ÇbkndfromŸ±Ç`a Ÿ±ÇbnnŸ¢ÑjmatplotlibŸ†Ñjmatplotlibe3.5.1fmodulejmatplotlibfmoduleıŸ±Çbnna.Ÿ±ÇbnnfcolorsŸ±Ç`a Ÿ±ÇbknfimportŸ±Ç`a Ÿ±Ç`gLogNormŸ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1x)# Fixing random state for reproducibilityŸ±Ç`a
Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`frandomŸ±Çaoa.Ÿ±Ç`dseedŸ±Ç`a(Ÿ±Çbmih19680801Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1xO###############################################################################Ÿ±Ç`a
Ÿ±Çbc1v# A simple pcolor demoŸ±Ç`a
Ÿ±Çbc1v# --------------------Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`aZŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`frandomŸ±Çaoa.Ÿ±Ç`drandŸ±Ç`a(Ÿ±Çbmia6Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmib10Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`cfigŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`a(Ÿ±Ç`cax0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`cax1Ÿ±Ç`a)Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`hsubplotsŸ±Ç`a(Ÿ±Çbmia2Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia1Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`acŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cax0Ÿ±Çaoa.Ÿ±Ç`fpcolorŸ±Ç`a(Ÿ±Ç`aZŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cax0Ÿ±Çaoa.Ÿ±Ç`iset_titleŸ±Ç`a(Ÿ±Çbs1a'Ÿ±Çbs1qdefault: no edgesŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`acŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cax1Ÿ±Çaoa.Ÿ±Ç`fpcolorŸ±Ç`a(Ÿ±Ç`aZŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`jedgecolorsŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1akŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`jlinewidthsŸ±Çaoa=Ÿ±Çbmia4Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cax1Ÿ±Çaoa.Ÿ±Ç`iset_titleŸ±Ç`a(Ÿ±Çbs1a'Ÿ±Çbs1kthick edgesŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`cfigŸ±Çaoa.Ÿ±Ç`ltight_layoutŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`dshowŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1xO###############################################################################Ÿ±Ç`a
Ÿ±Çbc1x)# Comparing pcolor with similar functionsŸ±Ç`a
Ÿ±Çbc1x)# ---------------------------------------Ÿ±Ç`a
Ÿ±Çbc1a#Ÿ±Ç`a
Ÿ±Çbc1x9# Demonstrates similarities between `~.axes.Axes.pcolor`,Ÿ±Ç`a
Ÿ±Çbc1x4# `~.axes.Axes.pcolormesh`, `~.axes.Axes.imshow` andŸ±Ç`a
Ÿ±Çbc1x;# `~.axes.Axes.pcolorfast` for drawing quadrilateral grids.Ÿ±Ç`a
Ÿ±Çbc1xN# Note that we call ``imshow`` with ``aspect="auto"`` so that it doesn't forceŸ±Ç`a
Ÿ±Çbc1xC# the data pixels to be square (the default is ``aspect="equal"``).Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1x/# make these smaller to increase the resolutionŸ±Ç`a
Ÿ±Ç`bdxŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`bdyŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Çbmfd0.15Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd0.05Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1x*# generate 2 2d grids for the x & y boundsŸ±Ç`a
Ÿ±Ç`ayŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`axŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`emgridŸ±Ç`a[Ÿ±Çaoa-Ÿ±Çbmia3Ÿ±Ç`a:Ÿ±Çbmia3Ÿ±Çaoa+Ÿ±Ç`bdyŸ±Ç`a:Ÿ±Ç`bdyŸ±Ç`a,Ÿ±Ç`a Ÿ±Çaoa-Ÿ±Çbmia3Ÿ±Ç`a:Ÿ±Çbmia3Ÿ±Çaoa+Ÿ±Ç`bdxŸ±Ç`a:Ÿ±Ç`bdxŸ±Ç`a]Ÿ±Ç`a
Ÿ±Ç`azŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`a(Ÿ±Çbmia1Ÿ±Ç`a Ÿ±Çaoa-Ÿ±Ç`a Ÿ±Ç`axŸ±Çaoa/Ÿ±Çbmia2Ÿ±Ç`a Ÿ±Çaoa+Ÿ±Ç`a Ÿ±Ç`axŸ±Çaoa*Ÿ±Çaoa*Ÿ±Çbmia5Ÿ±Ç`a Ÿ±Çaoa+Ÿ±Ç`a Ÿ±Ç`ayŸ±Çaoa*Ÿ±Çaoa*Ÿ±Çbmia3Ÿ±Ç`a)Ÿ±Ç`a Ÿ±Çaoa*Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`cexpŸ±Ç`a(Ÿ±Çaoa-Ÿ±Ç`axŸ±Çaoa*Ÿ±Çaoa*Ÿ±Çbmia2Ÿ±Ç`a Ÿ±Çaoa-Ÿ±Ç`a Ÿ±Ç`ayŸ±Çaoa*Ÿ±Çaoa*Ÿ±Çbmia2Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Çbc1xE# x and y are bounds, so z should be the value *inside* those bounds.Ÿ±Ç`a
Ÿ±Çbc1x4# Therefore, remove the last value from the z array.Ÿ±Ç`a
Ÿ±Ç`azŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`azŸ±Ç`a[Ÿ±Ç`a:Ÿ±Çaoa-Ÿ±Çbmia1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`a:Ÿ±Çaoa-Ÿ±Çbmia1Ÿ±Ç`a]Ÿ±Ç`a
Ÿ±Ç`ez_minŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ez_maxŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Çaoa-Ÿ±ÇbnbcabsŸ±Ç`a(Ÿ±Ç`azŸ±Ç`a)Ÿ±Çaoa.Ÿ±Ç`cmaxŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±ÇbnbcabsŸ±Ç`a(Ÿ±Ç`azŸ±Ç`a)Ÿ±Çaoa.Ÿ±Ç`cmaxŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`cfigŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`caxsŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`hsubplotsŸ±Ç`a(Ÿ±Çbmia2Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia2Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`baxŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`caxsŸ±Ç`a[Ÿ±Çbmia0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia0Ÿ±Ç`a]Ÿ±Ç`a
Ÿ±Ç`acŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`fpcolorŸ±Ç`a(Ÿ±Ç`axŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ayŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`azŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dcmapŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1dRdBuŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dvminŸ±Çaoa=Ÿ±Ç`ez_minŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dvmaxŸ±Çaoa=Ÿ±Ç`ez_maxŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`iset_titleŸ±Ç`a(Ÿ±Çbs1a'Ÿ±Çbs1fpcolorŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cfigŸ±Çaoa.Ÿ±Ç`hcolorbarŸ±Ç`a(Ÿ±Ç`acŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`baxŸ±Çaoa=Ÿ±Ç`baxŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`baxŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`caxsŸ±Ç`a[Ÿ±Çbmia0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia1Ÿ±Ç`a]Ÿ±Ç`a
Ÿ±Ç`acŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`jpcolormeshŸ±Ç`a(Ÿ±Ç`axŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ayŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`azŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dcmapŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1dRdBuŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dvminŸ±Çaoa=Ÿ±Ç`ez_minŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dvmaxŸ±Çaoa=Ÿ±Ç`ez_maxŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`iset_titleŸ±Ç`a(Ÿ±Çbs1a'Ÿ±Çbs1jpcolormeshŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cfigŸ±Çaoa.Ÿ±Ç`hcolorbarŸ±Ç`a(Ÿ±Ç`acŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`baxŸ±Çaoa=Ÿ±Ç`baxŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`baxŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`caxsŸ±Ç`a[Ÿ±Çbmia1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia0Ÿ±Ç`a]Ÿ±Ç`a
Ÿ±Ç`acŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`fimshowŸ±Ç`a(Ÿ±Ç`azŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dcmapŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1dRdBuŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dvminŸ±Çaoa=Ÿ±Ç`ez_minŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dvmaxŸ±Çaoa=Ÿ±Ç`ez_maxŸ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`n              Ÿ±Ç`fextentŸ±Çaoa=Ÿ±Ç`a[Ÿ±Ç`axŸ±Çaoa.Ÿ±Ç`cminŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`axŸ±Çaoa.Ÿ±Ç`cmaxŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ayŸ±Çaoa.Ÿ±Ç`cminŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ayŸ±Çaoa.Ÿ±Ç`cmaxŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`n              Ÿ±Ç`minterpolationŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1gnearestŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`foriginŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1elowerŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`faspectŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1dautoŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`iset_titleŸ±Ç`a(Ÿ±Çbs1a'Ÿ±Çbs1wimage (nearest, aspect=Ÿ±Çbs1a"Ÿ±Çbs1dautoŸ±Çbs1a"Ÿ±Çbs1a)Ÿ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cfigŸ±Çaoa.Ÿ±Ç`hcolorbarŸ±Ç`a(Ÿ±Ç`acŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`baxŸ±Çaoa=Ÿ±Ç`baxŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`baxŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`caxsŸ±Ç`a[Ÿ±Çbmia1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia1Ÿ±Ç`a]Ÿ±Ç`a
Ÿ±Ç`acŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`jpcolorfastŸ±Ç`a(Ÿ±Ç`axŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ayŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`azŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dcmapŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1dRdBuŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dvminŸ±Çaoa=Ÿ±Ç`ez_minŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dvmaxŸ±Çaoa=Ÿ±Ç`ez_maxŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`iset_titleŸ±Ç`a(Ÿ±Çbs1a'Ÿ±Çbs1jpcolorfastŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cfigŸ±Çaoa.Ÿ±Ç`hcolorbarŸ±Ç`a(Ÿ±Ç`acŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`baxŸ±Çaoa=Ÿ±Ç`baxŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`cfigŸ±Çaoa.Ÿ±Ç`ltight_layoutŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`dshowŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1xO###############################################################################Ÿ±Ç`a
Ÿ±Çbc1x# Pcolor with a log scaleŸ±Ç`a
Ÿ±Çbc1x# -----------------------Ÿ±Ç`a
Ÿ±Çbc1a#Ÿ±Ç`a
Ÿ±Çbc1x4# The following shows pcolor plots with a log scale.Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`aNŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Çbmic100Ÿ±Ç`a
Ÿ±Ç`aXŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`aYŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`hmeshgridŸ±Ç`a(Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`hlinspaceŸ±Ç`a(Ÿ±Çaoa-Ÿ±Çbmia3Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia3Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`aNŸ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`hlinspaceŸ±Ç`a(Ÿ±Çaoa-Ÿ±Çbmia2Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia2Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`aNŸ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1x%# A low hump with a spike coming out.Ÿ±Ç`a
Ÿ±Çbc1xK# Needs to have z/colour axis on a log scale so we see both hump and spike.Ÿ±Ç`a
Ÿ±Çbc1x$# linear scale only shows the spike.Ÿ±Ç`a
Ÿ±Ç`bZ1Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`cexpŸ±Ç`a(Ÿ±Çaoa-Ÿ±Ç`aXŸ±Çaoa*Ÿ±Çaoa*Ÿ±Çbmia2Ÿ±Ç`a Ÿ±Çaoa-Ÿ±Ç`a Ÿ±Ç`aYŸ±Çaoa*Ÿ±Çaoa*Ÿ±Çbmia2Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`bZ2Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`cexpŸ±Ç`a(Ÿ±Çaoa-Ÿ±Ç`a(Ÿ±Ç`aXŸ±Ç`a Ÿ±Çaoa*Ÿ±Ç`a Ÿ±Çbmib10Ÿ±Ç`a)Ÿ±Çaoa*Ÿ±Çaoa*Ÿ±Çbmia2Ÿ±Ç`a Ÿ±Çaoa-Ÿ±Ç`a Ÿ±Ç`a(Ÿ±Ç`aYŸ±Ç`a Ÿ±Çaoa*Ÿ±Ç`a Ÿ±Çbmib10Ÿ±Ç`a)Ÿ±Çaoa*Ÿ±Çaoa*Ÿ±Çbmia2Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`aZŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bZ1Ÿ±Ç`a Ÿ±Çaoa+Ÿ±Ç`a Ÿ±Çbmib50Ÿ±Ç`a Ÿ±Çaoa*Ÿ±Ç`a Ÿ±Ç`bZ2Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`cfigŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`a(Ÿ±Ç`cax0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`cax1Ÿ±Ç`a)Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`hsubplotsŸ±Ç`a(Ÿ±Çbmia2Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia1Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`acŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cax0Ÿ±Çaoa.Ÿ±Ç`fpcolorŸ±Ç`a(Ÿ±Ç`aXŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`aYŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`aZŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`gshadingŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1dautoŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`o               Ÿ±Ç`dnormŸ±Çaoa=Ÿ±Ç`gLogNormŸ±Ç`a(Ÿ±Ç`dvminŸ±Çaoa=Ÿ±Ç`aZŸ±Çaoa.Ÿ±Ç`cminŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dvmaxŸ±Çaoa=Ÿ±Ç`aZŸ±Çaoa.Ÿ±Ç`cmaxŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dcmapŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1fPuBu_rŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cfigŸ±Çaoa.Ÿ±Ç`hcolorbarŸ±Ç`a(Ÿ±Ç`acŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`baxŸ±Çaoa=Ÿ±Ç`cax0Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`acŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cax1Ÿ±Çaoa.Ÿ±Ç`fpcolorŸ±Ç`a(Ÿ±Ç`aXŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`aYŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`aZŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dcmapŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1fPuBu_rŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`gshadingŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1dautoŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cfigŸ±Çaoa.Ÿ±Ç`hcolorbarŸ±Ç`a(Ÿ±Ç`acŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`baxŸ±Çaoa=Ÿ±Ç`cax1Ÿ±Ç`a)Ÿ±Ç`a
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
Ÿ±Çbc1xA#    - `matplotlib.axes.Axes.pcolor` / `matplotlib.pyplot.pcolor`Ÿ±Ç`a
Ÿ±Çbc1xI#    - `matplotlib.axes.Axes.pcolormesh` / `matplotlib.pyplot.pcolormesh`Ÿ±Ç`a
Ÿ±Çbc1x(#    - `matplotlib.axes.Axes.pcolorfast`Ÿ±Ç`a
Ÿ±Çbc1xA#    - `matplotlib.axes.Axes.imshow` / `matplotlib.pyplot.imshow`Ÿ±Ç`a
Ÿ±Çbc1xI#    - `matplotlib.figure.Figure.colorbar` / `matplotlib.pyplot.colorbar`Ÿ±Ç`a
Ÿ±Çbc1x"#    - `matplotlib.colors.LogNorm`Ÿ±Ç`a
`dNoneˆ