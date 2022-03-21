Ù¯‚Ù´ƒ™şÙ±‚bsdy®"""
=================================
Rasterization for vector graphics
=================================

Rasterization converts vector graphics into a raster image (pixels). It can
speed up rendering and produce smaller files for large data sets, but comes
at the cost of a fixed resolution.

Whether rasterization should be used can be specified per artist.  This can be
useful to reduce the file size of large artists, while maintaining the
advantages of vector graphics for other artists such as the axes
and text.  For instance a complicated `~.Axes.pcolormesh` or
`~.Axes.contourf` can be made significantly simpler by rasterizing.
Setting rasterization only affects vector backends such as PDF, SVG, or PS.

Rasterization is disabled by default. There are two ways to enable it, which
can also be combined:

- Set `~.Artist.set_rasterized` on individual artists, or use the keyword
  argument *rasterized* when creating the artist.
- Set `.Axes.set_rasterization_zorder` to rasterize all artists with a zorder
  less than the given value.

The storage size and the resolution of the rasterized artist is determined by
its physical size and the value of the ``dpi`` parameter passed to
`~.Figure.savefig`.

.. note::

    The image of this example shown in the HTML documentation is not a vector
    graphic. Therefore, it cannot illustrate the rasterization effect. Please
    run this example locally and check the generated graphics files.

"""Ù±‚`a
Ù±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„enumpyÙ „enumpyf1.22.3fmoduleenumpyfmoduleõÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnnbnpÙ±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnnfpyplotÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnncpltÙ±‚`a
Ù±‚`a
Ù±‚`adÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`farangeÙ±‚`a(Ù±‚bmic100Ù±‚`a)Ù±‚aoa.Ù±‚`greshapeÙ±‚`a(Ù±‚bmib10Ù±‚`a,Ù±‚`a Ù±‚bmib10Ù±‚`a)Ù±‚`b  Ù±‚bc1x# the values to be color-mappedÙ±‚`a
Ù±‚`axÙ±‚`a,Ù±‚`a Ù±‚`ayÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`hmeshgridÙ±‚`a(Ù±‚`bnpÙ±‚aoa.Ù±‚`farangeÙ±‚`a(Ù±‚bmib11Ù±‚`a)Ù±‚`a,Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`farangeÙ±‚`a(Ù±‚bmib11Ù±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`ethetaÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bmfd0.25Ù±‚aoa*Ù±‚`bnpÙ±‚aoa.Ù±‚`bpiÙ±‚`a
Ù±‚`bxxÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`axÙ±‚aoa*Ù±‚`bnpÙ±‚aoa.Ù±‚`ccosÙ±‚`a(Ù±‚`ethetaÙ±‚`a)Ù±‚`a Ù±‚aoa-Ù±‚`a Ù±‚`ayÙ±‚aoa*Ù±‚`bnpÙ±‚aoa.Ù±‚`csinÙ±‚`a(Ù±‚`ethetaÙ±‚`a)Ù±‚`b  Ù±‚bc1t# rotate x by -thetaÙ±‚`a
Ù±‚`byyÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`axÙ±‚aoa*Ù±‚`bnpÙ±‚aoa.Ù±‚`csinÙ±‚`a(Ù±‚`ethetaÙ±‚`a)Ù±‚`a Ù±‚aoa+Ù±‚`a Ù±‚`ayÙ±‚aoa*Ù±‚`bnpÙ±‚aoa.Ù±‚`ccosÙ±‚`a(Ù±‚`ethetaÙ±‚`a)Ù±‚`b  Ù±‚bc1t# rotate y by -thetaÙ±‚`a
Ù±‚`a
Ù±‚`cfigÙ±‚`a,Ù±‚`a Ù±‚`a(Ù±‚`a(Ù±‚`cax1Ù±‚`a,Ù±‚`a Ù±‚`cax2Ù±‚`a)Ù±‚`a,Ù±‚`a Ù±‚`a(Ù±‚`cax3Ù±‚`a,Ù±‚`a Ù±‚`cax4Ù±‚`a)Ù±‚`a)Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cpltÙ±‚aoa.Ù±‚`hsubplotsÙ±‚`a(Ù±‚bmia2Ù±‚`a,Ù±‚`a Ù±‚bmia2Ù±‚`a,Ù±‚`a Ù±‚`rconstrained_layoutÙ±‚aoa=Ù±‚bkcdTrueÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚bc1x"# pcolormesh without rasterizationÙ±‚`a
Ù±‚`cax1Ù±‚aoa.Ù±‚`jset_aspectÙ±‚`a(Ù±‚bmia1Ù±‚`a)Ù±‚`a
Ù±‚`cax1Ù±‚aoa.Ù±‚`jpcolormeshÙ±‚`a(Ù±‚`bxxÙ±‚`a,Ù±‚`a Ù±‚`byyÙ±‚`a,Ù±‚`a Ù±‚`adÙ±‚`a)Ù±‚`a
Ù±‚`cax1Ù±‚aoa.Ù±‚`iset_titleÙ±‚`a(Ù±‚bs2a"Ù±‚bs2pNo RasterizationÙ±‚bs2a"Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚bc1x<# pcolormesh with rasterization; enabled by keyword argumentÙ±‚`a
Ù±‚`cax2Ù±‚aoa.Ù±‚`jset_aspectÙ±‚`a(Ù±‚bmia1Ù±‚`a)Ù±‚`a
Ù±‚`cax2Ù±‚aoa.Ù±‚`iset_titleÙ±‚`a(Ù±‚bs2a"Ù±‚bs2mRasterizationÙ±‚bs2a"Ù±‚`a)Ù±‚`a
Ù±‚`amÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cax2Ù±‚aoa.Ù±‚`jpcolormeshÙ±‚`a(Ù±‚`bxxÙ±‚`a,Ù±‚`a Ù±‚`byyÙ±‚`a,Ù±‚`a Ù±‚`adÙ±‚`a,Ù±‚`a Ù±‚`jrasterizedÙ±‚aoa=Ù±‚bkcdTrueÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚bc1x8# pcolormesh with an overlaid text without rasterizationÙ±‚`a
Ù±‚`cax3Ù±‚aoa.Ù±‚`jset_aspectÙ±‚`a(Ù±‚bmia1Ù±‚`a)Ù±‚`a
Ù±‚`cax3Ù±‚aoa.Ù±‚`jpcolormeshÙ±‚`a(Ù±‚`bxxÙ±‚`a,Ù±‚`a Ù±‚`byyÙ±‚`a,Ù±‚`a Ù±‚`adÙ±‚`a)Ù±‚`a
Ù±‚`cax3Ù±‚aoa.Ù±‚`dtextÙ±‚`a(Ù±‚bmfc0.5Ù±‚`a,Ù±‚`a Ù±‚bmfc0.5Ù±‚`a,Ù±‚`a Ù±‚bs2a"Ù±‚bs2dTextÙ±‚bs2a"Ù±‚`a,Ù±‚`a Ù±‚`ealphaÙ±‚aoa=Ù±‚bmfc0.2Ù±‚`a,Ù±‚`a
Ù±‚`i         Ù±‚`bvaÙ±‚aoa=Ù±‚bs2a"Ù±‚bs2fcenterÙ±‚bs2a"Ù±‚`a,Ù±‚`a Ù±‚`bhaÙ±‚aoa=Ù±‚bs2a"Ù±‚bs2fcenterÙ±‚bs2a"Ù±‚`a,Ù±‚`a Ù±‚`dsizeÙ±‚aoa=Ù±‚bmib50Ù±‚`a,Ù±‚`a Ù±‚`itransformÙ±‚aoa=Ù±‚`cax3Ù±‚aoa.Ù±‚`itransAxesÙ±‚`a)Ù±‚`a
Ù±‚`cax3Ù±‚aoa.Ù±‚`iset_titleÙ±‚`a(Ù±‚bs2a"Ù±‚bs2pNo RasterizationÙ±‚bs2a"Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚bc1xL# pcolormesh with an overlaid text without rasterization; enabled by zorder.Ù±‚`a
Ù±‚bc1xN# Setting the rasterization zorder threshold to 0 and a negative zorder on theÙ±‚`a
Ù±‚bc1xN# pcolormesh rasterizes it. All artists have a non-negative zorder by default,Ù±‚`a
Ù±‚bc1x0# so they (e.g. the text here) are not affected.Ù±‚`a
Ù±‚`cax4Ù±‚aoa.Ù±‚`jset_aspectÙ±‚`a(Ù±‚bmia1Ù±‚`a)Ù±‚`a
Ù±‚`amÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cax4Ù±‚aoa.Ù±‚`jpcolormeshÙ±‚`a(Ù±‚`bxxÙ±‚`a,Ù±‚`a Ù±‚`byyÙ±‚`a,Ù±‚`a Ù±‚`adÙ±‚`a,Ù±‚`a Ù±‚`fzorderÙ±‚aoa=Ù±‚aoa-Ù±‚bmib10Ù±‚`a)Ù±‚`a
Ù±‚`cax4Ù±‚aoa.Ù±‚`dtextÙ±‚`a(Ù±‚bmfc0.5Ù±‚`a,Ù±‚`a Ù±‚bmfc0.5Ù±‚`a,Ù±‚`a Ù±‚bs2a"Ù±‚bs2dTextÙ±‚bs2a"Ù±‚`a,Ù±‚`a Ù±‚`ealphaÙ±‚aoa=Ù±‚bmfc0.2Ù±‚`a,Ù±‚`a
Ù±‚`i         Ù±‚`bvaÙ±‚aoa=Ù±‚bs2a"Ù±‚bs2fcenterÙ±‚bs2a"Ù±‚`a,Ù±‚`a Ù±‚`bhaÙ±‚aoa=Ù±‚bs2a"Ù±‚bs2fcenterÙ±‚bs2a"Ù±‚`a,Ù±‚`a Ù±‚`dsizeÙ±‚aoa=Ù±‚bmib50Ù±‚`a,Ù±‚`a Ù±‚`itransformÙ±‚aoa=Ù±‚`cax4Ù±‚aoa.Ù±‚`itransAxesÙ±‚`a)Ù±‚`a
Ù±‚`cax4Ù±‚aoa.Ù±‚`xset_rasterization_zorderÙ±‚`a(Ù±‚bmia0Ù±‚`a)Ù±‚`a
Ù±‚`cax4Ù±‚aoa.Ù±‚`iset_titleÙ±‚`a(Ù±‚bs2a"Ù±‚bs2uRasterization z$<-10$Ù±‚bs2a"Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚bc1x"# Save files in pdf and eps formatÙ±‚`a
Ù±‚`cpltÙ±‚aoa.Ù±‚`gsavefigÙ±‚`a(Ù±‚bs2a"Ù±‚bs2vtest_rasterization.pdfÙ±‚bs2a"Ù±‚`a,Ù±‚`a Ù±‚`cdpiÙ±‚aoa=Ù±‚bmic150Ù±‚`a)Ù±‚`a
Ù±‚`cpltÙ±‚aoa.Ù±‚`gsavefigÙ±‚`a(Ù±‚bs2a"Ù±‚bs2vtest_rasterization.epsÙ±‚bs2a"Ù±‚`a,Ù±‚`a Ù±‚`cdpiÙ±‚aoa=Ù±‚bmic150Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚akbifÙ±‚`a Ù±‚bowcnotÙ±‚`a Ù±‚`cpltÙ±‚aoa.Ù±‚`hrcParamsÙ±‚`a[Ù±‚bs2a"Ù±‚bs2ktext.usetexÙ±‚bs2a"Ù±‚`a]Ù±‚`a:Ù±‚`a
Ù±‚`d    Ù±‚`cpltÙ±‚aoa.Ù±‚`gsavefigÙ±‚`a(Ù±‚bs2a"Ù±‚bs2vtest_rasterization.svgÙ±‚bs2a"Ù±‚`a,Ù±‚`a Ù±‚`cdpiÙ±‚aoa=Ù±‚bmic150Ù±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚bc1x'# svg backend currently ignores the dpiÙ±‚`a
Ù±‚`a
Ù±‚bc1xM#############################################################################Ù±‚`a
Ù±‚bc1a#Ù±‚`a
Ù±‚bc1x# .. admonition:: ReferencesÙ±‚`a
Ù±‚bc1a#Ù±‚`a
Ù±‚bc1xN#    The use of the following functions, methods, classes and modules is shownÙ±‚`a
Ù±‚bc1u#    in this example:Ù±‚`a
Ù±‚bc1a#Ù±‚`a
Ù±‚bc1x0#    - `matplotlib.artist.Artist.set_rasterized`Ù±‚`a
Ù±‚bc1x6#    - `matplotlib.axes.Axes.set_rasterization_zorder`Ù±‚`a
Ù±‚bc1xI#    - `matplotlib.axes.Axes.pcolormesh` / `matplotlib.pyplot.pcolormesh`Ù±‚`a
`dNoneö