Ù¯‚Ù´ƒ™êÙ±‚bsdy¦"""
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
"""Ù±‚`a
Ù±‚`a
Ù±‚bkndfromÙ±‚`a Ù±‚bnnkcollectionsÙ±‚`a Ù±‚bknfimportÙ±‚`a Ù±‚`jnamedtupleÙ±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„enumpyÙ „enumpyf1.22.3fmoduleenumpyfmoduleõÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnnbnpÙ±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnnfpyplotÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnncpltÙ±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚`gStudentÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`jnamedtupleÙ±‚`a(Ù±‚bs1a'Ù±‚bs1gStudentÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`a[Ù±‚bs1a'Ù±‚bs1dnameÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚bs1a'Ù±‚bs1egradeÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚bs1a'Ù±‚bs1fgenderÙ±‚bs1a'Ù±‚`a]Ù±‚`a)Ù±‚`a
Ù±‚`eScoreÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`jnamedtupleÙ±‚`a(Ù±‚bs1a'Ù±‚bs1eScoreÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`a[Ù±‚bs1a'Ù±‚bs1evalueÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚bs1a'Ù±‚bs1dunitÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚bs1a'Ù±‚bs1jpercentileÙ±‚bs1a'Ù±‚`a]Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚akcdefÙ±‚`a Ù±‚bnfjto_ordinalÙ±‚`a(Ù±‚`cnumÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`d    Ù±‚bsdx?"""Convert an integer to an ordinal string, e.g. 2 -> '2nd'."""Ù±‚`a
Ù±‚`d    Ù±‚`hsuffixesÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`a{Ù±‚bnbcstrÙ±‚`a(Ù±‚`aiÙ±‚`a)Ù±‚`a:Ù±‚`a Ù±‚`avÙ±‚`a
Ù±‚`p                Ù±‚akcforÙ±‚`a Ù±‚`aiÙ±‚`a,Ù±‚`a Ù±‚`avÙ±‚`a Ù±‚bowbinÙ±‚`a Ù±‚bnbienumerateÙ±‚`a(Ù±‚`a[Ù±‚bs1a'Ù±‚bs1bthÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚bs1a'Ù±‚bs1bstÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚bs1a'Ù±‚bs1bndÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚bs1a'Ù±‚bs1brdÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚bs1a'Ù±‚bs1bthÙ±‚bs1a'Ù±‚`a,Ù±‚`a
Ù±‚`x'                                       Ù±‚bs1a'Ù±‚bs1bthÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚bs1a'Ù±‚bs1bthÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚bs1a'Ù±‚bs1bthÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚bs1a'Ù±‚bs1bthÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚bs1a'Ù±‚bs1bthÙ±‚bs1a'Ù±‚`a]Ù±‚`a)Ù±‚`a}Ù±‚`a
Ù±‚`d    Ù±‚`avÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bnbcstrÙ±‚`a(Ù±‚`cnumÙ±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚bc1x# special case early teensÙ±‚`a
Ù±‚`d    Ù±‚akbifÙ±‚`a Ù±‚`avÙ±‚`a Ù±‚bowbinÙ±‚`a Ù±‚`a{Ù±‚bs1a'Ù±‚bs1b11Ù±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚bs1a'Ù±‚bs1b12Ù±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚bs1a'Ù±‚bs1b13Ù±‚bs1a'Ù±‚`a}Ù±‚`a:Ù±‚`a
Ù±‚`h        Ù±‚akfreturnÙ±‚`a Ù±‚`avÙ±‚`a Ù±‚aoa+Ù±‚`a Ù±‚bs1a'Ù±‚bs1bthÙ±‚bs1a'Ù±‚`a
Ù±‚`d    Ù±‚akfreturnÙ±‚`a Ù±‚`avÙ±‚`a Ù±‚aoa+Ù±‚`a Ù±‚`hsuffixesÙ±‚`a[Ù±‚`avÙ±‚`a[Ù±‚aoa-Ù±‚bmia1Ù±‚`a]Ù±‚`a]Ù±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚akcdefÙ±‚`a Ù±‚bnflformat_scoreÙ±‚`a(Ù±‚`escoreÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`d    Ù±‚bsdx"""
    Create score labels for the right y-axis as the test name followed by the
    measurement unit (if any), split over two lines.
    """Ù±‚`a
Ù±‚`d    Ù±‚akfreturnÙ±‚`a Ù±‚bsaafÙ±‚bs1a'Ù±‚bsia{Ù±‚`escoreÙ±‚aoa.Ù±‚`evalueÙ±‚bsia}Ù±‚bseb\nÙ±‚bsia{Ù±‚`escoreÙ±‚aoa.Ù±‚`dunitÙ±‚bsia}Ù±‚bs1a'Ù±‚`a Ù±‚akbifÙ±‚`a Ù±‚`escoreÙ±‚aoa.Ù±‚`dunitÙ±‚`a Ù±‚akdelseÙ±‚`a Ù±‚bnbcstrÙ±‚`a(Ù±‚`escoreÙ±‚aoa.Ù±‚`evalueÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚akcdefÙ±‚`a Ù±‚bnftplot_student_resultsÙ±‚`a(Ù±‚`gstudentÙ±‚`a,Ù±‚`a Ù±‚`nscores_by_testÙ±‚`a,Ù±‚`a Ù±‚`kcohort_sizeÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`d    Ù±‚`cfigÙ±‚`a,Ù±‚`a Ù±‚`cax1Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cpltÙ±‚aoa.Ù±‚`hsubplotsÙ±‚`a(Ù±‚`gfigsizeÙ±‚aoa=Ù±‚`a(Ù±‚bmia9Ù±‚`a,Ù±‚`a Ù±‚bmia7Ù±‚`a)Ù±‚`a,Ù±‚`a Ù±‚`rconstrained_layoutÙ±‚aoa=Ù±‚bkcdTrueÙ±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`cfigÙ±‚aoa.Ù±‚`fcanvasÙ±‚aoa.Ù±‚`gmanagerÙ±‚aoa.Ù±‚`pset_window_titleÙ±‚`a(Ù±‚bs1a'Ù±‚bs1xEldorado K-8 Fitness ChartÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚`cax1Ù±‚aoa.Ù±‚`iset_titleÙ±‚`a(Ù±‚`gstudentÙ±‚aoa.Ù±‚`dnameÙ±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`cax1Ù±‚aoa.Ù±‚`jset_xlabelÙ±‚`a(Ù±‚`a
Ù±‚`h        Ù±‚bs1a'Ù±‚bs1xPercentile Ranking Across Ù±‚bsig{grade}Ù±‚bs1g Grade Ù±‚bsih{gender}Ù±‚bs1asÙ±‚bseb\nÙ±‚bs1a'Ù±‚`a
Ù±‚`h        Ù±‚bs1a'Ù±‚bs1mCohort Size: Ù±‚bsim{cohort_size}Ù±‚bs1a'Ù±‚aoa.Ù±‚`fformatÙ±‚`a(Ù±‚`a
Ù±‚`l            Ù±‚`egradeÙ±‚aoa=Ù±‚`jto_ordinalÙ±‚`a(Ù±‚`gstudentÙ±‚aoa.Ù±‚`egradeÙ±‚`a)Ù±‚`a,Ù±‚`a
Ù±‚`l            Ù±‚`fgenderÙ±‚aoa=Ù±‚`gstudentÙ±‚aoa.Ù±‚`fgenderÙ±‚aoa.Ù±‚`etitleÙ±‚`a(Ù±‚`a)Ù±‚`a,Ù±‚`a
Ù±‚`l            Ù±‚`kcohort_sizeÙ±‚aoa=Ù±‚`kcohort_sizeÙ±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚`jtest_namesÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bnbdlistÙ±‚`a(Ù±‚`nscores_by_testÙ±‚aoa.Ù±‚`dkeysÙ±‚`a(Ù±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`kpercentilesÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`a[Ù±‚`escoreÙ±‚aoa.Ù±‚`jpercentileÙ±‚`a Ù±‚akcforÙ±‚`a Ù±‚`escoreÙ±‚`a Ù±‚bowbinÙ±‚`a Ù±‚`nscores_by_testÙ±‚aoa.Ù±‚`fvaluesÙ±‚`a(Ù±‚`a)Ù±‚`a]Ù±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚`erectsÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cax1Ù±‚aoa.Ù±‚`dbarhÙ±‚`a(Ù±‚`jtest_namesÙ±‚`a,Ù±‚`a Ù±‚`kpercentilesÙ±‚`a,Ù±‚`a Ù±‚`ealignÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1fcenterÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`fheightÙ±‚aoa=Ù±‚bmfc0.5Ù±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚bc1xE# Partition the percentile values to be able to draw large numbers inÙ±‚`a
Ù±‚`d    Ù±‚bc1xC# white within the bar, and small numbers in black outside the bar.Ù±‚`a
Ù±‚`d    Ù±‚`qlarge_percentilesÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`a[Ù±‚`jto_ordinalÙ±‚`a(Ù±‚`apÙ±‚`a)Ù±‚`a Ù±‚akbifÙ±‚`a Ù±‚`apÙ±‚`a Ù±‚aoa>Ù±‚`a Ù±‚bmib40Ù±‚`a Ù±‚akdelseÙ±‚`a Ù±‚bs1a'Ù±‚bs1a'Ù±‚`a Ù±‚akcforÙ±‚`a Ù±‚`apÙ±‚`a Ù±‚bowbinÙ±‚`a Ù±‚`kpercentilesÙ±‚`a]Ù±‚`a
Ù±‚`d    Ù±‚`qsmall_percentilesÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`a[Ù±‚`jto_ordinalÙ±‚`a(Ù±‚`apÙ±‚`a)Ù±‚`a Ù±‚akbifÙ±‚`a Ù±‚`apÙ±‚`a Ù±‚aoa<Ù±‚aoa=Ù±‚`a Ù±‚bmib40Ù±‚`a Ù±‚akdelseÙ±‚`a Ù±‚bs1a'Ù±‚bs1a'Ù±‚`a Ù±‚akcforÙ±‚`a Ù±‚`apÙ±‚`a Ù±‚bowbinÙ±‚`a Ù±‚`kpercentilesÙ±‚`a]Ù±‚`a
Ù±‚`d    Ù±‚`cax1Ù±‚aoa.Ù±‚`ibar_labelÙ±‚`a(Ù±‚`erectsÙ±‚`a,Ù±‚`a Ù±‚`qsmall_percentilesÙ±‚`a,Ù±‚`a
Ù±‚`r                  Ù±‚`gpaddingÙ±‚aoa=Ù±‚bmia5Ù±‚`a,Ù±‚`a Ù±‚`ecolorÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1eblackÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`jfontweightÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1dboldÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`cax1Ù±‚aoa.Ù±‚`ibar_labelÙ±‚`a(Ù±‚`erectsÙ±‚`a,Ù±‚`a Ù±‚`qlarge_percentilesÙ±‚`a,Ù±‚`a
Ù±‚`r                  Ù±‚`gpaddingÙ±‚aoa=Ù±‚aoa-Ù±‚bmib32Ù±‚`a,Ù±‚`a Ù±‚`ecolorÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1ewhiteÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`jfontweightÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1dboldÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚`cax1Ù±‚aoa.Ù±‚`hset_xlimÙ±‚`a(Ù±‚`a[Ù±‚bmia0Ù±‚`a,Ù±‚`a Ù±‚bmic100Ù±‚`a]Ù±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`cax1Ù±‚aoa.Ù±‚`jset_xticksÙ±‚`a(Ù±‚`a[Ù±‚bmia0Ù±‚`a,Ù±‚`a Ù±‚bmib10Ù±‚`a,Ù±‚`a Ù±‚bmib20Ù±‚`a,Ù±‚`a Ù±‚bmib30Ù±‚`a,Ù±‚`a Ù±‚bmib40Ù±‚`a,Ù±‚`a Ù±‚bmib50Ù±‚`a,Ù±‚`a Ù±‚bmib60Ù±‚`a,Ù±‚`a Ù±‚bmib70Ù±‚`a,Ù±‚`a Ù±‚bmib80Ù±‚`a,Ù±‚`a Ù±‚bmib90Ù±‚`a,Ù±‚`a Ù±‚bmic100Ù±‚`a]Ù±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`cax1Ù±‚aoa.Ù±‚`exaxisÙ±‚aoa.Ù±‚`dgridÙ±‚`a(Ù±‚bkcdTrueÙ±‚`a,Ù±‚`a Ù±‚`ilinestyleÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1b--Ù±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`ewhichÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1emajorÙ±‚bs1a'Ù±‚`a,Ù±‚`a
Ù±‚`s                   Ù±‚`ecolorÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1dgreyÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`ealphaÙ±‚aoa=Ù±‚bmfc.25Ù±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`cax1Ù±‚aoa.Ù±‚`gaxvlineÙ±‚`a(Ù±‚bmib50Ù±‚`a,Ù±‚`a Ù±‚`ecolorÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1dgreyÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`ealphaÙ±‚aoa=Ù±‚bmfd0.25Ù±‚`a)Ù±‚`b  Ù±‚bc1q# median positionÙ±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚bc1x,# Set the right-hand Y-axis ticks and labelsÙ±‚`a
Ù±‚`d    Ù±‚`cax2Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cax1Ù±‚aoa.Ù±‚`etwinxÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚bc1x:# Set equal limits on both yaxis so that the ticks line upÙ±‚`a
Ù±‚`d    Ù±‚`cax2Ù±‚aoa.Ù±‚`hset_ylimÙ±‚`a(Ù±‚`cax1Ù±‚aoa.Ù±‚`hget_ylimÙ±‚`a(Ù±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚bc1x## Set the tick locations and labelsÙ±‚`a
Ù±‚`d    Ù±‚`cax2Ù±‚aoa.Ù±‚`jset_yticksÙ±‚`a(Ù±‚`a
Ù±‚`h        Ù±‚`bnpÙ±‚aoa.Ù±‚`farangeÙ±‚`a(Ù±‚bnbclenÙ±‚`a(Ù±‚`nscores_by_testÙ±‚`a)Ù±‚`a)Ù±‚`a,Ù±‚`a
Ù±‚`h        Ù±‚`flabelsÙ±‚aoa=Ù±‚`a[Ù±‚`lformat_scoreÙ±‚`a(Ù±‚`escoreÙ±‚`a)Ù±‚`a Ù±‚akcforÙ±‚`a Ù±‚`escoreÙ±‚`a Ù±‚bowbinÙ±‚`a Ù±‚`nscores_by_testÙ±‚aoa.Ù±‚`fvaluesÙ±‚`a(Ù±‚`a)Ù±‚`a]Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚`cax2Ù±‚aoa.Ù±‚`jset_ylabelÙ±‚`a(Ù±‚bs1a'Ù±‚bs1kTest ScoresÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚`gstudentÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`gStudentÙ±‚`a(Ù±‚`dnameÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1jJohnny DoeÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`egradeÙ±‚aoa=Ù±‚bmia2Ù±‚`a,Ù±‚`a Ù±‚`fgenderÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1cBoyÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`nscores_by_testÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`a{Ù±‚`a
Ù±‚`d    Ù±‚bs1a'Ù±‚bs1jPacer TestÙ±‚bs1a'Ù±‚`a:Ù±‚`a Ù±‚`eScoreÙ±‚`a(Ù±‚bmia7Ù±‚`a,Ù±‚`a Ù±‚bs1a'Ù±‚bs1dlapsÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`jpercentileÙ±‚aoa=Ù±‚bmib37Ù±‚`a)Ù±‚`a,Ù±‚`a
Ù±‚`d    Ù±‚bs1a'Ù±‚bs1jFlexed ArmÙ±‚bseb\nÙ±‚bs1e HangÙ±‚bs1a'Ù±‚`a:Ù±‚`a Ù±‚`eScoreÙ±‚`a(Ù±‚bmib48Ù±‚`a,Ù±‚`a Ù±‚bs1a'Ù±‚bs1csecÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`jpercentileÙ±‚aoa=Ù±‚bmib95Ù±‚`a)Ù±‚`a,Ù±‚`a
Ù±‚`d    Ù±‚bs1a'Ù±‚bs1hMile RunÙ±‚bs1a'Ù±‚`a:Ù±‚`a Ù±‚`eScoreÙ±‚`a(Ù±‚bs1a'Ù±‚bs1e12:52Ù±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚bs1a'Ù±‚bs1gmin:secÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`jpercentileÙ±‚aoa=Ù±‚bmib73Ù±‚`a)Ù±‚`a,Ù±‚`a
Ù±‚`d    Ù±‚bs1a'Ù±‚bs1gAgilityÙ±‚bs1a'Ù±‚`a:Ù±‚`a Ù±‚`eScoreÙ±‚`a(Ù±‚bmib17Ù±‚`a,Ù±‚`a Ù±‚bs1a'Ù±‚bs1csecÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`jpercentileÙ±‚aoa=Ù±‚bmib60Ù±‚`a)Ù±‚`a,Ù±‚`a
Ù±‚`d    Ù±‚bs1a'Ù±‚bs1hPush UpsÙ±‚bs1a'Ù±‚`a:Ù±‚`a Ù±‚`eScoreÙ±‚`a(Ù±‚bmib14Ù±‚`a,Ù±‚`a Ù±‚bs1a'Ù±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`jpercentileÙ±‚aoa=Ù±‚bmib16Ù±‚`a)Ù±‚`a,Ù±‚`a
Ù±‚`a}Ù±‚`a
Ù±‚`a
Ù±‚`tplot_student_resultsÙ±‚`a(Ù±‚`gstudentÙ±‚`a,Ù±‚`a Ù±‚`nscores_by_testÙ±‚`a,Ù±‚`a Ù±‚`kcohort_sizeÙ±‚aoa=Ù±‚bmib62Ù±‚`a)Ù±‚`a
Ù±‚`cpltÙ±‚aoa.Ù±‚`dshowÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚bc1xM#############################################################################Ù±‚`a
Ù±‚bc1a#Ù±‚`a
Ù±‚bc1x# .. admonition:: ReferencesÙ±‚`a
Ù±‚bc1a#Ù±‚`a
Ù±‚bc1xN#    The use of the following functions, methods, classes and modules is shownÙ±‚`a
Ù±‚bc1u#    in this example:Ù±‚`a
Ù±‚bc1a#Ù±‚`a
Ù±‚bc1x;#    - `matplotlib.axes.Axes.bar` / `matplotlib.pyplot.bar`Ù±‚`a
Ù±‚bc1xG#    - `matplotlib.axes.Axes.bar_label` / `matplotlib.pyplot.bar_label`Ù±‚`a
Ù±‚bc1x?#    - `matplotlib.axes.Axes.twinx` / `matplotlib.pyplot.twinx`Ù±‚`a
`dNoneö