�����������bsdy�"""
======================================================
Controlling view limits using margins and sticky_edges
======================================================

The first figure in this example shows how to zoom in and out of a
plot using `~.Axes.margins` instead of `~.Axes.set_xlim` and
`~.Axes.set_ylim`. The second figure demonstrates the concept of
edge "stickiness" introduced by certain methods and artists and how
to effectively work around that.

"""���`a
���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���bkndfrom���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnngpatches���`a ���bknfimport���`a ���`gPolygon���`a
���`a
���`a
���akcdef���`a ���bnfaf���`a(���`at���`a)���`a:���`a
���`d    ���akfreturn���`a ���`bnp���aoa.���`cexp���`a(���aoa-���`at���`a)���`a ���aoa*���`a ���`bnp���aoa.���`ccos���`a(���bmia2���aoa*���`bnp���aoa.���`bpi���aoa*���`at���`a)���`a
���`a
���`a
���`bt1���`a ���aoa=���`a ���`bnp���aoa.���`farange���`a(���bmfc0.0���`a,���`a ���bmfc3.0���`a,���`a ���bmfd0.01���`a)���`a
���`a
���`cax1���`a ���aoa=���`a ���`cplt���aoa.���`gsubplot���`a(���bmic212���`a)���`a
���`cax1���aoa.���`gmargins���`a(���bmfd0.05���`a)���`k           ���bc1x+# Default margin is 0.05, value 0 means fit���`a
���`cax1���aoa.���`dplot���`a(���`bt1���`a,���`a ���`af���`a(���`bt1���`a)���`a)���`a
���`a
���`cax2���`a ���aoa=���`a ���`cplt���aoa.���`gsubplot���`a(���bmic221���`a)���`a
���`cax2���aoa.���`gmargins���`a(���bmia2���`a,���`a ���bmia2���`a)���`k           ���bc1v# Values >0.0 zoom out���`a
���`cax2���aoa.���`dplot���`a(���`bt1���`a,���`a ���`af���`a(���`bt1���`a)���`a)���`a
���`cax2���aoa.���`iset_title���`a(���bs1a'���bs1jZoomed out���bs1a'���`a)���`a
���`a
���`cax3���`a ���aoa=���`a ���`cplt���aoa.���`gsubplot���`a(���bmic222���`a)���`a
���`cax3���aoa.���`gmargins���`a(���`ax���aoa=���bmia0���`a,���`a ���`ay���aoa=���aoa-���bmfd0.25���`a)���`c   ���bc1x*# Values in (-0.5, 0.0) zooms in to center���`a
���`cax3���aoa.���`dplot���`a(���`bt1���`a,���`a ���`af���`a(���`bt1���`a)���`a)���`a
���`cax3���aoa.���`iset_title���`a(���bs1a'���bs1iZoomed in���bs1a'���`a)���`a
���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
���`a
���`a
���bc1xM#############################################################################���`a
���bc1a#���`a
���bc1x1# On the "stickiness" of certain plotting methods���`a
���bc1x1# """""""""""""""""""""""""""""""""""""""""""""""���`a
���bc1a#���`a
���bc1xM# Some plotting functions make the axis limits "sticky" or immune to the will���`a
���bc1xD# of the `~.Axes.margins` methods. For instance, `~.Axes.imshow` and���`a
���bc1xK# `~.Axes.pcolor` expect the user to want the limits to be tight around the���`a
���bc1xL# pixels shown in the plot. If this behavior is not desired, you need to set���`a
���bc1xG# `~.Axes.use_sticky_edges` to `False`. Consider the following example:���`a
���`a
���`ay���`a,���`a ���`ax���`a ���aoa=���`a ���`bnp���aoa.���`emgrid���`a[���`a:���bmia5���`a,���`a ���bmia1���`a:���bmia6���`a]���`a
���`kpoly_coords���`a ���aoa=���`a ���`a[���`a
���`d    ���`a(���bmfd0.25���`a,���`a ���bmfd2.75���`a)���`a,���`a ���`a(���bmfd3.25���`a,���`a ���bmfd2.75���`a)���`a,���`a
���`d    ���`a(���bmfd2.25���`a,���`a ���bmfd0.75���`a)���`a,���`a ���`a(���bmfd0.25���`a,���`a ���bmfd0.75���`a)���`a
���`a]���`a
���`cfig���`a,���`a ���`a(���`cax1���`a,���`a ���`cax2���`a)���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`encols���aoa=���bmia2���`a)���`a
���`a
���bc1x2# Here we set the stickiness of the axes object...���`a
���bc1x9# ax1 we'll leave as the default, which uses sticky edges���`a
���bc1x'# and we'll turn off stickiness for ax2���`a
���`cax2���aoa.���`puse_sticky_edges���`a ���aoa=���`a ���bkceFalse���`a
���`a
���akcfor���`a ���`bax���`a,���`a ���`fstatus���`a ���bowbin���`a ���bnbczip���`a(���`a(���`cax1���`a,���`a ���`cax2���`a)���`a,���`a ���`a(���bs1a'���bs1bIs���bs1a'���`a,���`a ���bs1a'���bs1fIs Not���bs1a'���`a)���`a)���`a:���`a
���`d    ���`ecells���`a ���aoa=���`a ���`bax���aoa.���`fpcolor���`a(���`ax���`a,���`a ���`ay���`a,���`a ���`ax���aoa+���`ay���`a,���`a ���`dcmap���aoa=���bs1a'���bs1ginferno���bs1a'���`a,���`a ���`gshading���aoa=���bs1a'���bs1dauto���bs1a'���`a)���`b  ���bc1h# sticky���`a
���`d    ���`bax���aoa.���`iadd_patch���`a(���`a
���`h        ���`gPolygon���`a(���`kpoly_coords���`a,���`a ���`ecolor���aoa=���bs1a'���bs1kforestgreen���bs1a'���`a,���`a ���`ealpha���aoa=���bmfc0.5���`a)���`a
���`d    ���`a)���`b  ���bc1l# not sticky���`a
���`d    ���`bax���aoa.���`gmargins���`a(���`ax���aoa=���bmfc0.1���`a,���`a ���`ay���aoa=���bmfd0.05���`a)���`a
���`d    ���`bax���aoa.���`jset_aspect���`a(���bs1a'���bs1eequal���bs1a'���`a)���`a
���`d    ���`bax���aoa.���`iset_title���`a(���bs1a'���bsib{}���bs1g Sticky���bs1a'���aoa.���`fformat���`a(���`fstatus���`a)���`a)���`a
���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
���`a
���`a
���bc1xM#############################################################################���`a
���bc1a#���`a
���bc1x# .. admonition:: References���`a
���bc1a#���`a
���bc1xN#    The use of the following functions, methods, classes and modules is shown���`a
���bc1u#    in this example:���`a
���bc1a#���`a
���bc1xC#    - `matplotlib.axes.Axes.margins` / `matplotlib.pyplot.margins`���`a
���bc1x.#    - `matplotlib.axes.Axes.use_sticky_edges`���`a
���bc1xA#    - `matplotlib.axes.Axes.pcolor` / `matplotlib.pyplot.pcolor`���`a
���bc1x##    - `matplotlib.patches.Polygon`���`a
`dNone�