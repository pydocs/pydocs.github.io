ŸØÇÅŸ¥ÉòèŸ±Çbsdyë"""
==============
Custom Ticker1
==============

The new ticker code was designed to explicitly support user customized
ticking. The documentation of :mod:`matplotlib.ticker` details this
process.  That code defines a lot of preset tickers but was primarily
designed to be user extensible.

In this example a user defined function is used to format the ticks in
millions of dollars on the y axis.
"""Ÿ±Ç`a
Ÿ±ÇbknfimportŸ±Ç`a Ÿ±ÇbnnŸ¢ÑjmatplotlibŸ†Ñjmatplotlibe3.5.1fmodulejmatplotlibfmoduleıŸ±Çbnna.Ÿ±ÇbnnfpyplotŸ±Ç`a Ÿ±ÇakbasŸ±Ç`a Ÿ±ÇbnncpltŸ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`emoneyŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`a[Ÿ±Çbmfe1.5e5Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfe2.5e6Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfe5.5e6Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfe2.0e7Ÿ±Ç`a]Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±ÇakcdefŸ±Ç`a Ÿ±ÇbnfhmillionsŸ±Ç`a(Ÿ±Ç`axŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`cposŸ±Ç`a)Ÿ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Çbsdx8"""The two arguments are the value and tick position."""Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±ÇakfreturnŸ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1a$Ÿ±Çbsig{:1.1f}Ÿ±Çbs1aMŸ±Çbs1a'Ÿ±Çaoa.Ÿ±Ç`fformatŸ±Ç`a(Ÿ±Ç`axŸ±Çaoa*Ÿ±Çbmfd1e-6Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`cfigŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`baxŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`hsubplotsŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Çbc1x&# Use automatic FuncFormatter creationŸ±Ç`a
Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`eyaxisŸ±Çaoa.Ÿ±Ç`sset_major_formatterŸ±Ç`a(Ÿ±Ç`hmillionsŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`cbarŸ±Ç`a(Ÿ±Ç`a[Ÿ±Çbs1a'Ÿ±Çbs1dBillŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1dFredŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1dMaryŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1cSueŸ±Çbs1a'Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`emoneyŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`dshowŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
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
Ÿ±Çbc1x(#    - `matplotlib.ticker.FuncFormatter`Ÿ±Ç`a
`dNoneˆ