Ù¯‚Ù´ƒ˜ÖÙ±‚bsdy¦"""
======================
Plotting with keywords
======================

There are some instances where you have data in a format that lets you
access particular variables with strings: for example, with
`numpy.recarray` or `pandas.DataFrame`.

Matplotlib allows you provide such an object with the ``data`` keyword
argument. If provided, then you may generate plots with the strings
corresponding to these variables.
"""Ù±‚`a
Ù±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„enumpyÙ „enumpyf1.22.3fmoduleenumpyfmoduleõÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnnbnpÙ±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnnfpyplotÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnncpltÙ±‚`a
Ù±‚`bnpÙ±‚aoa.Ù±‚`frandomÙ±‚aoa.Ù±‚`dseedÙ±‚`a(Ù±‚bmih19680801Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`ddataÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`a{Ù±‚bs1a'Ù±‚bs1aaÙ±‚bs1a'Ù±‚`a:Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`farangeÙ±‚`a(Ù±‚bmib50Ù±‚`a)Ù±‚`a,Ù±‚`a
Ù±‚`h        Ù±‚bs1a'Ù±‚bs1acÙ±‚bs1a'Ù±‚`a:Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`frandomÙ±‚aoa.Ù±‚`grandintÙ±‚`a(Ù±‚bmia0Ù±‚`a,Ù±‚`a Ù±‚bmib50Ù±‚`a,Ù±‚`a Ù±‚bmib50Ù±‚`a)Ù±‚`a,Ù±‚`a
Ù±‚`h        Ù±‚bs1a'Ù±‚bs1adÙ±‚bs1a'Ù±‚`a:Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`frandomÙ±‚aoa.Ù±‚`erandnÙ±‚`a(Ù±‚bmib50Ù±‚`a)Ù±‚`a}Ù±‚`a
Ù±‚`ddataÙ±‚`a[Ù±‚bs1a'Ù±‚bs1abÙ±‚bs1a'Ù±‚`a]Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`ddataÙ±‚`a[Ù±‚bs1a'Ù±‚bs1aaÙ±‚bs1a'Ù±‚`a]Ù±‚`a Ù±‚aoa+Ù±‚`a Ù±‚bmib10Ù±‚`a Ù±‚aoa*Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`frandomÙ±‚aoa.Ù±‚`erandnÙ±‚`a(Ù±‚bmib50Ù±‚`a)Ù±‚`a
Ù±‚`ddataÙ±‚`a[Ù±‚bs1a'Ù±‚bs1adÙ±‚bs1a'Ù±‚`a]Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`cabsÙ±‚`a(Ù±‚`ddataÙ±‚`a[Ù±‚bs1a'Ù±‚bs1adÙ±‚bs1a'Ù±‚`a]Ù±‚`a)Ù±‚`a Ù±‚aoa*Ù±‚`a Ù±‚bmic100Ù±‚`a
Ù±‚`a
Ù±‚`cfigÙ±‚`a,Ù±‚`a Ù±‚`baxÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cpltÙ±‚aoa.Ù±‚`hsubplotsÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`gscatterÙ±‚`a(Ù±‚bs1a'Ù±‚bs1aaÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚bs1a'Ù±‚bs1abÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`acÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1acÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`asÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1adÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`ddataÙ±‚aoa=Ù±‚`ddataÙ±‚`a)Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`csetÙ±‚`a(Ù±‚`fxlabelÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1gentry aÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`fylabelÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1gentry bÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`cpltÙ±‚aoa.Ù±‚`dshowÙ±‚`a(Ù±‚`a)Ù±‚`a
`dNoneö