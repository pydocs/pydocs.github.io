������������bsdy"""
==========
Image Demo
==========

Many ways to plot images in Matplotlib.

The most common way to plot images in Matplotlib is with
`~.axes.Axes.imshow`. The following examples demonstrate much of the
functionality of imshow and the many images you can create.
"""���`a
���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnbcm���`a ���akbas���`a ���bnnbcm���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnecbook���`a ���akbas���`a ���bnnecbook���`a
���bkndfrom���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnndpath���`a ���bknfimport���`a ���`dPath���`a
���bkndfrom���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnngpatches���`a ���bknfimport���`a ���`iPathPatch���`a
���`a
���`a
���bc1x)# Fixing random state for reproducibility���`a
���`bnp���aoa.���`frandom���aoa.���`dseed���`a(���bmih19680801���`a)���`a
���`a
���bc1xO###############################################################################���`a
���bc1x># First we'll generate a simple bivariate normal distribution.���`a
���`a
���`edelta���`a ���aoa=���`a ���bmfe0.025���`a
���`ax���`a ���aoa=���`a ���`ay���`a ���aoa=���`a ���`bnp���aoa.���`farange���`a(���aoa-���bmfc3.0���`a,���`a ���bmfc3.0���`a,���`a ���`edelta���`a)���`a
���`aX���`a,���`a ���`aY���`a ���aoa=���`a ���`bnp���aoa.���`hmeshgrid���`a(���`ax���`a,���`a ���`ay���`a)���`a
���`bZ1���`a ���aoa=���`a ���`bnp���aoa.���`cexp���`a(���aoa-���`aX���aoa*���aoa*���bmia2���`a ���aoa-���`a ���`aY���aoa*���aoa*���bmia2���`a)���`a
���`bZ2���`a ���aoa=���`a ���`bnp���aoa.���`cexp���`a(���aoa-���`a(���`aX���`a ���aoa-���`a ���bmia1���`a)���aoa*���aoa*���bmia2���`a ���aoa-���`a ���`a(���`aY���`a ���aoa-���`a ���bmia1���`a)���aoa*���aoa*���bmia2���`a)���`a
���`aZ���`a ���aoa=���`a ���`a(���`bZ1���`a ���aoa-���`a ���`bZ2���`a)���`a ���aoa*���`a ���bmia2���`a
���`a
���`cfig���`a,���`a ���`bax���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`a)���`a
���`bim���`a ���aoa=���`a ���`bax���aoa.���`fimshow���`a(���`aZ���`a,���`a ���`minterpolation���aoa=���bs1a'���bs1hbilinear���bs1a'���`a,���`a ���`dcmap���aoa=���`bcm���aoa.���`fRdYlGn���`a,���`a
���`o               ���`forigin���aoa=���bs1a'���bs1elower���bs1a'���`a,���`a ���`fextent���aoa=���`a[���aoa-���bmia3���`a,���`a ���bmia3���`a,���`a ���aoa-���bmia3���`a,���`a ���bmia3���`a]���`a,���`a
���`o               ���`dvmax���aoa=���bnbcabs���`a(���`aZ���`a)���aoa.���`cmax���`a(���`a)���`a,���`a ���`dvmin���aoa=���aoa-���bnbcabs���`a(���`aZ���`a)���aoa.���`cmax���`a(���`a)���`a)���`a
���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
���`a
���`a
���bc1xO###############################################################################���`a
���bc1x1# It is also possible to show images of pictures.���`a
���`a
���bc1p# A sample image���`a
���akdwith���`a ���`ecbook���aoa.���`oget_sample_data���`a(���bs1a'���bs1pgrace_hopper.jpg���bs1a'���`a)���`a ���akbas���`a ���`jimage_file���`a:���`a
���`d    ���`eimage���`a ���aoa=���`a ���`cplt���aoa.���`fimread���`a(���`jimage_file���`a)���`a
���`a
���bc1x3# And another image, using 256x256 16-bit integers.���`a
���`aw���`a,���`a ���`ah���`a ���aoa=���`a ���bmic256���`a,���`a ���bmic256���`a
���akdwith���`a ���`ecbook���aoa.���`oget_sample_data���`a(���bs1a'���bs1ls1045.ima.gz���bs1a'���`a)���`a ���akbas���`a ���`hdatafile���`a:���`a
���`d    ���`as���`a ���aoa=���`a ���`hdatafile���aoa.���`dread���`a(���`a)���`a
���`aA���`a ���aoa=���`a ���`bnp���aoa.���`jfrombuffer���`a(���`as���`a,���`a ���`bnp���aoa.���`fuint16���`a)���aoa.���`fastype���`a(���bnbefloat���`a)���aoa.���`greshape���`a(���`a(���`aw���`a,���`a ���`ah���`a)���`a)���`a
���`fextent���`a ���aoa=���`a ���`a(���bmia0���`a,���`a ���bmib25���`a,���`a ���bmia0���`a,���`a ���bmib25���`a)���`a
���`a
���`cfig���`a,���`a ���`bax���`a ���aoa=���`a ���`cplt���aoa.���`nsubplot_mosaic���`a(���`a[���`a
���`d    ���`a[���bs1a'���bs1fhopper���bs1a'���`a,���`a ���bs1a'���bs1cmri���bs1a'���`a]���`a
���`a]���`a,���`a ���`gfigsize���aoa=���`a(���bmia7���`a,���`a ���bmfc3.5���`a)���`a)���`a
���`a
���`bax���`a[���bs1a'���bs1fhopper���bs1a'���`a]���aoa.���`fimshow���`a(���`eimage���`a)���`a
���`bax���`a[���bs1a'���bs1fhopper���bs1a'���`a]���aoa.���`daxis���`a(���bs1a'���bs1coff���bs1a'���`a)���`b  ���bc1x# clear x-axis and y-axis���`a
���`a
���`bim���`a ���aoa=���`a ���`bax���`a[���bs1a'���bs1cmri���bs1a'���`a]���aoa.���`fimshow���`a(���`aA���`a,���`a ���`dcmap���aoa=���`cplt���aoa.���`bcm���aoa.���`chot���`a,���`a ���`forigin���aoa=���bs1a'���bs1eupper���bs1a'���`a,���`a ���`fextent���aoa=���`fextent���`a)���`a
���`a
���`gmarkers���`a ���aoa=���`a ���`a[���`a(���bmfd15.9���`a,���`a ���bmfd14.5���`a)���`a,���`a ���`a(���bmfd16.8���`a,���`a ���bmib15���`a)���`a]���`a
���`ax���`a,���`a ���`ay���`a ���aoa=���`a ���bnbczip���`a(���aoa*���`gmarkers���`a)���`a
���`bax���`a[���bs1a'���bs1cmri���bs1a'���`a]���aoa.���`dplot���`a(���`ax���`a,���`a ���`ay���`a,���`a ���bs1a'���bs1ao���bs1a'���`a)���`a
���`a
���`bax���`a[���bs1a'���bs1cmri���bs1a'���`a]���aoa.���`iset_title���`a(���bs1a'���bs1cMRI���bs1a'���`a)���`a
���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
���`a
���`a
���bc1xO###############################################################################���`a
���bc1v# Interpolating images���`a
���bc1v# --------------------���`a
���bc1a#���`a
���bc1xO# It is also possible to interpolate images before displaying them. Be careful,���`a
���bc1xK# as this may manipulate the way your data looks, but it can be helpful for���`a
���bc1xJ# achieving the look you want. Below we'll display the same (small) array,���`a
���bc1x:# interpolated with three different interpolation methods.���`a
���bc1a#���`a
���bc1xJ# The center of the pixel at A[i, j] is plotted at (i+0.5, i+0.5).  If you���`a
���bc1xE# are using interpolation='nearest', the region bounded by (i, j) and���`a
���bc1xG# (i+1, j+1) will have the same color.  If you are using interpolation,���`a
���bc1xH# the pixel center will have the same color as it does with nearest, but���`a
���bc1xC# other pixels will be interpolated between the neighboring pixels.���`a
���bc1a#���`a
���bc1xM# To prevent edge effects when doing interpolation, Matplotlib pads the input���`a
���bc1xK# array with identical pixels around the edge: if you have a 5x5 array with���`a
���bc1w# colors a-y as below::���`a
���bc1a#���`a
���bc1m#   a b c d e���`a
���bc1m#   f g h i j���`a
���bc1m#   k l m n o���`a
���bc1m#   p q r s t���`a
���bc1m#   u v w x y���`a
���bc1a#���`a
���bc1xK# Matplotlib computes the interpolation and resizing on the padded array ::���`a
���bc1a#���`a
���bc1q#   a a b c d e e���`a
���bc1q#   a a b c d e e���`a
���bc1q#   f f g h i j j���`a
���bc1q#   k k l m n o o���`a
���bc1q#   p p q r s t t���`a
���bc1q#   o u v w x y y���`a
���bc1q#   o u v w x y y���`a
���bc1a#���`a
���bc1xN# and then extracts the central region of the result.  (Extremely old versions���`a
���bc1xL# of Matplotlib (<0.63) did not pad the array, but instead adjusted the view���`a
���bc1x*# limits to hide the affected edge areas.)���`a
���bc1a#���`a
���bc1xC# This approach allows plotting the full extent of an array without���`a
���bc1xE# edge effects, and for example to layer multiple images of different���`a
���bc1xD# sizes over one another with different interpolation methods -- see���`a
���bc1xK# :doc:`/gallery/images_contours_and_fields/layer_images`.  It also implies���`a
���bc1xI# a performance hit, as this new temporary, padded array must be created.���`a
���bc1xI# Sophisticated interpolation also implies a performance hit; for maximal���`a
���bc1xI# performance or very large images, interpolation='nearest' is suggested.���`a
���`a
���`aA���`a ���aoa=���`a ���`bnp���aoa.���`frandom���aoa.���`drand���`a(���bmia5���`a,���`a ���bmia5���`a)���`a
���`a
���`cfig���`a,���`a ���`caxs���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���bmia1���`a,���`a ���bmia3���`a,���`a ���`gfigsize���aoa=���`a(���bmib10���`a,���`a ���bmia3���`a)���`a)���`a
���akcfor���`a ���`bax���`a,���`a ���`finterp���`a ���bowbin���`a ���bnbczip���`a(���`caxs���`a,���`a ���`a[���bs1a'���bs1gnearest���bs1a'���`a,���`a ���bs1a'���bs1hbilinear���bs1a'���`a,���`a ���bs1a'���bs1gbicubic���bs1a'���`a]���`a)���`a:���`a
���`d    ���`bax���aoa.���`fimshow���`a(���`aA���`a,���`a ���`minterpolation���aoa=���`finterp���`a)���`a
���`d    ���`bax���aoa.���`iset_title���`a(���`finterp���aoa.���`jcapitalize���`a(���`a)���`a)���`a
���`d    ���`bax���aoa.���`dgrid���`a(���bkcdTrue���`a)���`a
���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
���`a
���`a
���bc1xO###############################################################################���`a
���bc1xH# You can specify whether images should be plotted with the array origin���`a
���bc1xI# x[0, 0] in the upper left or lower right by using the origin parameter.���`a
���bc1x?# You can also control the default setting image.origin in your���`a
���bc1xM# :ref:`matplotlibrc file <customizing-with-matplotlibrc-files>`. For more on���`a
���bc1x># this topic see the :doc:`complete guide on origin and extent���`a
���bc1x+# </tutorials/intermediate/imshow_extent>`.���`a
���`a
���`ax���`a ���aoa=���`a ���`bnp���aoa.���`farange���`a(���bmic120���`a)���aoa.���`greshape���`a(���`a(���bmib10���`a,���`a ���bmib12���`a)���`a)���`a
���`a
���`finterp���`a ���aoa=���`a ���bs1a'���bs1hbilinear���bs1a'���`a
���`cfig���`a,���`a ���`caxs���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`enrows���aoa=���bmia2���`a,���`a ���`fsharex���aoa=���bkcdTrue���`a,���`a ���`gfigsize���aoa=���`a(���bmia3���`a,���`a ���bmia5���`a)���`a)���`a
���`caxs���`a[���bmia0���`a]���aoa.���`iset_title���`a(���bs1a'���bs1qblue should be up���bs1a'���`a)���`a
���`caxs���`a[���bmia0���`a]���aoa.���`fimshow���`a(���`ax���`a,���`a ���`forigin���aoa=���bs1a'���bs1eupper���bs1a'���`a,���`a ���`minterpolation���aoa=���`finterp���`a)���`a
���`a
���`caxs���`a[���bmia1���`a]���aoa.���`iset_title���`a(���bs1a'���bs1sblue should be down���bs1a'���`a)���`a
���`caxs���`a[���bmia1���`a]���aoa.���`fimshow���`a(���`ax���`a,���`a ���`forigin���aoa=���bs1a'���bs1elower���bs1a'���`a,���`a ���`minterpolation���aoa=���`finterp���`a)���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
���`a
���`a
���bc1xO###############################################################################���`a
���bc1x1# Finally, we'll show an image using a clip path.���`a
���`a
���`edelta���`a ���aoa=���`a ���bmfe0.025���`a
���`ax���`a ���aoa=���`a ���`ay���`a ���aoa=���`a ���`bnp���aoa.���`farange���`a(���aoa-���bmfc3.0���`a,���`a ���bmfc3.0���`a,���`a ���`edelta���`a)���`a
���`aX���`a,���`a ���`aY���`a ���aoa=���`a ���`bnp���aoa.���`hmeshgrid���`a(���`ax���`a,���`a ���`ay���`a)���`a
���`bZ1���`a ���aoa=���`a ���`bnp���aoa.���`cexp���`a(���aoa-���`aX���aoa*���aoa*���bmia2���`a ���aoa-���`a ���`aY���aoa*���aoa*���bmia2���`a)���`a
���`bZ2���`a ���aoa=���`a ���`bnp���aoa.���`cexp���`a(���aoa-���`a(���`aX���`a ���aoa-���`a ���bmia1���`a)���aoa*���aoa*���bmia2���`a ���aoa-���`a ���`a(���`aY���`a ���aoa-���`a ���bmia1���`a)���aoa*���aoa*���bmia2���`a)���`a
���`aZ���`a ���aoa=���`a ���`a(���`bZ1���`a ���aoa-���`a ���`bZ2���`a)���`a ���aoa*���`a ���bmia2���`a
���`a
���`dpath���`a ���aoa=���`a ���`dPath���`a(���`a[���`a[���bmia0���`a,���`a ���bmia1���`a]���`a,���`a ���`a[���bmia1���`a,���`a ���bmia0���`a]���`a,���`a ���`a[���bmia0���`a,���`a ���aoa-���bmia1���`a]���`a,���`a ���`a[���aoa-���bmia1���`a,���`a ���bmia0���`a]���`a,���`a ���`a[���bmia0���`a,���`a ���bmia1���`a]���`a]���`a)���`a
���`epatch���`a ���aoa=���`a ���`iPathPatch���`a(���`dpath���`a,���`a ���`ifacecolor���aoa=���bs1a'���bs1dnone���bs1a'���`a)���`a
���`a
���`cfig���`a,���`a ���`bax���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`a)���`a
���`bax���aoa.���`iadd_patch���`a(���`epatch���`a)���`a
���`a
���`bim���`a ���aoa=���`a ���`bax���aoa.���`fimshow���`a(���`aZ���`a,���`a ���`minterpolation���aoa=���bs1a'���bs1hbilinear���bs1a'���`a,���`a ���`dcmap���aoa=���`bcm���aoa.���`dgray���`a,���`a
���`o               ���`forigin���aoa=���bs1a'���bs1elower���bs1a'���`a,���`a ���`fextent���aoa=���`a[���aoa-���bmia3���`a,���`a ���bmia3���`a,���`a ���aoa-���bmia3���`a,���`a ���bmia3���`a]���`a,���`a
���`o               ���`iclip_path���aoa=���`epatch���`a,���`a ���`gclip_on���aoa=���bkcdTrue���`a)���`a
���`bim���aoa.���`mset_clip_path���`a(���`epatch���`a)���`a
���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
���`a
���bc1xM#############################################################################���`a
���bc1a#���`a
���bc1x# .. admonition:: References���`a
���bc1a#���`a
���bc1xN#    The use of the following functions, methods, classes and modules is shown���`a
���bc1u#    in this example:���`a
���bc1a#���`a
���bc1xA#    - `matplotlib.axes.Axes.imshow` / `matplotlib.pyplot.imshow`���`a
���bc1x/#    - `matplotlib.artist.Artist.set_clip_path`���`a
���bc1x%#    - `matplotlib.patches.PathPatch`���`a
`dNone�