Ù¯‚Ù´ƒ˜¹Ù±‚bsdxA"""
==================
Animated line plot
==================

"""Ù±‚`a
Ù±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„enumpyÙ „enumpyf1.22.3fmoduleenumpyfmoduleõÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnnbnpÙ±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnnfpyplotÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnncpltÙ±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnnianimationÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnnianimationÙ±‚`a
Ù±‚`a
Ù±‚`cfigÙ±‚`a,Ù±‚`a Ù±‚`baxÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cpltÙ±‚aoa.Ù±‚`hsubplotsÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`axÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`farangeÙ±‚`a(Ù±‚bmia0Ù±‚`a,Ù±‚`a Ù±‚bmia2Ù±‚aoa*Ù±‚`bnpÙ±‚aoa.Ù±‚`bpiÙ±‚`a,Ù±‚`a Ù±‚bmfd0.01Ù±‚`a)Ù±‚`a
Ù±‚`dlineÙ±‚`a,Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`baxÙ±‚aoa.Ù±‚`dplotÙ±‚`a(Ù±‚`axÙ±‚`a,Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`csinÙ±‚`a(Ù±‚`axÙ±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚akcdefÙ±‚`a Ù±‚bnfganimateÙ±‚`a(Ù±‚`aiÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`d    Ù±‚`dlineÙ±‚aoa.Ù±‚`iset_ydataÙ±‚`a(Ù±‚`bnpÙ±‚aoa.Ù±‚`csinÙ±‚`a(Ù±‚`axÙ±‚`a Ù±‚aoa+Ù±‚`a Ù±‚`aiÙ±‚`a Ù±‚aoa/Ù±‚`a Ù±‚bmib50Ù±‚`a)Ù±‚`a)Ù±‚`b  Ù±‚bc1r# update the data.Ù±‚`a
Ù±‚`d    Ù±‚akfreturnÙ±‚`a Ù±‚`dlineÙ±‚`a,Ù±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚`caniÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`ianimationÙ±‚aoa.Ù±‚`mFuncAnimationÙ±‚`a(Ù±‚`a
Ù±‚`d    Ù±‚`cfigÙ±‚`a,Ù±‚`a Ù±‚`ganimateÙ±‚`a,Ù±‚`a Ù±‚`hintervalÙ±‚aoa=Ù±‚bmib20Ù±‚`a,Ù±‚`a Ù±‚`dblitÙ±‚aoa=Ù±‚bkcdTrueÙ±‚`a,Ù±‚`a Ù±‚`jsave_countÙ±‚aoa=Ù±‚bmib50Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚bc1x!# To save the animation, use e.g.Ù±‚`a
Ù±‚bc1a#Ù±‚`a
Ù±‚bc1w# ani.save("movie.mp4")Ù±‚`a
Ù±‚bc1a#Ù±‚`a
Ù±‚bc1d# orÙ±‚`a
Ù±‚bc1a#Ù±‚`a
Ù±‚bc1x"# writer = animation.FFMpegWriter(Ù±‚`a
Ù±‚bc1x7#     fps=15, metadata=dict(artist='Me'), bitrate=1800)Ù±‚`a
Ù±‚bc1x&# ani.save("movie.mp4", writer=writer)Ù±‚`a
Ù±‚`a
Ù±‚`cpltÙ±‚aoa.Ù±‚`dshowÙ±‚`a(Ù±‚`a)Ù±‚`a
`dNoneö