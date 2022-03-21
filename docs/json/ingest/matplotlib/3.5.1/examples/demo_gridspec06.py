Ù¯‚Ù´ƒ™‹Ù±‚bsaarÙ±‚bsdxv"""
================
Nested GridSpecs
================

This example demonstrates the use of nested `.GridSpec`\s.
"""Ù±‚`a
Ù±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnnfpyplotÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnncpltÙ±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„enumpyÙ „enumpyf1.22.3fmoduleenumpyfmoduleõÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnnbnpÙ±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚akcdefÙ±‚`a Ù±‚bnfksquiggle_xyÙ±‚`a(Ù±‚`aaÙ±‚`a,Ù±‚`a Ù±‚`abÙ±‚`a,Ù±‚`a Ù±‚`acÙ±‚`a,Ù±‚`a Ù±‚`adÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`d    Ù±‚`aiÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`farangeÙ±‚`a(Ù±‚bmfc0.0Ù±‚`a,Ù±‚`a Ù±‚bmia2Ù±‚aoa*Ù±‚`bnpÙ±‚aoa.Ù±‚`bpiÙ±‚`a,Ù±‚`a Ù±‚bmfd0.05Ù±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚akfreturnÙ±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`csinÙ±‚`a(Ù±‚`aiÙ±‚aoa*Ù±‚`aaÙ±‚`a)Ù±‚aoa*Ù±‚`bnpÙ±‚aoa.Ù±‚`ccosÙ±‚`a(Ù±‚`aiÙ±‚aoa*Ù±‚`abÙ±‚`a)Ù±‚`a,Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`csinÙ±‚`a(Ù±‚`aiÙ±‚aoa*Ù±‚`acÙ±‚`a)Ù±‚aoa*Ù±‚`bnpÙ±‚aoa.Ù±‚`ccosÙ±‚`a(Ù±‚`aiÙ±‚aoa*Ù±‚`adÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚`cfigÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cpltÙ±‚aoa.Ù±‚`ffigureÙ±‚`a(Ù±‚`gfigsizeÙ±‚aoa=Ù±‚`a(Ù±‚bmia8Ù±‚`a,Ù±‚`a Ù±‚bmia8Ù±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`jouter_gridÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cfigÙ±‚aoa.Ù±‚`ladd_gridspecÙ±‚`a(Ù±‚bmia4Ù±‚`a,Ù±‚`a Ù±‚bmia4Ù±‚`a,Ù±‚`a Ù±‚`fwspaceÙ±‚aoa=Ù±‚bmia0Ù±‚`a,Ù±‚`a Ù±‚`fhspaceÙ±‚aoa=Ù±‚bmia0Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚akcforÙ±‚`a Ù±‚`aaÙ±‚`a Ù±‚bowbinÙ±‚`a Ù±‚bnberangeÙ±‚`a(Ù±‚bmia4Ù±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`d    Ù±‚akcforÙ±‚`a Ù±‚`abÙ±‚`a Ù±‚bowbinÙ±‚`a Ù±‚bnberangeÙ±‚`a(Ù±‚bmia4Ù±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`h        Ù±‚bc1x# gridspec inside gridspecÙ±‚`a
Ù±‚`h        Ù±‚`jinner_gridÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`jouter_gridÙ±‚`a[Ù±‚`aaÙ±‚`a,Ù±‚`a Ù±‚`abÙ±‚`a]Ù±‚aoa.Ù±‚`ksubgridspecÙ±‚`a(Ù±‚bmia3Ù±‚`a,Ù±‚`a Ù±‚bmia3Ù±‚`a,Ù±‚`a Ù±‚`fwspaceÙ±‚aoa=Ù±‚bmia0Ù±‚`a,Ù±‚`a Ù±‚`fhspaceÙ±‚aoa=Ù±‚bmia0Ù±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚`caxsÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`jinner_gridÙ±‚aoa.Ù±‚`hsubplotsÙ±‚`a(Ù±‚`a)Ù±‚`b  Ù±‚bc1x)# Create all subplots for the inner grid.Ù±‚`a
Ù±‚`h        Ù±‚akcforÙ±‚`a Ù±‚`a(Ù±‚`acÙ±‚`a,Ù±‚`a Ù±‚`adÙ±‚`a)Ù±‚`a,Ù±‚`a Ù±‚`baxÙ±‚`a Ù±‚bowbinÙ±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`kndenumerateÙ±‚`a(Ù±‚`caxsÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`l            Ù±‚`baxÙ±‚aoa.Ù±‚`dplotÙ±‚`a(Ù±‚aoa*Ù±‚`ksquiggle_xyÙ±‚`a(Ù±‚`aaÙ±‚`a Ù±‚aoa+Ù±‚`a Ù±‚bmia1Ù±‚`a,Ù±‚`a Ù±‚`abÙ±‚`a Ù±‚aoa+Ù±‚`a Ù±‚bmia1Ù±‚`a,Ù±‚`a Ù±‚`acÙ±‚`a Ù±‚aoa+Ù±‚`a Ù±‚bmia1Ù±‚`a,Ù±‚`a Ù±‚`adÙ±‚`a Ù±‚aoa+Ù±‚`a Ù±‚bmia1Ù±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`l            Ù±‚`baxÙ±‚aoa.Ù±‚`csetÙ±‚`a(Ù±‚`fxticksÙ±‚aoa=Ù±‚`a[Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`fyticksÙ±‚aoa=Ù±‚`a[Ù±‚`a]Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚bc1x# show only the outside spinesÙ±‚`a
Ù±‚akcforÙ±‚`a Ù±‚`baxÙ±‚`a Ù±‚bowbinÙ±‚`a Ù±‚`cfigÙ±‚aoa.Ù±‚`hget_axesÙ±‚`a(Ù±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`d    Ù±‚`bssÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`baxÙ±‚aoa.Ù±‚`oget_subplotspecÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`baxÙ±‚aoa.Ù±‚`fspinesÙ±‚aoa.Ù±‚`ctopÙ±‚aoa.Ù±‚`kset_visibleÙ±‚`a(Ù±‚`bssÙ±‚aoa.Ù±‚`lis_first_rowÙ±‚`a(Ù±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`baxÙ±‚aoa.Ù±‚`fspinesÙ±‚aoa.Ù±‚`fbottomÙ±‚aoa.Ù±‚`kset_visibleÙ±‚`a(Ù±‚`bssÙ±‚aoa.Ù±‚`kis_last_rowÙ±‚`a(Ù±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`baxÙ±‚aoa.Ù±‚`fspinesÙ±‚aoa.Ù±‚`dleftÙ±‚aoa.Ù±‚`kset_visibleÙ±‚`a(Ù±‚`bssÙ±‚aoa.Ù±‚`lis_first_colÙ±‚`a(Ù±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`baxÙ±‚aoa.Ù±‚`fspinesÙ±‚aoa.Ù±‚`erightÙ±‚aoa.Ù±‚`kset_visibleÙ±‚`a(Ù±‚`bssÙ±‚aoa.Ù±‚`kis_last_colÙ±‚`a(Ù±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`cpltÙ±‚aoa.Ù±‚`dshowÙ±‚`a(Ù±‚`a)Ù±‚`a
`dNoneö