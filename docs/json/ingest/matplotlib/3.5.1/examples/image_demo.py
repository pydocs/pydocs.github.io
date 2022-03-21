Ù¯‚Ù´ƒ™ÿÙ±‚bsdy"""
==========
Image Demo
==========

Many ways to plot images in Matplotlib.

The most common way to plot images in Matplotlib is with
`~.axes.Axes.imshow`. The following examples demonstrate much of the
functionality of imshow and the many images you can create.
"""Ù±‚`a
Ù±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„enumpyÙ „enumpyf1.22.3fmoduleenumpyfmoduleõÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnnbnpÙ±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnnbcmÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnnbcmÙ±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnnfpyplotÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnncpltÙ±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnnecbookÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnnecbookÙ±‚`a
Ù±‚bkndfromÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnndpathÙ±‚`a Ù±‚bknfimportÙ±‚`a Ù±‚`dPathÙ±‚`a
Ù±‚bkndfromÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnngpatchesÙ±‚`a Ù±‚bknfimportÙ±‚`a Ù±‚`iPathPatchÙ±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚bc1x)# Fixing random state for reproducibilityÙ±‚`a
Ù±‚`bnpÙ±‚aoa.Ù±‚`frandomÙ±‚aoa.Ù±‚`dseedÙ±‚`a(Ù±‚bmih19680801Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚bc1xO###############################################################################Ù±‚`a
Ù±‚bc1x># First we'll generate a simple bivariate normal distribution.Ù±‚`a
Ù±‚`a
Ù±‚`edeltaÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bmfe0.025Ù±‚`a
Ù±‚`axÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`ayÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`farangeÙ±‚`a(Ù±‚aoa-Ù±‚bmfc3.0Ù±‚`a,Ù±‚`a Ù±‚bmfc3.0Ù±‚`a,Ù±‚`a Ù±‚`edeltaÙ±‚`a)Ù±‚`a
Ù±‚`aXÙ±‚`a,Ù±‚`a Ù±‚`aYÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`hmeshgridÙ±‚`a(Ù±‚`axÙ±‚`a,Ù±‚`a Ù±‚`ayÙ±‚`a)Ù±‚`a
Ù±‚`bZ1Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`cexpÙ±‚`a(Ù±‚aoa-Ù±‚`aXÙ±‚aoa*Ù±‚aoa*Ù±‚bmia2Ù±‚`a Ù±‚aoa-Ù±‚`a Ù±‚`aYÙ±‚aoa*Ù±‚aoa*Ù±‚bmia2Ù±‚`a)Ù±‚`a
Ù±‚`bZ2Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`cexpÙ±‚`a(Ù±‚aoa-Ù±‚`a(Ù±‚`aXÙ±‚`a Ù±‚aoa-Ù±‚`a Ù±‚bmia1Ù±‚`a)Ù±‚aoa*Ù±‚aoa*Ù±‚bmia2Ù±‚`a Ù±‚aoa-Ù±‚`a Ù±‚`a(Ù±‚`aYÙ±‚`a Ù±‚aoa-Ù±‚`a Ù±‚bmia1Ù±‚`a)Ù±‚aoa*Ù±‚aoa*Ù±‚bmia2Ù±‚`a)Ù±‚`a
Ù±‚`aZÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`a(Ù±‚`bZ1Ù±‚`a Ù±‚aoa-Ù±‚`a Ù±‚`bZ2Ù±‚`a)Ù±‚`a Ù±‚aoa*Ù±‚`a Ù±‚bmia2Ù±‚`a
Ù±‚`a
Ù±‚`cfigÙ±‚`a,Ù±‚`a Ù±‚`baxÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cpltÙ±‚aoa.Ù±‚`hsubplotsÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`bimÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`baxÙ±‚aoa.Ù±‚`fimshowÙ±‚`a(Ù±‚`aZÙ±‚`a,Ù±‚`a Ù±‚`minterpolationÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1hbilinearÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`dcmapÙ±‚aoa=Ù±‚`bcmÙ±‚aoa.Ù±‚`fRdYlGnÙ±‚`a,Ù±‚`a
Ù±‚`o               Ù±‚`foriginÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1elowerÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`fextentÙ±‚aoa=Ù±‚`a[Ù±‚aoa-Ù±‚bmia3Ù±‚`a,Ù±‚`a Ù±‚bmia3Ù±‚`a,Ù±‚`a Ù±‚aoa-Ù±‚bmia3Ù±‚`a,Ù±‚`a Ù±‚bmia3Ù±‚`a]Ù±‚`a,Ù±‚`a
Ù±‚`o               Ù±‚`dvmaxÙ±‚aoa=Ù±‚bnbcabsÙ±‚`a(Ù±‚`aZÙ±‚`a)Ù±‚aoa.Ù±‚`cmaxÙ±‚`a(Ù±‚`a)Ù±‚`a,Ù±‚`a Ù±‚`dvminÙ±‚aoa=Ù±‚aoa-Ù±‚bnbcabsÙ±‚`a(Ù±‚`aZÙ±‚`a)Ù±‚aoa.Ù±‚`cmaxÙ±‚`a(Ù±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`cpltÙ±‚aoa.Ù±‚`dshowÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚bc1xO###############################################################################Ù±‚`a
Ù±‚bc1x1# It is also possible to show images of pictures.Ù±‚`a
Ù±‚`a
Ù±‚bc1p# A sample imageÙ±‚`a
Ù±‚akdwithÙ±‚`a Ù±‚`ecbookÙ±‚aoa.Ù±‚`oget_sample_dataÙ±‚`a(Ù±‚bs1a'Ù±‚bs1pgrace_hopper.jpgÙ±‚bs1a'Ù±‚`a)Ù±‚`a Ù±‚akbasÙ±‚`a Ù±‚`jimage_fileÙ±‚`a:Ù±‚`a
Ù±‚`d    Ù±‚`eimageÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cpltÙ±‚aoa.Ù±‚`fimreadÙ±‚`a(Ù±‚`jimage_fileÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚bc1x3# And another image, using 256x256 16-bit integers.Ù±‚`a
Ù±‚`awÙ±‚`a,Ù±‚`a Ù±‚`ahÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bmic256Ù±‚`a,Ù±‚`a Ù±‚bmic256Ù±‚`a
Ù±‚akdwithÙ±‚`a Ù±‚`ecbookÙ±‚aoa.Ù±‚`oget_sample_dataÙ±‚`a(Ù±‚bs1a'Ù±‚bs1ls1045.ima.gzÙ±‚bs1a'Ù±‚`a)Ù±‚`a Ù±‚akbasÙ±‚`a Ù±‚`hdatafileÙ±‚`a:Ù±‚`a
Ù±‚`d    Ù±‚`asÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`hdatafileÙ±‚aoa.Ù±‚`dreadÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`aAÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`jfrombufferÙ±‚`a(Ù±‚`asÙ±‚`a,Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`fuint16Ù±‚`a)Ù±‚aoa.Ù±‚`fastypeÙ±‚`a(Ù±‚bnbefloatÙ±‚`a)Ù±‚aoa.Ù±‚`greshapeÙ±‚`a(Ù±‚`a(Ù±‚`awÙ±‚`a,Ù±‚`a Ù±‚`ahÙ±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`fextentÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`a(Ù±‚bmia0Ù±‚`a,Ù±‚`a Ù±‚bmib25Ù±‚`a,Ù±‚`a Ù±‚bmia0Ù±‚`a,Ù±‚`a Ù±‚bmib25Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`cfigÙ±‚`a,Ù±‚`a Ù±‚`baxÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cpltÙ±‚aoa.Ù±‚`nsubplot_mosaicÙ±‚`a(Ù±‚`a[Ù±‚`a
Ù±‚`d    Ù±‚`a[Ù±‚bs1a'Ù±‚bs1fhopperÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚bs1a'Ù±‚bs1cmriÙ±‚bs1a'Ù±‚`a]Ù±‚`a
Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`gfigsizeÙ±‚aoa=Ù±‚`a(Ù±‚bmia7Ù±‚`a,Ù±‚`a Ù±‚bmfc3.5Ù±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`baxÙ±‚`a[Ù±‚bs1a'Ù±‚bs1fhopperÙ±‚bs1a'Ù±‚`a]Ù±‚aoa.Ù±‚`fimshowÙ±‚`a(Ù±‚`eimageÙ±‚`a)Ù±‚`a
Ù±‚`baxÙ±‚`a[Ù±‚bs1a'Ù±‚bs1fhopperÙ±‚bs1a'Ù±‚`a]Ù±‚aoa.Ù±‚`daxisÙ±‚`a(Ù±‚bs1a'Ù±‚bs1coffÙ±‚bs1a'Ù±‚`a)Ù±‚`b  Ù±‚bc1x# clear x-axis and y-axisÙ±‚`a
Ù±‚`a
Ù±‚`bimÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`baxÙ±‚`a[Ù±‚bs1a'Ù±‚bs1cmriÙ±‚bs1a'Ù±‚`a]Ù±‚aoa.Ù±‚`fimshowÙ±‚`a(Ù±‚`aAÙ±‚`a,Ù±‚`a Ù±‚`dcmapÙ±‚aoa=Ù±‚`cpltÙ±‚aoa.Ù±‚`bcmÙ±‚aoa.Ù±‚`chotÙ±‚`a,Ù±‚`a Ù±‚`foriginÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1eupperÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`fextentÙ±‚aoa=Ù±‚`fextentÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`gmarkersÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`a[Ù±‚`a(Ù±‚bmfd15.9Ù±‚`a,Ù±‚`a Ù±‚bmfd14.5Ù±‚`a)Ù±‚`a,Ù±‚`a Ù±‚`a(Ù±‚bmfd16.8Ù±‚`a,Ù±‚`a Ù±‚bmib15Ù±‚`a)Ù±‚`a]Ù±‚`a
Ù±‚`axÙ±‚`a,Ù±‚`a Ù±‚`ayÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bnbczipÙ±‚`a(Ù±‚aoa*Ù±‚`gmarkersÙ±‚`a)Ù±‚`a
Ù±‚`baxÙ±‚`a[Ù±‚bs1a'Ù±‚bs1cmriÙ±‚bs1a'Ù±‚`a]Ù±‚aoa.Ù±‚`dplotÙ±‚`a(Ù±‚`axÙ±‚`a,Ù±‚`a Ù±‚`ayÙ±‚`a,Ù±‚`a Ù±‚bs1a'Ù±‚bs1aoÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`baxÙ±‚`a[Ù±‚bs1a'Ù±‚bs1cmriÙ±‚bs1a'Ù±‚`a]Ù±‚aoa.Ù±‚`iset_titleÙ±‚`a(Ù±‚bs1a'Ù±‚bs1cMRIÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`cpltÙ±‚aoa.Ù±‚`dshowÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚bc1xO###############################################################################Ù±‚`a
Ù±‚bc1v# Interpolating imagesÙ±‚`a
Ù±‚bc1v# --------------------Ù±‚`a
Ù±‚bc1a#Ù±‚`a
Ù±‚bc1xO# It is also possible to interpolate images before displaying them. Be careful,Ù±‚`a
Ù±‚bc1xK# as this may manipulate the way your data looks, but it can be helpful forÙ±‚`a
Ù±‚bc1xJ# achieving the look you want. Below we'll display the same (small) array,Ù±‚`a
Ù±‚bc1x:# interpolated with three different interpolation methods.Ù±‚`a
Ù±‚bc1a#Ù±‚`a
Ù±‚bc1xJ# The center of the pixel at A[i, j] is plotted at (i+0.5, i+0.5).  If youÙ±‚`a
Ù±‚bc1xE# are using interpolation='nearest', the region bounded by (i, j) andÙ±‚`a
Ù±‚bc1xG# (i+1, j+1) will have the same color.  If you are using interpolation,Ù±‚`a
Ù±‚bc1xH# the pixel center will have the same color as it does with nearest, butÙ±‚`a
Ù±‚bc1xC# other pixels will be interpolated between the neighboring pixels.Ù±‚`a
Ù±‚bc1a#Ù±‚`a
Ù±‚bc1xM# To prevent edge effects when doing interpolation, Matplotlib pads the inputÙ±‚`a
Ù±‚bc1xK# array with identical pixels around the edge: if you have a 5x5 array withÙ±‚`a
Ù±‚bc1w# colors a-y as below::Ù±‚`a
Ù±‚bc1a#Ù±‚`a
Ù±‚bc1m#   a b c d eÙ±‚`a
Ù±‚bc1m#   f g h i jÙ±‚`a
Ù±‚bc1m#   k l m n oÙ±‚`a
Ù±‚bc1m#   p q r s tÙ±‚`a
Ù±‚bc1m#   u v w x yÙ±‚`a
Ù±‚bc1a#Ù±‚`a
Ù±‚bc1xK# Matplotlib computes the interpolation and resizing on the padded array ::Ù±‚`a
Ù±‚bc1a#Ù±‚`a
Ù±‚bc1q#   a a b c d e eÙ±‚`a
Ù±‚bc1q#   a a b c d e eÙ±‚`a
Ù±‚bc1q#   f f g h i j jÙ±‚`a
Ù±‚bc1q#   k k l m n o oÙ±‚`a
Ù±‚bc1q#   p p q r s t tÙ±‚`a
Ù±‚bc1q#   o u v w x y yÙ±‚`a
Ù±‚bc1q#   o u v w x y yÙ±‚`a
Ù±‚bc1a#Ù±‚`a
Ù±‚bc1xN# and then extracts the central region of the result.  (Extremely old versionsÙ±‚`a
Ù±‚bc1xL# of Matplotlib (<0.63) did not pad the array, but instead adjusted the viewÙ±‚`a
Ù±‚bc1x*# limits to hide the affected edge areas.)Ù±‚`a
Ù±‚bc1a#Ù±‚`a
Ù±‚bc1xC# This approach allows plotting the full extent of an array withoutÙ±‚`a
Ù±‚bc1xE# edge effects, and for example to layer multiple images of differentÙ±‚`a
Ù±‚bc1xD# sizes over one another with different interpolation methods -- seeÙ±‚`a
Ù±‚bc1xK# :doc:`/gallery/images_contours_and_fields/layer_images`.  It also impliesÙ±‚`a
Ù±‚bc1xI# a performance hit, as this new temporary, padded array must be created.Ù±‚`a
Ù±‚bc1xI# Sophisticated interpolation also implies a performance hit; for maximalÙ±‚`a
Ù±‚bc1xI# performance or very large images, interpolation='nearest' is suggested.Ù±‚`a
Ù±‚`a
Ù±‚`aAÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`frandomÙ±‚aoa.Ù±‚`drandÙ±‚`a(Ù±‚bmia5Ù±‚`a,Ù±‚`a Ù±‚bmia5Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`cfigÙ±‚`a,Ù±‚`a Ù±‚`caxsÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cpltÙ±‚aoa.Ù±‚`hsubplotsÙ±‚`a(Ù±‚bmia1Ù±‚`a,Ù±‚`a Ù±‚bmia3Ù±‚`a,Ù±‚`a Ù±‚`gfigsizeÙ±‚aoa=Ù±‚`a(Ù±‚bmib10Ù±‚`a,Ù±‚`a Ù±‚bmia3Ù±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚akcforÙ±‚`a Ù±‚`baxÙ±‚`a,Ù±‚`a Ù±‚`finterpÙ±‚`a Ù±‚bowbinÙ±‚`a Ù±‚bnbczipÙ±‚`a(Ù±‚`caxsÙ±‚`a,Ù±‚`a Ù±‚`a[Ù±‚bs1a'Ù±‚bs1gnearestÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚bs1a'Ù±‚bs1hbilinearÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚bs1a'Ù±‚bs1gbicubicÙ±‚bs1a'Ù±‚`a]Ù±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`d    Ù±‚`baxÙ±‚aoa.Ù±‚`fimshowÙ±‚`a(Ù±‚`aAÙ±‚`a,Ù±‚`a Ù±‚`minterpolationÙ±‚aoa=Ù±‚`finterpÙ±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`baxÙ±‚aoa.Ù±‚`iset_titleÙ±‚`a(Ù±‚`finterpÙ±‚aoa.Ù±‚`jcapitalizeÙ±‚`a(Ù±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`baxÙ±‚aoa.Ù±‚`dgridÙ±‚`a(Ù±‚bkcdTrueÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`cpltÙ±‚aoa.Ù±‚`dshowÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚bc1xO###############################################################################Ù±‚`a
Ù±‚bc1xH# You can specify whether images should be plotted with the array originÙ±‚`a
Ù±‚bc1xI# x[0, 0] in the upper left or lower right by using the origin parameter.Ù±‚`a
Ù±‚bc1x?# You can also control the default setting image.origin in yourÙ±‚`a
Ù±‚bc1xM# :ref:`matplotlibrc file <customizing-with-matplotlibrc-files>`. For more onÙ±‚`a
Ù±‚bc1x># this topic see the :doc:`complete guide on origin and extentÙ±‚`a
Ù±‚bc1x+# </tutorials/intermediate/imshow_extent>`.Ù±‚`a
Ù±‚`a
Ù±‚`axÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`farangeÙ±‚`a(Ù±‚bmic120Ù±‚`a)Ù±‚aoa.Ù±‚`greshapeÙ±‚`a(Ù±‚`a(Ù±‚bmib10Ù±‚`a,Ù±‚`a Ù±‚bmib12Ù±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`finterpÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bs1a'Ù±‚bs1hbilinearÙ±‚bs1a'Ù±‚`a
Ù±‚`cfigÙ±‚`a,Ù±‚`a Ù±‚`caxsÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cpltÙ±‚aoa.Ù±‚`hsubplotsÙ±‚`a(Ù±‚`enrowsÙ±‚aoa=Ù±‚bmia2Ù±‚`a,Ù±‚`a Ù±‚`fsharexÙ±‚aoa=Ù±‚bkcdTrueÙ±‚`a,Ù±‚`a Ù±‚`gfigsizeÙ±‚aoa=Ù±‚`a(Ù±‚bmia3Ù±‚`a,Ù±‚`a Ù±‚bmia5Ù±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`caxsÙ±‚`a[Ù±‚bmia0Ù±‚`a]Ù±‚aoa.Ù±‚`iset_titleÙ±‚`a(Ù±‚bs1a'Ù±‚bs1qblue should be upÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`caxsÙ±‚`a[Ù±‚bmia0Ù±‚`a]Ù±‚aoa.Ù±‚`fimshowÙ±‚`a(Ù±‚`axÙ±‚`a,Ù±‚`a Ù±‚`foriginÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1eupperÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`minterpolationÙ±‚aoa=Ù±‚`finterpÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`caxsÙ±‚`a[Ù±‚bmia1Ù±‚`a]Ù±‚aoa.Ù±‚`iset_titleÙ±‚`a(Ù±‚bs1a'Ù±‚bs1sblue should be downÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`caxsÙ±‚`a[Ù±‚bmia1Ù±‚`a]Ù±‚aoa.Ù±‚`fimshowÙ±‚`a(Ù±‚`axÙ±‚`a,Ù±‚`a Ù±‚`foriginÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1elowerÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`minterpolationÙ±‚aoa=Ù±‚`finterpÙ±‚`a)Ù±‚`a
Ù±‚`cpltÙ±‚aoa.Ù±‚`dshowÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚bc1xO###############################################################################Ù±‚`a
Ù±‚bc1x1# Finally, we'll show an image using a clip path.Ù±‚`a
Ù±‚`a
Ù±‚`edeltaÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bmfe0.025Ù±‚`a
Ù±‚`axÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`ayÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`farangeÙ±‚`a(Ù±‚aoa-Ù±‚bmfc3.0Ù±‚`a,Ù±‚`a Ù±‚bmfc3.0Ù±‚`a,Ù±‚`a Ù±‚`edeltaÙ±‚`a)Ù±‚`a
Ù±‚`aXÙ±‚`a,Ù±‚`a Ù±‚`aYÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`hmeshgridÙ±‚`a(Ù±‚`axÙ±‚`a,Ù±‚`a Ù±‚`ayÙ±‚`a)Ù±‚`a
Ù±‚`bZ1Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`cexpÙ±‚`a(Ù±‚aoa-Ù±‚`aXÙ±‚aoa*Ù±‚aoa*Ù±‚bmia2Ù±‚`a Ù±‚aoa-Ù±‚`a Ù±‚`aYÙ±‚aoa*Ù±‚aoa*Ù±‚bmia2Ù±‚`a)Ù±‚`a
Ù±‚`bZ2Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`cexpÙ±‚`a(Ù±‚aoa-Ù±‚`a(Ù±‚`aXÙ±‚`a Ù±‚aoa-Ù±‚`a Ù±‚bmia1Ù±‚`a)Ù±‚aoa*Ù±‚aoa*Ù±‚bmia2Ù±‚`a Ù±‚aoa-Ù±‚`a Ù±‚`a(Ù±‚`aYÙ±‚`a Ù±‚aoa-Ù±‚`a Ù±‚bmia1Ù±‚`a)Ù±‚aoa*Ù±‚aoa*Ù±‚bmia2Ù±‚`a)Ù±‚`a
Ù±‚`aZÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`a(Ù±‚`bZ1Ù±‚`a Ù±‚aoa-Ù±‚`a Ù±‚`bZ2Ù±‚`a)Ù±‚`a Ù±‚aoa*Ù±‚`a Ù±‚bmia2Ù±‚`a
Ù±‚`a
Ù±‚`dpathÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`dPathÙ±‚`a(Ù±‚`a[Ù±‚`a[Ù±‚bmia0Ù±‚`a,Ù±‚`a Ù±‚bmia1Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`a[Ù±‚bmia1Ù±‚`a,Ù±‚`a Ù±‚bmia0Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`a[Ù±‚bmia0Ù±‚`a,Ù±‚`a Ù±‚aoa-Ù±‚bmia1Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`a[Ù±‚aoa-Ù±‚bmia1Ù±‚`a,Ù±‚`a Ù±‚bmia0Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`a[Ù±‚bmia0Ù±‚`a,Ù±‚`a Ù±‚bmia1Ù±‚`a]Ù±‚`a]Ù±‚`a)Ù±‚`a
Ù±‚`epatchÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`iPathPatchÙ±‚`a(Ù±‚`dpathÙ±‚`a,Ù±‚`a Ù±‚`ifacecolorÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1dnoneÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`cfigÙ±‚`a,Ù±‚`a Ù±‚`baxÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cpltÙ±‚aoa.Ù±‚`hsubplotsÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`iadd_patchÙ±‚`a(Ù±‚`epatchÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`bimÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`baxÙ±‚aoa.Ù±‚`fimshowÙ±‚`a(Ù±‚`aZÙ±‚`a,Ù±‚`a Ù±‚`minterpolationÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1hbilinearÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`dcmapÙ±‚aoa=Ù±‚`bcmÙ±‚aoa.Ù±‚`dgrayÙ±‚`a,Ù±‚`a
Ù±‚`o               Ù±‚`foriginÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1elowerÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`fextentÙ±‚aoa=Ù±‚`a[Ù±‚aoa-Ù±‚bmia3Ù±‚`a,Ù±‚`a Ù±‚bmia3Ù±‚`a,Ù±‚`a Ù±‚aoa-Ù±‚bmia3Ù±‚`a,Ù±‚`a Ù±‚bmia3Ù±‚`a]Ù±‚`a,Ù±‚`a
Ù±‚`o               Ù±‚`iclip_pathÙ±‚aoa=Ù±‚`epatchÙ±‚`a,Ù±‚`a Ù±‚`gclip_onÙ±‚aoa=Ù±‚bkcdTrueÙ±‚`a)Ù±‚`a
Ù±‚`bimÙ±‚aoa.Ù±‚`mset_clip_pathÙ±‚`a(Ù±‚`epatchÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`cpltÙ±‚aoa.Ù±‚`dshowÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚bc1xM#############################################################################Ù±‚`a
Ù±‚bc1a#Ù±‚`a
Ù±‚bc1x# .. admonition:: ReferencesÙ±‚`a
Ù±‚bc1a#Ù±‚`a
Ù±‚bc1xN#    The use of the following functions, methods, classes and modules is shownÙ±‚`a
Ù±‚bc1u#    in this example:Ù±‚`a
Ù±‚bc1a#Ù±‚`a
Ù±‚bc1xA#    - `matplotlib.axes.Axes.imshow` / `matplotlib.pyplot.imshow`Ù±‚`a
Ù±‚bc1x/#    - `matplotlib.artist.Artist.set_clip_path`Ù±‚`a
Ù±‚bc1x%#    - `matplotlib.patches.PathPatch`Ù±‚`a
`dNoneö