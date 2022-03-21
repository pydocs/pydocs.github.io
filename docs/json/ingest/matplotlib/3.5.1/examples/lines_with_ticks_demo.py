������������bsdyI"""
==============================
Lines with a ticked patheffect
==============================

Ticks can be added along a line to mark one side as a barrier using
`~matplotlib.patheffects.TickedStroke`.  You can control the angle,
spacing, and length of the ticks.

The ticks will also appear appropriately in the legend.

"""���`a
���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���bkndfrom���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����`a ���bknfimport���`a ���`kpatheffects���`a
���`a
���`cfig���`a,���`a ���`bax���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`gfigsize���aoa=���`a(���bmia6���`a,���`a ���bmia6���`a)���`a)���`a
���`bax���aoa.���`dplot���`a(���`a[���bmia0���`a,���`a ���bmia1���`a]���`a,���`a ���`a[���bmia0���`a,���`a ���bmia1���`a]���`a,���`a ���`elabel���aoa=���bs2a"���bs2dLine���bs2a"���`a,���`a
���`h        ���`lpath_effects���aoa=���`a[���`kpatheffects���aoa.���`pwithTickedStroke���`a(���`gspacing���aoa=���bmia7���`a,���`a ���`eangle���aoa=���bmic135���`a)���`a]���`a)���`a
���`a
���`bnx���`a ���aoa=���`a ���bmic101���`a
���`ax���`a ���aoa=���`a ���`bnp���aoa.���`hlinspace���`a(���bmfc0.0���`a,���`a ���bmfc1.0���`a,���`a ���`bnx���`a)���`a
���`ay���`a ���aoa=���`a ���bmfc0.3���aoa*���`bnp���aoa.���`csin���`a(���`ax���aoa*���bmia8���`a)���`a ���aoa+���`a ���bmfc0.4���`a
���`bax���aoa.���`dplot���`a(���`ax���`a,���`a ���`ay���`a,���`a ���`elabel���aoa=���bs2a"���bs2eCurve���bs2a"���`a,���`a ���`lpath_effects���aoa=���`a[���`kpatheffects���aoa.���`pwithTickedStroke���`a(���`a)���`a]���`a)���`a
���`a
���`bax���aoa.���`flegend���`a(���`a)���`a
���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
`dNone�