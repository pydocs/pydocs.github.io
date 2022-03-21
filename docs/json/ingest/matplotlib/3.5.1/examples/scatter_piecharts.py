�����������bsdx�"""
===================================
Scatter plot with pie chart markers
===================================

This example makes custom 'pie charts' as the markers for a scatter plot.

Thanks to Manuel Metz for the example.
"""���`a
���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���`a
���bc1x# first define the ratios���`a
���`br1���`a ���aoa=���`a ���bmfc0.2���`g       ���bc1e# 20%���`a
���`br2���`a ���aoa=���`a ���`br1���`a ���aoa+���`a ���bmfc0.4���`b  ���bc1e# 40%���`a
���`a
���bc1x)# define some sizes of the scatter marker���`a
���`esizes���`a ���aoa=���`a ���`bnp���aoa.���`earray���`a(���`a[���bmib60���`a,���`a ���bmib80���`a,���`a ���bmic120���`a]���`a)���`a
���`a
���bc1x.# calculate the points of the first pie marker���`a
���bc1xG# these are just the origin (0, 0) + some (cos, sin) points on a circle���`a
���`bx1���`a ���aoa=���`a ���`bnp���aoa.���`ccos���`a(���bmia2���`a ���aoa*���`a ���`bnp���aoa.���`bpi���`a ���aoa*���`a ���`bnp���aoa.���`hlinspace���`a(���bmia0���`a,���`a ���`br1���`a)���`a)���`a
���`by1���`a ���aoa=���`a ���`bnp���aoa.���`csin���`a(���bmia2���`a ���aoa*���`a ���`bnp���aoa.���`bpi���`a ���aoa*���`a ���`bnp���aoa.���`hlinspace���`a(���bmia0���`a,���`a ���`br1���`a)���`a)���`a
���`cxy1���`a ���aoa=���`a ���`bnp���aoa.���`irow_stack���`a(���`a[���`a[���bmia0���`a,���`a ���bmia0���`a]���`a,���`a ���`bnp���aoa.���`lcolumn_stack���`a(���`a[���`bx1���`a,���`a ���`by1���`a]���`a)���`a]���`a)���`a
���`bs1���`a ���aoa=���`a ���`bnp���aoa.���`cabs���`a(���`cxy1���`a)���aoa.���`cmax���`a(���`a)���`a
���`a
���`bx2���`a ���aoa=���`a ���`bnp���aoa.���`ccos���`a(���bmia2���`a ���aoa*���`a ���`bnp���aoa.���`bpi���`a ���aoa*���`a ���`bnp���aoa.���`hlinspace���`a(���`br1���`a,���`a ���`br2���`a)���`a)���`a
���`by2���`a ���aoa=���`a ���`bnp���aoa.���`csin���`a(���bmia2���`a ���aoa*���`a ���`bnp���aoa.���`bpi���`a ���aoa*���`a ���`bnp���aoa.���`hlinspace���`a(���`br1���`a,���`a ���`br2���`a)���`a)���`a
���`cxy2���`a ���aoa=���`a ���`bnp���aoa.���`irow_stack���`a(���`a[���`a[���bmia0���`a,���`a ���bmia0���`a]���`a,���`a ���`bnp���aoa.���`lcolumn_stack���`a(���`a[���`bx2���`a,���`a ���`by2���`a]���`a)���`a]���`a)���`a
���`bs2���`a ���aoa=���`a ���`bnp���aoa.���`cabs���`a(���`cxy2���`a)���aoa.���`cmax���`a(���`a)���`a
���`a
���`bx3���`a ���aoa=���`a ���`bnp���aoa.���`ccos���`a(���bmia2���`a ���aoa*���`a ���`bnp���aoa.���`bpi���`a ���aoa*���`a ���`bnp���aoa.���`hlinspace���`a(���`br2���`a,���`a ���bmia1���`a)���`a)���`a
���`by3���`a ���aoa=���`a ���`bnp���aoa.���`csin���`a(���bmia2���`a ���aoa*���`a ���`bnp���aoa.���`bpi���`a ���aoa*���`a ���`bnp���aoa.���`hlinspace���`a(���`br2���`a,���`a ���bmia1���`a)���`a)���`a
���`cxy3���`a ���aoa=���`a ���`bnp���aoa.���`irow_stack���`a(���`a[���`a[���bmia0���`a,���`a ���bmia0���`a]���`a,���`a ���`bnp���aoa.���`lcolumn_stack���`a(���`a[���`bx3���`a,���`a ���`by3���`a]���`a)���`a]���`a)���`a
���`bs3���`a ���aoa=���`a ���`bnp���aoa.���`cabs���`a(���`cxy3���`a)���aoa.���`cmax���`a(���`a)���`a
���`a
���`cfig���`a,���`a ���`bax���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`a)���`a
���`bax���aoa.���`gscatter���`a(���bnberange���`a(���bmia3���`a)���`a,���`a ���bnberange���`a(���bmia3���`a)���`a,���`a ���`fmarker���aoa=���`cxy1���`a,���`a ���`as���aoa=���`bs1���aoa*���aoa*���bmia2���`a ���aoa*���`a ���`esizes���`a,���`a ���`ifacecolor���aoa=���bs1a'���bs1dblue���bs1a'���`a)���`a
���`bax���aoa.���`gscatter���`a(���bnberange���`a(���bmia3���`a)���`a,���`a ���bnberange���`a(���bmia3���`a)���`a,���`a ���`fmarker���aoa=���`cxy2���`a,���`a ���`as���aoa=���`bs2���aoa*���aoa*���bmia2���`a ���aoa*���`a ���`esizes���`a,���`a ���`ifacecolor���aoa=���bs1a'���bs1egreen���bs1a'���`a)���`a
���`bax���aoa.���`gscatter���`a(���bnberange���`a(���bmia3���`a)���`a,���`a ���bnberange���`a(���bmia3���`a)���`a,���`a ���`fmarker���aoa=���`cxy3���`a,���`a ���`as���aoa=���`bs3���aoa*���aoa*���bmia2���`a ���aoa*���`a ���`esizes���`a,���`a ���`ifacecolor���aoa=���bs1a'���bs1cred���bs1a'���`a)���`a
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
���bc1xC#    - `matplotlib.axes.Axes.scatter` / `matplotlib.pyplot.scatter`���`a
`dNone�