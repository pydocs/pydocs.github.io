Ù¯‚Ù´ƒ™Ù±‚bsdy\"""
===============
Aligning Labels
===============

Aligning xlabel and ylabel using `.Figure.align_xlabels` and
`.Figure.align_ylabels`

`.Figure.align_labels` wraps these two functions.

Note that the xlabel "XLabel1 1" would normally be much closer to the
x-axis, and "YLabel1 0" would be much closer to the y-axis of their
respective axes.
"""Ù±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnnfpyplotÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnncpltÙ±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„enumpyÙ „enumpyf1.22.3fmoduleenumpyfmoduleõÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnnbnpÙ±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnnhgridspecÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnnhgridspecÙ±‚`a
Ù±‚`a
Ù±‚`cfigÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cpltÙ±‚aoa.Ù±‚`ffigureÙ±‚`a(Ù±‚`ltight_layoutÙ±‚aoa=Ù±‚bkcdTrueÙ±‚`a)Ù±‚`a
Ù±‚`bgsÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`hgridspecÙ±‚aoa.Ù±‚`hGridSpecÙ±‚`a(Ù±‚bmia2Ù±‚`a,Ù±‚`a Ù±‚bmia2Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`baxÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cfigÙ±‚aoa.Ù±‚`kadd_subplotÙ±‚`a(Ù±‚`bgsÙ±‚`a[Ù±‚bmia0Ù±‚`a,Ù±‚`a Ù±‚`a:Ù±‚`a]Ù±‚`a)Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`dplotÙ±‚`a(Ù±‚`bnpÙ±‚aoa.Ù±‚`farangeÙ±‚`a(Ù±‚bmia0Ù±‚`a,Ù±‚`a Ù±‚bmfc1e6Ù±‚`a,Ù±‚`a Ù±‚bmid1000Ù±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`jset_ylabelÙ±‚`a(Ù±‚bs1a'Ù±‚bs1gYLabel0Ù±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`jset_xlabelÙ±‚`a(Ù±‚bs1a'Ù±‚bs1gXLabel0Ù±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚akcforÙ±‚`a Ù±‚`aiÙ±‚`a Ù±‚bowbinÙ±‚`a Ù±‚bnberangeÙ±‚`a(Ù±‚bmia2Ù±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`d    Ù±‚`baxÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cfigÙ±‚aoa.Ù±‚`kadd_subplotÙ±‚`a(Ù±‚`bgsÙ±‚`a[Ù±‚bmia1Ù±‚`a,Ù±‚`a Ù±‚`aiÙ±‚`a]Ù±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`baxÙ±‚aoa.Ù±‚`dplotÙ±‚`a(Ù±‚`bnpÙ±‚aoa.Ù±‚`farangeÙ±‚`a(Ù±‚bmfb1.Ù±‚`a,Ù±‚`a Ù±‚bmfb0.Ù±‚`a,Ù±‚`a Ù±‚aoa-Ù±‚bmfc0.1Ù±‚`a)Ù±‚`a Ù±‚aoa*Ù±‚`a Ù±‚bmfe2000.Ù±‚`a,Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`farangeÙ±‚`a(Ù±‚bmfb1.Ù±‚`a,Ù±‚`a Ù±‚bmfb0.Ù±‚`a,Ù±‚`a Ù±‚aoa-Ù±‚bmfc0.1Ù±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`baxÙ±‚aoa.Ù±‚`jset_ylabelÙ±‚`a(Ù±‚bs1a'Ù±‚bs1hYLabel1 Ù±‚bsib%dÙ±‚bs1a'Ù±‚`a Ù±‚aoa%Ù±‚`a Ù±‚`aiÙ±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`baxÙ±‚aoa.Ù±‚`jset_xlabelÙ±‚`a(Ù±‚bs1a'Ù±‚bs1hXLabel1 Ù±‚bsib%dÙ±‚bs1a'Ù±‚`a Ù±‚aoa%Ù±‚`a Ù±‚`aiÙ±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚akbifÙ±‚`a Ù±‚`aiÙ±‚`a Ù±‚aob==Ù±‚`a Ù±‚bmia0Ù±‚`a:Ù±‚`a
Ù±‚`h        Ù±‚akcforÙ±‚`a Ù±‚`dtickÙ±‚`a Ù±‚bowbinÙ±‚`a Ù±‚`baxÙ±‚aoa.Ù±‚`oget_xticklabelsÙ±‚`a(Ù±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`l            Ù±‚`dtickÙ±‚aoa.Ù±‚`lset_rotationÙ±‚`a(Ù±‚bmib55Ù±‚`a)Ù±‚`a
Ù±‚`cfigÙ±‚aoa.Ù±‚`lalign_labelsÙ±‚`a(Ù±‚`a)Ù±‚`b  Ù±‚bc1x2# same as fig.align_xlabels(); fig.align_ylabels()Ù±‚`a
Ù±‚`a
Ù±‚`cpltÙ±‚aoa.Ù±‚`dshowÙ±‚`a(Ù±‚`a)Ù±‚`a
`dNoneö