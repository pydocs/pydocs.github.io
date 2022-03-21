������������bsdy�"""
============================================
Set default y-axis tick labels on the right
============================================

We can use :rc:`ytick.labelright` (default False) and :rc:`ytick.right`
(default False) and :rc:`ytick.labelleft` (default True) and :rc:`ytick.left`
(default True) to control where on the axes ticks and their labels appear.
These properties can also be set in the ``.matplotlib/matplotlibrc``.

"""���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���`a
���`cplt���aoa.���`hrcParams���`a[���bs1a'���bs1kytick.right���bs1a'���`a]���`a ���aoa=���`a ���`cplt���aoa.���`hrcParams���`a[���bs1a'���bs1pytick.labelright���bs1a'���`a]���`a ���aoa=���`a ���bkcdTrue���`a
���`cplt���aoa.���`hrcParams���`a[���bs1a'���bs1jytick.left���bs1a'���`a]���`a ���aoa=���`a ���`cplt���aoa.���`hrcParams���`a[���bs1a'���bs1oytick.labelleft���bs1a'���`a]���`a ���aoa=���`a ���bkceFalse���`a
���`a
���`ax���`a ���aoa=���`a ���`bnp���aoa.���`farange���`a(���bmib10���`a)���`a
���`a
���`cfig���`a,���`a ���`a(���`cax0���`a,���`a ���`cax1���`a)���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���bmia2���`a,���`a ���bmia1���`a,���`a ���`fsharex���aoa=���bkcdTrue���`a,���`a ���`gfigsize���aoa=���`a(���bmia6���`a,���`a ���bmia6���`a)���`a)���`a
���`a
���`cax0���aoa.���`dplot���`a(���`ax���`a)���`a
���`cax0���aoa.���`eyaxis���aoa.���`itick_left���`a(���`a)���`a
���`a
���bc1x=# use default parameter in rcParams, not calling tick_right()���`a
���`cax1���aoa.���`dplot���`a(���`ax���`a)���`a
���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
`dNone�