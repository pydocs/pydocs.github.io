������������bsdy """
===========================
Centered spines with arrows
===========================

This example shows a way to draw a "math textbook" style plot, where the
spines ("axes lines") are drawn at ``x = 0`` and ``y = 0``, and have arrows at
their ends.
"""���`a
���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���`a
���`a
���`cfig���`a,���`a ���`bax���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`a)���`a
���bc1xC# Move the left and bottom spines to x = 0 and y = 0, respectively.���`a
���`bax���aoa.���`fspines���`a[���`a[���bs2a"���bs2dleft���bs2a"���`a,���`a ���bs2a"���bs2fbottom���bs2a"���`a]���`a]���aoa.���`lset_position���`a(���`a(���bs2a"���bs2ddata���bs2a"���`a,���`a ���bmia0���`a)���`a)���`a
���bc1x # Hide the top and right spines.���`a
���`bax���aoa.���`fspines���`a[���`a[���bs2a"���bs2ctop���bs2a"���`a,���`a ���bs2a"���bs2eright���bs2a"���`a]���`a]���aoa.���`kset_visible���`a(���bkceFalse���`a)���`a
���`a
���bc1xN# Draw arrows (as black triangles: ">k"/"^k") at the end of the axes.  In each���`a
���bc1xN# case, one of the coordinates (0) is a data coordinate (i.e., y = 0 or x = 0,���`a
���bc1xN# respectively) and the other one (1) is an axes coordinate (i.e., at the very���`a
���bc1xO# right/top of the axes).  Also, disable clipping (clip_on=False) as the marker���`a
���bc1x"# actually spills out of the axes.���`a
���`bax���aoa.���`dplot���`a(���bmia1���`a,���`a ���bmia0���`a,���`a ���bs2a"���bs2b>k���bs2a"���`a,���`a ���`itransform���aoa=���`bax���aoa.���`sget_yaxis_transform���`a(���`a)���`a,���`a ���`gclip_on���aoa=���bkceFalse���`a)���`a
���`bax���aoa.���`dplot���`a(���bmia0���`a,���`a ���bmia1���`a,���`a ���bs2a"���bs2b^k���bs2a"���`a,���`a ���`itransform���aoa=���`bax���aoa.���`sget_xaxis_transform���`a(���`a)���`a,���`a ���`gclip_on���aoa=���bkceFalse���`a)���`a
���`a
���bc1s# Some sample data.���`a
���`ax���`a ���aoa=���`a ���`bnp���aoa.���`hlinspace���`a(���aoa-���bmfc0.5���`a,���`a ���bmfb1.���`a,���`a ���bmic100���`a)���`a
���`bax���aoa.���`dplot���`a(���`ax���`a,���`a ���`bnp���aoa.���`csin���`a(���`ax���aoa*���`bnp���aoa.���`bpi���`a)���`a)���`a
���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
`dNone�