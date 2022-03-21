Ù¯‚Ù´ƒ˜ñÙ±‚bsdy"""
====================================
Automatically setting tick positions
====================================

Setting the behavior of tick auto-placement.

By default, Matplotlib will choose the number of ticks and tick positions so
that there is a reasonable number of ticks on the axis and they are located
at "round" numbers.

As a result, there may be no ticks on the edges of the plot.
"""Ù±‚`a
Ù±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnnfpyplotÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnncpltÙ±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„enumpyÙ „enumpyf1.22.3fmoduleenumpyfmoduleõÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnnbnpÙ±‚`a
Ù±‚`bnpÙ±‚aoa.Ù±‚`frandomÙ±‚aoa.Ù±‚`dseedÙ±‚`a(Ù±‚bmih19680801Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`cfigÙ±‚`a,Ù±‚`a Ù±‚`baxÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cpltÙ±‚aoa.Ù±‚`hsubplotsÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`ddotsÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`hlinspaceÙ±‚`a(Ù±‚bmfc0.3Ù±‚`a,Ù±‚`a Ù±‚bmfc1.2Ù±‚`a,Ù±‚`a Ù±‚bmib10Ù±‚`a)Ù±‚`a
Ù±‚`aXÙ±‚`a,Ù±‚`a Ù±‚`aYÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`hmeshgridÙ±‚`a(Ù±‚`ddotsÙ±‚`a,Ù±‚`a Ù±‚`ddotsÙ±‚`a)Ù±‚`a
Ù±‚`axÙ±‚`a,Ù±‚`a Ù±‚`ayÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`aXÙ±‚aoa.Ù±‚`eravelÙ±‚`a(Ù±‚`a)Ù±‚`a,Ù±‚`a Ù±‚`aYÙ±‚aoa.Ù±‚`eravelÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`gscatterÙ±‚`a(Ù±‚`axÙ±‚`a,Ù±‚`a Ù±‚`ayÙ±‚`a,Ù±‚`a Ù±‚`acÙ±‚aoa=Ù±‚`axÙ±‚aoa+Ù±‚`ayÙ±‚`a)Ù±‚`a
Ù±‚`cpltÙ±‚aoa.Ù±‚`dshowÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚bc1xO###############################################################################Ù±‚`a
Ù±‚bc1xN# If you want to keep ticks at round numbers, and also have ticks at the edgesÙ±‚`a
Ù±‚bc1xO# you can switch :rc:`axes.autolimit_mode` to 'round_numbers'. This expands theÙ±‚`a
Ù±‚bc1x'# axis limits to the next round number.Ù±‚`a
Ù±‚`a
Ù±‚`cpltÙ±‚aoa.Ù±‚`hrcParamsÙ±‚`a[Ù±‚bs1a'Ù±‚bs1saxes.autolimit_modeÙ±‚bs1a'Ù±‚`a]Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bs1a'Ù±‚bs1mround_numbersÙ±‚bs1a'Ù±‚`a
Ù±‚`a
Ù±‚bc1xE# Note: The limits are calculated at draw-time. Therefore, when usingÙ±‚`a
Ù±‚bc1xF# :rc:`axes.autolimit_mode` in a context manager, it is important thatÙ±‚`a
Ù±‚bc1x/# the ``show()`` command is within the context.Ù±‚`a
Ù±‚`a
Ù±‚`cfigÙ±‚`a,Ù±‚`a Ù±‚`baxÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cpltÙ±‚aoa.Ù±‚`hsubplotsÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`gscatterÙ±‚`a(Ù±‚`axÙ±‚`a,Ù±‚`a Ù±‚`ayÙ±‚`a,Ù±‚`a Ù±‚`acÙ±‚aoa=Ù±‚`axÙ±‚aoa+Ù±‚`ayÙ±‚`a)Ù±‚`a
Ù±‚`cpltÙ±‚aoa.Ù±‚`dshowÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚bc1xO###############################################################################Ù±‚`a
Ù±‚bc1xN# The round numbers autolimit_mode is still respected if you set an additionalÙ±‚`a
Ù±‚bc1xI# margin around the data using `.Axes.set_xmargin` / `.Axes.set_ymargin`:Ù±‚`a
Ù±‚`a
Ù±‚`cfigÙ±‚`a,Ù±‚`a Ù±‚`baxÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cpltÙ±‚aoa.Ù±‚`hsubplotsÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`gscatterÙ±‚`a(Ù±‚`axÙ±‚`a,Ù±‚`a Ù±‚`ayÙ±‚`a,Ù±‚`a Ù±‚`acÙ±‚aoa=Ù±‚`axÙ±‚aoa+Ù±‚`ayÙ±‚`a)Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`kset_xmarginÙ±‚`a(Ù±‚bmfc0.8Ù±‚`a)Ù±‚`a
Ù±‚`cpltÙ±‚aoa.Ù±‚`dshowÙ±‚`a(Ù±‚`a)Ù±‚`a
`dNoneö