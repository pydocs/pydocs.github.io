ŸØÇÅŸ¥Éô4Ÿ±Çbsdy"""
=============
Contour Image
=============

Test combinations of contouring, filled contouring, and image plotting.
For contour labelling, see also the :doc:`contour demo example
</gallery/images_contours_and_fields/contour_demo>`.

The emphasis in this demo is on showing how to make contours register
correctly on images, and on how to get both of them oriented as desired.
In particular, note the usage of the :doc:`"origin" and "extent"
</tutorials/intermediate/imshow_extent>` keyword arguments to imshow and
contour.
"""Ÿ±Ç`a
Ÿ±ÇbknfimportŸ±Ç`a Ÿ±ÇbnnŸ¢ÑjmatplotlibŸ†Ñjmatplotlibe3.5.1fmodulejmatplotlibfmoduleıŸ±Çbnna.Ÿ±ÇbnnfpyplotŸ±Ç`a Ÿ±ÇakbasŸ±Ç`a Ÿ±ÇbnncpltŸ±Ç`a
Ÿ±ÇbknfimportŸ±Ç`a Ÿ±ÇbnnŸ¢ÑenumpyŸ†Ñenumpyf1.22.3fmoduleenumpyfmoduleıŸ±Ç`a Ÿ±ÇakbasŸ±Ç`a Ÿ±ÇbnnbnpŸ±Ç`a
Ÿ±ÇbkndfromŸ±Ç`a Ÿ±ÇbnnŸ¢ÑjmatplotlibŸ†Ñjmatplotlibe3.5.1fmodulejmatplotlibfmoduleıŸ±Ç`a Ÿ±ÇbknfimportŸ±Ç`a Ÿ±Ç`bcmŸ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1xG# Default delta is large because that makes it fast, and it illustratesŸ±Ç`a
Ÿ±Çbc1x6# the correct registration between image and contours.Ÿ±Ç`a
Ÿ±Ç`edeltaŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Çbmfc0.5Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`fextentŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`a(Ÿ±Çaoa-Ÿ±Çbmia3Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia4Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çaoa-Ÿ±Çbmia4Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia3Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`axŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`farangeŸ±Ç`a(Ÿ±Çaoa-Ÿ±Çbmfc3.0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfe4.001Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`edeltaŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`ayŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`farangeŸ±Ç`a(Ÿ±Çaoa-Ÿ±Çbmfc4.0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfe3.001Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`edeltaŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`aXŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`aYŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`hmeshgridŸ±Ç`a(Ÿ±Ç`axŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ayŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`bZ1Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`cexpŸ±Ç`a(Ÿ±Çaoa-Ÿ±Ç`aXŸ±Çaoa*Ÿ±Çaoa*Ÿ±Çbmia2Ÿ±Ç`a Ÿ±Çaoa-Ÿ±Ç`a Ÿ±Ç`aYŸ±Çaoa*Ÿ±Çaoa*Ÿ±Çbmia2Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`bZ2Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`cexpŸ±Ç`a(Ÿ±Çaoa-Ÿ±Ç`a(Ÿ±Ç`aXŸ±Ç`a Ÿ±Çaoa-Ÿ±Ç`a Ÿ±Çbmia1Ÿ±Ç`a)Ÿ±Çaoa*Ÿ±Çaoa*Ÿ±Çbmia2Ÿ±Ç`a Ÿ±Çaoa-Ÿ±Ç`a Ÿ±Ç`a(Ÿ±Ç`aYŸ±Ç`a Ÿ±Çaoa-Ÿ±Ç`a Ÿ±Çbmia1Ÿ±Ç`a)Ÿ±Çaoa*Ÿ±Çaoa*Ÿ±Çbmia2Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`aZŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`a(Ÿ±Ç`bZ1Ÿ±Ç`a Ÿ±Çaoa-Ÿ±Ç`a Ÿ±Ç`bZ2Ÿ±Ç`a)Ÿ±Ç`a Ÿ±Çaoa*Ÿ±Ç`a Ÿ±Çbmia2Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1x3# Boost the upper limit to avoid truncation errors.Ÿ±Ç`a
Ÿ±Ç`flevelsŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`farangeŸ±Ç`a(Ÿ±Çaoa-Ÿ±Çbmfc2.0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfe1.601Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfc0.4Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`dnormŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bcmŸ±Çaoa.Ÿ±Ç`fcolorsŸ±Çaoa.Ÿ±Ç`iNormalizeŸ±Ç`a(Ÿ±Ç`dvmaxŸ±Çaoa=Ÿ±ÇbnbcabsŸ±Ç`a(Ÿ±Ç`aZŸ±Ç`a)Ÿ±Çaoa.Ÿ±Ç`cmaxŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dvminŸ±Çaoa=Ÿ±Çaoa-Ÿ±ÇbnbcabsŸ±Ç`a(Ÿ±Ç`aZŸ±Ç`a)Ÿ±Çaoa.Ÿ±Ç`cmaxŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`dcmapŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bcmŸ±Çaoa.Ÿ±Ç`dPRGnŸ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`cfigŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`d_axsŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`hsubplotsŸ±Ç`a(Ÿ±Ç`enrowsŸ±Çaoa=Ÿ±Çbmia2Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`encolsŸ±Çaoa=Ÿ±Çbmia2Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cfigŸ±Çaoa.Ÿ±Ç`osubplots_adjustŸ±Ç`a(Ÿ±Ç`fhspaceŸ±Çaoa=Ÿ±Çbmfc0.3Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`caxsŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`d_axsŸ±Çaoa.Ÿ±Ç`gflattenŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`ecset1Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`caxsŸ±Ç`a[Ÿ±Çbmia0Ÿ±Ç`a]Ÿ±Çaoa.Ÿ±Ç`hcontourfŸ±Ç`a(Ÿ±Ç`aXŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`aYŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`aZŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`flevelsŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dnormŸ±Çaoa=Ÿ±Ç`dnormŸ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`x                        Ÿ±Ç`dcmapŸ±Çaoa=Ÿ±Ç`bcmŸ±Çaoa.Ÿ±Ç`hget_cmapŸ±Ç`a(Ÿ±Ç`dcmapŸ±Ç`a,Ÿ±Ç`a Ÿ±ÇbnbclenŸ±Ç`a(Ÿ±Ç`flevelsŸ±Ç`a)Ÿ±Ç`a Ÿ±Çaoa-Ÿ±Ç`a Ÿ±Çbmia1Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Çbc1x=# It is not necessary, but for the colormap, we need only theŸ±Ç`a
Ÿ±Çbc1x?# number of levels minus 1.  To avoid discretization error, useŸ±Ç`a
Ÿ±Çbc1xA# either this number or a large number such as the default (256).Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1x=# If we want lines as well as filled regions, we need to callŸ±Ç`a
Ÿ±Çbc1xD# contour separately; don't try to change the edgecolor or edgewidthŸ±Ç`a
Ÿ±Çbc1x:# of the polygons in the collections returned by contourf.Ÿ±Ç`a
Ÿ±Çbc1xF# Use levels output from previous call to guarantee they are the same.Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`ecset2Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`caxsŸ±Ç`a[Ÿ±Çbmia0Ÿ±Ç`a]Ÿ±Çaoa.Ÿ±Ç`gcontourŸ±Ç`a(Ÿ±Ç`aXŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`aYŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`aZŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ecset1Ÿ±Çaoa.Ÿ±Ç`flevelsŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`fcolorsŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1akŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1x@# We don't really need dashed contour lines to indicate negativeŸ±Ç`a
Ÿ±Çbc1x"# regions, so let's turn them off.Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±ÇakcforŸ±Ç`a Ÿ±Ç`acŸ±Ç`a Ÿ±ÇbowbinŸ±Ç`a Ÿ±Ç`ecset2Ÿ±Çaoa.Ÿ±Ç`kcollectionsŸ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`acŸ±Çaoa.Ÿ±Ç`mset_linestyleŸ±Ç`a(Ÿ±Çbs1a'Ÿ±Çbs1esolidŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1x;# It is easier here to make a separate call to contour thanŸ±Ç`a
Ÿ±Çbc1x.# to set up an array of colors and linewidths.Ÿ±Ç`a
Ÿ±Çbc1x5# We are making a thick green line as a zero contour.Ÿ±Ç`a
Ÿ±Çbc1x6# Specify the zero level as a tuple with only 0 in it.Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`ecset3Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`caxsŸ±Ç`a[Ÿ±Çbmia0Ÿ±Ç`a]Ÿ±Çaoa.Ÿ±Ç`gcontourŸ±Ç`a(Ÿ±Ç`aXŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`aYŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`aZŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`a(Ÿ±Çbmia0Ÿ±Ç`a,Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`fcolorsŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1agŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`jlinewidthsŸ±Çaoa=Ÿ±Çbmia2Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`caxsŸ±Ç`a[Ÿ±Çbmia0Ÿ±Ç`a]Ÿ±Çaoa.Ÿ±Ç`iset_titleŸ±Ç`a(Ÿ±Çbs1a'Ÿ±Çbs1oFilled contoursŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cfigŸ±Çaoa.Ÿ±Ç`hcolorbarŸ±Ç`a(Ÿ±Ç`ecset1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`baxŸ±Çaoa=Ÿ±Ç`caxsŸ±Ç`a[Ÿ±Çbmia0Ÿ±Ç`a]Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`caxsŸ±Ç`a[Ÿ±Çbmia1Ÿ±Ç`a]Ÿ±Çaoa.Ÿ±Ç`fimshowŸ±Ç`a(Ÿ±Ç`aZŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`fextentŸ±Çaoa=Ÿ±Ç`fextentŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dcmapŸ±Çaoa=Ÿ±Ç`dcmapŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dnormŸ±Çaoa=Ÿ±Ç`dnormŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`caxsŸ±Ç`a[Ÿ±Çbmia1Ÿ±Ç`a]Ÿ±Çaoa.Ÿ±Ç`gcontourŸ±Ç`a(Ÿ±Ç`aZŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`flevelsŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`fcolorsŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1akŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`foriginŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1eupperŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`fextentŸ±Çaoa=Ÿ±Ç`fextentŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`caxsŸ±Ç`a[Ÿ±Çbmia1Ÿ±Ç`a]Ÿ±Çaoa.Ÿ±Ç`iset_titleŸ±Ç`a(Ÿ±Çbs2a"Ÿ±Çbs2nImage, origin Ÿ±Çbs2a'Ÿ±Çbs2eupperŸ±Çbs2a'Ÿ±Çbs2a"Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`caxsŸ±Ç`a[Ÿ±Çbmia2Ÿ±Ç`a]Ÿ±Çaoa.Ÿ±Ç`fimshowŸ±Ç`a(Ÿ±Ç`aZŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`foriginŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1elowerŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`fextentŸ±Çaoa=Ÿ±Ç`fextentŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dcmapŸ±Çaoa=Ÿ±Ç`dcmapŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dnormŸ±Çaoa=Ÿ±Ç`dnormŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`caxsŸ±Ç`a[Ÿ±Çbmia2Ÿ±Ç`a]Ÿ±Çaoa.Ÿ±Ç`gcontourŸ±Ç`a(Ÿ±Ç`aZŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`flevelsŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`fcolorsŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1akŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`foriginŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1elowerŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`fextentŸ±Çaoa=Ÿ±Ç`fextentŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`caxsŸ±Ç`a[Ÿ±Çbmia2Ÿ±Ç`a]Ÿ±Çaoa.Ÿ±Ç`iset_titleŸ±Ç`a(Ÿ±Çbs2a"Ÿ±Çbs2nImage, origin Ÿ±Çbs2a'Ÿ±Çbs2elowerŸ±Çbs2a'Ÿ±Çbs2a"Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1xA# We will use the interpolation "nearest" here to show the actualŸ±Ç`a
Ÿ±Çbc1o# image pixels.Ÿ±Ç`a
Ÿ±Çbc1xB# Note that the contour lines don't extend to the edge of the box.Ÿ±Ç`a
Ÿ±Çbc1xE# This is intentional. The Z values are defined at the center of eachŸ±Ç`a
Ÿ±Çbc1xA# image pixel (each color block on the following subplot), so theŸ±Ç`a
Ÿ±Çbc1xF# domain that is contoured does not extend beyond these pixel centers.Ÿ±Ç`a
Ÿ±Ç`bimŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`caxsŸ±Ç`a[Ÿ±Çbmia3Ÿ±Ç`a]Ÿ±Çaoa.Ÿ±Ç`fimshowŸ±Ç`a(Ÿ±Ç`aZŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`minterpolationŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1gnearestŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`fextentŸ±Çaoa=Ÿ±Ç`fextentŸ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`s                   Ÿ±Ç`dcmapŸ±Çaoa=Ÿ±Ç`dcmapŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dnormŸ±Çaoa=Ÿ±Ç`dnormŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`caxsŸ±Ç`a[Ÿ±Çbmia3Ÿ±Ç`a]Ÿ±Çaoa.Ÿ±Ç`gcontourŸ±Ç`a(Ÿ±Ç`aZŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`flevelsŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`fcolorsŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1akŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`foriginŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1eimageŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`fextentŸ±Çaoa=Ÿ±Ç`fextentŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`dylimŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`caxsŸ±Ç`a[Ÿ±Çbmia3Ÿ±Ç`a]Ÿ±Çaoa.Ÿ±Ç`hget_ylimŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`caxsŸ±Ç`a[Ÿ±Çbmia3Ÿ±Ç`a]Ÿ±Çaoa.Ÿ±Ç`hset_ylimŸ±Ç`a(Ÿ±Ç`dylimŸ±Ç`a[Ÿ±Ç`a:Ÿ±Ç`a:Ÿ±Çaoa-Ÿ±Çbmia1Ÿ±Ç`a]Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`caxsŸ±Ç`a[Ÿ±Çbmia3Ÿ±Ç`a]Ÿ±Çaoa.Ÿ±Ç`iset_titleŸ±Ç`a(Ÿ±Çbs2a"Ÿ±Çbs2xOrigin from rc, reversed y-axisŸ±Çbs2a"Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cfigŸ±Çaoa.Ÿ±Ç`hcolorbarŸ±Ç`a(Ÿ±Ç`bimŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`baxŸ±Çaoa=Ÿ±Ç`caxsŸ±Ç`a[Ÿ±Çbmia3Ÿ±Ç`a]Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`cfigŸ±Çaoa.Ÿ±Ç`ltight_layoutŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`dshowŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1xM#############################################################################Ÿ±Ç`a
Ÿ±Çbc1a#Ÿ±Ç`a
Ÿ±Çbc1x# .. admonition:: ReferencesŸ±Ç`a
Ÿ±Çbc1a#Ÿ±Ç`a
Ÿ±Çbc1xN#    The use of the following functions, methods, classes and modules is shownŸ±Ç`a
Ÿ±Çbc1u#    in this example:Ÿ±Ç`a
Ÿ±Çbc1a#Ÿ±Ç`a
Ÿ±Çbc1xC#    - `matplotlib.axes.Axes.contour` / `matplotlib.pyplot.contour`Ÿ±Ç`a
Ÿ±Çbc1xA#    - `matplotlib.axes.Axes.imshow` / `matplotlib.pyplot.imshow`Ÿ±Ç`a
Ÿ±Çbc1xI#    - `matplotlib.figure.Figure.colorbar` / `matplotlib.pyplot.colorbar`Ÿ±Ç`a
Ÿ±Çbc1x$#    - `matplotlib.colors.Normalize`Ÿ±Ç`a
`dNoneˆ