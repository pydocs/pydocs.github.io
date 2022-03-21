ŸØÇÅŸ¥Éô4Ÿ±Çbsdy%"""
==============================================================
Controlling the position and size of colorbars with Inset Axes
==============================================================

This example shows how to control the position, height, and width of
colorbars using `~mpl_toolkits.axes_grid1.inset_locator.inset_axes`.

Controlling the placement of the inset axes is done similarly as that of the
legend: either by providing a location option ("upper right", "best", ...), or
by providing a locator with respect to the parent bbox.

"""Ÿ±Ç`a
Ÿ±ÇbknfimportŸ±Ç`a Ÿ±ÇbnnŸ¢ÑjmatplotlibŸ†Ñjmatplotlibe3.5.1fmodulejmatplotlibfmoduleıŸ±Çbnna.Ÿ±ÇbnnfpyplotŸ±Ç`a Ÿ±ÇakbasŸ±Ç`a Ÿ±ÇbnncpltŸ±Ç`a
Ÿ±Ç`a
Ÿ±ÇbkndfromŸ±Ç`a Ÿ±Çbnnlmpl_toolkitsŸ±Çbnna.Ÿ±Çbnnjaxes_grid1Ÿ±Çbnna.Ÿ±Çbnnminset_locatorŸ±Ç`a Ÿ±ÇbknfimportŸ±Ç`a Ÿ±Ç`jinset_axesŸ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`cfigŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`a(Ÿ±Ç`cax1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`cax2Ÿ±Ç`a)Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`hsubplotsŸ±Ç`a(Ÿ±Çbmia1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia2Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`gfigsizeŸ±Çaoa=Ÿ±Ç`a[Ÿ±Çbmia6Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia3Ÿ±Ç`a]Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`faxins1Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`jinset_axesŸ±Ç`a(Ÿ±Ç`cax1Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`t                    Ÿ±Ç`ewidthŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2b50Ÿ±Çbs2a%Ÿ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`b  Ÿ±Çbc1x"# width = 50% of parent_bbox widthŸ±Ç`a
Ÿ±Ç`t                    Ÿ±Ç`fheightŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2a5Ÿ±Çbs2a%Ÿ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`b  Ÿ±Çbc1m# height : 5%Ÿ±Ç`a
Ÿ±Ç`t                    Ÿ±Ç`clocŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1kupper rightŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`cim1Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cax1Ÿ±Çaoa.Ÿ±Ç`fimshowŸ±Ç`a(Ÿ±Ç`a[Ÿ±Ç`a[Ÿ±Çbmia1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia2Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`a[Ÿ±Çbmia2Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia3Ÿ±Ç`a]Ÿ±Ç`a]Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cfigŸ±Çaoa.Ÿ±Ç`hcolorbarŸ±Ç`a(Ÿ±Ç`cim1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ccaxŸ±Çaoa=Ÿ±Ç`faxins1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`korientationŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2jhorizontalŸ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`eticksŸ±Çaoa=Ÿ±Ç`a[Ÿ±Çbmia1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia2Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia3Ÿ±Ç`a]Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`faxins1Ÿ±Çaoa.Ÿ±Ç`exaxisŸ±Çaoa.Ÿ±Ç`rset_ticks_positionŸ±Ç`a(Ÿ±Çbs2a"Ÿ±Çbs2fbottomŸ±Çbs2a"Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`eaxinsŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`jinset_axesŸ±Ç`a(Ÿ±Ç`cax2Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`s                   Ÿ±Ç`ewidthŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2a5Ÿ±Çbs2a%Ÿ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`b  Ÿ±Çbc1x!# width = 5% of parent_bbox widthŸ±Ç`a
Ÿ±Ç`s                   Ÿ±Ç`fheightŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2b50Ÿ±Çbs2a%Ÿ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`b  Ÿ±Çbc1n# height : 50%Ÿ±Ç`a
Ÿ±Ç`s                   Ÿ±Ç`clocŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1jlower leftŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`s                   Ÿ±Ç`nbbox_to_anchorŸ±Çaoa=Ÿ±Ç`a(Ÿ±Çbmfd1.05Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfb0.Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia1Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`s                   Ÿ±Ç`nbbox_transformŸ±Çaoa=Ÿ±Ç`cax2Ÿ±Çaoa.Ÿ±Ç`itransAxesŸ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`s                   Ÿ±Ç`iborderpadŸ±Çaoa=Ÿ±Çbmia0Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`s                   Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1xG# Controlling the placement of the inset axes is basically same as thatŸ±Ç`a
Ÿ±Çbc1xC# of the legend.  you may want to play with the borderpad value andŸ±Ç`a
Ÿ±Çbc1x # the bbox_to_anchor coordinate.Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`bimŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cax2Ÿ±Çaoa.Ÿ±Ç`fimshowŸ±Ç`a(Ÿ±Ç`a[Ÿ±Ç`a[Ÿ±Çbmia1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia2Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`a[Ÿ±Çbmia2Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia3Ÿ±Ç`a]Ÿ±Ç`a]Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cfigŸ±Çaoa.Ÿ±Ç`hcolorbarŸ±Ç`a(Ÿ±Ç`bimŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ccaxŸ±Çaoa=Ÿ±Ç`eaxinsŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`eticksŸ±Çaoa=Ÿ±Ç`a[Ÿ±Çbmia1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia2Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia3Ÿ±Ç`a]Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`dshowŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
`dNoneˆ