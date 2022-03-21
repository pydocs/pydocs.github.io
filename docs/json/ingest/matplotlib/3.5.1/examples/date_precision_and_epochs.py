ŸØÇÅŸ¥Éô5Ÿ±Çbsdy"""
=========================
Date Precision and Epochs
=========================

Matplotlib can handle `.datetime` objects and `numpy.datetime64` objects using
a unit converter that recognizes these dates and converts them to floating
point numbers.

Before Matplotlib 3.3, the default for this conversion returns a float that was
days since "0000-12-31T00:00:00".  As of Matplotlib 3.3, the default is
days from "1970-01-01T00:00:00".  This allows more resolution for modern
dates.  "2020-01-01" with the old epoch converted to 730120, and a 64-bit
floating point number has a resolution of 2^{-52}, or approximately
14 microseconds, so microsecond precision was lost.  With the new default
epoch "2020-01-01" is 10957.0, so the achievable resolution is 0.21
microseconds.

"""Ÿ±Ç`a
Ÿ±ÇbknfimportŸ±Ç`a Ÿ±ÇbnnhdatetimeŸ±Ç`a
Ÿ±ÇbknfimportŸ±Ç`a Ÿ±ÇbnnŸ¢ÑenumpyŸ†Ñenumpyf1.22.3fmoduleenumpyfmoduleıŸ±Ç`a Ÿ±ÇakbasŸ±Ç`a Ÿ±ÇbnnbnpŸ±Ç`a
Ÿ±Ç`a
Ÿ±ÇbknfimportŸ±Ç`a Ÿ±ÇbnnŸ¢ÑjmatplotlibŸ†Ñjmatplotlibe3.5.1fmodulejmatplotlibfmoduleıŸ±Çbnna.Ÿ±ÇbnnfpyplotŸ±Ç`a Ÿ±ÇakbasŸ±Ç`a Ÿ±ÇbnncpltŸ±Ç`a
Ÿ±ÇbknfimportŸ±Ç`a Ÿ±ÇbnnŸ¢ÑjmatplotlibŸ†Ñjmatplotlibe3.5.1fmodulejmatplotlibfmoduleıŸ±Çbnna.Ÿ±ÇbnnedatesŸ±Ç`a Ÿ±ÇakbasŸ±Ç`a Ÿ±ÇbnnfmdatesŸ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±ÇakcdefŸ±Ç`a Ÿ±Çbnfx_reset_epoch_for_tutorialŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Çbsdxn"""
    Users (and downstream libraries) should not use the private method of
    resetting the epoch.
    """Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`fmdatesŸ±Çaoa.Ÿ±Ç`x_reset_epoch_test_exampleŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1xM#############################################################################Ÿ±Ç`a
Ÿ±Çbc1j# DatetimeŸ±Ç`a
Ÿ±Çbc1j# --------Ÿ±Ç`a
Ÿ±Çbc1a#Ÿ±Ç`a
Ÿ±Çbc1xE# Python `.datetime` objects have microsecond resolution, so with theŸ±Ç`a
Ÿ±Çbc1xL# old default matplotlib dates could not round-trip full-resolution datetimeŸ±Ç`a
Ÿ±Çbc1j# objects.Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`iold_epochŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1s0000-12-31T00:00:00Ÿ±Çbs1a'Ÿ±Ç`a
Ÿ±Ç`inew_epochŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1s1970-01-01T00:00:00Ÿ±Çbs1a'Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`x_reset_epoch_for_tutorialŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`b  Ÿ±Çbc1x)# Don't do this.  Just for this tutorial.Ÿ±Ç`a
Ÿ±Ç`fmdatesŸ±Çaoa.Ÿ±Ç`iset_epochŸ±Ç`a(Ÿ±Ç`iold_epochŸ±Ç`a)Ÿ±Ç`b  Ÿ±Çbc1x# old epoch (pre MPL 3.3)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`edate1Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`hdatetimeŸ±Çaoa.Ÿ±Ç`hdatetimeŸ±Ç`a(Ÿ±Çbmid2000Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmib10Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmib12Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`x                          Ÿ±Ç`ftzinfoŸ±Çaoa=Ÿ±Ç`hdatetimeŸ±Çaoa.Ÿ±Ç`htimezoneŸ±Çaoa.Ÿ±Ç`cutcŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`fmdate1Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`fmdatesŸ±Çaoa.Ÿ±Ç`hdate2numŸ±Ç`a(Ÿ±Ç`edate1Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±ÇbnbeprintŸ±Ç`a(Ÿ±Çbs1a'Ÿ±Çbs1rBefore Roundtrip: Ÿ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`edate1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1pMatplotlib date:Ÿ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`fmdate1Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`edate2Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`fmdatesŸ±Çaoa.Ÿ±Ç`hnum2dateŸ±Ç`a(Ÿ±Ç`fmdate1Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±ÇbnbeprintŸ±Ç`a(Ÿ±Çbs1a'Ÿ±Çbs1rAfter Roundtrip:  Ÿ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`edate2Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1xM#############################################################################Ÿ±Ç`a
Ÿ±Çbc1xB# Note this is only a round-off error, and there is no problem forŸ±Ç`a
Ÿ±Çbc1x # dates closer to the old epoch:Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`edate1Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`hdatetimeŸ±Çaoa.Ÿ±Ç`hdatetimeŸ±Ç`a(Ÿ±Çbmib10Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmib10Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmib12Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`x                          Ÿ±Ç`ftzinfoŸ±Çaoa=Ÿ±Ç`hdatetimeŸ±Çaoa.Ÿ±Ç`htimezoneŸ±Çaoa.Ÿ±Ç`cutcŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`fmdate1Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`fmdatesŸ±Çaoa.Ÿ±Ç`hdate2numŸ±Ç`a(Ÿ±Ç`edate1Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±ÇbnbeprintŸ±Ç`a(Ÿ±Çbs1a'Ÿ±Çbs1rBefore Roundtrip: Ÿ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`edate1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1pMatplotlib date:Ÿ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`fmdate1Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`edate2Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`fmdatesŸ±Çaoa.Ÿ±Ç`hnum2dateŸ±Ç`a(Ÿ±Ç`fmdate1Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±ÇbnbeprintŸ±Ç`a(Ÿ±Çbs1a'Ÿ±Çbs1rAfter Roundtrip:  Ÿ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`edate2Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1xM#############################################################################Ÿ±Ç`a
Ÿ±Çbc1xD# If a user wants to use modern dates at microsecond precision, theyŸ±Ç`a
Ÿ±Çbc1xH# can change the epoch using `.set_epoch`.  However, the epoch has to beŸ±Ç`a
Ÿ±Çbc1xG# set before any date operations to prevent confusion between differentŸ±Ç`a
Ÿ±Çbc1xG# epochs. Trying to change the epoch later will raise a `RuntimeError`.Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±ÇakctryŸ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`fmdatesŸ±Çaoa.Ÿ±Ç`iset_epochŸ±Ç`a(Ÿ±Ç`inew_epochŸ±Ç`a)Ÿ±Ç`b  Ÿ±Çbc1x"# this is the new MPL 3.3 default.Ÿ±Ç`a
Ÿ±ÇakfexceptŸ±Ç`a Ÿ±ÇbnelRuntimeErrorŸ±Ç`a Ÿ±ÇakbasŸ±Ç`a Ÿ±Ç`aeŸ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±ÇbnbeprintŸ±Ç`a(Ÿ±Çbs1a'Ÿ±Çbs1mRuntimeError:Ÿ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±ÇbnbcstrŸ±Ç`a(Ÿ±Ç`aeŸ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1xM#############################################################################Ÿ±Ç`a
Ÿ±Çbc1xL# For this tutorial, we reset the sentinel using a private method, but usersŸ±Ç`a
Ÿ±Çbc1x,# should just set the epoch once, if at all.Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`x_reset_epoch_for_tutorialŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`b  Ÿ±Çbc1x$# Just being done for this tutorial.Ÿ±Ç`a
Ÿ±Ç`fmdatesŸ±Çaoa.Ÿ±Ç`iset_epochŸ±Ç`a(Ÿ±Ç`inew_epochŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`edate1Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`hdatetimeŸ±Çaoa.Ÿ±Ç`hdatetimeŸ±Ç`a(Ÿ±Çbmid2020Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmib10Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmib12Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`x                          Ÿ±Ç`ftzinfoŸ±Çaoa=Ÿ±Ç`hdatetimeŸ±Çaoa.Ÿ±Ç`htimezoneŸ±Çaoa.Ÿ±Ç`cutcŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`fmdate1Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`fmdatesŸ±Çaoa.Ÿ±Ç`hdate2numŸ±Ç`a(Ÿ±Ç`edate1Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±ÇbnbeprintŸ±Ç`a(Ÿ±Çbs1a'Ÿ±Çbs1rBefore Roundtrip: Ÿ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`edate1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1pMatplotlib date:Ÿ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`fmdate1Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`edate2Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`fmdatesŸ±Çaoa.Ÿ±Ç`hnum2dateŸ±Ç`a(Ÿ±Ç`fmdate1Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±ÇbnbeprintŸ±Ç`a(Ÿ±Çbs1a'Ÿ±Çbs1rAfter Roundtrip:  Ÿ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`edate2Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1xM#############################################################################Ÿ±Ç`a
Ÿ±Çbc1l# datetime64Ÿ±Ç`a
Ÿ±Çbc1l# ----------Ÿ±Ç`a
Ÿ±Çbc1a#Ÿ±Ç`a
Ÿ±Çbc1xI# `numpy.datetime64` objects have microsecond precision for a much largerŸ±Ç`a
Ÿ±Çbc1xL# timespace than `.datetime` objects.  However, currently Matplotlib time isŸ±Ç`a
Ÿ±Çbc1xM# only converted back to datetime objects, which have microsecond resolution,Ÿ±Ç`a
Ÿ±Çbc1x(# and years that only span 0000 to 9999.Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`x_reset_epoch_for_tutorialŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`b  Ÿ±Çbc1x)# Don't do this.  Just for this tutorial.Ÿ±Ç`a
Ÿ±Ç`fmdatesŸ±Çaoa.Ÿ±Ç`iset_epochŸ±Ç`a(Ÿ±Ç`inew_epochŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`edate1Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`jdatetime64Ÿ±Ç`a(Ÿ±Çbs1a'Ÿ±Çbs1x2000-01-01T00:10:00.000012Ÿ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`fmdate1Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`fmdatesŸ±Çaoa.Ÿ±Ç`hdate2numŸ±Ç`a(Ÿ±Ç`edate1Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±ÇbnbeprintŸ±Ç`a(Ÿ±Çbs1a'Ÿ±Çbs1rBefore Roundtrip: Ÿ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`edate1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1pMatplotlib date:Ÿ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`fmdate1Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`edate2Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`fmdatesŸ±Çaoa.Ÿ±Ç`hnum2dateŸ±Ç`a(Ÿ±Ç`fmdate1Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±ÇbnbeprintŸ±Ç`a(Ÿ±Çbs1a'Ÿ±Çbs1rAfter Roundtrip:  Ÿ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`edate2Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1xM#############################################################################Ÿ±Ç`a
Ÿ±Çbc1j# PlottingŸ±Ç`a
Ÿ±Çbc1j# --------Ÿ±Ç`a
Ÿ±Çbc1a#Ÿ±Ç`a
Ÿ±Çbc1xK# This all of course has an effect on plotting.  With the old default epochŸ±Ç`a
Ÿ±Çbc1xM# the times were rounded during the internal ``date2num`` conversion, leadingŸ±Ç`a
Ÿ±Çbc1w# to jumps in the data:Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`x_reset_epoch_for_tutorialŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`b  Ÿ±Çbc1x)# Don't do this.  Just for this tutorial.Ÿ±Ç`a
Ÿ±Ç`fmdatesŸ±Çaoa.Ÿ±Ç`iset_epochŸ±Ç`a(Ÿ±Ç`iold_epochŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`axŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`farangeŸ±Ç`a(Ÿ±Çbs1a'Ÿ±Çbs1u2000-01-01T00:00:00.0Ÿ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1x2000-01-01T00:00:00.000100Ÿ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`n              Ÿ±Ç`edtypeŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1ndatetime64[us]Ÿ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Çbc1x2# simulate the plot being made using the old epochŸ±Ç`a
Ÿ±Ç`dxoldŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`earrayŸ±Ç`a(Ÿ±Ç`a[Ÿ±Ç`fmdatesŸ±Çaoa.Ÿ±Ç`hnum2dateŸ±Ç`a(Ÿ±Ç`fmdatesŸ±Çaoa.Ÿ±Ç`hdate2numŸ±Ç`a(Ÿ±Ç`adŸ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a Ÿ±ÇakcforŸ±Ç`a Ÿ±Ç`adŸ±Ç`a Ÿ±ÇbowbinŸ±Ç`a Ÿ±Ç`axŸ±Ç`a]Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`ayŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`farangeŸ±Ç`a(Ÿ±Çbmia0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±ÇbnbclenŸ±Ç`a(Ÿ±Ç`axŸ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1x-# resetting the Epoch so plots are comparableŸ±Ç`a
Ÿ±Ç`x_reset_epoch_for_tutorialŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`b  Ÿ±Çbc1x)# Don't do this.  Just for this tutorial.Ÿ±Ç`a
Ÿ±Ç`fmdatesŸ±Çaoa.Ÿ±Ç`iset_epochŸ±Ç`a(Ÿ±Ç`inew_epochŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`cfigŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`baxŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`hsubplotsŸ±Ç`a(Ÿ±Ç`rconstrained_layoutŸ±Çaoa=Ÿ±ÇbkcdTrueŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`dplotŸ±Ç`a(Ÿ±Ç`dxoldŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ayŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`iset_titleŸ±Ç`a(Ÿ±Çbs1a'Ÿ±Çbs1gEpoch: Ÿ±Çbs1a'Ÿ±Ç`a Ÿ±Çaoa+Ÿ±Ç`a Ÿ±Ç`fmdatesŸ±Çaoa.Ÿ±Ç`iget_epochŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`exaxisŸ±Çaoa.Ÿ±Ç`oset_tick_paramsŸ±Ç`a(Ÿ±Ç`hrotationŸ±Çaoa=Ÿ±Çbmib40Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`dshowŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1xM#############################################################################Ÿ±Ç`a
Ÿ±Çbc1xD# For dates plotted using the more recent epoch, the plot is smooth:Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`cfigŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`baxŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`hsubplotsŸ±Ç`a(Ÿ±Ç`rconstrained_layoutŸ±Çaoa=Ÿ±ÇbkcdTrueŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`dplotŸ±Ç`a(Ÿ±Ç`axŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ayŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`iset_titleŸ±Ç`a(Ÿ±Çbs1a'Ÿ±Çbs1gEpoch: Ÿ±Çbs1a'Ÿ±Ç`a Ÿ±Çaoa+Ÿ±Ç`a Ÿ±Ç`fmdatesŸ±Çaoa.Ÿ±Ç`iget_epochŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`exaxisŸ±Çaoa.Ÿ±Ç`oset_tick_paramsŸ±Ç`a(Ÿ±Ç`hrotationŸ±Çaoa=Ÿ±Çbmib40Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`dshowŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`x_reset_epoch_for_tutorialŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`b  Ÿ±Çbc1x)# Don't do this.  Just for this tutorial.Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1xM#############################################################################Ÿ±Ç`a
Ÿ±Çbc1a#Ÿ±Ç`a
Ÿ±Çbc1x# .. admonition:: ReferencesŸ±Ç`a
Ÿ±Çbc1a#Ÿ±Ç`a
Ÿ±Çbc1xN#    The use of the following functions, methods, classes and modules is shownŸ±Ç`a
Ÿ±Çbc1u#    in this example:Ÿ±Ç`a
Ÿ±Çbc1a#Ÿ±Ç`a
Ÿ±Çbc1x"#    - `matplotlib.dates.num2date`Ÿ±Ç`a
Ÿ±Çbc1x"#    - `matplotlib.dates.date2num`Ÿ±Ç`a
Ÿ±Çbc1x##    - `matplotlib.dates.set_epoch`Ÿ±Ç`a
`dNoneˆ