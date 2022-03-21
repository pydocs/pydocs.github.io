Ù¯‚Ù´ƒ™Ù±‚bsdx>"""
=================
Date Demo Convert
=================

"""Ù±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnhdatetimeÙ±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnnfpyplotÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnncpltÙ±‚`a
Ù±‚bkndfromÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnnedatesÙ±‚`a Ù±‚bknfimportÙ±‚`a Ù±‚`jDayLocatorÙ±‚`a,Ù±‚`a Ù±‚`kHourLocatorÙ±‚`a,Ù±‚`a Ù±‚`mDateFormatterÙ±‚`a,Ù±‚`a Ù±‚`fdrangeÙ±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„enumpyÙ „enumpyf1.22.3fmoduleenumpyfmoduleõÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnnbnpÙ±‚`a
Ù±‚`a
Ù±‚`edate1Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`hdatetimeÙ±‚aoa.Ù±‚`hdatetimeÙ±‚`a(Ù±‚bmid2000Ù±‚`a,Ù±‚`a Ù±‚bmia3Ù±‚`a,Ù±‚`a Ù±‚bmia2Ù±‚`a)Ù±‚`a
Ù±‚`edate2Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`hdatetimeÙ±‚aoa.Ù±‚`hdatetimeÙ±‚`a(Ù±‚bmid2000Ù±‚`a,Ù±‚`a Ù±‚bmia3Ù±‚`a,Ù±‚`a Ù±‚bmia6Ù±‚`a)Ù±‚`a
Ù±‚`edeltaÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`hdatetimeÙ±‚aoa.Ù±‚`itimedeltaÙ±‚`a(Ù±‚`ehoursÙ±‚aoa=Ù±‚bmia6Ù±‚`a)Ù±‚`a
Ù±‚`edatesÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`fdrangeÙ±‚`a(Ù±‚`edate1Ù±‚`a,Ù±‚`a Ù±‚`edate2Ù±‚`a,Ù±‚`a Ù±‚`edeltaÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`ayÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`farangeÙ±‚`a(Ù±‚bnbclenÙ±‚`a(Ù±‚`edatesÙ±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`cfigÙ±‚`a,Ù±‚`a Ù±‚`baxÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cpltÙ±‚aoa.Ù±‚`hsubplotsÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`dplotÙ±‚`a(Ù±‚`edatesÙ±‚`a,Ù±‚`a Ù±‚`ayÙ±‚aoa*Ù±‚aoa*Ù±‚bmia2Ù±‚`a,Ù±‚`a Ù±‚bs1a'Ù±‚bs1aoÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚bc1xD# this is superfluous, since the autoscaler should get it right, butÙ±‚`a
Ù±‚bc1xB# use date2num and num2date to convert between dates and floats ifÙ±‚`a
Ù±‚bc1xF# you want; both date2num and num2date convert an instance or sequenceÙ±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`hset_xlimÙ±‚`a(Ù±‚`edatesÙ±‚`a[Ù±‚bmia0Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`edatesÙ±‚`a[Ù±‚aoa-Ù±‚bmia1Ù±‚`a]Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚bc1xB# The hour locator takes the hour or sequence of hours you want toÙ±‚`a
Ù±‚bc1x# tick, not the base multipleÙ±‚`a
Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`exaxisÙ±‚aoa.Ù±‚`qset_major_locatorÙ±‚`a(Ù±‚`jDayLocatorÙ±‚`a(Ù±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`exaxisÙ±‚aoa.Ù±‚`qset_minor_locatorÙ±‚`a(Ù±‚`kHourLocatorÙ±‚`a(Ù±‚bnberangeÙ±‚`a(Ù±‚bmia0Ù±‚`a,Ù±‚`a Ù±‚bmib25Ù±‚`a,Ù±‚`a Ù±‚bmia6Ù±‚`a)Ù±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`exaxisÙ±‚aoa.Ù±‚`sset_major_formatterÙ±‚`a(Ù±‚`mDateFormatterÙ±‚`a(Ù±‚bs1a'Ù±‚bs1a%Ù±‚bs1bY-Ù±‚bs1a%Ù±‚bs1bm-Ù±‚bsib%dÙ±‚bs1a'Ù±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`ifmt_xdataÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`mDateFormatterÙ±‚`a(Ù±‚bs1a'Ù±‚bs1a%Ù±‚bs1bY-Ù±‚bs1a%Ù±‚bs1bm-Ù±‚bsib%dÙ±‚bs1a Ù±‚bs1a%Ù±‚bs1bH:Ù±‚bs1a%Ù±‚bs1bM:Ù±‚bs1a%Ù±‚bs1aSÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`cfigÙ±‚aoa.Ù±‚`mautofmt_xdateÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`cpltÙ±‚aoa.Ù±‚`dshowÙ±‚`a(Ù±‚`a)Ù±‚`a
`dNoneö