Ù¯‚Ù´ƒ™ÎÙ±‚bsdxŒ"""
================
Trigradient Demo
================

Demonstrates computation of gradient with
`matplotlib.tri.CubicTriInterpolator`.
"""Ù±‚`a
Ù±‚bkndfromÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnnctriÙ±‚`a Ù±‚bknfimportÙ±‚`a Ù±‚`a(Ù±‚`a
Ù±‚`d    Ù±‚`mTriangulationÙ±‚`a,Ù±‚`a Ù±‚`qUniformTriRefinerÙ±‚`a,Ù±‚`a Ù±‚`tCubicTriInterpolatorÙ±‚`a)Ù±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnnfpyplotÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnncpltÙ±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„enumpyÙ „enumpyf1.22.3fmoduleenumpyfmoduleõÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnnbnpÙ±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚bc1xN# ----------------------------------------------------------------------------Ù±‚`a
Ù±‚bc1x"# Electrical potential of a dipoleÙ±‚`a
Ù±‚bc1xN# ----------------------------------------------------------------------------Ù±‚`a
Ù±‚akcdefÙ±‚`a Ù±‚bnfpdipole_potentialÙ±‚`a(Ù±‚`axÙ±‚`a,Ù±‚`a Ù±‚`ayÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`d    Ù±‚bsdx<"""The electric dipole potential V, at position *x*, *y*."""Ù±‚`a
Ù±‚`d    Ù±‚`dr_sqÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`axÙ±‚aoa*Ù±‚aoa*Ù±‚bmia2Ù±‚`a Ù±‚aoa+Ù±‚`a Ù±‚`ayÙ±‚aoa*Ù±‚aoa*Ù±‚bmia2Ù±‚`a
Ù±‚`d    Ù±‚`ethetaÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`garctan2Ù±‚`a(Ù±‚`ayÙ±‚`a,Ù±‚`a Ù±‚`axÙ±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`azÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`ccosÙ±‚`a(Ù±‚`ethetaÙ±‚`a)Ù±‚aoa/Ù±‚`dr_sqÙ±‚`a
Ù±‚`d    Ù±‚akfreturnÙ±‚`a Ù±‚`a(Ù±‚`bnpÙ±‚aoa.Ù±‚`cmaxÙ±‚`a(Ù±‚`azÙ±‚`a)Ù±‚`a Ù±‚aoa-Ù±‚`a Ù±‚`azÙ±‚`a)Ù±‚`a Ù±‚aoa/Ù±‚`a Ù±‚`a(Ù±‚`bnpÙ±‚aoa.Ù±‚`cmaxÙ±‚`a(Ù±‚`azÙ±‚`a)Ù±‚`a Ù±‚aoa-Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`cminÙ±‚`a(Ù±‚`azÙ±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚bc1xN# ----------------------------------------------------------------------------Ù±‚`a
Ù±‚bc1x# Creating a TriangulationÙ±‚`a
Ù±‚bc1xN# ----------------------------------------------------------------------------Ù±‚`a
Ù±‚bc1x5# First create the x and y coordinates of the points.Ù±‚`a
Ù±‚`hn_anglesÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bmib30Ù±‚`a
Ù±‚`gn_radiiÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bmib10Ù±‚`a
Ù±‚`jmin_radiusÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bmfc0.2Ù±‚`a
Ù±‚`eradiiÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`hlinspaceÙ±‚`a(Ù±‚`jmin_radiusÙ±‚`a,Ù±‚`a Ù±‚bmfd0.95Ù±‚`a,Ù±‚`a Ù±‚`gn_radiiÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`fanglesÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`hlinspaceÙ±‚`a(Ù±‚bmia0Ù±‚`a,Ù±‚`a Ù±‚bmia2Ù±‚`a Ù±‚aoa*Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`bpiÙ±‚`a,Ù±‚`a Ù±‚`hn_anglesÙ±‚`a,Ù±‚`a Ù±‚`hendpointÙ±‚aoa=Ù±‚bkceFalseÙ±‚`a)Ù±‚`a
Ù±‚`fanglesÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`frepeatÙ±‚`a(Ù±‚`fanglesÙ±‚`a[Ù±‚aoa.Ù±‚aoa.Ù±‚aoa.Ù±‚`a,Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`gnewaxisÙ±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`gn_radiiÙ±‚`a,Ù±‚`a Ù±‚`daxisÙ±‚aoa=Ù±‚bmia1Ù±‚`a)Ù±‚`a
Ù±‚`fanglesÙ±‚`a[Ù±‚`a:Ù±‚`a,Ù±‚`a Ù±‚bmia1Ù±‚`a:Ù±‚`a:Ù±‚bmia2Ù±‚`a]Ù±‚`a Ù±‚aoa+Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`bpiÙ±‚`a Ù±‚aoa/Ù±‚`a Ù±‚`hn_anglesÙ±‚`a
Ù±‚`a
Ù±‚`axÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`a(Ù±‚`eradiiÙ±‚aoa*Ù±‚`bnpÙ±‚aoa.Ù±‚`ccosÙ±‚`a(Ù±‚`fanglesÙ±‚`a)Ù±‚`a)Ù±‚aoa.Ù±‚`gflattenÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`ayÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`a(Ù±‚`eradiiÙ±‚aoa*Ù±‚`bnpÙ±‚aoa.Ù±‚`csinÙ±‚`a(Ù±‚`fanglesÙ±‚`a)Ù±‚`a)Ù±‚aoa.Ù±‚`gflattenÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`aVÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`pdipole_potentialÙ±‚`a(Ù±‚`axÙ±‚`a,Ù±‚`a Ù±‚`ayÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚bc1xL# Create the Triangulation; no triangles specified so Delaunay triangulationÙ±‚`a
Ù±‚bc1j# created.Ù±‚`a
Ù±‚`ftriangÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`mTriangulationÙ±‚`a(Ù±‚`axÙ±‚`a,Ù±‚`a Ù±‚`ayÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚bc1x# Mask off unwanted triangles.Ù±‚`a
Ù±‚`ftriangÙ±‚aoa.Ù±‚`hset_maskÙ±‚`a(Ù±‚`bnpÙ±‚aoa.Ù±‚`ehypotÙ±‚`a(Ù±‚`axÙ±‚`a[Ù±‚`ftriangÙ±‚aoa.Ù±‚`itrianglesÙ±‚`a]Ù±‚aoa.Ù±‚`dmeanÙ±‚`a(Ù±‚`daxisÙ±‚aoa=Ù±‚bmia1Ù±‚`a)Ù±‚`a,Ù±‚`a
Ù±‚`x                         Ù±‚`ayÙ±‚`a[Ù±‚`ftriangÙ±‚aoa.Ù±‚`itrianglesÙ±‚`a]Ù±‚aoa.Ù±‚`dmeanÙ±‚`a(Ù±‚`daxisÙ±‚aoa=Ù±‚bmia1Ù±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`p                Ù±‚aoa<Ù±‚`a Ù±‚`jmin_radiusÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚bc1xN# ----------------------------------------------------------------------------Ù±‚`a
Ù±‚bc1x7# Refine data - interpolates the electrical potential VÙ±‚`a
Ù±‚bc1xN# ----------------------------------------------------------------------------Ù±‚`a
Ù±‚`grefinerÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`qUniformTriRefinerÙ±‚`a(Ù±‚`ftriangÙ±‚`a)Ù±‚`a
Ù±‚`htri_refiÙ±‚`a,Ù±‚`a Ù±‚`kz_test_refiÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`grefinerÙ±‚aoa.Ù±‚`lrefine_fieldÙ±‚`a(Ù±‚`aVÙ±‚`a,Ù±‚`a Ù±‚`fsubdivÙ±‚aoa=Ù±‚bmia3Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚bc1xN# ----------------------------------------------------------------------------Ù±‚`a
Ù±‚bc1xL# Computes the electrical field (Ex, Ey) as gradient of electrical potentialÙ±‚`a
Ù±‚bc1xN# ----------------------------------------------------------------------------Ù±‚`a
Ù±‚`ctciÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`tCubicTriInterpolatorÙ±‚`a(Ù±‚`ftriangÙ±‚`a,Ù±‚`a Ù±‚aoa-Ù±‚`aVÙ±‚`a)Ù±‚`a
Ù±‚bc1xG# Gradient requested here at the mesh nodes but could be anywhere else:Ù±‚`a
Ù±‚`a(Ù±‚`bExÙ±‚`a,Ù±‚`a Ù±‚`bEyÙ±‚`a)Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`ctciÙ±‚aoa.Ù±‚`hgradientÙ±‚`a(Ù±‚`ftriangÙ±‚aoa.Ù±‚`axÙ±‚`a,Ù±‚`a Ù±‚`ftriangÙ±‚aoa.Ù±‚`ayÙ±‚`a)Ù±‚`a
Ù±‚`fE_normÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`dsqrtÙ±‚`a(Ù±‚`bExÙ±‚aoa*Ù±‚aoa*Ù±‚bmia2Ù±‚`a Ù±‚aoa+Ù±‚`a Ù±‚`bEyÙ±‚aoa*Ù±‚aoa*Ù±‚bmia2Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚bc1xN# ----------------------------------------------------------------------------Ù±‚`a
Ù±‚bc1xI# Plot the triangulation, the potential iso-contours and the vector fieldÙ±‚`a
Ù±‚bc1xN# ----------------------------------------------------------------------------Ù±‚`a
Ù±‚`cfigÙ±‚`a,Ù±‚`a Ù±‚`baxÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cpltÙ±‚aoa.Ù±‚`hsubplotsÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`jset_aspectÙ±‚`a(Ù±‚bs1a'Ù±‚bs1eequalÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚bc1xE# Enforce the margins, and enlarge them to give room for the vectors.Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`puse_sticky_edgesÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bkceFalseÙ±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`gmarginsÙ±‚`a(Ù±‚bmfd0.07Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`gtriplotÙ±‚`a(Ù±‚`ftriangÙ±‚`a,Ù±‚`a Ù±‚`ecolorÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1c0.8Ù±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`flevelsÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`farangeÙ±‚`a(Ù±‚bmfb0.Ù±‚`a,Ù±‚`a Ù±‚bmfb1.Ù±‚`a,Ù±‚`a Ù±‚bmfd0.01Ù±‚`a)Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`jtricontourÙ±‚`a(Ù±‚`htri_refiÙ±‚`a,Ù±‚`a Ù±‚`kz_test_refiÙ±‚`a,Ù±‚`a Ù±‚`flevelsÙ±‚aoa=Ù±‚`flevelsÙ±‚`a,Ù±‚`a Ù±‚`dcmapÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1chotÙ±‚bs1a'Ù±‚`a,Ù±‚`a
Ù±‚`n              Ù±‚`jlinewidthsÙ±‚aoa=Ù±‚`a[Ù±‚bmfc2.0Ù±‚`a,Ù±‚`a Ù±‚bmfc1.0Ù±‚`a,Ù±‚`a Ù±‚bmfc1.0Ù±‚`a,Ù±‚`a Ù±‚bmfc1.0Ù±‚`a]Ù±‚`a)Ù±‚`a
Ù±‚bc1x0# Plots direction of the electrical vector fieldÙ±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`fquiverÙ±‚`a(Ù±‚`ftriangÙ±‚aoa.Ù±‚`axÙ±‚`a,Ù±‚`a Ù±‚`ftriangÙ±‚aoa.Ù±‚`ayÙ±‚`a,Ù±‚`a Ù±‚`bExÙ±‚aoa/Ù±‚`fE_normÙ±‚`a,Ù±‚`a Ù±‚`bEyÙ±‚aoa/Ù±‚`fE_normÙ±‚`a,Ù±‚`a
Ù±‚`j          Ù±‚`eunitsÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1bxyÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`escaleÙ±‚aoa=Ù±‚bmfc10.Ù±‚`a,Ù±‚`a Ù±‚`fzorderÙ±‚aoa=Ù±‚bmia3Ù±‚`a,Ù±‚`a Ù±‚`ecolorÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1dblueÙ±‚bs1a'Ù±‚`a,Ù±‚`a
Ù±‚`j          Ù±‚`ewidthÙ±‚aoa=Ù±‚bmfe0.007Ù±‚`a,Ù±‚`a Ù±‚`iheadwidthÙ±‚aoa=Ù±‚bmfb3.Ù±‚`a,Ù±‚`a Ù±‚`jheadlengthÙ±‚aoa=Ù±‚bmfb4.Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`iset_titleÙ±‚`a(Ù±‚bs1a'Ù±‚bs1x#Gradient plot: an electrical dipoleÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`cpltÙ±‚aoa.Ù±‚`dshowÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚bc1xM#############################################################################Ù±‚`a
Ù±‚bc1a#Ù±‚`a
Ù±‚bc1x# .. admonition:: ReferencesÙ±‚`a
Ù±‚bc1a#Ù±‚`a
Ù±‚bc1xN#    The use of the following functions, methods, classes and modules is shownÙ±‚`a
Ù±‚bc1u#    in this example:Ù±‚`a
Ù±‚bc1a#Ù±‚`a
Ù±‚bc1xI#    - `matplotlib.axes.Axes.tricontour` / `matplotlib.pyplot.tricontour`Ù±‚`a
Ù±‚bc1xC#    - `matplotlib.axes.Axes.triplot` / `matplotlib.pyplot.triplot`Ù±‚`a
Ù±‚bc1w#    - `matplotlib.tri`Ù±‚`a
Ù±‚bc1x%#    - `matplotlib.tri.Triangulation`Ù±‚`a
Ù±‚bc1x,#    - `matplotlib.tri.CubicTriInterpolator`Ù±‚`a
Ù±‚bc1x5#    - `matplotlib.tri.CubicTriInterpolator.gradient`Ù±‚`a
Ù±‚bc1x)#    - `matplotlib.tri.UniformTriRefiner`Ù±‚`a
Ù±‚bc1xA#    - `matplotlib.axes.Axes.quiver` / `matplotlib.pyplot.quiver`Ù±‚`a
`dNoneö