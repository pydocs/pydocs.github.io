Ù¯‚Ù´ƒ™ßÙ±‚bsdx³"""
===========
Poly Editor
===========

This is an example to show how to build cross-GUI applications using
Matplotlib event handling to interact with objects on the canvas.
"""Ù±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„enumpyÙ „enumpyf1.22.3fmoduleenumpyfmoduleõÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnnbnpÙ±‚`a
Ù±‚bkndfromÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnnelinesÙ±‚`a Ù±‚bknfimportÙ±‚`a Ù±‚`fLine2DÙ±‚`a
Ù±‚bkndfromÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnnfartistÙ±‚`a Ù±‚bknfimportÙ±‚`a Ù±‚`fArtistÙ±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚akcdefÙ±‚`a Ù±‚bnfddistÙ±‚`a(Ù±‚`axÙ±‚`a,Ù±‚`a Ù±‚`ayÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`d    Ù±‚bsdx7"""
    Return the distance between two points.
    """Ù±‚`a
Ù±‚`d    Ù±‚`adÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`axÙ±‚`a Ù±‚aoa-Ù±‚`a Ù±‚`ayÙ±‚`a
Ù±‚`d    Ù±‚akfreturnÙ±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`dsqrtÙ±‚`a(Ù±‚`bnpÙ±‚aoa.Ù±‚`cdotÙ±‚`a(Ù±‚`adÙ±‚`a,Ù±‚`a Ù±‚`adÙ±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚akcdefÙ±‚`a Ù±‚bnfudist_point_to_segmentÙ±‚`a(Ù±‚`apÙ±‚`a,Ù±‚`a Ù±‚`bs0Ù±‚`a,Ù±‚`a Ù±‚`bs1Ù±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`d    Ù±‚bsdx¬"""
    Get the distance of a point to a segment.
      *p*, *s0*, *s1* are *xy* sequences
    This algorithm from
    http://www.geomalgorithms.com/algorithms.html
    """Ù±‚`a
Ù±‚`d    Ù±‚`avÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bs1Ù±‚`a Ù±‚aoa-Ù±‚`a Ù±‚`bs0Ù±‚`a
Ù±‚`d    Ù±‚`awÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`apÙ±‚`a Ù±‚aoa-Ù±‚`a Ù±‚`bs0Ù±‚`a
Ù±‚`d    Ù±‚`bc1Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`cdotÙ±‚`a(Ù±‚`awÙ±‚`a,Ù±‚`a Ù±‚`avÙ±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚akbifÙ±‚`a Ù±‚`bc1Ù±‚`a Ù±‚aoa<Ù±‚aoa=Ù±‚`a Ù±‚bmia0Ù±‚`a:Ù±‚`a
Ù±‚`h        Ù±‚akfreturnÙ±‚`a Ù±‚`ddistÙ±‚`a(Ù±‚`apÙ±‚`a,Ù±‚`a Ù±‚`bs0Ù±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`bc2Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`cdotÙ±‚`a(Ù±‚`avÙ±‚`a,Ù±‚`a Ù±‚`avÙ±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚akbifÙ±‚`a Ù±‚`bc2Ù±‚`a Ù±‚aoa<Ù±‚aoa=Ù±‚`a Ù±‚`bc1Ù±‚`a:Ù±‚`a
Ù±‚`h        Ù±‚akfreturnÙ±‚`a Ù±‚`ddistÙ±‚`a(Ù±‚`apÙ±‚`a,Ù±‚`a Ù±‚`bs1Ù±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`abÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bc1Ù±‚`a Ù±‚aoa/Ù±‚`a Ù±‚`bc2Ù±‚`a
Ù±‚`d    Ù±‚`bpbÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bs0Ù±‚`a Ù±‚aoa+Ù±‚`a Ù±‚`abÙ±‚`a Ù±‚aoa*Ù±‚`a Ù±‚`avÙ±‚`a
Ù±‚`d    Ù±‚akfreturnÙ±‚`a Ù±‚`ddistÙ±‚`a(Ù±‚`apÙ±‚`a,Ù±‚`a Ù±‚`bpbÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚akeclassÙ±‚`a Ù±‚bncqPolygonInteractorÙ±‚`a:Ù±‚`a
Ù±‚`d    Ù±‚bsdyH"""
    A polygon editor.

    Key-bindings

      't' toggle vertex markers on and off.  When vertex markers are on,
          you can move them, delete them

      'd' delete the vertex under point

      'i' insert a vertex at point.  You must be within epsilon of the
          line connecting two existing vertices

    """Ù±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚`ishowvertsÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bkcdTrueÙ±‚`a
Ù±‚`d    Ù±‚`gepsilonÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bmia5Ù±‚`b  Ù±‚bc1x-# max pixel distance to count as a vertex hitÙ±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚akcdefÙ±‚`a Ù±‚bfmh__init__Ù±‚`a(Ù±‚bbpdselfÙ±‚`a,Ù±‚`a Ù±‚`baxÙ±‚`a,Ù±‚`a Ù±‚`dpolyÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`h        Ù±‚akbifÙ±‚`a Ù±‚`dpolyÙ±‚aoa.Ù±‚`ffigureÙ±‚`a Ù±‚bowbisÙ±‚`a Ù±‚bkcdNoneÙ±‚`a:Ù±‚`a
Ù±‚`l            Ù±‚akeraiseÙ±‚`a Ù±‚bnelRuntimeErrorÙ±‚`a(Ù±‚bs1a'Ù±‚bs1x+You must first add the polygon to a figure Ù±‚bs1a'Ù±‚`a
Ù±‚`x                               Ù±‚bs1a'Ù±‚bs1x(or canvas before defining the interactorÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`baxÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`baxÙ±‚`a
Ù±‚`h        Ù±‚`fcanvasÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`dpolyÙ±‚aoa.Ù±‚`ffigureÙ±‚aoa.Ù±‚`fcanvasÙ±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`dpolyÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`dpolyÙ±‚`a
Ù±‚`a
Ù±‚`h        Ù±‚`axÙ±‚`a,Ù±‚`a Ù±‚`ayÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bnbczipÙ±‚`a(Ù±‚aoa*Ù±‚bbpdselfÙ±‚aoa.Ù±‚`dpolyÙ±‚aoa.Ù±‚`bxyÙ±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`dlineÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`fLine2DÙ±‚`a(Ù±‚`axÙ±‚`a,Ù±‚`a Ù±‚`ayÙ±‚`a,Ù±‚`a
Ù±‚`x                           Ù±‚`fmarkerÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1aoÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`omarkerfacecolorÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1arÙ±‚bs1a'Ù±‚`a,Ù±‚`a
Ù±‚`x                           Ù±‚`hanimatedÙ±‚aoa=Ù±‚bkcdTrueÙ±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`baxÙ±‚aoa.Ù±‚`hadd_lineÙ±‚`a(Ù±‚bbpdselfÙ±‚aoa.Ù±‚`dlineÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`ccidÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bbpdselfÙ±‚aoa.Ù±‚`dpolyÙ±‚aoa.Ù±‚`ladd_callbackÙ±‚`a(Ù±‚bbpdselfÙ±‚aoa.Ù±‚`lpoly_changedÙ±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`d_indÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bkcdNoneÙ±‚`b  Ù±‚bc1q# the active vertÙ±‚`a
Ù±‚`a
Ù±‚`h        Ù±‚`fcanvasÙ±‚aoa.Ù±‚`kmpl_connectÙ±‚`a(Ù±‚bs1a'Ù±‚bs1jdraw_eventÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚bbpdselfÙ±‚aoa.Ù±‚`gon_drawÙ±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚`fcanvasÙ±‚aoa.Ù±‚`kmpl_connectÙ±‚`a(Ù±‚bs1a'Ù±‚bs1rbutton_press_eventÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚bbpdselfÙ±‚aoa.Ù±‚`oon_button_pressÙ±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚`fcanvasÙ±‚aoa.Ù±‚`kmpl_connectÙ±‚`a(Ù±‚bs1a'Ù±‚bs1okey_press_eventÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚bbpdselfÙ±‚aoa.Ù±‚`lon_key_pressÙ±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚`fcanvasÙ±‚aoa.Ù±‚`kmpl_connectÙ±‚`a(Ù±‚bs1a'Ù±‚bs1tbutton_release_eventÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚bbpdselfÙ±‚aoa.Ù±‚`qon_button_releaseÙ±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚`fcanvasÙ±‚aoa.Ù±‚`kmpl_connectÙ±‚`a(Ù±‚bs1a'Ù±‚bs1smotion_notify_eventÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚bbpdselfÙ±‚aoa.Ù±‚`mon_mouse_moveÙ±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`fcanvasÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`fcanvasÙ±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚akcdefÙ±‚`a Ù±‚bnfgon_drawÙ±‚`a(Ù±‚bbpdselfÙ±‚`a,Ù±‚`a Ù±‚`eeventÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`jbackgroundÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bbpdselfÙ±‚aoa.Ù±‚`fcanvasÙ±‚aoa.Ù±‚`ncopy_from_bboxÙ±‚`a(Ù±‚bbpdselfÙ±‚aoa.Ù±‚`baxÙ±‚aoa.Ù±‚`dbboxÙ±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`baxÙ±‚aoa.Ù±‚`kdraw_artistÙ±‚`a(Ù±‚bbpdselfÙ±‚aoa.Ù±‚`dpolyÙ±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`baxÙ±‚aoa.Ù±‚`kdraw_artistÙ±‚`a(Ù±‚bbpdselfÙ±‚aoa.Ù±‚`dlineÙ±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚bc1x?# do not need to blit here, this will fire before the screen isÙ±‚`a
Ù±‚`h        Ù±‚bc1i# updatedÙ±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚akcdefÙ±‚`a Ù±‚bnflpoly_changedÙ±‚`a(Ù±‚bbpdselfÙ±‚`a,Ù±‚`a Ù±‚`dpolyÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`h        Ù±‚bsdxD"""This method is called whenever the pathpatch object is called."""Ù±‚`a
Ù±‚`h        Ù±‚bc1x<# only copy the artist props to the line (except visibility)Ù±‚`a
Ù±‚`h        Ù±‚`cvisÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bbpdselfÙ±‚aoa.Ù±‚`dlineÙ±‚aoa.Ù±‚`kget_visibleÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚`fArtistÙ±‚aoa.Ù±‚`kupdate_fromÙ±‚`a(Ù±‚bbpdselfÙ±‚aoa.Ù±‚`dlineÙ±‚`a,Ù±‚`a Ù±‚`dpolyÙ±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`dlineÙ±‚aoa.Ù±‚`kset_visibleÙ±‚`a(Ù±‚`cvisÙ±‚`a)Ù±‚`b  Ù±‚bc1x%# don't use the poly visibility stateÙ±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚akcdefÙ±‚`a Ù±‚bnfsget_ind_under_pointÙ±‚`a(Ù±‚bbpdselfÙ±‚`a,Ù±‚`a Ù±‚`eeventÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`h        Ù±‚bsdx£"""
        Return the index of the point closest to the event position or *None*
        if no point is within ``self.epsilon`` to the event position.
        """Ù±‚`a
Ù±‚`h        Ù±‚bc1p# display coordsÙ±‚`a
Ù±‚`h        Ù±‚`bxyÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`gasarrayÙ±‚`a(Ù±‚bbpdselfÙ±‚aoa.Ù±‚`dpolyÙ±‚aoa.Ù±‚`bxyÙ±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚`cxytÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bbpdselfÙ±‚aoa.Ù±‚`dpolyÙ±‚aoa.Ù±‚`mget_transformÙ±‚`a(Ù±‚`a)Ù±‚aoa.Ù±‚`itransformÙ±‚`a(Ù±‚`bxyÙ±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚`bxtÙ±‚`a,Ù±‚`a Ù±‚`bytÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cxytÙ±‚`a[Ù±‚`a:Ù±‚`a,Ù±‚`a Ù±‚bmia0Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`cxytÙ±‚`a[Ù±‚`a:Ù±‚`a,Ù±‚`a Ù±‚bmia1Ù±‚`a]Ù±‚`a
Ù±‚`h        Ù±‚`adÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`ehypotÙ±‚`a(Ù±‚`bxtÙ±‚`a Ù±‚aoa-Ù±‚`a Ù±‚`eeventÙ±‚aoa.Ù±‚`axÙ±‚`a,Ù±‚`a Ù±‚`bytÙ±‚`a Ù±‚aoa-Ù±‚`a Ù±‚`eeventÙ±‚aoa.Ù±‚`ayÙ±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚`findseqÙ±‚`a,Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`gnonzeroÙ±‚`a(Ù±‚`adÙ±‚`a Ù±‚aob==Ù±‚`a Ù±‚`adÙ±‚aoa.Ù±‚`cminÙ±‚`a(Ù±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚`cindÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`findseqÙ±‚`a[Ù±‚bmia0Ù±‚`a]Ù±‚`a
Ù±‚`a
Ù±‚`h        Ù±‚akbifÙ±‚`a Ù±‚`adÙ±‚`a[Ù±‚`cindÙ±‚`a]Ù±‚`a Ù±‚aoa>Ù±‚aoa=Ù±‚`a Ù±‚bbpdselfÙ±‚aoa.Ù±‚`gepsilonÙ±‚`a:Ù±‚`a
Ù±‚`l            Ù±‚`cindÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bkcdNoneÙ±‚`a
Ù±‚`a
Ù±‚`h        Ù±‚akfreturnÙ±‚`a Ù±‚`cindÙ±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚akcdefÙ±‚`a Ù±‚bnfoon_button_pressÙ±‚`a(Ù±‚bbpdselfÙ±‚`a,Ù±‚`a Ù±‚`eeventÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`h        Ù±‚bsdx("""Callback for mouse button presses."""Ù±‚`a
Ù±‚`h        Ù±‚akbifÙ±‚`a Ù±‚bowcnotÙ±‚`a Ù±‚bbpdselfÙ±‚aoa.Ù±‚`ishowvertsÙ±‚`a:Ù±‚`a
Ù±‚`l            Ù±‚akfreturnÙ±‚`a
Ù±‚`h        Ù±‚akbifÙ±‚`a Ù±‚`eeventÙ±‚aoa.Ù±‚`finaxesÙ±‚`a Ù±‚bowbisÙ±‚`a Ù±‚bkcdNoneÙ±‚`a:Ù±‚`a
Ù±‚`l            Ù±‚akfreturnÙ±‚`a
Ù±‚`h        Ù±‚akbifÙ±‚`a Ù±‚`eeventÙ±‚aoa.Ù±‚`fbuttonÙ±‚`a Ù±‚aob!=Ù±‚`a Ù±‚bmia1Ù±‚`a:Ù±‚`a
Ù±‚`l            Ù±‚akfreturnÙ±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`d_indÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bbpdselfÙ±‚aoa.Ù±‚`sget_ind_under_pointÙ±‚`a(Ù±‚`eeventÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚akcdefÙ±‚`a Ù±‚bnfqon_button_releaseÙ±‚`a(Ù±‚bbpdselfÙ±‚`a,Ù±‚`a Ù±‚`eeventÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`h        Ù±‚bsdx)"""Callback for mouse button releases."""Ù±‚`a
Ù±‚`h        Ù±‚akbifÙ±‚`a Ù±‚bowcnotÙ±‚`a Ù±‚bbpdselfÙ±‚aoa.Ù±‚`ishowvertsÙ±‚`a:Ù±‚`a
Ù±‚`l            Ù±‚akfreturnÙ±‚`a
Ù±‚`h        Ù±‚akbifÙ±‚`a Ù±‚`eeventÙ±‚aoa.Ù±‚`fbuttonÙ±‚`a Ù±‚aob!=Ù±‚`a Ù±‚bmia1Ù±‚`a:Ù±‚`a
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
Ù±‚`h        Ù±‚akdelifÙ±‚`a Ù±‚`eeventÙ±‚aoa.Ù±‚`ckeyÙ±‚`a Ù±‚aob==Ù±‚`a Ù±‚bs1a'Ù±‚bs1adÙ±‚bs1a'Ù±‚`a:Ù±‚`a
Ù±‚`l            Ù±‚`cindÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bbpdselfÙ±‚aoa.Ù±‚`sget_ind_under_pointÙ±‚`a(Ù±‚`eeventÙ±‚`a)Ù±‚`a
Ù±‚`l            Ù±‚akbifÙ±‚`a Ù±‚`cindÙ±‚`a Ù±‚bowbisÙ±‚`a Ù±‚bowcnotÙ±‚`a Ù±‚bkcdNoneÙ±‚`a:Ù±‚`a
Ù±‚`p                Ù±‚bbpdselfÙ±‚aoa.Ù±‚`dpolyÙ±‚aoa.Ù±‚`bxyÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`fdeleteÙ±‚`a(Ù±‚bbpdselfÙ±‚aoa.Ù±‚`dpolyÙ±‚aoa.Ù±‚`bxyÙ±‚`a,Ù±‚`a
Ù±‚`x)                                         Ù±‚`cindÙ±‚`a,Ù±‚`a Ù±‚`daxisÙ±‚aoa=Ù±‚bmia0Ù±‚`a)Ù±‚`a
Ù±‚`p                Ù±‚bbpdselfÙ±‚aoa.Ù±‚`dlineÙ±‚aoa.Ù±‚`hset_dataÙ±‚`a(Ù±‚bnbczipÙ±‚`a(Ù±‚aoa*Ù±‚bbpdselfÙ±‚aoa.Ù±‚`dpolyÙ±‚aoa.Ù±‚`bxyÙ±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚akdelifÙ±‚`a Ù±‚`eeventÙ±‚aoa.Ù±‚`ckeyÙ±‚`a Ù±‚aob==Ù±‚`a Ù±‚bs1a'Ù±‚bs1aiÙ±‚bs1a'Ù±‚`a:Ù±‚`a
Ù±‚`l            Ù±‚`cxysÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bbpdselfÙ±‚aoa.Ù±‚`dpolyÙ±‚aoa.Ù±‚`mget_transformÙ±‚`a(Ù±‚`a)Ù±‚aoa.Ù±‚`itransformÙ±‚`a(Ù±‚bbpdselfÙ±‚aoa.Ù±‚`dpolyÙ±‚aoa.Ù±‚`bxyÙ±‚`a)Ù±‚`a
Ù±‚`l            Ù±‚`apÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`eeventÙ±‚aoa.Ù±‚`axÙ±‚`a,Ù±‚`a Ù±‚`eeventÙ±‚aoa.Ù±‚`ayÙ±‚`b  Ù±‚bc1p# display coordsÙ±‚`a
Ù±‚`l            Ù±‚akcforÙ±‚`a Ù±‚`aiÙ±‚`a Ù±‚bowbinÙ±‚`a Ù±‚bnberangeÙ±‚`a(Ù±‚bnbclenÙ±‚`a(Ù±‚`cxysÙ±‚`a)Ù±‚`a Ù±‚aoa-Ù±‚`a Ù±‚bmia1Ù±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`p                Ù±‚`bs0Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cxysÙ±‚`a[Ù±‚`aiÙ±‚`a]Ù±‚`a
Ù±‚`p                Ù±‚`bs1Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cxysÙ±‚`a[Ù±‚`aiÙ±‚`a Ù±‚aoa+Ù±‚`a Ù±‚bmia1Ù±‚`a]Ù±‚`a
Ù±‚`p                Ù±‚`adÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`udist_point_to_segmentÙ±‚`a(Ù±‚`apÙ±‚`a,Ù±‚`a Ù±‚`bs0Ù±‚`a,Ù±‚`a Ù±‚`bs1Ù±‚`a)Ù±‚`a
Ù±‚`p                Ù±‚akbifÙ±‚`a Ù±‚`adÙ±‚`a Ù±‚aoa<Ù±‚aoa=Ù±‚`a Ù±‚bbpdselfÙ±‚aoa.Ù±‚`gepsilonÙ±‚`a:Ù±‚`a
Ù±‚`t                    Ù±‚bbpdselfÙ±‚aoa.Ù±‚`dpolyÙ±‚aoa.Ù±‚`bxyÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`finsertÙ±‚`a(Ù±‚`a
Ù±‚`x                        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`dpolyÙ±‚aoa.Ù±‚`bxyÙ±‚`a,Ù±‚`a Ù±‚`aiÙ±‚aoa+Ù±‚bmia1Ù±‚`a,Ù±‚`a
Ù±‚`x                        Ù±‚`a[Ù±‚`eeventÙ±‚aoa.Ù±‚`exdataÙ±‚`a,Ù±‚`a Ù±‚`eeventÙ±‚aoa.Ù±‚`eydataÙ±‚`a]Ù±‚`a,Ù±‚`a
Ù±‚`x                        Ù±‚`daxisÙ±‚aoa=Ù±‚bmia0Ù±‚`a)Ù±‚`a
Ù±‚`t                    Ù±‚bbpdselfÙ±‚aoa.Ù±‚`dlineÙ±‚aoa.Ù±‚`hset_dataÙ±‚`a(Ù±‚bnbczipÙ±‚`a(Ù±‚aoa*Ù±‚bbpdselfÙ±‚aoa.Ù±‚`dpolyÙ±‚aoa.Ù±‚`bxyÙ±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`t                    Ù±‚akebreakÙ±‚`a
Ù±‚`h        Ù±‚akbifÙ±‚`a Ù±‚bbpdselfÙ±‚aoa.Ù±‚`dlineÙ±‚aoa.Ù±‚`estaleÙ±‚`a:Ù±‚`a
Ù±‚`l            Ù±‚bbpdselfÙ±‚aoa.Ù±‚`fcanvasÙ±‚aoa.Ù±‚`idraw_idleÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚akcdefÙ±‚`a Ù±‚bnfmon_mouse_moveÙ±‚`a(Ù±‚bbpdselfÙ±‚`a,Ù±‚`a Ù±‚`eeventÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`h        Ù±‚bsdx#"""Callback for mouse movements."""Ù±‚`a
Ù±‚`h        Ù±‚akbifÙ±‚`a Ù±‚bowcnotÙ±‚`a Ù±‚bbpdselfÙ±‚aoa.Ù±‚`ishowvertsÙ±‚`a:Ù±‚`a
Ù±‚`l            Ù±‚akfreturnÙ±‚`a
Ù±‚`h        Ù±‚akbifÙ±‚`a Ù±‚bbpdselfÙ±‚aoa.Ù±‚`d_indÙ±‚`a Ù±‚bowbisÙ±‚`a Ù±‚bkcdNoneÙ±‚`a:Ù±‚`a
Ù±‚`l            Ù±‚akfreturnÙ±‚`a
Ù±‚`h        Ù±‚akbifÙ±‚`a Ù±‚`eeventÙ±‚aoa.Ù±‚`finaxesÙ±‚`a Ù±‚bowbisÙ±‚`a Ù±‚bkcdNoneÙ±‚`a:Ù±‚`a
Ù±‚`l            Ù±‚akfreturnÙ±‚`a
Ù±‚`h        Ù±‚akbifÙ±‚`a Ù±‚`eeventÙ±‚aoa.Ù±‚`fbuttonÙ±‚`a Ù±‚aob!=Ù±‚`a Ù±‚bmia1Ù±‚`a:Ù±‚`a
Ù±‚`l            Ù±‚akfreturnÙ±‚`a
Ù±‚`h        Ù±‚`axÙ±‚`a,Ù±‚`a Ù±‚`ayÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`eeventÙ±‚aoa.Ù±‚`exdataÙ±‚`a,Ù±‚`a Ù±‚`eeventÙ±‚aoa.Ù±‚`eydataÙ±‚`a
Ù±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`dpolyÙ±‚aoa.Ù±‚`bxyÙ±‚`a[Ù±‚bbpdselfÙ±‚aoa.Ù±‚`d_indÙ±‚`a]Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`axÙ±‚`a,Ù±‚`a Ù±‚`ayÙ±‚`a
Ù±‚`h        Ù±‚akbifÙ±‚`a Ù±‚bbpdselfÙ±‚aoa.Ù±‚`d_indÙ±‚`a Ù±‚aob==Ù±‚`a Ù±‚bmia0Ù±‚`a:Ù±‚`a
Ù±‚`l            Ù±‚bbpdselfÙ±‚aoa.Ù±‚`dpolyÙ±‚aoa.Ù±‚`bxyÙ±‚`a[Ù±‚aoa-Ù±‚bmia1Ù±‚`a]Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`axÙ±‚`a,Ù±‚`a Ù±‚`ayÙ±‚`a
Ù±‚`h        Ù±‚akdelifÙ±‚`a Ù±‚bbpdselfÙ±‚aoa.Ù±‚`d_indÙ±‚`a Ù±‚aob==Ù±‚`a Ù±‚bnbclenÙ±‚`a(Ù±‚bbpdselfÙ±‚aoa.Ù±‚`dpolyÙ±‚aoa.Ù±‚`bxyÙ±‚`a)Ù±‚`a Ù±‚aoa-Ù±‚`a Ù±‚bmia1Ù±‚`a:Ù±‚`a
Ù±‚`l            Ù±‚bbpdselfÙ±‚aoa.Ù±‚`dpolyÙ±‚aoa.Ù±‚`bxyÙ±‚`a[Ù±‚bmia0Ù±‚`a]Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`axÙ±‚`a,Ù±‚`a Ù±‚`ayÙ±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`dlineÙ±‚aoa.Ù±‚`hset_dataÙ±‚`a(Ù±‚bnbczipÙ±‚`a(Ù±‚aoa*Ù±‚bbpdselfÙ±‚aoa.Ù±‚`dpolyÙ±‚aoa.Ù±‚`bxyÙ±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`fcanvasÙ±‚aoa.Ù±‚`nrestore_regionÙ±‚`a(Ù±‚bbpdselfÙ±‚aoa.Ù±‚`jbackgroundÙ±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`baxÙ±‚aoa.Ù±‚`kdraw_artistÙ±‚`a(Ù±‚bbpdselfÙ±‚aoa.Ù±‚`dpolyÙ±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`baxÙ±‚aoa.Ù±‚`kdraw_artistÙ±‚`a(Ù±‚bbpdselfÙ±‚aoa.Ù±‚`dlineÙ±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`fcanvasÙ±‚aoa.Ù±‚`dblitÙ±‚`a(Ù±‚bbpdselfÙ±‚aoa.Ù±‚`baxÙ±‚aoa.Ù±‚`dbboxÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚akbifÙ±‚`a Ù±‚bvmh__name__Ù±‚`a Ù±‚aob==Ù±‚`a Ù±‚bs1a'Ù±‚bs1h__main__Ù±‚bs1a'Ù±‚`a:Ù±‚`a
Ù±‚`d    Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnnfpyplotÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnncpltÙ±‚`a
Ù±‚`d    Ù±‚bkndfromÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnngpatchesÙ±‚`a Ù±‚bknfimportÙ±‚`a Ù±‚`gPolygonÙ±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚`ethetaÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`farangeÙ±‚`a(Ù±‚bmia0Ù±‚`a,Ù±‚`a Ù±‚bmia2Ù±‚aoa*Ù±‚`bnpÙ±‚aoa.Ù±‚`bpiÙ±‚`a,Ù±‚`a Ù±‚bmfc0.1Ù±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`arÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bmfc1.5Ù±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚`bxsÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`arÙ±‚`a Ù±‚aoa*Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`ccosÙ±‚`a(Ù±‚`ethetaÙ±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`bysÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`arÙ±‚`a Ù±‚aoa*Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`csinÙ±‚`a(Ù±‚`ethetaÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚`dpolyÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`gPolygonÙ±‚`a(Ù±‚`bnpÙ±‚aoa.Ù±‚`lcolumn_stackÙ±‚`a(Ù±‚`a[Ù±‚`bxsÙ±‚`a,Ù±‚`a Ù±‚`bysÙ±‚`a]Ù±‚`a)Ù±‚`a,Ù±‚`a Ù±‚`hanimatedÙ±‚aoa=Ù±‚bkcdTrueÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚`cfigÙ±‚`a,Ù±‚`a Ù±‚`baxÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cpltÙ±‚aoa.Ù±‚`hsubplotsÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`baxÙ±‚aoa.Ù±‚`iadd_patchÙ±‚`a(Ù±‚`dpolyÙ±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`apÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`qPolygonInteractorÙ±‚`a(Ù±‚`baxÙ±‚`a,Ù±‚`a Ù±‚`dpolyÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚`baxÙ±‚aoa.Ù±‚`iset_titleÙ±‚`a(Ù±‚bs1a'Ù±‚bs1x!Click and drag a point to move itÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`baxÙ±‚aoa.Ù±‚`hset_xlimÙ±‚`a(Ù±‚`a(Ù±‚aoa-Ù±‚bmia2Ù±‚`a,Ù±‚`a Ù±‚bmia2Ù±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`baxÙ±‚aoa.Ù±‚`hset_ylimÙ±‚`a(Ù±‚`a(Ù±‚aoa-Ù±‚bmia2Ù±‚`a,Ù±‚`a Ù±‚bmia2Ù±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`cpltÙ±‚aoa.Ù±‚`dshowÙ±‚`a(Ù±‚`a)Ù±‚`a
`dNoneö