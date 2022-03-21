Ù¯‚Ù´ƒ™OÙ±‚bsdy("""
=================================
Triangular 3D filled contour plot
=================================

Filled contour plots of unstructured triangular grids.

The data used is the same as in the second plot of trisurf3d_demo2.
tricontour3d_demo shows the unfilled version of this example.
"""Ù±‚`a
Ù±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnnfpyplotÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnncpltÙ±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnnctriÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnnctriÙ±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„enumpyÙ „enumpyf1.22.3fmoduleenumpyfmoduleõÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnnbnpÙ±‚`a
Ù±‚`a
Ù±‚bc1x5# First create the x, y, z coordinates of the points.Ù±‚`a
Ù±‚`hn_anglesÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bmib48Ù±‚`a
Ù±‚`gn_radiiÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bmia8Ù±‚`a
Ù±‚`jmin_radiusÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bmfd0.25Ù±‚`a
Ù±‚`a
Ù±‚bc1x;# Create the mesh in polar coordinates and compute x, y, z.Ù±‚`a
Ù±‚`eradiiÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`hlinspaceÙ±‚`a(Ù±‚`jmin_radiusÙ±‚`a,Ù±‚`a Ù±‚bmfd0.95Ù±‚`a,Ù±‚`a Ù±‚`gn_radiiÙ±‚`a)Ù±‚`a
Ù±‚`fanglesÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`hlinspaceÙ±‚`a(Ù±‚bmia0Ù±‚`a,Ù±‚`a Ù±‚bmia2Ù±‚aoa*Ù±‚`bnpÙ±‚aoa.Ù±‚`bpiÙ±‚`a,Ù±‚`a Ù±‚`hn_anglesÙ±‚`a,Ù±‚`a Ù±‚`hendpointÙ±‚aoa=Ù±‚bkceFalseÙ±‚`a)Ù±‚`a
Ù±‚`fanglesÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`frepeatÙ±‚`a(Ù±‚`fanglesÙ±‚`a[Ù±‚aoa.Ù±‚aoa.Ù±‚aoa.Ù±‚`a,Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`gnewaxisÙ±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`gn_radiiÙ±‚`a,Ù±‚`a Ù±‚`daxisÙ±‚aoa=Ù±‚bmia1Ù±‚`a)Ù±‚`a
Ù±‚`fanglesÙ±‚`a[Ù±‚`a:Ù±‚`a,Ù±‚`a Ù±‚bmia1Ù±‚`a:Ù±‚`a:Ù±‚bmia2Ù±‚`a]Ù±‚`a Ù±‚aoa+Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`bpiÙ±‚aoa/Ù±‚`hn_anglesÙ±‚`a
Ù±‚`a
Ù±‚`axÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`a(Ù±‚`eradiiÙ±‚aoa*Ù±‚`bnpÙ±‚aoa.Ù±‚`ccosÙ±‚`a(Ù±‚`fanglesÙ±‚`a)Ù±‚`a)Ù±‚aoa.Ù±‚`gflattenÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`ayÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`a(Ù±‚`eradiiÙ±‚aoa*Ù±‚`bnpÙ±‚aoa.Ù±‚`csinÙ±‚`a(Ù±‚`fanglesÙ±‚`a)Ù±‚`a)Ù±‚aoa.Ù±‚`gflattenÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`azÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`a(Ù±‚`bnpÙ±‚aoa.Ù±‚`ccosÙ±‚`a(Ù±‚`eradiiÙ±‚`a)Ù±‚aoa*Ù±‚`bnpÙ±‚aoa.Ù±‚`ccosÙ±‚`a(Ù±‚bmia3Ù±‚aoa*Ù±‚`fanglesÙ±‚`a)Ù±‚`a)Ù±‚aoa.Ù±‚`gflattenÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚bc1x # Create a custom triangulation.Ù±‚`a
Ù±‚`ftriangÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`ctriÙ±‚aoa.Ù±‚`mTriangulationÙ±‚`a(Ù±‚`axÙ±‚`a,Ù±‚`a Ù±‚`ayÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚bc1x# Mask off unwanted triangles.Ù±‚`a
Ù±‚`ftriangÙ±‚aoa.Ù±‚`hset_maskÙ±‚`a(Ù±‚`bnpÙ±‚aoa.Ù±‚`ehypotÙ±‚`a(Ù±‚`axÙ±‚`a[Ù±‚`ftriangÙ±‚aoa.Ù±‚`itrianglesÙ±‚`a]Ù±‚aoa.Ù±‚`dmeanÙ±‚`a(Ù±‚`daxisÙ±‚aoa=Ù±‚bmia1Ù±‚`a)Ù±‚`a,Ù±‚`a
Ù±‚`x                         Ù±‚`ayÙ±‚`a[Ù±‚`ftriangÙ±‚aoa.Ù±‚`itrianglesÙ±‚`a]Ù±‚aoa.Ù±‚`dmeanÙ±‚`a(Ù±‚`daxisÙ±‚aoa=Ù±‚bmia1Ù±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`p                Ù±‚aoa<Ù±‚`a Ù±‚`jmin_radiusÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`baxÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cpltÙ±‚aoa.Ù±‚`ffigureÙ±‚`a(Ù±‚`a)Ù±‚aoa.Ù±‚`kadd_subplotÙ±‚`a(Ù±‚`jprojectionÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1b3dÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`ktricontourfÙ±‚`a(Ù±‚`ftriangÙ±‚`a,Ù±‚`a Ù±‚`azÙ±‚`a,Ù±‚`a Ù±‚`dcmapÙ±‚aoa=Ù±‚`cpltÙ±‚aoa.Ù±‚`bcmÙ±‚aoa.Ù±‚`fCMRmapÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚bc1xA# Customize the view angle so it's easier to understand the plot.Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`iview_initÙ±‚`a(Ù±‚`delevÙ±‚aoa=Ù±‚bmfc45.Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`cpltÙ±‚aoa.Ù±‚`dshowÙ±‚`a(Ù±‚`a)Ù±‚`a
`dNoneö