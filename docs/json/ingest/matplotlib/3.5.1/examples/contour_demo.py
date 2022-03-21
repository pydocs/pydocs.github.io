������������bsdy"""
============
Contour Demo
============

Illustrate simple contour plotting, contours on an image with
a colorbar for the contours, and labelled contours.

See also the :doc:`contour image example
</gallery/images_contours_and_fields/contour_image>`.
"""���`a
���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnbcm���`a ���akbas���`a ���bnnbcm���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���`a
���`a
���`edelta���`a ���aoa=���`a ���bmfe0.025���`a
���`ax���`a ���aoa=���`a ���`bnp���aoa.���`farange���`a(���aoa-���bmfc3.0���`a,���`a ���bmfc3.0���`a,���`a ���`edelta���`a)���`a
���`ay���`a ���aoa=���`a ���`bnp���aoa.���`farange���`a(���aoa-���bmfc2.0���`a,���`a ���bmfc2.0���`a,���`a ���`edelta���`a)���`a
���`aX���`a,���`a ���`aY���`a ���aoa=���`a ���`bnp���aoa.���`hmeshgrid���`a(���`ax���`a,���`a ���`ay���`a)���`a
���`bZ1���`a ���aoa=���`a ���`bnp���aoa.���`cexp���`a(���aoa-���`aX���aoa*���aoa*���bmia2���`a ���aoa-���`a ���`aY���aoa*���aoa*���bmia2���`a)���`a
���`bZ2���`a ���aoa=���`a ���`bnp���aoa.���`cexp���`a(���aoa-���`a(���`aX���`a ���aoa-���`a ���bmia1���`a)���aoa*���aoa*���bmia2���`a ���aoa-���`a ���`a(���`aY���`a ���aoa-���`a ���bmia1���`a)���aoa*���aoa*���bmia2���`a)���`a
���`aZ���`a ���aoa=���`a ���`a(���`bZ1���`a ���aoa-���`a ���`bZ2���`a)���`a ���aoa*���`a ���bmia2���`a
���`a
���bc1xO###############################################################################���`a
���bc1xL# Create a simple contour plot with labels using default colors.  The inline���`a
���bc1xK# argument to clabel will control whether the labels are draw over the line���`a
���bc1x@# segments of the contour, removing the lines beneath the label.���`a
���`a
���`cfig���`a,���`a ���`bax���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`a)���`a
���`bCS���`a ���aoa=���`a ���`bax���aoa.���`gcontour���`a(���`aX���`a,���`a ���`aY���`a,���`a ���`aZ���`a)���`a
���`bax���aoa.���`fclabel���`a(���`bCS���`a,���`a ���`finline���aoa=���bkcdTrue���`a,���`a ���`hfontsize���aoa=���bmib10���`a)���`a
���`bax���aoa.���`iset_title���`a(���bs1a'���bs1xSimplest default with labels���bs1a'���`a)���`a
���`a
���bc1xO###############################################################################���`a
���bc1xO# Contour labels can be placed manually by providing list of positions (in data���`a
���bc1xN# coordinate).  See :doc:`/gallery/event_handling/ginput_manual_clabel_sgskip`���`a
���bc1x# for interactive placement.���`a
���`a
���`cfig���`a,���`a ���`bax���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`a)���`a
���`bCS���`a ���aoa=���`a ���`bax���aoa.���`gcontour���`a(���`aX���`a,���`a ���`aY���`a,���`a ���`aZ���`a)���`a
���`pmanual_locations���`a ���aoa=���`a ���`a[���`a
���`d    ���`a(���aoa-���bmia1���`a,���`a ���aoa-���bmfc1.4���`a)���`a,���`a ���`a(���aoa-���bmfd0.62���`a,���`a ���aoa-���bmfc0.7���`a)���`a,���`a ���`a(���aoa-���bmia2���`a,���`a ���bmfc0.5���`a)���`a,���`a ���`a(���bmfc1.7���`a,���`a ���bmfc1.2���`a)���`a,���`a ���`a(���bmfc2.0���`a,���`a ���bmfc1.4���`a)���`a,���`a ���`a(���bmfc2.4���`a,���`a ���bmfc1.7���`a)���`a]���`a
���`bax���aoa.���`fclabel���`a(���`bCS���`a,���`a ���`finline���aoa=���bkcdTrue���`a,���`a ���`hfontsize���aoa=���bmib10���`a,���`a ���`fmanual���aoa=���`pmanual_locations���`a)���`a
���`bax���aoa.���`iset_title���`a(���bs1a'���bs1xlabels at selected locations���bs1a'���`a)���`a
���`a
���bc1xO###############################################################################���`a
���bc1x6# You can force all the contours to be the same color.���`a
���`a
���`cfig���`a,���`a ���`bax���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`a)���`a
���`bCS���`a ���aoa=���`a ���`bax���aoa.���`gcontour���`a(���`aX���`a,���`a ���`aY���`a,���`a ���`aZ���`a,���`a ���bmia6���`a,���`a ���`fcolors���aoa=���bs1a'���bs1ak���bs1a'���`a)���`b  ���bc1x&# Negative contours default to dashed.���`a
���`bax���aoa.���`fclabel���`a(���`bCS���`a,���`a ���`hfontsize���aoa=���bmia9���`a,���`a ���`finline���aoa=���bkcdTrue���`a)���`a
���`bax���aoa.���`iset_title���`a(���bs1a'���bs1x'Single color - negative contours dashed���bs1a'���`a)���`a
���`a
���bc1xO###############################################################################���`a
���bc1x># You can set negative contours to be solid instead of dashed:���`a
���`a
���`cplt���aoa.���`hrcParams���`a[���bs1a'���bs1xcontour.negative_linestyle���bs1a'���`a]���`a ���aoa=���`a ���bs1a'���bs1esolid���bs1a'���`a
���`cfig���`a,���`a ���`bax���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`a)���`a
���`bCS���`a ���aoa=���`a ���`bax���aoa.���`gcontour���`a(���`aX���`a,���`a ���`aY���`a,���`a ���`aZ���`a,���`a ���bmia6���`a,���`a ���`fcolors���aoa=���bs1a'���bs1ak���bs1a'���`a)���`b  ���bc1x&# Negative contours default to dashed.���`a
���`bax���aoa.���`fclabel���`a(���`bCS���`a,���`a ���`hfontsize���aoa=���bmia9���`a,���`a ���`finline���aoa=���bkcdTrue���`a)���`a
���`bax���aoa.���`iset_title���`a(���bs1a'���bs1x&Single color - negative contours solid���bs1a'���`a)���`a
���`a
���bc1xO###############################################################################���`a
���bc1x8# And you can manually specify the colors of the contour���`a
���`a
���`cfig���`a,���`a ���`bax���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`a)���`a
���`bCS���`a ���aoa=���`a ���`bax���aoa.���`gcontour���`a(���`aX���`a,���`a ���`aY���`a,���`a ���`aZ���`a,���`a ���bmia6���`a,���`a
���`p                ���`jlinewidths���aoa=���`bnp���aoa.���`farange���`a(���bmfb.5���`a,���`a ���bmia4���`a,���`a ���bmfb.5���`a)���`a,���`a
���`p                ���`fcolors���aoa=���`a(���bs1a'���bs1ar���bs1a'���`a,���`a ���bs1a'���bs1egreen���bs1a'���`a,���`a ���bs1a'���bs1dblue���bs1a'���`a,���`a ���`a(���bmia1���`a,���`a ���bmia1���`a,���`a ���bmia0���`a)���`a,���`a ���bs1a'���bs1g#afeeee���bs1a'���`a,���`a ���bs1a'���bs1c0.5���bs1a'���`a)���`a,���`a
���`p                ���`a)���`a
���`bax���aoa.���`fclabel���`a(���`bCS���`a,���`a ���`hfontsize���aoa=���bmia9���`a,���`a ���`finline���aoa=���bkcdTrue���`a)���`a
���`bax���aoa.���`iset_title���`a(���bs1a'���bs1kCrazy lines���bs1a'���`a)���`a
���`a
���bc1xO###############################################################################���`a
���bc1x># Or you can use a colormap to specify the colors; the default���`a
���bc1x-# colormap will be used for the contour lines���`a
���`a
���`cfig���`a,���`a ���`bax���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`a)���`a
���`bim���`a ���aoa=���`a ���`bax���aoa.���`fimshow���`a(���`aZ���`a,���`a ���`minterpolation���aoa=���bs1a'���bs1hbilinear���bs1a'���`a,���`a ���`forigin���aoa=���bs1a'���bs1elower���bs1a'���`a,���`a
���`o               ���`dcmap���aoa=���`bcm���aoa.���`dgray���`a,���`a ���`fextent���aoa=���`a(���aoa-���bmia3���`a,���`a ���bmia3���`a,���`a ���aoa-���bmia2���`a,���`a ���bmia2���`a)���`a)���`a
���`flevels���`a ���aoa=���`a ���`bnp���aoa.���`farange���`a(���aoa-���bmfc1.2���`a,���`a ���bmfc1.6���`a,���`a ���bmfc0.2���`a)���`a
���`bCS���`a ���aoa=���`a ���`bax���aoa.���`gcontour���`a(���`aZ���`a,���`a ���`flevels���`a,���`a ���`forigin���aoa=���bs1a'���bs1elower���bs1a'���`a,���`a ���`dcmap���aoa=���bs1a'���bs1dflag���bs1a'���`a,���`a ���`fextend���aoa=���bs1a'���bs1dboth���bs1a'���`a,���`a
���`p                ���`jlinewidths���aoa=���bmia2���`a,���`a ���`fextent���aoa=���`a(���aoa-���bmia3���`a,���`a ���bmia3���`a,���`a ���aoa-���bmia2���`a,���`a ���bmia2���`a)���`a)���`a
���`a
���bc1x# Thicken the zero contour.���`a
���`bCS���aoa.���`kcollections���`a[���bmia6���`a]���aoa.���`mset_linewidth���`a(���bmia4���`a)���`a
���`a
���`bax���aoa.���`fclabel���`a(���`bCS���`a,���`a ���`flevels���`a[���bmia1���`a:���`a:���bmia2���`a]���`a,���`b  ���bc1x# label every second level���`a
���`j          ���`finline���aoa=���bkcdTrue���`a,���`a ���`cfmt���aoa=���bs1a'���bsie%1.1f���bs1a'���`a,���`a ���`hfontsize���aoa=���bmib14���`a)���`a
���`a
���bc1x'# make a colorbar for the contour lines���`a
���`bCB���`a ���aoa=���`a ���`cfig���aoa.���`hcolorbar���`a(���`bCS���`a,���`a ���`fshrink���aoa=���bmfc0.8���`a)���`a
���`a
���`bax���aoa.���`iset_title���`a(���bs1a'���bs1sLines with colorbar���bs1a'���`a)���`a
���`a
���bc1x1# We can still add a colorbar for the image, too.���`a
���`cCBI���`a ���aoa=���`a ���`cfig���aoa.���`hcolorbar���`a(���`bim���`a,���`a ���`korientation���aoa=���bs1a'���bs1jhorizontal���bs1a'���`a,���`a ���`fshrink���aoa=���bmfc0.8���`a)���`a
���`a
���bc1x;# This makes the original colorbar look a bit out of place,���`a
���bc1x # so let's improve its position.���`a
���`a
���`al���`a,���`a ���`ab���`a,���`a ���`aw���`a,���`a ���`ah���`a ���aoa=���`a ���`bax���aoa.���`lget_position���`a(���`a)���aoa.���`fbounds���`a
���`bll���`a,���`a ���`bbb���`a,���`a ���`bww���`a,���`a ���`bhh���`a ���aoa=���`a ���`bCB���aoa.���`bax���aoa.���`lget_position���`a(���`a)���aoa.���`fbounds���`a
���`bCB���aoa.���`bax���aoa.���`lset_position���`a(���`a[���`bll���`a,���`a ���`ab���`a ���aoa+���`a ���bmfc0.1���aoa*���`ah���`a,���`a ���`bww���`a,���`a ���`ah���aoa*���bmfc0.8���`a]���`a)���`a
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
���bc1xC#    - `matplotlib.axes.Axes.contour` / `matplotlib.pyplot.contour`���`a
���bc1xI#    - `matplotlib.figure.Figure.colorbar` / `matplotlib.pyplot.colorbar`���`a
���bc1xA#    - `matplotlib.axes.Axes.clabel` / `matplotlib.pyplot.clabel`���`a
���bc1x*#    - `matplotlib.axes.Axes.get_position`���`a
���bc1x*#    - `matplotlib.axes.Axes.set_position`���`a
`dNone�