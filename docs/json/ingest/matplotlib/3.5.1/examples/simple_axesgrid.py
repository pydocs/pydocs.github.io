ŸØÇÅŸ¥ÉòºŸ±Çbsdxá"""
================
Simple ImageGrid
================

Align multiple images using `~mpl_toolkits.axes_grid1.axes_grid.ImageGrid`.
"""Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±ÇbknfimportŸ±Ç`a Ÿ±ÇbnnŸ¢ÑjmatplotlibŸ†Ñjmatplotlibe3.5.1fmodulejmatplotlibfmoduleıŸ±Çbnna.Ÿ±ÇbnnfpyplotŸ±Ç`a Ÿ±ÇakbasŸ±Ç`a Ÿ±ÇbnncpltŸ±Ç`a
Ÿ±ÇbkndfromŸ±Ç`a Ÿ±Çbnnlmpl_toolkitsŸ±Çbnna.Ÿ±Çbnnjaxes_grid1Ÿ±Ç`a Ÿ±ÇbknfimportŸ±Ç`a Ÿ±Ç`iImageGridŸ±Ç`a
Ÿ±ÇbknfimportŸ±Ç`a Ÿ±ÇbnnŸ¢ÑenumpyŸ†Ñenumpyf1.22.3fmoduleenumpyfmoduleıŸ±Ç`a Ÿ±ÇakbasŸ±Ç`a Ÿ±ÇbnnbnpŸ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`cim1Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`farangeŸ±Ç`a(Ÿ±Çbmic100Ÿ±Ç`a)Ÿ±Çaoa.Ÿ±Ç`greshapeŸ±Ç`a(Ÿ±Ç`a(Ÿ±Çbmib10Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmib10Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cim2Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cim1Ÿ±Çaoa.Ÿ±Ç`aTŸ±Ç`a
Ÿ±Ç`cim3Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`fflipudŸ±Ç`a(Ÿ±Ç`cim1Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cim4Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`ffliplrŸ±Ç`a(Ÿ±Ç`cim2Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`cfigŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`ffigureŸ±Ç`a(Ÿ±Ç`gfigsizeŸ±Çaoa=Ÿ±Ç`a(Ÿ±Çbmfb4.Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfb4.Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`dgridŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`iImageGridŸ±Ç`a(Ÿ±Ç`cfigŸ±Ç`a,Ÿ±Ç`a Ÿ±Çbmic111Ÿ±Ç`a,Ÿ±Ç`b  Ÿ±Çbc1x# similar to subplot(111)Ÿ±Ç`a
Ÿ±Ç`q                 Ÿ±Ç`knrows_ncolsŸ±Çaoa=Ÿ±Ç`a(Ÿ±Çbmia2Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia2Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`b  Ÿ±Çbc1x# creates 2x2 grid of axesŸ±Ç`a
Ÿ±Ç`q                 Ÿ±Ç`haxes_padŸ±Çaoa=Ÿ±Çbmfc0.1Ÿ±Ç`a,Ÿ±Ç`b  Ÿ±Çbc1x# pad between axes in inch.Ÿ±Ç`a
Ÿ±Ç`q                 Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±ÇakcforŸ±Ç`a Ÿ±Ç`baxŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`bimŸ±Ç`a Ÿ±ÇbowbinŸ±Ç`a Ÿ±ÇbnbczipŸ±Ç`a(Ÿ±Ç`dgridŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`a[Ÿ±Ç`cim1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`cim2Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`cim3Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`cim4Ÿ±Ç`a]Ÿ±Ç`a)Ÿ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Çbc1x+# Iterating over the grid returns the Axes.Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`fimshowŸ±Ç`a(Ÿ±Ç`bimŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`dshowŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
`dNoneˆ