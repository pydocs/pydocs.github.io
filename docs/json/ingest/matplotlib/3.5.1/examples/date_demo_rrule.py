Ù¯‚Ù´ƒ™Ù±‚bsdyÖ"""
=========================================
Placing date ticks using recurrence rules
=========================================

The `iCalender RFC`_ specifies *recurrence rules* (rrules), that define
date sequences. You can use rrules in Matplotlib to place date ticks.

This example sets custom date ticks on every 5th easter.

See https://dateutil.readthedocs.io/en/stable/rrule.html for help with rrules.

.. _iCalender RFC: https://tools.ietf.org/html/rfc5545
"""Ù±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnnfpyplotÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnncpltÙ±‚`a
Ù±‚bkndfromÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnnedatesÙ±‚`a Ù±‚bknfimportÙ±‚`a Ù±‚`a(Ù±‚`fYEARLYÙ±‚`a,Ù±‚`a Ù±‚`mDateFormatterÙ±‚`a,Ù±‚`a
Ù±‚`x                              Ù±‚`lrrulewrapperÙ±‚`a,Ù±‚`a Ù±‚`lRRuleLocatorÙ±‚`a,Ù±‚`a Ù±‚`fdrangeÙ±‚`a)Ù±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„enumpyÙ „enumpyf1.22.3fmoduleenumpyfmoduleõÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnnbnpÙ±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnhdatetimeÙ±‚`a
Ù±‚`a
Ù±‚bc1x)# Fixing random state for reproducibilityÙ±‚`a
Ù±‚`bnpÙ±‚aoa.Ù±‚`frandomÙ±‚aoa.Ù±‚`dseedÙ±‚`a(Ù±‚bmih19680801Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚bc1w# tick every 5th easterÙ±‚`a
Ù±‚`druleÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`lrrulewrapperÙ±‚`a(Ù±‚`fYEARLYÙ±‚`a,Ù±‚`a Ù±‚`hbyeasterÙ±‚aoa=Ù±‚bmia1Ù±‚`a,Ù±‚`a Ù±‚`hintervalÙ±‚aoa=Ù±‚bmia5Ù±‚`a)Ù±‚`a
Ù±‚`clocÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`lRRuleLocatorÙ±‚`a(Ù±‚`druleÙ±‚`a)Ù±‚`a
Ù±‚`iformatterÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`mDateFormatterÙ±‚`a(Ù±‚bs1a'Ù±‚bs1a%Ù±‚bs1bm/Ù±‚bsib%dÙ±‚bs1a/Ù±‚bs1a%Ù±‚bs1ayÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`edate1Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`hdatetimeÙ±‚aoa.Ù±‚`ddateÙ±‚`a(Ù±‚bmid1952Ù±‚`a,Ù±‚`a Ù±‚bmia1Ù±‚`a,Ù±‚`a Ù±‚bmia1Ù±‚`a)Ù±‚`a
Ù±‚`edate2Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`hdatetimeÙ±‚aoa.Ù±‚`ddateÙ±‚`a(Ù±‚bmid2004Ù±‚`a,Ù±‚`a Ù±‚bmia4Ù±‚`a,Ù±‚`a Ù±‚bmib12Ù±‚`a)Ù±‚`a
Ù±‚`edeltaÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`hdatetimeÙ±‚aoa.Ù±‚`itimedeltaÙ±‚`a(Ù±‚`ddaysÙ±‚aoa=Ù±‚bmic100Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`edatesÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`fdrangeÙ±‚`a(Ù±‚`edate1Ù±‚`a,Ù±‚`a Ù±‚`edate2Ù±‚`a,Ù±‚`a Ù±‚`edeltaÙ±‚`a)Ù±‚`a
Ù±‚`asÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`frandomÙ±‚aoa.Ù±‚`drandÙ±‚`a(Ù±‚bnbclenÙ±‚`a(Ù±‚`edatesÙ±‚`a)Ù±‚`a)Ù±‚`b  Ù±‚bc1x# make up some random y valuesÙ±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚`cfigÙ±‚`a,Ù±‚`a Ù±‚`baxÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cpltÙ±‚aoa.Ù±‚`hsubplotsÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`cpltÙ±‚aoa.Ù±‚`dplotÙ±‚`a(Ù±‚`edatesÙ±‚`a,Ù±‚`a Ù±‚`asÙ±‚`a,Ù±‚`a Ù±‚bs1a'Ù±‚bs1aoÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`exaxisÙ±‚aoa.Ù±‚`qset_major_locatorÙ±‚`a(Ù±‚`clocÙ±‚`a)Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`exaxisÙ±‚aoa.Ù±‚`sset_major_formatterÙ±‚`a(Ù±‚`iformatterÙ±‚`a)Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`exaxisÙ±‚aoa.Ù±‚`oset_tick_paramsÙ±‚`a(Ù±‚`hrotationÙ±‚aoa=Ù±‚bmib30Ù±‚`a,Ù±‚`a Ù±‚`ilabelsizeÙ±‚aoa=Ù±‚bmib10Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`cpltÙ±‚aoa.Ù±‚`dshowÙ±‚`a(Ù±‚`a)Ù±‚`a
`dNoneö