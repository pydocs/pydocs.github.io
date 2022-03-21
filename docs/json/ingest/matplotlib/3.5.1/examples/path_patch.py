ŸØÇÅŸ¥ÉôeŸ±ÇbsaarŸ±Çbsdx¶"""
================
PathPatch object
================

This example shows how to create `~.path.Path` and `~.patches.PathPatch`
objects through Matplotlib's API.
"""Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±ÇbknfimportŸ±Ç`a Ÿ±ÇbnnŸ¢ÑjmatplotlibŸ†Ñjmatplotlibe3.5.1fmodulejmatplotlibfmoduleıŸ±Çbnna.Ÿ±ÇbnndpathŸ±Ç`a Ÿ±ÇakbasŸ±Ç`a Ÿ±ÇbnnempathŸ±Ç`a
Ÿ±ÇbknfimportŸ±Ç`a Ÿ±ÇbnnŸ¢ÑjmatplotlibŸ†Ñjmatplotlibe3.5.1fmodulejmatplotlibfmoduleıŸ±Çbnna.Ÿ±ÇbnngpatchesŸ±Ç`a Ÿ±ÇakbasŸ±Ç`a Ÿ±ÇbnnhmpatchesŸ±Ç`a
Ÿ±ÇbknfimportŸ±Ç`a Ÿ±ÇbnnŸ¢ÑjmatplotlibŸ†Ñjmatplotlibe3.5.1fmodulejmatplotlibfmoduleıŸ±Çbnna.Ÿ±ÇbnnfpyplotŸ±Ç`a Ÿ±ÇakbasŸ±Ç`a Ÿ±ÇbnncpltŸ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`cfigŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`baxŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`hsubplotsŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`dPathŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`empathŸ±Çaoa.Ÿ±Ç`dPathŸ±Ç`a
Ÿ±Ç`ipath_dataŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`a[Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`a(Ÿ±Ç`dPathŸ±Çaoa.Ÿ±Ç`fMOVETOŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`a(Ÿ±Çbmfd1.58Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çaoa-Ÿ±Çbmfd2.57Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`a(Ÿ±Ç`dPathŸ±Çaoa.Ÿ±Ç`fCURVE4Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`a(Ÿ±Çbmfd0.35Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çaoa-Ÿ±Çbmfc1.1Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`a(Ÿ±Ç`dPathŸ±Çaoa.Ÿ±Ç`fCURVE4Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`a(Ÿ±Çaoa-Ÿ±Çbmfd1.75Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfc2.0Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`a(Ÿ±Ç`dPathŸ±Çaoa.Ÿ±Ç`fCURVE4Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`a(Ÿ±Çbmfe0.375Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfc2.0Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`a(Ÿ±Ç`dPathŸ±Çaoa.Ÿ±Ç`fLINETOŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`a(Ÿ±Çbmfd0.85Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd1.15Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`a(Ÿ±Ç`dPathŸ±Çaoa.Ÿ±Ç`fCURVE4Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`a(Ÿ±Çbmfc2.2Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfc3.2Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`a(Ÿ±Ç`dPathŸ±Çaoa.Ÿ±Ç`fCURVE4Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`a(Ÿ±Çbmia3Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd0.05Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`a(Ÿ±Ç`dPathŸ±Çaoa.Ÿ±Ç`fCURVE4Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`a(Ÿ±Çbmfc2.0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çaoa-Ÿ±Çbmfc0.5Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`a(Ÿ±Ç`dPathŸ±Çaoa.Ÿ±Ç`iCLOSEPOLYŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`a(Ÿ±Çbmfd1.58Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çaoa-Ÿ±Çbmfd2.57Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`a]Ÿ±Ç`a
Ÿ±Ç`ecodesŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`evertsŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±ÇbnbczipŸ±Ç`a(Ÿ±Çaoa*Ÿ±Ç`ipath_dataŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`dpathŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`empathŸ±Çaoa.Ÿ±Ç`dPathŸ±Ç`a(Ÿ±Ç`evertsŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ecodesŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`epatchŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`hmpatchesŸ±Çaoa.Ÿ±Ç`iPathPatchŸ±Ç`a(Ÿ±Ç`dpathŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ifacecolorŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1arŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ealphaŸ±Çaoa=Ÿ±Çbmfc0.5Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`iadd_patchŸ±Ç`a(Ÿ±Ç`epatchŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1x*# plot control points and connecting linesŸ±Ç`a
Ÿ±Ç`axŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ayŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±ÇbnbczipŸ±Ç`a(Ÿ±Çaoa*Ÿ±Ç`dpathŸ±Çaoa.Ÿ±Ç`hverticesŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`dlineŸ±Ç`a,Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`dplotŸ±Ç`a(Ÿ±Ç`axŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ayŸ±Ç`a,Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1cgo-Ÿ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`dgridŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`daxisŸ±Ç`a(Ÿ±Çbs1a'Ÿ±Çbs1eequalŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
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
Ÿ±Çbc1x'#    - `matplotlib.axes.Axes.add_patch`Ÿ±Ç`a
`dNoneˆ