ŸØÇÅŸ¥ÉôsŸ±ÇbsdxØ"""
===============
Rain simulation
===============

Simulates rain drops on a surface by animating the scale and opacity
of 50 scatter points.

Author: Nicolas P. Rougier
"""Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±ÇbknfimportŸ±Ç`a Ÿ±ÇbnnŸ¢ÑenumpyŸ†Ñenumpyf1.22.3fmoduleenumpyfmoduleıŸ±Ç`a Ÿ±ÇakbasŸ±Ç`a Ÿ±ÇbnnbnpŸ±Ç`a
Ÿ±ÇbknfimportŸ±Ç`a Ÿ±ÇbnnŸ¢ÑjmatplotlibŸ†Ñjmatplotlibe3.5.1fmodulejmatplotlibfmoduleıŸ±Çbnna.Ÿ±ÇbnnfpyplotŸ±Ç`a Ÿ±ÇakbasŸ±Ç`a Ÿ±ÇbnncpltŸ±Ç`a
Ÿ±ÇbkndfromŸ±Ç`a Ÿ±ÇbnnŸ¢ÑjmatplotlibŸ†Ñjmatplotlibe3.5.1fmodulejmatplotlibfmoduleıŸ±Çbnna.Ÿ±ÇbnnianimationŸ±Ç`a Ÿ±ÇbknfimportŸ±Ç`a Ÿ±Ç`mFuncAnimationŸ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1x)# Fixing random state for reproducibilityŸ±Ç`a
Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`frandomŸ±Çaoa.Ÿ±Ç`dseedŸ±Ç`a(Ÿ±Çbmih19680801Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1x/# Create new Figure and an Axes which fills it.Ÿ±Ç`a
Ÿ±Ç`cfigŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`ffigureŸ±Ç`a(Ÿ±Ç`gfigsizeŸ±Çaoa=Ÿ±Ç`a(Ÿ±Çbmia7Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia7Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`baxŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cfigŸ±Çaoa.Ÿ±Ç`hadd_axesŸ±Ç`a(Ÿ±Ç`a[Ÿ±Çbmia0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia1Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`gframeonŸ±Çaoa=Ÿ±ÇbkceFalseŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`hset_xlimŸ±Ç`a(Ÿ±Çbmia0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia1Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`jset_xticksŸ±Ç`a(Ÿ±Ç`a[Ÿ±Ç`a]Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`hset_ylimŸ±Ç`a(Ÿ±Çbmia0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia1Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`jset_yticksŸ±Ç`a(Ÿ±Ç`a[Ÿ±Ç`a]Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1r# Create rain dataŸ±Ç`a
Ÿ±Ç`gn_dropsŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Çbmib50Ÿ±Ç`a
Ÿ±Ç`jrain_dropsŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`ezerosŸ±Ç`a(Ÿ±Ç`gn_dropsŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`edtypeŸ±Çaoa=Ÿ±Ç`a[Ÿ±Ç`a(Ÿ±Çbs1a'Ÿ±Çbs1hpositionŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±ÇbnbefloatŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`a(Ÿ±Çbmia2Ÿ±Ç`a,Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`x&                                      Ÿ±Ç`a(Ÿ±Çbs1a'Ÿ±Çbs1dsizeŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`e     Ÿ±ÇbnbefloatŸ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`x&                                      Ÿ±Ç`a(Ÿ±Çbs1a'Ÿ±Çbs1fgrowthŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`c   Ÿ±ÇbnbefloatŸ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`x&                                      Ÿ±Ç`a(Ÿ±Çbs1a'Ÿ±Çbs1ecolorŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`d    Ÿ±ÇbnbefloatŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`a(Ÿ±Çbmia4Ÿ±Ç`a,Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a]Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1x7# Initialize the raindrops in random positions and withŸ±Ç`a
Ÿ±Çbc1v# random growth rates.Ÿ±Ç`a
Ÿ±Ç`jrain_dropsŸ±Ç`a[Ÿ±Çbs1a'Ÿ±Çbs1hpositionŸ±Çbs1a'Ÿ±Ç`a]Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`frandomŸ±Çaoa.Ÿ±Ç`guniformŸ±Ç`a(Ÿ±Çbmia0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`a(Ÿ±Ç`gn_dropsŸ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia2Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`jrain_dropsŸ±Ç`a[Ÿ±Çbs1a'Ÿ±Çbs1fgrowthŸ±Çbs1a'Ÿ±Ç`a]Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`frandomŸ±Çaoa.Ÿ±Ç`guniformŸ±Ç`a(Ÿ±Çbmib50Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmic200Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`gn_dropsŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1x=# Construct the scatter which we will update during animationŸ±Ç`a
Ÿ±Çbc1x# as the raindrops develop.Ÿ±Ç`a
Ÿ±Ç`dscatŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`gscatterŸ±Ç`a(Ÿ±Ç`jrain_dropsŸ±Ç`a[Ÿ±Çbs1a'Ÿ±Çbs1hpositionŸ±Çbs1a'Ÿ±Ç`a]Ÿ±Ç`a[Ÿ±Ç`a:Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia0Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`jrain_dropsŸ±Ç`a[Ÿ±Çbs1a'Ÿ±Çbs1hpositionŸ±Çbs1a'Ÿ±Ç`a]Ÿ±Ç`a[Ÿ±Ç`a:Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia1Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`r                  Ÿ±Ç`asŸ±Çaoa=Ÿ±Ç`jrain_dropsŸ±Ç`a[Ÿ±Çbs1a'Ÿ±Çbs1dsizeŸ±Çbs1a'Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`blwŸ±Çaoa=Ÿ±Çbmfc0.5Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`jedgecolorsŸ±Çaoa=Ÿ±Ç`jrain_dropsŸ±Ç`a[Ÿ±Çbs1a'Ÿ±Çbs1ecolorŸ±Çbs1a'Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`r                  Ÿ±Ç`jfacecolorsŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1dnoneŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±ÇakcdefŸ±Ç`a Ÿ±ÇbnffupdateŸ±Ç`a(Ÿ±Ç`lframe_numberŸ±Ç`a)Ÿ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Çbc1x@# Get an index which we can use to re-spawn the oldest raindrop.Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`mcurrent_indexŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`lframe_numberŸ±Ç`a Ÿ±Çaoa%Ÿ±Ç`a Ÿ±Ç`gn_dropsŸ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Çbc1x6# Make all colors more transparent as time progresses.Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`jrain_dropsŸ±Ç`a[Ÿ±Çbs1a'Ÿ±Çbs1ecolorŸ±Çbs1a'Ÿ±Ç`a]Ÿ±Ç`a[Ÿ±Ç`a:Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia3Ÿ±Ç`a]Ÿ±Ç`a Ÿ±Çaoa-Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Çbmfc1.0Ÿ±Çaoa/Ÿ±ÇbnbclenŸ±Ç`a(Ÿ±Ç`jrain_dropsŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`jrain_dropsŸ±Ç`a[Ÿ±Çbs1a'Ÿ±Çbs1ecolorŸ±Çbs1a'Ÿ±Ç`a]Ÿ±Ç`a[Ÿ±Ç`a:Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia3Ÿ±Ç`a]Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`dclipŸ±Ç`a(Ÿ±Ç`jrain_dropsŸ±Ç`a[Ÿ±Çbs1a'Ÿ±Çbs1ecolorŸ±Çbs1a'Ÿ±Ç`a]Ÿ±Ç`a[Ÿ±Ç`a:Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia3Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia1Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Çbc1x# Make all circles bigger.Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`jrain_dropsŸ±Ç`a[Ÿ±Çbs1a'Ÿ±Çbs1dsizeŸ±Çbs1a'Ÿ±Ç`a]Ÿ±Ç`a Ÿ±Çaoa+Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`jrain_dropsŸ±Ç`a[Ÿ±Çbs1a'Ÿ±Çbs1fgrowthŸ±Çbs1a'Ÿ±Ç`a]Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Çbc1x?# Pick a new position for oldest rain drop, resetting its size,Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Çbc1x# color and growth factor.Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`jrain_dropsŸ±Ç`a[Ÿ±Çbs1a'Ÿ±Çbs1hpositionŸ±Çbs1a'Ÿ±Ç`a]Ÿ±Ç`a[Ÿ±Ç`mcurrent_indexŸ±Ç`a]Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`frandomŸ±Çaoa.Ÿ±Ç`guniformŸ±Ç`a(Ÿ±Çbmia0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia2Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`jrain_dropsŸ±Ç`a[Ÿ±Çbs1a'Ÿ±Çbs1dsizeŸ±Çbs1a'Ÿ±Ç`a]Ÿ±Ç`a[Ÿ±Ç`mcurrent_indexŸ±Ç`a]Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Çbmia5Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`jrain_dropsŸ±Ç`a[Ÿ±Çbs1a'Ÿ±Çbs1ecolorŸ±Çbs1a'Ÿ±Ç`a]Ÿ±Ç`a[Ÿ±Ç`mcurrent_indexŸ±Ç`a]Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`a(Ÿ±Çbmia0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia1Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`jrain_dropsŸ±Ç`a[Ÿ±Çbs1a'Ÿ±Çbs1fgrowthŸ±Çbs1a'Ÿ±Ç`a]Ÿ±Ç`a[Ÿ±Ç`mcurrent_indexŸ±Ç`a]Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`frandomŸ±Çaoa.Ÿ±Ç`guniformŸ±Ç`a(Ÿ±Çbmib50Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmic200Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Çbc1xJ# Update the scatter collection, with the new colors, sizes and positions.Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`dscatŸ±Çaoa.Ÿ±Ç`nset_edgecolorsŸ±Ç`a(Ÿ±Ç`jrain_dropsŸ±Ç`a[Ÿ±Çbs1a'Ÿ±Çbs1ecolorŸ±Çbs1a'Ÿ±Ç`a]Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`dscatŸ±Çaoa.Ÿ±Ç`iset_sizesŸ±Ç`a(Ÿ±Ç`jrain_dropsŸ±Ç`a[Ÿ±Çbs1a'Ÿ±Çbs1dsizeŸ±Çbs1a'Ÿ±Ç`a]Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`dscatŸ±Çaoa.Ÿ±Ç`kset_offsetsŸ±Ç`a(Ÿ±Ç`jrain_dropsŸ±Ç`a[Ÿ±Çbs1a'Ÿ±Çbs1hpositionŸ±Çbs1a'Ÿ±Ç`a]Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1xO# Construct the animation, using the update function as the animation director.Ÿ±Ç`a
Ÿ±Ç`ianimationŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`mFuncAnimationŸ±Ç`a(Ÿ±Ç`cfigŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`fupdateŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`hintervalŸ±Çaoa=Ÿ±Çbmib10Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`dshowŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
`dNoneˆ