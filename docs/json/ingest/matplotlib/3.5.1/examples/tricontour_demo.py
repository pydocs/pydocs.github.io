Ù¯‚Ù´ƒ™	¸Ù±‚bsdxh"""
===============
Tricontour Demo
===============

Contour plots of unstructured triangular grids.
"""Ù±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnnfpyplotÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnncpltÙ±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnnctriÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnnctriÙ±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„enumpyÙ „enumpyf1.22.3fmoduleenumpyfmoduleõÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnnbnpÙ±‚`a
Ù±‚`a
Ù±‚bc1xO###############################################################################Ù±‚`a
Ù±‚bc1xJ# Creating a Triangulation without specifying the triangles results in theÙ±‚`a
Ù±‚bc1x'# Delaunay triangulation of the points.Ù±‚`a
Ù±‚`a
Ù±‚bc1x5# First create the x and y coordinates of the points.Ù±‚`a
Ù±‚`hn_anglesÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bmib48Ù±‚`a
Ù±‚`gn_radiiÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bmia8Ù±‚`a
Ù±‚`jmin_radiusÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bmfd0.25Ù±‚`a
Ù±‚`eradiiÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`hlinspaceÙ±‚`a(Ù±‚`jmin_radiusÙ±‚`a,Ù±‚`a Ù±‚bmfd0.95Ù±‚`a,Ù±‚`a Ù±‚`gn_radiiÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`fanglesÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`hlinspaceÙ±‚`a(Ù±‚bmia0Ù±‚`a,Ù±‚`a Ù±‚bmia2Ù±‚`a Ù±‚aoa*Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`bpiÙ±‚`a,Ù±‚`a Ù±‚`hn_anglesÙ±‚`a,Ù±‚`a Ù±‚`hendpointÙ±‚aoa=Ù±‚bkceFalseÙ±‚`a)Ù±‚`a
Ù±‚`fanglesÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`frepeatÙ±‚`a(Ù±‚`fanglesÙ±‚`a[Ù±‚aoa.Ù±‚aoa.Ù±‚aoa.Ù±‚`a,Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`gnewaxisÙ±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`gn_radiiÙ±‚`a,Ù±‚`a Ù±‚`daxisÙ±‚aoa=Ù±‚bmia1Ù±‚`a)Ù±‚`a
Ù±‚`fanglesÙ±‚`a[Ù±‚`a:Ù±‚`a,Ù±‚`a Ù±‚bmia1Ù±‚`a:Ù±‚`a:Ù±‚bmia2Ù±‚`a]Ù±‚`a Ù±‚aoa+Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`bpiÙ±‚`a Ù±‚aoa/Ù±‚`a Ù±‚`hn_anglesÙ±‚`a
Ù±‚`a
Ù±‚`axÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`a(Ù±‚`eradiiÙ±‚`a Ù±‚aoa*Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`ccosÙ±‚`a(Ù±‚`fanglesÙ±‚`a)Ù±‚`a)Ù±‚aoa.Ù±‚`gflattenÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`ayÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`a(Ù±‚`eradiiÙ±‚`a Ù±‚aoa*Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`csinÙ±‚`a(Ù±‚`fanglesÙ±‚`a)Ù±‚`a)Ù±‚aoa.Ù±‚`gflattenÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`azÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`a(Ù±‚`bnpÙ±‚aoa.Ù±‚`ccosÙ±‚`a(Ù±‚`eradiiÙ±‚`a)Ù±‚`a Ù±‚aoa*Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`ccosÙ±‚`a(Ù±‚bmia3Ù±‚`a Ù±‚aoa*Ù±‚`a Ù±‚`fanglesÙ±‚`a)Ù±‚`a)Ù±‚aoa.Ù±‚`gflattenÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚bc1xK# Create the Triangulation; no triangles so Delaunay triangulation created.Ù±‚`a
Ù±‚`ftriangÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`ctriÙ±‚aoa.Ù±‚`mTriangulationÙ±‚`a(Ù±‚`axÙ±‚`a,Ù±‚`a Ù±‚`ayÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚bc1x# Mask off unwanted triangles.Ù±‚`a
Ù±‚`ftriangÙ±‚aoa.Ù±‚`hset_maskÙ±‚`a(Ù±‚`bnpÙ±‚aoa.Ù±‚`ehypotÙ±‚`a(Ù±‚`axÙ±‚`a[Ù±‚`ftriangÙ±‚aoa.Ù±‚`itrianglesÙ±‚`a]Ù±‚aoa.Ù±‚`dmeanÙ±‚`a(Ù±‚`daxisÙ±‚aoa=Ù±‚bmia1Ù±‚`a)Ù±‚`a,Ù±‚`a
Ù±‚`x                         Ù±‚`ayÙ±‚`a[Ù±‚`ftriangÙ±‚aoa.Ù±‚`itrianglesÙ±‚`a]Ù±‚aoa.Ù±‚`dmeanÙ±‚`a(Ù±‚`daxisÙ±‚aoa=Ù±‚bmia1Ù±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`p                Ù±‚aoa<Ù±‚`a Ù±‚`jmin_radiusÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚bc1xO###############################################################################Ù±‚`a
Ù±‚bc1n# pcolor plot.Ù±‚`a
Ù±‚`a
Ù±‚`dfig1Ù±‚`a,Ù±‚`a Ù±‚`cax1Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cpltÙ±‚aoa.Ù±‚`hsubplotsÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`cax1Ù±‚aoa.Ù±‚`jset_aspectÙ±‚`a(Ù±‚bs1a'Ù±‚bs1eequalÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`ctcfÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cax1Ù±‚aoa.Ù±‚`ktricontourfÙ±‚`a(Ù±‚`ftriangÙ±‚`a,Ù±‚`a Ù±‚`azÙ±‚`a)Ù±‚`a
Ù±‚`dfig1Ù±‚aoa.Ù±‚`hcolorbarÙ±‚`a(Ù±‚`ctcfÙ±‚`a)Ù±‚`a
Ù±‚`cax1Ù±‚aoa.Ù±‚`jtricontourÙ±‚`a(Ù±‚`ftriangÙ±‚`a,Ù±‚`a Ù±‚`azÙ±‚`a,Ù±‚`a Ù±‚`fcolorsÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1akÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`cax1Ù±‚aoa.Ù±‚`iset_titleÙ±‚`a(Ù±‚bs1a'Ù±‚bs1x&Contour plot of Delaunay triangulationÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚bc1xO###############################################################################Ù±‚`a
Ù±‚bc1xF# You could also specify hatching patterns along with different cmaps.Ù±‚`a
Ù±‚`a
Ù±‚`dfig2Ù±‚`a,Ù±‚`a Ù±‚`cax2Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cpltÙ±‚aoa.Ù±‚`hsubplotsÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`cax2Ù±‚aoa.Ù±‚`jset_aspectÙ±‚`a(Ù±‚bs2a"Ù±‚bs2eequalÙ±‚bs2a"Ù±‚`a)Ù±‚`a
Ù±‚`ctcfÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cax2Ù±‚aoa.Ù±‚`ktricontourfÙ±‚`a(Ù±‚`a
Ù±‚`d    Ù±‚`ftriangÙ±‚`a,Ù±‚`a
Ù±‚`d    Ù±‚`azÙ±‚`a,Ù±‚`a
Ù±‚`d    Ù±‚`ghatchesÙ±‚aoa=Ù±‚`a[Ù±‚bs2a"Ù±‚bs2a*Ù±‚bs2a"Ù±‚`a,Ù±‚`a Ù±‚bs2a"Ù±‚bs2a-Ù±‚bs2a"Ù±‚`a,Ù±‚`a Ù±‚bs2a"Ù±‚bs2a/Ù±‚bs2a"Ù±‚`a,Ù±‚`a Ù±‚bs2a"Ù±‚bs2b//Ù±‚bs2a"Ù±‚`a,Ù±‚`a Ù±‚bs2a"Ù±‚bseb\\Ù±‚bs2a"Ù±‚`a,Ù±‚`a Ù±‚bkcdNoneÙ±‚`a]Ù±‚`a,Ù±‚`a
Ù±‚`d    Ù±‚`dcmapÙ±‚aoa=Ù±‚bs2a"Ù±‚bs2gcividisÙ±‚bs2a"Ù±‚`a
Ù±‚`a)Ù±‚`a
Ù±‚`dfig2Ù±‚aoa.Ù±‚`hcolorbarÙ±‚`a(Ù±‚`ctcfÙ±‚`a)Ù±‚`a
Ù±‚`cax2Ù±‚aoa.Ù±‚`jtricontourÙ±‚`a(Ù±‚`ftriangÙ±‚`a,Ù±‚`a Ù±‚`azÙ±‚`a,Ù±‚`a Ù±‚`jlinestylesÙ±‚aoa=Ù±‚bs2a"Ù±‚bs2esolidÙ±‚bs2a"Ù±‚`a,Ù±‚`a Ù±‚`fcolorsÙ±‚aoa=Ù±‚bs2a"Ù±‚bs2akÙ±‚bs2a"Ù±‚`a,Ù±‚`a Ù±‚`jlinewidthsÙ±‚aoa=Ù±‚bmfc2.0Ù±‚`a)Ù±‚`a
Ù±‚`cax2Ù±‚aoa.Ù±‚`iset_titleÙ±‚`a(Ù±‚bs2a"Ù±‚bs2x.Hatched Contour plot of Delaunay triangulationÙ±‚bs2a"Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚bc1xO###############################################################################Ù±‚`a
Ù±‚bc1xB# You could also generate hatching patterns labeled with no color.Ù±‚`a
Ù±‚`a
Ù±‚`dfig3Ù±‚`a,Ù±‚`a Ù±‚`cax3Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cpltÙ±‚aoa.Ù±‚`hsubplotsÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`hn_levelsÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bmia7Ù±‚`a
Ù±‚`ctcfÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cax3Ù±‚aoa.Ù±‚`ktricontourfÙ±‚`a(Ù±‚`a
Ù±‚`d    Ù±‚`ftriangÙ±‚`a,Ù±‚`a
Ù±‚`d    Ù±‚`azÙ±‚`a,Ù±‚`a
Ù±‚`d    Ù±‚`hn_levelsÙ±‚`a,Ù±‚`a
Ù±‚`d    Ù±‚`fcolorsÙ±‚aoa=Ù±‚bs2a"Ù±‚bs2dnoneÙ±‚bs2a"Ù±‚`a,Ù±‚`a
Ù±‚`d    Ù±‚`ghatchesÙ±‚aoa=Ù±‚`a[Ù±‚bs2a"Ù±‚bs2a.Ù±‚bs2a"Ù±‚`a,Ù±‚`a Ù±‚bs2a"Ù±‚bs2a/Ù±‚bs2a"Ù±‚`a,Ù±‚`a Ù±‚bs2a"Ù±‚bseb\\Ù±‚bs2a"Ù±‚`a,Ù±‚`a Ù±‚bkcdNoneÙ±‚`a,Ù±‚`a Ù±‚bs2a"Ù±‚bseb\\Ù±‚bseb\\Ù±‚bs2a"Ù±‚`a,Ù±‚`a Ù±‚bs2a"Ù±‚bs2a*Ù±‚bs2a"Ù±‚`a]Ù±‚`a,Ù±‚`a
Ù±‚`a)Ù±‚`a
Ù±‚`cax3Ù±‚aoa.Ù±‚`jtricontourÙ±‚`a(Ù±‚`ftriangÙ±‚`a,Ù±‚`a Ù±‚`azÙ±‚`a,Ù±‚`a Ù±‚`hn_levelsÙ±‚`a,Ù±‚`a Ù±‚`fcolorsÙ±‚aoa=Ù±‚bs2a"Ù±‚bs2eblackÙ±‚bs2a"Ù±‚`a,Ù±‚`a Ù±‚`jlinestylesÙ±‚aoa=Ù±‚bs2a"Ù±‚bs2a-Ù±‚bs2a"Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚bc1x%# create a legend for the contour setÙ±‚`a
Ù±‚`gartistsÙ±‚`a,Ù±‚`a Ù±‚`flabelsÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`ctcfÙ±‚aoa.Ù±‚`olegend_elementsÙ±‚`a(Ù±‚`jstr_formatÙ±‚aoa=Ù±‚bs2a"Ù±‚bsig{:2.1f}Ù±‚bs2a"Ù±‚aoa.Ù±‚`fformatÙ±‚`a)Ù±‚`a
Ù±‚`cax3Ù±‚aoa.Ù±‚`flegendÙ±‚`a(Ù±‚`gartistsÙ±‚`a,Ù±‚`a Ù±‚`flabelsÙ±‚`a,Ù±‚`a Ù±‚`lhandleheightÙ±‚aoa=Ù±‚bmia2Ù±‚`a,Ù±‚`a Ù±‚`jframealphaÙ±‚aoa=Ù±‚bmia1Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚bc1xO###############################################################################Ù±‚`a
Ù±‚bc1xG# You can specify your own triangulation rather than perform a DelaunayÙ±‚`a
Ù±‚bc1xM# triangulation of the points, where each triangle is given by the indices ofÙ±‚`a
Ù±‚bc1xN# the three points that make up the triangle, ordered in either a clockwise orÙ±‚`a
Ù±‚bc1w# anticlockwise manner.Ù±‚`a
Ù±‚`a
Ù±‚`bxyÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`gasarrayÙ±‚`a(Ù±‚`a[Ù±‚`a
Ù±‚`d    Ù±‚`a[Ù±‚aoa-Ù±‚bmfe0.101Ù±‚`a,Ù±‚`a Ù±‚bmfe0.872Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`a[Ù±‚aoa-Ù±‚bmfe0.080Ù±‚`a,Ù±‚`a Ù±‚bmfe0.883Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`a[Ù±‚aoa-Ù±‚bmfe0.069Ù±‚`a,Ù±‚`a Ù±‚bmfe0.888Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`a[Ù±‚aoa-Ù±‚bmfe0.054Ù±‚`a,Ù±‚`a Ù±‚bmfe0.890Ù±‚`a]Ù±‚`a,Ù±‚`a
Ù±‚`d    Ù±‚`a[Ù±‚aoa-Ù±‚bmfe0.045Ù±‚`a,Ù±‚`a Ù±‚bmfe0.897Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`a[Ù±‚aoa-Ù±‚bmfe0.057Ù±‚`a,Ù±‚`a Ù±‚bmfe0.895Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`a[Ù±‚aoa-Ù±‚bmfe0.073Ù±‚`a,Ù±‚`a Ù±‚bmfe0.900Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`a[Ù±‚aoa-Ù±‚bmfe0.087Ù±‚`a,Ù±‚`a Ù±‚bmfe0.898Ù±‚`a]Ù±‚`a,Ù±‚`a
Ù±‚`d    Ù±‚`a[Ù±‚aoa-Ù±‚bmfe0.090Ù±‚`a,Ù±‚`a Ù±‚bmfe0.904Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`a[Ù±‚aoa-Ù±‚bmfe0.069Ù±‚`a,Ù±‚`a Ù±‚bmfe0.907Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`a[Ù±‚aoa-Ù±‚bmfe0.069Ù±‚`a,Ù±‚`a Ù±‚bmfe0.921Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`a[Ù±‚aoa-Ù±‚bmfe0.080Ù±‚`a,Ù±‚`a Ù±‚bmfe0.919Ù±‚`a]Ù±‚`a,Ù±‚`a
Ù±‚`d    Ù±‚`a[Ù±‚aoa-Ù±‚bmfe0.073Ù±‚`a,Ù±‚`a Ù±‚bmfe0.928Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`a[Ù±‚aoa-Ù±‚bmfe0.052Ù±‚`a,Ù±‚`a Ù±‚bmfe0.930Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`a[Ù±‚aoa-Ù±‚bmfe0.048Ù±‚`a,Ù±‚`a Ù±‚bmfe0.942Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`a[Ù±‚aoa-Ù±‚bmfe0.062Ù±‚`a,Ù±‚`a Ù±‚bmfe0.949Ù±‚`a]Ù±‚`a,Ù±‚`a
Ù±‚`d    Ù±‚`a[Ù±‚aoa-Ù±‚bmfe0.054Ù±‚`a,Ù±‚`a Ù±‚bmfe0.958Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`a[Ù±‚aoa-Ù±‚bmfe0.069Ù±‚`a,Ù±‚`a Ù±‚bmfe0.954Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`a[Ù±‚aoa-Ù±‚bmfe0.087Ù±‚`a,Ù±‚`a Ù±‚bmfe0.952Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`a[Ù±‚aoa-Ù±‚bmfe0.087Ù±‚`a,Ù±‚`a Ù±‚bmfe0.959Ù±‚`a]Ù±‚`a,Ù±‚`a
Ù±‚`d    Ù±‚`a[Ù±‚aoa-Ù±‚bmfe0.080Ù±‚`a,Ù±‚`a Ù±‚bmfe0.966Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`a[Ù±‚aoa-Ù±‚bmfe0.085Ù±‚`a,Ù±‚`a Ù±‚bmfe0.973Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`a[Ù±‚aoa-Ù±‚bmfe0.087Ù±‚`a,Ù±‚`a Ù±‚bmfe0.965Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`a[Ù±‚aoa-Ù±‚bmfe0.097Ù±‚`a,Ù±‚`a Ù±‚bmfe0.965Ù±‚`a]Ù±‚`a,Ù±‚`a
Ù±‚`d    Ù±‚`a[Ù±‚aoa-Ù±‚bmfe0.097Ù±‚`a,Ù±‚`a Ù±‚bmfe0.975Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`a[Ù±‚aoa-Ù±‚bmfe0.092Ù±‚`a,Ù±‚`a Ù±‚bmfe0.984Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`a[Ù±‚aoa-Ù±‚bmfe0.101Ù±‚`a,Ù±‚`a Ù±‚bmfe0.980Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`a[Ù±‚aoa-Ù±‚bmfe0.108Ù±‚`a,Ù±‚`a Ù±‚bmfe0.980Ù±‚`a]Ù±‚`a,Ù±‚`a
Ù±‚`d    Ù±‚`a[Ù±‚aoa-Ù±‚bmfe0.104Ù±‚`a,Ù±‚`a Ù±‚bmfe0.987Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`a[Ù±‚aoa-Ù±‚bmfe0.102Ù±‚`a,Ù±‚`a Ù±‚bmfe0.993Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`a[Ù±‚aoa-Ù±‚bmfe0.115Ù±‚`a,Ù±‚`a Ù±‚bmfe1.001Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`a[Ù±‚aoa-Ù±‚bmfe0.099Ù±‚`a,Ù±‚`a Ù±‚bmfe0.996Ù±‚`a]Ù±‚`a,Ù±‚`a
Ù±‚`d    Ù±‚`a[Ù±‚aoa-Ù±‚bmfe0.101Ù±‚`a,Ù±‚`a Ù±‚bmfe1.007Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`a[Ù±‚aoa-Ù±‚bmfe0.090Ù±‚`a,Ù±‚`a Ù±‚bmfe1.010Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`a[Ù±‚aoa-Ù±‚bmfe0.087Ù±‚`a,Ù±‚`a Ù±‚bmfe1.021Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`a[Ù±‚aoa-Ù±‚bmfe0.069Ù±‚`a,Ù±‚`a Ù±‚bmfe1.021Ù±‚`a]Ù±‚`a,Ù±‚`a
Ù±‚`d    Ù±‚`a[Ù±‚aoa-Ù±‚bmfe0.052Ù±‚`a,Ù±‚`a Ù±‚bmfe1.022Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`a[Ù±‚aoa-Ù±‚bmfe0.052Ù±‚`a,Ù±‚`a Ù±‚bmfe1.017Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`a[Ù±‚aoa-Ù±‚bmfe0.069Ù±‚`a,Ù±‚`a Ù±‚bmfe1.010Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`a[Ù±‚aoa-Ù±‚bmfe0.064Ù±‚`a,Ù±‚`a Ù±‚bmfe1.005Ù±‚`a]Ù±‚`a,Ù±‚`a
Ù±‚`d    Ù±‚`a[Ù±‚aoa-Ù±‚bmfe0.048Ù±‚`a,Ù±‚`a Ù±‚bmfe1.005Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`a[Ù±‚aoa-Ù±‚bmfe0.031Ù±‚`a,Ù±‚`a Ù±‚bmfe1.005Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`a[Ù±‚aoa-Ù±‚bmfe0.031Ù±‚`a,Ù±‚`a Ù±‚bmfe0.996Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`a[Ù±‚aoa-Ù±‚bmfe0.040Ù±‚`a,Ù±‚`a Ù±‚bmfe0.987Ù±‚`a]Ù±‚`a,Ù±‚`a
Ù±‚`d    Ù±‚`a[Ù±‚aoa-Ù±‚bmfe0.045Ù±‚`a,Ù±‚`a Ù±‚bmfe0.980Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`a[Ù±‚aoa-Ù±‚bmfe0.052Ù±‚`a,Ù±‚`a Ù±‚bmfe0.975Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`a[Ù±‚aoa-Ù±‚bmfe0.040Ù±‚`a,Ù±‚`a Ù±‚bmfe0.973Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`a[Ù±‚aoa-Ù±‚bmfe0.026Ù±‚`a,Ù±‚`a Ù±‚bmfe0.968Ù±‚`a]Ù±‚`a,Ù±‚`a
Ù±‚`d    Ù±‚`a[Ù±‚aoa-Ù±‚bmfe0.020Ù±‚`a,Ù±‚`a Ù±‚bmfe0.954Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`a[Ù±‚aoa-Ù±‚bmfe0.006Ù±‚`a,Ù±‚`a Ù±‚bmfe0.947Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`a[Ù±‚`a Ù±‚bmfe0.003Ù±‚`a,Ù±‚`a Ù±‚bmfe0.935Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`a[Ù±‚`a Ù±‚bmfe0.006Ù±‚`a,Ù±‚`a Ù±‚bmfe0.926Ù±‚`a]Ù±‚`a,Ù±‚`a
Ù±‚`d    Ù±‚`a[Ù±‚`a Ù±‚bmfe0.005Ù±‚`a,Ù±‚`a Ù±‚bmfe0.921Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`a[Ù±‚`a Ù±‚bmfe0.022Ù±‚`a,Ù±‚`a Ù±‚bmfe0.923Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`a[Ù±‚`a Ù±‚bmfe0.033Ù±‚`a,Ù±‚`a Ù±‚bmfe0.912Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`a[Ù±‚`a Ù±‚bmfe0.029Ù±‚`a,Ù±‚`a Ù±‚bmfe0.905Ù±‚`a]Ù±‚`a,Ù±‚`a
Ù±‚`d    Ù±‚`a[Ù±‚`a Ù±‚bmfe0.017Ù±‚`a,Ù±‚`a Ù±‚bmfe0.900Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`a[Ù±‚`a Ù±‚bmfe0.012Ù±‚`a,Ù±‚`a Ù±‚bmfe0.895Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`a[Ù±‚`a Ù±‚bmfe0.027Ù±‚`a,Ù±‚`a Ù±‚bmfe0.893Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`a[Ù±‚`a Ù±‚bmfe0.019Ù±‚`a,Ù±‚`a Ù±‚bmfe0.886Ù±‚`a]Ù±‚`a,Ù±‚`a
Ù±‚`d    Ù±‚`a[Ù±‚`a Ù±‚bmfe0.001Ù±‚`a,Ù±‚`a Ù±‚bmfe0.883Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`a[Ù±‚aoa-Ù±‚bmfe0.012Ù±‚`a,Ù±‚`a Ù±‚bmfe0.884Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`a[Ù±‚aoa-Ù±‚bmfe0.029Ù±‚`a,Ù±‚`a Ù±‚bmfe0.883Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`a[Ù±‚aoa-Ù±‚bmfe0.038Ù±‚`a,Ù±‚`a Ù±‚bmfe0.879Ù±‚`a]Ù±‚`a,Ù±‚`a
Ù±‚`d    Ù±‚`a[Ù±‚aoa-Ù±‚bmfe0.057Ù±‚`a,Ù±‚`a Ù±‚bmfe0.881Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`a[Ù±‚aoa-Ù±‚bmfe0.062Ù±‚`a,Ù±‚`a Ù±‚bmfe0.876Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`a[Ù±‚aoa-Ù±‚bmfe0.078Ù±‚`a,Ù±‚`a Ù±‚bmfe0.876Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`a[Ù±‚aoa-Ù±‚bmfe0.087Ù±‚`a,Ù±‚`a Ù±‚bmfe0.872Ù±‚`a]Ù±‚`a,Ù±‚`a
Ù±‚`d    Ù±‚`a[Ù±‚aoa-Ù±‚bmfe0.030Ù±‚`a,Ù±‚`a Ù±‚bmfe0.907Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`a[Ù±‚aoa-Ù±‚bmfe0.007Ù±‚`a,Ù±‚`a Ù±‚bmfe0.905Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`a[Ù±‚aoa-Ù±‚bmfe0.057Ù±‚`a,Ù±‚`a Ù±‚bmfe0.916Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`a[Ù±‚aoa-Ù±‚bmfe0.025Ù±‚`a,Ù±‚`a Ù±‚bmfe0.933Ù±‚`a]Ù±‚`a,Ù±‚`a
Ù±‚`d    Ù±‚`a[Ù±‚aoa-Ù±‚bmfe0.077Ù±‚`a,Ù±‚`a Ù±‚bmfe0.990Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`a[Ù±‚aoa-Ù±‚bmfe0.059Ù±‚`a,Ù±‚`a Ù±‚bmfe0.993Ù±‚`a]Ù±‚`a]Ù±‚`a)Ù±‚`a
Ù±‚`axÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`gdegreesÙ±‚`a(Ù±‚`bxyÙ±‚`a[Ù±‚`a:Ù±‚`a,Ù±‚`a Ù±‚bmia0Ù±‚`a]Ù±‚`a)Ù±‚`a
Ù±‚`ayÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`gdegreesÙ±‚`a(Ù±‚`bxyÙ±‚`a[Ù±‚`a:Ù±‚`a,Ù±‚`a Ù±‚bmia1Ù±‚`a]Ù±‚`a)Ù±‚`a
Ù±‚`bx0Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚aoa-Ù±‚bmia5Ù±‚`a
Ù±‚`by0Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bmib52Ù±‚`a
Ù±‚`azÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`cexpÙ±‚`a(Ù±‚aoa-Ù±‚bmfd0.01Ù±‚`a Ù±‚aoa*Ù±‚`a Ù±‚`a(Ù±‚`a(Ù±‚`axÙ±‚`a Ù±‚aoa-Ù±‚`a Ù±‚`bx0Ù±‚`a)Ù±‚`a Ù±‚aoa*Ù±‚aoa*Ù±‚`a Ù±‚bmia2Ù±‚`a Ù±‚aoa+Ù±‚`a Ù±‚`a(Ù±‚`ayÙ±‚`a Ù±‚aoa-Ù±‚`a Ù±‚`by0Ù±‚`a)Ù±‚`a Ù±‚aoa*Ù±‚aoa*Ù±‚`a Ù±‚bmia2Ù±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`itrianglesÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`gasarrayÙ±‚`a(Ù±‚`a[Ù±‚`a
Ù±‚`d    Ù±‚`a[Ù±‚bmib67Ù±‚`a,Ù±‚`a Ù±‚bmib66Ù±‚`a,Ù±‚`b  Ù±‚bmia1Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`a[Ù±‚bmib65Ù±‚`a,Ù±‚`b  Ù±‚bmia2Ù±‚`a,Ù±‚`a Ù±‚bmib66Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`a[Ù±‚`a Ù±‚bmia1Ù±‚`a,Ù±‚`a Ù±‚bmib66Ù±‚`a,Ù±‚`b  Ù±‚bmia2Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`a[Ù±‚bmib64Ù±‚`a,Ù±‚`b  Ù±‚bmia2Ù±‚`a,Ù±‚`a Ù±‚bmib65Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`a[Ù±‚bmib63Ù±‚`a,Ù±‚`b  Ù±‚bmia3Ù±‚`a,Ù±‚`a Ù±‚bmib64Ù±‚`a]Ù±‚`a,Ù±‚`a
Ù±‚`d    Ù±‚`a[Ù±‚bmib60Ù±‚`a,Ù±‚`a Ù±‚bmib59Ù±‚`a,Ù±‚`a Ù±‚bmib57Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`a[Ù±‚`a Ù±‚bmia2Ù±‚`a,Ù±‚`a Ù±‚bmib64Ù±‚`a,Ù±‚`b  Ù±‚bmia3Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`a[Ù±‚`a Ù±‚bmia3Ù±‚`a,Ù±‚`a Ù±‚bmib63Ù±‚`a,Ù±‚`b  Ù±‚bmia4Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`a[Ù±‚`a Ù±‚bmia0Ù±‚`a,Ù±‚`a Ù±‚bmib67Ù±‚`a,Ù±‚`b  Ù±‚bmia1Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`a[Ù±‚bmib62Ù±‚`a,Ù±‚`b  Ù±‚bmia4Ù±‚`a,Ù±‚`a Ù±‚bmib63Ù±‚`a]Ù±‚`a,Ù±‚`a
Ù±‚`d    Ù±‚`a[Ù±‚bmib57Ù±‚`a,Ù±‚`a Ù±‚bmib59Ù±‚`a,Ù±‚`a Ù±‚bmib56Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`a[Ù±‚bmib59Ù±‚`a,Ù±‚`a Ù±‚bmib58Ù±‚`a,Ù±‚`a Ù±‚bmib56Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`a[Ù±‚bmib61Ù±‚`a,Ù±‚`a Ù±‚bmib60Ù±‚`a,Ù±‚`a Ù±‚bmib69Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`a[Ù±‚bmib57Ù±‚`a,Ù±‚`a Ù±‚bmib69Ù±‚`a,Ù±‚`a Ù±‚bmib60Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`a[Ù±‚`a Ù±‚bmia4Ù±‚`a,Ù±‚`a Ù±‚bmib62Ù±‚`a,Ù±‚`a Ù±‚bmib68Ù±‚`a]Ù±‚`a,Ù±‚`a
Ù±‚`d    Ù±‚`a[Ù±‚`a Ù±‚bmia6Ù±‚`a,Ù±‚`b  Ù±‚bmia5Ù±‚`a,Ù±‚`b  Ù±‚bmia9Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`a[Ù±‚bmib61Ù±‚`a,Ù±‚`a Ù±‚bmib68Ù±‚`a,Ù±‚`a Ù±‚bmib62Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`a[Ù±‚bmib69Ù±‚`a,Ù±‚`a Ù±‚bmib68Ù±‚`a,Ù±‚`a Ù±‚bmib61Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`a[Ù±‚`a Ù±‚bmia9Ù±‚`a,Ù±‚`b  Ù±‚bmia5Ù±‚`a,Ù±‚`a Ù±‚bmib70Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`a[Ù±‚`a Ù±‚bmia6Ù±‚`a,Ù±‚`b  Ù±‚bmia8Ù±‚`a,Ù±‚`b  Ù±‚bmia7Ù±‚`a]Ù±‚`a,Ù±‚`a
Ù±‚`d    Ù±‚`a[Ù±‚`a Ù±‚bmia4Ù±‚`a,Ù±‚`a Ù±‚bmib70Ù±‚`a,Ù±‚`b  Ù±‚bmia5Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`a[Ù±‚`a Ù±‚bmia8Ù±‚`a,Ù±‚`b  Ù±‚bmia6Ù±‚`a,Ù±‚`b  Ù±‚bmia9Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`a[Ù±‚bmib56Ù±‚`a,Ù±‚`a Ù±‚bmib69Ù±‚`a,Ù±‚`a Ù±‚bmib57Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`a[Ù±‚bmib69Ù±‚`a,Ù±‚`a Ù±‚bmib56Ù±‚`a,Ù±‚`a Ù±‚bmib52Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`a[Ù±‚bmib70Ù±‚`a,Ù±‚`a Ù±‚bmib10Ù±‚`a,Ù±‚`b  Ù±‚bmia9Ù±‚`a]Ù±‚`a,Ù±‚`a
Ù±‚`d    Ù±‚`a[Ù±‚bmib54Ù±‚`a,Ù±‚`a Ù±‚bmib53Ù±‚`a,Ù±‚`a Ù±‚bmib55Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`a[Ù±‚bmib56Ù±‚`a,Ù±‚`a Ù±‚bmib55Ù±‚`a,Ù±‚`a Ù±‚bmib53Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`a[Ù±‚bmib68Ù±‚`a,Ù±‚`a Ù±‚bmib70Ù±‚`a,Ù±‚`b  Ù±‚bmia4Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`a[Ù±‚bmib52Ù±‚`a,Ù±‚`a Ù±‚bmib56Ù±‚`a,Ù±‚`a Ù±‚bmib53Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`a[Ù±‚bmib11Ù±‚`a,Ù±‚`a Ù±‚bmib10Ù±‚`a,Ù±‚`a Ù±‚bmib12Ù±‚`a]Ù±‚`a,Ù±‚`a
Ù±‚`d    Ù±‚`a[Ù±‚bmib69Ù±‚`a,Ù±‚`a Ù±‚bmib71Ù±‚`a,Ù±‚`a Ù±‚bmib68Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`a[Ù±‚bmib68Ù±‚`a,Ù±‚`a Ù±‚bmib13Ù±‚`a,Ù±‚`a Ù±‚bmib70Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`a[Ù±‚bmib10Ù±‚`a,Ù±‚`a Ù±‚bmib70Ù±‚`a,Ù±‚`a Ù±‚bmib13Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`a[Ù±‚bmib51Ù±‚`a,Ù±‚`a Ù±‚bmib50Ù±‚`a,Ù±‚`a Ù±‚bmib52Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`a[Ù±‚bmib13Ù±‚`a,Ù±‚`a Ù±‚bmib68Ù±‚`a,Ù±‚`a Ù±‚bmib71Ù±‚`a]Ù±‚`a,Ù±‚`a
Ù±‚`d    Ù±‚`a[Ù±‚bmib52Ù±‚`a,Ù±‚`a Ù±‚bmib71Ù±‚`a,Ù±‚`a Ù±‚bmib69Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`a[Ù±‚bmib12Ù±‚`a,Ù±‚`a Ù±‚bmib10Ù±‚`a,Ù±‚`a Ù±‚bmib13Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`a[Ù±‚bmib71Ù±‚`a,Ù±‚`a Ù±‚bmib52Ù±‚`a,Ù±‚`a Ù±‚bmib50Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`a[Ù±‚bmib71Ù±‚`a,Ù±‚`a Ù±‚bmib14Ù±‚`a,Ù±‚`a Ù±‚bmib13Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`a[Ù±‚bmib50Ù±‚`a,Ù±‚`a Ù±‚bmib49Ù±‚`a,Ù±‚`a Ù±‚bmib71Ù±‚`a]Ù±‚`a,Ù±‚`a
Ù±‚`d    Ù±‚`a[Ù±‚bmib49Ù±‚`a,Ù±‚`a Ù±‚bmib48Ù±‚`a,Ù±‚`a Ù±‚bmib71Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`a[Ù±‚bmib14Ù±‚`a,Ù±‚`a Ù±‚bmib16Ù±‚`a,Ù±‚`a Ù±‚bmib15Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`a[Ù±‚bmib14Ù±‚`a,Ù±‚`a Ù±‚bmib71Ù±‚`a,Ù±‚`a Ù±‚bmib48Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`a[Ù±‚bmib17Ù±‚`a,Ù±‚`a Ù±‚bmib19Ù±‚`a,Ù±‚`a Ù±‚bmib18Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`a[Ù±‚bmib17Ù±‚`a,Ù±‚`a Ù±‚bmib20Ù±‚`a,Ù±‚`a Ù±‚bmib19Ù±‚`a]Ù±‚`a,Ù±‚`a
Ù±‚`d    Ù±‚`a[Ù±‚bmib48Ù±‚`a,Ù±‚`a Ù±‚bmib16Ù±‚`a,Ù±‚`a Ù±‚bmib14Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`a[Ù±‚bmib48Ù±‚`a,Ù±‚`a Ù±‚bmib47Ù±‚`a,Ù±‚`a Ù±‚bmib16Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`a[Ù±‚bmib47Ù±‚`a,Ù±‚`a Ù±‚bmib46Ù±‚`a,Ù±‚`a Ù±‚bmib16Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`a[Ù±‚bmib16Ù±‚`a,Ù±‚`a Ù±‚bmib46Ù±‚`a,Ù±‚`a Ù±‚bmib45Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`a[Ù±‚bmib23Ù±‚`a,Ù±‚`a Ù±‚bmib22Ù±‚`a,Ù±‚`a Ù±‚bmib24Ù±‚`a]Ù±‚`a,Ù±‚`a
Ù±‚`d    Ù±‚`a[Ù±‚bmib21Ù±‚`a,Ù±‚`a Ù±‚bmib24Ù±‚`a,Ù±‚`a Ù±‚bmib22Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`a[Ù±‚bmib17Ù±‚`a,Ù±‚`a Ù±‚bmib16Ù±‚`a,Ù±‚`a Ù±‚bmib45Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`a[Ù±‚bmib20Ù±‚`a,Ù±‚`a Ù±‚bmib17Ù±‚`a,Ù±‚`a Ù±‚bmib45Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`a[Ù±‚bmib21Ù±‚`a,Ù±‚`a Ù±‚bmib25Ù±‚`a,Ù±‚`a Ù±‚bmib24Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`a[Ù±‚bmib27Ù±‚`a,Ù±‚`a Ù±‚bmib26Ù±‚`a,Ù±‚`a Ù±‚bmib28Ù±‚`a]Ù±‚`a,Ù±‚`a
Ù±‚`d    Ù±‚`a[Ù±‚bmib20Ù±‚`a,Ù±‚`a Ù±‚bmib72Ù±‚`a,Ù±‚`a Ù±‚bmib21Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`a[Ù±‚bmib25Ù±‚`a,Ù±‚`a Ù±‚bmib21Ù±‚`a,Ù±‚`a Ù±‚bmib72Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`a[Ù±‚bmib45Ù±‚`a,Ù±‚`a Ù±‚bmib72Ù±‚`a,Ù±‚`a Ù±‚bmib20Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`a[Ù±‚bmib25Ù±‚`a,Ù±‚`a Ù±‚bmib28Ù±‚`a,Ù±‚`a Ù±‚bmib26Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`a[Ù±‚bmib44Ù±‚`a,Ù±‚`a Ù±‚bmib73Ù±‚`a,Ù±‚`a Ù±‚bmib45Ù±‚`a]Ù±‚`a,Ù±‚`a
Ù±‚`d    Ù±‚`a[Ù±‚bmib72Ù±‚`a,Ù±‚`a Ù±‚bmib45Ù±‚`a,Ù±‚`a Ù±‚bmib73Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`a[Ù±‚bmib28Ù±‚`a,Ù±‚`a Ù±‚bmib25Ù±‚`a,Ù±‚`a Ù±‚bmib29Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`a[Ù±‚bmib29Ù±‚`a,Ù±‚`a Ù±‚bmib25Ù±‚`a,Ù±‚`a Ù±‚bmib31Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`a[Ù±‚bmib43Ù±‚`a,Ù±‚`a Ù±‚bmib73Ù±‚`a,Ù±‚`a Ù±‚bmib44Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`a[Ù±‚bmib73Ù±‚`a,Ù±‚`a Ù±‚bmib43Ù±‚`a,Ù±‚`a Ù±‚bmib40Ù±‚`a]Ù±‚`a,Ù±‚`a
Ù±‚`d    Ù±‚`a[Ù±‚bmib72Ù±‚`a,Ù±‚`a Ù±‚bmib73Ù±‚`a,Ù±‚`a Ù±‚bmib39Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`a[Ù±‚bmib72Ù±‚`a,Ù±‚`a Ù±‚bmib31Ù±‚`a,Ù±‚`a Ù±‚bmib25Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`a[Ù±‚bmib42Ù±‚`a,Ù±‚`a Ù±‚bmib40Ù±‚`a,Ù±‚`a Ù±‚bmib43Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`a[Ù±‚bmib31Ù±‚`a,Ù±‚`a Ù±‚bmib30Ù±‚`a,Ù±‚`a Ù±‚bmib29Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`a[Ù±‚bmib39Ù±‚`a,Ù±‚`a Ù±‚bmib73Ù±‚`a,Ù±‚`a Ù±‚bmib40Ù±‚`a]Ù±‚`a,Ù±‚`a
Ù±‚`d    Ù±‚`a[Ù±‚bmib42Ù±‚`a,Ù±‚`a Ù±‚bmib41Ù±‚`a,Ù±‚`a Ù±‚bmib40Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`a[Ù±‚bmib72Ù±‚`a,Ù±‚`a Ù±‚bmib33Ù±‚`a,Ù±‚`a Ù±‚bmib31Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`a[Ù±‚bmib32Ù±‚`a,Ù±‚`a Ù±‚bmib31Ù±‚`a,Ù±‚`a Ù±‚bmib33Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`a[Ù±‚bmib39Ù±‚`a,Ù±‚`a Ù±‚bmib38Ù±‚`a,Ù±‚`a Ù±‚bmib72Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`a[Ù±‚bmib33Ù±‚`a,Ù±‚`a Ù±‚bmib72Ù±‚`a,Ù±‚`a Ù±‚bmib38Ù±‚`a]Ù±‚`a,Ù±‚`a
Ù±‚`d    Ù±‚`a[Ù±‚bmib33Ù±‚`a,Ù±‚`a Ù±‚bmib38Ù±‚`a,Ù±‚`a Ù±‚bmib34Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`a[Ù±‚bmib37Ù±‚`a,Ù±‚`a Ù±‚bmib35Ù±‚`a,Ù±‚`a Ù±‚bmib38Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`a[Ù±‚bmib34Ù±‚`a,Ù±‚`a Ù±‚bmib38Ù±‚`a,Ù±‚`a Ù±‚bmib35Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`a[Ù±‚bmib35Ù±‚`a,Ù±‚`a Ù±‚bmib37Ù±‚`a,Ù±‚`a Ù±‚bmib36Ù±‚`a]Ù±‚`a]Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚bc1xO###############################################################################Ù±‚`a
Ù±‚bc1xO# Rather than create a Triangulation object, can simply pass x, y and trianglesÙ±‚`a
Ù±‚bc1xJ# arrays to tripcolor directly.  It would be better to use a TriangulationÙ±‚`a
Ù±‚bc1xH# object if the same triangulation was to be used more than once to saveÙ±‚`a
Ù±‚bc1x# duplicated calculations.Ù±‚`a
Ù±‚`a
Ù±‚`dfig4Ù±‚`a,Ù±‚`a Ù±‚`cax4Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cpltÙ±‚aoa.Ù±‚`hsubplotsÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`cax4Ù±‚aoa.Ù±‚`jset_aspectÙ±‚`a(Ù±‚bs1a'Ù±‚bs1eequalÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`ctcfÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cax4Ù±‚aoa.Ù±‚`ktricontourfÙ±‚`a(Ù±‚`axÙ±‚`a,Ù±‚`a Ù±‚`ayÙ±‚`a,Ù±‚`a Ù±‚`itrianglesÙ±‚`a,Ù±‚`a Ù±‚`azÙ±‚`a)Ù±‚`a
Ù±‚`dfig4Ù±‚aoa.Ù±‚`hcolorbarÙ±‚`a(Ù±‚`ctcfÙ±‚`a)Ù±‚`a
Ù±‚`cax4Ù±‚aoa.Ù±‚`iset_titleÙ±‚`a(Ù±‚bs1a'Ù±‚bs1x,Contour plot of user-specified triangulationÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`cax4Ù±‚aoa.Ù±‚`jset_xlabelÙ±‚`a(Ù±‚bs1a'Ù±‚bs1sLongitude (degrees)Ù±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`cax4Ù±‚aoa.Ù±‚`jset_ylabelÙ±‚`a(Ù±‚bs1a'Ù±‚bs1rLatitude (degrees)Ù±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`cpltÙ±‚aoa.Ù±‚`dshowÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚bc1xM#############################################################################Ù±‚`a
Ù±‚bc1a#Ù±‚`a
Ù±‚bc1x# .. admonition:: ReferencesÙ±‚`a
Ù±‚bc1a#Ù±‚`a
Ù±‚bc1xN#    The use of the following functions, methods, classes and modules is shownÙ±‚`a
Ù±‚bc1u#    in this example:Ù±‚`a
Ù±‚bc1a#Ù±‚`a
Ù±‚bc1xK#    - `matplotlib.axes.Axes.tricontourf` / `matplotlib.pyplot.tricontourf`Ù±‚`a
Ù±‚bc1x%#    - `matplotlib.tri.Triangulation`Ù±‚`a
Ù±‚bc1xI#    - `matplotlib.figure.Figure.colorbar` / `matplotlib.pyplot.colorbar`Ù±‚`a
Ù±‚bc1xA#    - `matplotlib.axes.Axes.legend` / `matplotlib.pyplot.legend`Ù±‚`a
Ù±‚bc1x6#    - `matplotlib.contour.ContourSet.legend_elements`Ù±‚`a
`dNoneö