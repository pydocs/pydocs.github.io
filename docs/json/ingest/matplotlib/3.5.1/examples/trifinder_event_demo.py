Ù¯‚Ù´ƒ™"Ù±‚bsdy"""
====================
Trifinder Event Demo
====================

Example showing the use of a TriFinder object.  As the mouse is moved over the
triangulation, the triangle under the cursor is highlighted and the index of
the triangle is displayed in the plot title.
"""Ù±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnnfpyplotÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnncpltÙ±‚`a
Ù±‚bkndfromÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnnctriÙ±‚`a Ù±‚bknfimportÙ±‚`a Ù±‚`mTriangulationÙ±‚`a
Ù±‚bkndfromÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnngpatchesÙ±‚`a Ù±‚bknfimportÙ±‚`a Ù±‚`gPolygonÙ±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„enumpyÙ „enumpyf1.22.3fmoduleenumpyfmoduleõÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnnbnpÙ±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚akcdefÙ±‚`a Ù±‚bnfnupdate_polygonÙ±‚`a(Ù±‚`ctriÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`d    Ù±‚akbifÙ±‚`a Ù±‚`ctriÙ±‚`a Ù±‚aob==Ù±‚`a Ù±‚aoa-Ù±‚bmia1Ù±‚`a:Ù±‚`a
Ù±‚`h        Ù±‚`fpointsÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`a[Ù±‚bmia0Ù±‚`a,Ù±‚`a Ù±‚bmia0Ù±‚`a,Ù±‚`a Ù±‚bmia0Ù±‚`a]Ù±‚`a
Ù±‚`d    Ù±‚akdelseÙ±‚`a:Ù±‚`a
Ù±‚`h        Ù±‚`fpointsÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`ftriangÙ±‚aoa.Ù±‚`itrianglesÙ±‚`a[Ù±‚`ctriÙ±‚`a]Ù±‚`a
Ù±‚`d    Ù±‚`bxsÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`ftriangÙ±‚aoa.Ù±‚`axÙ±‚`a[Ù±‚`fpointsÙ±‚`a]Ù±‚`a
Ù±‚`d    Ù±‚`bysÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`ftriangÙ±‚aoa.Ù±‚`ayÙ±‚`a[Ù±‚`fpointsÙ±‚`a]Ù±‚`a
Ù±‚`d    Ù±‚`gpolygonÙ±‚aoa.Ù±‚`fset_xyÙ±‚`a(Ù±‚`bnpÙ±‚aoa.Ù±‚`lcolumn_stackÙ±‚`a(Ù±‚`a[Ù±‚`bxsÙ±‚`a,Ù±‚`a Ù±‚`bysÙ±‚`a]Ù±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚akcdefÙ±‚`a Ù±‚bnfmon_mouse_moveÙ±‚`a(Ù±‚`eeventÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`d    Ù±‚akbifÙ±‚`a Ù±‚`eeventÙ±‚aoa.Ù±‚`finaxesÙ±‚`a Ù±‚bowbisÙ±‚`a Ù±‚bkcdNoneÙ±‚`a:Ù±‚`a
Ù±‚`h        Ù±‚`ctriÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚aoa-Ù±‚bmia1Ù±‚`a
Ù±‚`d    Ù±‚akdelseÙ±‚`a:Ù±‚`a
Ù±‚`h        Ù±‚`ctriÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`itrifinderÙ±‚`a(Ù±‚`eeventÙ±‚aoa.Ù±‚`exdataÙ±‚`a,Ù±‚`a Ù±‚`eeventÙ±‚aoa.Ù±‚`eydataÙ±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`nupdate_polygonÙ±‚`a(Ù±‚`ctriÙ±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`baxÙ±‚aoa.Ù±‚`iset_titleÙ±‚`a(Ù±‚bsaafÙ±‚bs1a'Ù±‚bs1lIn triangle Ù±‚bsia{Ù±‚`ctriÙ±‚bsia}Ù±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`eeventÙ±‚aoa.Ù±‚`fcanvasÙ±‚aoa.Ù±‚`ddrawÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚bc1x# Create a Triangulation.Ù±‚`a
Ù±‚`hn_anglesÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bmib16Ù±‚`a
Ù±‚`gn_radiiÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bmia5Ù±‚`a
Ù±‚`jmin_radiusÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bmfd0.25Ù±‚`a
Ù±‚`eradiiÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`hlinspaceÙ±‚`a(Ù±‚`jmin_radiusÙ±‚`a,Ù±‚`a Ù±‚bmfd0.95Ù±‚`a,Ù±‚`a Ù±‚`gn_radiiÙ±‚`a)Ù±‚`a
Ù±‚`fanglesÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`hlinspaceÙ±‚`a(Ù±‚bmia0Ù±‚`a,Ù±‚`a Ù±‚bmia2Ù±‚`a Ù±‚aoa*Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`bpiÙ±‚`a,Ù±‚`a Ù±‚`hn_anglesÙ±‚`a,Ù±‚`a Ù±‚`hendpointÙ±‚aoa=Ù±‚bkceFalseÙ±‚`a)Ù±‚`a
Ù±‚`fanglesÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`frepeatÙ±‚`a(Ù±‚`fanglesÙ±‚`a[Ù±‚aoa.Ù±‚aoa.Ù±‚aoa.Ù±‚`a,Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`gnewaxisÙ±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`gn_radiiÙ±‚`a,Ù±‚`a Ù±‚`daxisÙ±‚aoa=Ù±‚bmia1Ù±‚`a)Ù±‚`a
Ù±‚`fanglesÙ±‚`a[Ù±‚`a:Ù±‚`a,Ù±‚`a Ù±‚bmia1Ù±‚`a:Ù±‚`a:Ù±‚bmia2Ù±‚`a]Ù±‚`a Ù±‚aoa+Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`bpiÙ±‚`a Ù±‚aoa/Ù±‚`a Ù±‚`hn_anglesÙ±‚`a
Ù±‚`axÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`a(Ù±‚`eradiiÙ±‚aoa*Ù±‚`bnpÙ±‚aoa.Ù±‚`ccosÙ±‚`a(Ù±‚`fanglesÙ±‚`a)Ù±‚`a)Ù±‚aoa.Ù±‚`gflattenÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`ayÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`a(Ù±‚`eradiiÙ±‚aoa*Ù±‚`bnpÙ±‚aoa.Ù±‚`csinÙ±‚`a(Ù±‚`fanglesÙ±‚`a)Ù±‚`a)Ù±‚aoa.Ù±‚`gflattenÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`ftriangÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`mTriangulationÙ±‚`a(Ù±‚`axÙ±‚`a,Ù±‚`a Ù±‚`ayÙ±‚`a)Ù±‚`a
Ù±‚`ftriangÙ±‚aoa.Ù±‚`hset_maskÙ±‚`a(Ù±‚`bnpÙ±‚aoa.Ù±‚`ehypotÙ±‚`a(Ù±‚`axÙ±‚`a[Ù±‚`ftriangÙ±‚aoa.Ù±‚`itrianglesÙ±‚`a]Ù±‚aoa.Ù±‚`dmeanÙ±‚`a(Ù±‚`daxisÙ±‚aoa=Ù±‚bmia1Ù±‚`a)Ù±‚`a,Ù±‚`a
Ù±‚`x                         Ù±‚`ayÙ±‚`a[Ù±‚`ftriangÙ±‚aoa.Ù±‚`itrianglesÙ±‚`a]Ù±‚aoa.Ù±‚`dmeanÙ±‚`a(Ù±‚`daxisÙ±‚aoa=Ù±‚bmia1Ù±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`p                Ù±‚aoa<Ù±‚`a Ù±‚`jmin_radiusÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚bc1x3# Use the triangulation's default TriFinder object.Ù±‚`a
Ù±‚`itrifinderÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`ftriangÙ±‚aoa.Ù±‚`mget_trifinderÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚bc1x# Setup plot and callbacks.Ù±‚`a
Ù±‚`cfigÙ±‚`a,Ù±‚`a Ù±‚`baxÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cpltÙ±‚aoa.Ù±‚`hsubplotsÙ±‚`a(Ù±‚`jsubplot_kwÙ±‚aoa=Ù±‚`a{Ù±‚bs1a'Ù±‚bs1faspectÙ±‚bs1a'Ù±‚`a:Ù±‚`a Ù±‚bs1a'Ù±‚bs1eequalÙ±‚bs1a'Ù±‚`a}Ù±‚`a)Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`gtriplotÙ±‚`a(Ù±‚`ftriangÙ±‚`a,Ù±‚`a Ù±‚bs1a'Ù±‚bs1cbo-Ù±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`gpolygonÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`gPolygonÙ±‚`a(Ù±‚`a[Ù±‚`a[Ù±‚bmia0Ù±‚`a,Ù±‚`a Ù±‚bmia0Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`a[Ù±‚bmia0Ù±‚`a,Ù±‚`a Ù±‚bmia0Ù±‚`a]Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`ifacecolorÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1ayÙ±‚bs1a'Ù±‚`a)Ù±‚`b  Ù±‚bc1x# dummy data for (xs, ys)Ù±‚`a
Ù±‚`nupdate_polygonÙ±‚`a(Ù±‚aoa-Ù±‚bmia1Ù±‚`a)Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`iadd_patchÙ±‚`a(Ù±‚`gpolygonÙ±‚`a)Ù±‚`a
Ù±‚`cfigÙ±‚aoa.Ù±‚`fcanvasÙ±‚aoa.Ù±‚`kmpl_connectÙ±‚`a(Ù±‚bs1a'Ù±‚bs1smotion_notify_eventÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`mon_mouse_moveÙ±‚`a)Ù±‚`a
Ù±‚`cpltÙ±‚aoa.Ù±‚`dshowÙ±‚`a(Ù±‚`a)Ù±‚`a
`dNoneö