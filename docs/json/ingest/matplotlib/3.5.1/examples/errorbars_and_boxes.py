Ù¯‚Ù´ƒ™ªÙ±‚bsdy<"""
====================================================
Creating boxes from error bars using PatchCollection
====================================================

In this example, we snazz up a pretty standard error bar plot by adding
a rectangle patch defined by the limits of the bars in both the x- and
y- directions. To do this, we have to write our own custom function
called ``make_error_boxes``. Close inspection of this function will
reveal the preferred pattern in writing functions for matplotlib:

  1. an `~.axes.Axes` object is passed directly to the function
  2. the function operates on the ``Axes`` methods directly, not through
     the ``pyplot`` interface
  3. plotting keyword arguments that could be abbreviated are spelled out for
     better code readability in the future (for example we use *facecolor*
     instead of *fc*)
  4. the artists returned by the ``Axes`` plotting methods are then
     returned by the function so that, if desired, their styles
     can be modified later outside of the function (they are not
     modified in this example).
"""Ù±‚`a
Ù±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„enumpyÙ „enumpyf1.22.3fmoduleenumpyfmoduleõÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnnbnpÙ±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnnfpyplotÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnncpltÙ±‚`a
Ù±‚bkndfromÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnnkcollectionsÙ±‚`a Ù±‚bknfimportÙ±‚`a Ù±‚`oPatchCollectionÙ±‚`a
Ù±‚bkndfromÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnngpatchesÙ±‚`a Ù±‚bknfimportÙ±‚`a Ù±‚`iRectangleÙ±‚`a
Ù±‚`a
Ù±‚bc1w# Number of data pointsÙ±‚`a
Ù±‚`anÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bmia5Ù±‚`a
Ù±‚`a
Ù±‚bc1l# Dummy dataÙ±‚`a
Ù±‚`bnpÙ±‚aoa.Ù±‚`frandomÙ±‚aoa.Ù±‚`dseedÙ±‚`a(Ù±‚bmih19680801Ù±‚`a)Ù±‚`a
Ù±‚`axÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`farangeÙ±‚`a(Ù±‚bmia0Ù±‚`a,Ù±‚`a Ù±‚`anÙ±‚`a,Ù±‚`a Ù±‚bmia1Ù±‚`a)Ù±‚`a
Ù±‚`ayÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`frandomÙ±‚aoa.Ù±‚`drandÙ±‚`a(Ù±‚`anÙ±‚`a)Ù±‚`a Ù±‚aoa*Ù±‚`a Ù±‚bmfb5.Ù±‚`a
Ù±‚`a
Ù±‚bc1x # Dummy errors (above and below)Ù±‚`a
Ù±‚`dxerrÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`frandomÙ±‚aoa.Ù±‚`drandÙ±‚`a(Ù±‚bmia2Ù±‚`a,Ù±‚`a Ù±‚`anÙ±‚`a)Ù±‚`a Ù±‚aoa+Ù±‚`a Ù±‚bmfc0.1Ù±‚`a
Ù±‚`dyerrÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`frandomÙ±‚aoa.Ù±‚`drandÙ±‚`a(Ù±‚bmia2Ù±‚`a,Ù±‚`a Ù±‚`anÙ±‚`a)Ù±‚`a Ù±‚aoa+Ù±‚`a Ù±‚bmfc0.2Ù±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚akcdefÙ±‚`a Ù±‚bnfpmake_error_boxesÙ±‚`a(Ù±‚`baxÙ±‚`a,Ù±‚`a Ù±‚`exdataÙ±‚`a,Ù±‚`a Ù±‚`eydataÙ±‚`a,Ù±‚`a Ù±‚`fxerrorÙ±‚`a,Ù±‚`a Ù±‚`fyerrorÙ±‚`a,Ù±‚`a Ù±‚`ifacecolorÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1arÙ±‚bs1a'Ù±‚`a,Ù±‚`a
Ù±‚`u                     Ù±‚`iedgecolorÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1dnoneÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`ealphaÙ±‚aoa=Ù±‚bmfc0.5Ù±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚bc1x=# Loop over data points; create box from errors at each pointÙ±‚`a
Ù±‚`d    Ù±‚`jerrorboxesÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`a[Ù±‚`iRectangleÙ±‚`a(Ù±‚`a(Ù±‚`axÙ±‚`a Ù±‚aoa-Ù±‚`a Ù±‚`bxeÙ±‚`a[Ù±‚bmia0Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`ayÙ±‚`a Ù±‚aoa-Ù±‚`a Ù±‚`byeÙ±‚`a[Ù±‚bmia0Ù±‚`a]Ù±‚`a)Ù±‚`a,Ù±‚`a Ù±‚`bxeÙ±‚aoa.Ù±‚`csumÙ±‚`a(Ù±‚`a)Ù±‚`a,Ù±‚`a Ù±‚`byeÙ±‚aoa.Ù±‚`csumÙ±‚`a(Ù±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`r                  Ù±‚akcforÙ±‚`a Ù±‚`axÙ±‚`a,Ù±‚`a Ù±‚`ayÙ±‚`a,Ù±‚`a Ù±‚`bxeÙ±‚`a,Ù±‚`a Ù±‚`byeÙ±‚`a Ù±‚bowbinÙ±‚`a Ù±‚bnbczipÙ±‚`a(Ù±‚`exdataÙ±‚`a,Ù±‚`a Ù±‚`eydataÙ±‚`a,Ù±‚`a Ù±‚`fxerrorÙ±‚aoa.Ù±‚`aTÙ±‚`a,Ù±‚`a Ù±‚`fyerrorÙ±‚aoa.Ù±‚`aTÙ±‚`a)Ù±‚`a]Ù±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚bc1x5# Create patch collection with specified colour/alphaÙ±‚`a
Ù±‚`d    Ù±‚`bpcÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`oPatchCollectionÙ±‚`a(Ù±‚`jerrorboxesÙ±‚`a,Ù±‚`a Ù±‚`ifacecolorÙ±‚aoa=Ù±‚`ifacecolorÙ±‚`a,Ù±‚`a Ù±‚`ealphaÙ±‚aoa=Ù±‚`ealphaÙ±‚`a,Ù±‚`a
Ù±‚`x                         Ù±‚`iedgecolorÙ±‚aoa=Ù±‚`iedgecolorÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚bc1x# Add collection to axesÙ±‚`a
Ù±‚`d    Ù±‚`baxÙ±‚aoa.Ù±‚`nadd_collectionÙ±‚`a(Ù±‚`bpcÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚bc1p# Plot errorbarsÙ±‚`a
Ù±‚`d    Ù±‚`gartistsÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`baxÙ±‚aoa.Ù±‚`herrorbarÙ±‚`a(Ù±‚`exdataÙ±‚`a,Ù±‚`a Ù±‚`eydataÙ±‚`a,Ù±‚`a Ù±‚`dxerrÙ±‚aoa=Ù±‚`fxerrorÙ±‚`a,Ù±‚`a Ù±‚`dyerrÙ±‚aoa=Ù±‚`fyerrorÙ±‚`a,Ù±‚`a
Ù±‚`x                          Ù±‚`cfmtÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1dnoneÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`fecolorÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1akÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚akfreturnÙ±‚`a Ù±‚`gartistsÙ±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚bc1x# Create figure and axesÙ±‚`a
Ù±‚`cfigÙ±‚`a,Ù±‚`a Ù±‚`baxÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cpltÙ±‚aoa.Ù±‚`hsubplotsÙ±‚`a(Ù±‚bmia1Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚bc1x%# Call function to create error boxesÙ±‚`a
Ù±‚`a_Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`pmake_error_boxesÙ±‚`a(Ù±‚`baxÙ±‚`a,Ù±‚`a Ù±‚`axÙ±‚`a,Ù±‚`a Ù±‚`ayÙ±‚`a,Ù±‚`a Ù±‚`dxerrÙ±‚`a,Ù±‚`a Ù±‚`dyerrÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`cpltÙ±‚aoa.Ù±‚`dshowÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚bc1xM#############################################################################Ù±‚`a
Ù±‚bc1a#Ù±‚`a
Ù±‚bc1x# .. admonition:: ReferencesÙ±‚`a
Ù±‚bc1a#Ù±‚`a
Ù±‚bc1xN#    The use of the following functions, methods, classes and modules is shownÙ±‚`a
Ù±‚bc1u#    in this example:Ù±‚`a
Ù±‚bc1a#Ù±‚`a
Ù±‚bc1xE#    - `matplotlib.axes.Axes.errorbar` / `matplotlib.pyplot.errorbar`Ù±‚`a
Ù±‚bc1x,#    - `matplotlib.axes.Axes.add_collection`Ù±‚`a
Ù±‚bc1x/#    - `matplotlib.collections.PatchCollection`Ù±‚`a
`dNoneö