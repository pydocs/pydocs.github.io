������������bsdyX"""
==================================
Scatter Histogram (Locatable Axes)
==================================

Show the marginal distributions of a scatter as histograms at the sides of
the plot.

For a nice alignment of the main axes with the marginals, the axes positions
are defined by a ``Divider``, produced via `.make_axes_locatable`.

An alternative method to produce a similar figure is shown in the
:doc:`/gallery/lines_bars_and_markers/scatter_hist` example. The advantage of
the locatable axes method shown below is that the marginal axes follow the
fixed aspect ratio of the main axes.
"""���`a
���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���bkndfrom���`a ���bnnlmpl_toolkits���bnna.���bnnjaxes_grid1���`a ���bknfimport���`a ���`smake_axes_locatable���`a
���`a
���bc1x)# Fixing random state for reproducibility���`a
���`bnp���aoa.���`frandom���aoa.���`dseed���`a(���bmih19680801���`a)���`a
���`a
���bc1q# the random data���`a
���`ax���`a ���aoa=���`a ���`bnp���aoa.���`frandom���aoa.���`erandn���`a(���bmid1000���`a)���`a
���`ay���`a ���aoa=���`a ���`bnp���aoa.���`frandom���aoa.���`erandn���`a(���bmid1000���`a)���`a
���`a
���`a
���`cfig���`a,���`a ���`bax���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`gfigsize���aoa=���`a(���bmfc5.5���`a,���`a ���bmfc5.5���`a)���`a)���`a
���`a
���bc1s# the scatter plot:���`a
���`bax���aoa.���`gscatter���`a(���`ax���`a,���`a ���`ay���`a)���`a
���`a
���bc1x# Set aspect of the main axes.���`a
���`bax���aoa.���`jset_aspect���`a(���bmfb1.���`a)���`a
���`a
���bc1xA# create new axes on the right and on the top of the current axes���`a
���`gdivider���`a ���aoa=���`a ���`smake_axes_locatable���`a(���`bax���`a)���`a
���bc1x$# below height and pad are in inches���`a
���`hax_histx���`a ���aoa=���`a ���`gdivider���aoa.���`kappend_axes���`a(���bs2a"���bs2ctop���bs2a"���`a,���`a ���bmfc1.2���`a,���`a ���`cpad���aoa=���bmfc0.1���`a,���`a ���`fsharex���aoa=���`bax���`a)���`a
���`hax_histy���`a ���aoa=���`a ���`gdivider���aoa.���`kappend_axes���`a(���bs2a"���bs2eright���bs2a"���`a,���`a ���bmfc1.2���`a,���`a ���`cpad���aoa=���bmfc0.1���`a,���`a ���`fsharey���aoa=���`bax���`a)���`a
���`a
���bc1x# make some labels invisible���`a
���`hax_histx���aoa.���`exaxis���aoa.���`oset_tick_params���`a(���`klabelbottom���aoa=���bkceFalse���`a)���`a
���`hax_histy���aoa.���`eyaxis���aoa.���`oset_tick_params���`a(���`ilabelleft���aoa=���bkceFalse���`a)���`a
���`a
���bc1x$# now determine nice limits by hand:���`a
���`hbinwidth���`a ���aoa=���`a ���bmfd0.25���`a
���`exymax���`a ���aoa=���`a ���bnbcmax���`a(���`bnp���aoa.���`cmax���`a(���`bnp���aoa.���`cabs���`a(���`ax���`a)���`a)���`a,���`a ���`bnp���aoa.���`cmax���`a(���`bnp���aoa.���`cabs���`a(���`ay���`a)���`a)���`a)���`a
���`clim���`a ���aoa=���`a ���`a(���bnbcint���`a(���`exymax���aoa/���`hbinwidth���`a)���`a ���aoa+���`a ���bmia1���`a)���aoa*���`hbinwidth���`a
���`a
���`dbins���`a ���aoa=���`a ���`bnp���aoa.���`farange���`a(���aoa-���`clim���`a,���`a ���`clim���`a ���aoa+���`a ���`hbinwidth���`a,���`a ���`hbinwidth���`a)���`a
���`hax_histx���aoa.���`dhist���`a(���`ax���`a,���`a ���`dbins���aoa=���`dbins���`a)���`a
���`hax_histy���aoa.���`dhist���`a(���`ay���`a,���`a ���`dbins���aoa=���`dbins���`a,���`a ���`korientation���aoa=���bs1a'���bs1jhorizontal���bs1a'���`a)���`a
���`a
���bc1xA# the xaxis of ax_histx and yaxis of ax_histy are shared with ax,���`a
���bc1xE# thus there is no need to manually adjust the xlim and ylim of these���`a
���bc1g# axis.���`a
���`a
���`hax_histx���aoa.���`jset_yticks���`a(���`a[���bmia0���`a,���`a ���bmib50���`a,���`a ���bmic100���`a]���`a)���`a
���`hax_histy���aoa.���`jset_xticks���`a(���`a[���bmia0���`a,���`a ���bmib50���`a,���`a ���bmic100���`a]���`a)���`a
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
���bc1xA#    - `mpl_toolkits.axes_grid1.axes_divider.make_axes_locatable`���`a
���bc1x(#    - `matplotlib.axes.Axes.set_aspect`���`a
���bc1x%#    - `matplotlib.axes.Axes.scatter`���`a
���bc1x"#    - `matplotlib.axes.Axes.hist`���`a
`dNone�