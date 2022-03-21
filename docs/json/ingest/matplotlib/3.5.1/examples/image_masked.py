��������{���bsdx�"""
============
Image Masked
============

imshow with masked array input and out-of-range colors.

The second subplot illustrates the use of BoundaryNorm to
get a filled contour effect.
"""���`a
���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfcolors���`a ���akbas���`a ���bnnfcolors���`a
���`a
���bc1x# compute some interesting data���`a
���`bx0���`a,���`a ���`bx1���`a ���aoa=���`a ���aoa-���bmia5���`a,���`a ���bmia5���`a
���`by0���`a,���`a ���`by1���`a ���aoa=���`a ���aoa-���bmia3���`a,���`a ���bmia3���`a
���`ax���`a ���aoa=���`a ���`bnp���aoa.���`hlinspace���`a(���`bx0���`a,���`a ���`bx1���`a,���`a ���bmic500���`a)���`a
���`ay���`a ���aoa=���`a ���`bnp���aoa.���`hlinspace���`a(���`by0���`a,���`a ���`by1���`a,���`a ���bmic500���`a)���`a
���`aX���`a,���`a ���`aY���`a ���aoa=���`a ���`bnp���aoa.���`hmeshgrid���`a(���`ax���`a,���`a ���`ay���`a)���`a
���`bZ1���`a ���aoa=���`a ���`bnp���aoa.���`cexp���`a(���aoa-���`aX���aoa*���aoa*���bmia2���`a ���aoa-���`a ���`aY���aoa*���aoa*���bmia2���`a)���`a
���`bZ2���`a ���aoa=���`a ���`bnp���aoa.���`cexp���`a(���aoa-���`a(���`aX���`a ���aoa-���`a ���bmia1���`a)���aoa*���aoa*���bmia2���`a ���aoa-���`a ���`a(���`aY���`a ���aoa-���`a ���bmia1���`a)���aoa*���aoa*���bmia2���`a)���`a
���`aZ���`a ���aoa=���`a ���`a(���`bZ1���`a ���aoa-���`a ���`bZ2���`a)���`a ���aoa*���`a ���bmia2���`a
���`a
���bc1t# Set up a colormap:���`a
���`gpalette���`a ���aoa=���`a ���`cplt���aoa.���`bcm���aoa.���`dgray���aoa.���`mwith_extremes���`a(���`dover���aoa=���bs1a'���bs1ar���bs1a'���`a,���`a ���`eunder���aoa=���bs1a'���bs1ag���bs1a'���`a,���`a ���`cbad���aoa=���bs1a'���bs1ab���bs1a'���`a)���`a
���bc1x# Alternatively, we could use���`a
���bc1x# palette.set_bad(alpha = 0.0)���`a
���bc1x;# to make the bad region transparent.  This is the default.���`a
���bc1x=# If you comment out all the palette.set* lines, you will see���`a
���bc1x;# all the defaults; under and over will be colored with the���`a
���bc1x5# first and last colors in the palette, respectively.���`a
���`bZm���`a ���aoa=���`a ���`bnp���aoa.���`bma���aoa.���`lmasked_where���`a(���`aZ���`a ���aoa>���`a ���bmfc1.2���`a,���`a ���`aZ���`a)���`a
���`a
���bc1x8# By setting vmin and vmax in the norm, we establish the���`a
���bc1x<# range to which the regular palette color scale is applied.���`a
���bc1xF# Anything above that range is colored based on palette.set_over, etc.���`a
���`a
���bc1x# set up the Axes objects���`a
���`cfig���`a,���`a ���`a(���`cax1���`a,���`a ���`cax2���`a)���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`enrows���aoa=���bmia2���`a,���`a ���`gfigsize���aoa=���`a(���bmia6���`a,���`a ���bmfc5.4���`a)���`a)���`a
���`a
���bc1x"# plot using 'continuous' colormap���`a
���`bim���`a ���aoa=���`a ���`cax1���aoa.���`fimshow���`a(���`bZm���`a,���`a ���`minterpolation���aoa=���bs1a'���bs1hbilinear���bs1a'���`a,���`a
���`p                ���`dcmap���aoa=���`gpalette���`a,���`a
���`p                ���`dnorm���aoa=���`fcolors���aoa.���`iNormalize���`a(���`dvmin���aoa=���aoa-���bmfc1.0���`a,���`a ���`dvmax���aoa=���bmfc1.0���`a)���`a,���`a
���`p                ���`faspect���aoa=���bs1a'���bs1dauto���bs1a'���`a,���`a
���`p                ���`forigin���aoa=���bs1a'���bs1elower���bs1a'���`a,���`a
���`p                ���`fextent���aoa=���`a[���`bx0���`a,���`a ���`bx1���`a,���`a ���`by0���`a,���`a ���`by1���`a]���`a)���`a
���`cax1���aoa.���`iset_title���`a(���bs1a'���bs1x Green=low, Red=high, Blue=masked���bs1a'���`a)���`a
���`dcbar���`a ���aoa=���`a ���`cfig���aoa.���`hcolorbar���`a(���`bim���`a,���`a ���`fextend���aoa=���bs1a'���bs1dboth���bs1a'���`a,���`a ���`fshrink���aoa=���bmfc0.9���`a,���`a ���`bax���aoa=���`cax1���`a)���`a
���`dcbar���aoa.���`iset_label���`a(���bs1a'���bs1guniform���bs1a'���`a)���`a
���akcfor���`a ���`iticklabel���`a ���bowbin���`a ���`cax1���aoa.���`exaxis���aoa.���`nget_ticklabels���`a(���`a)���`a:���`a
���`d    ���`iticklabel���aoa.���`kset_visible���`a(���bkceFalse���`a)���`a
���`a
���bc1xG# Plot using a small number of colors, with unevenly spaced boundaries.���`a
���`bim���`a ���aoa=���`a ���`cax2���aoa.���`fimshow���`a(���`bZm���`a,���`a ���`minterpolation���aoa=���bs1a'���bs1gnearest���bs1a'���`a,���`a
���`p                ���`dcmap���aoa=���`gpalette���`a,���`a
���`p                ���`dnorm���aoa=���`fcolors���aoa.���`lBoundaryNorm���`a(���`a[���aoa-���bmia1���`a,���`a ���aoa-���bmfc0.5���`a,���`a ���aoa-���bmfc0.2���`a,���`a ���bmia0���`a,���`a ���bmfc0.2���`a,���`a ���bmfc0.5���`a,���`a ���bmia1���`a]���`a,���`a
���`x)                                         ���`gncolors���aoa=���`gpalette���aoa.���`aN���`a)���`a,���`a
���`p                ���`faspect���aoa=���bs1a'���bs1dauto���bs1a'���`a,���`a
���`p                ���`forigin���aoa=���bs1a'���bs1elower���bs1a'���`a,���`a
���`p                ���`fextent���aoa=���`a[���`bx0���`a,���`a ���`bx1���`a,���`a ���`by0���`a,���`a ���`by1���`a]���`a)���`a
���`cax2���aoa.���`iset_title���`a(���bs1a'���bs1qWith BoundaryNorm���bs1a'���`a)���`a
���`dcbar���`a ���aoa=���`a ���`cfig���aoa.���`hcolorbar���`a(���`bim���`a,���`a ���`fextend���aoa=���bs1a'���bs1dboth���bs1a'���`a,���`a ���`gspacing���aoa=���bs1a'���bs1lproportional���bs1a'���`a,���`a
���`t                    ���`fshrink���aoa=���bmfc0.9���`a,���`a ���`bax���aoa=���`cax2���`a)���`a
���`dcbar���aoa.���`iset_label���`a(���bs1a'���bs1lproportional���bs1a'���`a)���`a
���`a
���`cfig���aoa.���`hsuptitle���`a(���bs1a'���bs1x)imshow, with out-of-range and masked data���bs1a'���`a)���`a
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
���bc1xI#    - `matplotlib.figure.Figure.colorbar` / `matplotlib.pyplot.colorbar`���`a
���bc1x'#    - `matplotlib.colors.BoundaryNorm`���`a
���bc1x/#    - `matplotlib.colorbar.Colorbar.set_label`���`a
`dNone�