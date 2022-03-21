������������bsdx`"""
===========
Hillshading
===========

Demonstrates a few common tricks with shaded plots.
"""���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���bkndfrom���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfcolors���`a ���bknfimport���`a ���`kLightSource���`a,���`a ���`iNormalize���`a
���`a
���`a
���akcdef���`a ���bnfpdisplay_colorbar���`a(���`a)���`a:���`a
���`d    ���bsdx;"""Display a correct numeric colorbar for a shaded plot."""���`a
���`d    ���`ay���`a,���`a ���`ax���`a ���aoa=���`a ���`bnp���aoa.���`emgrid���`a[���aoa-���bmia4���`a:���bmia2���`a:���bmic200���`aj���`a,���`a ���aoa-���bmia4���`a:���bmia2���`a:���bmic200���`aj���`a]���`a
���`d    ���`az���`a ���aoa=���`a ���bmib10���`a ���aoa*���`a ���`bnp���aoa.���`ccos���`a(���`ax���aoa*���aoa*���bmia2���`a ���aoa+���`a ���`ay���aoa*���aoa*���bmia2���`a)���`a
���`a
���`d    ���`dcmap���`a ���aoa=���`a ���`cplt���aoa.���`bcm���aoa.���`fcopper���`a
���`d    ���`bls���`a ���aoa=���`a ���`kLightSource���`a(���bmic315���`a,���`a ���bmib45���`a)���`a
���`d    ���`crgb���`a ���aoa=���`a ���`bls���aoa.���`eshade���`a(���`az���`a,���`a ���`dcmap���`a)���`a
���`a
���`d    ���`cfig���`a,���`a ���`bax���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`a)���`a
���`d    ���`bax���aoa.���`fimshow���`a(���`crgb���`a,���`a ���`minterpolation���aoa=���bs1a'���bs1hbilinear���bs1a'���`a)���`a
���`a
���`d    ���bc1x(# Use a proxy artist for the colorbar...���`a
���`d    ���`bim���`a ���aoa=���`a ���`bax���aoa.���`fimshow���`a(���`az���`a,���`a ���`dcmap���aoa=���`dcmap���`a)���`a
���`d    ���`bim���aoa.���`fremove���`a(���`a)���`a
���`d    ���`cfig���aoa.���`hcolorbar���`a(���`bim���`a,���`a ���`bax���aoa=���`bax���`a)���`a
���`a
���`d    ���`bax���aoa.���`iset_title���`a(���bs1a'���bs1x#Using a colorbar with a shaded plot���bs1a'���`a,���`a ���`dsize���aoa=���bs1a'���bs1gx-large���bs1a'���`a)���`a
���`a
���`a
���akcdef���`a ���bnfnavoid_outliers���`a(���`a)���`a:���`a
���`d    ���bsdxJ"""Use a custom norm to control the displayed z-range of a shaded plot."""���`a
���`d    ���`ay���`a,���`a ���`ax���`a ���aoa=���`a ���`bnp���aoa.���`emgrid���`a[���aoa-���bmia4���`a:���bmia2���`a:���bmic200���`aj���`a,���`a ���aoa-���bmia4���`a:���bmia2���`a:���bmic200���`aj���`a]���`a
���`d    ���`az���`a ���aoa=���`a ���bmib10���`a ���aoa*���`a ���`bnp���aoa.���`ccos���`a(���`ax���aoa*���aoa*���bmia2���`a ���aoa+���`a ���`ay���aoa*���aoa*���bmia2���`a)���`a
���`a
���`d    ���bc1v# Add some outliers...���`a
���`d    ���`az���`a[���bmic100���`a,���`a ���bmic105���`a]���`a ���aoa=���`a ���bmid2000���`a
���`d    ���`az���`a[���bmic120���`a,���`a ���bmic110���`a]���`a ���aoa=���`a ���aoa-���bmid9000���`a
���`a
���`d    ���`bls���`a ���aoa=���`a ���`kLightSource���`a(���bmic315���`a,���`a ���bmib45���`a)���`a
���`d    ���`cfig���`a,���`a ���`a(���`cax1���`a,���`a ���`cax2���`a)���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`encols���aoa=���bmia2���`a,���`a ���`gfigsize���aoa=���`a(���bmia8���`a,���`a ���bmfc4.5���`a)���`a)���`a
���`a
���`d    ���`crgb���`a ���aoa=���`a ���`bls���aoa.���`eshade���`a(���`az���`a,���`a ���`cplt���aoa.���`bcm���aoa.���`fcopper���`a)���`a
���`d    ���`cax1���aoa.���`fimshow���`a(���`crgb���`a,���`a ���`minterpolation���aoa=���bs1a'���bs1hbilinear���bs1a'���`a)���`a
���`d    ���`cax1���aoa.���`iset_title���`a(���bs1a'���bs1rFull range of data���bs1a'���`a)���`a
���`a
���`d    ���`crgb���`a ���aoa=���`a ���`bls���aoa.���`eshade���`a(���`az���`a,���`a ���`cplt���aoa.���`bcm���aoa.���`fcopper���`a,���`a ���`dvmin���aoa=���aoa-���bmib10���`a,���`a ���`dvmax���aoa=���bmib10���`a)���`a
���`d    ���`cax2���aoa.���`fimshow���`a(���`crgb���`a,���`a ���`minterpolation���aoa=���bs1a'���bs1hbilinear���bs1a'���`a)���`a
���`d    ���`cax2���aoa.���`iset_title���`a(���bs1a'���bs1rManually set range���bs1a'���`a)���`a
���`a
���`d    ���`cfig���aoa.���`hsuptitle���`a(���bs1a'���bs1x!Avoiding Outliers in Shaded Plots���bs1a'���`a,���`a ���`dsize���aoa=���bs1a'���bs1gx-large���bs1a'���`a)���`a
���`a
���`a
���akcdef���`a ���bnfpshade_other_data���`a(���`a)���`a:���`a
���`d    ���bsdxJ"""Demonstrates displaying different variables through shade and color."""���`a
���`d    ���`ay���`a,���`a ���`ax���`a ���aoa=���`a ���`bnp���aoa.���`emgrid���`a[���aoa-���bmia4���`a:���bmia2���`a:���bmic200���`aj���`a,���`a ���aoa-���bmia4���`a:���bmia2���`a:���bmic200���`aj���`a]���`a
���`d    ���`bz1���`a ���aoa=���`a ���`bnp���aoa.���`csin���`a(���`ax���aoa*���aoa*���bmia2���`a)���`b  ���bc1s# Data to hillshade���`a
���`d    ���`bz2���`a ���aoa=���`a ���`bnp���aoa.���`ccos���`a(���`ax���aoa*���aoa*���bmia2���`a ���aoa+���`a ���`ay���aoa*���aoa*���bmia2���`a)���`b  ���bc1o# Data to color���`a
���`a
���`d    ���`dnorm���`a ���aoa=���`a ���`iNormalize���`a(���`bz2���aoa.���`cmin���`a(���`a)���`a,���`a ���`bz2���aoa.���`cmax���`a(���`a)���`a)���`a
���`d    ���`dcmap���`a ���aoa=���`a ���`cplt���aoa.���`bcm���aoa.���`dRdBu���`a
���`a
���`d    ���`bls���`a ���aoa=���`a ���`kLightSource���`a(���bmic315���`a,���`a ���bmib45���`a)���`a
���`d    ���`crgb���`a ���aoa=���`a ���`bls���aoa.���`ishade_rgb���`a(���`dcmap���`a(���`dnorm���`a(���`bz2���`a)���`a)���`a,���`a ���`bz1���`a)���`a
���`a
���`d    ���`cfig���`a,���`a ���`bax���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`a)���`a
���`d    ���`bax���aoa.���`fimshow���`a(���`crgb���`a,���`a ���`minterpolation���aoa=���bs1a'���bs1hbilinear���bs1a'���`a)���`a
���`d    ���`bax���aoa.���`iset_title���`a(���bs1a'���bs1x'Shade by one variable, color by another���bs1a'���`a,���`a ���`dsize���aoa=���bs1a'���bs1gx-large���bs1a'���`a)���`a
���`a
���`pdisplay_colorbar���`a(���`a)���`a
���`navoid_outliers���`a(���`a)���`a
���`pshade_other_data���`a(���`a)���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
`dNone�