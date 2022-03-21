Ù¯‚Ù´ƒ˜¹Ù±‚bsdyI"""
========================================
Bayesian Methods for Hackers style sheet
========================================

This example demonstrates the style used in the Bayesian Methods for Hackers
[1]_ online book.

.. [1] http://camdavidsonpilon.github.io/Probabilistic-Programming-and-Bayesian-Methods-for-Hackers/

"""Ù±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„enumpyÙ „enumpyf1.22.3fmoduleenumpyfmoduleõÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnnbnpÙ±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnnfpyplotÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnncpltÙ±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚bc1x)# Fixing random state for reproducibilityÙ±‚`a
Ù±‚`bnpÙ±‚aoa.Ù±‚`frandomÙ±‚aoa.Ù±‚`dseedÙ±‚`a(Ù±‚bmih19680801Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`cpltÙ±‚aoa.Ù±‚`estyleÙ±‚aoa.Ù±‚`cuseÙ±‚`a(Ù±‚bs1a'Ù±‚bs1cbmhÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚akcdefÙ±‚`a Ù±‚bnfnplot_beta_histÙ±‚`a(Ù±‚`baxÙ±‚`a,Ù±‚`a Ù±‚`aaÙ±‚`a,Ù±‚`a Ù±‚`abÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`d    Ù±‚`baxÙ±‚aoa.Ù±‚`dhistÙ±‚`a(Ù±‚`bnpÙ±‚aoa.Ù±‚`frandomÙ±‚aoa.Ù±‚`dbetaÙ±‚`a(Ù±‚`aaÙ±‚`a,Ù±‚`a Ù±‚`abÙ±‚`a,Ù±‚`a Ù±‚`dsizeÙ±‚aoa=Ù±‚bmie10000Ù±‚`a)Ù±‚`a,Ù±‚`a
Ù±‚`l            Ù±‚`hhisttypeÙ±‚aoa=Ù±‚bs2a"Ù±‚bs2jstepfilledÙ±‚bs2a"Ù±‚`a,Ù±‚`a Ù±‚`dbinsÙ±‚aoa=Ù±‚bmib25Ù±‚`a,Ù±‚`a Ù±‚`ealphaÙ±‚aoa=Ù±‚bmfc0.8Ù±‚`a,Ù±‚`a Ù±‚`gdensityÙ±‚aoa=Ù±‚bkcdTrueÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚`cfigÙ±‚`a,Ù±‚`a Ù±‚`baxÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cpltÙ±‚aoa.Ù±‚`hsubplotsÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`nplot_beta_histÙ±‚`a(Ù±‚`baxÙ±‚`a,Ù±‚`a Ù±‚bmib10Ù±‚`a,Ù±‚`a Ù±‚bmib10Ù±‚`a)Ù±‚`a
Ù±‚`nplot_beta_histÙ±‚`a(Ù±‚`baxÙ±‚`a,Ù±‚`a Ù±‚bmia4Ù±‚`a,Ù±‚`a Ù±‚bmib12Ù±‚`a)Ù±‚`a
Ù±‚`nplot_beta_histÙ±‚`a(Ù±‚`baxÙ±‚`a,Ù±‚`a Ù±‚bmib50Ù±‚`a,Ù±‚`a Ù±‚bmib12Ù±‚`a)Ù±‚`a
Ù±‚`nplot_beta_histÙ±‚`a(Ù±‚`baxÙ±‚`a,Ù±‚`a Ù±‚bmia6Ù±‚`a,Ù±‚`a Ù±‚bmib55Ù±‚`a)Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`iset_titleÙ±‚`a(Ù±‚bs2a"Ù±‚bs2a'Ù±‚bs2cbmhÙ±‚bs2a'Ù±‚bs2l style sheetÙ±‚bs2a"Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`cpltÙ±‚aoa.Ù±‚`dshowÙ±‚`a(Ù±‚`a)Ù±‚`a
`dNoneö