Ù¯‚Ù´ƒ™{Ù±‚bsdx¿"""
============
Image Masked
============

imshow with masked array input and out-of-range colors.

The second subplot illustrates the use of BoundaryNorm to
get a filled contour effect.
"""Ù±‚`a
Ù±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„enumpyÙ „enumpyf1.22.3fmoduleenumpyfmoduleõÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnnbnpÙ±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnnfpyplotÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnncpltÙ±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnnfcolorsÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnnfcolorsÙ±‚`a
Ù±‚`a
Ù±‚bc1x# compute some interesting dataÙ±‚`a
Ù±‚`bx0Ù±‚`a,Ù±‚`a Ù±‚`bx1Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚aoa-Ù±‚bmia5Ù±‚`a,Ù±‚`a Ù±‚bmia5Ù±‚`a
Ù±‚`by0Ù±‚`a,Ù±‚`a Ù±‚`by1Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚aoa-Ù±‚bmia3Ù±‚`a,Ù±‚`a Ù±‚bmia3Ù±‚`a
Ù±‚`axÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`hlinspaceÙ±‚`a(Ù±‚`bx0Ù±‚`a,Ù±‚`a Ù±‚`bx1Ù±‚`a,Ù±‚`a Ù±‚bmic500Ù±‚`a)Ù±‚`a
Ù±‚`ayÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`hlinspaceÙ±‚`a(Ù±‚`by0Ù±‚`a,Ù±‚`a Ù±‚`by1Ù±‚`a,Ù±‚`a Ù±‚bmic500Ù±‚`a)Ù±‚`a
Ù±‚`aXÙ±‚`a,Ù±‚`a Ù±‚`aYÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`hmeshgridÙ±‚`a(Ù±‚`axÙ±‚`a,Ù±‚`a Ù±‚`ayÙ±‚`a)Ù±‚`a
Ù±‚`bZ1Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`cexpÙ±‚`a(Ù±‚aoa-Ù±‚`aXÙ±‚aoa*Ù±‚aoa*Ù±‚bmia2Ù±‚`a Ù±‚aoa-Ù±‚`a Ù±‚`aYÙ±‚aoa*Ù±‚aoa*Ù±‚bmia2Ù±‚`a)Ù±‚`a
Ù±‚`bZ2Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`cexpÙ±‚`a(Ù±‚aoa-Ù±‚`a(Ù±‚`aXÙ±‚`a Ù±‚aoa-Ù±‚`a Ù±‚bmia1Ù±‚`a)Ù±‚aoa*Ù±‚aoa*Ù±‚bmia2Ù±‚`a Ù±‚aoa-Ù±‚`a Ù±‚`a(Ù±‚`aYÙ±‚`a Ù±‚aoa-Ù±‚`a Ù±‚bmia1Ù±‚`a)Ù±‚aoa*Ù±‚aoa*Ù±‚bmia2Ù±‚`a)Ù±‚`a
Ù±‚`aZÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`a(Ù±‚`bZ1Ù±‚`a Ù±‚aoa-Ù±‚`a Ù±‚`bZ2Ù±‚`a)Ù±‚`a Ù±‚aoa*Ù±‚`a Ù±‚bmia2Ù±‚`a
Ù±‚`a
Ù±‚bc1t# Set up a colormap:Ù±‚`a
Ù±‚`gpaletteÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cpltÙ±‚aoa.Ù±‚`bcmÙ±‚aoa.Ù±‚`dgrayÙ±‚aoa.Ù±‚`mwith_extremesÙ±‚`a(Ù±‚`doverÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1arÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`eunderÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1agÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`cbadÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1abÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚bc1x# Alternatively, we could useÙ±‚`a
Ù±‚bc1x# palette.set_bad(alpha = 0.0)Ù±‚`a
Ù±‚bc1x;# to make the bad region transparent.  This is the default.Ù±‚`a
Ù±‚bc1x=# If you comment out all the palette.set* lines, you will seeÙ±‚`a
Ù±‚bc1x;# all the defaults; under and over will be colored with theÙ±‚`a
Ù±‚bc1x5# first and last colors in the palette, respectively.Ù±‚`a
Ù±‚`bZmÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`bmaÙ±‚aoa.Ù±‚`lmasked_whereÙ±‚`a(Ù±‚`aZÙ±‚`a Ù±‚aoa>Ù±‚`a Ù±‚bmfc1.2Ù±‚`a,Ù±‚`a Ù±‚`aZÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚bc1x8# By setting vmin and vmax in the norm, we establish theÙ±‚`a
Ù±‚bc1x<# range to which the regular palette color scale is applied.Ù±‚`a
Ù±‚bc1xF# Anything above that range is colored based on palette.set_over, etc.Ù±‚`a
Ù±‚`a
Ù±‚bc1x# set up the Axes objectsÙ±‚`a
Ù±‚`cfigÙ±‚`a,Ù±‚`a Ù±‚`a(Ù±‚`cax1Ù±‚`a,Ù±‚`a Ù±‚`cax2Ù±‚`a)Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cpltÙ±‚aoa.Ù±‚`hsubplotsÙ±‚`a(Ù±‚`enrowsÙ±‚aoa=Ù±‚bmia2Ù±‚`a,Ù±‚`a Ù±‚`gfigsizeÙ±‚aoa=Ù±‚`a(Ù±‚bmia6Ù±‚`a,Ù±‚`a Ù±‚bmfc5.4Ù±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚bc1x"# plot using 'continuous' colormapÙ±‚`a
Ù±‚`bimÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cax1Ù±‚aoa.Ù±‚`fimshowÙ±‚`a(Ù±‚`bZmÙ±‚`a,Ù±‚`a Ù±‚`minterpolationÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1hbilinearÙ±‚bs1a'Ù±‚`a,Ù±‚`a
Ù±‚`p                Ù±‚`dcmapÙ±‚aoa=Ù±‚`gpaletteÙ±‚`a,Ù±‚`a
Ù±‚`p                Ù±‚`dnormÙ±‚aoa=Ù±‚`fcolorsÙ±‚aoa.Ù±‚`iNormalizeÙ±‚`a(Ù±‚`dvminÙ±‚aoa=Ù±‚aoa-Ù±‚bmfc1.0Ù±‚`a,Ù±‚`a Ù±‚`dvmaxÙ±‚aoa=Ù±‚bmfc1.0Ù±‚`a)Ù±‚`a,Ù±‚`a
Ù±‚`p                Ù±‚`faspectÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1dautoÙ±‚bs1a'Ù±‚`a,Ù±‚`a
Ù±‚`p                Ù±‚`foriginÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1elowerÙ±‚bs1a'Ù±‚`a,Ù±‚`a
Ù±‚`p                Ù±‚`fextentÙ±‚aoa=Ù±‚`a[Ù±‚`bx0Ù±‚`a,Ù±‚`a Ù±‚`bx1Ù±‚`a,Ù±‚`a Ù±‚`by0Ù±‚`a,Ù±‚`a Ù±‚`by1Ù±‚`a]Ù±‚`a)Ù±‚`a
Ù±‚`cax1Ù±‚aoa.Ù±‚`iset_titleÙ±‚`a(Ù±‚bs1a'Ù±‚bs1x Green=low, Red=high, Blue=maskedÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`dcbarÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cfigÙ±‚aoa.Ù±‚`hcolorbarÙ±‚`a(Ù±‚`bimÙ±‚`a,Ù±‚`a Ù±‚`fextendÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1dbothÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`fshrinkÙ±‚aoa=Ù±‚bmfc0.9Ù±‚`a,Ù±‚`a Ù±‚`baxÙ±‚aoa=Ù±‚`cax1Ù±‚`a)Ù±‚`a
Ù±‚`dcbarÙ±‚aoa.Ù±‚`iset_labelÙ±‚`a(Ù±‚bs1a'Ù±‚bs1guniformÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚akcforÙ±‚`a Ù±‚`iticklabelÙ±‚`a Ù±‚bowbinÙ±‚`a Ù±‚`cax1Ù±‚aoa.Ù±‚`exaxisÙ±‚aoa.Ù±‚`nget_ticklabelsÙ±‚`a(Ù±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`d    Ù±‚`iticklabelÙ±‚aoa.Ù±‚`kset_visibleÙ±‚`a(Ù±‚bkceFalseÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚bc1xG# Plot using a small number of colors, with unevenly spaced boundaries.Ù±‚`a
Ù±‚`bimÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cax2Ù±‚aoa.Ù±‚`fimshowÙ±‚`a(Ù±‚`bZmÙ±‚`a,Ù±‚`a Ù±‚`minterpolationÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1gnearestÙ±‚bs1a'Ù±‚`a,Ù±‚`a
Ù±‚`p                Ù±‚`dcmapÙ±‚aoa=Ù±‚`gpaletteÙ±‚`a,Ù±‚`a
Ù±‚`p                Ù±‚`dnormÙ±‚aoa=Ù±‚`fcolorsÙ±‚aoa.Ù±‚`lBoundaryNormÙ±‚`a(Ù±‚`a[Ù±‚aoa-Ù±‚bmia1Ù±‚`a,Ù±‚`a Ù±‚aoa-Ù±‚bmfc0.5Ù±‚`a,Ù±‚`a Ù±‚aoa-Ù±‚bmfc0.2Ù±‚`a,Ù±‚`a Ù±‚bmia0Ù±‚`a,Ù±‚`a Ù±‚bmfc0.2Ù±‚`a,Ù±‚`a Ù±‚bmfc0.5Ù±‚`a,Ù±‚`a Ù±‚bmia1Ù±‚`a]Ù±‚`a,Ù±‚`a
Ù±‚`x)                                         Ù±‚`gncolorsÙ±‚aoa=Ù±‚`gpaletteÙ±‚aoa.Ù±‚`aNÙ±‚`a)Ù±‚`a,Ù±‚`a
Ù±‚`p                Ù±‚`faspectÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1dautoÙ±‚bs1a'Ù±‚`a,Ù±‚`a
Ù±‚`p                Ù±‚`foriginÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1elowerÙ±‚bs1a'Ù±‚`a,Ù±‚`a
Ù±‚`p                Ù±‚`fextentÙ±‚aoa=Ù±‚`a[Ù±‚`bx0Ù±‚`a,Ù±‚`a Ù±‚`bx1Ù±‚`a,Ù±‚`a Ù±‚`by0Ù±‚`a,Ù±‚`a Ù±‚`by1Ù±‚`a]Ù±‚`a)Ù±‚`a
Ù±‚`cax2Ù±‚aoa.Ù±‚`iset_titleÙ±‚`a(Ù±‚bs1a'Ù±‚bs1qWith BoundaryNormÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`dcbarÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cfigÙ±‚aoa.Ù±‚`hcolorbarÙ±‚`a(Ù±‚`bimÙ±‚`a,Ù±‚`a Ù±‚`fextendÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1dbothÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`gspacingÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1lproportionalÙ±‚bs1a'Ù±‚`a,Ù±‚`a
Ù±‚`t                    Ù±‚`fshrinkÙ±‚aoa=Ù±‚bmfc0.9Ù±‚`a,Ù±‚`a Ù±‚`baxÙ±‚aoa=Ù±‚`cax2Ù±‚`a)Ù±‚`a
Ù±‚`dcbarÙ±‚aoa.Ù±‚`iset_labelÙ±‚`a(Ù±‚bs1a'Ù±‚bs1lproportionalÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`cfigÙ±‚aoa.Ù±‚`hsuptitleÙ±‚`a(Ù±‚bs1a'Ù±‚bs1x)imshow, with out-of-range and masked dataÙ±‚bs1a'Ù±‚`a)Ù±‚`a
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
Ù±‚bc1xI#    - `matplotlib.figure.Figure.colorbar` / `matplotlib.pyplot.colorbar`Ù±‚`a
Ù±‚bc1x'#    - `matplotlib.colors.BoundaryNorm`Ù±‚`a
Ù±‚bc1x/#    - `matplotlib.colorbar.Colorbar.set_label`Ù±‚`a
`dNoneö