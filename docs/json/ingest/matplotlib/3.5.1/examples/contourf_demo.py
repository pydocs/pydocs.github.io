ŸØÇÅŸ¥ÉôíŸ±Çbsdx~"""
=============
Contourf Demo
=============

How to use the `.axes.Axes.contourf` method to create filled contour plots.
"""Ÿ±Ç`a
Ÿ±ÇbknfimportŸ±Ç`a Ÿ±ÇbnnŸ¢ÑenumpyŸ†Ñenumpyf1.22.3fmoduleenumpyfmoduleıŸ±Ç`a Ÿ±ÇakbasŸ±Ç`a Ÿ±ÇbnnbnpŸ±Ç`a
Ÿ±ÇbknfimportŸ±Ç`a Ÿ±ÇbnnŸ¢ÑjmatplotlibŸ†Ñjmatplotlibe3.5.1fmodulejmatplotlibfmoduleıŸ±Çbnna.Ÿ±ÇbnnfpyplotŸ±Ç`a Ÿ±ÇakbasŸ±Ç`a Ÿ±ÇbnncpltŸ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`foriginŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1elowerŸ±Çbs1a'Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`edeltaŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Çbmfe0.025Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`axŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`ayŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`farangeŸ±Ç`a(Ÿ±Çaoa-Ÿ±Çbmfc3.0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd3.01Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`edeltaŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`aXŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`aYŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`hmeshgridŸ±Ç`a(Ÿ±Ç`axŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ayŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`bZ1Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`cexpŸ±Ç`a(Ÿ±Çaoa-Ÿ±Ç`aXŸ±Çaoa*Ÿ±Çaoa*Ÿ±Çbmia2Ÿ±Ç`a Ÿ±Çaoa-Ÿ±Ç`a Ÿ±Ç`aYŸ±Çaoa*Ÿ±Çaoa*Ÿ±Çbmia2Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`bZ2Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`cexpŸ±Ç`a(Ÿ±Çaoa-Ÿ±Ç`a(Ÿ±Ç`aXŸ±Ç`a Ÿ±Çaoa-Ÿ±Ç`a Ÿ±Çbmia1Ÿ±Ç`a)Ÿ±Çaoa*Ÿ±Çaoa*Ÿ±Çbmia2Ÿ±Ç`a Ÿ±Çaoa-Ÿ±Ç`a Ÿ±Ç`a(Ÿ±Ç`aYŸ±Ç`a Ÿ±Çaoa-Ÿ±Ç`a Ÿ±Çbmia1Ÿ±Ç`a)Ÿ±Çaoa*Ÿ±Çaoa*Ÿ±Çbmia2Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`aZŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`a(Ÿ±Ç`bZ1Ÿ±Ç`a Ÿ±Çaoa-Ÿ±Ç`a Ÿ±Ç`bZ2Ÿ±Ç`a)Ÿ±Ç`a Ÿ±Çaoa*Ÿ±Ç`a Ÿ±Çbmia2Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`bnrŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`bncŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`aZŸ±Çaoa.Ÿ±Ç`eshapeŸ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1x# put NaNs in one corner:Ÿ±Ç`a
Ÿ±Ç`aZŸ±Ç`a[Ÿ±Çaoa-Ÿ±Ç`bnrŸ±Ç`a Ÿ±Çaoa/Ÿ±Çaoa/Ÿ±Ç`a Ÿ±Çbmia6Ÿ±Ç`a:Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çaoa-Ÿ±Ç`bncŸ±Ç`a Ÿ±Çaoa/Ÿ±Çaoa/Ÿ±Ç`a Ÿ±Çbmia6Ÿ±Ç`a:Ÿ±Ç`a]Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`cnanŸ±Ç`a
Ÿ±Çbc1x'# contourf will convert these to maskedŸ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`aZŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`bmaŸ±Çaoa.Ÿ±Ç`earrayŸ±Ç`a(Ÿ±Ç`aZŸ±Ç`a)Ÿ±Ç`a
Ÿ±Çbc1v# mask another corner:Ÿ±Ç`a
Ÿ±Ç`aZŸ±Ç`a[Ÿ±Ç`a:Ÿ±Ç`bnrŸ±Ç`a Ÿ±Çaoa/Ÿ±Çaoa/Ÿ±Ç`a Ÿ±Çbmia6Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`a:Ÿ±Ç`bncŸ±Ç`a Ÿ±Çaoa/Ÿ±Çaoa/Ÿ±Ç`a Ÿ±Çbmia6Ÿ±Ç`a]Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`bmaŸ±Çaoa.Ÿ±Ç`fmaskedŸ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1x# mask a circle in the middle:Ÿ±Ç`a
Ÿ±Ç`hinteriorŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`dsqrtŸ±Ç`a(Ÿ±Ç`aXŸ±Çaoa*Ÿ±Çaoa*Ÿ±Çbmia2Ÿ±Ç`a Ÿ±Çaoa+Ÿ±Ç`a Ÿ±Ç`aYŸ±Çaoa*Ÿ±Çaoa*Ÿ±Çbmia2Ÿ±Ç`a)Ÿ±Ç`a Ÿ±Çaoa<Ÿ±Ç`a Ÿ±Çbmfc0.5Ÿ±Ç`a
Ÿ±Ç`aZŸ±Ç`a[Ÿ±Ç`hinteriorŸ±Ç`a]Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`bmaŸ±Çaoa.Ÿ±Ç`fmaskedŸ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1xM#############################################################################Ÿ±Ç`a
Ÿ±Çbc1x# Automatic contour levelsŸ±Ç`a
Ÿ±Çbc1x# ------------------------Ÿ±Ç`a
Ÿ±Çbc1xN# We are using automatic selection of contour levels; this is usually not suchŸ±Ç`a
Ÿ±Çbc1xM# a good idea, because they don't occur on nice boundaries, but we do it hereŸ±Ç`a
Ÿ±Çbc1x# for purposes of illustration.Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`dfig1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`cax2Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`hsubplotsŸ±Ç`a(Ÿ±Ç`rconstrained_layoutŸ±Çaoa=Ÿ±ÇbkcdTrueŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`bCSŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cax2Ÿ±Çaoa.Ÿ±Ç`hcontourfŸ±Ç`a(Ÿ±Ç`aXŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`aYŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`aZŸ±Ç`a,Ÿ±Ç`a Ÿ±Çbmib10Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dcmapŸ±Çaoa=Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`bcmŸ±Çaoa.Ÿ±Ç`dboneŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`foriginŸ±Çaoa=Ÿ±Ç`foriginŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1xK# Note that in the following, we explicitly pass in a subset of the contourŸ±Ç`a
Ÿ±Çbc1xG# levels used for the filled contours.  Alternatively, we could pass inŸ±Ç`a
Ÿ±Çbc1xJ# additional levels to provide extra resolution, or leave out the *levels*Ÿ±Ç`a
Ÿ±Çbc1x5# keyword argument to use all of the original levels.Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`cCS2Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cax2Ÿ±Çaoa.Ÿ±Ç`gcontourŸ±Ç`a(Ÿ±Ç`bCSŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`flevelsŸ±Çaoa=Ÿ±Ç`bCSŸ±Çaoa.Ÿ±Ç`flevelsŸ±Ç`a[Ÿ±Ç`a:Ÿ±Ç`a:Ÿ±Çbmia2Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`fcolorsŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1arŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`foriginŸ±Çaoa=Ÿ±Ç`foriginŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`cax2Ÿ±Çaoa.Ÿ±Ç`iset_titleŸ±Ç`a(Ÿ±Çbs1a'Ÿ±Çbs1xNonsense (3 masked regions)Ÿ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cax2Ÿ±Çaoa.Ÿ±Ç`jset_xlabelŸ±Ç`a(Ÿ±Çbs1a'Ÿ±Çbs1sword length anomalyŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cax2Ÿ±Çaoa.Ÿ±Ç`jset_ylabelŸ±Ç`a(Ÿ±Çbs1a'Ÿ±Çbs1wsentence length anomalyŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1xC# Make a colorbar for the ContourSet returned by the contourf call.Ÿ±Ç`a
Ÿ±Ç`dcbarŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`dfig1Ÿ±Çaoa.Ÿ±Ç`hcolorbarŸ±Ç`a(Ÿ±Ç`bCSŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`dcbarŸ±Çaoa.Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`jset_ylabelŸ±Ç`a(Ÿ±Çbs1a'Ÿ±Çbs1uverbosity coefficientŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Çbc1x-# Add the contour line levels to the colorbarŸ±Ç`a
Ÿ±Ç`dcbarŸ±Çaoa.Ÿ±Ç`iadd_linesŸ±Ç`a(Ÿ±Ç`cCS2Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1xM#############################################################################Ÿ±Ç`a
Ÿ±Çbc1x# Explicit contour levelsŸ±Ç`a
Ÿ±Çbc1x# -----------------------Ÿ±Ç`a
Ÿ±Çbc1xJ# Now make a contour plot with the levels specified, and with the colormapŸ±Ç`a
Ÿ±Çbc1x0# generated automatically from a list of colors.Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`dfig2Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`cax2Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`hsubplotsŸ±Ç`a(Ÿ±Ç`rconstrained_layoutŸ±Çaoa=Ÿ±ÇbkcdTrueŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`flevelsŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`a[Ÿ±Çaoa-Ÿ±Çbmfc1.5Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çaoa-Ÿ±Çbmia1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çaoa-Ÿ±Çbmfc0.5Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfc0.5Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia1Ÿ±Ç`a]Ÿ±Ç`a
Ÿ±Ç`cCS3Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cax2Ÿ±Çaoa.Ÿ±Ç`hcontourfŸ±Ç`a(Ÿ±Ç`aXŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`aYŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`aZŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`flevelsŸ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`s                   Ÿ±Ç`fcolorsŸ±Çaoa=Ÿ±Ç`a(Ÿ±Çbs1a'Ÿ±Çbs1arŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1agŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1abŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`s                   Ÿ±Ç`foriginŸ±Çaoa=Ÿ±Ç`foriginŸ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`s                   Ÿ±Ç`fextendŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1dbothŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Çbc1x:# Our data range extends outside the range of levels; makeŸ±Ç`a
Ÿ±Çbc1x;# data below the lowest contour level yellow, and above theŸ±Ç`a
Ÿ±Çbc1u# highest level cyan:Ÿ±Ç`a
Ÿ±Ç`cCS3Ÿ±Çaoa.Ÿ±Ç`dcmapŸ±Çaoa.Ÿ±Ç`iset_underŸ±Ç`a(Ÿ±Çbs1a'Ÿ±Çbs1fyellowŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cCS3Ÿ±Çaoa.Ÿ±Ç`dcmapŸ±Çaoa.Ÿ±Ç`hset_overŸ±Ç`a(Ÿ±Çbs1a'Ÿ±Çbs1dcyanŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`cCS4Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cax2Ÿ±Çaoa.Ÿ±Ç`gcontourŸ±Ç`a(Ÿ±Ç`aXŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`aYŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`aZŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`flevelsŸ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`r                  Ÿ±Ç`fcolorsŸ±Çaoa=Ÿ±Ç`a(Ÿ±Çbs1a'Ÿ±Çbs1akŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`r                  Ÿ±Ç`jlinewidthsŸ±Çaoa=Ÿ±Ç`a(Ÿ±Çbmia3Ÿ±Ç`a,Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`r                  Ÿ±Ç`foriginŸ±Çaoa=Ÿ±Ç`foriginŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cax2Ÿ±Çaoa.Ÿ±Ç`iset_titleŸ±Ç`a(Ÿ±Çbs1a'Ÿ±Çbs1x Listed colors (3 masked regions)Ÿ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cax2Ÿ±Çaoa.Ÿ±Ç`fclabelŸ±Ç`a(Ÿ±Ç`cCS4Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`cfmtŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbsie%2.1fŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`fcolorsŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1awŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`hfontsizeŸ±Çaoa=Ÿ±Çbmib14Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1x6# Notice that the colorbar gets all the information itŸ±Ç`a
Ÿ±Çbc1x(# needs from the ContourSet object, CS3.Ÿ±Ç`a
Ÿ±Ç`dfig2Ÿ±Çaoa.Ÿ±Ç`hcolorbarŸ±Ç`a(Ÿ±Ç`cCS3Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1xM#############################################################################Ÿ±Ç`a
Ÿ±Çbc1t# Extension settingsŸ±Ç`a
Ÿ±Çbc1t# ------------------Ÿ±Ç`a
Ÿ±Çbc1x.# Illustrate all 4 possible "extend" settings:Ÿ±Ç`a
Ÿ±Ç`gextendsŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`a[Ÿ±Çbs2a"Ÿ±Çbs2gneitherŸ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs2a"Ÿ±Çbs2dbothŸ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs2a"Ÿ±Çbs2cminŸ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs2a"Ÿ±Çbs2cmaxŸ±Çbs2a"Ÿ±Ç`a]Ÿ±Ç`a
Ÿ±Ç`dcmapŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`icolormapsŸ±Ç`a[Ÿ±Çbs2a"Ÿ±Çbs2fwinterŸ±Çbs2a"Ÿ±Ç`a]Ÿ±Çaoa.Ÿ±Ç`mwith_extremesŸ±Ç`a(Ÿ±Ç`eunderŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2gmagentaŸ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`doverŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2fyellowŸ±Çbs2a"Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Çbc1x<# Note: contouring simply excludes masked or nan regions, soŸ±Ç`a
Ÿ±Çbc1x># instead of using the "bad" colormap value for them, it drawsŸ±Ç`a
Ÿ±Çbc1x=# nothing at all in them.  Therefore the following would haveŸ±Ç`a
Ÿ±Çbc1l# no effect:Ÿ±Ç`a
Ÿ±Çbc1u# cmap.set_bad("red")Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`cfigŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`caxsŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`hsubplotsŸ±Ç`a(Ÿ±Çbmia2Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia2Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`rconstrained_layoutŸ±Çaoa=Ÿ±ÇbkcdTrueŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±ÇakcforŸ±Ç`a Ÿ±Ç`baxŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`fextendŸ±Ç`a Ÿ±ÇbowbinŸ±Ç`a Ÿ±ÇbnbczipŸ±Ç`a(Ÿ±Ç`caxsŸ±Çaoa.Ÿ±Ç`dflatŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`gextendsŸ±Ç`a)Ÿ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`bcsŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`hcontourfŸ±Ç`a(Ÿ±Ç`aXŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`aYŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`aZŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`flevelsŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dcmapŸ±Çaoa=Ÿ±Ç`dcmapŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`fextendŸ±Çaoa=Ÿ±Ç`fextendŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`foriginŸ±Çaoa=Ÿ±Ç`foriginŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`cfigŸ±Çaoa.Ÿ±Ç`hcolorbarŸ±Ç`a(Ÿ±Ç`bcsŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`baxŸ±Çaoa=Ÿ±Ç`baxŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`fshrinkŸ±Çaoa=Ÿ±Çbmfc0.9Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`iset_titleŸ±Ç`a(Ÿ±Çbs2a"Ÿ±Çbs2iextend = Ÿ±Çbsib%sŸ±Çbs2a"Ÿ±Ç`a Ÿ±Çaoa%Ÿ±Ç`a Ÿ±Ç`fextendŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`nlocator_paramsŸ±Ç`a(Ÿ±Ç`enbinsŸ±Çaoa=Ÿ±Çbmia4Ÿ±Ç`a)Ÿ±Ç`a
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
Ÿ±Çbc1xC#    - `matplotlib.axes.Axes.contour` / `matplotlib.pyplot.contour`Ÿ±Ç`a
Ÿ±Çbc1xE#    - `matplotlib.axes.Axes.contourf` / `matplotlib.pyplot.contourf`Ÿ±Ç`a
Ÿ±Çbc1xA#    - `matplotlib.axes.Axes.clabel` / `matplotlib.pyplot.clabel`Ÿ±Ç`a
Ÿ±Çbc1xI#    - `matplotlib.figure.Figure.colorbar` / `matplotlib.pyplot.colorbar`Ÿ±Ç`a
Ÿ±Çbc1x##    - `matplotlib.colors.Colormap`Ÿ±Ç`a
Ÿ±Çbc1x+#    - `matplotlib.colors.Colormap.set_bad`Ÿ±Ç`a
Ÿ±Çbc1x-#    - `matplotlib.colors.Colormap.set_under`Ÿ±Ç`a
Ÿ±Çbc1x,#    - `matplotlib.colors.Colormap.set_over`Ÿ±Ç`a
`dNoneˆ