Ù¯‚Ù´ƒ˜Ù±‚bsdy·"""
=============================
Subplots spacings and margins
=============================

Adjusting the spacing of margins and subplots using `.pyplot.subplots_adjust`.

.. note::
   There is also a tool window to adjust the margins and spacings of displayed
   figures interactively.  It can be opened via the toolbar or by calling
   `.pyplot.subplot_tool`.

.. redirect-from:: /gallery/subplots_axes_and_figures/subplot_toolbar
"""Ù±‚`a
Ù±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnnfpyplotÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnncpltÙ±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„enumpyÙ „enumpyf1.22.3fmoduleenumpyfmoduleõÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnnbnpÙ±‚`a
Ù±‚`a
Ù±‚bc1x)# Fixing random state for reproducibilityÙ±‚`a
Ù±‚`bnpÙ±‚aoa.Ù±‚`frandomÙ±‚aoa.Ù±‚`dseedÙ±‚`a(Ù±‚bmih19680801Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`cpltÙ±‚aoa.Ù±‚`gsubplotÙ±‚`a(Ù±‚bmic211Ù±‚`a)Ù±‚`a
Ù±‚`cpltÙ±‚aoa.Ù±‚`fimshowÙ±‚`a(Ù±‚`bnpÙ±‚aoa.Ù±‚`frandomÙ±‚aoa.Ù±‚`frandomÙ±‚`a(Ù±‚`a(Ù±‚bmic100Ù±‚`a,Ù±‚`a Ù±‚bmic100Ù±‚`a)Ù±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`cpltÙ±‚aoa.Ù±‚`gsubplotÙ±‚`a(Ù±‚bmic212Ù±‚`a)Ù±‚`a
Ù±‚`cpltÙ±‚aoa.Ù±‚`fimshowÙ±‚`a(Ù±‚`bnpÙ±‚aoa.Ù±‚`frandomÙ±‚aoa.Ù±‚`frandomÙ±‚`a(Ù±‚`a(Ù±‚bmic100Ù±‚`a,Ù±‚`a Ù±‚bmic100Ù±‚`a)Ù±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`cpltÙ±‚aoa.Ù±‚`osubplots_adjustÙ±‚`a(Ù±‚`fbottomÙ±‚aoa=Ù±‚bmfc0.1Ù±‚`a,Ù±‚`a Ù±‚`erightÙ±‚aoa=Ù±‚bmfc0.8Ù±‚`a,Ù±‚`a Ù±‚`ctopÙ±‚aoa=Ù±‚bmfc0.9Ù±‚`a)Ù±‚`a
Ù±‚`ccaxÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cpltÙ±‚aoa.Ù±‚`daxesÙ±‚`a(Ù±‚`a[Ù±‚bmfd0.85Ù±‚`a,Ù±‚`a Ù±‚bmfc0.1Ù±‚`a,Ù±‚`a Ù±‚bmfe0.075Ù±‚`a,Ù±‚`a Ù±‚bmfc0.8Ù±‚`a]Ù±‚`a)Ù±‚`a
Ù±‚`cpltÙ±‚aoa.Ù±‚`hcolorbarÙ±‚`a(Ù±‚`ccaxÙ±‚aoa=Ù±‚`ccaxÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`cpltÙ±‚aoa.Ù±‚`dshowÙ±‚`a(Ù±‚`a)Ù±‚`a
`dNoneö