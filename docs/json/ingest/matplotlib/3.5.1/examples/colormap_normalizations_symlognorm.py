��������S���bsdx�"""
==================================
Colormap Normalizations Symlognorm
==================================

Demonstration of using norm to map colormaps onto data in non-linear ways.
"""���`a
���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfcolors���`a ���akbas���`a ���bnnfcolors���`a
���`a
���bsdy$"""
SymLogNorm: two humps, one negative and one positive, The positive
with 5-times the amplitude. Linearly, you cannot see detail in the
negative hump.  Here we logarithmically scale the positive and
negative data separately.

Note that colorbar labels do not come out looking very good.
"""���`a
���`a
���`aN���`a ���aoa=���`a ���bmic100���`a
���`aX���`a,���`a ���`aY���`a ���aoa=���`a ���`bnp���aoa.���`emgrid���`a[���aoa-���bmia3���`a:���bmia3���`a:���bnbgcomplex���`a(���bmia0���`a,���`a ���`aN���`a)���`a,���`a ���aoa-���bmia2���`a:���bmia2���`a:���bnbgcomplex���`a(���bmia0���`a,���`a ���`aN���`a)���`a]���`a
���`bZ1���`a ���aoa=���`a ���`bnp���aoa.���`cexp���`a(���aoa-���`aX���aoa*���aoa*���bmia2���`a ���aoa-���`a ���`aY���aoa*���aoa*���bmia2���`a)���`a
���`bZ2���`a ���aoa=���`a ���`bnp���aoa.���`cexp���`a(���aoa-���`a(���`aX���`a ���aoa-���`a ���bmia1���`a)���aoa*���aoa*���bmia2���`a ���aoa-���`a ���`a(���`aY���`a ���aoa-���`a ���bmia1���`a)���aoa*���aoa*���bmia2���`a)���`a
���`aZ���`a ���aoa=���`a ���`a(���`bZ1���`a ���aoa-���`a ���`bZ2���`a)���`a ���aoa*���`a ���bmia2���`a
���`a
���`cfig���`a,���`a ���`bax���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���bmia2���`a,���`a ���bmia1���`a)���`a
���`a
���`cpcm���`a ���aoa=���`a ���`bax���`a[���bmia0���`a]���aoa.���`jpcolormesh���`a(���`aX���`a,���`a ���`aY���`a,���`a ���`aZ���`a,���`a
���`w                       ���`dnorm���aoa=���`fcolors���aoa.���`jSymLogNorm���`a(���`ilinthresh���aoa=���bmfd0.03���`a,���`a ���`hlinscale���aoa=���bmfd0.03���`a,���`a
���`x.                                              ���`dvmin���aoa=���aoa-���bmfc1.0���`a,���`a ���`dvmax���aoa=���bmfc1.0���`a,���`a ���`dbase���aoa=���bmib10���`a)���`a,���`a
���`w                       ���`dcmap���aoa=���bs1a'���bs1fRdBu_r���bs1a'���`a,���`a ���`gshading���aoa=���bs1a'���bs1gnearest���bs1a'���`a)���`a
���`cfig���aoa.���`hcolorbar���`a(���`cpcm���`a,���`a ���`bax���aoa=���`bax���`a[���bmia0���`a]���`a,���`a ���`fextend���aoa=���bs1a'���bs1dboth���bs1a'���`a)���`a
���`a
���`cpcm���`a ���aoa=���`a ���`bax���`a[���bmia1���`a]���aoa.���`jpcolormesh���`a(���`aX���`a,���`a ���`aY���`a,���`a ���`aZ���`a,���`a ���`dcmap���aoa=���bs1a'���bs1fRdBu_r���bs1a'���`a,���`a ���`dvmin���aoa=���aoa-���`bnp���aoa.���`cmax���`a(���`aZ���`a)���`a,���`a
���`w                       ���`gshading���aoa=���bs1a'���bs1gnearest���bs1a'���`a)���`a
���`cfig���aoa.���`hcolorbar���`a(���`cpcm���`a,���`a ���`bax���aoa=���`bax���`a[���bmia1���`a]���`a,���`a ���`fextend���aoa=���bs1a'���bs1dboth���bs1a'���`a)���`a
���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
`dNone�