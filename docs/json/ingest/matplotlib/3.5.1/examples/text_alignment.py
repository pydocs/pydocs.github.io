��������l���bsdx�"""
===================
Precise text layout
===================

You can precisely layout text in data or axes coordinates.  This example shows
you some of the alignment and rotation specifications for text layout.
"""���`a
���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���`a
���`cfig���`a,���`a ���`bax���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`a)���`a
���`a
���bc1x"# Build a rectangle in axes coords���`a
���`dleft���`a,���`a ���`ewidth���`a ���aoa=���`a ���bmfc.25���`a,���`a ���bmfb.5���`a
���`fbottom���`a,���`a ���`fheight���`a ���aoa=���`a ���bmfc.25���`a,���`a ���bmfb.5���`a
���`eright���`a ���aoa=���`a ���`dleft���`a ���aoa+���`a ���`ewidth���`a
���`ctop���`a ���aoa=���`a ���`fbottom���`a ���aoa+���`a ���`fheight���`a
���`ap���`a ���aoa=���`a ���`cplt���aoa.���`iRectangle���`a(���`a(���`dleft���`a,���`a ���`fbottom���`a)���`a,���`a ���`ewidth���`a,���`a ���`fheight���`a,���`a ���`dfill���aoa=���bkceFalse���`a)���`a
���`ap���aoa.���`mset_transform���`a(���`bax���aoa.���`itransAxes���`a)���`a
���`ap���aoa.���`kset_clip_on���`a(���bkceFalse���`a)���`a
���`bax���aoa.���`iadd_patch���`a(���`ap���`a)���`a
���`a
���`bax���aoa.���`dtext���`a(���`dleft���`a,���`a ���`fbottom���`a,���`a ���bs1a'���bs1hleft top���bs1a'���`a,���`a
���`h        ���`shorizontalalignment���aoa=���bs1a'���bs1dleft���bs1a'���`a,���`a
���`h        ���`qverticalalignment���aoa=���bs1a'���bs1ctop���bs1a'���`a,���`a
���`h        ���`itransform���aoa=���`bax���aoa.���`itransAxes���`a)���`a
���`a
���`bax���aoa.���`dtext���`a(���`dleft���`a,���`a ���`fbottom���`a,���`a ���bs1a'���bs1kleft bottom���bs1a'���`a,���`a
���`h        ���`shorizontalalignment���aoa=���bs1a'���bs1dleft���bs1a'���`a,���`a
���`h        ���`qverticalalignment���aoa=���bs1a'���bs1fbottom���bs1a'���`a,���`a
���`h        ���`itransform���aoa=���`bax���aoa.���`itransAxes���`a)���`a
���`a
���`bax���aoa.���`dtext���`a(���`eright���`a,���`a ���`ctop���`a,���`a ���bs1a'���bs1lright bottom���bs1a'���`a,���`a
���`h        ���`shorizontalalignment���aoa=���bs1a'���bs1eright���bs1a'���`a,���`a
���`h        ���`qverticalalignment���aoa=���bs1a'���bs1fbottom���bs1a'���`a,���`a
���`h        ���`itransform���aoa=���`bax���aoa.���`itransAxes���`a)���`a
���`a
���`bax���aoa.���`dtext���`a(���`eright���`a,���`a ���`ctop���`a,���`a ���bs1a'���bs1iright top���bs1a'���`a,���`a
���`h        ���`shorizontalalignment���aoa=���bs1a'���bs1eright���bs1a'���`a,���`a
���`h        ���`qverticalalignment���aoa=���bs1a'���bs1ctop���bs1a'���`a,���`a
���`h        ���`itransform���aoa=���`bax���aoa.���`itransAxes���`a)���`a
���`a
���`bax���aoa.���`dtext���`a(���`eright���`a,���`a ���`fbottom���`a,���`a ���bs1a'���bs1jcenter top���bs1a'���`a,���`a
���`h        ���`shorizontalalignment���aoa=���bs1a'���bs1fcenter���bs1a'���`a,���`a
���`h        ���`qverticalalignment���aoa=���bs1a'���bs1ctop���bs1a'���`a,���`a
���`h        ���`itransform���aoa=���`bax���aoa.���`itransAxes���`a)���`a
���`a
���`bax���aoa.���`dtext���`a(���`dleft���`a,���`a ���bmfc0.5���`a ���aoa*���`a ���`a(���`fbottom���`a ���aoa+���`a ���`ctop���`a)���`a,���`a ���bs1a'���bs1lright center���bs1a'���`a,���`a
���`h        ���`shorizontalalignment���aoa=���bs1a'���bs1eright���bs1a'���`a,���`a
���`h        ���`qverticalalignment���aoa=���bs1a'���bs1fcenter���bs1a'���`a,���`a
���`h        ���`hrotation���aoa=���bs1a'���bs1hvertical���bs1a'���`a,���`a
���`h        ���`itransform���aoa=���`bax���aoa.���`itransAxes���`a)���`a
���`a
���`bax���aoa.���`dtext���`a(���`dleft���`a,���`a ���bmfc0.5���`a ���aoa*���`a ���`a(���`fbottom���`a ���aoa+���`a ���`ctop���`a)���`a,���`a ���bs1a'���bs1kleft center���bs1a'���`a,���`a
���`h        ���`shorizontalalignment���aoa=���bs1a'���bs1dleft���bs1a'���`a,���`a
���`h        ���`qverticalalignment���aoa=���bs1a'���bs1fcenter���bs1a'���`a,���`a
���`h        ���`hrotation���aoa=���bs1a'���bs1hvertical���bs1a'���`a,���`a
���`h        ���`itransform���aoa=���`bax���aoa.���`itransAxes���`a)���`a
���`a
���`bax���aoa.���`dtext���`a(���bmfc0.5���`a ���aoa*���`a ���`a(���`dleft���`a ���aoa+���`a ���`eright���`a)���`a,���`a ���bmfc0.5���`a ���aoa*���`a ���`a(���`fbottom���`a ���aoa+���`a ���`ctop���`a)���`a,���`a ���bs1a'���bs1fmiddle���bs1a'���`a,���`a
���`h        ���`shorizontalalignment���aoa=���bs1a'���bs1fcenter���bs1a'���`a,���`a
���`h        ���`qverticalalignment���aoa=���bs1a'���bs1fcenter���bs1a'���`a,���`a
���`h        ���`itransform���aoa=���`bax���aoa.���`itransAxes���`a)���`a
���`a
���`bax���aoa.���`dtext���`a(���`eright���`a,���`a ���bmfc0.5���`a ���aoa*���`a ���`a(���`fbottom���`a ���aoa+���`a ���`ctop���`a)���`a,���`a ���bs1a'���bs1hcentered���bs1a'���`a,���`a
���`h        ���`shorizontalalignment���aoa=���bs1a'���bs1fcenter���bs1a'���`a,���`a
���`h        ���`qverticalalignment���aoa=���bs1a'���bs1fcenter���bs1a'���`a,���`a
���`h        ���`hrotation���aoa=���bs1a'���bs1hvertical���bs1a'���`a,���`a
���`h        ���`itransform���aoa=���`bax���aoa.���`itransAxes���`a)���`a
���`a
���`bax���aoa.���`dtext���`a(���`dleft���`a,���`a ���`ctop���`a,���`a ���bs1a'���bs1grotated���bseb\n���bs1mwith newlines���bs1a'���`a,���`a
���`h        ���`shorizontalalignment���aoa=���bs1a'���bs1fcenter���bs1a'���`a,���`a
���`h        ���`qverticalalignment���aoa=���bs1a'���bs1fcenter���bs1a'���`a,���`a
���`h        ���`hrotation���aoa=���bmib45���`a,���`a
���`h        ���`itransform���aoa=���`bax���aoa.���`itransAxes���`a)���`a
���`a
���`bax���aoa.���`lset_axis_off���`a(���`a)���`a
���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
`dNone�