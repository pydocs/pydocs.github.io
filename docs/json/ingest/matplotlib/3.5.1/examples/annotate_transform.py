ŸØÇÅŸ¥ÉôkŸ±Çbsdy"""
==================
Annotate Transform
==================

This example shows how to use different coordinate systems for annotations.
For a complete overview of the annotation capabilities, also see the
:doc:`annotation tutorial</tutorials/text/annotations>`.
"""Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±ÇbknfimportŸ±Ç`a Ÿ±ÇbnnŸ¢ÑenumpyŸ†Ñenumpyf1.22.3fmoduleenumpyfmoduleıŸ±Ç`a Ÿ±ÇakbasŸ±Ç`a Ÿ±ÇbnnbnpŸ±Ç`a
Ÿ±ÇbknfimportŸ±Ç`a Ÿ±ÇbnnŸ¢ÑjmatplotlibŸ†Ñjmatplotlibe3.5.1fmodulejmatplotlibfmoduleıŸ±Çbnna.Ÿ±ÇbnnfpyplotŸ±Ç`a Ÿ±ÇakbasŸ±Ç`a Ÿ±ÇbnncpltŸ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`axŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`farangeŸ±Ç`a(Ÿ±Çbmia0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmib10Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfe0.005Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`ayŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`cexpŸ±Ç`a(Ÿ±Çaoa-Ÿ±Ç`axŸ±Çaoa/Ÿ±Çbmfb2.Ÿ±Ç`a)Ÿ±Ç`a Ÿ±Çaoa*Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`csinŸ±Ç`a(Ÿ±Çbmia2Ÿ±Çaoa*Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`bpiŸ±Çaoa*Ÿ±Ç`axŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`cfigŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`baxŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`hsubplotsŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`dplotŸ±Ç`a(Ÿ±Ç`axŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ayŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`hset_xlimŸ±Ç`a(Ÿ±Çbmia0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmib10Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`hset_ylimŸ±Ç`a(Ÿ±Çaoa-Ÿ±Çbmia1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia1Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`exdataŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`eydataŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Çbmia5Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia0Ÿ±Ç`a
Ÿ±Ç`hxdisplayŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`hydisplayŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`itransDataŸ±Çaoa.Ÿ±Ç`itransformŸ±Ç`a(Ÿ±Ç`a(Ÿ±Ç`exdataŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`eydataŸ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`dbboxŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±ÇbnbddictŸ±Ç`a(Ÿ±Ç`hboxstyleŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2eroundŸ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`bfcŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2c0.8Ÿ±Çbs2a"Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`jarrowpropsŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±ÇbnbddictŸ±Ç`a(Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`jarrowstyleŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2b->Ÿ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`oconnectionstyleŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2xangle,angleA=0,angleB=90,rad=10Ÿ±Çbs2a"Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`foffsetŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Çbmib72Ÿ±Ç`a
Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`hannotateŸ±Ç`a(Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±ÇbsaafŸ±Çbs1a'Ÿ±Çbs1hdata = (Ÿ±Çbsia{Ÿ±Ç`exdataŸ±Çbsia:Ÿ±Çbs1c.1fŸ±Çbsia}Ÿ±Çbs1b, Ÿ±Çbsia{Ÿ±Ç`eydataŸ±Çbsia:Ÿ±Çbs1c.1fŸ±Çbsia}Ÿ±Çbs1a)Ÿ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`a(Ÿ±Ç`exdataŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`eydataŸ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`fxytextŸ±Çaoa=Ÿ±Ç`a(Ÿ±Çaoa-Ÿ±Çbmia2Ÿ±Çaoa*Ÿ±Ç`foffsetŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`foffsetŸ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`jtextcoordsŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1moffset pointsŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`dbboxŸ±Çaoa=Ÿ±Ç`dbboxŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`jarrowpropsŸ±Çaoa=Ÿ±Ç`jarrowpropsŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`hannotateŸ±Ç`a(Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±ÇbsaafŸ±Çbs1a'Ÿ±Çbs1kdisplay = (Ÿ±Çbsia{Ÿ±Ç`hxdisplayŸ±Çbsia:Ÿ±Çbs1c.1fŸ±Çbsia}Ÿ±Çbs1b, Ÿ±Çbsia{Ÿ±Ç`hydisplayŸ±Çbsia:Ÿ±Çbs1c.1fŸ±Çbsia}Ÿ±Çbs1a)Ÿ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`bxyŸ±Çaoa=Ÿ±Ç`a(Ÿ±Ç`hxdisplayŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`hydisplayŸ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`hxycoordsŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1mfigure pixelsŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`fxytextŸ±Çaoa=Ÿ±Ç`a(Ÿ±Çbmfc0.5Ÿ±Çaoa*Ÿ±Ç`foffsetŸ±Ç`a,Ÿ±Ç`a Ÿ±Çaoa-Ÿ±Ç`foffsetŸ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`jtextcoordsŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1moffset pointsŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`dbboxŸ±Çaoa=Ÿ±Ç`dbboxŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`jarrowpropsŸ±Çaoa=Ÿ±Ç`jarrowpropsŸ±Ç`a)Ÿ±Ç`a
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
Ÿ±Çbc1x2#    - `matplotlib.transforms.Transform.transform`Ÿ±Ç`a
Ÿ±Çbc1xE#    - `matplotlib.axes.Axes.annotate` / `matplotlib.pyplot.annotate`Ÿ±Ç`a
`dNoneˆ