Ù¯‚Ù´ƒ™Ù±‚bsdx¦"""
==============================
Create 3D histogram of 2D data
==============================

Demo of a histogram for 2 dimensional data as a bar graph in 3D.
"""Ù±‚`a
Ù±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnnfpyplotÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnncpltÙ±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„enumpyÙ „enumpyf1.22.3fmoduleenumpyfmoduleõÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnnbnpÙ±‚`a
Ù±‚`a
Ù±‚bc1x)# Fixing random state for reproducibilityÙ±‚`a
Ù±‚`bnpÙ±‚aoa.Ù±‚`frandomÙ±‚aoa.Ù±‚`dseedÙ±‚`a(Ù±‚bmih19680801Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚`cfigÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cpltÙ±‚aoa.Ù±‚`ffigureÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`baxÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cfigÙ±‚aoa.Ù±‚`kadd_subplotÙ±‚`a(Ù±‚`jprojectionÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1b3dÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`axÙ±‚`a,Ù±‚`a Ù±‚`ayÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`frandomÙ±‚aoa.Ù±‚`drandÙ±‚`a(Ù±‚bmia2Ù±‚`a,Ù±‚`a Ù±‚bmic100Ù±‚`a)Ù±‚`a Ù±‚aoa*Ù±‚`a Ù±‚bmia4Ù±‚`a
Ù±‚`dhistÙ±‚`a,Ù±‚`a Ù±‚`fxedgesÙ±‚`a,Ù±‚`a Ù±‚`fyedgesÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`khistogram2dÙ±‚`a(Ù±‚`axÙ±‚`a,Ù±‚`a Ù±‚`ayÙ±‚`a,Ù±‚`a Ù±‚`dbinsÙ±‚aoa=Ù±‚bmia4Ù±‚`a,Ù±‚`a Ù±‚bnberangeÙ±‚aoa=Ù±‚`a[Ù±‚`a[Ù±‚bmia0Ù±‚`a,Ù±‚`a Ù±‚bmia4Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`a[Ù±‚bmia0Ù±‚`a,Ù±‚`a Ù±‚bmia4Ù±‚`a]Ù±‚`a]Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚bc1x;# Construct arrays for the anchor positions of the 16 bars.Ù±‚`a
Ù±‚`dxposÙ±‚`a,Ù±‚`a Ù±‚`dyposÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`hmeshgridÙ±‚`a(Ù±‚`fxedgesÙ±‚`a[Ù±‚`a:Ù±‚aoa-Ù±‚bmia1Ù±‚`a]Ù±‚`a Ù±‚aoa+Ù±‚`a Ù±‚bmfd0.25Ù±‚`a,Ù±‚`a Ù±‚`fyedgesÙ±‚`a[Ù±‚`a:Ù±‚aoa-Ù±‚bmia1Ù±‚`a]Ù±‚`a Ù±‚aoa+Ù±‚`a Ù±‚bmfd0.25Ù±‚`a,Ù±‚`a Ù±‚`hindexingÙ±‚aoa=Ù±‚bs2a"Ù±‚bs2bijÙ±‚bs2a"Ù±‚`a)Ù±‚`a
Ù±‚`dxposÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`dxposÙ±‚aoa.Ù±‚`eravelÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`dyposÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`dyposÙ±‚aoa.Ù±‚`eravelÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`dzposÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bmia0Ù±‚`a
Ù±‚`a
Ù±‚bc1x7# Construct arrays with the dimensions for the 16 bars.Ù±‚`a
Ù±‚`bdxÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bdyÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bmfc0.5Ù±‚`a Ù±‚aoa*Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`iones_likeÙ±‚`a(Ù±‚`dzposÙ±‚`a)Ù±‚`a
Ù±‚`bdzÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`dhistÙ±‚aoa.Ù±‚`eravelÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`ebar3dÙ±‚`a(Ù±‚`dxposÙ±‚`a,Ù±‚`a Ù±‚`dyposÙ±‚`a,Ù±‚`a Ù±‚`dzposÙ±‚`a,Ù±‚`a Ù±‚`bdxÙ±‚`a,Ù±‚`a Ù±‚`bdyÙ±‚`a,Ù±‚`a Ù±‚`bdzÙ±‚`a,Ù±‚`a Ù±‚`ezsortÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1gaverageÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`cpltÙ±‚aoa.Ù±‚`dshowÙ±‚`a(Ù±‚`a)Ù±‚`a
`dNoneö