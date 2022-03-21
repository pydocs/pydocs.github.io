Ù¯‚Ù´ƒ˜Ù±‚bsdx}"""
============
Dollar Ticks
============

Use a `~.ticker.FormatStrFormatter` to prepend dollar signs on y axis labels.
"""Ù±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„enumpyÙ „enumpyf1.22.3fmoduleenumpyfmoduleõÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnnbnpÙ±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnnfpyplotÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnncpltÙ±‚`a
Ù±‚`a
Ù±‚bc1x)# Fixing random state for reproducibilityÙ±‚`a
Ù±‚`bnpÙ±‚aoa.Ù±‚`frandomÙ±‚aoa.Ù±‚`dseedÙ±‚`a(Ù±‚bmih19680801Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`cfigÙ±‚`a,Ù±‚`a Ù±‚`baxÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cpltÙ±‚aoa.Ù±‚`hsubplotsÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`dplotÙ±‚`a(Ù±‚bmic100Ù±‚aoa*Ù±‚`bnpÙ±‚aoa.Ù±‚`frandomÙ±‚aoa.Ù±‚`drandÙ±‚`a(Ù±‚bmib20Ù±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚bc1x"# Use automatic StrMethodFormatterÙ±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`eyaxisÙ±‚aoa.Ù±‚`sset_major_formatterÙ±‚`a(Ù±‚bs1a'Ù±‚bs1a$Ù±‚bsih{x:1.2f}Ù±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`eyaxisÙ±‚aoa.Ù±‚`oset_tick_paramsÙ±‚`a(Ù±‚`ewhichÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1emajorÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`jlabelcolorÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1egreenÙ±‚bs1a'Ù±‚`a,Ù±‚`a
Ù±‚`x                         Ù±‚`ilabelleftÙ±‚aoa=Ù±‚bkceFalseÙ±‚`a,Ù±‚`a Ù±‚`jlabelrightÙ±‚aoa=Ù±‚bkcdTrueÙ±‚`a)Ù±‚`a
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
Ù±‚bc1x##    - `matplotlib.pyplot.subplots`Ù±‚`a
Ù±‚bc1x1#    - `matplotlib.axis.Axis.set_major_formatter`Ù±‚`a
Ù±‚bc1x-#    - `matplotlib.axis.Axis.set_tick_params`Ù±‚`a
Ù±‚bc1x#    - `matplotlib.axis.Tick`Ù±‚`a
Ù±‚bc1x-#    - `matplotlib.ticker.StrMethodFormatter`Ù±‚`a
`dNoneö