Ù¯‚Ù´ƒ™ÀÙ±‚bsdxm"""
===========
Multi Image
===========

Make a set of images with a single colormap, norm, and colorbar.
"""Ù±‚`a
Ù±‚`a
Ù±‚bkndfromÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚`a Ù±‚bknfimportÙ±‚`a Ù±‚`fcolorsÙ±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnnfpyplotÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnncpltÙ±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„enumpyÙ „enumpyf1.22.3fmoduleenumpyfmoduleõÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnnbnpÙ±‚`a
Ù±‚`a
Ù±‚`bnpÙ±‚aoa.Ù±‚`frandomÙ±‚aoa.Ù±‚`dseedÙ±‚`a(Ù±‚bmih19680801Ù±‚`a)Ù±‚`a
Ù±‚`bNrÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bmia3Ù±‚`a
Ù±‚`bNcÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bmia2Ù±‚`a
Ù±‚`a
Ù±‚`cfigÙ±‚`a,Ù±‚`a Ù±‚`caxsÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cpltÙ±‚aoa.Ù±‚`hsubplotsÙ±‚`a(Ù±‚`bNrÙ±‚`a,Ù±‚`a Ù±‚`bNcÙ±‚`a)Ù±‚`a
Ù±‚`cfigÙ±‚aoa.Ù±‚`hsuptitleÙ±‚`a(Ù±‚bs1a'Ù±‚bs1oMultiple imagesÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`fimagesÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`a[Ù±‚`a]Ù±‚`a
Ù±‚akcforÙ±‚`a Ù±‚`aiÙ±‚`a Ù±‚bowbinÙ±‚`a Ù±‚bnberangeÙ±‚`a(Ù±‚`bNrÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`d    Ù±‚akcforÙ±‚`a Ù±‚`ajÙ±‚`a Ù±‚bowbinÙ±‚`a Ù±‚bnberangeÙ±‚`a(Ù±‚`bNcÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`h        Ù±‚bc1xC# Generate data with a range that varies from one plot to the next.Ù±‚`a
Ù±‚`h        Ù±‚`ddataÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`a(Ù±‚`a(Ù±‚bmia1Ù±‚`a Ù±‚aoa+Ù±‚`a Ù±‚`aiÙ±‚`a Ù±‚aoa+Ù±‚`a Ù±‚`ajÙ±‚`a)Ù±‚`a Ù±‚aoa/Ù±‚`a Ù±‚bmib10Ù±‚`a)Ù±‚`a Ù±‚aoa*Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`frandomÙ±‚aoa.Ù±‚`drandÙ±‚`a(Ù±‚bmib10Ù±‚`a,Ù±‚`a Ù±‚bmib20Ù±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚`fimagesÙ±‚aoa.Ù±‚`fappendÙ±‚`a(Ù±‚`caxsÙ±‚`a[Ù±‚`aiÙ±‚`a,Ù±‚`a Ù±‚`ajÙ±‚`a]Ù±‚aoa.Ù±‚`fimshowÙ±‚`a(Ù±‚`ddataÙ±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚`caxsÙ±‚`a[Ù±‚`aiÙ±‚`a,Ù±‚`a Ù±‚`ajÙ±‚`a]Ù±‚aoa.Ù±‚`klabel_outerÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚bc1xH# Find the min and max of all colors for use in setting the color scale.Ù±‚`a
Ù±‚`dvminÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bnbcminÙ±‚`a(Ù±‚`eimageÙ±‚aoa.Ù±‚`iget_arrayÙ±‚`a(Ù±‚`a)Ù±‚aoa.Ù±‚`cminÙ±‚`a(Ù±‚`a)Ù±‚`a Ù±‚akcforÙ±‚`a Ù±‚`eimageÙ±‚`a Ù±‚bowbinÙ±‚`a Ù±‚`fimagesÙ±‚`a)Ù±‚`a
Ù±‚`dvmaxÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bnbcmaxÙ±‚`a(Ù±‚`eimageÙ±‚aoa.Ù±‚`iget_arrayÙ±‚`a(Ù±‚`a)Ù±‚aoa.Ù±‚`cmaxÙ±‚`a(Ù±‚`a)Ù±‚`a Ù±‚akcforÙ±‚`a Ù±‚`eimageÙ±‚`a Ù±‚bowbinÙ±‚`a Ù±‚`fimagesÙ±‚`a)Ù±‚`a
Ù±‚`dnormÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`fcolorsÙ±‚aoa.Ù±‚`iNormalizeÙ±‚`a(Ù±‚`dvminÙ±‚aoa=Ù±‚`dvminÙ±‚`a,Ù±‚`a Ù±‚`dvmaxÙ±‚aoa=Ù±‚`dvmaxÙ±‚`a)Ù±‚`a
Ù±‚akcforÙ±‚`a Ù±‚`bimÙ±‚`a Ù±‚bowbinÙ±‚`a Ù±‚`fimagesÙ±‚`a:Ù±‚`a
Ù±‚`d    Ù±‚`bimÙ±‚aoa.Ù±‚`hset_normÙ±‚`a(Ù±‚`dnormÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`cfigÙ±‚aoa.Ù±‚`hcolorbarÙ±‚`a(Ù±‚`fimagesÙ±‚`a[Ù±‚bmia0Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`baxÙ±‚aoa=Ù±‚`caxsÙ±‚`a,Ù±‚`a Ù±‚`korientationÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1jhorizontalÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`hfractionÙ±‚aoa=Ù±‚bmfb.1Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚bc1xJ# Make images respond to changes in the norm of other images (e.g. via theÙ±‚`a
Ù±‚bc1xM# "edit axis, curves and images parameters" GUI on Qt), but be careful not toÙ±‚`a
Ù±‚bc1u# recurse infinitely!Ù±‚`a
Ù±‚akcdefÙ±‚`a Ù±‚bnffupdateÙ±‚`a(Ù±‚`mchanged_imageÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`d    Ù±‚akcforÙ±‚`a Ù±‚`bimÙ±‚`a Ù±‚bowbinÙ±‚`a Ù±‚`fimagesÙ±‚`a:Ù±‚`a
Ù±‚`h        Ù±‚akbifÙ±‚`a Ù±‚`a(Ù±‚`mchanged_imageÙ±‚aoa.Ù±‚`hget_cmapÙ±‚`a(Ù±‚`a)Ù±‚`a Ù±‚aob!=Ù±‚`a Ù±‚`bimÙ±‚aoa.Ù±‚`hget_cmapÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`p                Ù±‚bowborÙ±‚`a Ù±‚`mchanged_imageÙ±‚aoa.Ù±‚`hget_climÙ±‚`a(Ù±‚`a)Ù±‚`a Ù±‚aob!=Ù±‚`a Ù±‚`bimÙ±‚aoa.Ù±‚`hget_climÙ±‚`a(Ù±‚`a)Ù±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`l            Ù±‚`bimÙ±‚aoa.Ù±‚`hset_cmapÙ±‚`a(Ù±‚`mchanged_imageÙ±‚aoa.Ù±‚`hget_cmapÙ±‚`a(Ù±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`l            Ù±‚`bimÙ±‚aoa.Ù±‚`hset_climÙ±‚`a(Ù±‚`mchanged_imageÙ±‚aoa.Ù±‚`hget_climÙ±‚`a(Ù±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚akcforÙ±‚`a Ù±‚`bimÙ±‚`a Ù±‚bowbinÙ±‚`a Ù±‚`fimagesÙ±‚`a:Ù±‚`a
Ù±‚`d    Ù±‚`bimÙ±‚aoa.Ù±‚`icallbacksÙ±‚aoa.Ù±‚`gconnectÙ±‚`a(Ù±‚bs1a'Ù±‚bs1gchangedÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`fupdateÙ±‚`a)Ù±‚`a
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
Ù±‚bc1xA#    - `matplotlib.axes.Axes.imshow` / `matplotlib.pyplot.imshow`Ù±‚`a
Ù±‚bc1xI#    - `matplotlib.figure.Figure.colorbar` / `matplotlib.pyplot.colorbar`Ù±‚`a
Ù±‚bc1x$#    - `matplotlib.colors.Normalize`Ù±‚`a
Ù±‚bc1x.#    - `matplotlib.cm.ScalarMappable.set_cmap`Ù±‚`a
Ù±‚bc1x.#    - `matplotlib.cm.ScalarMappable.set_norm`Ù±‚`a
Ù±‚bc1x.#    - `matplotlib.cm.ScalarMappable.set_clim`Ù±‚`a
Ù±‚bc1x2#    - `matplotlib.cbook.CallbackRegistry.connect`Ù±‚`a
`dNoneö