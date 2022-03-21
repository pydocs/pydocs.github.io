��������>���bsdy�"""
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

"""���`a
���bknfimport���`a ���bnnhdatetime���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnedates���`a ���akbas���`a ���bnnfmdates���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���`a
���bc1xM#############################################################################���`a
���bc1x# First, the default formatter.���`a
���`a
���`dbase���`a ���aoa=���`a ���`hdatetime���aoa.���`hdatetime���`a(���bmid2005���`a,���`a ���bmia2���`a,���`a ���bmia1���`a)���`a
���`edates���`a ���aoa=���`a ���`a[���`dbase���`a ���aoa+���`a ���`hdatetime���aoa.���`itimedelta���`a(���`ehours���aoa=���`a(���bmia2���`a ���aoa*���`a ���`ai���`a)���`a)���`a ���akcfor���`a ���`ai���`a ���bowbin���`a ���bnberange���`a(���bmic732���`a)���`a]���`a
���`aN���`a ���aoa=���`a ���bnbclen���`a(���`edates���`a)���`a
���`bnp���aoa.���`frandom���aoa.���`dseed���`a(���bmih19680801���`a)���`a
���`ay���`a ���aoa=���`a ���`bnp���aoa.���`fcumsum���`a(���`bnp���aoa.���`frandom���aoa.���`erandn���`a(���`aN���`a)���`a)���`a
���`a
���`cfig���`a,���`a ���`caxs���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���bmia3���`a,���`a ���bmia1���`a,���`a ���`rconstrained_layout���aoa=���bkcdTrue���`a,���`a ���`gfigsize���aoa=���`a(���bmia6���`a,���`a ���bmia6���`a)���`a)���`a
���`dlims���`a ���aoa=���`a ���`a[���`a(���`bnp���aoa.���`jdatetime64���`a(���bs1a'���bs1g2005-02���bs1a'���`a)���`a,���`a ���`bnp���aoa.���`jdatetime64���`a(���bs1a'���bs1g2005-04���bs1a'���`a)���`a)���`a,���`a
���`h        ���`a(���`bnp���aoa.���`jdatetime64���`a(���bs1a'���bs1j2005-02-03���bs1a'���`a)���`a,���`a ���`bnp���aoa.���`jdatetime64���`a(���bs1a'���bs1j2005-02-15���bs1a'���`a)���`a)���`a,���`a
���`h        ���`a(���`bnp���aoa.���`jdatetime64���`a(���bs1a'���bs1p2005-02-03 11:00���bs1a'���`a)���`a,���`a ���`bnp���aoa.���`jdatetime64���`a(���bs1a'���bs1p2005-02-04 13:20���bs1a'���`a)���`a)���`a]���`a
���akcfor���`a ���`bnn���`a,���`a ���`bax���`a ���bowbin���`a ���bnbienumerate���`a(���`caxs���`a)���`a:���`a
���`d    ���`bax���aoa.���`dplot���`a(���`edates���`a,���`a ���`ay���`a)���`a
���`d    ���`bax���aoa.���`hset_xlim���`a(���`dlims���`a[���`bnn���`a]���`a)���`a
���`d    ���bc1r# rotate_labels...���`a
���`d    ���akcfor���`a ���`elabel���`a ���bowbin���`a ���`bax���aoa.���`oget_xticklabels���`a(���`a)���`a:���`a
���`h        ���`elabel���aoa.���`lset_rotation���`a(���bmib40���`a)���`a
���`h        ���`elabel���aoa.���`wset_horizontalalignment���`a(���bs1a'���bs1eright���bs1a'���`a)���`a
���`caxs���`a[���bmia0���`a]���aoa.���`iset_title���`a(���bs1a'���bs1vDefault Date Formatter���bs1a'���`a)���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
���`a
���bc1xM#############################################################################���`a
���bc1xG# The default date formatter is quite verbose, so we have the option of���`a
���bc1xB# using `~.dates.ConciseDateFormatter`, as shown below.  Note that���`a
���bc1xJ# for this example the labels do not need to be rotated as they do for the���`a
���bc1x@# default formatter because the labels are as small as possible.���`a
���`a
���`cfig���`a,���`a ���`caxs���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���bmia3���`a,���`a ���bmia1���`a,���`a ���`rconstrained_layout���aoa=���bkcdTrue���`a,���`a ���`gfigsize���aoa=���`a(���bmia6���`a,���`a ���bmia6���`a)���`a)���`a
���akcfor���`a ���`bnn���`a,���`a ���`bax���`a ���bowbin���`a ���bnbienumerate���`a(���`caxs���`a)���`a:���`a
���`d    ���`glocator���`a ���aoa=���`a ���`fmdates���aoa.���`oAutoDateLocator���`a(���`hminticks���aoa=���bmia3���`a,���`a ���`hmaxticks���aoa=���bmia7���`a)���`a
���`d    ���`iformatter���`a ���aoa=���`a ���`fmdates���aoa.���`tConciseDateFormatter���`a(���`glocator���`a)���`a
���`d    ���`bax���aoa.���`exaxis���aoa.���`qset_major_locator���`a(���`glocator���`a)���`a
���`d    ���`bax���aoa.���`exaxis���aoa.���`sset_major_formatter���`a(���`iformatter���`a)���`a
���`a
���`d    ���`bax���aoa.���`dplot���`a(���`edates���`a,���`a ���`ay���`a)���`a
���`d    ���`bax���aoa.���`hset_xlim���`a(���`dlims���`a[���`bnn���`a]���`a)���`a
���`caxs���`a[���bmia0���`a]���aoa.���`iset_title���`a(���bs1a'���bs1vConcise Date Formatter���bs1a'���`a)���`a
���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
���`a
���bc1xM#############################################################################���`a
���bc1xK# If all calls to axes that have dates are to be made using this converter,���`a
���bc1xG# it is probably most convenient to use the units registry where you do���`a
���bc1j# imports:���`a
���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnneunits���`a ���akbas���`a ���bnnfmunits���`a
���`iconverter���`a ���aoa=���`a ���`fmdates���aoa.���`tConciseDateConverter���`a(���`a)���`a
���`fmunits���aoa.���`hregistry���`a[���`bnp���aoa.���`jdatetime64���`a]���`a ���aoa=���`a ���`iconverter���`a
���`fmunits���aoa.���`hregistry���`a[���`hdatetime���aoa.���`ddate���`a]���`a ���aoa=���`a ���`iconverter���`a
���`fmunits���aoa.���`hregistry���`a[���`hdatetime���aoa.���`hdatetime���`a]���`a ���aoa=���`a ���`iconverter���`a
���`a
���`cfig���`a,���`a ���`caxs���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���bmia3���`a,���`a ���bmia1���`a,���`a ���`gfigsize���aoa=���`a(���bmia6���`a,���`a ���bmia6���`a)���`a,���`a ���`rconstrained_layout���aoa=���bkcdTrue���`a)���`a
���akcfor���`a ���`bnn���`a,���`a ���`bax���`a ���bowbin���`a ���bnbienumerate���`a(���`caxs���`a)���`a:���`a
���`d    ���`bax���aoa.���`dplot���`a(���`edates���`a,���`a ���`ay���`a)���`a
���`d    ���`bax���aoa.���`hset_xlim���`a(���`dlims���`a[���`bnn���`a]���`a)���`a
���`caxs���`a[���bmia0���`a]���aoa.���`iset_title���`a(���bs1a'���bs1vConcise Date Formatter���bs1a'���`a)���`a
���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
���`a
���bc1xM#############################################################################���`a
���bc1x# Localization of date formats���`a
���bc1x# ============================���`a
���bc1a#���`a
���bc1xL# Dates formats can be localized if the default formats are not desirable by���`a
���bc1x-# manipulating one of three lists of strings.���`a
���bc1a#���`a
���bc1xJ# The ``formatter.formats`` list of formats is for the normal tick labels,���`a
���bc1xE# There are six levels: years, months, days, hours, minutes, seconds.���`a
���bc1xJ# The ``formatter.offset_formats`` is how the "offset" string on the right���`a
���bc1xL# of the axis is formatted.  This is usually much more verbose than the tick���`a
���bc1xH# labels. Finally, the ``formatter.zero_formats`` are the formats of the���`a
���bc1xM# ticks that are "zeros".  These are tick values that are either the first of���`a
���bc1xJ# the year, month, or day of month, or the zeroth hour, minute, or second.���`a
���bc1x-# These are usually the same as the format of���`a
���bc1xM# the ticks a level above.  For example if the axis limits mean the ticks are���`a
���bc1xI# mostly days, then we label 1 Mar 2005 simply with a "Mar".  If the axis���`a
���bc1xB# limits are mostly hours, we label Feb 4 00:00 as simply "Feb-4".���`a
���bc1a#���`a
���bc1xL# Note that these format lists can also be passed to `.ConciseDateFormatter`���`a
���bc1x # as optional keyword arguments.���`a
���bc1a#���`a
���bc1xF# Here we modify the labels to be "day month year", instead of the ISO���`a
���bc1s# "year month day":���`a
���`a
���`cfig���`a,���`a ���`caxs���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���bmia3���`a,���`a ���bmia1���`a,���`a ���`rconstrained_layout���aoa=���bkcdTrue���`a,���`a ���`gfigsize���aoa=���`a(���bmia6���`a,���`a ���bmia6���`a)���`a)���`a
���`a
���akcfor���`a ���`bnn���`a,���`a ���`bax���`a ���bowbin���`a ���bnbienumerate���`a(���`caxs���`a)���`a:���`a
���`d    ���`glocator���`a ���aoa=���`a ���`fmdates���aoa.���`oAutoDateLocator���`a(���`a)���`a
���`d    ���`iformatter���`a ���aoa=���`a ���`fmdates���aoa.���`tConciseDateFormatter���`a(���`glocator���`a)���`a
���`d    ���`iformatter���aoa.���`gformats���`a ���aoa=���`a ���`a[���bs1a'���bs1a%���bs1ay���bs1a'���`a,���`b  ���bc1x# ticks are mostly years���`a
���`x                         ���bs1a'���bs1a%���bs1ab���bs1a'���`a,���`g       ���bc1x# ticks are mostly months���`a
���`x                         ���bs1a'���bsib%d���bs1a'���`a,���`g       ���bc1w# ticks are mostly days���`a
���`x                         ���bs1a'���bs1a%���bs1bH:���bs1a%���bs1aM���bs1a'���`a,���`d    ���bc1e# hrs���`a
���`x                         ���bs1a'���bs1a%���bs1bH:���bs1a%���bs1aM���bs1a'���`a,���`d    ���bc1e# min���`a
���`x                         ���bs1a'���bs1a%���bs1bS.���bsib%f���bs1a'���`a,���`a ���`a]���`b  ���bc1f# secs���`a
���`d    ���bc1x*# these are mostly just the level above...���`a
���`d    ���`iformatter���aoa.���`lzero_formats���`a ���aoa=���`a ���`a[���bs1a'���bs1a'���`a]���`a ���aoa+���`a ���`iformatter���aoa.���`gformats���`a[���`a:���aoa-���bmia1���`a]���`a
���`d    ���bc1xD# ...except for ticks that are mostly hours, then it is nice to have���`a
���`d    ���bc1l# month-day:���`a
���`d    ���`iformatter���aoa.���`lzero_formats���`a[���bmia3���`a]���`a ���aoa=���`a ���bs1a'���bsib%d���bs1a-���bs1a%���bs1ab���bs1a'���`a
���`a
���`d    ���`iformatter���aoa.���`noffset_formats���`a ���aoa=���`a ���`a[���bs1a'���bs1a'���`a,���`a
���`x                                 ���bs1a'���bs1a%���bs1aY���bs1a'���`a,���`a
���`x                                 ���bs1a'���bs1a%���bs1bb ���bs1a%���bs1aY���bs1a'���`a,���`a
���`x                                 ���bs1a'���bsib%d���bs1a ���bs1a%���bs1bb ���bs1a%���bs1aY���bs1a'���`a,���`a
���`x                                 ���bs1a'���bsib%d���bs1a ���bs1a%���bs1bb ���bs1a%���bs1aY���bs1a'���`a,���`a
���`x                                 ���bs1a'���bsib%d���bs1a ���bs1a%���bs1bb ���bs1a%���bs1bY ���bs1a%���bs1bH:���bs1a%���bs1aM���bs1a'���`a,���`a ���`a]���`a
���`d    ���`bax���aoa.���`exaxis���aoa.���`qset_major_locator���`a(���`glocator���`a)���`a
���`d    ���`bax���aoa.���`exaxis���aoa.���`sset_major_formatter���`a(���`iformatter���`a)���`a
���`a
���`d    ���`bax���aoa.���`dplot���`a(���`edates���`a,���`a ���`ay���`a)���`a
���`d    ���`bax���aoa.���`hset_xlim���`a(���`dlims���`a[���`bnn���`a]���`a)���`a
���`caxs���`a[���bmia0���`a]���aoa.���`iset_title���`a(���bs1a'���bs1vConcise Date Formatter���bs1a'���`a)���`a
���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
���`a
���bc1xM#############################################################################���`a
���bc1x+# Registering a converter with localization���`a
���bc1x+# =========================================���`a
���bc1a#���`a
���bc1xM# `.ConciseDateFormatter` doesn't have rcParams entries, but localization can���`a
���bc1xM# be accomplished by passing keyword arguments to `.ConciseDateConverter` and���`a
���bc1xA# registering the datatypes you will use with the units registry:���`a
���`a
���bknfimport���`a ���bnnhdatetime���`a
���`a
���`gformats���`a ���aoa=���`a ���`a[���bs1a'���bs1a%���bs1ay���bs1a'���`a,���`j          ���bc1x# ticks are mostly years���`a
���`k           ���bs1a'���bs1a%���bs1ab���bs1a'���`a,���`e     ���bc1x# ticks are mostly months���`a
���`k           ���bs1a'���bsib%d���bs1a'���`a,���`e     ���bc1w# ticks are mostly days���`a
���`k           ���bs1a'���bs1a%���bs1bH:���bs1a%���bs1aM���bs1a'���`a,���`b  ���bc1e# hrs���`a
���`k           ���bs1a'���bs1a%���bs1bH:���bs1a%���bs1aM���bs1a'���`a,���`b  ���bc1e# min���`a
���`k           ���bs1a'���bs1a%���bs1bS.���bsib%f���bs1a'���`a,���`a ���`a]���`b  ���bc1f# secs���`a
���bc1x7# these can be the same, except offset by one level....���`a
���`lzero_formats���`a ���aoa=���`a ���`a[���bs1a'���bs1a'���`a]���`a ���aoa+���`a ���`gformats���`a[���`a:���aoa-���bmia1���`a]���`a
���bc1xL# ...except for ticks that are mostly hours, then its nice to have month-day���`a
���`lzero_formats���`a[���bmia3���`a]���`a ���aoa=���`a ���bs1a'���bsib%d���bs1a-���bs1a%���bs1ab���bs1a'���`a
���`noffset_formats���`a ���aoa=���`a ���`a[���bs1a'���bs1a'���`a,���`a
���`r                  ���bs1a'���bs1a%���bs1aY���bs1a'���`a,���`a
���`r                  ���bs1a'���bs1a%���bs1bb ���bs1a%���bs1aY���bs1a'���`a,���`a
���`r                  ���bs1a'���bsib%d���bs1a ���bs1a%���bs1bb ���bs1a%���bs1aY���bs1a'���`a,���`a
���`r                  ���bs1a'���bsib%d���bs1a ���bs1a%���bs1bb ���bs1a%���bs1aY���bs1a'���`a,���`a
���`r                  ���bs1a'���bsib%d���bs1a ���bs1a%���bs1bb ���bs1a%���bs1bY ���bs1a%���bs1bH:���bs1a%���bs1aM���bs1a'���`a,���`a ���`a]���`a
���`a
���`iconverter���`a ���aoa=���`a ���`fmdates���aoa.���`tConciseDateConverter���`a(���`a
���`d    ���`gformats���aoa=���`gformats���`a,���`a ���`lzero_formats���aoa=���`lzero_formats���`a,���`a ���`noffset_formats���aoa=���`noffset_formats���`a)���`a
���`a
���`fmunits���aoa.���`hregistry���`a[���`bnp���aoa.���`jdatetime64���`a]���`a ���aoa=���`a ���`iconverter���`a
���`fmunits���aoa.���`hregistry���`a[���`hdatetime���aoa.���`ddate���`a]���`a ���aoa=���`a ���`iconverter���`a
���`fmunits���aoa.���`hregistry���`a[���`hdatetime���aoa.���`hdatetime���`a]���`a ���aoa=���`a ���`iconverter���`a
���`a
���`cfig���`a,���`a ���`caxs���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���bmia3���`a,���`a ���bmia1���`a,���`a ���`rconstrained_layout���aoa=���bkcdTrue���`a,���`a ���`gfigsize���aoa=���`a(���bmia6���`a,���`a ���bmia6���`a)���`a)���`a
���akcfor���`a ���`bnn���`a,���`a ���`bax���`a ���bowbin���`a ���bnbienumerate���`a(���`caxs���`a)���`a:���`a
���`d    ���`bax���aoa.���`dplot���`a(���`edates���`a,���`a ���`ay���`a)���`a
���`d    ���`bax���aoa.���`hset_xlim���`a(���`dlims���`a[���`bnn���`a]���`a)���`a
���`caxs���`a[���bmia0���`a]���aoa.���`iset_title���`a(���bs1a'���bs1x-Concise Date Formatter registered non-default���bs1a'���`a)���`a
���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
`dNone�