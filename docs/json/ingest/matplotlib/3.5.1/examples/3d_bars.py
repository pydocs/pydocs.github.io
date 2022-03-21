Ù¯‚Ù´ƒ˜şÙ±‚bsdxˆ"""
=====================
Demo of 3D bar charts
=====================

A basic demo of how to plot 3D bars with and without shading.
"""Ù±‚`a
Ù±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„enumpyÙ „enumpyf1.22.3fmoduleenumpyfmoduleõÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnnbnpÙ±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnnfpyplotÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnncpltÙ±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚bc1x# setup the figure and axesÙ±‚`a
Ù±‚`cfigÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cpltÙ±‚aoa.Ù±‚`ffigureÙ±‚`a(Ù±‚`gfigsizeÙ±‚aoa=Ù±‚`a(Ù±‚bmia8Ù±‚`a,Ù±‚`a Ù±‚bmia3Ù±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`cax1Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cfigÙ±‚aoa.Ù±‚`kadd_subplotÙ±‚`a(Ù±‚bmic121Ù±‚`a,Ù±‚`a Ù±‚`jprojectionÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1b3dÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`cax2Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cfigÙ±‚aoa.Ù±‚`kadd_subplotÙ±‚`a(Ù±‚bmic122Ù±‚`a,Ù±‚`a Ù±‚`jprojectionÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1b3dÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚bc1k# fake dataÙ±‚`a
Ù±‚`b_xÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`farangeÙ±‚`a(Ù±‚bmia4Ù±‚`a)Ù±‚`a
Ù±‚`b_yÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`farangeÙ±‚`a(Ù±‚bmia5Ù±‚`a)Ù±‚`a
Ù±‚`c_xxÙ±‚`a,Ù±‚`a Ù±‚`c_yyÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`hmeshgridÙ±‚`a(Ù±‚`b_xÙ±‚`a,Ù±‚`a Ù±‚`b_yÙ±‚`a)Ù±‚`a
Ù±‚`axÙ±‚`a,Ù±‚`a Ù±‚`ayÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`c_xxÙ±‚aoa.Ù±‚`eravelÙ±‚`a(Ù±‚`a)Ù±‚`a,Ù±‚`a Ù±‚`c_yyÙ±‚aoa.Ù±‚`eravelÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`ctopÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`axÙ±‚`a Ù±‚aoa+Ù±‚`a Ù±‚`ayÙ±‚`a
Ù±‚`fbottomÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`jzeros_likeÙ±‚`a(Ù±‚`ctopÙ±‚`a)Ù±‚`a
Ù±‚`ewidthÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`edepthÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bmia1Ù±‚`a
Ù±‚`a
Ù±‚`cax1Ù±‚aoa.Ù±‚`ebar3dÙ±‚`a(Ù±‚`axÙ±‚`a,Ù±‚`a Ù±‚`ayÙ±‚`a,Ù±‚`a Ù±‚`fbottomÙ±‚`a,Ù±‚`a Ù±‚`ewidthÙ±‚`a,Ù±‚`a Ù±‚`edepthÙ±‚`a,Ù±‚`a Ù±‚`ctopÙ±‚`a,Ù±‚`a Ù±‚`eshadeÙ±‚aoa=Ù±‚bkcdTrueÙ±‚`a)Ù±‚`a
Ù±‚`cax1Ù±‚aoa.Ù±‚`iset_titleÙ±‚`a(Ù±‚bs1a'Ù±‚bs1fShadedÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`cax2Ù±‚aoa.Ù±‚`ebar3dÙ±‚`a(Ù±‚`axÙ±‚`a,Ù±‚`a Ù±‚`ayÙ±‚`a,Ù±‚`a Ù±‚`fbottomÙ±‚`a,Ù±‚`a Ù±‚`ewidthÙ±‚`a,Ù±‚`a Ù±‚`edepthÙ±‚`a,Ù±‚`a Ù±‚`ctopÙ±‚`a,Ù±‚`a Ù±‚`eshadeÙ±‚aoa=Ù±‚bkceFalseÙ±‚`a)Ù±‚`a
Ù±‚`cax2Ù±‚aoa.Ù±‚`iset_titleÙ±‚`a(Ù±‚bs1a'Ù±‚bs1jNot ShadedÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`cpltÙ±‚aoa.Ù±‚`dshowÙ±‚`a(Ù±‚`a)Ù±‚`a
`dNoneö