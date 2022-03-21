Ù¯‚Ù´ƒ˜{Ù±‚bsdyn"""
==========================================
Set default x-axis tick labels on the top
==========================================

We can use :rc:`xtick.labeltop` and :rc:`xtick.top` and :rc:`xtick.labelbottom`
and :rc:`xtick.bottom` to control where on the axes ticks and their labels
appear.

These properties can also be set in ``.matplotlib/matplotlibrc``.
"""Ù±‚`a
Ù±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnnfpyplotÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnncpltÙ±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„enumpyÙ „enumpyf1.22.3fmoduleenumpyfmoduleõÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnnbnpÙ±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚`cpltÙ±‚aoa.Ù±‚`hrcParamsÙ±‚`a[Ù±‚bs1a'Ù±‚bs1lxtick.bottomÙ±‚bs1a'Ù±‚`a]Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cpltÙ±‚aoa.Ù±‚`hrcParamsÙ±‚`a[Ù±‚bs1a'Ù±‚bs1qxtick.labelbottomÙ±‚bs1a'Ù±‚`a]Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bkceFalseÙ±‚`a
Ù±‚`cpltÙ±‚aoa.Ù±‚`hrcParamsÙ±‚`a[Ù±‚bs1a'Ù±‚bs1ixtick.topÙ±‚bs1a'Ù±‚`a]Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cpltÙ±‚aoa.Ù±‚`hrcParamsÙ±‚`a[Ù±‚bs1a'Ù±‚bs1nxtick.labeltopÙ±‚bs1a'Ù±‚`a]Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bkcdTrueÙ±‚`a
Ù±‚`a
Ù±‚`axÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`farangeÙ±‚`a(Ù±‚bmib10Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`cfigÙ±‚`a,Ù±‚`a Ù±‚`baxÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cpltÙ±‚aoa.Ù±‚`hsubplotsÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`dplotÙ±‚`a(Ù±‚`axÙ±‚`a)Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`iset_titleÙ±‚`a(Ù±‚bs1a'Ù±‚bs1jxlabel topÙ±‚bs1a'Ù±‚`a)Ù±‚`b  Ù±‚bc1x)# Note title moves to make room for ticksÙ±‚`a
Ù±‚`a
Ù±‚`cpltÙ±‚aoa.Ù±‚`dshowÙ±‚`a(Ù±‚`a)Ù±‚`a
`dNoneö