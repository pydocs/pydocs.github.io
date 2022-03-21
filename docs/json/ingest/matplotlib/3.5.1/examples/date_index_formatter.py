��������K���bsdy<"""
=====================================
Custom tick formatter for time series
=====================================

.. redirect-from:: /gallery/text_labels_and_annotations/date_index_formatter
.. redirect-from:: /gallery/ticks/date_index_formatter2

When plotting daily data, e.g., financial time series, one often wants
to leave out days on which there is no data, for instance weekends, so that
the data are plotted at regular intervals without extra spaces for the days
with no data.
The example shows how to use an 'index formatter' to achieve the desired plot.
"""���`a
���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnecbook���`a ���akbas���`a ���bnnecbook���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnelines���`a ���akbas���`a ���bnnbml���`a
���bkndfrom���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnedates���`a ���bknfimport���`a ���`mDateFormatter���`a,���`a ���`jDayLocator���`a
���bkndfrom���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfticker���`a ���bknfimport���`a ���`iFormatter���`a
���`a
���`a
���bc1xM# Load a numpy record array from yahoo csv data with fields date, open, high,���`a
���bc1xL# low, close, volume, adj_close from the mpl-data/sample_data directory. The���`a
���bc1xK# record array stores the date as an np.datetime64 with a day unit ('D') in���`a
���bc1x# the date column (``r.date``).���`a
���`ar���`a ���aoa=���`a ���`a(���`ecbook���aoa.���`oget_sample_data���`a(���bs1a'���bs1hgoog.npz���bs1a'���`a,���`a ���`gnp_load���aoa=���bkcdTrue���`a)���`a[���bs1a'���bs1jprice_data���bs1a'���`a]���`a
���`e     ���aoa.���`dview���`a(���`bnp���aoa.���`hrecarray���`a)���`a)���`a
���`ar���`a ���aoa=���`a ���`ar���`a[���`a:���bmia9���`a]���`b  ���bc1v# get the first 9 days���`a
���`a
���`cfig���`a,���`a ���`a(���`cax1���`a,���`a ���`cax2���`a)���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`enrows���aoa=���bmia2���`a,���`a ���`gfigsize���aoa=���`a(���bmia6���`a,���`a ���bmia6���`a)���`a,���`a
���`x                               ���`rconstrained_layout���aoa=���`a{���bs1a'���bs1fhspace���bs1a'���`a:���`a ���bmfc.15���`a}���`a)���`a
���`a
���bc1x:# First we'll do it the default way, with gaps on weekends���`a
���`cax1���aoa.���`dplot���`a(���`ar���aoa.���`ddate���`a,���`a ���`ar���aoa.���`iadj_close���`a,���`a ���bs1a'���bs1bo-���bs1a'���`a)���`a
���`a
���bc1x# Highlight gaps in daily data���`a
���`dgaps���`a ���aoa=���`a ���`bnp���aoa.���`kflatnonzero���`a(���`bnp���aoa.���`ddiff���`a(���`ar���aoa.���`ddate���`a)���`a ���aoa>���`a ���`bnp���aoa.���`ktimedelta64���`a(���bmia1���`a,���`a ���bs1a'���bs1aD���bs1a'���`a)���`a)���`a
���akcfor���`a ���`cgap���`a ���bowbin���`a ���`ar���`a[���`a[���bs1a'���bs1ddate���bs1a'���`a,���`a ���bs1a'���bs1iadj_close���bs1a'���`a]���`a]���`a[���`bnp���aoa.���`estack���`a(���`a(���`dgaps���`a,���`a ���`dgaps���`a ���aoa+���`a ���bmia1���`a)���`a)���aoa.���`aT���`a]���`a:���`a
���`d    ���`cax1���aoa.���`dplot���`a(���`cgap���aoa.���`ddate���`a,���`a ���`cgap���aoa.���`iadj_close���`a,���`a ���bs1a'���bs1cw--���bs1a'���`a,���`a ���`blw���aoa=���bmia2���`a)���`a
���`cax1���aoa.���`flegend���`a(���`ghandles���aoa=���`a[���`bml���aoa.���`fLine2D���`a(���`a[���`a]���`a,���`a ���`a[���`a]���`a,���`a ���`bls���aoa=���bs1a'���bs1b--���bs1a'���`a,���`a ���`elabel���aoa=���bs1a'���bs1rGaps in daily data���bs1a'���`a)���`a]���`a)���`a
���`a
���`cax1���aoa.���`iset_title���`a(���bs2a"���bs2wPlot y at x Coordinates���bs2a"���`a)���`a
���`cax1���aoa.���`exaxis���aoa.���`qset_major_locator���`a(���`jDayLocator���`a(���`a)���`a)���`a
���`cax1���aoa.���`exaxis���aoa.���`sset_major_formatter���`a(���`mDateFormatter���`a(���bs1a'���bsib%a���bs1a'���`a)���`a)���`a
���`a
���`a
���bc1x?# Next we'll write a custom index formatter. Below we will plot���`a
���bc1xL# the data against an index that goes from 0, 1,  ... len(data).  Instead of���`a
���bc1x<# formatting the tick marks as integers, we format as times.���`a
���akcdef���`a ���bnfkformat_date���`a(���`ax���`a,���`a ���`a_���`a)���`a:���`a
���`d    ���akctry���`a:���`a
���`h        ���bc1x># convert datetime64 to datetime, and use datetime's strftime:���`a
���`h        ���akfreturn���`a ���`ar���aoa.���`ddate���`a[���bnberound���`a(���`ax���`a)���`a]���aoa.���`ditem���`a(���`a)���aoa.���`hstrftime���`a(���bs1a'���bsib%a���bs1a'���`a)���`a
���`d    ���akfexcept���`a ���bnejIndexError���`a:���`a
���`h        ���akdpass���`a
���`a
���bc1x?# Create an index plot (x defaults to range(len(y)) if omitted)���`a
���`cax2���aoa.���`dplot���`a(���`ar���aoa.���`iadj_close���`a,���`a ���bs1a'���bs1bo-���bs1a'���`a)���`a
���`a
���`cax2���aoa.���`iset_title���`a(���bs2a"���bs2x2Plot y at Index Coordinates Using Custom Formatter���bs2a"���`a)���`a
���`cax2���aoa.���`exaxis���aoa.���`sset_major_formatter���`a(���`kformat_date���`a)���`b  ���bc1x"# internally creates FuncFormatter���`a
���`a
���bc1xM#############################################################################���`a
���bc1xL# Instead of passing a function into `.Axis.set_major_formatter` you can use���`a
���bc1xK# any other callable, e.g. an instance of a class that implements __call__:���`a
���`a
���`a
���akeclass���`a ���bnckMyFormatter���`a(���`iFormatter���`a)���`a:���`a
���`d    ���akcdef���`a ���bfmh__init__���`a(���bbpdself���`a,���`a ���`edates���`a,���`a ���`cfmt���aoa=���bs1a'���bsib%a���bs1a'���`a)���`a:���`a
���`h        ���bbpdself���aoa.���`edates���`a ���aoa=���`a ���`edates���`a
���`h        ���bbpdself���aoa.���`cfmt���`a ���aoa=���`a ���`cfmt���`a
���`a
���`d    ���akcdef���`a ���bfmh__call__���`a(���bbpdself���`a,���`a ���`ax���`a,���`a ���`cpos���aoa=���bmia0���`a)���`a:���`a
���`h        ���bsdx2"""Return the label for time x at position pos."""���`a
���`h        ���akctry���`a:���`a
���`l            ���akfreturn���`a ���bbpdself���aoa.���`edates���`a[���bnberound���`a(���`ax���`a)���`a]���aoa.���`ditem���`a(���`a)���aoa.���`hstrftime���`a(���bbpdself���aoa.���`cfmt���`a)���`a
���`h        ���akfexcept���`a ���bnejIndexError���`a:���`a
���`l            ���akdpass���`a
���`a
���`a
���`cax2���aoa.���`exaxis���aoa.���`sset_major_formatter���`a(���`kMyFormatter���`a(���`ar���aoa.���`ddate���`a,���`a ���bs1a'���bsib%a���bs1a'���`a)���`a)���`a
`dNone�