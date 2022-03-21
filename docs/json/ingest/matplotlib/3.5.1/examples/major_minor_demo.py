ŸØÇÅŸ¥ÉôtŸ±ÇbsaarŸ±Çbsdy'"""
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
"""Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±ÇbknfimportŸ±Ç`a Ÿ±ÇbnnŸ¢ÑjmatplotlibŸ†Ñjmatplotlibe3.5.1fmodulejmatplotlibfmoduleıŸ±Çbnna.Ÿ±ÇbnnfpyplotŸ±Ç`a Ÿ±ÇakbasŸ±Ç`a Ÿ±ÇbnncpltŸ±Ç`a
Ÿ±ÇbknfimportŸ±Ç`a Ÿ±ÇbnnŸ¢ÑenumpyŸ†Ñenumpyf1.22.3fmoduleenumpyfmoduleıŸ±Ç`a Ÿ±ÇakbasŸ±Ç`a Ÿ±ÇbnnbnpŸ±Ç`a
Ÿ±ÇbkndfromŸ±Ç`a Ÿ±ÇbnnŸ¢ÑjmatplotlibŸ†Ñjmatplotlibe3.5.1fmodulejmatplotlibfmoduleıŸ±Çbnna.Ÿ±ÇbnnftickerŸ±Ç`a Ÿ±ÇbknfimportŸ±Ç`a Ÿ±Ç`a(Ÿ±Ç`oMultipleLocatorŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`pAutoMinorLocatorŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`atŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`farangeŸ±Ç`a(Ÿ±Çbmfc0.0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfe100.0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfc0.1Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`asŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`csinŸ±Ç`a(Ÿ±Çbmfc0.1Ÿ±Ç`a Ÿ±Çaoa*Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`bpiŸ±Ç`a Ÿ±Çaoa*Ÿ±Ç`a Ÿ±Ç`atŸ±Ç`a)Ÿ±Ç`a Ÿ±Çaoa*Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`cexpŸ±Ç`a(Ÿ±Çaoa-Ÿ±Ç`atŸ±Ç`a Ÿ±Çaoa*Ÿ±Ç`a Ÿ±Çbmfd0.01Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`cfigŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`baxŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`hsubplotsŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`dplotŸ±Ç`a(Ÿ±Ç`atŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`asŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1xL# Make a plot with major ticks that are multiples of 20 and minor ticks thatŸ±Ç`a
Ÿ±Çbc1xN# are multiples of 5.  Label major ticks with '.0f' formatting but don't labelŸ±Ç`a
Ÿ±Çbc1xH# minor ticks.  The string is used directly, the `StrMethodFormatter` isŸ±Ç`a
Ÿ±Çbc1x# created automatically.Ÿ±Ç`a
Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`exaxisŸ±Çaoa.Ÿ±Ç`qset_major_locatorŸ±Ç`a(Ÿ±Ç`oMultipleLocatorŸ±Ç`a(Ÿ±Çbmib20Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`exaxisŸ±Çaoa.Ÿ±Ç`sset_major_formatterŸ±Ç`a(Ÿ±Çbs1a'Ÿ±Çbsig{x:.0f}Ÿ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1x<# For the minor ticks, use no labels; default NullFormatter.Ÿ±Ç`a
Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`exaxisŸ±Çaoa.Ÿ±Ç`qset_minor_locatorŸ±Ç`a(Ÿ±Ç`oMultipleLocatorŸ±Ç`a(Ÿ±Çbmia5Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`dshowŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1xO###############################################################################Ÿ±Ç`a
Ÿ±Çbc1x5# Automatic tick selection for major and minor ticks.Ÿ±Ç`a
Ÿ±Çbc1a#Ÿ±Ç`a
Ÿ±Çbc1xO# Use interactive pan and zoom to see how the tick intervals change. There willŸ±Ç`a
Ÿ±Çbc1xL# be either 4 or 5 minor tick intervals per major interval, depending on theŸ±Ç`a
Ÿ±Çbc1q# major interval.Ÿ±Ç`a
Ÿ±Çbc1a#Ÿ±Ç`a
Ÿ±Çbc1xM# One can supply an argument to `.AutoMinorLocator` to specify a fixed numberŸ±Ç`a
Ÿ±Çbc1xK# of minor intervals per major interval, e.g. ``AutoMinorLocator(2)`` wouldŸ±Ç`a
Ÿ±Çbc1x2# lead to a single minor tick between major ticks.Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`atŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`farangeŸ±Ç`a(Ÿ±Çbmfc0.0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfe100.0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd0.01Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`asŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`csinŸ±Ç`a(Ÿ±Çbmia2Ÿ±Ç`a Ÿ±Çaoa*Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`bpiŸ±Ç`a Ÿ±Çaoa*Ÿ±Ç`a Ÿ±Ç`atŸ±Ç`a)Ÿ±Ç`a Ÿ±Çaoa*Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`cexpŸ±Ç`a(Ÿ±Çaoa-Ÿ±Ç`atŸ±Ç`a Ÿ±Çaoa*Ÿ±Ç`a Ÿ±Çbmfd0.01Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`cfigŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`baxŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`hsubplotsŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`dplotŸ±Ç`a(Ÿ±Ç`atŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`asŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`exaxisŸ±Çaoa.Ÿ±Ç`qset_minor_locatorŸ±Ç`a(Ÿ±Ç`pAutoMinorLocatorŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`ktick_paramsŸ±Ç`a(Ÿ±Ç`ewhichŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1dbothŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ewidthŸ±Çaoa=Ÿ±Çbmia2Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`ktick_paramsŸ±Ç`a(Ÿ±Ç`ewhichŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1emajorŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`flengthŸ±Çaoa=Ÿ±Çbmia7Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`ktick_paramsŸ±Ç`a(Ÿ±Ç`ewhichŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1eminorŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`flengthŸ±Çaoa=Ÿ±Çbmia4Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ecolorŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1arŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`dshowŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1xM#############################################################################Ÿ±Ç`a
Ÿ±Çbc1a#Ÿ±Ç`a
Ÿ±Çbc1x# .. admonition:: ReferencesŸ±Ç`a
Ÿ±Çbc1a#Ÿ±Ç`a
Ÿ±Çbc1xN#    The use of the following functions, methods, classes and modules is shownŸ±Ç`a
Ÿ±Çbc1u#    in this example:Ÿ±Ç`a
Ÿ±Çbc1a#Ÿ±Ç`a
Ÿ±Çbc1x##    - `matplotlib.pyplot.subplots`Ÿ±Ç`a
Ÿ±Çbc1x1#    - `matplotlib.axis.Axis.set_major_formatter`Ÿ±Ç`a
Ÿ±Çbc1x/#    - `matplotlib.axis.Axis.set_major_locator`Ÿ±Ç`a
Ÿ±Çbc1x/#    - `matplotlib.axis.Axis.set_minor_locator`Ÿ±Ç`a
Ÿ±Çbc1x+#    - `matplotlib.ticker.AutoMinorLocator`Ÿ±Ç`a
Ÿ±Çbc1x*#    - `matplotlib.ticker.MultipleLocator`Ÿ±Ç`a
Ÿ±Çbc1x-#    - `matplotlib.ticker.StrMethodFormatter`Ÿ±Ç`a
`dNoneˆ