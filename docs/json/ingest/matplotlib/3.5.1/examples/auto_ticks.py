������������bsdy�"""
====================================
Automatically setting tick positions
====================================

Setting the behavior of tick auto-placement.

By default, Matplotlib will choose the number of ticks and tick positions so
that there is a reasonable number of ticks on the axis and they are located
at "round" numbers.

As a result, there may be no ticks on the edges of the plot.
"""���`a
���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���`bnp���aoa.���`frandom���aoa.���`dseed���`a(���bmih19680801���`a)���`a
���`a
���`cfig���`a,���`a ���`bax���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`a)���`a
���`ddots���`a ���aoa=���`a ���`bnp���aoa.���`hlinspace���`a(���bmfc0.3���`a,���`a ���bmfc1.2���`a,���`a ���bmib10���`a)���`a
���`aX���`a,���`a ���`aY���`a ���aoa=���`a ���`bnp���aoa.���`hmeshgrid���`a(���`ddots���`a,���`a ���`ddots���`a)���`a
���`ax���`a,���`a ���`ay���`a ���aoa=���`a ���`aX���aoa.���`eravel���`a(���`a)���`a,���`a ���`aY���aoa.���`eravel���`a(���`a)���`a
���`bax���aoa.���`gscatter���`a(���`ax���`a,���`a ���`ay���`a,���`a ���`ac���aoa=���`ax���aoa+���`ay���`a)���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
���`a
���bc1xO###############################################################################���`a
���bc1xN# If you want to keep ticks at round numbers, and also have ticks at the edges���`a
���bc1xO# you can switch :rc:`axes.autolimit_mode` to 'round_numbers'. This expands the���`a
���bc1x'# axis limits to the next round number.���`a
���`a
���`cplt���aoa.���`hrcParams���`a[���bs1a'���bs1saxes.autolimit_mode���bs1a'���`a]���`a ���aoa=���`a ���bs1a'���bs1mround_numbers���bs1a'���`a
���`a
���bc1xE# Note: The limits are calculated at draw-time. Therefore, when using���`a
���bc1xF# :rc:`axes.autolimit_mode` in a context manager, it is important that���`a
���bc1x/# the ``show()`` command is within the context.���`a
���`a
���`cfig���`a,���`a ���`bax���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`a)���`a
���`bax���aoa.���`gscatter���`a(���`ax���`a,���`a ���`ay���`a,���`a ���`ac���aoa=���`ax���aoa+���`ay���`a)���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
���`a
���bc1xO###############################################################################���`a
���bc1xN# The round numbers autolimit_mode is still respected if you set an additional���`a
���bc1xI# margin around the data using `.Axes.set_xmargin` / `.Axes.set_ymargin`:���`a
���`a
���`cfig���`a,���`a ���`bax���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`a)���`a
���`bax���aoa.���`gscatter���`a(���`ax���`a,���`a ���`ay���`a,���`a ���`ac���aoa=���`ax���aoa+���`ay���`a)���`a
���`bax���aoa.���`kset_xmargin���`a(���bmfc0.8���`a)���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
`dNone�