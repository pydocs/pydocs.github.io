��������j���bsdx�"""
=======================
Colormap Normalizations
=======================

Demonstration of using norm to map colormaps onto data in non-linear ways.
"""���`a
���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfcolors���`a ���akbas���`a ���bnnfcolors���`a
���`a
���bc1xO###############################################################################���`a
���bc1xG# Lognorm: Instead of pcolor log10(Z1) you can have colorbars that have���`a
���bc1x&# the exponential labels using a norm.���`a
���`a
���`aN���`a ���aoa=���`a ���bmic100���`a
���`aX���`a,���`a ���`aY���`a ���aoa=���`a ���`bnp���aoa.���`emgrid���`a[���aoa-���bmia3���`a:���bmia3���`a:���bnbgcomplex���`a(���bmia0���`a,���`a ���`aN���`a)���`a,���`a ���aoa-���bmia2���`a:���bmia2���`a:���bnbgcomplex���`a(���bmia0���`a,���`a ���`aN���`a)���`a]���`a
���`a
���bc1x?# A low hump with a spike coming out of the top.  Needs to have���`a
���bc1xE# z/colour axis on a log scale so we see both hump and spike.  linear���`a
���bc1x# scale only shows the spike.���`a
���`a
���`bZ1���`a ���aoa=���`a ���`bnp���aoa.���`cexp���`a(���aoa-���`aX���aoa*���aoa*���bmia2���`a ���aoa-���`a ���`aY���aoa*���aoa*���bmia2���`a)���`a
���`bZ2���`a ���aoa=���`a ���`bnp���aoa.���`cexp���`a(���aoa-���`a(���`aX���`a ���aoa*���`a ���bmib10���`a)���aoa*���aoa*���bmia2���`a ���aoa-���`a ���`a(���`aY���`a ���aoa*���`a ���bmib10���`a)���aoa*���aoa*���bmia2���`a)���`a
���`aZ���`a ���aoa=���`a ���`bZ1���`a ���aoa+���`a ���bmib50���`a ���aoa*���`a ���`bZ2���`a
���`a
���`cfig���`a,���`a ���`bax���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���bmia2���`a,���`a ���bmia1���`a)���`a
���`a
���`cpcm���`a ���aoa=���`a ���`bax���`a[���bmia0���`a]���aoa.���`fpcolor���`a(���`aX���`a,���`a ���`aY���`a,���`a ���`aZ���`a,���`a
���`s                   ���`dnorm���aoa=���`fcolors���aoa.���`gLogNorm���`a(���`dvmin���aoa=���`aZ���aoa.���`cmin���`a(���`a)���`a,���`a ���`dvmax���aoa=���`aZ���aoa.���`cmax���`a(���`a)���`a)���`a,���`a
���`s                   ���`dcmap���aoa=���bs1a'���bs1fPuBu_r���bs1a'���`a,���`a ���`gshading���aoa=���bs1a'���bs1gnearest���bs1a'���`a)���`a
���`cfig���aoa.���`hcolorbar���`a(���`cpcm���`a,���`a ���`bax���aoa=���`bax���`a[���bmia0���`a]���`a,���`a ���`fextend���aoa=���bs1a'���bs1cmax���bs1a'���`a)���`a
���`a
���`cpcm���`a ���aoa=���`a ���`bax���`a[���bmia1���`a]���aoa.���`fpcolor���`a(���`aX���`a,���`a ���`aY���`a,���`a ���`aZ���`a,���`a ���`dcmap���aoa=���bs1a'���bs1fPuBu_r���bs1a'���`a,���`a ���`gshading���aoa=���bs1a'���bs1gnearest���bs1a'���`a)���`a
���`cfig���aoa.���`hcolorbar���`a(���`cpcm���`a,���`a ���`bax���aoa=���`bax���`a[���bmia1���`a]���`a,���`a ���`fextend���aoa=���bs1a'���bs1cmax���bs1a'���`a)���`a
���`a
���`a
���bc1xO###############################################################################���`a
���bc1xG# PowerNorm: Here a power-law trend in X partially obscures a rectified���`a
���bc1x@# sine wave in Y. We can remove the power law using a PowerNorm.���`a
���`a
���`aX���`a,���`a ���`aY���`a ���aoa=���`a ���`bnp���aoa.���`emgrid���`a[���bmia0���`a:���bmia3���`a:���bnbgcomplex���`a(���bmia0���`a,���`a ���`aN���`a)���`a,���`a ���bmia0���`a:���bmia2���`a:���bnbgcomplex���`a(���bmia0���`a,���`a ���`aN���`a)���`a]���`a
���`bZ1���`a ���aoa=���`a ���`a(���bmia1���`a ���aoa+���`a ���`bnp���aoa.���`csin���`a(���`aY���`a ���aoa*���`a ���bmfc10.���`a)���`a)���`a ���aoa*���`a ���`aX���aoa*���aoa*���bmia2���`a
���`a
���`cfig���`a,���`a ���`bax���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���bmia2���`a,���`a ���bmia1���`a)���`a
���`a
���`cpcm���`a ���aoa=���`a ���`bax���`a[���bmia0���`a]���aoa.���`jpcolormesh���`a(���`aX���`a,���`a ���`aY���`a,���`a ���`bZ1���`a,���`a ���`dnorm���aoa=���`fcolors���aoa.���`iPowerNorm���`a(���`egamma���aoa=���bmfb1.���`a ���aoa/���`a ���bmfb2.���`a)���`a,���`a
���`w                       ���`dcmap���aoa=���bs1a'���bs1fPuBu_r���bs1a'���`a,���`a ���`gshading���aoa=���bs1a'���bs1gnearest���bs1a'���`a)���`a
���`cfig���aoa.���`hcolorbar���`a(���`cpcm���`a,���`a ���`bax���aoa=���`bax���`a[���bmia0���`a]���`a,���`a ���`fextend���aoa=���bs1a'���bs1cmax���bs1a'���`a)���`a
���`a
���`cpcm���`a ���aoa=���`a ���`bax���`a[���bmia1���`a]���aoa.���`jpcolormesh���`a(���`aX���`a,���`a ���`aY���`a,���`a ���`bZ1���`a,���`a ���`dcmap���aoa=���bs1a'���bs1fPuBu_r���bs1a'���`a,���`a ���`gshading���aoa=���bs1a'���bs1gnearest���bs1a'���`a)���`a
���`cfig���aoa.���`hcolorbar���`a(���`cpcm���`a,���`a ���`bax���aoa=���`bax���`a[���bmia1���`a]���`a,���`a ���`fextend���aoa=���bs1a'���bs1cmax���bs1a'���`a)���`a
���`a
���bc1xO###############################################################################���`a
���bc1xD# SymLogNorm: two humps, one negative and one positive, The positive���`a
���bc1xD# with 5-times the amplitude. Linearly, you cannot see detail in the���`a
���bc1x@# negative hump.  Here we logarithmically scale the positive and���`a
���bc1x# negative data separately.���`a
���bc1a#���`a
���bc1x># Note that colorbar labels do not come out looking very good.���`a
���`a
���`aX���`a,���`a ���`aY���`a ���aoa=���`a ���`bnp���aoa.���`emgrid���`a[���aoa-���bmia3���`a:���bmia3���`a:���bnbgcomplex���`a(���bmia0���`a,���`a ���`aN���`a)���`a,���`a ���aoa-���bmia2���`a:���bmia2���`a:���bnbgcomplex���`a(���bmia0���`a,���`a ���`aN���`a)���`a]���`a
���`bZ1���`a ���aoa=���`a ���bmia5���`a ���aoa*���`a ���`bnp���aoa.���`cexp���`a(���aoa-���`aX���aoa*���aoa*���bmia2���`a ���aoa-���`a ���`aY���aoa*���aoa*���bmia2���`a)���`a
���`bZ2���`a ���aoa=���`a ���`bnp���aoa.���`cexp���`a(���aoa-���`a(���`aX���`a ���aoa-���`a ���bmia1���`a)���aoa*���aoa*���bmia2���`a ���aoa-���`a ���`a(���`aY���`a ���aoa-���`a ���bmia1���`a)���aoa*���aoa*���bmia2���`a)���`a
���`aZ���`a ���aoa=���`a ���`a(���`bZ1���`a ���aoa-���`a ���`bZ2���`a)���`a ���aoa*���`a ���bmia2���`a
���`a
���`cfig���`a,���`a ���`bax���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���bmia2���`a,���`a ���bmia1���`a)���`a
���`a
���`cpcm���`a ���aoa=���`a ���`bax���`a[���bmia0���`a]���aoa.���`jpcolormesh���`a(���`aX���`a,���`a ���`aY���`a,���`a ���`bZ1���`a,���`a
���`w                       ���`dnorm���aoa=���`fcolors���aoa.���`jSymLogNorm���`a(���`ilinthresh���aoa=���bmfd0.03���`a,���`a ���`hlinscale���aoa=���bmfd0.03���`a,���`a
���`x.                                              ���`dvmin���aoa=���aoa-���bmfc1.0���`a,���`a ���`dvmax���aoa=���bmfc1.0���`a,���`a ���`dbase���aoa=���bmib10���`a)���`a,���`a
���`w                       ���`dcmap���aoa=���bs1a'���bs1fRdBu_r���bs1a'���`a,���`a ���`gshading���aoa=���bs1a'���bs1gnearest���bs1a'���`a)���`a
���`cfig���aoa.���`hcolorbar���`a(���`cpcm���`a,���`a ���`bax���aoa=���`bax���`a[���bmia0���`a]���`a,���`a ���`fextend���aoa=���bs1a'���bs1dboth���bs1a'���`a)���`a
���`a
���`cpcm���`a ���aoa=���`a ���`bax���`a[���bmia1���`a]���aoa.���`jpcolormesh���`a(���`aX���`a,���`a ���`aY���`a,���`a ���`bZ1���`a,���`a ���`dcmap���aoa=���bs1a'���bs1fRdBu_r���bs1a'���`a,���`a ���`dvmin���aoa=���aoa-���`bnp���aoa.���`cmax���`a(���`bZ1���`a)���`a,���`a
���`w                       ���`gshading���aoa=���bs1a'���bs1gnearest���bs1a'���`a)���`a
���`cfig���aoa.���`hcolorbar���`a(���`cpcm���`a,���`a ���`bax���aoa=���`bax���`a[���bmia1���`a]���`a,���`a ���`fextend���aoa=���bs1a'���bs1dboth���bs1a'���`a)���`a
���`a
���bc1xO###############################################################################���`a
���bc1xD# Custom Norm: An example with a customized normalization.  This one���`a
���bc1xF# uses the example above, and normalizes the negative data differently���`a
���bc1t# from the positive.���`a
���`a
���`aX���`a,���`a ���`aY���`a ���aoa=���`a ���`bnp���aoa.���`emgrid���`a[���aoa-���bmia3���`a:���bmia3���`a:���bnbgcomplex���`a(���bmia0���`a,���`a ���`aN���`a)���`a,���`a ���aoa-���bmia2���`a:���bmia2���`a:���bnbgcomplex���`a(���bmia0���`a,���`a ���`aN���`a)���`a]���`a
���`bZ1���`a ���aoa=���`a ���`bnp���aoa.���`cexp���`a(���aoa-���`aX���aoa*���aoa*���bmia2���`a ���aoa-���`a ���`aY���aoa*���aoa*���bmia2���`a)���`a
���`bZ2���`a ���aoa=���`a ���`bnp���aoa.���`cexp���`a(���aoa-���`a(���`aX���`a ���aoa-���`a ���bmia1���`a)���aoa*���aoa*���bmia2���`a ���aoa-���`a ���`a(���`aY���`a ���aoa-���`a ���bmia1���`a)���aoa*���aoa*���bmia2���`a)���`a
���`aZ���`a ���aoa=���`a ���`a(���`bZ1���`a ���aoa-���`a ���`bZ2���`a)���`a ���aoa*���`a ���bmia2���`a
���`a
���bc1x?# Example of making your own norm.  Also see matplotlib.colors.���`a
���bc1x># From Joe Kington: This one gives two different linear ramps:���`a
���`a
���`a
���akeclass���`a ���bncqMidpointNormalize���`a(���`fcolors���aoa.���`iNormalize���`a)���`a:���`a
���`d    ���akcdef���`a ���bfmh__init__���`a(���bbpdself���`a,���`a ���`dvmin���aoa=���bkcdNone���`a,���`a ���`dvmax���aoa=���bkcdNone���`a,���`a ���`hmidpoint���aoa=���bkcdNone���`a,���`a ���`dclip���aoa=���bkceFalse���`a)���`a:���`a
���`h        ���bbpdself���aoa.���`hmidpoint���`a ���aoa=���`a ���`hmidpoint���`a
���`h        ���bnbesuper���`a(���`a)���aoa.���bfmh__init__���`a(���`dvmin���`a,���`a ���`dvmax���`a,���`a ���`dclip���`a)���`a
���`a
���`d    ���akcdef���`a ���bfmh__call__���`a(���bbpdself���`a,���`a ���`evalue���`a,���`a ���`dclip���aoa=���bkcdNone���`a)���`a:���`a
���`h        ���bc1xB# I'm ignoring masked values and all kinds of edge cases to make a���`a
���`h        ���bc1s# simple example...���`a
���`h        ���`ax���`a,���`a ���`ay���`a ���aoa=���`a ���`a[���bbpdself���aoa.���`dvmin���`a,���`a ���bbpdself���aoa.���`hmidpoint���`a,���`a ���bbpdself���aoa.���`dvmax���`a]���`a,���`a ���`a[���bmia0���`a,���`a ���bmfc0.5���`a,���`a ���bmia1���`a]���`a
���`h        ���akfreturn���`a ���`bnp���aoa.���`bma���aoa.���`lmasked_array���`a(���`bnp���aoa.���`finterp���`a(���`evalue���`a,���`a ���`ax���`a,���`a ���`ay���`a)���`a)���`a
���`a
���`a
���bc1e#####���`a
���`cfig���`a,���`a ���`bax���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���bmia2���`a,���`a ���bmia1���`a)���`a
���`a
���`cpcm���`a ���aoa=���`a ���`bax���`a[���bmia0���`a]���aoa.���`jpcolormesh���`a(���`aX���`a,���`a ���`aY���`a,���`a ���`aZ���`a,���`a
���`w                       ���`dnorm���aoa=���`qMidpointNormalize���`a(���`hmidpoint���aoa=���bmfb0.���`a)���`a,���`a
���`w                       ���`dcmap���aoa=���bs1a'���bs1fRdBu_r���bs1a'���`a,���`a ���`gshading���aoa=���bs1a'���bs1gnearest���bs1a'���`a)���`a
���`cfig���aoa.���`hcolorbar���`a(���`cpcm���`a,���`a ���`bax���aoa=���`bax���`a[���bmia0���`a]���`a,���`a ���`fextend���aoa=���bs1a'���bs1dboth���bs1a'���`a)���`a
���`a
���`cpcm���`a ���aoa=���`a ���`bax���`a[���bmia1���`a]���aoa.���`jpcolormesh���`a(���`aX���`a,���`a ���`aY���`a,���`a ���`aZ���`a,���`a ���`dcmap���aoa=���bs1a'���bs1fRdBu_r���bs1a'���`a,���`a ���`dvmin���aoa=���aoa-���`bnp���aoa.���`cmax���`a(���`aZ���`a)���`a,���`a
���`w                       ���`gshading���aoa=���bs1a'���bs1gnearest���bs1a'���`a)���`a
���`cfig���aoa.���`hcolorbar���`a(���`cpcm���`a,���`a ���`bax���aoa=���`bax���`a[���bmia1���`a]���`a,���`a ���`fextend���aoa=���bs1a'���bs1dboth���bs1a'���`a)���`a
���`a
���bc1xO###############################################################################���`a
���bc1xH# BoundaryNorm: For this one you provide the boundaries for your colors,���`a
���bc1xB# and the Norm puts the first color in between the first pair, the���`a
���bc1x,# second color between the second pair, etc.���`a
���`a
���`cfig���`a,���`a ���`bax���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���bmia3���`a,���`a ���bmia1���`a,���`a ���`gfigsize���aoa=���`a(���bmia8���`a,���`a ���bmia8���`a)���`a)���`a
���`bax���`a ���aoa=���`a ���`bax���aoa.���`gflatten���`a(���`a)���`a
���bc1x)# even bounds gives a contour-like effect���`a
���`fbounds���`a ���aoa=���`a ���`bnp���aoa.���`hlinspace���`a(���aoa-���bmia1���`a,���`a ���bmia1���`a,���`a ���bmib10���`a)���`a
���`dnorm���`a ���aoa=���`a ���`fcolors���aoa.���`lBoundaryNorm���`a(���`jboundaries���aoa=���`fbounds���`a,���`a ���`gncolors���aoa=���bmic256���`a)���`a
���`cpcm���`a ���aoa=���`a ���`bax���`a[���bmia0���`a]���aoa.���`jpcolormesh���`a(���`aX���`a,���`a ���`aY���`a,���`a ���`aZ���`a,���`a
���`w                       ���`dnorm���aoa=���`dnorm���`a,���`a
���`w                       ���`dcmap���aoa=���bs1a'���bs1fRdBu_r���bs1a'���`a,���`a ���`gshading���aoa=���bs1a'���bs1gnearest���bs1a'���`a)���`a
���`cfig���aoa.���`hcolorbar���`a(���`cpcm���`a,���`a ���`bax���aoa=���`bax���`a[���bmia0���`a]���`a,���`a ���`fextend���aoa=���bs1a'���bs1dboth���bs1a'���`a,���`a ���`korientation���aoa=���bs1a'���bs1hvertical���bs1a'���`a)���`a
���`a
���bc1x)# uneven bounds changes the colormapping:���`a
���`fbounds���`a ���aoa=���`a ���`bnp���aoa.���`earray���`a(���`a[���aoa-���bmfd0.25���`a,���`a ���aoa-���bmfe0.125���`a,���`a ���bmia0���`a,���`a ���bmfc0.5���`a,���`a ���bmia1���`a]���`a)���`a
���`dnorm���`a ���aoa=���`a ���`fcolors���aoa.���`lBoundaryNorm���`a(���`jboundaries���aoa=���`fbounds���`a,���`a ���`gncolors���aoa=���bmic256���`a)���`a
���`cpcm���`a ���aoa=���`a ���`bax���`a[���bmia1���`a]���aoa.���`jpcolormesh���`a(���`aX���`a,���`a ���`aY���`a,���`a ���`aZ���`a,���`a ���`dnorm���aoa=���`dnorm���`a,���`a ���`dcmap���aoa=���bs1a'���bs1fRdBu_r���bs1a'���`a,���`a ���`gshading���aoa=���bs1a'���bs1gnearest���bs1a'���`a)���`a
���`cfig���aoa.���`hcolorbar���`a(���`cpcm���`a,���`a ���`bax���aoa=���`bax���`a[���bmia1���`a]���`a,���`a ���`fextend���aoa=���bs1a'���bs1dboth���bs1a'���`a,���`a ���`korientation���aoa=���bs1a'���bs1hvertical���bs1a'���`a)���`a
���`a
���`cpcm���`a ���aoa=���`a ���`bax���`a[���bmia2���`a]���aoa.���`jpcolormesh���`a(���`aX���`a,���`a ���`aY���`a,���`a ���`aZ���`a,���`a ���`dcmap���aoa=���bs1a'���bs1fRdBu_r���bs1a'���`a,���`a ���`dvmin���aoa=���aoa-���`bnp���aoa.���`cmax���`a(���`bZ1���`a)���`a,���`a
���`w                       ���`gshading���aoa=���bs1a'���bs1gnearest���bs1a'���`a)���`a
���`cfig���aoa.���`hcolorbar���`a(���`cpcm���`a,���`a ���`bax���aoa=���`bax���`a[���bmia2���`a]���`a,���`a ���`fextend���aoa=���bs1a'���bs1dboth���bs1a'���`a,���`a ���`korientation���aoa=���bs1a'���bs1hvertical���bs1a'���`a)���`a
���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
`dNone�