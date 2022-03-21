��������n���bsdx�"""
===================
Contour Corner Mask
===================

Illustrate the difference between ``corner_mask=False`` and
``corner_mask=True`` for masked contour plots.
"""���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���`a
���bc1o# Data to plot.���`a
���`ax���`a,���`a ���`ay���`a ���aoa=���`a ���`bnp���aoa.���`hmeshgrid���`a(���`bnp���aoa.���`farange���`a(���bmia7���`a)���`a,���`a ���`bnp���aoa.���`farange���`a(���bmib10���`a)���`a)���`a
���`az���`a ���aoa=���`a ���`bnp���aoa.���`csin���`a(���bmfc0.5���`a ���aoa*���`a ���`ax���`a)���`a ���aoa*���`a ���`bnp���aoa.���`ccos���`a(���bmfd0.52���`a ���aoa*���`a ���`ay���`a)���`a
���`a
���bc1x# Mask various z values.���`a
���`dmask���`a ���aoa=���`a ���`bnp���aoa.���`jzeros_like���`a(���`az���`a,���`a ���`edtype���aoa=���bnbdbool���`a)���`a
���`dmask���`a[���bmia2���`a,���`a ���bmia3���`a:���bmia5���`a]���`a ���aoa=���`a ���bkcdTrue���`a
���`dmask���`a[���bmia3���`a:���bmia5���`a,���`a ���bmia4���`a]���`a ���aoa=���`a ���bkcdTrue���`a
���`dmask���`a[���bmia7���`a,���`a ���bmia2���`a]���`a ���aoa=���`a ���bkcdTrue���`a
���`dmask���`a[���bmia5���`a,���`a ���bmia0���`a]���`a ���aoa=���`a ���bkcdTrue���`a
���`dmask���`a[���bmia0���`a,���`a ���bmia6���`a]���`a ���aoa=���`a ���bkcdTrue���`a
���`az���`a ���aoa=���`a ���`bnp���aoa.���`bma���aoa.���`earray���`a(���`az���`a,���`a ���`dmask���aoa=���`dmask���`a)���`a
���`a
���`lcorner_masks���`a ���aoa=���`a ���`a[���bkceFalse���`a,���`a ���bkcdTrue���`a]���`a
���`cfig���`a,���`a ���`caxs���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`encols���aoa=���bmia2���`a)���`a
���akcfor���`a ���`bax���`a,���`a ���`kcorner_mask���`a ���bowbin���`a ���bnbczip���`a(���`caxs���`a,���`a ���`lcorner_masks���`a)���`a:���`a
���`d    ���`bcs���`a ���aoa=���`a ���`bax���aoa.���`hcontourf���`a(���`ax���`a,���`a ���`ay���`a,���`a ���`az���`a,���`a ���`kcorner_mask���aoa=���`kcorner_mask���`a)���`a
���`d    ���`bax���aoa.���`gcontour���`a(���`bcs���`a,���`a ���`fcolors���aoa=���bs1a'���bs1ak���bs1a'���`a)���`a
���`d    ���`bax���aoa.���`iset_title���`a(���bs1a'���bs1ncorner_mask = ���bsic{0}���bs1a'���aoa.���`fformat���`a(���`kcorner_mask���`a)���`a)���`a
���`a
���`d    ���bc1l# Plot grid.���`a
���`d    ���`bax���aoa.���`dgrid���`a(���`ac���aoa=���bs1a'���bs1ak���bs1a'���`a,���`a ���`bls���aoa=���bs1a'���bs1a-���bs1a'���`a,���`a ���`ealpha���aoa=���bmfc0.3���`a)���`a
���`a
���`d    ���bc1x*# Indicate masked points with red circles.���`a
���`d    ���`bax���aoa.���`dplot���`a(���`bnp���aoa.���`bma���aoa.���`earray���`a(���`ax���`a,���`a ���`dmask���aoa=���aoa~���`dmask���`a)���`a,���`a ���`ay���`a,���`a ���bs1a'���bs1bro���bs1a'���`a)���`a
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
���bc1xC#    - `matplotlib.axes.Axes.contour` / `matplotlib.pyplot.contour`���`a
���bc1xE#    - `matplotlib.axes.Axes.contourf` / `matplotlib.pyplot.contourf`���`a
`dNone�