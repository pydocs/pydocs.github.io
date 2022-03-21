Ù¯‚Ù´ƒ˜øÙ±‚bsdyW"""
==================================
Modifying the coordinate formatter
==================================

Modify the coordinate formatter to report the image "z"
value of the nearest pixel given x and y.
This functionality is built in by default, but it
is still useful to show how to customize the
`~.axes.Axes.format_coord` function.
"""Ù±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„enumpyÙ „enumpyf1.22.3fmoduleenumpyfmoduleõÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnnbnpÙ±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnnfpyplotÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnncpltÙ±‚`a
Ù±‚`a
Ù±‚bc1x)# Fixing random state for reproducibilityÙ±‚`a
Ù±‚`bnpÙ±‚aoa.Ù±‚`frandomÙ±‚aoa.Ù±‚`dseedÙ±‚`a(Ù±‚bmih19680801Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚`aXÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bmib10Ù±‚aoa*Ù±‚`bnpÙ±‚aoa.Ù±‚`frandomÙ±‚aoa.Ù±‚`drandÙ±‚`a(Ù±‚bmia5Ù±‚`a,Ù±‚`a Ù±‚bmia3Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`cfigÙ±‚`a,Ù±‚`a Ù±‚`baxÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cpltÙ±‚aoa.Ù±‚`hsubplotsÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`fimshowÙ±‚`a(Ù±‚`aXÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`gnumrowsÙ±‚`a,Ù±‚`a Ù±‚`gnumcolsÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`aXÙ±‚aoa.Ù±‚`eshapeÙ±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚akcdefÙ±‚`a Ù±‚bnflformat_coordÙ±‚`a(Ù±‚`axÙ±‚`a,Ù±‚`a Ù±‚`ayÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`d    Ù±‚`ccolÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bnbcintÙ±‚`a(Ù±‚`axÙ±‚`a Ù±‚aoa+Ù±‚`a Ù±‚bmfc0.5Ù±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`crowÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bnbcintÙ±‚`a(Ù±‚`ayÙ±‚`a Ù±‚aoa+Ù±‚`a Ù±‚bmfc0.5Ù±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚akbifÙ±‚`a Ù±‚bmia0Ù±‚`a Ù±‚aoa<Ù±‚aoa=Ù±‚`a Ù±‚`ccolÙ±‚`a Ù±‚aoa<Ù±‚`a Ù±‚`gnumcolsÙ±‚`a Ù±‚bowcandÙ±‚`a Ù±‚bmia0Ù±‚`a Ù±‚aoa<Ù±‚aoa=Ù±‚`a Ù±‚`crowÙ±‚`a Ù±‚aoa<Ù±‚`a Ù±‚`gnumrowsÙ±‚`a:Ù±‚`a
Ù±‚`h        Ù±‚`azÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`aXÙ±‚`a[Ù±‚`crowÙ±‚`a,Ù±‚`a Ù±‚`ccolÙ±‚`a]Ù±‚`a
Ù±‚`h        Ù±‚akfreturnÙ±‚`a Ù±‚bs1a'Ù±‚bs1bx=Ù±‚bsie%1.4fÙ±‚bs1d, y=Ù±‚bsie%1.4fÙ±‚bs1d, z=Ù±‚bsie%1.4fÙ±‚bs1a'Ù±‚`a Ù±‚aoa%Ù±‚`a Ù±‚`a(Ù±‚`axÙ±‚`a,Ù±‚`a Ù±‚`ayÙ±‚`a,Ù±‚`a Ù±‚`azÙ±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚akdelseÙ±‚`a:Ù±‚`a
Ù±‚`h        Ù±‚akfreturnÙ±‚`a Ù±‚bs1a'Ù±‚bs1bx=Ù±‚bsie%1.4fÙ±‚bs1d, y=Ù±‚bsie%1.4fÙ±‚bs1a'Ù±‚`a Ù±‚aoa%Ù±‚`a Ù±‚`a(Ù±‚`axÙ±‚`a,Ù±‚`a Ù±‚`ayÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`lformat_coordÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`lformat_coordÙ±‚`a
Ù±‚`cpltÙ±‚aoa.Ù±‚`dshowÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚bc1xM#############################################################################Ù±‚`a
Ù±‚bc1a#Ù±‚`a
Ù±‚bc1x# .. admonition:: ReferencesÙ±‚`a
Ù±‚bc1a#Ù±‚`a
Ù±‚bc1xN#    The use of the following functions, methods, classes and modules is shownÙ±‚`a
Ù±‚bc1u#    in this example:Ù±‚`a
Ù±‚bc1a#Ù±‚`a
Ù±‚bc1x*#    - `matplotlib.axes.Axes.format_coord`Ù±‚`a
Ù±‚bc1x$#    - `matplotlib.axes.Axes.imshow`Ù±‚`a
`dNoneö