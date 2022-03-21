Ù¯‚Ù´ƒ™kÙ±‚bsdy"""
==================================
Showing RGB channels using RGBAxes
==================================

`~.axes_grid1.axes_rgb.RGBAxes` creates a layout of 4 Axes for displaying RGB
channels: one large Axes for the RGB image and 3 smaller Axes for the R, G, B
channels.
"""Ù±‚`a
Ù±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„enumpyÙ „enumpyf1.22.3fmoduleenumpyfmoduleõÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnnbnpÙ±‚`a
Ù±‚bkndfromÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚`a Ù±‚bknfimportÙ±‚`a Ù±‚`ecbookÙ±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnnfpyplotÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnncpltÙ±‚`a
Ù±‚bkndfromÙ±‚`a Ù±‚bnnlmpl_toolkitsÙ±‚bnna.Ù±‚bnnjaxes_grid1Ù±‚bnna.Ù±‚bnnhaxes_rgbÙ±‚`a Ù±‚bknfimportÙ±‚`a Ù±‚`mmake_rgb_axesÙ±‚`a,Ù±‚`a Ù±‚`gRGBAxesÙ±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚akcdefÙ±‚`a Ù±‚bnfgget_rgbÙ±‚`a(Ù±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`d    Ù±‚`aZÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`ecbookÙ±‚aoa.Ù±‚`oget_sample_dataÙ±‚`a(Ù±‚bs2a"Ù±‚bs2xaxes_grid/bivariate_normal.npyÙ±‚bs2a"Ù±‚`a,Ù±‚`a Ù±‚`gnp_loadÙ±‚aoa=Ù±‚bkcdTrueÙ±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`aZÙ±‚`a[Ù±‚`aZÙ±‚`a Ù±‚aoa<Ù±‚`a Ù±‚bmia0Ù±‚`a]Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bmfb0.Ù±‚`a
Ù±‚`d    Ù±‚`aZÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`aZÙ±‚`a Ù±‚aoa/Ù±‚`a Ù±‚`aZÙ±‚aoa.Ù±‚`cmaxÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚`aRÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`aZÙ±‚`a[Ù±‚`a:Ù±‚bmib13Ù±‚`a,Ù±‚`a Ù±‚`a:Ù±‚bmib13Ù±‚`a]Ù±‚`a
Ù±‚`d    Ù±‚`aGÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`aZÙ±‚`a[Ù±‚bmia2Ù±‚`a:Ù±‚`a,Ù±‚`a Ù±‚bmia2Ù±‚`a:Ù±‚`a]Ù±‚`a
Ù±‚`d    Ù±‚`aBÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`aZÙ±‚`a[Ù±‚`a:Ù±‚bmib13Ù±‚`a,Ù±‚`a Ù±‚bmia2Ù±‚`a:Ù±‚`a]Ù±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚akfreturnÙ±‚`a Ù±‚`aRÙ±‚`a,Ù±‚`a Ù±‚`aGÙ±‚`a,Ù±‚`a Ù±‚`aBÙ±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚akcdefÙ±‚`a Ù±‚bnfimake_cubeÙ±‚`a(Ù±‚`arÙ±‚`a,Ù±‚`a Ù±‚`agÙ±‚`a,Ù±‚`a Ù±‚`abÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`d    Ù±‚`bnyÙ±‚`a,Ù±‚`a Ù±‚`bnxÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`arÙ±‚aoa.Ù±‚`eshapeÙ±‚`a
Ù±‚`d    Ù±‚`aRÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`ezerosÙ±‚`a(Ù±‚`a(Ù±‚`bnyÙ±‚`a,Ù±‚`a Ù±‚`bnxÙ±‚`a,Ù±‚`a Ù±‚bmia3Ù±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`aRÙ±‚`a[Ù±‚`a:Ù±‚`a,Ù±‚`a Ù±‚`a:Ù±‚`a,Ù±‚`a Ù±‚bmia0Ù±‚`a]Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`arÙ±‚`a
Ù±‚`d    Ù±‚`aGÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`jzeros_likeÙ±‚`a(Ù±‚`aRÙ±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`aGÙ±‚`a[Ù±‚`a:Ù±‚`a,Ù±‚`a Ù±‚`a:Ù±‚`a,Ù±‚`a Ù±‚bmia1Ù±‚`a]Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`agÙ±‚`a
Ù±‚`d    Ù±‚`aBÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`jzeros_likeÙ±‚`a(Ù±‚`aRÙ±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`aBÙ±‚`a[Ù±‚`a:Ù±‚`a,Ù±‚`a Ù±‚`a:Ù±‚`a,Ù±‚`a Ù±‚bmia2Ù±‚`a]Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`abÙ±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚`cRGBÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`aRÙ±‚`a Ù±‚aoa+Ù±‚`a Ù±‚`aGÙ±‚`a Ù±‚aoa+Ù±‚`a Ù±‚`aBÙ±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚akfreturnÙ±‚`a Ù±‚`aRÙ±‚`a,Ù±‚`a Ù±‚`aGÙ±‚`a,Ù±‚`a Ù±‚`aBÙ±‚`a,Ù±‚`a Ù±‚`cRGBÙ±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚akcdefÙ±‚`a Ù±‚bnfidemo_rgb1Ù±‚`a(Ù±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`d    Ù±‚`cfigÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cpltÙ±‚aoa.Ù±‚`ffigureÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`baxÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`gRGBAxesÙ±‚`a(Ù±‚`cfigÙ±‚`a,Ù±‚`a Ù±‚`a[Ù±‚bmfc0.1Ù±‚`a,Ù±‚`a Ù±‚bmfc0.1Ù±‚`a,Ù±‚`a Ù±‚bmfc0.8Ù±‚`a,Ù±‚`a Ù±‚bmfc0.8Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`cpadÙ±‚aoa=Ù±‚bmfc0.0Ù±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`arÙ±‚`a,Ù±‚`a Ù±‚`agÙ±‚`a,Ù±‚`a Ù±‚`abÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`gget_rgbÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`baxÙ±‚aoa.Ù±‚`jimshow_rgbÙ±‚`a(Ù±‚`arÙ±‚`a,Ù±‚`a Ù±‚`agÙ±‚`a,Ù±‚`a Ù±‚`abÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚akcdefÙ±‚`a Ù±‚bnfidemo_rgb2Ù±‚`a(Ù±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`d    Ù±‚`cfigÙ±‚`a,Ù±‚`a Ù±‚`baxÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cpltÙ±‚aoa.Ù±‚`hsubplotsÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`dax_rÙ±‚`a,Ù±‚`a Ù±‚`dax_gÙ±‚`a,Ù±‚`a Ù±‚`dax_bÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`mmake_rgb_axesÙ±‚`a(Ù±‚`baxÙ±‚`a,Ù±‚`a Ù±‚`cpadÙ±‚aoa=Ù±‚bmfd0.02Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚`arÙ±‚`a,Ù±‚`a Ù±‚`agÙ±‚`a,Ù±‚`a Ù±‚`abÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`gget_rgbÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`dim_rÙ±‚`a,Ù±‚`a Ù±‚`dim_gÙ±‚`a,Ù±‚`a Ù±‚`dim_bÙ±‚`a,Ù±‚`a Ù±‚`fim_rgbÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`imake_cubeÙ±‚`a(Ù±‚`arÙ±‚`a,Ù±‚`a Ù±‚`agÙ±‚`a,Ù±‚`a Ù±‚`abÙ±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`baxÙ±‚aoa.Ù±‚`fimshowÙ±‚`a(Ù±‚`fim_rgbÙ±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`dax_rÙ±‚aoa.Ù±‚`fimshowÙ±‚`a(Ù±‚`dim_rÙ±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`dax_gÙ±‚aoa.Ù±‚`fimshowÙ±‚`a(Ù±‚`dim_gÙ±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`dax_bÙ±‚aoa.Ù±‚`fimshowÙ±‚`a(Ù±‚`dim_bÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚akcforÙ±‚`a Ù±‚`baxÙ±‚`a Ù±‚bowbinÙ±‚`a Ù±‚`cfigÙ±‚aoa.Ù±‚`daxesÙ±‚`a:Ù±‚`a
Ù±‚`h        Ù±‚`baxÙ±‚aoa.Ù±‚`ktick_paramsÙ±‚`a(Ù±‚`daxisÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1dbothÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`idirectionÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1binÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚`baxÙ±‚aoa.Ù±‚`fspinesÙ±‚`a[Ù±‚`a:Ù±‚`a]Ù±‚aoa.Ù±‚`iset_colorÙ±‚`a(Ù±‚bs2a"Ù±‚bs2awÙ±‚bs2a"Ù±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚akcforÙ±‚`a Ù±‚`dtickÙ±‚`a Ù±‚bowbinÙ±‚`a Ù±‚`baxÙ±‚aoa.Ù±‚`exaxisÙ±‚aoa.Ù±‚`oget_major_ticksÙ±‚`a(Ù±‚`a)Ù±‚`a Ù±‚aoa+Ù±‚`a Ù±‚`baxÙ±‚aoa.Ù±‚`eyaxisÙ±‚aoa.Ù±‚`oget_major_ticksÙ±‚`a(Ù±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`l            Ù±‚`dtickÙ±‚aoa.Ù±‚`itick1lineÙ±‚aoa.Ù±‚`sset_markeredgecolorÙ±‚`a(Ù±‚bs2a"Ù±‚bs2awÙ±‚bs2a"Ù±‚`a)Ù±‚`a
Ù±‚`l            Ù±‚`dtickÙ±‚aoa.Ù±‚`itick2lineÙ±‚aoa.Ù±‚`sset_markeredgecolorÙ±‚`a(Ù±‚bs2a"Ù±‚bs2awÙ±‚bs2a"Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚`idemo_rgb1Ù±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`idemo_rgb2Ù±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`cpltÙ±‚aoa.Ù±‚`dshowÙ±‚`a(Ù±‚`a)Ù±‚`a
`dNoneö