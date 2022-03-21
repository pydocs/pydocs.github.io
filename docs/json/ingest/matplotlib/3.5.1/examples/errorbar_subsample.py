ŸØÇÅŸ¥ÉôIŸ±Çbsdy"""
====================
Errorbar subsampling
====================

The parameter *errorevery* of `.Axes.errorbar` can be used to draw error bars
only on a subset of data points. This is particularly useful if there are many
data points with similar errors.
"""Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±ÇbknfimportŸ±Ç`a Ÿ±ÇbnnŸ¢ÑenumpyŸ†Ñenumpyf1.22.3fmoduleenumpyfmoduleıŸ±Ç`a Ÿ±ÇakbasŸ±Ç`a Ÿ±ÇbnnbnpŸ±Ç`a
Ÿ±ÇbknfimportŸ±Ç`a Ÿ±ÇbnnŸ¢ÑjmatplotlibŸ†Ñjmatplotlibe3.5.1fmodulejmatplotlibfmoduleıŸ±Çbnna.Ÿ±ÇbnnfpyplotŸ±Ç`a Ÿ±ÇakbasŸ±Ç`a Ÿ±ÇbnncpltŸ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1n# example dataŸ±Ç`a
Ÿ±Ç`axŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`farangeŸ±Ç`a(Ÿ±Çbmfc0.1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia4Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfc0.1Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`by1Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`cexpŸ±Ç`a(Ÿ±Çaoa-Ÿ±Çbmfc1.0Ÿ±Ç`a Ÿ±Çaoa*Ÿ±Ç`a Ÿ±Ç`axŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`by2Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`cexpŸ±Ç`a(Ÿ±Çaoa-Ÿ±Çbmfc0.5Ÿ±Ç`a Ÿ±Çaoa*Ÿ±Ç`a Ÿ±Ç`axŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1x## example variable error bar valuesŸ±Ç`a
Ÿ±Ç`ey1errŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Çbmfc0.1Ÿ±Ç`a Ÿ±Çaoa+Ÿ±Ç`a Ÿ±Çbmfc0.1Ÿ±Ç`a Ÿ±Çaoa*Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`dsqrtŸ±Ç`a(Ÿ±Ç`axŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`ey2errŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Çbmfc0.1Ÿ±Ç`a Ÿ±Çaoa+Ÿ±Ç`a Ÿ±Çbmfc0.1Ÿ±Ç`a Ÿ±Çaoa*Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`dsqrtŸ±Ç`a(Ÿ±Ç`axŸ±Çaoa/Ÿ±Çbmia2Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`cfigŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`a(Ÿ±Ç`cax0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`cax1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`cax2Ÿ±Ç`a)Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`hsubplotsŸ±Ç`a(Ÿ±Ç`enrowsŸ±Çaoa=Ÿ±Çbmia1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`encolsŸ±Çaoa=Ÿ±Çbmia3Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`fsharexŸ±Çaoa=Ÿ±ÇbkcdTrueŸ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`x$                                    Ÿ±Ç`gfigsizeŸ±Çaoa=Ÿ±Ç`a(Ÿ±Çbmib12Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia6Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`cax0Ÿ±Çaoa.Ÿ±Ç`iset_titleŸ±Ç`a(Ÿ±Çbs1a'Ÿ±Çbs1mall errorbarsŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cax0Ÿ±Çaoa.Ÿ±Ç`herrorbarŸ±Ç`a(Ÿ±Ç`axŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`by1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dyerrŸ±Çaoa=Ÿ±Ç`ey1errŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cax0Ÿ±Çaoa.Ÿ±Ç`herrorbarŸ±Ç`a(Ÿ±Ç`axŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`by2Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dyerrŸ±Çaoa=Ÿ±Ç`ey2errŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`cax1Ÿ±Çaoa.Ÿ±Ç`iset_titleŸ±Ç`a(Ÿ±Çbs1a'Ÿ±Çbs1wonly every 6th errorbarŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cax1Ÿ±Çaoa.Ÿ±Ç`herrorbarŸ±Ç`a(Ÿ±Ç`axŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`by1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dyerrŸ±Çaoa=Ÿ±Ç`ey1errŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`jerroreveryŸ±Çaoa=Ÿ±Çbmia6Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cax1Ÿ±Çaoa.Ÿ±Ç`herrorbarŸ±Ç`a(Ÿ±Ç`axŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`by2Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dyerrŸ±Çaoa=Ÿ±Ç`ey2errŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`jerroreveryŸ±Çaoa=Ÿ±Çbmia6Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`cax2Ÿ±Çaoa.Ÿ±Ç`iset_titleŸ±Ç`a(Ÿ±Çbs1a'Ÿ±Çbs1xsecond series shifted by 3Ÿ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cax2Ÿ±Çaoa.Ÿ±Ç`herrorbarŸ±Ç`a(Ÿ±Ç`axŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`by1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dyerrŸ±Çaoa=Ÿ±Ç`ey1errŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`jerroreveryŸ±Çaoa=Ÿ±Ç`a(Ÿ±Çbmia0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia6Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cax2Ÿ±Çaoa.Ÿ±Ç`herrorbarŸ±Ç`a(Ÿ±Ç`axŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`by2Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dyerrŸ±Çaoa=Ÿ±Ç`ey2errŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`jerroreveryŸ±Çaoa=Ÿ±Ç`a(Ÿ±Çbmia3Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia6Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`cfigŸ±Çaoa.Ÿ±Ç`hsuptitleŸ±Ç`a(Ÿ±Çbs1a'Ÿ±Çbs1tErrorbar subsamplingŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`dshowŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
`dNoneˆ