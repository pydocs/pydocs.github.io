��������Q���bsdy�"""
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
"""���`a
���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���`a
���bc1xO###############################################################################���`a
���bc1xI# First we generate a 450x450 pixel image with varying frequency content:���`a
���`aN���`a ���aoa=���`a ���bmic450���`a
���`ax���`a ���aoa=���`a ���`bnp���aoa.���`farange���`a(���`aN���`a)���`a ���aoa/���`a ���`aN���`a ���aoa-���`a ���bmfc0.5���`a
���`ay���`a ���aoa=���`a ���`bnp���aoa.���`farange���`a(���`aN���`a)���`a ���aoa/���`a ���`aN���`a ���aoa-���`a ���bmfc0.5���`a
���`baa���`a ���aoa=���`a ���`bnp���aoa.���`dones���`a(���`a(���`aN���`a,���`a ���`aN���`a)���`a)���`a
���`baa���`a[���`a:���`a:���bmia2���`a,���`a ���`a:���`a]���`a ���aoa=���`a ���aoa-���bmia1���`a
���`a
���`aX���`a,���`a ���`aY���`a ���aoa=���`a ���`bnp���aoa.���`hmeshgrid���`a(���`ax���`a,���`a ���`ay���`a)���`a
���`aR���`a ���aoa=���`a ���`bnp���aoa.���`dsqrt���`a(���`aX���aoa*���aoa*���bmia2���`a ���aoa+���`a ���`aY���aoa*���aoa*���bmia2���`a)���`a
���`bf0���`a ���aoa=���`a ���bmia5���`a
���`ak���`a ���aoa=���`a ���bmic100���`a
���`aa���`a ���aoa=���`a ���`bnp���aoa.���`csin���`a(���`bnp���aoa.���`bpi���`a ���aoa*���`a ���bmia2���`a ���aoa*���`a ���`a(���`bf0���`a ���aoa*���`a ���`aR���`a ���aoa+���`a ���`ak���`a ���aoa*���`a ���`aR���aoa*���aoa*���bmia2���`a ���aoa/���`a ���bmia2���`a)���`a)���`a
���bc1x!# make the left hand side of this���`a
���`aa���`a[���`a:���bnbcint���`a(���`aN���`a ���aoa/���`a ���bmia2���`a)���`a,���`a ���`a:���`a]���`a[���`aR���`a[���`a:���bnbcint���`a(���`aN���`a ���aoa/���`a ���bmia2���`a)���`a,���`a ���`a:���`a]���`a ���aoa<���`a ���bmfc0.4���`a]���`a ���aoa=���`a ���aoa-���bmia1���`a
���`aa���`a[���`a:���bnbcint���`a(���`aN���`a ���aoa/���`a ���bmia2���`a)���`a,���`a ���`a:���`a]���`a[���`aR���`a[���`a:���bnbcint���`a(���`aN���`a ���aoa/���`a ���bmia2���`a)���`a,���`a ���`a:���`a]���`a ���aoa<���`a ���bmfc0.3���`a]���`a ���aoa=���`a ���bmia1���`a
���`baa���`a[���`a:���`a,���`a ���bnbcint���`a(���`aN���`a ���aoa/���`a ���bmia3���`a)���`a:���`a]���`a ���aoa=���`a ���`aa���`a[���`a:���`a,���`a ���bnbcint���`a(���`aN���`a ���aoa/���`a ���bmia3���`a)���`a:���`a]���`a
���`aa���`a ���aoa=���`a ���`baa���`a
���bc1xO###############################################################################���`a
���bc1xD# The following images are subsampled from 450 data pixels to either���`a
���bc1x7# 125 pixels or 250 pixels (depending on your display).���`a
���bc1xE# The Moire patterns in the 'nearest' interpolation are caused by the���`a
���bc1xA# high-frequency data being subsampled.  The 'antialiased' imaged���`a
���bc1xF# still has some Moire patterns as well, but they are greatly reduced.���`a
���bc1a#���`a
���bc1xH# There are substantial differences between the 'data' interpolation and���`a
���bc1xI# the 'rgba' interpolation.  The alternating bands of red and blue on the���`a
���bc1xK# left third of the image are subsampled.  By interpolating in 'data' space���`a
���bc1xI# (the default) the antialiasing filter makes the stripes close to white,���`a
���bc1xE# because the average of -1 and +1 is zero, and zero is white in this���`a
���bc1k# colormap.���`a
���bc1a#���`a
���bc1xH# Conversely, when the anti-aliasing occurs in 'rgba' space, the red and���`a
���bc1xK# blue are combined visually to make purple.  This behaviour is more like a���`a
���bc1xF# typical image processing package, but note that purple is not in the���`a
���bc1xE# original colormap, so it is no longer possible to invert individual���`a
���bc1x"# pixels back to their data value.���`a
���`a
���`cfig���`a,���`a ���`caxs���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���bmia2���`a,���`a ���bmia2���`a,���`a ���`gfigsize���aoa=���`a(���bmia5���`a,���`a ���bmia6���`a)���`a,���`a ���`rconstrained_layout���aoa=���bkcdTrue���`a)���`a
���`caxs���`a[���bmia0���`a,���`a ���bmia0���`a]���aoa.���`fimshow���`a(���`aa���`a,���`a ���`minterpolation���aoa=���bs1a'���bs1gnearest���bs1a'���`a,���`a ���`dcmap���aoa=���bs1a'���bs1fRdBu_r���bs1a'���`a)���`a
���`caxs���`a[���bmia0���`a,���`a ���bmia0���`a]���aoa.���`hset_xlim���`a(���bmic100���`a,���`a ���bmic200���`a)���`a
���`caxs���`a[���bmia0���`a,���`a ���bmia0���`a]���aoa.���`hset_ylim���`a(���bmic275���`a,���`a ���bmic175���`a)���`a
���`caxs���`a[���bmia0���`a,���`a ���bmia0���`a]���aoa.���`iset_title���`a(���bs1a'���bs1dZoom���bs1a'���`a)���`a
���`a
���akcfor���`a ���`bax���`a,���`a ���`finterp���`a,���`a ���`espace���`a ���bowbin���`a ���bnbczip���`a(���`caxs���aoa.���`dflat���`a[���bmia1���`a:���`a]���`a,���`a
���`x                             ���`a[���bs1a'���bs1gnearest���bs1a'���`a,���`a ���bs1a'���bs1kantialiased���bs1a'���`a,���`a ���bs1a'���bs1kantialiased���bs1a'���`a]���`a,���`a
���`x                             ���`a[���bs1a'���bs1ddata���bs1a'���`a,���`a ���bs1a'���bs1ddata���bs1a'���`a,���`a ���bs1a'���bs1drgba���bs1a'���`a]���`a)���`a:���`a
���`d    ���`bax���aoa.���`fimshow���`a(���`aa���`a,���`a ���`minterpolation���aoa=���`finterp���`a,���`a ���`sinterpolation_stage���aoa=���`espace���`a,���`a
���`n              ���`dcmap���aoa=���bs1a'���bs1fRdBu_r���bs1a'���`a)���`a
���`d    ���`bax���aoa.���`iset_title���`a(���bsaaf���bs2a"���bs2ninterpolation=���bs2a'���bsia{���`finterp���bsia}���bs2a'���bseb\n���bs2fspace=���bs2a'���bsia{���`espace���bsia}���bs2a'���bs2a"���`a)���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
���`a
���bc1xO###############################################################################���`a
���bc1xK# Even up-sampling an image with 'nearest' interpolation will lead to Moire���`a
���bc1xI# patterns when the upsampling factor is not integer. The following image���`a
���bc1xJ# upsamples 500 data pixels to 530 rendered pixels. You may note a grid of���`a
���bc1xM# 30 line-like artifacts which stem from the 524 - 500 = 24 extra pixels that���`a
���bc1xL# had to be made up. Since interpolation is 'nearest' they are the same as a���`a
���bc1xJ# neighboring line of pixels and thus stretch the image locally so that it���`a
���bc1r# looks distorted.���`a
���`cfig���`a,���`a ���`bax���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`gfigsize���aoa=���`a(���bmfc6.8���`a,���`a ���bmfc6.8���`a)���`a)���`a
���`bax���aoa.���`fimshow���`a(���`aa���`a,���`a ���`minterpolation���aoa=���bs1a'���bs1gnearest���bs1a'���`a,���`a ���`dcmap���aoa=���bs1a'���bs1dgray���bs1a'���`a)���`a
���`bax���aoa.���`iset_title���`a(���bs2a"���bs2x+upsampled by factor a 1.048, interpolation=���bs2a'���bs2gnearest���bs2a'���bs2a"���`a)���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
���`a
���bc1xO###############################################################################���`a
���bc1x8# Better antialiasing algorithms can reduce this effect:���`a
���`cfig���`a,���`a ���`bax���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`gfigsize���aoa=���`a(���bmfc6.8���`a,���`a ���bmfc6.8���`a)���`a)���`a
���`bax���aoa.���`fimshow���`a(���`aa���`a,���`a ���`minterpolation���aoa=���bs1a'���bs1kantialiased���bs1a'���`a,���`a ���`dcmap���aoa=���bs1a'���bs1dgray���bs1a'���`a)���`a
���`bax���aoa.���`iset_title���`a(���bs2a"���bs2x+upsampled by factor a 1.048, interpolation=���bs2a'���bs2kantialiased���bs2a'���bs2a"���`a)���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
���`a
���bc1xO###############################################################################���`a
���bc1xK# Apart from the default 'hanning' antialiasing, `~.Axes.imshow` supports a���`a
���bc1xH# number of different interpolation algorithms, which may work better or���`a
���bc1x!# worse depending on the pattern.���`a
���`cfig���`a,���`a ���`caxs���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���bmia1���`a,���`a ���bmia2���`a,���`a ���`gfigsize���aoa=���`a(���bmia7���`a,���`a ���bmia4���`a)���`a,���`a ���`rconstrained_layout���aoa=���bkcdTrue���`a)���`a
���akcfor���`a ���`bax���`a,���`a ���`finterp���`a ���bowbin���`a ���bnbczip���`a(���`caxs���`a,���`a ���`a[���bs1a'���bs1ghanning���bs1a'���`a,���`a ���bs1a'���bs1glanczos���bs1a'���`a]���`a)���`a:���`a
���`d    ���`bax���aoa.���`fimshow���`a(���`aa���`a,���`a ���`minterpolation���aoa=���`finterp���`a,���`a ���`dcmap���aoa=���bs1a'���bs1dgray���bs1a'���`a)���`a
���`d    ���`bax���aoa.���`iset_title���`a(���bsaaf���bs2a"���bs2ninterpolation=���bs2a'���bsia{���`finterp���bsia}���bs2a'���bs2a"���`a)���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
���`a
���bc1xM#############################################################################���`a
���bc1a#���`a
���bc1x# .. admonition:: References���`a
���bc1a#���`a
���bc1xN#    The use of the following functions, methods, classes and modules is shown���`a
���bc1u#    in this example:���`a
���bc1a#���`a
���bc1x$#    - `matplotlib.axes.Axes.imshow`���`a
`dNone�