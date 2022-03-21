��������(���bsdx�"""
======
Scales
======

Illustrate the scale transformations applied to axes, e.g. log, symlog, logit.

The last two examples are examples of using the ``'function'`` scale by
supplying forward and inverse functions for the scale transformation.
"""���`a
���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���bkndfrom���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfticker���`a ���bknfimport���`a ���`mNullFormatter���`a,���`a ���`lFixedLocator���`a
���`a
���bc1x)# Fixing random state for reproducibility���`a
���`bnp���aoa.���`frandom���aoa.���`dseed���`a(���bmih19680801���`a)���`a
���`a
���bc1x*# make up some data in the interval ]0, 1[���`a
���`ay���`a ���aoa=���`a ���`bnp���aoa.���`frandom���aoa.���`fnormal���`a(���`cloc���aoa=���bmfc0.5���`a,���`a ���`escale���aoa=���bmfc0.4���`a,���`a ���`dsize���aoa=���bmid1000���`a)���`a
���`ay���`a ���aoa=���`a ���`ay���`a[���`a(���`ay���`a ���aoa>���`a ���bmia0���`a)���`a ���aoa&���`a ���`a(���`ay���`a ���aoa<���`a ���bmia1���`a)���`a]���`a
���`ay���aoa.���`dsort���`a(���`a)���`a
���`ax���`a ���aoa=���`a ���`bnp���aoa.���`farange���`a(���bnbclen���`a(���`ay���`a)���`a)���`a
���`a
���bc1x# plot with various axes scales���`a
���`cfig���`a,���`a ���`caxs���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���bmia3���`a,���`a ���bmia2���`a,���`a ���`gfigsize���aoa=���`a(���bmia6���`a,���`a ���bmia8���`a)���`a,���`a
���`x                        ���`rconstrained_layout���aoa=���bkcdTrue���`a)���`a
���`a
���bc1h# linear���`a
���`bax���`a ���aoa=���`a ���`caxs���`a[���bmia0���`a,���`a ���bmia0���`a]���`a
���`bax���aoa.���`dplot���`a(���`ax���`a,���`a ���`ay���`a)���`a
���`bax���aoa.���`jset_yscale���`a(���bs1a'���bs1flinear���bs1a'���`a)���`a
���`bax���aoa.���`iset_title���`a(���bs1a'���bs1flinear���bs1a'���`a)���`a
���`bax���aoa.���`dgrid���`a(���bkcdTrue���`a)���`a
���`a
���`a
���bc1e# log���`a
���`bax���`a ���aoa=���`a ���`caxs���`a[���bmia0���`a,���`a ���bmia1���`a]���`a
���`bax���aoa.���`dplot���`a(���`ax���`a,���`a ���`ay���`a)���`a
���`bax���aoa.���`jset_yscale���`a(���bs1a'���bs1clog���bs1a'���`a)���`a
���`bax���aoa.���`iset_title���`a(���bs1a'���bs1clog���bs1a'���`a)���`a
���`bax���aoa.���`dgrid���`a(���bkcdTrue���`a)���`a
���`a
���`a
���bc1o# symmetric log���`a
���`bax���`a ���aoa=���`a ���`caxs���`a[���bmia1���`a,���`a ���bmia1���`a]���`a
���`bax���aoa.���`dplot���`a(���`ax���`a,���`a ���`ay���`a ���aoa-���`a ���`ay���aoa.���`dmean���`a(���`a)���`a)���`a
���`bax���aoa.���`jset_yscale���`a(���bs1a'���bs1fsymlog���bs1a'���`a,���`a ���`ilinthresh���aoa=���bmfd0.02���`a)���`a
���`bax���aoa.���`iset_title���`a(���bs1a'���bs1fsymlog���bs1a'���`a)���`a
���`bax���aoa.���`dgrid���`a(���bkcdTrue���`a)���`a
���`a
���bc1g# logit���`a
���`bax���`a ���aoa=���`a ���`caxs���`a[���bmia1���`a,���`a ���bmia0���`a]���`a
���`bax���aoa.���`dplot���`a(���`ax���`a,���`a ���`ay���`a)���`a
���`bax���aoa.���`jset_yscale���`a(���bs1a'���bs1elogit���bs1a'���`a)���`a
���`bax���aoa.���`iset_title���`a(���bs1a'���bs1elogit���bs1a'���`a)���`a
���`bax���aoa.���`dgrid���`a(���bkcdTrue���`a)���`a
���`a
���`a
���bc1s# Function x**(1/2)���`a
���akcdef���`a ���bnfgforward���`a(���`ax���`a)���`a:���`a
���`d    ���akfreturn���`a ���`ax���aoa*���aoa*���`a(���bmia1���aoa/���bmia2���`a)���`a
���`a
���`a
���akcdef���`a ���bnfginverse���`a(���`ax���`a)���`a:���`a
���`d    ���akfreturn���`a ���`ax���aoa*���aoa*���bmia2���`a
���`a
���`a
���`bax���`a ���aoa=���`a ���`caxs���`a[���bmia2���`a,���`a ���bmia0���`a]���`a
���`bax���aoa.���`dplot���`a(���`ax���`a,���`a ���`ay���`a)���`a
���`bax���aoa.���`jset_yscale���`a(���bs1a'���bs1hfunction���bs1a'���`a,���`a ���`ifunctions���aoa=���`a(���`gforward���`a,���`a ���`ginverse���`a)���`a)���`a
���`bax���aoa.���`iset_title���`a(���bs1a'���bs1mfunction: $x^���bs1a{���bs1e1/2}$���bs1a'���`a)���`a
���`bax���aoa.���`dgrid���`a(���bkcdTrue���`a)���`a
���`bax���aoa.���`eyaxis���aoa.���`qset_major_locator���`a(���`lFixedLocator���`a(���`bnp���aoa.���`farange���`a(���bmia0���`a,���`a ���bmia1���`a,���`a ���bmfc0.2���`a)���aoa*���aoa*���bmia2���`a)���`a)���`a
���`bax���aoa.���`eyaxis���aoa.���`qset_major_locator���`a(���`lFixedLocator���`a(���`bnp���aoa.���`farange���`a(���bmia0���`a,���`a ���bmia1���`a,���`a ���bmfc0.2���`a)���`a)���`a)���`a
���`a
���`a
���bc1x# Function Mercator transform���`a
���akcdef���`a ���bnfgforward���`a(���`aa���`a)���`a:���`a
���`d    ���`aa���`a ���aoa=���`a ���`bnp���aoa.���`gdeg2rad���`a(���`aa���`a)���`a
���`d    ���akfreturn���`a ���`bnp���aoa.���`grad2deg���`a(���`bnp���aoa.���`clog���`a(���`bnp���aoa.���`cabs���`a(���`bnp���aoa.���`ctan���`a(���`aa���`a)���`a ���aoa+���`a ���bmfc1.0���`a ���aoa/���`a ���`bnp���aoa.���`ccos���`a(���`aa���`a)���`a)���`a)���`a)���`a
���`a
���`a
���akcdef���`a ���bnfginverse���`a(���`aa���`a)���`a:���`a
���`d    ���`aa���`a ���aoa=���`a ���`bnp���aoa.���`gdeg2rad���`a(���`aa���`a)���`a
���`d    ���akfreturn���`a ���`bnp���aoa.���`grad2deg���`a(���`bnp���aoa.���`farctan���`a(���`bnp���aoa.���`dsinh���`a(���`aa���`a)���`a)���`a)���`a
���`a
���`bax���`a ���aoa=���`a ���`caxs���`a[���bmia2���`a,���`a ���bmia1���`a]���`a
���`a
���`at���`a ���aoa=���`a ���`bnp���aoa.���`farange���`a(���bmia0���`a,���`a ���bmfe170.0���`a,���`a ���bmfc0.1���`a)���`a
���`as���`a ���aoa=���`a ���`at���`a ���aoa/���`a ���bmfb2.���`a
���`a
���`bax���aoa.���`dplot���`a(���`at���`a,���`a ���`as���`a,���`a ���bs1a'���bs1a-���bs1a'���`a,���`a ���`blw���aoa=���bmia2���`a)���`a
���`a
���`bax���aoa.���`jset_yscale���`a(���bs1a'���bs1hfunction���bs1a'���`a,���`a ���`ifunctions���aoa=���`a(���`gforward���`a,���`a ���`ginverse���`a)���`a)���`a
���`bax���aoa.���`iset_title���`a(���bs1a'���bs1rfunction: Mercator���bs1a'���`a)���`a
���`bax���aoa.���`dgrid���`a(���bkcdTrue���`a)���`a
���`bax���aoa.���`hset_xlim���`a(���`a[���bmia0���`a,���`a ���bmic180���`a]���`a)���`a
���`bax���aoa.���`eyaxis���aoa.���`sset_minor_formatter���`a(���`mNullFormatter���`a(���`a)���`a)���`a
���`bax���aoa.���`eyaxis���aoa.���`qset_major_locator���`a(���`lFixedLocator���`a(���`bnp���aoa.���`farange���`a(���bmia0���`a,���`a ���bmib90���`a,���`a ���bmib10���`a)���`a)���`a)���`a
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
���bc1x(#    - `matplotlib.axes.Axes.set_xscale`���`a
���bc1x(#    - `matplotlib.axes.Axes.set_yscale`���`a
���bc1x/#    - `matplotlib.axis.Axis.set_major_locator`���`a
���bc1x%#    - `matplotlib.scale.LinearScale`���`a
���bc1x"#    - `matplotlib.scale.LogScale`���`a
���bc1x-#    - `matplotlib.scale.SymmetricalLogScale`���`a
���bc1x$#    - `matplotlib.scale.LogitScale`���`a
���bc1x##    - `matplotlib.scale.FuncScale`���`a
`dNone�