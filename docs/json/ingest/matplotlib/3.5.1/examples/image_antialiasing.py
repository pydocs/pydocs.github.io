Ù¯‚Ù´ƒ™QÙ±‚bsdy…"""
==================
Image antialiasing
==================

Images are represented by discrete pixels, either on the screen or in an
image file.  When data that makes up the image has a different resolution
than its representation on the screen we will see aliasing effects.  How
noticeable these are depends on how much down-sampling takes place in
the change of resolution (if any).

When subsampling data, aliasing is reduced by smoothing first and then
subsampling the smoothed data.  In Matplotlib, we can do that
smoothing before mapping the data to colors, or we can do the smoothing
on the RGB(A) data in the final image.  The difference between these is
shown below, and controlled with the *interpolation_stage* keyword argument.

The default image interpolation in Matplotlib is 'antialiased', and
it is applied to the data.  This uses a
hanning interpolation on the data provided by the user for reduced aliasing
in most situations. Only when there is upsampling by a factor of 1, 2 or
>=3 is 'nearest' neighbor interpolation used.

Other anti-aliasing filters can be specified in `.Axes.imshow` using the
*interpolation* keyword argument.
"""Ù±‚`a
Ù±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„enumpyÙ „enumpyf1.22.3fmoduleenumpyfmoduleõÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnnbnpÙ±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnnfpyplotÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnncpltÙ±‚`a
Ù±‚`a
Ù±‚bc1xO###############################################################################Ù±‚`a
Ù±‚bc1xI# First we generate a 450x450 pixel image with varying frequency content:Ù±‚`a
Ù±‚`aNÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bmic450Ù±‚`a
Ù±‚`axÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`farangeÙ±‚`a(Ù±‚`aNÙ±‚`a)Ù±‚`a Ù±‚aoa/Ù±‚`a Ù±‚`aNÙ±‚`a Ù±‚aoa-Ù±‚`a Ù±‚bmfc0.5Ù±‚`a
Ù±‚`ayÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`farangeÙ±‚`a(Ù±‚`aNÙ±‚`a)Ù±‚`a Ù±‚aoa/Ù±‚`a Ù±‚`aNÙ±‚`a Ù±‚aoa-Ù±‚`a Ù±‚bmfc0.5Ù±‚`a
Ù±‚`baaÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`donesÙ±‚`a(Ù±‚`a(Ù±‚`aNÙ±‚`a,Ù±‚`a Ù±‚`aNÙ±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`baaÙ±‚`a[Ù±‚`a:Ù±‚`a:Ù±‚bmia2Ù±‚`a,Ù±‚`a Ù±‚`a:Ù±‚`a]Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚aoa-Ù±‚bmia1Ù±‚`a
Ù±‚`a
Ù±‚`aXÙ±‚`a,Ù±‚`a Ù±‚`aYÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`hmeshgridÙ±‚`a(Ù±‚`axÙ±‚`a,Ù±‚`a Ù±‚`ayÙ±‚`a)Ù±‚`a
Ù±‚`aRÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`dsqrtÙ±‚`a(Ù±‚`aXÙ±‚aoa*Ù±‚aoa*Ù±‚bmia2Ù±‚`a Ù±‚aoa+Ù±‚`a Ù±‚`aYÙ±‚aoa*Ù±‚aoa*Ù±‚bmia2Ù±‚`a)Ù±‚`a
Ù±‚`bf0Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bmia5Ù±‚`a
Ù±‚`akÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bmic100Ù±‚`a
Ù±‚`aaÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`csinÙ±‚`a(Ù±‚`bnpÙ±‚aoa.Ù±‚`bpiÙ±‚`a Ù±‚aoa*Ù±‚`a Ù±‚bmia2Ù±‚`a Ù±‚aoa*Ù±‚`a Ù±‚`a(Ù±‚`bf0Ù±‚`a Ù±‚aoa*Ù±‚`a Ù±‚`aRÙ±‚`a Ù±‚aoa+Ù±‚`a Ù±‚`akÙ±‚`a Ù±‚aoa*Ù±‚`a Ù±‚`aRÙ±‚aoa*Ù±‚aoa*Ù±‚bmia2Ù±‚`a Ù±‚aoa/Ù±‚`a Ù±‚bmia2Ù±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚bc1x!# make the left hand side of thisÙ±‚`a
Ù±‚`aaÙ±‚`a[Ù±‚`a:Ù±‚bnbcintÙ±‚`a(Ù±‚`aNÙ±‚`a Ù±‚aoa/Ù±‚`a Ù±‚bmia2Ù±‚`a)Ù±‚`a,Ù±‚`a Ù±‚`a:Ù±‚`a]Ù±‚`a[Ù±‚`aRÙ±‚`a[Ù±‚`a:Ù±‚bnbcintÙ±‚`a(Ù±‚`aNÙ±‚`a Ù±‚aoa/Ù±‚`a Ù±‚bmia2Ù±‚`a)Ù±‚`a,Ù±‚`a Ù±‚`a:Ù±‚`a]Ù±‚`a Ù±‚aoa<Ù±‚`a Ù±‚bmfc0.4Ù±‚`a]Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚aoa-Ù±‚bmia1Ù±‚`a
Ù±‚`aaÙ±‚`a[Ù±‚`a:Ù±‚bnbcintÙ±‚`a(Ù±‚`aNÙ±‚`a Ù±‚aoa/Ù±‚`a Ù±‚bmia2Ù±‚`a)Ù±‚`a,Ù±‚`a Ù±‚`a:Ù±‚`a]Ù±‚`a[Ù±‚`aRÙ±‚`a[Ù±‚`a:Ù±‚bnbcintÙ±‚`a(Ù±‚`aNÙ±‚`a Ù±‚aoa/Ù±‚`a Ù±‚bmia2Ù±‚`a)Ù±‚`a,Ù±‚`a Ù±‚`a:Ù±‚`a]Ù±‚`a Ù±‚aoa<Ù±‚`a Ù±‚bmfc0.3Ù±‚`a]Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bmia1Ù±‚`a
Ù±‚`baaÙ±‚`a[Ù±‚`a:Ù±‚`a,Ù±‚`a Ù±‚bnbcintÙ±‚`a(Ù±‚`aNÙ±‚`a Ù±‚aoa/Ù±‚`a Ù±‚bmia3Ù±‚`a)Ù±‚`a:Ù±‚`a]Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`aaÙ±‚`a[Ù±‚`a:Ù±‚`a,Ù±‚`a Ù±‚bnbcintÙ±‚`a(Ù±‚`aNÙ±‚`a Ù±‚aoa/Ù±‚`a Ù±‚bmia3Ù±‚`a)Ù±‚`a:Ù±‚`a]Ù±‚`a
Ù±‚`aaÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`baaÙ±‚`a
Ù±‚bc1xO###############################################################################Ù±‚`a
Ù±‚bc1xD# The following images are subsampled from 450 data pixels to eitherÙ±‚`a
Ù±‚bc1x7# 125 pixels or 250 pixels (depending on your display).Ù±‚`a
Ù±‚bc1xE# The Moire patterns in the 'nearest' interpolation are caused by theÙ±‚`a
Ù±‚bc1xA# high-frequency data being subsampled.  The 'antialiased' imagedÙ±‚`a
Ù±‚bc1xF# still has some Moire patterns as well, but they are greatly reduced.Ù±‚`a
Ù±‚bc1a#Ù±‚`a
Ù±‚bc1xH# There are substantial differences between the 'data' interpolation andÙ±‚`a
Ù±‚bc1xI# the 'rgba' interpolation.  The alternating bands of red and blue on theÙ±‚`a
Ù±‚bc1xK# left third of the image are subsampled.  By interpolating in 'data' spaceÙ±‚`a
Ù±‚bc1xI# (the default) the antialiasing filter makes the stripes close to white,Ù±‚`a
Ù±‚bc1xE# because the average of -1 and +1 is zero, and zero is white in thisÙ±‚`a
Ù±‚bc1k# colormap.Ù±‚`a
Ù±‚bc1a#Ù±‚`a
Ù±‚bc1xH# Conversely, when the anti-aliasing occurs in 'rgba' space, the red andÙ±‚`a
Ù±‚bc1xK# blue are combined visually to make purple.  This behaviour is more like aÙ±‚`a
Ù±‚bc1xF# typical image processing package, but note that purple is not in theÙ±‚`a
Ù±‚bc1xE# original colormap, so it is no longer possible to invert individualÙ±‚`a
Ù±‚bc1x"# pixels back to their data value.Ù±‚`a
Ù±‚`a
Ù±‚`cfigÙ±‚`a,Ù±‚`a Ù±‚`caxsÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cpltÙ±‚aoa.Ù±‚`hsubplotsÙ±‚`a(Ù±‚bmia2Ù±‚`a,Ù±‚`a Ù±‚bmia2Ù±‚`a,Ù±‚`a Ù±‚`gfigsizeÙ±‚aoa=Ù±‚`a(Ù±‚bmia5Ù±‚`a,Ù±‚`a Ù±‚bmia6Ù±‚`a)Ù±‚`a,Ù±‚`a Ù±‚`rconstrained_layoutÙ±‚aoa=Ù±‚bkcdTrueÙ±‚`a)Ù±‚`a
Ù±‚`caxsÙ±‚`a[Ù±‚bmia0Ù±‚`a,Ù±‚`a Ù±‚bmia0Ù±‚`a]Ù±‚aoa.Ù±‚`fimshowÙ±‚`a(Ù±‚`aaÙ±‚`a,Ù±‚`a Ù±‚`minterpolationÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1gnearestÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`dcmapÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1fRdBu_rÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`caxsÙ±‚`a[Ù±‚bmia0Ù±‚`a,Ù±‚`a Ù±‚bmia0Ù±‚`a]Ù±‚aoa.Ù±‚`hset_xlimÙ±‚`a(Ù±‚bmic100Ù±‚`a,Ù±‚`a Ù±‚bmic200Ù±‚`a)Ù±‚`a
Ù±‚`caxsÙ±‚`a[Ù±‚bmia0Ù±‚`a,Ù±‚`a Ù±‚bmia0Ù±‚`a]Ù±‚aoa.Ù±‚`hset_ylimÙ±‚`a(Ù±‚bmic275Ù±‚`a,Ù±‚`a Ù±‚bmic175Ù±‚`a)Ù±‚`a
Ù±‚`caxsÙ±‚`a[Ù±‚bmia0Ù±‚`a,Ù±‚`a Ù±‚bmia0Ù±‚`a]Ù±‚aoa.Ù±‚`iset_titleÙ±‚`a(Ù±‚bs1a'Ù±‚bs1dZoomÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚akcforÙ±‚`a Ù±‚`baxÙ±‚`a,Ù±‚`a Ù±‚`finterpÙ±‚`a,Ù±‚`a Ù±‚`espaceÙ±‚`a Ù±‚bowbinÙ±‚`a Ù±‚bnbczipÙ±‚`a(Ù±‚`caxsÙ±‚aoa.Ù±‚`dflatÙ±‚`a[Ù±‚bmia1Ù±‚`a:Ù±‚`a]Ù±‚`a,Ù±‚`a
Ù±‚`x                             Ù±‚`a[Ù±‚bs1a'Ù±‚bs1gnearestÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚bs1a'Ù±‚bs1kantialiasedÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚bs1a'Ù±‚bs1kantialiasedÙ±‚bs1a'Ù±‚`a]Ù±‚`a,Ù±‚`a
Ù±‚`x                             Ù±‚`a[Ù±‚bs1a'Ù±‚bs1ddataÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚bs1a'Ù±‚bs1ddataÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚bs1a'Ù±‚bs1drgbaÙ±‚bs1a'Ù±‚`a]Ù±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`d    Ù±‚`baxÙ±‚aoa.Ù±‚`fimshowÙ±‚`a(Ù±‚`aaÙ±‚`a,Ù±‚`a Ù±‚`minterpolationÙ±‚aoa=Ù±‚`finterpÙ±‚`a,Ù±‚`a Ù±‚`sinterpolation_stageÙ±‚aoa=Ù±‚`espaceÙ±‚`a,Ù±‚`a
Ù±‚`n              Ù±‚`dcmapÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1fRdBu_rÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`baxÙ±‚aoa.Ù±‚`iset_titleÙ±‚`a(Ù±‚bsaafÙ±‚bs2a"Ù±‚bs2ninterpolation=Ù±‚bs2a'Ù±‚bsia{Ù±‚`finterpÙ±‚bsia}Ù±‚bs2a'Ù±‚bseb\nÙ±‚bs2fspace=Ù±‚bs2a'Ù±‚bsia{Ù±‚`espaceÙ±‚bsia}Ù±‚bs2a'Ù±‚bs2a"Ù±‚`a)Ù±‚`a
Ù±‚`cpltÙ±‚aoa.Ù±‚`dshowÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚bc1xO###############################################################################Ù±‚`a
Ù±‚bc1xK# Even up-sampling an image with 'nearest' interpolation will lead to MoireÙ±‚`a
Ù±‚bc1xI# patterns when the upsampling factor is not integer. The following imageÙ±‚`a
Ù±‚bc1xJ# upsamples 500 data pixels to 530 rendered pixels. You may note a grid ofÙ±‚`a
Ù±‚bc1xM# 30 line-like artifacts which stem from the 524 - 500 = 24 extra pixels thatÙ±‚`a
Ù±‚bc1xL# had to be made up. Since interpolation is 'nearest' they are the same as aÙ±‚`a
Ù±‚bc1xJ# neighboring line of pixels and thus stretch the image locally so that itÙ±‚`a
Ù±‚bc1r# looks distorted.Ù±‚`a
Ù±‚`cfigÙ±‚`a,Ù±‚`a Ù±‚`baxÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cpltÙ±‚aoa.Ù±‚`hsubplotsÙ±‚`a(Ù±‚`gfigsizeÙ±‚aoa=Ù±‚`a(Ù±‚bmfc6.8Ù±‚`a,Ù±‚`a Ù±‚bmfc6.8Ù±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`fimshowÙ±‚`a(Ù±‚`aaÙ±‚`a,Ù±‚`a Ù±‚`minterpolationÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1gnearestÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`dcmapÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1dgrayÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`iset_titleÙ±‚`a(Ù±‚bs2a"Ù±‚bs2x+upsampled by factor a 1.048, interpolation=Ù±‚bs2a'Ù±‚bs2gnearestÙ±‚bs2a'Ù±‚bs2a"Ù±‚`a)Ù±‚`a
Ù±‚`cpltÙ±‚aoa.Ù±‚`dshowÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚bc1xO###############################################################################Ù±‚`a
Ù±‚bc1x8# Better antialiasing algorithms can reduce this effect:Ù±‚`a
Ù±‚`cfigÙ±‚`a,Ù±‚`a Ù±‚`baxÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cpltÙ±‚aoa.Ù±‚`hsubplotsÙ±‚`a(Ù±‚`gfigsizeÙ±‚aoa=Ù±‚`a(Ù±‚bmfc6.8Ù±‚`a,Ù±‚`a Ù±‚bmfc6.8Ù±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`fimshowÙ±‚`a(Ù±‚`aaÙ±‚`a,Ù±‚`a Ù±‚`minterpolationÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1kantialiasedÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`dcmapÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1dgrayÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`iset_titleÙ±‚`a(Ù±‚bs2a"Ù±‚bs2x+upsampled by factor a 1.048, interpolation=Ù±‚bs2a'Ù±‚bs2kantialiasedÙ±‚bs2a'Ù±‚bs2a"Ù±‚`a)Ù±‚`a
Ù±‚`cpltÙ±‚aoa.Ù±‚`dshowÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚bc1xO###############################################################################Ù±‚`a
Ù±‚bc1xK# Apart from the default 'hanning' antialiasing, `~.Axes.imshow` supports aÙ±‚`a
Ù±‚bc1xH# number of different interpolation algorithms, which may work better orÙ±‚`a
Ù±‚bc1x!# worse depending on the pattern.Ù±‚`a
Ù±‚`cfigÙ±‚`a,Ù±‚`a Ù±‚`caxsÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cpltÙ±‚aoa.Ù±‚`hsubplotsÙ±‚`a(Ù±‚bmia1Ù±‚`a,Ù±‚`a Ù±‚bmia2Ù±‚`a,Ù±‚`a Ù±‚`gfigsizeÙ±‚aoa=Ù±‚`a(Ù±‚bmia7Ù±‚`a,Ù±‚`a Ù±‚bmia4Ù±‚`a)Ù±‚`a,Ù±‚`a Ù±‚`rconstrained_layoutÙ±‚aoa=Ù±‚bkcdTrueÙ±‚`a)Ù±‚`a
Ù±‚akcforÙ±‚`a Ù±‚`baxÙ±‚`a,Ù±‚`a Ù±‚`finterpÙ±‚`a Ù±‚bowbinÙ±‚`a Ù±‚bnbczipÙ±‚`a(Ù±‚`caxsÙ±‚`a,Ù±‚`a Ù±‚`a[Ù±‚bs1a'Ù±‚bs1ghanningÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚bs1a'Ù±‚bs1glanczosÙ±‚bs1a'Ù±‚`a]Ù±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`d    Ù±‚`baxÙ±‚aoa.Ù±‚`fimshowÙ±‚`a(Ù±‚`aaÙ±‚`a,Ù±‚`a Ù±‚`minterpolationÙ±‚aoa=Ù±‚`finterpÙ±‚`a,Ù±‚`a Ù±‚`dcmapÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1dgrayÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`baxÙ±‚aoa.Ù±‚`iset_titleÙ±‚`a(Ù±‚bsaafÙ±‚bs2a"Ù±‚bs2ninterpolation=Ù±‚bs2a'Ù±‚bsia{Ù±‚`finterpÙ±‚bsia}Ù±‚bs2a'Ù±‚bs2a"Ù±‚`a)Ù±‚`a
Ù±‚`cpltÙ±‚aoa.Ù±‚`dshowÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚bc1xM#############################################################################Ù±‚`a
Ù±‚bc1a#Ù±‚`a
Ù±‚bc1x# .. admonition:: ReferencesÙ±‚`a
Ù±‚bc1a#Ù±‚`a
Ù±‚bc1xN#    The use of the following functions, methods, classes and modules is shownÙ±‚`a
Ù±‚bc1u#    in this example:Ù±‚`a
Ù±‚bc1a#Ù±‚`a
Ù±‚bc1x$#    - `matplotlib.axes.Axes.imshow`Ù±‚`a
`dNoneö