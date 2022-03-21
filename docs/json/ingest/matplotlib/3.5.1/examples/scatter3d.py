Ù¯‚Ù´ƒ™Ù±‚bsdxa"""
==============
3D scatterplot
==============

Demonstration of a basic scatterplot in 3D.
"""Ù±‚`a
Ù±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnnfpyplotÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnncpltÙ±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„enumpyÙ „enumpyf1.22.3fmoduleenumpyfmoduleõÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnnbnpÙ±‚`a
Ù±‚`a
Ù±‚bc1x)# Fixing random state for reproducibilityÙ±‚`a
Ù±‚`bnpÙ±‚aoa.Ù±‚`frandomÙ±‚aoa.Ù±‚`dseedÙ±‚`a(Ù±‚bmih19680801Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚akcdefÙ±‚`a Ù±‚bnfirandrangeÙ±‚`a(Ù±‚`anÙ±‚`a,Ù±‚`a Ù±‚`dvminÙ±‚`a,Ù±‚`a Ù±‚`dvmaxÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`d    Ù±‚bsdx‹"""
    Helper function to make an array of random numbers having shape (n, )
    with each number distributed Uniform(vmin, vmax).
    """Ù±‚`a
Ù±‚`d    Ù±‚akfreturnÙ±‚`a Ù±‚`a(Ù±‚`dvmaxÙ±‚`a Ù±‚aoa-Ù±‚`a Ù±‚`dvminÙ±‚`a)Ù±‚aoa*Ù±‚`bnpÙ±‚aoa.Ù±‚`frandomÙ±‚aoa.Ù±‚`drandÙ±‚`a(Ù±‚`anÙ±‚`a)Ù±‚`a Ù±‚aoa+Ù±‚`a Ù±‚`dvminÙ±‚`a
Ù±‚`a
Ù±‚`cfigÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cpltÙ±‚aoa.Ù±‚`ffigureÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`baxÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cfigÙ±‚aoa.Ù±‚`kadd_subplotÙ±‚`a(Ù±‚`jprojectionÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1b3dÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`anÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bmic100Ù±‚`a
Ù±‚`a
Ù±‚bc1xK# For each set of style and range settings, plot n random points in the boxÙ±‚`a
Ù±‚bc1x># defined by x in [23, 32], y in [0, 100], z in [zlow, zhigh].Ù±‚`a
Ù±‚akcforÙ±‚`a Ù±‚`amÙ±‚`a,Ù±‚`a Ù±‚`dzlowÙ±‚`a,Ù±‚`a Ù±‚`ezhighÙ±‚`a Ù±‚bowbinÙ±‚`a Ù±‚`a[Ù±‚`a(Ù±‚bs1a'Ù±‚bs1aoÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚aoa-Ù±‚bmib50Ù±‚`a,Ù±‚`a Ù±‚aoa-Ù±‚bmib25Ù±‚`a)Ù±‚`a,Ù±‚`a Ù±‚`a(Ù±‚bs1a'Ù±‚bs1a^Ù±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚aoa-Ù±‚bmib30Ù±‚`a,Ù±‚`a Ù±‚aoa-Ù±‚bmia5Ù±‚`a)Ù±‚`a]Ù±‚`a:Ù±‚`a
Ù±‚`d    Ù±‚`bxsÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`irandrangeÙ±‚`a(Ù±‚`anÙ±‚`a,Ù±‚`a Ù±‚bmib23Ù±‚`a,Ù±‚`a Ù±‚bmib32Ù±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`bysÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`irandrangeÙ±‚`a(Ù±‚`anÙ±‚`a,Ù±‚`a Ù±‚bmia0Ù±‚`a,Ù±‚`a Ù±‚bmic100Ù±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`bzsÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`irandrangeÙ±‚`a(Ù±‚`anÙ±‚`a,Ù±‚`a Ù±‚`dzlowÙ±‚`a,Ù±‚`a Ù±‚`ezhighÙ±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`baxÙ±‚aoa.Ù±‚`gscatterÙ±‚`a(Ù±‚`bxsÙ±‚`a,Ù±‚`a Ù±‚`bysÙ±‚`a,Ù±‚`a Ù±‚`bzsÙ±‚`a,Ù±‚`a Ù±‚`fmarkerÙ±‚aoa=Ù±‚`amÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`jset_xlabelÙ±‚`a(Ù±‚bs1a'Ù±‚bs1gX LabelÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`jset_ylabelÙ±‚`a(Ù±‚bs1a'Ù±‚bs1gY LabelÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`jset_zlabelÙ±‚`a(Ù±‚bs1a'Ù±‚bs1gZ LabelÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`cpltÙ±‚aoa.Ù±‚`dshowÙ±‚`a(Ù±‚`a)Ù±‚`a
`dNoneö