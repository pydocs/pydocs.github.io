Ù¯‚Ù´ƒ™ÇÙ±‚bsdxX"""
================
Logit Demo
================

Examples of plots with logit axes.
"""Ù±‚`a
Ù±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnndmathÙ±‚`a
Ù±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„enumpyÙ „enumpyf1.22.3fmoduleenumpyfmoduleõÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnnbnpÙ±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnnfpyplotÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnncpltÙ±‚`a
Ù±‚`a
Ù±‚`dxmaxÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bmib10Ù±‚`a
Ù±‚`axÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`hlinspaceÙ±‚`a(Ù±‚aoa-Ù±‚`dxmaxÙ±‚`a,Ù±‚`a Ù±‚`dxmaxÙ±‚`a,Ù±‚`a Ù±‚bmie10000Ù±‚`a)Ù±‚`a
Ù±‚`hcdf_normÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`a[Ù±‚`dmathÙ±‚aoa.Ù±‚`cerfÙ±‚`a(Ù±‚`awÙ±‚`a Ù±‚aoa/Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`dsqrtÙ±‚`a(Ù±‚bmia2Ù±‚`a)Ù±‚`a)Ù±‚`a Ù±‚aoa/Ù±‚`a Ù±‚bmia2Ù±‚`a Ù±‚aoa+Ù±‚`a Ù±‚bmia1Ù±‚`a Ù±‚aoa/Ù±‚`a Ù±‚bmia2Ù±‚`a Ù±‚akcforÙ±‚`a Ù±‚`awÙ±‚`a Ù±‚bowbinÙ±‚`a Ù±‚`axÙ±‚`a]Ù±‚`a
Ù±‚`mcdf_laplacianÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`ewhereÙ±‚`a(Ù±‚`axÙ±‚`a Ù±‚aoa<Ù±‚`a Ù±‚bmia0Ù±‚`a,Ù±‚`a Ù±‚bmia1Ù±‚`a Ù±‚aoa/Ù±‚`a Ù±‚bmia2Ù±‚`a Ù±‚aoa*Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`cexpÙ±‚`a(Ù±‚`axÙ±‚`a)Ù±‚`a,Ù±‚`a Ù±‚bmia1Ù±‚`a Ù±‚aoa-Ù±‚`a Ù±‚bmia1Ù±‚`a Ù±‚aoa/Ù±‚`a Ù±‚bmia2Ù±‚`a Ù±‚aoa*Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`cexpÙ±‚`a(Ù±‚aoa-Ù±‚`axÙ±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`jcdf_cauchyÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`farctanÙ±‚`a(Ù±‚`axÙ±‚`a)Ù±‚`a Ù±‚aoa/Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`bpiÙ±‚`a Ù±‚aoa+Ù±‚`a Ù±‚bmia1Ù±‚`a Ù±‚aoa/Ù±‚`a Ù±‚bmia2Ù±‚`a
Ù±‚`a
Ù±‚`cfigÙ±‚`a,Ù±‚`a Ù±‚`caxsÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cpltÙ±‚aoa.Ù±‚`hsubplotsÙ±‚`a(Ù±‚`enrowsÙ±‚aoa=Ù±‚bmia3Ù±‚`a,Ù±‚`a Ù±‚`encolsÙ±‚aoa=Ù±‚bmia2Ù±‚`a,Ù±‚`a Ù±‚`gfigsizeÙ±‚aoa=Ù±‚`a(Ù±‚bmfc6.4Ù±‚`a,Ù±‚`a Ù±‚bmfc8.5Ù±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚bc1xG# Common part, for the example, we will do the same plots on all graphsÙ±‚`a
Ù±‚akcforÙ±‚`a Ù±‚`aiÙ±‚`a Ù±‚bowbinÙ±‚`a Ù±‚bnberangeÙ±‚`a(Ù±‚bmia3Ù±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`d    Ù±‚akcforÙ±‚`a Ù±‚`ajÙ±‚`a Ù±‚bowbinÙ±‚`a Ù±‚bnberangeÙ±‚`a(Ù±‚bmia2Ù±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`h        Ù±‚`caxsÙ±‚`a[Ù±‚`aiÙ±‚`a,Ù±‚`a Ù±‚`ajÙ±‚`a]Ù±‚aoa.Ù±‚`dplotÙ±‚`a(Ù±‚`axÙ±‚`a,Ù±‚`a Ù±‚`hcdf_normÙ±‚`a,Ù±‚`a Ù±‚`elabelÙ±‚aoa=Ù±‚bsaarÙ±‚bs2a"Ù±‚bs2a$Ù±‚bs2a\Ù±‚bs2gmathcalÙ±‚bsic{N}Ù±‚bs2a$Ù±‚bs2a"Ù±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚`caxsÙ±‚`a[Ù±‚`aiÙ±‚`a,Ù±‚`a Ù±‚`ajÙ±‚`a]Ù±‚aoa.Ù±‚`dplotÙ±‚`a(Ù±‚`axÙ±‚`a,Ù±‚`a Ù±‚`mcdf_laplacianÙ±‚`a,Ù±‚`a Ù±‚`elabelÙ±‚aoa=Ù±‚bsaarÙ±‚bs2a"Ù±‚bs2a$Ù±‚bs2a\Ù±‚bs2gmathcalÙ±‚bsic{L}Ù±‚bs2a$Ù±‚bs2a"Ù±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚`caxsÙ±‚`a[Ù±‚`aiÙ±‚`a,Ù±‚`a Ù±‚`ajÙ±‚`a]Ù±‚aoa.Ù±‚`dplotÙ±‚`a(Ù±‚`axÙ±‚`a,Ù±‚`a Ù±‚`jcdf_cauchyÙ±‚`a,Ù±‚`a Ù±‚`elabelÙ±‚aoa=Ù±‚bs2a"Ù±‚bs2fCauchyÙ±‚bs2a"Ù±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚`caxsÙ±‚`a[Ù±‚`aiÙ±‚`a,Ù±‚`a Ù±‚`ajÙ±‚`a]Ù±‚aoa.Ù±‚`flegendÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚`caxsÙ±‚`a[Ù±‚`aiÙ±‚`a,Ù±‚`a Ù±‚`ajÙ±‚`a]Ù±‚aoa.Ù±‚`dgridÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚bc1x0# First line, logitscale, with standard notationÙ±‚`a
Ù±‚`caxsÙ±‚`a[Ù±‚bmia0Ù±‚`a,Ù±‚`a Ù±‚bmia0Ù±‚`a]Ù±‚aoa.Ù±‚`csetÙ±‚`a(Ù±‚`etitleÙ±‚aoa=Ù±‚bs2a"Ù±‚bs2klogit scaleÙ±‚bs2a"Ù±‚`a)Ù±‚`a
Ù±‚`caxsÙ±‚`a[Ù±‚bmia0Ù±‚`a,Ù±‚`a Ù±‚bmia0Ù±‚`a]Ù±‚aoa.Ù±‚`jset_yscaleÙ±‚`a(Ù±‚bs2a"Ù±‚bs2elogitÙ±‚bs2a"Ù±‚`a)Ù±‚`a
Ù±‚`caxsÙ±‚`a[Ù±‚bmia0Ù±‚`a,Ù±‚`a Ù±‚bmia0Ù±‚`a]Ù±‚aoa.Ù±‚`hset_ylimÙ±‚`a(Ù±‚bmfd1e-5Ù±‚`a,Ù±‚`a Ù±‚bmia1Ù±‚`a Ù±‚aoa-Ù±‚`a Ù±‚bmfd1e-5Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`caxsÙ±‚`a[Ù±‚bmia0Ù±‚`a,Ù±‚`a Ù±‚bmia1Ù±‚`a]Ù±‚aoa.Ù±‚`csetÙ±‚`a(Ù±‚`etitleÙ±‚aoa=Ù±‚bs2a"Ù±‚bs2klogit scaleÙ±‚bs2a"Ù±‚`a)Ù±‚`a
Ù±‚`caxsÙ±‚`a[Ù±‚bmia0Ù±‚`a,Ù±‚`a Ù±‚bmia1Ù±‚`a]Ù±‚aoa.Ù±‚`jset_yscaleÙ±‚`a(Ù±‚bs2a"Ù±‚bs2elogitÙ±‚bs2a"Ù±‚`a)Ù±‚`a
Ù±‚`caxsÙ±‚`a[Ù±‚bmia0Ù±‚`a,Ù±‚`a Ù±‚bmia1Ù±‚`a]Ù±‚aoa.Ù±‚`hset_xlimÙ±‚`a(Ù±‚bmia0Ù±‚`a,Ù±‚`a Ù±‚`dxmaxÙ±‚`a)Ù±‚`a
Ù±‚`caxsÙ±‚`a[Ù±‚bmia0Ù±‚`a,Ù±‚`a Ù±‚bmia1Ù±‚`a]Ù±‚aoa.Ù±‚`hset_ylimÙ±‚`a(Ù±‚bmfc0.8Ù±‚`a,Ù±‚`a Ù±‚bmia1Ù±‚`a Ù±‚aoa-Ù±‚`a Ù±‚bmfd5e-3Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚bc1xL# Second line, logitscale, with survival notation (with `use_overline`), andÙ±‚`a
Ù±‚bc1x# other format display 1/2Ù±‚`a
Ù±‚`caxsÙ±‚`a[Ù±‚bmia1Ù±‚`a,Ù±‚`a Ù±‚bmia0Ù±‚`a]Ù±‚aoa.Ù±‚`csetÙ±‚`a(Ù±‚`etitleÙ±‚aoa=Ù±‚bs2a"Ù±‚bs2klogit scaleÙ±‚bs2a"Ù±‚`a)Ù±‚`a
Ù±‚`caxsÙ±‚`a[Ù±‚bmia1Ù±‚`a,Ù±‚`a Ù±‚bmia0Ù±‚`a]Ù±‚aoa.Ù±‚`jset_yscaleÙ±‚`a(Ù±‚bs2a"Ù±‚bs2elogitÙ±‚bs2a"Ù±‚`a,Ù±‚`a Ù±‚`hone_halfÙ±‚aoa=Ù±‚bs2a"Ù±‚bs2c1/2Ù±‚bs2a"Ù±‚`a,Ù±‚`a Ù±‚`luse_overlineÙ±‚aoa=Ù±‚bkcdTrueÙ±‚`a)Ù±‚`a
Ù±‚`caxsÙ±‚`a[Ù±‚bmia1Ù±‚`a,Ù±‚`a Ù±‚bmia0Ù±‚`a]Ù±‚aoa.Ù±‚`hset_ylimÙ±‚`a(Ù±‚bmfd1e-5Ù±‚`a,Ù±‚`a Ù±‚bmia1Ù±‚`a Ù±‚aoa-Ù±‚`a Ù±‚bmfd1e-5Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`caxsÙ±‚`a[Ù±‚bmia1Ù±‚`a,Ù±‚`a Ù±‚bmia1Ù±‚`a]Ù±‚aoa.Ù±‚`csetÙ±‚`a(Ù±‚`etitleÙ±‚aoa=Ù±‚bs2a"Ù±‚bs2klogit scaleÙ±‚bs2a"Ù±‚`a)Ù±‚`a
Ù±‚`caxsÙ±‚`a[Ù±‚bmia1Ù±‚`a,Ù±‚`a Ù±‚bmia1Ù±‚`a]Ù±‚aoa.Ù±‚`jset_yscaleÙ±‚`a(Ù±‚bs2a"Ù±‚bs2elogitÙ±‚bs2a"Ù±‚`a,Ù±‚`a Ù±‚`hone_halfÙ±‚aoa=Ù±‚bs2a"Ù±‚bs2c1/2Ù±‚bs2a"Ù±‚`a,Ù±‚`a Ù±‚`luse_overlineÙ±‚aoa=Ù±‚bkcdTrueÙ±‚`a)Ù±‚`a
Ù±‚`caxsÙ±‚`a[Ù±‚bmia1Ù±‚`a,Ù±‚`a Ù±‚bmia1Ù±‚`a]Ù±‚aoa.Ù±‚`hset_xlimÙ±‚`a(Ù±‚bmia0Ù±‚`a,Ù±‚`a Ù±‚`dxmaxÙ±‚`a)Ù±‚`a
Ù±‚`caxsÙ±‚`a[Ù±‚bmia1Ù±‚`a,Ù±‚`a Ù±‚bmia1Ù±‚`a]Ù±‚aoa.Ù±‚`hset_ylimÙ±‚`a(Ù±‚bmfc0.8Ù±‚`a,Ù±‚`a Ù±‚bmia1Ù±‚`a Ù±‚aoa-Ù±‚`a Ù±‚bmfd5e-3Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚bc1x# Third line, linear scaleÙ±‚`a
Ù±‚`caxsÙ±‚`a[Ù±‚bmia2Ù±‚`a,Ù±‚`a Ù±‚bmia0Ù±‚`a]Ù±‚aoa.Ù±‚`csetÙ±‚`a(Ù±‚`etitleÙ±‚aoa=Ù±‚bs2a"Ù±‚bs2llinear scaleÙ±‚bs2a"Ù±‚`a)Ù±‚`a
Ù±‚`caxsÙ±‚`a[Ù±‚bmia2Ù±‚`a,Ù±‚`a Ù±‚bmia0Ù±‚`a]Ù±‚aoa.Ù±‚`hset_ylimÙ±‚`a(Ù±‚bmia0Ù±‚`a,Ù±‚`a Ù±‚bmia1Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`caxsÙ±‚`a[Ù±‚bmia2Ù±‚`a,Ù±‚`a Ù±‚bmia1Ù±‚`a]Ù±‚aoa.Ù±‚`csetÙ±‚`a(Ù±‚`etitleÙ±‚aoa=Ù±‚bs2a"Ù±‚bs2llinear scaleÙ±‚bs2a"Ù±‚`a)Ù±‚`a
Ù±‚`caxsÙ±‚`a[Ù±‚bmia2Ù±‚`a,Ù±‚`a Ù±‚bmia1Ù±‚`a]Ù±‚aoa.Ù±‚`hset_xlimÙ±‚`a(Ù±‚bmia0Ù±‚`a,Ù±‚`a Ù±‚`dxmaxÙ±‚`a)Ù±‚`a
Ù±‚`caxsÙ±‚`a[Ù±‚bmia2Ù±‚`a,Ù±‚`a Ù±‚bmia1Ù±‚`a]Ù±‚aoa.Ù±‚`hset_ylimÙ±‚`a(Ù±‚bmfc0.8Ù±‚`a,Ù±‚`a Ù±‚bmia1Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`cfigÙ±‚aoa.Ù±‚`ltight_layoutÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`cpltÙ±‚aoa.Ù±‚`dshowÙ±‚`a(Ù±‚`a)Ù±‚`a
`dNoneö