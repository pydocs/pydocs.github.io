Ù¯‚Ù´ƒ™}Ù±‚bsdy"""
=================================
Pausing and Resuming an Animation
=================================

This example showcases:

- using the Animation.pause() method to pause an animation.
- using the Animation.resume() method to resume an animation.
"""Ù±‚`a
Ù±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnnfpyplotÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnncpltÙ±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnnianimationÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnnianimationÙ±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„enumpyÙ „enumpyf1.22.3fmoduleenumpyfmoduleõÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnnbnpÙ±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚akeclassÙ±‚`a Ù±‚bncnPauseAnimationÙ±‚`a:Ù±‚`a
Ù±‚`d    Ù±‚akcdefÙ±‚`a Ù±‚bfmh__init__Ù±‚`a(Ù±‚bbpdselfÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`h        Ù±‚`cfigÙ±‚`a,Ù±‚`a Ù±‚`baxÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cpltÙ±‚aoa.Ù±‚`hsubplotsÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚`baxÙ±‚aoa.Ù±‚`iset_titleÙ±‚`a(Ù±‚bs1a'Ù±‚bs1x#Click to pause/resume the animationÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚`axÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`hlinspaceÙ±‚`a(Ù±‚aoa-Ù±‚bmfc0.1Ù±‚`a,Ù±‚`a Ù±‚bmfc0.1Ù±‚`a,Ù±‚`a Ù±‚bmid1000Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`h        Ù±‚bc1x"# Start with a normal distributionÙ±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`bn0Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`a(Ù±‚bmfc1.0Ù±‚`a Ù±‚aoa/Ù±‚`a Ù±‚`a(Ù±‚`a(Ù±‚bmia4Ù±‚`a Ù±‚aoa*Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`bpiÙ±‚`a Ù±‚aoa*Ù±‚`a Ù±‚bmfd2e-4Ù±‚`a Ù±‚aoa*Ù±‚`a Ù±‚bmfc0.1Ù±‚`a)Ù±‚`a Ù±‚aoa*Ù±‚aoa*Ù±‚`a Ù±‚bmfc0.5Ù±‚`a)Ù±‚`a
Ù±‚`s                   Ù±‚aoa*Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`cexpÙ±‚`a(Ù±‚aoa-Ù±‚`axÙ±‚`a Ù±‚aoa*Ù±‚aoa*Ù±‚`a Ù±‚bmia2Ù±‚`a Ù±‚aoa/Ù±‚`a Ù±‚`a(Ù±‚bmia4Ù±‚`a Ù±‚aoa*Ù±‚`a Ù±‚bmfd2e-4Ù±‚`a Ù±‚aoa*Ù±‚`a Ù±‚bmfc0.1Ù±‚`a)Ù±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`apÙ±‚`a,Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`baxÙ±‚aoa.Ù±‚`dplotÙ±‚`a(Ù±‚`axÙ±‚`a,Ù±‚`a Ù±‚bbpdselfÙ±‚aoa.Ù±‚`bn0Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`ianimationÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`ianimationÙ±‚aoa.Ù±‚`mFuncAnimationÙ±‚`a(Ù±‚`a
Ù±‚`l            Ù±‚`cfigÙ±‚`a,Ù±‚`a Ù±‚bbpdselfÙ±‚aoa.Ù±‚`fupdateÙ±‚`a,Ù±‚`a Ù±‚`fframesÙ±‚aoa=Ù±‚bmic200Ù±‚`a,Ù±‚`a Ù±‚`hintervalÙ±‚aoa=Ù±‚bmib50Ù±‚`a,Ù±‚`a Ù±‚`dblitÙ±‚aoa=Ù±‚bkcdTrueÙ±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`fpausedÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bkceFalseÙ±‚`a
Ù±‚`a
Ù±‚`h        Ù±‚`cfigÙ±‚aoa.Ù±‚`fcanvasÙ±‚aoa.Ù±‚`kmpl_connectÙ±‚`a(Ù±‚bs1a'Ù±‚bs1rbutton_press_eventÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚bbpdselfÙ±‚aoa.Ù±‚`ltoggle_pauseÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚akcdefÙ±‚`a Ù±‚bnfltoggle_pauseÙ±‚`a(Ù±‚bbpdselfÙ±‚`a,Ù±‚`a Ù±‚aoa*Ù±‚`dargsÙ±‚`a,Ù±‚`a Ù±‚aoa*Ù±‚aoa*Ù±‚`fkwargsÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`h        Ù±‚akbifÙ±‚`a Ù±‚bbpdselfÙ±‚aoa.Ù±‚`fpausedÙ±‚`a:Ù±‚`a
Ù±‚`l            Ù±‚bbpdselfÙ±‚aoa.Ù±‚`ianimationÙ±‚aoa.Ù±‚`fresumeÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚akdelseÙ±‚`a:Ù±‚`a
Ù±‚`l            Ù±‚bbpdselfÙ±‚aoa.Ù±‚`ianimationÙ±‚aoa.Ù±‚`epauseÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`fpausedÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bowcnotÙ±‚`a Ù±‚bbpdselfÙ±‚aoa.Ù±‚`fpausedÙ±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚akcdefÙ±‚`a Ù±‚bnffupdateÙ±‚`a(Ù±‚bbpdselfÙ±‚`a,Ù±‚`a Ù±‚`aiÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`bn0Ù±‚`a Ù±‚aoa+Ù±‚aoa=Ù±‚`a Ù±‚`aiÙ±‚`a Ù±‚aoa/Ù±‚`a Ù±‚bmic100Ù±‚`a Ù±‚aoa%Ù±‚`a Ù±‚bmia5Ù±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`apÙ±‚aoa.Ù±‚`iset_ydataÙ±‚`a(Ù±‚bbpdselfÙ±‚aoa.Ù±‚`bn0Ù±‚`a Ù±‚aoa%Ù±‚`a Ù±‚bmib20Ù±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚akfreturnÙ±‚`a Ù±‚`a(Ù±‚bbpdselfÙ±‚aoa.Ù±‚`apÙ±‚`a,Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚`bpaÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`nPauseAnimationÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`cpltÙ±‚aoa.Ù±‚`dshowÙ±‚`a(Ù±‚`a)Ù±‚`a
`dNoneö