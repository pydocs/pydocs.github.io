Ù¯‚Ù´ƒ™CÙ±‚bsdxš"""
==================
Animated histogram
==================

Use histogram's `.BarContainer` to draw a bunch of rectangles for an animated
histogram.
"""Ù±‚`a
Ù±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„enumpyÙ „enumpyf1.22.3fmoduleenumpyfmoduleõÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnnbnpÙ±‚`a
Ù±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnnfpyplotÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnncpltÙ±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnnianimationÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnnianimationÙ±‚`a
Ù±‚`a
Ù±‚bc1x)# Fixing random state for reproducibilityÙ±‚`a
Ù±‚`bnpÙ±‚aoa.Ù±‚`frandomÙ±‚aoa.Ù±‚`dseedÙ±‚`a(Ù±‚bmih19680801Ù±‚`a)Ù±‚`a
Ù±‚bc1r# Fixing bin edgesÙ±‚`a
Ù±‚`iHIST_BINSÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`hlinspaceÙ±‚`a(Ù±‚aoa-Ù±‚bmia4Ù±‚`a,Ù±‚`a Ù±‚bmia4Ù±‚`a,Ù±‚`a Ù±‚bmic100Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚bc1x# histogram our data with numpyÙ±‚`a
Ù±‚`ddataÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`frandomÙ±‚aoa.Ù±‚`erandnÙ±‚`a(Ù±‚bmid1000Ù±‚`a)Ù±‚`a
Ù±‚`anÙ±‚`a,Ù±‚`a Ù±‚`a_Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`ihistogramÙ±‚`a(Ù±‚`ddataÙ±‚`a,Ù±‚`a Ù±‚`iHIST_BINSÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚bc1xO###############################################################################Ù±‚`a
Ù±‚bc1xL# To animate the histogram, we need an ``animate`` function, which generatesÙ±‚`a
Ù±‚bc1xM# a random set of numbers and updates the heights of rectangles. We utilize aÙ±‚`a
Ù±‚bc1xK# python closure to track an instance of `.BarContainer` whose `.Rectangle`Ù±‚`a
Ù±‚bc1x# patches we shall update.Ù±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚akcdefÙ±‚`a Ù±‚bnfqprepare_animationÙ±‚`a(Ù±‚`mbar_containerÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚akcdefÙ±‚`a Ù±‚bnfganimateÙ±‚`a(Ù±‚`lframe_numberÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`h        Ù±‚bc1x# simulate new data coming inÙ±‚`a
Ù±‚`h        Ù±‚`ddataÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`frandomÙ±‚aoa.Ù±‚`erandnÙ±‚`a(Ù±‚bmid1000Ù±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚`anÙ±‚`a,Ù±‚`a Ù±‚`a_Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`ihistogramÙ±‚`a(Ù±‚`ddataÙ±‚`a,Ù±‚`a Ù±‚`iHIST_BINSÙ±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚akcforÙ±‚`a Ù±‚`ecountÙ±‚`a,Ù±‚`a Ù±‚`drectÙ±‚`a Ù±‚bowbinÙ±‚`a Ù±‚bnbczipÙ±‚`a(Ù±‚`anÙ±‚`a,Ù±‚`a Ù±‚`mbar_containerÙ±‚aoa.Ù±‚`gpatchesÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`l            Ù±‚`drectÙ±‚aoa.Ù±‚`jset_heightÙ±‚`a(Ù±‚`ecountÙ±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚akfreturnÙ±‚`a Ù±‚`mbar_containerÙ±‚aoa.Ù±‚`gpatchesÙ±‚`a
Ù±‚`d    Ù±‚akfreturnÙ±‚`a Ù±‚`ganimateÙ±‚`a
Ù±‚`a
Ù±‚bc1xO###############################################################################Ù±‚`a
Ù±‚bc1xG# Using :func:`~matplotlib.pyplot.hist` allows us to get an instance ofÙ±‚`a
Ù±‚bc1xK# `.BarContainer`, which is a collection of `.Rectangle` instances. CallingÙ±‚`a
Ù±‚bc1xN# ``prepare_animation`` will define ``animate`` function working with suppliedÙ±‚`a
Ù±‚bc1x># `.BarContainer`, all this is used to setup `.FuncAnimation`.Ù±‚`a
Ù±‚`a
Ù±‚`cfigÙ±‚`a,Ù±‚`a Ù±‚`baxÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cpltÙ±‚aoa.Ù±‚`hsubplotsÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`a_Ù±‚`a,Ù±‚`a Ù±‚`a_Ù±‚`a,Ù±‚`a Ù±‚`mbar_containerÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`baxÙ±‚aoa.Ù±‚`dhistÙ±‚`a(Ù±‚`ddataÙ±‚`a,Ù±‚`a Ù±‚`iHIST_BINSÙ±‚`a,Ù±‚`a Ù±‚`blwÙ±‚aoa=Ù±‚bmia1Ù±‚`a,Ù±‚`a
Ù±‚`x                              Ù±‚`becÙ±‚aoa=Ù±‚bs2a"Ù±‚bs2fyellowÙ±‚bs2a"Ù±‚`a,Ù±‚`a Ù±‚`bfcÙ±‚aoa=Ù±‚bs2a"Ù±‚bs2egreenÙ±‚bs2a"Ù±‚`a,Ù±‚`a Ù±‚`ealphaÙ±‚aoa=Ù±‚bmfc0.5Ù±‚`a)Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`hset_ylimÙ±‚`a(Ù±‚`ctopÙ±‚aoa=Ù±‚bmib55Ù±‚`a)Ù±‚`b  Ù±‚bc1x4# set safe limit to ensure that all data is visible.Ù±‚`a
Ù±‚`a
Ù±‚`caniÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`ianimationÙ±‚aoa.Ù±‚`mFuncAnimationÙ±‚`a(Ù±‚`cfigÙ±‚`a,Ù±‚`a Ù±‚`qprepare_animationÙ±‚`a(Ù±‚`mbar_containerÙ±‚`a)Ù±‚`a,Ù±‚`a Ù±‚bmib50Ù±‚`a,Ù±‚`a
Ù±‚`x                              Ù±‚`frepeatÙ±‚aoa=Ù±‚bkceFalseÙ±‚`a,Ù±‚`a Ù±‚`dblitÙ±‚aoa=Ù±‚bkcdTrueÙ±‚`a)Ù±‚`a
Ù±‚`cpltÙ±‚aoa.Ù±‚`dshowÙ±‚`a(Ù±‚`a)Ù±‚`a
`dNoneö