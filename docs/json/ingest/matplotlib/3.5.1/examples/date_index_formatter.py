ŸØÇÅŸ¥ÉôKŸ±Çbsdy<"""
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
"""Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±ÇbknfimportŸ±Ç`a Ÿ±ÇbnnŸ¢ÑenumpyŸ†Ñenumpyf1.22.3fmoduleenumpyfmoduleıŸ±Ç`a Ÿ±ÇakbasŸ±Ç`a Ÿ±ÇbnnbnpŸ±Ç`a
Ÿ±ÇbknfimportŸ±Ç`a Ÿ±ÇbnnŸ¢ÑjmatplotlibŸ†Ñjmatplotlibe3.5.1fmodulejmatplotlibfmoduleıŸ±Çbnna.Ÿ±ÇbnnfpyplotŸ±Ç`a Ÿ±ÇakbasŸ±Ç`a Ÿ±ÇbnncpltŸ±Ç`a
Ÿ±ÇbknfimportŸ±Ç`a Ÿ±ÇbnnŸ¢ÑjmatplotlibŸ†Ñjmatplotlibe3.5.1fmodulejmatplotlibfmoduleıŸ±Çbnna.Ÿ±ÇbnnecbookŸ±Ç`a Ÿ±ÇakbasŸ±Ç`a Ÿ±ÇbnnecbookŸ±Ç`a
Ÿ±ÇbknfimportŸ±Ç`a Ÿ±ÇbnnŸ¢ÑjmatplotlibŸ†Ñjmatplotlibe3.5.1fmodulejmatplotlibfmoduleıŸ±Çbnna.Ÿ±ÇbnnelinesŸ±Ç`a Ÿ±ÇakbasŸ±Ç`a Ÿ±ÇbnnbmlŸ±Ç`a
Ÿ±ÇbkndfromŸ±Ç`a Ÿ±ÇbnnŸ¢ÑjmatplotlibŸ†Ñjmatplotlibe3.5.1fmodulejmatplotlibfmoduleıŸ±Çbnna.Ÿ±ÇbnnedatesŸ±Ç`a Ÿ±ÇbknfimportŸ±Ç`a Ÿ±Ç`mDateFormatterŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`jDayLocatorŸ±Ç`a
Ÿ±ÇbkndfromŸ±Ç`a Ÿ±ÇbnnŸ¢ÑjmatplotlibŸ†Ñjmatplotlibe3.5.1fmodulejmatplotlibfmoduleıŸ±Çbnna.Ÿ±ÇbnnftickerŸ±Ç`a Ÿ±ÇbknfimportŸ±Ç`a Ÿ±Ç`iFormatterŸ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1xM# Load a numpy record array from yahoo csv data with fields date, open, high,Ÿ±Ç`a
Ÿ±Çbc1xL# low, close, volume, adj_close from the mpl-data/sample_data directory. TheŸ±Ç`a
Ÿ±Çbc1xK# record array stores the date as an np.datetime64 with a day unit ('D') inŸ±Ç`a
Ÿ±Çbc1x# the date column (``r.date``).Ÿ±Ç`a
Ÿ±Ç`arŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`a(Ÿ±Ç`ecbookŸ±Çaoa.Ÿ±Ç`oget_sample_dataŸ±Ç`a(Ÿ±Çbs1a'Ÿ±Çbs1hgoog.npzŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`gnp_loadŸ±Çaoa=Ÿ±ÇbkcdTrueŸ±Ç`a)Ÿ±Ç`a[Ÿ±Çbs1a'Ÿ±Çbs1jprice_dataŸ±Çbs1a'Ÿ±Ç`a]Ÿ±Ç`a
Ÿ±Ç`e     Ÿ±Çaoa.Ÿ±Ç`dviewŸ±Ç`a(Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`hrecarrayŸ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`arŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`arŸ±Ç`a[Ÿ±Ç`a:Ÿ±Çbmia9Ÿ±Ç`a]Ÿ±Ç`b  Ÿ±Çbc1v# get the first 9 daysŸ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`cfigŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`a(Ÿ±Ç`cax1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`cax2Ÿ±Ç`a)Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`hsubplotsŸ±Ç`a(Ÿ±Ç`enrowsŸ±Çaoa=Ÿ±Çbmia2Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`gfigsizeŸ±Çaoa=Ÿ±Ç`a(Ÿ±Çbmia6Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia6Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`x                               Ÿ±Ç`rconstrained_layoutŸ±Çaoa=Ÿ±Ç`a{Ÿ±Çbs1a'Ÿ±Çbs1fhspaceŸ±Çbs1a'Ÿ±Ç`a:Ÿ±Ç`a Ÿ±Çbmfc.15Ÿ±Ç`a}Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1x:# First we'll do it the default way, with gaps on weekendsŸ±Ç`a
Ÿ±Ç`cax1Ÿ±Çaoa.Ÿ±Ç`dplotŸ±Ç`a(Ÿ±Ç`arŸ±Çaoa.Ÿ±Ç`ddateŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`arŸ±Çaoa.Ÿ±Ç`iadj_closeŸ±Ç`a,Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1bo-Ÿ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1x# Highlight gaps in daily dataŸ±Ç`a
Ÿ±Ç`dgapsŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`kflatnonzeroŸ±Ç`a(Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`ddiffŸ±Ç`a(Ÿ±Ç`arŸ±Çaoa.Ÿ±Ç`ddateŸ±Ç`a)Ÿ±Ç`a Ÿ±Çaoa>Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`ktimedelta64Ÿ±Ç`a(Ÿ±Çbmia1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1aDŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±ÇakcforŸ±Ç`a Ÿ±Ç`cgapŸ±Ç`a Ÿ±ÇbowbinŸ±Ç`a Ÿ±Ç`arŸ±Ç`a[Ÿ±Ç`a[Ÿ±Çbs1a'Ÿ±Çbs1ddateŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1iadj_closeŸ±Çbs1a'Ÿ±Ç`a]Ÿ±Ç`a]Ÿ±Ç`a[Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`estackŸ±Ç`a(Ÿ±Ç`a(Ÿ±Ç`dgapsŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dgapsŸ±Ç`a Ÿ±Çaoa+Ÿ±Ç`a Ÿ±Çbmia1Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Çaoa.Ÿ±Ç`aTŸ±Ç`a]Ÿ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`cax1Ÿ±Çaoa.Ÿ±Ç`dplotŸ±Ç`a(Ÿ±Ç`cgapŸ±Çaoa.Ÿ±Ç`ddateŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`cgapŸ±Çaoa.Ÿ±Ç`iadj_closeŸ±Ç`a,Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1cw--Ÿ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`blwŸ±Çaoa=Ÿ±Çbmia2Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cax1Ÿ±Çaoa.Ÿ±Ç`flegendŸ±Ç`a(Ÿ±Ç`ghandlesŸ±Çaoa=Ÿ±Ç`a[Ÿ±Ç`bmlŸ±Çaoa.Ÿ±Ç`fLine2DŸ±Ç`a(Ÿ±Ç`a[Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`a[Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`blsŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1b--Ÿ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`elabelŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1rGaps in daily dataŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a]Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`cax1Ÿ±Çaoa.Ÿ±Ç`iset_titleŸ±Ç`a(Ÿ±Çbs2a"Ÿ±Çbs2wPlot y at x CoordinatesŸ±Çbs2a"Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cax1Ÿ±Çaoa.Ÿ±Ç`exaxisŸ±Çaoa.Ÿ±Ç`qset_major_locatorŸ±Ç`a(Ÿ±Ç`jDayLocatorŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cax1Ÿ±Çaoa.Ÿ±Ç`exaxisŸ±Çaoa.Ÿ±Ç`sset_major_formatterŸ±Ç`a(Ÿ±Ç`mDateFormatterŸ±Ç`a(Ÿ±Çbs1a'Ÿ±Çbsib%aŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1x?# Next we'll write a custom index formatter. Below we will plotŸ±Ç`a
Ÿ±Çbc1xL# the data against an index that goes from 0, 1,  ... len(data).  Instead ofŸ±Ç`a
Ÿ±Çbc1x<# formatting the tick marks as integers, we format as times.Ÿ±Ç`a
Ÿ±ÇakcdefŸ±Ç`a Ÿ±Çbnfkformat_dateŸ±Ç`a(Ÿ±Ç`axŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`a_Ÿ±Ç`a)Ÿ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±ÇakctryŸ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±Çbc1x># convert datetime64 to datetime, and use datetime's strftime:Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±ÇakfreturnŸ±Ç`a Ÿ±Ç`arŸ±Çaoa.Ÿ±Ç`ddateŸ±Ç`a[Ÿ±ÇbnberoundŸ±Ç`a(Ÿ±Ç`axŸ±Ç`a)Ÿ±Ç`a]Ÿ±Çaoa.Ÿ±Ç`ditemŸ±Ç`a(Ÿ±Ç`a)Ÿ±Çaoa.Ÿ±Ç`hstrftimeŸ±Ç`a(Ÿ±Çbs1a'Ÿ±Çbsib%aŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±ÇakfexceptŸ±Ç`a Ÿ±ÇbnejIndexErrorŸ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±ÇakdpassŸ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1x?# Create an index plot (x defaults to range(len(y)) if omitted)Ÿ±Ç`a
Ÿ±Ç`cax2Ÿ±Çaoa.Ÿ±Ç`dplotŸ±Ç`a(Ÿ±Ç`arŸ±Çaoa.Ÿ±Ç`iadj_closeŸ±Ç`a,Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1bo-Ÿ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`cax2Ÿ±Çaoa.Ÿ±Ç`iset_titleŸ±Ç`a(Ÿ±Çbs2a"Ÿ±Çbs2x2Plot y at Index Coordinates Using Custom FormatterŸ±Çbs2a"Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cax2Ÿ±Çaoa.Ÿ±Ç`exaxisŸ±Çaoa.Ÿ±Ç`sset_major_formatterŸ±Ç`a(Ÿ±Ç`kformat_dateŸ±Ç`a)Ÿ±Ç`b  Ÿ±Çbc1x"# internally creates FuncFormatterŸ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1xM#############################################################################Ÿ±Ç`a
Ÿ±Çbc1xL# Instead of passing a function into `.Axis.set_major_formatter` you can useŸ±Ç`a
Ÿ±Çbc1xK# any other callable, e.g. an instance of a class that implements __call__:Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±ÇakeclassŸ±Ç`a Ÿ±ÇbnckMyFormatterŸ±Ç`a(Ÿ±Ç`iFormatterŸ±Ç`a)Ÿ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±ÇakcdefŸ±Ç`a Ÿ±Çbfmh__init__Ÿ±Ç`a(Ÿ±ÇbbpdselfŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`edatesŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`cfmtŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbsib%aŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±ÇbbpdselfŸ±Çaoa.Ÿ±Ç`edatesŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`edatesŸ±Ç`a
Ÿ±Ç`h        Ÿ±ÇbbpdselfŸ±Çaoa.Ÿ±Ç`cfmtŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cfmtŸ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±ÇakcdefŸ±Ç`a Ÿ±Çbfmh__call__Ÿ±Ç`a(Ÿ±ÇbbpdselfŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`axŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`cposŸ±Çaoa=Ÿ±Çbmia0Ÿ±Ç`a)Ÿ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±Çbsdx2"""Return the label for time x at position pos."""Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±ÇakctryŸ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`l            Ÿ±ÇakfreturnŸ±Ç`a Ÿ±ÇbbpdselfŸ±Çaoa.Ÿ±Ç`edatesŸ±Ç`a[Ÿ±ÇbnberoundŸ±Ç`a(Ÿ±Ç`axŸ±Ç`a)Ÿ±Ç`a]Ÿ±Çaoa.Ÿ±Ç`ditemŸ±Ç`a(Ÿ±Ç`a)Ÿ±Çaoa.Ÿ±Ç`hstrftimeŸ±Ç`a(Ÿ±ÇbbpdselfŸ±Çaoa.Ÿ±Ç`cfmtŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±ÇakfexceptŸ±Ç`a Ÿ±ÇbnejIndexErrorŸ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`l            Ÿ±ÇakdpassŸ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`cax2Ÿ±Çaoa.Ÿ±Ç`exaxisŸ±Çaoa.Ÿ±Ç`sset_major_formatterŸ±Ç`a(Ÿ±Ç`kMyFormatterŸ±Ç`a(Ÿ±Ç`arŸ±Çaoa.Ÿ±Ç`ddateŸ±Ç`a,Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbsib%aŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
`dNoneˆ