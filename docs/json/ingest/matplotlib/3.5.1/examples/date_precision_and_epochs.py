��������5���bsdy"""
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

"""���`a
���bknfimport���`a ���bnnhdatetime���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnedates���`a ���akbas���`a ���bnnfmdates���`a
���`a
���`a
���akcdef���`a ���bnfx_reset_epoch_for_tutorial���`a(���`a)���`a:���`a
���`d    ���bsdxn"""
    Users (and downstream libraries) should not use the private method of
    resetting the epoch.
    """���`a
���`d    ���`fmdates���aoa.���`x_reset_epoch_test_example���`a(���`a)���`a
���`a
���`a
���bc1xM#############################################################################���`a
���bc1j# Datetime���`a
���bc1j# --------���`a
���bc1a#���`a
���bc1xE# Python `.datetime` objects have microsecond resolution, so with the���`a
���bc1xL# old default matplotlib dates could not round-trip full-resolution datetime���`a
���bc1j# objects.���`a
���`a
���`iold_epoch���`a ���aoa=���`a ���bs1a'���bs1s0000-12-31T00:00:00���bs1a'���`a
���`inew_epoch���`a ���aoa=���`a ���bs1a'���bs1s1970-01-01T00:00:00���bs1a'���`a
���`a
���`x_reset_epoch_for_tutorial���`a(���`a)���`b  ���bc1x)# Don't do this.  Just for this tutorial.���`a
���`fmdates���aoa.���`iset_epoch���`a(���`iold_epoch���`a)���`b  ���bc1x# old epoch (pre MPL 3.3)���`a
���`a
���`edate1���`a ���aoa=���`a ���`hdatetime���aoa.���`hdatetime���`a(���bmid2000���`a,���`a ���bmia1���`a,���`a ���bmia1���`a,���`a ���bmia0���`a,���`a ���bmib10���`a,���`a ���bmia0���`a,���`a ���bmib12���`a,���`a
���`x                          ���`ftzinfo���aoa=���`hdatetime���aoa.���`htimezone���aoa.���`cutc���`a)���`a
���`fmdate1���`a ���aoa=���`a ���`fmdates���aoa.���`hdate2num���`a(���`edate1���`a)���`a
���bnbeprint���`a(���bs1a'���bs1rBefore Roundtrip: ���bs1a'���`a,���`a ���`edate1���`a,���`a ���bs1a'���bs1pMatplotlib date:���bs1a'���`a,���`a ���`fmdate1���`a)���`a
���`edate2���`a ���aoa=���`a ���`fmdates���aoa.���`hnum2date���`a(���`fmdate1���`a)���`a
���bnbeprint���`a(���bs1a'���bs1rAfter Roundtrip:  ���bs1a'���`a,���`a ���`edate2���`a)���`a
���`a
���bc1xM#############################################################################���`a
���bc1xB# Note this is only a round-off error, and there is no problem for���`a
���bc1x # dates closer to the old epoch:���`a
���`a
���`edate1���`a ���aoa=���`a ���`hdatetime���aoa.���`hdatetime���`a(���bmib10���`a,���`a ���bmia1���`a,���`a ���bmia1���`a,���`a ���bmia0���`a,���`a ���bmib10���`a,���`a ���bmia0���`a,���`a ���bmib12���`a,���`a
���`x                          ���`ftzinfo���aoa=���`hdatetime���aoa.���`htimezone���aoa.���`cutc���`a)���`a
���`fmdate1���`a ���aoa=���`a ���`fmdates���aoa.���`hdate2num���`a(���`edate1���`a)���`a
���bnbeprint���`a(���bs1a'���bs1rBefore Roundtrip: ���bs1a'���`a,���`a ���`edate1���`a,���`a ���bs1a'���bs1pMatplotlib date:���bs1a'���`a,���`a ���`fmdate1���`a)���`a
���`edate2���`a ���aoa=���`a ���`fmdates���aoa.���`hnum2date���`a(���`fmdate1���`a)���`a
���bnbeprint���`a(���bs1a'���bs1rAfter Roundtrip:  ���bs1a'���`a,���`a ���`edate2���`a)���`a
���`a
���bc1xM#############################################################################���`a
���bc1xD# If a user wants to use modern dates at microsecond precision, they���`a
���bc1xH# can change the epoch using `.set_epoch`.  However, the epoch has to be���`a
���bc1xG# set before any date operations to prevent confusion between different���`a
���bc1xG# epochs. Trying to change the epoch later will raise a `RuntimeError`.���`a
���`a
���akctry���`a:���`a
���`d    ���`fmdates���aoa.���`iset_epoch���`a(���`inew_epoch���`a)���`b  ���bc1x"# this is the new MPL 3.3 default.���`a
���akfexcept���`a ���bnelRuntimeError���`a ���akbas���`a ���`ae���`a:���`a
���`d    ���bnbeprint���`a(���bs1a'���bs1mRuntimeError:���bs1a'���`a,���`a ���bnbcstr���`a(���`ae���`a)���`a)���`a
���`a
���bc1xM#############################################################################���`a
���bc1xL# For this tutorial, we reset the sentinel using a private method, but users���`a
���bc1x,# should just set the epoch once, if at all.���`a
���`a
���`x_reset_epoch_for_tutorial���`a(���`a)���`b  ���bc1x$# Just being done for this tutorial.���`a
���`fmdates���aoa.���`iset_epoch���`a(���`inew_epoch���`a)���`a
���`a
���`edate1���`a ���aoa=���`a ���`hdatetime���aoa.���`hdatetime���`a(���bmid2020���`a,���`a ���bmia1���`a,���`a ���bmia1���`a,���`a ���bmia0���`a,���`a ���bmib10���`a,���`a ���bmia0���`a,���`a ���bmib12���`a,���`a
���`x                          ���`ftzinfo���aoa=���`hdatetime���aoa.���`htimezone���aoa.���`cutc���`a)���`a
���`fmdate1���`a ���aoa=���`a ���`fmdates���aoa.���`hdate2num���`a(���`edate1���`a)���`a
���bnbeprint���`a(���bs1a'���bs1rBefore Roundtrip: ���bs1a'���`a,���`a ���`edate1���`a,���`a ���bs1a'���bs1pMatplotlib date:���bs1a'���`a,���`a ���`fmdate1���`a)���`a
���`edate2���`a ���aoa=���`a ���`fmdates���aoa.���`hnum2date���`a(���`fmdate1���`a)���`a
���bnbeprint���`a(���bs1a'���bs1rAfter Roundtrip:  ���bs1a'���`a,���`a ���`edate2���`a)���`a
���`a
���bc1xM#############################################################################���`a
���bc1l# datetime64���`a
���bc1l# ----------���`a
���bc1a#���`a
���bc1xI# `numpy.datetime64` objects have microsecond precision for a much larger���`a
���bc1xL# timespace than `.datetime` objects.  However, currently Matplotlib time is���`a
���bc1xM# only converted back to datetime objects, which have microsecond resolution,���`a
���bc1x(# and years that only span 0000 to 9999.���`a
���`a
���`x_reset_epoch_for_tutorial���`a(���`a)���`b  ���bc1x)# Don't do this.  Just for this tutorial.���`a
���`fmdates���aoa.���`iset_epoch���`a(���`inew_epoch���`a)���`a
���`a
���`edate1���`a ���aoa=���`a ���`bnp���aoa.���`jdatetime64���`a(���bs1a'���bs1x2000-01-01T00:10:00.000012���bs1a'���`a)���`a
���`fmdate1���`a ���aoa=���`a ���`fmdates���aoa.���`hdate2num���`a(���`edate1���`a)���`a
���bnbeprint���`a(���bs1a'���bs1rBefore Roundtrip: ���bs1a'���`a,���`a ���`edate1���`a,���`a ���bs1a'���bs1pMatplotlib date:���bs1a'���`a,���`a ���`fmdate1���`a)���`a
���`edate2���`a ���aoa=���`a ���`fmdates���aoa.���`hnum2date���`a(���`fmdate1���`a)���`a
���bnbeprint���`a(���bs1a'���bs1rAfter Roundtrip:  ���bs1a'���`a,���`a ���`edate2���`a)���`a
���`a
���bc1xM#############################################################################���`a
���bc1j# Plotting���`a
���bc1j# --------���`a
���bc1a#���`a
���bc1xK# This all of course has an effect on plotting.  With the old default epoch���`a
���bc1xM# the times were rounded during the internal ``date2num`` conversion, leading���`a
���bc1w# to jumps in the data:���`a
���`a
���`x_reset_epoch_for_tutorial���`a(���`a)���`b  ���bc1x)# Don't do this.  Just for this tutorial.���`a
���`fmdates���aoa.���`iset_epoch���`a(���`iold_epoch���`a)���`a
���`a
���`ax���`a ���aoa=���`a ���`bnp���aoa.���`farange���`a(���bs1a'���bs1u2000-01-01T00:00:00.0���bs1a'���`a,���`a ���bs1a'���bs1x2000-01-01T00:00:00.000100���bs1a'���`a,���`a
���`n              ���`edtype���aoa=���bs1a'���bs1ndatetime64[us]���bs1a'���`a)���`a
���bc1x2# simulate the plot being made using the old epoch���`a
���`dxold���`a ���aoa=���`a ���`bnp���aoa.���`earray���`a(���`a[���`fmdates���aoa.���`hnum2date���`a(���`fmdates���aoa.���`hdate2num���`a(���`ad���`a)���`a)���`a ���akcfor���`a ���`ad���`a ���bowbin���`a ���`ax���`a]���`a)���`a
���`ay���`a ���aoa=���`a ���`bnp���aoa.���`farange���`a(���bmia0���`a,���`a ���bnbclen���`a(���`ax���`a)���`a)���`a
���`a
���bc1x-# resetting the Epoch so plots are comparable���`a
���`x_reset_epoch_for_tutorial���`a(���`a)���`b  ���bc1x)# Don't do this.  Just for this tutorial.���`a
���`fmdates���aoa.���`iset_epoch���`a(���`inew_epoch���`a)���`a
���`a
���`cfig���`a,���`a ���`bax���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`rconstrained_layout���aoa=���bkcdTrue���`a)���`a
���`bax���aoa.���`dplot���`a(���`dxold���`a,���`a ���`ay���`a)���`a
���`bax���aoa.���`iset_title���`a(���bs1a'���bs1gEpoch: ���bs1a'���`a ���aoa+���`a ���`fmdates���aoa.���`iget_epoch���`a(���`a)���`a)���`a
���`bax���aoa.���`exaxis���aoa.���`oset_tick_params���`a(���`hrotation���aoa=���bmib40���`a)���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
���`a
���bc1xM#############################################################################���`a
���bc1xD# For dates plotted using the more recent epoch, the plot is smooth:���`a
���`a
���`cfig���`a,���`a ���`bax���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`rconstrained_layout���aoa=���bkcdTrue���`a)���`a
���`bax���aoa.���`dplot���`a(���`ax���`a,���`a ���`ay���`a)���`a
���`bax���aoa.���`iset_title���`a(���bs1a'���bs1gEpoch: ���bs1a'���`a ���aoa+���`a ���`fmdates���aoa.���`iget_epoch���`a(���`a)���`a)���`a
���`bax���aoa.���`exaxis���aoa.���`oset_tick_params���`a(���`hrotation���aoa=���bmib40���`a)���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
���`a
���`x_reset_epoch_for_tutorial���`a(���`a)���`b  ���bc1x)# Don't do this.  Just for this tutorial.���`a
���`a
���bc1xM#############################################################################���`a
���bc1a#���`a
���bc1x# .. admonition:: References���`a
���bc1a#���`a
���bc1xN#    The use of the following functions, methods, classes and modules is shown���`a
���bc1u#    in this example:���`a
���bc1a#���`a
���bc1x"#    - `matplotlib.dates.num2date`���`a
���bc1x"#    - `matplotlib.dates.date2num`���`a
���bc1x##    - `matplotlib.dates.set_epoch`���`a
`dNone�