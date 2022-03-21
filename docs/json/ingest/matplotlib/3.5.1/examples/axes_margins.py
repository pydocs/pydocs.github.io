Ù¯‚Ù´ƒ™Ù±‚bsdyÔ"""
======================================================
Controlling view limits using margins and sticky_edges
======================================================

The first figure in this example shows how to zoom in and out of a
plot using `~.Axes.margins` instead of `~.Axes.set_xlim` and
`~.Axes.set_ylim`. The second figure demonstrates the concept of
edge "stickiness" introduced by certain methods and artists and how
to effectively work around that.

"""Ù±‚`a
Ù±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„enumpyÙ „enumpyf1.22.3fmoduleenumpyfmoduleõÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnnbnpÙ±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnnfpyplotÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnncpltÙ±‚`a
Ù±‚bkndfromÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnngpatchesÙ±‚`a Ù±‚bknfimportÙ±‚`a Ù±‚`gPolygonÙ±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚akcdefÙ±‚`a Ù±‚bnfafÙ±‚`a(Ù±‚`atÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`d    Ù±‚akfreturnÙ±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`cexpÙ±‚`a(Ù±‚aoa-Ù±‚`atÙ±‚`a)Ù±‚`a Ù±‚aoa*Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`ccosÙ±‚`a(Ù±‚bmia2Ù±‚aoa*Ù±‚`bnpÙ±‚aoa.Ù±‚`bpiÙ±‚aoa*Ù±‚`atÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚`bt1Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`farangeÙ±‚`a(Ù±‚bmfc0.0Ù±‚`a,Ù±‚`a Ù±‚bmfc3.0Ù±‚`a,Ù±‚`a Ù±‚bmfd0.01Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`cax1Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cpltÙ±‚aoa.Ù±‚`gsubplotÙ±‚`a(Ù±‚bmic212Ù±‚`a)Ù±‚`a
Ù±‚`cax1Ù±‚aoa.Ù±‚`gmarginsÙ±‚`a(Ù±‚bmfd0.05Ù±‚`a)Ù±‚`k           Ù±‚bc1x+# Default margin is 0.05, value 0 means fitÙ±‚`a
Ù±‚`cax1Ù±‚aoa.Ù±‚`dplotÙ±‚`a(Ù±‚`bt1Ù±‚`a,Ù±‚`a Ù±‚`afÙ±‚`a(Ù±‚`bt1Ù±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`cax2Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cpltÙ±‚aoa.Ù±‚`gsubplotÙ±‚`a(Ù±‚bmic221Ù±‚`a)Ù±‚`a
Ù±‚`cax2Ù±‚aoa.Ù±‚`gmarginsÙ±‚`a(Ù±‚bmia2Ù±‚`a,Ù±‚`a Ù±‚bmia2Ù±‚`a)Ù±‚`k           Ù±‚bc1v# Values >0.0 zoom outÙ±‚`a
Ù±‚`cax2Ù±‚aoa.Ù±‚`dplotÙ±‚`a(Ù±‚`bt1Ù±‚`a,Ù±‚`a Ù±‚`afÙ±‚`a(Ù±‚`bt1Ù±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`cax2Ù±‚aoa.Ù±‚`iset_titleÙ±‚`a(Ù±‚bs1a'Ù±‚bs1jZoomed outÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`cax3Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cpltÙ±‚aoa.Ù±‚`gsubplotÙ±‚`a(Ù±‚bmic222Ù±‚`a)Ù±‚`a
Ù±‚`cax3Ù±‚aoa.Ù±‚`gmarginsÙ±‚`a(Ù±‚`axÙ±‚aoa=Ù±‚bmia0Ù±‚`a,Ù±‚`a Ù±‚`ayÙ±‚aoa=Ù±‚aoa-Ù±‚bmfd0.25Ù±‚`a)Ù±‚`c   Ù±‚bc1x*# Values in (-0.5, 0.0) zooms in to centerÙ±‚`a
Ù±‚`cax3Ù±‚aoa.Ù±‚`dplotÙ±‚`a(Ù±‚`bt1Ù±‚`a,Ù±‚`a Ù±‚`afÙ±‚`a(Ù±‚`bt1Ù±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`cax3Ù±‚aoa.Ù±‚`iset_titleÙ±‚`a(Ù±‚bs1a'Ù±‚bs1iZoomed inÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`cpltÙ±‚aoa.Ù±‚`dshowÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚bc1xM#############################################################################Ù±‚`a
Ù±‚bc1a#Ù±‚`a
Ù±‚bc1x1# On the "stickiness" of certain plotting methodsÙ±‚`a
Ù±‚bc1x1# """""""""""""""""""""""""""""""""""""""""""""""Ù±‚`a
Ù±‚bc1a#Ù±‚`a
Ù±‚bc1xM# Some plotting functions make the axis limits "sticky" or immune to the willÙ±‚`a
Ù±‚bc1xD# of the `~.Axes.margins` methods. For instance, `~.Axes.imshow` andÙ±‚`a
Ù±‚bc1xK# `~.Axes.pcolor` expect the user to want the limits to be tight around theÙ±‚`a
Ù±‚bc1xL# pixels shown in the plot. If this behavior is not desired, you need to setÙ±‚`a
Ù±‚bc1xG# `~.Axes.use_sticky_edges` to `False`. Consider the following example:Ù±‚`a
Ù±‚`a
Ù±‚`ayÙ±‚`a,Ù±‚`a Ù±‚`axÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`emgridÙ±‚`a[Ù±‚`a:Ù±‚bmia5Ù±‚`a,Ù±‚`a Ù±‚bmia1Ù±‚`a:Ù±‚bmia6Ù±‚`a]Ù±‚`a
Ù±‚`kpoly_coordsÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`a[Ù±‚`a
Ù±‚`d    Ù±‚`a(Ù±‚bmfd0.25Ù±‚`a,Ù±‚`a Ù±‚bmfd2.75Ù±‚`a)Ù±‚`a,Ù±‚`a Ù±‚`a(Ù±‚bmfd3.25Ù±‚`a,Ù±‚`a Ù±‚bmfd2.75Ù±‚`a)Ù±‚`a,Ù±‚`a
Ù±‚`d    Ù±‚`a(Ù±‚bmfd2.25Ù±‚`a,Ù±‚`a Ù±‚bmfd0.75Ù±‚`a)Ù±‚`a,Ù±‚`a Ù±‚`a(Ù±‚bmfd0.25Ù±‚`a,Ù±‚`a Ù±‚bmfd0.75Ù±‚`a)Ù±‚`a
Ù±‚`a]Ù±‚`a
Ù±‚`cfigÙ±‚`a,Ù±‚`a Ù±‚`a(Ù±‚`cax1Ù±‚`a,Ù±‚`a Ù±‚`cax2Ù±‚`a)Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cpltÙ±‚aoa.Ù±‚`hsubplotsÙ±‚`a(Ù±‚`encolsÙ±‚aoa=Ù±‚bmia2Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚bc1x2# Here we set the stickiness of the axes object...Ù±‚`a
Ù±‚bc1x9# ax1 we'll leave as the default, which uses sticky edgesÙ±‚`a
Ù±‚bc1x'# and we'll turn off stickiness for ax2Ù±‚`a
Ù±‚`cax2Ù±‚aoa.Ù±‚`puse_sticky_edgesÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bkceFalseÙ±‚`a
Ù±‚`a
Ù±‚akcforÙ±‚`a Ù±‚`baxÙ±‚`a,Ù±‚`a Ù±‚`fstatusÙ±‚`a Ù±‚bowbinÙ±‚`a Ù±‚bnbczipÙ±‚`a(Ù±‚`a(Ù±‚`cax1Ù±‚`a,Ù±‚`a Ù±‚`cax2Ù±‚`a)Ù±‚`a,Ù±‚`a Ù±‚`a(Ù±‚bs1a'Ù±‚bs1bIsÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚bs1a'Ù±‚bs1fIs NotÙ±‚bs1a'Ù±‚`a)Ù±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`d    Ù±‚`ecellsÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`baxÙ±‚aoa.Ù±‚`fpcolorÙ±‚`a(Ù±‚`axÙ±‚`a,Ù±‚`a Ù±‚`ayÙ±‚`a,Ù±‚`a Ù±‚`axÙ±‚aoa+Ù±‚`ayÙ±‚`a,Ù±‚`a Ù±‚`dcmapÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1ginfernoÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`gshadingÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1dautoÙ±‚bs1a'Ù±‚`a)Ù±‚`b  Ù±‚bc1h# stickyÙ±‚`a
Ù±‚`d    Ù±‚`baxÙ±‚aoa.Ù±‚`iadd_patchÙ±‚`a(Ù±‚`a
Ù±‚`h        Ù±‚`gPolygonÙ±‚`a(Ù±‚`kpoly_coordsÙ±‚`a,Ù±‚`a Ù±‚`ecolorÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1kforestgreenÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`ealphaÙ±‚aoa=Ù±‚bmfc0.5Ù±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`a)Ù±‚`b  Ù±‚bc1l# not stickyÙ±‚`a
Ù±‚`d    Ù±‚`baxÙ±‚aoa.Ù±‚`gmarginsÙ±‚`a(Ù±‚`axÙ±‚aoa=Ù±‚bmfc0.1Ù±‚`a,Ù±‚`a Ù±‚`ayÙ±‚aoa=Ù±‚bmfd0.05Ù±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`baxÙ±‚aoa.Ù±‚`jset_aspectÙ±‚`a(Ù±‚bs1a'Ù±‚bs1eequalÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`baxÙ±‚aoa.Ù±‚`iset_titleÙ±‚`a(Ù±‚bs1a'Ù±‚bsib{}Ù±‚bs1g StickyÙ±‚bs1a'Ù±‚aoa.Ù±‚`fformatÙ±‚`a(Ù±‚`fstatusÙ±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`cpltÙ±‚aoa.Ù±‚`dshowÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚bc1xM#############################################################################Ù±‚`a
Ù±‚bc1a#Ù±‚`a
Ù±‚bc1x# .. admonition:: ReferencesÙ±‚`a
Ù±‚bc1a#Ù±‚`a
Ù±‚bc1xN#    The use of the following functions, methods, classes and modules is shownÙ±‚`a
Ù±‚bc1u#    in this example:Ù±‚`a
Ù±‚bc1a#Ù±‚`a
Ù±‚bc1xC#    - `matplotlib.axes.Axes.margins` / `matplotlib.pyplot.margins`Ù±‚`a
Ù±‚bc1x.#    - `matplotlib.axes.Axes.use_sticky_edges`Ù±‚`a
Ù±‚bc1xA#    - `matplotlib.axes.Axes.pcolor` / `matplotlib.pyplot.pcolor`Ù±‚`a
Ù±‚bc1x##    - `matplotlib.patches.Polygon`Ù±‚`a
`dNoneö