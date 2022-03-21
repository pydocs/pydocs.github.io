ŸØÇÅŸ¥ÉôŸ±Çbsdyg"""
================================
Reference for Matplotlib artists
================================

This example displays several of Matplotlib's graphics primitives (artists)
drawn using matplotlib API. A full list of artists and the documentation is
available at :ref:`the artist API <artist-api>`.

Copyright (c) 2010, Bartosz Telenczuk
BSD License
"""Ÿ±Ç`a
Ÿ±ÇbknfimportŸ±Ç`a Ÿ±ÇbnnŸ¢ÑjmatplotlibŸ†Ñjmatplotlibe3.5.1fmodulejmatplotlibfmoduleıŸ±Çbnna.Ÿ±ÇbnnfpyplotŸ±Ç`a Ÿ±ÇakbasŸ±Ç`a Ÿ±ÇbnncpltŸ±Ç`a
Ÿ±ÇbknfimportŸ±Ç`a Ÿ±ÇbnnŸ¢ÑenumpyŸ†Ñenumpyf1.22.3fmoduleenumpyfmoduleıŸ±Ç`a Ÿ±ÇakbasŸ±Ç`a Ÿ±ÇbnnbnpŸ±Ç`a
Ÿ±ÇbknfimportŸ±Ç`a Ÿ±ÇbnnŸ¢ÑjmatplotlibŸ†Ñjmatplotlibe3.5.1fmodulejmatplotlibfmoduleıŸ±Çbnna.Ÿ±ÇbnndpathŸ±Ç`a Ÿ±ÇakbasŸ±Ç`a Ÿ±ÇbnnempathŸ±Ç`a
Ÿ±ÇbknfimportŸ±Ç`a Ÿ±ÇbnnŸ¢ÑjmatplotlibŸ†Ñjmatplotlibe3.5.1fmodulejmatplotlibfmoduleıŸ±Çbnna.Ÿ±ÇbnnelinesŸ±Ç`a Ÿ±ÇakbasŸ±Ç`a Ÿ±ÇbnnfmlinesŸ±Ç`a
Ÿ±ÇbknfimportŸ±Ç`a Ÿ±ÇbnnŸ¢ÑjmatplotlibŸ†Ñjmatplotlibe3.5.1fmodulejmatplotlibfmoduleıŸ±Çbnna.Ÿ±ÇbnngpatchesŸ±Ç`a Ÿ±ÇakbasŸ±Ç`a Ÿ±ÇbnnhmpatchesŸ±Ç`a
Ÿ±ÇbkndfromŸ±Ç`a Ÿ±ÇbnnŸ¢ÑjmatplotlibŸ†Ñjmatplotlibe3.5.1fmodulejmatplotlibfmoduleıŸ±Çbnna.Ÿ±ÇbnnkcollectionsŸ±Ç`a Ÿ±ÇbknfimportŸ±Ç`a Ÿ±Ç`oPatchCollectionŸ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±ÇakcdefŸ±Ç`a Ÿ±ÇbnfelabelŸ±Ç`a(Ÿ±Ç`bxyŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dtextŸ±Ç`a)Ÿ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`ayŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bxyŸ±Ç`a[Ÿ±Çbmia1Ÿ±Ç`a]Ÿ±Ç`a Ÿ±Çaoa-Ÿ±Ç`a Ÿ±Çbmfd0.15Ÿ±Ç`b  Ÿ±Çbc1x7# shift y-value for label so that it's below the artistŸ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`dtextŸ±Ç`a(Ÿ±Ç`bxyŸ±Ç`a[Ÿ±Çbmia0Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ayŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dtextŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`bhaŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2fcenterŸ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ffamilyŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1jsans-serifŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dsizeŸ±Çaoa=Ÿ±Çbmib14Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`cfigŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`baxŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`hsubplotsŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Çbc1x%# create 3x3 grid to plot the artistsŸ±Ç`a
Ÿ±Ç`dgridŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`emgridŸ±Ç`a[Ÿ±Çbmfc0.2Ÿ±Ç`a:Ÿ±Çbmfc0.8Ÿ±Ç`a:Ÿ±Çbmia3Ÿ±Ç`ajŸ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfc0.2Ÿ±Ç`a:Ÿ±Çbmfc0.8Ÿ±Ç`a:Ÿ±Çbmia3Ÿ±Ç`ajŸ±Ç`a]Ÿ±Çaoa.Ÿ±Ç`greshapeŸ±Ç`a(Ÿ±Çbmia2Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çaoa-Ÿ±Çbmia1Ÿ±Ç`a)Ÿ±Çaoa.Ÿ±Ç`aTŸ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`gpatchesŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`a[Ÿ±Ç`a]Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1n# add a circleŸ±Ç`a
Ÿ±Ç`fcircleŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`hmpatchesŸ±Çaoa.Ÿ±Ç`fCircleŸ±Ç`a(Ÿ±Ç`dgridŸ±Ç`a[Ÿ±Çbmia0Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfc0.1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`becŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2dnoneŸ±Çbs2a"Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`gpatchesŸ±Çaoa.Ÿ±Ç`fappendŸ±Ç`a(Ÿ±Ç`fcircleŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`elabelŸ±Ç`a(Ÿ±Ç`dgridŸ±Ç`a[Ÿ±Çbmia0Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs2a"Ÿ±Çbs2fCircleŸ±Çbs2a"Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1q# add a rectangleŸ±Ç`a
Ÿ±Ç`drectŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`hmpatchesŸ±Çaoa.Ÿ±Ç`iRectangleŸ±Ç`a(Ÿ±Ç`dgridŸ±Ç`a[Ÿ±Çbmia1Ÿ±Ç`a]Ÿ±Ç`a Ÿ±Çaoa-Ÿ±Ç`a Ÿ±Ç`a[Ÿ±Çbmfe0.025Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd0.05Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd0.05Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfc0.1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`becŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2dnoneŸ±Çbs2a"Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`gpatchesŸ±Çaoa.Ÿ±Ç`fappendŸ±Ç`a(Ÿ±Ç`drectŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`elabelŸ±Ç`a(Ÿ±Ç`dgridŸ±Ç`a[Ÿ±Çbmia1Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs2a"Ÿ±Çbs2iRectangleŸ±Çbs2a"Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1m# add a wedgeŸ±Ç`a
Ÿ±Ç`ewedgeŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`hmpatchesŸ±Çaoa.Ÿ±Ç`eWedgeŸ±Ç`a(Ÿ±Ç`dgridŸ±Ç`a[Ÿ±Çbmia2Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfc0.1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmib30Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmic270Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`becŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2dnoneŸ±Çbs2a"Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`gpatchesŸ±Çaoa.Ÿ±Ç`fappendŸ±Ç`a(Ÿ±Ç`ewedgeŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`elabelŸ±Ç`a(Ÿ±Ç`dgridŸ±Ç`a[Ÿ±Çbmia2Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs2a"Ÿ±Çbs2eWedgeŸ±Çbs2a"Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1o# add a PolygonŸ±Ç`a
Ÿ±Ç`gpolygonŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`hmpatchesŸ±Çaoa.Ÿ±Ç`nRegularPolygonŸ±Ç`a(Ÿ±Ç`dgridŸ±Ç`a[Ÿ±Çbmia3Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia5Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfc0.1Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`gpatchesŸ±Çaoa.Ÿ±Ç`fappendŸ±Ç`a(Ÿ±Ç`gpolygonŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`elabelŸ±Ç`a(Ÿ±Ç`dgridŸ±Ç`a[Ÿ±Çbmia3Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs2a"Ÿ±Çbs2gPolygonŸ±Çbs2a"Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1p# add an ellipseŸ±Ç`a
Ÿ±Ç`gellipseŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`hmpatchesŸ±Çaoa.Ÿ±Ç`gEllipseŸ±Ç`a(Ÿ±Ç`dgridŸ±Ç`a[Ÿ±Çbmia4Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfc0.2Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfc0.1Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`gpatchesŸ±Çaoa.Ÿ±Ç`fappendŸ±Ç`a(Ÿ±Ç`gellipseŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`elabelŸ±Ç`a(Ÿ±Ç`dgridŸ±Ç`a[Ÿ±Çbmia4Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs2a"Ÿ±Çbs2gEllipseŸ±Çbs2a"Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1n# add an arrowŸ±Ç`a
Ÿ±Ç`earrowŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`hmpatchesŸ±Çaoa.Ÿ±Ç`eArrowŸ±Ç`a(Ÿ±Ç`dgridŸ±Ç`a[Ÿ±Çbmia5Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia0Ÿ±Ç`a]Ÿ±Ç`a Ÿ±Çaoa-Ÿ±Ç`a Ÿ±Çbmfd0.05Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dgridŸ±Ç`a[Ÿ±Çbmia5Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia1Ÿ±Ç`a]Ÿ±Ç`a Ÿ±Çaoa-Ÿ±Ç`a Ÿ±Çbmfd0.05Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfc0.1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfc0.1Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`w                       Ÿ±Ç`ewidthŸ±Çaoa=Ÿ±Çbmfc0.1Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`gpatchesŸ±Çaoa.Ÿ±Ç`fappendŸ±Ç`a(Ÿ±Ç`earrowŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`elabelŸ±Ç`a(Ÿ±Ç`dgridŸ±Ç`a[Ÿ±Çbmia5Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs2a"Ÿ±Çbs2eArrowŸ±Çbs2a"Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1r# add a path patchŸ±Ç`a
Ÿ±Ç`dPathŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`empathŸ±Çaoa.Ÿ±Ç`dPathŸ±Ç`a
Ÿ±Ç`ipath_dataŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`a[Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`a(Ÿ±Ç`dPathŸ±Çaoa.Ÿ±Ç`fMOVETOŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`a[Ÿ±Çbmfe0.018Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çaoa-Ÿ±Çbmfd0.11Ÿ±Ç`a]Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`a(Ÿ±Ç`dPathŸ±Çaoa.Ÿ±Ç`fCURVE4Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`a[Ÿ±Çaoa-Ÿ±Çbmfe0.031Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çaoa-Ÿ±Çbmfe0.051Ÿ±Ç`a]Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`a(Ÿ±Ç`dPathŸ±Çaoa.Ÿ±Ç`fCURVE4Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`a[Ÿ±Çaoa-Ÿ±Çbmfe0.115Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfe0.073Ÿ±Ç`a]Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`a(Ÿ±Ç`dPathŸ±Çaoa.Ÿ±Ç`fCURVE4Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`a[Ÿ±Çaoa-Ÿ±Çbmfd0.03Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfe0.073Ÿ±Ç`a]Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`a(Ÿ±Ç`dPathŸ±Çaoa.Ÿ±Ç`fLINETOŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`a[Ÿ±Çaoa-Ÿ±Çbmfe0.011Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfe0.039Ÿ±Ç`a]Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`a(Ÿ±Ç`dPathŸ±Çaoa.Ÿ±Ç`fCURVE4Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`a[Ÿ±Çbmfe0.043Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfe0.121Ÿ±Ç`a]Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`a(Ÿ±Ç`dPathŸ±Çaoa.Ÿ±Ç`fCURVE4Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`a[Ÿ±Çbmfe0.075Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çaoa-Ÿ±Çbmfe0.005Ÿ±Ç`a]Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`a(Ÿ±Ç`dPathŸ±Çaoa.Ÿ±Ç`fCURVE4Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`a[Ÿ±Çbmfe0.035Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çaoa-Ÿ±Çbmfe0.027Ÿ±Ç`a]Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`a(Ÿ±Ç`dPathŸ±Çaoa.Ÿ±Ç`iCLOSEPOLYŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`a[Ÿ±Çbmfe0.018Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çaoa-Ÿ±Çbmfd0.11Ÿ±Ç`a]Ÿ±Ç`a)Ÿ±Ç`a]Ÿ±Ç`a
Ÿ±Ç`ecodesŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`evertsŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±ÇbnbczipŸ±Ç`a(Ÿ±Çaoa*Ÿ±Ç`ipath_dataŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`dpathŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`empathŸ±Çaoa.Ÿ±Ç`dPathŸ±Ç`a(Ÿ±Ç`evertsŸ±Ç`a Ÿ±Çaoa+Ÿ±Ç`a Ÿ±Ç`dgridŸ±Ç`a[Ÿ±Çbmia6Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ecodesŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`epatchŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`hmpatchesŸ±Çaoa.Ÿ±Ç`iPathPatchŸ±Ç`a(Ÿ±Ç`dpathŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`gpatchesŸ±Çaoa.Ÿ±Ç`fappendŸ±Ç`a(Ÿ±Ç`epatchŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`elabelŸ±Ç`a(Ÿ±Ç`dgridŸ±Ç`a[Ÿ±Çbmia6Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs2a"Ÿ±Çbs2iPathPatchŸ±Çbs2a"Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1q# add a fancy boxŸ±Ç`a
Ÿ±Ç`hfancyboxŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`hmpatchesŸ±Çaoa.Ÿ±Ç`nFancyBboxPatchŸ±Ç`a(Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`dgridŸ±Ç`a[Ÿ±Çbmia7Ÿ±Ç`a]Ÿ±Ç`a Ÿ±Çaoa-Ÿ±Ç`a Ÿ±Ç`a[Ÿ±Çbmfe0.025Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd0.05Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd0.05Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfc0.1Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`hboxstyleŸ±Çaoa=Ÿ±Ç`hmpatchesŸ±Çaoa.Ÿ±Ç`hBoxStyleŸ±Ç`a(Ÿ±Çbs2a"Ÿ±Çbs2eRoundŸ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`cpadŸ±Çaoa=Ÿ±Çbmfd0.02Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`gpatchesŸ±Çaoa.Ÿ±Ç`fappendŸ±Ç`a(Ÿ±Ç`hfancyboxŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`elabelŸ±Ç`a(Ÿ±Ç`dgridŸ±Ç`a[Ÿ±Çbmia7Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs2a"Ÿ±Çbs2nFancyBboxPatchŸ±Çbs2a"Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1l# add a lineŸ±Ç`a
Ÿ±Ç`axŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ayŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`a(Ÿ±Ç`a[Ÿ±Çaoa-Ÿ±Çbmfd0.06Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfc0.0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfc0.1Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`a[Ÿ±Çbmfd0.05Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çaoa-Ÿ±Çbmfd0.05Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd0.05Ÿ±Ç`a]Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`dlineŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`fmlinesŸ±Çaoa.Ÿ±Ç`fLine2DŸ±Ç`a(Ÿ±Ç`axŸ±Ç`a Ÿ±Çaoa+Ÿ±Ç`a Ÿ±Ç`dgridŸ±Ç`a[Ÿ±Çbmia8Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia0Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ayŸ±Ç`a Ÿ±Çaoa+Ÿ±Ç`a Ÿ±Ç`dgridŸ±Ç`a[Ÿ±Çbmia8Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia1Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`blwŸ±Çaoa=Ÿ±Çbmfb5.Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ealphaŸ±Çaoa=Ÿ±Çbmfc0.3Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`elabelŸ±Ç`a(Ÿ±Ç`dgridŸ±Ç`a[Ÿ±Çbmia8Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs2a"Ÿ±Çbs2fLine2DŸ±Çbs2a"Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`fcolorsŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`hlinspaceŸ±Ç`a(Ÿ±Çbmia0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±ÇbnbclenŸ±Ç`a(Ÿ±Ç`gpatchesŸ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`jcollectionŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`oPatchCollectionŸ±Ç`a(Ÿ±Ç`gpatchesŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dcmapŸ±Çaoa=Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`bcmŸ±Çaoa.Ÿ±Ç`chsvŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ealphaŸ±Çaoa=Ÿ±Çbmfc0.3Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`jcollectionŸ±Çaoa.Ÿ±Ç`iset_arrayŸ±Ç`a(Ÿ±Ç`fcolorsŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`nadd_collectionŸ±Ç`a(Ÿ±Ç`jcollectionŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`hadd_lineŸ±Ç`a(Ÿ±Ç`dlineŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`daxisŸ±Ç`a(Ÿ±Çbs1a'Ÿ±Çbs1eequalŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`daxisŸ±Ç`a(Ÿ±Çbs1a'Ÿ±Çbs1coffŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`ltight_layoutŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
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
Ÿ±Çbc1x#    - `matplotlib.path`Ÿ±Ç`a
Ÿ±Çbc1x#    - `matplotlib.path.Path`Ÿ±Ç`a
Ÿ±Çbc1x#    - `matplotlib.lines`Ÿ±Ç`a
Ÿ±Çbc1x #    - `matplotlib.lines.Line2D`Ÿ±Ç`a
Ÿ±Çbc1x#    - `matplotlib.patches`Ÿ±Ç`a
Ÿ±Çbc1x"#    - `matplotlib.patches.Circle`Ÿ±Ç`a
Ÿ±Çbc1x##    - `matplotlib.patches.Ellipse`Ÿ±Ç`a
Ÿ±Çbc1x!#    - `matplotlib.patches.Wedge`Ÿ±Ç`a
Ÿ±Çbc1x%#    - `matplotlib.patches.Rectangle`Ÿ±Ç`a
Ÿ±Çbc1x!#    - `matplotlib.patches.Arrow`Ÿ±Ç`a
Ÿ±Çbc1x%#    - `matplotlib.patches.PathPatch`Ÿ±Ç`a
Ÿ±Çbc1x*#    - `matplotlib.patches.FancyBboxPatch`Ÿ±Ç`a
Ÿ±Çbc1x*#    - `matplotlib.patches.RegularPolygon`Ÿ±Ç`a
Ÿ±Çbc1x#    - `matplotlib.collections`Ÿ±Ç`a
Ÿ±Çbc1x/#    - `matplotlib.collections.PatchCollection`Ÿ±Ç`a
Ÿ±Çbc1x/#    - `matplotlib.cm.ScalarMappable.set_array`Ÿ±Ç`a
Ÿ±Çbc1x,#    - `matplotlib.axes.Axes.add_collection`Ÿ±Ç`a
Ÿ±Çbc1x&#    - `matplotlib.axes.Axes.add_line`Ÿ±Ç`a
`dNoneˆ