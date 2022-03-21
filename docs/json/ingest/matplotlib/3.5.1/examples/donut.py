ŸØÇÅŸ¥ÉôWŸ±ÇbsaarŸ±Çbsdx«"""
=============
Mmh Donuts!!!
=============

Draw donuts (miam!) using `~.path.Path`\s and `~.patches.PathPatch`\es.
This example shows the effect of the path's orientations in a compound path.
"""Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±ÇbknfimportŸ±Ç`a Ÿ±ÇbnnŸ¢ÑenumpyŸ†Ñenumpyf1.22.3fmoduleenumpyfmoduleıŸ±Ç`a Ÿ±ÇakbasŸ±Ç`a Ÿ±ÇbnnbnpŸ±Ç`a
Ÿ±ÇbknfimportŸ±Ç`a Ÿ±ÇbnnŸ¢ÑjmatplotlibŸ†Ñjmatplotlibe3.5.1fmodulejmatplotlibfmoduleıŸ±Çbnna.Ÿ±ÇbnndpathŸ±Ç`a Ÿ±ÇakbasŸ±Ç`a Ÿ±ÇbnnempathŸ±Ç`a
Ÿ±ÇbknfimportŸ±Ç`a Ÿ±ÇbnnŸ¢ÑjmatplotlibŸ†Ñjmatplotlibe3.5.1fmodulejmatplotlibfmoduleıŸ±Çbnna.Ÿ±ÇbnngpatchesŸ±Ç`a Ÿ±ÇakbasŸ±Ç`a Ÿ±ÇbnnhmpatchesŸ±Ç`a
Ÿ±ÇbknfimportŸ±Ç`a Ÿ±ÇbnnŸ¢ÑjmatplotlibŸ†Ñjmatplotlibe3.5.1fmodulejmatplotlibfmoduleıŸ±Çbnna.Ÿ±ÇbnnfpyplotŸ±Ç`a Ÿ±ÇakbasŸ±Ç`a Ÿ±ÇbnncpltŸ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±ÇakcdefŸ±Ç`a Ÿ±ÇbnfdwiseŸ±Ç`a(Ÿ±Ç`avŸ±Ç`a)Ÿ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±ÇakbifŸ±Ç`a Ÿ±Ç`avŸ±Ç`a Ÿ±Çaob==Ÿ±Ç`a Ÿ±Çbmia1Ÿ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±ÇakfreturnŸ±Ç`a Ÿ±Çbs2a"Ÿ±Çbs2cCCWŸ±Çbs2a"Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±ÇakdelseŸ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±ÇakfreturnŸ±Ç`a Ÿ±Çbs2a"Ÿ±Çbs2bCWŸ±Çbs2a"Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±ÇakcdefŸ±Ç`a Ÿ±Çbnfkmake_circleŸ±Ç`a(Ÿ±Ç`arŸ±Ç`a)Ÿ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`atŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`farangeŸ±Ç`a(Ÿ±Çbmia0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`bpiŸ±Ç`a Ÿ±Çaoa*Ÿ±Ç`a Ÿ±Çbmfc2.0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd0.01Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`atŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`atŸ±Çaoa.Ÿ±Ç`greshapeŸ±Ç`a(Ÿ±Ç`a(Ÿ±ÇbnbclenŸ±Ç`a(Ÿ±Ç`atŸ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia1Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`axŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`arŸ±Ç`a Ÿ±Çaoa*Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`ccosŸ±Ç`a(Ÿ±Ç`atŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`ayŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`arŸ±Ç`a Ÿ±Çaoa*Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`csinŸ±Ç`a(Ÿ±Ç`atŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±ÇakfreturnŸ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`fhstackŸ±Ç`a(Ÿ±Ç`a(Ÿ±Ç`axŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ayŸ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`dPathŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`empathŸ±Çaoa.Ÿ±Ç`dPathŸ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`cfigŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`baxŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`hsubplotsŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`oinside_verticesŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`kmake_circleŸ±Ç`a(Ÿ±Çbmfc0.5Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`poutside_verticesŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`kmake_circleŸ±Ç`a(Ÿ±Çbmfc1.0Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`ecodesŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`donesŸ±Ç`a(Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±ÇbnbclenŸ±Ç`a(Ÿ±Ç`oinside_verticesŸ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`edtypeŸ±Çaoa=Ÿ±Ç`empathŸ±Çaoa.Ÿ±Ç`dPathŸ±Çaoa.Ÿ±Ç`icode_typeŸ±Ç`a)Ÿ±Ç`a Ÿ±Çaoa*Ÿ±Ç`a Ÿ±Ç`empathŸ±Çaoa.Ÿ±Ç`dPathŸ±Çaoa.Ÿ±Ç`fLINETOŸ±Ç`a
Ÿ±Ç`ecodesŸ±Ç`a[Ÿ±Çbmia0Ÿ±Ç`a]Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`empathŸ±Çaoa.Ÿ±Ç`dPathŸ±Çaoa.Ÿ±Ç`fMOVETOŸ±Ç`a
Ÿ±Ç`a
Ÿ±ÇakcforŸ±Ç`a Ÿ±Ç`aiŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`a(Ÿ±Ç`finsideŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`goutsideŸ±Ç`a)Ÿ±Ç`a Ÿ±ÇbowbinŸ±Ç`a Ÿ±ÇbnbienumerateŸ±Ç`a(Ÿ±Ç`a(Ÿ±Ç`a(Ÿ±Çbmia1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia1Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`a(Ÿ±Çbmia1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çaoa-Ÿ±Çbmia1Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`a(Ÿ±Çaoa-Ÿ±Çbmia1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia1Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`a(Ÿ±Çaoa-Ÿ±Çbmia1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çaoa-Ÿ±Çbmia1Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Çbc1xF# Concatenate the inside and outside subpaths together, changing theirŸ±Ç`a
Ÿ±Ç`d    Ÿ±Çbc1q# order as neededŸ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`hverticesŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`kconcatenateŸ±Ç`a(Ÿ±Ç`a(Ÿ±Ç`poutside_verticesŸ±Ç`a[Ÿ±Ç`a:Ÿ±Ç`a:Ÿ±Ç`goutsideŸ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`x                               Ÿ±Ç`oinside_verticesŸ±Ç`a[Ÿ±Ç`a:Ÿ±Ç`a:Ÿ±Ç`finsideŸ±Ç`a]Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Çbc1p# Shift the pathŸ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`hverticesŸ±Ç`a[Ÿ±Ç`a:Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia0Ÿ±Ç`a]Ÿ±Ç`a Ÿ±Çaoa+Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`aiŸ±Ç`a Ÿ±Çaoa*Ÿ±Ç`a Ÿ±Çbmfc2.5Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Çbc1xF# The codes will be all "LINETO" commands, except for "MOVETO"s at theŸ±Ç`a
Ÿ±Ç`d    Ÿ±Çbc1x# beginning of each subpathŸ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`iall_codesŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`kconcatenateŸ±Ç`a(Ÿ±Ç`a(Ÿ±Ç`ecodesŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ecodesŸ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Çbc1x# Create the Path objectŸ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`dpathŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`empathŸ±Çaoa.Ÿ±Ç`dPathŸ±Ç`a(Ÿ±Ç`hverticesŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`iall_codesŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Çbc1m# Add plot itŸ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`epatchŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`hmpatchesŸ±Çaoa.Ÿ±Ç`iPathPatchŸ±Ç`a(Ÿ±Ç`dpathŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ifacecolorŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1g#885500Ÿ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`iedgecolorŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1eblackŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`iadd_patchŸ±Ç`a(Ÿ±Ç`epatchŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`hannotateŸ±Ç`a(Ÿ±Çbs2a"Ÿ±Çbs2hOutside Ÿ±Çbsib%sŸ±Çbs2a,Ÿ±Çbseb\nŸ±Çbs2gInside Ÿ±Çbsib%sŸ±Çbs2a"Ÿ±Ç`a Ÿ±Çaoa%Ÿ±Ç`a Ÿ±Ç`a(Ÿ±Ç`dwiseŸ±Ç`a(Ÿ±Ç`goutsideŸ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dwiseŸ±Ç`a(Ÿ±Ç`finsideŸ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`p                Ÿ±Ç`a(Ÿ±Ç`aiŸ±Ç`a Ÿ±Çaoa*Ÿ±Ç`a Ÿ±Çbmfc2.5Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çaoa-Ÿ±Çbmfc1.5Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`bvaŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2ctopŸ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`bhaŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2fcenterŸ±Çbs2a"Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`hset_xlimŸ±Ç`a(Ÿ±Çaoa-Ÿ±Çbmia2Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmib10Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`hset_ylimŸ±Ç`a(Ÿ±Çaoa-Ÿ±Çbmia3Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia2Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`iset_titleŸ±Ç`a(Ÿ±Çbs1a'Ÿ±Çbs1lMmm, donuts!Ÿ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`jset_aspectŸ±Ç`a(Ÿ±Çbmfc1.0Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`dshowŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1xM#############################################################################Ÿ±Ç`a
Ÿ±Çbc1a#Ÿ±Ç`a
Ÿ±Çbc1x# .. admonition:: ReferencesŸ±Ç`a
Ÿ±Çbc1a#Ÿ±Ç`a
Ÿ±Çbc1xN#    The use of the following functions, methods, classes and modules is shownŸ±Ç`a
Ÿ±Çbc1u#    in this example:Ÿ±Ç`a
Ÿ±Çbc1a#Ÿ±Ç`a
Ÿ±Çbc1x#    - `matplotlib.path`Ÿ±Ç`a
Ÿ±Çbc1x#    - `matplotlib.path.Path`Ÿ±Ç`a
Ÿ±Çbc1x#    - `matplotlib.patches`Ÿ±Ç`a
Ÿ±Çbc1x%#    - `matplotlib.patches.PathPatch`Ÿ±Ç`a
Ÿ±Çbc1x"#    - `matplotlib.patches.Circle`Ÿ±Ç`a
Ÿ±Çbc1x'#    - `matplotlib.axes.Axes.add_patch`Ÿ±Ç`a
Ÿ±Çbc1x&#    - `matplotlib.axes.Axes.annotate`Ÿ±Ç`a
Ÿ±Çbc1x(#    - `matplotlib.axes.Axes.set_aspect`Ÿ±Ç`a
Ÿ±Çbc1x&#    - `matplotlib.axes.Axes.set_xlim`Ÿ±Ç`a
Ÿ±Çbc1x&#    - `matplotlib.axes.Axes.set_ylim`Ÿ±Ç`a
Ÿ±Çbc1x'#    - `matplotlib.axes.Axes.set_title`Ÿ±Ç`a
`dNoneˆ