ŸØÇÅŸ¥Éô—Ÿ±Çbsdyó"""
==================
ggplot style sheet
==================

This example demonstrates the "ggplot" style, which adjusts the style to
emulate ggplot_ (a popular plotting package for R_).

These settings were shamelessly stolen from [1]_ (with permission).

.. [1] https://everyhue.me/posts/sane-color-scheme-for-matplotlib/

.. _ggplot: https://ggplot2.tidyverse.org/
.. _R: https://www.r-project.org/

"""Ÿ±Ç`a
Ÿ±ÇbknfimportŸ±Ç`a Ÿ±ÇbnnŸ¢ÑenumpyŸ†Ñenumpyf1.22.3fmoduleenumpyfmoduleıŸ±Ç`a Ÿ±ÇakbasŸ±Ç`a Ÿ±ÇbnnbnpŸ±Ç`a
Ÿ±ÇbknfimportŸ±Ç`a Ÿ±ÇbnnŸ¢ÑjmatplotlibŸ†Ñjmatplotlibe3.5.1fmodulejmatplotlibfmoduleıŸ±Çbnna.Ÿ±ÇbnnfpyplotŸ±Ç`a Ÿ±ÇakbasŸ±Ç`a Ÿ±ÇbnncpltŸ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`estyleŸ±Çaoa.Ÿ±Ç`cuseŸ±Ç`a(Ÿ±Çbs1a'Ÿ±Çbs1fggplotŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1x)# Fixing random state for reproducibilityŸ±Ç`a
Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`frandomŸ±Çaoa.Ÿ±Ç`dseedŸ±Ç`a(Ÿ±Çbmih19680801Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`cfigŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`caxsŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`hsubplotsŸ±Ç`a(Ÿ±Ç`encolsŸ±Çaoa=Ÿ±Çbmia2Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`enrowsŸ±Çaoa=Ÿ±Çbmia2Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cax1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`cax2Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`cax3Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`cax4Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`caxsŸ±Çaoa.Ÿ±Ç`dflatŸ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1x?# scatter plot (Note: `plt.scatter` doesn't use default colors)Ÿ±Ç`a
Ÿ±Ç`axŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ayŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`frandomŸ±Çaoa.Ÿ±Ç`fnormalŸ±Ç`a(Ÿ±Ç`dsizeŸ±Çaoa=Ÿ±Ç`a(Ÿ±Çbmia2Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmic200Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cax1Ÿ±Çaoa.Ÿ±Ç`dplotŸ±Ç`a(Ÿ±Ç`axŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ayŸ±Ç`a,Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1aoŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1x7# sinusoidal lines with colors from default color cycleŸ±Ç`a
Ÿ±Ç`aLŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Çbmia2Ÿ±Çaoa*Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`bpiŸ±Ç`a
Ÿ±Ç`axŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`hlinspaceŸ±Ç`a(Ÿ±Çbmia0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`aLŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`gncolorsŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±ÇbnbclenŸ±Ç`a(Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`hrcParamsŸ±Ç`a[Ÿ±Çbs1a'Ÿ±Çbs1oaxes.prop_cycleŸ±Çbs1a'Ÿ±Ç`a]Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`eshiftŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`hlinspaceŸ±Ç`a(Ÿ±Çbmia0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`aLŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`gncolorsŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`hendpointŸ±Çaoa=Ÿ±ÇbkceFalseŸ±Ç`a)Ÿ±Ç`a
Ÿ±ÇakcforŸ±Ç`a Ÿ±Ç`asŸ±Ç`a Ÿ±ÇbowbinŸ±Ç`a Ÿ±Ç`eshiftŸ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`cax2Ÿ±Çaoa.Ÿ±Ç`dplotŸ±Ç`a(Ÿ±Ç`axŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`csinŸ±Ç`a(Ÿ±Ç`axŸ±Ç`a Ÿ±Çaoa+Ÿ±Ç`a Ÿ±Ç`asŸ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1a-Ÿ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cax2Ÿ±Çaoa.Ÿ±Ç`gmarginsŸ±Ç`a(Ÿ±Çbmia0Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1l# bar graphsŸ±Ç`a
Ÿ±Ç`axŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`farangeŸ±Ç`a(Ÿ±Çbmia5Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`by1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`by2Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`frandomŸ±Çaoa.Ÿ±Ç`grandintŸ±Ç`a(Ÿ±Çbmia1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmib25Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dsizeŸ±Çaoa=Ÿ±Ç`a(Ÿ±Çbmia2Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia5Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`ewidthŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Çbmfd0.25Ÿ±Ç`a
Ÿ±Ç`cax3Ÿ±Çaoa.Ÿ±Ç`cbarŸ±Ç`a(Ÿ±Ç`axŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`by1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ewidthŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cax3Ÿ±Çaoa.Ÿ±Ç`cbarŸ±Ç`a(Ÿ±Ç`axŸ±Ç`a Ÿ±Çaoa+Ÿ±Ç`a Ÿ±Ç`ewidthŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`by2Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ewidthŸ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±Ç`ecolorŸ±Çaoa=Ÿ±ÇbnbdlistŸ±Ç`a(Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`hrcParamsŸ±Ç`a[Ÿ±Çbs1a'Ÿ±Çbs1oaxes.prop_cycleŸ±Çbs1a'Ÿ±Ç`a]Ÿ±Ç`a)Ÿ±Ç`a[Ÿ±Çbmia2Ÿ±Ç`a]Ÿ±Ç`a[Ÿ±Çbs1a'Ÿ±Çbs1ecolorŸ±Çbs1a'Ÿ±Ç`a]Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cax3Ÿ±Çaoa.Ÿ±Ç`jset_xticksŸ±Ç`a(Ÿ±Ç`axŸ±Ç`a Ÿ±Çaoa+Ÿ±Ç`a Ÿ±Ç`ewidthŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`flabelsŸ±Çaoa=Ÿ±Ç`a[Ÿ±Çbs1a'Ÿ±Çbs1aaŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1abŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1acŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1adŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1aeŸ±Çbs1a'Ÿ±Ç`a]Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1x.# circles with colors from default color cycleŸ±Ç`a
Ÿ±ÇakcforŸ±Ç`a Ÿ±Ç`aiŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ecolorŸ±Ç`a Ÿ±ÇbowbinŸ±Ç`a Ÿ±ÇbnbienumerateŸ±Ç`a(Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`hrcParamsŸ±Ç`a[Ÿ±Çbs1a'Ÿ±Çbs1oaxes.prop_cycleŸ±Çbs1a'Ÿ±Ç`a]Ÿ±Ç`a)Ÿ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`bxyŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`frandomŸ±Çaoa.Ÿ±Ç`fnormalŸ±Ç`a(Ÿ±Ç`dsizeŸ±Çaoa=Ÿ±Çbmia2Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`cax4Ÿ±Çaoa.Ÿ±Ç`iadd_patchŸ±Ç`a(Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`fCircleŸ±Ç`a(Ÿ±Ç`bxyŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`fradiusŸ±Çaoa=Ÿ±Çbmfc0.3Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ecolorŸ±Çaoa=Ÿ±Ç`ecolorŸ±Ç`a[Ÿ±Çbs1a'Ÿ±Çbs1ecolorŸ±Çbs1a'Ÿ±Ç`a]Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cax4Ÿ±Çaoa.Ÿ±Ç`daxisŸ±Ç`a(Ÿ±Çbs1a'Ÿ±Çbs1eequalŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cax4Ÿ±Çaoa.Ÿ±Ç`gmarginsŸ±Ç`a(Ÿ±Çbmia0Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`dshowŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
`dNoneˆ