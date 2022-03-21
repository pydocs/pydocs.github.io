ŸØÇÅŸ¥ÉôQŸ±Çbsdxô"""
======================
Zoom region inset axes
======================

Example of an inset axes and a rectangle showing where the zoom is located.
"""Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±ÇbkndfromŸ±Ç`a Ÿ±ÇbnnŸ¢ÑjmatplotlibŸ†Ñjmatplotlibe3.5.1fmodulejmatplotlibfmoduleıŸ±Ç`a Ÿ±ÇbknfimportŸ±Ç`a Ÿ±Ç`ecbookŸ±Ç`a
Ÿ±ÇbknfimportŸ±Ç`a Ÿ±ÇbnnŸ¢ÑjmatplotlibŸ†Ñjmatplotlibe3.5.1fmodulejmatplotlibfmoduleıŸ±Çbnna.Ÿ±ÇbnnfpyplotŸ±Ç`a Ÿ±ÇakbasŸ±Ç`a Ÿ±ÇbnncpltŸ±Ç`a
Ÿ±ÇbknfimportŸ±Ç`a Ÿ±ÇbnnŸ¢ÑenumpyŸ†Ñenumpyf1.22.3fmoduleenumpyfmoduleıŸ±Ç`a Ÿ±ÇakbasŸ±Ç`a Ÿ±ÇbnnbnpŸ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±ÇakcdefŸ±Ç`a Ÿ±Çbnfnget_demo_imageŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`azŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`ecbookŸ±Çaoa.Ÿ±Ç`oget_sample_dataŸ±Ç`a(Ÿ±Çbs2a"Ÿ±Çbs2xaxes_grid/bivariate_normal.npyŸ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`gnp_loadŸ±Çaoa=Ÿ±ÇbkcdTrueŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Çbc1x# z is a numpy array of 15x15Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±ÇakfreturnŸ±Ç`a Ÿ±Ç`azŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`a(Ÿ±Çaoa-Ÿ±Çbmia3Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia4Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çaoa-Ÿ±Çbmia4Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia3Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`cfigŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`baxŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`hsubplotsŸ±Ç`a(Ÿ±Ç`gfigsizeŸ±Çaoa=Ÿ±Ç`a[Ÿ±Çbmia5Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia4Ÿ±Ç`a]Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1k# make dataŸ±Ç`a
Ÿ±Ç`aZŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`fextentŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`nget_demo_imageŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`bZ2Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`ezerosŸ±Ç`a(Ÿ±Ç`a(Ÿ±Çbmic150Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmic150Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`bnyŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`bnxŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`aZŸ±Çaoa.Ÿ±Ç`eshapeŸ±Ç`a
Ÿ±Ç`bZ2Ÿ±Ç`a[Ÿ±Çbmib30Ÿ±Ç`a:Ÿ±Çbmib30Ÿ±Çaoa+Ÿ±Ç`bnyŸ±Ç`a,Ÿ±Ç`a Ÿ±Çbmib30Ÿ±Ç`a:Ÿ±Çbmib30Ÿ±Çaoa+Ÿ±Ç`bnxŸ±Ç`a]Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`aZŸ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`fimshowŸ±Ç`a(Ÿ±Ç`bZ2Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`fextentŸ±Çaoa=Ÿ±Ç`fextentŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`foriginŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2elowerŸ±Çbs2a"Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1p# inset axes....Ÿ±Ç`a
Ÿ±Ç`eaxinsŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`jinset_axesŸ±Ç`a(Ÿ±Ç`a[Ÿ±Çbmfc0.5Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfc0.5Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd0.47Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd0.47Ÿ±Ç`a]Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`eaxinsŸ±Çaoa.Ÿ±Ç`fimshowŸ±Ç`a(Ÿ±Ç`bZ2Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`fextentŸ±Çaoa=Ÿ±Ç`fextentŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`foriginŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2elowerŸ±Çbs2a"Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Çbc1x"# sub region of the original imageŸ±Ç`a
Ÿ±Ç`bx1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`bx2Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`by1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`by2Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Çaoa-Ÿ±Çbmfc1.5Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çaoa-Ÿ±Çbmfc0.9Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çaoa-Ÿ±Çbmfc2.5Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çaoa-Ÿ±Çbmfc1.9Ÿ±Ç`a
Ÿ±Ç`eaxinsŸ±Çaoa.Ÿ±Ç`hset_xlimŸ±Ç`a(Ÿ±Ç`bx1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`bx2Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`eaxinsŸ±Çaoa.Ÿ±Ç`hset_ylimŸ±Ç`a(Ÿ±Ç`by1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`by2Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`eaxinsŸ±Çaoa.Ÿ±Ç`oset_xticklabelsŸ±Ç`a(Ÿ±Ç`a[Ÿ±Ç`a]Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`eaxinsŸ±Çaoa.Ÿ±Ç`oset_yticklabelsŸ±Ç`a(Ÿ±Ç`a[Ÿ±Ç`a]Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`sindicate_inset_zoomŸ±Ç`a(Ÿ±Ç`eaxinsŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`iedgecolorŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2eblackŸ±Çbs2a"Ÿ±Ç`a)Ÿ±Ç`a
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
Ÿ±Çbc1x(#    - `matplotlib.axes.Axes.inset_axes`Ÿ±Ç`a
Ÿ±Çbc1x1#    - `matplotlib.axes.Axes.indicate_inset_zoom`Ÿ±Ç`a
Ÿ±Çbc1x$#    - `matplotlib.axes.Axes.imshow`Ÿ±Ç`a
`dNoneˆ