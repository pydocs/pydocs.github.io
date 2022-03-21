��������G���bsdx�"""
=================================
Date tick locators and formatters
=================================

This example illustrates the usage and effect of the various date locators and
formatters.
"""���`a
���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfticker���`a ���akbas���`a ���bnnfticker���`a
���bkndfrom���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnedates���`a ���bknfimport���`a ���`a(���`oAutoDateLocator���`a,���`a ���`kYearLocator���`a,���`a ���`lMonthLocator���`a,���`a
���`x                              ���`jDayLocator���`a,���`a ���`nWeekdayLocator���`a,���`a ���`kHourLocator���`a,���`a
���`x                              ���`mMinuteLocator���`a,���`a ���`mSecondLocator���`a,���`a ���`rMicrosecondLocator���`a,���`a
���`x                              ���`lRRuleLocator���`a,���`a ���`lrrulewrapper���`a,���`a ���`gMONTHLY���`a,���`a
���`x                              ���`bMO���`a,���`a ���`bTU���`a,���`a ���`bWE���`a,���`a ���`bTH���`a,���`a ���`bFR���`a,���`a ���`bSA���`a,���`a ���`bSU���`a,���`a ���`mDateFormatter���`a,���`a
���`x                              ���`qAutoDateFormatter���`a,���`a ���`tConciseDateFormatter���`a)���`a
���`a
���`hlocators���`a ���aoa=���`a ���`a[���`a
���`d    ���`a(���bs1a'���bs1xAutoDateLocator(maxticks=8)���bs1a'���`a,���`a ���bs1a'���bs1j2003-02-01���bs1a'���`a,���`a ���bs1a'���bs1a%���bs1bY-���bs1a%���bs1am���bs1a'���`a)���`a,���`a
���`d    ���`a(���bs1a'���bs1tYearLocator(month=4)���bs1a'���`a,���`a ���bs1a'���bs1j2003-02-01���bs1a'���`a,���`a ���bs1a'���bs1a%���bs1bY-���bs1a%���bs1am���bs1a'���`a)���`a,���`a
���`d    ���`a(���bs1a'���bs1xMonthLocator(bymonth=[4,8,12])���bs1a'���`a,���`a ���bs1a'���bs1j2003-02-01���bs1a'���`a,���`a ���bs1a'���bs1a%���bs1bY-���bs1a%���bs1am���bs1a'���`a)���`a,���`a
���`d    ���`a(���bs1a'���bs1xDayLocator(interval=180)���bs1a'���`a,���`a ���bs1a'���bs1j2003-02-01���bs1a'���`a,���`a ���bs1a'���bs1a%���bs1bY-���bs1a%���bs1bm-���bsib%d���bs1a'���`a)���`a,���`a
���`d    ���`a(���bs1a'���bs1x(WeekdayLocator(byweekday=SU, interval=4)���bs1a'���`a,���`a ���bs1a'���bs1j2000-07-01���bs1a'���`a,���`a ���bs1a'���bsib%a���bs1a ���bs1a%���bs1bY-���bs1a%���bs1bm-���bsib%d���bs1a'���`a)���`a,���`a
���`d    ���`a(���bs1a'���bs1x!HourLocator(byhour=range(0,24,6))���bs1a'���`a,���`a ���bs1a'���bs1j2000-02-04���bs1a'���`a,���`a ���bs1a'���bs1a%���bs1cH h���bs1a'���`a)���`a,���`a
���`d    ���`a(���bs1a'���bs1xMinuteLocator(interval=15)���bs1a'���`a,���`a ���bs1a'���bs1p2000-02-01 02:00���bs1a'���`a,���`a ���bs1a'���bs1a%���bs1bH:���bs1a%���bs1aM���bs1a'���`a)���`a,���`a
���`d    ���`a(���bs1a'���bs1xSecondLocator(bysecond=(0,30))���bs1a'���`a,���`a ���bs1a'���bs1p2000-02-01 00:02���bs1a'���`a,���`a ���bs1a'���bs1a%���bs1bH:���bs1a%���bs1bM:���bs1a%���bs1aS���bs1a'���`a)���`a,���`a
���`d    ���`a(���bs1a'���bs1x!MicrosecondLocator(interval=1000)���bs1a'���`a,���`a ���bs1a'���bs1w2000-02-01 00:00:00.005���bs1a'���`a,���`a ���bs1a'���bs1a%���bs1bS.���bsib%f���bs1a'���`a)���`a,���`a
���`d    ���`a(���bs1a'���bs1x(RRuleLocator(rrulewrapper(freq=MONTHLY, ���bseb\n���bs1xbyweekday=(MO, TU, WE, TH,���bs1a'���`a ���aoa+���`a
���`e     ���bs1a'���bs1s FR), bysetpos=-1))���bs1a'���`a,���`a ���bs1a'���bs1j2000-07-01���bs1a'���`a,���`a ���bs1a'���bs1a%���bs1bY-���bs1a%���bs1bm-���bsib%d���bs1a'���`a)���`a
���`a]���`a
���`a
���`jformatters���`a ���aoa=���`a ���`a[���`a
���`d    ���`a(���bs1a'���bs1x/AutoDateFormatter(ax.xaxis.get_major_locator())���bs1a'���`a)���`a,���`a
���`d    ���`a(���bs1a'���bs1x2ConciseDateFormatter(ax.xaxis.get_major_locator())���bs1a'���`a)���`a,���`a
���`d    ���`a(���bs1a'���bs1nDateFormatter(���bs1a"���bs1a%���bs1bb ���bs1a%���bs1aY���bs1a"���bs1a)���bs1a'���`a)���`a
���`a]���`a
���`a
���`a
���akcdef���`a ���bnfiplot_axis���`a(���`bax���`a,���`a ���`glocator���aoa=���bkcdNone���`a,���`a ���`dxmax���aoa=���bs1a'���bs1j2002-02-01���bs1a'���`a,���`a ���`cfmt���aoa=���bkcdNone���`a,���`a ���`iformatter���aoa=���bkcdNone���`a)���`a:���`a
���`d    ���bsdx;"""Set up common parameters for the Axes in the example."""���`a
���`d    ���`bax���aoa.���`fspines���aoa.���`eright���aoa.���`kset_visible���`a(���bkceFalse���`a)���`a
���`d    ���`bax���aoa.���`fspines���aoa.���`dleft���aoa.���`kset_visible���`a(���bkceFalse���`a)���`a
���`d    ���`bax���aoa.���`fspines���aoa.���`ctop���aoa.���`kset_visible���`a(���bkceFalse���`a)���`a
���`d    ���`bax���aoa.���`eyaxis���aoa.���`qset_major_locator���`a(���`fticker���aoa.���`kNullLocator���`a(���`a)���`a)���`a
���`d    ���`bax���aoa.���`ktick_params���`a(���`ewhich���aoa=���bs1a'���bs1emajor���bs1a'���`a,���`a ���`ewidth���aoa=���bmfd1.00���`a,���`a ���`flength���aoa=���bmia5���`a)���`a
���`d    ���`bax���aoa.���`ktick_params���`a(���`ewhich���aoa=���bs1a'���bs1eminor���bs1a'���`a,���`a ���`ewidth���aoa=���bmfd0.75���`a,���`a ���`flength���aoa=���bmfc2.5���`a)���`a
���`d    ���`bax���aoa.���`hset_xlim���`a(���`bnp���aoa.���`jdatetime64���`a(���bs1a'���bs1j2000-02-01���bs1a'���`a)���`a,���`a ���`bnp���aoa.���`jdatetime64���`a(���`dxmax���`a)���`a)���`a
���`d    ���akbif���`a ���`glocator���`a:���`a
���`h        ���`bax���aoa.���`exaxis���aoa.���`qset_major_locator���`a(���bnbdeval���`a(���`glocator���`a)���`a)���`a
���`h        ���`bax���aoa.���`exaxis���aoa.���`sset_major_formatter���`a(���`mDateFormatter���`a(���`cfmt���`a)���`a)���`a
���`d    ���akdelse���`a:���`a
���`h        ���`bax���aoa.���`exaxis���aoa.���`sset_major_formatter���`a(���bnbdeval���`a(���`iformatter���`a)���`a)���`a
���`d    ���`bax���aoa.���`dtext���`a(���bmfc0.0���`a,���`a ���bmfc0.2���`a,���`a ���`glocator���`a ���bowbor���`a ���`iformatter���`a,���`a ���`itransform���aoa=���`bax���aoa.���`itransAxes���`a,���`a
���`l            ���`hfontsize���aoa=���bmib14���`a,���`a ���`hfontname���aoa=���bs1a'���bs1iMonospace���bs1a'���`a,���`a ���`ecolor���aoa=���bs1a'���bs1htab:blue���bs1a'���`a)���`a
���`a
���`a
���`cfig���`a,���`a ���`bax���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���bnbclen���`a(���`hlocators���`a)���`a,���`a ���bmia1���`a,���`a ���`gfigsize���aoa=���`a(���bmia8���`a,���`a ���bnbclen���`a(���`hlocators���`a)���`a ���aoa*���`a ���bmfb.8���`a)���`a,���`a
���`w                       ���`flayout���aoa=���bs1a'���bs1kconstrained���bs1a'���`a)���`a
���`cfig���aoa.���`hsuptitle���`a(���bs1a'���bs1mDate Locators���bs1a'���`a)���`a
���akcfor���`a ���`ai���`a,���`a ���`cloc���`a ���bowbin���`a ���bnbienumerate���`a(���`hlocators���`a)���`a:���`a
���`d    ���`iplot_axis���`a(���`bax���`a[���`ai���`a]���`a,���`a ���aoa*���`cloc���`a)���`a
���`a
���`cfig���`a,���`a ���`bax���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���bnbclen���`a(���`jformatters���`a)���`a,���`a ���bmia1���`a,���`a ���`gfigsize���aoa=���`a(���bmia8���`a,���`a ���bnbclen���`a(���`jformatters���`a)���`a ���aoa*���`a ���bmfb.8���`a)���`a,���`a
���`w                       ���`flayout���aoa=���bs1a'���bs1kconstrained���bs1a'���`a)���`a
���`cfig���aoa.���`hsuptitle���`a(���bs1a'���bs1oDate Formatters���bs1a'���`a)���`a
���akcfor���`a ���`ai���`a,���`a ���`cfmt���`a ���bowbin���`a ���bnbienumerate���`a(���`jformatters���`a)���`a:���`a
���`d    ���`iplot_axis���`a(���`bax���`a[���`ai���`a]���`a,���`a ���`iformatter���aoa=���`cfmt���`a)���`a
���`a
���`a
���bc1xM#############################################################################���`a
���bc1a#���`a
���bc1x# .. admonition:: References���`a
���bc1a#���`a
���bc1xN#    The use of the following functions, methods, classes and modules is shown���`a
���bc1u#    in this example:���`a
���bc1a#���`a
���bc1x)#    - `matplotlib.dates.AutoDateLocator`���`a
���bc1x%#    - `matplotlib.dates.YearLocator`���`a
���bc1x&#    - `matplotlib.dates.MonthLocator`���`a
���bc1x$#    - `matplotlib.dates.DayLocator`���`a
���bc1x(#    - `matplotlib.dates.WeekdayLocator`���`a
���bc1x%#    - `matplotlib.dates.HourLocator`���`a
���bc1x'#    - `matplotlib.dates.MinuteLocator`���`a
���bc1x'#    - `matplotlib.dates.SecondLocator`���`a
���bc1x,#    - `matplotlib.dates.MicrosecondLocator`���`a
���bc1x&#    - `matplotlib.dates.RRuleLocator`���`a
���bc1x&#    - `matplotlib.dates.rrulewrapper`���`a
���bc1x'#    - `matplotlib.dates.DateFormatter`���`a
���bc1x+#    - `matplotlib.dates.AutoDateFormatter`���`a
���bc1x.#    - `matplotlib.dates.ConciseDateFormatter`���`a
`dNone�