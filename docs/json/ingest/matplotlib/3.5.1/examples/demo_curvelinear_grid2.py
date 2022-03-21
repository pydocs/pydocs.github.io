��������?���bsdy3"""
======================
Demo CurveLinear Grid2
======================

Custom grid and ticklines.

This example demonstrates how to use GridHelperCurveLinear to define
custom grids and ticklines by applying a transformation on the grid.
As showcase on the plot, a 5x5 matrix is displayed on the axes.
"""���`a
���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���`a
���bkndfrom���`a ���bnnlmpl_toolkits���bnna.���bnnjaxisartist���bnna.���bnnwgrid_helper_curvelinear���`a ���bknfimport���`a ���`a(���`a
���`d    ���`uGridHelperCurveLinear���`a)���`a
���bkndfrom���`a ���bnnlmpl_toolkits���bnna.���bnnjaxisartist���bnna.���bnnkgrid_finder���`a ���bknfimport���`a ���`a(���`a
���`d    ���`sExtremeFinderSimple���`a,���`a ���`kMaxNLocator���`a)���`a
���bkndfrom���`a ���bnnlmpl_toolkits���bnna.���bnnjaxisartist���bnna.���bnniaxislines���`a ���bknfimport���`a ���`dAxes���`a
���`a
���`a
���akcdef���`a ���bnfqcurvelinear_test1���`a(���`cfig���`a)���`a:���`a
���`d    ���bsdx """Grid for custom transform."""���`a
���`a
���`d    ���akcdef���`a ���bnfbtr���`a(���`ax���`a,���`a ���`ay���`a)���`a:���`a
���`h        ���akfreturn���`a ���`bnp���aoa.���`dsign���`a(���`ax���`a)���aoa*���bnbcabs���`a(���`ax���`a)���aoa*���aoa*���bmfb.5���`a,���`a ���`ay���`a
���`a
���`d    ���akcdef���`a ���bnffinv_tr���`a(���`ax���`a,���`a ���`ay���`a)���`a:���`a
���`h        ���akfreturn���`a ���`bnp���aoa.���`dsign���`a(���`ax���`a)���aoa*���`ax���aoa*���aoa*���bmia2���`a,���`a ���`ay���`a
���`a
���`d    ���`kgrid_helper���`a ���aoa=���`a ���`uGridHelperCurveLinear���`a(���`a
���`h        ���`a(���`btr���`a,���`a ���`finv_tr���`a)���`a,���`a
���`h        ���`nextreme_finder���aoa=���`sExtremeFinderSimple���`a(���bmib20���`a,���`a ���bmib20���`a)���`a,���`a
���`h        ���bc1u# better tick density���`a
���`h        ���`mgrid_locator1���aoa=���`kMaxNLocator���`a(���`enbins���aoa=���bmia6���`a)���`a,���`a ���`mgrid_locator2���aoa=���`kMaxNLocator���`a(���`enbins���aoa=���bmia6���`a)���`a)���`a
���`a
���`d    ���`cax1���`a ���aoa=���`a ���`cfig���aoa.���`kadd_subplot���`a(���`jaxes_class���aoa=���`dAxes���`a,���`a ���`kgrid_helper���aoa=���`kgrid_helper���`a)���`a
���`d    ���bc1x:# ax1 will have a ticks and gridlines defined by the given���`a
���`d    ���bc1xJ# transform (+ transData of the Axes). Note that the transform of the Axes���`a
���`d    ���bc1xB# itself (i.e., transData) is not affected by the given transform.���`a
���`a
���`d    ���`cax1���aoa.���`fimshow���`a(���`bnp���aoa.���`farange���`a(���bmib25���`a)���aoa.���`greshape���`a(���bmia5���`a,���`a ���bmia5���`a)���`a,���`a
���`o               ���`dvmax���aoa=���bmib50���`a,���`a ���`dcmap���aoa=���`cplt���aoa.���`bcm���aoa.���`fgray_r���`a,���`a ���`forigin���aoa=���bs2a"���bs2elower���bs2a"���`a)���`a
���`a
���`a
���akbif���`a ���bvmh__name__���`a ���aob==���`a ���bs2a"���bs2h__main__���bs2a"���`a:���`a
���`d    ���`cfig���`a ���aoa=���`a ���`cplt���aoa.���`ffigure���`a(���`gfigsize���aoa=���`a(���bmia7���`a,���`a ���bmia4���`a)���`a)���`a
���`d    ���`qcurvelinear_test1���`a(���`cfig���`a)���`a
���`d    ���`cplt���aoa.���`dshow���`a(���`a)���`a
`dNone�