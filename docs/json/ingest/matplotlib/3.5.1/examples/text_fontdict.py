������������bsdyD"""
=======================================================
Controlling style of text and labels using a dictionary
=======================================================

This example shows how to share parameters across many text objects and labels
by creating a dictionary of options passed across several functions.
"""���`a
���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���`a
���`a
���`dfont���`a ���aoa=���`a ���`a{���bs1a'���bs1ffamily���bs1a'���`a:���`a ���bs1a'���bs1eserif���bs1a'���`a,���`a
���`h        ���bs1a'���bs1ecolor���bs1a'���`a:���`b  ���bs1a'���bs1gdarkred���bs1a'���`a,���`a
���`h        ���bs1a'���bs1fweight���bs1a'���`a:���`a ���bs1a'���bs1fnormal���bs1a'���`a,���`a
���`h        ���bs1a'���bs1dsize���bs1a'���`a:���`a ���bmib16���`a,���`a
���`h        ���`a}���`a
���`a
���`ax���`a ���aoa=���`a ���`bnp���aoa.���`hlinspace���`a(���bmfc0.0���`a,���`a ���bmfc5.0���`a,���`a ���bmic100���`a)���`a
���`ay���`a ���aoa=���`a ���`bnp���aoa.���`ccos���`a(���bmia2���aoa*���`bnp���aoa.���`bpi���aoa*���`ax���`a)���`a ���aoa*���`a ���`bnp���aoa.���`cexp���`a(���aoa-���`ax���`a)���`a
���`a
���`cplt���aoa.���`dplot���`a(���`ax���`a,���`a ���`ay���`a,���`a ���bs1a'���bs1ak���bs1a'���`a)���`a
���`cplt���aoa.���`etitle���`a(���bs1a'���bs1xDamped exponential decay���bs1a'���`a,���`a ���`hfontdict���aoa=���`dfont���`a)���`a
���`cplt���aoa.���`dtext���`a(���bmia2���`a,���`a ���bmfd0.65���`a,���`a ���bsaar���bs1a'���bs1a$���bs1a\���bs1fcos(2 ���bs1a\���bs1fpi t) ���bs1a\���bs1hexp(-t)$���bs1a'���`a,���`a ���`hfontdict���aoa=���`dfont���`a)���`a
���`cplt���aoa.���`fxlabel���`a(���bs1a'���bs1htime (s)���bs1a'���`a,���`a ���`hfontdict���aoa=���`dfont���`a)���`a
���`cplt���aoa.���`fylabel���`a(���bs1a'���bs1lvoltage (mV)���bs1a'���`a,���`a ���`hfontdict���aoa=���`dfont���`a)���`a
���`a
���bc1x-# Tweak spacing to prevent clipping of ylabel���`a
���`cplt���aoa.���`osubplots_adjust���`a(���`dleft���aoa=���bmfd0.15���`a)���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
`dNone�