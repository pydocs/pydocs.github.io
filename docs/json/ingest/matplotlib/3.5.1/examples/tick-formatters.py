ŸØÇÅŸ¥ÉôÄŸ±ÇbsdxÔ"""
===============
Tick formatters
===============

Tick formatters define how the numeric value associated with a tick on an axis
is formatted as a string.

This example illustrates the usage and effect of the most common formatters.
"""Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±ÇbknfimportŸ±Ç`a Ÿ±ÇbnnŸ¢ÑjmatplotlibŸ†Ñjmatplotlibe3.5.1fmodulejmatplotlibfmoduleıŸ±Çbnna.Ÿ±ÇbnnfpyplotŸ±Ç`a Ÿ±ÇakbasŸ±Ç`a Ÿ±ÇbnncpltŸ±Ç`a
Ÿ±ÇbkndfromŸ±Ç`a Ÿ±ÇbnnŸ¢ÑjmatplotlibŸ†Ñjmatplotlibe3.5.1fmodulejmatplotlibfmoduleıŸ±Ç`a Ÿ±ÇbknfimportŸ±Ç`a Ÿ±Ç`ftickerŸ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±ÇakcdefŸ±Ç`a Ÿ±ÇbnfesetupŸ±Ç`a(Ÿ±Ç`baxŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`etitleŸ±Ç`a)Ÿ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Çbsdx;"""Set up common parameters for the Axes in the example."""Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Çbc1x# only show the bottom spineŸ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`eyaxisŸ±Çaoa.Ÿ±Ç`qset_major_locatorŸ±Ç`a(Ÿ±Ç`ftickerŸ±Çaoa.Ÿ±Ç`kNullLocatorŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`fspinesŸ±Çaoa.Ÿ±Ç`erightŸ±Çaoa.Ÿ±Ç`iset_colorŸ±Ç`a(Ÿ±Çbs1a'Ÿ±Çbs1dnoneŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`fspinesŸ±Çaoa.Ÿ±Ç`dleftŸ±Çaoa.Ÿ±Ç`iset_colorŸ±Ç`a(Ÿ±Çbs1a'Ÿ±Çbs1dnoneŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`fspinesŸ±Çaoa.Ÿ±Ç`ctopŸ±Çaoa.Ÿ±Ç`iset_colorŸ±Ç`a(Ÿ±Çbs1a'Ÿ±Çbs1dnoneŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Çbc1w# define tick positionsŸ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`exaxisŸ±Çaoa.Ÿ±Ç`qset_major_locatorŸ±Ç`a(Ÿ±Ç`ftickerŸ±Çaoa.Ÿ±Ç`oMultipleLocatorŸ±Ç`a(Ÿ±Çbmfd1.00Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`exaxisŸ±Çaoa.Ÿ±Ç`qset_minor_locatorŸ±Ç`a(Ÿ±Ç`ftickerŸ±Çaoa.Ÿ±Ç`oMultipleLocatorŸ±Ç`a(Ÿ±Çbmfd0.25Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`exaxisŸ±Çaoa.Ÿ±Ç`rset_ticks_positionŸ±Ç`a(Ÿ±Çbs1a'Ÿ±Çbs1fbottomŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`ktick_paramsŸ±Ç`a(Ÿ±Ç`ewhichŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1emajorŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ewidthŸ±Çaoa=Ÿ±Çbmfd1.00Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`flengthŸ±Çaoa=Ÿ±Çbmia5Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`ktick_paramsŸ±Ç`a(Ÿ±Ç`ewhichŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1eminorŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ewidthŸ±Çaoa=Ÿ±Çbmfd0.75Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`flengthŸ±Çaoa=Ÿ±Çbmfc2.5Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ilabelsizeŸ±Çaoa=Ÿ±Çbmib10Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`hset_xlimŸ±Ç`a(Ÿ±Çbmia0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia5Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`hset_ylimŸ±Ç`a(Ÿ±Çbmia0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia1Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`dtextŸ±Ç`a(Ÿ±Çbmfc0.0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfc0.2Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`etitleŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`itransformŸ±Çaoa=Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`itransAxesŸ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`l            Ÿ±Ç`hfontsizeŸ±Çaoa=Ÿ±Çbmib14Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`hfontnameŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1iMonospaceŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ecolorŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1htab:blueŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1xM#############################################################################Ÿ±Ç`a
Ÿ±Çbc1xL# Tick formatters can be set in one of two ways, either by passing a ``str``Ÿ±Ç`a
Ÿ±Çbc1xN# or function to `~.Axis.set_major_formatter` or `~.Axis.set_minor_formatter`,Ÿ±Ç`a
Ÿ±Çbc1xO# or by creating an instance of one of the various `~.ticker.Formatter` classesŸ±Ç`a
Ÿ±Çbc1x7# and providing that to `~.Axis.set_major_formatter` orŸ±Ç`a
Ÿ±Çbc1x# `~.Axis.set_minor_formatter`.Ÿ±Ç`a
Ÿ±Çbc1a#Ÿ±Ç`a
Ÿ±Çbc1x=# The first two examples directly pass a ``str`` or function.Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`dfig0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`daxs0Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`hsubplotsŸ±Ç`a(Ÿ±Çbmia2Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`gfigsizeŸ±Çaoa=Ÿ±Ç`a(Ÿ±Çbmia8Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia2Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`dfig0Ÿ±Çaoa.Ÿ±Ç`hsuptitleŸ±Ç`a(Ÿ±Çbs1a'Ÿ±Çbs1qSimple FormattingŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1xK# A ``str``, using format string function syntax, can be used directly as aŸ±Ç`a
Ÿ±Çbc1xN# formatter.  The variable ``x`` is the tick value and the variable ``pos`` isŸ±Ç`a
Ÿ±Çbc1xB# tick position.  This creates a StrMethodFormatter automatically.Ÿ±Ç`a
Ÿ±Ç`esetupŸ±Ç`a(Ÿ±Ç`daxs0Ÿ±Ç`a[Ÿ±Çbmia0Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`etitleŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2a'Ÿ±Çbsic{x}Ÿ±Çbs2c kmŸ±Çbs2a'Ÿ±Çbs2a"Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`daxs0Ÿ±Ç`a[Ÿ±Çbmia0Ÿ±Ç`a]Ÿ±Çaoa.Ÿ±Ç`exaxisŸ±Çaoa.Ÿ±Ç`sset_major_formatterŸ±Ç`a(Ÿ±Çbs1a'Ÿ±Çbsic{x}Ÿ±Çbs1c kmŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1xM# A function can also be used directly as a formatter. The function must takeŸ±Ç`a
Ÿ±Çbc1xL# two arguments: ``x`` for the tick value and ``pos`` for the tick position,Ÿ±Ç`a
Ÿ±Çbc1xH# and must return a ``str``. This creates a FuncFormatter automatically.Ÿ±Ç`a
Ÿ±Ç`esetupŸ±Ç`a(Ÿ±Ç`daxs0Ÿ±Ç`a[Ÿ±Çbmia1Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`etitleŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2wlambda x, pos: str(x-5)Ÿ±Çbs2a"Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`daxs0Ÿ±Ç`a[Ÿ±Çbmia1Ÿ±Ç`a]Ÿ±Çaoa.Ÿ±Ç`exaxisŸ±Çaoa.Ÿ±Ç`sset_major_formatterŸ±Ç`a(Ÿ±ÇakflambdaŸ±Ç`a Ÿ±Ç`axŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`cposŸ±Ç`a:Ÿ±Ç`a Ÿ±ÇbnbcstrŸ±Ç`a(Ÿ±Ç`axŸ±Çaoa-Ÿ±Çbmia5Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`dfig0Ÿ±Çaoa.Ÿ±Ç`ltight_layoutŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1xM#############################################################################Ÿ±Ç`a
Ÿ±Çbc1x2# The remaining examples use `.Formatter` objects.Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`dfig1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`daxs1Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`hsubplotsŸ±Ç`a(Ÿ±Çbmia7Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`gfigsizeŸ±Çaoa=Ÿ±Ç`a(Ÿ±Çbmia8Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia6Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`dfig1Ÿ±Çaoa.Ÿ±Ç`hsuptitleŸ±Ç`a(Ÿ±Çbs1a'Ÿ±Çbs1xFormatter Object FormattingŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1p# Null formatterŸ±Ç`a
Ÿ±Ç`esetupŸ±Ç`a(Ÿ±Ç`daxs1Ÿ±Ç`a[Ÿ±Çbmia0Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`etitleŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2oNullFormatter()Ÿ±Çbs2a"Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`daxs1Ÿ±Ç`a[Ÿ±Çbmia0Ÿ±Ç`a]Ÿ±Çaoa.Ÿ±Ç`exaxisŸ±Çaoa.Ÿ±Ç`sset_major_formatterŸ±Ç`a(Ÿ±Ç`ftickerŸ±Çaoa.Ÿ±Ç`mNullFormatterŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1u# StrMethod formatterŸ±Ç`a
Ÿ±Ç`esetupŸ±Ç`a(Ÿ±Ç`daxs1Ÿ±Ç`a[Ÿ±Çbmia1Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`etitleŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2sStrMethodFormatter(Ÿ±Çbs2a'Ÿ±Çbsig{x:.3f}Ÿ±Çbs2a'Ÿ±Çbs2a)Ÿ±Çbs2a"Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`daxs1Ÿ±Ç`a[Ÿ±Çbmia1Ÿ±Ç`a]Ÿ±Çaoa.Ÿ±Ç`exaxisŸ±Çaoa.Ÿ±Ç`sset_major_formatterŸ±Ç`a(Ÿ±Ç`ftickerŸ±Çaoa.Ÿ±Ç`rStrMethodFormatterŸ±Ç`a(Ÿ±Çbs2a"Ÿ±Çbsig{x:.3f}Ÿ±Çbs2a"Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1x*# FuncFormatter can be used as a decoratorŸ±Ç`a
Ÿ±Çbndg@tickerŸ±Çaoa.Ÿ±Ç`mFuncFormatterŸ±Ç`a
Ÿ±ÇakcdefŸ±Ç`a Ÿ±Çbnfomajor_formatterŸ±Ç`a(Ÿ±Ç`axŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`cposŸ±Ç`a)Ÿ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±ÇakfreturnŸ±Ç`a Ÿ±ÇbsaafŸ±Çbs1a'Ÿ±Çbs1a[Ÿ±Çbsia{Ÿ±Ç`axŸ±Çbsia:Ÿ±Çbs1c.2fŸ±Çbsia}Ÿ±Çbs1a]Ÿ±Çbs1a'Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`esetupŸ±Ç`a(Ÿ±Ç`daxs1Ÿ±Ç`a[Ÿ±Çbmia2Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`etitleŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1nFuncFormatter(Ÿ±Çbs1a"Ÿ±Çbs1a[Ÿ±Çbsif{:.2f}Ÿ±Çbs1a]Ÿ±Çbs1a"Ÿ±Çbs1h.format)Ÿ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`daxs1Ÿ±Ç`a[Ÿ±Çbmia2Ÿ±Ç`a]Ÿ±Çaoa.Ÿ±Ç`exaxisŸ±Çaoa.Ÿ±Ç`sset_major_formatterŸ±Ç`a(Ÿ±Ç`omajor_formatterŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1q# Fixed formatterŸ±Ç`a
Ÿ±Ç`esetupŸ±Ç`a(Ÿ±Ç`daxs1Ÿ±Ç`a[Ÿ±Çbmia3Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`etitleŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2pFixedFormatter([Ÿ±Çbs2a'Ÿ±Çbs2aAŸ±Çbs2a'Ÿ±Çbs2b, Ÿ±Çbs2a'Ÿ±Çbs2aBŸ±Çbs2a'Ÿ±Çbs2b, Ÿ±Çbs2a'Ÿ±Çbs2aCŸ±Çbs2a'Ÿ±Çbs2g, ...])Ÿ±Çbs2a"Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Çbc1x@# FixedFormatter should only be used together with FixedLocator.Ÿ±Ç`a
Ÿ±Çbc1x=# Otherwise, one cannot be sure where the labels will end up.Ÿ±Ç`a
Ÿ±Ç`ipositionsŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`a[Ÿ±Çbmia0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia2Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia3Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia4Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia5Ÿ±Ç`a]Ÿ±Ç`a
Ÿ±Ç`flabelsŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`a[Ÿ±Çbs1a'Ÿ±Çbs1aAŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1aBŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1aCŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1aDŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1aEŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1aFŸ±Çbs1a'Ÿ±Ç`a]Ÿ±Ç`a
Ÿ±Ç`daxs1Ÿ±Ç`a[Ÿ±Çbmia3Ÿ±Ç`a]Ÿ±Çaoa.Ÿ±Ç`exaxisŸ±Çaoa.Ÿ±Ç`qset_major_locatorŸ±Ç`a(Ÿ±Ç`ftickerŸ±Çaoa.Ÿ±Ç`lFixedLocatorŸ±Ç`a(Ÿ±Ç`ipositionsŸ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`daxs1Ÿ±Ç`a[Ÿ±Çbmia3Ÿ±Ç`a]Ÿ±Çaoa.Ÿ±Ç`exaxisŸ±Çaoa.Ÿ±Ç`sset_major_formatterŸ±Ç`a(Ÿ±Ç`ftickerŸ±Çaoa.Ÿ±Ç`nFixedFormatterŸ±Ç`a(Ÿ±Ç`flabelsŸ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1r# Scalar formatterŸ±Ç`a
Ÿ±Ç`esetupŸ±Ç`a(Ÿ±Ç`daxs1Ÿ±Ç`a[Ÿ±Çbmia4Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`etitleŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2qScalarFormatter()Ÿ±Çbs2a"Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`daxs1Ÿ±Ç`a[Ÿ±Çbmia4Ÿ±Ç`a]Ÿ±Çaoa.Ÿ±Ç`exaxisŸ±Çaoa.Ÿ±Ç`sset_major_formatterŸ±Ç`a(Ÿ±Ç`ftickerŸ±Çaoa.Ÿ±Ç`oScalarFormatterŸ±Ç`a(Ÿ±Ç`kuseMathTextŸ±Çaoa=Ÿ±ÇbkcdTrueŸ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1u# FormatStr formatterŸ±Ç`a
Ÿ±Ç`esetupŸ±Ç`a(Ÿ±Ç`daxs1Ÿ±Ç`a[Ÿ±Çbmia5Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`etitleŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2sFormatStrFormatter(Ÿ±Çbs2a'Ÿ±Çbs2a#Ÿ±Çbsib%dŸ±Çbs2a'Ÿ±Çbs2a)Ÿ±Çbs2a"Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`daxs1Ÿ±Ç`a[Ÿ±Çbmia5Ÿ±Ç`a]Ÿ±Çaoa.Ÿ±Ç`exaxisŸ±Çaoa.Ÿ±Ç`sset_major_formatterŸ±Ç`a(Ÿ±Ç`ftickerŸ±Çaoa.Ÿ±Ç`rFormatStrFormatterŸ±Ç`a(Ÿ±Çbs2a"Ÿ±Çbs2a#Ÿ±Çbsib%dŸ±Çbs2a"Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1s# Percent formatterŸ±Ç`a
Ÿ±Ç`esetupŸ±Ç`a(Ÿ±Ç`daxs1Ÿ±Ç`a[Ÿ±Çbmia6Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`etitleŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2xPercentFormatter(xmax=5)Ÿ±Çbs2a"Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`daxs1Ÿ±Ç`a[Ÿ±Çbmia6Ÿ±Ç`a]Ÿ±Çaoa.Ÿ±Ç`exaxisŸ±Çaoa.Ÿ±Ç`sset_major_formatterŸ±Ç`a(Ÿ±Ç`ftickerŸ±Çaoa.Ÿ±Ç`pPercentFormatterŸ±Ç`a(Ÿ±Ç`dxmaxŸ±Çaoa=Ÿ±Çbmia5Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`dfig1Ÿ±Çaoa.Ÿ±Ç`ltight_layoutŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
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
Ÿ±Çbc1x"#    - `matplotlib.axes.Axes.text`Ÿ±Ç`a
Ÿ±Çbc1x1#    - `matplotlib.axis.Axis.set_major_formatter`Ÿ±Ç`a
Ÿ±Çbc1x/#    - `matplotlib.axis.Axis.set_major_locator`Ÿ±Ç`a
Ÿ±Çbc1x/#    - `matplotlib.axis.Axis.set_minor_locator`Ÿ±Ç`a
Ÿ±Çbc1x1#    - `matplotlib.axis.XAxis.set_ticks_position`Ÿ±Ç`a
Ÿ±Çbc1x1#    - `matplotlib.axis.YAxis.set_ticks_position`Ÿ±Ç`a
Ÿ±Çbc1x)#    - `matplotlib.ticker.FixedFormatter`Ÿ±Ç`a
Ÿ±Çbc1x'#    - `matplotlib.ticker.FixedLocator`Ÿ±Ç`a
Ÿ±Çbc1x-#    - `matplotlib.ticker.FormatStrFormatter`Ÿ±Ç`a
Ÿ±Çbc1x(#    - `matplotlib.ticker.FuncFormatter`Ÿ±Ç`a
Ÿ±Çbc1x*#    - `matplotlib.ticker.MultipleLocator`Ÿ±Ç`a
Ÿ±Çbc1x(#    - `matplotlib.ticker.NullFormatter`Ÿ±Ç`a
Ÿ±Çbc1x&#    - `matplotlib.ticker.NullLocator`Ÿ±Ç`a
Ÿ±Çbc1x+#    - `matplotlib.ticker.PercentFormatter`Ÿ±Ç`a
Ÿ±Çbc1x*#    - `matplotlib.ticker.ScalarFormatter`Ÿ±Ç`a
Ÿ±Çbc1x-#    - `matplotlib.ticker.StrMethodFormatter`Ÿ±Ç`a
`dNoneˆ