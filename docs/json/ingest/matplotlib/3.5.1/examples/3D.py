Ù¯‚Ù´ƒ™lÙ±‚bsdxy"""
====================
Frontpage 3D example
====================

This example reproduces the frontpage 3D example.
"""Ù±‚`a
Ù±‚`a
Ù±‚bkndfromÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚`a Ù±‚bknfimportÙ±‚`a Ù±‚`ecbookÙ±‚`a
Ù±‚bkndfromÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚`a Ù±‚bknfimportÙ±‚`a Ù±‚`bcmÙ±‚`a
Ù±‚bkndfromÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnnfcolorsÙ±‚`a Ù±‚bknfimportÙ±‚`a Ù±‚`kLightSourceÙ±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnnfpyplotÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnncpltÙ±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„enumpyÙ „enumpyf1.22.3fmoduleenumpyfmoduleõÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnnbnpÙ±‚`a
Ù±‚`a
Ù±‚`cdemÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`ecbookÙ±‚aoa.Ù±‚`oget_sample_dataÙ±‚`a(Ù±‚bs1a'Ù±‚bs1wjacksboro_fault_dem.npzÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`gnp_loadÙ±‚aoa=Ù±‚bkcdTrueÙ±‚`a)Ù±‚`a
Ù±‚`azÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cdemÙ±‚`a[Ù±‚bs1a'Ù±‚bs1ielevationÙ±‚bs1a'Ù±‚`a]Ù±‚`a
Ù±‚`enrowsÙ±‚`a,Ù±‚`a Ù±‚`encolsÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`azÙ±‚aoa.Ù±‚`eshapeÙ±‚`a
Ù±‚`axÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`hlinspaceÙ±‚`a(Ù±‚`cdemÙ±‚`a[Ù±‚bs1a'Ù±‚bs1dxminÙ±‚bs1a'Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`cdemÙ±‚`a[Ù±‚bs1a'Ù±‚bs1dxmaxÙ±‚bs1a'Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`encolsÙ±‚`a)Ù±‚`a
Ù±‚`ayÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`hlinspaceÙ±‚`a(Ù±‚`cdemÙ±‚`a[Ù±‚bs1a'Ù±‚bs1dyminÙ±‚bs1a'Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`cdemÙ±‚`a[Ù±‚bs1a'Ù±‚bs1dymaxÙ±‚bs1a'Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`enrowsÙ±‚`a)Ù±‚`a
Ù±‚`axÙ±‚`a,Ù±‚`a Ù±‚`ayÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`hmeshgridÙ±‚`a(Ù±‚`axÙ±‚`a,Ù±‚`a Ù±‚`ayÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`fregionÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`bs_Ù±‚`a[Ù±‚bmia5Ù±‚`a:Ù±‚bmib50Ù±‚`a,Ù±‚`a Ù±‚bmia5Ù±‚`a:Ù±‚bmib50Ù±‚`a]Ù±‚`a
Ù±‚`axÙ±‚`a,Ù±‚`a Ù±‚`ayÙ±‚`a,Ù±‚`a Ù±‚`azÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`axÙ±‚`a[Ù±‚`fregionÙ±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`ayÙ±‚`a[Ù±‚`fregionÙ±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`azÙ±‚`a[Ù±‚`fregionÙ±‚`a]Ù±‚`a
Ù±‚`a
Ù±‚`cfigÙ±‚`a,Ù±‚`a Ù±‚`baxÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cpltÙ±‚aoa.Ù±‚`hsubplotsÙ±‚`a(Ù±‚`jsubplot_kwÙ±‚aoa=Ù±‚bnbddictÙ±‚`a(Ù±‚`jprojectionÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1b3dÙ±‚bs1a'Ù±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`blsÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`kLightSourceÙ±‚`a(Ù±‚bmic270Ù±‚`a,Ù±‚`a Ù±‚bmib45Ù±‚`a)Ù±‚`a
Ù±‚bc1xJ# To use a custom hillshading mode, override the built-in shading and passÙ±‚`a
Ù±‚bc1xB# in the rgb colors of the shaded surface calculated from "shade".Ù±‚`a
Ù±‚`crgbÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`blsÙ±‚aoa.Ù±‚`eshadeÙ±‚`a(Ù±‚`azÙ±‚`a,Ù±‚`a Ù±‚`dcmapÙ±‚aoa=Ù±‚`bcmÙ±‚aoa.Ù±‚`jgist_earthÙ±‚`a,Ù±‚`a Ù±‚`ivert_exagÙ±‚aoa=Ù±‚bmfc0.1Ù±‚`a,Ù±‚`a Ù±‚`jblend_modeÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1dsoftÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`dsurfÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`baxÙ±‚aoa.Ù±‚`lplot_surfaceÙ±‚`a(Ù±‚`axÙ±‚`a,Ù±‚`a Ù±‚`ayÙ±‚`a,Ù±‚`a Ù±‚`azÙ±‚`a,Ù±‚`a Ù±‚`grstrideÙ±‚aoa=Ù±‚bmia1Ù±‚`a,Ù±‚`a Ù±‚`gcstrideÙ±‚aoa=Ù±‚bmia1Ù±‚`a,Ù±‚`a Ù±‚`jfacecolorsÙ±‚aoa=Ù±‚`crgbÙ±‚`a,Ù±‚`a
Ù±‚`w                       Ù±‚`ilinewidthÙ±‚aoa=Ù±‚bmia0Ù±‚`a,Ù±‚`a Ù±‚`kantialiasedÙ±‚aoa=Ù±‚bkceFalseÙ±‚`a,Ù±‚`a Ù±‚`eshadeÙ±‚aoa=Ù±‚bkceFalseÙ±‚`a)Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`jset_xticksÙ±‚`a(Ù±‚`a[Ù±‚`a]Ù±‚`a)Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`jset_yticksÙ±‚`a(Ù±‚`a[Ù±‚`a]Ù±‚`a)Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`jset_zticksÙ±‚`a(Ù±‚`a[Ù±‚`a]Ù±‚`a)Ù±‚`a
Ù±‚`cfigÙ±‚aoa.Ù±‚`gsavefigÙ±‚`a(Ù±‚bs2a"Ù±‚bs2wsurface3d_frontpage.pngÙ±‚bs2a"Ù±‚`a,Ù±‚`a Ù±‚`cdpiÙ±‚aoa=Ù±‚bmib25Ù±‚`a)Ù±‚`b  Ù±‚bc1x# results in 160x120 px imageÙ±‚`a
`dNoneö