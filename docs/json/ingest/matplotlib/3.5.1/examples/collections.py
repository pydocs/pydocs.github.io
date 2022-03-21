ŸØÇÅŸ¥Éô{Ÿ±Çbsdy"""
=========================================================
Line, Poly and RegularPoly Collection with autoscaling
=========================================================

For the first two subplots, we will use spirals.  Their size will be set in
plot units, not data units.  Their positions will be set in data units by using
the *offsets* and *transOffset* keyword arguments of the `.LineCollection` and
`.PolyCollection`.

The third subplot will make regular polygons, with the same
type of scaling and positioning as in the first two.

The last subplot illustrates the use of "offsets=(xo, yo)",
that is, a single tuple instead of a list of tuples, to generate
successively offset curves, with the offset given in data
units.  This behavior is available only for the LineCollection.
"""Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±ÇbknfimportŸ±Ç`a Ÿ±ÇbnnŸ¢ÑjmatplotlibŸ†Ñjmatplotlibe3.5.1fmodulejmatplotlibfmoduleıŸ±Çbnna.Ÿ±ÇbnnfpyplotŸ±Ç`a Ÿ±ÇakbasŸ±Ç`a Ÿ±ÇbnncpltŸ±Ç`a
Ÿ±ÇbkndfromŸ±Ç`a Ÿ±ÇbnnŸ¢ÑjmatplotlibŸ†Ñjmatplotlibe3.5.1fmodulejmatplotlibfmoduleıŸ±Ç`a Ÿ±ÇbknfimportŸ±Ç`a Ÿ±Ç`kcollectionsŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`fcolorsŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`jtransformsŸ±Ç`a
Ÿ±ÇbknfimportŸ±Ç`a Ÿ±ÇbnnŸ¢ÑenumpyŸ†Ñenumpyf1.22.3fmoduleenumpyfmoduleıŸ±Ç`a Ÿ±ÇakbasŸ±Ç`a Ÿ±ÇbnnbnpŸ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`fnvertsŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Çbmib50Ÿ±Ç`a
Ÿ±Ç`dnptsŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Çbmic100Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1s# Make some spiralsŸ±Ç`a
Ÿ±Ç`arŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`farangeŸ±Ç`a(Ÿ±Ç`fnvertsŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`ethetaŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`hlinspaceŸ±Ç`a(Ÿ±Çbmia0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia2Ÿ±Çaoa*Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`bpiŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`fnvertsŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`bxxŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`arŸ±Ç`a Ÿ±Çaoa*Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`csinŸ±Ç`a(Ÿ±Ç`ethetaŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`byyŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`arŸ±Ç`a Ÿ±Çaoa*Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`ccosŸ±Ç`a(Ÿ±Ç`ethetaŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`fspiralŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`lcolumn_stackŸ±Ç`a(Ÿ±Ç`a[Ÿ±Ç`bxxŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`byyŸ±Ç`a]Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1x)# Fixing random state for reproducibilityŸ±Ç`a
Ÿ±Ç`brsŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`frandomŸ±Çaoa.Ÿ±Ç`kRandomStateŸ±Ç`a(Ÿ±Çbmih19680801Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1s# Make some offsetsŸ±Ç`a
Ÿ±Ç`cxyoŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`brsŸ±Çaoa.Ÿ±Ç`erandnŸ±Ç`a(Ÿ±Ç`dnptsŸ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia2Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1x;# Make a list of colors cycling through the default series.Ÿ±Ç`a
Ÿ±Ç`fcolorsŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`a[Ÿ±Ç`fcolorsŸ±Çaoa.Ÿ±Ç`gto_rgbaŸ±Ç`a(Ÿ±Ç`acŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`j          Ÿ±ÇakcforŸ±Ç`a Ÿ±Ç`acŸ±Ç`a Ÿ±ÇbowbinŸ±Ç`a Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`hrcParamsŸ±Ç`a[Ÿ±Çbs1a'Ÿ±Çbs1oaxes.prop_cycleŸ±Çbs1a'Ÿ±Ç`a]Ÿ±Çaoa.Ÿ±Ç`fby_keyŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a[Ÿ±Çbs1a'Ÿ±Çbs1ecolorŸ±Çbs1a'Ÿ±Ç`a]Ÿ±Ç`a]Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`cfigŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`a(Ÿ±Ç`a(Ÿ±Ç`cax1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`cax2Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`a(Ÿ±Ç`cax3Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`cax4Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`hsubplotsŸ±Ç`a(Ÿ±Çbmia2Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia2Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cfigŸ±Çaoa.Ÿ±Ç`osubplots_adjustŸ±Ç`a(Ÿ±Ç`ctopŸ±Çaoa=Ÿ±Çbmfd0.92Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dleftŸ±Çaoa=Ÿ±Çbmfd0.07Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`erightŸ±Çaoa=Ÿ±Çbmfd0.97Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`t                    Ÿ±Ç`fhspaceŸ±Çaoa=Ÿ±Çbmfc0.3Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`fwspaceŸ±Çaoa=Ÿ±Çbmfc0.3Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`ccolŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`kcollectionsŸ±Çaoa.Ÿ±Ç`nLineCollectionŸ±Ç`a(Ÿ±Ç`a[Ÿ±Ç`fspiralŸ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`goffsetsŸ±Çaoa=Ÿ±Ç`cxyoŸ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`x!                                 Ÿ±Ç`ktransOffsetŸ±Çaoa=Ÿ±Ç`cax1Ÿ±Çaoa.Ÿ±Ç`itransDataŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`etransŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cfigŸ±Çaoa.Ÿ±Ç`odpi_scale_transŸ±Ç`a Ÿ±Çaoa+Ÿ±Ç`a Ÿ±Ç`jtransformsŸ±Çaoa.Ÿ±Ç`hAffine2DŸ±Ç`a(Ÿ±Ç`a)Ÿ±Çaoa.Ÿ±Ç`escaleŸ±Ç`a(Ÿ±Çbmfc1.0Ÿ±Çaoa/Ÿ±Çbmfd72.0Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`ccolŸ±Çaoa.Ÿ±Ç`mset_transformŸ±Ç`a(Ÿ±Ç`etransŸ±Ç`a)Ÿ±Ç`b  Ÿ±Çbc1x # the points to pixels transformŸ±Ç`a
Ÿ±Çbc1x8# Note: the first argument to the collection initializerŸ±Ç`a
Ÿ±Çbc1x<# must be a list of sequences of (x, y) tuples; we have onlyŸ±Ç`a
Ÿ±Çbc1x6# one sequence, but we still have to put it in a list.Ÿ±Ç`a
Ÿ±Ç`cax1Ÿ±Çaoa.Ÿ±Ç`nadd_collectionŸ±Ç`a(Ÿ±Ç`ccolŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`gautolimŸ±Çaoa=Ÿ±ÇbkcdTrueŸ±Ç`a)Ÿ±Ç`a
Ÿ±Çbc1x9# autolim=True enables autoscaling.  For collections withŸ±Ç`a
Ÿ±Çbc1x:# offsets like this, it is neither efficient nor accurate,Ÿ±Ç`a
Ÿ±Çbc1x;# but it is good enough to generate a plot that you can useŸ±Ç`a
Ÿ±Çbc1x;# as a starting point.  If you know beforehand the range ofŸ±Ç`a
Ÿ±Çbc1x9# x and y that you want to show, it is better to set themŸ±Ç`a
Ÿ±Çbc1xL# explicitly, leave out the *autolim* keyword argument (or set it to False),Ÿ±Ç`a
Ÿ±Çbc1x1# and omit the 'ax1.autoscale_view()' call below.Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1x@# Make a transform for the line segments such that their size isŸ±Ç`a
Ÿ±Çbc1r# given in points:Ÿ±Ç`a
Ÿ±Ç`ccolŸ±Çaoa.Ÿ±Ç`iset_colorŸ±Ç`a(Ÿ±Ç`fcolorsŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`cax1Ÿ±Çaoa.Ÿ±Ç`nautoscale_viewŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`b  Ÿ±Çbc1x.# See comment above, after ax1.add_collection.Ÿ±Ç`a
Ÿ±Ç`cax1Ÿ±Çaoa.Ÿ±Ç`iset_titleŸ±Ç`a(Ÿ±Çbs1a'Ÿ±Çbs1xLineCollection using offsetsŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1x.# The same data as above, but fill the curves.Ÿ±Ç`a
Ÿ±Ç`ccolŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`kcollectionsŸ±Çaoa.Ÿ±Ç`nPolyCollectionŸ±Ç`a(Ÿ±Ç`a[Ÿ±Ç`fspiralŸ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`goffsetsŸ±Çaoa=Ÿ±Ç`cxyoŸ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`x!                                 Ÿ±Ç`ktransOffsetŸ±Çaoa=Ÿ±Ç`cax2Ÿ±Çaoa.Ÿ±Ç`itransDataŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`etransŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`jtransformsŸ±Çaoa.Ÿ±Ç`hAffine2DŸ±Ç`a(Ÿ±Ç`a)Ÿ±Çaoa.Ÿ±Ç`escaleŸ±Ç`a(Ÿ±Ç`cfigŸ±Çaoa.Ÿ±Ç`cdpiŸ±Çaoa/Ÿ±Çbmfd72.0Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`ccolŸ±Çaoa.Ÿ±Ç`mset_transformŸ±Ç`a(Ÿ±Ç`etransŸ±Ç`a)Ÿ±Ç`b  Ÿ±Çbc1x # the points to pixels transformŸ±Ç`a
Ÿ±Ç`cax2Ÿ±Çaoa.Ÿ±Ç`nadd_collectionŸ±Ç`a(Ÿ±Ç`ccolŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`gautolimŸ±Çaoa=Ÿ±ÇbkcdTrueŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`ccolŸ±Çaoa.Ÿ±Ç`iset_colorŸ±Ç`a(Ÿ±Ç`fcolorsŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`cax2Ÿ±Çaoa.Ÿ±Ç`nautoscale_viewŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cax2Ÿ±Çaoa.Ÿ±Ç`iset_titleŸ±Ç`a(Ÿ±Çbs1a'Ÿ±Çbs1xPolyCollection using offsetsŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1x# 7-sided regular polygonsŸ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`ccolŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`kcollectionsŸ±Çaoa.Ÿ±Ç`uRegularPolyCollectionŸ±Ç`a(Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Çbmia7Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`esizesŸ±Çaoa=Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`cabsŸ±Ç`a(Ÿ±Ç`bxxŸ±Ç`a)Ÿ±Ç`a Ÿ±Çaoa*Ÿ±Ç`a Ÿ±Çbmfd10.0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`goffsetsŸ±Çaoa=Ÿ±Ç`cxyoŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ktransOffsetŸ±Çaoa=Ÿ±Ç`cax3Ÿ±Çaoa.Ÿ±Ç`itransDataŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`etransŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`jtransformsŸ±Çaoa.Ÿ±Ç`hAffine2DŸ±Ç`a(Ÿ±Ç`a)Ÿ±Çaoa.Ÿ±Ç`escaleŸ±Ç`a(Ÿ±Ç`cfigŸ±Çaoa.Ÿ±Ç`cdpiŸ±Ç`a Ÿ±Çaoa/Ÿ±Ç`a Ÿ±Çbmfd72.0Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`ccolŸ±Çaoa.Ÿ±Ç`mset_transformŸ±Ç`a(Ÿ±Ç`etransŸ±Ç`a)Ÿ±Ç`b  Ÿ±Çbc1x # the points to pixels transformŸ±Ç`a
Ÿ±Ç`cax3Ÿ±Çaoa.Ÿ±Ç`nadd_collectionŸ±Ç`a(Ÿ±Ç`ccolŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`gautolimŸ±Çaoa=Ÿ±ÇbkcdTrueŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`ccolŸ±Çaoa.Ÿ±Ç`iset_colorŸ±Ç`a(Ÿ±Ç`fcolorsŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cax3Ÿ±Çaoa.Ÿ±Ç`nautoscale_viewŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cax3Ÿ±Çaoa.Ÿ±Ç`iset_titleŸ±Ç`a(Ÿ±Çbs1a'Ÿ±Çbs1x#RegularPolyCollection using offsetsŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1x;# Simulate a series of ocean current profiles, successivelyŸ±Ç`a
Ÿ±Çbc1x># offset by 0.1 m/s so that they form what is sometimes calledŸ±Ç`a
Ÿ±Çbc1x)# a "waterfall" plot or a "stagger" plot.Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`fnvertsŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Çbmib60Ÿ±Ç`a
Ÿ±Ç`gncurvesŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Çbmib20Ÿ±Ç`a
Ÿ±Ç`doffsŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`a(Ÿ±Çbmfc0.1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfc0.0Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`byyŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`hlinspaceŸ±Ç`a(Ÿ±Çbmia0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia2Ÿ±Çaoa*Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`bpiŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`fnvertsŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`bymŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`cmaxŸ±Ç`a(Ÿ±Ç`byyŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`bxxŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`a(Ÿ±Çbmfc0.2Ÿ±Ç`a Ÿ±Çaoa+Ÿ±Ç`a Ÿ±Ç`a(Ÿ±Ç`bymŸ±Ç`a Ÿ±Çaoa-Ÿ±Ç`a Ÿ±Ç`byyŸ±Ç`a)Ÿ±Ç`a Ÿ±Çaoa/Ÿ±Ç`a Ÿ±Ç`bymŸ±Ç`a)Ÿ±Ç`a Ÿ±Çaoa*Ÿ±Çaoa*Ÿ±Ç`a Ÿ±Çbmia2Ÿ±Ç`a Ÿ±Çaoa*Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`ccosŸ±Ç`a(Ÿ±Ç`byyŸ±Ç`a Ÿ±Çaoa-Ÿ±Ç`a Ÿ±Çbmfc0.4Ÿ±Ç`a)Ÿ±Ç`a Ÿ±Çaoa*Ÿ±Ç`a Ÿ±Çbmfc0.5Ÿ±Ç`a
Ÿ±Ç`dsegsŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`a[Ÿ±Ç`a]Ÿ±Ç`a
Ÿ±ÇakcforŸ±Ç`a Ÿ±Ç`aiŸ±Ç`a Ÿ±ÇbowbinŸ±Ç`a Ÿ±ÇbnberangeŸ±Ç`a(Ÿ±Ç`gncurvesŸ±Ç`a)Ÿ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`cxxxŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bxxŸ±Ç`a Ÿ±Çaoa+Ÿ±Ç`a Ÿ±Çbmfd0.02Ÿ±Çaoa*Ÿ±Ç`brsŸ±Çaoa.Ÿ±Ç`erandnŸ±Ç`a(Ÿ±Ç`fnvertsŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`ecurveŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`lcolumn_stackŸ±Ç`a(Ÿ±Ç`a[Ÿ±Ç`cxxxŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`byyŸ±Ç`a Ÿ±Çaoa*Ÿ±Ç`a Ÿ±Çbmic100Ÿ±Ç`a]Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`dsegsŸ±Çaoa.Ÿ±Ç`fappendŸ±Ç`a(Ÿ±Ç`ecurveŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`ccolŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`kcollectionsŸ±Çaoa.Ÿ±Ç`nLineCollectionŸ±Ç`a(Ÿ±Ç`dsegsŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`goffsetsŸ±Çaoa=Ÿ±Ç`doffsŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cax4Ÿ±Çaoa.Ÿ±Ç`nadd_collectionŸ±Ç`a(Ÿ±Ç`ccolŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`gautolimŸ±Çaoa=Ÿ±ÇbkcdTrueŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`ccolŸ±Çaoa.Ÿ±Ç`iset_colorŸ±Ç`a(Ÿ±Ç`fcolorsŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cax4Ÿ±Çaoa.Ÿ±Ç`nautoscale_viewŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cax4Ÿ±Çaoa.Ÿ±Ç`iset_titleŸ±Ç`a(Ÿ±Çbs1a'Ÿ±Çbs1wSuccessive data offsetsŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cax4Ÿ±Çaoa.Ÿ±Ç`jset_xlabelŸ±Ç`a(Ÿ±Çbs1a'Ÿ±Çbs1xZonal velocity component (m/s)Ÿ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cax4Ÿ±Çaoa.Ÿ±Ç`jset_ylabelŸ±Ç`a(Ÿ±Çbs1a'Ÿ±Çbs1iDepth (m)Ÿ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Çbc1x0# Reverse the y-axis so depth increases downwardŸ±Ç`a
Ÿ±Ç`cax4Ÿ±Çaoa.Ÿ±Ç`hset_ylimŸ±Ç`a(Ÿ±Ç`cax4Ÿ±Çaoa.Ÿ±Ç`hget_ylimŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a[Ÿ±Ç`a:Ÿ±Ç`a:Ÿ±Çaoa-Ÿ±Çbmia1Ÿ±Ç`a]Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`dshowŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1xM#############################################################################Ÿ±Ç`a
Ÿ±Çbc1a#Ÿ±Ç`a
Ÿ±Çbc1x# .. admonition:: ReferencesŸ±Ç`a
Ÿ±Çbc1a#Ÿ±Ç`a
Ÿ±Çbc1xN#    The use of the following functions, methods, classes and modules is shownŸ±Ç`a
Ÿ±Çbc1u#    in this example:Ÿ±Ç`a
Ÿ±Çbc1a#Ÿ±Ç`a
Ÿ±Çbc1x!#    - `matplotlib.figure.Figure`Ÿ±Ç`a
Ÿ±Çbc1x#    - `matplotlib.collections`Ÿ±Ç`a
Ÿ±Çbc1x.#    - `matplotlib.collections.LineCollection`Ÿ±Ç`a
Ÿ±Çbc1x5#    - `matplotlib.collections.RegularPolyCollection`Ÿ±Ç`a
Ÿ±Çbc1x,#    - `matplotlib.axes.Axes.add_collection`Ÿ±Ç`a
Ÿ±Çbc1x,#    - `matplotlib.axes.Axes.autoscale_view`Ÿ±Ç`a
Ÿ±Çbc1x'#    - `matplotlib.transforms.Affine2D`Ÿ±Ç`a
Ÿ±Çbc1x-#    - `matplotlib.transforms.Affine2D.scale`Ÿ±Ç`a
`dNoneˆ