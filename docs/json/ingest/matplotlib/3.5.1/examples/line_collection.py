Ù¯‚Ù´ƒ™YÙ±‚bsdxÛ"""
===============
Line Collection
===============

Plotting lines with Matplotlib.

`~matplotlib.collections.LineCollection` allows one to plot multiple
lines on a figure. Below we show off some of its properties.
"""Ù±‚`a
Ù±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnnfpyplotÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnncpltÙ±‚`a
Ù±‚bkndfromÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnnkcollectionsÙ±‚`a Ù±‚bknfimportÙ±‚`a Ù±‚`nLineCollectionÙ±‚`a
Ù±‚bkndfromÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚`a Ù±‚bknfimportÙ±‚`a Ù±‚`fcolorsÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚`gmcolorsÙ±‚`a
Ù±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„enumpyÙ „enumpyf1.22.3fmoduleenumpyfmoduleõÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnnbnpÙ±‚`a
Ù±‚`a
Ù±‚bc1xB# In order to efficiently plot many lines in a single set of axes,Ù±‚`a
Ù±‚bc1xD# Matplotlib has the ability to add the lines all at once. Here is aÙ±‚`a
Ù±‚bc1x(# simple example showing how it is done.Ù±‚`a
Ù±‚`a
Ù±‚`axÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`farangeÙ±‚`a(Ù±‚bmic100Ù±‚`a)Ù±‚`a
Ù±‚bc1x'# Here are many sets of y to plot vs. xÙ±‚`a
Ù±‚`bysÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`axÙ±‚`a[Ù±‚`a:Ù±‚bmib50Ù±‚`a,Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`gnewaxisÙ±‚`a]Ù±‚`a Ù±‚aoa+Ù±‚`a Ù±‚`axÙ±‚`a[Ù±‚`bnpÙ±‚aoa.Ù±‚`gnewaxisÙ±‚`a,Ù±‚`a Ù±‚`a:Ù±‚`a]Ù±‚`a
Ù±‚`a
Ù±‚`dsegsÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`ezerosÙ±‚`a(Ù±‚`a(Ù±‚bmib50Ù±‚`a,Ù±‚`a Ù±‚bmic100Ù±‚`a,Ù±‚`a Ù±‚bmia2Ù±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`dsegsÙ±‚`a[Ù±‚`a:Ù±‚`a,Ù±‚`a Ù±‚`a:Ù±‚`a,Ù±‚`a Ù±‚bmia1Ù±‚`a]Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bysÙ±‚`a
Ù±‚`dsegsÙ±‚`a[Ù±‚`a:Ù±‚`a,Ù±‚`a Ù±‚`a:Ù±‚`a,Ù±‚`a Ù±‚bmia0Ù±‚`a]Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`axÙ±‚`a
Ù±‚`a
Ù±‚bc1x0# Mask some values to test masked array support:Ù±‚`a
Ù±‚`dsegsÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`bmaÙ±‚aoa.Ù±‚`lmasked_whereÙ±‚`a(Ù±‚`a(Ù±‚`dsegsÙ±‚`a Ù±‚aoa>Ù±‚`a Ù±‚bmib50Ù±‚`a)Ù±‚`a Ù±‚aoa&Ù±‚`a Ù±‚`a(Ù±‚`dsegsÙ±‚`a Ù±‚aoa<Ù±‚`a Ù±‚bmib60Ù±‚`a)Ù±‚`a,Ù±‚`a Ù±‚`dsegsÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚bc1x!# We need to set the plot limits.Ù±‚`a
Ù±‚`cfigÙ±‚`a,Ù±‚`a Ù±‚`baxÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cpltÙ±‚aoa.Ù±‚`hsubplotsÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`hset_xlimÙ±‚`a(Ù±‚`axÙ±‚aoa.Ù±‚`cminÙ±‚`a(Ù±‚`a)Ù±‚`a,Ù±‚`a Ù±‚`axÙ±‚aoa.Ù±‚`cmaxÙ±‚`a(Ù±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`hset_ylimÙ±‚`a(Ù±‚`bysÙ±‚aoa.Ù±‚`cminÙ±‚`a(Ù±‚`a)Ù±‚`a,Ù±‚`a Ù±‚`bysÙ±‚aoa.Ù±‚`cmaxÙ±‚`a(Ù±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚bc1x&# *colors* is sequence of rgba tuples.Ù±‚`a
Ù±‚bc1x@# *linestyle* is a string or dash tuple. Legal string values areÙ±‚`a
Ù±‚bc1xJ# solid|dashed|dashdot|dotted.  The dash tuple is (offset, onoffseq) whereÙ±‚`a
Ù±‚bc1xM# onoffseq is an even length tuple of on and off ink in points.  If linestyleÙ±‚`a
Ù±‚bc1x# is omitted, 'solid' is used.Ù±‚`a
Ù±‚bc1xC# See `matplotlib.collections.LineCollection` for more information.Ù±‚`a
Ù±‚`fcolorsÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`a[Ù±‚`gmcolorsÙ±‚aoa.Ù±‚`gto_rgbaÙ±‚`a(Ù±‚`acÙ±‚`a)Ù±‚`a
Ù±‚`j          Ù±‚akcforÙ±‚`a Ù±‚`acÙ±‚`a Ù±‚bowbinÙ±‚`a Ù±‚`cpltÙ±‚aoa.Ù±‚`hrcParamsÙ±‚`a[Ù±‚bs1a'Ù±‚bs1oaxes.prop_cycleÙ±‚bs1a'Ù±‚`a]Ù±‚aoa.Ù±‚`fby_keyÙ±‚`a(Ù±‚`a)Ù±‚`a[Ù±‚bs1a'Ù±‚bs1ecolorÙ±‚bs1a'Ù±‚`a]Ù±‚`a]Ù±‚`a
Ù±‚`a
Ù±‚`mline_segmentsÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`nLineCollectionÙ±‚`a(Ù±‚`dsegsÙ±‚`a,Ù±‚`a Ù±‚`jlinewidthsÙ±‚aoa=Ù±‚`a(Ù±‚bmfc0.5Ù±‚`a,Ù±‚`a Ù±‚bmia1Ù±‚`a,Ù±‚`a Ù±‚bmfc1.5Ù±‚`a,Ù±‚`a Ù±‚bmia2Ù±‚`a)Ù±‚`a,Ù±‚`a
Ù±‚`x                               Ù±‚`fcolorsÙ±‚aoa=Ù±‚`fcolorsÙ±‚`a,Ù±‚`a Ù±‚`ilinestyleÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1esolidÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`nadd_collectionÙ±‚`a(Ù±‚`mline_segmentsÙ±‚`a)Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`iset_titleÙ±‚`a(Ù±‚bs1a'Ù±‚bs1x"Line collection with masked arraysÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`cpltÙ±‚aoa.Ù±‚`dshowÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚bc1xO###############################################################################Ù±‚`a
Ù±‚bc1xB# In order to efficiently plot many lines in a single set of axes,Ù±‚`a
Ù±‚bc1xD# Matplotlib has the ability to add the lines all at once. Here is aÙ±‚`a
Ù±‚bc1x(# simple example showing how it is done.Ù±‚`a
Ù±‚`a
Ù±‚`aNÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bmib50Ù±‚`a
Ù±‚`axÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`farangeÙ±‚`a(Ù±‚`aNÙ±‚`a)Ù±‚`a
Ù±‚bc1x'# Here are many sets of y to plot vs. xÙ±‚`a
Ù±‚`bysÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`a[Ù±‚`axÙ±‚`a Ù±‚aoa+Ù±‚`a Ù±‚`aiÙ±‚`a Ù±‚akcforÙ±‚`a Ù±‚`aiÙ±‚`a Ù±‚bowbinÙ±‚`a Ù±‚`axÙ±‚`a]Ù±‚`a
Ù±‚`a
Ù±‚bc1x9# We need to set the plot limits, they will not autoscaleÙ±‚`a
Ù±‚`cfigÙ±‚`a,Ù±‚`a Ù±‚`baxÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cpltÙ±‚aoa.Ù±‚`hsubplotsÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`hset_xlimÙ±‚`a(Ù±‚`bnpÙ±‚aoa.Ù±‚`cminÙ±‚`a(Ù±‚`axÙ±‚`a)Ù±‚`a,Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`cmaxÙ±‚`a(Ù±‚`axÙ±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`hset_ylimÙ±‚`a(Ù±‚`bnpÙ±‚aoa.Ù±‚`cminÙ±‚`a(Ù±‚`bysÙ±‚`a)Ù±‚`a,Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`cmaxÙ±‚`a(Ù±‚`bysÙ±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚bc1x## colors is sequence of rgba tuplesÙ±‚`a
Ù±‚bc1x># linestyle is a string or dash tuple. Legal string values areÙ±‚`a
Ù±‚bc1xM#          solid|dashed|dashdot|dotted.  The dash tuple is (offset, onoffseq)Ù±‚`a
Ù±‚bc1xN#          where onoffseq is an even length tuple of on and off ink in points.Ù±‚`a
Ù±‚bc1x3#          If linestyle is omitted, 'solid' is usedÙ±‚`a
Ù±‚bc1xB# See `matplotlib.collections.LineCollection` for more informationÙ±‚`a
Ù±‚`a
Ù±‚bc1x"# Make a sequence of (x, y) pairs.Ù±‚`a
Ù±‚`mline_segmentsÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`nLineCollectionÙ±‚`a(Ù±‚`a[Ù±‚`bnpÙ±‚aoa.Ù±‚`lcolumn_stackÙ±‚`a(Ù±‚`a[Ù±‚`axÙ±‚`a,Ù±‚`a Ù±‚`ayÙ±‚`a]Ù±‚`a)Ù±‚`a Ù±‚akcforÙ±‚`a Ù±‚`ayÙ±‚`a Ù±‚bowbinÙ±‚`a Ù±‚`bysÙ±‚`a]Ù±‚`a,Ù±‚`a
Ù±‚`x                               Ù±‚`jlinewidthsÙ±‚aoa=Ù±‚`a(Ù±‚bmfc0.5Ù±‚`a,Ù±‚`a Ù±‚bmia1Ù±‚`a,Ù±‚`a Ù±‚bmfc1.5Ù±‚`a,Ù±‚`a Ù±‚bmia2Ù±‚`a)Ù±‚`a,Ù±‚`a
Ù±‚`x                               Ù±‚`jlinestylesÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1esolidÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`mline_segmentsÙ±‚aoa.Ù±‚`iset_arrayÙ±‚`a(Ù±‚`axÙ±‚`a)Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`nadd_collectionÙ±‚`a(Ù±‚`mline_segmentsÙ±‚`a)Ù±‚`a
Ù±‚`daxcbÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cfigÙ±‚aoa.Ù±‚`hcolorbarÙ±‚`a(Ù±‚`mline_segmentsÙ±‚`a)Ù±‚`a
Ù±‚`daxcbÙ±‚aoa.Ù±‚`iset_labelÙ±‚`a(Ù±‚bs1a'Ù±‚bs1kLine NumberÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`iset_titleÙ±‚`a(Ù±‚bs1a'Ù±‚bs1x"Line Collection with mapped colorsÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`cpltÙ±‚aoa.Ù±‚`csciÙ±‚`a(Ù±‚`mline_segmentsÙ±‚`a)Ù±‚`b  Ù±‚bc1x3# This allows interactive changing of the colormap.Ù±‚`a
Ù±‚`cpltÙ±‚aoa.Ù±‚`dshowÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚bc1xM#############################################################################Ù±‚`a
Ù±‚bc1a#Ù±‚`a
Ù±‚bc1x# .. admonition:: ReferencesÙ±‚`a
Ù±‚bc1a#Ù±‚`a
Ù±‚bc1xN#    The use of the following functions, methods, classes and modules is shownÙ±‚`a
Ù±‚bc1u#    in this example:Ù±‚`a
Ù±‚bc1a#Ù±‚`a
Ù±‚bc1x#    - `matplotlib.collections`Ù±‚`a
Ù±‚bc1x.#    - `matplotlib.collections.LineCollection`Ù±‚`a
Ù±‚bc1x/#    - `matplotlib.cm.ScalarMappable.set_array`Ù±‚`a
Ù±‚bc1x,#    - `matplotlib.axes.Axes.add_collection`Ù±‚`a
Ù±‚bc1xI#    - `matplotlib.figure.Figure.colorbar` / `matplotlib.pyplot.colorbar`Ù±‚`a
Ù±‚bc1x#    - `matplotlib.pyplot.sci`Ù±‚`a
`dNoneö