������������bsdy""""
===============
Math fontfamily
===============

A simple example showcasing the new *math_fontfamily* parameter that can
be used to change the family of fonts for each individual text
element in a plot.

If no parameter is set, the global value
:rc:`mathtext.fontset` will be used.
"""���`a
���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���`a
���`a
���`cfig���`a,���`a ���`bax���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`gfigsize���aoa=���`a(���bmia6���`a,���`a ���bmia5���`a)���`a)���`a
���`a
���bc1x## A simple plot for the background.���`a
���`bax���aoa.���`dplot���`a(���bnberange���`a(���bmib11���`a)���`a,���`a ���`ecolor���aoa=���bs2a"���bs2c0.9���bs2a"���`a)���`a
���`a
���bc1x*# A text mixing normal text and math text.���`a
���`cmsg���`a ���aoa=���`a ���`a(���bsaar���bs2a"���bs2rNormal Text. $Text���bs2a\���bs2c in���bs2a\���bs2e math���bs2a\���bs2f mode:���bs2a\���bs2a ���bs2a"���`a
���`g       ���bsaar���bs2a"���bs2a\���bs2dint_���bsic{0}���bs2a^���bs2a{���bs2a\���bs2oinfty } x^2 dx$���bs2a"���`a)���`a
���`a
���bc1x# Set the text in the plot.���`a
���`bax���aoa.���`dtext���`a(���bmia1���`a,���`a ���bmia7���`a,���`a ���`cmsg���`a,���`a ���`dsize���aoa=���bmib12���`a,���`a ���`omath_fontfamily���aoa=���bs1a'���bs1bcm���bs1a'���`a)���`a
���`a
���bc1x%# Set another font for the next text.���`a
���`bax���aoa.���`dtext���`a(���bmia1���`a,���`a ���bmia3���`a,���`a ���`cmsg���`a,���`a ���`dsize���aoa=���bmib12���`a,���`a ���`omath_fontfamily���aoa=���bs1a'���bs1kdejavuserif���bs1a'���`a)���`a
���`a
���bc1xC# *math_fontfamily* can be used in most places where there is text,���`a
���bc1t# like in the title:���`a
���`bax���aoa.���`iset_title���`a(���bsaar���bs2a"���bs2f$Title���bs2a\���bs2c in���bs2a\���bs2e math���bs2a\���bs2f mode:���bs2a\���bs2a ���bs2a\���bs2dint_���bsic{0}���bs2a^���bs2a{���bs2a\���bs2oinfty } x^2 dx$���bs2a"���`a,���`a
���`m             ���`omath_fontfamily���aoa=���bs1a'���bs1hstixsans���bs1a'���`a,���`a ���`dsize���aoa=���bmib14���`a)���`a
���`a
���bc1x@# Note that the normal text is not changed by *math_fontfamily*.���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
`dNone�