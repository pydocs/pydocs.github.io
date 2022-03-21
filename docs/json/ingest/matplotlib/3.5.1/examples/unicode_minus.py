ŸØÇÅŸ¥ÉòÖŸ±Çbsdy∑"""
=============
Unicode minus
=============

By default, tick labels at negative values are rendered using a `Unicode
minus`__ (U+2212) rather than an ASCII hyphen (U+002D).  This can be controlled
by setting :rc:`axes.unicode_minus`.

__ https://en.wikipedia.org/wiki/Plus_and_minus_signs#Character_codes

The replacement is performed at draw time of the tick labels (usually during a
`.pyplot.show()` or `.pyplot.savefig()` call). Therefore, all tick labels of
the figure follow the same setting and we cannot demonstrate both glyphs on
real tick labels of the same figure simultaneously.

Instead, this example simply showcases the difference between the two glyphs
in a magnified font.
"""Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±ÇbknfimportŸ±Ç`a Ÿ±ÇbnnŸ¢ÑjmatplotlibŸ†Ñjmatplotlibe3.5.1fmodulejmatplotlibfmoduleıŸ±Çbnna.Ÿ±ÇbnnfpyplotŸ±Ç`a Ÿ±ÇakbasŸ±Ç`a Ÿ±ÇbnncpltŸ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`cfigŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`ffigureŸ±Ç`a(Ÿ±Ç`gfigsizeŸ±Çaoa=Ÿ±Ç`a(Ÿ±Çbmia4Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia2Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cfigŸ±Çaoa.Ÿ±Ç`dtextŸ±Ç`a(Ÿ±Çbmfc.15Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfb.6Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs2a"Ÿ±Çbs2nUnicode minus:Ÿ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`hfontsizeŸ±Çaoa=Ÿ±Çbmib20Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cfigŸ±Çaoa.Ÿ±Ç`dtextŸ±Ç`a(Ÿ±Çbmfc.85Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfb.6Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs2a"Ÿ±Çbsen\N{MINUS SIGN}Ÿ±Çbs2a1Ÿ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`bhaŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1erightŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`hfontsizeŸ±Çaoa=Ÿ±Çbmib20Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cfigŸ±Çaoa.Ÿ±Ç`dtextŸ±Ç`a(Ÿ±Çbmfc.15Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfb.3Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs2a"Ÿ±Çbs2mASCII hyphen:Ÿ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`hfontsizeŸ±Çaoa=Ÿ±Çbmib20Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cfigŸ±Çaoa.Ÿ±Ç`dtextŸ±Ç`a(Ÿ±Çbmfc.85Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfb.3Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs2a"Ÿ±Çbs2b-1Ÿ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`bhaŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1erightŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`hfontsizeŸ±Çaoa=Ÿ±Çbmib20Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`dshowŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
`dNoneˆ