ŸØÇÅŸ¥ÉôçŸ±Çbsdx©"""
==========
pcolormesh
==========

`.axes.Axes.pcolormesh` allows you to generate 2D image-style plots.  Note it
is faster than the similar `~.axes.Axes.pcolor`.

"""Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±ÇbknfimportŸ±Ç`a Ÿ±ÇbnnŸ¢ÑjmatplotlibŸ†Ñjmatplotlibe3.5.1fmodulejmatplotlibfmoduleıŸ±Çbnna.Ÿ±ÇbnnfpyplotŸ±Ç`a Ÿ±ÇakbasŸ±Ç`a Ÿ±ÇbnncpltŸ±Ç`a
Ÿ±ÇbkndfromŸ±Ç`a Ÿ±ÇbnnŸ¢ÑjmatplotlibŸ†Ñjmatplotlibe3.5.1fmodulejmatplotlibfmoduleıŸ±Çbnna.Ÿ±ÇbnnfcolorsŸ±Ç`a Ÿ±ÇbknfimportŸ±Ç`a Ÿ±Ç`lBoundaryNormŸ±Ç`a
Ÿ±ÇbkndfromŸ±Ç`a Ÿ±ÇbnnŸ¢ÑjmatplotlibŸ†Ñjmatplotlibe3.5.1fmodulejmatplotlibfmoduleıŸ±Çbnna.Ÿ±ÇbnnftickerŸ±Ç`a Ÿ±ÇbknfimportŸ±Ç`a Ÿ±Ç`kMaxNLocatorŸ±Ç`a
Ÿ±ÇbknfimportŸ±Ç`a Ÿ±ÇbnnŸ¢ÑenumpyŸ†Ñenumpyf1.22.3fmoduleenumpyfmoduleıŸ±Ç`a Ÿ±ÇakbasŸ±Ç`a Ÿ±ÇbnnbnpŸ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1xO###############################################################################Ÿ±Ç`a
Ÿ±Çbc1r# Basic pcolormeshŸ±Ç`a
Ÿ±Çbc1r# ----------------Ÿ±Ç`a
Ÿ±Çbc1a#Ÿ±Ç`a
Ÿ±Çbc1xL# We usually specify a pcolormesh by defining the edge of quadrilaterals andŸ±Ç`a
Ÿ±Çbc1xK# the value of the quadrilateral.  Note that here *x* and *y* each have oneŸ±Ç`a
Ÿ±Çbc1x3# extra element than Z in the respective dimension.Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`frandomŸ±Çaoa.Ÿ±Ç`dseedŸ±Ç`a(Ÿ±Çbmih19680801Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`aZŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`frandomŸ±Çaoa.Ÿ±Ç`drandŸ±Ç`a(Ÿ±Çbmia6Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmib10Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`axŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`farangeŸ±Ç`a(Ÿ±Çaoa-Ÿ±Çbmfc0.5Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmib10Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia1Ÿ±Ç`a)Ÿ±Ç`b  Ÿ±Çbc1j# len = 11Ÿ±Ç`a
Ÿ±Ç`ayŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`farangeŸ±Ç`a(Ÿ±Çbmfc4.5Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmib11Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia1Ÿ±Ç`a)Ÿ±Ç`b  Ÿ±Çbc1i# len = 7Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`cfigŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`baxŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`hsubplotsŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`jpcolormeshŸ±Ç`a(Ÿ±Ç`axŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ayŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`aZŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1xO###############################################################################Ÿ±Ç`a
Ÿ±Çbc1x# Non-rectilinear pcolormeshŸ±Ç`a
Ÿ±Çbc1x# --------------------------Ÿ±Ç`a
Ÿ±Çbc1a#Ÿ±Ç`a
Ÿ±Çbc1xA# Note that we can also specify matrices for *X* and *Y* and haveŸ±Ç`a
Ÿ±Çbc1x!# non-rectilinear quadrilaterals.Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`axŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`farangeŸ±Ç`a(Ÿ±Çaoa-Ÿ±Çbmfc0.5Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmib10Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia1Ÿ±Ç`a)Ÿ±Ç`b  Ÿ±Çbc1j# len = 11Ÿ±Ç`a
Ÿ±Ç`ayŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`farangeŸ±Ç`a(Ÿ±Çbmfc4.5Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmib11Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia1Ÿ±Ç`a)Ÿ±Ç`b  Ÿ±Çbc1i# len = 7Ÿ±Ç`a
Ÿ±Ç`aXŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`aYŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`hmeshgridŸ±Ç`a(Ÿ±Ç`axŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ayŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`aXŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`aXŸ±Ç`a Ÿ±Çaoa+Ÿ±Ç`a Ÿ±Çbmfc0.2Ÿ±Ç`a Ÿ±Çaoa*Ÿ±Ç`a Ÿ±Ç`aYŸ±Ç`b  Ÿ±Çbc1w# tilt the coordinates.Ÿ±Ç`a
Ÿ±Ç`aYŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`aYŸ±Ç`a Ÿ±Çaoa+Ÿ±Ç`a Ÿ±Çbmfc0.3Ÿ±Ç`a Ÿ±Çaoa*Ÿ±Ç`a Ÿ±Ç`aXŸ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`cfigŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`baxŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`hsubplotsŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`jpcolormeshŸ±Ç`a(Ÿ±Ç`aXŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`aYŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`aZŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1xO###############################################################################Ÿ±Ç`a
Ÿ±Çbc1v# Centered CoordinatesŸ±Ç`a
Ÿ±Çbc1w# ---------------------Ÿ±Ç`a
Ÿ±Çbc1a#Ÿ±Ç`a
Ÿ±Çbc1xF# Often a user wants to pass *X* and *Y* with the same sizes as *Z* toŸ±Ç`a
Ÿ±Çbc1xH# `.axes.Axes.pcolormesh`. This is also allowed if ``shading='auto'`` isŸ±Ç`a
Ÿ±Çbc1xC# passed (default set by :rc:`pcolor.shading`). Pre Matplotlib 3.3,Ÿ±Ç`a
Ÿ±Çbc1xJ# ``shading='flat'`` would drop the last column and row of *Z*; while thatŸ±Ç`a
Ÿ±Çbc1xK# is still allowed for back compatibility purposes, a DeprecationWarning isŸ±Ç`a
Ÿ±Çbc1xL# raised. If this is really what you want, then simply drop the last row andŸ±Ç`a
Ÿ±Çbc1w# column of Z manually:Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`axŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`farangeŸ±Ç`a(Ÿ±Çbmib10Ÿ±Ç`a)Ÿ±Ç`b  Ÿ±Çbc1j# len = 10Ÿ±Ç`a
Ÿ±Ç`ayŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`farangeŸ±Ç`a(Ÿ±Çbmia6Ÿ±Ç`a)Ÿ±Ç`b  Ÿ±Çbc1i# len = 6Ÿ±Ç`a
Ÿ±Ç`aXŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`aYŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`hmeshgridŸ±Ç`a(Ÿ±Ç`axŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ayŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`cfigŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`caxsŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`hsubplotsŸ±Ç`a(Ÿ±Çbmia2Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`fsharexŸ±Çaoa=Ÿ±ÇbkcdTrueŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`fshareyŸ±Çaoa=Ÿ±ÇbkcdTrueŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`caxsŸ±Ç`a[Ÿ±Çbmia0Ÿ±Ç`a]Ÿ±Çaoa.Ÿ±Ç`jpcolormeshŸ±Ç`a(Ÿ±Ç`aXŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`aYŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`aZŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dvminŸ±Çaoa=Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`cminŸ±Ç`a(Ÿ±Ç`aZŸ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dvmaxŸ±Çaoa=Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`cmaxŸ±Ç`a(Ÿ±Ç`aZŸ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`gshadingŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1dautoŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`caxsŸ±Ç`a[Ÿ±Çbmia0Ÿ±Ç`a]Ÿ±Çaoa.Ÿ±Ç`iset_titleŸ±Ç`a(Ÿ±Çbs2a"Ÿ±Çbs2hshading=Ÿ±Çbs2a'Ÿ±Çbs2dautoŸ±Çbs2a'Ÿ±Çbs2c = Ÿ±Çbs2a'Ÿ±Çbs2gnearestŸ±Çbs2a'Ÿ±Çbs2a"Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`caxsŸ±Ç`a[Ÿ±Çbmia1Ÿ±Ç`a]Ÿ±Çaoa.Ÿ±Ç`jpcolormeshŸ±Ç`a(Ÿ±Ç`aXŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`aYŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`aZŸ±Ç`a[Ÿ±Ç`a:Ÿ±Çaoa-Ÿ±Çbmia1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`a:Ÿ±Çaoa-Ÿ±Çbmia1Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dvminŸ±Çaoa=Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`cminŸ±Ç`a(Ÿ±Ç`aZŸ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dvmaxŸ±Çaoa=Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`cmaxŸ±Ç`a(Ÿ±Ç`aZŸ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`r                  Ÿ±Ç`gshadingŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1dflatŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`caxsŸ±Ç`a[Ÿ±Çbmia1Ÿ±Ç`a]Ÿ±Çaoa.Ÿ±Ç`iset_titleŸ±Ç`a(Ÿ±Çbs2a"Ÿ±Çbs2hshading=Ÿ±Çbs2a'Ÿ±Çbs2dflatŸ±Çbs2a'Ÿ±Çbs2a"Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1xO###############################################################################Ÿ±Ç`a
Ÿ±Çbc1x# Making levels using NormsŸ±Ç`a
Ÿ±Çbc1x# -------------------------Ÿ±Ç`a
Ÿ±Çbc1a#Ÿ±Ç`a
Ÿ±Çbc1xC# Shows how to combine Normalization and Colormap instances to drawŸ±Ç`a
Ÿ±Çbc1x:# "levels" in `.axes.Axes.pcolor`, `.axes.Axes.pcolormesh`Ÿ±Ç`a
Ÿ±Çbc1x1# and `.axes.Axes.imshow` type plots in a similarŸ±Ç`a
Ÿ±Çbc1x9# way to the levels keyword argument to contour/contourf.Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1x/# make these smaller to increase the resolutionŸ±Ç`a
Ÿ±Ç`bdxŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`bdyŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Çbmfd0.05Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd0.05Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1x*# generate 2 2d grids for the x & y boundsŸ±Ç`a
Ÿ±Ç`ayŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`axŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`emgridŸ±Ç`a[Ÿ±ÇbnbesliceŸ±Ç`a(Ÿ±Çbmia1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia5Ÿ±Ç`a Ÿ±Çaoa+Ÿ±Ç`a Ÿ±Ç`bdyŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`bdyŸ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`p                Ÿ±ÇbnbesliceŸ±Ç`a(Ÿ±Çbmia1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia5Ÿ±Ç`a Ÿ±Çaoa+Ÿ±Ç`a Ÿ±Ç`bdxŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`bdxŸ±Ç`a)Ÿ±Ç`a]Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`azŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`csinŸ±Ç`a(Ÿ±Ç`axŸ±Ç`a)Ÿ±Çaoa*Ÿ±Çaoa*Ÿ±Çbmib10Ÿ±Ç`a Ÿ±Çaoa+Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`ccosŸ±Ç`a(Ÿ±Çbmib10Ÿ±Ç`a Ÿ±Çaoa+Ÿ±Ç`a Ÿ±Ç`ayŸ±Çaoa*Ÿ±Ç`axŸ±Ç`a)Ÿ±Ç`a Ÿ±Çaoa*Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`ccosŸ±Ç`a(Ÿ±Ç`axŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1xE# x and y are bounds, so z should be the value *inside* those bounds.Ÿ±Ç`a
Ÿ±Çbc1x4# Therefore, remove the last value from the z array.Ÿ±Ç`a
Ÿ±Ç`azŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`azŸ±Ç`a[Ÿ±Ç`a:Ÿ±Çaoa-Ÿ±Çbmia1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`a:Ÿ±Çaoa-Ÿ±Çbmia1Ÿ±Ç`a]Ÿ±Ç`a
Ÿ±Ç`flevelsŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`kMaxNLocatorŸ±Ç`a(Ÿ±Ç`enbinsŸ±Çaoa=Ÿ±Çbmib15Ÿ±Ç`a)Ÿ±Çaoa.Ÿ±Ç`ktick_valuesŸ±Ç`a(Ÿ±Ç`azŸ±Çaoa.Ÿ±Ç`cminŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`azŸ±Çaoa.Ÿ±Ç`cmaxŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1xH# pick the desired colormap, sensible levels, and define a normalizationŸ±Ç`a
Ÿ±Çbc1xD# instance which takes data values and translates those into levels.Ÿ±Ç`a
Ÿ±Ç`dcmapŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`icolormapsŸ±Ç`a[Ÿ±Çbs1a'Ÿ±Çbs1dPiYGŸ±Çbs1a'Ÿ±Ç`a]Ÿ±Ç`a
Ÿ±Ç`dnormŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`lBoundaryNormŸ±Ç`a(Ÿ±Ç`flevelsŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`gncolorsŸ±Çaoa=Ÿ±Ç`dcmapŸ±Çaoa.Ÿ±Ç`aNŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dclipŸ±Çaoa=Ÿ±ÇbkcdTrueŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`cfigŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`a(Ÿ±Ç`cax0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`cax1Ÿ±Ç`a)Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`hsubplotsŸ±Ç`a(Ÿ±Ç`enrowsŸ±Çaoa=Ÿ±Çbmia2Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`bimŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cax0Ÿ±Çaoa.Ÿ±Ç`jpcolormeshŸ±Ç`a(Ÿ±Ç`axŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ayŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`azŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dcmapŸ±Çaoa=Ÿ±Ç`dcmapŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dnormŸ±Çaoa=Ÿ±Ç`dnormŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cfigŸ±Çaoa.Ÿ±Ç`hcolorbarŸ±Ç`a(Ÿ±Ç`bimŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`baxŸ±Çaoa=Ÿ±Ç`cax0Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cax0Ÿ±Çaoa.Ÿ±Ç`iset_titleŸ±Ç`a(Ÿ±Çbs1a'Ÿ±Çbs1vpcolormesh with levelsŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1xC# contours are *point* based plots, so convert our bound into pointŸ±Ç`a
Ÿ±Çbc1i# centersŸ±Ç`a
Ÿ±Ç`bcfŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cax1Ÿ±Çaoa.Ÿ±Ç`hcontourfŸ±Ç`a(Ÿ±Ç`axŸ±Ç`a[Ÿ±Ç`a:Ÿ±Çaoa-Ÿ±Çbmia1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`a:Ÿ±Çaoa-Ÿ±Çbmia1Ÿ±Ç`a]Ÿ±Ç`a Ÿ±Çaoa+Ÿ±Ç`a Ÿ±Ç`bdxŸ±Çaoa/Ÿ±Çbmfb2.Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`r                  Ÿ±Ç`ayŸ±Ç`a[Ÿ±Ç`a:Ÿ±Çaoa-Ÿ±Çbmia1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`a:Ÿ±Çaoa-Ÿ±Çbmia1Ÿ±Ç`a]Ÿ±Ç`a Ÿ±Çaoa+Ÿ±Ç`a Ÿ±Ç`bdyŸ±Çaoa/Ÿ±Çbmfb2.Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`azŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`flevelsŸ±Çaoa=Ÿ±Ç`flevelsŸ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`r                  Ÿ±Ç`dcmapŸ±Çaoa=Ÿ±Ç`dcmapŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cfigŸ±Çaoa.Ÿ±Ç`hcolorbarŸ±Ç`a(Ÿ±Ç`bcfŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`baxŸ±Çaoa=Ÿ±Ç`cax1Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cax1Ÿ±Çaoa.Ÿ±Ç`iset_titleŸ±Ç`a(Ÿ±Çbs1a'Ÿ±Çbs1tcontourf with levelsŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1xF# adjust spacing between subplots so `ax1` title and `ax0` tick labelsŸ±Ç`a
Ÿ±Çbc1o# don't overlapŸ±Ç`a
Ÿ±Ç`cfigŸ±Çaoa.Ÿ±Ç`ltight_layoutŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
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
Ÿ±Çbc1xI#    - `matplotlib.axes.Axes.pcolormesh` / `matplotlib.pyplot.pcolormesh`Ÿ±Ç`a
Ÿ±Çbc1xE#    - `matplotlib.axes.Axes.contourf` / `matplotlib.pyplot.contourf`Ÿ±Ç`a
Ÿ±Çbc1xI#    - `matplotlib.figure.Figure.colorbar` / `matplotlib.pyplot.colorbar`Ÿ±Ç`a
Ÿ±Çbc1x'#    - `matplotlib.colors.BoundaryNorm`Ÿ±Ç`a
Ÿ±Çbc1x&#    - `matplotlib.ticker.MaxNLocator`Ÿ±Ç`a
`dNoneˆ