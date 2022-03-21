ŸØÇÅŸ¥ÉôŸ±Çbsdx_"""
===========
Text Layout
===========

Create text with different alignment and rotation.
"""Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±ÇbknfimportŸ±Ç`a Ÿ±ÇbnnŸ¢ÑjmatplotlibŸ†Ñjmatplotlibe3.5.1fmodulejmatplotlibfmoduleıŸ±Çbnna.Ÿ±ÇbnnfpyplotŸ±Ç`a Ÿ±ÇakbasŸ±Ç`a Ÿ±ÇbnncpltŸ±Ç`a
Ÿ±ÇbknfimportŸ±Ç`a Ÿ±ÇbnnŸ¢ÑjmatplotlibŸ†Ñjmatplotlibe3.5.1fmodulejmatplotlibfmoduleıŸ±Çbnna.Ÿ±ÇbnngpatchesŸ±Ç`a Ÿ±ÇakbasŸ±Ç`a Ÿ±ÇbnngpatchesŸ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`cfigŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`ffigureŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`dleftŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ewidthŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Çbmfc.25Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfb.5Ÿ±Ç`a
Ÿ±Ç`fbottomŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`fheightŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Çbmfc.25Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfb.5Ÿ±Ç`a
Ÿ±Ç`erightŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`dleftŸ±Ç`a Ÿ±Çaoa+Ÿ±Ç`a Ÿ±Ç`ewidthŸ±Ç`a
Ÿ±Ç`ctopŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`fbottomŸ±Ç`a Ÿ±Çaoa+Ÿ±Ç`a Ÿ±Ç`fheightŸ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1xM# Draw a rectangle in figure coordinates ((0, 0) is bottom left and (1, 1) isŸ±Ç`a
Ÿ±Çbc1o# upper right).Ÿ±Ç`a
Ÿ±Ç`apŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`gpatchesŸ±Çaoa.Ÿ±Ç`iRectangleŸ±Ç`a(Ÿ±Ç`a(Ÿ±Ç`dleftŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`fbottomŸ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ewidthŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`fheightŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dfillŸ±Çaoa=Ÿ±ÇbkceFalseŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cfigŸ±Çaoa.Ÿ±Ç`jadd_artistŸ±Ç`a(Ÿ±Ç`apŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1xM# Figure.text (aka. plt.figtext) behaves like Axes.text (aka. plt.text), withŸ±Ç`a
Ÿ±Çbc1xO# the sole exception that the coordinates are relative to the figure ((0, 0) isŸ±Ç`a
Ÿ±Çbc1x)# bottom left and (1, 1) is upper right).Ÿ±Ç`a
Ÿ±Ç`cfigŸ±Çaoa.Ÿ±Ç`dtextŸ±Ç`a(Ÿ±Ç`dleftŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`fbottomŸ±Ç`a,Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1hleft topŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`i         Ÿ±Ç`shorizontalalignmentŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1dleftŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`qverticalalignmentŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1ctopŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cfigŸ±Çaoa.Ÿ±Ç`dtextŸ±Ç`a(Ÿ±Ç`dleftŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`fbottomŸ±Ç`a,Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1kleft bottomŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`i         Ÿ±Ç`shorizontalalignmentŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1dleftŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`qverticalalignmentŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1fbottomŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cfigŸ±Çaoa.Ÿ±Ç`dtextŸ±Ç`a(Ÿ±Ç`erightŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ctopŸ±Ç`a,Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1lright bottomŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`i         Ÿ±Ç`shorizontalalignmentŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1erightŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`qverticalalignmentŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1fbottomŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cfigŸ±Çaoa.Ÿ±Ç`dtextŸ±Ç`a(Ÿ±Ç`erightŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ctopŸ±Ç`a,Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1iright topŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`i         Ÿ±Ç`shorizontalalignmentŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1erightŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`qverticalalignmentŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1ctopŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cfigŸ±Çaoa.Ÿ±Ç`dtextŸ±Ç`a(Ÿ±Ç`erightŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`fbottomŸ±Ç`a,Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1jcenter topŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`i         Ÿ±Ç`shorizontalalignmentŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1fcenterŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`qverticalalignmentŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1ctopŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cfigŸ±Çaoa.Ÿ±Ç`dtextŸ±Ç`a(Ÿ±Ç`dleftŸ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfc0.5Ÿ±Çaoa*Ÿ±Ç`a(Ÿ±Ç`fbottomŸ±Çaoa+Ÿ±Ç`ctopŸ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1lright centerŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`i         Ÿ±Ç`shorizontalalignmentŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1erightŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`qverticalalignmentŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1fcenterŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`i         Ÿ±Ç`hrotationŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1hverticalŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cfigŸ±Çaoa.Ÿ±Ç`dtextŸ±Ç`a(Ÿ±Ç`dleftŸ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfc0.5Ÿ±Çaoa*Ÿ±Ç`a(Ÿ±Ç`fbottomŸ±Çaoa+Ÿ±Ç`ctopŸ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1kleft centerŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`i         Ÿ±Ç`shorizontalalignmentŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1dleftŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`qverticalalignmentŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1fcenterŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`i         Ÿ±Ç`hrotationŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1hverticalŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cfigŸ±Çaoa.Ÿ±Ç`dtextŸ±Ç`a(Ÿ±Çbmfc0.5Ÿ±Çaoa*Ÿ±Ç`a(Ÿ±Ç`dleftŸ±Çaoa+Ÿ±Ç`erightŸ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfc0.5Ÿ±Çaoa*Ÿ±Ç`a(Ÿ±Ç`fbottomŸ±Çaoa+Ÿ±Ç`ctopŸ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1fmiddleŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`i         Ÿ±Ç`shorizontalalignmentŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1fcenterŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`qverticalalignmentŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1fcenterŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`i         Ÿ±Ç`hfontsizeŸ±Çaoa=Ÿ±Çbmib20Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ecolorŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1credŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cfigŸ±Çaoa.Ÿ±Ç`dtextŸ±Ç`a(Ÿ±Ç`erightŸ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfc0.5Ÿ±Çaoa*Ÿ±Ç`a(Ÿ±Ç`fbottomŸ±Çaoa+Ÿ±Ç`ctopŸ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1hcenteredŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`i         Ÿ±Ç`shorizontalalignmentŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1fcenterŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`qverticalalignmentŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1fcenterŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`i         Ÿ±Ç`hrotationŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1hverticalŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cfigŸ±Çaoa.Ÿ±Ç`dtextŸ±Ç`a(Ÿ±Ç`dleftŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ctopŸ±Ç`a,Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1grotatedŸ±Çbseb\nŸ±Çbs1mwith newlinesŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`i         Ÿ±Ç`shorizontalalignmentŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1fcenterŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`qverticalalignmentŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1fcenterŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`i         Ÿ±Ç`hrotationŸ±Çaoa=Ÿ±Çbmib45Ÿ±Ç`a)Ÿ±Ç`a
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
Ÿ±Çbc1x,#    - `matplotlib.figure.Figure.add_artist`Ÿ±Ç`a
Ÿ±Çbc1x&#    - `matplotlib.figure.Figure.text`Ÿ±Ç`a
`dNoneˆ