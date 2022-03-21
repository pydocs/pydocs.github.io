ŸØÇÅŸ¥ÉôqŸ±Çbsdyx"""
==============
Infinite lines
==============

`~.axes.Axes.axvline` and `~.axes.Axes.axhline` draw infinite vertical /
horizontal lines, at given *x* / *y* positions. They are usually used to mark
special data values, e.g. in this example the center and limit values of the
sigmoid function.

`~.axes.Axes.axline` draws infinite straight lines in arbitrary directions.
"""Ÿ±Ç`a
Ÿ±ÇbknfimportŸ±Ç`a Ÿ±ÇbnnŸ¢ÑenumpyŸ†Ñenumpyf1.22.3fmoduleenumpyfmoduleıŸ±Ç`a Ÿ±ÇakbasŸ±Ç`a Ÿ±ÇbnnbnpŸ±Ç`a
Ÿ±ÇbknfimportŸ±Ç`a Ÿ±ÇbnnŸ¢ÑjmatplotlibŸ†Ñjmatplotlibe3.5.1fmodulejmatplotlibfmoduleıŸ±Çbnna.Ÿ±ÇbnnfpyplotŸ±Ç`a Ÿ±ÇakbasŸ±Ç`a Ÿ±ÇbnncpltŸ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`atŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`hlinspaceŸ±Ç`a(Ÿ±Çaoa-Ÿ±Çbmib10Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmib10Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmic100Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`csigŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Çbmia1Ÿ±Ç`a Ÿ±Çaoa/Ÿ±Ç`a Ÿ±Ç`a(Ÿ±Çbmia1Ÿ±Ç`a Ÿ±Çaoa+Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`cexpŸ±Ç`a(Ÿ±Çaoa-Ÿ±Ç`atŸ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`gaxhlineŸ±Ç`a(Ÿ±Ç`ayŸ±Çaoa=Ÿ±Çbmia0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ecolorŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2eblackŸ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ilinestyleŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2b--Ÿ±Çbs2a"Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`gaxhlineŸ±Ç`a(Ÿ±Ç`ayŸ±Çaoa=Ÿ±Çbmfc0.5Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ecolorŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2eblackŸ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ilinestyleŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2a:Ÿ±Çbs2a"Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`gaxhlineŸ±Ç`a(Ÿ±Ç`ayŸ±Çaoa=Ÿ±Çbmfc1.0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ecolorŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2eblackŸ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ilinestyleŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2b--Ÿ±Çbs2a"Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`gaxvlineŸ±Ç`a(Ÿ±Ç`ecolorŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2dgreyŸ±Çbs2a"Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`faxlineŸ±Ç`a(Ÿ±Ç`a(Ÿ±Çbmia0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfc0.5Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`eslopeŸ±Çaoa=Ÿ±Çbmfd0.25Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ecolorŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2eblackŸ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ilinestyleŸ±Çaoa=Ÿ±Ç`a(Ÿ±Çbmia0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`a(Ÿ±Çbmia5Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia5Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`dplotŸ±Ç`a(Ÿ±Ç`atŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`csigŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ilinewidthŸ±Çaoa=Ÿ±Çbmia2Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`elabelŸ±Çaoa=Ÿ±ÇbsaarŸ±Çbs2a"Ÿ±Çbs2a$Ÿ±Çbs2a\Ÿ±Çbs2ksigma(t) = Ÿ±Çbs2a\Ÿ±Çbs2dfracŸ±Çbsic{1}Ÿ±Çbs2a{Ÿ±Çbs2f1 + e^Ÿ±Çbs2a{Ÿ±Çbs2e-t}}$Ÿ±Çbs2a"Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`dxlimŸ±Ç`a(Ÿ±Çaoa-Ÿ±Çbmib10Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmib10Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`fxlabelŸ±Ç`a(Ÿ±Çbs2a"Ÿ±Çbs2atŸ±Çbs2a"Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`flegendŸ±Ç`a(Ÿ±Ç`hfontsizeŸ±Çaoa=Ÿ±Çbmib14Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`dshowŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1xN##############################################################################Ÿ±Ç`a
Ÿ±Çbc1xM# `~.axes.Axes.axline` can also be used with a ``transform`` parameter, whichŸ±Ç`a
Ÿ±Çbc1xL# applies to the point, but not to the slope. This can be useful for drawingŸ±Ç`a
Ÿ±Çbc1xF# diagonal grid lines with a fixed slope, which stay in place when theŸ±Ç`a
Ÿ±Çbc1x# plot limits are moved.Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±ÇakcforŸ±Ç`a Ÿ±Ç`cposŸ±Ç`a Ÿ±ÇbowbinŸ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`hlinspaceŸ±Ç`a(Ÿ±Çaoa-Ÿ±Çbmia2Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmib10Ÿ±Ç`a)Ÿ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`faxlineŸ±Ç`a(Ÿ±Ç`a(Ÿ±Ç`cposŸ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia0Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`eslopeŸ±Çaoa=Ÿ±Çbmfc0.5Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ecolorŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1akŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`itransformŸ±Çaoa=Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`cgcaŸ±Ç`a(Ÿ±Ç`a)Ÿ±Çaoa.Ÿ±Ç`itransAxesŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`dylimŸ±Ç`a(Ÿ±Ç`a[Ÿ±Çbmia0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia1Ÿ±Ç`a]Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`dxlimŸ±Ç`a(Ÿ±Ç`a[Ÿ±Çbmia0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia1Ÿ±Ç`a]Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`dshowŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1xM#############################################################################Ÿ±Ç`a
Ÿ±Çbc1a#Ÿ±Ç`a
Ÿ±Çbc1x# .. admonition:: ReferencesŸ±Ç`a
Ÿ±Çbc1a#Ÿ±Ç`a
Ÿ±Çbc1xN#    The use of the following functions, methods, classes and modules is shownŸ±Ç`a
Ÿ±Çbc1u#    in this example:Ÿ±Ç`a
Ÿ±Çbc1a#Ÿ±Ç`a
Ÿ±Çbc1xC#    - `matplotlib.axes.Axes.axhline` / `matplotlib.pyplot.axhline`Ÿ±Ç`a
Ÿ±Çbc1xC#    - `matplotlib.axes.Axes.axvline` / `matplotlib.pyplot.axvline`Ÿ±Ç`a
Ÿ±Çbc1xA#    - `matplotlib.axes.Axes.axline` / `matplotlib.pyplot.axline`Ÿ±Ç`a
`dNoneˆ