Ù¯‚Ù´ƒ™>Ù±‚bsdyŽ"""
================================================
Formatting date ticks using ConciseDateFormatter
================================================

Finding good tick values and formatting the ticks for an axis that
has date data is often a challenge.  `~.dates.ConciseDateFormatter` is
meant to improve the strings chosen for the ticklabels, and to minimize
the strings used in those tick labels as much as possible.

.. note::

    This formatter is a candidate to become the default date tick formatter
    in future versions of Matplotlib.  Please report any issues or
    suggestions for improvement to the github repository or mailing list.

"""Ù±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnhdatetimeÙ±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnnfpyplotÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnncpltÙ±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnnedatesÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnnfmdatesÙ±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„enumpyÙ „enumpyf1.22.3fmoduleenumpyfmoduleõÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnnbnpÙ±‚`a
Ù±‚`a
Ù±‚bc1xM#############################################################################Ù±‚`a
Ù±‚bc1x# First, the default formatter.Ù±‚`a
Ù±‚`a
Ù±‚`dbaseÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`hdatetimeÙ±‚aoa.Ù±‚`hdatetimeÙ±‚`a(Ù±‚bmid2005Ù±‚`a,Ù±‚`a Ù±‚bmia2Ù±‚`a,Ù±‚`a Ù±‚bmia1Ù±‚`a)Ù±‚`a
Ù±‚`edatesÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`a[Ù±‚`dbaseÙ±‚`a Ù±‚aoa+Ù±‚`a Ù±‚`hdatetimeÙ±‚aoa.Ù±‚`itimedeltaÙ±‚`a(Ù±‚`ehoursÙ±‚aoa=Ù±‚`a(Ù±‚bmia2Ù±‚`a Ù±‚aoa*Ù±‚`a Ù±‚`aiÙ±‚`a)Ù±‚`a)Ù±‚`a Ù±‚akcforÙ±‚`a Ù±‚`aiÙ±‚`a Ù±‚bowbinÙ±‚`a Ù±‚bnberangeÙ±‚`a(Ù±‚bmic732Ù±‚`a)Ù±‚`a]Ù±‚`a
Ù±‚`aNÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bnbclenÙ±‚`a(Ù±‚`edatesÙ±‚`a)Ù±‚`a
Ù±‚`bnpÙ±‚aoa.Ù±‚`frandomÙ±‚aoa.Ù±‚`dseedÙ±‚`a(Ù±‚bmih19680801Ù±‚`a)Ù±‚`a
Ù±‚`ayÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`fcumsumÙ±‚`a(Ù±‚`bnpÙ±‚aoa.Ù±‚`frandomÙ±‚aoa.Ù±‚`erandnÙ±‚`a(Ù±‚`aNÙ±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`cfigÙ±‚`a,Ù±‚`a Ù±‚`caxsÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cpltÙ±‚aoa.Ù±‚`hsubplotsÙ±‚`a(Ù±‚bmia3Ù±‚`a,Ù±‚`a Ù±‚bmia1Ù±‚`a,Ù±‚`a Ù±‚`rconstrained_layoutÙ±‚aoa=Ù±‚bkcdTrueÙ±‚`a,Ù±‚`a Ù±‚`gfigsizeÙ±‚aoa=Ù±‚`a(Ù±‚bmia6Ù±‚`a,Ù±‚`a Ù±‚bmia6Ù±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`dlimsÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`a[Ù±‚`a(Ù±‚`bnpÙ±‚aoa.Ù±‚`jdatetime64Ù±‚`a(Ù±‚bs1a'Ù±‚bs1g2005-02Ù±‚bs1a'Ù±‚`a)Ù±‚`a,Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`jdatetime64Ù±‚`a(Ù±‚bs1a'Ù±‚bs1g2005-04Ù±‚bs1a'Ù±‚`a)Ù±‚`a)Ù±‚`a,Ù±‚`a
Ù±‚`h        Ù±‚`a(Ù±‚`bnpÙ±‚aoa.Ù±‚`jdatetime64Ù±‚`a(Ù±‚bs1a'Ù±‚bs1j2005-02-03Ù±‚bs1a'Ù±‚`a)Ù±‚`a,Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`jdatetime64Ù±‚`a(Ù±‚bs1a'Ù±‚bs1j2005-02-15Ù±‚bs1a'Ù±‚`a)Ù±‚`a)Ù±‚`a,Ù±‚`a
Ù±‚`h        Ù±‚`a(Ù±‚`bnpÙ±‚aoa.Ù±‚`jdatetime64Ù±‚`a(Ù±‚bs1a'Ù±‚bs1p2005-02-03 11:00Ù±‚bs1a'Ù±‚`a)Ù±‚`a,Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`jdatetime64Ù±‚`a(Ù±‚bs1a'Ù±‚bs1p2005-02-04 13:20Ù±‚bs1a'Ù±‚`a)Ù±‚`a)Ù±‚`a]Ù±‚`a
Ù±‚akcforÙ±‚`a Ù±‚`bnnÙ±‚`a,Ù±‚`a Ù±‚`baxÙ±‚`a Ù±‚bowbinÙ±‚`a Ù±‚bnbienumerateÙ±‚`a(Ù±‚`caxsÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`d    Ù±‚`baxÙ±‚aoa.Ù±‚`dplotÙ±‚`a(Ù±‚`edatesÙ±‚`a,Ù±‚`a Ù±‚`ayÙ±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`baxÙ±‚aoa.Ù±‚`hset_xlimÙ±‚`a(Ù±‚`dlimsÙ±‚`a[Ù±‚`bnnÙ±‚`a]Ù±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚bc1r# rotate_labels...Ù±‚`a
Ù±‚`d    Ù±‚akcforÙ±‚`a Ù±‚`elabelÙ±‚`a Ù±‚bowbinÙ±‚`a Ù±‚`baxÙ±‚aoa.Ù±‚`oget_xticklabelsÙ±‚`a(Ù±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`h        Ù±‚`elabelÙ±‚aoa.Ù±‚`lset_rotationÙ±‚`a(Ù±‚bmib40Ù±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚`elabelÙ±‚aoa.Ù±‚`wset_horizontalalignmentÙ±‚`a(Ù±‚bs1a'Ù±‚bs1erightÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`caxsÙ±‚`a[Ù±‚bmia0Ù±‚`a]Ù±‚aoa.Ù±‚`iset_titleÙ±‚`a(Ù±‚bs1a'Ù±‚bs1vDefault Date FormatterÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`cpltÙ±‚aoa.Ù±‚`dshowÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚bc1xM#############################################################################Ù±‚`a
Ù±‚bc1xG# The default date formatter is quite verbose, so we have the option ofÙ±‚`a
Ù±‚bc1xB# using `~.dates.ConciseDateFormatter`, as shown below.  Note thatÙ±‚`a
Ù±‚bc1xJ# for this example the labels do not need to be rotated as they do for theÙ±‚`a
Ù±‚bc1x@# default formatter because the labels are as small as possible.Ù±‚`a
Ù±‚`a
Ù±‚`cfigÙ±‚`a,Ù±‚`a Ù±‚`caxsÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cpltÙ±‚aoa.Ù±‚`hsubplotsÙ±‚`a(Ù±‚bmia3Ù±‚`a,Ù±‚`a Ù±‚bmia1Ù±‚`a,Ù±‚`a Ù±‚`rconstrained_layoutÙ±‚aoa=Ù±‚bkcdTrueÙ±‚`a,Ù±‚`a Ù±‚`gfigsizeÙ±‚aoa=Ù±‚`a(Ù±‚bmia6Ù±‚`a,Ù±‚`a Ù±‚bmia6Ù±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚akcforÙ±‚`a Ù±‚`bnnÙ±‚`a,Ù±‚`a Ù±‚`baxÙ±‚`a Ù±‚bowbinÙ±‚`a Ù±‚bnbienumerateÙ±‚`a(Ù±‚`caxsÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`d    Ù±‚`glocatorÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`fmdatesÙ±‚aoa.Ù±‚`oAutoDateLocatorÙ±‚`a(Ù±‚`hminticksÙ±‚aoa=Ù±‚bmia3Ù±‚`a,Ù±‚`a Ù±‚`hmaxticksÙ±‚aoa=Ù±‚bmia7Ù±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`iformatterÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`fmdatesÙ±‚aoa.Ù±‚`tConciseDateFormatterÙ±‚`a(Ù±‚`glocatorÙ±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`baxÙ±‚aoa.Ù±‚`exaxisÙ±‚aoa.Ù±‚`qset_major_locatorÙ±‚`a(Ù±‚`glocatorÙ±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`baxÙ±‚aoa.Ù±‚`exaxisÙ±‚aoa.Ù±‚`sset_major_formatterÙ±‚`a(Ù±‚`iformatterÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚`baxÙ±‚aoa.Ù±‚`dplotÙ±‚`a(Ù±‚`edatesÙ±‚`a,Ù±‚`a Ù±‚`ayÙ±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`baxÙ±‚aoa.Ù±‚`hset_xlimÙ±‚`a(Ù±‚`dlimsÙ±‚`a[Ù±‚`bnnÙ±‚`a]Ù±‚`a)Ù±‚`a
Ù±‚`caxsÙ±‚`a[Ù±‚bmia0Ù±‚`a]Ù±‚aoa.Ù±‚`iset_titleÙ±‚`a(Ù±‚bs1a'Ù±‚bs1vConcise Date FormatterÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`cpltÙ±‚aoa.Ù±‚`dshowÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚bc1xM#############################################################################Ù±‚`a
Ù±‚bc1xK# If all calls to axes that have dates are to be made using this converter,Ù±‚`a
Ù±‚bc1xG# it is probably most convenient to use the units registry where you doÙ±‚`a
Ù±‚bc1j# imports:Ù±‚`a
Ù±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnneunitsÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnnfmunitsÙ±‚`a
Ù±‚`iconverterÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`fmdatesÙ±‚aoa.Ù±‚`tConciseDateConverterÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`fmunitsÙ±‚aoa.Ù±‚`hregistryÙ±‚`a[Ù±‚`bnpÙ±‚aoa.Ù±‚`jdatetime64Ù±‚`a]Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`iconverterÙ±‚`a
Ù±‚`fmunitsÙ±‚aoa.Ù±‚`hregistryÙ±‚`a[Ù±‚`hdatetimeÙ±‚aoa.Ù±‚`ddateÙ±‚`a]Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`iconverterÙ±‚`a
Ù±‚`fmunitsÙ±‚aoa.Ù±‚`hregistryÙ±‚`a[Ù±‚`hdatetimeÙ±‚aoa.Ù±‚`hdatetimeÙ±‚`a]Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`iconverterÙ±‚`a
Ù±‚`a
Ù±‚`cfigÙ±‚`a,Ù±‚`a Ù±‚`caxsÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cpltÙ±‚aoa.Ù±‚`hsubplotsÙ±‚`a(Ù±‚bmia3Ù±‚`a,Ù±‚`a Ù±‚bmia1Ù±‚`a,Ù±‚`a Ù±‚`gfigsizeÙ±‚aoa=Ù±‚`a(Ù±‚bmia6Ù±‚`a,Ù±‚`a Ù±‚bmia6Ù±‚`a)Ù±‚`a,Ù±‚`a Ù±‚`rconstrained_layoutÙ±‚aoa=Ù±‚bkcdTrueÙ±‚`a)Ù±‚`a
Ù±‚akcforÙ±‚`a Ù±‚`bnnÙ±‚`a,Ù±‚`a Ù±‚`baxÙ±‚`a Ù±‚bowbinÙ±‚`a Ù±‚bnbienumerateÙ±‚`a(Ù±‚`caxsÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`d    Ù±‚`baxÙ±‚aoa.Ù±‚`dplotÙ±‚`a(Ù±‚`edatesÙ±‚`a,Ù±‚`a Ù±‚`ayÙ±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`baxÙ±‚aoa.Ù±‚`hset_xlimÙ±‚`a(Ù±‚`dlimsÙ±‚`a[Ù±‚`bnnÙ±‚`a]Ù±‚`a)Ù±‚`a
Ù±‚`caxsÙ±‚`a[Ù±‚bmia0Ù±‚`a]Ù±‚aoa.Ù±‚`iset_titleÙ±‚`a(Ù±‚bs1a'Ù±‚bs1vConcise Date FormatterÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`cpltÙ±‚aoa.Ù±‚`dshowÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚bc1xM#############################################################################Ù±‚`a
Ù±‚bc1x# Localization of date formatsÙ±‚`a
Ù±‚bc1x# ============================Ù±‚`a
Ù±‚bc1a#Ù±‚`a
Ù±‚bc1xL# Dates formats can be localized if the default formats are not desirable byÙ±‚`a
Ù±‚bc1x-# manipulating one of three lists of strings.Ù±‚`a
Ù±‚bc1a#Ù±‚`a
Ù±‚bc1xJ# The ``formatter.formats`` list of formats is for the normal tick labels,Ù±‚`a
Ù±‚bc1xE# There are six levels: years, months, days, hours, minutes, seconds.Ù±‚`a
Ù±‚bc1xJ# The ``formatter.offset_formats`` is how the "offset" string on the rightÙ±‚`a
Ù±‚bc1xL# of the axis is formatted.  This is usually much more verbose than the tickÙ±‚`a
Ù±‚bc1xH# labels. Finally, the ``formatter.zero_formats`` are the formats of theÙ±‚`a
Ù±‚bc1xM# ticks that are "zeros".  These are tick values that are either the first ofÙ±‚`a
Ù±‚bc1xJ# the year, month, or day of month, or the zeroth hour, minute, or second.Ù±‚`a
Ù±‚bc1x-# These are usually the same as the format ofÙ±‚`a
Ù±‚bc1xM# the ticks a level above.  For example if the axis limits mean the ticks areÙ±‚`a
Ù±‚bc1xI# mostly days, then we label 1 Mar 2005 simply with a "Mar".  If the axisÙ±‚`a
Ù±‚bc1xB# limits are mostly hours, we label Feb 4 00:00 as simply "Feb-4".Ù±‚`a
Ù±‚bc1a#Ù±‚`a
Ù±‚bc1xL# Note that these format lists can also be passed to `.ConciseDateFormatter`Ù±‚`a
Ù±‚bc1x # as optional keyword arguments.Ù±‚`a
Ù±‚bc1a#Ù±‚`a
Ù±‚bc1xF# Here we modify the labels to be "day month year", instead of the ISOÙ±‚`a
Ù±‚bc1s# "year month day":Ù±‚`a
Ù±‚`a
Ù±‚`cfigÙ±‚`a,Ù±‚`a Ù±‚`caxsÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cpltÙ±‚aoa.Ù±‚`hsubplotsÙ±‚`a(Ù±‚bmia3Ù±‚`a,Ù±‚`a Ù±‚bmia1Ù±‚`a,Ù±‚`a Ù±‚`rconstrained_layoutÙ±‚aoa=Ù±‚bkcdTrueÙ±‚`a,Ù±‚`a Ù±‚`gfigsizeÙ±‚aoa=Ù±‚`a(Ù±‚bmia6Ù±‚`a,Ù±‚`a Ù±‚bmia6Ù±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚akcforÙ±‚`a Ù±‚`bnnÙ±‚`a,Ù±‚`a Ù±‚`baxÙ±‚`a Ù±‚bowbinÙ±‚`a Ù±‚bnbienumerateÙ±‚`a(Ù±‚`caxsÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`d    Ù±‚`glocatorÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`fmdatesÙ±‚aoa.Ù±‚`oAutoDateLocatorÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`iformatterÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`fmdatesÙ±‚aoa.Ù±‚`tConciseDateFormatterÙ±‚`a(Ù±‚`glocatorÙ±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`iformatterÙ±‚aoa.Ù±‚`gformatsÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`a[Ù±‚bs1a'Ù±‚bs1a%Ù±‚bs1ayÙ±‚bs1a'Ù±‚`a,Ù±‚`b  Ù±‚bc1x# ticks are mostly yearsÙ±‚`a
Ù±‚`x                         Ù±‚bs1a'Ù±‚bs1a%Ù±‚bs1abÙ±‚bs1a'Ù±‚`a,Ù±‚`g       Ù±‚bc1x# ticks are mostly monthsÙ±‚`a
Ù±‚`x                         Ù±‚bs1a'Ù±‚bsib%dÙ±‚bs1a'Ù±‚`a,Ù±‚`g       Ù±‚bc1w# ticks are mostly daysÙ±‚`a
Ù±‚`x                         Ù±‚bs1a'Ù±‚bs1a%Ù±‚bs1bH:Ù±‚bs1a%Ù±‚bs1aMÙ±‚bs1a'Ù±‚`a,Ù±‚`d    Ù±‚bc1e# hrsÙ±‚`a
Ù±‚`x                         Ù±‚bs1a'Ù±‚bs1a%Ù±‚bs1bH:Ù±‚bs1a%Ù±‚bs1aMÙ±‚bs1a'Ù±‚`a,Ù±‚`d    Ù±‚bc1e# minÙ±‚`a
Ù±‚`x                         Ù±‚bs1a'Ù±‚bs1a%Ù±‚bs1bS.Ù±‚bsib%fÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`a]Ù±‚`b  Ù±‚bc1f# secsÙ±‚`a
Ù±‚`d    Ù±‚bc1x*# these are mostly just the level above...Ù±‚`a
Ù±‚`d    Ù±‚`iformatterÙ±‚aoa.Ù±‚`lzero_formatsÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`a[Ù±‚bs1a'Ù±‚bs1a'Ù±‚`a]Ù±‚`a Ù±‚aoa+Ù±‚`a Ù±‚`iformatterÙ±‚aoa.Ù±‚`gformatsÙ±‚`a[Ù±‚`a:Ù±‚aoa-Ù±‚bmia1Ù±‚`a]Ù±‚`a
Ù±‚`d    Ù±‚bc1xD# ...except for ticks that are mostly hours, then it is nice to haveÙ±‚`a
Ù±‚`d    Ù±‚bc1l# month-day:Ù±‚`a
Ù±‚`d    Ù±‚`iformatterÙ±‚aoa.Ù±‚`lzero_formatsÙ±‚`a[Ù±‚bmia3Ù±‚`a]Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bs1a'Ù±‚bsib%dÙ±‚bs1a-Ù±‚bs1a%Ù±‚bs1abÙ±‚bs1a'Ù±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚`iformatterÙ±‚aoa.Ù±‚`noffset_formatsÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`a[Ù±‚bs1a'Ù±‚bs1a'Ù±‚`a,Ù±‚`a
Ù±‚`x                                 Ù±‚bs1a'Ù±‚bs1a%Ù±‚bs1aYÙ±‚bs1a'Ù±‚`a,Ù±‚`a
Ù±‚`x                                 Ù±‚bs1a'Ù±‚bs1a%Ù±‚bs1bb Ù±‚bs1a%Ù±‚bs1aYÙ±‚bs1a'Ù±‚`a,Ù±‚`a
Ù±‚`x                                 Ù±‚bs1a'Ù±‚bsib%dÙ±‚bs1a Ù±‚bs1a%Ù±‚bs1bb Ù±‚bs1a%Ù±‚bs1aYÙ±‚bs1a'Ù±‚`a,Ù±‚`a
Ù±‚`x                                 Ù±‚bs1a'Ù±‚bsib%dÙ±‚bs1a Ù±‚bs1a%Ù±‚bs1bb Ù±‚bs1a%Ù±‚bs1aYÙ±‚bs1a'Ù±‚`a,Ù±‚`a
Ù±‚`x                                 Ù±‚bs1a'Ù±‚bsib%dÙ±‚bs1a Ù±‚bs1a%Ù±‚bs1bb Ù±‚bs1a%Ù±‚bs1bY Ù±‚bs1a%Ù±‚bs1bH:Ù±‚bs1a%Ù±‚bs1aMÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`a]Ù±‚`a
Ù±‚`d    Ù±‚`baxÙ±‚aoa.Ù±‚`exaxisÙ±‚aoa.Ù±‚`qset_major_locatorÙ±‚`a(Ù±‚`glocatorÙ±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`baxÙ±‚aoa.Ù±‚`exaxisÙ±‚aoa.Ù±‚`sset_major_formatterÙ±‚`a(Ù±‚`iformatterÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚`baxÙ±‚aoa.Ù±‚`dplotÙ±‚`a(Ù±‚`edatesÙ±‚`a,Ù±‚`a Ù±‚`ayÙ±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`baxÙ±‚aoa.Ù±‚`hset_xlimÙ±‚`a(Ù±‚`dlimsÙ±‚`a[Ù±‚`bnnÙ±‚`a]Ù±‚`a)Ù±‚`a
Ù±‚`caxsÙ±‚`a[Ù±‚bmia0Ù±‚`a]Ù±‚aoa.Ù±‚`iset_titleÙ±‚`a(Ù±‚bs1a'Ù±‚bs1vConcise Date FormatterÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`cpltÙ±‚aoa.Ù±‚`dshowÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚bc1xM#############################################################################Ù±‚`a
Ù±‚bc1x+# Registering a converter with localizationÙ±‚`a
Ù±‚bc1x+# =========================================Ù±‚`a
Ù±‚bc1a#Ù±‚`a
Ù±‚bc1xM# `.ConciseDateFormatter` doesn't have rcParams entries, but localization canÙ±‚`a
Ù±‚bc1xM# be accomplished by passing keyword arguments to `.ConciseDateConverter` andÙ±‚`a
Ù±‚bc1xA# registering the datatypes you will use with the units registry:Ù±‚`a
Ù±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnhdatetimeÙ±‚`a
Ù±‚`a
Ù±‚`gformatsÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`a[Ù±‚bs1a'Ù±‚bs1a%Ù±‚bs1ayÙ±‚bs1a'Ù±‚`a,Ù±‚`j          Ù±‚bc1x# ticks are mostly yearsÙ±‚`a
Ù±‚`k           Ù±‚bs1a'Ù±‚bs1a%Ù±‚bs1abÙ±‚bs1a'Ù±‚`a,Ù±‚`e     Ù±‚bc1x# ticks are mostly monthsÙ±‚`a
Ù±‚`k           Ù±‚bs1a'Ù±‚bsib%dÙ±‚bs1a'Ù±‚`a,Ù±‚`e     Ù±‚bc1w# ticks are mostly daysÙ±‚`a
Ù±‚`k           Ù±‚bs1a'Ù±‚bs1a%Ù±‚bs1bH:Ù±‚bs1a%Ù±‚bs1aMÙ±‚bs1a'Ù±‚`a,Ù±‚`b  Ù±‚bc1e# hrsÙ±‚`a
Ù±‚`k           Ù±‚bs1a'Ù±‚bs1a%Ù±‚bs1bH:Ù±‚bs1a%Ù±‚bs1aMÙ±‚bs1a'Ù±‚`a,Ù±‚`b  Ù±‚bc1e# minÙ±‚`a
Ù±‚`k           Ù±‚bs1a'Ù±‚bs1a%Ù±‚bs1bS.Ù±‚bsib%fÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`a]Ù±‚`b  Ù±‚bc1f# secsÙ±‚`a
Ù±‚bc1x7# these can be the same, except offset by one level....Ù±‚`a
Ù±‚`lzero_formatsÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`a[Ù±‚bs1a'Ù±‚bs1a'Ù±‚`a]Ù±‚`a Ù±‚aoa+Ù±‚`a Ù±‚`gformatsÙ±‚`a[Ù±‚`a:Ù±‚aoa-Ù±‚bmia1Ù±‚`a]Ù±‚`a
Ù±‚bc1xL# ...except for ticks that are mostly hours, then its nice to have month-dayÙ±‚`a
Ù±‚`lzero_formatsÙ±‚`a[Ù±‚bmia3Ù±‚`a]Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bs1a'Ù±‚bsib%dÙ±‚bs1a-Ù±‚bs1a%Ù±‚bs1abÙ±‚bs1a'Ù±‚`a
Ù±‚`noffset_formatsÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`a[Ù±‚bs1a'Ù±‚bs1a'Ù±‚`a,Ù±‚`a
Ù±‚`r                  Ù±‚bs1a'Ù±‚bs1a%Ù±‚bs1aYÙ±‚bs1a'Ù±‚`a,Ù±‚`a
Ù±‚`r                  Ù±‚bs1a'Ù±‚bs1a%Ù±‚bs1bb Ù±‚bs1a%Ù±‚bs1aYÙ±‚bs1a'Ù±‚`a,Ù±‚`a
Ù±‚`r                  Ù±‚bs1a'Ù±‚bsib%dÙ±‚bs1a Ù±‚bs1a%Ù±‚bs1bb Ù±‚bs1a%Ù±‚bs1aYÙ±‚bs1a'Ù±‚`a,Ù±‚`a
Ù±‚`r                  Ù±‚bs1a'Ù±‚bsib%dÙ±‚bs1a Ù±‚bs1a%Ù±‚bs1bb Ù±‚bs1a%Ù±‚bs1aYÙ±‚bs1a'Ù±‚`a,Ù±‚`a
Ù±‚`r                  Ù±‚bs1a'Ù±‚bsib%dÙ±‚bs1a Ù±‚bs1a%Ù±‚bs1bb Ù±‚bs1a%Ù±‚bs1bY Ù±‚bs1a%Ù±‚bs1bH:Ù±‚bs1a%Ù±‚bs1aMÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`a]Ù±‚`a
Ù±‚`a
Ù±‚`iconverterÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`fmdatesÙ±‚aoa.Ù±‚`tConciseDateConverterÙ±‚`a(Ù±‚`a
Ù±‚`d    Ù±‚`gformatsÙ±‚aoa=Ù±‚`gformatsÙ±‚`a,Ù±‚`a Ù±‚`lzero_formatsÙ±‚aoa=Ù±‚`lzero_formatsÙ±‚`a,Ù±‚`a Ù±‚`noffset_formatsÙ±‚aoa=Ù±‚`noffset_formatsÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`fmunitsÙ±‚aoa.Ù±‚`hregistryÙ±‚`a[Ù±‚`bnpÙ±‚aoa.Ù±‚`jdatetime64Ù±‚`a]Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`iconverterÙ±‚`a
Ù±‚`fmunitsÙ±‚aoa.Ù±‚`hregistryÙ±‚`a[Ù±‚`hdatetimeÙ±‚aoa.Ù±‚`ddateÙ±‚`a]Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`iconverterÙ±‚`a
Ù±‚`fmunitsÙ±‚aoa.Ù±‚`hregistryÙ±‚`a[Ù±‚`hdatetimeÙ±‚aoa.Ù±‚`hdatetimeÙ±‚`a]Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`iconverterÙ±‚`a
Ù±‚`a
Ù±‚`cfigÙ±‚`a,Ù±‚`a Ù±‚`caxsÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cpltÙ±‚aoa.Ù±‚`hsubplotsÙ±‚`a(Ù±‚bmia3Ù±‚`a,Ù±‚`a Ù±‚bmia1Ù±‚`a,Ù±‚`a Ù±‚`rconstrained_layoutÙ±‚aoa=Ù±‚bkcdTrueÙ±‚`a,Ù±‚`a Ù±‚`gfigsizeÙ±‚aoa=Ù±‚`a(Ù±‚bmia6Ù±‚`a,Ù±‚`a Ù±‚bmia6Ù±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚akcforÙ±‚`a Ù±‚`bnnÙ±‚`a,Ù±‚`a Ù±‚`baxÙ±‚`a Ù±‚bowbinÙ±‚`a Ù±‚bnbienumerateÙ±‚`a(Ù±‚`caxsÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`d    Ù±‚`baxÙ±‚aoa.Ù±‚`dplotÙ±‚`a(Ù±‚`edatesÙ±‚`a,Ù±‚`a Ù±‚`ayÙ±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`baxÙ±‚aoa.Ù±‚`hset_xlimÙ±‚`a(Ù±‚`dlimsÙ±‚`a[Ù±‚`bnnÙ±‚`a]Ù±‚`a)Ù±‚`a
Ù±‚`caxsÙ±‚`a[Ù±‚bmia0Ù±‚`a]Ù±‚aoa.Ù±‚`iset_titleÙ±‚`a(Ù±‚bs1a'Ù±‚bs1x-Concise Date Formatter registered non-defaultÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`cpltÙ±‚aoa.Ù±‚`dshowÙ±‚`a(Ù±‚`a)Ù±‚`a
`dNoneö