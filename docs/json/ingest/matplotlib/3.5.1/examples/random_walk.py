Ù¯‚Ù´ƒ™›Ù±‚bsdxP"""
=======================
Animated 3D random walk
=======================

"""Ù±‚`a
Ù±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„enumpyÙ „enumpyf1.22.3fmoduleenumpyfmoduleõÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnnbnpÙ±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnnfpyplotÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnncpltÙ±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnnianimationÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnnianimationÙ±‚`a
Ù±‚`a
Ù±‚bc1x)# Fixing random state for reproducibilityÙ±‚`a
Ù±‚`bnpÙ±‚aoa.Ù±‚`frandomÙ±‚aoa.Ù±‚`dseedÙ±‚`a(Ù±‚bmih19680801Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚akcdefÙ±‚`a Ù±‚bnfkrandom_walkÙ±‚`a(Ù±‚`inum_stepsÙ±‚`a,Ù±‚`a Ù±‚`hmax_stepÙ±‚aoa=Ù±‚bmfd0.05Ù±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`d    Ù±‚bsdx6"""Return a 3D random walk as (num_steps, 3) array."""Ù±‚`a
Ù±‚`d    Ù±‚`istart_posÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`frandomÙ±‚aoa.Ù±‚`frandomÙ±‚`a(Ù±‚bmia3Ù±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`estepsÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`frandomÙ±‚aoa.Ù±‚`guniformÙ±‚`a(Ù±‚aoa-Ù±‚`hmax_stepÙ±‚`a,Ù±‚`a Ù±‚`hmax_stepÙ±‚`a,Ù±‚`a Ù±‚`dsizeÙ±‚aoa=Ù±‚`a(Ù±‚`inum_stepsÙ±‚`a,Ù±‚`a Ù±‚bmia3Ù±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`dwalkÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`istart_posÙ±‚`a Ù±‚aoa+Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`fcumsumÙ±‚`a(Ù±‚`estepsÙ±‚`a,Ù±‚`a Ù±‚`daxisÙ±‚aoa=Ù±‚bmia0Ù±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚akfreturnÙ±‚`a Ù±‚`dwalkÙ±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚akcdefÙ±‚`a Ù±‚bnflupdate_linesÙ±‚`a(Ù±‚`cnumÙ±‚`a,Ù±‚`a Ù±‚`ewalksÙ±‚`a,Ù±‚`a Ù±‚`elinesÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`d    Ù±‚akcforÙ±‚`a Ù±‚`dlineÙ±‚`a,Ù±‚`a Ù±‚`dwalkÙ±‚`a Ù±‚bowbinÙ±‚`a Ù±‚bnbczipÙ±‚`a(Ù±‚`elinesÙ±‚`a,Ù±‚`a Ù±‚`ewalksÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`h        Ù±‚bc1x1# NOTE: there is no .set_data() for 3 dim data...Ù±‚`a
Ù±‚`h        Ù±‚`dlineÙ±‚aoa.Ù±‚`hset_dataÙ±‚`a(Ù±‚`dwalkÙ±‚`a[Ù±‚`a:Ù±‚`cnumÙ±‚`a,Ù±‚`a Ù±‚`a:Ù±‚bmia2Ù±‚`a]Ù±‚aoa.Ù±‚`aTÙ±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚`dlineÙ±‚aoa.Ù±‚`qset_3d_propertiesÙ±‚`a(Ù±‚`dwalkÙ±‚`a[Ù±‚`a:Ù±‚`cnumÙ±‚`a,Ù±‚`a Ù±‚bmia2Ù±‚`a]Ù±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚akfreturnÙ±‚`a Ù±‚`elinesÙ±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚bc1x0# Data: 40 random walks as (num_steps, 3) arraysÙ±‚`a
Ù±‚`inum_stepsÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bmib30Ù±‚`a
Ù±‚`ewalksÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`a[Ù±‚`krandom_walkÙ±‚`a(Ù±‚`inum_stepsÙ±‚`a)Ù±‚`a Ù±‚akcforÙ±‚`a Ù±‚`eindexÙ±‚`a Ù±‚bowbinÙ±‚`a Ù±‚bnberangeÙ±‚`a(Ù±‚bmib40Ù±‚`a)Ù±‚`a]Ù±‚`a
Ù±‚`a
Ù±‚bc1x!# Attaching 3D axis to the figureÙ±‚`a
Ù±‚`cfigÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cpltÙ±‚aoa.Ù±‚`ffigureÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`baxÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cfigÙ±‚aoa.Ù±‚`kadd_subplotÙ±‚`a(Ù±‚`jprojectionÙ±‚aoa=Ù±‚bs2a"Ù±‚bs2b3dÙ±‚bs2a"Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚bc1x%# Create lines initially without dataÙ±‚`a
Ù±‚`elinesÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`a[Ù±‚`baxÙ±‚aoa.Ù±‚`dplotÙ±‚`a(Ù±‚`a[Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`a[Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`a[Ù±‚`a]Ù±‚`a)Ù±‚`a[Ù±‚bmia0Ù±‚`a]Ù±‚`a Ù±‚akcforÙ±‚`a Ù±‚`a_Ù±‚`a Ù±‚bowbinÙ±‚`a Ù±‚`ewalksÙ±‚`a]Ù±‚`a
Ù±‚`a
Ù±‚bc1x# Setting the axes propertiesÙ±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`csetÙ±‚`a(Ù±‚`fxlim3dÙ±‚aoa=Ù±‚`a(Ù±‚bmia0Ù±‚`a,Ù±‚`a Ù±‚bmia1Ù±‚`a)Ù±‚`a,Ù±‚`a Ù±‚`fxlabelÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1aXÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`csetÙ±‚`a(Ù±‚`fylim3dÙ±‚aoa=Ù±‚`a(Ù±‚bmia0Ù±‚`a,Ù±‚`a Ù±‚bmia1Ù±‚`a)Ù±‚`a,Ù±‚`a Ù±‚`fylabelÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1aYÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`csetÙ±‚`a(Ù±‚`fzlim3dÙ±‚aoa=Ù±‚`a(Ù±‚bmia0Ù±‚`a,Ù±‚`a Ù±‚bmia1Ù±‚`a)Ù±‚`a,Ù±‚`a Ù±‚`fzlabelÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1aZÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚bc1x# Creating the Animation objectÙ±‚`a
Ù±‚`caniÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`ianimationÙ±‚aoa.Ù±‚`mFuncAnimationÙ±‚`a(Ù±‚`a
Ù±‚`d    Ù±‚`cfigÙ±‚`a,Ù±‚`a Ù±‚`lupdate_linesÙ±‚`a,Ù±‚`a Ù±‚`inum_stepsÙ±‚`a,Ù±‚`a Ù±‚`efargsÙ±‚aoa=Ù±‚`a(Ù±‚`ewalksÙ±‚`a,Ù±‚`a Ù±‚`elinesÙ±‚`a)Ù±‚`a,Ù±‚`a Ù±‚`hintervalÙ±‚aoa=Ù±‚bmic100Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`cpltÙ±‚aoa.Ù±‚`dshowÙ±‚`a(Ù±‚`a)Ù±‚`a
`dNoneö