�����������bsdy�"""
=========================
Interpolations for imshow
=========================

This example displays the difference between interpolation methods for
`~.axes.Axes.imshow`.

If *interpolation* is None, it defaults to the :rc:`image.interpolation`.
If the interpolation is ``'none'``, then no interpolation is performed for the
Agg, ps and pdf backends. Other backends will default to ``'antialiased'``.

For the Agg, ps and pdf backends, ``interpolation = 'none'`` works well when a
big image is scaled down, while ``interpolation = 'nearest'`` works well when
a small image is scaled up.

See :doc:`/gallery/images_contours_and_fields/image_antialiasing` for a
discussion on the default ``interpolation="antialiased"`` option.
"""���`a
���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���`a
���`gmethods���`a ���aoa=���`a ���`a[���bkcdNone���`a,���`a ���bs1a'���bs1dnone���bs1a'���`a,���`a ���bs1a'���bs1gnearest���bs1a'���`a,���`a ���bs1a'���bs1hbilinear���bs1a'���`a,���`a ���bs1a'���bs1gbicubic���bs1a'���`a,���`a ���bs1a'���bs1hspline16���bs1a'���`a,���`a
���`k           ���bs1a'���bs1hspline36���bs1a'���`a,���`a ���bs1a'���bs1ghanning���bs1a'���`a,���`a ���bs1a'���bs1ghamming���bs1a'���`a,���`a ���bs1a'���bs1ghermite���bs1a'���`a,���`a ���bs1a'���bs1fkaiser���bs1a'���`a,���`a ���bs1a'���bs1gquadric���bs1a'���`a,���`a
���`k           ���bs1a'���bs1fcatrom���bs1a'���`a,���`a ���bs1a'���bs1hgaussian���bs1a'���`a,���`a ���bs1a'���bs1fbessel���bs1a'���`a,���`a ���bs1a'���bs1hmitchell���bs1a'���`a,���`a ���bs1a'���bs1dsinc���bs1a'���`a,���`a ���bs1a'���bs1glanczos���bs1a'���`a]���`a
���`a
���bc1x)# Fixing random state for reproducibility���`a
���`bnp���aoa.���`frandom���aoa.���`dseed���`a(���bmih19680801���`a)���`a
���`a
���`dgrid���`a ���aoa=���`a ���`bnp���aoa.���`frandom���aoa.���`drand���`a(���bmia4���`a,���`a ���bmia4���`a)���`a
���`a
���`cfig���`a,���`a ���`caxs���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`enrows���aoa=���bmia3���`a,���`a ���`encols���aoa=���bmia6���`a,���`a ���`gfigsize���aoa=���`a(���bmia9���`a,���`a ���bmia6���`a)���`a,���`a
���`x                        ���`jsubplot_kw���aoa=���`a{���bs1a'���bs1fxticks���bs1a'���`a:���`a ���`a[���`a]���`a,���`a ���bs1a'���bs1fyticks���bs1a'���`a:���`a ���`a[���`a]���`a}���`a)���`a
���`a
���akcfor���`a ���`bax���`a,���`a ���`minterp_method���`a ���bowbin���`a ���bnbczip���`a(���`caxs���aoa.���`dflat���`a,���`a ���`gmethods���`a)���`a:���`a
���`d    ���`bax���aoa.���`fimshow���`a(���`dgrid���`a,���`a ���`minterpolation���aoa=���`minterp_method���`a,���`a ���`dcmap���aoa=���bs1a'���bs1gviridis���bs1a'���`a)���`a
���`d    ���`bax���aoa.���`iset_title���`a(���bnbcstr���`a(���`minterp_method���`a)���`a)���`a
���`a
���`cplt���aoa.���`ltight_layout���`a(���`a)���`a
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
`dNone�