�����������bsdx>"""
=================
Date Demo Convert
=================

"""���`a
���bknfimport���`a ���bnnhdatetime���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���bkndfrom���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnedates���`a ���bknfimport���`a ���`jDayLocator���`a,���`a ���`kHourLocator���`a,���`a ���`mDateFormatter���`a,���`a ���`fdrange���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���`a
���`edate1���`a ���aoa=���`a ���`hdatetime���aoa.���`hdatetime���`a(���bmid2000���`a,���`a ���bmia3���`a,���`a ���bmia2���`a)���`a
���`edate2���`a ���aoa=���`a ���`hdatetime���aoa.���`hdatetime���`a(���bmid2000���`a,���`a ���bmia3���`a,���`a ���bmia6���`a)���`a
���`edelta���`a ���aoa=���`a ���`hdatetime���aoa.���`itimedelta���`a(���`ehours���aoa=���bmia6���`a)���`a
���`edates���`a ���aoa=���`a ���`fdrange���`a(���`edate1���`a,���`a ���`edate2���`a,���`a ���`edelta���`a)���`a
���`a
���`ay���`a ���aoa=���`a ���`bnp���aoa.���`farange���`a(���bnbclen���`a(���`edates���`a)���`a)���`a
���`a
���`cfig���`a,���`a ���`bax���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`a)���`a
���`bax���aoa.���`dplot���`a(���`edates���`a,���`a ���`ay���aoa*���aoa*���bmia2���`a,���`a ���bs1a'���bs1ao���bs1a'���`a)���`a
���`a
���bc1xD# this is superfluous, since the autoscaler should get it right, but���`a
���bc1xB# use date2num and num2date to convert between dates and floats if���`a
���bc1xF# you want; both date2num and num2date convert an instance or sequence���`a
���`bax���aoa.���`hset_xlim���`a(���`edates���`a[���bmia0���`a]���`a,���`a ���`edates���`a[���aoa-���bmia1���`a]���`a)���`a
���`a
���bc1xB# The hour locator takes the hour or sequence of hours you want to���`a
���bc1x# tick, not the base multiple���`a
���`a
���`bax���aoa.���`exaxis���aoa.���`qset_major_locator���`a(���`jDayLocator���`a(���`a)���`a)���`a
���`bax���aoa.���`exaxis���aoa.���`qset_minor_locator���`a(���`kHourLocator���`a(���bnberange���`a(���bmia0���`a,���`a ���bmib25���`a,���`a ���bmia6���`a)���`a)���`a)���`a
���`bax���aoa.���`exaxis���aoa.���`sset_major_formatter���`a(���`mDateFormatter���`a(���bs1a'���bs1a%���bs1bY-���bs1a%���bs1bm-���bsib%d���bs1a'���`a)���`a)���`a
���`a
���`bax���aoa.���`ifmt_xdata���`a ���aoa=���`a ���`mDateFormatter���`a(���bs1a'���bs1a%���bs1bY-���bs1a%���bs1bm-���bsib%d���bs1a ���bs1a%���bs1bH:���bs1a%���bs1bM:���bs1a%���bs1aS���bs1a'���`a)���`a
���`cfig���aoa.���`mautofmt_xdate���`a(���`a)���`a
���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
`dNone�