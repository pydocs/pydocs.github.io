ŸØÇÅŸ¥Éô@Ÿ±Çbsdy
"""
===========================
The double pendulum problem
===========================

This animation illustrates the double pendulum problem.

Double pendulum formula translated from the C code at
http://www.physics.usyd.edu.au/~wheat/dpend_html/solve_dpend.c
"""Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±ÇbkndfromŸ±Ç`a Ÿ±ÇbnnŸ¢ÑenumpyŸ†Ñenumpyf1.22.3fmoduleenumpyfmoduleıŸ±Ç`a Ÿ±ÇbknfimportŸ±Ç`a Ÿ±Ç`csinŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ccosŸ±Ç`a
Ÿ±ÇbknfimportŸ±Ç`a Ÿ±ÇbnnŸ¢ÑenumpyŸ†Ñenumpyf1.22.3fmoduleenumpyfmoduleıŸ±Ç`a Ÿ±ÇakbasŸ±Ç`a Ÿ±ÇbnnbnpŸ±Ç`a
Ÿ±ÇbknfimportŸ±Ç`a Ÿ±ÇbnnŸ¢ÑjmatplotlibŸ†Ñjmatplotlibe3.5.1fmodulejmatplotlibfmoduleıŸ±Çbnna.Ÿ±ÇbnnfpyplotŸ±Ç`a Ÿ±ÇakbasŸ±Ç`a Ÿ±ÇbnncpltŸ±Ç`a
Ÿ±ÇbknfimportŸ±Ç`a Ÿ±ÇbnnŸ¢ÑescipyŸ†Ñescipye1.8.0fmoduleescipyfmoduleıŸ±Çbnna.Ÿ±ÇbnniintegrateŸ±Ç`a Ÿ±ÇakbasŸ±Ç`a Ÿ±ÇbnniintegrateŸ±Ç`a
Ÿ±ÇbknfimportŸ±Ç`a Ÿ±ÇbnnŸ¢ÑjmatplotlibŸ†Ñjmatplotlibe3.5.1fmodulejmatplotlibfmoduleıŸ±Çbnna.Ÿ±ÇbnnianimationŸ±Ç`a Ÿ±ÇakbasŸ±Ç`a Ÿ±ÇbnnianimationŸ±Ç`a
Ÿ±ÇbkndfromŸ±Ç`a Ÿ±ÇbnnkcollectionsŸ±Ç`a Ÿ±ÇbknfimportŸ±Ç`a Ÿ±Ç`edequeŸ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`aGŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Çbmfc9.8Ÿ±Ç`b  Ÿ±Çbc1x'# acceleration due to gravity, in m/s^2Ÿ±Ç`a
Ÿ±Ç`bL1Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Çbmfc1.0Ÿ±Ç`b  Ÿ±Çbc1x# length of pendulum 1 in mŸ±Ç`a
Ÿ±Ç`bL2Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Çbmfc1.0Ÿ±Ç`b  Ÿ±Çbc1x# length of pendulum 2 in mŸ±Ç`a
Ÿ±Ç`aLŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bL1Ÿ±Ç`a Ÿ±Çaoa+Ÿ±Ç`a Ÿ±Ç`bL2Ÿ±Ç`b  Ÿ±Çbc1x)# maximal length of the combined pendulumŸ±Ç`a
Ÿ±Ç`bM1Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Çbmfc1.0Ÿ±Ç`b  Ÿ±Çbc1x# mass of pendulum 1 in kgŸ±Ç`a
Ÿ±Ç`bM2Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Çbmfc1.0Ÿ±Ç`b  Ÿ±Çbc1x# mass of pendulum 2 in kgŸ±Ç`a
Ÿ±Ç`ft_stopŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Çbmia5Ÿ±Ç`b  Ÿ±Çbc1x# how many seconds to simulateŸ±Ç`a
Ÿ±Ç`khistory_lenŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Çbmic500Ÿ±Ç`b  Ÿ±Çbc1x'# how many trajectory points to displayŸ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±ÇakcdefŸ±Ç`a Ÿ±ÇbnffderivsŸ±Ç`a(Ÿ±Ç`estateŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`atŸ±Ç`a)Ÿ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`ddydxŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`jzeros_likeŸ±Ç`a(Ÿ±Ç`estateŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`ddydxŸ±Ç`a[Ÿ±Çbmia0Ÿ±Ç`a]Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`estateŸ±Ç`a[Ÿ±Çbmia1Ÿ±Ç`a]Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`edeltaŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`estateŸ±Ç`a[Ÿ±Çbmia2Ÿ±Ç`a]Ÿ±Ç`a Ÿ±Çaoa-Ÿ±Ç`a Ÿ±Ç`estateŸ±Ç`a[Ÿ±Çbmia0Ÿ±Ç`a]Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`dden1Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`a(Ÿ±Ç`bM1Ÿ±Çaoa+Ÿ±Ç`bM2Ÿ±Ç`a)Ÿ±Ç`a Ÿ±Çaoa*Ÿ±Ç`a Ÿ±Ç`bL1Ÿ±Ç`a Ÿ±Çaoa-Ÿ±Ç`a Ÿ±Ç`bM2Ÿ±Ç`a Ÿ±Çaoa*Ÿ±Ç`a Ÿ±Ç`bL1Ÿ±Ç`a Ÿ±Çaoa*Ÿ±Ç`a Ÿ±Ç`ccosŸ±Ç`a(Ÿ±Ç`edeltaŸ±Ç`a)Ÿ±Ç`a Ÿ±Çaoa*Ÿ±Ç`a Ÿ±Ç`ccosŸ±Ç`a(Ÿ±Ç`edeltaŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`ddydxŸ±Ç`a[Ÿ±Çbmia1Ÿ±Ç`a]Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`a(Ÿ±Ç`a(Ÿ±Ç`bM2Ÿ±Ç`a Ÿ±Çaoa*Ÿ±Ç`a Ÿ±Ç`bL1Ÿ±Ç`a Ÿ±Çaoa*Ÿ±Ç`a Ÿ±Ç`estateŸ±Ç`a[Ÿ±Çbmia1Ÿ±Ç`a]Ÿ±Ç`a Ÿ±Çaoa*Ÿ±Ç`a Ÿ±Ç`estateŸ±Ç`a[Ÿ±Çbmia1Ÿ±Ç`a]Ÿ±Ç`a Ÿ±Çaoa*Ÿ±Ç`a Ÿ±Ç`csinŸ±Ç`a(Ÿ±Ç`edeltaŸ±Ç`a)Ÿ±Ç`a Ÿ±Çaoa*Ÿ±Ç`a Ÿ±Ç`ccosŸ±Ç`a(Ÿ±Ç`edeltaŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`p                Ÿ±Çaoa+Ÿ±Ç`a Ÿ±Ç`bM2Ÿ±Ç`a Ÿ±Çaoa*Ÿ±Ç`a Ÿ±Ç`aGŸ±Ç`a Ÿ±Çaoa*Ÿ±Ç`a Ÿ±Ç`csinŸ±Ç`a(Ÿ±Ç`estateŸ±Ç`a[Ÿ±Çbmia2Ÿ±Ç`a]Ÿ±Ç`a)Ÿ±Ç`a Ÿ±Çaoa*Ÿ±Ç`a Ÿ±Ç`ccosŸ±Ç`a(Ÿ±Ç`edeltaŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`p                Ÿ±Çaoa+Ÿ±Ç`a Ÿ±Ç`bM2Ÿ±Ç`a Ÿ±Çaoa*Ÿ±Ç`a Ÿ±Ç`bL2Ÿ±Ç`a Ÿ±Çaoa*Ÿ±Ç`a Ÿ±Ç`estateŸ±Ç`a[Ÿ±Çbmia3Ÿ±Ç`a]Ÿ±Ç`a Ÿ±Çaoa*Ÿ±Ç`a Ÿ±Ç`estateŸ±Ç`a[Ÿ±Çbmia3Ÿ±Ç`a]Ÿ±Ç`a Ÿ±Çaoa*Ÿ±Ç`a Ÿ±Ç`csinŸ±Ç`a(Ÿ±Ç`edeltaŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`p                Ÿ±Çaoa-Ÿ±Ç`a Ÿ±Ç`a(Ÿ±Ç`bM1Ÿ±Çaoa+Ÿ±Ç`bM2Ÿ±Ç`a)Ÿ±Ç`a Ÿ±Çaoa*Ÿ±Ç`a Ÿ±Ç`aGŸ±Ç`a Ÿ±Çaoa*Ÿ±Ç`a Ÿ±Ç`csinŸ±Ç`a(Ÿ±Ç`estateŸ±Ç`a[Ÿ±Çbmia0Ÿ±Ç`a]Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`o               Ÿ±Çaoa/Ÿ±Ç`a Ÿ±Ç`dden1Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`ddydxŸ±Ç`a[Ÿ±Çbmia2Ÿ±Ç`a]Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`estateŸ±Ç`a[Ÿ±Çbmia3Ÿ±Ç`a]Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`dden2Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`a(Ÿ±Ç`bL2Ÿ±Çaoa/Ÿ±Ç`bL1Ÿ±Ç`a)Ÿ±Ç`a Ÿ±Çaoa*Ÿ±Ç`a Ÿ±Ç`dden1Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`ddydxŸ±Ç`a[Ÿ±Çbmia3Ÿ±Ç`a]Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`a(Ÿ±Ç`a(Ÿ±Çaoa-Ÿ±Ç`a Ÿ±Ç`bM2Ÿ±Ç`a Ÿ±Çaoa*Ÿ±Ç`a Ÿ±Ç`bL2Ÿ±Ç`a Ÿ±Çaoa*Ÿ±Ç`a Ÿ±Ç`estateŸ±Ç`a[Ÿ±Çbmia3Ÿ±Ç`a]Ÿ±Ç`a Ÿ±Çaoa*Ÿ±Ç`a Ÿ±Ç`estateŸ±Ç`a[Ÿ±Çbmia3Ÿ±Ç`a]Ÿ±Ç`a Ÿ±Çaoa*Ÿ±Ç`a Ÿ±Ç`csinŸ±Ç`a(Ÿ±Ç`edeltaŸ±Ç`a)Ÿ±Ç`a Ÿ±Çaoa*Ÿ±Ç`a Ÿ±Ç`ccosŸ±Ç`a(Ÿ±Ç`edeltaŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`p                Ÿ±Çaoa+Ÿ±Ç`a Ÿ±Ç`a(Ÿ±Ç`bM1Ÿ±Çaoa+Ÿ±Ç`bM2Ÿ±Ç`a)Ÿ±Ç`a Ÿ±Çaoa*Ÿ±Ç`a Ÿ±Ç`aGŸ±Ç`a Ÿ±Çaoa*Ÿ±Ç`a Ÿ±Ç`csinŸ±Ç`a(Ÿ±Ç`estateŸ±Ç`a[Ÿ±Çbmia0Ÿ±Ç`a]Ÿ±Ç`a)Ÿ±Ç`a Ÿ±Çaoa*Ÿ±Ç`a Ÿ±Ç`ccosŸ±Ç`a(Ÿ±Ç`edeltaŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`p                Ÿ±Çaoa-Ÿ±Ç`a Ÿ±Ç`a(Ÿ±Ç`bM1Ÿ±Çaoa+Ÿ±Ç`bM2Ÿ±Ç`a)Ÿ±Ç`a Ÿ±Çaoa*Ÿ±Ç`a Ÿ±Ç`bL1Ÿ±Ç`a Ÿ±Çaoa*Ÿ±Ç`a Ÿ±Ç`estateŸ±Ç`a[Ÿ±Çbmia1Ÿ±Ç`a]Ÿ±Ç`a Ÿ±Çaoa*Ÿ±Ç`a Ÿ±Ç`estateŸ±Ç`a[Ÿ±Çbmia1Ÿ±Ç`a]Ÿ±Ç`a Ÿ±Çaoa*Ÿ±Ç`a Ÿ±Ç`csinŸ±Ç`a(Ÿ±Ç`edeltaŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`p                Ÿ±Çaoa-Ÿ±Ç`a Ÿ±Ç`a(Ÿ±Ç`bM1Ÿ±Çaoa+Ÿ±Ç`bM2Ÿ±Ç`a)Ÿ±Ç`a Ÿ±Çaoa*Ÿ±Ç`a Ÿ±Ç`aGŸ±Ç`a Ÿ±Çaoa*Ÿ±Ç`a Ÿ±Ç`csinŸ±Ç`a(Ÿ±Ç`estateŸ±Ç`a[Ÿ±Çbmia2Ÿ±Ç`a]Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`o               Ÿ±Çaoa/Ÿ±Ç`a Ÿ±Ç`dden2Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±ÇakfreturnŸ±Ç`a Ÿ±Ç`ddydxŸ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1xA# create a time array from 0..t_stop sampled at 0.02 second stepsŸ±Ç`a
Ÿ±Ç`bdtŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Çbmfd0.02Ÿ±Ç`a
Ÿ±Ç`atŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`farangeŸ±Ç`a(Ÿ±Çbmia0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ft_stopŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`bdtŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1x.# th1 and th2 are the initial angles (degrees)Ÿ±Ç`a
Ÿ±Çbc1xE# w10 and w20 are the initial angular velocities (degrees per second)Ÿ±Ç`a
Ÿ±Ç`cth1Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Çbmfe120.0Ÿ±Ç`a
Ÿ±Ç`bw1Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Çbmfc0.0Ÿ±Ç`a
Ÿ±Ç`cth2Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Çaoa-Ÿ±Çbmfd10.0Ÿ±Ç`a
Ÿ±Ç`bw2Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Çbmfc0.0Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1o# initial stateŸ±Ç`a
Ÿ±Ç`estateŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`gradiansŸ±Ç`a(Ÿ±Ç`a[Ÿ±Ç`cth1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`bw1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`cth2Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`bw2Ÿ±Ç`a]Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1x+# integrate your ODE using scipy.integrate.Ÿ±Ç`a
Ÿ±Ç`ayŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`iintegrateŸ±Çaoa.Ÿ±Ç`fodeintŸ±Ç`a(Ÿ±Ç`fderivsŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`estateŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`atŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`bx1Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bL1Ÿ±Çaoa*Ÿ±Ç`csinŸ±Ç`a(Ÿ±Ç`ayŸ±Ç`a[Ÿ±Ç`a:Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia0Ÿ±Ç`a]Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`by1Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Çaoa-Ÿ±Ç`bL1Ÿ±Çaoa*Ÿ±Ç`ccosŸ±Ç`a(Ÿ±Ç`ayŸ±Ç`a[Ÿ±Ç`a:Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia0Ÿ±Ç`a]Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`bx2Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bL2Ÿ±Çaoa*Ÿ±Ç`csinŸ±Ç`a(Ÿ±Ç`ayŸ±Ç`a[Ÿ±Ç`a:Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia2Ÿ±Ç`a]Ÿ±Ç`a)Ÿ±Ç`a Ÿ±Çaoa+Ÿ±Ç`a Ÿ±Ç`bx1Ÿ±Ç`a
Ÿ±Ç`by2Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Çaoa-Ÿ±Ç`bL2Ÿ±Çaoa*Ÿ±Ç`ccosŸ±Ç`a(Ÿ±Ç`ayŸ±Ç`a[Ÿ±Ç`a:Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia2Ÿ±Ç`a]Ÿ±Ç`a)Ÿ±Ç`a Ÿ±Çaoa+Ÿ±Ç`a Ÿ±Ç`by1Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`cfigŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`ffigureŸ±Ç`a(Ÿ±Ç`gfigsizeŸ±Çaoa=Ÿ±Ç`a(Ÿ±Çbmia5Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia4Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`baxŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cfigŸ±Çaoa.Ÿ±Ç`kadd_subplotŸ±Ç`a(Ÿ±Ç`lautoscale_onŸ±Çaoa=Ÿ±ÇbkceFalseŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dxlimŸ±Çaoa=Ÿ±Ç`a(Ÿ±Çaoa-Ÿ±Ç`aLŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`aLŸ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dylimŸ±Çaoa=Ÿ±Ç`a(Ÿ±Çaoa-Ÿ±Ç`aLŸ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfb1.Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`jset_aspectŸ±Ç`a(Ÿ±Çbs1a'Ÿ±Çbs1eequalŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`dgridŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`dlineŸ±Ç`a,Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`dplotŸ±Ç`a(Ÿ±Ç`a[Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`a[Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1bo-Ÿ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`blwŸ±Çaoa=Ÿ±Çbmia2Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`etraceŸ±Ç`a,Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`dplotŸ±Ç`a(Ÿ±Ç`a[Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`a[Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1b.-Ÿ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`blwŸ±Çaoa=Ÿ±Çbmia1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`bmsŸ±Çaoa=Ÿ±Çbmia2Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`mtime_templateŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1gtime = Ÿ±Çbsid%.1fŸ±Çbs1asŸ±Çbs1a'Ÿ±Ç`a
Ÿ±Ç`itime_textŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`dtextŸ±Ç`a(Ÿ±Çbmfd0.05Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfc0.9Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`itransformŸ±Çaoa=Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`itransAxesŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`ihistory_xŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ihistory_yŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`edequeŸ±Ç`a(Ÿ±Ç`fmaxlenŸ±Çaoa=Ÿ±Ç`khistory_lenŸ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`edequeŸ±Ç`a(Ÿ±Ç`fmaxlenŸ±Çaoa=Ÿ±Ç`khistory_lenŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±ÇakcdefŸ±Ç`a Ÿ±ÇbnfganimateŸ±Ç`a(Ÿ±Ç`aiŸ±Ç`a)Ÿ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`ethisxŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`a[Ÿ±Çbmia0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`bx1Ÿ±Ç`a[Ÿ±Ç`aiŸ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`bx2Ÿ±Ç`a[Ÿ±Ç`aiŸ±Ç`a]Ÿ±Ç`a]Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`ethisyŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`a[Ÿ±Çbmia0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`by1Ÿ±Ç`a[Ÿ±Ç`aiŸ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`by2Ÿ±Ç`a[Ÿ±Ç`aiŸ±Ç`a]Ÿ±Ç`a]Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±ÇakbifŸ±Ç`a Ÿ±Ç`aiŸ±Ç`a Ÿ±Çaob==Ÿ±Ç`a Ÿ±Çbmia0Ÿ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±Ç`ihistory_xŸ±Çaoa.Ÿ±Ç`eclearŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±Ç`ihistory_yŸ±Çaoa.Ÿ±Ç`eclearŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`ihistory_xŸ±Çaoa.Ÿ±Ç`jappendleftŸ±Ç`a(Ÿ±Ç`ethisxŸ±Ç`a[Ÿ±Çbmia2Ÿ±Ç`a]Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`ihistory_yŸ±Çaoa.Ÿ±Ç`jappendleftŸ±Ç`a(Ÿ±Ç`ethisyŸ±Ç`a[Ÿ±Çbmia2Ÿ±Ç`a]Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`dlineŸ±Çaoa.Ÿ±Ç`hset_dataŸ±Ç`a(Ÿ±Ç`ethisxŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ethisyŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`etraceŸ±Çaoa.Ÿ±Ç`hset_dataŸ±Ç`a(Ÿ±Ç`ihistory_xŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ihistory_yŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`itime_textŸ±Çaoa.Ÿ±Ç`hset_textŸ±Ç`a(Ÿ±Ç`mtime_templateŸ±Ç`a Ÿ±Çaoa%Ÿ±Ç`a Ÿ±Ç`a(Ÿ±Ç`aiŸ±Çaoa*Ÿ±Ç`bdtŸ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±ÇakfreturnŸ±Ç`a Ÿ±Ç`dlineŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`etraceŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`itime_textŸ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`caniŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`ianimationŸ±Çaoa.Ÿ±Ç`mFuncAnimationŸ±Ç`a(Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`cfigŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ganimateŸ±Ç`a,Ÿ±Ç`a Ÿ±ÇbnbclenŸ±Ç`a(Ÿ±Ç`ayŸ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`hintervalŸ±Çaoa=Ÿ±Ç`bdtŸ±Çaoa*Ÿ±Çbmid1000Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dblitŸ±Çaoa=Ÿ±ÇbkcdTrueŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`dshowŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
`dNoneˆ