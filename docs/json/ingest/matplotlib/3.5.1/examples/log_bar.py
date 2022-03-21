Ù¯‚Ù´ƒ˜şÙ±‚bsdxP"""
=======
Log Bar
=======

Plotting a bar chart with a logarithmic y-axis.
"""Ù±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnnfpyplotÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnncpltÙ±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„enumpyÙ „enumpyf1.22.3fmoduleenumpyfmoduleõÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnnbnpÙ±‚`a
Ù±‚`a
Ù±‚`ddataÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`a(Ù±‚`a(Ù±‚bmia3Ù±‚`a,Ù±‚`a Ù±‚bmid1000Ù±‚`a)Ù±‚`a,Ù±‚`a Ù±‚`a(Ù±‚bmib10Ù±‚`a,Ù±‚`a Ù±‚bmia3Ù±‚`a)Ù±‚`a,Ù±‚`a Ù±‚`a(Ù±‚bmic100Ù±‚`a,Ù±‚`a Ù±‚bmib30Ù±‚`a)Ù±‚`a,Ù±‚`a Ù±‚`a(Ù±‚bmic500Ù±‚`a,Ù±‚`a Ù±‚bmic800Ù±‚`a)Ù±‚`a,Ù±‚`a Ù±‚`a(Ù±‚bmib50Ù±‚`a,Ù±‚`a Ù±‚bmia1Ù±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`cdimÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bnbclenÙ±‚`a(Ù±‚`ddataÙ±‚`a[Ù±‚bmia0Ù±‚`a]Ù±‚`a)Ù±‚`a
Ù±‚`awÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bmfd0.75Ù±‚`a
Ù±‚`ddimwÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`awÙ±‚`a Ù±‚aoa/Ù±‚`a Ù±‚`cdimÙ±‚`a
Ù±‚`a
Ù±‚`cfigÙ±‚`a,Ù±‚`a Ù±‚`baxÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cpltÙ±‚aoa.Ù±‚`hsubplotsÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`axÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`farangeÙ±‚`a(Ù±‚bnbclenÙ±‚`a(Ù±‚`ddataÙ±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚akcforÙ±‚`a Ù±‚`aiÙ±‚`a Ù±‚bowbinÙ±‚`a Ù±‚bnberangeÙ±‚`a(Ù±‚bnbclenÙ±‚`a(Ù±‚`ddataÙ±‚`a[Ù±‚bmia0Ù±‚`a]Ù±‚`a)Ù±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`d    Ù±‚`ayÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`a[Ù±‚`adÙ±‚`a[Ù±‚`aiÙ±‚`a]Ù±‚`a Ù±‚akcforÙ±‚`a Ù±‚`adÙ±‚`a Ù±‚bowbinÙ±‚`a Ù±‚`ddataÙ±‚`a]Ù±‚`a
Ù±‚`d    Ù±‚`abÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`baxÙ±‚aoa.Ù±‚`cbarÙ±‚`a(Ù±‚`axÙ±‚`a Ù±‚aoa+Ù±‚`a Ù±‚`aiÙ±‚`a Ù±‚aoa*Ù±‚`a Ù±‚`ddimwÙ±‚`a,Ù±‚`a Ù±‚`ayÙ±‚`a,Ù±‚`a Ù±‚`ddimwÙ±‚`a,Ù±‚`a Ù±‚`fbottomÙ±‚aoa=Ù±‚bmfe0.001Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`jset_xticksÙ±‚`a(Ù±‚`axÙ±‚`a Ù±‚aoa+Ù±‚`a Ù±‚`ddimwÙ±‚`a Ù±‚aoa/Ù±‚`a Ù±‚bmia2Ù±‚`a,Ù±‚`a Ù±‚`flabelsÙ±‚aoa=Ù±‚bnbcmapÙ±‚`a(Ù±‚bnbcstrÙ±‚`a,Ù±‚`a Ù±‚`axÙ±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`jset_yscaleÙ±‚`a(Ù±‚bs1a'Ù±‚bs1clogÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`jset_xlabelÙ±‚`a(Ù±‚bs1a'Ù±‚bs1axÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`jset_ylabelÙ±‚`a(Ù±‚bs1a'Ù±‚bs1ayÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`cpltÙ±‚aoa.Ù±‚`dshowÙ±‚`a(Ù±‚`a)Ù±‚`a
`dNoneö