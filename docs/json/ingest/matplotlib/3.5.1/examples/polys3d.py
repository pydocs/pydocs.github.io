Ù¯‚Ù´ƒ™FÙ±‚bsdy?"""
=============================================
Generate polygons to fill under 3D line graph
=============================================

Demonstrate how to create polygons which fill the space under a line
graph. In this example polygons are semi-transparent, creating a sort
of 'jagged stained glass' effect.
"""Ù±‚`a
Ù±‚`a
Ù±‚bkndfromÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnnkcollectionsÙ±‚`a Ù±‚bknfimportÙ±‚`a Ù±‚`nPolyCollectionÙ±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnnfpyplotÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnncpltÙ±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„enumpyÙ „enumpyf1.22.3fmoduleenumpyfmoduleõÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnnbnpÙ±‚`a
Ù±‚bkndfromÙ±‚`a Ù±‚bnnÙ¢„escipyÙ „escipye1.8.0fmoduleescipyfmoduleõÙ±‚bnna.Ù±‚bnnestatsÙ±‚`a Ù±‚bknfimportÙ±‚`a Ù±‚`gpoissonÙ±‚`a
Ù±‚`a
Ù±‚bc1x)# Fixing random state for reproducibilityÙ±‚`a
Ù±‚`bnpÙ±‚aoa.Ù±‚`frandomÙ±‚aoa.Ù±‚`dseedÙ±‚`a(Ù±‚bmih19680801Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚akcdefÙ±‚`a Ù±‚bnfspolygon_under_graphÙ±‚`a(Ù±‚`axÙ±‚`a,Ù±‚`a Ù±‚`ayÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`d    Ù±‚bsdxœ"""
    Construct the vertex list which defines the polygon filling the space under
    the (x, y) line graph. This assumes x is in ascending order.
    """Ù±‚`a
Ù±‚`d    Ù±‚akfreturnÙ±‚`a Ù±‚`a[Ù±‚`a(Ù±‚`axÙ±‚`a[Ù±‚bmia0Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚bmfb0.Ù±‚`a)Ù±‚`a,Ù±‚`a Ù±‚aoa*Ù±‚bnbczipÙ±‚`a(Ù±‚`axÙ±‚`a,Ù±‚`a Ù±‚`ayÙ±‚`a)Ù±‚`a,Ù±‚`a Ù±‚`a(Ù±‚`axÙ±‚`a[Ù±‚aoa-Ù±‚bmia1Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚bmfb0.Ù±‚`a)Ù±‚`a]Ù±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚`baxÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cpltÙ±‚aoa.Ù±‚`ffigureÙ±‚`a(Ù±‚`a)Ù±‚aoa.Ù±‚`kadd_subplotÙ±‚`a(Ù±‚`jprojectionÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1b3dÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`axÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`hlinspaceÙ±‚`a(Ù±‚bmfb0.Ù±‚`a,Ù±‚`a Ù±‚bmfc10.Ù±‚`a,Ù±‚`a Ù±‚bmib31Ù±‚`a)Ù±‚`a
Ù±‚`glambdasÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bnberangeÙ±‚`a(Ù±‚bmia1Ù±‚`a,Ù±‚`a Ù±‚bmia9Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚bc1x8# verts[i] is a list of (x, y) pairs defining polygon i.Ù±‚`a
Ù±‚`evertsÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`a[Ù±‚`spolygon_under_graphÙ±‚`a(Ù±‚`axÙ±‚`a,Ù±‚`a Ù±‚`gpoissonÙ±‚aoa.Ù±‚`cpmfÙ±‚`a(Ù±‚`alÙ±‚`a,Ù±‚`a Ù±‚`axÙ±‚`a)Ù±‚`a)Ù±‚`a Ù±‚akcforÙ±‚`a Ù±‚`alÙ±‚`a Ù±‚bowbinÙ±‚`a Ù±‚`glambdasÙ±‚`a]Ù±‚`a
Ù±‚`jfacecolorsÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cpltÙ±‚aoa.Ù±‚`icolormapsÙ±‚`a[Ù±‚bs1a'Ù±‚bs1iviridis_rÙ±‚bs1a'Ù±‚`a]Ù±‚`a(Ù±‚`bnpÙ±‚aoa.Ù±‚`hlinspaceÙ±‚`a(Ù±‚bmia0Ù±‚`a,Ù±‚`a Ù±‚bmia1Ù±‚`a,Ù±‚`a Ù±‚bnbclenÙ±‚`a(Ù±‚`evertsÙ±‚`a)Ù±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`dpolyÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`nPolyCollectionÙ±‚`a(Ù±‚`evertsÙ±‚`a,Ù±‚`a Ù±‚`jfacecolorsÙ±‚aoa=Ù±‚`jfacecolorsÙ±‚`a,Ù±‚`a Ù±‚`ealphaÙ±‚aoa=Ù±‚bmfb.7Ù±‚`a)Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`padd_collection3dÙ±‚`a(Ù±‚`dpolyÙ±‚`a,Ù±‚`a Ù±‚`bzsÙ±‚aoa=Ù±‚`glambdasÙ±‚`a,Ù±‚`a Ù±‚`dzdirÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1ayÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`csetÙ±‚`a(Ù±‚`dxlimÙ±‚aoa=Ù±‚`a(Ù±‚bmia0Ù±‚`a,Ù±‚`a Ù±‚bmib10Ù±‚`a)Ù±‚`a,Ù±‚`a Ù±‚`dylimÙ±‚aoa=Ù±‚`a(Ù±‚bmia1Ù±‚`a,Ù±‚`a Ù±‚bmia9Ù±‚`a)Ù±‚`a,Ù±‚`a Ù±‚`dzlimÙ±‚aoa=Ù±‚`a(Ù±‚bmia0Ù±‚`a,Ù±‚`a Ù±‚bmfd0.35Ù±‚`a)Ù±‚`a,Ù±‚`a
Ù±‚`g       Ù±‚`fxlabelÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1axÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`fylabelÙ±‚aoa=Ù±‚bsaarÙ±‚bs1a'Ù±‚bs1a$Ù±‚bs1a\Ù±‚bs1glambda$Ù±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`fzlabelÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1kprobabilityÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`cpltÙ±‚aoa.Ù±‚`dshowÙ±‚`a(Ù±‚`a)Ù±‚`a
`dNoneö