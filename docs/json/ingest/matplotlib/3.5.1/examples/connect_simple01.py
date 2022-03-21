ŸØÇÅŸ¥Éô|Ÿ±Çbsdx """
================
Connect Simple01
================

A `.ConnectionPatch` can be used to draw a line (possibly with arrow head)
between points defined in different coordinate systems and/or axes.
"""Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±ÇbkndfromŸ±Ç`a Ÿ±ÇbnnŸ¢ÑjmatplotlibŸ†Ñjmatplotlibe3.5.1fmodulejmatplotlibfmoduleıŸ±Çbnna.Ÿ±ÇbnngpatchesŸ±Ç`a Ÿ±ÇbknfimportŸ±Ç`a Ÿ±Ç`oConnectionPatchŸ±Ç`a
Ÿ±ÇbknfimportŸ±Ç`a Ÿ±ÇbnnŸ¢ÑjmatplotlibŸ†Ñjmatplotlibe3.5.1fmodulejmatplotlibfmoduleıŸ±Çbnna.Ÿ±ÇbnnfpyplotŸ±Ç`a Ÿ±ÇakbasŸ±Ç`a Ÿ±ÇbnncpltŸ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`cfigŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`a(Ÿ±Ç`cax1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`cax2Ÿ±Ç`a)Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`hsubplotsŸ±Ç`a(Ÿ±Çbmia1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia2Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`gfigsizeŸ±Çaoa=Ÿ±Ç`a(Ÿ±Çbmia6Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia3Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1x<# Draw a simple arrow between two points in axes coordinatesŸ±Ç`a
Ÿ±Çbc1w# within a single axes.Ÿ±Ç`a
Ÿ±Ç`cxyAŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`a(Ÿ±Çbmfc0.2Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfc0.2Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cxyBŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`a(Ÿ±Çbmfc0.8Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfc0.8Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`gcoordsAŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Çbs2a"Ÿ±Çbs2ddataŸ±Çbs2a"Ÿ±Ç`a
Ÿ±Ç`gcoordsBŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Çbs2a"Ÿ±Çbs2ddataŸ±Çbs2a"Ÿ±Ç`a
Ÿ±Ç`cconŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`oConnectionPatchŸ±Ç`a(Ÿ±Ç`cxyAŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`cxyBŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`gcoordsAŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`gcoordsBŸ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`v                      Ÿ±Ç`jarrowstyleŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2c-|>Ÿ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`gshrinkAŸ±Çaoa=Ÿ±Çbmia5Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`gshrinkBŸ±Çaoa=Ÿ±Çbmia5Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`v                      Ÿ±Ç`nmutation_scaleŸ±Çaoa=Ÿ±Çbmib20Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`bfcŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2awŸ±Çbs2a"Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cax1Ÿ±Çaoa.Ÿ±Ç`dplotŸ±Ç`a(Ÿ±Ç`a[Ÿ±Ç`cxyAŸ±Ç`a[Ÿ±Çbmia0Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`cxyBŸ±Ç`a[Ÿ±Çbmia0Ÿ±Ç`a]Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`a[Ÿ±Ç`cxyAŸ±Ç`a[Ÿ±Çbmia1Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`cxyBŸ±Ç`a[Ÿ±Çbmia1Ÿ±Ç`a]Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs2a"Ÿ±Çbs2aoŸ±Çbs2a"Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cax1Ÿ±Çaoa.Ÿ±Ç`jadd_artistŸ±Ç`a(Ÿ±Ç`cconŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1x;# Draw an arrow between the same point in data coordinates,Ÿ±Ç`a
Ÿ±Çbc1x# but in different axes.Ÿ±Ç`a
Ÿ±Ç`bxyŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`a(Ÿ±Çbmfc0.3Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfc0.2Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cconŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`oConnectionPatchŸ±Ç`a(Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`cxyAŸ±Çaoa=Ÿ±Ç`bxyŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`gcoordsAŸ±Çaoa=Ÿ±Ç`cax2Ÿ±Çaoa.Ÿ±Ç`itransDataŸ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`cxyBŸ±Çaoa=Ÿ±Ç`bxyŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`gcoordsBŸ±Çaoa=Ÿ±Ç`cax1Ÿ±Çaoa.Ÿ±Ç`itransDataŸ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`jarrowstyleŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2b->Ÿ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`gshrinkBŸ±Çaoa=Ÿ±Çbmia5Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cfigŸ±Çaoa.Ÿ±Ç`jadd_artistŸ±Ç`a(Ÿ±Ç`cconŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1xK# Draw a line between the different points, defined in different coordinateŸ±Ç`a
Ÿ±Çbc1j# systems.Ÿ±Ç`a
Ÿ±Ç`cconŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`oConnectionPatchŸ±Ç`a(Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Çbc1u# in axes coordinatesŸ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`cxyAŸ±Çaoa=Ÿ±Ç`a(Ÿ±Çbmfc0.6Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfc1.0Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`gcoordsAŸ±Çaoa=Ÿ±Ç`cax2Ÿ±Çaoa.Ÿ±Ç`itransAxesŸ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Çbc1x.# x in axes coordinates, y in data coordinatesŸ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`cxyBŸ±Çaoa=Ÿ±Ç`a(Ÿ±Çbmfc0.0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfc0.2Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`gcoordsBŸ±Çaoa=Ÿ±Ç`cax2Ÿ±Çaoa.Ÿ±Ç`sget_yaxis_transformŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`jarrowstyleŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2a-Ÿ±Çbs2a"Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cax2Ÿ±Çaoa.Ÿ±Ç`jadd_artistŸ±Ç`a(Ÿ±Ç`cconŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`cax1Ÿ±Çaoa.Ÿ±Ç`hset_xlimŸ±Ç`a(Ÿ±Çbmia0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia1Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cax1Ÿ±Çaoa.Ÿ±Ç`hset_ylimŸ±Ç`a(Ÿ±Çbmia0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia1Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cax2Ÿ±Çaoa.Ÿ±Ç`hset_xlimŸ±Ç`a(Ÿ±Çbmia0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfb.5Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cax2Ÿ±Çaoa.Ÿ±Ç`hset_ylimŸ±Ç`a(Ÿ±Çbmia0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfb.5Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`dshowŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
`dNoneˆ