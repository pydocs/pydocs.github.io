ŸØÇÅŸ¥ÉôRŸ±Çbsdxp"""
=============
Font indexing
=============

This example shows how the font tables relate to one another.
"""Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±ÇbknfimportŸ±Ç`a Ÿ±ÇbnnbosŸ±Ç`a
Ÿ±Ç`a
Ÿ±ÇbknfimportŸ±Ç`a Ÿ±ÇbnnŸ¢ÑjmatplotlibŸ†Ñjmatplotlibe3.5.1fmodulejmatplotlibfmoduleıŸ±Ç`a
Ÿ±ÇbkndfromŸ±Ç`a Ÿ±ÇbnnŸ¢ÑjmatplotlibŸ†Ñjmatplotlibe3.5.1fmodulejmatplotlibfmoduleıŸ±Çbnna.Ÿ±Çbnngft2fontŸ±Ç`a Ÿ±ÇbknfimportŸ±Ç`a Ÿ±Ç`a(Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`gFT2FontŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`oKERNING_DEFAULTŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`pKERNING_UNFITTEDŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`pKERNING_UNSCALEDŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`dfontŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`gFT2FontŸ±Ç`a(Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`bosŸ±Çaoa.Ÿ±Ç`dpathŸ±Çaoa.Ÿ±Ç`djoinŸ±Ç`a(Ÿ±Ç`Ÿ¢ÑjmatplotlibŸ†Ñjmatplotlibe3.5.1fmodulejmatplotlibfmoduleıŸ±Çaoa.Ÿ±Ç`mget_data_pathŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1xfonts/ttf/DejaVuSans.ttfŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`dfontŸ±Çaoa.Ÿ±Ç`kset_charmapŸ±Ç`a(Ÿ±Çbmia0Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`ecodesŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`dfontŸ±Çaoa.Ÿ±Ç`kget_charmapŸ±Ç`a(Ÿ±Ç`a)Ÿ±Çaoa.Ÿ±Ç`eitemsŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1x5# make a charname to charcode and glyphind dictionaryŸ±Ç`a
Ÿ±Ç`ecodedŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`a{Ÿ±Ç`a}Ÿ±Ç`a
Ÿ±Ç`fglyphdŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`a{Ÿ±Ç`a}Ÿ±Ç`a
Ÿ±ÇakcforŸ±Ç`a Ÿ±Ç`eccodeŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`hglyphindŸ±Ç`a Ÿ±ÇbowbinŸ±Ç`a Ÿ±Ç`ecodesŸ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`dnameŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`dfontŸ±Çaoa.Ÿ±Ç`nget_glyph_nameŸ±Ç`a(Ÿ±Ç`hglyphindŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`ecodedŸ±Ç`a[Ÿ±Ç`dnameŸ±Ç`a]Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`eccodeŸ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`fglyphdŸ±Ç`a[Ÿ±Ç`dnameŸ±Ç`a]Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`hglyphindŸ±Ç`a
Ÿ±Ç`d    Ÿ±Çbc1x/# print(glyphind, ccode, hex(int(ccode)), name)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`dcodeŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`ecodedŸ±Ç`a[Ÿ±Çbs1a'Ÿ±Çbs1aAŸ±Çbs1a'Ÿ±Ç`a]Ÿ±Ç`a
Ÿ±Ç`eglyphŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`dfontŸ±Çaoa.Ÿ±Ç`iload_charŸ±Ç`a(Ÿ±Ç`dcodeŸ±Ç`a)Ÿ±Ç`a
Ÿ±ÇbnbeprintŸ±Ç`a(Ÿ±Ç`eglyphŸ±Çaoa.Ÿ±Ç`dbboxŸ±Ç`a)Ÿ±Ç`a
Ÿ±ÇbnbeprintŸ±Ç`a(Ÿ±Ç`fglyphdŸ±Ç`a[Ÿ±Çbs1a'Ÿ±Çbs1aAŸ±Çbs1a'Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`fglyphdŸ±Ç`a[Ÿ±Çbs1a'Ÿ±Çbs1aVŸ±Çbs1a'Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ecodedŸ±Ç`a[Ÿ±Çbs1a'Ÿ±Çbs1aAŸ±Çbs1a'Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ecodedŸ±Ç`a[Ÿ±Çbs1a'Ÿ±Çbs1aVŸ±Çbs1a'Ÿ±Ç`a]Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±ÇbnbeprintŸ±Ç`a(Ÿ±Çbs1a'Ÿ±Çbs1bAVŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dfontŸ±Çaoa.Ÿ±Ç`kget_kerningŸ±Ç`a(Ÿ±Ç`fglyphdŸ±Ç`a[Ÿ±Çbs1a'Ÿ±Çbs1aAŸ±Çbs1a'Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`fglyphdŸ±Ç`a[Ÿ±Çbs1a'Ÿ±Çbs1aVŸ±Çbs1a'Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`oKERNING_DEFAULTŸ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±ÇbnbeprintŸ±Ç`a(Ÿ±Çbs1a'Ÿ±Çbs1bAVŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dfontŸ±Çaoa.Ÿ±Ç`kget_kerningŸ±Ç`a(Ÿ±Ç`fglyphdŸ±Ç`a[Ÿ±Çbs1a'Ÿ±Çbs1aAŸ±Çbs1a'Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`fglyphdŸ±Ç`a[Ÿ±Çbs1a'Ÿ±Çbs1aVŸ±Çbs1a'Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`pKERNING_UNFITTEDŸ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±ÇbnbeprintŸ±Ç`a(Ÿ±Çbs1a'Ÿ±Çbs1bAVŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dfontŸ±Çaoa.Ÿ±Ç`kget_kerningŸ±Ç`a(Ÿ±Ç`fglyphdŸ±Ç`a[Ÿ±Çbs1a'Ÿ±Çbs1aAŸ±Çbs1a'Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`fglyphdŸ±Ç`a[Ÿ±Çbs1a'Ÿ±Çbs1aVŸ±Çbs1a'Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`pKERNING_UNSCALEDŸ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±ÇbnbeprintŸ±Ç`a(Ÿ±Çbs1a'Ÿ±Çbs1bATŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dfontŸ±Çaoa.Ÿ±Ç`kget_kerningŸ±Ç`a(Ÿ±Ç`fglyphdŸ±Ç`a[Ÿ±Çbs1a'Ÿ±Çbs1aAŸ±Çbs1a'Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`fglyphdŸ±Ç`a[Ÿ±Çbs1a'Ÿ±Çbs1aTŸ±Çbs1a'Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`pKERNING_UNSCALEDŸ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
`dNoneˆ