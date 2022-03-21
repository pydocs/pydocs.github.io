�����������bsdy{"""
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
"""���`a
���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnecbook���`a ���akbas���`a ���bnnecbook���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnedates���`a ���akbas���`a ���bnnedates���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfticker���`a ���akbas���`a ���bnnfticker���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���`a
���bc1x0# load some financial data; Google's stock price���`a
���`ar���`a ���aoa=���`a ���`a(���`ecbook���aoa.���`oget_sample_data���`a(���bs1a'���bs1hgoog.npz���bs1a'���`a,���`a ���`gnp_load���aoa=���bkcdTrue���`a)���`a[���bs1a'���bs1jprice_data���bs1a'���`a]���`a
���`e     ���aoa.���`dview���`a(���`bnp���aoa.���`hrecarray���`a)���`a)���`a
���`ar���`a ���aoa=���`a ���`ar���`a[���aoa-���bmic250���`a:���`a]���`b  ���bc1w# get the last 250 days���`a
���`a
���`cfig���`a,���`a ���`bax���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`a)���`a
���`bax���aoa.���`dplot���`a(���`ar���aoa.���`ddate���`a,���`a ���`ar���aoa.���`iadj_close���`a)���`a
���`a
���`bax���aoa.���`exaxis���aoa.���`qset_major_locator���`a(���`edates���aoa.���`lMonthLocator���`a(���`a)���`a)���`a
���bc1xE# 16 is a slight approximation since months differ in number of days.���`a
���`bax���aoa.���`exaxis���aoa.���`qset_minor_locator���`a(���`edates���aoa.���`lMonthLocator���`a(���`jbymonthday���aoa=���bmib16���`a)���`a)���`a
���`a
���`bax���aoa.���`exaxis���aoa.���`sset_major_formatter���`a(���`fticker���aoa.���`mNullFormatter���`a(���`a)���`a)���`a
���`bax���aoa.���`exaxis���aoa.���`sset_minor_formatter���`a(���`edates���aoa.���`mDateFormatter���`a(���bs1a'���bs1a%���bs1ab���bs1a'���`a)���`a)���`a
���`a
���akcfor���`a ���`dtick���`a ���bowbin���`a ���`bax���aoa.���`exaxis���aoa.���`oget_minor_ticks���`a(���`a)���`a:���`a
���`d    ���`dtick���aoa.���`itick1line���aoa.���`nset_markersize���`a(���bmia0���`a)���`a
���`d    ���`dtick���aoa.���`itick2line���aoa.���`nset_markersize���`a(���bmia0���`a)���`a
���`d    ���`dtick���aoa.���`flabel1���aoa.���`wset_horizontalalignment���`a(���bs1a'���bs1fcenter���bs1a'���`a)���`a
���`a
���`dimid���`a ���aoa=���`a ���bnbclen���`a(���`ar���`a)���`a ���aoa/���aoa/���`a ���bmia2���`a
���`bax���aoa.���`jset_xlabel���`a(���bnbcstr���`a(���`ar���aoa.���`ddate���`a[���`dimid���`a]���aoa.���`ditem���`a(���`a)���aoa.���`dyear���`a)���`a)���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
`dNone�