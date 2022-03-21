Ù¯‚Ù´ƒ™™Ù±‚bsdxÓ"""
============
Ellipse Demo
============

Draw many ellipses. Here individual ellipses are drawn. Compare this
to the :doc:`Ellipse collection example
</gallery/shapes_and_collections/ellipse_collection>`.
"""Ù±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnnfpyplotÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnncpltÙ±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„enumpyÙ „enumpyf1.22.3fmoduleenumpyfmoduleõÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnnbnpÙ±‚`a
Ù±‚bkndfromÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnngpatchesÙ±‚`a Ù±‚bknfimportÙ±‚`a Ù±‚`gEllipseÙ±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚bc1x)# Fixing random state for reproducibilityÙ±‚`a
Ù±‚`bnpÙ±‚aoa.Ù±‚`frandomÙ±‚aoa.Ù±‚`dseedÙ±‚`a(Ù±‚bmih19680801Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`cNUMÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bmic250Ù±‚`a
Ù±‚`a
Ù±‚`dellsÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`a[Ù±‚`gEllipseÙ±‚`a(Ù±‚`bxyÙ±‚aoa=Ù±‚`bnpÙ±‚aoa.Ù±‚`frandomÙ±‚aoa.Ù±‚`drandÙ±‚`a(Ù±‚bmia2Ù±‚`a)Ù±‚`a Ù±‚aoa*Ù±‚`a Ù±‚bmib10Ù±‚`a,Ù±‚`a
Ù±‚`p                Ù±‚`ewidthÙ±‚aoa=Ù±‚`bnpÙ±‚aoa.Ù±‚`frandomÙ±‚aoa.Ù±‚`drandÙ±‚`a(Ù±‚`a)Ù±‚`a,Ù±‚`a Ù±‚`fheightÙ±‚aoa=Ù±‚`bnpÙ±‚aoa.Ù±‚`frandomÙ±‚aoa.Ù±‚`drandÙ±‚`a(Ù±‚`a)Ù±‚`a,Ù±‚`a
Ù±‚`p                Ù±‚`eangleÙ±‚aoa=Ù±‚`bnpÙ±‚aoa.Ù±‚`frandomÙ±‚aoa.Ù±‚`drandÙ±‚`a(Ù±‚`a)Ù±‚`a Ù±‚aoa*Ù±‚`a Ù±‚bmic360Ù±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚akcforÙ±‚`a Ù±‚`aiÙ±‚`a Ù±‚bowbinÙ±‚`a Ù±‚bnberangeÙ±‚`a(Ù±‚`cNUMÙ±‚`a)Ù±‚`a]Ù±‚`a
Ù±‚`a
Ù±‚`cfigÙ±‚`a,Ù±‚`a Ù±‚`baxÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cpltÙ±‚aoa.Ù±‚`hsubplotsÙ±‚`a(Ù±‚`jsubplot_kwÙ±‚aoa=Ù±‚`a{Ù±‚bs1a'Ù±‚bs1faspectÙ±‚bs1a'Ù±‚`a:Ù±‚`a Ù±‚bs1a'Ù±‚bs1eequalÙ±‚bs1a'Ù±‚`a}Ù±‚`a)Ù±‚`a
Ù±‚akcforÙ±‚`a Ù±‚`aeÙ±‚`a Ù±‚bowbinÙ±‚`a Ù±‚`dellsÙ±‚`a:Ù±‚`a
Ù±‚`d    Ù±‚`baxÙ±‚aoa.Ù±‚`jadd_artistÙ±‚`a(Ù±‚`aeÙ±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`aeÙ±‚aoa.Ù±‚`lset_clip_boxÙ±‚`a(Ù±‚`baxÙ±‚aoa.Ù±‚`dbboxÙ±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`aeÙ±‚aoa.Ù±‚`iset_alphaÙ±‚`a(Ù±‚`bnpÙ±‚aoa.Ù±‚`frandomÙ±‚aoa.Ù±‚`drandÙ±‚`a(Ù±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`aeÙ±‚aoa.Ù±‚`mset_facecolorÙ±‚`a(Ù±‚`bnpÙ±‚aoa.Ù±‚`frandomÙ±‚aoa.Ù±‚`drandÙ±‚`a(Ù±‚bmia3Ù±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`hset_xlimÙ±‚`a(Ù±‚bmia0Ù±‚`a,Ù±‚`a Ù±‚bmib10Ù±‚`a)Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`hset_ylimÙ±‚`a(Ù±‚bmia0Ù±‚`a,Ù±‚`a Ù±‚bmib10Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`cpltÙ±‚aoa.Ù±‚`dshowÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚bc1xM#############################################################################Ù±‚`a
Ù±‚bc1q# ===============Ù±‚`a
Ù±‚bc1q# Ellipse RotatedÙ±‚`a
Ù±‚bc1q# ===============Ù±‚`a
Ù±‚bc1a#Ù±‚`a
Ù±‚bc1x+# Draw many ellipses with different angles.Ù±‚`a
Ù±‚bc1a#Ù±‚`a
Ù±‚`a
Ù±‚`jangle_stepÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bmib45Ù±‚`b  Ù±‚bc1i# degreesÙ±‚`a
Ù±‚`fanglesÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`farangeÙ±‚`a(Ù±‚bmia0Ù±‚`a,Ù±‚`a Ù±‚bmic180Ù±‚`a,Ù±‚`a Ù±‚`jangle_stepÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`cfigÙ±‚`a,Ù±‚`a Ù±‚`baxÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cpltÙ±‚aoa.Ù±‚`hsubplotsÙ±‚`a(Ù±‚`jsubplot_kwÙ±‚aoa=Ù±‚`a{Ù±‚bs1a'Ù±‚bs1faspectÙ±‚bs1a'Ù±‚`a:Ù±‚`a Ù±‚bs1a'Ù±‚bs1eequalÙ±‚bs1a'Ù±‚`a}Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚akcforÙ±‚`a Ù±‚`eangleÙ±‚`a Ù±‚bowbinÙ±‚`a Ù±‚`fanglesÙ±‚`a:Ù±‚`a
Ù±‚`d    Ù±‚`gellipseÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`gEllipseÙ±‚`a(Ù±‚`a(Ù±‚bmia0Ù±‚`a,Ù±‚`a Ù±‚bmia0Ù±‚`a)Ù±‚`a,Ù±‚`a Ù±‚bmia4Ù±‚`a,Ù±‚`a Ù±‚bmia2Ù±‚`a,Ù±‚`a Ù±‚`eangleÙ±‚aoa=Ù±‚`eangleÙ±‚`a,Ù±‚`a Ù±‚`ealphaÙ±‚aoa=Ù±‚bmfc0.1Ù±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`baxÙ±‚aoa.Ù±‚`jadd_artistÙ±‚`a(Ù±‚`gellipseÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`hset_xlimÙ±‚`a(Ù±‚aoa-Ù±‚bmfc2.2Ù±‚`a,Ù±‚`a Ù±‚bmfc2.2Ù±‚`a)Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`hset_ylimÙ±‚`a(Ù±‚aoa-Ù±‚bmfc2.2Ù±‚`a,Ù±‚`a Ù±‚bmfc2.2Ù±‚`a)Ù±‚`a
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
Ù±‚bc1x#    - `matplotlib.patches`Ù±‚`a
Ù±‚bc1x##    - `matplotlib.patches.Ellipse`Ù±‚`a
Ù±‚bc1x(#    - `matplotlib.axes.Axes.add_artist`Ù±‚`a
Ù±‚bc1x.#    - `matplotlib.artist.Artist.set_clip_box`Ù±‚`a
Ù±‚bc1x+#    - `matplotlib.artist.Artist.set_alpha`Ù±‚`a
Ù±‚bc1x/#    - `matplotlib.patches.Patch.set_facecolor`Ù±‚`a
`dNoneö