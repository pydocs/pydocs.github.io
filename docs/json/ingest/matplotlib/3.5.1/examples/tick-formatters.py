������������bsdx�"""
===============
Tick formatters
===============

Tick formatters define how the numeric value associated with a tick on an axis
is formatted as a string.

This example illustrates the usage and effect of the most common formatters.
"""���`a
���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���bkndfrom���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����`a ���bknfimport���`a ���`fticker���`a
���`a
���`a
���akcdef���`a ���bnfesetup���`a(���`bax���`a,���`a ���`etitle���`a)���`a:���`a
���`d    ���bsdx;"""Set up common parameters for the Axes in the example."""���`a
���`d    ���bc1x# only show the bottom spine���`a
���`d    ���`bax���aoa.���`eyaxis���aoa.���`qset_major_locator���`a(���`fticker���aoa.���`kNullLocator���`a(���`a)���`a)���`a
���`d    ���`bax���aoa.���`fspines���aoa.���`eright���aoa.���`iset_color���`a(���bs1a'���bs1dnone���bs1a'���`a)���`a
���`d    ���`bax���aoa.���`fspines���aoa.���`dleft���aoa.���`iset_color���`a(���bs1a'���bs1dnone���bs1a'���`a)���`a
���`d    ���`bax���aoa.���`fspines���aoa.���`ctop���aoa.���`iset_color���`a(���bs1a'���bs1dnone���bs1a'���`a)���`a
���`a
���`d    ���bc1w# define tick positions���`a
���`d    ���`bax���aoa.���`exaxis���aoa.���`qset_major_locator���`a(���`fticker���aoa.���`oMultipleLocator���`a(���bmfd1.00���`a)���`a)���`a
���`d    ���`bax���aoa.���`exaxis���aoa.���`qset_minor_locator���`a(���`fticker���aoa.���`oMultipleLocator���`a(���bmfd0.25���`a)���`a)���`a
���`a
���`d    ���`bax���aoa.���`exaxis���aoa.���`rset_ticks_position���`a(���bs1a'���bs1fbottom���bs1a'���`a)���`a
���`d    ���`bax���aoa.���`ktick_params���`a(���`ewhich���aoa=���bs1a'���bs1emajor���bs1a'���`a,���`a ���`ewidth���aoa=���bmfd1.00���`a,���`a ���`flength���aoa=���bmia5���`a)���`a
���`d    ���`bax���aoa.���`ktick_params���`a(���`ewhich���aoa=���bs1a'���bs1eminor���bs1a'���`a,���`a ���`ewidth���aoa=���bmfd0.75���`a,���`a ���`flength���aoa=���bmfc2.5���`a,���`a ���`ilabelsize���aoa=���bmib10���`a)���`a
���`d    ���`bax���aoa.���`hset_xlim���`a(���bmia0���`a,���`a ���bmia5���`a)���`a
���`d    ���`bax���aoa.���`hset_ylim���`a(���bmia0���`a,���`a ���bmia1���`a)���`a
���`d    ���`bax���aoa.���`dtext���`a(���bmfc0.0���`a,���`a ���bmfc0.2���`a,���`a ���`etitle���`a,���`a ���`itransform���aoa=���`bax���aoa.���`itransAxes���`a,���`a
���`l            ���`hfontsize���aoa=���bmib14���`a,���`a ���`hfontname���aoa=���bs1a'���bs1iMonospace���bs1a'���`a,���`a ���`ecolor���aoa=���bs1a'���bs1htab:blue���bs1a'���`a)���`a
���`a
���`a
���bc1xM#############################################################################���`a
���bc1xL# Tick formatters can be set in one of two ways, either by passing a ``str``���`a
���bc1xN# or function to `~.Axis.set_major_formatter` or `~.Axis.set_minor_formatter`,���`a
���bc1xO# or by creating an instance of one of the various `~.ticker.Formatter` classes���`a
���bc1x7# and providing that to `~.Axis.set_major_formatter` or���`a
���bc1x# `~.Axis.set_minor_formatter`.���`a
���bc1a#���`a
���bc1x=# The first two examples directly pass a ``str`` or function.���`a
���`a
���`dfig0���`a,���`a ���`daxs0���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���bmia2���`a,���`a ���bmia1���`a,���`a ���`gfigsize���aoa=���`a(���bmia8���`a,���`a ���bmia2���`a)���`a)���`a
���`dfig0���aoa.���`hsuptitle���`a(���bs1a'���bs1qSimple Formatting���bs1a'���`a)���`a
���`a
���bc1xK# A ``str``, using format string function syntax, can be used directly as a���`a
���bc1xN# formatter.  The variable ``x`` is the tick value and the variable ``pos`` is���`a
���bc1xB# tick position.  This creates a StrMethodFormatter automatically.���`a
���`esetup���`a(���`daxs0���`a[���bmia0���`a]���`a,���`a ���`etitle���aoa=���bs2a"���bs2a'���bsic{x}���bs2c km���bs2a'���bs2a"���`a)���`a
���`daxs0���`a[���bmia0���`a]���aoa.���`exaxis���aoa.���`sset_major_formatter���`a(���bs1a'���bsic{x}���bs1c km���bs1a'���`a)���`a
���`a
���bc1xM# A function can also be used directly as a formatter. The function must take���`a
���bc1xL# two arguments: ``x`` for the tick value and ``pos`` for the tick position,���`a
���bc1xH# and must return a ``str``. This creates a FuncFormatter automatically.���`a
���`esetup���`a(���`daxs0���`a[���bmia1���`a]���`a,���`a ���`etitle���aoa=���bs2a"���bs2wlambda x, pos: str(x-5)���bs2a"���`a)���`a
���`daxs0���`a[���bmia1���`a]���aoa.���`exaxis���aoa.���`sset_major_formatter���`a(���akflambda���`a ���`ax���`a,���`a ���`cpos���`a:���`a ���bnbcstr���`a(���`ax���aoa-���bmia5���`a)���`a)���`a
���`a
���`dfig0���aoa.���`ltight_layout���`a(���`a)���`a
���`a
���`a
���bc1xM#############################################################################���`a
���bc1x2# The remaining examples use `.Formatter` objects.���`a
���`a
���`dfig1���`a,���`a ���`daxs1���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���bmia7���`a,���`a ���bmia1���`a,���`a ���`gfigsize���aoa=���`a(���bmia8���`a,���`a ���bmia6���`a)���`a)���`a
���`dfig1���aoa.���`hsuptitle���`a(���bs1a'���bs1xFormatter Object Formatting���bs1a'���`a)���`a
���`a
���bc1p# Null formatter���`a
���`esetup���`a(���`daxs1���`a[���bmia0���`a]���`a,���`a ���`etitle���aoa=���bs2a"���bs2oNullFormatter()���bs2a"���`a)���`a
���`daxs1���`a[���bmia0���`a]���aoa.���`exaxis���aoa.���`sset_major_formatter���`a(���`fticker���aoa.���`mNullFormatter���`a(���`a)���`a)���`a
���`a
���bc1u# StrMethod formatter���`a
���`esetup���`a(���`daxs1���`a[���bmia1���`a]���`a,���`a ���`etitle���aoa=���bs2a"���bs2sStrMethodFormatter(���bs2a'���bsig{x:.3f}���bs2a'���bs2a)���bs2a"���`a)���`a
���`daxs1���`a[���bmia1���`a]���aoa.���`exaxis���aoa.���`sset_major_formatter���`a(���`fticker���aoa.���`rStrMethodFormatter���`a(���bs2a"���bsig{x:.3f}���bs2a"���`a)���`a)���`a
���`a
���`a
���bc1x*# FuncFormatter can be used as a decorator���`a
���bndg@ticker���aoa.���`mFuncFormatter���`a
���akcdef���`a ���bnfomajor_formatter���`a(���`ax���`a,���`a ���`cpos���`a)���`a:���`a
���`d    ���akfreturn���`a ���bsaaf���bs1a'���bs1a[���bsia{���`ax���bsia:���bs1c.2f���bsia}���bs1a]���bs1a'���`a
���`a
���`a
���`esetup���`a(���`daxs1���`a[���bmia2���`a]���`a,���`a ���`etitle���aoa=���bs1a'���bs1nFuncFormatter(���bs1a"���bs1a[���bsif{:.2f}���bs1a]���bs1a"���bs1h.format)���bs1a'���`a)���`a
���`daxs1���`a[���bmia2���`a]���aoa.���`exaxis���aoa.���`sset_major_formatter���`a(���`omajor_formatter���`a)���`a
���`a
���bc1q# Fixed formatter���`a
���`esetup���`a(���`daxs1���`a[���bmia3���`a]���`a,���`a ���`etitle���aoa=���bs2a"���bs2pFixedFormatter([���bs2a'���bs2aA���bs2a'���bs2b, ���bs2a'���bs2aB���bs2a'���bs2b, ���bs2a'���bs2aC���bs2a'���bs2g, ...])���bs2a"���`a)���`a
���bc1x@# FixedFormatter should only be used together with FixedLocator.���`a
���bc1x=# Otherwise, one cannot be sure where the labels will end up.���`a
���`ipositions���`a ���aoa=���`a ���`a[���bmia0���`a,���`a ���bmia1���`a,���`a ���bmia2���`a,���`a ���bmia3���`a,���`a ���bmia4���`a,���`a ���bmia5���`a]���`a
���`flabels���`a ���aoa=���`a ���`a[���bs1a'���bs1aA���bs1a'���`a,���`a ���bs1a'���bs1aB���bs1a'���`a,���`a ���bs1a'���bs1aC���bs1a'���`a,���`a ���bs1a'���bs1aD���bs1a'���`a,���`a ���bs1a'���bs1aE���bs1a'���`a,���`a ���bs1a'���bs1aF���bs1a'���`a]���`a
���`daxs1���`a[���bmia3���`a]���aoa.���`exaxis���aoa.���`qset_major_locator���`a(���`fticker���aoa.���`lFixedLocator���`a(���`ipositions���`a)���`a)���`a
���`daxs1���`a[���bmia3���`a]���aoa.���`exaxis���aoa.���`sset_major_formatter���`a(���`fticker���aoa.���`nFixedFormatter���`a(���`flabels���`a)���`a)���`a
���`a
���bc1r# Scalar formatter���`a
���`esetup���`a(���`daxs1���`a[���bmia4���`a]���`a,���`a ���`etitle���aoa=���bs2a"���bs2qScalarFormatter()���bs2a"���`a)���`a
���`daxs1���`a[���bmia4���`a]���aoa.���`exaxis���aoa.���`sset_major_formatter���`a(���`fticker���aoa.���`oScalarFormatter���`a(���`kuseMathText���aoa=���bkcdTrue���`a)���`a)���`a
���`a
���bc1u# FormatStr formatter���`a
���`esetup���`a(���`daxs1���`a[���bmia5���`a]���`a,���`a ���`etitle���aoa=���bs2a"���bs2sFormatStrFormatter(���bs2a'���bs2a#���bsib%d���bs2a'���bs2a)���bs2a"���`a)���`a
���`daxs1���`a[���bmia5���`a]���aoa.���`exaxis���aoa.���`sset_major_formatter���`a(���`fticker���aoa.���`rFormatStrFormatter���`a(���bs2a"���bs2a#���bsib%d���bs2a"���`a)���`a)���`a
���`a
���bc1s# Percent formatter���`a
���`esetup���`a(���`daxs1���`a[���bmia6���`a]���`a,���`a ���`etitle���aoa=���bs2a"���bs2xPercentFormatter(xmax=5)���bs2a"���`a)���`a
���`daxs1���`a[���bmia6���`a]���aoa.���`exaxis���aoa.���`sset_major_formatter���`a(���`fticker���aoa.���`pPercentFormatter���`a(���`dxmax���aoa=���bmia5���`a)���`a)���`a
���`a
���`dfig1���aoa.���`ltight_layout���`a(���`a)���`a
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
���bc1x##    - `matplotlib.pyplot.subplots`���`a
���bc1x"#    - `matplotlib.axes.Axes.text`���`a
���bc1x1#    - `matplotlib.axis.Axis.set_major_formatter`���`a
���bc1x/#    - `matplotlib.axis.Axis.set_major_locator`���`a
���bc1x/#    - `matplotlib.axis.Axis.set_minor_locator`���`a
���bc1x1#    - `matplotlib.axis.XAxis.set_ticks_position`���`a
���bc1x1#    - `matplotlib.axis.YAxis.set_ticks_position`���`a
���bc1x)#    - `matplotlib.ticker.FixedFormatter`���`a
���bc1x'#    - `matplotlib.ticker.FixedLocator`���`a
���bc1x-#    - `matplotlib.ticker.FormatStrFormatter`���`a
���bc1x(#    - `matplotlib.ticker.FuncFormatter`���`a
���bc1x*#    - `matplotlib.ticker.MultipleLocator`���`a
���bc1x(#    - `matplotlib.ticker.NullFormatter`���`a
���bc1x&#    - `matplotlib.ticker.NullLocator`���`a
���bc1x+#    - `matplotlib.ticker.PercentFormatter`���`a
���bc1x*#    - `matplotlib.ticker.ScalarFormatter`���`a
���bc1x-#    - `matplotlib.ticker.StrMethodFormatter`���`a
`dNone�