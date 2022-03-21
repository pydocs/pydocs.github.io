�����������bsdx�"""
==============================
Filling the area between lines
==============================

This example shows how to use `~.axes.Axes.fill_between` to color the area
between two lines.
"""���`a
���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���`a
���bc1xO###############################################################################���`a
���bc1a#���`a
���bc1m# Basic usage���`a
���bc1m# -----------���`a
���bc1xF# The parameters *y1* and *y2* can be scalars, indicating a horizontal���`a
���bc1xL# boundary at the given y-values. If only *y1* is given, *y2* defaults to 0.���`a
���`a
���`ax���`a ���aoa=���`a ���`bnp���aoa.���`farange���`a(���bmfc0.0���`a,���`a ���bmia2���`a,���`a ���bmfd0.01���`a)���`a
���`by1���`a ���aoa=���`a ���`bnp���aoa.���`csin���`a(���bmia2���`a ���aoa*���`a ���`bnp���aoa.���`bpi���`a ���aoa*���`a ���`ax���`a)���`a
���`by2���`a ���aoa=���`a ���bmfc0.8���`a ���aoa*���`a ���`bnp���aoa.���`csin���`a(���bmia4���`a ���aoa*���`a ���`bnp���aoa.���`bpi���`a ���aoa*���`a ���`ax���`a)���`a
���`a
���`cfig���`a,���`a ���`a(���`cax1���`a,���`a ���`cax2���`a,���`a ���`cax3���`a)���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���bmia3���`a,���`a ���bmia1���`a,���`a ���`fsharex���aoa=���bkcdTrue���`a,���`a ���`gfigsize���aoa=���`a(���bmia6���`a,���`a ���bmia6���`a)���`a)���`a
���`a
���`cax1���aoa.���`lfill_between���`a(���`ax���`a,���`a ���`by1���`a)���`a
���`cax1���aoa.���`iset_title���`a(���bs1a'���bs1ufill between y1 and 0���bs1a'���`a)���`a
���`a
���`cax2���aoa.���`lfill_between���`a(���`ax���`a,���`a ���`by1���`a,���`a ���bmia1���`a)���`a
���`cax2���aoa.���`iset_title���`a(���bs1a'���bs1ufill between y1 and 1���bs1a'���`a)���`a
���`a
���`cax3���aoa.���`lfill_between���`a(���`ax���`a,���`a ���`by1���`a,���`a ���`by2���`a)���`a
���`cax3���aoa.���`iset_title���`a(���bs1a'���bs1vfill between y1 and y2���bs1a'���`a)���`a
���`cax3���aoa.���`jset_xlabel���`a(���bs1a'���bs1ax���bs1a'���`a)���`a
���`cfig���aoa.���`ltight_layout���`a(���`a)���`a
���`a
���bc1xO###############################################################################���`a
���bc1a#���`a
���bc1x# Example: Confidence bands���`a
���bc1x# -------------------------���`a
���bc1xJ# A common application for `~.axes.Axes.fill_between` is the indication of���`a
���bc1s# confidence bands.���`a
���bc1a#���`a
���bc1xK# `~.axes.Axes.fill_between` uses the colors of the color cycle as the fill���`a
���bc1xD# color. These may be a bit strong when applied to fill areas. It is���`a
���bc1xI# therefore often a good practice to lighten the color by making the area���`a
���bc1x!# semi-transparent using *alpha*.���`a
���`a
���bc1x%# sphinx_gallery_thumbnail_number = 2���`a
���`a
���`aN���`a ���aoa=���`a ���bmib21���`a
���`ax���`a ���aoa=���`a ���`bnp���aoa.���`hlinspace���`a(���bmia0���`a,���`a ���bmib10���`a,���`a ���bmib11���`a)���`a
���`ay���`a ���aoa=���`a ���`a[���bmfc3.9���`a,���`a ���bmfc4.4���`a,���`a ���bmfd10.8���`a,���`a ���bmfd10.3���`a,���`a ���bmfd11.2���`a,���`a ���bmfd13.1���`a,���`a ���bmfd14.1���`a,���`b  ���bmfc9.9���`a,���`a ���bmfd13.9���`a,���`a ���bmfd15.1���`a,���`a ���bmfd12.5���`a]���`a
���`a
���bc1x># fit a linear curve an estimate its y-values and their error.���`a
���`aa���`a,���`a ���`ab���`a ���aoa=���`a ���`bnp���aoa.���`gpolyfit���`a(���`ax���`a,���`a ���`ay���`a,���`a ���`cdeg���aoa=���bmia1���`a)���`a
���`ey_est���`a ���aoa=���`a ���`aa���`a ���aoa*���`a ���`ax���`a ���aoa+���`a ���`ab���`a
���`ey_err���`a ���aoa=���`a ���`ax���aoa.���`cstd���`a(���`a)���`a ���aoa*���`a ���`bnp���aoa.���`dsqrt���`a(���bmia1���aoa/���bnbclen���`a(���`ax���`a)���`a ���aoa+���`a
���`x                          ���`a(���`ax���`a ���aoa-���`a ���`ax���aoa.���`dmean���`a(���`a)���`a)���aoa*���aoa*���bmia2���`a ���aoa/���`a ���`bnp���aoa.���`csum���`a(���`a(���`ax���`a ���aoa-���`a ���`ax���aoa.���`dmean���`a(���`a)���`a)���aoa*���aoa*���bmia2���`a)���`a)���`a
���`a
���`cfig���`a,���`a ���`bax���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`a)���`a
���`bax���aoa.���`dplot���`a(���`ax���`a,���`a ���`ey_est���`a,���`a ���bs1a'���bs1a-���bs1a'���`a)���`a
���`bax���aoa.���`lfill_between���`a(���`ax���`a,���`a ���`ey_est���`a ���aoa-���`a ���`ey_err���`a,���`a ���`ey_est���`a ���aoa+���`a ���`ey_err���`a,���`a ���`ealpha���aoa=���bmfc0.2���`a)���`a
���`bax���aoa.���`dplot���`a(���`ax���`a,���`a ���`ay���`a,���`a ���bs1a'���bs1ao���bs1a'���`a,���`a ���`ecolor���aoa=���bs1a'���bs1itab:brown���bs1a'���`a)���`a
���`a
���bc1xO###############################################################################���`a
���bc1a#���`a
���bc1x(# Selectively filling horizontal regions���`a
���bc1x(# --------------------------------------���`a
���bc1xN# The parameter *where* allows to specify the x-ranges to fill. It's a boolean���`a
���bc1x"# array with the same size as *x*.���`a
���bc1a#���`a
���bc1xJ# Only x-ranges of contiguous *True* sequences are filled. As a result the���`a
���bc1xK# range between neighboring *True* and *False* values is never filled. This���`a
���bc1xN# often undesired when the data points should represent a contiguous quantity.���`a
���bc1xD# It is therefore recommended to set ``interpolate=True`` unless the���`a
���bc1xN# x-distance of the data points is fine enough so that the above effect is not���`a
���bc1xK# noticeable. Interpolation approximates the actual x position at which the���`a
���bc1xD# *where* condition will change and extends the filling up to there.���`a
���`a
���`ax���`a ���aoa=���`a ���`bnp���aoa.���`earray���`a(���`a[���bmia0���`a,���`a ���bmia1���`a,���`a ���bmia2���`a,���`a ���bmia3���`a]���`a)���`a
���`by1���`a ���aoa=���`a ���`bnp���aoa.���`earray���`a(���`a[���bmfc0.8���`a,���`a ���bmfc0.8���`a,���`a ���bmfc0.2���`a,���`a ���bmfc0.2���`a]���`a)���`a
���`by2���`a ���aoa=���`a ���`bnp���aoa.���`earray���`a(���`a[���bmia0���`a,���`a ���bmia0���`a,���`a ���bmia1���`a,���`a ���bmia1���`a]���`a)���`a
���`a
���`cfig���`a,���`a ���`a(���`cax1���`a,���`a ���`cax2���`a)���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���bmia2���`a,���`a ���bmia1���`a,���`a ���`fsharex���aoa=���bkcdTrue���`a)���`a
���`a
���`cax1���aoa.���`iset_title���`a(���bs1a'���bs1sinterpolation=False���bs1a'���`a)���`a
���`cax1���aoa.���`dplot���`a(���`ax���`a,���`a ���`by1���`a,���`a ���bs1a'���bs1co--���bs1a'���`a)���`a
���`cax1���aoa.���`dplot���`a(���`ax���`a,���`a ���`by2���`a,���`a ���bs1a'���bs1co--���bs1a'���`a)���`a
���`cax1���aoa.���`lfill_between���`a(���`ax���`a,���`a ���`by1���`a,���`a ���`by2���`a,���`a ���`ewhere���aoa=���`a(���`by1���`a ���aoa>���`a ���`by2���`a)���`a,���`a ���`ecolor���aoa=���bs1a'���bs1bC0���bs1a'���`a,���`a ���`ealpha���aoa=���bmfc0.3���`a)���`a
���`cax1���aoa.���`lfill_between���`a(���`ax���`a,���`a ���`by1���`a,���`a ���`by2���`a,���`a ���`ewhere���aoa=���`a(���`by1���`a ���aoa<���`a ���`by2���`a)���`a,���`a ���`ecolor���aoa=���bs1a'���bs1bC1���bs1a'���`a,���`a ���`ealpha���aoa=���bmfc0.3���`a)���`a
���`a
���`cax2���aoa.���`iset_title���`a(���bs1a'���bs1rinterpolation=True���bs1a'���`a)���`a
���`cax2���aoa.���`dplot���`a(���`ax���`a,���`a ���`by1���`a,���`a ���bs1a'���bs1co--���bs1a'���`a)���`a
���`cax2���aoa.���`dplot���`a(���`ax���`a,���`a ���`by2���`a,���`a ���bs1a'���bs1co--���bs1a'���`a)���`a
���`cax2���aoa.���`lfill_between���`a(���`ax���`a,���`a ���`by1���`a,���`a ���`by2���`a,���`a ���`ewhere���aoa=���`a(���`by1���`a ���aoa>���`a ���`by2���`a)���`a,���`a ���`ecolor���aoa=���bs1a'���bs1bC0���bs1a'���`a,���`a ���`ealpha���aoa=���bmfc0.3���`a,���`a
���`q                 ���`kinterpolate���aoa=���bkcdTrue���`a)���`a
���`cax2���aoa.���`lfill_between���`a(���`ax���`a,���`a ���`by1���`a,���`a ���`by2���`a,���`a ���`ewhere���aoa=���`a(���`by1���`a ���aoa<���aoa=���`a ���`by2���`a)���`a,���`a ���`ecolor���aoa=���bs1a'���bs1bC1���bs1a'���`a,���`a ���`ealpha���aoa=���bmfc0.3���`a,���`a
���`q                 ���`kinterpolate���aoa=���bkcdTrue���`a)���`a
���`cfig���aoa.���`ltight_layout���`a(���`a)���`a
���`a
���bc1xO###############################################################################���`a
���bc1a#���`a
���bc1k# .. note::���`a
���bc1a#���`a
���bc1xM#    Similar gaps will occur if *y1* or *y2* are masked arrays. Since missing���`a
���bc1xM#    values cannot be approximated, *interpolate* has no effect in this case.���`a
���bc1xJ#    The gaps around masked values can only be reduced by adding more data���`a
���bc1x'#    points close to the masked values.���`a
���`a
���bc1xO###############################################################################���`a
���bc1a#���`a
���bc1x># Selectively marking horizontal regions across the whole Axes���`a
���bc1x># ------------------------------------------------------------���`a
���bc1xN# The same selection mechanism can be applied to fill the full vertical height���`a
���bc1xE# of the axes. To be independent of y-limits, we add a transform that���`a
���bc1xF# interprets the x-values in data coorindates and the y-values in axes���`a
���bc1n# coordinates.���`a
���bc1a#���`a
���bc1xI# The following example marks the regions in which the y-data are above a���`a
���bc1r# given threshold.���`a
���`a
���`cfig���`a,���`a ���`bax���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`a)���`a
���`ax���`a ���aoa=���`a ���`bnp���aoa.���`farange���`a(���bmia0���`a,���`a ���bmia4���`a ���aoa*���`a ���`bnp���aoa.���`bpi���`a,���`a ���bmfd0.01���`a)���`a
���`ay���`a ���aoa=���`a ���`bnp���aoa.���`csin���`a(���`ax���`a)���`a
���`bax���aoa.���`dplot���`a(���`ax���`a,���`a ���`ay���`a,���`a ���`ecolor���aoa=���bs1a'���bs1eblack���bs1a'���`a)���`a
���`a
���`ithreshold���`a ���aoa=���`a ���bmfd0.75���`a
���`bax���aoa.���`gaxhline���`a(���`ithreshold���`a,���`a ���`ecolor���aoa=���bs1a'���bs1egreen���bs1a'���`a,���`a ���`blw���aoa=���bmia2���`a,���`a ���`ealpha���aoa=���bmfc0.7���`a)���`a
���`bax���aoa.���`lfill_between���`a(���`ax���`a,���`a ���bmia0���`a,���`a ���bmia1���`a,���`a ���`ewhere���aoa=���`ay���`a ���aoa>���`a ���`ithreshold���`a,���`a
���`p                ���`ecolor���aoa=���bs1a'���bs1egreen���bs1a'���`a,���`a ���`ealpha���aoa=���bmfc0.5���`a,���`a ���`itransform���aoa=���`bax���aoa.���`sget_xaxis_transform���`a(���`a)���`a)���`a
���`a
���bc1xM#############################################################################���`a
���bc1a#���`a
���bc1x# .. admonition:: References���`a
���bc1a#���`a
���bc1xN#    The use of the following functions, methods, classes and modules is shown���`a
���bc1u#    in this example:���`a
���bc1a#���`a
���bc1xM#    - `matplotlib.axes.Axes.fill_between` / `matplotlib.pyplot.fill_between`���`a
���bc1x1#    - `matplotlib.axes.Axes.get_xaxis_transform`���`a
`dNone�