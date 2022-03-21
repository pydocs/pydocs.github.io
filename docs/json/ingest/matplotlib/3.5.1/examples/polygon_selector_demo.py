Ù¯‚Ù´ƒ™fÙ±‚bsdxx"""
================
Polygon Selector
================

Shows how one can select indices of a polygon interactively.
"""Ù±‚`a
Ù±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„enumpyÙ „enumpyf1.22.3fmoduleenumpyfmoduleõÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnnbnpÙ±‚`a
Ù±‚`a
Ù±‚bkndfromÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnngwidgetsÙ±‚`a Ù±‚bknfimportÙ±‚`a Ù±‚`oPolygonSelectorÙ±‚`a
Ù±‚bkndfromÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnndpathÙ±‚`a Ù±‚bknfimportÙ±‚`a Ù±‚`dPathÙ±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚akeclassÙ±‚`a Ù±‚bnctSelectFromCollectionÙ±‚`a:Ù±‚`a
Ù±‚`d    Ù±‚bsdy0"""
    Select indices from a matplotlib collection using `PolygonSelector`.

    Selected indices are saved in the `ind` attribute. This tool fades out the
    points that are not part of the selection (i.e., reduces their alpha
    values). If your collection has alpha < 1, this tool will permanently
    alter the alpha values.

    Note that this tool selects collection objects based on their *origins*
    (i.e., `offsets`).

    Parameters
    ----------
    ax : `~matplotlib.axes.Axes`
        Axes to interact with.
    collection : `matplotlib.collections.Collection` subclass
        Collection you want to select from.
    alpha_other : 0 <= float <= 1
        To highlight a selection, this tool sets all selected points to an
        alpha value of 1 and non-selected points to *alpha_other*.
    """Ù±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚akcdefÙ±‚`a Ù±‚bfmh__init__Ù±‚`a(Ù±‚bbpdselfÙ±‚`a,Ù±‚`a Ù±‚`baxÙ±‚`a,Ù±‚`a Ù±‚`jcollectionÙ±‚`a,Ù±‚`a Ù±‚`kalpha_otherÙ±‚aoa=Ù±‚bmfc0.3Ù±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`fcanvasÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`baxÙ±‚aoa.Ù±‚`ffigureÙ±‚aoa.Ù±‚`fcanvasÙ±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`jcollectionÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`jcollectionÙ±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`kalpha_otherÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`kalpha_otherÙ±‚`a
Ù±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`cxysÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`jcollectionÙ±‚aoa.Ù±‚`kget_offsetsÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`dNptsÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bnbclenÙ±‚`a(Ù±‚bbpdselfÙ±‚aoa.Ù±‚`cxysÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`h        Ù±‚bc1x5# Ensure that we have separate colors for each objectÙ±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`bfcÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`jcollectionÙ±‚aoa.Ù±‚`nget_facecolorsÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚akbifÙ±‚`a Ù±‚bnbclenÙ±‚`a(Ù±‚bbpdselfÙ±‚aoa.Ù±‚`bfcÙ±‚`a)Ù±‚`a Ù±‚aob==Ù±‚`a Ù±‚bmia0Ù±‚`a:Ù±‚`a
Ù±‚`l            Ù±‚akeraiseÙ±‚`a Ù±‚bnejValueErrorÙ±‚`a(Ù±‚bs1a'Ù±‚bs1x Collection must have a facecolorÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚akdelifÙ±‚`a Ù±‚bnbclenÙ±‚`a(Ù±‚bbpdselfÙ±‚aoa.Ù±‚`bfcÙ±‚`a)Ù±‚`a Ù±‚aob==Ù±‚`a Ù±‚bmia1Ù±‚`a:Ù±‚`a
Ù±‚`l            Ù±‚bbpdselfÙ±‚aoa.Ù±‚`bfcÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`dtileÙ±‚`a(Ù±‚bbpdselfÙ±‚aoa.Ù±‚`bfcÙ±‚`a,Ù±‚`a Ù±‚`a(Ù±‚bbpdselfÙ±‚aoa.Ù±‚`dNptsÙ±‚`a,Ù±‚`a Ù±‚bmia1Ù±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`dpolyÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`oPolygonSelectorÙ±‚`a(Ù±‚`baxÙ±‚`a,Ù±‚`a Ù±‚bbpdselfÙ±‚aoa.Ù±‚`honselectÙ±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`cindÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`a[Ù±‚`a]Ù±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚akcdefÙ±‚`a Ù±‚bnfhonselectÙ±‚`a(Ù±‚bbpdselfÙ±‚`a,Ù±‚`a Ù±‚`evertsÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`h        Ù±‚`dpathÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`dPathÙ±‚`a(Ù±‚`evertsÙ±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`cindÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`gnonzeroÙ±‚`a(Ù±‚`dpathÙ±‚aoa.Ù±‚`ocontains_pointsÙ±‚`a(Ù±‚bbpdselfÙ±‚aoa.Ù±‚`cxysÙ±‚`a)Ù±‚`a)Ù±‚`a[Ù±‚bmia0Ù±‚`a]Ù±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`bfcÙ±‚`a[Ù±‚`a:Ù±‚`a,Ù±‚`a Ù±‚aoa-Ù±‚bmia1Ù±‚`a]Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bbpdselfÙ±‚aoa.Ù±‚`kalpha_otherÙ±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`bfcÙ±‚`a[Ù±‚bbpdselfÙ±‚aoa.Ù±‚`cindÙ±‚`a,Ù±‚`a Ù±‚aoa-Ù±‚bmia1Ù±‚`a]Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bmia1Ù±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`jcollectionÙ±‚aoa.Ù±‚`nset_facecolorsÙ±‚`a(Ù±‚bbpdselfÙ±‚aoa.Ù±‚`bfcÙ±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`fcanvasÙ±‚aoa.Ù±‚`idraw_idleÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚akcdefÙ±‚`a Ù±‚bnfjdisconnectÙ±‚`a(Ù±‚bbpdselfÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`dpolyÙ±‚aoa.Ù±‚`qdisconnect_eventsÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`bfcÙ±‚`a[Ù±‚`a:Ù±‚`a,Ù±‚`a Ù±‚aoa-Ù±‚bmia1Ù±‚`a]Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bmia1Ù±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`jcollectionÙ±‚aoa.Ù±‚`nset_facecolorsÙ±‚`a(Ù±‚bbpdselfÙ±‚aoa.Ù±‚`bfcÙ±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`fcanvasÙ±‚aoa.Ù±‚`idraw_idleÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚akbifÙ±‚`a Ù±‚bvmh__name__Ù±‚`a Ù±‚aob==Ù±‚`a Ù±‚bs1a'Ù±‚bs1h__main__Ù±‚bs1a'Ù±‚`a:Ù±‚`a
Ù±‚`d    Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnnfpyplotÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnncpltÙ±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚`cfigÙ±‚`a,Ù±‚`a Ù±‚`baxÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cpltÙ±‚aoa.Ù±‚`hsubplotsÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`igrid_sizeÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bmia5Ù±‚`a
Ù±‚`d    Ù±‚`fgrid_xÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`dtileÙ±‚`a(Ù±‚`bnpÙ±‚aoa.Ù±‚`farangeÙ±‚`a(Ù±‚`igrid_sizeÙ±‚`a)Ù±‚`a,Ù±‚`a Ù±‚`igrid_sizeÙ±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`fgrid_yÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`frepeatÙ±‚`a(Ù±‚`bnpÙ±‚aoa.Ù±‚`farangeÙ±‚`a(Ù±‚`igrid_sizeÙ±‚`a)Ù±‚`a,Ù±‚`a Ù±‚`igrid_sizeÙ±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`cptsÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`baxÙ±‚aoa.Ù±‚`gscatterÙ±‚`a(Ù±‚`fgrid_xÙ±‚`a,Ù±‚`a Ù±‚`fgrid_yÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚`hselectorÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`tSelectFromCollectionÙ±‚`a(Ù±‚`baxÙ±‚`a,Ù±‚`a Ù±‚`cptsÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚bnbeprintÙ±‚`a(Ù±‚bs2a"Ù±‚bs2x?Select points in the figure by enclosing them within a polygon.Ù±‚bs2a"Ù±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚bnbeprintÙ±‚`a(Ù±‚bs2a"Ù±‚bs2jPress the Ù±‚bs2a'Ù±‚bs2cescÙ±‚bs2a'Ù±‚bs2x key to start a new polygon.Ù±‚bs2a"Ù±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚bnbeprintÙ±‚`a(Ù±‚bs2a"Ù±‚bs2pTry holding the Ù±‚bs2a'Ù±‚bs2eshiftÙ±‚bs2a'Ù±‚bs2x! key to move all of the vertices.Ù±‚bs2a"Ù±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚bnbeprintÙ±‚`a(Ù±‚bs2a"Ù±‚bs2pTry holding the Ù±‚bs2a'Ù±‚bs2dctrlÙ±‚bs2a'Ù±‚bs2x key to move a single vertex.Ù±‚bs2a"Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚`cpltÙ±‚aoa.Ù±‚`dshowÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚`hselectorÙ±‚aoa.Ù±‚`jdisconnectÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚bc1xE# After figure is closed print the coordinates of the selected pointsÙ±‚`a
Ù±‚`d    Ù±‚bnbeprintÙ±‚`a(Ù±‚bs1a'Ù±‚bseb\nÙ±‚bs1pSelected points:Ù±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚bnbeprintÙ±‚`a(Ù±‚`hselectorÙ±‚aoa.Ù±‚`cxysÙ±‚`a[Ù±‚`hselectorÙ±‚aoa.Ù±‚`cindÙ±‚`a]Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚bc1xM#############################################################################Ù±‚`a
Ù±‚bc1a#Ù±‚`a
Ù±‚bc1x# .. admonition:: ReferencesÙ±‚`a
Ù±‚bc1a#Ù±‚`a
Ù±‚bc1xN#    The use of the following functions, methods, classes and modules is shownÙ±‚`a
Ù±‚bc1u#    in this example:Ù±‚`a
Ù±‚bc1a#Ù±‚`a
Ù±‚bc1x+#    - `matplotlib.widgets.PolygonSelector`Ù±‚`a
Ù±‚bc1x#    - `matplotlib.path.Path`Ù±‚`a
`dNoneö