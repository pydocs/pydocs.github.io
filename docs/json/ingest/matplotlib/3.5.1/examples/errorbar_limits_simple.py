Ù¯‚Ù´ƒ™ÒÙ±‚bsdy9"""
========================
Errorbar limit selection
========================

Illustration of selectively drawing lower and/or upper limit symbols on
errorbars using the parameters ``uplims``, ``lolims`` of `~.pyplot.errorbar`.

Alternatively, you can use 2xN values to draw errorbars in only one direction.
"""Ù±‚`a
Ù±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„enumpyÙ „enumpyf1.22.3fmoduleenumpyfmoduleõÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnnbnpÙ±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnnfpyplotÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnncpltÙ±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚`cfigÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cpltÙ±‚aoa.Ù±‚`ffigureÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`axÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`farangeÙ±‚`a(Ù±‚bmib10Ù±‚`a)Ù±‚`a
Ù±‚`ayÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bmfc2.5Ù±‚`a Ù±‚aoa*Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`csinÙ±‚`a(Ù±‚`axÙ±‚`a Ù±‚aoa/Ù±‚`a Ù±‚bmib20Ù±‚`a Ù±‚aoa*Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`bpiÙ±‚`a)Ù±‚`a
Ù±‚`dyerrÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`hlinspaceÙ±‚`a(Ù±‚bmfd0.05Ù±‚`a,Ù±‚`a Ù±‚bmfc0.2Ù±‚`a,Ù±‚`a Ù±‚bmib10Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`cpltÙ±‚aoa.Ù±‚`herrorbarÙ±‚`a(Ù±‚`axÙ±‚`a,Ù±‚`a Ù±‚`ayÙ±‚`a Ù±‚aoa+Ù±‚`a Ù±‚bmia3Ù±‚`a,Ù±‚`a Ù±‚`dyerrÙ±‚aoa=Ù±‚`dyerrÙ±‚`a,Ù±‚`a Ù±‚`elabelÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1uboth limits (default)Ù±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`cpltÙ±‚aoa.Ù±‚`herrorbarÙ±‚`a(Ù±‚`axÙ±‚`a,Ù±‚`a Ù±‚`ayÙ±‚`a Ù±‚aoa+Ù±‚`a Ù±‚bmia2Ù±‚`a,Ù±‚`a Ù±‚`dyerrÙ±‚aoa=Ù±‚`dyerrÙ±‚`a,Ù±‚`a Ù±‚`fuplimsÙ±‚aoa=Ù±‚bkcdTrueÙ±‚`a,Ù±‚`a Ù±‚`elabelÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1kuplims=TrueÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`cpltÙ±‚aoa.Ù±‚`herrorbarÙ±‚`a(Ù±‚`axÙ±‚`a,Ù±‚`a Ù±‚`ayÙ±‚`a Ù±‚aoa+Ù±‚`a Ù±‚bmia1Ù±‚`a,Ù±‚`a Ù±‚`dyerrÙ±‚aoa=Ù±‚`dyerrÙ±‚`a,Ù±‚`a Ù±‚`fuplimsÙ±‚aoa=Ù±‚bkcdTrueÙ±‚`a,Ù±‚`a Ù±‚`flolimsÙ±‚aoa=Ù±‚bkcdTrueÙ±‚`a,Ù±‚`a
Ù±‚`m             Ù±‚`elabelÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1xuplims=True, lolims=TrueÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`kupperlimitsÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`a[Ù±‚bkcdTrueÙ±‚`a,Ù±‚`a Ù±‚bkceFalseÙ±‚`a]Ù±‚`a Ù±‚aoa*Ù±‚`a Ù±‚bmia5Ù±‚`a
Ù±‚`klowerlimitsÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`a[Ù±‚bkceFalseÙ±‚`a,Ù±‚`a Ù±‚bkcdTrueÙ±‚`a]Ù±‚`a Ù±‚aoa*Ù±‚`a Ù±‚bmia5Ù±‚`a
Ù±‚`cpltÙ±‚aoa.Ù±‚`herrorbarÙ±‚`a(Ù±‚`axÙ±‚`a,Ù±‚`a Ù±‚`ayÙ±‚`a,Ù±‚`a Ù±‚`dyerrÙ±‚aoa=Ù±‚`dyerrÙ±‚`a,Ù±‚`a Ù±‚`fuplimsÙ±‚aoa=Ù±‚`kupperlimitsÙ±‚`a,Ù±‚`a Ù±‚`flolimsÙ±‚aoa=Ù±‚`klowerlimitsÙ±‚`a,Ù±‚`a
Ù±‚`m             Ù±‚`elabelÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1xsubsets of uplims and lolimsÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`cpltÙ±‚aoa.Ù±‚`flegendÙ±‚`a(Ù±‚`clocÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1klower rightÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚bc1xN##############################################################################Ù±‚`a
Ù±‚bc1xN# Similarly ``xuplims`` and ``xlolims`` can be used on the horizontal ``xerr``Ù±‚`a
Ù±‚bc1l# errorbars.Ù±‚`a
Ù±‚`a
Ù±‚`cfigÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cpltÙ±‚aoa.Ù±‚`ffigureÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`axÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`farangeÙ±‚`a(Ù±‚bmib10Ù±‚`a)Ù±‚`a Ù±‚aoa/Ù±‚`a Ù±‚bmib10Ù±‚`a
Ù±‚`ayÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`a(Ù±‚`axÙ±‚`a Ù±‚aoa+Ù±‚`a Ù±‚bmfc0.1Ù±‚`a)Ù±‚aoa*Ù±‚aoa*Ù±‚bmia2Ù±‚`a
Ù±‚`a
Ù±‚`cpltÙ±‚aoa.Ù±‚`herrorbarÙ±‚`a(Ù±‚`axÙ±‚`a,Ù±‚`a Ù±‚`ayÙ±‚`a,Ù±‚`a Ù±‚`dxerrÙ±‚aoa=Ù±‚bmfc0.1Ù±‚`a,Ù±‚`a Ù±‚`gxlolimsÙ±‚aoa=Ù±‚bkcdTrueÙ±‚`a,Ù±‚`a Ù±‚`elabelÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1lxlolims=TrueÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`ayÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`a(Ù±‚`axÙ±‚`a Ù±‚aoa+Ù±‚`a Ù±‚bmfc0.1Ù±‚`a)Ù±‚aoa*Ù±‚aoa*Ù±‚bmia3Ù±‚`a
Ù±‚`a
Ù±‚`cpltÙ±‚aoa.Ù±‚`herrorbarÙ±‚`a(Ù±‚`axÙ±‚`a Ù±‚aoa+Ù±‚`a Ù±‚bmfc0.6Ù±‚`a,Ù±‚`a Ù±‚`ayÙ±‚`a,Ù±‚`a Ù±‚`dxerrÙ±‚aoa=Ù±‚bmfc0.1Ù±‚`a,Ù±‚`a Ù±‚`gxuplimsÙ±‚aoa=Ù±‚`kupperlimitsÙ±‚`a,Ù±‚`a Ù±‚`gxlolimsÙ±‚aoa=Ù±‚`klowerlimitsÙ±‚`a,Ù±‚`a
Ù±‚`m             Ù±‚`elabelÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1xsubsets of xuplims and xlolimsÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`ayÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`a(Ù±‚`axÙ±‚`a Ù±‚aoa+Ù±‚`a Ù±‚bmfc0.1Ù±‚`a)Ù±‚aoa*Ù±‚aoa*Ù±‚bmia4Ù±‚`a
Ù±‚`cpltÙ±‚aoa.Ù±‚`herrorbarÙ±‚`a(Ù±‚`axÙ±‚`a Ù±‚aoa+Ù±‚`a Ù±‚bmfc1.2Ù±‚`a,Ù±‚`a Ù±‚`ayÙ±‚`a,Ù±‚`a Ù±‚`dxerrÙ±‚aoa=Ù±‚bmfc0.1Ù±‚`a,Ù±‚`a Ù±‚`gxuplimsÙ±‚aoa=Ù±‚bkcdTrueÙ±‚`a,Ù±‚`a Ù±‚`elabelÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1lxuplims=TrueÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`cpltÙ±‚aoa.Ù±‚`flegendÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`cpltÙ±‚aoa.Ù±‚`dshowÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚bc1xN##############################################################################Ù±‚`a
Ù±‚bc1a#Ù±‚`a
Ù±‚bc1x# .. admonition:: ReferencesÙ±‚`a
Ù±‚bc1a#Ù±‚`a
Ù±‚bc1xN#    The use of the following functions, methods, classes and modules is shownÙ±‚`a
Ù±‚bc1u#    in this example:Ù±‚`a
Ù±‚bc1a#Ù±‚`a
Ù±‚bc1xE#    - `matplotlib.axes.Axes.errorbar` / `matplotlib.pyplot.errorbar`Ù±‚`a
`dNoneö