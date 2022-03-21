��������4���bsdy"""
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
"""���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���bkndfrom���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����`a ���bknfimport���`a ���`bcm���`a
���`a
���bc1xG# Default delta is large because that makes it fast, and it illustrates���`a
���bc1x6# the correct registration between image and contours.���`a
���`edelta���`a ���aoa=���`a ���bmfc0.5���`a
���`a
���`fextent���`a ���aoa=���`a ���`a(���aoa-���bmia3���`a,���`a ���bmia4���`a,���`a ���aoa-���bmia4���`a,���`a ���bmia3���`a)���`a
���`a
���`ax���`a ���aoa=���`a ���`bnp���aoa.���`farange���`a(���aoa-���bmfc3.0���`a,���`a ���bmfe4.001���`a,���`a ���`edelta���`a)���`a
���`ay���`a ���aoa=���`a ���`bnp���aoa.���`farange���`a(���aoa-���bmfc4.0���`a,���`a ���bmfe3.001���`a,���`a ���`edelta���`a)���`a
���`aX���`a,���`a ���`aY���`a ���aoa=���`a ���`bnp���aoa.���`hmeshgrid���`a(���`ax���`a,���`a ���`ay���`a)���`a
���`bZ1���`a ���aoa=���`a ���`bnp���aoa.���`cexp���`a(���aoa-���`aX���aoa*���aoa*���bmia2���`a ���aoa-���`a ���`aY���aoa*���aoa*���bmia2���`a)���`a
���`bZ2���`a ���aoa=���`a ���`bnp���aoa.���`cexp���`a(���aoa-���`a(���`aX���`a ���aoa-���`a ���bmia1���`a)���aoa*���aoa*���bmia2���`a ���aoa-���`a ���`a(���`aY���`a ���aoa-���`a ���bmia1���`a)���aoa*���aoa*���bmia2���`a)���`a
���`aZ���`a ���aoa=���`a ���`a(���`bZ1���`a ���aoa-���`a ���`bZ2���`a)���`a ���aoa*���`a ���bmia2���`a
���`a
���bc1x3# Boost the upper limit to avoid truncation errors.���`a
���`flevels���`a ���aoa=���`a ���`bnp���aoa.���`farange���`a(���aoa-���bmfc2.0���`a,���`a ���bmfe1.601���`a,���`a ���bmfc0.4���`a)���`a
���`a
���`dnorm���`a ���aoa=���`a ���`bcm���aoa.���`fcolors���aoa.���`iNormalize���`a(���`dvmax���aoa=���bnbcabs���`a(���`aZ���`a)���aoa.���`cmax���`a(���`a)���`a,���`a ���`dvmin���aoa=���aoa-���bnbcabs���`a(���`aZ���`a)���aoa.���`cmax���`a(���`a)���`a)���`a
���`dcmap���`a ���aoa=���`a ���`bcm���aoa.���`dPRGn���`a
���`a
���`cfig���`a,���`a ���`d_axs���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`enrows���aoa=���bmia2���`a,���`a ���`encols���aoa=���bmia2���`a)���`a
���`cfig���aoa.���`osubplots_adjust���`a(���`fhspace���aoa=���bmfc0.3���`a)���`a
���`caxs���`a ���aoa=���`a ���`d_axs���aoa.���`gflatten���`a(���`a)���`a
���`a
���`ecset1���`a ���aoa=���`a ���`caxs���`a[���bmia0���`a]���aoa.���`hcontourf���`a(���`aX���`a,���`a ���`aY���`a,���`a ���`aZ���`a,���`a ���`flevels���`a,���`a ���`dnorm���aoa=���`dnorm���`a,���`a
���`x                        ���`dcmap���aoa=���`bcm���aoa.���`hget_cmap���`a(���`dcmap���`a,���`a ���bnbclen���`a(���`flevels���`a)���`a ���aoa-���`a ���bmia1���`a)���`a)���`a
���bc1x=# It is not necessary, but for the colormap, we need only the���`a
���bc1x?# number of levels minus 1.  To avoid discretization error, use���`a
���bc1xA# either this number or a large number such as the default (256).���`a
���`a
���bc1x=# If we want lines as well as filled regions, we need to call���`a
���bc1xD# contour separately; don't try to change the edgecolor or edgewidth���`a
���bc1x:# of the polygons in the collections returned by contourf.���`a
���bc1xF# Use levels output from previous call to guarantee they are the same.���`a
���`a
���`ecset2���`a ���aoa=���`a ���`caxs���`a[���bmia0���`a]���aoa.���`gcontour���`a(���`aX���`a,���`a ���`aY���`a,���`a ���`aZ���`a,���`a ���`ecset1���aoa.���`flevels���`a,���`a ���`fcolors���aoa=���bs1a'���bs1ak���bs1a'���`a)���`a
���`a
���bc1x@# We don't really need dashed contour lines to indicate negative���`a
���bc1x"# regions, so let's turn them off.���`a
���`a
���akcfor���`a ���`ac���`a ���bowbin���`a ���`ecset2���aoa.���`kcollections���`a:���`a
���`d    ���`ac���aoa.���`mset_linestyle���`a(���bs1a'���bs1esolid���bs1a'���`a)���`a
���`a
���bc1x;# It is easier here to make a separate call to contour than���`a
���bc1x.# to set up an array of colors and linewidths.���`a
���bc1x5# We are making a thick green line as a zero contour.���`a
���bc1x6# Specify the zero level as a tuple with only 0 in it.���`a
���`a
���`ecset3���`a ���aoa=���`a ���`caxs���`a[���bmia0���`a]���aoa.���`gcontour���`a(���`aX���`a,���`a ���`aY���`a,���`a ���`aZ���`a,���`a ���`a(���bmia0���`a,���`a)���`a,���`a ���`fcolors���aoa=���bs1a'���bs1ag���bs1a'���`a,���`a ���`jlinewidths���aoa=���bmia2���`a)���`a
���`caxs���`a[���bmia0���`a]���aoa.���`iset_title���`a(���bs1a'���bs1oFilled contours���bs1a'���`a)���`a
���`cfig���aoa.���`hcolorbar���`a(���`ecset1���`a,���`a ���`bax���aoa=���`caxs���`a[���bmia0���`a]���`a)���`a
���`a
���`a
���`caxs���`a[���bmia1���`a]���aoa.���`fimshow���`a(���`aZ���`a,���`a ���`fextent���aoa=���`fextent���`a,���`a ���`dcmap���aoa=���`dcmap���`a,���`a ���`dnorm���aoa=���`dnorm���`a)���`a
���`caxs���`a[���bmia1���`a]���aoa.���`gcontour���`a(���`aZ���`a,���`a ���`flevels���`a,���`a ���`fcolors���aoa=���bs1a'���bs1ak���bs1a'���`a,���`a ���`forigin���aoa=���bs1a'���bs1eupper���bs1a'���`a,���`a ���`fextent���aoa=���`fextent���`a)���`a
���`caxs���`a[���bmia1���`a]���aoa.���`iset_title���`a(���bs2a"���bs2nImage, origin ���bs2a'���bs2eupper���bs2a'���bs2a"���`a)���`a
���`a
���`caxs���`a[���bmia2���`a]���aoa.���`fimshow���`a(���`aZ���`a,���`a ���`forigin���aoa=���bs1a'���bs1elower���bs1a'���`a,���`a ���`fextent���aoa=���`fextent���`a,���`a ���`dcmap���aoa=���`dcmap���`a,���`a ���`dnorm���aoa=���`dnorm���`a)���`a
���`caxs���`a[���bmia2���`a]���aoa.���`gcontour���`a(���`aZ���`a,���`a ���`flevels���`a,���`a ���`fcolors���aoa=���bs1a'���bs1ak���bs1a'���`a,���`a ���`forigin���aoa=���bs1a'���bs1elower���bs1a'���`a,���`a ���`fextent���aoa=���`fextent���`a)���`a
���`caxs���`a[���bmia2���`a]���aoa.���`iset_title���`a(���bs2a"���bs2nImage, origin ���bs2a'���bs2elower���bs2a'���bs2a"���`a)���`a
���`a
���bc1xA# We will use the interpolation "nearest" here to show the actual���`a
���bc1o# image pixels.���`a
���bc1xB# Note that the contour lines don't extend to the edge of the box.���`a
���bc1xE# This is intentional. The Z values are defined at the center of each���`a
���bc1xA# image pixel (each color block on the following subplot), so the���`a
���bc1xF# domain that is contoured does not extend beyond these pixel centers.���`a
���`bim���`a ���aoa=���`a ���`caxs���`a[���bmia3���`a]���aoa.���`fimshow���`a(���`aZ���`a,���`a ���`minterpolation���aoa=���bs1a'���bs1gnearest���bs1a'���`a,���`a ���`fextent���aoa=���`fextent���`a,���`a
���`s                   ���`dcmap���aoa=���`dcmap���`a,���`a ���`dnorm���aoa=���`dnorm���`a)���`a
���`caxs���`a[���bmia3���`a]���aoa.���`gcontour���`a(���`aZ���`a,���`a ���`flevels���`a,���`a ���`fcolors���aoa=���bs1a'���bs1ak���bs1a'���`a,���`a ���`forigin���aoa=���bs1a'���bs1eimage���bs1a'���`a,���`a ���`fextent���aoa=���`fextent���`a)���`a
���`dylim���`a ���aoa=���`a ���`caxs���`a[���bmia3���`a]���aoa.���`hget_ylim���`a(���`a)���`a
���`caxs���`a[���bmia3���`a]���aoa.���`hset_ylim���`a(���`dylim���`a[���`a:���`a:���aoa-���bmia1���`a]���`a)���`a
���`caxs���`a[���bmia3���`a]���aoa.���`iset_title���`a(���bs2a"���bs2xOrigin from rc, reversed y-axis���bs2a"���`a)���`a
���`cfig���aoa.���`hcolorbar���`a(���`bim���`a,���`a ���`bax���aoa=���`caxs���`a[���bmia3���`a]���`a)���`a
���`a
���`cfig���aoa.���`ltight_layout���`a(���`a)���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
���`a
���`a
���bc1xM#############################################################################���`a
���bc1a#���`a
���bc1x# .. admonition:: References���`a
���bc1a#���`a
���bc1xN#    The use of the following functions, methods, classes and modules is shown���`a
���bc1u#    in this example:���`a
���bc1a#���`a
���bc1xC#    - `matplotlib.axes.Axes.contour` / `matplotlib.pyplot.contour`���`a
���bc1xA#    - `matplotlib.axes.Axes.imshow` / `matplotlib.pyplot.imshow`���`a
���bc1xI#    - `matplotlib.figure.Figure.colorbar` / `matplotlib.pyplot.colorbar`���`a
���bc1x$#    - `matplotlib.colors.Normalize`���`a
`dNone�