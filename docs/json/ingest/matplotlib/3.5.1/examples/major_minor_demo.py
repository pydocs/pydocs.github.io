��������t���bsaar���bsdy'"""
=====================
Major and minor ticks
=====================

Demonstrate how to use major and minor tickers.

The two relevant classes are `.Locator`\s and `.Formatter`\s.  Locators
determine where the ticks are, and formatters control the formatting of tick
labels.

Minor ticks are off by default (using `.NullLocator` and `.NullFormatter`).
Minor ticks can be turned on without labels by setting the minor locator.
Minor tick labels can be turned on by setting the minor formatter.

`.MultipleLocator` places ticks on multiples of some base.
`.StrMethodFormatter` uses a format string (e.g., ``'{x:d}'`` or ``'{x:1.2f}'``
or ``'{x:1.1f} cm'``) to format the tick labels (the variable in the format
string must be ``'x'``).  For a `.StrMethodFormatter`, the string can be passed
directly to `.Axis.set_major_formatter` or
`.Axis.set_minor_formatter`.  An appropriate `.StrMethodFormatter` will
be created and used automatically.

`.pyplot.grid` changes the grid settings of the major ticks of the y and y axis
together.  If you want to control the grid of the minor ticks for a given axis,
use for example ::

  ax.xaxis.grid(True, which='minor')

Note that a given locator or formatter instance can only be used on a single
axis (because the locator stores references to the axis data and view limits).
"""���`a
���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���bkndfrom���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfticker���`a ���bknfimport���`a ���`a(���`oMultipleLocator���`a,���`a ���`pAutoMinorLocator���`a)���`a
���`a
���`a
���`at���`a ���aoa=���`a ���`bnp���aoa.���`farange���`a(���bmfc0.0���`a,���`a ���bmfe100.0���`a,���`a ���bmfc0.1���`a)���`a
���`as���`a ���aoa=���`a ���`bnp���aoa.���`csin���`a(���bmfc0.1���`a ���aoa*���`a ���`bnp���aoa.���`bpi���`a ���aoa*���`a ���`at���`a)���`a ���aoa*���`a ���`bnp���aoa.���`cexp���`a(���aoa-���`at���`a ���aoa*���`a ���bmfd0.01���`a)���`a
���`a
���`cfig���`a,���`a ���`bax���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`a)���`a
���`bax���aoa.���`dplot���`a(���`at���`a,���`a ���`as���`a)���`a
���`a
���bc1xL# Make a plot with major ticks that are multiples of 20 and minor ticks that���`a
���bc1xN# are multiples of 5.  Label major ticks with '.0f' formatting but don't label���`a
���bc1xH# minor ticks.  The string is used directly, the `StrMethodFormatter` is���`a
���bc1x# created automatically.���`a
���`bax���aoa.���`exaxis���aoa.���`qset_major_locator���`a(���`oMultipleLocator���`a(���bmib20���`a)���`a)���`a
���`bax���aoa.���`exaxis���aoa.���`sset_major_formatter���`a(���bs1a'���bsig{x:.0f}���bs1a'���`a)���`a
���`a
���bc1x<# For the minor ticks, use no labels; default NullFormatter.���`a
���`bax���aoa.���`exaxis���aoa.���`qset_minor_locator���`a(���`oMultipleLocator���`a(���bmia5���`a)���`a)���`a
���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
���`a
���bc1xO###############################################################################���`a
���bc1x5# Automatic tick selection for major and minor ticks.���`a
���bc1a#���`a
���bc1xO# Use interactive pan and zoom to see how the tick intervals change. There will���`a
���bc1xL# be either 4 or 5 minor tick intervals per major interval, depending on the���`a
���bc1q# major interval.���`a
���bc1a#���`a
���bc1xM# One can supply an argument to `.AutoMinorLocator` to specify a fixed number���`a
���bc1xK# of minor intervals per major interval, e.g. ``AutoMinorLocator(2)`` would���`a
���bc1x2# lead to a single minor tick between major ticks.���`a
���`a
���`at���`a ���aoa=���`a ���`bnp���aoa.���`farange���`a(���bmfc0.0���`a,���`a ���bmfe100.0���`a,���`a ���bmfd0.01���`a)���`a
���`as���`a ���aoa=���`a ���`bnp���aoa.���`csin���`a(���bmia2���`a ���aoa*���`a ���`bnp���aoa.���`bpi���`a ���aoa*���`a ���`at���`a)���`a ���aoa*���`a ���`bnp���aoa.���`cexp���`a(���aoa-���`at���`a ���aoa*���`a ���bmfd0.01���`a)���`a
���`a
���`cfig���`a,���`a ���`bax���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`a)���`a
���`bax���aoa.���`dplot���`a(���`at���`a,���`a ���`as���`a)���`a
���`a
���`bax���aoa.���`exaxis���aoa.���`qset_minor_locator���`a(���`pAutoMinorLocator���`a(���`a)���`a)���`a
���`a
���`bax���aoa.���`ktick_params���`a(���`ewhich���aoa=���bs1a'���bs1dboth���bs1a'���`a,���`a ���`ewidth���aoa=���bmia2���`a)���`a
���`bax���aoa.���`ktick_params���`a(���`ewhich���aoa=���bs1a'���bs1emajor���bs1a'���`a,���`a ���`flength���aoa=���bmia7���`a)���`a
���`bax���aoa.���`ktick_params���`a(���`ewhich���aoa=���bs1a'���bs1eminor���bs1a'���`a,���`a ���`flength���aoa=���bmia4���`a,���`a ���`ecolor���aoa=���bs1a'���bs1ar���bs1a'���`a)���`a
���`a
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
���bc1x1#    - `matplotlib.axis.Axis.set_major_formatter`���`a
���bc1x/#    - `matplotlib.axis.Axis.set_major_locator`���`a
���bc1x/#    - `matplotlib.axis.Axis.set_minor_locator`���`a
���bc1x+#    - `matplotlib.ticker.AutoMinorLocator`���`a
���bc1x*#    - `matplotlib.ticker.MultipleLocator`���`a
���bc1x-#    - `matplotlib.ticker.StrMethodFormatter`���`a
`dNone�