ŸØÇÅŸ¥ÉôUŸ±Çbsdx"""
==================
Contour Label Demo
==================

Illustrate some of the more advanced things that one can do with
contour labels.

See also the :doc:`contour demo example
</gallery/images_contours_and_fields/contour_demo>`.
"""Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±ÇbknfimportŸ±Ç`a Ÿ±ÇbnnŸ¢ÑenumpyŸ†Ñenumpyf1.22.3fmoduleenumpyfmoduleıŸ±Ç`a Ÿ±ÇakbasŸ±Ç`a Ÿ±ÇbnnbnpŸ±Ç`a
Ÿ±ÇbknfimportŸ±Ç`a Ÿ±ÇbnnŸ¢ÑjmatplotlibŸ†Ñjmatplotlibe3.5.1fmodulejmatplotlibfmoduleıŸ±Çbnna.Ÿ±ÇbnnftickerŸ±Ç`a Ÿ±ÇakbasŸ±Ç`a Ÿ±ÇbnnftickerŸ±Ç`a
Ÿ±ÇbknfimportŸ±Ç`a Ÿ±ÇbnnŸ¢ÑjmatplotlibŸ†Ñjmatplotlibe3.5.1fmodulejmatplotlibfmoduleıŸ±Çbnna.Ÿ±ÇbnnfpyplotŸ±Ç`a Ÿ±ÇakbasŸ±Ç`a Ÿ±ÇbnncpltŸ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1xO###############################################################################Ÿ±Ç`a
Ÿ±Çbc1t# Define our surfaceŸ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`edeltaŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Çbmfe0.025Ÿ±Ç`a
Ÿ±Ç`axŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`farangeŸ±Ç`a(Ÿ±Çaoa-Ÿ±Çbmfc3.0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfc3.0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`edeltaŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`ayŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`farangeŸ±Ç`a(Ÿ±Çaoa-Ÿ±Çbmfc2.0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfc2.0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`edeltaŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`aXŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`aYŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`hmeshgridŸ±Ç`a(Ÿ±Ç`axŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ayŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`bZ1Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`cexpŸ±Ç`a(Ÿ±Çaoa-Ÿ±Ç`aXŸ±Çaoa*Ÿ±Çaoa*Ÿ±Çbmia2Ÿ±Ç`a Ÿ±Çaoa-Ÿ±Ç`a Ÿ±Ç`aYŸ±Çaoa*Ÿ±Çaoa*Ÿ±Çbmia2Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`bZ2Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`cexpŸ±Ç`a(Ÿ±Çaoa-Ÿ±Ç`a(Ÿ±Ç`aXŸ±Ç`a Ÿ±Çaoa-Ÿ±Ç`a Ÿ±Çbmia1Ÿ±Ç`a)Ÿ±Çaoa*Ÿ±Çaoa*Ÿ±Çbmia2Ÿ±Ç`a Ÿ±Çaoa-Ÿ±Ç`a Ÿ±Ç`a(Ÿ±Ç`aYŸ±Ç`a Ÿ±Çaoa-Ÿ±Ç`a Ÿ±Çbmia1Ÿ±Ç`a)Ÿ±Çaoa*Ÿ±Çaoa*Ÿ±Çbmia2Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`aZŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`a(Ÿ±Ç`bZ1Ÿ±Ç`a Ÿ±Çaoa-Ÿ±Ç`a Ÿ±Ç`bZ2Ÿ±Ç`a)Ÿ±Ç`a Ÿ±Çaoa*Ÿ±Ç`a Ÿ±Çbmia2Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1xO###############################################################################Ÿ±Ç`a
Ÿ±Çbc1x2# Make contour labels with custom level formattersŸ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1xK# This custom formatter removes trailing zeros, e.g. "1.0" becomes "1", andŸ±Ç`a
Ÿ±Çbc1x# then adds a percent sign.Ÿ±Ç`a
Ÿ±ÇakcdefŸ±Ç`a Ÿ±ÇbnfcfmtŸ±Ç`a(Ÿ±Ç`axŸ±Ç`a)Ÿ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`asŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±ÇbsaafŸ±Çbs2a"Ÿ±Çbsia{Ÿ±Ç`axŸ±Çbsia:Ÿ±Çbs2c.1fŸ±Çbsia}Ÿ±Çbs2a"Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±ÇakbifŸ±Ç`a Ÿ±Ç`asŸ±Çaoa.Ÿ±Ç`hendswithŸ±Ç`a(Ÿ±Çbs2a"Ÿ±Çbs2a0Ÿ±Çbs2a"Ÿ±Ç`a)Ÿ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±Ç`asŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±ÇbsaafŸ±Çbs2a"Ÿ±Çbsia{Ÿ±Ç`axŸ±Çbsia:Ÿ±Çbs2c.0fŸ±Çbsia}Ÿ±Çbs2a"Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±ÇakfreturnŸ±Ç`a Ÿ±ÇbsabrfŸ±Çbs2a"Ÿ±Çbsia{Ÿ±Ç`asŸ±Çbsia}Ÿ±Çbs2a Ÿ±Çbs2a\Ÿ±Çbs2a%Ÿ±Çbs2a"Ÿ±Ç`a Ÿ±ÇakbifŸ±Ç`a Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`hrcParamsŸ±Ç`a[Ÿ±Çbs2a"Ÿ±Çbs2ktext.usetexŸ±Çbs2a"Ÿ±Ç`a]Ÿ±Ç`a Ÿ±ÇakdelseŸ±Ç`a Ÿ±ÇbsaafŸ±Çbs2a"Ÿ±Çbsia{Ÿ±Ç`asŸ±Çbsia}Ÿ±Çbs2b %Ÿ±Çbs2a"Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1t# Basic contour plotŸ±Ç`a
Ÿ±Ç`cfigŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`baxŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`hsubplotsŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`bCSŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`gcontourŸ±Ç`a(Ÿ±Ç`aXŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`aYŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`aZŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`fclabelŸ±Ç`a(Ÿ±Ç`bCSŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`bCSŸ±Çaoa.Ÿ±Ç`flevelsŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`finlineŸ±Çaoa=Ÿ±ÇbkcdTrueŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`cfmtŸ±Çaoa=Ÿ±Ç`cfmtŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`hfontsizeŸ±Çaoa=Ÿ±Çbmib10Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1xO###############################################################################Ÿ±Ç`a
Ÿ±Çbc1x:# Label contours with arbitrary strings using a dictionaryŸ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`dfig1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`cax1Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`hsubplotsŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1t# Basic contour plotŸ±Ç`a
Ÿ±Ç`cCS1Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cax1Ÿ±Çaoa.Ÿ±Ç`gcontourŸ±Ç`a(Ÿ±Ç`aXŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`aYŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`aZŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`cfmtŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`a{Ÿ±Ç`a}Ÿ±Ç`a
Ÿ±Ç`dstrsŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`a[Ÿ±Çbs1a'Ÿ±Çbs1efirstŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1fsecondŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1ethirdŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1ffourthŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1efifthŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1esixthŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1gseventhŸ±Çbs1a'Ÿ±Ç`a]Ÿ±Ç`a
Ÿ±ÇakcforŸ±Ç`a Ÿ±Ç`alŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`asŸ±Ç`a Ÿ±ÇbowbinŸ±Ç`a Ÿ±ÇbnbczipŸ±Ç`a(Ÿ±Ç`cCS1Ÿ±Çaoa.Ÿ±Ç`flevelsŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dstrsŸ±Ç`a)Ÿ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`cfmtŸ±Ç`a[Ÿ±Ç`alŸ±Ç`a]Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`asŸ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1x'# Label every other level using stringsŸ±Ç`a
Ÿ±Ç`cax1Ÿ±Çaoa.Ÿ±Ç`fclabelŸ±Ç`a(Ÿ±Ç`cCS1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`cCS1Ÿ±Çaoa.Ÿ±Ç`flevelsŸ±Ç`a[Ÿ±Ç`a:Ÿ±Ç`a:Ÿ±Çbmia2Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`finlineŸ±Çaoa=Ÿ±ÇbkcdTrueŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`cfmtŸ±Çaoa=Ÿ±Ç`cfmtŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`hfontsizeŸ±Çaoa=Ÿ±Çbmib10Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1xO###############################################################################Ÿ±Ç`a
Ÿ±Çbc1q# Use a FormatterŸ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`dfig2Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`cax2Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`hsubplotsŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`cCS2Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cax2Ÿ±Çaoa.Ÿ±Ç`gcontourŸ±Ç`a(Ÿ±Ç`aXŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`aYŸ±Ç`a,Ÿ±Ç`a Ÿ±Çbmic100Ÿ±Çaoa*Ÿ±Çaoa*Ÿ±Ç`aZŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`glocatorŸ±Çaoa=Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`jLogLocatorŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cfmtŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`ftickerŸ±Çaoa.Ÿ±Ç`tLogFormatterMathtextŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cfmtŸ±Çaoa.Ÿ±Ç`qcreate_dummy_axisŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cax2Ÿ±Çaoa.Ÿ±Ç`fclabelŸ±Ç`a(Ÿ±Ç`cCS2Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`cCS2Ÿ±Çaoa.Ÿ±Ç`flevelsŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`cfmtŸ±Çaoa=Ÿ±Ç`cfmtŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cax2Ÿ±Çaoa.Ÿ±Ç`iset_titleŸ±Ç`a(Ÿ±Çbs2a"Ÿ±Çbs2g$100^Z$Ÿ±Çbs2a"Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`dshowŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1xM#############################################################################Ÿ±Ç`a
Ÿ±Çbc1a#Ÿ±Ç`a
Ÿ±Çbc1x# .. admonition:: ReferencesŸ±Ç`a
Ÿ±Çbc1a#Ÿ±Ç`a
Ÿ±Çbc1xN#    The use of the following functions, methods, classes and modules is shownŸ±Ç`a
Ÿ±Çbc1u#    in this example:Ÿ±Ç`a
Ÿ±Çbc1a#Ÿ±Ç`a
Ÿ±Çbc1xC#    - `matplotlib.axes.Axes.contour` / `matplotlib.pyplot.contour`Ÿ±Ç`a
Ÿ±Çbc1xA#    - `matplotlib.axes.Axes.clabel` / `matplotlib.pyplot.clabel`Ÿ±Ç`a
Ÿ±Çbc1x/#    - `matplotlib.ticker.LogFormatterMathtext`Ÿ±Ç`a
Ÿ±Çbc1x7#    - `matplotlib.ticker.TickHelper.create_dummy_axis`Ÿ±Ç`a
`dNoneˆ