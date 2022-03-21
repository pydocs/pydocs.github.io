ŸØÇÅŸ¥ÉòqŸ±ÇbsaarŸ±Çbsdy∞"""
=========================================
The difference between \\dfrac and \\frac
=========================================

In this example, the differences between the \\dfrac and \\frac TeX macros are
illustrated; in particular, the difference between display style and text style
fractions when using Mathtex.

.. versionadded:: 2.1

.. note::
    To use \\dfrac with the LaTeX engine (text.usetex : True), you need to
    import the amsmath package with the text.latex.preamble rc, which is
    an unsupported feature; therefore, it is probably a better idea to just
    use the \\displaystyle option before the \\frac macro to get this behavior
    with the LaTeX engine.

"""Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±ÇbknfimportŸ±Ç`a Ÿ±ÇbnnŸ¢ÑjmatplotlibŸ†Ñjmatplotlibe3.5.1fmodulejmatplotlibfmoduleıŸ±Çbnna.Ÿ±ÇbnnfpyplotŸ±Ç`a Ÿ±ÇakbasŸ±Ç`a Ÿ±ÇbnncpltŸ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`cfigŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`ffigureŸ±Ç`a(Ÿ±Ç`gfigsizeŸ±Çaoa=Ÿ±Ç`a(Ÿ±Çbmfd5.25Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd0.75Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cfigŸ±Çaoa.Ÿ±Ç`dtextŸ±Ç`a(Ÿ±Çbmfc0.5Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfc0.3Ÿ±Ç`a,Ÿ±Ç`a Ÿ±ÇbsaarŸ±Çbs1a'Ÿ±Çbs1a\Ÿ±Çbs1hdfrac: $Ÿ±Çbs1a\Ÿ±Çbs1edfracŸ±Çbsic{a}Ÿ±Çbsic{b}Ÿ±Çbs1a$Ÿ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`i         Ÿ±Ç`shorizontalalignmentŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1fcenterŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`qverticalalignmentŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1fcenterŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cfigŸ±Çaoa.Ÿ±Ç`dtextŸ±Ç`a(Ÿ±Çbmfc0.5Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfc0.7Ÿ±Ç`a,Ÿ±Ç`a Ÿ±ÇbsaarŸ±Çbs1a'Ÿ±Çbs1a\Ÿ±Çbs1gfrac: $Ÿ±Çbs1a\Ÿ±Çbs1dfracŸ±Çbsic{a}Ÿ±Çbsic{b}Ÿ±Çbs1a$Ÿ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`i         Ÿ±Ç`shorizontalalignmentŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1fcenterŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`qverticalalignmentŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1fcenterŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`dshowŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
`dNoneˆ