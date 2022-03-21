Ù¯‚Ù´ƒ™/Ù±‚bsdx"""
=================================================
Animated image using a precomputed list of images
=================================================

"""Ù±‚`a
Ù±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„enumpyÙ „enumpyf1.22.3fmoduleenumpyfmoduleõÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnnbnpÙ±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnnfpyplotÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnncpltÙ±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnnianimationÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnnianimationÙ±‚`a
Ù±‚`a
Ù±‚`cfigÙ±‚`a,Ù±‚`a Ù±‚`baxÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cpltÙ±‚aoa.Ù±‚`hsubplotsÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚akcdefÙ±‚`a Ù±‚bnfafÙ±‚`a(Ù±‚`axÙ±‚`a,Ù±‚`a Ù±‚`ayÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`d    Ù±‚akfreturnÙ±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`csinÙ±‚`a(Ù±‚`axÙ±‚`a)Ù±‚`a Ù±‚aoa+Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`ccosÙ±‚`a(Ù±‚`ayÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`axÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`hlinspaceÙ±‚`a(Ù±‚bmia0Ù±‚`a,Ù±‚`a Ù±‚bmia2Ù±‚`a Ù±‚aoa*Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`bpiÙ±‚`a,Ù±‚`a Ù±‚bmic120Ù±‚`a)Ù±‚`a
Ù±‚`ayÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`hlinspaceÙ±‚`a(Ù±‚bmia0Ù±‚`a,Ù±‚`a Ù±‚bmia2Ù±‚`a Ù±‚aoa*Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`bpiÙ±‚`a,Ù±‚`a Ù±‚bmic100Ù±‚`a)Ù±‚aoa.Ù±‚`greshapeÙ±‚`a(Ù±‚aoa-Ù±‚bmia1Ù±‚`a,Ù±‚`a Ù±‚bmia1Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚bc1xF# ims is a list of lists, each row is a list of artists to draw in theÙ±‚`a
Ù±‚bc1xE# current frame; here we are just animating one artist, the image, inÙ±‚`a
Ù±‚bc1l# each frameÙ±‚`a
Ù±‚`cimsÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`a[Ù±‚`a]Ù±‚`a
Ù±‚akcforÙ±‚`a Ù±‚`aiÙ±‚`a Ù±‚bowbinÙ±‚`a Ù±‚bnberangeÙ±‚`a(Ù±‚bmib60Ù±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`d    Ù±‚`axÙ±‚`a Ù±‚aoa+Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`bpiÙ±‚`a Ù±‚aoa/Ù±‚`a Ù±‚bmfc15.Ù±‚`a
Ù±‚`d    Ù±‚`ayÙ±‚`a Ù±‚aoa+Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`bpiÙ±‚`a Ù±‚aoa/Ù±‚`a Ù±‚bmfc20.Ù±‚`a
Ù±‚`d    Ù±‚`bimÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`baxÙ±‚aoa.Ù±‚`fimshowÙ±‚`a(Ù±‚`afÙ±‚`a(Ù±‚`axÙ±‚`a,Ù±‚`a Ù±‚`ayÙ±‚`a)Ù±‚`a,Ù±‚`a Ù±‚`hanimatedÙ±‚aoa=Ù±‚bkcdTrueÙ±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚akbifÙ±‚`a Ù±‚`aiÙ±‚`a Ù±‚aob==Ù±‚`a Ù±‚bmia0Ù±‚`a:Ù±‚`a
Ù±‚`h        Ù±‚`baxÙ±‚aoa.Ù±‚`fimshowÙ±‚`a(Ù±‚`afÙ±‚`a(Ù±‚`axÙ±‚`a,Ù±‚`a Ù±‚`ayÙ±‚`a)Ù±‚`a)Ù±‚`b  Ù±‚bc1x# show an initial one firstÙ±‚`a
Ù±‚`d    Ù±‚`cimsÙ±‚aoa.Ù±‚`fappendÙ±‚`a(Ù±‚`a[Ù±‚`bimÙ±‚`a]Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`caniÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`ianimationÙ±‚aoa.Ù±‚`oArtistAnimationÙ±‚`a(Ù±‚`cfigÙ±‚`a,Ù±‚`a Ù±‚`cimsÙ±‚`a,Ù±‚`a Ù±‚`hintervalÙ±‚aoa=Ù±‚bmib50Ù±‚`a,Ù±‚`a Ù±‚`dblitÙ±‚aoa=Ù±‚bkcdTrueÙ±‚`a,Ù±‚`a
Ù±‚`x                                 Ù±‚`lrepeat_delayÙ±‚aoa=Ù±‚bmid1000Ù±‚`a)Ù±‚`a
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