��������V���bsdx�"""
========================
Exploring normalizations
========================

Various normalization on a multivariate normal distribution.

"""���`a
���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfcolors���`a ���akbas���`a ���bnngmcolors���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���bkndfrom���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����bnna.���bnnfrandom���`a ���bknfimport���`a ���`smultivariate_normal���`a
���`a
���`a
���bc1x*# Fixing random state for reproducibility.���`a
���`bnp���aoa.���`frandom���aoa.���`dseed���`a(���bmih19680801���`a)���`a
���`a
���`ddata���`a ���aoa=���`a ���`bnp���aoa.���`fvstack���`a(���`a[���`a
���`d    ���`smultivariate_normal���`a(���`a[���bmib10���`a,���`a ���bmib10���`a]���`a,���`a ���`a[���`a[���bmia3���`a,���`a ���bmia2���`a]���`a,���`a ���`a[���bmia2���`a,���`a ���bmia3���`a]���`a]���`a,���`a ���`dsize���aoa=���bmif100000���`a)���`a,���`a
���`d    ���`smultivariate_normal���`a(���`a[���bmib30���`a,���`a ���bmib20���`a]���`a,���`a ���`a[���`a[���bmia3���`a,���`a ���bmia1���`a]���`a,���`a ���`a[���bmia1���`a,���`a ���bmia3���`a]���`a]���`a,���`a ���`dsize���aoa=���bmid1000���`a)���`a
���`a]���`a)���`a
���`a
���`fgammas���`a ���aoa=���`a ���`a[���bmfc0.8���`a,���`a ���bmfc0.5���`a,���`a ���bmfc0.3���`a]���`a
���`a
���`cfig���`a,���`a ���`caxs���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`enrows���aoa=���bmia2���`a,���`a ���`encols���aoa=���bmia2���`a)���`a
���`a
���`caxs���`a[���bmia0���`a,���`a ���bmia0���`a]���aoa.���`iset_title���`a(���bs1a'���bs1tLinear normalization���bs1a'���`a)���`a
���`caxs���`a[���bmia0���`a,���`a ���bmia0���`a]���aoa.���`fhist2d���`a(���`ddata���`a[���`a:���`a,���`a ���bmia0���`a]���`a,���`a ���`ddata���`a[���`a:���`a,���`a ���bmia1���`a]���`a,���`a ���`dbins���aoa=���bmic100���`a)���`a
���`a
���akcfor���`a ���`bax���`a,���`a ���`egamma���`a ���bowbin���`a ���bnbczip���`a(���`caxs���aoa.���`dflat���`a[���bmia1���`a:���`a]���`a,���`a ���`fgammas���`a)���`a:���`a
���`d    ���`bax���aoa.���`iset_title���`a(���bsaar���bs1a'���bs1lPower law $(���bs1a\���bs1fgamma=���bsie%1.1f���bs1b)$���bs1a'���`a ���aoa%���`a ���`egamma���`a)���`a
���`d    ���`bax���aoa.���`fhist2d���`a(���`ddata���`a[���`a:���`a,���`a ���bmia0���`a]���`a,���`a ���`ddata���`a[���`a:���`a,���`a ���bmia1���`a]���`a,���`a ���`dbins���aoa=���bmic100���`a,���`a ���`dnorm���aoa=���`gmcolors���aoa.���`iPowerNorm���`a(���`egamma���`a)���`a)���`a
���`a
���`cfig���aoa.���`ltight_layout���`a(���`a)���`a
���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
���`a
���bc1xM#############################################################################���`a
���bc1a#���`a
���bc1x# .. admonition:: References���`a
���bc1a#���`a
���bc1xN#    The use of the following functions, methods, classes and modules is shown���`a
���bc1u#    in this example:���`a
���bc1a#���`a
���bc1x#    - `matplotlib.colors`���`a
���bc1x$#    - `matplotlib.colors.PowerNorm`���`a
���bc1x$#    - `matplotlib.axes.Axes.hist2d`���`a
���bc1x!#    - `matplotlib.pyplot.hist2d`���`a
`dNone�