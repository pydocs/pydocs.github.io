ŸØÇÅŸ¥ÉôGŸ±Çbsdx…"""
=================================
Date tick locators and formatters
=================================

This example illustrates the usage and effect of the various date locators and
formatters.
"""Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±ÇbknfimportŸ±Ç`a Ÿ±ÇbnnŸ¢ÑenumpyŸ†Ñenumpyf1.22.3fmoduleenumpyfmoduleıŸ±Ç`a Ÿ±ÇakbasŸ±Ç`a Ÿ±ÇbnnbnpŸ±Ç`a
Ÿ±ÇbknfimportŸ±Ç`a Ÿ±ÇbnnŸ¢ÑjmatplotlibŸ†Ñjmatplotlibe3.5.1fmodulejmatplotlibfmoduleıŸ±Çbnna.Ÿ±ÇbnnfpyplotŸ±Ç`a Ÿ±ÇakbasŸ±Ç`a Ÿ±ÇbnncpltŸ±Ç`a
Ÿ±ÇbknfimportŸ±Ç`a Ÿ±ÇbnnŸ¢ÑjmatplotlibŸ†Ñjmatplotlibe3.5.1fmodulejmatplotlibfmoduleıŸ±Çbnna.Ÿ±ÇbnnftickerŸ±Ç`a Ÿ±ÇakbasŸ±Ç`a Ÿ±ÇbnnftickerŸ±Ç`a
Ÿ±ÇbkndfromŸ±Ç`a Ÿ±ÇbnnŸ¢ÑjmatplotlibŸ†Ñjmatplotlibe3.5.1fmodulejmatplotlibfmoduleıŸ±Çbnna.Ÿ±ÇbnnedatesŸ±Ç`a Ÿ±ÇbknfimportŸ±Ç`a Ÿ±Ç`a(Ÿ±Ç`oAutoDateLocatorŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`kYearLocatorŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`lMonthLocatorŸ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`x                              Ÿ±Ç`jDayLocatorŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`nWeekdayLocatorŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`kHourLocatorŸ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`x                              Ÿ±Ç`mMinuteLocatorŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`mSecondLocatorŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`rMicrosecondLocatorŸ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`x                              Ÿ±Ç`lRRuleLocatorŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`lrrulewrapperŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`gMONTHLYŸ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`x                              Ÿ±Ç`bMOŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`bTUŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`bWEŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`bTHŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`bFRŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`bSAŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`bSUŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`mDateFormatterŸ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`x                              Ÿ±Ç`qAutoDateFormatterŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`tConciseDateFormatterŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`hlocatorsŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`a[Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`a(Ÿ±Çbs1a'Ÿ±Çbs1xAutoDateLocator(maxticks=8)Ÿ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1j2003-02-01Ÿ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1a%Ÿ±Çbs1bY-Ÿ±Çbs1a%Ÿ±Çbs1amŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`a(Ÿ±Çbs1a'Ÿ±Çbs1tYearLocator(month=4)Ÿ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1j2003-02-01Ÿ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1a%Ÿ±Çbs1bY-Ÿ±Çbs1a%Ÿ±Çbs1amŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`a(Ÿ±Çbs1a'Ÿ±Çbs1xMonthLocator(bymonth=[4,8,12])Ÿ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1j2003-02-01Ÿ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1a%Ÿ±Çbs1bY-Ÿ±Çbs1a%Ÿ±Çbs1amŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`a(Ÿ±Çbs1a'Ÿ±Çbs1xDayLocator(interval=180)Ÿ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1j2003-02-01Ÿ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1a%Ÿ±Çbs1bY-Ÿ±Çbs1a%Ÿ±Çbs1bm-Ÿ±Çbsib%dŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`a(Ÿ±Çbs1a'Ÿ±Çbs1x(WeekdayLocator(byweekday=SU, interval=4)Ÿ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1j2000-07-01Ÿ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbsib%aŸ±Çbs1a Ÿ±Çbs1a%Ÿ±Çbs1bY-Ÿ±Çbs1a%Ÿ±Çbs1bm-Ÿ±Çbsib%dŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`a(Ÿ±Çbs1a'Ÿ±Çbs1x!HourLocator(byhour=range(0,24,6))Ÿ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1j2000-02-04Ÿ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1a%Ÿ±Çbs1cH hŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`a(Ÿ±Çbs1a'Ÿ±Çbs1xMinuteLocator(interval=15)Ÿ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1p2000-02-01 02:00Ÿ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1a%Ÿ±Çbs1bH:Ÿ±Çbs1a%Ÿ±Çbs1aMŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`a(Ÿ±Çbs1a'Ÿ±Çbs1xSecondLocator(bysecond=(0,30))Ÿ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1p2000-02-01 00:02Ÿ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1a%Ÿ±Çbs1bH:Ÿ±Çbs1a%Ÿ±Çbs1bM:Ÿ±Çbs1a%Ÿ±Çbs1aSŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`a(Ÿ±Çbs1a'Ÿ±Çbs1x!MicrosecondLocator(interval=1000)Ÿ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1w2000-02-01 00:00:00.005Ÿ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1a%Ÿ±Çbs1bS.Ÿ±Çbsib%fŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`a(Ÿ±Çbs1a'Ÿ±Çbs1x(RRuleLocator(rrulewrapper(freq=MONTHLY, Ÿ±Çbseb\nŸ±Çbs1xbyweekday=(MO, TU, WE, TH,Ÿ±Çbs1a'Ÿ±Ç`a Ÿ±Çaoa+Ÿ±Ç`a
Ÿ±Ç`e     Ÿ±Çbs1a'Ÿ±Çbs1s FR), bysetpos=-1))Ÿ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1j2000-07-01Ÿ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1a%Ÿ±Çbs1bY-Ÿ±Çbs1a%Ÿ±Çbs1bm-Ÿ±Çbsib%dŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a]Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`jformattersŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`a[Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`a(Ÿ±Çbs1a'Ÿ±Çbs1x/AutoDateFormatter(ax.xaxis.get_major_locator())Ÿ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`a(Ÿ±Çbs1a'Ÿ±Çbs1x2ConciseDateFormatter(ax.xaxis.get_major_locator())Ÿ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`a(Ÿ±Çbs1a'Ÿ±Çbs1nDateFormatter(Ÿ±Çbs1a"Ÿ±Çbs1a%Ÿ±Çbs1bb Ÿ±Çbs1a%Ÿ±Çbs1aYŸ±Çbs1a"Ÿ±Çbs1a)Ÿ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a]Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±ÇakcdefŸ±Ç`a Ÿ±Çbnfiplot_axisŸ±Ç`a(Ÿ±Ç`baxŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`glocatorŸ±Çaoa=Ÿ±ÇbkcdNoneŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dxmaxŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1j2002-02-01Ÿ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`cfmtŸ±Çaoa=Ÿ±ÇbkcdNoneŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`iformatterŸ±Çaoa=Ÿ±ÇbkcdNoneŸ±Ç`a)Ÿ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Çbsdx;"""Set up common parameters for the Axes in the example."""Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`fspinesŸ±Çaoa.Ÿ±Ç`erightŸ±Çaoa.Ÿ±Ç`kset_visibleŸ±Ç`a(Ÿ±ÇbkceFalseŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`fspinesŸ±Çaoa.Ÿ±Ç`dleftŸ±Çaoa.Ÿ±Ç`kset_visibleŸ±Ç`a(Ÿ±ÇbkceFalseŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`fspinesŸ±Çaoa.Ÿ±Ç`ctopŸ±Çaoa.Ÿ±Ç`kset_visibleŸ±Ç`a(Ÿ±ÇbkceFalseŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`eyaxisŸ±Çaoa.Ÿ±Ç`qset_major_locatorŸ±Ç`a(Ÿ±Ç`ftickerŸ±Çaoa.Ÿ±Ç`kNullLocatorŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`ktick_paramsŸ±Ç`a(Ÿ±Ç`ewhichŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1emajorŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ewidthŸ±Çaoa=Ÿ±Çbmfd1.00Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`flengthŸ±Çaoa=Ÿ±Çbmia5Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`ktick_paramsŸ±Ç`a(Ÿ±Ç`ewhichŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1eminorŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ewidthŸ±Çaoa=Ÿ±Çbmfd0.75Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`flengthŸ±Çaoa=Ÿ±Çbmfc2.5Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`hset_xlimŸ±Ç`a(Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`jdatetime64Ÿ±Ç`a(Ÿ±Çbs1a'Ÿ±Çbs1j2000-02-01Ÿ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`jdatetime64Ÿ±Ç`a(Ÿ±Ç`dxmaxŸ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±ÇakbifŸ±Ç`a Ÿ±Ç`glocatorŸ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`exaxisŸ±Çaoa.Ÿ±Ç`qset_major_locatorŸ±Ç`a(Ÿ±ÇbnbdevalŸ±Ç`a(Ÿ±Ç`glocatorŸ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`exaxisŸ±Çaoa.Ÿ±Ç`sset_major_formatterŸ±Ç`a(Ÿ±Ç`mDateFormatterŸ±Ç`a(Ÿ±Ç`cfmtŸ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±ÇakdelseŸ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`exaxisŸ±Çaoa.Ÿ±Ç`sset_major_formatterŸ±Ç`a(Ÿ±ÇbnbdevalŸ±Ç`a(Ÿ±Ç`iformatterŸ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`dtextŸ±Ç`a(Ÿ±Çbmfc0.0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfc0.2Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`glocatorŸ±Ç`a Ÿ±ÇbowborŸ±Ç`a Ÿ±Ç`iformatterŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`itransformŸ±Çaoa=Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`itransAxesŸ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`l            Ÿ±Ç`hfontsizeŸ±Çaoa=Ÿ±Çbmib14Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`hfontnameŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1iMonospaceŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ecolorŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1htab:blueŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`cfigŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`baxŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`hsubplotsŸ±Ç`a(Ÿ±ÇbnbclenŸ±Ç`a(Ÿ±Ç`hlocatorsŸ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`gfigsizeŸ±Çaoa=Ÿ±Ç`a(Ÿ±Çbmia8Ÿ±Ç`a,Ÿ±Ç`a Ÿ±ÇbnbclenŸ±Ç`a(Ÿ±Ç`hlocatorsŸ±Ç`a)Ÿ±Ç`a Ÿ±Çaoa*Ÿ±Ç`a Ÿ±Çbmfb.8Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`w                       Ÿ±Ç`flayoutŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1kconstrainedŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cfigŸ±Çaoa.Ÿ±Ç`hsuptitleŸ±Ç`a(Ÿ±Çbs1a'Ÿ±Çbs1mDate LocatorsŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±ÇakcforŸ±Ç`a Ÿ±Ç`aiŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`clocŸ±Ç`a Ÿ±ÇbowbinŸ±Ç`a Ÿ±ÇbnbienumerateŸ±Ç`a(Ÿ±Ç`hlocatorsŸ±Ç`a)Ÿ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`iplot_axisŸ±Ç`a(Ÿ±Ç`baxŸ±Ç`a[Ÿ±Ç`aiŸ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çaoa*Ÿ±Ç`clocŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`cfigŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`baxŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`hsubplotsŸ±Ç`a(Ÿ±ÇbnbclenŸ±Ç`a(Ÿ±Ç`jformattersŸ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`gfigsizeŸ±Çaoa=Ÿ±Ç`a(Ÿ±Çbmia8Ÿ±Ç`a,Ÿ±Ç`a Ÿ±ÇbnbclenŸ±Ç`a(Ÿ±Ç`jformattersŸ±Ç`a)Ÿ±Ç`a Ÿ±Çaoa*Ÿ±Ç`a Ÿ±Çbmfb.8Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`w                       Ÿ±Ç`flayoutŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1kconstrainedŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cfigŸ±Çaoa.Ÿ±Ç`hsuptitleŸ±Ç`a(Ÿ±Çbs1a'Ÿ±Çbs1oDate FormattersŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±ÇakcforŸ±Ç`a Ÿ±Ç`aiŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`cfmtŸ±Ç`a Ÿ±ÇbowbinŸ±Ç`a Ÿ±ÇbnbienumerateŸ±Ç`a(Ÿ±Ç`jformattersŸ±Ç`a)Ÿ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`iplot_axisŸ±Ç`a(Ÿ±Ç`baxŸ±Ç`a[Ÿ±Ç`aiŸ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`iformatterŸ±Çaoa=Ÿ±Ç`cfmtŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1xM#############################################################################Ÿ±Ç`a
Ÿ±Çbc1a#Ÿ±Ç`a
Ÿ±Çbc1x# .. admonition:: ReferencesŸ±Ç`a
Ÿ±Çbc1a#Ÿ±Ç`a
Ÿ±Çbc1xN#    The use of the following functions, methods, classes and modules is shownŸ±Ç`a
Ÿ±Çbc1u#    in this example:Ÿ±Ç`a
Ÿ±Çbc1a#Ÿ±Ç`a
Ÿ±Çbc1x)#    - `matplotlib.dates.AutoDateLocator`Ÿ±Ç`a
Ÿ±Çbc1x%#    - `matplotlib.dates.YearLocator`Ÿ±Ç`a
Ÿ±Çbc1x&#    - `matplotlib.dates.MonthLocator`Ÿ±Ç`a
Ÿ±Çbc1x$#    - `matplotlib.dates.DayLocator`Ÿ±Ç`a
Ÿ±Çbc1x(#    - `matplotlib.dates.WeekdayLocator`Ÿ±Ç`a
Ÿ±Çbc1x%#    - `matplotlib.dates.HourLocator`Ÿ±Ç`a
Ÿ±Çbc1x'#    - `matplotlib.dates.MinuteLocator`Ÿ±Ç`a
Ÿ±Çbc1x'#    - `matplotlib.dates.SecondLocator`Ÿ±Ç`a
Ÿ±Çbc1x,#    - `matplotlib.dates.MicrosecondLocator`Ÿ±Ç`a
Ÿ±Çbc1x&#    - `matplotlib.dates.RRuleLocator`Ÿ±Ç`a
Ÿ±Çbc1x&#    - `matplotlib.dates.rrulewrapper`Ÿ±Ç`a
Ÿ±Çbc1x'#    - `matplotlib.dates.DateFormatter`Ÿ±Ç`a
Ÿ±Çbc1x+#    - `matplotlib.dates.AutoDateFormatter`Ÿ±Ç`a
Ÿ±Çbc1x.#    - `matplotlib.dates.ConciseDateFormatter`Ÿ±Ç`a
`dNoneˆ