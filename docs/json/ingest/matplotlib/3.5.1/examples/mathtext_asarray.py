Ù¯‚Ù´ƒ™Ù±‚bsdxO"""
=======================
Convert texts to images
=======================
"""Ù±‚`a
Ù±‚`a
Ù±‚bkndfromÙ±‚`a Ù±‚bnnbioÙ±‚`a Ù±‚bknfimportÙ±‚`a Ù±‚`gBytesIOÙ±‚`a
Ù±‚`a
Ù±‚bkndfromÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnnffigureÙ±‚`a Ù±‚bknfimportÙ±‚`a Ù±‚`fFigureÙ±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnnfpyplotÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnncpltÙ±‚`a
Ù±‚bkndfromÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnnjtransformsÙ±‚`a Ù±‚bknfimportÙ±‚`a Ù±‚`qIdentityTransformÙ±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚akcdefÙ±‚`a Ù±‚bnfltext_to_rgbaÙ±‚`a(Ù±‚`asÙ±‚`a,Ù±‚`a Ù±‚aoa*Ù±‚`a,Ù±‚`a Ù±‚`cdpiÙ±‚`a,Ù±‚`a Ù±‚aoa*Ù±‚aoa*Ù±‚`fkwargsÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`d    Ù±‚bc1x/# To convert a text string to an image, we can:Ù±‚`a
Ù±‚`d    Ù±‚bc1x/# - draw it on an empty and transparent figure;Ù±‚`a
Ù±‚`d    Ù±‚bc1xF# - save the figure to a temporary buffer using ``bbox_inches="tight",Ù±‚`a
Ù±‚`d    Ù±‚bc1x<#   pad_inches=0`` which will pick the correct area to save;Ù±‚`a
Ù±‚`d    Ù±‚bc1x)# - load the buffer using ``plt.imread``.Ù±‚`a
Ù±‚`d    Ù±‚bc1a#Ù±‚`a
Ù±‚`d    Ù±‚bc1xG# (If desired, one can also directly save the image to the filesystem.)Ù±‚`a
Ù±‚`d    Ù±‚`cfigÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`fFigureÙ±‚`a(Ù±‚`ifacecolorÙ±‚aoa=Ù±‚bs2a"Ù±‚bs2dnoneÙ±‚bs2a"Ù±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`cfigÙ±‚aoa.Ù±‚`dtextÙ±‚`a(Ù±‚bmia0Ù±‚`a,Ù±‚`a Ù±‚bmia0Ù±‚`a,Ù±‚`a Ù±‚`asÙ±‚`a,Ù±‚`a Ù±‚aoa*Ù±‚aoa*Ù±‚`fkwargsÙ±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚akdwithÙ±‚`a Ù±‚`gBytesIOÙ±‚`a(Ù±‚`a)Ù±‚`a Ù±‚akbasÙ±‚`a Ù±‚`cbufÙ±‚`a:Ù±‚`a
Ù±‚`h        Ù±‚`cfigÙ±‚aoa.Ù±‚`gsavefigÙ±‚`a(Ù±‚`cbufÙ±‚`a,Ù±‚`a Ù±‚`cdpiÙ±‚aoa=Ù±‚`cdpiÙ±‚`a,Ù±‚`a Ù±‚bnbfformatÙ±‚aoa=Ù±‚bs2a"Ù±‚bs2cpngÙ±‚bs2a"Ù±‚`a,Ù±‚`a Ù±‚`kbbox_inchesÙ±‚aoa=Ù±‚bs2a"Ù±‚bs2etightÙ±‚bs2a"Ù±‚`a,Ù±‚`a
Ù±‚`t                    Ù±‚`jpad_inchesÙ±‚aoa=Ù±‚bmia0Ù±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚`cbufÙ±‚aoa.Ù±‚`dseekÙ±‚`a(Ù±‚bmia0Ù±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚`drgbaÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cpltÙ±‚aoa.Ù±‚`fimreadÙ±‚`a(Ù±‚`cbufÙ±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚akfreturnÙ±‚`a Ù±‚`drgbaÙ±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚`cfigÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cpltÙ±‚aoa.Ù±‚`ffigureÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`ergba1Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`ltext_to_rgbaÙ±‚`a(Ù±‚bsaarÙ±‚bs2a"Ù±‚bs2eIQ: $Ù±‚bs2a\Ù±‚bs2ksigma_i=15$Ù±‚bs2a"Ù±‚`a,Ù±‚`a Ù±‚`ecolorÙ±‚aoa=Ù±‚bs2a"Ù±‚bs2dblueÙ±‚bs2a"Ù±‚`a,Ù±‚`a Ù±‚`hfontsizeÙ±‚aoa=Ù±‚bmib20Ù±‚`a,Ù±‚`a Ù±‚`cdpiÙ±‚aoa=Ù±‚bmic200Ù±‚`a)Ù±‚`a
Ù±‚`ergba2Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`ltext_to_rgbaÙ±‚`a(Ù±‚bsaarÙ±‚bs2a"Ù±‚bs2qsome other stringÙ±‚bs2a"Ù±‚`a,Ù±‚`a Ù±‚`ecolorÙ±‚aoa=Ù±‚bs2a"Ù±‚bs2credÙ±‚bs2a"Ù±‚`a,Ù±‚`a Ù±‚`hfontsizeÙ±‚aoa=Ù±‚bmib20Ù±‚`a,Ù±‚`a Ù±‚`cdpiÙ±‚aoa=Ù±‚bmic200Ù±‚`a)Ù±‚`a
Ù±‚bc1xJ# One can then draw such text images to a Figure using `.Figure.figimage`.Ù±‚`a
Ù±‚`cfigÙ±‚aoa.Ù±‚`hfigimageÙ±‚`a(Ù±‚`ergba1Ù±‚`a,Ù±‚`a Ù±‚bmic100Ù±‚`a,Ù±‚`a Ù±‚bmib50Ù±‚`a)Ù±‚`a
Ù±‚`cfigÙ±‚aoa.Ù±‚`hfigimageÙ±‚`a(Ù±‚`ergba2Ù±‚`a,Ù±‚`a Ù±‚bmic100Ù±‚`a,Ù±‚`a Ù±‚bmic150Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚bc1x?# One can also directly draw texts to a figure with positioningÙ±‚`a
Ù±‚bc1x<# in pixel coordinates by using `.Figure.text` together withÙ±‚`a
Ù±‚bc1x"# `.transforms.IdentityTransform`.Ù±‚`a
Ù±‚`cfigÙ±‚aoa.Ù±‚`dtextÙ±‚`a(Ù±‚bmic100Ù±‚`a,Ù±‚`a Ù±‚bmic250Ù±‚`a,Ù±‚`a Ù±‚bsaarÙ±‚bs2a"Ù±‚bs2eIQ: $Ù±‚bs2a\Ù±‚bs2ksigma_i=15$Ù±‚bs2a"Ù±‚`a,Ù±‚`a Ù±‚`ecolorÙ±‚aoa=Ù±‚bs2a"Ù±‚bs2dblueÙ±‚bs2a"Ù±‚`a,Ù±‚`a Ù±‚`hfontsizeÙ±‚aoa=Ù±‚bmib20Ù±‚`a,Ù±‚`a
Ù±‚`i         Ù±‚`itransformÙ±‚aoa=Ù±‚`qIdentityTransformÙ±‚`a(Ù±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`cfigÙ±‚aoa.Ù±‚`dtextÙ±‚`a(Ù±‚bmic100Ù±‚`a,Ù±‚`a Ù±‚bmic350Ù±‚`a,Ù±‚`a Ù±‚bsaarÙ±‚bs2a"Ù±‚bs2qsome other stringÙ±‚bs2a"Ù±‚`a,Ù±‚`a Ù±‚`ecolorÙ±‚aoa=Ù±‚bs2a"Ù±‚bs2credÙ±‚bs2a"Ù±‚`a,Ù±‚`a Ù±‚`hfontsizeÙ±‚aoa=Ù±‚bmib20Ù±‚`a,Ù±‚`a
Ù±‚`i         Ù±‚`itransformÙ±‚aoa=Ù±‚`qIdentityTransformÙ±‚`a(Ù±‚`a)Ù±‚`a)Ù±‚`a
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
Ù±‚bc1x*#    - `matplotlib.figure.Figure.figimage`Ù±‚`a
Ù±‚bc1x&#    - `matplotlib.figure.Figure.text`Ù±‚`a
Ù±‚bc1x0#    - `matplotlib.transforms.IdentityTransform`Ù±‚`a
Ù±‚bc1x #    - `matplotlib.image.imread`Ù±‚`a
`dNoneö