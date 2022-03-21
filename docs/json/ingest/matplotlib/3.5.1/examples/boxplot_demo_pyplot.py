ŸØÇÅŸ¥ÉôNŸ±ÇbsdxD"""
============
Boxplot Demo
============

Example boxplot code
"""Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±ÇbknfimportŸ±Ç`a Ÿ±ÇbnnŸ¢ÑenumpyŸ†Ñenumpyf1.22.3fmoduleenumpyfmoduleıŸ±Ç`a Ÿ±ÇakbasŸ±Ç`a Ÿ±ÇbnnbnpŸ±Ç`a
Ÿ±ÇbknfimportŸ±Ç`a Ÿ±ÇbnnŸ¢ÑjmatplotlibŸ†Ñjmatplotlibe3.5.1fmodulejmatplotlibfmoduleıŸ±Çbnna.Ÿ±ÇbnnfpyplotŸ±Ç`a Ÿ±ÇakbasŸ±Ç`a Ÿ±ÇbnncpltŸ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1x)# Fixing random state for reproducibilityŸ±Ç`a
Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`frandomŸ±Çaoa.Ÿ±Ç`dseedŸ±Ç`a(Ÿ±Çbmih19680801Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1s# fake up some dataŸ±Ç`a
Ÿ±Ç`fspreadŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`frandomŸ±Çaoa.Ÿ±Ç`drandŸ±Ç`a(Ÿ±Çbmib50Ÿ±Ç`a)Ÿ±Ç`a Ÿ±Çaoa*Ÿ±Ç`a Ÿ±Çbmic100Ÿ±Ç`a
Ÿ±Ç`fcenterŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`donesŸ±Ç`a(Ÿ±Çbmib25Ÿ±Ç`a)Ÿ±Ç`a Ÿ±Çaoa*Ÿ±Ç`a Ÿ±Çbmib50Ÿ±Ç`a
Ÿ±Ç`jflier_highŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`frandomŸ±Çaoa.Ÿ±Ç`drandŸ±Ç`a(Ÿ±Çbmib10Ÿ±Ç`a)Ÿ±Ç`a Ÿ±Çaoa*Ÿ±Ç`a Ÿ±Çbmic100Ÿ±Ç`a Ÿ±Çaoa+Ÿ±Ç`a Ÿ±Çbmic100Ÿ±Ç`a
Ÿ±Ç`iflier_lowŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`frandomŸ±Çaoa.Ÿ±Ç`drandŸ±Ç`a(Ÿ±Çbmib10Ÿ±Ç`a)Ÿ±Ç`a Ÿ±Çaoa*Ÿ±Ç`a Ÿ±Çaoa-Ÿ±Çbmic100Ÿ±Ç`a
Ÿ±Ç`ddataŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`kconcatenateŸ±Ç`a(Ÿ±Ç`a(Ÿ±Ç`fspreadŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`fcenterŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`jflier_highŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`iflier_lowŸ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1xO###############################################################################Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`dfig1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`cax1Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`hsubplotsŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cax1Ÿ±Çaoa.Ÿ±Ç`iset_titleŸ±Ç`a(Ÿ±Çbs1a'Ÿ±Çbs1jBasic PlotŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cax1Ÿ±Çaoa.Ÿ±Ç`gboxplotŸ±Ç`a(Ÿ±Ç`ddataŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1xO###############################################################################Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`dfig2Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`cax2Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`hsubplotsŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cax2Ÿ±Çaoa.Ÿ±Ç`iset_titleŸ±Ç`a(Ÿ±Çbs1a'Ÿ±Çbs1mNotched boxesŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cax2Ÿ±Çaoa.Ÿ±Ç`gboxplotŸ±Ç`a(Ÿ±Ç`ddataŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`enotchŸ±Çaoa=Ÿ±ÇbkcdTrueŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1xO###############################################################################Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`mgreen_diamondŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±ÇbnbddictŸ±Ç`a(Ÿ±Ç`omarkerfacecolorŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1agŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`fmarkerŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1aDŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`dfig3Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`cax3Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`hsubplotsŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cax3Ÿ±Çaoa.Ÿ±Ç`iset_titleŸ±Ç`a(Ÿ±Çbs1a'Ÿ±Çbs1wChanged Outlier SymbolsŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cax3Ÿ±Çaoa.Ÿ±Ç`gboxplotŸ±Ç`a(Ÿ±Ç`ddataŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`jflierpropsŸ±Çaoa=Ÿ±Ç`mgreen_diamondŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1xO###############################################################################Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`dfig4Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`cax4Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`hsubplotsŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cax4Ÿ±Çaoa.Ÿ±Ç`iset_titleŸ±Ç`a(Ÿ±Çbs1a'Ÿ±Çbs1sHide Outlier PointsŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cax4Ÿ±Çaoa.Ÿ±Ç`gboxplotŸ±Ç`a(Ÿ±Ç`ddataŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`jshowfliersŸ±Çaoa=Ÿ±ÇbkceFalseŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1xO###############################################################################Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`jred_squareŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±ÇbnbddictŸ±Ç`a(Ÿ±Ç`omarkerfacecolorŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1arŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`fmarkerŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1asŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`dfig5Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`cax5Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`hsubplotsŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cax5Ÿ±Çaoa.Ÿ±Ç`iset_titleŸ±Ç`a(Ÿ±Çbs1a'Ÿ±Çbs1pHorizontal BoxesŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cax5Ÿ±Çaoa.Ÿ±Ç`gboxplotŸ±Ç`a(Ÿ±Ç`ddataŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dvertŸ±Çaoa=Ÿ±ÇbkceFalseŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`jflierpropsŸ±Çaoa=Ÿ±Ç`jred_squareŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1xO###############################################################################Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`dfig6Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`cax6Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`hsubplotsŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cax6Ÿ±Çaoa.Ÿ±Ç`iset_titleŸ±Ç`a(Ÿ±Çbs1a'Ÿ±Çbs1vShorter Whisker LengthŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cax6Ÿ±Çaoa.Ÿ±Ç`gboxplotŸ±Ç`a(Ÿ±Ç`ddataŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`jflierpropsŸ±Çaoa=Ÿ±Ç`jred_squareŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dvertŸ±Çaoa=Ÿ±ÇbkceFalseŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dwhisŸ±Çaoa=Ÿ±Çbmfd0.75Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1xO###############################################################################Ÿ±Ç`a
Ÿ±Çbc1x# Fake up some more dataŸ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`fspreadŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`frandomŸ±Çaoa.Ÿ±Ç`drandŸ±Ç`a(Ÿ±Çbmib50Ÿ±Ç`a)Ÿ±Ç`a Ÿ±Çaoa*Ÿ±Ç`a Ÿ±Çbmic100Ÿ±Ç`a
Ÿ±Ç`fcenterŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`donesŸ±Ç`a(Ÿ±Çbmib25Ÿ±Ç`a)Ÿ±Ç`a Ÿ±Çaoa*Ÿ±Ç`a Ÿ±Çbmib40Ÿ±Ç`a
Ÿ±Ç`jflier_highŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`frandomŸ±Çaoa.Ÿ±Ç`drandŸ±Ç`a(Ÿ±Çbmib10Ÿ±Ç`a)Ÿ±Ç`a Ÿ±Çaoa*Ÿ±Ç`a Ÿ±Çbmic100Ÿ±Ç`a Ÿ±Çaoa+Ÿ±Ç`a Ÿ±Çbmic100Ÿ±Ç`a
Ÿ±Ç`iflier_lowŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`frandomŸ±Çaoa.Ÿ±Ç`drandŸ±Ç`a(Ÿ±Çbmib10Ÿ±Ç`a)Ÿ±Ç`a Ÿ±Çaoa*Ÿ±Ç`a Ÿ±Çaoa-Ÿ±Çbmic100Ÿ±Ç`a
Ÿ±Ç`bd2Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`kconcatenateŸ±Ç`a(Ÿ±Ç`a(Ÿ±Ç`fspreadŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`fcenterŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`jflier_highŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`iflier_lowŸ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1xO###############################################################################Ÿ±Ç`a
Ÿ±Çbc1x:# Making a 2-D array only works if all the columns are theŸ±Ç`a
Ÿ±Çbc1x9# same length.  If they are not, then use a list instead.Ÿ±Ç`a
Ÿ±Çbc1x:# This is actually more efficient because boxplot convertsŸ±Ç`a
Ÿ±Çbc1x7# a 2-D array into a list of vectors internally anyway.Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`ddataŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`a[Ÿ±Ç`ddataŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`bd2Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`bd2Ÿ±Ç`a[Ÿ±Ç`a:Ÿ±Ç`a:Ÿ±Çbmia2Ÿ±Ç`a]Ÿ±Ç`a]Ÿ±Ç`a
Ÿ±Ç`dfig7Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`cax7Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`hsubplotsŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cax7Ÿ±Çaoa.Ÿ±Ç`iset_titleŸ±Ç`a(Ÿ±Çbs1a'Ÿ±Çbs1x%Multiple Samples with Different sizesŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cax7Ÿ±Çaoa.Ÿ±Ç`gboxplotŸ±Ç`a(Ÿ±Ç`ddataŸ±Ç`a)Ÿ±Ç`a
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
Ÿ±Çbc1xC#    - `matplotlib.axes.Axes.boxplot` / `matplotlib.pyplot.boxplot`Ÿ±Ç`a
`dNoneˆ