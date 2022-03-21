ŸØÇÅŸ¥Éô}Ÿ±Çbsdxó"""
============
Axes Divider
============

Axes divider to calculate location of axes and
create a divider for them using existing axes instances.
"""Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±ÇbkndfromŸ±Ç`a Ÿ±ÇbnnŸ¢ÑjmatplotlibŸ†Ñjmatplotlibe3.5.1fmodulejmatplotlibfmoduleıŸ±Ç`a Ÿ±ÇbknfimportŸ±Ç`a Ÿ±Ç`ecbookŸ±Ç`a
Ÿ±ÇbknfimportŸ±Ç`a Ÿ±ÇbnnŸ¢ÑjmatplotlibŸ†Ñjmatplotlibe3.5.1fmodulejmatplotlibfmoduleıŸ±Çbnna.Ÿ±ÇbnnfpyplotŸ±Ç`a Ÿ±ÇakbasŸ±Ç`a Ÿ±ÇbnncpltŸ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±ÇakcdefŸ±Ç`a Ÿ±Çbnfnget_demo_imageŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`azŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`ecbookŸ±Çaoa.Ÿ±Ç`oget_sample_dataŸ±Ç`a(Ÿ±Çbs2a"Ÿ±Çbs2xaxes_grid/bivariate_normal.npyŸ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`gnp_loadŸ±Çaoa=Ÿ±ÇbkcdTrueŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Çbc1x# z is a numpy array of 15x15Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±ÇakfreturnŸ±Ç`a Ÿ±Ç`azŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`a(Ÿ±Çaoa-Ÿ±Çbmia3Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia4Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çaoa-Ÿ±Çbmia4Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia3Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±ÇakcdefŸ±Ç`a Ÿ±Çbnfqdemo_simple_imageŸ±Ç`a(Ÿ±Ç`baxŸ±Ç`a)Ÿ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`aZŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`fextentŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`nget_demo_imageŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`bimŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`fimshowŸ±Ç`a(Ÿ±Ç`aZŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`fextentŸ±Çaoa=Ÿ±Ç`fextentŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`bcbŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`hcolorbarŸ±Ç`a(Ÿ±Ç`bimŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`bcbŸ±Çaoa.Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`eyaxisŸ±Çaoa.Ÿ±Ç`oset_tick_paramsŸ±Ç`a(Ÿ±Ç`jlabelrightŸ±Çaoa=Ÿ±ÇbkceFalseŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±ÇakcdefŸ±Ç`a Ÿ±Çbnfxdemo_locatable_axes_hardŸ±Ç`a(Ÿ±Ç`cfigŸ±Ç`a)Ÿ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±ÇbkndfromŸ±Ç`a Ÿ±Çbnnlmpl_toolkitsŸ±Çbnna.Ÿ±Çbnnjaxes_grid1Ÿ±Ç`a Ÿ±ÇbknfimportŸ±Ç`a Ÿ±Ç`nSubplotDividerŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dSizeŸ±Ç`a
Ÿ±Ç`d    Ÿ±ÇbkndfromŸ±Ç`a Ÿ±Çbnnlmpl_toolkitsŸ±Çbnna.Ÿ±Çbnnjaxes_grid1Ÿ±Çbnna.Ÿ±Çbnnhmpl_axesŸ±Ç`a Ÿ±ÇbknfimportŸ±Ç`a Ÿ±Ç`dAxesŸ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`gdividerŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`nSubplotDividerŸ±Ç`a(Ÿ±Ç`cfigŸ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia2Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia2Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia2Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`faspectŸ±Çaoa=Ÿ±ÇbkcdTrueŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Çbc1p# axes for imageŸ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`baxŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cfigŸ±Çaoa.Ÿ±Ç`hadd_axesŸ±Ç`a(Ÿ±Ç`gdividerŸ±Çaoa.Ÿ±Ç`lget_positionŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`jaxes_classŸ±Çaoa=Ÿ±Ç`dAxesŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Çbc1s# axes for colorbarŸ±Ç`a
Ÿ±Ç`d    Ÿ±Çbc1xK# (the label prevents Axes.add_axes from incorrectly believing that the twoŸ±Ç`a
Ÿ±Ç`d    Ÿ±Çbc1t# axes are the same)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`eax_cbŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cfigŸ±Çaoa.Ÿ±Ç`hadd_axesŸ±Ç`a(Ÿ±Ç`gdividerŸ±Çaoa.Ÿ±Ç`lget_positionŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`jaxes_classŸ±Çaoa=Ÿ±Ç`dAxesŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`elabelŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2bcbŸ±Çbs2a"Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`ahŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`a[Ÿ±Ç`dSizeŸ±Çaoa.Ÿ±Ç`eAxesXŸ±Ç`a(Ÿ±Ç`baxŸ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`b  Ÿ±Çbc1k# main axesŸ±Ç`a
Ÿ±Ç`i         Ÿ±Ç`dSizeŸ±Çaoa.Ÿ±Ç`eFixedŸ±Ç`a(Ÿ±Çbmfd0.05Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`b  Ÿ±Çbc1s# padding, 0.1 inchŸ±Ç`a
Ÿ±Ç`i         Ÿ±Ç`dSizeŸ±Çaoa.Ÿ±Ç`eFixedŸ±Ç`a(Ÿ±Çbmfc0.2Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`b  Ÿ±Çbc1t# colorbar, 0.3 inchŸ±Ç`a
Ÿ±Ç`i         Ÿ±Ç`a]Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`avŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`a[Ÿ±Ç`dSizeŸ±Çaoa.Ÿ±Ç`eAxesYŸ±Ç`a(Ÿ±Ç`baxŸ±Ç`a)Ÿ±Ç`a]Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`gdividerŸ±Çaoa.Ÿ±Ç`nset_horizontalŸ±Ç`a(Ÿ±Ç`ahŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`gdividerŸ±Çaoa.Ÿ±Ç`lset_verticalŸ±Ç`a(Ÿ±Ç`avŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`pset_axes_locatorŸ±Ç`a(Ÿ±Ç`gdividerŸ±Çaoa.Ÿ±Ç`knew_locatorŸ±Ç`a(Ÿ±Ç`bnxŸ±Çaoa=Ÿ±Çbmia0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`bnyŸ±Çaoa=Ÿ±Çbmia0Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`eax_cbŸ±Çaoa.Ÿ±Ç`pset_axes_locatorŸ±Ç`a(Ÿ±Ç`gdividerŸ±Çaoa.Ÿ±Ç`knew_locatorŸ±Ç`a(Ÿ±Ç`bnxŸ±Çaoa=Ÿ±Çbmia2Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`bnyŸ±Çaoa=Ÿ±Çbmia0Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`eax_cbŸ±Çaoa.Ÿ±Ç`daxisŸ±Ç`a[Ÿ±Çbs2a"Ÿ±Çbs2dleftŸ±Çbs2a"Ÿ±Ç`a]Ÿ±Çaoa.Ÿ±Ç`ftoggleŸ±Ç`a(Ÿ±ÇbnbcallŸ±Çaoa=Ÿ±ÇbkceFalseŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`eax_cbŸ±Çaoa.Ÿ±Ç`daxisŸ±Ç`a[Ÿ±Çbs2a"Ÿ±Çbs2erightŸ±Çbs2a"Ÿ±Ç`a]Ÿ±Çaoa.Ÿ±Ç`ftoggleŸ±Ç`a(Ÿ±Ç`eticksŸ±Çaoa=Ÿ±ÇbkcdTrueŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`aZŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`fextentŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`nget_demo_imageŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`bimŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`fimshowŸ±Ç`a(Ÿ±Ç`aZŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`fextentŸ±Çaoa=Ÿ±Ç`fextentŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`hcolorbarŸ±Ç`a(Ÿ±Ç`bimŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ccaxŸ±Çaoa=Ÿ±Ç`eax_cbŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`eax_cbŸ±Çaoa.Ÿ±Ç`eyaxisŸ±Çaoa.Ÿ±Ç`oset_tick_paramsŸ±Ç`a(Ÿ±Ç`jlabelrightŸ±Çaoa=Ÿ±ÇbkceFalseŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±ÇakcdefŸ±Ç`a Ÿ±Çbnfxdemo_locatable_axes_easyŸ±Ç`a(Ÿ±Ç`baxŸ±Ç`a)Ÿ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±ÇbkndfromŸ±Ç`a Ÿ±Çbnnlmpl_toolkitsŸ±Çbnna.Ÿ±Çbnnjaxes_grid1Ÿ±Ç`a Ÿ±ÇbknfimportŸ±Ç`a Ÿ±Ç`smake_axes_locatableŸ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`gdividerŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`smake_axes_locatableŸ±Ç`a(Ÿ±Ç`baxŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`eax_cbŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`gdividerŸ±Çaoa.Ÿ±Ç`nnew_horizontalŸ±Ç`a(Ÿ±Ç`dsizeŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2a5Ÿ±Çbs2a%Ÿ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`cpadŸ±Çaoa=Ÿ±Çbmfd0.05Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`cfigŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`jget_figureŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`cfigŸ±Çaoa.Ÿ±Ç`hadd_axesŸ±Ç`a(Ÿ±Ç`eax_cbŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`aZŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`fextentŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`nget_demo_imageŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`bimŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`fimshowŸ±Ç`a(Ÿ±Ç`aZŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`fextentŸ±Çaoa=Ÿ±Ç`fextentŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`hcolorbarŸ±Ç`a(Ÿ±Ç`bimŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ccaxŸ±Çaoa=Ÿ±Ç`eax_cbŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`eax_cbŸ±Çaoa.Ÿ±Ç`eyaxisŸ±Çaoa.Ÿ±Ç`jtick_rightŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`eax_cbŸ±Çaoa.Ÿ±Ç`eyaxisŸ±Çaoa.Ÿ±Ç`oset_tick_paramsŸ±Ç`a(Ÿ±Ç`jlabelrightŸ±Çaoa=Ÿ±ÇbkceFalseŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±ÇakcdefŸ±Ç`a Ÿ±Çbnfxdemo_images_side_by_sideŸ±Ç`a(Ÿ±Ç`baxŸ±Ç`a)Ÿ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±ÇbkndfromŸ±Ç`a Ÿ±Çbnnlmpl_toolkitsŸ±Çbnna.Ÿ±Çbnnjaxes_grid1Ÿ±Ç`a Ÿ±ÇbknfimportŸ±Ç`a Ÿ±Ç`smake_axes_locatableŸ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`gdividerŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`smake_axes_locatableŸ±Ç`a(Ÿ±Ç`baxŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`aZŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`fextentŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`nget_demo_imageŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`cax2Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`gdividerŸ±Çaoa.Ÿ±Ç`nnew_horizontalŸ±Ç`a(Ÿ±Ç`dsizeŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2c100Ÿ±Çbs2a%Ÿ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`cpadŸ±Çaoa=Ÿ±Çbmfd0.05Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`dfig1Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`jget_figureŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`dfig1Ÿ±Çaoa.Ÿ±Ç`hadd_axesŸ±Ç`a(Ÿ±Ç`cax2Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`fimshowŸ±Ç`a(Ÿ±Ç`aZŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`fextentŸ±Çaoa=Ÿ±Ç`fextentŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`cax2Ÿ±Çaoa.Ÿ±Ç`fimshowŸ±Ç`a(Ÿ±Ç`aZŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`fextentŸ±Çaoa=Ÿ±Ç`fextentŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`cax2Ÿ±Çaoa.Ÿ±Ç`eyaxisŸ±Çaoa.Ÿ±Ç`oset_tick_paramsŸ±Ç`a(Ÿ±Ç`ilabelleftŸ±Çaoa=Ÿ±ÇbkceFalseŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±ÇakcdefŸ±Ç`a Ÿ±ÇbnfddemoŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`cfigŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`ffigureŸ±Ç`a(Ÿ±Ç`gfigsizeŸ±Çaoa=Ÿ±Ç`a(Ÿ±Çbmia6Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia6Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Çbc1h# PLOT 1Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Çbc1x# simple image & colorbarŸ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`baxŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cfigŸ±Çaoa.Ÿ±Ç`kadd_subplotŸ±Ç`a(Ÿ±Çbmia2Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia2Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia1Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`qdemo_simple_imageŸ±Ç`a(Ÿ±Ç`baxŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Çbc1h# PLOT 2Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Çbc1xD# image and colorbar whose location is adjusted in the drawing time.Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Çbc1l# a hard wayŸ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`xdemo_locatable_axes_hardŸ±Ç`a(Ÿ±Ç`cfigŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Çbc1h# PLOT 3Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Çbc1xD# image and colorbar whose location is adjusted in the drawing time.Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Çbc1l# a easy wayŸ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`baxŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cfigŸ±Çaoa.Ÿ±Ç`kadd_subplotŸ±Ç`a(Ÿ±Çbmia2Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia2Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia3Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`xdemo_locatable_axes_easyŸ±Ç`a(Ÿ±Ç`baxŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Çbc1h# PLOT 4Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Çbc1x-# two images side by side with fixed padding.Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`baxŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cfigŸ±Çaoa.Ÿ±Ç`kadd_subplotŸ±Ç`a(Ÿ±Çbmia2Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia2Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia4Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`xdemo_images_side_by_sideŸ±Ç`a(Ÿ±Ç`baxŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`dshowŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`ddemoŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
`dNoneˆ