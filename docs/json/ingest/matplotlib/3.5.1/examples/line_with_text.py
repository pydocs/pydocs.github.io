Ù¯‚Ù´ƒ™	Ù±‚bsdxÎ"""
=======================
Artist within an artist
=======================

Override basic methods so an artist can contain another
artist.  In this case, the line contains a Text instance to label it.
"""Ù±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„enumpyÙ „enumpyf1.22.3fmoduleenumpyfmoduleõÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnnbnpÙ±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnnfpyplotÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnncpltÙ±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnnelinesÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnnelinesÙ±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnnjtransformsÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnnkmtransformsÙ±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnndtextÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnnemtextÙ±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚akeclassÙ±‚`a Ù±‚bncfMyLineÙ±‚`a(Ù±‚`elinesÙ±‚aoa.Ù±‚`fLine2DÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`d    Ù±‚akcdefÙ±‚`a Ù±‚bfmh__init__Ù±‚`a(Ù±‚bbpdselfÙ±‚`a,Ù±‚`a Ù±‚aoa*Ù±‚`dargsÙ±‚`a,Ù±‚`a Ù±‚aoa*Ù±‚aoa*Ù±‚`fkwargsÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`h        Ù±‚bc1x5# we'll update the position when the line data is setÙ±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`dtextÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`emtextÙ±‚aoa.Ù±‚`dTextÙ±‚`a(Ù±‚bmia0Ù±‚`a,Ù±‚`a Ù±‚bmia0Ù±‚`a,Ù±‚`a Ù±‚bs1a'Ù±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚bnbesuperÙ±‚`a(Ù±‚`a)Ù±‚aoa.Ù±‚bfmh__init__Ù±‚`a(Ù±‚aoa*Ù±‚`dargsÙ±‚`a,Ù±‚`a Ù±‚aoa*Ù±‚aoa*Ù±‚`fkwargsÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`h        Ù±‚bc1x:# we can't access the label attr until *after* the line isÙ±‚`a
Ù±‚`h        Ù±‚bc1k# initiatedÙ±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`dtextÙ±‚aoa.Ù±‚`hset_textÙ±‚`a(Ù±‚bbpdselfÙ±‚aoa.Ù±‚`iget_labelÙ±‚`a(Ù±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚akcdefÙ±‚`a Ù±‚bnfjset_figureÙ±‚`a(Ù±‚bbpdselfÙ±‚`a,Ù±‚`a Ù±‚`ffigureÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`dtextÙ±‚aoa.Ù±‚`jset_figureÙ±‚`a(Ù±‚`ffigureÙ±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚bnbesuperÙ±‚`a(Ù±‚`a)Ù±‚aoa.Ù±‚`jset_figureÙ±‚`a(Ù±‚`ffigureÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚akcdefÙ±‚`a Ù±‚bnfhset_axesÙ±‚`a(Ù±‚bbpdselfÙ±‚`a,Ù±‚`a Ù±‚`daxesÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`dtextÙ±‚aoa.Ù±‚`hset_axesÙ±‚`a(Ù±‚`daxesÙ±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚bnbesuperÙ±‚`a(Ù±‚`a)Ù±‚aoa.Ù±‚`hset_axesÙ±‚`a(Ù±‚`daxesÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚akcdefÙ±‚`a Ù±‚bnfmset_transformÙ±‚`a(Ù±‚bbpdselfÙ±‚`a,Ù±‚`a Ù±‚`itransformÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`h        Ù±‚bc1p# 2 pixel offsetÙ±‚`a
Ù±‚`h        Ù±‚`itexttransÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`itransformÙ±‚`a Ù±‚aoa+Ù±‚`a Ù±‚`kmtransformsÙ±‚aoa.Ù±‚`hAffine2DÙ±‚`a(Ù±‚`a)Ù±‚aoa.Ù±‚`itranslateÙ±‚`a(Ù±‚bmia2Ù±‚`a,Ù±‚`a Ù±‚bmia2Ù±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`dtextÙ±‚aoa.Ù±‚`mset_transformÙ±‚`a(Ù±‚`itexttransÙ±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚bnbesuperÙ±‚`a(Ù±‚`a)Ù±‚aoa.Ù±‚`mset_transformÙ±‚`a(Ù±‚`itransformÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚akcdefÙ±‚`a Ù±‚bnfhset_dataÙ±‚`a(Ù±‚bbpdselfÙ±‚`a,Ù±‚`a Ù±‚`axÙ±‚`a,Ù±‚`a Ù±‚`ayÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`h        Ù±‚akbifÙ±‚`a Ù±‚bnbclenÙ±‚`a(Ù±‚`axÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`l            Ù±‚bbpdselfÙ±‚aoa.Ù±‚`dtextÙ±‚aoa.Ù±‚`lset_positionÙ±‚`a(Ù±‚`a(Ù±‚`axÙ±‚`a[Ù±‚aoa-Ù±‚bmia1Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`ayÙ±‚`a[Ù±‚aoa-Ù±‚bmia1Ù±‚`a]Ù±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`h        Ù±‚bnbesuperÙ±‚`a(Ù±‚`a)Ù±‚aoa.Ù±‚`hset_dataÙ±‚`a(Ù±‚`axÙ±‚`a,Ù±‚`a Ù±‚`ayÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚akcdefÙ±‚`a Ù±‚bnfddrawÙ±‚`a(Ù±‚bbpdselfÙ±‚`a,Ù±‚`a Ù±‚`hrendererÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`h        Ù±‚bc1x:# draw my label at the end of the line with 2 pixel offsetÙ±‚`a
Ù±‚`h        Ù±‚bnbesuperÙ±‚`a(Ù±‚`a)Ù±‚aoa.Ù±‚`ddrawÙ±‚`a(Ù±‚`hrendererÙ±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`dtextÙ±‚aoa.Ù±‚`ddrawÙ±‚`a(Ù±‚`hrendererÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚bc1x)# Fixing random state for reproducibilityÙ±‚`a
Ù±‚`bnpÙ±‚aoa.Ù±‚`frandomÙ±‚aoa.Ù±‚`dseedÙ±‚`a(Ù±‚bmih19680801Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚`cfigÙ±‚`a,Ù±‚`a Ù±‚`baxÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cpltÙ±‚aoa.Ù±‚`hsubplotsÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`axÙ±‚`a,Ù±‚`a Ù±‚`ayÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`frandomÙ±‚aoa.Ù±‚`drandÙ±‚`a(Ù±‚bmia2Ù±‚`a,Ù±‚`a Ù±‚bmib20Ù±‚`a)Ù±‚`a
Ù±‚`dlineÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`fMyLineÙ±‚`a(Ù±‚`axÙ±‚`a,Ù±‚`a Ù±‚`ayÙ±‚`a,Ù±‚`a Ù±‚`cmfcÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1credÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`bmsÙ±‚aoa=Ù±‚bmib12Ù±‚`a,Ù±‚`a Ù±‚`elabelÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1jline labelÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`dlineÙ±‚aoa.Ù±‚`dtextÙ±‚aoa.Ù±‚`iset_colorÙ±‚`a(Ù±‚bs1a'Ù±‚bs1credÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`dlineÙ±‚aoa.Ù±‚`dtextÙ±‚aoa.Ù±‚`lset_fontsizeÙ±‚`a(Ù±‚bmib16Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`hadd_lineÙ±‚`a(Ù±‚`dlineÙ±‚`a)Ù±‚`a
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
Ù±‚bc1x#    - `matplotlib.lines`Ù±‚`a
Ù±‚bc1x #    - `matplotlib.lines.Line2D`Ù±‚`a
Ù±‚bc1x)#    - `matplotlib.lines.Line2D.set_data`Ù±‚`a
Ù±‚bc1x#    - `matplotlib.artist`Ù±‚`a
Ù±‚bc1x!#    - `matplotlib.artist.Artist`Ù±‚`a
Ù±‚bc1x&#    - `matplotlib.artist.Artist.draw`Ù±‚`a
Ù±‚bc1x/#    - `matplotlib.artist.Artist.set_transform`Ù±‚`a
Ù±‚bc1x#    - `matplotlib.text`Ù±‚`a
Ù±‚bc1x#    - `matplotlib.text.Text`Ù±‚`a
Ù±‚bc1x'#    - `matplotlib.text.Text.set_color`Ù±‚`a
Ù±‚bc1x*#    - `matplotlib.text.Text.set_fontsize`Ù±‚`a
Ù±‚bc1x*#    - `matplotlib.text.Text.set_position`Ù±‚`a
Ù±‚bc1x&#    - `matplotlib.axes.Axes.add_line`Ù±‚`a
Ù±‚bc1x#    - `matplotlib.transforms`Ù±‚`a
Ù±‚bc1x'#    - `matplotlib.transforms.Affine2D`Ù±‚`a
`dNoneö