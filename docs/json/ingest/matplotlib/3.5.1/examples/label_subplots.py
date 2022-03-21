�����������bsdy�"""
==================
Labelling subplots
==================

Labelling subplots is relatively straightforward, and varies,
so Matplotlib does not have a general method for doing this.

Simplest is putting the label inside the axes.  Note, here
we use `.pyplot.subplot_mosaic`, and use the subplot labels
as keys for the subplots, which is a nice convenience.  However,
the same method works with `.pyplot.subplots` or keys that are
different than what you want to label the subplot with.
"""���`a
���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnjtransforms���`a ���akbas���`a ���bnnkmtransforms���`a
���`a
���`cfig���`a,���`a ���`caxs���`a ���aoa=���`a ���`cplt���aoa.���`nsubplot_mosaic���`a(���`a[���`a[���bs1a'���bs1ba)���bs1a'���`a,���`a ���bs1a'���bs1bc)���bs1a'���`a]���`a,���`a ���`a[���bs1a'���bs1bb)���bs1a'���`a,���`a ���bs1a'���bs1bc)���bs1a'���`a]���`a,���`a ���`a[���bs1a'���bs1bd)���bs1a'���`a,���`a ���bs1a'���bs1bd)���bs1a'���`a]���`a]���`a,���`a
���`x                              ���`rconstrained_layout���aoa=���bkcdTrue���`a)���`a
���`a
���akcfor���`a ���`elabel���`a,���`a ���`bax���`a ���bowbin���`a ���`caxs���aoa.���`eitems���`a(���`a)���`a:���`a
���`d    ���bc1x&# label physical distance in and down:���`a
���`d    ���`etrans���`a ���aoa=���`a ���`kmtransforms���aoa.���`qScaledTranslation���`a(���bmib10���aoa/���bmib72���`a,���`a ���aoa-���bmia5���aoa/���bmib72���`a,���`a ���`cfig���aoa.���`odpi_scale_trans���`a)���`a
���`d    ���`bax���aoa.���`dtext���`a(���bmfc0.0���`a,���`a ���bmfc1.0���`a,���`a ���`elabel���`a,���`a ���`itransform���aoa=���`bax���aoa.���`itransAxes���`a ���aoa+���`a ���`etrans���`a,���`a
���`l            ���`hfontsize���aoa=���bs1a'���bs1fmedium���bs1a'���`a,���`a ���`qverticalalignment���aoa=���bs1a'���bs1ctop���bs1a'���`a,���`a ���`jfontfamily���aoa=���bs1a'���bs1eserif���bs1a'���`a,���`a
���`l            ���`dbbox���aoa=���bnbddict���`a(���`ifacecolor���aoa=���bs1a'���bs1c0.7���bs1a'���`a,���`a ���`iedgecolor���aoa=���bs1a'���bs1dnone���bs1a'���`a,���`a ���`cpad���aoa=���bmfc3.0���`a)���`a)���`a
���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
���`a
���bc1xN##############################################################################���`a
���bc1x># We may prefer the labels outside the axes, but still aligned���`a
���bc1xG# with each other, in which case we use a slightly different transform:���`a
���`a
���`cfig���`a,���`a ���`caxs���`a ���aoa=���`a ���`cplt���aoa.���`nsubplot_mosaic���`a(���`a[���`a[���bs1a'���bs1ba)���bs1a'���`a,���`a ���bs1a'���bs1bc)���bs1a'���`a]���`a,���`a ���`a[���bs1a'���bs1bb)���bs1a'���`a,���`a ���bs1a'���bs1bc)���bs1a'���`a]���`a,���`a ���`a[���bs1a'���bs1bd)���bs1a'���`a,���`a ���bs1a'���bs1bd)���bs1a'���`a]���`a]���`a,���`a
���`x                              ���`rconstrained_layout���aoa=���bkcdTrue���`a)���`a
���`a
���akcfor���`a ���`elabel���`a,���`a ���`bax���`a ���bowbin���`a ���`caxs���aoa.���`eitems���`a(���`a)���`a:���`a
���`d    ���bc1x-# label physical distance to the left and up:���`a
���`d    ���`etrans���`a ���aoa=���`a ���`kmtransforms���aoa.���`qScaledTranslation���`a(���aoa-���bmib20���aoa/���bmib72���`a,���`a ���bmia7���aoa/���bmib72���`a,���`a ���`cfig���aoa.���`odpi_scale_trans���`a)���`a
���`d    ���`bax���aoa.���`dtext���`a(���bmfc0.0���`a,���`a ���bmfc1.0���`a,���`a ���`elabel���`a,���`a ���`itransform���aoa=���`bax���aoa.���`itransAxes���`a ���aoa+���`a ���`etrans���`a,���`a
���`l            ���`hfontsize���aoa=���bs1a'���bs1fmedium���bs1a'���`a,���`a ���`bva���aoa=���bs1a'���bs1fbottom���bs1a'���`a,���`a ���`jfontfamily���aoa=���bs1a'���bs1eserif���bs1a'���`a)���`a
���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
���`a
���bc1xN##############################################################################���`a
���bc1xJ# If we want it aligned with the title, either incorporate in the title or���`a
���bc1x!# use the *loc* keyword argument:���`a
���`a
���`cfig���`a,���`a ���`caxs���`a ���aoa=���`a ���`cplt���aoa.���`nsubplot_mosaic���`a(���`a[���`a[���bs1a'���bs1ba)���bs1a'���`a,���`a ���bs1a'���bs1bc)���bs1a'���`a]���`a,���`a ���`a[���bs1a'���bs1bb)���bs1a'���`a,���`a ���bs1a'���bs1bc)���bs1a'���`a]���`a,���`a ���`a[���bs1a'���bs1bd)���bs1a'���`a,���`a ���bs1a'���bs1bd)���bs1a'���`a]���`a]���`a,���`a
���`x                              ���`rconstrained_layout���aoa=���bkcdTrue���`a)���`a
���`a
���akcfor���`a ���`elabel���`a,���`a ���`bax���`a ���bowbin���`a ���`caxs���aoa.���`eitems���`a(���`a)���`a:���`a
���`d    ���`bax���aoa.���`iset_title���`a(���bs1a'���bs1lNormal Title���bs1a'���`a,���`a ���`ifontstyle���aoa=���bs1a'���bs1fitalic���bs1a'���`a)���`a
���`d    ���`bax���aoa.���`iset_title���`a(���`elabel���`a,���`a ���`jfontfamily���aoa=���bs1a'���bs1eserif���bs1a'���`a,���`a ���`cloc���aoa=���bs1a'���bs1dleft���bs1a'���`a,���`a ���`hfontsize���aoa=���bs1a'���bs1fmedium���bs1a'���`a)���`a
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
���bc1x2#    - `matplotlib.figure.Figure.subplot_mosaic` /���`a
���bc1x)#      `matplotlib.pyplot.subplot_mosaic`���`a
���bc1x'#    - `matplotlib.axes.Axes.set_title`���`a
���bc1x"#    - `matplotlib.axes.Axes.text`���`a
���bc1x0#    - `matplotlib.transforms.ScaledTranslation`���`a
`dNone�