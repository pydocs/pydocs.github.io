������������bsdxt"""
==============
Dropped spines
==============

Demo of spines offset from the axes (a.k.a. "dropped spines").
"""���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���`a
���bc1x)# Fixing random state for reproducibility���`a
���`bnp���aoa.���`frandom���aoa.���`dseed���`a(���bmih19680801���`a)���`a
���`a
���`cfig���`a,���`a ���`bax���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`a)���`a
���`a
���`eimage���`a ���aoa=���`a ���`bnp���aoa.���`frandom���aoa.���`guniform���`a(���`dsize���aoa=���`a(���bmib10���`a,���`a ���bmib10���`a)���`a)���`a
���`bax���aoa.���`fimshow���`a(���`eimage���`a,���`a ���`dcmap���aoa=���`cplt���aoa.���`bcm���aoa.���`dgray���`a)���`a
���`bax���aoa.���`iset_title���`a(���bs1a'���bs1ndropped spines���bs1a'���`a)���`a
���`a
���bc1x2# Move left and bottom spines outward by 10 points���`a
���`bax���aoa.���`fspines���aoa.���`dleft���aoa.���`lset_position���`a(���`a(���bs1a'���bs1goutward���bs1a'���`a,���`a ���bmib10���`a)���`a)���`a
���`bax���aoa.���`fspines���aoa.���`fbottom���aoa.���`lset_position���`a(���`a(���bs1a'���bs1goutward���bs1a'���`a,���`a ���bmib10���`a)���`a)���`a
���bc1x# Hide the right and top spines���`a
���`bax���aoa.���`fspines���aoa.���`eright���aoa.���`kset_visible���`a(���bkceFalse���`a)���`a
���`bax���aoa.���`fspines���aoa.���`ctop���aoa.���`kset_visible���`a(���bkceFalse���`a)���`a
���bc1x/# Only show ticks on the left and bottom spines���`a
���`bax���aoa.���`eyaxis���aoa.���`rset_ticks_position���`a(���bs1a'���bs1dleft���bs1a'���`a)���`a
���`bax���aoa.���`exaxis���aoa.���`rset_ticks_position���`a(���bs1a'���bs1fbottom���bs1a'���`a)���`a
���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
`dNone�