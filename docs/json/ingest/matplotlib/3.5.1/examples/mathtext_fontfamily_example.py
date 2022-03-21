ŸØÇÅŸ¥Éò∆Ÿ±Çbsdy""""
===============
Math fontfamily
===============

A simple example showcasing the new *math_fontfamily* parameter that can
be used to change the family of fonts for each individual text
element in a plot.

If no parameter is set, the global value
:rc:`mathtext.fontset` will be used.
"""Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±ÇbknfimportŸ±Ç`a Ÿ±ÇbnnŸ¢ÑjmatplotlibŸ†Ñjmatplotlibe3.5.1fmodulejmatplotlibfmoduleıŸ±Çbnna.Ÿ±ÇbnnfpyplotŸ±Ç`a Ÿ±ÇakbasŸ±Ç`a Ÿ±ÇbnncpltŸ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`cfigŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`baxŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`hsubplotsŸ±Ç`a(Ÿ±Ç`gfigsizeŸ±Çaoa=Ÿ±Ç`a(Ÿ±Çbmia6Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia5Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1x## A simple plot for the background.Ÿ±Ç`a
Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`dplotŸ±Ç`a(Ÿ±ÇbnberangeŸ±Ç`a(Ÿ±Çbmib11Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ecolorŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2c0.9Ÿ±Çbs2a"Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1x*# A text mixing normal text and math text.Ÿ±Ç`a
Ÿ±Ç`cmsgŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`a(Ÿ±ÇbsaarŸ±Çbs2a"Ÿ±Çbs2rNormal Text. $TextŸ±Çbs2a\Ÿ±Çbs2c inŸ±Çbs2a\Ÿ±Çbs2e mathŸ±Çbs2a\Ÿ±Çbs2f mode:Ÿ±Çbs2a\Ÿ±Çbs2a Ÿ±Çbs2a"Ÿ±Ç`a
Ÿ±Ç`g       Ÿ±ÇbsaarŸ±Çbs2a"Ÿ±Çbs2a\Ÿ±Çbs2dint_Ÿ±Çbsic{0}Ÿ±Çbs2a^Ÿ±Çbs2a{Ÿ±Çbs2a\Ÿ±Çbs2oinfty } x^2 dx$Ÿ±Çbs2a"Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1x# Set the text in the plot.Ÿ±Ç`a
Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`dtextŸ±Ç`a(Ÿ±Çbmia1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia7Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`cmsgŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dsizeŸ±Çaoa=Ÿ±Çbmib12Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`omath_fontfamilyŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1bcmŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1x%# Set another font for the next text.Ÿ±Ç`a
Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`dtextŸ±Ç`a(Ÿ±Çbmia1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia3Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`cmsgŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dsizeŸ±Çaoa=Ÿ±Çbmib12Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`omath_fontfamilyŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1kdejavuserifŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1xC# *math_fontfamily* can be used in most places where there is text,Ÿ±Ç`a
Ÿ±Çbc1t# like in the title:Ÿ±Ç`a
Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`iset_titleŸ±Ç`a(Ÿ±ÇbsaarŸ±Çbs2a"Ÿ±Çbs2f$TitleŸ±Çbs2a\Ÿ±Çbs2c inŸ±Çbs2a\Ÿ±Çbs2e mathŸ±Çbs2a\Ÿ±Çbs2f mode:Ÿ±Çbs2a\Ÿ±Çbs2a Ÿ±Çbs2a\Ÿ±Çbs2dint_Ÿ±Çbsic{0}Ÿ±Çbs2a^Ÿ±Çbs2a{Ÿ±Çbs2a\Ÿ±Çbs2oinfty } x^2 dx$Ÿ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`m             Ÿ±Ç`omath_fontfamilyŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1hstixsansŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dsizeŸ±Çaoa=Ÿ±Çbmib14Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1x@# Note that the normal text is not changed by *math_fontfamily*.Ÿ±Ç`a
Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`dshowŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
`dNoneˆ