������������bsdx�"""
==============
Align y-labels
==============

Two methods are shown here, one using a short call to `.Figure.align_ylabels`
and the second a manual way to align the labels.

"""���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���`a
���`a
���akcdef���`a ���bnfimake_plot���`a(���`caxs���`a)���`a:���`a
���`d    ���`cbox���`a ���aoa=���`a ���bnbddict���`a(���`ifacecolor���aoa=���bs1a'���bs1fyellow���bs1a'���`a,���`a ���`cpad���aoa=���bmia5���`a,���`a ���`ealpha���aoa=���bmfc0.2���`a)���`a
���`a
���`d    ���bc1x)# Fixing random state for reproducibility���`a
���`d    ���`bnp���aoa.���`frandom���aoa.���`dseed���`a(���bmih19680801���`a)���`a
���`d    ���`cax1���`a ���aoa=���`a ���`caxs���`a[���bmia0���`a,���`a ���bmia0���`a]���`a
���`d    ���`cax1���aoa.���`dplot���`a(���bmid2000���aoa*���`bnp���aoa.���`frandom���aoa.���`drand���`a(���bmib10���`a)���`a)���`a
���`d    ���`cax1���aoa.���`iset_title���`a(���bs1a'���bs1sylabels not aligned���bs1a'���`a)���`a
���`d    ���`cax1���aoa.���`jset_ylabel���`a(���bs1a'���bs1lmisaligned 1���bs1a'���`a,���`a ���`dbbox���aoa=���`cbox���`a)���`a
���`d    ���`cax1���aoa.���`hset_ylim���`a(���bmia0���`a,���`a ���bmid2000���`a)���`a
���`a
���`d    ���`cax3���`a ���aoa=���`a ���`caxs���`a[���bmia1���`a,���`a ���bmia0���`a]���`a
���`d    ���`cax3���aoa.���`jset_ylabel���`a(���bs1a'���bs1lmisaligned 2���bs1a'���`a,���`a ���`dbbox���aoa=���`cbox���`a)���`a
���`d    ���`cax3���aoa.���`dplot���`a(���`bnp���aoa.���`frandom���aoa.���`drand���`a(���bmib10���`a)���`a)���`a
���`a
���`d    ���`cax2���`a ���aoa=���`a ���`caxs���`a[���bmia0���`a,���`a ���bmia1���`a]���`a
���`d    ���`cax2���aoa.���`iset_title���`a(���bs1a'���bs1oylabels aligned���bs1a'���`a)���`a
���`d    ���`cax2���aoa.���`dplot���`a(���bmid2000���aoa*���`bnp���aoa.���`frandom���aoa.���`drand���`a(���bmib10���`a)���`a)���`a
���`d    ���`cax2���aoa.���`jset_ylabel���`a(���bs1a'���bs1ialigned 1���bs1a'���`a,���`a ���`dbbox���aoa=���`cbox���`a)���`a
���`d    ���`cax2���aoa.���`hset_ylim���`a(���bmia0���`a,���`a ���bmid2000���`a)���`a
���`a
���`d    ���`cax4���`a ���aoa=���`a ���`caxs���`a[���bmia1���`a,���`a ���bmia1���`a]���`a
���`d    ���`cax4���aoa.���`dplot���`a(���`bnp���aoa.���`frandom���aoa.���`drand���`a(���bmib10���`a)���`a)���`a
���`d    ���`cax4���aoa.���`jset_ylabel���`a(���bs1a'���bs1ialigned 2���bs1a'���`a,���`a ���`dbbox���aoa=���`cbox���`a)���`a
���`a
���`a
���bc1i# Plot 1:���`a
���`cfig���`a,���`a ���`caxs���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���bmia2���`a,���`a ���bmia2���`a)���`a
���`cfig���aoa.���`osubplots_adjust���`a(���`dleft���aoa=���bmfc0.2���`a,���`a ���`fwspace���aoa=���bmfc0.6���`a)���`a
���`imake_plot���`a(���`caxs���`a)���`a
���`a
���bc1x%# just align the last column of axes:���`a
���`cfig���aoa.���`malign_ylabels���`a(���`caxs���`a[���`a:���`a,���`a ���bmia1���`a]���`a)���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
���`a
���bc1xM#############################################################################���`a
���bc1a#���`a
���bc1n# .. seealso::���`a
���bc1xL#     `.Figure.align_ylabels` and `.Figure.align_labels` for a direct method���`a
���bc1x#     of doing the same thing.���`a
���bc1xF#     Also :doc:`/gallery/subplots_axes_and_figures/align_labels_demo`���`a
���bc1a#���`a
���bc1a#���`a
���bc1xN# Or we can manually align the axis labels between subplots manually using the���`a
���bc1xL# `~.Axis.set_label_coords` method of the y-axis object.  Note this requires���`a
���bc1x1# we know a good offset value which is hardcoded.���`a
���`a
���`cfig���`a,���`a ���`caxs���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���bmia2���`a,���`a ���bmia2���`a)���`a
���`cfig���aoa.���`osubplots_adjust���`a(���`dleft���aoa=���bmfc0.2���`a,���`a ���`fwspace���aoa=���bmfc0.6���`a)���`a
���`a
���`imake_plot���`a(���`caxs���`a)���`a
���`a
���`flabelx���`a ���aoa=���`a ���aoa-���bmfc0.3���`b  ���bc1m# axes coords���`a
���`a
���akcfor���`a ���`aj���`a ���bowbin���`a ���bnberange���`a(���bmia2���`a)���`a:���`a
���`d    ���`caxs���`a[���`aj���`a,���`a ���bmia1���`a]���aoa.���`eyaxis���aoa.���`pset_label_coords���`a(���`flabelx���`a,���`a ���bmfc0.5���`a)���`a
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
���bc1x/#    - `matplotlib.figure.Figure.align_ylabels`���`a
���bc1x.#    - `matplotlib.axis.Axis.set_label_coords`���`a
���bc1x=#    - `matplotlib.axes.Axes.plot` / `matplotlib.pyplot.plot`���`a
���bc1x'#    - `matplotlib.axes.Axes.set_title`���`a
���bc1x(#    - `matplotlib.axes.Axes.set_ylabel`���`a
���bc1x&#    - `matplotlib.axes.Axes.set_ylim`���`a
`dNone�