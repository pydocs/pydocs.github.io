ŸØÇÅŸ¥Éô+Ÿ±Çbsdy∫"""
========================================================
Building histograms using Rectangles and PolyCollections
========================================================

Using a path patch to draw rectangles.
The technique of using lots of Rectangle instances, or
the faster method of using PolyCollections, were implemented before we
had proper paths with moveto/lineto, closepoly etc in mpl.  Now that
we have them, we can draw collections of regularly shaped objects with
homogeneous properties more efficiently with a PathCollection. This
example makes a histogram -- it's more work to set up the vertex arrays
at the outset, but it should be much faster for large numbers of
objects.
"""Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±ÇbknfimportŸ±Ç`a Ÿ±ÇbnnŸ¢ÑenumpyŸ†Ñenumpyf1.22.3fmoduleenumpyfmoduleıŸ±Ç`a Ÿ±ÇakbasŸ±Ç`a Ÿ±ÇbnnbnpŸ±Ç`a
Ÿ±ÇbknfimportŸ±Ç`a Ÿ±ÇbnnŸ¢ÑjmatplotlibŸ†Ñjmatplotlibe3.5.1fmodulejmatplotlibfmoduleıŸ±Çbnna.Ÿ±ÇbnnfpyplotŸ±Ç`a Ÿ±ÇakbasŸ±Ç`a Ÿ±ÇbnncpltŸ±Ç`a
Ÿ±ÇbknfimportŸ±Ç`a Ÿ±ÇbnnŸ¢ÑjmatplotlibŸ†Ñjmatplotlibe3.5.1fmodulejmatplotlibfmoduleıŸ±Çbnna.Ÿ±ÇbnngpatchesŸ±Ç`a Ÿ±ÇakbasŸ±Ç`a Ÿ±ÇbnngpatchesŸ±Ç`a
Ÿ±ÇbknfimportŸ±Ç`a Ÿ±ÇbnnŸ¢ÑjmatplotlibŸ†Ñjmatplotlibe3.5.1fmodulejmatplotlibfmoduleıŸ±Çbnna.Ÿ±ÇbnndpathŸ±Ç`a Ÿ±ÇakbasŸ±Ç`a Ÿ±ÇbnndpathŸ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`cfigŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`baxŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`hsubplotsŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1x)# Fixing random state for reproducibilityŸ±Ç`a
Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`frandomŸ±Çaoa.Ÿ±Ç`dseedŸ±Ç`a(Ÿ±Çbmih19680801Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1x# histogram our data with numpyŸ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`ddataŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`frandomŸ±Çaoa.Ÿ±Ç`erandnŸ±Ç`a(Ÿ±Çbmid1000Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`anŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dbinsŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`ihistogramŸ±Ç`a(Ÿ±Ç`ddataŸ±Ç`a,Ÿ±Ç`a Ÿ±Çbmib50Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1x5# get the corners of the rectangles for the histogramŸ±Ç`a
Ÿ±Ç`dleftŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`dbinsŸ±Ç`a[Ÿ±Ç`a:Ÿ±Çaoa-Ÿ±Çbmia1Ÿ±Ç`a]Ÿ±Ç`a
Ÿ±Ç`erightŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`dbinsŸ±Ç`a[Ÿ±Çbmia1Ÿ±Ç`a:Ÿ±Ç`a]Ÿ±Ç`a
Ÿ±Ç`fbottomŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`ezerosŸ±Ç`a(Ÿ±ÇbnbclenŸ±Ç`a(Ÿ±Ç`dleftŸ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`ctopŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`fbottomŸ±Ç`a Ÿ±Çaoa+Ÿ±Ç`a Ÿ±Ç`anŸ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1xE# we need a (numrects x numsides x 2) numpy array for the path helperŸ±Ç`a
Ÿ±Çbc1x## function to build a compound pathŸ±Ç`a
Ÿ±Ç`bXYŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`earrayŸ±Ç`a(Ÿ±Ç`a[Ÿ±Ç`a[Ÿ±Ç`dleftŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dleftŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`erightŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`erightŸ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`a[Ÿ±Ç`fbottomŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ctopŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ctopŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`fbottomŸ±Ç`a]Ÿ±Ç`a]Ÿ±Ç`a)Ÿ±Çaoa.Ÿ±Ç`aTŸ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1u# get the Path objectŸ±Ç`a
Ÿ±Ç`gbarpathŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`dpathŸ±Çaoa.Ÿ±Ç`dPathŸ±Çaoa.Ÿ±Ç`xmake_compound_path_from_polysŸ±Ç`a(Ÿ±Ç`bXYŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1x# make a patch out of itŸ±Ç`a
Ÿ±Ç`epatchŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`gpatchesŸ±Çaoa.Ÿ±Ç`iPathPatchŸ±Ç`a(Ÿ±Ç`gbarpathŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`iadd_patchŸ±Ç`a(Ÿ±Ç`epatchŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1x# update the view limitsŸ±Ç`a
Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`hset_xlimŸ±Ç`a(Ÿ±Ç`dleftŸ±Ç`a[Ÿ±Çbmia0Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`erightŸ±Ç`a[Ÿ±Çaoa-Ÿ±Çbmia1Ÿ±Ç`a]Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`hset_ylimŸ±Ç`a(Ÿ±Ç`fbottomŸ±Çaoa.Ÿ±Ç`cminŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ctopŸ±Çaoa.Ÿ±Ç`cmaxŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`dshowŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1xM#############################################################################Ÿ±Ç`a
Ÿ±Çbc1xK# It should be noted that instead of creating a three-dimensional array andŸ±Ç`a
Ÿ±Çbc1xL# using `~.path.Path.make_compound_path_from_polys`, we could as well createŸ±Ç`a
Ÿ±Çbc1xD# the compound path directly using vertices and codes as shown belowŸ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`fnrectsŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±ÇbnbclenŸ±Ç`a(Ÿ±Ç`dleftŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`fnvertsŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`fnrectsŸ±Çaoa*Ÿ±Ç`a(Ÿ±Çbmia1Ÿ±Çaoa+Ÿ±Çbmia3Ÿ±Çaoa+Ÿ±Çbmia1Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`evertsŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`ezerosŸ±Ç`a(Ÿ±Ç`a(Ÿ±Ç`fnvertsŸ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia2Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`ecodesŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`donesŸ±Ç`a(Ÿ±Ç`fnvertsŸ±Ç`a,Ÿ±Ç`a Ÿ±ÇbnbcintŸ±Ç`a)Ÿ±Ç`a Ÿ±Çaoa*Ÿ±Ç`a Ÿ±Ç`dpathŸ±Çaoa.Ÿ±Ç`dPathŸ±Çaoa.Ÿ±Ç`fLINETOŸ±Ç`a
Ÿ±Ç`ecodesŸ±Ç`a[Ÿ±Çbmia0Ÿ±Ç`a:Ÿ±Ç`a:Ÿ±Çbmia5Ÿ±Ç`a]Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`dpathŸ±Çaoa.Ÿ±Ç`dPathŸ±Çaoa.Ÿ±Ç`fMOVETOŸ±Ç`a
Ÿ±Ç`ecodesŸ±Ç`a[Ÿ±Çbmia4Ÿ±Ç`a:Ÿ±Ç`a:Ÿ±Çbmia5Ÿ±Ç`a]Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`dpathŸ±Çaoa.Ÿ±Ç`dPathŸ±Çaoa.Ÿ±Ç`iCLOSEPOLYŸ±Ç`a
Ÿ±Ç`evertsŸ±Ç`a[Ÿ±Çbmia0Ÿ±Ç`a:Ÿ±Ç`a:Ÿ±Çbmia5Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia0Ÿ±Ç`a]Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`dleftŸ±Ç`a
Ÿ±Ç`evertsŸ±Ç`a[Ÿ±Çbmia0Ÿ±Ç`a:Ÿ±Ç`a:Ÿ±Çbmia5Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia1Ÿ±Ç`a]Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`fbottomŸ±Ç`a
Ÿ±Ç`evertsŸ±Ç`a[Ÿ±Çbmia1Ÿ±Ç`a:Ÿ±Ç`a:Ÿ±Çbmia5Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia0Ÿ±Ç`a]Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`dleftŸ±Ç`a
Ÿ±Ç`evertsŸ±Ç`a[Ÿ±Çbmia1Ÿ±Ç`a:Ÿ±Ç`a:Ÿ±Çbmia5Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia1Ÿ±Ç`a]Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`ctopŸ±Ç`a
Ÿ±Ç`evertsŸ±Ç`a[Ÿ±Çbmia2Ÿ±Ç`a:Ÿ±Ç`a:Ÿ±Çbmia5Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia0Ÿ±Ç`a]Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`erightŸ±Ç`a
Ÿ±Ç`evertsŸ±Ç`a[Ÿ±Çbmia2Ÿ±Ç`a:Ÿ±Ç`a:Ÿ±Çbmia5Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia1Ÿ±Ç`a]Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`ctopŸ±Ç`a
Ÿ±Ç`evertsŸ±Ç`a[Ÿ±Çbmia3Ÿ±Ç`a:Ÿ±Ç`a:Ÿ±Çbmia5Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia0Ÿ±Ç`a]Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`erightŸ±Ç`a
Ÿ±Ç`evertsŸ±Ç`a[Ÿ±Çbmia3Ÿ±Ç`a:Ÿ±Ç`a:Ÿ±Çbmia5Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia1Ÿ±Ç`a]Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`fbottomŸ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`gbarpathŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`dpathŸ±Çaoa.Ÿ±Ç`dPathŸ±Ç`a(Ÿ±Ç`evertsŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ecodesŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1xM#############################################################################Ÿ±Ç`a
Ÿ±Çbc1a#Ÿ±Ç`a
Ÿ±Çbc1x# .. admonition:: ReferencesŸ±Ç`a
Ÿ±Çbc1a#Ÿ±Ç`a
Ÿ±Çbc1xN#    The use of the following functions, methods, classes and modules is shownŸ±Ç`a
Ÿ±Çbc1u#    in this example:Ÿ±Ç`a
Ÿ±Çbc1a#Ÿ±Ç`a
Ÿ±Çbc1x#    - `matplotlib.patches`Ÿ±Ç`a
Ÿ±Çbc1x%#    - `matplotlib.patches.PathPatch`Ÿ±Ç`a
Ÿ±Çbc1x#    - `matplotlib.path`Ÿ±Ç`a
Ÿ±Çbc1x#    - `matplotlib.path.Path`Ÿ±Ç`a
Ÿ±Çbc1x;#    - `matplotlib.path.Path.make_compound_path_from_polys`Ÿ±Ç`a
Ÿ±Çbc1x'#    - `matplotlib.axes.Axes.add_patch`Ÿ±Ç`a
Ÿ±Çbc1x.#    - `matplotlib.collections.PathCollection`Ÿ±Ç`a
Ÿ±Çbc1a#Ÿ±Ç`a
Ÿ±Çbc1x)#    This example shows an alternative toŸ±Ç`a
Ÿ±Çbc1a#Ÿ±Ç`a
Ÿ±Çbc1x.#    - `matplotlib.collections.PolyCollection`Ÿ±Ç`a
Ÿ±Çbc1x"#    - `matplotlib.axes.Axes.hist`Ÿ±Ç`a
`dNoneˆ