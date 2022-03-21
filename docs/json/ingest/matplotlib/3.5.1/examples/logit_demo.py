������������bsdxX"""
================
Logit Demo
================

Examples of plots with logit axes.
"""���`a
���`a
���bknfimport���`a ���bnndmath���`a
���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���`a
���`dxmax���`a ���aoa=���`a ���bmib10���`a
���`ax���`a ���aoa=���`a ���`bnp���aoa.���`hlinspace���`a(���aoa-���`dxmax���`a,���`a ���`dxmax���`a,���`a ���bmie10000���`a)���`a
���`hcdf_norm���`a ���aoa=���`a ���`a[���`dmath���aoa.���`cerf���`a(���`aw���`a ���aoa/���`a ���`bnp���aoa.���`dsqrt���`a(���bmia2���`a)���`a)���`a ���aoa/���`a ���bmia2���`a ���aoa+���`a ���bmia1���`a ���aoa/���`a ���bmia2���`a ���akcfor���`a ���`aw���`a ���bowbin���`a ���`ax���`a]���`a
���`mcdf_laplacian���`a ���aoa=���`a ���`bnp���aoa.���`ewhere���`a(���`ax���`a ���aoa<���`a ���bmia0���`a,���`a ���bmia1���`a ���aoa/���`a ���bmia2���`a ���aoa*���`a ���`bnp���aoa.���`cexp���`a(���`ax���`a)���`a,���`a ���bmia1���`a ���aoa-���`a ���bmia1���`a ���aoa/���`a ���bmia2���`a ���aoa*���`a ���`bnp���aoa.���`cexp���`a(���aoa-���`ax���`a)���`a)���`a
���`jcdf_cauchy���`a ���aoa=���`a ���`bnp���aoa.���`farctan���`a(���`ax���`a)���`a ���aoa/���`a ���`bnp���aoa.���`bpi���`a ���aoa+���`a ���bmia1���`a ���aoa/���`a ���bmia2���`a
���`a
���`cfig���`a,���`a ���`caxs���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`enrows���aoa=���bmia3���`a,���`a ���`encols���aoa=���bmia2���`a,���`a ���`gfigsize���aoa=���`a(���bmfc6.4���`a,���`a ���bmfc8.5���`a)���`a)���`a
���`a
���bc1xG# Common part, for the example, we will do the same plots on all graphs���`a
���akcfor���`a ���`ai���`a ���bowbin���`a ���bnberange���`a(���bmia3���`a)���`a:���`a
���`d    ���akcfor���`a ���`aj���`a ���bowbin���`a ���bnberange���`a(���bmia2���`a)���`a:���`a
���`h        ���`caxs���`a[���`ai���`a,���`a ���`aj���`a]���aoa.���`dplot���`a(���`ax���`a,���`a ���`hcdf_norm���`a,���`a ���`elabel���aoa=���bsaar���bs2a"���bs2a$���bs2a\���bs2gmathcal���bsic{N}���bs2a$���bs2a"���`a)���`a
���`h        ���`caxs���`a[���`ai���`a,���`a ���`aj���`a]���aoa.���`dplot���`a(���`ax���`a,���`a ���`mcdf_laplacian���`a,���`a ���`elabel���aoa=���bsaar���bs2a"���bs2a$���bs2a\���bs2gmathcal���bsic{L}���bs2a$���bs2a"���`a)���`a
���`h        ���`caxs���`a[���`ai���`a,���`a ���`aj���`a]���aoa.���`dplot���`a(���`ax���`a,���`a ���`jcdf_cauchy���`a,���`a ���`elabel���aoa=���bs2a"���bs2fCauchy���bs2a"���`a)���`a
���`h        ���`caxs���`a[���`ai���`a,���`a ���`aj���`a]���aoa.���`flegend���`a(���`a)���`a
���`h        ���`caxs���`a[���`ai���`a,���`a ���`aj���`a]���aoa.���`dgrid���`a(���`a)���`a
���`a
���bc1x0# First line, logitscale, with standard notation���`a
���`caxs���`a[���bmia0���`a,���`a ���bmia0���`a]���aoa.���`cset���`a(���`etitle���aoa=���bs2a"���bs2klogit scale���bs2a"���`a)���`a
���`caxs���`a[���bmia0���`a,���`a ���bmia0���`a]���aoa.���`jset_yscale���`a(���bs2a"���bs2elogit���bs2a"���`a)���`a
���`caxs���`a[���bmia0���`a,���`a ���bmia0���`a]���aoa.���`hset_ylim���`a(���bmfd1e-5���`a,���`a ���bmia1���`a ���aoa-���`a ���bmfd1e-5���`a)���`a
���`a
���`caxs���`a[���bmia0���`a,���`a ���bmia1���`a]���aoa.���`cset���`a(���`etitle���aoa=���bs2a"���bs2klogit scale���bs2a"���`a)���`a
���`caxs���`a[���bmia0���`a,���`a ���bmia1���`a]���aoa.���`jset_yscale���`a(���bs2a"���bs2elogit���bs2a"���`a)���`a
���`caxs���`a[���bmia0���`a,���`a ���bmia1���`a]���aoa.���`hset_xlim���`a(���bmia0���`a,���`a ���`dxmax���`a)���`a
���`caxs���`a[���bmia0���`a,���`a ���bmia1���`a]���aoa.���`hset_ylim���`a(���bmfc0.8���`a,���`a ���bmia1���`a ���aoa-���`a ���bmfd5e-3���`a)���`a
���`a
���bc1xL# Second line, logitscale, with survival notation (with `use_overline`), and���`a
���bc1x# other format display 1/2���`a
���`caxs���`a[���bmia1���`a,���`a ���bmia0���`a]���aoa.���`cset���`a(���`etitle���aoa=���bs2a"���bs2klogit scale���bs2a"���`a)���`a
���`caxs���`a[���bmia1���`a,���`a ���bmia0���`a]���aoa.���`jset_yscale���`a(���bs2a"���bs2elogit���bs2a"���`a,���`a ���`hone_half���aoa=���bs2a"���bs2c1/2���bs2a"���`a,���`a ���`luse_overline���aoa=���bkcdTrue���`a)���`a
���`caxs���`a[���bmia1���`a,���`a ���bmia0���`a]���aoa.���`hset_ylim���`a(���bmfd1e-5���`a,���`a ���bmia1���`a ���aoa-���`a ���bmfd1e-5���`a)���`a
���`a
���`caxs���`a[���bmia1���`a,���`a ���bmia1���`a]���aoa.���`cset���`a(���`etitle���aoa=���bs2a"���bs2klogit scale���bs2a"���`a)���`a
���`caxs���`a[���bmia1���`a,���`a ���bmia1���`a]���aoa.���`jset_yscale���`a(���bs2a"���bs2elogit���bs2a"���`a,���`a ���`hone_half���aoa=���bs2a"���bs2c1/2���bs2a"���`a,���`a ���`luse_overline���aoa=���bkcdTrue���`a)���`a
���`caxs���`a[���bmia1���`a,���`a ���bmia1���`a]���aoa.���`hset_xlim���`a(���bmia0���`a,���`a ���`dxmax���`a)���`a
���`caxs���`a[���bmia1���`a,���`a ���bmia1���`a]���aoa.���`hset_ylim���`a(���bmfc0.8���`a,���`a ���bmia1���`a ���aoa-���`a ���bmfd5e-3���`a)���`a
���`a
���bc1x# Third line, linear scale���`a
���`caxs���`a[���bmia2���`a,���`a ���bmia0���`a]���aoa.���`cset���`a(���`etitle���aoa=���bs2a"���bs2llinear scale���bs2a"���`a)���`a
���`caxs���`a[���bmia2���`a,���`a ���bmia0���`a]���aoa.���`hset_ylim���`a(���bmia0���`a,���`a ���bmia1���`a)���`a
���`a
���`caxs���`a[���bmia2���`a,���`a ���bmia1���`a]���aoa.���`cset���`a(���`etitle���aoa=���bs2a"���bs2llinear scale���bs2a"���`a)���`a
���`caxs���`a[���bmia2���`a,���`a ���bmia1���`a]���aoa.���`hset_xlim���`a(���bmia0���`a,���`a ���`dxmax���`a)���`a
���`caxs���`a[���bmia2���`a,���`a ���bmia1���`a]���aoa.���`hset_ylim���`a(���bmfc0.8���`a,���`a ���bmia1���`a)���`a
���`a
���`cfig���aoa.���`ltight_layout���`a(���`a)���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
`dNone�