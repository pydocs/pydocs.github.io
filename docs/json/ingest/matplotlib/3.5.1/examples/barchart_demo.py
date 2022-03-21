������������bsdy�"""
===================================
Percentiles as horizontal bar chart
===================================

Bar charts are useful for visualizing counts, or summary statistics
with error bars. Also see the :doc:`/gallery/lines_bars_and_markers/barchart`
or the :doc:`/gallery/lines_bars_and_markers/barh` example for simpler versions
of those features.

This example comes from an application in which grade school gym
teachers wanted to be able to show parents how their child did across
a handful of fitness tests, and importantly, relative to how other
children did. To extract the plotting code for demo purposes, we'll
just make up some data for little Johnny Doe.
"""���`a
���`a
���bkndfrom���`a ���bnnkcollections���`a ���bknfimport���`a ���`jnamedtuple���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���`a
���`a
���`gStudent���`a ���aoa=���`a ���`jnamedtuple���`a(���bs1a'���bs1gStudent���bs1a'���`a,���`a ���`a[���bs1a'���bs1dname���bs1a'���`a,���`a ���bs1a'���bs1egrade���bs1a'���`a,���`a ���bs1a'���bs1fgender���bs1a'���`a]���`a)���`a
���`eScore���`a ���aoa=���`a ���`jnamedtuple���`a(���bs1a'���bs1eScore���bs1a'���`a,���`a ���`a[���bs1a'���bs1evalue���bs1a'���`a,���`a ���bs1a'���bs1dunit���bs1a'���`a,���`a ���bs1a'���bs1jpercentile���bs1a'���`a]���`a)���`a
���`a
���`a
���akcdef���`a ���bnfjto_ordinal���`a(���`cnum���`a)���`a:���`a
���`d    ���bsdx?"""Convert an integer to an ordinal string, e.g. 2 -> '2nd'."""���`a
���`d    ���`hsuffixes���`a ���aoa=���`a ���`a{���bnbcstr���`a(���`ai���`a)���`a:���`a ���`av���`a
���`p                ���akcfor���`a ���`ai���`a,���`a ���`av���`a ���bowbin���`a ���bnbienumerate���`a(���`a[���bs1a'���bs1bth���bs1a'���`a,���`a ���bs1a'���bs1bst���bs1a'���`a,���`a ���bs1a'���bs1bnd���bs1a'���`a,���`a ���bs1a'���bs1brd���bs1a'���`a,���`a ���bs1a'���bs1bth���bs1a'���`a,���`a
���`x'                                       ���bs1a'���bs1bth���bs1a'���`a,���`a ���bs1a'���bs1bth���bs1a'���`a,���`a ���bs1a'���bs1bth���bs1a'���`a,���`a ���bs1a'���bs1bth���bs1a'���`a,���`a ���bs1a'���bs1bth���bs1a'���`a]���`a)���`a}���`a
���`d    ���`av���`a ���aoa=���`a ���bnbcstr���`a(���`cnum���`a)���`a
���`d    ���bc1x# special case early teens���`a
���`d    ���akbif���`a ���`av���`a ���bowbin���`a ���`a{���bs1a'���bs1b11���bs1a'���`a,���`a ���bs1a'���bs1b12���bs1a'���`a,���`a ���bs1a'���bs1b13���bs1a'���`a}���`a:���`a
���`h        ���akfreturn���`a ���`av���`a ���aoa+���`a ���bs1a'���bs1bth���bs1a'���`a
���`d    ���akfreturn���`a ���`av���`a ���aoa+���`a ���`hsuffixes���`a[���`av���`a[���aoa-���bmia1���`a]���`a]���`a
���`a
���`a
���akcdef���`a ���bnflformat_score���`a(���`escore���`a)���`a:���`a
���`d    ���bsdx�"""
    Create score labels for the right y-axis as the test name followed by the
    measurement unit (if any), split over two lines.
    """���`a
���`d    ���akfreturn���`a ���bsaaf���bs1a'���bsia{���`escore���aoa.���`evalue���bsia}���bseb\n���bsia{���`escore���aoa.���`dunit���bsia}���bs1a'���`a ���akbif���`a ���`escore���aoa.���`dunit���`a ���akdelse���`a ���bnbcstr���`a(���`escore���aoa.���`evalue���`a)���`a
���`a
���`a
���akcdef���`a ���bnftplot_student_results���`a(���`gstudent���`a,���`a ���`nscores_by_test���`a,���`a ���`kcohort_size���`a)���`a:���`a
���`d    ���`cfig���`a,���`a ���`cax1���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`gfigsize���aoa=���`a(���bmia9���`a,���`a ���bmia7���`a)���`a,���`a ���`rconstrained_layout���aoa=���bkcdTrue���`a)���`a
���`d    ���`cfig���aoa.���`fcanvas���aoa.���`gmanager���aoa.���`pset_window_title���`a(���bs1a'���bs1xEldorado K-8 Fitness Chart���bs1a'���`a)���`a
���`a
���`d    ���`cax1���aoa.���`iset_title���`a(���`gstudent���aoa.���`dname���`a)���`a
���`d    ���`cax1���aoa.���`jset_xlabel���`a(���`a
���`h        ���bs1a'���bs1xPercentile Ranking Across ���bsig{grade}���bs1g Grade ���bsih{gender}���bs1as���bseb\n���bs1a'���`a
���`h        ���bs1a'���bs1mCohort Size: ���bsim{cohort_size}���bs1a'���aoa.���`fformat���`a(���`a
���`l            ���`egrade���aoa=���`jto_ordinal���`a(���`gstudent���aoa.���`egrade���`a)���`a,���`a
���`l            ���`fgender���aoa=���`gstudent���aoa.���`fgender���aoa.���`etitle���`a(���`a)���`a,���`a
���`l            ���`kcohort_size���aoa=���`kcohort_size���`a)���`a)���`a
���`a
���`d    ���`jtest_names���`a ���aoa=���`a ���bnbdlist���`a(���`nscores_by_test���aoa.���`dkeys���`a(���`a)���`a)���`a
���`d    ���`kpercentiles���`a ���aoa=���`a ���`a[���`escore���aoa.���`jpercentile���`a ���akcfor���`a ���`escore���`a ���bowbin���`a ���`nscores_by_test���aoa.���`fvalues���`a(���`a)���`a]���`a
���`a
���`d    ���`erects���`a ���aoa=���`a ���`cax1���aoa.���`dbarh���`a(���`jtest_names���`a,���`a ���`kpercentiles���`a,���`a ���`ealign���aoa=���bs1a'���bs1fcenter���bs1a'���`a,���`a ���`fheight���aoa=���bmfc0.5���`a)���`a
���`d    ���bc1xE# Partition the percentile values to be able to draw large numbers in���`a
���`d    ���bc1xC# white within the bar, and small numbers in black outside the bar.���`a
���`d    ���`qlarge_percentiles���`a ���aoa=���`a ���`a[���`jto_ordinal���`a(���`ap���`a)���`a ���akbif���`a ���`ap���`a ���aoa>���`a ���bmib40���`a ���akdelse���`a ���bs1a'���bs1a'���`a ���akcfor���`a ���`ap���`a ���bowbin���`a ���`kpercentiles���`a]���`a
���`d    ���`qsmall_percentiles���`a ���aoa=���`a ���`a[���`jto_ordinal���`a(���`ap���`a)���`a ���akbif���`a ���`ap���`a ���aoa<���aoa=���`a ���bmib40���`a ���akdelse���`a ���bs1a'���bs1a'���`a ���akcfor���`a ���`ap���`a ���bowbin���`a ���`kpercentiles���`a]���`a
���`d    ���`cax1���aoa.���`ibar_label���`a(���`erects���`a,���`a ���`qsmall_percentiles���`a,���`a
���`r                  ���`gpadding���aoa=���bmia5���`a,���`a ���`ecolor���aoa=���bs1a'���bs1eblack���bs1a'���`a,���`a ���`jfontweight���aoa=���bs1a'���bs1dbold���bs1a'���`a)���`a
���`d    ���`cax1���aoa.���`ibar_label���`a(���`erects���`a,���`a ���`qlarge_percentiles���`a,���`a
���`r                  ���`gpadding���aoa=���aoa-���bmib32���`a,���`a ���`ecolor���aoa=���bs1a'���bs1ewhite���bs1a'���`a,���`a ���`jfontweight���aoa=���bs1a'���bs1dbold���bs1a'���`a)���`a
���`a
���`d    ���`cax1���aoa.���`hset_xlim���`a(���`a[���bmia0���`a,���`a ���bmic100���`a]���`a)���`a
���`d    ���`cax1���aoa.���`jset_xticks���`a(���`a[���bmia0���`a,���`a ���bmib10���`a,���`a ���bmib20���`a,���`a ���bmib30���`a,���`a ���bmib40���`a,���`a ���bmib50���`a,���`a ���bmib60���`a,���`a ���bmib70���`a,���`a ���bmib80���`a,���`a ���bmib90���`a,���`a ���bmic100���`a]���`a)���`a
���`d    ���`cax1���aoa.���`exaxis���aoa.���`dgrid���`a(���bkcdTrue���`a,���`a ���`ilinestyle���aoa=���bs1a'���bs1b--���bs1a'���`a,���`a ���`ewhich���aoa=���bs1a'���bs1emajor���bs1a'���`a,���`a
���`s                   ���`ecolor���aoa=���bs1a'���bs1dgrey���bs1a'���`a,���`a ���`ealpha���aoa=���bmfc.25���`a)���`a
���`d    ���`cax1���aoa.���`gaxvline���`a(���bmib50���`a,���`a ���`ecolor���aoa=���bs1a'���bs1dgrey���bs1a'���`a,���`a ���`ealpha���aoa=���bmfd0.25���`a)���`b  ���bc1q# median position���`a
���`a
���`d    ���bc1x,# Set the right-hand Y-axis ticks and labels���`a
���`d    ���`cax2���`a ���aoa=���`a ���`cax1���aoa.���`etwinx���`a(���`a)���`a
���`d    ���bc1x:# Set equal limits on both yaxis so that the ticks line up���`a
���`d    ���`cax2���aoa.���`hset_ylim���`a(���`cax1���aoa.���`hget_ylim���`a(���`a)���`a)���`a
���`d    ���bc1x## Set the tick locations and labels���`a
���`d    ���`cax2���aoa.���`jset_yticks���`a(���`a
���`h        ���`bnp���aoa.���`farange���`a(���bnbclen���`a(���`nscores_by_test���`a)���`a)���`a,���`a
���`h        ���`flabels���aoa=���`a[���`lformat_score���`a(���`escore���`a)���`a ���akcfor���`a ���`escore���`a ���bowbin���`a ���`nscores_by_test���aoa.���`fvalues���`a(���`a)���`a]���`a)���`a
���`a
���`d    ���`cax2���aoa.���`jset_ylabel���`a(���bs1a'���bs1kTest Scores���bs1a'���`a)���`a
���`a
���`a
���`gstudent���`a ���aoa=���`a ���`gStudent���`a(���`dname���aoa=���bs1a'���bs1jJohnny Doe���bs1a'���`a,���`a ���`egrade���aoa=���bmia2���`a,���`a ���`fgender���aoa=���bs1a'���bs1cBoy���bs1a'���`a)���`a
���`nscores_by_test���`a ���aoa=���`a ���`a{���`a
���`d    ���bs1a'���bs1jPacer Test���bs1a'���`a:���`a ���`eScore���`a(���bmia7���`a,���`a ���bs1a'���bs1dlaps���bs1a'���`a,���`a ���`jpercentile���aoa=���bmib37���`a)���`a,���`a
���`d    ���bs1a'���bs1jFlexed Arm���bseb\n���bs1e Hang���bs1a'���`a:���`a ���`eScore���`a(���bmib48���`a,���`a ���bs1a'���bs1csec���bs1a'���`a,���`a ���`jpercentile���aoa=���bmib95���`a)���`a,���`a
���`d    ���bs1a'���bs1hMile Run���bs1a'���`a:���`a ���`eScore���`a(���bs1a'���bs1e12:52���bs1a'���`a,���`a ���bs1a'���bs1gmin:sec���bs1a'���`a,���`a ���`jpercentile���aoa=���bmib73���`a)���`a,���`a
���`d    ���bs1a'���bs1gAgility���bs1a'���`a:���`a ���`eScore���`a(���bmib17���`a,���`a ���bs1a'���bs1csec���bs1a'���`a,���`a ���`jpercentile���aoa=���bmib60���`a)���`a,���`a
���`d    ���bs1a'���bs1hPush Ups���bs1a'���`a:���`a ���`eScore���`a(���bmib14���`a,���`a ���bs1a'���bs1a'���`a,���`a ���`jpercentile���aoa=���bmib16���`a)���`a,���`a
���`a}���`a
���`a
���`tplot_student_results���`a(���`gstudent���`a,���`a ���`nscores_by_test���`a,���`a ���`kcohort_size���aoa=���bmib62���`a)���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
���`a
���bc1xM#############################################################################���`a
���bc1a#���`a
���bc1x# .. admonition:: References���`a
���bc1a#���`a
���bc1xN#    The use of the following functions, methods, classes and modules is shown���`a
���bc1u#    in this example:���`a
���bc1a#���`a
���bc1x;#    - `matplotlib.axes.Axes.bar` / `matplotlib.pyplot.bar`���`a
���bc1xG#    - `matplotlib.axes.Axes.bar_label` / `matplotlib.pyplot.bar_label`���`a
���bc1x?#    - `matplotlib.axes.Axes.twinx` / `matplotlib.pyplot.twinx`���`a
`dNone�