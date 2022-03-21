ŸØÇÅŸ¥Éô=Ÿ±Çbsdy("""
===================
Inset Locator Demo2
===================

This Demo shows how to create a zoomed inset via `.zoomed_inset_axes`.
In the first subplot an `.AnchoredSizeBar` shows the zoom effect.
In the second subplot a connection to the region of interest is
created via `.mark_inset`.
"""Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±ÇbkndfromŸ±Ç`a Ÿ±ÇbnnŸ¢ÑjmatplotlibŸ†Ñjmatplotlibe3.5.1fmodulejmatplotlibfmoduleıŸ±Ç`a Ÿ±ÇbknfimportŸ±Ç`a Ÿ±Ç`ecbookŸ±Ç`a
Ÿ±ÇbknfimportŸ±Ç`a Ÿ±ÇbnnŸ¢ÑjmatplotlibŸ†Ñjmatplotlibe3.5.1fmodulejmatplotlibfmoduleıŸ±Çbnna.Ÿ±ÇbnnfpyplotŸ±Ç`a Ÿ±ÇakbasŸ±Ç`a Ÿ±ÇbnncpltŸ±Ç`a
Ÿ±ÇbkndfromŸ±Ç`a Ÿ±Çbnnlmpl_toolkitsŸ±Çbnna.Ÿ±Çbnnjaxes_grid1Ÿ±Çbnna.Ÿ±Çbnnminset_locatorŸ±Ç`a Ÿ±ÇbknfimportŸ±Ç`a Ÿ±Ç`qzoomed_inset_axesŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`jmark_insetŸ±Ç`a
Ÿ±ÇbkndfromŸ±Ç`a Ÿ±Çbnnlmpl_toolkitsŸ±Çbnna.Ÿ±Çbnnjaxes_grid1Ÿ±Çbnna.Ÿ±Çbnnpanchored_artistsŸ±Ç`a Ÿ±ÇbknfimportŸ±Ç`a Ÿ±Ç`oAnchoredSizeBarŸ±Ç`a
Ÿ±Ç`a
Ÿ±ÇbknfimportŸ±Ç`a Ÿ±ÇbnnŸ¢ÑenumpyŸ†Ñenumpyf1.22.3fmoduleenumpyfmoduleıŸ±Ç`a Ÿ±ÇakbasŸ±Ç`a Ÿ±ÇbnnbnpŸ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±ÇakcdefŸ±Ç`a Ÿ±Çbnfnget_demo_imageŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`azŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`ecbookŸ±Çaoa.Ÿ±Ç`oget_sample_dataŸ±Ç`a(Ÿ±Çbs2a"Ÿ±Çbs2xaxes_grid/bivariate_normal.npyŸ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`gnp_loadŸ±Çaoa=Ÿ±ÇbkcdTrueŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Çbc1x# z is a numpy array of 15x15Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±ÇakfreturnŸ±Ç`a Ÿ±Ç`azŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`a(Ÿ±Çaoa-Ÿ±Çbmia3Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia4Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çaoa-Ÿ±Çbmia4Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia3Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`cfigŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`a(Ÿ±Ç`baxŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`cax2Ÿ±Ç`a)Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`hsubplotsŸ±Ç`a(Ÿ±Ç`encolsŸ±Çaoa=Ÿ±Çbmia2Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`gfigsizeŸ±Çaoa=Ÿ±Ç`a[Ÿ±Çbmia6Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia3Ÿ±Ç`a]Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1x2# First subplot, showing an inset with a size bar.Ÿ±Ç`a
Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`jset_aspectŸ±Ç`a(Ÿ±Çbmia1Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`eaxinsŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`qzoomed_inset_axesŸ±Ç`a(Ÿ±Ç`baxŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dzoomŸ±Çaoa=Ÿ±Çbmfc0.5Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`clocŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1kupper rightŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Çbc1x+# fix the number of ticks on the inset axesŸ±Ç`a
Ÿ±Ç`eaxinsŸ±Çaoa.Ÿ±Ç`eyaxisŸ±Çaoa.Ÿ±Ç`qget_major_locatorŸ±Ç`a(Ÿ±Ç`a)Ÿ±Çaoa.Ÿ±Ç`jset_paramsŸ±Ç`a(Ÿ±Ç`enbinsŸ±Çaoa=Ÿ±Çbmia7Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`eaxinsŸ±Çaoa.Ÿ±Ç`exaxisŸ±Çaoa.Ÿ±Ç`qget_major_locatorŸ±Ç`a(Ÿ±Ç`a)Ÿ±Çaoa.Ÿ±Ç`jset_paramsŸ±Ç`a(Ÿ±Ç`enbinsŸ±Çaoa=Ÿ±Çbmia7Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`eaxinsŸ±Çaoa.Ÿ±Ç`ktick_paramsŸ±Ç`a(Ÿ±Ç`ilabelleftŸ±Çaoa=Ÿ±ÇbkceFalseŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`klabelbottomŸ±Çaoa=Ÿ±ÇbkceFalseŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±ÇakcdefŸ±Ç`a Ÿ±Çbnfkadd_sizebarŸ±Ç`a(Ÿ±Ç`baxŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dsizeŸ±Ç`a)Ÿ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`casbŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`oAnchoredSizeBarŸ±Ç`a(Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`itransDataŸ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`x                          Ÿ±Ç`dsizeŸ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`x                          Ÿ±ÇbnbcstrŸ±Ç`a(Ÿ±Ç`dsizeŸ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`x                          Ÿ±Ç`clocŸ±Çaoa=Ÿ±Çbmia8Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`x                          Ÿ±Ç`cpadŸ±Çaoa=Ÿ±Çbmfc0.1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`iborderpadŸ±Çaoa=Ÿ±Çbmfc0.5Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`csepŸ±Çaoa=Ÿ±Çbmia5Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`x                          Ÿ±Ç`gframeonŸ±Çaoa=Ÿ±ÇbkceFalseŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`jadd_artistŸ±Ç`a(Ÿ±Ç`casbŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`kadd_sizebarŸ±Ç`a(Ÿ±Ç`baxŸ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfc0.5Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`kadd_sizebarŸ±Ç`a(Ÿ±Ç`eaxinsŸ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfc0.5Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1x5# Second subplot, showing an image with an inset zoomŸ±Ç`a
Ÿ±Çbc1t# and a marked insetŸ±Ç`a
Ÿ±Ç`aZŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`fextentŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`nget_demo_imageŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`bZ2Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`ezerosŸ±Ç`a(Ÿ±Ç`a(Ÿ±Çbmic150Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmic150Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`bnyŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`bnxŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`aZŸ±Çaoa.Ÿ±Ç`eshapeŸ±Ç`a
Ÿ±Ç`bZ2Ÿ±Ç`a[Ÿ±Çbmib30Ÿ±Ç`a:Ÿ±Çbmib30Ÿ±Çaoa+Ÿ±Ç`bnyŸ±Ç`a,Ÿ±Ç`a Ÿ±Çbmib30Ÿ±Ç`a:Ÿ±Çbmib30Ÿ±Çaoa+Ÿ±Ç`bnxŸ±Ç`a]Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`aZŸ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`cax2Ÿ±Çaoa.Ÿ±Ç`fimshowŸ±Ç`a(Ÿ±Ç`bZ2Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`fextentŸ±Çaoa=Ÿ±Ç`fextentŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`foriginŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2elowerŸ±Çbs2a"Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`faxins2Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`qzoomed_inset_axesŸ±Ç`a(Ÿ±Ç`cax2Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dzoomŸ±Çaoa=Ÿ±Çbmia6Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`clocŸ±Çaoa=Ÿ±Çbmia1Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`faxins2Ÿ±Çaoa.Ÿ±Ç`fimshowŸ±Ç`a(Ÿ±Ç`bZ2Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`fextentŸ±Çaoa=Ÿ±Ç`fextentŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`foriginŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2elowerŸ±Çbs2a"Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1x"# sub region of the original imageŸ±Ç`a
Ÿ±Ç`bx1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`bx2Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`by1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`by2Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Çaoa-Ÿ±Çbmfc1.5Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çaoa-Ÿ±Çbmfc0.9Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çaoa-Ÿ±Çbmfc2.5Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çaoa-Ÿ±Çbmfc1.9Ÿ±Ç`a
Ÿ±Ç`faxins2Ÿ±Çaoa.Ÿ±Ç`hset_xlimŸ±Ç`a(Ÿ±Ç`bx1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`bx2Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`faxins2Ÿ±Çaoa.Ÿ±Ç`hset_ylimŸ±Ç`a(Ÿ±Ç`by1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`by2Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Çbc1x+# fix the number of ticks on the inset axesŸ±Ç`a
Ÿ±Ç`faxins2Ÿ±Çaoa.Ÿ±Ç`eyaxisŸ±Çaoa.Ÿ±Ç`qget_major_locatorŸ±Ç`a(Ÿ±Ç`a)Ÿ±Çaoa.Ÿ±Ç`jset_paramsŸ±Ç`a(Ÿ±Ç`enbinsŸ±Çaoa=Ÿ±Çbmia7Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`faxins2Ÿ±Çaoa.Ÿ±Ç`exaxisŸ±Çaoa.Ÿ±Ç`qget_major_locatorŸ±Ç`a(Ÿ±Ç`a)Ÿ±Çaoa.Ÿ±Ç`jset_paramsŸ±Ç`a(Ÿ±Ç`enbinsŸ±Çaoa=Ÿ±Çbmia7Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`faxins2Ÿ±Çaoa.Ÿ±Ç`ktick_paramsŸ±Ç`a(Ÿ±Ç`ilabelleftŸ±Çaoa=Ÿ±ÇbkceFalseŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`klabelbottomŸ±Çaoa=Ÿ±ÇbkceFalseŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1xD# draw a bbox of the region of the inset axes in the parent axes andŸ±Ç`a
Ÿ±Çbc1x;# connecting lines between the bbox and the inset axes areaŸ±Ç`a
Ÿ±Ç`jmark_insetŸ±Ç`a(Ÿ±Ç`cax2Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`faxins2Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dloc1Ÿ±Çaoa=Ÿ±Çbmia2Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dloc2Ÿ±Çaoa=Ÿ±Çbmia4Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`bfcŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2dnoneŸ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`becŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2c0.5Ÿ±Çbs2a"Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`dshowŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
`dNoneˆ