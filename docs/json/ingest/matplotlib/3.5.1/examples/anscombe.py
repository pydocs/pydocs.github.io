ŸØÇÅŸ¥ÉôŸ±Çbsdyµ"""
==================
Anscombe's quartet
==================

`Anscombe's quartet`_ is a group of datasets (x, y) that have the same mean,
standard deviation, and regression line, but which are qualitatively different.

It is often used to illustrate the importance of looking at a set of data
graphically and not only relying on basic statistic properties.

.. _Anscombe's quartet: https://en.wikipedia.org/wiki/Anscombe%27s_quartet
"""Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±ÇbknfimportŸ±Ç`a Ÿ±ÇbnnŸ¢ÑjmatplotlibŸ†Ñjmatplotlibe3.5.1fmodulejmatplotlibfmoduleıŸ±Çbnna.Ÿ±ÇbnnfpyplotŸ±Ç`a Ÿ±ÇakbasŸ±Ç`a Ÿ±ÇbnncpltŸ±Ç`a
Ÿ±ÇbknfimportŸ±Ç`a Ÿ±ÇbnnŸ¢ÑenumpyŸ†Ñenumpyf1.22.3fmoduleenumpyfmoduleıŸ±Ç`a Ÿ±ÇakbasŸ±Ç`a Ÿ±ÇbnnbnpŸ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`axŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`a[Ÿ±Çbmib10Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia8Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmib13Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia9Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmib11Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmib14Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia6Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia4Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmib12Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia7Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia5Ÿ±Ç`a]Ÿ±Ç`a
Ÿ±Ç`by1Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`a[Ÿ±Çbmfd8.04Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd6.95Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd7.58Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd8.81Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd8.33Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd9.96Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd7.24Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd4.26Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfe10.84Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd4.82Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd5.68Ÿ±Ç`a]Ÿ±Ç`a
Ÿ±Ç`by2Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`a[Ÿ±Çbmfd9.14Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd8.14Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd8.74Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd8.77Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd9.26Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd8.10Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd6.13Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd3.10Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd9.13Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd7.26Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd4.74Ÿ±Ç`a]Ÿ±Ç`a
Ÿ±Ç`by3Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`a[Ÿ±Çbmfd7.46Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd6.77Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfe12.74Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd7.11Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd7.81Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd8.84Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd6.08Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd5.39Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd8.15Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd6.42Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd5.73Ÿ±Ç`a]Ÿ±Ç`a
Ÿ±Ç`bx4Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`a[Ÿ±Çbmia8Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia8Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia8Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia8Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia8Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia8Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia8Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmib19Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia8Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia8Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia8Ÿ±Ç`a]Ÿ±Ç`a
Ÿ±Ç`by4Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`a[Ÿ±Çbmfd6.58Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd5.76Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd7.71Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd8.84Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd8.47Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd7.04Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd5.25Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfe12.50Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd5.56Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd7.91Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd6.89Ÿ±Ç`a]Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`hdatasetsŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`a{Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Çbs1a'Ÿ±Çbs1aIŸ±Çbs1a'Ÿ±Ç`a:Ÿ±Ç`a Ÿ±Ç`a(Ÿ±Ç`axŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`by1Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Çbs1a'Ÿ±Çbs1bIIŸ±Çbs1a'Ÿ±Ç`a:Ÿ±Ç`a Ÿ±Ç`a(Ÿ±Ç`axŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`by2Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Çbs1a'Ÿ±Çbs1cIIIŸ±Çbs1a'Ÿ±Ç`a:Ÿ±Ç`a Ÿ±Ç`a(Ÿ±Ç`axŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`by3Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Çbs1a'Ÿ±Çbs1bIVŸ±Çbs1a'Ÿ±Ç`a:Ÿ±Ç`a Ÿ±Ç`a(Ÿ±Ç`bx4Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`by4Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a}Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`cfigŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`caxsŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`hsubplotsŸ±Ç`a(Ÿ±Çbmia2Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia2Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`fsharexŸ±Çaoa=Ÿ±ÇbkcdTrueŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`fshareyŸ±Çaoa=Ÿ±ÇbkcdTrueŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`gfigsizeŸ±Çaoa=Ÿ±Ç`a(Ÿ±Çbmia6Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia6Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`x                        Ÿ±Ç`kgridspec_kwŸ±Çaoa=Ÿ±Ç`a{Ÿ±Çbs1a'Ÿ±Çbs1fwspaceŸ±Çbs1a'Ÿ±Ç`a:Ÿ±Ç`a Ÿ±Çbmfd0.08Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1fhspaceŸ±Çbs1a'Ÿ±Ç`a:Ÿ±Ç`a Ÿ±Çbmfd0.08Ÿ±Ç`a}Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`caxsŸ±Ç`a[Ÿ±Çbmia0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia0Ÿ±Ç`a]Ÿ±Çaoa.Ÿ±Ç`csetŸ±Ç`a(Ÿ±Ç`dxlimŸ±Çaoa=Ÿ±Ç`a(Ÿ±Çbmia0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmib20Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dylimŸ±Çaoa=Ÿ±Ç`a(Ÿ±Çbmia2Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmib14Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`caxsŸ±Ç`a[Ÿ±Çbmia0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia0Ÿ±Ç`a]Ÿ±Çaoa.Ÿ±Ç`csetŸ±Ç`a(Ÿ±Ç`fxticksŸ±Çaoa=Ÿ±Ç`a(Ÿ±Çbmia0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmib10Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmib20Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`fyticksŸ±Çaoa=Ÿ±Ç`a(Ÿ±Çbmia4Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia8Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmib12Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±ÇakcforŸ±Ç`a Ÿ±Ç`baxŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`a(Ÿ±Ç`elabelŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`a(Ÿ±Ç`axŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ayŸ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a Ÿ±ÇbowbinŸ±Ç`a Ÿ±ÇbnbczipŸ±Ç`a(Ÿ±Ç`caxsŸ±Çaoa.Ÿ±Ç`dflatŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`hdatasetsŸ±Çaoa.Ÿ±Ç`eitemsŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`dtextŸ±Ç`a(Ÿ±Çbmfc0.1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfc0.9Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`elabelŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`hfontsizeŸ±Çaoa=Ÿ±Çbmib20Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`itransformŸ±Çaoa=Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`itransAxesŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`bvaŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1ctopŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`ktick_paramsŸ±Ç`a(Ÿ±Ç`idirectionŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1binŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ctopŸ±Çaoa=Ÿ±ÇbkcdTrueŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`erightŸ±Çaoa=Ÿ±ÇbkcdTrueŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`dplotŸ±Ç`a(Ÿ±Ç`axŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ayŸ±Ç`a,Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1aoŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Çbc1s# linear regressionŸ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`bp1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`bp0Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`gpolyfitŸ±Ç`a(Ÿ±Ç`axŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ayŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`cdegŸ±Çaoa=Ÿ±Çbmia1Ÿ±Ç`a)Ÿ±Ç`b  Ÿ±Çbc1r# slope, interceptŸ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`faxlineŸ±Ç`a(Ÿ±Ç`cxy1Ÿ±Çaoa=Ÿ±Ç`a(Ÿ±Çbmia0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`bp0Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`eslopeŸ±Çaoa=Ÿ±Ç`bp1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ecolorŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1arŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`blwŸ±Çaoa=Ÿ±Çbmia2Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Çbc1x!# add text box for the statisticsŸ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`estatsŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`a(Ÿ±ÇbsaafŸ±Çbs1a'Ÿ±Çbs1a$Ÿ±Çbseb\\Ÿ±Çbs1fmu$ = Ÿ±Çbsia{Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`dmeanŸ±Ç`a(Ÿ±Ç`ayŸ±Ç`a)Ÿ±Çbsia:Ÿ±Çbs1c.2fŸ±Çbsia}Ÿ±Çbseb\nŸ±Çbs1a'Ÿ±Ç`a
Ÿ±Ç`m             Ÿ±ÇbsaafŸ±Çbs1a'Ÿ±Çbs1a$Ÿ±Çbseb\\Ÿ±Çbs1isigma$ = Ÿ±Çbsia{Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`cstdŸ±Ç`a(Ÿ±Ç`ayŸ±Ç`a)Ÿ±Çbsia:Ÿ±Çbs1c.2fŸ±Çbsia}Ÿ±Çbseb\nŸ±Çbs1a'Ÿ±Ç`a
Ÿ±Ç`m             Ÿ±ÇbsaafŸ±Çbs1a'Ÿ±Çbs1f$r$ = Ÿ±Çbsia{Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`hcorrcoefŸ±Ç`a(Ÿ±Ç`axŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ayŸ±Ç`a)Ÿ±Ç`a[Ÿ±Çbmia0Ÿ±Ç`a]Ÿ±Ç`a[Ÿ±Çbmia1Ÿ±Ç`a]Ÿ±Çbsia:Ÿ±Çbs1c.2fŸ±Çbsia}Ÿ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`dbboxŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±ÇbnbddictŸ±Ç`a(Ÿ±Ç`hboxstyleŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1eroundŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`bfcŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1nblanchedalmondŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`becŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1forangeŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ealphaŸ±Çaoa=Ÿ±Çbmfc0.5Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`dtextŸ±Ç`a(Ÿ±Çbmfd0.95Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd0.07Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`estatsŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`hfontsizeŸ±Çaoa=Ÿ±Çbmia9Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dbboxŸ±Çaoa=Ÿ±Ç`dbboxŸ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`l            Ÿ±Ç`itransformŸ±Çaoa=Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`itransAxesŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`shorizontalalignmentŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1erightŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
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
Ÿ±Çbc1xA#    - `matplotlib.axes.Axes.axline` / `matplotlib.pyplot.axline`Ÿ±Ç`a
Ÿ±Çbc1x=#    - `matplotlib.axes.Axes.text` / `matplotlib.pyplot.text`Ÿ±Ç`a
Ÿ±Çbc1xJ#    - `matplotlib.axes.Axes.tick_params` / matplotlib.pyplot.tick_params`Ÿ±Ç`a
`dNoneˆ