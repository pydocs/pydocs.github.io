������������bsdx�"""
====================================
Colors in the default property cycle
====================================

Display the colors from the default prop_cycle, which is obtained from the
:doc:`rc parameters</tutorials/introductory/customizing>`.
"""���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���`a
���`a
���`jprop_cycle���`a ���aoa=���`a ���`cplt���aoa.���`hrcParams���`a[���bs1a'���bs1oaxes.prop_cycle���bs1a'���`a]���`a
���`fcolors���`a ���aoa=���`a ���`jprop_cycle���aoa.���`fby_key���`a(���`a)���`a[���bs1a'���bs1ecolor���bs1a'���`a]���`a
���`a
���`flwbase���`a ���aoa=���`a ���`cplt���aoa.���`hrcParams���`a[���bs1a'���bs1olines.linewidth���bs1a'���`a]���`a
���`dthin���`a ���aoa=���`a ���`flwbase���`a ���aoa/���`a ���bmia2���`a
���`ethick���`a ���aoa=���`a ���`flwbase���`a ���aoa*���`a ���bmia3���`a
���`a
���`cfig���`a,���`a ���`caxs���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`enrows���aoa=���bmia2���`a,���`a ���`encols���aoa=���bmia2���`a,���`a ���`fsharex���aoa=���bkcdTrue���`a,���`a ���`fsharey���aoa=���bkcdTrue���`a)���`a
���akcfor���`a ���`dicol���`a ���bowbin���`a ���bnberange���`a(���bmia2���`a)���`a:���`a
���`d    ���akbif���`a ���`dicol���`a ���aob==���`a ���bmia0���`a:���`a
���`h        ���`clwx���`a,���`a ���`clwy���`a ���aoa=���`a ���`dthin���`a,���`a ���`flwbase���`a
���`d    ���akdelse���`a:���`a
���`h        ���`clwx���`a,���`a ���`clwy���`a ���aoa=���`a ���`flwbase���`a,���`a ���`ethick���`a
���`d    ���akcfor���`a ���`dirow���`a ���bowbin���`a ���bnberange���`a(���bmia2���`a)���`a:���`a
���`h        ���akcfor���`a ���`ai���`a,���`a ���`ecolor���`a ���bowbin���`a ���bnbienumerate���`a(���`fcolors���`a)���`a:���`a
���`l            ���`caxs���`a[���`dirow���`a,���`a ���`dicol���`a]���aoa.���`gaxhline���`a(���`ai���`a,���`a ���`ecolor���aoa=���`ecolor���`a,���`a ���`blw���aoa=���`clwx���`a)���`a
���`l            ���`caxs���`a[���`dirow���`a,���`a ���`dicol���`a]���aoa.���`gaxvline���`a(���`ai���`a,���`a ���`ecolor���aoa=���`ecolor���`a,���`a ���`blw���aoa=���`clwy���`a)���`a
���`a
���`d    ���`caxs���`a[���bmia1���`a,���`a ���`dicol���`a]���aoa.���`mset_facecolor���`a(���bs1a'���bs1ak���bs1a'���`a)���`a
���`d    ���`caxs���`a[���bmia1���`a,���`a ���`dicol���`a]���aoa.���`exaxis���aoa.���`iset_ticks���`a(���`bnp���aoa.���`farange���`a(���bmia0���`a,���`a ���bmib10���`a,���`a ���bmia2���`a)���`a)���`a
���`d    ���`caxs���`a[���bmia0���`a,���`a ���`dicol���`a]���aoa.���`iset_title���`a(���bs1a'���bs1sline widths (pts): ���bsib%g���bs1b, ���bsib%g���bs1a'���`a ���aoa%���`a ���`a(���`clwx���`a,���`a ���`clwy���`a)���`a,���`a
���`x                           ���`hfontsize���aoa=���bs1a'���bs1fmedium���bs1a'���`a)���`a
���`a
���akcfor���`a ���`dirow���`a ���bowbin���`a ���bnberange���`a(���bmia2���`a)���`a:���`a
���`d    ���`caxs���`a[���`dirow���`a,���`a ���bmia0���`a]���aoa.���`eyaxis���aoa.���`iset_ticks���`a(���`bnp���aoa.���`farange���`a(���bmia0���`a,���`a ���bmib10���`a,���`a ���bmia2���`a)���`a)���`a
���`a
���`cfig���aoa.���`hsuptitle���`a(���bs1a'���bs1x Colors in the default prop_cycle���bs1a'���`a,���`a ���`hfontsize���aoa=���bs1a'���bs1elarge���bs1a'���`a)���`a
���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
���`a
���bc1xM#############################################################################���`a
���bc1a#���`a
���bc1x# .. admonition:: References���`a
���bc1a#���`a
���bc1xN#    The use of the following functions, methods, classes and modules is shown���`a
���bc1u#    in this example:���`a
���bc1a#���`a
���bc1xC#    - `matplotlib.axes.Axes.axhline` / `matplotlib.pyplot.axhline`���`a
���bc1xC#    - `matplotlib.axes.Axes.axvline` / `matplotlib.pyplot.axvline`���`a
���bc1x+#    - `matplotlib.axes.Axes.set_facecolor`���`a
���bc1x*#    - `matplotlib.figure.Figure.suptitle`���`a
`dNone�