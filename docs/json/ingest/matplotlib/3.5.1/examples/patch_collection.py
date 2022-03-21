ŸØÇÅŸ¥ÉôHŸ±Çbsdx§"""
============================
Circles, Wedges and Polygons
============================

This example demonstrates how to use `.collections.PatchCollection`.
"""Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±ÇbknfimportŸ±Ç`a Ÿ±ÇbnnŸ¢ÑenumpyŸ†Ñenumpyf1.22.3fmoduleenumpyfmoduleıŸ±Ç`a Ÿ±ÇakbasŸ±Ç`a Ÿ±ÇbnnbnpŸ±Ç`a
Ÿ±ÇbkndfromŸ±Ç`a Ÿ±ÇbnnŸ¢ÑjmatplotlibŸ†Ñjmatplotlibe3.5.1fmodulejmatplotlibfmoduleıŸ±Çbnna.Ÿ±ÇbnngpatchesŸ±Ç`a Ÿ±ÇbknfimportŸ±Ç`a Ÿ±Ç`fCircleŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`eWedgeŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`gPolygonŸ±Ç`a
Ÿ±ÇbkndfromŸ±Ç`a Ÿ±ÇbnnŸ¢ÑjmatplotlibŸ†Ñjmatplotlibe3.5.1fmodulejmatplotlibfmoduleıŸ±Çbnna.Ÿ±ÇbnnkcollectionsŸ±Ç`a Ÿ±ÇbknfimportŸ±Ç`a Ÿ±Ç`oPatchCollectionŸ±Ç`a
Ÿ±ÇbknfimportŸ±Ç`a Ÿ±ÇbnnŸ¢ÑjmatplotlibŸ†Ñjmatplotlibe3.5.1fmodulejmatplotlibfmoduleıŸ±Çbnna.Ÿ±ÇbnnfpyplotŸ±Ç`a Ÿ±ÇakbasŸ±Ç`a Ÿ±ÇbnncpltŸ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1x)# Fixing random state for reproducibilityŸ±Ç`a
Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`frandomŸ±Çaoa.Ÿ±Ç`dseedŸ±Ç`a(Ÿ±Çbmih19680801Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`cfigŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`baxŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`hsubplotsŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`jresolutionŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Çbmib50Ÿ±Ç`b  Ÿ±Çbc1x# the number of verticesŸ±Ç`a
Ÿ±Ç`aNŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Çbmia3Ÿ±Ç`a
Ÿ±Ç`axŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`frandomŸ±Çaoa.Ÿ±Ç`drandŸ±Ç`a(Ÿ±Ç`aNŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`ayŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`frandomŸ±Çaoa.Ÿ±Ç`drandŸ±Ç`a(Ÿ±Ç`aNŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`eradiiŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Çbmfc0.1Ÿ±Çaoa*Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`frandomŸ±Çaoa.Ÿ±Ç`drandŸ±Ç`a(Ÿ±Ç`aNŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`gpatchesŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`a[Ÿ±Ç`a]Ÿ±Ç`a
Ÿ±ÇakcforŸ±Ç`a Ÿ±Ç`bx1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`by1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`arŸ±Ç`a Ÿ±ÇbowbinŸ±Ç`a Ÿ±ÇbnbczipŸ±Ç`a(Ÿ±Ç`axŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ayŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`eradiiŸ±Ç`a)Ÿ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`fcircleŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`fCircleŸ±Ç`a(Ÿ±Ç`a(Ÿ±Ç`bx1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`by1Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`arŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`gpatchesŸ±Çaoa.Ÿ±Ç`fappendŸ±Ç`a(Ÿ±Ç`fcircleŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`axŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`frandomŸ±Çaoa.Ÿ±Ç`drandŸ±Ç`a(Ÿ±Ç`aNŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`ayŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`frandomŸ±Çaoa.Ÿ±Ç`drandŸ±Ç`a(Ÿ±Ç`aNŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`eradiiŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Çbmfc0.1Ÿ±Çaoa*Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`frandomŸ±Çaoa.Ÿ±Ç`drandŸ±Ç`a(Ÿ±Ç`aNŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`ftheta1Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Çbmfe360.0Ÿ±Çaoa*Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`frandomŸ±Çaoa.Ÿ±Ç`drandŸ±Ç`a(Ÿ±Ç`aNŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`ftheta2Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Çbmfe360.0Ÿ±Çaoa*Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`frandomŸ±Çaoa.Ÿ±Ç`drandŸ±Ç`a(Ÿ±Ç`aNŸ±Ç`a)Ÿ±Ç`a
Ÿ±ÇakcforŸ±Ç`a Ÿ±Ç`bx1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`by1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`arŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`bt1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`bt2Ÿ±Ç`a Ÿ±ÇbowbinŸ±Ç`a Ÿ±ÇbnbczipŸ±Ç`a(Ÿ±Ç`axŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ayŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`eradiiŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ftheta1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ftheta2Ÿ±Ç`a)Ÿ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`ewedgeŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`eWedgeŸ±Ç`a(Ÿ±Ç`a(Ÿ±Ç`bx1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`by1Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`arŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`bt1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`bt2Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`gpatchesŸ±Çaoa.Ÿ±Ç`fappendŸ±Ç`a(Ÿ±Ç`ewedgeŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1x## Some limiting conditions on WedgeŸ±Ç`a
Ÿ±Ç`gpatchesŸ±Ç`a Ÿ±Çaoa+Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`a[Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`eWedgeŸ±Ç`a(Ÿ±Ç`a(Ÿ±Çbmfb.3Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfb.7Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfb.1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmic360Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`m             Ÿ±Çbc1m# Full circleŸ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`eWedgeŸ±Ç`a(Ÿ±Ç`a(Ÿ±Çbmfb.7Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfb.8Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfb.2Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmic360Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ewidthŸ±Çaoa=Ÿ±Çbmfd0.05Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`b  Ÿ±Çbc1k# Full ringŸ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`eWedgeŸ±Ç`a(Ÿ±Ç`a(Ÿ±Çbmfb.8Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfb.3Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfb.2Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmib45Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`n              Ÿ±Çbc1m# Full sectorŸ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`eWedgeŸ±Ç`a(Ÿ±Ç`a(Ÿ±Çbmfb.8Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfb.3Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfb.2Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmib45Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmib90Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ewidthŸ±Çaoa=Ÿ±Çbmfd0.10Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`b  Ÿ±Çbc1m# Ring sectorŸ±Ç`a
Ÿ±Ç`a]Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±ÇakcforŸ±Ç`a Ÿ±Ç`aiŸ±Ç`a Ÿ±ÇbowbinŸ±Ç`a Ÿ±ÇbnberangeŸ±Ç`a(Ÿ±Ç`aNŸ±Ç`a)Ÿ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`gpolygonŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`gPolygonŸ±Ç`a(Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`frandomŸ±Çaoa.Ÿ±Ç`drandŸ±Ç`a(Ÿ±Ç`aNŸ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia2Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±ÇbkcdTrueŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`gpatchesŸ±Çaoa.Ÿ±Ç`fappendŸ±Ç`a(Ÿ±Ç`gpolygonŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`fcolorsŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Çbmic100Ÿ±Ç`a Ÿ±Çaoa*Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`frandomŸ±Çaoa.Ÿ±Ç`drandŸ±Ç`a(Ÿ±ÇbnbclenŸ±Ç`a(Ÿ±Ç`gpatchesŸ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`apŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`oPatchCollectionŸ±Ç`a(Ÿ±Ç`gpatchesŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ealphaŸ±Çaoa=Ÿ±Çbmfc0.4Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`apŸ±Çaoa.Ÿ±Ç`iset_arrayŸ±Ç`a(Ÿ±Ç`fcolorsŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`nadd_collectionŸ±Ç`a(Ÿ±Ç`apŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cfigŸ±Çaoa.Ÿ±Ç`hcolorbarŸ±Ç`a(Ÿ±Ç`apŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`baxŸ±Çaoa=Ÿ±Ç`baxŸ±Ç`a)Ÿ±Ç`a
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
Ÿ±Çbc1x#    - `matplotlib.patches`Ÿ±Ç`a
Ÿ±Çbc1x"#    - `matplotlib.patches.Circle`Ÿ±Ç`a
Ÿ±Çbc1x!#    - `matplotlib.patches.Wedge`Ÿ±Ç`a
Ÿ±Çbc1x##    - `matplotlib.patches.Polygon`Ÿ±Ç`a
Ÿ±Çbc1x/#    - `matplotlib.collections.PatchCollection`Ÿ±Ç`a
Ÿ±Çbc1x4#    - `matplotlib.collections.Collection.set_array`Ÿ±Ç`a
Ÿ±Çbc1x,#    - `matplotlib.axes.Axes.add_collection`Ÿ±Ç`a
Ÿ±Çbc1x*#    - `matplotlib.figure.Figure.colorbar`Ÿ±Ç`a
`dNoneˆ