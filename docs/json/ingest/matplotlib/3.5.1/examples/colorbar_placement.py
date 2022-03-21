ŸØÇÅŸ¥Éô£Ÿ±Çbsdy"""
=================
Placing Colorbars
=================

Colorbars indicate the quantitative extent of image data.  Placing in
a figure is non-trivial because room needs to be made for them.

The simplest case is just attaching a colorbar to each axes:
"""Ÿ±Ç`a
Ÿ±ÇbknfimportŸ±Ç`a Ÿ±ÇbnnŸ¢ÑjmatplotlibŸ†Ñjmatplotlibe3.5.1fmodulejmatplotlibfmoduleıŸ±Çbnna.Ÿ±ÇbnnfpyplotŸ±Ç`a Ÿ±ÇakbasŸ±Ç`a Ÿ±ÇbnncpltŸ±Ç`a
Ÿ±ÇbknfimportŸ±Ç`a Ÿ±ÇbnnŸ¢ÑenumpyŸ†Ñenumpyf1.22.3fmoduleenumpyfmoduleıŸ±Ç`a Ÿ±ÇakbasŸ±Ç`a Ÿ±ÇbnnbnpŸ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1x)# Fixing random state for reproducibilityŸ±Ç`a
Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`frandomŸ±Çaoa.Ÿ±Ç`dseedŸ±Ç`a(Ÿ±Çbmih19680801Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`cfigŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`caxsŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`hsubplotsŸ±Ç`a(Ÿ±Çbmia2Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia2Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`ecmapsŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`a[Ÿ±Çbs1a'Ÿ±Çbs1fRdBu_rŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1gviridisŸ±Çbs1a'Ÿ±Ç`a]Ÿ±Ç`a
Ÿ±ÇakcforŸ±Ç`a Ÿ±Ç`ccolŸ±Ç`a Ÿ±ÇbowbinŸ±Ç`a Ÿ±ÇbnberangeŸ±Ç`a(Ÿ±Çbmia2Ÿ±Ç`a)Ÿ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±ÇakcforŸ±Ç`a Ÿ±Ç`crowŸ±Ç`a Ÿ±ÇbowbinŸ±Ç`a Ÿ±ÇbnberangeŸ±Ç`a(Ÿ±Çbmia2Ÿ±Ç`a)Ÿ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±Ç`baxŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`caxsŸ±Ç`a[Ÿ±Ç`crowŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ccolŸ±Ç`a]Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±Ç`cpcmŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`jpcolormeshŸ±Ç`a(Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`frandomŸ±Çaoa.Ÿ±Ç`frandomŸ±Ç`a(Ÿ±Ç`a(Ÿ±Çbmib20Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmib20Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a Ÿ±Çaoa*Ÿ±Ç`a Ÿ±Ç`a(Ÿ±Ç`ccolŸ±Ç`a Ÿ±Çaoa+Ÿ±Ç`a Ÿ±Çbmia1Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`x                            Ÿ±Ç`dcmapŸ±Çaoa=Ÿ±Ç`ecmapsŸ±Ç`a[Ÿ±Ç`ccolŸ±Ç`a]Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±Ç`cfigŸ±Çaoa.Ÿ±Ç`hcolorbarŸ±Ç`a(Ÿ±Ç`cpcmŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`baxŸ±Çaoa=Ÿ±Ç`baxŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`dshowŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1xF######################################################################Ÿ±Ç`a
Ÿ±Çbc1xD# The first column has the same type of data in both rows, so it mayŸ±Ç`a
Ÿ±Çbc1x=# be desirable to combine the colorbar which we do by callingŸ±Ç`a
Ÿ±Çbc1xB# `.Figure.colorbar` with a list of axes instead of a single axes.Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`cfigŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`caxsŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`hsubplotsŸ±Ç`a(Ÿ±Çbmia2Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia2Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`ecmapsŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`a[Ÿ±Çbs1a'Ÿ±Çbs1fRdBu_rŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1gviridisŸ±Çbs1a'Ÿ±Ç`a]Ÿ±Ç`a
Ÿ±ÇakcforŸ±Ç`a Ÿ±Ç`ccolŸ±Ç`a Ÿ±ÇbowbinŸ±Ç`a Ÿ±ÇbnberangeŸ±Ç`a(Ÿ±Çbmia2Ÿ±Ç`a)Ÿ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±ÇakcforŸ±Ç`a Ÿ±Ç`crowŸ±Ç`a Ÿ±ÇbowbinŸ±Ç`a Ÿ±ÇbnberangeŸ±Ç`a(Ÿ±Çbmia2Ÿ±Ç`a)Ÿ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±Ç`baxŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`caxsŸ±Ç`a[Ÿ±Ç`crowŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ccolŸ±Ç`a]Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±Ç`cpcmŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`jpcolormeshŸ±Ç`a(Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`frandomŸ±Çaoa.Ÿ±Ç`frandomŸ±Ç`a(Ÿ±Ç`a(Ÿ±Çbmib20Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmib20Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a Ÿ±Çaoa*Ÿ±Ç`a Ÿ±Ç`a(Ÿ±Ç`ccolŸ±Ç`a Ÿ±Çaoa+Ÿ±Ç`a Ÿ±Çbmia1Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`x                            Ÿ±Ç`dcmapŸ±Çaoa=Ÿ±Ç`ecmapsŸ±Ç`a[Ÿ±Ç`ccolŸ±Ç`a]Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`cfigŸ±Çaoa.Ÿ±Ç`hcolorbarŸ±Ç`a(Ÿ±Ç`cpcmŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`baxŸ±Çaoa=Ÿ±Ç`caxsŸ±Ç`a[Ÿ±Ç`a:Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ccolŸ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`fshrinkŸ±Çaoa=Ÿ±Çbmfc0.6Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`dshowŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1xF######################################################################Ÿ±Ç`a
Ÿ±Çbc1xA# Relatively complicated colorbar layouts are possible using thisŸ±Ç`a
Ÿ±Çbc1x9# paradigm.  Note that this example works far better withŸ±Ç`a
Ÿ±Çbc1x# ``constrained_layout=True``Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`cfigŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`caxsŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`hsubplotsŸ±Ç`a(Ÿ±Çbmia3Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia3Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`rconstrained_layoutŸ±Çaoa=Ÿ±ÇbkcdTrueŸ±Ç`a)Ÿ±Ç`a
Ÿ±ÇakcforŸ±Ç`a Ÿ±Ç`baxŸ±Ç`a Ÿ±ÇbowbinŸ±Ç`a Ÿ±Ç`caxsŸ±Çaoa.Ÿ±Ç`dflatŸ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`cpcmŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`jpcolormeshŸ±Ç`a(Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`frandomŸ±Çaoa.Ÿ±Ç`frandomŸ±Ç`a(Ÿ±Ç`a(Ÿ±Çbmib20Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmib20Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`cfigŸ±Çaoa.Ÿ±Ç`hcolorbarŸ±Ç`a(Ÿ±Ç`cpcmŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`baxŸ±Çaoa=Ÿ±Ç`caxsŸ±Ç`a[Ÿ±Çbmia0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`a:Ÿ±Çbmia2Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`fshrinkŸ±Çaoa=Ÿ±Çbmfc0.6Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`hlocationŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1fbottomŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cfigŸ±Çaoa.Ÿ±Ç`hcolorbarŸ±Ç`a(Ÿ±Ç`cpcmŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`baxŸ±Çaoa=Ÿ±Ç`a[Ÿ±Ç`caxsŸ±Ç`a[Ÿ±Çbmia0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia2Ÿ±Ç`a]Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`hlocationŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1fbottomŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cfigŸ±Çaoa.Ÿ±Ç`hcolorbarŸ±Ç`a(Ÿ±Ç`cpcmŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`baxŸ±Çaoa=Ÿ±Ç`caxsŸ±Ç`a[Ÿ±Çbmia1Ÿ±Ç`a:Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`a:Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`hlocationŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1erightŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`fshrinkŸ±Çaoa=Ÿ±Çbmfc0.6Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cfigŸ±Çaoa.Ÿ±Ç`hcolorbarŸ±Ç`a(Ÿ±Ç`cpcmŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`baxŸ±Çaoa=Ÿ±Ç`a[Ÿ±Ç`caxsŸ±Ç`a[Ÿ±Çbmia2Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia1Ÿ±Ç`a]Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`hlocationŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1dleftŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`dshowŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1xF######################################################################Ÿ±Ç`a
Ÿ±Çbc1x(# Colorbars with fixed-aspect-ratio axesŸ±Ç`a
Ÿ±Çbc1x(# ======================================Ÿ±Ç`a
Ÿ±Çbc1a#Ÿ±Ç`a
Ÿ±Çbc1xH# Placing colorbars for axes with a fixed aspect ratio pose a particularŸ±Ç`a
Ÿ±Çbc1xG# challenge as the parent axes changes size depending on the data view.Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`cfigŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`caxsŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`hsubplotsŸ±Ç`a(Ÿ±Çbmia2Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia2Ÿ±Ç`a,Ÿ±Ç`b  Ÿ±Ç`rconstrained_layoutŸ±Çaoa=Ÿ±ÇbkcdTrueŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`ecmapsŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`a[Ÿ±Çbs1a'Ÿ±Çbs1fRdBu_rŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1gviridisŸ±Çbs1a'Ÿ±Ç`a]Ÿ±Ç`a
Ÿ±ÇakcforŸ±Ç`a Ÿ±Ç`ccolŸ±Ç`a Ÿ±ÇbowbinŸ±Ç`a Ÿ±ÇbnberangeŸ±Ç`a(Ÿ±Çbmia2Ÿ±Ç`a)Ÿ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±ÇakcforŸ±Ç`a Ÿ±Ç`crowŸ±Ç`a Ÿ±ÇbowbinŸ±Ç`a Ÿ±ÇbnberangeŸ±Ç`a(Ÿ±Çbmia2Ÿ±Ç`a)Ÿ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±Ç`baxŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`caxsŸ±Ç`a[Ÿ±Ç`crowŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ccolŸ±Ç`a]Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±Ç`cpcmŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`jpcolormeshŸ±Ç`a(Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`frandomŸ±Çaoa.Ÿ±Ç`frandomŸ±Ç`a(Ÿ±Ç`a(Ÿ±Çbmib20Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmib20Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a Ÿ±Çaoa*Ÿ±Ç`a Ÿ±Ç`a(Ÿ±Ç`ccolŸ±Ç`a Ÿ±Çaoa+Ÿ±Ç`a Ÿ±Çbmia1Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`x                            Ÿ±Ç`dcmapŸ±Çaoa=Ÿ±Ç`ecmapsŸ±Ç`a[Ÿ±Ç`ccolŸ±Ç`a]Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±ÇakbifŸ±Ç`a Ÿ±Ç`ccolŸ±Ç`a Ÿ±Çaob==Ÿ±Ç`a Ÿ±Çbmia0Ÿ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`l            Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`jset_aspectŸ±Ç`a(Ÿ±Çbmia2Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±ÇakdelseŸ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`l            Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`jset_aspectŸ±Ç`a(Ÿ±Çbmia1Ÿ±Çaoa/Ÿ±Çbmia2Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±ÇakbifŸ±Ç`a Ÿ±Ç`crowŸ±Ç`a Ÿ±Çaob==Ÿ±Ç`a Ÿ±Çbmia1Ÿ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`l            Ÿ±Ç`cfigŸ±Çaoa.Ÿ±Ç`hcolorbarŸ±Ç`a(Ÿ±Ç`cpcmŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`baxŸ±Çaoa=Ÿ±Ç`baxŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`fshrinkŸ±Çaoa=Ÿ±Çbmfc0.6Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`dshowŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1xF######################################################################Ÿ±Ç`a
Ÿ±Çbc1xI# One way around this issue is to use an `.Axes.inset_axes` to locate theŸ±Ç`a
Ÿ±Çbc1xF# axes in axes coordinates.  Note that if you zoom in on the axes, andŸ±Ç`a
Ÿ±Çbc1xG# change the shape of the axes, the colorbar will also change position.Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`cfigŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`caxsŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`hsubplotsŸ±Ç`a(Ÿ±Çbmia2Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia2Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`rconstrained_layoutŸ±Çaoa=Ÿ±ÇbkcdTrueŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`ecmapsŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`a[Ÿ±Çbs1a'Ÿ±Çbs1fRdBu_rŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1gviridisŸ±Çbs1a'Ÿ±Ç`a]Ÿ±Ç`a
Ÿ±ÇakcforŸ±Ç`a Ÿ±Ç`ccolŸ±Ç`a Ÿ±ÇbowbinŸ±Ç`a Ÿ±ÇbnberangeŸ±Ç`a(Ÿ±Çbmia2Ÿ±Ç`a)Ÿ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±ÇakcforŸ±Ç`a Ÿ±Ç`crowŸ±Ç`a Ÿ±ÇbowbinŸ±Ç`a Ÿ±ÇbnberangeŸ±Ç`a(Ÿ±Çbmia2Ÿ±Ç`a)Ÿ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±Ç`baxŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`caxsŸ±Ç`a[Ÿ±Ç`crowŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ccolŸ±Ç`a]Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±Ç`cpcmŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`jpcolormeshŸ±Ç`a(Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`frandomŸ±Çaoa.Ÿ±Ç`frandomŸ±Ç`a(Ÿ±Ç`a(Ÿ±Çbmib20Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmib20Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a Ÿ±Çaoa*Ÿ±Ç`a Ÿ±Ç`a(Ÿ±Ç`ccolŸ±Ç`a Ÿ±Çaoa+Ÿ±Ç`a Ÿ±Çbmia1Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`x                            Ÿ±Ç`dcmapŸ±Çaoa=Ÿ±Ç`ecmapsŸ±Ç`a[Ÿ±Ç`ccolŸ±Ç`a]Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±ÇakbifŸ±Ç`a Ÿ±Ç`ccolŸ±Ç`a Ÿ±Çaob==Ÿ±Ç`a Ÿ±Çbmia0Ÿ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`l            Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`jset_aspectŸ±Ç`a(Ÿ±Çbmia2Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±ÇakdelseŸ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`l            Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`jset_aspectŸ±Ç`a(Ÿ±Çbmia1Ÿ±Çaoa/Ÿ±Çbmia2Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±ÇakbifŸ±Ç`a Ÿ±Ç`crowŸ±Ç`a Ÿ±Çaob==Ÿ±Ç`a Ÿ±Çbmia1Ÿ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`l            Ÿ±Ç`ccaxŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`jinset_axesŸ±Ç`a(Ÿ±Ç`a[Ÿ±Çbmfd1.04Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfc0.2Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd0.05Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfc0.6Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`itransformŸ±Çaoa=Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`itransAxesŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`l            Ÿ±Ç`cfigŸ±Çaoa.Ÿ±Ç`hcolorbarŸ±Ç`a(Ÿ±Ç`cpcmŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`baxŸ±Çaoa=Ÿ±Ç`baxŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ccaxŸ±Çaoa=Ÿ±Ç`ccaxŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`dshowŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
`dNoneˆ