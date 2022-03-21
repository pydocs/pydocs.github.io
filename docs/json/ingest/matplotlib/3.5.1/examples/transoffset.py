��������l���bsdy�"""
======================
transforms.offset_copy
======================

This illustrates the use of `.transforms.offset_copy` to
make a transform that positions a drawing element such as
a text string at a specified offset in screen coordinates
(dots or inches) relative to a location given in any
coordinates.

Every Artist (Text, Line2D, etc.) has a transform that can be
set when the Artist is created, such as by the corresponding
pyplot function.  By default this is usually the Axes.transData
transform, going from data units to screen pixels.  We can
use the `.offset_copy` function to make a modified copy of
this transform, where the modification consists of an
offset.
"""���`a
���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnjtransforms���`a ���akbas���`a ���bnnkmtransforms���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���`a
���`a
���`bxs���`a ���aoa=���`a ���`bnp���aoa.���`farange���`a(���bmia7���`a)���`a
���`bys���`a ���aoa=���`a ���`bxs���aoa*���aoa*���bmia2���`a
���`a
���`cfig���`a ���aoa=���`a ���`cplt���aoa.���`ffigure���`a(���`gfigsize���aoa=���`a(���bmia5���`a,���`a ���bmib10���`a)���`a)���`a
���`bax���`a ���aoa=���`a ���`cplt���aoa.���`gsubplot���`a(���bmia2���`a,���`a ���bmia1���`a,���`a ���bmia1���`a)���`a
���`a
���bc1x4# If we want the same offset for each text instance,���`a
���bc1x1# we only need to make one transform.  To get the���`a
���bc1x=# transform argument to offset_copy, we need to make the axes���`a
���bc1x:# first; the subplot function above is one way to do this.���`a
���`ltrans_offset���`a ���aoa=���`a ���`kmtransforms���aoa.���`koffset_copy���`a(���`bax���aoa.���`itransData���`a,���`a ���`cfig���aoa=���`cfig���`a,���`a
���`x'                                       ���`ax���aoa=���bmfd0.05���`a,���`a ���`ay���aoa=���bmfd0.10���`a,���`a ���`eunits���aoa=���bs1a'���bs1finches���bs1a'���`a)���`a
���`a
���akcfor���`a ���`ax���`a,���`a ���`ay���`a ���bowbin���`a ���bnbczip���`a(���`bxs���`a,���`a ���`bys���`a)���`a:���`a
���`d    ���`cplt���aoa.���`dplot���`a(���`ax���`a,���`a ���`ay���`a,���`a ���bs1a'���bs1bro���bs1a'���`a)���`a
���`d    ���`cplt���aoa.���`dtext���`a(���`ax���`a,���`a ���`ay���`a,���`a ���bs1a'���bsib%d���bs1b, ���bsib%d���bs1a'���`a ���aoa%���`a ���`a(���bnbcint���`a(���`ax���`a)���`a,���`a ���bnbcint���`a(���`ay���`a)���`a)���`a,���`a ���`itransform���aoa=���`ltrans_offset���`a)���`a
���`a
���`a
���bc1x)# offset_copy works for polar plots also.���`a
���`bax���`a ���aoa=���`a ���`cplt���aoa.���`gsubplot���`a(���bmia2���`a,���`a ���bmia1���`a,���`a ���bmia2���`a,���`a ���`jprojection���aoa=���bs1a'���bs1epolar���bs1a'���`a)���`a
���`a
���`ltrans_offset���`a ���aoa=���`a ���`kmtransforms���aoa.���`koffset_copy���`a(���`bax���aoa.���`itransData���`a,���`a ���`cfig���aoa=���`cfig���`a,���`a
���`x'                                       ���`ay���aoa=���bmia6���`a,���`a ���`eunits���aoa=���bs1a'���bs1ddots���bs1a'���`a)���`a
���`a
���akcfor���`a ���`ax���`a,���`a ���`ay���`a ���bowbin���`a ���bnbczip���`a(���`bxs���`a,���`a ���`bys���`a)���`a:���`a
���`d    ���`cplt���aoa.���`epolar���`a(���`ax���`a,���`a ���`ay���`a,���`a ���bs1a'���bs1bro���bs1a'���`a)���`a
���`d    ���`cplt���aoa.���`dtext���`a(���`ax���`a,���`a ���`ay���`a,���`a ���bs1a'���bsib%d���bs1b, ���bsib%d���bs1a'���`a ���aoa%���`a ���`a(���bnbcint���`a(���`ax���`a)���`a,���`a ���bnbcint���`a(���`ay���`a)���`a)���`a,���`a
���`m             ���`itransform���aoa=���`ltrans_offset���`a,���`a
���`m             ���`shorizontalalignment���aoa=���bs1a'���bs1fcenter���bs1a'���`a,���`a
���`m             ���`qverticalalignment���aoa=���bs1a'���bs1fbottom���bs1a'���`a)���`a
���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
`dNone�