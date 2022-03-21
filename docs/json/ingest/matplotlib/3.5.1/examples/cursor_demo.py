Ù¯‚Ù´ƒ™åÙ±‚bsdy"""
=================
Cross hair cursor
=================

This example adds a cross hair as a data cursor.  The cross hair is
implemented as regular line objects that are updated on mouse move.

We show three implementations:

1) A simple cursor implementation that redraws the figure on every mouse move.
   This is a bit slow and you may notice some lag of the cross hair movement.
2) A cursor that uses blitting for speedup of the rendering.
3) A cursor that snaps to data points.

Faster cursoring is possible using native GUI drawing, as in
:doc:`/gallery/user_interfaces/wxcursor_demo_sgskip`.

The mpldatacursor__ and mplcursors__ third-party packages can be used to
achieve a similar effect.

__ https://github.com/joferkington/mpldatacursor
__ https://github.com/anntzer/mplcursors
"""Ù±‚`a
Ù±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnnfpyplotÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnncpltÙ±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„enumpyÙ „enumpyf1.22.3fmoduleenumpyfmoduleõÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnnbnpÙ±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚akeclassÙ±‚`a Ù±‚bncfCursorÙ±‚`a:Ù±‚`a
Ù±‚`d    Ù±‚bsdx$"""
    A cross hair cursor.
    """Ù±‚`a
Ù±‚`d    Ù±‚akcdefÙ±‚`a Ù±‚bfmh__init__Ù±‚`a(Ù±‚bbpdselfÙ±‚`a,Ù±‚`a Ù±‚`baxÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`baxÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`baxÙ±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`ohorizontal_lineÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`baxÙ±‚aoa.Ù±‚`gaxhlineÙ±‚`a(Ù±‚`ecolorÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1akÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`blwÙ±‚aoa=Ù±‚bmfc0.8Ù±‚`a,Ù±‚`a Ù±‚`blsÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1b--Ù±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`mvertical_lineÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`baxÙ±‚aoa.Ù±‚`gaxvlineÙ±‚`a(Ù±‚`ecolorÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1akÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`blwÙ±‚aoa=Ù±‚bmfc0.8Ù±‚`a,Ù±‚`a Ù±‚`blsÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1b--Ù±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚bc1x## text location in axes coordinatesÙ±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`dtextÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`baxÙ±‚aoa.Ù±‚`dtextÙ±‚`a(Ù±‚bmfd0.72Ù±‚`a,Ù±‚`a Ù±‚bmfc0.9Ù±‚`a,Ù±‚`a Ù±‚bs1a'Ù±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`itransformÙ±‚aoa=Ù±‚`baxÙ±‚aoa.Ù±‚`itransAxesÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚akcdefÙ±‚`a Ù±‚bnfvset_cross_hair_visibleÙ±‚`a(Ù±‚bbpdselfÙ±‚`a,Ù±‚`a Ù±‚`gvisibleÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`h        Ù±‚`kneed_redrawÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bbpdselfÙ±‚aoa.Ù±‚`ohorizontal_lineÙ±‚aoa.Ù±‚`kget_visibleÙ±‚`a(Ù±‚`a)Ù±‚`a Ù±‚aob!=Ù±‚`a Ù±‚`gvisibleÙ±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`ohorizontal_lineÙ±‚aoa.Ù±‚`kset_visibleÙ±‚`a(Ù±‚`gvisibleÙ±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`mvertical_lineÙ±‚aoa.Ù±‚`kset_visibleÙ±‚`a(Ù±‚`gvisibleÙ±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`dtextÙ±‚aoa.Ù±‚`kset_visibleÙ±‚`a(Ù±‚`gvisibleÙ±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚akfreturnÙ±‚`a Ù±‚`kneed_redrawÙ±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚akcdefÙ±‚`a Ù±‚bnfmon_mouse_moveÙ±‚`a(Ù±‚bbpdselfÙ±‚`a,Ù±‚`a Ù±‚`eeventÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`h        Ù±‚akbifÙ±‚`a Ù±‚bowcnotÙ±‚`a Ù±‚`eeventÙ±‚aoa.Ù±‚`finaxesÙ±‚`a:Ù±‚`a
Ù±‚`l            Ù±‚`kneed_redrawÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bbpdselfÙ±‚aoa.Ù±‚`vset_cross_hair_visibleÙ±‚`a(Ù±‚bkceFalseÙ±‚`a)Ù±‚`a
Ù±‚`l            Ù±‚akbifÙ±‚`a Ù±‚`kneed_redrawÙ±‚`a:Ù±‚`a
Ù±‚`p                Ù±‚bbpdselfÙ±‚aoa.Ù±‚`baxÙ±‚aoa.Ù±‚`ffigureÙ±‚aoa.Ù±‚`fcanvasÙ±‚aoa.Ù±‚`ddrawÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚akdelseÙ±‚`a:Ù±‚`a
Ù±‚`l            Ù±‚bbpdselfÙ±‚aoa.Ù±‚`vset_cross_hair_visibleÙ±‚`a(Ù±‚bkcdTrueÙ±‚`a)Ù±‚`a
Ù±‚`l            Ù±‚`axÙ±‚`a,Ù±‚`a Ù±‚`ayÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`eeventÙ±‚aoa.Ù±‚`exdataÙ±‚`a,Ù±‚`a Ù±‚`eeventÙ±‚aoa.Ù±‚`eydataÙ±‚`a
Ù±‚`l            Ù±‚bc1x# update the line positionsÙ±‚`a
Ù±‚`l            Ù±‚bbpdselfÙ±‚aoa.Ù±‚`ohorizontal_lineÙ±‚aoa.Ù±‚`iset_ydataÙ±‚`a(Ù±‚`ayÙ±‚`a)Ù±‚`a
Ù±‚`l            Ù±‚bbpdselfÙ±‚aoa.Ù±‚`mvertical_lineÙ±‚aoa.Ù±‚`iset_xdataÙ±‚`a(Ù±‚`axÙ±‚`a)Ù±‚`a
Ù±‚`l            Ù±‚bbpdselfÙ±‚aoa.Ù±‚`dtextÙ±‚aoa.Ù±‚`hset_textÙ±‚`a(Ù±‚bs1a'Ù±‚bs1bx=Ù±‚bsie%1.2fÙ±‚bs1d, y=Ù±‚bsie%1.2fÙ±‚bs1a'Ù±‚`a Ù±‚aoa%Ù±‚`a Ù±‚`a(Ù±‚`axÙ±‚`a,Ù±‚`a Ù±‚`ayÙ±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`l            Ù±‚bbpdselfÙ±‚aoa.Ù±‚`baxÙ±‚aoa.Ù±‚`ffigureÙ±‚aoa.Ù±‚`fcanvasÙ±‚aoa.Ù±‚`ddrawÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚`axÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`farangeÙ±‚`a(Ù±‚bmia0Ù±‚`a,Ù±‚`a Ù±‚bmia1Ù±‚`a,Ù±‚`a Ù±‚bmfd0.01Ù±‚`a)Ù±‚`a
Ù±‚`ayÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`csinÙ±‚`a(Ù±‚bmia2Ù±‚`a Ù±‚aoa*Ù±‚`a Ù±‚bmia2Ù±‚`a Ù±‚aoa*Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`bpiÙ±‚`a Ù±‚aoa*Ù±‚`a Ù±‚`axÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`cfigÙ±‚`a,Ù±‚`a Ù±‚`baxÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cpltÙ±‚aoa.Ù±‚`hsubplotsÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`iset_titleÙ±‚`a(Ù±‚bs1a'Ù±‚bs1mSimple cursorÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`dplotÙ±‚`a(Ù±‚`axÙ±‚`a,Ù±‚`a Ù±‚`ayÙ±‚`a,Ù±‚`a Ù±‚bs1a'Ù±‚bs1aoÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`fcursorÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`fCursorÙ±‚`a(Ù±‚`baxÙ±‚`a)Ù±‚`a
Ù±‚`cfigÙ±‚aoa.Ù±‚`fcanvasÙ±‚aoa.Ù±‚`kmpl_connectÙ±‚`a(Ù±‚bs1a'Ù±‚bs1smotion_notify_eventÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`fcursorÙ±‚aoa.Ù±‚`mon_mouse_moveÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚bc1xN##############################################################################Ù±‚`a
Ù±‚bc1x!# Faster redrawing using blittingÙ±‚`a
Ù±‚bc1x!# """""""""""""""""""""""""""""""Ù±‚`a
Ù±‚bc1xI# This technique stores the rendered plot as a background image. Only theÙ±‚`a
Ù±‚bc1xI# changed artists (cross hair lines and text) are rendered anew. They areÙ±‚`a
Ù±‚bc1x.# combined with the background using blitting.Ù±‚`a
Ù±‚bc1a#Ù±‚`a
Ù±‚bc1xN# This technique is significantly faster. It requires a bit more setup becauseÙ±‚`a
Ù±‚bc1xC# the background has to be stored without the cross hair lines (seeÙ±‚`a
Ù±‚bc1xH# ``create_new_background()``). Additionally, a new background has to beÙ±‚`a
Ù±‚bc1xL# created whenever the figure changes. This is achieved by connecting to theÙ±‚`a
Ù±‚bc1s# ``'draw_event'``.Ù±‚`a
Ù±‚`a
Ù±‚akeclassÙ±‚`a Ù±‚bncmBlittedCursorÙ±‚`a:Ù±‚`a
Ù±‚`d    Ù±‚bsdxE"""
    A cross hair cursor using blitting for faster redraw.
    """Ù±‚`a
Ù±‚`d    Ù±‚akcdefÙ±‚`a Ù±‚bfmh__init__Ù±‚`a(Ù±‚bbpdselfÙ±‚`a,Ù±‚`a Ù±‚`baxÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`baxÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`baxÙ±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`jbackgroundÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bkcdNoneÙ±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`ohorizontal_lineÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`baxÙ±‚aoa.Ù±‚`gaxhlineÙ±‚`a(Ù±‚`ecolorÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1akÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`blwÙ±‚aoa=Ù±‚bmfc0.8Ù±‚`a,Ù±‚`a Ù±‚`blsÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1b--Ù±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`mvertical_lineÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`baxÙ±‚aoa.Ù±‚`gaxvlineÙ±‚`a(Ù±‚`ecolorÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1akÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`blwÙ±‚aoa=Ù±‚bmfc0.8Ù±‚`a,Ù±‚`a Ù±‚`blsÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1b--Ù±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚bc1x## text location in axes coordinatesÙ±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`dtextÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`baxÙ±‚aoa.Ù±‚`dtextÙ±‚`a(Ù±‚bmfd0.72Ù±‚`a,Ù±‚`a Ù±‚bmfc0.9Ù±‚`a,Ù±‚`a Ù±‚bs1a'Ù±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`itransformÙ±‚aoa=Ù±‚`baxÙ±‚aoa.Ù±‚`itransAxesÙ±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`t_creating_backgroundÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bkceFalseÙ±‚`a
Ù±‚`h        Ù±‚`baxÙ±‚aoa.Ù±‚`ffigureÙ±‚aoa.Ù±‚`fcanvasÙ±‚aoa.Ù±‚`kmpl_connectÙ±‚`a(Ù±‚bs1a'Ù±‚bs1jdraw_eventÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚bbpdselfÙ±‚aoa.Ù±‚`gon_drawÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚akcdefÙ±‚`a Ù±‚bnfgon_drawÙ±‚`a(Ù±‚bbpdselfÙ±‚`a,Ù±‚`a Ù±‚`eeventÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`ucreate_new_backgroundÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚akcdefÙ±‚`a Ù±‚bnfvset_cross_hair_visibleÙ±‚`a(Ù±‚bbpdselfÙ±‚`a,Ù±‚`a Ù±‚`gvisibleÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`h        Ù±‚`kneed_redrawÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bbpdselfÙ±‚aoa.Ù±‚`ohorizontal_lineÙ±‚aoa.Ù±‚`kget_visibleÙ±‚`a(Ù±‚`a)Ù±‚`a Ù±‚aob!=Ù±‚`a Ù±‚`gvisibleÙ±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`ohorizontal_lineÙ±‚aoa.Ù±‚`kset_visibleÙ±‚`a(Ù±‚`gvisibleÙ±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`mvertical_lineÙ±‚aoa.Ù±‚`kset_visibleÙ±‚`a(Ù±‚`gvisibleÙ±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`dtextÙ±‚aoa.Ù±‚`kset_visibleÙ±‚`a(Ù±‚`gvisibleÙ±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚akfreturnÙ±‚`a Ù±‚`kneed_redrawÙ±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚akcdefÙ±‚`a Ù±‚bnfucreate_new_backgroundÙ±‚`a(Ù±‚bbpdselfÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`h        Ù±‚akbifÙ±‚`a Ù±‚bbpdselfÙ±‚aoa.Ù±‚`t_creating_backgroundÙ±‚`a:Ù±‚`a
Ù±‚`l            Ù±‚bc1x3# discard calls triggered from within this functionÙ±‚`a
Ù±‚`l            Ù±‚akfreturnÙ±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`t_creating_backgroundÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bkcdTrueÙ±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`vset_cross_hair_visibleÙ±‚`a(Ù±‚bkceFalseÙ±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`baxÙ±‚aoa.Ù±‚`ffigureÙ±‚aoa.Ù±‚`fcanvasÙ±‚aoa.Ù±‚`ddrawÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`jbackgroundÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bbpdselfÙ±‚aoa.Ù±‚`baxÙ±‚aoa.Ù±‚`ffigureÙ±‚aoa.Ù±‚`fcanvasÙ±‚aoa.Ù±‚`ncopy_from_bboxÙ±‚`a(Ù±‚bbpdselfÙ±‚aoa.Ù±‚`baxÙ±‚aoa.Ù±‚`dbboxÙ±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`vset_cross_hair_visibleÙ±‚`a(Ù±‚bkcdTrueÙ±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`t_creating_backgroundÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bkceFalseÙ±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚akcdefÙ±‚`a Ù±‚bnfmon_mouse_moveÙ±‚`a(Ù±‚bbpdselfÙ±‚`a,Ù±‚`a Ù±‚`eeventÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`h        Ù±‚akbifÙ±‚`a Ù±‚bbpdselfÙ±‚aoa.Ù±‚`jbackgroundÙ±‚`a Ù±‚bowbisÙ±‚`a Ù±‚bkcdNoneÙ±‚`a:Ù±‚`a
Ù±‚`l            Ù±‚bbpdselfÙ±‚aoa.Ù±‚`ucreate_new_backgroundÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚akbifÙ±‚`a Ù±‚bowcnotÙ±‚`a Ù±‚`eeventÙ±‚aoa.Ù±‚`finaxesÙ±‚`a:Ù±‚`a
Ù±‚`l            Ù±‚`kneed_redrawÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bbpdselfÙ±‚aoa.Ù±‚`vset_cross_hair_visibleÙ±‚`a(Ù±‚bkceFalseÙ±‚`a)Ù±‚`a
Ù±‚`l            Ù±‚akbifÙ±‚`a Ù±‚`kneed_redrawÙ±‚`a:Ù±‚`a
Ù±‚`p                Ù±‚bbpdselfÙ±‚aoa.Ù±‚`baxÙ±‚aoa.Ù±‚`ffigureÙ±‚aoa.Ù±‚`fcanvasÙ±‚aoa.Ù±‚`nrestore_regionÙ±‚`a(Ù±‚bbpdselfÙ±‚aoa.Ù±‚`jbackgroundÙ±‚`a)Ù±‚`a
Ù±‚`p                Ù±‚bbpdselfÙ±‚aoa.Ù±‚`baxÙ±‚aoa.Ù±‚`ffigureÙ±‚aoa.Ù±‚`fcanvasÙ±‚aoa.Ù±‚`dblitÙ±‚`a(Ù±‚bbpdselfÙ±‚aoa.Ù±‚`baxÙ±‚aoa.Ù±‚`dbboxÙ±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚akdelseÙ±‚`a:Ù±‚`a
Ù±‚`l            Ù±‚bbpdselfÙ±‚aoa.Ù±‚`vset_cross_hair_visibleÙ±‚`a(Ù±‚bkcdTrueÙ±‚`a)Ù±‚`a
Ù±‚`l            Ù±‚bc1x# update the line positionsÙ±‚`a
Ù±‚`l            Ù±‚`axÙ±‚`a,Ù±‚`a Ù±‚`ayÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`eeventÙ±‚aoa.Ù±‚`exdataÙ±‚`a,Ù±‚`a Ù±‚`eeventÙ±‚aoa.Ù±‚`eydataÙ±‚`a
Ù±‚`l            Ù±‚bbpdselfÙ±‚aoa.Ù±‚`ohorizontal_lineÙ±‚aoa.Ù±‚`iset_ydataÙ±‚`a(Ù±‚`ayÙ±‚`a)Ù±‚`a
Ù±‚`l            Ù±‚bbpdselfÙ±‚aoa.Ù±‚`mvertical_lineÙ±‚aoa.Ù±‚`iset_xdataÙ±‚`a(Ù±‚`axÙ±‚`a)Ù±‚`a
Ù±‚`l            Ù±‚bbpdselfÙ±‚aoa.Ù±‚`dtextÙ±‚aoa.Ù±‚`hset_textÙ±‚`a(Ù±‚bs1a'Ù±‚bs1bx=Ù±‚bsie%1.2fÙ±‚bs1d, y=Ù±‚bsie%1.2fÙ±‚bs1a'Ù±‚`a Ù±‚aoa%Ù±‚`a Ù±‚`a(Ù±‚`axÙ±‚`a,Ù±‚`a Ù±‚`ayÙ±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`l            Ù±‚bbpdselfÙ±‚aoa.Ù±‚`baxÙ±‚aoa.Ù±‚`ffigureÙ±‚aoa.Ù±‚`fcanvasÙ±‚aoa.Ù±‚`nrestore_regionÙ±‚`a(Ù±‚bbpdselfÙ±‚aoa.Ù±‚`jbackgroundÙ±‚`a)Ù±‚`a
Ù±‚`l            Ù±‚bbpdselfÙ±‚aoa.Ù±‚`baxÙ±‚aoa.Ù±‚`kdraw_artistÙ±‚`a(Ù±‚bbpdselfÙ±‚aoa.Ù±‚`ohorizontal_lineÙ±‚`a)Ù±‚`a
Ù±‚`l            Ù±‚bbpdselfÙ±‚aoa.Ù±‚`baxÙ±‚aoa.Ù±‚`kdraw_artistÙ±‚`a(Ù±‚bbpdselfÙ±‚aoa.Ù±‚`mvertical_lineÙ±‚`a)Ù±‚`a
Ù±‚`l            Ù±‚bbpdselfÙ±‚aoa.Ù±‚`baxÙ±‚aoa.Ù±‚`kdraw_artistÙ±‚`a(Ù±‚bbpdselfÙ±‚aoa.Ù±‚`dtextÙ±‚`a)Ù±‚`a
Ù±‚`l            Ù±‚bbpdselfÙ±‚aoa.Ù±‚`baxÙ±‚aoa.Ù±‚`ffigureÙ±‚aoa.Ù±‚`fcanvasÙ±‚aoa.Ù±‚`dblitÙ±‚`a(Ù±‚bbpdselfÙ±‚aoa.Ù±‚`baxÙ±‚aoa.Ù±‚`dbboxÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚`axÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`farangeÙ±‚`a(Ù±‚bmia0Ù±‚`a,Ù±‚`a Ù±‚bmia1Ù±‚`a,Ù±‚`a Ù±‚bmfd0.01Ù±‚`a)Ù±‚`a
Ù±‚`ayÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`csinÙ±‚`a(Ù±‚bmia2Ù±‚`a Ù±‚aoa*Ù±‚`a Ù±‚bmia2Ù±‚`a Ù±‚aoa*Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`bpiÙ±‚`a Ù±‚aoa*Ù±‚`a Ù±‚`axÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`cfigÙ±‚`a,Ù±‚`a Ù±‚`baxÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cpltÙ±‚aoa.Ù±‚`hsubplotsÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`iset_titleÙ±‚`a(Ù±‚bs1a'Ù±‚bs1nBlitted cursorÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`dplotÙ±‚`a(Ù±‚`axÙ±‚`a,Ù±‚`a Ù±‚`ayÙ±‚`a,Ù±‚`a Ù±‚bs1a'Ù±‚bs1aoÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`nblitted_cursorÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`mBlittedCursorÙ±‚`a(Ù±‚`baxÙ±‚`a)Ù±‚`a
Ù±‚`cfigÙ±‚aoa.Ù±‚`fcanvasÙ±‚aoa.Ù±‚`kmpl_connectÙ±‚`a(Ù±‚bs1a'Ù±‚bs1smotion_notify_eventÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`nblitted_cursorÙ±‚aoa.Ù±‚`mon_mouse_moveÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚bc1xN##############################################################################Ù±‚`a
Ù±‚bc1x# Snapping to data pointsÙ±‚`a
Ù±‚bc1x# """""""""""""""""""""""Ù±‚`a
Ù±‚bc1xK# The following cursor snaps its position to the data points of a `.Line2D`Ù±‚`a
Ù±‚bc1i# object.Ù±‚`a
Ù±‚bc1a#Ù±‚`a
Ù±‚bc1xL# To save unnecessary redraws, the index of the last indicated data point isÙ±‚`a
Ù±‚bc1xJ# saved in ``self._last_index``. A redraw is only triggered when the mouseÙ±‚`a
Ù±‚bc1xL# moves far enough so that another data point must be selected. This reducesÙ±‚`a
Ù±‚bc1xN# the lag due to many redraws. Of course, blitting could still be added on topÙ±‚`a
Ù±‚bc1x# for additional speedup.Ù±‚`a
Ù±‚`a
Ù±‚akeclassÙ±‚`a Ù±‚bncnSnappingCursorÙ±‚`a:Ù±‚`a
Ù±‚`d    Ù±‚bsdxÍ"""
    A cross hair cursor that snaps to the data point of a line, which is
    closest to the *x* position of the cursor.

    For simplicity, this assumes that *x* values of the data are sorted.
    """Ù±‚`a
Ù±‚`d    Ù±‚akcdefÙ±‚`a Ù±‚bfmh__init__Ù±‚`a(Ù±‚bbpdselfÙ±‚`a,Ù±‚`a Ù±‚`baxÙ±‚`a,Ù±‚`a Ù±‚`dlineÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`baxÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`baxÙ±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`ohorizontal_lineÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`baxÙ±‚aoa.Ù±‚`gaxhlineÙ±‚`a(Ù±‚`ecolorÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1akÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`blwÙ±‚aoa=Ù±‚bmfc0.8Ù±‚`a,Ù±‚`a Ù±‚`blsÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1b--Ù±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`mvertical_lineÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`baxÙ±‚aoa.Ù±‚`gaxvlineÙ±‚`a(Ù±‚`ecolorÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1akÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`blwÙ±‚aoa=Ù±‚bmfc0.8Ù±‚`a,Ù±‚`a Ù±‚`blsÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1b--Ù±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`axÙ±‚`a,Ù±‚`a Ù±‚bbpdselfÙ±‚aoa.Ù±‚`ayÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`dlineÙ±‚aoa.Ù±‚`hget_dataÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`k_last_indexÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bkcdNoneÙ±‚`a
Ù±‚`h        Ù±‚bc1x# text location in axes coordsÙ±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`dtextÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`baxÙ±‚aoa.Ù±‚`dtextÙ±‚`a(Ù±‚bmfd0.72Ù±‚`a,Ù±‚`a Ù±‚bmfc0.9Ù±‚`a,Ù±‚`a Ù±‚bs1a'Ù±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`itransformÙ±‚aoa=Ù±‚`baxÙ±‚aoa.Ù±‚`itransAxesÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚akcdefÙ±‚`a Ù±‚bnfvset_cross_hair_visibleÙ±‚`a(Ù±‚bbpdselfÙ±‚`a,Ù±‚`a Ù±‚`gvisibleÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`h        Ù±‚`kneed_redrawÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bbpdselfÙ±‚aoa.Ù±‚`ohorizontal_lineÙ±‚aoa.Ù±‚`kget_visibleÙ±‚`a(Ù±‚`a)Ù±‚`a Ù±‚aob!=Ù±‚`a Ù±‚`gvisibleÙ±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`ohorizontal_lineÙ±‚aoa.Ù±‚`kset_visibleÙ±‚`a(Ù±‚`gvisibleÙ±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`mvertical_lineÙ±‚aoa.Ù±‚`kset_visibleÙ±‚`a(Ù±‚`gvisibleÙ±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`dtextÙ±‚aoa.Ù±‚`kset_visibleÙ±‚`a(Ù±‚`gvisibleÙ±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚akfreturnÙ±‚`a Ù±‚`kneed_redrawÙ±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚akcdefÙ±‚`a Ù±‚bnfmon_mouse_moveÙ±‚`a(Ù±‚bbpdselfÙ±‚`a,Ù±‚`a Ù±‚`eeventÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`h        Ù±‚akbifÙ±‚`a Ù±‚bowcnotÙ±‚`a Ù±‚`eeventÙ±‚aoa.Ù±‚`finaxesÙ±‚`a:Ù±‚`a
Ù±‚`l            Ù±‚bbpdselfÙ±‚aoa.Ù±‚`k_last_indexÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bkcdNoneÙ±‚`a
Ù±‚`l            Ù±‚`kneed_redrawÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bbpdselfÙ±‚aoa.Ù±‚`vset_cross_hair_visibleÙ±‚`a(Ù±‚bkceFalseÙ±‚`a)Ù±‚`a
Ù±‚`l            Ù±‚akbifÙ±‚`a Ù±‚`kneed_redrawÙ±‚`a:Ù±‚`a
Ù±‚`p                Ù±‚bbpdselfÙ±‚aoa.Ù±‚`baxÙ±‚aoa.Ù±‚`ffigureÙ±‚aoa.Ù±‚`fcanvasÙ±‚aoa.Ù±‚`ddrawÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚akdelseÙ±‚`a:Ù±‚`a
Ù±‚`l            Ù±‚bbpdselfÙ±‚aoa.Ù±‚`vset_cross_hair_visibleÙ±‚`a(Ù±‚bkcdTrueÙ±‚`a)Ù±‚`a
Ù±‚`l            Ù±‚`axÙ±‚`a,Ù±‚`a Ù±‚`ayÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`eeventÙ±‚aoa.Ù±‚`exdataÙ±‚`a,Ù±‚`a Ù±‚`eeventÙ±‚aoa.Ù±‚`eydataÙ±‚`a
Ù±‚`l            Ù±‚`eindexÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bnbcminÙ±‚`a(Ù±‚`bnpÙ±‚aoa.Ù±‚`lsearchsortedÙ±‚`a(Ù±‚bbpdselfÙ±‚aoa.Ù±‚`axÙ±‚`a,Ù±‚`a Ù±‚`axÙ±‚`a)Ù±‚`a,Ù±‚`a Ù±‚bnbclenÙ±‚`a(Ù±‚bbpdselfÙ±‚aoa.Ù±‚`axÙ±‚`a)Ù±‚`a Ù±‚aoa-Ù±‚`a Ù±‚bmia1Ù±‚`a)Ù±‚`a
Ù±‚`l            Ù±‚akbifÙ±‚`a Ù±‚`eindexÙ±‚`a Ù±‚aob==Ù±‚`a Ù±‚bbpdselfÙ±‚aoa.Ù±‚`k_last_indexÙ±‚`a:Ù±‚`a
Ù±‚`p                Ù±‚akfreturnÙ±‚`b  Ù±‚bc1x.# still on the same data point. Nothing to do.Ù±‚`a
Ù±‚`l            Ù±‚bbpdselfÙ±‚aoa.Ù±‚`k_last_indexÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`eindexÙ±‚`a
Ù±‚`l            Ù±‚`axÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bbpdselfÙ±‚aoa.Ù±‚`axÙ±‚`a[Ù±‚`eindexÙ±‚`a]Ù±‚`a
Ù±‚`l            Ù±‚`ayÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bbpdselfÙ±‚aoa.Ù±‚`ayÙ±‚`a[Ù±‚`eindexÙ±‚`a]Ù±‚`a
Ù±‚`l            Ù±‚bc1x# update the line positionsÙ±‚`a
Ù±‚`l            Ù±‚bbpdselfÙ±‚aoa.Ù±‚`ohorizontal_lineÙ±‚aoa.Ù±‚`iset_ydataÙ±‚`a(Ù±‚`ayÙ±‚`a)Ù±‚`a
Ù±‚`l            Ù±‚bbpdselfÙ±‚aoa.Ù±‚`mvertical_lineÙ±‚aoa.Ù±‚`iset_xdataÙ±‚`a(Ù±‚`axÙ±‚`a)Ù±‚`a
Ù±‚`l            Ù±‚bbpdselfÙ±‚aoa.Ù±‚`dtextÙ±‚aoa.Ù±‚`hset_textÙ±‚`a(Ù±‚bs1a'Ù±‚bs1bx=Ù±‚bsie%1.2fÙ±‚bs1d, y=Ù±‚bsie%1.2fÙ±‚bs1a'Ù±‚`a Ù±‚aoa%Ù±‚`a Ù±‚`a(Ù±‚`axÙ±‚`a,Ù±‚`a Ù±‚`ayÙ±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`l            Ù±‚bbpdselfÙ±‚aoa.Ù±‚`baxÙ±‚aoa.Ù±‚`ffigureÙ±‚aoa.Ù±‚`fcanvasÙ±‚aoa.Ù±‚`ddrawÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚`axÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`farangeÙ±‚`a(Ù±‚bmia0Ù±‚`a,Ù±‚`a Ù±‚bmia1Ù±‚`a,Ù±‚`a Ù±‚bmfd0.01Ù±‚`a)Ù±‚`a
Ù±‚`ayÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`csinÙ±‚`a(Ù±‚bmia2Ù±‚`a Ù±‚aoa*Ù±‚`a Ù±‚bmia2Ù±‚`a Ù±‚aoa*Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`bpiÙ±‚`a Ù±‚aoa*Ù±‚`a Ù±‚`axÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`cfigÙ±‚`a,Ù±‚`a Ù±‚`baxÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cpltÙ±‚aoa.Ù±‚`hsubplotsÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`iset_titleÙ±‚`a(Ù±‚bs1a'Ù±‚bs1oSnapping cursorÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`dlineÙ±‚`a,Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`baxÙ±‚aoa.Ù±‚`dplotÙ±‚`a(Ù±‚`axÙ±‚`a,Ù±‚`a Ù±‚`ayÙ±‚`a,Ù±‚`a Ù±‚bs1a'Ù±‚bs1aoÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`ksnap_cursorÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`nSnappingCursorÙ±‚`a(Ù±‚`baxÙ±‚`a,Ù±‚`a Ù±‚`dlineÙ±‚`a)Ù±‚`a
Ù±‚`cfigÙ±‚aoa.Ù±‚`fcanvasÙ±‚aoa.Ù±‚`kmpl_connectÙ±‚`a(Ù±‚bs1a'Ù±‚bs1smotion_notify_eventÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`ksnap_cursorÙ±‚aoa.Ù±‚`mon_mouse_moveÙ±‚`a)Ù±‚`a
Ù±‚`cpltÙ±‚aoa.Ù±‚`dshowÙ±‚`a(Ù±‚`a)Ù±‚`a
`dNoneö