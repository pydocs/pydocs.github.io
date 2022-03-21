��������	���bsdx�"""
======
Spines
======

This demo compares:

- normal axes, with spines on all four sides;
- an axes with spines only on the left and bottom;
- an axes using custom bounds to limit the extent of the spine.
"""���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���`a
���`a
���`ax���`a ���aoa=���`a ���`bnp���aoa.���`hlinspace���`a(���bmia0���`a,���`a ���bmia2���`a ���aoa*���`a ���`bnp���aoa.���`bpi���`a,���`a ���bmic100���`a)���`a
���`ay���`a ���aoa=���`a ���bmia2���`a ���aoa*���`a ���`bnp���aoa.���`csin���`a(���`ax���`a)���`a
���`a
���bc1xB# Constrained layout makes sure the labels don't overlap the axes.���`a
���`cfig���`a,���`a ���`a(���`cax0���`a,���`a ���`cax1���`a,���`a ���`cax2���`a)���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`enrows���aoa=���bmia3���`a,���`a ���`rconstrained_layout���aoa=���bkcdTrue���`a)���`a
���`a
���`cax0���aoa.���`dplot���`a(���`ax���`a,���`a ���`ay���`a)���`a
���`cax0���aoa.���`iset_title���`a(���bs1a'���bs1mnormal spines���bs1a'���`a)���`a
���`a
���`cax1���aoa.���`dplot���`a(���`ax���`a,���`a ���`ay���`a)���`a
���`cax1���aoa.���`iset_title���`a(���bs1a'���bs1rbottom-left spines���bs1a'���`a)���`a
���`a
���bc1x# Hide the right and top spines���`a
���`cax1���aoa.���`fspines���aoa.���`eright���aoa.���`kset_visible���`a(���bkceFalse���`a)���`a
���`cax1���aoa.���`fspines���aoa.���`ctop���aoa.���`kset_visible���`a(���bkceFalse���`a)���`a
���bc1x/# Only show ticks on the left and bottom spines���`a
���`cax1���aoa.���`eyaxis���aoa.���`rset_ticks_position���`a(���bs1a'���bs1dleft���bs1a'���`a)���`a
���`cax1���aoa.���`exaxis���aoa.���`rset_ticks_position���`a(���bs1a'���bs1fbottom���bs1a'���`a)���`a
���`a
���`cax2���aoa.���`dplot���`a(���`ax���`a,���`a ���`ay���`a)���`a
���`a
���bc1x%# Only draw spine between the y-ticks���`a
���`cax2���aoa.���`fspines���aoa.���`dleft���aoa.���`jset_bounds���`a(���aoa-���bmia1���`a,���`a ���bmia1���`a)���`a
���bc1x# Hide the right and top spines���`a
���`cax2���aoa.���`fspines���aoa.���`eright���aoa.���`kset_visible���`a(���bkceFalse���`a)���`a
���`cax2���aoa.���`fspines���aoa.���`ctop���aoa.���`kset_visible���`a(���bkceFalse���`a)���`a
���bc1x/# Only show ticks on the left and bottom spines���`a
���`cax2���aoa.���`eyaxis���aoa.���`rset_ticks_position���`a(���bs1a'���bs1dleft���bs1a'���`a)���`a
���`cax2���aoa.���`exaxis���aoa.���`rset_ticks_position���`a(���bs1a'���bs1fbottom���bs1a'���`a)���`a
���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
`dNone�