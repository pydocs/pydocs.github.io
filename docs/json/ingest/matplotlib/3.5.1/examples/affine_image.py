ŸØÇÅŸ¥Éô%Ÿ±ÇbsdyΩ"""
============================
Affine transform of an image
============================


Prepending an affine transformation (`~.transforms.Affine2D`) to the :ref:`data
transform <data-coords>` of an image allows to manipulate the image's shape and
orientation.  This is an example of the concept of :ref:`transform chaining
<transformation-pipeline>`.

The image of the output should have its boundary match the dashed yellow
rectangle.
"""Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±ÇbknfimportŸ±Ç`a Ÿ±ÇbnnŸ¢ÑenumpyŸ†Ñenumpyf1.22.3fmoduleenumpyfmoduleıŸ±Ç`a Ÿ±ÇakbasŸ±Ç`a Ÿ±ÇbnnbnpŸ±Ç`a
Ÿ±ÇbknfimportŸ±Ç`a Ÿ±ÇbnnŸ¢ÑjmatplotlibŸ†Ñjmatplotlibe3.5.1fmodulejmatplotlibfmoduleıŸ±Çbnna.Ÿ±ÇbnnfpyplotŸ±Ç`a Ÿ±ÇakbasŸ±Ç`a Ÿ±ÇbnncpltŸ±Ç`a
Ÿ±ÇbknfimportŸ±Ç`a Ÿ±ÇbnnŸ¢ÑjmatplotlibŸ†Ñjmatplotlibe3.5.1fmodulejmatplotlibfmoduleıŸ±Çbnna.Ÿ±ÇbnnjtransformsŸ±Ç`a Ÿ±ÇakbasŸ±Ç`a Ÿ±ÇbnnkmtransformsŸ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±ÇakcdefŸ±Ç`a Ÿ±Çbnfiget_imageŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`edeltaŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Çbmfd0.25Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`axŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`ayŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`farangeŸ±Ç`a(Ÿ±Çaoa-Ÿ±Çbmfc3.0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfc3.0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`edeltaŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`aXŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`aYŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`hmeshgridŸ±Ç`a(Ÿ±Ç`axŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ayŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`bZ1Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`cexpŸ±Ç`a(Ÿ±Çaoa-Ÿ±Ç`aXŸ±Çaoa*Ÿ±Çaoa*Ÿ±Çbmia2Ÿ±Ç`a Ÿ±Çaoa-Ÿ±Ç`a Ÿ±Ç`aYŸ±Çaoa*Ÿ±Çaoa*Ÿ±Çbmia2Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`bZ2Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`cexpŸ±Ç`a(Ÿ±Çaoa-Ÿ±Ç`a(Ÿ±Ç`aXŸ±Ç`a Ÿ±Çaoa-Ÿ±Ç`a Ÿ±Çbmia1Ÿ±Ç`a)Ÿ±Çaoa*Ÿ±Çaoa*Ÿ±Çbmia2Ÿ±Ç`a Ÿ±Çaoa-Ÿ±Ç`a Ÿ±Ç`a(Ÿ±Ç`aYŸ±Ç`a Ÿ±Çaoa-Ÿ±Ç`a Ÿ±Çbmia1Ÿ±Ç`a)Ÿ±Çaoa*Ÿ±Çaoa*Ÿ±Çbmia2Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`aZŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`a(Ÿ±Ç`bZ1Ÿ±Ç`a Ÿ±Çaoa-Ÿ±Ç`a Ÿ±Ç`bZ2Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±ÇakfreturnŸ±Ç`a Ÿ±Ç`aZŸ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±ÇakcdefŸ±Ç`a Ÿ±Çbnfgdo_plotŸ±Ç`a(Ÿ±Ç`baxŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`aZŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`itransformŸ±Ç`a)Ÿ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`bimŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`fimshowŸ±Ç`a(Ÿ±Ç`aZŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`minterpolationŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1dnoneŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`s                   Ÿ±Ç`foriginŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1elowerŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`s                   Ÿ±Ç`fextentŸ±Çaoa=Ÿ±Ç`a[Ÿ±Çaoa-Ÿ±Çbmia2Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia4Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çaoa-Ÿ±Çbmia3Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia2Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`gclip_onŸ±Çaoa=Ÿ±ÇbkcdTrueŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`jtrans_dataŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`itransformŸ±Ç`a Ÿ±Çaoa+Ÿ±Ç`a Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`itransDataŸ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`bimŸ±Çaoa.Ÿ±Ç`mset_transformŸ±Ç`a(Ÿ±Ç`jtrans_dataŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Çbc1x&# display intended extent of the imageŸ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`bx1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`bx2Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`by1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`by2Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bimŸ±Çaoa.Ÿ±Ç`jget_extentŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`dplotŸ±Ç`a(Ÿ±Ç`a[Ÿ±Ç`bx1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`bx2Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`bx2Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`bx1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`bx1Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`a[Ÿ±Ç`by1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`by1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`by2Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`by2Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`by1Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs2a"Ÿ±Çbs2cy--Ÿ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`l            Ÿ±Ç`itransformŸ±Çaoa=Ÿ±Ç`jtrans_dataŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`hset_xlimŸ±Ç`a(Ÿ±Çaoa-Ÿ±Çbmia5Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia5Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`hset_ylimŸ±Ç`a(Ÿ±Çaoa-Ÿ±Çbmia4Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia4Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1x# prepare image and figureŸ±Ç`a
Ÿ±Ç`cfigŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`a(Ÿ±Ç`a(Ÿ±Ç`cax1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`cax2Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`a(Ÿ±Ç`cax3Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`cax4Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`hsubplotsŸ±Ç`a(Ÿ±Çbmia2Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia2Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`aZŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`iget_imageŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1p# image rotationŸ±Ç`a
Ÿ±Ç`gdo_plotŸ±Ç`a(Ÿ±Ç`cax1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`aZŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`kmtransformsŸ±Çaoa.Ÿ±Ç`hAffine2DŸ±Ç`a(Ÿ±Ç`a)Ÿ±Çaoa.Ÿ±Ç`jrotate_degŸ±Ç`a(Ÿ±Çbmib30Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1l# image skewŸ±Ç`a
Ÿ±Ç`gdo_plotŸ±Ç`a(Ÿ±Ç`cax2Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`aZŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`kmtransformsŸ±Çaoa.Ÿ±Ç`hAffine2DŸ±Ç`a(Ÿ±Ç`a)Ÿ±Çaoa.Ÿ±Ç`hskew_degŸ±Ç`a(Ÿ±Çbmib30Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmib15Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1v# scale and reflectionŸ±Ç`a
Ÿ±Ç`gdo_plotŸ±Ç`a(Ÿ±Ç`cax3Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`aZŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`kmtransformsŸ±Çaoa.Ÿ±Ç`hAffine2DŸ±Ç`a(Ÿ±Ç`a)Ÿ±Çaoa.Ÿ±Ç`escaleŸ±Ç`a(Ÿ±Çaoa-Ÿ±Çbmia1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfb.5Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1x# everything and a translationŸ±Ç`a
Ÿ±Ç`gdo_plotŸ±Ç`a(Ÿ±Ç`cax4Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`aZŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`kmtransformsŸ±Çaoa.Ÿ±Ç`hAffine2DŸ±Ç`a(Ÿ±Ç`a)Ÿ±Çaoa.Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±Ç`jrotate_degŸ±Ç`a(Ÿ±Çbmib30Ÿ±Ç`a)Ÿ±Çaoa.Ÿ±Ç`hskew_degŸ±Ç`a(Ÿ±Çbmib30Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmib15Ÿ±Ç`a)Ÿ±Çaoa.Ÿ±Ç`escaleŸ±Ç`a(Ÿ±Çaoa-Ÿ±Çbmia1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfb.5Ÿ±Ç`a)Ÿ±Çaoa.Ÿ±Ç`itranslateŸ±Ç`a(Ÿ±Çbmfb.5Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çaoa-Ÿ±Çbmia1Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
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
Ÿ±Çbc1xA#    - `matplotlib.axes.Axes.imshow` / `matplotlib.pyplot.imshow`Ÿ±Ç`a
Ÿ±Çbc1x'#    - `matplotlib.transforms.Affine2D`Ÿ±Ç`a
`dNoneˆ