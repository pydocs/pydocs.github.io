Ù¯‚Ù´ƒ˜¦Ù±‚bsdx"""
=========
Stem Plot
=========

`~.pyplot.stem` plots vertical lines from a baseline to the y-coordinate and
places a marker at the tip.
"""Ù±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnnfpyplotÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnncpltÙ±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„enumpyÙ „enumpyf1.22.3fmoduleenumpyfmoduleõÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnnbnpÙ±‚`a
Ù±‚`a
Ù±‚`axÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`hlinspaceÙ±‚`a(Ù±‚bmfc0.1Ù±‚`a,Ù±‚`a Ù±‚bmia2Ù±‚`a Ù±‚aoa*Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`bpiÙ±‚`a,Ù±‚`a Ù±‚bmib41Ù±‚`a)Ù±‚`a
Ù±‚`ayÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`cexpÙ±‚`a(Ù±‚`bnpÙ±‚aoa.Ù±‚`csinÙ±‚`a(Ù±‚`axÙ±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`cpltÙ±‚aoa.Ù±‚`dstemÙ±‚`a(Ù±‚`axÙ±‚`a,Ù±‚`a Ù±‚`ayÙ±‚`a)Ù±‚`a
Ù±‚`cpltÙ±‚aoa.Ù±‚`dshowÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚bc1xM#############################################################################Ù±‚`a
Ù±‚bc1a#Ù±‚`a
Ù±‚bc1x=# The position of the baseline can be adapted using *bottom*.Ù±‚`a
Ù±‚bc1xK# The parameters *linefmt*, *markerfmt*, and *basefmt* control basic formatÙ±‚`a
Ù±‚bc1xI# properties of the plot. However, in contrast to `~.pyplot.plot` not allÙ±‚`a
Ù±‚bc1xF# properties are configurable via keyword arguments. For more advancedÙ±‚`a
Ù±‚bc1x7# control adapt the line objects returned by `.pyplot`.Ù±‚`a
Ù±‚`a
Ù±‚`jmarkerlineÙ±‚`a,Ù±‚`a Ù±‚`istemlinesÙ±‚`a,Ù±‚`a Ù±‚`hbaselineÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cpltÙ±‚aoa.Ù±‚`dstemÙ±‚`a(Ù±‚`a
Ù±‚`d    Ù±‚`axÙ±‚`a,Ù±‚`a Ù±‚`ayÙ±‚`a,Ù±‚`a Ù±‚`glinefmtÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1dgreyÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`imarkerfmtÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1aDÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`fbottomÙ±‚aoa=Ù±‚bmfc1.1Ù±‚`a)Ù±‚`a
Ù±‚`jmarkerlineÙ±‚aoa.Ù±‚`sset_markerfacecolorÙ±‚`a(Ù±‚bs1a'Ù±‚bs1dnoneÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`cpltÙ±‚aoa.Ù±‚`dshowÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚bc1xM#############################################################################Ù±‚`a
Ù±‚bc1a#Ù±‚`a
Ù±‚bc1x# .. admonition:: ReferencesÙ±‚`a
Ù±‚bc1a#Ù±‚`a
Ù±‚bc1xN#    The use of the following functions, methods, classes and modules is shownÙ±‚`a
Ù±‚bc1u#    in this example:Ù±‚`a
Ù±‚bc1a#Ù±‚`a
Ù±‚bc1x=#    - `matplotlib.axes.Axes.stem` / `matplotlib.pyplot.stem`Ù±‚`a
`dNoneö