Ù¯‚Ù´ƒ™€Ù±‚bsdy*"""
==========================
Solarized Light stylesheet
==========================

This shows an example of "Solarized_Light" styling, which
tries to replicate the styles of:

- https://ethanschoonover.com/solarized/
- https://github.com/jrnold/ggthemes
- http://www.pygal.org/en/stable/documentation/builtin_styles.html#light-solarized

and work of:

- https://github.com/tonysyu/mpltools

using all 8 accents of the color palette - starting with blue

Still TODO:

- Create alpha values for bar and stacked charts. .33 or .5
- Apply Layout Rules
"""Ù±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnnfpyplotÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnncpltÙ±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„enumpyÙ „enumpyf1.22.3fmoduleenumpyfmoduleõÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnnbnpÙ±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚bc1x)# Fixing random state for reproducibilityÙ±‚`a
Ù±‚`bnpÙ±‚aoa.Ù±‚`frandomÙ±‚aoa.Ù±‚`dseedÙ±‚`a(Ù±‚bmih19680801Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`axÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`hlinspaceÙ±‚`a(Ù±‚bmia0Ù±‚`a,Ù±‚`a Ù±‚bmib10Ù±‚`a)Ù±‚`a
Ù±‚akdwithÙ±‚`a Ù±‚`cpltÙ±‚aoa.Ù±‚`estyleÙ±‚aoa.Ù±‚`gcontextÙ±‚`a(Ù±‚bs1a'Ù±‚bs1oSolarize_Light2Ù±‚bs1a'Ù±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`d    Ù±‚`cpltÙ±‚aoa.Ù±‚`dplotÙ±‚`a(Ù±‚`axÙ±‚`a,Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`csinÙ±‚`a(Ù±‚`axÙ±‚`a)Ù±‚`a Ù±‚aoa+Ù±‚`a Ù±‚`axÙ±‚`a Ù±‚aoa+Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`frandomÙ±‚aoa.Ù±‚`erandnÙ±‚`a(Ù±‚bmib50Ù±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`cpltÙ±‚aoa.Ù±‚`dplotÙ±‚`a(Ù±‚`axÙ±‚`a,Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`csinÙ±‚`a(Ù±‚`axÙ±‚`a)Ù±‚`a Ù±‚aoa+Ù±‚`a Ù±‚bmia2Ù±‚`a Ù±‚aoa*Ù±‚`a Ù±‚`axÙ±‚`a Ù±‚aoa+Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`frandomÙ±‚aoa.Ù±‚`erandnÙ±‚`a(Ù±‚bmib50Ù±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`cpltÙ±‚aoa.Ù±‚`dplotÙ±‚`a(Ù±‚`axÙ±‚`a,Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`csinÙ±‚`a(Ù±‚`axÙ±‚`a)Ù±‚`a Ù±‚aoa+Ù±‚`a Ù±‚bmia3Ù±‚`a Ù±‚aoa*Ù±‚`a Ù±‚`axÙ±‚`a Ù±‚aoa+Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`frandomÙ±‚aoa.Ù±‚`erandnÙ±‚`a(Ù±‚bmib50Ù±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`cpltÙ±‚aoa.Ù±‚`dplotÙ±‚`a(Ù±‚`axÙ±‚`a,Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`csinÙ±‚`a(Ù±‚`axÙ±‚`a)Ù±‚`a Ù±‚aoa+Ù±‚`a Ù±‚bmia4Ù±‚`a Ù±‚aoa+Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`frandomÙ±‚aoa.Ù±‚`erandnÙ±‚`a(Ù±‚bmib50Ù±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`cpltÙ±‚aoa.Ù±‚`dplotÙ±‚`a(Ù±‚`axÙ±‚`a,Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`csinÙ±‚`a(Ù±‚`axÙ±‚`a)Ù±‚`a Ù±‚aoa+Ù±‚`a Ù±‚bmia5Ù±‚`a Ù±‚aoa*Ù±‚`a Ù±‚`axÙ±‚`a Ù±‚aoa+Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`frandomÙ±‚aoa.Ù±‚`erandnÙ±‚`a(Ù±‚bmib50Ù±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`cpltÙ±‚aoa.Ù±‚`dplotÙ±‚`a(Ù±‚`axÙ±‚`a,Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`csinÙ±‚`a(Ù±‚`axÙ±‚`a)Ù±‚`a Ù±‚aoa+Ù±‚`a Ù±‚bmia6Ù±‚`a Ù±‚aoa*Ù±‚`a Ù±‚`axÙ±‚`a Ù±‚aoa+Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`frandomÙ±‚aoa.Ù±‚`erandnÙ±‚`a(Ù±‚bmib50Ù±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`cpltÙ±‚aoa.Ù±‚`dplotÙ±‚`a(Ù±‚`axÙ±‚`a,Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`csinÙ±‚`a(Ù±‚`axÙ±‚`a)Ù±‚`a Ù±‚aoa+Ù±‚`a Ù±‚bmia7Ù±‚`a Ù±‚aoa*Ù±‚`a Ù±‚`axÙ±‚`a Ù±‚aoa+Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`frandomÙ±‚aoa.Ù±‚`erandnÙ±‚`a(Ù±‚bmib50Ù±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`cpltÙ±‚aoa.Ù±‚`dplotÙ±‚`a(Ù±‚`axÙ±‚`a,Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`csinÙ±‚`a(Ù±‚`axÙ±‚`a)Ù±‚`a Ù±‚aoa+Ù±‚`a Ù±‚bmia8Ù±‚`a Ù±‚aoa*Ù±‚`a Ù±‚`axÙ±‚`a Ù±‚aoa+Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`frandomÙ±‚aoa.Ù±‚`erandnÙ±‚`a(Ù±‚bmib50Ù±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚bc1x-# Number of accent colors in the color schemeÙ±‚`a
Ù±‚`d    Ù±‚`cpltÙ±‚aoa.Ù±‚`etitleÙ±‚`a(Ù±‚bs1a'Ù±‚bs1u8 Random Lines - LineÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`cpltÙ±‚aoa.Ù±‚`fxlabelÙ±‚`a(Ù±‚bs1a'Ù±‚bs1gx labelÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`hfontsizeÙ±‚aoa=Ù±‚bmib14Ù±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`cpltÙ±‚aoa.Ù±‚`fylabelÙ±‚`a(Ù±‚bs1a'Ù±‚bs1gy labelÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`hfontsizeÙ±‚aoa=Ù±‚bmib14Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`cpltÙ±‚aoa.Ù±‚`dshowÙ±‚`a(Ù±‚`a)Ù±‚`a
`dNoneö