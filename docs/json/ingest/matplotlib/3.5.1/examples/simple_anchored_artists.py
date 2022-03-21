ŸØÇÅŸ¥Éô¸Ÿ±ÇbsdyZ"""
=======================
Simple Anchored Artists
=======================

This example illustrates the use of the anchored helper classes found in
:mod:`matplotlib.offsetbox` and in :mod:`mpl_toolkits.axes_grid1`.
An implementation of a similar figure, but without use of the toolkit,
can be found in :doc:`/gallery/misc/anchored_artists`.
"""Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±ÇbknfimportŸ±Ç`a Ÿ±ÇbnnŸ¢ÑjmatplotlibŸ†Ñjmatplotlibe3.5.1fmodulejmatplotlibfmoduleıŸ±Çbnna.Ÿ±ÇbnnfpyplotŸ±Ç`a Ÿ±ÇakbasŸ±Ç`a Ÿ±ÇbnncpltŸ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±ÇakcdefŸ±Ç`a Ÿ±Çbnfidraw_textŸ±Ç`a(Ÿ±Ç`baxŸ±Ç`a)Ÿ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Çbsdxn"""
    Draw two text-boxes, anchored by different corners to the upper-left
    corner of the figure.
    """Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±ÇbkndfromŸ±Ç`a Ÿ±ÇbnnŸ¢ÑjmatplotlibŸ†Ñjmatplotlibe3.5.1fmodulejmatplotlibfmoduleıŸ±Çbnna.Ÿ±ÇbnnioffsetboxŸ±Ç`a Ÿ±ÇbknfimportŸ±Ç`a Ÿ±Ç`lAnchoredTextŸ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`batŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`lAnchoredTextŸ±Ç`a(Ÿ±Çbs2a"Ÿ±Çbs2iFigure 1aŸ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`v                      Ÿ±Ç`clocŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1jupper leftŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dpropŸ±Çaoa=Ÿ±ÇbnbddictŸ±Ç`a(Ÿ±Ç`dsizeŸ±Çaoa=Ÿ±Çbmia8Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`gframeonŸ±Çaoa=Ÿ±ÇbkcdTrueŸ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`v                      Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`batŸ±Çaoa.Ÿ±Ç`epatchŸ±Çaoa.Ÿ±Ç`lset_boxstyleŸ±Ç`a(Ÿ±Çbs2a"Ÿ±Çbs2xround,pad=0.,rounding_size=0.2Ÿ±Çbs2a"Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`jadd_artistŸ±Ç`a(Ÿ±Ç`batŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`cat2Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`lAnchoredTextŸ±Ç`a(Ÿ±Çbs2a"Ÿ±Çbs2kFigure 1(b)Ÿ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`w                       Ÿ±Ç`clocŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1jlower leftŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dpropŸ±Çaoa=Ÿ±ÇbnbddictŸ±Ç`a(Ÿ±Ç`dsizeŸ±Çaoa=Ÿ±Çbmia8Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`gframeonŸ±Çaoa=Ÿ±ÇbkcdTrueŸ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`w                       Ÿ±Ç`nbbox_to_anchorŸ±Çaoa=Ÿ±Ç`a(Ÿ±Çbmfb0.Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfb1.Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`w                       Ÿ±Ç`nbbox_transformŸ±Çaoa=Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`itransAxesŸ±Ç`a
Ÿ±Ç`w                       Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`cat2Ÿ±Çaoa.Ÿ±Ç`epatchŸ±Çaoa.Ÿ±Ç`lset_boxstyleŸ±Ç`a(Ÿ±Çbs2a"Ÿ±Çbs2xround,pad=0.,rounding_size=0.2Ÿ±Çbs2a"Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`jadd_artistŸ±Ç`a(Ÿ±Ç`cat2Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±ÇakcdefŸ±Ç`a Ÿ±Çbnfkdraw_circleŸ±Ç`a(Ÿ±Ç`baxŸ±Ç`a)Ÿ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Çbsdx1"""
    Draw a circle in axis coordinates
    """Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±ÇbkndfromŸ±Ç`a Ÿ±Çbnnlmpl_toolkitsŸ±Çbnna.Ÿ±Çbnnjaxes_grid1Ÿ±Çbnna.Ÿ±Çbnnpanchored_artistsŸ±Ç`a Ÿ±ÇbknfimportŸ±Ç`a Ÿ±Ç`sAnchoredDrawingAreaŸ±Ç`a
Ÿ±Ç`d    Ÿ±ÇbkndfromŸ±Ç`a Ÿ±ÇbnnŸ¢ÑjmatplotlibŸ†Ñjmatplotlibe3.5.1fmodulejmatplotlibfmoduleıŸ±Çbnna.Ÿ±ÇbnngpatchesŸ±Ç`a Ÿ±ÇbknfimportŸ±Ç`a Ÿ±Ç`fCircleŸ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`cadaŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`sAnchoredDrawingAreaŸ±Ç`a(Ÿ±Çbmib20Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmib20Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia0Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`x                              Ÿ±Ç`clocŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1kupper rightŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`cpadŸ±Çaoa=Ÿ±Çbmfb0.Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`gframeonŸ±Çaoa=Ÿ±ÇbkceFalseŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`apŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`fCircleŸ±Ç`a(Ÿ±Ç`a(Ÿ±Çbmib10Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmib10Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmib10Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`cadaŸ±Çaoa.Ÿ±Ç`bdaŸ±Çaoa.Ÿ±Ç`jadd_artistŸ±Ç`a(Ÿ±Ç`apŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`jadd_artistŸ±Ç`a(Ÿ±Ç`cadaŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±ÇakcdefŸ±Ç`a Ÿ±Çbnfldraw_ellipseŸ±Ç`a(Ÿ±Ç`baxŸ±Ç`a)Ÿ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±ÇbsdxM"""
    Draw an ellipse of width=0.1, height=0.15 in data coordinates
    """Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±ÇbkndfromŸ±Ç`a Ÿ±Çbnnlmpl_toolkitsŸ±Çbnna.Ÿ±Çbnnjaxes_grid1Ÿ±Çbnna.Ÿ±Çbnnpanchored_artistsŸ±Ç`a Ÿ±ÇbknfimportŸ±Ç`a Ÿ±Ç`oAnchoredEllipseŸ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`baeŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`oAnchoredEllipseŸ±Ç`a(Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`itransDataŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ewidthŸ±Çaoa=Ÿ±Çbmfc0.1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`fheightŸ±Çaoa=Ÿ±Çbmfd0.15Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`eangleŸ±Çaoa=Ÿ±Çbmfb0.Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`x                         Ÿ±Ç`clocŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1jlower leftŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`cpadŸ±Çaoa=Ÿ±Çbmfc0.5Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`iborderpadŸ±Çaoa=Ÿ±Çbmfc0.4Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`x                         Ÿ±Ç`gframeonŸ±Çaoa=Ÿ±ÇbkcdTrueŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`jadd_artistŸ±Ç`a(Ÿ±Ç`baeŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±ÇakcdefŸ±Ç`a Ÿ±Çbnfldraw_sizebarŸ±Ç`a(Ÿ±Ç`baxŸ±Ç`a)Ÿ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Çbsdxp"""
    Draw a horizontal bar with length of 0.1 in data coordinates,
    with a fixed label underneath.
    """Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±ÇbkndfromŸ±Ç`a Ÿ±Çbnnlmpl_toolkitsŸ±Çbnna.Ÿ±Çbnnjaxes_grid1Ÿ±Çbnna.Ÿ±Çbnnpanchored_artistsŸ±Ç`a Ÿ±ÇbknfimportŸ±Ç`a Ÿ±Ç`oAnchoredSizeBarŸ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`casbŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`oAnchoredSizeBarŸ±Ç`a(Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`itransDataŸ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`x                          Ÿ±Çbmfc0.1Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`x                          Ÿ±ÇbsaarŸ±Çbs2a"Ÿ±Çbs2c1$^Ÿ±Çbs2a{Ÿ±Çbs2a\Ÿ±Çbs2gprime}$Ÿ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`x                          Ÿ±Ç`clocŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1llower centerŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`x                          Ÿ±Ç`cpadŸ±Çaoa=Ÿ±Çbmfc0.1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`iborderpadŸ±Çaoa=Ÿ±Çbmfc0.5Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`csepŸ±Çaoa=Ÿ±Çbmia5Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`x                          Ÿ±Ç`gframeonŸ±Çaoa=Ÿ±ÇbkceFalseŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`jadd_artistŸ±Ç`a(Ÿ±Ç`casbŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`cfigŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`baxŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`hsubplotsŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`jset_aspectŸ±Ç`a(Ÿ±Çbmfb1.Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`idraw_textŸ±Ç`a(Ÿ±Ç`baxŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`kdraw_circleŸ±Ç`a(Ÿ±Ç`baxŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`ldraw_ellipseŸ±Ç`a(Ÿ±Ç`baxŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`ldraw_sizebarŸ±Ç`a(Ÿ±Ç`baxŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`dshowŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
`dNoneˆ