��������%���bsdx�"""
===================
Custom spine bounds
===================

Demo of spines using custom bounds to limit the extent of the spine.
"""���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���`a
���bc1x)# Fixing random state for reproducibility���`a
���`bnp���aoa.���`frandom���aoa.���`dseed���`a(���bmih19680801���`a)���`a
���`a
���`ax���`a ���aoa=���`a ���`bnp���aoa.���`hlinspace���`a(���bmia0���`a,���`a ���bmia2���aoa*���`bnp���aoa.���`bpi���`a,���`a ���bmib50���`a)���`a
���`ay���`a ���aoa=���`a ���`bnp���aoa.���`csin���`a(���`ax���`a)���`a
���`by2���`a ���aoa=���`a ���`ay���`a ���aoa+���`a ���bmfc0.1���`a ���aoa*���`a ���`bnp���aoa.���`frandom���aoa.���`fnormal���`a(���`dsize���aoa=���`ax���aoa.���`eshape���`a)���`a
���`a
���`cfig���`a,���`a ���`bax���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`a)���`a
���`bax���aoa.���`dplot���`a(���`ax���`a,���`a ���`ay���`a)���`a
���`bax���aoa.���`dplot���`a(���`ax���`a,���`a ���`by2���`a)���`a
���`a
���bc1x# set ticks and tick labels���`a
���`bax���aoa.���`hset_xlim���`a(���`a(���bmia0���`a,���`a ���bmia2���aoa*���`bnp���aoa.���`bpi���`a)���`a)���`a
���`bax���aoa.���`jset_xticks���`a(���`a[���bmia0���`a,���`a ���`bnp���aoa.���`bpi���`a,���`a ���bmia2���aoa*���`bnp���aoa.���`bpi���`a]���`a,���`a ���`flabels���aoa=���`a[���bs1a'���bs1a0���bs1a'���`a,���`a ���bsaar���bs1a'���bs1a$���bs1a\���bs1cpi$���bs1a'���`a,���`a ���bsaar���bs1a'���bs1b2$���bs1a\���bs1cpi$���bs1a'���`a]���`a)���`a
���`bax���aoa.���`hset_ylim���`a(���`a(���aoa-���bmfc1.5���`a,���`a ���bmfc1.5���`a)���`a)���`a
���`bax���aoa.���`jset_yticks���`a(���`a[���aoa-���bmia1���`a,���`a ���bmia0���`a,���`a ���bmia1���`a]���`a)���`a
���`a
���bc1x%# Only draw spine between the y-ticks���`a
���`bax���aoa.���`fspines���aoa.���`dleft���aoa.���`jset_bounds���`a(���`a(���aoa-���bmia1���`a,���`a ���bmia1���`a)���`a)���`a
���bc1x# Hide the right and top spines���`a
���`bax���aoa.���`fspines���aoa.���`eright���aoa.���`kset_visible���`a(���bkceFalse���`a)���`a
���`bax���aoa.���`fspines���aoa.���`ctop���aoa.���`kset_visible���`a(���bkceFalse���`a)���`a
���bc1x/# Only show ticks on the left and bottom spines���`a
���`bax���aoa.���`eyaxis���aoa.���`rset_ticks_position���`a(���bs1a'���bs1dleft���bs1a'���`a)���`a
���`bax���aoa.���`exaxis���aoa.���`rset_ticks_position���`a(���bs1a'���bs1fbottom���bs1a'���`a)���`a
���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
`dNone�