ŸØÇÅŸ¥Éô∞Ÿ±Çbsdx√"""
===============================
Per-row or per-column colorbars
===============================

This example shows how to use one common colorbar for each row or column
of an image grid.
"""Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±ÇbkndfromŸ±Ç`a Ÿ±ÇbnnŸ¢ÑjmatplotlibŸ†Ñjmatplotlibe3.5.1fmodulejmatplotlibfmoduleıŸ±Ç`a Ÿ±ÇbknfimportŸ±Ç`a Ÿ±Ç`ecbookŸ±Ç`a
Ÿ±ÇbknfimportŸ±Ç`a Ÿ±ÇbnnŸ¢ÑjmatplotlibŸ†Ñjmatplotlibe3.5.1fmodulejmatplotlibfmoduleıŸ±Çbnna.Ÿ±ÇbnnfpyplotŸ±Ç`a Ÿ±ÇakbasŸ±Ç`a Ÿ±ÇbnncpltŸ±Ç`a
Ÿ±ÇbkndfromŸ±Ç`a Ÿ±Çbnnlmpl_toolkitsŸ±Çbnna.Ÿ±Çbnnjaxes_grid1Ÿ±Ç`a Ÿ±ÇbknfimportŸ±Ç`a Ÿ±Ç`hAxesGridŸ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±ÇakcdefŸ±Ç`a Ÿ±Çbnfnget_demo_imageŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`azŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`ecbookŸ±Çaoa.Ÿ±Ç`oget_sample_dataŸ±Ç`a(Ÿ±Çbs2a"Ÿ±Çbs2xaxes_grid/bivariate_normal.npyŸ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`gnp_loadŸ±Çaoa=Ÿ±ÇbkcdTrueŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Çbc1x# z is a numpy array of 15x15Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±ÇakfreturnŸ±Ç`a Ÿ±Ç`azŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`a(Ÿ±Çaoa-Ÿ±Çbmia3Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia4Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çaoa-Ÿ±Çbmia4Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia3Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±ÇakcdefŸ±Ç`a Ÿ±Çbnfpdemo_bottom_cbarŸ±Ç`a(Ÿ±Ç`cfigŸ±Ç`a)Ÿ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±ÇbsdxE"""
    A grid of 2x2 images with a colorbar for each column.
    """Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`dgridŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`hAxesGridŸ±Ç`a(Ÿ±Ç`cfigŸ±Ç`a,Ÿ±Ç`a Ÿ±Çbmic121Ÿ±Ç`a,Ÿ±Ç`b  Ÿ±Çbc1x# similar to subplot(121)Ÿ±Ç`a
Ÿ±Ç`t                    Ÿ±Ç`knrows_ncolsŸ±Çaoa=Ÿ±Ç`a(Ÿ±Çbmia2Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia2Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`t                    Ÿ±Ç`haxes_padŸ±Çaoa=Ÿ±Çbmfd0.10Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`t                    Ÿ±Ç`ishare_allŸ±Çaoa=Ÿ±ÇbkcdTrueŸ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`t                    Ÿ±Ç`jlabel_modeŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2a1Ÿ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`t                    Ÿ±Ç`mcbar_locationŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2fbottomŸ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`t                    Ÿ±Ç`icbar_modeŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2dedgeŸ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`t                    Ÿ±Ç`hcbar_padŸ±Çaoa=Ÿ±Çbmfd0.25Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`t                    Ÿ±Ç`icbar_sizeŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2b15Ÿ±Çbs2a%Ÿ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`t                    Ÿ±Ç`idirectionŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2fcolumnŸ±Çbs2a"Ÿ±Ç`a
Ÿ±Ç`t                    Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`aZŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`fextentŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`nget_demo_imageŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`ecmapsŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`a[Ÿ±Çbs2a"Ÿ±Çbs2fautumnŸ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs2a"Ÿ±Çbs2fsummerŸ±Çbs2a"Ÿ±Ç`a]Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±ÇakcforŸ±Ç`a Ÿ±Ç`aiŸ±Ç`a Ÿ±ÇbowbinŸ±Ç`a Ÿ±ÇbnberangeŸ±Ç`a(Ÿ±Çbmia4Ÿ±Ç`a)Ÿ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±Ç`bimŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`dgridŸ±Ç`a[Ÿ±Ç`aiŸ±Ç`a]Ÿ±Çaoa.Ÿ±Ç`fimshowŸ±Ç`a(Ÿ±Ç`aZŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`fextentŸ±Çaoa=Ÿ±Ç`fextentŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dcmapŸ±Çaoa=Ÿ±Ç`ecmapsŸ±Ç`a[Ÿ±Ç`aiŸ±Çaoa/Ÿ±Çaoa/Ÿ±Çbmia2Ÿ±Ç`a]Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±ÇakbifŸ±Ç`a Ÿ±Ç`aiŸ±Ç`a Ÿ±Çaoa%Ÿ±Ç`a Ÿ±Çbmia2Ÿ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`l            Ÿ±Ç`dgridŸ±Çaoa.Ÿ±Ç`icbar_axesŸ±Ç`a[Ÿ±Ç`aiŸ±Çaoa/Ÿ±Çaoa/Ÿ±Çbmia2Ÿ±Ç`a]Ÿ±Çaoa.Ÿ±Ç`hcolorbarŸ±Ç`a(Ÿ±Ç`bimŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±ÇakcforŸ±Ç`a Ÿ±Ç`ccaxŸ±Ç`a Ÿ±ÇbowbinŸ±Ç`a Ÿ±Ç`dgridŸ±Çaoa.Ÿ±Ç`icbar_axesŸ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±Ç`ccaxŸ±Çaoa.Ÿ±Ç`ltoggle_labelŸ±Ç`a(Ÿ±ÇbkcdTrueŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±Ç`ccaxŸ±Çaoa.Ÿ±Ç`daxisŸ±Ç`a[Ÿ±Ç`ccaxŸ±Çaoa.Ÿ±Ç`korientationŸ±Ç`a]Ÿ±Çaoa.Ÿ±Ç`iset_labelŸ±Ç`a(Ÿ±Çbs2a"Ÿ±Çbs2cBarŸ±Çbs2a"Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Çbc1x,# This affects all axes as share_all = True.Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`dgridŸ±Çaoa.Ÿ±Ç`haxes_llcŸ±Çaoa.Ÿ±Ç`jset_xticksŸ±Ç`a(Ÿ±Ç`a[Ÿ±Çaoa-Ÿ±Çbmia2Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia2Ÿ±Ç`a]Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`dgridŸ±Çaoa.Ÿ±Ç`haxes_llcŸ±Çaoa.Ÿ±Ç`jset_yticksŸ±Ç`a(Ÿ±Ç`a[Ÿ±Çaoa-Ÿ±Çbmia2Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia2Ÿ±Ç`a]Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±ÇakcdefŸ±Ç`a Ÿ±Çbnfodemo_right_cbarŸ±Ç`a(Ÿ±Ç`cfigŸ±Ç`a)Ÿ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±ÇbsdxD"""
    A grid of 2x2 images. Each row has its own colorbar.
    """Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`dgridŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`hAxesGridŸ±Ç`a(Ÿ±Ç`cfigŸ±Ç`a,Ÿ±Ç`a Ÿ±Çbmic122Ÿ±Ç`a,Ÿ±Ç`b  Ÿ±Çbc1x# similar to subplot(122)Ÿ±Ç`a
Ÿ±Ç`t                    Ÿ±Ç`knrows_ncolsŸ±Çaoa=Ÿ±Ç`a(Ÿ±Çbmia2Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia2Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`t                    Ÿ±Ç`haxes_padŸ±Çaoa=Ÿ±Çbmfd0.10Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`t                    Ÿ±Ç`jlabel_modeŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2a1Ÿ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`t                    Ÿ±Ç`ishare_allŸ±Çaoa=Ÿ±ÇbkcdTrueŸ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`t                    Ÿ±Ç`mcbar_locationŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2erightŸ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`t                    Ÿ±Ç`icbar_modeŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2dedgeŸ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`t                    Ÿ±Ç`icbar_sizeŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2a7Ÿ±Çbs2a%Ÿ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`t                    Ÿ±Ç`hcbar_padŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2a2Ÿ±Çbs2a%Ÿ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`t                    Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`aZŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`fextentŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`nget_demo_imageŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`ecmapsŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`a[Ÿ±Çbs2a"Ÿ±Çbs2fspringŸ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs2a"Ÿ±Çbs2fwinterŸ±Çbs2a"Ÿ±Ç`a]Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±ÇakcforŸ±Ç`a Ÿ±Ç`aiŸ±Ç`a Ÿ±ÇbowbinŸ±Ç`a Ÿ±ÇbnberangeŸ±Ç`a(Ÿ±Çbmia4Ÿ±Ç`a)Ÿ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±Ç`bimŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`dgridŸ±Ç`a[Ÿ±Ç`aiŸ±Ç`a]Ÿ±Çaoa.Ÿ±Ç`fimshowŸ±Ç`a(Ÿ±Ç`aZŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`fextentŸ±Çaoa=Ÿ±Ç`fextentŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dcmapŸ±Çaoa=Ÿ±Ç`ecmapsŸ±Ç`a[Ÿ±Ç`aiŸ±Çaoa/Ÿ±Çaoa/Ÿ±Çbmia2Ÿ±Ç`a]Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±ÇakbifŸ±Ç`a Ÿ±Ç`aiŸ±Ç`a Ÿ±Çaoa%Ÿ±Ç`a Ÿ±Çbmia2Ÿ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`l            Ÿ±Ç`dgridŸ±Çaoa.Ÿ±Ç`icbar_axesŸ±Ç`a[Ÿ±Ç`aiŸ±Çaoa/Ÿ±Çaoa/Ÿ±Çbmia2Ÿ±Ç`a]Ÿ±Çaoa.Ÿ±Ç`hcolorbarŸ±Ç`a(Ÿ±Ç`bimŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±ÇakcforŸ±Ç`a Ÿ±Ç`ccaxŸ±Ç`a Ÿ±ÇbowbinŸ±Ç`a Ÿ±Ç`dgridŸ±Çaoa.Ÿ±Ç`icbar_axesŸ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±Ç`ccaxŸ±Çaoa.Ÿ±Ç`ltoggle_labelŸ±Ç`a(Ÿ±ÇbkcdTrueŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±Ç`ccaxŸ±Çaoa.Ÿ±Ç`daxisŸ±Ç`a[Ÿ±Ç`ccaxŸ±Çaoa.Ÿ±Ç`korientationŸ±Ç`a]Ÿ±Çaoa.Ÿ±Ç`iset_labelŸ±Ç`a(Ÿ±Çbs1a'Ÿ±Çbs1cFooŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Çbc1x8# This affects all axes because we set share_all = True.Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`dgridŸ±Çaoa.Ÿ±Ç`haxes_llcŸ±Çaoa.Ÿ±Ç`jset_xticksŸ±Ç`a(Ÿ±Ç`a[Ÿ±Çaoa-Ÿ±Çbmia2Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia2Ÿ±Ç`a]Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`dgridŸ±Çaoa.Ÿ±Ç`haxes_llcŸ±Çaoa.Ÿ±Ç`jset_yticksŸ±Ç`a(Ÿ±Ç`a[Ÿ±Çaoa-Ÿ±Çbmia2Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia2Ÿ±Ç`a]Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`cfigŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`ffigureŸ±Ç`a(Ÿ±Ç`gfigsizeŸ±Çaoa=Ÿ±Ç`a(Ÿ±Çbmfc5.5Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfc2.5Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cfigŸ±Çaoa.Ÿ±Ç`osubplots_adjustŸ±Ç`a(Ÿ±Ç`dleftŸ±Çaoa=Ÿ±Çbmfd0.05Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`erightŸ±Çaoa=Ÿ±Çbmfd0.93Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`pdemo_bottom_cbarŸ±Ç`a(Ÿ±Ç`cfigŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`odemo_right_cbarŸ±Ç`a(Ÿ±Ç`cfigŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`dshowŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
`dNoneˆ