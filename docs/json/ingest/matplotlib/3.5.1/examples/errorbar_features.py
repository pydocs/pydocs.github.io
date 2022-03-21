������������bsdy�"""
=======================================
Different ways of specifying error bars
=======================================

Errors can be specified as a constant value (as shown in
:doc:`/gallery/statistics/errorbar`). However, this example demonstrates
how they vary by specifying arrays of error values.

If the raw ``x`` and ``y`` data have length N, there are two options:

Array of shape (N,):
    Error varies for each point, but the error values are
    symmetric (i.e. the lower and upper values are equal).

Array of shape (2, N):
    Error varies for each point, and the lower and upper limits
    (in that order) are different (asymmetric case)

In addition, this example demonstrates how to use log
scale with error bars.
"""���`a
���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���`a
���bc1n# example data���`a
���`ax���`a ���aoa=���`a ���`bnp���aoa.���`farange���`a(���bmfc0.1���`a,���`a ���bmia4���`a,���`a ���bmfc0.5���`a)���`a
���`ay���`a ���aoa=���`a ���`bnp���aoa.���`cexp���`a(���aoa-���`ax���`a)���`a
���`a
���bc1x4# example error bar values that vary with x-position���`a
���`eerror���`a ���aoa=���`a ���bmfc0.1���`a ���aoa+���`a ���bmfc0.2���`a ���aoa*���`a ���`ax���`a
���`a
���`cfig���`a,���`a ���`a(���`cax0���`a,���`a ���`cax1���`a)���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`enrows���aoa=���bmia2���`a,���`a ���`fsharex���aoa=���bkcdTrue���`a)���`a
���`cax0���aoa.���`herrorbar���`a(���`ax���`a,���`a ���`ay���`a,���`a ���`dyerr���aoa=���`eerror���`a,���`a ���`cfmt���aoa=���bs1a'���bs1b-o���bs1a'���`a)���`a
���`cax0���aoa.���`iset_title���`a(���bs1a'���bs1xvariable, symmetric error���bs1a'���`a)���`a
���`a
���bc1x/# error bar values w/ different -/+ errors that���`a
���bc1x# also vary with the x-position���`a
���`klower_error���`a ���aoa=���`a ���bmfc0.4���`a ���aoa*���`a ���`eerror���`a
���`kupper_error���`a ���aoa=���`a ���`eerror���`a
���`pasymmetric_error���`a ���aoa=���`a ���`a[���`klower_error���`a,���`a ���`kupper_error���`a]���`a
���`a
���`cax1���aoa.���`herrorbar���`a(���`ax���`a,���`a ���`ay���`a,���`a ���`dxerr���aoa=���`pasymmetric_error���`a,���`a ���`cfmt���aoa=���bs1a'���bs1ao���bs1a'���`a)���`a
���`cax1���aoa.���`iset_title���`a(���bs1a'���bs1xvariable, asymmetric error���bs1a'���`a)���`a
���`cax1���aoa.���`jset_yscale���`a(���bs1a'���bs1clog���bs1a'���`a)���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
���`a
���bc1xM#############################################################################���`a
���bc1a#���`a
���bc1x# .. admonition:: References���`a
���bc1a#���`a
���bc1xN#    The use of the following functions, methods, classes and modules is shown���`a
���bc1u#    in this example:���`a
���bc1a#���`a
���bc1xE#    - `matplotlib.axes.Axes.errorbar` / `matplotlib.pyplot.errorbar`���`a
`dNone�