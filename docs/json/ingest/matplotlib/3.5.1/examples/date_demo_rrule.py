�����������bsdy�"""
=========================================
Placing date ticks using recurrence rules
=========================================

The `iCalender RFC`_ specifies *recurrence rules* (rrules), that define
date sequences. You can use rrules in Matplotlib to place date ticks.

This example sets custom date ticks on every 5th easter.

See https://dateutil.readthedocs.io/en/stable/rrule.html for help with rrules.

.. _iCalender RFC: https://tools.ietf.org/html/rfc5545
"""���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���bkndfrom���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnedates���`a ���bknfimport���`a ���`a(���`fYEARLY���`a,���`a ���`mDateFormatter���`a,���`a
���`x                              ���`lrrulewrapper���`a,���`a ���`lRRuleLocator���`a,���`a ���`fdrange���`a)���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���bknfimport���`a ���bnnhdatetime���`a
���`a
���bc1x)# Fixing random state for reproducibility���`a
���`bnp���aoa.���`frandom���aoa.���`dseed���`a(���bmih19680801���`a)���`a
���`a
���`a
���bc1w# tick every 5th easter���`a
���`drule���`a ���aoa=���`a ���`lrrulewrapper���`a(���`fYEARLY���`a,���`a ���`hbyeaster���aoa=���bmia1���`a,���`a ���`hinterval���aoa=���bmia5���`a)���`a
���`cloc���`a ���aoa=���`a ���`lRRuleLocator���`a(���`drule���`a)���`a
���`iformatter���`a ���aoa=���`a ���`mDateFormatter���`a(���bs1a'���bs1a%���bs1bm/���bsib%d���bs1a/���bs1a%���bs1ay���bs1a'���`a)���`a
���`edate1���`a ���aoa=���`a ���`hdatetime���aoa.���`ddate���`a(���bmid1952���`a,���`a ���bmia1���`a,���`a ���bmia1���`a)���`a
���`edate2���`a ���aoa=���`a ���`hdatetime���aoa.���`ddate���`a(���bmid2004���`a,���`a ���bmia4���`a,���`a ���bmib12���`a)���`a
���`edelta���`a ���aoa=���`a ���`hdatetime���aoa.���`itimedelta���`a(���`ddays���aoa=���bmic100���`a)���`a
���`a
���`edates���`a ���aoa=���`a ���`fdrange���`a(���`edate1���`a,���`a ���`edate2���`a,���`a ���`edelta���`a)���`a
���`as���`a ���aoa=���`a ���`bnp���aoa.���`frandom���aoa.���`drand���`a(���bnbclen���`a(���`edates���`a)���`a)���`b  ���bc1x# make up some random y values���`a
���`a
���`a
���`cfig���`a,���`a ���`bax���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`a)���`a
���`cplt���aoa.���`dplot���`a(���`edates���`a,���`a ���`as���`a,���`a ���bs1a'���bs1ao���bs1a'���`a)���`a
���`bax���aoa.���`exaxis���aoa.���`qset_major_locator���`a(���`cloc���`a)���`a
���`bax���aoa.���`exaxis���aoa.���`sset_major_formatter���`a(���`iformatter���`a)���`a
���`bax���aoa.���`exaxis���aoa.���`oset_tick_params���`a(���`hrotation���aoa=���bmib30���`a,���`a ���`ilabelsize���aoa=���bmib10���`a)���`a
���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
`dNone�