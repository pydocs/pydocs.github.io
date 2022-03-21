ŸØÇÅŸ¥Éò‡Ÿ±Çbsdx†"""
==================
Simple ImageGrid 2
==================

Align multiple images of different sizes using
`~mpl_toolkits.axes_grid1.axes_grid.ImageGrid`.
"""Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±ÇbkndfromŸ±Ç`a Ÿ±ÇbnnŸ¢ÑjmatplotlibŸ†Ñjmatplotlibe3.5.1fmodulejmatplotlibfmoduleıŸ±Ç`a Ÿ±ÇbknfimportŸ±Ç`a Ÿ±Ç`ecbookŸ±Ç`a
Ÿ±ÇbknfimportŸ±Ç`a Ÿ±ÇbnnŸ¢ÑjmatplotlibŸ†Ñjmatplotlibe3.5.1fmodulejmatplotlibfmoduleıŸ±Çbnna.Ÿ±ÇbnnfpyplotŸ±Ç`a Ÿ±ÇakbasŸ±Ç`a Ÿ±ÇbnncpltŸ±Ç`a
Ÿ±ÇbkndfromŸ±Ç`a Ÿ±Çbnnlmpl_toolkitsŸ±Çbnna.Ÿ±Çbnnjaxes_grid1Ÿ±Ç`a Ÿ±ÇbknfimportŸ±Ç`a Ÿ±Ç`iImageGridŸ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`cfigŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`ffigureŸ±Ç`a(Ÿ±Ç`gfigsizeŸ±Çaoa=Ÿ±Ç`a(Ÿ±Çbmfc5.5Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfc3.5Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`dgridŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`iImageGridŸ±Ç`a(Ÿ±Ç`cfigŸ±Ç`a,Ÿ±Ç`a Ÿ±Çbmic111Ÿ±Ç`a,Ÿ±Ç`b  Ÿ±Çbc1x# similar to subplot(111)Ÿ±Ç`a
Ÿ±Ç`q                 Ÿ±Ç`knrows_ncolsŸ±Çaoa=Ÿ±Ç`a(Ÿ±Çbmia1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia3Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`q                 Ÿ±Ç`haxes_padŸ±Çaoa=Ÿ±Çbmfc0.1Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`q                 Ÿ±Ç`jlabel_modeŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2aLŸ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`q                 Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1l# demo imageŸ±Ç`a
Ÿ±Ç`aZŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`ecbookŸ±Çaoa.Ÿ±Ç`oget_sample_dataŸ±Ç`a(Ÿ±Çbs2a"Ÿ±Çbs2xaxes_grid/bivariate_normal.npyŸ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`gnp_loadŸ±Çaoa=Ÿ±ÇbkcdTrueŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cim1Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`aZŸ±Ç`a
Ÿ±Ç`cim2Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`aZŸ±Ç`a[Ÿ±Ç`a:Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`a:Ÿ±Çbmib10Ÿ±Ç`a]Ÿ±Ç`a
Ÿ±Ç`cim3Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`aZŸ±Ç`a[Ÿ±Ç`a:Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmib10Ÿ±Ç`a:Ÿ±Ç`a]Ÿ±Ç`a
Ÿ±Ç`dvminŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dvmaxŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`aZŸ±Çaoa.Ÿ±Ç`cminŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`aZŸ±Çaoa.Ÿ±Ç`cmaxŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±ÇakcforŸ±Ç`a Ÿ±Ç`baxŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`bimŸ±Ç`a Ÿ±ÇbowbinŸ±Ç`a Ÿ±ÇbnbczipŸ±Ç`a(Ÿ±Ç`dgridŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`a[Ÿ±Ç`cim1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`cim2Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`cim3Ÿ±Ç`a]Ÿ±Ç`a)Ÿ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`fimshowŸ±Ç`a(Ÿ±Ç`bimŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`foriginŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2elowerŸ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dvminŸ±Çaoa=Ÿ±Ç`dvminŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dvmaxŸ±Çaoa=Ÿ±Ç`dvmaxŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`dshowŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
`dNoneˆ