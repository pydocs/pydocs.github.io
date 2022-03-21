Ù¯‚Ù´ƒ™ÇÙ±‚bsdxÛ"""
======
Pipong
======

A Matplotlib based game of Pong illustrating one way to write interactive
animation which are easily ported to multiple backends
pipong.py was written by Paul Ivanov <http://pirsquared.org>
"""Ù±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„enumpyÙ „enumpyf1.22.3fmoduleenumpyfmoduleõÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnnbnpÙ±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnnfpyplotÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnncpltÙ±‚`a
Ù±‚bkndfromÙ±‚`a Ù±‚bnnÙ¢„enumpyÙ „enumpyf1.22.3fmoduleenumpyfmoduleõÙ±‚bnna.Ù±‚bnnfrandomÙ±‚`a Ù±‚bknfimportÙ±‚`a Ù±‚`erandnÙ±‚`a,Ù±‚`a Ù±‚`grandintÙ±‚`a
Ù±‚bkndfromÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnnlfont_managerÙ±‚`a Ù±‚bknfimportÙ±‚`a Ù±‚`nFontPropertiesÙ±‚`a
Ù±‚`a
Ù±‚`linstructionsÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bs2c"""Ù±‚bs2a
Ù±‚bs2xPlayer A:       Player B:Ù±‚bs2a
Ù±‚bs2b  Ù±‚bs2a'Ù±‚bs2aeÙ±‚bs2a'Ù±‚bs2m      up     Ù±‚bs2a'Ù±‚bs2aiÙ±‚bs2a'Ù±‚bs2a
Ù±‚bs2b  Ù±‚bs2a'Ù±‚bs2adÙ±‚bs2a'Ù±‚bs2m     down    Ù±‚bs2a'Ù±‚bs2akÙ±‚bs2a'Ù±‚bs2a
Ù±‚bs2a
Ù±‚bs2fpress Ù±‚bs2a'Ù±‚bs2atÙ±‚bs2a'Ù±‚bs2x -- close these instructionsÙ±‚bs2a
Ù±‚bs2x+            (animation will be much faster)Ù±‚bs2a
Ù±‚bs2fpress Ù±‚bs2a'Ù±‚bs2aaÙ±‚bs2a'Ù±‚bs2n -- add a puckÙ±‚bs2a
Ù±‚bs2fpress Ù±‚bs2a'Ù±‚bs2aAÙ±‚bs2a'Ù±‚bs2q -- remove a puckÙ±‚bs2a
Ù±‚bs2fpress Ù±‚bs2a'Ù±‚bs2a1Ù±‚bs2a'Ù±‚bs2w -- slow down all pucksÙ±‚bs2a
Ù±‚bs2fpress Ù±‚bs2a'Ù±‚bs2a2Ù±‚bs2a'Ù±‚bs2v -- speed up all pucksÙ±‚bs2a
Ù±‚bs2fpress Ù±‚bs2a'Ù±‚bs2a3Ù±‚bs2a'Ù±‚bs2x -- slow down distractorsÙ±‚bs2a
Ù±‚bs2fpress Ù±‚bs2a'Ù±‚bs2a4Ù±‚bs2a'Ù±‚bs2x -- speed up distractorsÙ±‚bs2a
Ù±‚bs2fpress Ù±‚bs2a'Ù±‚bs2a Ù±‚bs2a'Ù±‚bs2x -- reset the first puckÙ±‚bs2a
Ù±‚bs2fpress Ù±‚bs2a'Ù±‚bs2anÙ±‚bs2a'Ù±‚bs2x -- toggle distractors on/offÙ±‚bs2a
Ù±‚bs2fpress Ù±‚bs2a'Ù±‚bs2agÙ±‚bs2a'Ù±‚bs2x -- toggle the game on/offÙ±‚bs2a
Ù±‚bs2a
Ù±‚bs2b  Ù±‚bs2c"""Ù±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚akeclassÙ±‚`a Ù±‚bnccPadÙ±‚`a:Ù±‚`a
Ù±‚`d    Ù±‚akcdefÙ±‚`a Ù±‚bfmh__init__Ù±‚`a(Ù±‚bbpdselfÙ±‚`a,Ù±‚`a Ù±‚`ddispÙ±‚`a,Ù±‚`a Ù±‚`axÙ±‚`a,Ù±‚`a Ù±‚`ayÙ±‚`a,Ù±‚`a Ù±‚bnbdtypeÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1alÙ±‚bs1a'Ù±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`ddispÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`ddispÙ±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`axÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`axÙ±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`ayÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`ayÙ±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`awÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bmfb.3Ù±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`escoreÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bmia0Ù±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`gxoffsetÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bmfc0.3Ù±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`gyoffsetÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bmfc0.1Ù±‚`a
Ù±‚`h        Ù±‚akbifÙ±‚`a Ù±‚bnbdtypeÙ±‚`a Ù±‚aob==Ù±‚`a Ù±‚bs1a'Ù±‚bs1arÙ±‚bs1a'Ù±‚`a:Ù±‚`a
Ù±‚`l            Ù±‚bbpdselfÙ±‚aoa.Ù±‚`gxoffsetÙ±‚`a Ù±‚aoa*Ù±‚aoa=Ù±‚`a Ù±‚aoa-Ù±‚bmfc1.0Ù±‚`a
Ù±‚`a
Ù±‚`h        Ù±‚akbifÙ±‚`a Ù±‚bnbdtypeÙ±‚`a Ù±‚aob==Ù±‚`a Ù±‚bs1a'Ù±‚bs1alÙ±‚bs1a'Ù±‚`a Ù±‚bowborÙ±‚`a Ù±‚bnbdtypeÙ±‚`a Ù±‚aob==Ù±‚`a Ù±‚bs1a'Ù±‚bs1arÙ±‚bs1a'Ù±‚`a:Ù±‚`a
Ù±‚`l            Ù±‚bbpdselfÙ±‚aoa.Ù±‚`esignxÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚aoa-Ù±‚bmfc1.0Ù±‚`a
Ù±‚`l            Ù±‚bbpdselfÙ±‚aoa.Ù±‚`esignyÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bmfc1.0Ù±‚`a
Ù±‚`h        Ù±‚akdelseÙ±‚`a:Ù±‚`a
Ù±‚`l            Ù±‚bbpdselfÙ±‚aoa.Ù±‚`esignxÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bmfc1.0Ù±‚`a
Ù±‚`l            Ù±‚bbpdselfÙ±‚aoa.Ù±‚`esignyÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚aoa-Ù±‚bmfc1.0Ù±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚akcdefÙ±‚`a Ù±‚bnfhcontainsÙ±‚`a(Ù±‚bbpdselfÙ±‚`a,Ù±‚`a Ù±‚`clocÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`h        Ù±‚akfreturnÙ±‚`a Ù±‚bbpdselfÙ±‚aoa.Ù±‚`ddispÙ±‚aoa.Ù±‚`hget_bboxÙ±‚`a(Ù±‚`a)Ù±‚aoa.Ù±‚`hcontainsÙ±‚`a(Ù±‚`clocÙ±‚aoa.Ù±‚`axÙ±‚`a,Ù±‚`a Ù±‚`clocÙ±‚aoa.Ù±‚`ayÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚akeclassÙ±‚`a Ù±‚bncdPuckÙ±‚`a:Ù±‚`a
Ù±‚`d    Ù±‚akcdefÙ±‚`a Ù±‚bfmh__init__Ù±‚`a(Ù±‚bbpdselfÙ±‚`a,Ù±‚`a Ù±‚`ddispÙ±‚`a,Ù±‚`a Ù±‚`cpadÙ±‚`a,Ù±‚`a Ù±‚`efieldÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`dvmaxÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bmfb.2Ù±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`ddispÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`ddispÙ±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`efieldÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`efieldÙ±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`f_resetÙ±‚`a(Ù±‚`cpadÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚akcdefÙ±‚`a Ù±‚bnff_resetÙ±‚`a(Ù±‚bbpdselfÙ±‚`a,Ù±‚`a Ù±‚`cpadÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`axÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cpadÙ±‚aoa.Ù±‚`axÙ±‚`a Ù±‚aoa+Ù±‚`a Ù±‚`cpadÙ±‚aoa.Ù±‚`gxoffsetÙ±‚`a
Ù±‚`h        Ù±‚akbifÙ±‚`a Ù±‚`cpadÙ±‚aoa.Ù±‚`ayÙ±‚`a Ù±‚aoa<Ù±‚`a Ù±‚bmia0Ù±‚`a:Ù±‚`a
Ù±‚`l            Ù±‚bbpdselfÙ±‚aoa.Ù±‚`ayÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cpadÙ±‚aoa.Ù±‚`ayÙ±‚`a Ù±‚aoa+Ù±‚`a Ù±‚`cpadÙ±‚aoa.Ù±‚`gyoffsetÙ±‚`a
Ù±‚`h        Ù±‚akdelseÙ±‚`a:Ù±‚`a
Ù±‚`l            Ù±‚bbpdselfÙ±‚aoa.Ù±‚`ayÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cpadÙ±‚aoa.Ù±‚`ayÙ±‚`a Ù±‚aoa-Ù±‚`a Ù±‚`cpadÙ±‚aoa.Ù±‚`gyoffsetÙ±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`bvxÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cpadÙ±‚aoa.Ù±‚`axÙ±‚`a Ù±‚aoa-Ù±‚`a Ù±‚bbpdselfÙ±‚aoa.Ù±‚`axÙ±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`bvyÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cpadÙ±‚aoa.Ù±‚`ayÙ±‚`a Ù±‚aoa+Ù±‚`a Ù±‚`cpadÙ±‚aoa.Ù±‚`awÙ±‚aoa/Ù±‚bmia2Ù±‚`a Ù±‚aoa-Ù±‚`a Ù±‚bbpdselfÙ±‚aoa.Ù±‚`ayÙ±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`k_speedlimitÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`g_slowerÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`g_slowerÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚akcdefÙ±‚`a Ù±‚bnffupdateÙ±‚`a(Ù±‚bbpdselfÙ±‚`a,Ù±‚`a Ù±‚`dpadsÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`axÙ±‚`a Ù±‚aoa+Ù±‚aoa=Ù±‚`a Ù±‚bbpdselfÙ±‚aoa.Ù±‚`bvxÙ±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`ayÙ±‚`a Ù±‚aoa+Ù±‚aoa=Ù±‚`a Ù±‚bbpdselfÙ±‚aoa.Ù±‚`bvyÙ±‚`a
Ù±‚`h        Ù±‚akcforÙ±‚`a Ù±‚`cpadÙ±‚`a Ù±‚bowbinÙ±‚`a Ù±‚`dpadsÙ±‚`a:Ù±‚`a
Ù±‚`l            Ù±‚akbifÙ±‚`a Ù±‚`cpadÙ±‚aoa.Ù±‚`hcontainsÙ±‚`a(Ù±‚bbpdselfÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`p                Ù±‚bbpdselfÙ±‚aoa.Ù±‚`bvxÙ±‚`a Ù±‚aoa*Ù±‚aoa=Ù±‚`a Ù±‚bmfc1.2Ù±‚`a Ù±‚aoa*Ù±‚`a Ù±‚`cpadÙ±‚aoa.Ù±‚`esignxÙ±‚`a
Ù±‚`p                Ù±‚bbpdselfÙ±‚aoa.Ù±‚`bvyÙ±‚`a Ù±‚aoa*Ù±‚aoa=Ù±‚`a Ù±‚bmfc1.2Ù±‚`a Ù±‚aoa*Ù±‚`a Ù±‚`cpadÙ±‚aoa.Ù±‚`esignyÙ±‚`a
Ù±‚`h        Ù±‚`efudgeÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bmfd.001Ù±‚`a
Ù±‚`h        Ù±‚bc1x)# probably cleaner with something like...Ù±‚`a
Ù±‚`h        Ù±‚akbifÙ±‚`a Ù±‚bbpdselfÙ±‚aoa.Ù±‚`axÙ±‚`a Ù±‚aoa<Ù±‚`a Ù±‚`efudgeÙ±‚`a:Ù±‚`a
Ù±‚`l            Ù±‚`dpadsÙ±‚`a[Ù±‚bmia1Ù±‚`a]Ù±‚aoa.Ù±‚`escoreÙ±‚`a Ù±‚aoa+Ù±‚aoa=Ù±‚`a Ù±‚bmia1Ù±‚`a
Ù±‚`l            Ù±‚bbpdselfÙ±‚aoa.Ù±‚`f_resetÙ±‚`a(Ù±‚`dpadsÙ±‚`a[Ù±‚bmia0Ù±‚`a]Ù±‚`a)Ù±‚`a
Ù±‚`l            Ù±‚akfreturnÙ±‚`a Ù±‚bkcdTrueÙ±‚`a
Ù±‚`h        Ù±‚akbifÙ±‚`a Ù±‚bbpdselfÙ±‚aoa.Ù±‚`axÙ±‚`a Ù±‚aoa>Ù±‚`a Ù±‚bmia7Ù±‚`a Ù±‚aoa-Ù±‚`a Ù±‚`efudgeÙ±‚`a:Ù±‚`a
Ù±‚`l            Ù±‚`dpadsÙ±‚`a[Ù±‚bmia0Ù±‚`a]Ù±‚aoa.Ù±‚`escoreÙ±‚`a Ù±‚aoa+Ù±‚aoa=Ù±‚`a Ù±‚bmia1Ù±‚`a
Ù±‚`l            Ù±‚bbpdselfÙ±‚aoa.Ù±‚`f_resetÙ±‚`a(Ù±‚`dpadsÙ±‚`a[Ù±‚bmia1Ù±‚`a]Ù±‚`a)Ù±‚`a
Ù±‚`l            Ù±‚akfreturnÙ±‚`a Ù±‚bkcdTrueÙ±‚`a
Ù±‚`h        Ù±‚akbifÙ±‚`a Ù±‚bbpdselfÙ±‚aoa.Ù±‚`ayÙ±‚`a Ù±‚aoa<Ù±‚`a Ù±‚aoa-Ù±‚bmia1Ù±‚`a Ù±‚aoa+Ù±‚`a Ù±‚`efudgeÙ±‚`a Ù±‚bowborÙ±‚`a Ù±‚bbpdselfÙ±‚aoa.Ù±‚`ayÙ±‚`a Ù±‚aoa>Ù±‚`a Ù±‚bmia1Ù±‚`a Ù±‚aoa-Ù±‚`a Ù±‚`efudgeÙ±‚`a:Ù±‚`a
Ù±‚`l            Ù±‚bbpdselfÙ±‚aoa.Ù±‚`bvyÙ±‚`a Ù±‚aoa*Ù±‚aoa=Ù±‚`a Ù±‚aoa-Ù±‚bmfc1.0Ù±‚`a
Ù±‚`l            Ù±‚bc1x2# add some randomness, just to make it interestingÙ±‚`a
Ù±‚`l            Ù±‚bbpdselfÙ±‚aoa.Ù±‚`bvyÙ±‚`a Ù±‚aoa-Ù±‚aoa=Ù±‚`a Ù±‚`a(Ù±‚`erandnÙ±‚`a(Ù±‚`a)Ù±‚aoa/Ù±‚bmfe300.0Ù±‚`a Ù±‚aoa+Ù±‚`a Ù±‚bmia1Ù±‚aoa/Ù±‚bmfe300.0Ù±‚`a)Ù±‚`a Ù±‚aoa*Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`dsignÙ±‚`a(Ù±‚bbpdselfÙ±‚aoa.Ù±‚`bvyÙ±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`k_speedlimitÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚akfreturnÙ±‚`a Ù±‚bkceFalseÙ±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚akcdefÙ±‚`a Ù±‚bnfg_slowerÙ±‚`a(Ù±‚bbpdselfÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`bvxÙ±‚`a Ù±‚aoa/Ù±‚aoa=Ù±‚`a Ù±‚bmfc5.0Ù±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`bvyÙ±‚`a Ù±‚aoa/Ù±‚aoa=Ù±‚`a Ù±‚bmfc5.0Ù±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚akcdefÙ±‚`a Ù±‚bnfg_fasterÙ±‚`a(Ù±‚bbpdselfÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`bvxÙ±‚`a Ù±‚aoa*Ù±‚aoa=Ù±‚`a Ù±‚bmfc5.0Ù±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`bvyÙ±‚`a Ù±‚aoa*Ù±‚aoa=Ù±‚`a Ù±‚bmfc5.0Ù±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚akcdefÙ±‚`a Ù±‚bnfk_speedlimitÙ±‚`a(Ù±‚bbpdselfÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`h        Ù±‚akbifÙ±‚`a Ù±‚bbpdselfÙ±‚aoa.Ù±‚`bvxÙ±‚`a Ù±‚aoa>Ù±‚`a Ù±‚bbpdselfÙ±‚aoa.Ù±‚`dvmaxÙ±‚`a:Ù±‚`a
Ù±‚`l            Ù±‚bbpdselfÙ±‚aoa.Ù±‚`bvxÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bbpdselfÙ±‚aoa.Ù±‚`dvmaxÙ±‚`a
Ù±‚`h        Ù±‚akbifÙ±‚`a Ù±‚bbpdselfÙ±‚aoa.Ù±‚`bvxÙ±‚`a Ù±‚aoa<Ù±‚`a Ù±‚aoa-Ù±‚bbpdselfÙ±‚aoa.Ù±‚`dvmaxÙ±‚`a:Ù±‚`a
Ù±‚`l            Ù±‚bbpdselfÙ±‚aoa.Ù±‚`bvxÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚aoa-Ù±‚bbpdselfÙ±‚aoa.Ù±‚`dvmaxÙ±‚`a
Ù±‚`a
Ù±‚`h        Ù±‚akbifÙ±‚`a Ù±‚bbpdselfÙ±‚aoa.Ù±‚`bvyÙ±‚`a Ù±‚aoa>Ù±‚`a Ù±‚bbpdselfÙ±‚aoa.Ù±‚`dvmaxÙ±‚`a:Ù±‚`a
Ù±‚`l            Ù±‚bbpdselfÙ±‚aoa.Ù±‚`bvyÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bbpdselfÙ±‚aoa.Ù±‚`dvmaxÙ±‚`a
Ù±‚`h        Ù±‚akbifÙ±‚`a Ù±‚bbpdselfÙ±‚aoa.Ù±‚`bvyÙ±‚`a Ù±‚aoa<Ù±‚`a Ù±‚aoa-Ù±‚bbpdselfÙ±‚aoa.Ù±‚`dvmaxÙ±‚`a:Ù±‚`a
Ù±‚`l            Ù±‚bbpdselfÙ±‚aoa.Ù±‚`bvyÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚aoa-Ù±‚bbpdselfÙ±‚aoa.Ù±‚`dvmaxÙ±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚akeclassÙ±‚`a Ù±‚bncdGameÙ±‚`a:Ù±‚`a
Ù±‚`d    Ù±‚akcdefÙ±‚`a Ù±‚bfmh__init__Ù±‚`a(Ù±‚bbpdselfÙ±‚`a,Ù±‚`a Ù±‚`baxÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`h        Ù±‚bc1x# create the initial lineÙ±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`baxÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`baxÙ±‚`a
Ù±‚`h        Ù±‚`baxÙ±‚aoa.Ù±‚`exaxisÙ±‚aoa.Ù±‚`kset_visibleÙ±‚`a(Ù±‚bkceFalseÙ±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚`baxÙ±‚aoa.Ù±‚`hset_xlimÙ±‚`a(Ù±‚`a[Ù±‚bmia0Ù±‚`a,Ù±‚`a Ù±‚bmia7Ù±‚`a]Ù±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚`baxÙ±‚aoa.Ù±‚`eyaxisÙ±‚aoa.Ù±‚`kset_visibleÙ±‚`a(Ù±‚bkceFalseÙ±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚`baxÙ±‚aoa.Ù±‚`hset_ylimÙ±‚`a(Ù±‚`a[Ù±‚aoa-Ù±‚bmia1Ù±‚`a,Ù±‚`a Ù±‚bmia1Ù±‚`a]Ù±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚`gpad_a_xÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bmia0Ù±‚`a
Ù±‚`h        Ù±‚`gpad_b_xÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bmfc.50Ù±‚`a
Ù±‚`h        Ù±‚`gpad_a_yÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`gpad_b_yÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bmfc.30Ù±‚`a
Ù±‚`h        Ù±‚`gpad_b_xÙ±‚`a Ù±‚aoa+Ù±‚aoa=Ù±‚`a Ù±‚bmfc6.3Ù±‚`a
Ù±‚`a
Ù±‚`h        Ù±‚bc1f# padsÙ±‚`a
Ù±‚`h        Ù±‚`bpAÙ±‚`a,Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bbpdselfÙ±‚aoa.Ù±‚`baxÙ±‚aoa.Ù±‚`dbarhÙ±‚`a(Ù±‚`gpad_a_yÙ±‚`a,Ù±‚`a Ù±‚bmfb.2Ù±‚`a,Ù±‚`a
Ù±‚`x                           Ù±‚`fheightÙ±‚aoa=Ù±‚bmfb.3Ù±‚`a,Ù±‚`a Ù±‚`ecolorÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1akÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`ealphaÙ±‚aoa=Ù±‚bmfb.5Ù±‚`a,Ù±‚`a Ù±‚`iedgecolorÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1abÙ±‚bs1a'Ù±‚`a,Ù±‚`a
Ù±‚`x                           Ù±‚`blwÙ±‚aoa=Ù±‚bmia2Ù±‚`a,Ù±‚`a Ù±‚`elabelÙ±‚aoa=Ù±‚bs2a"Ù±‚bs2hPlayer BÙ±‚bs2a"Ù±‚`a,Ù±‚`a
Ù±‚`x                           Ù±‚`hanimatedÙ±‚aoa=Ù±‚bkcdTrueÙ±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚`bpBÙ±‚`a,Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bbpdselfÙ±‚aoa.Ù±‚`baxÙ±‚aoa.Ù±‚`dbarhÙ±‚`a(Ù±‚`gpad_b_yÙ±‚`a,Ù±‚`a Ù±‚bmfb.2Ù±‚`a,Ù±‚`a
Ù±‚`x                           Ù±‚`fheightÙ±‚aoa=Ù±‚bmfb.3Ù±‚`a,Ù±‚`a Ù±‚`dleftÙ±‚aoa=Ù±‚`gpad_b_xÙ±‚`a,Ù±‚`a Ù±‚`ecolorÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1akÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`ealphaÙ±‚aoa=Ù±‚bmfb.5Ù±‚`a,Ù±‚`a
Ù±‚`x                           Ù±‚`iedgecolorÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1arÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`blwÙ±‚aoa=Ù±‚bmia2Ù±‚`a,Ù±‚`a Ù±‚`elabelÙ±‚aoa=Ù±‚bs2a"Ù±‚bs2hPlayer AÙ±‚bs2a"Ù±‚`a,Ù±‚`a
Ù±‚`x                           Ù±‚`hanimatedÙ±‚aoa=Ù±‚bkcdTrueÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`h        Ù±‚bc1m# distractorsÙ±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`axÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`farangeÙ±‚`a(Ù±‚bmia0Ù±‚`a,Ù±‚`a Ù±‚bmfd2.22Ù±‚aoa*Ù±‚`bnpÙ±‚aoa.Ù±‚`bpiÙ±‚`a,Ù±‚`a Ù±‚bmfd0.01Ù±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`dlineÙ±‚`a,Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bbpdselfÙ±‚aoa.Ù±‚`baxÙ±‚aoa.Ù±‚`dplotÙ±‚`a(Ù±‚bbpdselfÙ±‚aoa.Ù±‚`axÙ±‚`a,Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`csinÙ±‚`a(Ù±‚bbpdselfÙ±‚aoa.Ù±‚`axÙ±‚`a)Ù±‚`a,Ù±‚`a Ù±‚bs2a"Ù±‚bs2arÙ±‚bs2a"Ù±‚`a,Ù±‚`a
Ù±‚`x"                                  Ù±‚`hanimatedÙ±‚aoa=Ù±‚bkcdTrueÙ±‚`a,Ù±‚`a Ù±‚`blwÙ±‚aoa=Ù±‚bmia4Ù±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`eline2Ù±‚`a,Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bbpdselfÙ±‚aoa.Ù±‚`baxÙ±‚aoa.Ù±‚`dplotÙ±‚`a(Ù±‚bbpdselfÙ±‚aoa.Ù±‚`axÙ±‚`a,Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`ccosÙ±‚`a(Ù±‚bbpdselfÙ±‚aoa.Ù±‚`axÙ±‚`a)Ù±‚`a,Ù±‚`a Ù±‚bs2a"Ù±‚bs2agÙ±‚bs2a"Ù±‚`a,Ù±‚`a
Ù±‚`x#                                   Ù±‚`hanimatedÙ±‚aoa=Ù±‚bkcdTrueÙ±‚`a,Ù±‚`a Ù±‚`blwÙ±‚aoa=Ù±‚bmia4Ù±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`eline3Ù±‚`a,Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bbpdselfÙ±‚aoa.Ù±‚`baxÙ±‚aoa.Ù±‚`dplotÙ±‚`a(Ù±‚bbpdselfÙ±‚aoa.Ù±‚`axÙ±‚`a,Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`ccosÙ±‚`a(Ù±‚bbpdselfÙ±‚aoa.Ù±‚`axÙ±‚`a)Ù±‚`a,Ù±‚`a Ù±‚bs2a"Ù±‚bs2agÙ±‚bs2a"Ù±‚`a,Ù±‚`a
Ù±‚`x#                                   Ù±‚`hanimatedÙ±‚aoa=Ù±‚bkcdTrueÙ±‚`a,Ù±‚`a Ù±‚`blwÙ±‚aoa=Ù±‚bmia4Ù±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`eline4Ù±‚`a,Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bbpdselfÙ±‚aoa.Ù±‚`baxÙ±‚aoa.Ù±‚`dplotÙ±‚`a(Ù±‚bbpdselfÙ±‚aoa.Ù±‚`axÙ±‚`a,Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`ccosÙ±‚`a(Ù±‚bbpdselfÙ±‚aoa.Ù±‚`axÙ±‚`a)Ù±‚`a,Ù±‚`a Ù±‚bs2a"Ù±‚bs2arÙ±‚bs2a"Ù±‚`a,Ù±‚`a
Ù±‚`x#                                   Ù±‚`hanimatedÙ±‚aoa=Ù±‚bkcdTrueÙ±‚`a,Ù±‚`a Ù±‚`blwÙ±‚aoa=Ù±‚bmia4Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`h        Ù±‚bc1m# center lineÙ±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`jcenterlineÙ±‚`a,Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bbpdselfÙ±‚aoa.Ù±‚`baxÙ±‚aoa.Ù±‚`dplotÙ±‚`a(Ù±‚`a[Ù±‚bmfc3.5Ù±‚`a,Ù±‚`a Ù±‚bmfc3.5Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`a[Ù±‚bmia1Ù±‚`a,Ù±‚`a Ù±‚aoa-Ù±‚bmia1Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚bs1a'Ù±‚bs1akÙ±‚bs1a'Ù±‚`a,Ù±‚`a
Ù±‚`x(                                        Ù±‚`ealphaÙ±‚aoa=Ù±‚bmfb.5Ù±‚`a,Ù±‚`a Ù±‚`hanimatedÙ±‚aoa=Ù±‚bkcdTrueÙ±‚`a,Ù±‚`a Ù±‚`blwÙ±‚aoa=Ù±‚bmia8Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`h        Ù±‚bc1j# puck (s)Ù±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`hpuckdispÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bbpdselfÙ±‚aoa.Ù±‚`baxÙ±‚aoa.Ù±‚`gscatterÙ±‚`a(Ù±‚`a[Ù±‚bmia1Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`a[Ù±‚bmia1Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`elabelÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1j_nolegend_Ù±‚bs1a'Ù±‚`a,Ù±‚`a
Ù±‚`x(                                        Ù±‚`asÙ±‚aoa=Ù±‚bmic200Ù±‚`a,Ù±‚`a Ù±‚`acÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1agÙ±‚bs1a'Ù±‚`a,Ù±‚`a
Ù±‚`x(                                        Ù±‚`ealphaÙ±‚aoa=Ù±‚bmfb.9Ù±‚`a,Ù±‚`a Ù±‚`hanimatedÙ±‚aoa=Ù±‚bkcdTrueÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`fcanvasÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bbpdselfÙ±‚aoa.Ù±‚`baxÙ±‚aoa.Ù±‚`ffigureÙ±‚aoa.Ù±‚`fcanvasÙ±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`jbackgroundÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bkcdNoneÙ±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`ccntÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bmia0Ù±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`hdistractÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bkcdTrueÙ±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`cresÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bmfe100.0Ù±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`bonÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bkceFalseÙ±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`dinstÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bkcdTrueÙ±‚`d    Ù±‚bc1x&# show instructions from the beginningÙ±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`dpadsÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`a[Ù±‚`cPadÙ±‚`a(Ù±‚`bpAÙ±‚`a,Ù±‚`a Ù±‚`gpad_a_xÙ±‚`a,Ù±‚`a Ù±‚`gpad_a_yÙ±‚`a)Ù±‚`a,Ù±‚`a
Ù±‚`u                     Ù±‚`cPadÙ±‚`a(Ù±‚`bpBÙ±‚`a,Ù±‚`a Ù±‚`gpad_b_xÙ±‚`a,Ù±‚`a Ù±‚`gpad_b_yÙ±‚`a,Ù±‚`a Ù±‚bs1a'Ù±‚bs1arÙ±‚bs1a'Ù±‚`a)Ù±‚`a]Ù±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`epucksÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`a[Ù±‚`a]Ù±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`aiÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bbpdselfÙ±‚aoa.Ù±‚`baxÙ±‚aoa.Ù±‚`hannotateÙ±‚`a(Ù±‚`linstructionsÙ±‚`a,Ù±‚`a Ù±‚`a(Ù±‚bmfb.5Ù±‚`a,Ù±‚`a Ù±‚bmfc0.5Ù±‚`a)Ù±‚`a,Ù±‚`a
Ù±‚`x"                                  Ù±‚`dnameÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1imonospaceÙ±‚bs1a'Ù±‚`a,Ù±‚`a
Ù±‚`x"                                  Ù±‚`qverticalalignmentÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1fcenterÙ±‚bs1a'Ù±‚`a,Ù±‚`a
Ù±‚`x"                                  Ù±‚`shorizontalalignmentÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1fcenterÙ±‚bs1a'Ù±‚`a,Ù±‚`a
Ù±‚`x"                                  Ù±‚`nmultialignmentÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1dleftÙ±‚bs1a'Ù±‚`a,Ù±‚`a
Ù±‚`x"                                  Ù±‚`hxycoordsÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1maxes fractionÙ±‚bs1a'Ù±‚`a,Ù±‚`a
Ù±‚`x"                                  Ù±‚`hanimatedÙ±‚aoa=Ù±‚bkceFalseÙ±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`fcanvasÙ±‚aoa.Ù±‚`kmpl_connectÙ±‚`a(Ù±‚bs1a'Ù±‚bs1okey_press_eventÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚bbpdselfÙ±‚aoa.Ù±‚`lon_key_pressÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚akcdefÙ±‚`a Ù±‚bnfddrawÙ±‚`a(Ù±‚bbpdselfÙ±‚`a,Ù±‚`a Ù±‚`eeventÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`h        Ù±‚`kdraw_artistÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bbpdselfÙ±‚aoa.Ù±‚`baxÙ±‚aoa.Ù±‚`kdraw_artistÙ±‚`a
Ù±‚`h        Ù±‚akbifÙ±‚`a Ù±‚bbpdselfÙ±‚aoa.Ù±‚`jbackgroundÙ±‚`a Ù±‚bowbisÙ±‚`a Ù±‚bkcdNoneÙ±‚`a:Ù±‚`a
Ù±‚`l            Ù±‚bbpdselfÙ±‚aoa.Ù±‚`jbackgroundÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bbpdselfÙ±‚aoa.Ù±‚`fcanvasÙ±‚aoa.Ù±‚`ncopy_from_bboxÙ±‚`a(Ù±‚bbpdselfÙ±‚aoa.Ù±‚`baxÙ±‚aoa.Ù±‚`dbboxÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`h        Ù±‚bc1x$# restore the clean slate backgroundÙ±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`fcanvasÙ±‚aoa.Ù±‚`nrestore_regionÙ±‚`a(Ù±‚bbpdselfÙ±‚aoa.Ù±‚`jbackgroundÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`h        Ù±‚bc1v# show the distractorsÙ±‚`a
Ù±‚`h        Ù±‚akbifÙ±‚`a Ù±‚bbpdselfÙ±‚aoa.Ù±‚`hdistractÙ±‚`a:Ù±‚`a
Ù±‚`l            Ù±‚bbpdselfÙ±‚aoa.Ù±‚`dlineÙ±‚aoa.Ù±‚`iset_ydataÙ±‚`a(Ù±‚`bnpÙ±‚aoa.Ù±‚`csinÙ±‚`a(Ù±‚bbpdselfÙ±‚aoa.Ù±‚`axÙ±‚`a Ù±‚aoa+Ù±‚`a Ù±‚bbpdselfÙ±‚aoa.Ù±‚`ccntÙ±‚aoa/Ù±‚bbpdselfÙ±‚aoa.Ù±‚`cresÙ±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`l            Ù±‚bbpdselfÙ±‚aoa.Ù±‚`eline2Ù±‚aoa.Ù±‚`iset_ydataÙ±‚`a(Ù±‚`bnpÙ±‚aoa.Ù±‚`ccosÙ±‚`a(Ù±‚bbpdselfÙ±‚aoa.Ù±‚`axÙ±‚`a Ù±‚aoa-Ù±‚`a Ù±‚bbpdselfÙ±‚aoa.Ù±‚`ccntÙ±‚aoa/Ù±‚bbpdselfÙ±‚aoa.Ù±‚`cresÙ±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`l            Ù±‚bbpdselfÙ±‚aoa.Ù±‚`eline3Ù±‚aoa.Ù±‚`iset_ydataÙ±‚`a(Ù±‚`bnpÙ±‚aoa.Ù±‚`ctanÙ±‚`a(Ù±‚bbpdselfÙ±‚aoa.Ù±‚`axÙ±‚`a Ù±‚aoa+Ù±‚`a Ù±‚bbpdselfÙ±‚aoa.Ù±‚`ccntÙ±‚aoa/Ù±‚bbpdselfÙ±‚aoa.Ù±‚`cresÙ±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`l            Ù±‚bbpdselfÙ±‚aoa.Ù±‚`eline4Ù±‚aoa.Ù±‚`iset_ydataÙ±‚`a(Ù±‚`bnpÙ±‚aoa.Ù±‚`ctanÙ±‚`a(Ù±‚bbpdselfÙ±‚aoa.Ù±‚`axÙ±‚`a Ù±‚aoa-Ù±‚`a Ù±‚bbpdselfÙ±‚aoa.Ù±‚`ccntÙ±‚aoa/Ù±‚bbpdselfÙ±‚aoa.Ù±‚`cresÙ±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`l            Ù±‚`kdraw_artistÙ±‚`a(Ù±‚bbpdselfÙ±‚aoa.Ù±‚`dlineÙ±‚`a)Ù±‚`a
Ù±‚`l            Ù±‚`kdraw_artistÙ±‚`a(Ù±‚bbpdselfÙ±‚aoa.Ù±‚`eline2Ù±‚`a)Ù±‚`a
Ù±‚`l            Ù±‚`kdraw_artistÙ±‚`a(Ù±‚bbpdselfÙ±‚aoa.Ù±‚`eline3Ù±‚`a)Ù±‚`a
Ù±‚`l            Ù±‚`kdraw_artistÙ±‚`a(Ù±‚bbpdselfÙ±‚aoa.Ù±‚`eline4Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`h        Ù±‚bc1p# pucks and padsÙ±‚`a
Ù±‚`h        Ù±‚akbifÙ±‚`a Ù±‚bbpdselfÙ±‚aoa.Ù±‚`bonÙ±‚`a:Ù±‚`a
Ù±‚`l            Ù±‚bbpdselfÙ±‚aoa.Ù±‚`baxÙ±‚aoa.Ù±‚`kdraw_artistÙ±‚`a(Ù±‚bbpdselfÙ±‚aoa.Ù±‚`jcenterlineÙ±‚`a)Ù±‚`a
Ù±‚`l            Ù±‚akcforÙ±‚`a Ù±‚`cpadÙ±‚`a Ù±‚bowbinÙ±‚`a Ù±‚bbpdselfÙ±‚aoa.Ù±‚`dpadsÙ±‚`a:Ù±‚`a
Ù±‚`p                Ù±‚`cpadÙ±‚aoa.Ù±‚`ddispÙ±‚aoa.Ù±‚`eset_yÙ±‚`a(Ù±‚`cpadÙ±‚aoa.Ù±‚`ayÙ±‚`a)Ù±‚`a
Ù±‚`p                Ù±‚`cpadÙ±‚aoa.Ù±‚`ddispÙ±‚aoa.Ù±‚`eset_xÙ±‚`a(Ù±‚`cpadÙ±‚aoa.Ù±‚`axÙ±‚`a)Ù±‚`a
Ù±‚`p                Ù±‚bbpdselfÙ±‚aoa.Ù±‚`baxÙ±‚aoa.Ù±‚`kdraw_artistÙ±‚`a(Ù±‚`cpadÙ±‚aoa.Ù±‚`ddispÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`l            Ù±‚akcforÙ±‚`a Ù±‚`dpuckÙ±‚`a Ù±‚bowbinÙ±‚`a Ù±‚bbpdselfÙ±‚aoa.Ù±‚`epucksÙ±‚`a:Ù±‚`a
Ù±‚`p                Ù±‚akbifÙ±‚`a Ù±‚`dpuckÙ±‚aoa.Ù±‚`fupdateÙ±‚`a(Ù±‚bbpdselfÙ±‚aoa.Ù±‚`dpadsÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`t                    Ù±‚bc1x$# we only get here if someone scoredÙ±‚`a
Ù±‚`t                    Ù±‚bbpdselfÙ±‚aoa.Ù±‚`dpadsÙ±‚`a[Ù±‚bmia0Ù±‚`a]Ù±‚aoa.Ù±‚`ddispÙ±‚aoa.Ù±‚`iset_labelÙ±‚`a(Ù±‚`a
Ù±‚`x                        Ù±‚bs2a"Ù±‚bs2c   Ù±‚bs2a"Ù±‚`a Ù±‚aoa+Ù±‚`a Ù±‚bnbcstrÙ±‚`a(Ù±‚bbpdselfÙ±‚aoa.Ù±‚`dpadsÙ±‚`a[Ù±‚bmia0Ù±‚`a]Ù±‚aoa.Ù±‚`escoreÙ±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`t                    Ù±‚bbpdselfÙ±‚aoa.Ù±‚`dpadsÙ±‚`a[Ù±‚bmia1Ù±‚`a]Ù±‚aoa.Ù±‚`ddispÙ±‚aoa.Ù±‚`iset_labelÙ±‚`a(Ù±‚`a
Ù±‚`x                        Ù±‚bs2a"Ù±‚bs2c   Ù±‚bs2a"Ù±‚`a Ù±‚aoa+Ù±‚`a Ù±‚bnbcstrÙ±‚`a(Ù±‚bbpdselfÙ±‚aoa.Ù±‚`dpadsÙ±‚`a[Ù±‚bmia1Ù±‚`a]Ù±‚aoa.Ù±‚`escoreÙ±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`t                    Ù±‚bbpdselfÙ±‚aoa.Ù±‚`baxÙ±‚aoa.Ù±‚`flegendÙ±‚`a(Ù±‚`clocÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1fcenterÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`jframealphaÙ±‚aoa=Ù±‚bmfb.2Ù±‚`a,Ù±‚`a
Ù±‚`x#                                   Ù±‚`ifacecolorÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1c0.5Ù±‚bs1a'Ù±‚`a,Ù±‚`a
Ù±‚`x#                                   Ù±‚`dpropÙ±‚aoa=Ù±‚`nFontPropertiesÙ±‚`a(Ù±‚`dsizeÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1hxx-largeÙ±‚bs1a'Ù±‚`a,Ù±‚`a
Ù±‚`x7                                                       Ù±‚`fweightÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1dboldÙ±‚bs1a'Ù±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`t                    Ù±‚bbpdselfÙ±‚aoa.Ù±‚`jbackgroundÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bkcdNoneÙ±‚`a
Ù±‚`t                    Ù±‚bbpdselfÙ±‚aoa.Ù±‚`baxÙ±‚aoa.Ù±‚`ffigureÙ±‚aoa.Ù±‚`fcanvasÙ±‚aoa.Ù±‚`idraw_idleÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`t                    Ù±‚akfreturnÙ±‚`a Ù±‚bkcdTrueÙ±‚`a
Ù±‚`p                Ù±‚`dpuckÙ±‚aoa.Ù±‚`ddispÙ±‚aoa.Ù±‚`kset_offsetsÙ±‚`a(Ù±‚`a[Ù±‚`a[Ù±‚`dpuckÙ±‚aoa.Ù±‚`axÙ±‚`a,Ù±‚`a Ù±‚`dpuckÙ±‚aoa.Ù±‚`ayÙ±‚`a]Ù±‚`a]Ù±‚`a)Ù±‚`a
Ù±‚`p                Ù±‚bbpdselfÙ±‚aoa.Ù±‚`baxÙ±‚aoa.Ù±‚`kdraw_artistÙ±‚`a(Ù±‚`dpuckÙ±‚aoa.Ù±‚`ddispÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`h        Ù±‚bc1x # just redraw the axes rectangleÙ±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`fcanvasÙ±‚aoa.Ù±‚`dblitÙ±‚`a(Ù±‚bbpdselfÙ±‚aoa.Ù±‚`baxÙ±‚aoa.Ù±‚`dbboxÙ±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`fcanvasÙ±‚aoa.Ù±‚`lflush_eventsÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚akbifÙ±‚`a Ù±‚bbpdselfÙ±‚aoa.Ù±‚`ccntÙ±‚`a Ù±‚aob==Ù±‚`a Ù±‚bmie50000Ù±‚`a:Ù±‚`a
Ù±‚`l            Ù±‚bc1x## just so we don't get carried awayÙ±‚`a
Ù±‚`l            Ù±‚bnbeprintÙ±‚`a(Ù±‚bs2a"Ù±‚bs2j...and youÙ±‚bs2a'Ù±‚bs2xve been playing for too long!!!Ù±‚bs2a"Ù±‚`a)Ù±‚`a
Ù±‚`l            Ù±‚`cpltÙ±‚aoa.Ù±‚`ecloseÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`ccntÙ±‚`a Ù±‚aoa+Ù±‚aoa=Ù±‚`a Ù±‚bmia1Ù±‚`a
Ù±‚`h        Ù±‚akfreturnÙ±‚`a Ù±‚bkcdTrueÙ±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚akcdefÙ±‚`a Ù±‚bnflon_key_pressÙ±‚`a(Ù±‚bbpdselfÙ±‚`a,Ù±‚`a Ù±‚`eeventÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`h        Ù±‚akbifÙ±‚`a Ù±‚`eeventÙ±‚aoa.Ù±‚`ckeyÙ±‚`a Ù±‚aob==Ù±‚`a Ù±‚bs1a'Ù±‚bs1a3Ù±‚bs1a'Ù±‚`a:Ù±‚`a
Ù±‚`l            Ù±‚bbpdselfÙ±‚aoa.Ù±‚`cresÙ±‚`a Ù±‚aoa*Ù±‚aoa=Ù±‚`a Ù±‚bmfc5.0Ù±‚`a
Ù±‚`h        Ù±‚akbifÙ±‚`a Ù±‚`eeventÙ±‚aoa.Ù±‚`ckeyÙ±‚`a Ù±‚aob==Ù±‚`a Ù±‚bs1a'Ù±‚bs1a4Ù±‚bs1a'Ù±‚`a:Ù±‚`a
Ù±‚`l            Ù±‚bbpdselfÙ±‚aoa.Ù±‚`cresÙ±‚`a Ù±‚aoa/Ù±‚aoa=Ù±‚`a Ù±‚bmfc5.0Ù±‚`a
Ù±‚`a
Ù±‚`h        Ù±‚akbifÙ±‚`a Ù±‚`eeventÙ±‚aoa.Ù±‚`ckeyÙ±‚`a Ù±‚aob==Ù±‚`a Ù±‚bs1a'Ù±‚bs1aeÙ±‚bs1a'Ù±‚`a:Ù±‚`a
Ù±‚`l            Ù±‚bbpdselfÙ±‚aoa.Ù±‚`dpadsÙ±‚`a[Ù±‚bmia0Ù±‚`a]Ù±‚aoa.Ù±‚`ayÙ±‚`a Ù±‚aoa+Ù±‚aoa=Ù±‚`a Ù±‚bmfb.1Ù±‚`a
Ù±‚`l            Ù±‚akbifÙ±‚`a Ù±‚bbpdselfÙ±‚aoa.Ù±‚`dpadsÙ±‚`a[Ù±‚bmia0Ù±‚`a]Ù±‚aoa.Ù±‚`ayÙ±‚`a Ù±‚aoa>Ù±‚`a Ù±‚bmia1Ù±‚`a Ù±‚aoa-Ù±‚`a Ù±‚bmfb.3Ù±‚`a:Ù±‚`a
Ù±‚`p                Ù±‚bbpdselfÙ±‚aoa.Ù±‚`dpadsÙ±‚`a[Ù±‚bmia0Ù±‚`a]Ù±‚aoa.Ù±‚`ayÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bmia1Ù±‚`a Ù±‚aoa-Ù±‚`a Ù±‚bmfb.3Ù±‚`a
Ù±‚`h        Ù±‚akbifÙ±‚`a Ù±‚`eeventÙ±‚aoa.Ù±‚`ckeyÙ±‚`a Ù±‚aob==Ù±‚`a Ù±‚bs1a'Ù±‚bs1adÙ±‚bs1a'Ù±‚`a:Ù±‚`a
Ù±‚`l            Ù±‚bbpdselfÙ±‚aoa.Ù±‚`dpadsÙ±‚`a[Ù±‚bmia0Ù±‚`a]Ù±‚aoa.Ù±‚`ayÙ±‚`a Ù±‚aoa-Ù±‚aoa=Ù±‚`a Ù±‚bmfb.1Ù±‚`a
Ù±‚`l            Ù±‚akbifÙ±‚`a Ù±‚bbpdselfÙ±‚aoa.Ù±‚`dpadsÙ±‚`a[Ù±‚bmia0Ù±‚`a]Ù±‚aoa.Ù±‚`ayÙ±‚`a Ù±‚aoa<Ù±‚`a Ù±‚aoa-Ù±‚bmia1Ù±‚`a:Ù±‚`a
Ù±‚`p                Ù±‚bbpdselfÙ±‚aoa.Ù±‚`dpadsÙ±‚`a[Ù±‚bmia0Ù±‚`a]Ù±‚aoa.Ù±‚`ayÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚aoa-Ù±‚bmia1Ù±‚`a
Ù±‚`a
Ù±‚`h        Ù±‚akbifÙ±‚`a Ù±‚`eeventÙ±‚aoa.Ù±‚`ckeyÙ±‚`a Ù±‚aob==Ù±‚`a Ù±‚bs1a'Ù±‚bs1aiÙ±‚bs1a'Ù±‚`a:Ù±‚`a
Ù±‚`l            Ù±‚bbpdselfÙ±‚aoa.Ù±‚`dpadsÙ±‚`a[Ù±‚bmia1Ù±‚`a]Ù±‚aoa.Ù±‚`ayÙ±‚`a Ù±‚aoa+Ù±‚aoa=Ù±‚`a Ù±‚bmfb.1Ù±‚`a
Ù±‚`l            Ù±‚akbifÙ±‚`a Ù±‚bbpdselfÙ±‚aoa.Ù±‚`dpadsÙ±‚`a[Ù±‚bmia1Ù±‚`a]Ù±‚aoa.Ù±‚`ayÙ±‚`a Ù±‚aoa>Ù±‚`a Ù±‚bmia1Ù±‚`a Ù±‚aoa-Ù±‚`a Ù±‚bmfb.3Ù±‚`a:Ù±‚`a
Ù±‚`p                Ù±‚bbpdselfÙ±‚aoa.Ù±‚`dpadsÙ±‚`a[Ù±‚bmia1Ù±‚`a]Ù±‚aoa.Ù±‚`ayÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bmia1Ù±‚`a Ù±‚aoa-Ù±‚`a Ù±‚bmfb.3Ù±‚`a
Ù±‚`h        Ù±‚akbifÙ±‚`a Ù±‚`eeventÙ±‚aoa.Ù±‚`ckeyÙ±‚`a Ù±‚aob==Ù±‚`a Ù±‚bs1a'Ù±‚bs1akÙ±‚bs1a'Ù±‚`a:Ù±‚`a
Ù±‚`l            Ù±‚bbpdselfÙ±‚aoa.Ù±‚`dpadsÙ±‚`a[Ù±‚bmia1Ù±‚`a]Ù±‚aoa.Ù±‚`ayÙ±‚`a Ù±‚aoa-Ù±‚aoa=Ù±‚`a Ù±‚bmfb.1Ù±‚`a
Ù±‚`l            Ù±‚akbifÙ±‚`a Ù±‚bbpdselfÙ±‚aoa.Ù±‚`dpadsÙ±‚`a[Ù±‚bmia1Ù±‚`a]Ù±‚aoa.Ù±‚`ayÙ±‚`a Ù±‚aoa<Ù±‚`a Ù±‚aoa-Ù±‚bmia1Ù±‚`a:Ù±‚`a
Ù±‚`p                Ù±‚bbpdselfÙ±‚aoa.Ù±‚`dpadsÙ±‚`a[Ù±‚bmia1Ù±‚`a]Ù±‚aoa.Ù±‚`ayÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚aoa-Ù±‚bmia1Ù±‚`a
Ù±‚`a
Ù±‚`h        Ù±‚akbifÙ±‚`a Ù±‚`eeventÙ±‚aoa.Ù±‚`ckeyÙ±‚`a Ù±‚aob==Ù±‚`a Ù±‚bs1a'Ù±‚bs1aaÙ±‚bs1a'Ù±‚`a:Ù±‚`a
Ù±‚`l            Ù±‚bbpdselfÙ±‚aoa.Ù±‚`epucksÙ±‚aoa.Ù±‚`fappendÙ±‚`a(Ù±‚`dPuckÙ±‚`a(Ù±‚bbpdselfÙ±‚aoa.Ù±‚`hpuckdispÙ±‚`a,Ù±‚`a
Ù±‚`x#                                   Ù±‚bbpdselfÙ±‚aoa.Ù±‚`dpadsÙ±‚`a[Ù±‚`grandintÙ±‚`a(Ù±‚bmia2Ù±‚`a)Ù±‚`a]Ù±‚`a,Ù±‚`a
Ù±‚`x#                                   Ù±‚bbpdselfÙ±‚aoa.Ù±‚`baxÙ±‚aoa.Ù±‚`dbboxÙ±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚akbifÙ±‚`a Ù±‚`eeventÙ±‚aoa.Ù±‚`ckeyÙ±‚`a Ù±‚aob==Ù±‚`a Ù±‚bs1a'Ù±‚bs1aAÙ±‚bs1a'Ù±‚`a Ù±‚bowcandÙ±‚`a Ù±‚bnbclenÙ±‚`a(Ù±‚bbpdselfÙ±‚aoa.Ù±‚`epucksÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`l            Ù±‚bbpdselfÙ±‚aoa.Ù±‚`epucksÙ±‚aoa.Ù±‚`cpopÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚akbifÙ±‚`a Ù±‚`eeventÙ±‚aoa.Ù±‚`ckeyÙ±‚`a Ù±‚aob==Ù±‚`a Ù±‚bs1a'Ù±‚bs1a Ù±‚bs1a'Ù±‚`a Ù±‚bowcandÙ±‚`a Ù±‚bnbclenÙ±‚`a(Ù±‚bbpdselfÙ±‚aoa.Ù±‚`epucksÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`l            Ù±‚bbpdselfÙ±‚aoa.Ù±‚`epucksÙ±‚`a[Ù±‚bmia0Ù±‚`a]Ù±‚aoa.Ù±‚`f_resetÙ±‚`a(Ù±‚bbpdselfÙ±‚aoa.Ù±‚`dpadsÙ±‚`a[Ù±‚`grandintÙ±‚`a(Ù±‚bmia2Ù±‚`a)Ù±‚`a]Ù±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚akbifÙ±‚`a Ù±‚`eeventÙ±‚aoa.Ù±‚`ckeyÙ±‚`a Ù±‚aob==Ù±‚`a Ù±‚bs1a'Ù±‚bs1a1Ù±‚bs1a'Ù±‚`a:Ù±‚`a
Ù±‚`l            Ù±‚akcforÙ±‚`a Ù±‚`apÙ±‚`a Ù±‚bowbinÙ±‚`a Ù±‚bbpdselfÙ±‚aoa.Ù±‚`epucksÙ±‚`a:Ù±‚`a
Ù±‚`p                Ù±‚`apÙ±‚aoa.Ù±‚`g_slowerÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚akbifÙ±‚`a Ù±‚`eeventÙ±‚aoa.Ù±‚`ckeyÙ±‚`a Ù±‚aob==Ù±‚`a Ù±‚bs1a'Ù±‚bs1a2Ù±‚bs1a'Ù±‚`a:Ù±‚`a
Ù±‚`l            Ù±‚akcforÙ±‚`a Ù±‚`apÙ±‚`a Ù±‚bowbinÙ±‚`a Ù±‚bbpdselfÙ±‚aoa.Ù±‚`epucksÙ±‚`a:Ù±‚`a
Ù±‚`p                Ù±‚`apÙ±‚aoa.Ù±‚`g_fasterÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`h        Ù±‚akbifÙ±‚`a Ù±‚`eeventÙ±‚aoa.Ù±‚`ckeyÙ±‚`a Ù±‚aob==Ù±‚`a Ù±‚bs1a'Ù±‚bs1anÙ±‚bs1a'Ù±‚`a:Ù±‚`a
Ù±‚`l            Ù±‚bbpdselfÙ±‚aoa.Ù±‚`hdistractÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bowcnotÙ±‚`a Ù±‚bbpdselfÙ±‚aoa.Ù±‚`hdistractÙ±‚`a
Ù±‚`a
Ù±‚`h        Ù±‚akbifÙ±‚`a Ù±‚`eeventÙ±‚aoa.Ù±‚`ckeyÙ±‚`a Ù±‚aob==Ù±‚`a Ù±‚bs1a'Ù±‚bs1agÙ±‚bs1a'Ù±‚`a:Ù±‚`a
Ù±‚`l            Ù±‚bbpdselfÙ±‚aoa.Ù±‚`bonÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bowcnotÙ±‚`a Ù±‚bbpdselfÙ±‚aoa.Ù±‚`bonÙ±‚`a
Ù±‚`h        Ù±‚akbifÙ±‚`a Ù±‚`eeventÙ±‚aoa.Ù±‚`ckeyÙ±‚`a Ù±‚aob==Ù±‚`a Ù±‚bs1a'Ù±‚bs1atÙ±‚bs1a'Ù±‚`a:Ù±‚`a
Ù±‚`l            Ù±‚bbpdselfÙ±‚aoa.Ù±‚`dinstÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bowcnotÙ±‚`a Ù±‚bbpdselfÙ±‚aoa.Ù±‚`dinstÙ±‚`a
Ù±‚`l            Ù±‚bbpdselfÙ±‚aoa.Ù±‚`aiÙ±‚aoa.Ù±‚`kset_visibleÙ±‚`a(Ù±‚bowcnotÙ±‚`a Ù±‚bbpdselfÙ±‚aoa.Ù±‚`aiÙ±‚aoa.Ù±‚`kget_visibleÙ±‚`a(Ù±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`l            Ù±‚bbpdselfÙ±‚aoa.Ù±‚`jbackgroundÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bkcdNoneÙ±‚`a
Ù±‚`l            Ù±‚bbpdselfÙ±‚aoa.Ù±‚`fcanvasÙ±‚aoa.Ù±‚`idraw_idleÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚akbifÙ±‚`a Ù±‚`eeventÙ±‚aoa.Ù±‚`ckeyÙ±‚`a Ù±‚aob==Ù±‚`a Ù±‚bs1a'Ù±‚bs1aqÙ±‚bs1a'Ù±‚`a:Ù±‚`a
Ù±‚`l            Ù±‚`cpltÙ±‚aoa.Ù±‚`ecloseÙ±‚`a(Ù±‚`a)Ù±‚`a
`dNoneö