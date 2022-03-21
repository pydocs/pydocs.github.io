��������L���bsdy"""
========================
MATPLOTLIB **UNCHAINED**
========================

Comparative path demonstration of frequency from a fake signal of a pulsar
(mostly known because of the cover for Joy Division's Unknown Pleasures).

Author: Nicolas P. Rougier
"""���`a
���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnianimation���`a ���akbas���`a ���bnnianimation���`a
���`a
���bc1x)# Fixing random state for reproducibility���`a
���`bnp���aoa.���`frandom���aoa.���`dseed���`a(���bmih19680801���`a)���`a
���`a
���`a
���bc1x)# Create new Figure with black background���`a
���`cfig���`a ���aoa=���`a ���`cplt���aoa.���`ffigure���`a(���`gfigsize���aoa=���`a(���bmia8���`a,���`a ���bmia8���`a)���`a,���`a ���`ifacecolor���aoa=���bs1a'���bs1eblack���bs1a'���`a)���`a
���`a
���bc1x# Add a subplot with no frame���`a
���`bax���`a ���aoa=���`a ���`cplt���aoa.���`gsubplot���`a(���`gframeon���aoa=���bkceFalse���`a)���`a
���`a
���bc1v# Generate random data���`a
���`ddata���`a ���aoa=���`a ���`bnp���aoa.���`frandom���aoa.���`guniform���`a(���bmia0���`a,���`a ���bmia1���`a,���`a ���`a(���bmib64���`a,���`a ���bmib75���`a)���`a)���`a
���`aX���`a ���aoa=���`a ���`bnp���aoa.���`hlinspace���`a(���aoa-���bmia1���`a,���`a ���bmia1���`a,���`a ���`ddata���aoa.���`eshape���`a[���aoa-���bmia1���`a]���`a)���`a
���`aG���`a ���aoa=���`a ���bmfc1.5���`a ���aoa*���`a ���`bnp���aoa.���`cexp���`a(���aoa-���bmia4���`a ���aoa*���`a ���`aX���`a ���aoa*���aoa*���`a ���bmia2���`a)���`a
���`a
���bc1u# Generate line plots���`a
���`elines���`a ���aoa=���`a ���`a[���`a]���`a
���akcfor���`a ���`ai���`a ���bowbin���`a ���bnberange���`a(���bnbclen���`a(���`ddata���`a)���`a)���`a:���`a
���`d    ���bc1xD# Small reduction of the X extents to get a cheap perspective effect���`a
���`d    ���`fxscale���`a ���aoa=���`a ���bmia1���`a ���aoa-���`a ���`ai���`a ���aoa/���`a ���bmfd200.���`a
���`d    ���bc1x0# Same for linewidth (thicker strokes on bottom)���`a
���`d    ���`blw���`a ���aoa=���`a ���bmfc1.5���`a ���aoa-���`a ���`ai���`a ���aoa/���`a ���bmfe100.0���`a
���`d    ���`dline���`a,���`a ���aoa=���`a ���`bax���aoa.���`dplot���`a(���`fxscale���`a ���aoa*���`a ���`aX���`a,���`a ���`ai���`a ���aoa+���`a ���`aG���`a ���aoa*���`a ���`ddata���`a[���`ai���`a]���`a,���`a ���`ecolor���aoa=���bs2a"���bs2aw���bs2a"���`a,���`a ���`blw���aoa=���`blw���`a)���`a
���`d    ���`elines���aoa.���`fappend���`a(���`dline���`a)���`a
���`a
���bc1x=# Set y limit (or first line is cropped because of thickness)���`a
���`bax���aoa.���`hset_ylim���`a(���aoa-���bmia1���`a,���`a ���bmib70���`a)���`a
���`a
���bc1j# No ticks���`a
���`bax���aoa.���`jset_xticks���`a(���`a[���`a]���`a)���`a
���`bax���aoa.���`jset_yticks���`a(���`a[���`a]���`a)���`a
���`a
���bc1x-# 2 part titles to get different font weights���`a
���`bax���aoa.���`dtext���`a(���bmfc0.5���`a,���`a ���bmfc1.0���`a,���`a ���bs2a"���bs2kMATPLOTLIB ���bs2a"���`a,���`a ���`itransform���aoa=���`bax���aoa.���`itransAxes���`a,���`a
���`h        ���`bha���aoa=���bs2a"���bs2eright���bs2a"���`a,���`a ���`bva���aoa=���bs2a"���bs2fbottom���bs2a"���`a,���`a ���`ecolor���aoa=���bs2a"���bs2aw���bs2a"���`a,���`a
���`h        ���`ffamily���aoa=���bs2a"���bs2jsans-serif���bs2a"���`a,���`a ���`jfontweight���aoa=���bs2a"���bs2elight���bs2a"���`a,���`a ���`hfontsize���aoa=���bmib16���`a)���`a
���`bax���aoa.���`dtext���`a(���bmfc0.5���`a,���`a ���bmfc1.0���`a,���`a ���bs2a"���bs2iUNCHAINED���bs2a"���`a,���`a ���`itransform���aoa=���`bax���aoa.���`itransAxes���`a,���`a
���`h        ���`bha���aoa=���bs2a"���bs2dleft���bs2a"���`a,���`a ���`bva���aoa=���bs2a"���bs2fbottom���bs2a"���`a,���`a ���`ecolor���aoa=���bs2a"���bs2aw���bs2a"���`a,���`a
���`h        ���`ffamily���aoa=���bs2a"���bs2jsans-serif���bs2a"���`a,���`a ���`jfontweight���aoa=���bs2a"���bs2dbold���bs2a"���`a,���`a ���`hfontsize���aoa=���bmib16���`a)���`a
���`a
���`a
���akcdef���`a ���bnffupdate���`a(���aoa*���`dargs���`a)���`a:���`a
���`d    ���bc1x# Shift all data to the right���`a
���`d    ���`ddata���`a[���`a:���`a,���`a ���bmia1���`a:���`a]���`a ���aoa=���`a ���`ddata���`a[���`a:���`a,���`a ���`a:���aoa-���bmia1���`a]���`a
���`a
���`d    ���bc1t# Fill-in new values���`a
���`d    ���`ddata���`a[���`a:���`a,���`a ���bmia0���`a]���`a ���aoa=���`a ���`bnp���aoa.���`frandom���aoa.���`guniform���`a(���bmia0���`a,���`a ���bmia1���`a,���`a ���bnbclen���`a(���`ddata���`a)���`a)���`a
���`a
���`d    ���bc1m# Update data���`a
���`d    ���akcfor���`a ���`ai���`a ���bowbin���`a ���bnberange���`a(���bnbclen���`a(���`ddata���`a)���`a)���`a:���`a
���`h        ���`elines���`a[���`ai���`a]���aoa.���`iset_ydata���`a(���`ai���`a ���aoa+���`a ���`aG���`a ���aoa*���`a ���`ddata���`a[���`ai���`a]���`a)���`a
���`a
���`d    ���bc1x# Return modified artists���`a
���`d    ���akfreturn���`a ���`elines���`a
���`a
���bc1xO# Construct the animation, using the update function as the animation director.���`a
���`danim���`a ���aoa=���`a ���`ianimation���aoa.���`mFuncAnimation���`a(���`cfig���`a,���`a ���`fupdate���`a,���`a ���`hinterval���aoa=���bmib10���`a)���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
`dNone�