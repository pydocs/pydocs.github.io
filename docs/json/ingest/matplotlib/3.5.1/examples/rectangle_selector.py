Ù¯‚Ù´ƒ™ðÙ±‚bsdy£"""
===============================
Rectangle and ellipse selectors
===============================

Click somewhere, move the mouse, and release the mouse button.
`.RectangleSelector` and `.EllipseSelector` draw a rectangle or an ellipse
from the initial click position to the current mouse position (within the same
axes) until the button is released.  A connected callback receives the click-
and release-events.
"""Ù±‚`a
Ù±‚`a
Ù±‚bkndfromÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnngwidgetsÙ±‚`a Ù±‚bknfimportÙ±‚`a Ù±‚`oEllipseSelectorÙ±‚`a,Ù±‚`a Ù±‚`qRectangleSelectorÙ±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„enumpyÙ „enumpyf1.22.3fmoduleenumpyfmoduleõÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnnbnpÙ±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnnfpyplotÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnncpltÙ±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚akcdefÙ±‚`a Ù±‚bnfoselect_callbackÙ±‚`a(Ù±‚`feclickÙ±‚`a,Ù±‚`a Ù±‚`hereleaseÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`d    Ù±‚bsdxk"""
    Callback for line selection.

    *eclick* and *erelease* are the press and release events.
    """Ù±‚`a
Ù±‚`d    Ù±‚`bx1Ù±‚`a,Ù±‚`a Ù±‚`by1Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`feclickÙ±‚aoa.Ù±‚`exdataÙ±‚`a,Ù±‚`a Ù±‚`feclickÙ±‚aoa.Ù±‚`eydataÙ±‚`a
Ù±‚`d    Ù±‚`bx2Ù±‚`a,Ù±‚`a Ù±‚`by2Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`hereleaseÙ±‚aoa.Ù±‚`exdataÙ±‚`a,Ù±‚`a Ù±‚`hereleaseÙ±‚aoa.Ù±‚`eydataÙ±‚`a
Ù±‚`d    Ù±‚bnbeprintÙ±‚`a(Ù±‚bsaafÙ±‚bs2a"Ù±‚bs2a(Ù±‚bsia{Ù±‚`bx1Ù±‚bsia:Ù±‚bs2d3.2fÙ±‚bsia}Ù±‚bs2b, Ù±‚bsia{Ù±‚`by1Ù±‚bsia:Ù±‚bs2d3.2fÙ±‚bsia}Ù±‚bs2g) --> (Ù±‚bsia{Ù±‚`bx2Ù±‚bsia:Ù±‚bs2d3.2fÙ±‚bsia}Ù±‚bs2b, Ù±‚bsia{Ù±‚`by2Ù±‚bsia:Ù±‚bs2d3.2fÙ±‚bsia}Ù±‚bs2a)Ù±‚bs2a"Ù±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚bnbeprintÙ±‚`a(Ù±‚bsaafÙ±‚bs2a"Ù±‚bs2xThe buttons you used were: Ù±‚bsia{Ù±‚`feclickÙ±‚aoa.Ù±‚`fbuttonÙ±‚bsia}Ù±‚bs2a Ù±‚bsia{Ù±‚`hereleaseÙ±‚aoa.Ù±‚`fbuttonÙ±‚bsia}Ù±‚bs2a"Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚akcdefÙ±‚`a Ù±‚bnfotoggle_selectorÙ±‚`a(Ù±‚`eeventÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`d    Ù±‚bnbeprintÙ±‚`a(Ù±‚bs1a'Ù±‚bs1lKey pressed.Ù±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚akbifÙ±‚`a Ù±‚`eeventÙ±‚aoa.Ù±‚`ckeyÙ±‚`a Ù±‚aob==Ù±‚`a Ù±‚bs1a'Ù±‚bs1atÙ±‚bs1a'Ù±‚`a:Ù±‚`a
Ù±‚`h        Ù±‚akcforÙ±‚`a Ù±‚`hselectorÙ±‚`a Ù±‚bowbinÙ±‚`a Ù±‚`iselectorsÙ±‚`a:Ù±‚`a
Ù±‚`l            Ù±‚`dnameÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bnbdtypeÙ±‚`a(Ù±‚`hselectorÙ±‚`a)Ù±‚aoa.Ù±‚bvmh__name__Ù±‚`a
Ù±‚`l            Ù±‚akbifÙ±‚`a Ù±‚`hselectorÙ±‚aoa.Ù±‚`factiveÙ±‚`a:Ù±‚`a
Ù±‚`p                Ù±‚bnbeprintÙ±‚`a(Ù±‚bsaafÙ±‚bs1a'Ù±‚bsia{Ù±‚`dnameÙ±‚bsia}Ù±‚bs1m deactivated.Ù±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`p                Ù±‚`hselectorÙ±‚aoa.Ù±‚`jset_activeÙ±‚`a(Ù±‚bkceFalseÙ±‚`a)Ù±‚`a
Ù±‚`l            Ù±‚akdelseÙ±‚`a:Ù±‚`a
Ù±‚`p                Ù±‚bnbeprintÙ±‚`a(Ù±‚bsaafÙ±‚bs1a'Ù±‚bsia{Ù±‚`dnameÙ±‚bsia}Ù±‚bs1k activated.Ù±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`p                Ù±‚`hselectorÙ±‚aoa.Ù±‚`jset_activeÙ±‚`a(Ù±‚bkcdTrueÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚`cfigÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cpltÙ±‚aoa.Ù±‚`ffigureÙ±‚`a(Ù±‚`rconstrained_layoutÙ±‚aoa=Ù±‚bkcdTrueÙ±‚`a)Ù±‚`a
Ù±‚`caxsÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cfigÙ±‚aoa.Ù±‚`hsubplotsÙ±‚`a(Ù±‚bmia2Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`aNÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bmif100000Ù±‚`b  Ù±‚bc1x:# If N is large one can see improvement by using blitting.Ù±‚`a
Ù±‚`axÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`hlinspaceÙ±‚`a(Ù±‚bmia0Ù±‚`a,Ù±‚`a Ù±‚bmib10Ù±‚`a,Ù±‚`a Ù±‚`aNÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`iselectorsÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`a[Ù±‚`a]Ù±‚`a
Ù±‚akcforÙ±‚`a Ù±‚`baxÙ±‚`a,Ù±‚`a Ù±‚`nselector_classÙ±‚`a Ù±‚bowbinÙ±‚`a Ù±‚bnbczipÙ±‚`a(Ù±‚`caxsÙ±‚`a,Ù±‚`a Ù±‚`a[Ù±‚`qRectangleSelectorÙ±‚`a,Ù±‚`a Ù±‚`oEllipseSelectorÙ±‚`a]Ù±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`d    Ù±‚`baxÙ±‚aoa.Ù±‚`dplotÙ±‚`a(Ù±‚`axÙ±‚`a,Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`csinÙ±‚`a(Ù±‚bmia2Ù±‚aoa*Ù±‚`bnpÙ±‚aoa.Ù±‚`bpiÙ±‚aoa*Ù±‚`axÙ±‚`a)Ù±‚`a)Ù±‚`b  Ù±‚bc1p# plot somethingÙ±‚`a
Ù±‚`d    Ù±‚`baxÙ±‚aoa.Ù±‚`iset_titleÙ±‚`a(Ù±‚bsaafÙ±‚bs2a"Ù±‚bs2xClick and drag to draw a Ù±‚bsia{Ù±‚`nselector_classÙ±‚aoa.Ù±‚bvmh__name__Ù±‚bsia}Ù±‚bs2a.Ù±‚bs2a"Ù±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`iselectorsÙ±‚aoa.Ù±‚`fappendÙ±‚`a(Ù±‚`nselector_classÙ±‚`a(Ù±‚`a
Ù±‚`h        Ù±‚`baxÙ±‚`a,Ù±‚`a Ù±‚`oselect_callbackÙ±‚`a,Ù±‚`a
Ù±‚`h        Ù±‚`guseblitÙ±‚aoa=Ù±‚bkcdTrueÙ±‚`a,Ù±‚`a
Ù±‚`h        Ù±‚`fbuttonÙ±‚aoa=Ù±‚`a[Ù±‚bmia1Ù±‚`a,Ù±‚`a Ù±‚bmia3Ù±‚`a]Ù±‚`a,Ù±‚`b  Ù±‚bc1w# disable middle buttonÙ±‚`a
Ù±‚`h        Ù±‚`hminspanxÙ±‚aoa=Ù±‚bmia5Ù±‚`a,Ù±‚`a Ù±‚`hminspanyÙ±‚aoa=Ù±‚bmia5Ù±‚`a,Ù±‚`a
Ù±‚`h        Ù±‚`jspancoordsÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1fpixelsÙ±‚bs1a'Ù±‚`a,Ù±‚`a
Ù±‚`h        Ù±‚`kinteractiveÙ±‚aoa=Ù±‚bkcdTrueÙ±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`cfigÙ±‚aoa.Ù±‚`fcanvasÙ±‚aoa.Ù±‚`kmpl_connectÙ±‚`a(Ù±‚bs1a'Ù±‚bs1okey_press_eventÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`otoggle_selectorÙ±‚`a)Ù±‚`a
Ù±‚`caxsÙ±‚`a[Ù±‚bmia0Ù±‚`a]Ù±‚aoa.Ù±‚`iset_titleÙ±‚`a(Ù±‚bs2a"Ù±‚bs2fPress Ù±‚bs2a'Ù±‚bs2atÙ±‚bs2a'Ù±‚bs2x$ to toggle the selectors on and off.Ù±‚bseb\nÙ±‚bs2a"Ù±‚`a
Ù±‚`q                 Ù±‚aoa+Ù±‚`a Ù±‚`caxsÙ±‚`a[Ù±‚bmia0Ù±‚`a]Ù±‚aoa.Ù±‚`iget_titleÙ±‚`a(Ù±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`cpltÙ±‚aoa.Ù±‚`dshowÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚bc1xM#############################################################################Ù±‚`a
Ù±‚bc1a#Ù±‚`a
Ù±‚bc1x# .. admonition:: ReferencesÙ±‚`a
Ù±‚bc1a#Ù±‚`a
Ù±‚bc1xN#    The use of the following functions, methods, classes and modules is shownÙ±‚`a
Ù±‚bc1u#    in this example:Ù±‚`a
Ù±‚bc1a#Ù±‚`a
Ù±‚bc1x-#    - `matplotlib.widgets.RectangleSelector`Ù±‚`a
Ù±‚bc1x+#    - `matplotlib.widgets.EllipseSelector`Ù±‚`a
`dNoneö