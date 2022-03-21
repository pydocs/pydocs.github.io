ŸØÇÅŸ¥ÉôŸ±Çbsdy#"""
==================
Ellipse Collection
==================

Drawing a collection of ellipses. While this would equally be possible using
a `~.collections.EllipseCollection` or `~.collections.PathCollection`, the use
of an `~.collections.EllipseCollection` allows for much shorter code.
"""Ÿ±Ç`a
Ÿ±ÇbknfimportŸ±Ç`a Ÿ±ÇbnnŸ¢ÑjmatplotlibŸ†Ñjmatplotlibe3.5.1fmodulejmatplotlibfmoduleıŸ±Çbnna.Ÿ±ÇbnnfpyplotŸ±Ç`a Ÿ±ÇakbasŸ±Ç`a Ÿ±ÇbnncpltŸ±Ç`a
Ÿ±ÇbknfimportŸ±Ç`a Ÿ±ÇbnnŸ¢ÑenumpyŸ†Ñenumpyf1.22.3fmoduleenumpyfmoduleıŸ±Ç`a Ÿ±ÇakbasŸ±Ç`a Ÿ±ÇbnnbnpŸ±Ç`a
Ÿ±ÇbkndfromŸ±Ç`a Ÿ±ÇbnnŸ¢ÑjmatplotlibŸ†Ñjmatplotlibe3.5.1fmodulejmatplotlibfmoduleıŸ±Çbnna.Ÿ±ÇbnnkcollectionsŸ±Ç`a Ÿ±ÇbknfimportŸ±Ç`a Ÿ±Ç`qEllipseCollectionŸ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`axŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`farangeŸ±Ç`a(Ÿ±Çbmib10Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`ayŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`farangeŸ±Ç`a(Ÿ±Çbmib15Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`aXŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`aYŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`hmeshgridŸ±Ç`a(Ÿ±Ç`axŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ayŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`bXYŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`lcolumn_stackŸ±Ç`a(Ÿ±Ç`a(Ÿ±Ç`aXŸ±Çaoa.Ÿ±Ç`eravelŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`aYŸ±Çaoa.Ÿ±Ç`eravelŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`bwwŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`aXŸ±Ç`a Ÿ±Çaoa/Ÿ±Ç`a Ÿ±Çbmfd10.0Ÿ±Ç`a
Ÿ±Ç`bhhŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`aYŸ±Ç`a Ÿ±Çaoa/Ÿ±Ç`a Ÿ±Çbmfd15.0Ÿ±Ç`a
Ÿ±Ç`baaŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`aXŸ±Ç`a Ÿ±Çaoa*Ÿ±Ç`a Ÿ±Çbmia9Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`cfigŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`baxŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`hsubplotsŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`becŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`qEllipseCollectionŸ±Ç`a(Ÿ±Ç`bwwŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`bhhŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`baaŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`eunitsŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1axŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`goffsetsŸ±Çaoa=Ÿ±Ç`bXYŸ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`w                       Ÿ±Ç`ktransOffsetŸ±Çaoa=Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`itransDataŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`becŸ±Çaoa.Ÿ±Ç`iset_arrayŸ±Ç`a(Ÿ±Ç`a(Ÿ±Ç`aXŸ±Ç`a Ÿ±Çaoa+Ÿ±Ç`a Ÿ±Ç`aYŸ±Ç`a)Ÿ±Çaoa.Ÿ±Ç`eravelŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`nadd_collectionŸ±Ç`a(Ÿ±Ç`becŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`nautoscale_viewŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`jset_xlabelŸ±Ç`a(Ÿ±Çbs1a'Ÿ±Çbs1aXŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`jset_ylabelŸ±Ç`a(Ÿ±Çbs1a'Ÿ±Çbs1ayŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`dcbarŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`hcolorbarŸ±Ç`a(Ÿ±Ç`becŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`dcbarŸ±Çaoa.Ÿ±Ç`iset_labelŸ±Ç`a(Ÿ±Çbs1a'Ÿ±Çbs1cX+YŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`dshowŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1xM#############################################################################Ÿ±Ç`a
Ÿ±Çbc1a#Ÿ±Ç`a
Ÿ±Çbc1x# .. admonition:: ReferencesŸ±Ç`a
Ÿ±Çbc1a#Ÿ±Ç`a
Ÿ±Çbc1xN#    The use of the following functions, methods, classes and modules is shownŸ±Ç`a
Ÿ±Çbc1u#    in this example:Ÿ±Ç`a
Ÿ±Çbc1a#Ÿ±Ç`a
Ÿ±Çbc1x#    - `matplotlib.collections`Ÿ±Ç`a
Ÿ±Çbc1x1#    - `matplotlib.collections.EllipseCollection`Ÿ±Ç`a
Ÿ±Çbc1x,#    - `matplotlib.axes.Axes.add_collection`Ÿ±Ç`a
Ÿ±Çbc1x,#    - `matplotlib.axes.Axes.autoscale_view`Ÿ±Ç`a
Ÿ±Çbc1x/#    - `matplotlib.cm.ScalarMappable.set_array`Ÿ±Ç`a
`dNoneˆ