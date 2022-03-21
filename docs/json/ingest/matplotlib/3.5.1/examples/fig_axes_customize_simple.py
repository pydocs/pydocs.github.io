ŸØÇÅŸ¥Éò›Ÿ±Çbsdxì"""
=========================
Fig Axes Customize Simple
=========================

Customize the background, labels and ticks of a simple plot.
"""Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±ÇbknfimportŸ±Ç`a Ÿ±ÇbnnŸ¢ÑjmatplotlibŸ†Ñjmatplotlibe3.5.1fmodulejmatplotlibfmoduleıŸ±Çbnna.Ÿ±ÇbnnfpyplotŸ±Ç`a Ÿ±ÇakbasŸ±Ç`a Ÿ±ÇbnncpltŸ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1xO###############################################################################Ÿ±Ç`a
Ÿ±Çbc1xA# `.pyplot.figure` creates a `matplotlib.figure.Figure` instance.Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`cfigŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`ffigureŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`drectŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cfigŸ±Çaoa.Ÿ±Ç`epatchŸ±Ç`b  Ÿ±Çbc1v# a rectangle instanceŸ±Ç`a
Ÿ±Ç`drectŸ±Çaoa.Ÿ±Ç`mset_facecolorŸ±Ç`a(Ÿ±Çbs1a'Ÿ±Çbs1tlightgoldenrodyellowŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`cax1Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cfigŸ±Çaoa.Ÿ±Ç`hadd_axesŸ±Ç`a(Ÿ±Ç`a[Ÿ±Çbmfc0.1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfc0.3Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfc0.4Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfc0.4Ÿ±Ç`a]Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`drectŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cax1Ÿ±Çaoa.Ÿ±Ç`epatchŸ±Ç`a
Ÿ±Ç`drectŸ±Çaoa.Ÿ±Ç`mset_facecolorŸ±Ç`a(Ÿ±Çbs1a'Ÿ±Çbs1nlightslategrayŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±ÇakcforŸ±Ç`a Ÿ±Ç`elabelŸ±Ç`a Ÿ±ÇbowbinŸ±Ç`a Ÿ±Ç`cax1Ÿ±Çaoa.Ÿ±Ç`exaxisŸ±Çaoa.Ÿ±Ç`nget_ticklabelsŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Çbc1x# label is a Text instanceŸ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`elabelŸ±Çaoa.Ÿ±Ç`iset_colorŸ±Ç`a(Ÿ±Çbs1a'Ÿ±Çbs1gtab:redŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`elabelŸ±Çaoa.Ÿ±Ç`lset_rotationŸ±Ç`a(Ÿ±Çbmib45Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`elabelŸ±Çaoa.Ÿ±Ç`lset_fontsizeŸ±Ç`a(Ÿ±Çbmib16Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±ÇakcforŸ±Ç`a Ÿ±Ç`dlineŸ±Ç`a Ÿ±ÇbowbinŸ±Ç`a Ÿ±Ç`cax1Ÿ±Çaoa.Ÿ±Ç`eyaxisŸ±Çaoa.Ÿ±Ç`mget_ticklinesŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Çbc1x# line is a Line2D instanceŸ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`dlineŸ±Çaoa.Ÿ±Ç`iset_colorŸ±Ç`a(Ÿ±Çbs1a'Ÿ±Çbs1itab:greenŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`dlineŸ±Çaoa.Ÿ±Ç`nset_markersizeŸ±Ç`a(Ÿ±Çbmib25Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`dlineŸ±Çaoa.Ÿ±Ç`sset_markeredgewidthŸ±Ç`a(Ÿ±Çbmia3Ÿ±Ç`a)Ÿ±Ç`a
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
Ÿ±Çbc1x,#    - `matplotlib.axis.Axis.get_ticklabels`Ÿ±Ç`a
Ÿ±Çbc1x+#    - `matplotlib.axis.Axis.get_ticklines`Ÿ±Ç`a
Ÿ±Çbc1x*#    - `matplotlib.text.Text.set_rotation`Ÿ±Ç`a
Ÿ±Çbc1x*#    - `matplotlib.text.Text.set_fontsize`Ÿ±Ç`a
Ÿ±Çbc1x'#    - `matplotlib.text.Text.set_color`Ÿ±Ç`a
Ÿ±Çbc1x #    - `matplotlib.lines.Line2D`Ÿ±Ç`a
Ÿ±Çbc1x*#    - `matplotlib.lines.Line2D.set_color`Ÿ±Ç`a
Ÿ±Çbc1x/#    - `matplotlib.lines.Line2D.set_markersize`Ÿ±Ç`a
Ÿ±Çbc1x4#    - `matplotlib.lines.Line2D.set_markeredgewidth`Ÿ±Ç`a
Ÿ±Çbc1x/#    - `matplotlib.patches.Patch.set_facecolor`Ÿ±Ç`a
`dNoneˆ