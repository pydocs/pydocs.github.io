������������bsdy�"""
===================================
Shaded & power normalized rendering
===================================

The Mandelbrot set rendering can be improved by using a normalized recount
associated with a power normalized colormap (gamma=0.3). Rendering can be
further enhanced thanks to shading.

The ``maxiter`` gives the precision of the computation. ``maxiter=200`` should
take a few seconds on most modern laptops.
"""���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���`a
���`a
���akcdef���`a ���bnfnmandelbrot_set���`a(���`dxmin���`a,���`a ���`dxmax���`a,���`a ���`dymin���`a,���`a ���`dymax���`a,���`a ���`bxn���`a,���`a ���`byn���`a,���`a ���`gmaxiter���`a,���`a ���`ghorizon���aoa=���bmfc2.0���`a)���`a:���`a
���`d    ���`aX���`a ���aoa=���`a ���`bnp���aoa.���`hlinspace���`a(���`dxmin���`a,���`a ���`dxmax���`a,���`a ���`bxn���`a)���aoa.���`fastype���`a(���`bnp���aoa.���`gfloat32���`a)���`a
���`d    ���`aY���`a ���aoa=���`a ���`bnp���aoa.���`hlinspace���`a(���`dymin���`a,���`a ���`dymax���`a,���`a ���`byn���`a)���aoa.���`fastype���`a(���`bnp���aoa.���`gfloat32���`a)���`a
���`d    ���`aC���`a ���aoa=���`a ���`aX���`a ���aoa+���`a ���`aY���`a[���`a:���`a,���`a ���bkcdNone���`a]���`a ���aoa*���`a ���bmia1���`aj���`a
���`d    ���`aN���`a ���aoa=���`a ���`bnp���aoa.���`jzeros_like���`a(���`aC���`a,���`a ���`edtype���aoa=���bnbcint���`a)���`a
���`d    ���`aZ���`a ���aoa=���`a ���`bnp���aoa.���`jzeros_like���`a(���`aC���`a)���`a
���`d    ���akcfor���`a ���`an���`a ���bowbin���`a ���bnberange���`a(���`gmaxiter���`a)���`a:���`a
���`h        ���`aI���`a ���aoa=���`a ���bnbcabs���`a(���`aZ���`a)���`a ���aoa<���`a ���`ghorizon���`a
���`h        ���`aN���`a[���`aI���`a]���`a ���aoa=���`a ���`an���`a
���`h        ���`aZ���`a[���`aI���`a]���`a ���aoa=���`a ���`aZ���`a[���`aI���`a]���aoa*���aoa*���bmia2���`a ���aoa+���`a ���`aC���`a[���`aI���`a]���`a
���`d    ���`aN���`a[���`aN���`a ���aob==���`a ���`gmaxiter���aoa-���bmia1���`a]���`a ���aoa=���`a ���bmia0���`a
���`d    ���akfreturn���`a ���`aZ���`a,���`a ���`aN���`a
���`a
���`a
���akbif���`a ���bvmh__name__���`a ���aob==���`a ���bs1a'���bs1h__main__���bs1a'���`a:���`a
���`d    ���bknfimport���`a ���bnndtime���`a
���`d    ���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����`a
���`d    ���bkndfrom���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����`a ���bknfimport���`a ���`fcolors���`a
���`d    ���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���`a
���`d    ���`dxmin���`a,���`a ���`dxmax���`a,���`a ���`bxn���`a ���aoa=���`a ���aoa-���bmfd2.25���`a,���`a ���aoa+���bmfd0.75���`a,���`a ���bmid3000���`a ���aoa/���aoa/���`a ���bmia2���`a
���`d    ���`dymin���`a,���`a ���`dymax���`a,���`a ���`byn���`a ���aoa=���`a ���aoa-���bmfd1.25���`a,���`a ���aoa+���bmfd1.25���`a,���`a ���bmid2500���`a ���aoa/���aoa/���`a ���bmia2���`a
���`d    ���`gmaxiter���`a ���aoa=���`a ���bmic200���`a
���`d    ���`ghorizon���`a ���aoa=���`a ���bmfc2.0���`a ���aoa*���aoa*���`a ���bmib40���`a
���`d    ���`klog_horizon���`a ���aoa=���`a ���`bnp���aoa.���`dlog2���`a(���`bnp���aoa.���`clog���`a(���`ghorizon���`a)���`a)���`a
���`d    ���`aZ���`a,���`a ���`aN���`a ���aoa=���`a ���`nmandelbrot_set���`a(���`dxmin���`a,���`a ���`dxmax���`a,���`a ���`dymin���`a,���`a ���`dymax���`a,���`a ���`bxn���`a,���`a ���`byn���`a,���`a ���`gmaxiter���`a,���`a ���`ghorizon���`a)���`a
���`a
���`d    ���bc1x%# Normalized recount as explained in:���`a
���`d    ���bc1x2# https://linas.org/art-gallery/escape/smooth.html���`a
���`d    ���bc1x�# https://web.archive.org/web/20160331171238/https://www.ibm.com/developerworks/community/blogs/jfp/entry/My_Christmas_Gift?lang=en���`a
���`a
���`d    ���bc1xF# This line will generate warnings for null values but it is faster to���`a
���`d    ���bc1x.# process them afterwards using the nan_to_num���`a
���`d    ���akdwith���`a ���`bnp���aoa.���`herrstate���`a(���`ginvalid���aoa=���bs1a'���bs1fignore���bs1a'���`a)���`a:���`a
���`h        ���`aM���`a ���aoa=���`a ���`bnp���aoa.���`jnan_to_num���`a(���`aN���`a ���aoa+���`a ���bmia1���`a ���aoa-���`a ���`bnp���aoa.���`dlog2���`a(���`bnp���aoa.���`clog���`a(���bnbcabs���`a(���`aZ���`a)���`a)���`a)���`a ���aoa+���`a ���`klog_horizon���`a)���`a
���`a
���`d    ���`cdpi���`a ���aoa=���`a ���bmib72���`a
���`d    ���`ewidth���`a ���aoa=���`a ���bmib10���`a
���`d    ���`fheight���`a ���aoa=���`a ���bmib10���aoa*���`byn���aoa/���`bxn���`a
���`d    ���`cfig���`a ���aoa=���`a ���`cplt���aoa.���`ffigure���`a(���`gfigsize���aoa=���`a(���`ewidth���`a,���`a ���`fheight���`a)���`a,���`a ���`cdpi���aoa=���`cdpi���`a)���`a
���`d    ���`bax���`a ���aoa=���`a ���`cfig���aoa.���`hadd_axes���`a(���`a[���bmia0���`a,���`a ���bmia0���`a,���`a ���bmia1���`a,���`a ���bmia1���`a]���`a,���`a ���`gframeon���aoa=���bkceFalse���`a,���`a ���`faspect���aoa=���bmia1���`a)���`a
���`a
���`d    ���bc1r# Shaded rendering���`a
���`d    ���`elight���`a ���aoa=���`a ���`fcolors���aoa.���`kLightSource���`a(���`eazdeg���aoa=���bmic315���`a,���`a ���`faltdeg���aoa=���bmib10���`a)���`a
���`d    ���`aM���`a ���aoa=���`a ���`elight���aoa.���`eshade���`a(���`aM���`a,���`a ���`dcmap���aoa=���`cplt���aoa.���`bcm���aoa.���`chot���`a,���`a ���`ivert_exag���aoa=���bmfc1.5���`a,���`a
���`t                    ���`dnorm���aoa=���`fcolors���aoa.���`iPowerNorm���`a(���bmfc0.3���`a)���`a,���`a ���`jblend_mode���aoa=���bs1a'���bs1chsv���bs1a'���`a)���`a
���`d    ���`bax���aoa.���`fimshow���`a(���`aM���`a,���`a ���`fextent���aoa=���`a[���`dxmin���`a,���`a ���`dxmax���`a,���`a ���`dymin���`a,���`a ���`dymax���`a]���`a,���`a ���`minterpolation���aoa=���bs2a"���bs2gbicubic���bs2a"���`a)���`a
���`d    ���`bax���aoa.���`jset_xticks���`a(���`a[���`a]���`a)���`a
���`d    ���`bax���aoa.���`jset_yticks���`a(���`a[���`a]���`a)���`a
���`a
���`d    ���bc1x## Some advertisement for matplotlib���`a
���`d    ���`dyear���`a ���aoa=���`a ���`dtime���aoa.���`hstrftime���`a(���bs2a"���bs2a%���bs2aY���bs2a"���`a)���`a
���`d    ���`dtext���`a ���aoa=���`a ���`a(���bs2a"���bs2xThe Mandelbrot fractal set���bseb\n���bs2a"���`a
���`l            ���bs2a"���bs2xRendered with matplotlib ���bsib%s���bs2b, ���bsib%s���bs2x - https://matplotlib.org���bs2a"���`a
���`l            ���aoa%���`a ���`a(���`���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����aoa.���`k__version__���`a,���`a ���`dyear���`a)���`a)���`a
���`d    ���`bax���aoa.���`dtext���`a(���`dxmin���aoa+���bmfd.025���`a,���`a ���`dymin���aoa+���bmfd.025���`a,���`a ���`dtext���`a,���`a ���`ecolor���aoa=���bs2a"���bs2ewhite���bs2a"���`a,���`a ���`hfontsize���aoa=���bmib12���`a,���`a ���`ealpha���aoa=���bmfc0.5���`a)���`a
���`a
���`d    ���`cplt���aoa.���`dshow���`a(���`a)���`a
`dNone�