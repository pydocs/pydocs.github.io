Ù¯‚Ù´ƒ™ Ù±‚bsdyC"""
===========================
More triangular 3D surfaces
===========================

Two additional examples of plotting surfaces with triangular mesh.

The first demonstrates use of plot_trisurf's triangles argument, and the
second sets a Triangulation object's mask and passes the object directly
to plot_trisurf.
"""Ù±‚`a
Ù±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„enumpyÙ „enumpyf1.22.3fmoduleenumpyfmoduleõÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnnbnpÙ±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnnfpyplotÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnncpltÙ±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnnctriÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnndmtriÙ±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚`cfigÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cpltÙ±‚aoa.Ù±‚`ffigureÙ±‚`a(Ù±‚`gfigsizeÙ±‚aoa=Ù±‚`cpltÙ±‚aoa.Ù±‚`ifigaspectÙ±‚`a(Ù±‚bmfc0.5Ù±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚bc1l# ==========Ù±‚`a
Ù±‚bc1l# First plotÙ±‚`a
Ù±‚bc1l# ==========Ù±‚`a
Ù±‚`a
Ù±‚bc1x@# Make a mesh in the space of parameterisation variables u and vÙ±‚`a
Ù±‚`auÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`hlinspaceÙ±‚`a(Ù±‚bmia0Ù±‚`a,Ù±‚`a Ù±‚bmfc2.0Ù±‚`a Ù±‚aoa*Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`bpiÙ±‚`a,Ù±‚`a Ù±‚`hendpointÙ±‚aoa=Ù±‚bkcdTrueÙ±‚`a,Ù±‚`a Ù±‚`cnumÙ±‚aoa=Ù±‚bmib50Ù±‚`a)Ù±‚`a
Ù±‚`avÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`hlinspaceÙ±‚`a(Ù±‚aoa-Ù±‚bmfc0.5Ù±‚`a,Ù±‚`a Ù±‚bmfc0.5Ù±‚`a,Ù±‚`a Ù±‚`hendpointÙ±‚aoa=Ù±‚bkcdTrueÙ±‚`a,Ù±‚`a Ù±‚`cnumÙ±‚aoa=Ù±‚bmib10Ù±‚`a)Ù±‚`a
Ù±‚`auÙ±‚`a,Ù±‚`a Ù±‚`avÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`hmeshgridÙ±‚`a(Ù±‚`auÙ±‚`a,Ù±‚`a Ù±‚`avÙ±‚`a)Ù±‚`a
Ù±‚`auÙ±‚`a,Ù±‚`a Ù±‚`avÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`auÙ±‚aoa.Ù±‚`gflattenÙ±‚`a(Ù±‚`a)Ù±‚`a,Ù±‚`a Ù±‚`avÙ±‚aoa.Ù±‚`gflattenÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚bc1xI# This is the Mobius mapping, taking a u, v pair and returning an x, y, zÙ±‚`a
Ù±‚bc1h# tripleÙ±‚`a
Ù±‚`axÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`a(Ù±‚bmia1Ù±‚`a Ù±‚aoa+Ù±‚`a Ù±‚bmfc0.5Ù±‚`a Ù±‚aoa*Ù±‚`a Ù±‚`avÙ±‚`a Ù±‚aoa*Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`ccosÙ±‚`a(Ù±‚`auÙ±‚`a Ù±‚aoa/Ù±‚`a Ù±‚bmfc2.0Ù±‚`a)Ù±‚`a)Ù±‚`a Ù±‚aoa*Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`ccosÙ±‚`a(Ù±‚`auÙ±‚`a)Ù±‚`a
Ù±‚`ayÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`a(Ù±‚bmia1Ù±‚`a Ù±‚aoa+Ù±‚`a Ù±‚bmfc0.5Ù±‚`a Ù±‚aoa*Ù±‚`a Ù±‚`avÙ±‚`a Ù±‚aoa*Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`ccosÙ±‚`a(Ù±‚`auÙ±‚`a Ù±‚aoa/Ù±‚`a Ù±‚bmfc2.0Ù±‚`a)Ù±‚`a)Ù±‚`a Ù±‚aoa*Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`csinÙ±‚`a(Ù±‚`auÙ±‚`a)Ù±‚`a
Ù±‚`azÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bmfc0.5Ù±‚`a Ù±‚aoa*Ù±‚`a Ù±‚`avÙ±‚`a Ù±‚aoa*Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`csinÙ±‚`a(Ù±‚`auÙ±‚`a Ù±‚aoa/Ù±‚`a Ù±‚bmfc2.0Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚bc1x8# Triangulate parameter space to determine the trianglesÙ±‚`a
Ù±‚`ctriÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`dmtriÙ±‚aoa.Ù±‚`mTriangulationÙ±‚`a(Ù±‚`auÙ±‚`a,Ù±‚`a Ù±‚`avÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚bc1xM# Plot the surface.  The triangles in parameter space determine which x, y, zÙ±‚`a
Ù±‚bc1x"# points are connected by an edge.Ù±‚`a
Ù±‚`baxÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cfigÙ±‚aoa.Ù±‚`kadd_subplotÙ±‚`a(Ù±‚bmia1Ù±‚`a,Ù±‚`a Ù±‚bmia2Ù±‚`a,Ù±‚`a Ù±‚bmia1Ù±‚`a,Ù±‚`a Ù±‚`jprojectionÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1b3dÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`lplot_trisurfÙ±‚`a(Ù±‚`axÙ±‚`a,Ù±‚`a Ù±‚`ayÙ±‚`a,Ù±‚`a Ù±‚`azÙ±‚`a,Ù±‚`a Ù±‚`itrianglesÙ±‚aoa=Ù±‚`ctriÙ±‚aoa.Ù±‚`itrianglesÙ±‚`a,Ù±‚`a Ù±‚`dcmapÙ±‚aoa=Ù±‚`cpltÙ±‚aoa.Ù±‚`bcmÙ±‚aoa.Ù±‚`hSpectralÙ±‚`a)Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`hset_zlimÙ±‚`a(Ù±‚aoa-Ù±‚bmia1Ù±‚`a,Ù±‚`a Ù±‚bmia1Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚bc1m# ===========Ù±‚`a
Ù±‚bc1m# Second plotÙ±‚`a
Ù±‚bc1m# ===========Ù±‚`a
Ù±‚`a
Ù±‚bc1x)# Make parameter spaces radii and angles.Ù±‚`a
Ù±‚`hn_anglesÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bmib36Ù±‚`a
Ù±‚`gn_radiiÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bmia8Ù±‚`a
Ù±‚`jmin_radiusÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bmfd0.25Ù±‚`a
Ù±‚`eradiiÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`hlinspaceÙ±‚`a(Ù±‚`jmin_radiusÙ±‚`a,Ù±‚`a Ù±‚bmfd0.95Ù±‚`a,Ù±‚`a Ù±‚`gn_radiiÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`fanglesÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`hlinspaceÙ±‚`a(Ù±‚bmia0Ù±‚`a,Ù±‚`a Ù±‚bmia2Ù±‚aoa*Ù±‚`bnpÙ±‚aoa.Ù±‚`bpiÙ±‚`a,Ù±‚`a Ù±‚`hn_anglesÙ±‚`a,Ù±‚`a Ù±‚`hendpointÙ±‚aoa=Ù±‚bkceFalseÙ±‚`a)Ù±‚`a
Ù±‚`fanglesÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`frepeatÙ±‚`a(Ù±‚`fanglesÙ±‚`a[Ù±‚aoa.Ù±‚aoa.Ù±‚aoa.Ù±‚`a,Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`gnewaxisÙ±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`gn_radiiÙ±‚`a,Ù±‚`a Ù±‚`daxisÙ±‚aoa=Ù±‚bmia1Ù±‚`a)Ù±‚`a
Ù±‚`fanglesÙ±‚`a[Ù±‚`a:Ù±‚`a,Ù±‚`a Ù±‚bmia1Ù±‚`a:Ù±‚`a:Ù±‚bmia2Ù±‚`a]Ù±‚`a Ù±‚aoa+Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`bpiÙ±‚aoa/Ù±‚`hn_anglesÙ±‚`a
Ù±‚`a
Ù±‚bc1x,# Map radius, angle pairs to x, y, z points.Ù±‚`a
Ù±‚`axÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`a(Ù±‚`eradiiÙ±‚aoa*Ù±‚`bnpÙ±‚aoa.Ù±‚`ccosÙ±‚`a(Ù±‚`fanglesÙ±‚`a)Ù±‚`a)Ù±‚aoa.Ù±‚`gflattenÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`ayÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`a(Ù±‚`eradiiÙ±‚aoa*Ù±‚`bnpÙ±‚aoa.Ù±‚`csinÙ±‚`a(Ù±‚`fanglesÙ±‚`a)Ù±‚`a)Ù±‚aoa.Ù±‚`gflattenÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`azÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`a(Ù±‚`bnpÙ±‚aoa.Ù±‚`ccosÙ±‚`a(Ù±‚`eradiiÙ±‚`a)Ù±‚aoa*Ù±‚`bnpÙ±‚aoa.Ù±‚`ccosÙ±‚`a(Ù±‚bmia3Ù±‚aoa*Ù±‚`fanglesÙ±‚`a)Ù±‚`a)Ù±‚aoa.Ù±‚`gflattenÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚bc1xK# Create the Triangulation; no triangles so Delaunay triangulation created.Ù±‚`a
Ù±‚`ftriangÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`dmtriÙ±‚aoa.Ù±‚`mTriangulationÙ±‚`a(Ù±‚`axÙ±‚`a,Ù±‚`a Ù±‚`ayÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚bc1x# Mask off unwanted triangles.Ù±‚`a
Ù±‚`dxmidÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`axÙ±‚`a[Ù±‚`ftriangÙ±‚aoa.Ù±‚`itrianglesÙ±‚`a]Ù±‚aoa.Ù±‚`dmeanÙ±‚`a(Ù±‚`daxisÙ±‚aoa=Ù±‚bmia1Ù±‚`a)Ù±‚`a
Ù±‚`dymidÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`ayÙ±‚`a[Ù±‚`ftriangÙ±‚aoa.Ù±‚`itrianglesÙ±‚`a]Ù±‚aoa.Ù±‚`dmeanÙ±‚`a(Ù±‚`daxisÙ±‚aoa=Ù±‚bmia1Ù±‚`a)Ù±‚`a
Ù±‚`dmaskÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`dxmidÙ±‚aoa*Ù±‚aoa*Ù±‚bmia2Ù±‚`a Ù±‚aoa+Ù±‚`a Ù±‚`dymidÙ±‚aoa*Ù±‚aoa*Ù±‚bmia2Ù±‚`a Ù±‚aoa<Ù±‚`a Ù±‚`jmin_radiusÙ±‚aoa*Ù±‚aoa*Ù±‚bmia2Ù±‚`a
Ù±‚`ftriangÙ±‚aoa.Ù±‚`hset_maskÙ±‚`a(Ù±‚`dmaskÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚bc1s# Plot the surface.Ù±‚`a
Ù±‚`baxÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cfigÙ±‚aoa.Ù±‚`kadd_subplotÙ±‚`a(Ù±‚bmia1Ù±‚`a,Ù±‚`a Ù±‚bmia2Ù±‚`a,Ù±‚`a Ù±‚bmia2Ù±‚`a,Ù±‚`a Ù±‚`jprojectionÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1b3dÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`lplot_trisurfÙ±‚`a(Ù±‚`ftriangÙ±‚`a,Ù±‚`a Ù±‚`azÙ±‚`a,Ù±‚`a Ù±‚`dcmapÙ±‚aoa=Ù±‚`cpltÙ±‚aoa.Ù±‚`bcmÙ±‚aoa.Ù±‚`fCMRmapÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚`cpltÙ±‚aoa.Ù±‚`dshowÙ±‚`a(Ù±‚`a)Ù±‚`a
`dNoneö