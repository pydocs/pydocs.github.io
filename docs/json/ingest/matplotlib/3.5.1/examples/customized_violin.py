ŸØÇÅŸ¥ÉôËŸ±Çbsdy5"""
=========================
Violin plot customization
=========================

This example demonstrates how to fully customize violin plots. The first plot
shows the default style by providing only the data. The second plot first
limits what Matplotlib draws with additional keyword arguments. Then a
simplified representation of a box plot is drawn on top. Lastly, the styles of
the artists of the violins are modified.

For more information on violin plots, the scikit-learn docs have a great
section: https://scikit-learn.org/stable/modules/density.html
"""Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±ÇbknfimportŸ±Ç`a Ÿ±ÇbnnŸ¢ÑjmatplotlibŸ†Ñjmatplotlibe3.5.1fmodulejmatplotlibfmoduleıŸ±Çbnna.Ÿ±ÇbnnfpyplotŸ±Ç`a Ÿ±ÇakbasŸ±Ç`a Ÿ±ÇbnncpltŸ±Ç`a
Ÿ±ÇbknfimportŸ±Ç`a Ÿ±ÇbnnŸ¢ÑenumpyŸ†Ñenumpyf1.22.3fmoduleenumpyfmoduleıŸ±Ç`a Ÿ±ÇakbasŸ±Ç`a Ÿ±ÇbnnbnpŸ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±ÇakcdefŸ±Ç`a Ÿ±Çbnfoadjacent_valuesŸ±Ç`a(Ÿ±Ç`dvalsŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`bq1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`bq3Ÿ±Ç`a)Ÿ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`tupper_adjacent_valueŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bq3Ÿ±Ç`a Ÿ±Çaoa+Ÿ±Ç`a Ÿ±Ç`a(Ÿ±Ç`bq3Ÿ±Ç`a Ÿ±Çaoa-Ÿ±Ç`a Ÿ±Ç`bq1Ÿ±Ç`a)Ÿ±Ç`a Ÿ±Çaoa*Ÿ±Ç`a Ÿ±Çbmfc1.5Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`tupper_adjacent_valueŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`dclipŸ±Ç`a(Ÿ±Ç`tupper_adjacent_valueŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`bq3Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dvalsŸ±Ç`a[Ÿ±Çaoa-Ÿ±Çbmia1Ÿ±Ç`a]Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`tlower_adjacent_valueŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bq1Ÿ±Ç`a Ÿ±Çaoa-Ÿ±Ç`a Ÿ±Ç`a(Ÿ±Ç`bq3Ÿ±Ç`a Ÿ±Çaoa-Ÿ±Ç`a Ÿ±Ç`bq1Ÿ±Ç`a)Ÿ±Ç`a Ÿ±Çaoa*Ÿ±Ç`a Ÿ±Çbmfc1.5Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`tlower_adjacent_valueŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`dclipŸ±Ç`a(Ÿ±Ç`tlower_adjacent_valueŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dvalsŸ±Ç`a[Ÿ±Çbmia0Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`bq1Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±ÇakfreturnŸ±Ç`a Ÿ±Ç`tlower_adjacent_valueŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`tupper_adjacent_valueŸ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±ÇakcdefŸ±Ç`a Ÿ±Çbnfnset_axis_styleŸ±Ç`a(Ÿ±Ç`baxŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`flabelsŸ±Ç`a)Ÿ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`exaxisŸ±Çaoa.Ÿ±Ç`oset_tick_paramsŸ±Ç`a(Ÿ±Ç`idirectionŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1coutŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`exaxisŸ±Çaoa.Ÿ±Ç`rset_ticks_positionŸ±Ç`a(Ÿ±Çbs1a'Ÿ±Çbs1fbottomŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`jset_xticksŸ±Ç`a(Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`farangeŸ±Ç`a(Ÿ±Çbmia1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±ÇbnbclenŸ±Ç`a(Ÿ±Ç`flabelsŸ±Ç`a)Ÿ±Ç`a Ÿ±Çaoa+Ÿ±Ç`a Ÿ±Çbmia1Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`flabelsŸ±Çaoa=Ÿ±Ç`flabelsŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`hset_xlimŸ±Ç`a(Ÿ±Çbmfd0.25Ÿ±Ç`a,Ÿ±Ç`a Ÿ±ÇbnbclenŸ±Ç`a(Ÿ±Ç`flabelsŸ±Ç`a)Ÿ±Ç`a Ÿ±Çaoa+Ÿ±Ç`a Ÿ±Çbmfd0.75Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`jset_xlabelŸ±Ç`a(Ÿ±Çbs1a'Ÿ±Çbs1kSample nameŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1r# create test dataŸ±Ç`a
Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`frandomŸ±Çaoa.Ÿ±Ç`dseedŸ±Ç`a(Ÿ±Çbmih19680801Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`ddataŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`a[Ÿ±ÇbnbfsortedŸ±Ç`a(Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`frandomŸ±Çaoa.Ÿ±Ç`fnormalŸ±Ç`a(Ÿ±Çbmia0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`cstdŸ±Ç`a,Ÿ±Ç`a Ÿ±Çbmic100Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a Ÿ±ÇakcforŸ±Ç`a Ÿ±Ç`cstdŸ±Ç`a Ÿ±ÇbowbinŸ±Ç`a Ÿ±ÇbnberangeŸ±Ç`a(Ÿ±Çbmia1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia5Ÿ±Ç`a)Ÿ±Ç`a]Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`cfigŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`a(Ÿ±Ç`cax1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`cax2Ÿ±Ç`a)Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`hsubplotsŸ±Ç`a(Ÿ±Ç`enrowsŸ±Çaoa=Ÿ±Çbmia1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`encolsŸ±Çaoa=Ÿ±Çbmia2Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`gfigsizeŸ±Çaoa=Ÿ±Ç`a(Ÿ±Çbmia9Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia4Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`fshareyŸ±Çaoa=Ÿ±ÇbkcdTrueŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`cax1Ÿ±Çaoa.Ÿ±Ç`iset_titleŸ±Ç`a(Ÿ±Çbs1a'Ÿ±Çbs1sDefault violin plotŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cax1Ÿ±Çaoa.Ÿ±Ç`jset_ylabelŸ±Ç`a(Ÿ±Çbs1a'Ÿ±Çbs1oObserved valuesŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cax1Ÿ±Çaoa.Ÿ±Ç`jviolinplotŸ±Ç`a(Ÿ±Ç`ddataŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`cax2Ÿ±Çaoa.Ÿ±Ç`iset_titleŸ±Ç`a(Ÿ±Çbs1a'Ÿ±Çbs1vCustomized violin plotŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`epartsŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cax2Ÿ±Çaoa.Ÿ±Ç`jviolinplotŸ±Ç`a(Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±Ç`ddataŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ishowmeansŸ±Çaoa=Ÿ±ÇbkceFalseŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`kshowmediansŸ±Çaoa=Ÿ±ÇbkceFalseŸ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±Ç`kshowextremaŸ±Çaoa=Ÿ±ÇbkceFalseŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±ÇakcforŸ±Ç`a Ÿ±Ç`bpcŸ±Ç`a Ÿ±ÇbowbinŸ±Ç`a Ÿ±Ç`epartsŸ±Ç`a[Ÿ±Çbs1a'Ÿ±Çbs1fbodiesŸ±Çbs1a'Ÿ±Ç`a]Ÿ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`bpcŸ±Çaoa.Ÿ±Ç`mset_facecolorŸ±Ç`a(Ÿ±Çbs1a'Ÿ±Çbs1g#D43F3AŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`bpcŸ±Çaoa.Ÿ±Ç`mset_edgecolorŸ±Ç`a(Ÿ±Çbs1a'Ÿ±Çbs1eblackŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`bpcŸ±Çaoa.Ÿ±Ç`iset_alphaŸ±Ç`a(Ÿ±Çbmia1Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`iquartile1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`gmediansŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`iquartile3Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`jpercentileŸ±Ç`a(Ÿ±Ç`ddataŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`a[Ÿ±Çbmib25Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmib50Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmib75Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`daxisŸ±Çaoa=Ÿ±Çbmia1Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`hwhiskersŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`earrayŸ±Ç`a(Ÿ±Ç`a[Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`oadjacent_valuesŸ±Ç`a(Ÿ±Ç`lsorted_arrayŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`bq1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`bq3Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±ÇakcforŸ±Ç`a Ÿ±Ç`lsorted_arrayŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`bq1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`bq3Ÿ±Ç`a Ÿ±ÇbowbinŸ±Ç`a Ÿ±ÇbnbczipŸ±Ç`a(Ÿ±Ç`ddataŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`iquartile1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`iquartile3Ÿ±Ç`a)Ÿ±Ç`a]Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`lwhiskers_minŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`lwhiskers_maxŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`hwhiskersŸ±Ç`a[Ÿ±Ç`a:Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia0Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`hwhiskersŸ±Ç`a[Ÿ±Ç`a:Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia1Ÿ±Ç`a]Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`dindsŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`farangeŸ±Ç`a(Ÿ±Çbmia1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±ÇbnbclenŸ±Ç`a(Ÿ±Ç`gmediansŸ±Ç`a)Ÿ±Ç`a Ÿ±Çaoa+Ÿ±Ç`a Ÿ±Çbmia1Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cax2Ÿ±Çaoa.Ÿ±Ç`gscatterŸ±Ç`a(Ÿ±Ç`dindsŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`gmediansŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`fmarkerŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1aoŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ecolorŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1ewhiteŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`asŸ±Çaoa=Ÿ±Çbmib30Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`fzorderŸ±Çaoa=Ÿ±Çbmia3Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cax2Ÿ±Çaoa.Ÿ±Ç`fvlinesŸ±Ç`a(Ÿ±Ç`dindsŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`iquartile1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`iquartile3Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ecolorŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1akŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ilinestyleŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1a-Ÿ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`blwŸ±Çaoa=Ÿ±Çbmia5Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cax2Ÿ±Çaoa.Ÿ±Ç`fvlinesŸ±Ç`a(Ÿ±Ç`dindsŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`lwhiskers_minŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`lwhiskers_maxŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ecolorŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1akŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ilinestyleŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1a-Ÿ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`blwŸ±Çaoa=Ÿ±Çbmia1Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1x# set style for the axesŸ±Ç`a
Ÿ±Ç`flabelsŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`a[Ÿ±Çbs1a'Ÿ±Çbs1aAŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1aBŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1aCŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1aDŸ±Çbs1a'Ÿ±Ç`a]Ÿ±Ç`a
Ÿ±ÇakcforŸ±Ç`a Ÿ±Ç`baxŸ±Ç`a Ÿ±ÇbowbinŸ±Ç`a Ÿ±Ç`a[Ÿ±Ç`cax1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`cax2Ÿ±Ç`a]Ÿ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`nset_axis_styleŸ±Ç`a(Ÿ±Ç`baxŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`flabelsŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`osubplots_adjustŸ±Ç`a(Ÿ±Ç`fbottomŸ±Çaoa=Ÿ±Çbmfd0.15Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`fwspaceŸ±Çaoa=Ÿ±Çbmfd0.05Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`dshowŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1xM#############################################################################Ÿ±Ç`a
Ÿ±Çbc1a#Ÿ±Ç`a
Ÿ±Çbc1x# .. admonition:: ReferencesŸ±Ç`a
Ÿ±Çbc1a#Ÿ±Ç`a
Ÿ±Çbc1xN#    The use of the following functions, methods, classes and modules is shownŸ±Ç`a
Ÿ±Çbc1u#    in this example:Ÿ±Ç`a
Ÿ±Çbc1a#Ÿ±Ç`a
Ÿ±Çbc1xI#    - `matplotlib.axes.Axes.violinplot` / `matplotlib.pyplot.violinplot`Ÿ±Ç`a
Ÿ±Çbc1xA#    - `matplotlib.axes.Axes.vlines` / `matplotlib.pyplot.vlines`Ÿ±Ç`a
`dNoneˆ