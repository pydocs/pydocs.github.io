ŸØÇÅŸ¥ÉôÈŸ±Çbsdy!"""
=============
Radio Buttons
=============

Using radio buttons to choose properties of your plot.

Radio buttons let you choose between multiple options in a visualization.
In this case, the buttons let the user choose one of the three different sine
waves to be shown in the plot.
"""Ÿ±Ç`a
Ÿ±ÇbknfimportŸ±Ç`a Ÿ±ÇbnnŸ¢ÑenumpyŸ†Ñenumpyf1.22.3fmoduleenumpyfmoduleıŸ±Ç`a Ÿ±ÇakbasŸ±Ç`a Ÿ±ÇbnnbnpŸ±Ç`a
Ÿ±ÇbknfimportŸ±Ç`a Ÿ±ÇbnnŸ¢ÑjmatplotlibŸ†Ñjmatplotlibe3.5.1fmodulejmatplotlibfmoduleıŸ±Çbnna.Ÿ±ÇbnnfpyplotŸ±Ç`a Ÿ±ÇakbasŸ±Ç`a Ÿ±ÇbnncpltŸ±Ç`a
Ÿ±ÇbkndfromŸ±Ç`a Ÿ±ÇbnnŸ¢ÑjmatplotlibŸ†Ñjmatplotlibe3.5.1fmodulejmatplotlibfmoduleıŸ±Çbnna.Ÿ±ÇbnngwidgetsŸ±Ç`a Ÿ±ÇbknfimportŸ±Ç`a Ÿ±Ç`lRadioButtonsŸ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`atŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`farangeŸ±Ç`a(Ÿ±Çbmfc0.0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfc2.0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd0.01Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`bs0Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`csinŸ±Ç`a(Ÿ±Çbmia2Ÿ±Çaoa*Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`bpiŸ±Çaoa*Ÿ±Ç`atŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`bs1Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`csinŸ±Ç`a(Ÿ±Çbmia4Ÿ±Çaoa*Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`bpiŸ±Çaoa*Ÿ±Ç`atŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`bs2Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`csinŸ±Ç`a(Ÿ±Çbmia8Ÿ±Çaoa*Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`bpiŸ±Çaoa*Ÿ±Ç`atŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`cfigŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`baxŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`hsubplotsŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`alŸ±Ç`a,Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`dplotŸ±Ç`a(Ÿ±Ç`atŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`bs0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`blwŸ±Çaoa=Ÿ±Çbmia2Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ecolorŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1credŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`osubplots_adjustŸ±Ç`a(Ÿ±Ç`dleftŸ±Çaoa=Ÿ±Çbmfc0.3Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`gaxcolorŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1tlightgoldenrodyellowŸ±Çbs1a'Ÿ±Ç`a
Ÿ±Ç`craxŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`daxesŸ±Ç`a(Ÿ±Ç`a[Ÿ±Çbmfd0.05Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfc0.7Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd0.15Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd0.15Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ifacecolorŸ±Çaoa=Ÿ±Ç`gaxcolorŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`eradioŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`lRadioButtonsŸ±Ç`a(Ÿ±Ç`craxŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`a(Ÿ±Çbs1a'Ÿ±Çbs1d2 HzŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1d4 HzŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1d8 HzŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±ÇakcdefŸ±Ç`a Ÿ±ÇbnffhzfuncŸ±Ç`a(Ÿ±Ç`elabelŸ±Ç`a)Ÿ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`fhzdictŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`a{Ÿ±Çbs1a'Ÿ±Çbs1d2 HzŸ±Çbs1a'Ÿ±Ç`a:Ÿ±Ç`a Ÿ±Ç`bs0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1d4 HzŸ±Çbs1a'Ÿ±Ç`a:Ÿ±Ç`a Ÿ±Ç`bs1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1d8 HzŸ±Çbs1a'Ÿ±Ç`a:Ÿ±Ç`a Ÿ±Ç`bs2Ÿ±Ç`a}Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`eydataŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`fhzdictŸ±Ç`a[Ÿ±Ç`elabelŸ±Ç`a]Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`alŸ±Çaoa.Ÿ±Ç`iset_ydataŸ±Ç`a(Ÿ±Ç`eydataŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`ddrawŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`eradioŸ±Çaoa.Ÿ±Ç`jon_clickedŸ±Ç`a(Ÿ±Ç`fhzfuncŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`craxŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`daxesŸ±Ç`a(Ÿ±Ç`a[Ÿ±Çbmfd0.05Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfc0.4Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd0.15Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd0.15Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ifacecolorŸ±Çaoa=Ÿ±Ç`gaxcolorŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`fradio2Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`lRadioButtonsŸ±Ç`a(Ÿ±Ç`craxŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`a(Ÿ±Çbs1a'Ÿ±Çbs1credŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1dblueŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1egreenŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±ÇakcdefŸ±Ç`a Ÿ±ÇbnficolorfuncŸ±Ç`a(Ÿ±Ç`elabelŸ±Ç`a)Ÿ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`alŸ±Çaoa.Ÿ±Ç`iset_colorŸ±Ç`a(Ÿ±Ç`elabelŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`ddrawŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`fradio2Ÿ±Çaoa.Ÿ±Ç`jon_clickedŸ±Ç`a(Ÿ±Ç`icolorfuncŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`craxŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`daxesŸ±Ç`a(Ÿ±Ç`a[Ÿ±Çbmfd0.05Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfc0.1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd0.15Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd0.15Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ifacecolorŸ±Çaoa=Ÿ±Ç`gaxcolorŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`fradio3Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`lRadioButtonsŸ±Ç`a(Ÿ±Ç`craxŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`a(Ÿ±Çbs1a'Ÿ±Çbs1a-Ÿ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1b--Ÿ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1b-.Ÿ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1estepsŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1a:Ÿ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±ÇakcdefŸ±Ç`a Ÿ±ÇbnfistylefuncŸ±Ç`a(Ÿ±Ç`elabelŸ±Ç`a)Ÿ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`alŸ±Çaoa.Ÿ±Ç`mset_linestyleŸ±Ç`a(Ÿ±Ç`elabelŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`ddrawŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`fradio3Ÿ±Çaoa.Ÿ±Ç`jon_clickedŸ±Ç`a(Ÿ±Ç`istylefuncŸ±Ç`a)Ÿ±Ç`a
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
Ÿ±Çbc1x(#    - `matplotlib.widgets.RadioButtons`Ÿ±Ç`a
`dNoneˆ