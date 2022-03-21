Ù¯‚Ù´ƒ™‡Ù±‚bsdyX"""
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
"""Ù±‚`a
Ù±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„enumpyÙ „enumpyf1.22.3fmoduleenumpyfmoduleõÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnnbnpÙ±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnnfpyplotÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnncpltÙ±‚`a
Ù±‚bkndfromÙ±‚`a Ù±‚bnnlmpl_toolkitsÙ±‚bnna.Ù±‚bnnjaxes_grid1Ù±‚`a Ù±‚bknfimportÙ±‚`a Ù±‚`smake_axes_locatableÙ±‚`a
Ù±‚`a
Ù±‚bc1x)# Fixing random state for reproducibilityÙ±‚`a
Ù±‚`bnpÙ±‚aoa.Ù±‚`frandomÙ±‚aoa.Ù±‚`dseedÙ±‚`a(Ù±‚bmih19680801Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚bc1q# the random dataÙ±‚`a
Ù±‚`axÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`frandomÙ±‚aoa.Ù±‚`erandnÙ±‚`a(Ù±‚bmid1000Ù±‚`a)Ù±‚`a
Ù±‚`ayÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`frandomÙ±‚aoa.Ù±‚`erandnÙ±‚`a(Ù±‚bmid1000Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚`cfigÙ±‚`a,Ù±‚`a Ù±‚`baxÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cpltÙ±‚aoa.Ù±‚`hsubplotsÙ±‚`a(Ù±‚`gfigsizeÙ±‚aoa=Ù±‚`a(Ù±‚bmfc5.5Ù±‚`a,Ù±‚`a Ù±‚bmfc5.5Ù±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚bc1s# the scatter plot:Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`gscatterÙ±‚`a(Ù±‚`axÙ±‚`a,Ù±‚`a Ù±‚`ayÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚bc1x# Set aspect of the main axes.Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`jset_aspectÙ±‚`a(Ù±‚bmfb1.Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚bc1xA# create new axes on the right and on the top of the current axesÙ±‚`a
Ù±‚`gdividerÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`smake_axes_locatableÙ±‚`a(Ù±‚`baxÙ±‚`a)Ù±‚`a
Ù±‚bc1x$# below height and pad are in inchesÙ±‚`a
Ù±‚`hax_histxÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`gdividerÙ±‚aoa.Ù±‚`kappend_axesÙ±‚`a(Ù±‚bs2a"Ù±‚bs2ctopÙ±‚bs2a"Ù±‚`a,Ù±‚`a Ù±‚bmfc1.2Ù±‚`a,Ù±‚`a Ù±‚`cpadÙ±‚aoa=Ù±‚bmfc0.1Ù±‚`a,Ù±‚`a Ù±‚`fsharexÙ±‚aoa=Ù±‚`baxÙ±‚`a)Ù±‚`a
Ù±‚`hax_histyÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`gdividerÙ±‚aoa.Ù±‚`kappend_axesÙ±‚`a(Ù±‚bs2a"Ù±‚bs2erightÙ±‚bs2a"Ù±‚`a,Ù±‚`a Ù±‚bmfc1.2Ù±‚`a,Ù±‚`a Ù±‚`cpadÙ±‚aoa=Ù±‚bmfc0.1Ù±‚`a,Ù±‚`a Ù±‚`fshareyÙ±‚aoa=Ù±‚`baxÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚bc1x# make some labels invisibleÙ±‚`a
Ù±‚`hax_histxÙ±‚aoa.Ù±‚`exaxisÙ±‚aoa.Ù±‚`oset_tick_paramsÙ±‚`a(Ù±‚`klabelbottomÙ±‚aoa=Ù±‚bkceFalseÙ±‚`a)Ù±‚`a
Ù±‚`hax_histyÙ±‚aoa.Ù±‚`eyaxisÙ±‚aoa.Ù±‚`oset_tick_paramsÙ±‚`a(Ù±‚`ilabelleftÙ±‚aoa=Ù±‚bkceFalseÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚bc1x$# now determine nice limits by hand:Ù±‚`a
Ù±‚`hbinwidthÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bmfd0.25Ù±‚`a
Ù±‚`exymaxÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bnbcmaxÙ±‚`a(Ù±‚`bnpÙ±‚aoa.Ù±‚`cmaxÙ±‚`a(Ù±‚`bnpÙ±‚aoa.Ù±‚`cabsÙ±‚`a(Ù±‚`axÙ±‚`a)Ù±‚`a)Ù±‚`a,Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`cmaxÙ±‚`a(Ù±‚`bnpÙ±‚aoa.Ù±‚`cabsÙ±‚`a(Ù±‚`ayÙ±‚`a)Ù±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`climÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`a(Ù±‚bnbcintÙ±‚`a(Ù±‚`exymaxÙ±‚aoa/Ù±‚`hbinwidthÙ±‚`a)Ù±‚`a Ù±‚aoa+Ù±‚`a Ù±‚bmia1Ù±‚`a)Ù±‚aoa*Ù±‚`hbinwidthÙ±‚`a
Ù±‚`a
Ù±‚`dbinsÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`farangeÙ±‚`a(Ù±‚aoa-Ù±‚`climÙ±‚`a,Ù±‚`a Ù±‚`climÙ±‚`a Ù±‚aoa+Ù±‚`a Ù±‚`hbinwidthÙ±‚`a,Ù±‚`a Ù±‚`hbinwidthÙ±‚`a)Ù±‚`a
Ù±‚`hax_histxÙ±‚aoa.Ù±‚`dhistÙ±‚`a(Ù±‚`axÙ±‚`a,Ù±‚`a Ù±‚`dbinsÙ±‚aoa=Ù±‚`dbinsÙ±‚`a)Ù±‚`a
Ù±‚`hax_histyÙ±‚aoa.Ù±‚`dhistÙ±‚`a(Ù±‚`ayÙ±‚`a,Ù±‚`a Ù±‚`dbinsÙ±‚aoa=Ù±‚`dbinsÙ±‚`a,Ù±‚`a Ù±‚`korientationÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1jhorizontalÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚bc1xA# the xaxis of ax_histx and yaxis of ax_histy are shared with ax,Ù±‚`a
Ù±‚bc1xE# thus there is no need to manually adjust the xlim and ylim of theseÙ±‚`a
Ù±‚bc1g# axis.Ù±‚`a
Ù±‚`a
Ù±‚`hax_histxÙ±‚aoa.Ù±‚`jset_yticksÙ±‚`a(Ù±‚`a[Ù±‚bmia0Ù±‚`a,Ù±‚`a Ù±‚bmib50Ù±‚`a,Ù±‚`a Ù±‚bmic100Ù±‚`a]Ù±‚`a)Ù±‚`a
Ù±‚`hax_histyÙ±‚aoa.Ù±‚`jset_xticksÙ±‚`a(Ù±‚`a[Ù±‚bmia0Ù±‚`a,Ù±‚`a Ù±‚bmib50Ù±‚`a,Ù±‚`a Ù±‚bmic100Ù±‚`a]Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`cpltÙ±‚aoa.Ù±‚`dshowÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚bc1xM#############################################################################Ù±‚`a
Ù±‚bc1a#Ù±‚`a
Ù±‚bc1x# .. admonition:: ReferencesÙ±‚`a
Ù±‚bc1a#Ù±‚`a
Ù±‚bc1xN#    The use of the following functions, methods, classes and modules is shownÙ±‚`a
Ù±‚bc1u#    in this example:Ù±‚`a
Ù±‚bc1a#Ù±‚`a
Ù±‚bc1xA#    - `mpl_toolkits.axes_grid1.axes_divider.make_axes_locatable`Ù±‚`a
Ù±‚bc1x(#    - `matplotlib.axes.Axes.set_aspect`Ù±‚`a
Ù±‚bc1x%#    - `matplotlib.axes.Axes.scatter`Ù±‚`a
Ù±‚bc1x"#    - `matplotlib.axes.Axes.hist`Ù±‚`a
`dNoneö