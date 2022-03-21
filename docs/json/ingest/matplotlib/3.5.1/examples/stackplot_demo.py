ŸØÇÅŸ¥ÉônŸ±Çbsdx["""
===========================
Stackplots and streamgraphs
===========================
"""Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1xN##############################################################################Ÿ±Ç`a
Ÿ±Çbc1l# StackplotsŸ±Ç`a
Ÿ±Çbc1l# ----------Ÿ±Ç`a
Ÿ±Çbc1a#Ÿ±Ç`a
Ÿ±Çbc1xH# Stackplots draw multiple datasets as vertically stacked areas. This isŸ±Ç`a
Ÿ±Çbc1xJ# useful when the individual data values and additionally their cumulativeŸ±Ç`a
Ÿ±Çbc1x# value are of interest.Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±ÇbknfimportŸ±Ç`a Ÿ±ÇbnnŸ¢ÑenumpyŸ†Ñenumpyf1.22.3fmoduleenumpyfmoduleıŸ±Ç`a Ÿ±ÇakbasŸ±Ç`a Ÿ±ÇbnnbnpŸ±Ç`a
Ÿ±ÇbknfimportŸ±Ç`a Ÿ±ÇbnnŸ¢ÑjmatplotlibŸ†Ñjmatplotlibe3.5.1fmodulejmatplotlibfmoduleıŸ±Çbnna.Ÿ±ÇbnnfpyplotŸ±Ç`a Ÿ±ÇakbasŸ±Ç`a Ÿ±ÇbnncpltŸ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1xE# data from United Nations World Population Prospects (Revision 2019)Ÿ±Ç`a
Ÿ±Çbc1x8# https://population.un.org/wpp/, license: CC BY 3.0 IGOŸ±Ç`a
Ÿ±Ç`dyearŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`a[Ÿ±Çbmid1950Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmid1960Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmid1970Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmid1980Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmid1990Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmid2000Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmid2010Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmid2018Ÿ±Ç`a]Ÿ±Ç`a
Ÿ±Ç`wpopulation_by_continentŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`a{Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Çbs1a'Ÿ±Çbs1fafricaŸ±Çbs1a'Ÿ±Ç`a:Ÿ±Ç`a Ÿ±Ç`a[Ÿ±Çbmic228Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmic284Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmic365Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmic477Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmic631Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmic814Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmid1044Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmid1275Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Çbs1a'Ÿ±Çbs1hamericasŸ±Çbs1a'Ÿ±Ç`a:Ÿ±Ç`a Ÿ±Ç`a[Ÿ±Çbmic340Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmic425Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmic519Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmic619Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmic727Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmic840Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmic943Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmid1006Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Çbs1a'Ÿ±Çbs1dasiaŸ±Çbs1a'Ÿ±Ç`a:Ÿ±Ç`a Ÿ±Ç`a[Ÿ±Çbmid1394Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmid1686Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmid2120Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmid2625Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmid3202Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmid3714Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmid4169Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmid4560Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Çbs1a'Ÿ±Çbs1feuropeŸ±Çbs1a'Ÿ±Ç`a:Ÿ±Ç`a Ÿ±Ç`a[Ÿ±Çbmic220Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmic253Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmic276Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmic295Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmic310Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmic303Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmic294Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmic293Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Çbs1a'Ÿ±Çbs1goceaniaŸ±Çbs1a'Ÿ±Ç`a:Ÿ±Ç`a Ÿ±Ç`a[Ÿ±Çbmib12Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmib15Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmib19Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmib22Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmib26Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmib31Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmib36Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmib39Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`a}Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`cfigŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`baxŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`hsubplotsŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`istackplotŸ±Ç`a(Ÿ±Ç`dyearŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`wpopulation_by_continentŸ±Çaoa.Ÿ±Ç`fvaluesŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`m             Ÿ±Ç`flabelsŸ±Çaoa=Ÿ±Ç`wpopulation_by_continentŸ±Çaoa.Ÿ±Ç`dkeysŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ealphaŸ±Çaoa=Ÿ±Çbmfc0.8Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`flegendŸ±Ç`a(Ÿ±Ç`clocŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1jupper leftŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`iset_titleŸ±Ç`a(Ÿ±Çbs1a'Ÿ±Çbs1pWorld populationŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`jset_xlabelŸ±Ç`a(Ÿ±Çbs1a'Ÿ±Çbs1dYearŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`jset_ylabelŸ±Ç`a(Ÿ±Çbs1a'Ÿ±Çbs1xNumber of people (millions)Ÿ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`dshowŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1xN##############################################################################Ÿ±Ç`a
Ÿ±Çbc1n# StreamgraphsŸ±Ç`a
Ÿ±Çbc1n# ------------Ÿ±Ç`a
Ÿ±Çbc1a#Ÿ±Ç`a
Ÿ±Çbc1xL# Using the *baseline* parameter, you can turn an ordinary stacked area plotŸ±Ç`a
Ÿ±Çbc1x&# with baseline 0 into a stream graph.Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1x)# Fixing random state for reproducibilityŸ±Ç`a
Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`frandomŸ±Çaoa.Ÿ±Ç`dseedŸ±Ç`a(Ÿ±Çbmih19680801Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±ÇakcdefŸ±Ç`a Ÿ±Çbnfpgaussian_mixtureŸ±Ç`a(Ÿ±Ç`axŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`anŸ±Çaoa=Ÿ±Çbmia5Ÿ±Ç`a)Ÿ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±ÇbsdxK"""Return a random mixture of *n* Gaussians, evaluated at positions *x*."""Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±ÇakcdefŸ±Ç`a Ÿ±Çbnfsadd_random_gaussianŸ±Ç`a(Ÿ±Ç`aaŸ±Ç`a)Ÿ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±Ç`iamplitudeŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Çbmia1Ÿ±Ç`a Ÿ±Çaoa/Ÿ±Ç`a Ÿ±Ç`a(Ÿ±Çbmfb.1Ÿ±Ç`a Ÿ±Çaoa+Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`frandomŸ±Çaoa.Ÿ±Ç`frandomŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±Ç`bdxŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`axŸ±Ç`a[Ÿ±Çaoa-Ÿ±Çbmia1Ÿ±Ç`a]Ÿ±Ç`a Ÿ±Çaoa-Ÿ±Ç`a Ÿ±Ç`axŸ±Ç`a[Ÿ±Çbmia0Ÿ±Ç`a]Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±Ç`bx0Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`a(Ÿ±Çbmia2Ÿ±Ç`a Ÿ±Çaoa*Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`frandomŸ±Çaoa.Ÿ±Ç`frandomŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a Ÿ±Çaoa-Ÿ±Ç`a Ÿ±Çbmfb.5Ÿ±Ç`a)Ÿ±Ç`a Ÿ±Çaoa*Ÿ±Ç`a Ÿ±Ç`bdxŸ±Ç`a
Ÿ±Ç`h        Ÿ±Ç`azŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Çbmib10Ÿ±Ç`a Ÿ±Çaoa/Ÿ±Ç`a Ÿ±Ç`a(Ÿ±Çbmfb.1Ÿ±Ç`a Ÿ±Çaoa+Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`frandomŸ±Çaoa.Ÿ±Ç`frandomŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a Ÿ±Çaoa/Ÿ±Ç`a Ÿ±Ç`bdxŸ±Ç`a
Ÿ±Ç`h        Ÿ±Ç`aaŸ±Ç`a Ÿ±Çaoa+Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`iamplitudeŸ±Ç`a Ÿ±Çaoa*Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`cexpŸ±Ç`a(Ÿ±Çaoa-Ÿ±Ç`a(Ÿ±Ç`azŸ±Ç`a Ÿ±Çaoa*Ÿ±Ç`a Ÿ±Ç`a(Ÿ±Ç`axŸ±Ç`a Ÿ±Çaoa-Ÿ±Ç`a Ÿ±Ç`bx0Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Çaoa*Ÿ±Çaoa*Ÿ±Çbmia2Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`aaŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`jzeros_likeŸ±Ç`a(Ÿ±Ç`axŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±ÇakcforŸ±Ç`a Ÿ±Ç`ajŸ±Ç`a Ÿ±ÇbowbinŸ±Ç`a Ÿ±ÇbnberangeŸ±Ç`a(Ÿ±Ç`anŸ±Ç`a)Ÿ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±Ç`sadd_random_gaussianŸ±Ç`a(Ÿ±Ç`aaŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±ÇakfreturnŸ±Ç`a Ÿ±Ç`aaŸ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`axŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`hlinspaceŸ±Ç`a(Ÿ±Çbmia0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmic100Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmic101Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`bysŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`a[Ÿ±Ç`pgaussian_mixtureŸ±Ç`a(Ÿ±Ç`axŸ±Ç`a)Ÿ±Ç`a Ÿ±ÇakcforŸ±Ç`a Ÿ±Ç`a_Ÿ±Ç`a Ÿ±ÇbowbinŸ±Ç`a Ÿ±ÇbnberangeŸ±Ç`a(Ÿ±Çbmia3Ÿ±Ç`a)Ÿ±Ç`a]Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`cfigŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`baxŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`hsubplotsŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`istackplotŸ±Ç`a(Ÿ±Ç`axŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`bysŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`hbaselineŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1fwiggleŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`dshowŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
`dNoneˆ