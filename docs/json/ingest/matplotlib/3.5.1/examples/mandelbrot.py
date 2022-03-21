ŸØÇÅŸ¥ÉôıŸ±Çbsdy®"""
===================================
Shaded & power normalized rendering
===================================

The Mandelbrot set rendering can be improved by using a normalized recount
associated with a power normalized colormap (gamma=0.3). Rendering can be
further enhanced thanks to shading.

The ``maxiter`` gives the precision of the computation. ``maxiter=200`` should
take a few seconds on most modern laptops.
"""Ÿ±Ç`a
Ÿ±ÇbknfimportŸ±Ç`a Ÿ±ÇbnnŸ¢ÑenumpyŸ†Ñenumpyf1.22.3fmoduleenumpyfmoduleıŸ±Ç`a Ÿ±ÇakbasŸ±Ç`a Ÿ±ÇbnnbnpŸ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±ÇakcdefŸ±Ç`a Ÿ±Çbnfnmandelbrot_setŸ±Ç`a(Ÿ±Ç`dxminŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dxmaxŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dyminŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dymaxŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`bxnŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`bynŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`gmaxiterŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ghorizonŸ±Çaoa=Ÿ±Çbmfc2.0Ÿ±Ç`a)Ÿ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`aXŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`hlinspaceŸ±Ç`a(Ÿ±Ç`dxminŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dxmaxŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`bxnŸ±Ç`a)Ÿ±Çaoa.Ÿ±Ç`fastypeŸ±Ç`a(Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`gfloat32Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`aYŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`hlinspaceŸ±Ç`a(Ÿ±Ç`dyminŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dymaxŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`bynŸ±Ç`a)Ÿ±Çaoa.Ÿ±Ç`fastypeŸ±Ç`a(Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`gfloat32Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`aCŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`aXŸ±Ç`a Ÿ±Çaoa+Ÿ±Ç`a Ÿ±Ç`aYŸ±Ç`a[Ÿ±Ç`a:Ÿ±Ç`a,Ÿ±Ç`a Ÿ±ÇbkcdNoneŸ±Ç`a]Ÿ±Ç`a Ÿ±Çaoa*Ÿ±Ç`a Ÿ±Çbmia1Ÿ±Ç`ajŸ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`aNŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`jzeros_likeŸ±Ç`a(Ÿ±Ç`aCŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`edtypeŸ±Çaoa=Ÿ±ÇbnbcintŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`aZŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`jzeros_likeŸ±Ç`a(Ÿ±Ç`aCŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±ÇakcforŸ±Ç`a Ÿ±Ç`anŸ±Ç`a Ÿ±ÇbowbinŸ±Ç`a Ÿ±ÇbnberangeŸ±Ç`a(Ÿ±Ç`gmaxiterŸ±Ç`a)Ÿ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±Ç`aIŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±ÇbnbcabsŸ±Ç`a(Ÿ±Ç`aZŸ±Ç`a)Ÿ±Ç`a Ÿ±Çaoa<Ÿ±Ç`a Ÿ±Ç`ghorizonŸ±Ç`a
Ÿ±Ç`h        Ÿ±Ç`aNŸ±Ç`a[Ÿ±Ç`aIŸ±Ç`a]Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`anŸ±Ç`a
Ÿ±Ç`h        Ÿ±Ç`aZŸ±Ç`a[Ÿ±Ç`aIŸ±Ç`a]Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`aZŸ±Ç`a[Ÿ±Ç`aIŸ±Ç`a]Ÿ±Çaoa*Ÿ±Çaoa*Ÿ±Çbmia2Ÿ±Ç`a Ÿ±Çaoa+Ÿ±Ç`a Ÿ±Ç`aCŸ±Ç`a[Ÿ±Ç`aIŸ±Ç`a]Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`aNŸ±Ç`a[Ÿ±Ç`aNŸ±Ç`a Ÿ±Çaob==Ÿ±Ç`a Ÿ±Ç`gmaxiterŸ±Çaoa-Ÿ±Çbmia1Ÿ±Ç`a]Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Çbmia0Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±ÇakfreturnŸ±Ç`a Ÿ±Ç`aZŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`aNŸ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±ÇakbifŸ±Ç`a Ÿ±Çbvmh__name__Ÿ±Ç`a Ÿ±Çaob==Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1h__main__Ÿ±Çbs1a'Ÿ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±ÇbknfimportŸ±Ç`a Ÿ±ÇbnndtimeŸ±Ç`a
Ÿ±Ç`d    Ÿ±ÇbknfimportŸ±Ç`a Ÿ±ÇbnnŸ¢ÑjmatplotlibŸ†Ñjmatplotlibe3.5.1fmodulejmatplotlibfmoduleıŸ±Ç`a
Ÿ±Ç`d    Ÿ±ÇbkndfromŸ±Ç`a Ÿ±ÇbnnŸ¢ÑjmatplotlibŸ†Ñjmatplotlibe3.5.1fmodulejmatplotlibfmoduleıŸ±Ç`a Ÿ±ÇbknfimportŸ±Ç`a Ÿ±Ç`fcolorsŸ±Ç`a
Ÿ±Ç`d    Ÿ±ÇbknfimportŸ±Ç`a Ÿ±ÇbnnŸ¢ÑjmatplotlibŸ†Ñjmatplotlibe3.5.1fmodulejmatplotlibfmoduleıŸ±Çbnna.Ÿ±ÇbnnfpyplotŸ±Ç`a Ÿ±ÇakbasŸ±Ç`a Ÿ±ÇbnncpltŸ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`dxminŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dxmaxŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`bxnŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Çaoa-Ÿ±Çbmfd2.25Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çaoa+Ÿ±Çbmfd0.75Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmid3000Ÿ±Ç`a Ÿ±Çaoa/Ÿ±Çaoa/Ÿ±Ç`a Ÿ±Çbmia2Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`dyminŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dymaxŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`bynŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Çaoa-Ÿ±Çbmfd1.25Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çaoa+Ÿ±Çbmfd1.25Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmid2500Ÿ±Ç`a Ÿ±Çaoa/Ÿ±Çaoa/Ÿ±Ç`a Ÿ±Çbmia2Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`gmaxiterŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Çbmic200Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`ghorizonŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Çbmfc2.0Ÿ±Ç`a Ÿ±Çaoa*Ÿ±Çaoa*Ÿ±Ç`a Ÿ±Çbmib40Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`klog_horizonŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`dlog2Ÿ±Ç`a(Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`clogŸ±Ç`a(Ÿ±Ç`ghorizonŸ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`aZŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`aNŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`nmandelbrot_setŸ±Ç`a(Ÿ±Ç`dxminŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dxmaxŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dyminŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dymaxŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`bxnŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`bynŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`gmaxiterŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ghorizonŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Çbc1x%# Normalized recount as explained in:Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Çbc1x2# https://linas.org/art-gallery/escape/smooth.htmlŸ±Ç`a
Ÿ±Ç`d    Ÿ±Çbc1xÉ# https://web.archive.org/web/20160331171238/https://www.ibm.com/developerworks/community/blogs/jfp/entry/My_Christmas_Gift?lang=enŸ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Çbc1xF# This line will generate warnings for null values but it is faster toŸ±Ç`a
Ÿ±Ç`d    Ÿ±Çbc1x.# process them afterwards using the nan_to_numŸ±Ç`a
Ÿ±Ç`d    Ÿ±ÇakdwithŸ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`herrstateŸ±Ç`a(Ÿ±Ç`ginvalidŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1fignoreŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±Ç`aMŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`jnan_to_numŸ±Ç`a(Ÿ±Ç`aNŸ±Ç`a Ÿ±Çaoa+Ÿ±Ç`a Ÿ±Çbmia1Ÿ±Ç`a Ÿ±Çaoa-Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`dlog2Ÿ±Ç`a(Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`clogŸ±Ç`a(Ÿ±ÇbnbcabsŸ±Ç`a(Ÿ±Ç`aZŸ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a Ÿ±Çaoa+Ÿ±Ç`a Ÿ±Ç`klog_horizonŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`cdpiŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Çbmib72Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`ewidthŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Çbmib10Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`fheightŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Çbmib10Ÿ±Çaoa*Ÿ±Ç`bynŸ±Çaoa/Ÿ±Ç`bxnŸ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`cfigŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`ffigureŸ±Ç`a(Ÿ±Ç`gfigsizeŸ±Çaoa=Ÿ±Ç`a(Ÿ±Ç`ewidthŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`fheightŸ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`cdpiŸ±Çaoa=Ÿ±Ç`cdpiŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`baxŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cfigŸ±Çaoa.Ÿ±Ç`hadd_axesŸ±Ç`a(Ÿ±Ç`a[Ÿ±Çbmia0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia1Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`gframeonŸ±Çaoa=Ÿ±ÇbkceFalseŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`faspectŸ±Çaoa=Ÿ±Çbmia1Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Çbc1r# Shaded renderingŸ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`elightŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`fcolorsŸ±Çaoa.Ÿ±Ç`kLightSourceŸ±Ç`a(Ÿ±Ç`eazdegŸ±Çaoa=Ÿ±Çbmic315Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`faltdegŸ±Çaoa=Ÿ±Çbmib10Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`aMŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`elightŸ±Çaoa.Ÿ±Ç`eshadeŸ±Ç`a(Ÿ±Ç`aMŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dcmapŸ±Çaoa=Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`bcmŸ±Çaoa.Ÿ±Ç`chotŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ivert_exagŸ±Çaoa=Ÿ±Çbmfc1.5Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`t                    Ÿ±Ç`dnormŸ±Çaoa=Ÿ±Ç`fcolorsŸ±Çaoa.Ÿ±Ç`iPowerNormŸ±Ç`a(Ÿ±Çbmfc0.3Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`jblend_modeŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1chsvŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`fimshowŸ±Ç`a(Ÿ±Ç`aMŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`fextentŸ±Çaoa=Ÿ±Ç`a[Ÿ±Ç`dxminŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dxmaxŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dyminŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dymaxŸ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`minterpolationŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2gbicubicŸ±Çbs2a"Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`jset_xticksŸ±Ç`a(Ÿ±Ç`a[Ÿ±Ç`a]Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`jset_yticksŸ±Ç`a(Ÿ±Ç`a[Ÿ±Ç`a]Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Çbc1x## Some advertisement for matplotlibŸ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`dyearŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`dtimeŸ±Çaoa.Ÿ±Ç`hstrftimeŸ±Ç`a(Ÿ±Çbs2a"Ÿ±Çbs2a%Ÿ±Çbs2aYŸ±Çbs2a"Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`dtextŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`a(Ÿ±Çbs2a"Ÿ±Çbs2xThe Mandelbrot fractal setŸ±Çbseb\nŸ±Çbs2a"Ÿ±Ç`a
Ÿ±Ç`l            Ÿ±Çbs2a"Ÿ±Çbs2xRendered with matplotlib Ÿ±Çbsib%sŸ±Çbs2b, Ÿ±Çbsib%sŸ±Çbs2x - https://matplotlib.orgŸ±Çbs2a"Ÿ±Ç`a
Ÿ±Ç`l            Ÿ±Çaoa%Ÿ±Ç`a Ÿ±Ç`a(Ÿ±Ç`Ÿ¢ÑjmatplotlibŸ†Ñjmatplotlibe3.5.1fmodulejmatplotlibfmoduleıŸ±Çaoa.Ÿ±Ç`k__version__Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dyearŸ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`dtextŸ±Ç`a(Ÿ±Ç`dxminŸ±Çaoa+Ÿ±Çbmfd.025Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dyminŸ±Çaoa+Ÿ±Çbmfd.025Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dtextŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ecolorŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2ewhiteŸ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`hfontsizeŸ±Çaoa=Ÿ±Çbmib12Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ealphaŸ±Çaoa=Ÿ±Çbmfc0.5Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`dshowŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
`dNoneˆ