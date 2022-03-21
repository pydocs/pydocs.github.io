Ù¯‚Ù´ƒ™SÙ±‚bsdxs"""
====================
3D plots as subplots
====================

Demonstrate including 3D plots as subplots.
"""Ù±‚`a
Ù±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnnfpyplotÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnncpltÙ±‚`a
Ù±‚bkndfromÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚`a Ù±‚bknfimportÙ±‚`a Ù±‚`bcmÙ±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„enumpyÙ „enumpyf1.22.3fmoduleenumpyfmoduleõÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnnbnpÙ±‚`a
Ù±‚`a
Ù±‚bkndfromÙ±‚`a Ù±‚bnnlmpl_toolkitsÙ±‚bnna.Ù±‚bnngmplot3dÙ±‚bnna.Ù±‚bnnfaxes3dÙ±‚`a Ù±‚bknfimportÙ±‚`a Ù±‚`mget_test_dataÙ±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚bc1x-# set up a figure twice as wide as it is tallÙ±‚`a
Ù±‚`cfigÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cpltÙ±‚aoa.Ù±‚`ffigureÙ±‚`a(Ù±‚`gfigsizeÙ±‚aoa=Ù±‚`cpltÙ±‚aoa.Ù±‚`ifigaspectÙ±‚`a(Ù±‚bmfc0.5Ù±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚bc1o# =============Ù±‚`a
Ù±‚bc1o# First subplotÙ±‚`a
Ù±‚bc1o# =============Ù±‚`a
Ù±‚bc1x$# set up the axes for the first plotÙ±‚`a
Ù±‚`baxÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cfigÙ±‚aoa.Ù±‚`kadd_subplotÙ±‚`a(Ù±‚bmia1Ù±‚`a,Ù±‚`a Ù±‚bmia2Ù±‚`a,Ù±‚`a Ù±‚bmia1Ù±‚`a,Ù±‚`a Ù±‚`jprojectionÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1b3dÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚bc1x># plot a 3D surface like in the example mplot3d/surface3d_demoÙ±‚`a
Ù±‚`aXÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`farangeÙ±‚`a(Ù±‚aoa-Ù±‚bmia5Ù±‚`a,Ù±‚`a Ù±‚bmia5Ù±‚`a,Ù±‚`a Ù±‚bmfd0.25Ù±‚`a)Ù±‚`a
Ù±‚`aYÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`farangeÙ±‚`a(Ù±‚aoa-Ù±‚bmia5Ù±‚`a,Ù±‚`a Ù±‚bmia5Ù±‚`a,Ù±‚`a Ù±‚bmfd0.25Ù±‚`a)Ù±‚`a
Ù±‚`aXÙ±‚`a,Ù±‚`a Ù±‚`aYÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`hmeshgridÙ±‚`a(Ù±‚`aXÙ±‚`a,Ù±‚`a Ù±‚`aYÙ±‚`a)Ù±‚`a
Ù±‚`aRÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`dsqrtÙ±‚`a(Ù±‚`aXÙ±‚aoa*Ù±‚aoa*Ù±‚bmia2Ù±‚`a Ù±‚aoa+Ù±‚`a Ù±‚`aYÙ±‚aoa*Ù±‚aoa*Ù±‚bmia2Ù±‚`a)Ù±‚`a
Ù±‚`aZÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`csinÙ±‚`a(Ù±‚`aRÙ±‚`a)Ù±‚`a
Ù±‚`dsurfÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`baxÙ±‚aoa.Ù±‚`lplot_surfaceÙ±‚`a(Ù±‚`aXÙ±‚`a,Ù±‚`a Ù±‚`aYÙ±‚`a,Ù±‚`a Ù±‚`aZÙ±‚`a,Ù±‚`a Ù±‚`grstrideÙ±‚aoa=Ù±‚bmia1Ù±‚`a,Ù±‚`a Ù±‚`gcstrideÙ±‚aoa=Ù±‚bmia1Ù±‚`a,Ù±‚`a Ù±‚`dcmapÙ±‚aoa=Ù±‚`bcmÙ±‚aoa.Ù±‚`hcoolwarmÙ±‚`a,Ù±‚`a
Ù±‚`w                       Ù±‚`ilinewidthÙ±‚aoa=Ù±‚bmia0Ù±‚`a,Ù±‚`a Ù±‚`kantialiasedÙ±‚aoa=Ù±‚bkceFalseÙ±‚`a)Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`hset_zlimÙ±‚`a(Ù±‚aoa-Ù±‚bmfd1.01Ù±‚`a,Ù±‚`a Ù±‚bmfd1.01Ù±‚`a)Ù±‚`a
Ù±‚`cfigÙ±‚aoa.Ù±‚`hcolorbarÙ±‚`a(Ù±‚`dsurfÙ±‚`a,Ù±‚`a Ù±‚`fshrinkÙ±‚aoa=Ù±‚bmfc0.5Ù±‚`a,Ù±‚`a Ù±‚`faspectÙ±‚aoa=Ù±‚bmib10Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚bc1p# ==============Ù±‚`a
Ù±‚bc1p# Second subplotÙ±‚`a
Ù±‚bc1p# ==============Ù±‚`a
Ù±‚bc1x%# set up the axes for the second plotÙ±‚`a
Ù±‚`baxÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cfigÙ±‚aoa.Ù±‚`kadd_subplotÙ±‚`a(Ù±‚bmia1Ù±‚`a,Ù±‚`a Ù±‚bmia2Ù±‚`a,Ù±‚`a Ù±‚bmia2Ù±‚`a,Ù±‚`a Ù±‚`jprojectionÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1b3dÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚bc1x=# plot a 3D wireframe like in the example mplot3d/wire3d_demoÙ±‚`a
Ù±‚`aXÙ±‚`a,Ù±‚`a Ù±‚`aYÙ±‚`a,Ù±‚`a Ù±‚`aZÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`mget_test_dataÙ±‚`a(Ù±‚bmfd0.05Ù±‚`a)Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`nplot_wireframeÙ±‚`a(Ù±‚`aXÙ±‚`a,Ù±‚`a Ù±‚`aYÙ±‚`a,Ù±‚`a Ù±‚`aZÙ±‚`a,Ù±‚`a Ù±‚`grstrideÙ±‚aoa=Ù±‚bmib10Ù±‚`a,Ù±‚`a Ù±‚`gcstrideÙ±‚aoa=Ù±‚bmib10Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`cpltÙ±‚aoa.Ù±‚`dshowÙ±‚`a(Ù±‚`a)Ù±‚`a
`dNoneö