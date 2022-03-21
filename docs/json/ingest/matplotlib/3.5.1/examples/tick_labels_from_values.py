ŸØÇÅŸ¥Éò∑Ÿ±Çbsdy*"""
=========================================
Setting tick labels from a list of values
=========================================

Using `.Axes.set_xticks` causes the tick labels to be set on the currently
chosen ticks. However, you may want to allow matplotlib to dynamically
choose the number of ticks and their spacing.

In this case it may be better to determine the tick label from the
value at the tick. The following example shows how to do this.

NB: The `.ticker.MaxNLocator` is used here to ensure that the tick values
take integer values.

"""Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±ÇbknfimportŸ±Ç`a Ÿ±ÇbnnŸ¢ÑjmatplotlibŸ†Ñjmatplotlibe3.5.1fmodulejmatplotlibfmoduleıŸ±Çbnna.Ÿ±ÇbnnfpyplotŸ±Ç`a Ÿ±ÇakbasŸ±Ç`a Ÿ±ÇbnncpltŸ±Ç`a
Ÿ±ÇbkndfromŸ±Ç`a Ÿ±ÇbnnŸ¢ÑjmatplotlibŸ†Ñjmatplotlibe3.5.1fmodulejmatplotlibfmoduleıŸ±Çbnna.Ÿ±ÇbnnftickerŸ±Ç`a Ÿ±ÇbknfimportŸ±Ç`a Ÿ±Ç`kMaxNLocatorŸ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`cfigŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`baxŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`hsubplotsŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`bxsŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±ÇbnberangeŸ±Ç`a(Ÿ±Çbmib26Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`bysŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±ÇbnberangeŸ±Ç`a(Ÿ±Çbmib26Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`flabelsŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±ÇbnbdlistŸ±Ç`a(Ÿ±Çbs1a'Ÿ±Çbs1xabcdefghijklmnopqrstuvwxyzŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±ÇakcdefŸ±Ç`a Ÿ±Çbnfiformat_fnŸ±Ç`a(Ÿ±Ç`htick_valŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`htick_posŸ±Ç`a)Ÿ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±ÇakbifŸ±Ç`a Ÿ±ÇbnbcintŸ±Ç`a(Ÿ±Ç`htick_valŸ±Ç`a)Ÿ±Ç`a Ÿ±ÇbowbinŸ±Ç`a Ÿ±Ç`bxsŸ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±ÇakfreturnŸ±Ç`a Ÿ±Ç`flabelsŸ±Ç`a[Ÿ±ÇbnbcintŸ±Ç`a(Ÿ±Ç`htick_valŸ±Ç`a)Ÿ±Ç`a]Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±ÇakdelseŸ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±ÇakfreturnŸ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1a'Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1x+# A FuncFormatter is created automatically.Ÿ±Ç`a
Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`exaxisŸ±Çaoa.Ÿ±Ç`sset_major_formatterŸ±Ç`a(Ÿ±Ç`iformat_fnŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`exaxisŸ±Çaoa.Ÿ±Ç`qset_major_locatorŸ±Ç`a(Ÿ±Ç`kMaxNLocatorŸ±Ç`a(Ÿ±Ç`gintegerŸ±Çaoa=Ÿ±ÇbkcdTrueŸ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`dplotŸ±Ç`a(Ÿ±Ç`bxsŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`bysŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`dshowŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1xM#############################################################################Ÿ±Ç`a
Ÿ±Çbc1a#Ÿ±Ç`a
Ÿ±Çbc1x# .. admonition:: ReferencesŸ±Ç`a
Ÿ±Çbc1a#Ÿ±Ç`a
Ÿ±Çbc1xN#    The use of the following functions, methods, classes and modules is shownŸ±Ç`a
Ÿ±Çbc1u#    in this example:Ÿ±Ç`a
Ÿ±Çbc1a#Ÿ±Ç`a
Ÿ±Çbc1x##    - `matplotlib.pyplot.subplots`Ÿ±Ç`a
Ÿ±Çbc1x1#    - `matplotlib.axis.Axis.set_major_formatter`Ÿ±Ç`a
Ÿ±Çbc1x/#    - `matplotlib.axis.Axis.set_major_locator`Ÿ±Ç`a
Ÿ±Çbc1x(#    - `matplotlib.ticker.FuncFormatter`Ÿ±Ç`a
Ÿ±Çbc1x&#    - `matplotlib.ticker.MaxNLocator`Ÿ±Ç`a
`dNoneˆ