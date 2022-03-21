Ù¯‚Ù´ƒ™˜Ù±‚bsdy$"""
=============
Check Buttons
=============

Turning visual elements on and off with check buttons.

This program shows the use of 'Check Buttons' which is similar to
check boxes. There are 3 different sine waves shown and we can choose which
waves are displayed with the check buttons.
"""Ù±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„enumpyÙ „enumpyf1.22.3fmoduleenumpyfmoduleõÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnnbnpÙ±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnnfpyplotÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnncpltÙ±‚`a
Ù±‚bkndfromÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnngwidgetsÙ±‚`a Ù±‚bknfimportÙ±‚`a Ù±‚`lCheckButtonsÙ±‚`a
Ù±‚`a
Ù±‚`atÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`farangeÙ±‚`a(Ù±‚bmfc0.0Ù±‚`a,Ù±‚`a Ù±‚bmfc2.0Ù±‚`a,Ù±‚`a Ù±‚bmfd0.01Ù±‚`a)Ù±‚`a
Ù±‚`bs0Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`csinÙ±‚`a(Ù±‚bmia2Ù±‚aoa*Ù±‚`bnpÙ±‚aoa.Ù±‚`bpiÙ±‚aoa*Ù±‚`atÙ±‚`a)Ù±‚`a
Ù±‚`bs1Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`csinÙ±‚`a(Ù±‚bmia4Ù±‚aoa*Ù±‚`bnpÙ±‚aoa.Ù±‚`bpiÙ±‚aoa*Ù±‚`atÙ±‚`a)Ù±‚`a
Ù±‚`bs2Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`csinÙ±‚`a(Ù±‚bmia6Ù±‚aoa*Ù±‚`bnpÙ±‚aoa.Ù±‚`bpiÙ±‚aoa*Ù±‚`atÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`cfigÙ±‚`a,Ù±‚`a Ù±‚`baxÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cpltÙ±‚aoa.Ù±‚`hsubplotsÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`bl0Ù±‚`a,Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`baxÙ±‚aoa.Ù±‚`dplotÙ±‚`a(Ù±‚`atÙ±‚`a,Ù±‚`a Ù±‚`bs0Ù±‚`a,Ù±‚`a Ù±‚`gvisibleÙ±‚aoa=Ù±‚bkceFalseÙ±‚`a,Ù±‚`a Ù±‚`blwÙ±‚aoa=Ù±‚bmia2Ù±‚`a,Ù±‚`a Ù±‚`ecolorÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1akÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`elabelÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1d2 HzÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`bl1Ù±‚`a,Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`baxÙ±‚aoa.Ù±‚`dplotÙ±‚`a(Ù±‚`atÙ±‚`a,Ù±‚`a Ù±‚`bs1Ù±‚`a,Ù±‚`a Ù±‚`blwÙ±‚aoa=Ù±‚bmia2Ù±‚`a,Ù±‚`a Ù±‚`ecolorÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1arÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`elabelÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1d4 HzÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`bl2Ù±‚`a,Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`baxÙ±‚aoa.Ù±‚`dplotÙ±‚`a(Ù±‚`atÙ±‚`a,Ù±‚`a Ù±‚`bs2Ù±‚`a,Ù±‚`a Ù±‚`blwÙ±‚aoa=Ù±‚bmia2Ù±‚`a,Ù±‚`a Ù±‚`ecolorÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1agÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`elabelÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1d6 HzÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`cpltÙ±‚aoa.Ù±‚`osubplots_adjustÙ±‚`a(Ù±‚`dleftÙ±‚aoa=Ù±‚bmfc0.2Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`elinesÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`a[Ù±‚`bl0Ù±‚`a,Ù±‚`a Ù±‚`bl1Ù±‚`a,Ù±‚`a Ù±‚`bl2Ù±‚`a]Ù±‚`a
Ù±‚`a
Ù±‚bc1xB# Make checkbuttons with all plotted lines with correct visibilityÙ±‚`a
Ù±‚`craxÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cpltÙ±‚aoa.Ù±‚`daxesÙ±‚`a(Ù±‚`a[Ù±‚bmfd0.05Ù±‚`a,Ù±‚`a Ù±‚bmfc0.4Ù±‚`a,Ù±‚`a Ù±‚bmfc0.1Ù±‚`a,Ù±‚`a Ù±‚bmfd0.15Ù±‚`a]Ù±‚`a)Ù±‚`a
Ù±‚`flabelsÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`a[Ù±‚bnbcstrÙ±‚`a(Ù±‚`dlineÙ±‚aoa.Ù±‚`iget_labelÙ±‚`a(Ù±‚`a)Ù±‚`a)Ù±‚`a Ù±‚akcforÙ±‚`a Ù±‚`dlineÙ±‚`a Ù±‚bowbinÙ±‚`a Ù±‚`elinesÙ±‚`a]Ù±‚`a
Ù±‚`jvisibilityÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`a[Ù±‚`dlineÙ±‚aoa.Ù±‚`kget_visibleÙ±‚`a(Ù±‚`a)Ù±‚`a Ù±‚akcforÙ±‚`a Ù±‚`dlineÙ±‚`a Ù±‚bowbinÙ±‚`a Ù±‚`elinesÙ±‚`a]Ù±‚`a
Ù±‚`echeckÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`lCheckButtonsÙ±‚`a(Ù±‚`craxÙ±‚`a,Ù±‚`a Ù±‚`flabelsÙ±‚`a,Ù±‚`a Ù±‚`jvisibilityÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚akcdefÙ±‚`a Ù±‚bnfdfuncÙ±‚`a(Ù±‚`elabelÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`d    Ù±‚`eindexÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`flabelsÙ±‚aoa.Ù±‚`eindexÙ±‚`a(Ù±‚`elabelÙ±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`elinesÙ±‚`a[Ù±‚`eindexÙ±‚`a]Ù±‚aoa.Ù±‚`kset_visibleÙ±‚`a(Ù±‚bowcnotÙ±‚`a Ù±‚`elinesÙ±‚`a[Ù±‚`eindexÙ±‚`a]Ù±‚aoa.Ù±‚`kget_visibleÙ±‚`a(Ù±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`cpltÙ±‚aoa.Ù±‚`ddrawÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`echeckÙ±‚aoa.Ù±‚`jon_clickedÙ±‚`a(Ù±‚`dfuncÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`cpltÙ±‚aoa.Ù±‚`dshowÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚bc1xM#############################################################################Ù±‚`a
Ù±‚bc1a#Ù±‚`a
Ù±‚bc1x# .. admonition:: ReferencesÙ±‚`a
Ù±‚bc1a#Ù±‚`a
Ù±‚bc1xN#    The use of the following functions, methods, classes and modules is shownÙ±‚`a
Ù±‚bc1u#    in this example:Ù±‚`a
Ù±‚bc1a#Ù±‚`a
Ù±‚bc1x(#    - `matplotlib.widgets.CheckButtons`Ù±‚`a
`dNoneö