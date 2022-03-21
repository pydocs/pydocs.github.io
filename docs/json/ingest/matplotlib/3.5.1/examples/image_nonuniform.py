��������\���bsdx�"""
================
Image Nonuniform
================

This illustrates the NonUniformImage class.  It is not
available via an Axes method but it is easily added to an
Axes instance as shown here.
"""���`a
���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���bkndfrom���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnneimage���`a ���bknfimport���`a ���`oNonUniformImage���`a
���bkndfrom���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����`a ���bknfimport���`a ���`bcm���`a
���`a
���`finterp���`a ���aoa=���`a ���bs1a'���bs1gnearest���bs1a'���`a
���`a
���bc1x"# Linear x array for cell centers:���`a
���`ax���`a ���aoa=���`a ���`bnp���aoa.���`hlinspace���`a(���aoa-���bmia4���`a,���`a ���bmia4���`a,���`a ���bmia9���`a)���`a
���`a
���bc1x# Highly nonlinear x array:���`a
���`bx2���`a ���aoa=���`a ���`ax���aoa*���aoa*���bmia3���`a
���`a
���`ay���`a ���aoa=���`a ���`bnp���aoa.���`hlinspace���`a(���aoa-���bmia4���`a,���`a ���bmia4���`a,���`a ���bmia9���`a)���`a
���`a
���`az���`a ���aoa=���`a ���`bnp���aoa.���`dsqrt���`a(���`ax���`a[���`bnp���aoa.���`gnewaxis���`a,���`a ���`a:���`a]���aoa*���aoa*���bmia2���`a ���aoa+���`a ���`ay���`a[���`a:���`a,���`a ���`bnp���aoa.���`gnewaxis���`a]���aoa*���aoa*���bmia2���`a)���`a
���`a
���`cfig���`a,���`a ���`caxs���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`enrows���aoa=���bmia2���`a,���`a ���`encols���aoa=���bmia2���`a,���`a ���`rconstrained_layout���aoa=���bkcdTrue���`a)���`a
���`cfig���aoa.���`hsuptitle���`a(���bs1a'���bs1uNonUniformImage class���bs1a'���`a,���`a ���`hfontsize���aoa=���bs1a'���bs1elarge���bs1a'���`a)���`a
���`bax���`a ���aoa=���`a ���`caxs���`a[���bmia0���`a,���`a ���bmia0���`a]���`a
���`bim���`a ���aoa=���`a ���`oNonUniformImage���`a(���`bax���`a,���`a ���`minterpolation���aoa=���`finterp���`a,���`a ���`fextent���aoa=���`a(���aoa-���bmia4���`a,���`a ���bmia4���`a,���`a ���aoa-���bmia4���`a,���`a ���bmia4���`a)���`a,���`a
���`u                     ���`dcmap���aoa=���`bcm���aoa.���`gPurples���`a)���`a
���`bim���aoa.���`hset_data���`a(���`ax���`a,���`a ���`ay���`a,���`a ���`az���`a)���`a
���`bax���aoa.���`iadd_image���`a(���`bim���`a)���`a
���`bax���aoa.���`hset_xlim���`a(���aoa-���bmia4���`a,���`a ���bmia4���`a)���`a
���`bax���aoa.���`hset_ylim���`a(���aoa-���bmia4���`a,���`a ���bmia4���`a)���`a
���`bax���aoa.���`iset_title���`a(���`finterp���`a)���`a
���`a
���`bax���`a ���aoa=���`a ���`caxs���`a[���bmia0���`a,���`a ���bmia1���`a]���`a
���`bim���`a ���aoa=���`a ���`oNonUniformImage���`a(���`bax���`a,���`a ���`minterpolation���aoa=���`finterp���`a,���`a ���`fextent���aoa=���`a(���aoa-���bmib64���`a,���`a ���bmib64���`a,���`a ���aoa-���bmia4���`a,���`a ���bmia4���`a)���`a,���`a
���`u                     ���`dcmap���aoa=���`bcm���aoa.���`gPurples���`a)���`a
���`bim���aoa.���`hset_data���`a(���`bx2���`a,���`a ���`ay���`a,���`a ���`az���`a)���`a
���`bax���aoa.���`iadd_image���`a(���`bim���`a)���`a
���`bax���aoa.���`hset_xlim���`a(���aoa-���bmib64���`a,���`a ���bmib64���`a)���`a
���`bax���aoa.���`hset_ylim���`a(���aoa-���bmia4���`a,���`a ���bmia4���`a)���`a
���`bax���aoa.���`iset_title���`a(���`finterp���`a)���`a
���`a
���`finterp���`a ���aoa=���`a ���bs1a'���bs1hbilinear���bs1a'���`a
���`a
���`bax���`a ���aoa=���`a ���`caxs���`a[���bmia1���`a,���`a ���bmia0���`a]���`a
���`bim���`a ���aoa=���`a ���`oNonUniformImage���`a(���`bax���`a,���`a ���`minterpolation���aoa=���`finterp���`a,���`a ���`fextent���aoa=���`a(���aoa-���bmia4���`a,���`a ���bmia4���`a,���`a ���aoa-���bmia4���`a,���`a ���bmia4���`a)���`a,���`a
���`u                     ���`dcmap���aoa=���`bcm���aoa.���`gPurples���`a)���`a
���`bim���aoa.���`hset_data���`a(���`ax���`a,���`a ���`ay���`a,���`a ���`az���`a)���`a
���`bax���aoa.���`iadd_image���`a(���`bim���`a)���`a
���`bax���aoa.���`hset_xlim���`a(���aoa-���bmia4���`a,���`a ���bmia4���`a)���`a
���`bax���aoa.���`hset_ylim���`a(���aoa-���bmia4���`a,���`a ���bmia4���`a)���`a
���`bax���aoa.���`iset_title���`a(���`finterp���`a)���`a
���`a
���`bax���`a ���aoa=���`a ���`caxs���`a[���bmia1���`a,���`a ���bmia1���`a]���`a
���`bim���`a ���aoa=���`a ���`oNonUniformImage���`a(���`bax���`a,���`a ���`minterpolation���aoa=���`finterp���`a,���`a ���`fextent���aoa=���`a(���aoa-���bmib64���`a,���`a ���bmib64���`a,���`a ���aoa-���bmia4���`a,���`a ���bmia4���`a)���`a,���`a
���`u                     ���`dcmap���aoa=���`bcm���aoa.���`gPurples���`a)���`a
���`bim���aoa.���`hset_data���`a(���`bx2���`a,���`a ���`ay���`a,���`a ���`az���`a)���`a
���`bax���aoa.���`iadd_image���`a(���`bim���`a)���`a
���`bax���aoa.���`hset_xlim���`a(���aoa-���bmib64���`a,���`a ���bmib64���`a)���`a
���`bax���aoa.���`hset_ylim���`a(���aoa-���bmia4���`a,���`a ���bmia4���`a)���`a
���`bax���aoa.���`iset_title���`a(���`finterp���`a)���`a
���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
`dNone�