Ù¯‚Ù´ƒ™°Ù±‚bsdxÎ"""
===========
Path Editor
===========

Sharing events across GUIs.

This example demonstrates a cross-GUI application using Matplotlib event
handling to interact with and modify objects on the canvas.
"""Ù±‚`a
Ù±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„enumpyÙ „enumpyf1.22.3fmoduleenumpyfmoduleõÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnnbnpÙ±‚`a
Ù±‚bkndfromÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnnmbackend_basesÙ±‚`a Ù±‚bknfimportÙ±‚`a Ù±‚`kMouseButtonÙ±‚`a
Ù±‚bkndfromÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnndpathÙ±‚`a Ù±‚bknfimportÙ±‚`a Ù±‚`dPathÙ±‚`a
Ù±‚bkndfromÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnngpatchesÙ±‚`a Ù±‚bknfimportÙ±‚`a Ù±‚`iPathPatchÙ±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnnfpyplotÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnncpltÙ±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚`cfigÙ±‚`a,Ù±‚`a Ù±‚`baxÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cpltÙ±‚aoa.Ù±‚`hsubplotsÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`hpathdataÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`a[Ù±‚`a
Ù±‚`d    Ù±‚`a(Ù±‚`dPathÙ±‚aoa.Ù±‚`fMOVETOÙ±‚`a,Ù±‚`a Ù±‚`a(Ù±‚bmfd1.58Ù±‚`a,Ù±‚`a Ù±‚aoa-Ù±‚bmfd2.57Ù±‚`a)Ù±‚`a)Ù±‚`a,Ù±‚`a
Ù±‚`d    Ù±‚`a(Ù±‚`dPathÙ±‚aoa.Ù±‚`fCURVE4Ù±‚`a,Ù±‚`a Ù±‚`a(Ù±‚bmfd0.35Ù±‚`a,Ù±‚`a Ù±‚aoa-Ù±‚bmfc1.1Ù±‚`a)Ù±‚`a)Ù±‚`a,Ù±‚`a
Ù±‚`d    Ù±‚`a(Ù±‚`dPathÙ±‚aoa.Ù±‚`fCURVE4Ù±‚`a,Ù±‚`a Ù±‚`a(Ù±‚aoa-Ù±‚bmfd1.75Ù±‚`a,Ù±‚`a Ù±‚bmfc2.0Ù±‚`a)Ù±‚`a)Ù±‚`a,Ù±‚`a
Ù±‚`d    Ù±‚`a(Ù±‚`dPathÙ±‚aoa.Ù±‚`fCURVE4Ù±‚`a,Ù±‚`a Ù±‚`a(Ù±‚bmfe0.375Ù±‚`a,Ù±‚`a Ù±‚bmfc2.0Ù±‚`a)Ù±‚`a)Ù±‚`a,Ù±‚`a
Ù±‚`d    Ù±‚`a(Ù±‚`dPathÙ±‚aoa.Ù±‚`fLINETOÙ±‚`a,Ù±‚`a Ù±‚`a(Ù±‚bmfd0.85Ù±‚`a,Ù±‚`a Ù±‚bmfd1.15Ù±‚`a)Ù±‚`a)Ù±‚`a,Ù±‚`a
Ù±‚`d    Ù±‚`a(Ù±‚`dPathÙ±‚aoa.Ù±‚`fCURVE4Ù±‚`a,Ù±‚`a Ù±‚`a(Ù±‚bmfc2.2Ù±‚`a,Ù±‚`a Ù±‚bmfc3.2Ù±‚`a)Ù±‚`a)Ù±‚`a,Ù±‚`a
Ù±‚`d    Ù±‚`a(Ù±‚`dPathÙ±‚aoa.Ù±‚`fCURVE4Ù±‚`a,Ù±‚`a Ù±‚`a(Ù±‚bmia3Ù±‚`a,Ù±‚`a Ù±‚bmfd0.05Ù±‚`a)Ù±‚`a)Ù±‚`a,Ù±‚`a
Ù±‚`d    Ù±‚`a(Ù±‚`dPathÙ±‚aoa.Ù±‚`fCURVE4Ù±‚`a,Ù±‚`a Ù±‚`a(Ù±‚bmfc2.0Ù±‚`a,Ù±‚`a Ù±‚aoa-Ù±‚bmfc0.5Ù±‚`a)Ù±‚`a)Ù±‚`a,Ù±‚`a
Ù±‚`d    Ù±‚`a(Ù±‚`dPathÙ±‚aoa.Ù±‚`iCLOSEPOLYÙ±‚`a,Ù±‚`a Ù±‚`a(Ù±‚bmfd1.58Ù±‚`a,Ù±‚`a Ù±‚aoa-Ù±‚bmfd2.57Ù±‚`a)Ù±‚`a)Ù±‚`a,Ù±‚`a
Ù±‚`a]Ù±‚`a
Ù±‚`a
Ù±‚`ecodesÙ±‚`a,Ù±‚`a Ù±‚`evertsÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bnbczipÙ±‚`a(Ù±‚aoa*Ù±‚`hpathdataÙ±‚`a)Ù±‚`a
Ù±‚`dpathÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`dPathÙ±‚`a(Ù±‚`evertsÙ±‚`a,Ù±‚`a Ù±‚`ecodesÙ±‚`a)Ù±‚`a
Ù±‚`epatchÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`iPathPatchÙ±‚`a(Ù±‚`a
Ù±‚`d    Ù±‚`dpathÙ±‚`a,Ù±‚`a Ù±‚`ifacecolorÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1egreenÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`iedgecolorÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1fyellowÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`ealphaÙ±‚aoa=Ù±‚bmfc0.5Ù±‚`a)Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`iadd_patchÙ±‚`a(Ù±‚`epatchÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚akeclassÙ±‚`a Ù±‚bncnPathInteractorÙ±‚`a:Ù±‚`a
Ù±‚`d    Ù±‚bsdx˜"""
    An path editor.

    Press 't' to toggle vertex markers on and off.  When vertex markers are on,
    they can be dragged with the mouse.
    """Ù±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚`ishowvertsÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bkcdTrueÙ±‚`a
Ù±‚`d    Ù±‚`gepsilonÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bmia5Ù±‚`b  Ù±‚bc1x-# max pixel distance to count as a vertex hitÙ±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚akcdefÙ±‚`a Ù±‚bfmh__init__Ù±‚`a(Ù±‚bbpdselfÙ±‚`a,Ù±‚`a Ù±‚`ipathpatchÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`baxÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`ipathpatchÙ±‚aoa.Ù±‚`daxesÙ±‚`a
Ù±‚`h        Ù±‚`fcanvasÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bbpdselfÙ±‚aoa.Ù±‚`baxÙ±‚aoa.Ù±‚`ffigureÙ±‚aoa.Ù±‚`fcanvasÙ±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`ipathpatchÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`ipathpatchÙ±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`ipathpatchÙ±‚aoa.Ù±‚`lset_animatedÙ±‚`a(Ù±‚bkcdTrueÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`h        Ù±‚`axÙ±‚`a,Ù±‚`a Ù±‚`ayÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bnbczipÙ±‚`a(Ù±‚aoa*Ù±‚bbpdselfÙ±‚aoa.Ù±‚`ipathpatchÙ±‚aoa.Ù±‚`hget_pathÙ±‚`a(Ù±‚`a)Ù±‚aoa.Ù±‚`hverticesÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`dlineÙ±‚`a,Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`baxÙ±‚aoa.Ù±‚`dplotÙ±‚`a(Ù±‚`a
Ù±‚`l            Ù±‚`axÙ±‚`a,Ù±‚`a Ù±‚`ayÙ±‚`a,Ù±‚`a Ù±‚`fmarkerÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1aoÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`omarkerfacecolorÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1arÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`hanimatedÙ±‚aoa=Ù±‚bkcdTrueÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`d_indÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bkcdNoneÙ±‚`b  Ù±‚bc1s# the active vertexÙ±‚`a
Ù±‚`a
Ù±‚`h        Ù±‚`fcanvasÙ±‚aoa.Ù±‚`kmpl_connectÙ±‚`a(Ù±‚bs1a'Ù±‚bs1jdraw_eventÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚bbpdselfÙ±‚aoa.Ù±‚`gon_drawÙ±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚`fcanvasÙ±‚aoa.Ù±‚`kmpl_connectÙ±‚`a(Ù±‚bs1a'Ù±‚bs1rbutton_press_eventÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚bbpdselfÙ±‚aoa.Ù±‚`oon_button_pressÙ±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚`fcanvasÙ±‚aoa.Ù±‚`kmpl_connectÙ±‚`a(Ù±‚bs1a'Ù±‚bs1okey_press_eventÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚bbpdselfÙ±‚aoa.Ù±‚`lon_key_pressÙ±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚`fcanvasÙ±‚aoa.Ù±‚`kmpl_connectÙ±‚`a(Ù±‚bs1a'Ù±‚bs1tbutton_release_eventÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚bbpdselfÙ±‚aoa.Ù±‚`qon_button_releaseÙ±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚`fcanvasÙ±‚aoa.Ù±‚`kmpl_connectÙ±‚`a(Ù±‚bs1a'Ù±‚bs1smotion_notify_eventÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚bbpdselfÙ±‚aoa.Ù±‚`mon_mouse_moveÙ±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`fcanvasÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`fcanvasÙ±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚akcdefÙ±‚`a Ù±‚bnfsget_ind_under_pointÙ±‚`a(Ù±‚bbpdselfÙ±‚`a,Ù±‚`a Ù±‚`eeventÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`h        Ù±‚bsdx£"""
        Return the index of the point closest to the event position or *None*
        if no point is within ``self.epsilon`` to the event position.
        """Ù±‚`a
Ù±‚`h        Ù±‚bc1p# display coordsÙ±‚`a
Ù±‚`h        Ù±‚`bxyÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`gasarrayÙ±‚`a(Ù±‚bbpdselfÙ±‚aoa.Ù±‚`ipathpatchÙ±‚aoa.Ù±‚`hget_pathÙ±‚`a(Ù±‚`a)Ù±‚aoa.Ù±‚`hverticesÙ±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚`cxytÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bbpdselfÙ±‚aoa.Ù±‚`ipathpatchÙ±‚aoa.Ù±‚`mget_transformÙ±‚`a(Ù±‚`a)Ù±‚aoa.Ù±‚`itransformÙ±‚`a(Ù±‚`bxyÙ±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚`bxtÙ±‚`a,Ù±‚`a Ù±‚`bytÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cxytÙ±‚`a[Ù±‚`a:Ù±‚`a,Ù±‚`a Ù±‚bmia0Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`cxytÙ±‚`a[Ù±‚`a:Ù±‚`a,Ù±‚`a Ù±‚bmia1Ù±‚`a]Ù±‚`a
Ù±‚`h        Ù±‚`adÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`dsqrtÙ±‚`a(Ù±‚`a(Ù±‚`bxtÙ±‚`a Ù±‚aoa-Ù±‚`a Ù±‚`eeventÙ±‚aoa.Ù±‚`axÙ±‚`a)Ù±‚aoa*Ù±‚aoa*Ù±‚bmia2Ù±‚`a Ù±‚aoa+Ù±‚`a Ù±‚`a(Ù±‚`bytÙ±‚`a Ù±‚aoa-Ù±‚`a Ù±‚`eeventÙ±‚aoa.Ù±‚`ayÙ±‚`a)Ù±‚aoa*Ù±‚aoa*Ù±‚bmia2Ù±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚`cindÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`adÙ±‚aoa.Ù±‚`fargminÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`h        Ù±‚akbifÙ±‚`a Ù±‚`adÙ±‚`a[Ù±‚`cindÙ±‚`a]Ù±‚`a Ù±‚aoa>Ù±‚aoa=Ù±‚`a Ù±‚bbpdselfÙ±‚aoa.Ù±‚`gepsilonÙ±‚`a:Ù±‚`a
Ù±‚`l            Ù±‚`cindÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bkcdNoneÙ±‚`a
Ù±‚`a
Ù±‚`h        Ù±‚akfreturnÙ±‚`a Ù±‚`cindÙ±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚akcdefÙ±‚`a Ù±‚bnfgon_drawÙ±‚`a(Ù±‚bbpdselfÙ±‚`a,Ù±‚`a Ù±‚`eeventÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`h        Ù±‚bsdx"""Callback for draws."""Ù±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`jbackgroundÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bbpdselfÙ±‚aoa.Ù±‚`fcanvasÙ±‚aoa.Ù±‚`ncopy_from_bboxÙ±‚`a(Ù±‚bbpdselfÙ±‚aoa.Ù±‚`baxÙ±‚aoa.Ù±‚`dbboxÙ±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`baxÙ±‚aoa.Ù±‚`kdraw_artistÙ±‚`a(Ù±‚bbpdselfÙ±‚aoa.Ù±‚`ipathpatchÙ±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`baxÙ±‚aoa.Ù±‚`kdraw_artistÙ±‚`a(Ù±‚bbpdselfÙ±‚aoa.Ù±‚`dlineÙ±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`fcanvasÙ±‚aoa.Ù±‚`dblitÙ±‚`a(Ù±‚bbpdselfÙ±‚aoa.Ù±‚`baxÙ±‚aoa.Ù±‚`dbboxÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚akcdefÙ±‚`a Ù±‚bnfoon_button_pressÙ±‚`a(Ù±‚bbpdselfÙ±‚`a,Ù±‚`a Ù±‚`eeventÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`h        Ù±‚bsdx("""Callback for mouse button presses."""Ù±‚`a
Ù±‚`h        Ù±‚akbifÙ±‚`a Ù±‚`a(Ù±‚`eeventÙ±‚aoa.Ù±‚`finaxesÙ±‚`a Ù±‚bowbisÙ±‚`a Ù±‚bkcdNoneÙ±‚`a
Ù±‚`p                Ù±‚bowborÙ±‚`a Ù±‚`eeventÙ±‚aoa.Ù±‚`fbuttonÙ±‚`a Ù±‚aob!=Ù±‚`a Ù±‚`kMouseButtonÙ±‚aoa.Ù±‚`dLEFTÙ±‚`a
Ù±‚`p                Ù±‚bowborÙ±‚`a Ù±‚bowcnotÙ±‚`a Ù±‚bbpdselfÙ±‚aoa.Ù±‚`ishowvertsÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`l            Ù±‚akfreturnÙ±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`d_indÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bbpdselfÙ±‚aoa.Ù±‚`sget_ind_under_pointÙ±‚`a(Ù±‚`eeventÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚akcdefÙ±‚`a Ù±‚bnfqon_button_releaseÙ±‚`a(Ù±‚bbpdselfÙ±‚`a,Ù±‚`a Ù±‚`eeventÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`h        Ù±‚bsdx)"""Callback for mouse button releases."""Ù±‚`a
Ù±‚`h        Ù±‚akbifÙ±‚`a Ù±‚`a(Ù±‚`eeventÙ±‚aoa.Ù±‚`fbuttonÙ±‚`a Ù±‚aob!=Ù±‚`a Ù±‚`kMouseButtonÙ±‚aoa.Ù±‚`dLEFTÙ±‚`a
Ù±‚`p                Ù±‚bowborÙ±‚`a Ù±‚bowcnotÙ±‚`a Ù±‚bbpdselfÙ±‚aoa.Ù±‚`ishowvertsÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`l            Ù±‚akfreturnÙ±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`d_indÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bkcdNoneÙ±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚akcdefÙ±‚`a Ù±‚bnflon_key_pressÙ±‚`a(Ù±‚bbpdselfÙ±‚`a,Ù±‚`a Ù±‚`eeventÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`h        Ù±‚bsdx"""Callback for key presses."""Ù±‚`a
Ù±‚`h        Ù±‚akbifÙ±‚`a Ù±‚bowcnotÙ±‚`a Ù±‚`eeventÙ±‚aoa.Ù±‚`finaxesÙ±‚`a:Ù±‚`a
Ù±‚`l            Ù±‚akfreturnÙ±‚`a
Ù±‚`h        Ù±‚akbifÙ±‚`a Ù±‚`eeventÙ±‚aoa.Ù±‚`ckeyÙ±‚`a Ù±‚aob==Ù±‚`a Ù±‚bs1a'Ù±‚bs1atÙ±‚bs1a'Ù±‚`a:Ù±‚`a
Ù±‚`l            Ù±‚bbpdselfÙ±‚aoa.Ù±‚`ishowvertsÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bowcnotÙ±‚`a Ù±‚bbpdselfÙ±‚aoa.Ù±‚`ishowvertsÙ±‚`a
Ù±‚`l            Ù±‚bbpdselfÙ±‚aoa.Ù±‚`dlineÙ±‚aoa.Ù±‚`kset_visibleÙ±‚`a(Ù±‚bbpdselfÙ±‚aoa.Ù±‚`ishowvertsÙ±‚`a)Ù±‚`a
Ù±‚`l            Ù±‚akbifÙ±‚`a Ù±‚bowcnotÙ±‚`a Ù±‚bbpdselfÙ±‚aoa.Ù±‚`ishowvertsÙ±‚`a:Ù±‚`a
Ù±‚`p                Ù±‚bbpdselfÙ±‚aoa.Ù±‚`d_indÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bkcdNoneÙ±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`fcanvasÙ±‚aoa.Ù±‚`ddrawÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚akcdefÙ±‚`a Ù±‚bnfmon_mouse_moveÙ±‚`a(Ù±‚bbpdselfÙ±‚`a,Ù±‚`a Ù±‚`eeventÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`h        Ù±‚bsdx#"""Callback for mouse movements."""Ù±‚`a
Ù±‚`h        Ù±‚akbifÙ±‚`a Ù±‚`a(Ù±‚bbpdselfÙ±‚aoa.Ù±‚`d_indÙ±‚`a Ù±‚bowbisÙ±‚`a Ù±‚bkcdNoneÙ±‚`a
Ù±‚`p                Ù±‚bowborÙ±‚`a Ù±‚`eeventÙ±‚aoa.Ù±‚`finaxesÙ±‚`a Ù±‚bowbisÙ±‚`a Ù±‚bkcdNoneÙ±‚`a
Ù±‚`p                Ù±‚bowborÙ±‚`a Ù±‚`eeventÙ±‚aoa.Ù±‚`fbuttonÙ±‚`a Ù±‚aob!=Ù±‚`a Ù±‚`kMouseButtonÙ±‚aoa.Ù±‚`dLEFTÙ±‚`a
Ù±‚`p                Ù±‚bowborÙ±‚`a Ù±‚bowcnotÙ±‚`a Ù±‚bbpdselfÙ±‚aoa.Ù±‚`ishowvertsÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`l            Ù±‚akfreturnÙ±‚`a
Ù±‚`a
Ù±‚`h        Ù±‚`hverticesÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bbpdselfÙ±‚aoa.Ù±‚`ipathpatchÙ±‚aoa.Ù±‚`hget_pathÙ±‚`a(Ù±‚`a)Ù±‚aoa.Ù±‚`hverticesÙ±‚`a
Ù±‚`a
Ù±‚`h        Ù±‚`hverticesÙ±‚`a[Ù±‚bbpdselfÙ±‚aoa.Ù±‚`d_indÙ±‚`a]Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`eeventÙ±‚aoa.Ù±‚`exdataÙ±‚`a,Ù±‚`a Ù±‚`eeventÙ±‚aoa.Ù±‚`eydataÙ±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`dlineÙ±‚aoa.Ù±‚`hset_dataÙ±‚`a(Ù±‚bnbczipÙ±‚`a(Ù±‚aoa*Ù±‚`hverticesÙ±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`fcanvasÙ±‚aoa.Ù±‚`nrestore_regionÙ±‚`a(Ù±‚bbpdselfÙ±‚aoa.Ù±‚`jbackgroundÙ±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`baxÙ±‚aoa.Ù±‚`kdraw_artistÙ±‚`a(Ù±‚bbpdselfÙ±‚aoa.Ù±‚`ipathpatchÙ±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`baxÙ±‚aoa.Ù±‚`kdraw_artistÙ±‚`a(Ù±‚bbpdselfÙ±‚aoa.Ù±‚`dlineÙ±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`fcanvasÙ±‚aoa.Ù±‚`dblitÙ±‚`a(Ù±‚bbpdselfÙ±‚aoa.Ù±‚`baxÙ±‚aoa.Ù±‚`dbboxÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚`jinteractorÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`nPathInteractorÙ±‚`a(Ù±‚`epatchÙ±‚`a)Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`iset_titleÙ±‚`a(Ù±‚bs1a'Ù±‚bs1xdrag vertices to update pathÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`hset_xlimÙ±‚`a(Ù±‚aoa-Ù±‚bmia3Ù±‚`a,Ù±‚`a Ù±‚bmia4Ù±‚`a)Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`hset_ylimÙ±‚`a(Ù±‚aoa-Ù±‚bmia3Ù±‚`a,Ù±‚`a Ù±‚bmia4Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`cpltÙ±‚aoa.Ù±‚`dshowÙ±‚`a(Ù±‚`a)Ù±‚`a
`dNoneö