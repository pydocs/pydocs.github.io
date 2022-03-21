Ù¯‚Ù´ƒ™Ù±‚bsdy{"""
==============================
Centering labels between ticks
==============================

Ticklabels are aligned relative to their associated tick. The alignment
'center', 'left', or 'right' can be controlled using the horizontal alignment
property::

    for label in ax.xaxis.get_xticklabels():
        label.set_horizontalalignment('right')

However there is no direct way to center the labels between ticks. To fake
this behavior, one can place a label on the minor ticks in between the major
ticks, and hide the major tick labels and minor ticks.

Here is an example that labels the months, centered between the ticks.
"""Ù±‚`a
Ù±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„enumpyÙ „enumpyf1.22.3fmoduleenumpyfmoduleõÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnnbnpÙ±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnnecbookÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnnecbookÙ±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnnedatesÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnnedatesÙ±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnnftickerÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnnftickerÙ±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnnfpyplotÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnncpltÙ±‚`a
Ù±‚`a
Ù±‚bc1x0# load some financial data; Google's stock priceÙ±‚`a
Ù±‚`arÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`a(Ù±‚`ecbookÙ±‚aoa.Ù±‚`oget_sample_dataÙ±‚`a(Ù±‚bs1a'Ù±‚bs1hgoog.npzÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`gnp_loadÙ±‚aoa=Ù±‚bkcdTrueÙ±‚`a)Ù±‚`a[Ù±‚bs1a'Ù±‚bs1jprice_dataÙ±‚bs1a'Ù±‚`a]Ù±‚`a
Ù±‚`e     Ù±‚aoa.Ù±‚`dviewÙ±‚`a(Ù±‚`bnpÙ±‚aoa.Ù±‚`hrecarrayÙ±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`arÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`arÙ±‚`a[Ù±‚aoa-Ù±‚bmic250Ù±‚`a:Ù±‚`a]Ù±‚`b  Ù±‚bc1w# get the last 250 daysÙ±‚`a
Ù±‚`a
Ù±‚`cfigÙ±‚`a,Ù±‚`a Ù±‚`baxÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cpltÙ±‚aoa.Ù±‚`hsubplotsÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`dplotÙ±‚`a(Ù±‚`arÙ±‚aoa.Ù±‚`ddateÙ±‚`a,Ù±‚`a Ù±‚`arÙ±‚aoa.Ù±‚`iadj_closeÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`exaxisÙ±‚aoa.Ù±‚`qset_major_locatorÙ±‚`a(Ù±‚`edatesÙ±‚aoa.Ù±‚`lMonthLocatorÙ±‚`a(Ù±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚bc1xE# 16 is a slight approximation since months differ in number of days.Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`exaxisÙ±‚aoa.Ù±‚`qset_minor_locatorÙ±‚`a(Ù±‚`edatesÙ±‚aoa.Ù±‚`lMonthLocatorÙ±‚`a(Ù±‚`jbymonthdayÙ±‚aoa=Ù±‚bmib16Ù±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`exaxisÙ±‚aoa.Ù±‚`sset_major_formatterÙ±‚`a(Ù±‚`ftickerÙ±‚aoa.Ù±‚`mNullFormatterÙ±‚`a(Ù±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`exaxisÙ±‚aoa.Ù±‚`sset_minor_formatterÙ±‚`a(Ù±‚`edatesÙ±‚aoa.Ù±‚`mDateFormatterÙ±‚`a(Ù±‚bs1a'Ù±‚bs1a%Ù±‚bs1abÙ±‚bs1a'Ù±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚akcforÙ±‚`a Ù±‚`dtickÙ±‚`a Ù±‚bowbinÙ±‚`a Ù±‚`baxÙ±‚aoa.Ù±‚`exaxisÙ±‚aoa.Ù±‚`oget_minor_ticksÙ±‚`a(Ù±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`d    Ù±‚`dtickÙ±‚aoa.Ù±‚`itick1lineÙ±‚aoa.Ù±‚`nset_markersizeÙ±‚`a(Ù±‚bmia0Ù±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`dtickÙ±‚aoa.Ù±‚`itick2lineÙ±‚aoa.Ù±‚`nset_markersizeÙ±‚`a(Ù±‚bmia0Ù±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`dtickÙ±‚aoa.Ù±‚`flabel1Ù±‚aoa.Ù±‚`wset_horizontalalignmentÙ±‚`a(Ù±‚bs1a'Ù±‚bs1fcenterÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`dimidÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bnbclenÙ±‚`a(Ù±‚`arÙ±‚`a)Ù±‚`a Ù±‚aoa/Ù±‚aoa/Ù±‚`a Ù±‚bmia2Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`jset_xlabelÙ±‚`a(Ù±‚bnbcstrÙ±‚`a(Ù±‚`arÙ±‚aoa.Ù±‚`ddateÙ±‚`a[Ù±‚`dimidÙ±‚`a]Ù±‚aoa.Ù±‚`ditemÙ±‚`a(Ù±‚`a)Ù±‚aoa.Ù±‚`dyearÙ±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`cpltÙ±‚aoa.Ù±‚`dshowÙ±‚`a(Ù±‚`a)Ù±‚`a
`dNoneö