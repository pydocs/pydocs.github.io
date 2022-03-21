��������I���bsdy"""
====================
Errorbar subsampling
====================

The parameter *errorevery* of `.Axes.errorbar` can be used to draw error bars
only on a subset of data points. This is particularly useful if there are many
data points with similar errors.
"""���`a
���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���`a
���bc1n# example data���`a
���`ax���`a ���aoa=���`a ���`bnp���aoa.���`farange���`a(���bmfc0.1���`a,���`a ���bmia4���`a,���`a ���bmfc0.1���`a)���`a
���`by1���`a ���aoa=���`a ���`bnp���aoa.���`cexp���`a(���aoa-���bmfc1.0���`a ���aoa*���`a ���`ax���`a)���`a
���`by2���`a ���aoa=���`a ���`bnp���aoa.���`cexp���`a(���aoa-���bmfc0.5���`a ���aoa*���`a ���`ax���`a)���`a
���`a
���bc1x## example variable error bar values���`a
���`ey1err���`a ���aoa=���`a ���bmfc0.1���`a ���aoa+���`a ���bmfc0.1���`a ���aoa*���`a ���`bnp���aoa.���`dsqrt���`a(���`ax���`a)���`a
���`ey2err���`a ���aoa=���`a ���bmfc0.1���`a ���aoa+���`a ���bmfc0.1���`a ���aoa*���`a ���`bnp���aoa.���`dsqrt���`a(���`ax���aoa/���bmia2���`a)���`a
���`a
���`a
���`cfig���`a,���`a ���`a(���`cax0���`a,���`a ���`cax1���`a,���`a ���`cax2���`a)���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`enrows���aoa=���bmia1���`a,���`a ���`encols���aoa=���bmia3���`a,���`a ���`fsharex���aoa=���bkcdTrue���`a,���`a
���`x$                                    ���`gfigsize���aoa=���`a(���bmib12���`a,���`a ���bmia6���`a)���`a)���`a
���`a
���`cax0���aoa.���`iset_title���`a(���bs1a'���bs1mall errorbars���bs1a'���`a)���`a
���`cax0���aoa.���`herrorbar���`a(���`ax���`a,���`a ���`by1���`a,���`a ���`dyerr���aoa=���`ey1err���`a)���`a
���`cax0���aoa.���`herrorbar���`a(���`ax���`a,���`a ���`by2���`a,���`a ���`dyerr���aoa=���`ey2err���`a)���`a
���`a
���`cax1���aoa.���`iset_title���`a(���bs1a'���bs1wonly every 6th errorbar���bs1a'���`a)���`a
���`cax1���aoa.���`herrorbar���`a(���`ax���`a,���`a ���`by1���`a,���`a ���`dyerr���aoa=���`ey1err���`a,���`a ���`jerrorevery���aoa=���bmia6���`a)���`a
���`cax1���aoa.���`herrorbar���`a(���`ax���`a,���`a ���`by2���`a,���`a ���`dyerr���aoa=���`ey2err���`a,���`a ���`jerrorevery���aoa=���bmia6���`a)���`a
���`a
���`cax2���aoa.���`iset_title���`a(���bs1a'���bs1xsecond series shifted by 3���bs1a'���`a)���`a
���`cax2���aoa.���`herrorbar���`a(���`ax���`a,���`a ���`by1���`a,���`a ���`dyerr���aoa=���`ey1err���`a,���`a ���`jerrorevery���aoa=���`a(���bmia0���`a,���`a ���bmia6���`a)���`a)���`a
���`cax2���aoa.���`herrorbar���`a(���`ax���`a,���`a ���`by2���`a,���`a ���`dyerr���aoa=���`ey2err���`a,���`a ���`jerrorevery���aoa=���`a(���bmia3���`a,���`a ���bmia6���`a)���`a)���`a
���`a
���`cfig���aoa.���`hsuptitle���`a(���bs1a'���bs1tErrorbar subsampling���bs1a'���`a)���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
`dNone�