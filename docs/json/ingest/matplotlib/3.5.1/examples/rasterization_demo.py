������������bsdy�"""
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

"""���`a
���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���`a
���`ad���`a ���aoa=���`a ���`bnp���aoa.���`farange���`a(���bmic100���`a)���aoa.���`greshape���`a(���bmib10���`a,���`a ���bmib10���`a)���`b  ���bc1x# the values to be color-mapped���`a
���`ax���`a,���`a ���`ay���`a ���aoa=���`a ���`bnp���aoa.���`hmeshgrid���`a(���`bnp���aoa.���`farange���`a(���bmib11���`a)���`a,���`a ���`bnp���aoa.���`farange���`a(���bmib11���`a)���`a)���`a
���`a
���`etheta���`a ���aoa=���`a ���bmfd0.25���aoa*���`bnp���aoa.���`bpi���`a
���`bxx���`a ���aoa=���`a ���`ax���aoa*���`bnp���aoa.���`ccos���`a(���`etheta���`a)���`a ���aoa-���`a ���`ay���aoa*���`bnp���aoa.���`csin���`a(���`etheta���`a)���`b  ���bc1t# rotate x by -theta���`a
���`byy���`a ���aoa=���`a ���`ax���aoa*���`bnp���aoa.���`csin���`a(���`etheta���`a)���`a ���aoa+���`a ���`ay���aoa*���`bnp���aoa.���`ccos���`a(���`etheta���`a)���`b  ���bc1t# rotate y by -theta���`a
���`a
���`cfig���`a,���`a ���`a(���`a(���`cax1���`a,���`a ���`cax2���`a)���`a,���`a ���`a(���`cax3���`a,���`a ���`cax4���`a)���`a)���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���bmia2���`a,���`a ���bmia2���`a,���`a ���`rconstrained_layout���aoa=���bkcdTrue���`a)���`a
���`a
���bc1x"# pcolormesh without rasterization���`a
���`cax1���aoa.���`jset_aspect���`a(���bmia1���`a)���`a
���`cax1���aoa.���`jpcolormesh���`a(���`bxx���`a,���`a ���`byy���`a,���`a ���`ad���`a)���`a
���`cax1���aoa.���`iset_title���`a(���bs2a"���bs2pNo Rasterization���bs2a"���`a)���`a
���`a
���bc1x<# pcolormesh with rasterization; enabled by keyword argument���`a
���`cax2���aoa.���`jset_aspect���`a(���bmia1���`a)���`a
���`cax2���aoa.���`iset_title���`a(���bs2a"���bs2mRasterization���bs2a"���`a)���`a
���`am���`a ���aoa=���`a ���`cax2���aoa.���`jpcolormesh���`a(���`bxx���`a,���`a ���`byy���`a,���`a ���`ad���`a,���`a ���`jrasterized���aoa=���bkcdTrue���`a)���`a
���`a
���bc1x8# pcolormesh with an overlaid text without rasterization���`a
���`cax3���aoa.���`jset_aspect���`a(���bmia1���`a)���`a
���`cax3���aoa.���`jpcolormesh���`a(���`bxx���`a,���`a ���`byy���`a,���`a ���`ad���`a)���`a
���`cax3���aoa.���`dtext���`a(���bmfc0.5���`a,���`a ���bmfc0.5���`a,���`a ���bs2a"���bs2dText���bs2a"���`a,���`a ���`ealpha���aoa=���bmfc0.2���`a,���`a
���`i         ���`bva���aoa=���bs2a"���bs2fcenter���bs2a"���`a,���`a ���`bha���aoa=���bs2a"���bs2fcenter���bs2a"���`a,���`a ���`dsize���aoa=���bmib50���`a,���`a ���`itransform���aoa=���`cax3���aoa.���`itransAxes���`a)���`a
���`cax3���aoa.���`iset_title���`a(���bs2a"���bs2pNo Rasterization���bs2a"���`a)���`a
���`a
���bc1xL# pcolormesh with an overlaid text without rasterization; enabled by zorder.���`a
���bc1xN# Setting the rasterization zorder threshold to 0 and a negative zorder on the���`a
���bc1xN# pcolormesh rasterizes it. All artists have a non-negative zorder by default,���`a
���bc1x0# so they (e.g. the text here) are not affected.���`a
���`cax4���aoa.���`jset_aspect���`a(���bmia1���`a)���`a
���`am���`a ���aoa=���`a ���`cax4���aoa.���`jpcolormesh���`a(���`bxx���`a,���`a ���`byy���`a,���`a ���`ad���`a,���`a ���`fzorder���aoa=���aoa-���bmib10���`a)���`a
���`cax4���aoa.���`dtext���`a(���bmfc0.5���`a,���`a ���bmfc0.5���`a,���`a ���bs2a"���bs2dText���bs2a"���`a,���`a ���`ealpha���aoa=���bmfc0.2���`a,���`a
���`i         ���`bva���aoa=���bs2a"���bs2fcenter���bs2a"���`a,���`a ���`bha���aoa=���bs2a"���bs2fcenter���bs2a"���`a,���`a ���`dsize���aoa=���bmib50���`a,���`a ���`itransform���aoa=���`cax4���aoa.���`itransAxes���`a)���`a
���`cax4���aoa.���`xset_rasterization_zorder���`a(���bmia0���`a)���`a
���`cax4���aoa.���`iset_title���`a(���bs2a"���bs2uRasterization z$<-10$���bs2a"���`a)���`a
���`a
���bc1x"# Save files in pdf and eps format���`a
���`cplt���aoa.���`gsavefig���`a(���bs2a"���bs2vtest_rasterization.pdf���bs2a"���`a,���`a ���`cdpi���aoa=���bmic150���`a)���`a
���`cplt���aoa.���`gsavefig���`a(���bs2a"���bs2vtest_rasterization.eps���bs2a"���`a,���`a ���`cdpi���aoa=���bmic150���`a)���`a
���`a
���akbif���`a ���bowcnot���`a ���`cplt���aoa.���`hrcParams���`a[���bs2a"���bs2ktext.usetex���bs2a"���`a]���`a:���`a
���`d    ���`cplt���aoa.���`gsavefig���`a(���bs2a"���bs2vtest_rasterization.svg���bs2a"���`a,���`a ���`cdpi���aoa=���bmic150���`a)���`a
���`d    ���bc1x'# svg backend currently ignores the dpi���`a
���`a
���bc1xM#############################################################################���`a
���bc1a#���`a
���bc1x# .. admonition:: References���`a
���bc1a#���`a
���bc1xN#    The use of the following functions, methods, classes and modules is shown���`a
���bc1u#    in this example:���`a
���bc1a#���`a
���bc1x0#    - `matplotlib.artist.Artist.set_rasterized`���`a
���bc1x6#    - `matplotlib.axes.Axes.set_rasterization_zorder`���`a
���bc1xI#    - `matplotlib.axes.Axes.pcolormesh` / `matplotlib.pyplot.pcolormesh`���`a
`dNone�