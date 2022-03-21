������������bsdyW"""
==================================
Modifying the coordinate formatter
==================================

Modify the coordinate formatter to report the image "z"
value of the nearest pixel given x and y.
This functionality is built in by default, but it
is still useful to show how to customize the
`~.axes.Axes.format_coord` function.
"""���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���`a
���bc1x)# Fixing random state for reproducibility���`a
���`bnp���aoa.���`frandom���aoa.���`dseed���`a(���bmih19680801���`a)���`a
���`a
���`a
���`aX���`a ���aoa=���`a ���bmib10���aoa*���`bnp���aoa.���`frandom���aoa.���`drand���`a(���bmia5���`a,���`a ���bmia3���`a)���`a
���`a
���`cfig���`a,���`a ���`bax���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`a)���`a
���`bax���aoa.���`fimshow���`a(���`aX���`a)���`a
���`a
���`gnumrows���`a,���`a ���`gnumcols���`a ���aoa=���`a ���`aX���aoa.���`eshape���`a
���`a
���`a
���akcdef���`a ���bnflformat_coord���`a(���`ax���`a,���`a ���`ay���`a)���`a:���`a
���`d    ���`ccol���`a ���aoa=���`a ���bnbcint���`a(���`ax���`a ���aoa+���`a ���bmfc0.5���`a)���`a
���`d    ���`crow���`a ���aoa=���`a ���bnbcint���`a(���`ay���`a ���aoa+���`a ���bmfc0.5���`a)���`a
���`d    ���akbif���`a ���bmia0���`a ���aoa<���aoa=���`a ���`ccol���`a ���aoa<���`a ���`gnumcols���`a ���bowcand���`a ���bmia0���`a ���aoa<���aoa=���`a ���`crow���`a ���aoa<���`a ���`gnumrows���`a:���`a
���`h        ���`az���`a ���aoa=���`a ���`aX���`a[���`crow���`a,���`a ���`ccol���`a]���`a
���`h        ���akfreturn���`a ���bs1a'���bs1bx=���bsie%1.4f���bs1d, y=���bsie%1.4f���bs1d, z=���bsie%1.4f���bs1a'���`a ���aoa%���`a ���`a(���`ax���`a,���`a ���`ay���`a,���`a ���`az���`a)���`a
���`d    ���akdelse���`a:���`a
���`h        ���akfreturn���`a ���bs1a'���bs1bx=���bsie%1.4f���bs1d, y=���bsie%1.4f���bs1a'���`a ���aoa%���`a ���`a(���`ax���`a,���`a ���`ay���`a)���`a
���`a
���`bax���aoa.���`lformat_coord���`a ���aoa=���`a ���`lformat_coord���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
���`a
���bc1xM#############################################################################���`a
���bc1a#���`a
���bc1x# .. admonition:: References���`a
���bc1a#���`a
���bc1xN#    The use of the following functions, methods, classes and modules is shown���`a
���bc1u#    in this example:���`a
���bc1a#���`a
���bc1x*#    - `matplotlib.axes.Axes.format_coord`���`a
���bc1x$#    - `matplotlib.axes.Axes.imshow`���`a
`dNone�