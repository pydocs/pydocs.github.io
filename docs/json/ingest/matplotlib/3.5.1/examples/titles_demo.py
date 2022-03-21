��������|���bsdx�"""
=================
Title positioning
=================

Matplotlib can display plot titles centered, flush with the left side of
a set of axes, and flush with the right side of a set of axes.

"""���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���`a
���`cplt���aoa.���`dplot���`a(���bnberange���`a(���bmib10���`a)���`a)���`a
���`a
���`cplt���aoa.���`etitle���`a(���bs1a'���bs1lCenter Title���bs1a'���`a)���`a
���`cplt���aoa.���`etitle���`a(���bs1a'���bs1jLeft Title���bs1a'���`a,���`a ���`cloc���aoa=���bs1a'���bs1dleft���bs1a'���`a)���`a
���`cplt���aoa.���`etitle���`a(���bs1a'���bs1kRight Title���bs1a'���`a,���`a ���`cloc���aoa=���bs1a'���bs1eright���bs1a'���`a)���`a
���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
���`a
���bc1xK###########################################################################���`a
���bc1xD# The vertical position is automatically chosen to avoid decorations���`a
���bc1x0# (i.e. labels and ticks) on the topmost x-axis:���`a
���`a
���`cfig���`a,���`a ���`caxs���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���bmia1���`a,���`a ���bmia2���`a,���`a ���`rconstrained_layout���aoa=���bkcdTrue���`a)���`a
���`a
���`bax���`a ���aoa=���`a ���`caxs���`a[���bmia0���`a]���`a
���`bax���aoa.���`dplot���`a(���bnberange���`a(���bmib10���`a)���`a)���`a
���`bax���aoa.���`exaxis���aoa.���`rset_label_position���`a(���bs1a'���bs1ctop���bs1a'���`a)���`a
���`bax���aoa.���`jset_xlabel���`a(���bs1a'���bs1gX-label���bs1a'���`a)���`a
���`bax���aoa.���`iset_title���`a(���bs1a'���bs1lCenter Title���bs1a'���`a)���`a
���`a
���`bax���`a ���aoa=���`a ���`caxs���`a[���bmia1���`a]���`a
���`bax���aoa.���`dplot���`a(���bnberange���`a(���bmib10���`a)���`a)���`a
���`bax���aoa.���`exaxis���aoa.���`rset_label_position���`a(���bs1a'���bs1ctop���bs1a'���`a)���`a
���`bax���aoa.���`exaxis���aoa.���`htick_top���`a(���`a)���`a
���`bax���aoa.���`jset_xlabel���`a(���bs1a'���bs1gX-label���bs1a'���`a)���`a
���`bax���aoa.���`iset_title���`a(���bs1a'���bs1lCenter Title���bs1a'���`a)���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
���`a
���bc1xK###########################################################################���`a
���bc1xH# Automatic positioning can be turned off by manually specifying the *y*���`a
���bc1xN# keyword argument for the title or setting :rc:`axes.titley` in the rcParams.���`a
���`a
���`cfig���`a,���`a ���`caxs���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���bmia1���`a,���`a ���bmia2���`a,���`a ���`rconstrained_layout���aoa=���bkcdTrue���`a)���`a
���`a
���`bax���`a ���aoa=���`a ���`caxs���`a[���bmia0���`a]���`a
���`bax���aoa.���`dplot���`a(���bnberange���`a(���bmib10���`a)���`a)���`a
���`bax���aoa.���`exaxis���aoa.���`rset_label_position���`a(���bs1a'���bs1ctop���bs1a'���`a)���`a
���`bax���aoa.���`jset_xlabel���`a(���bs1a'���bs1gX-label���bs1a'���`a)���`a
���`bax���aoa.���`iset_title���`a(���bs1a'���bs1hManual y���bs1a'���`a,���`a ���`ay���aoa=���bmfc1.0���`a,���`a ���`cpad���aoa=���aoa-���bmib14���`a)���`a
���`a
���`cplt���aoa.���`hrcParams���`a[���bs1a'���bs1kaxes.titley���bs1a'���`a]���`a ���aoa=���`a ���bmfc1.0���`d    ���bc1x$# y is in axes-relative coordinates.���`a
���`cplt���aoa.���`hrcParams���`a[���bs1a'���bs1maxes.titlepad���bs1a'���`a]���`a ���aoa=���`a ���aoa-���bmib14���`b  ���bc1u# pad is in points...���`a
���`bax���`a ���aoa=���`a ���`caxs���`a[���bmia1���`a]���`a
���`bax���aoa.���`dplot���`a(���bnberange���`a(���bmib10���`a)���`a)���`a
���`bax���aoa.���`jset_xlabel���`a(���bs1a'���bs1gX-label���bs1a'���`a)���`a
���`bax���aoa.���`iset_title���`a(���bs1a'���bs1ircParam y���bs1a'���`a)���`a
���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
`dNone�