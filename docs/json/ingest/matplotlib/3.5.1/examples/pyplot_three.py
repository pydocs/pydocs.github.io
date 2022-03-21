��������m���bsdxt"""
============
Pyplot Three
============

Plot three line plots in a single call to `~matplotlib.pyplot.plot`.
"""���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���`a
���bc1x(# evenly sampled time at 200ms intervals���`a
���`at���`a ���aoa=���`a ���`bnp���aoa.���`farange���`a(���bmfb0.���`a,���`a ���bmfb5.���`a,���`a ���bmfc0.2���`a)���`a
���`a
���bc1x.# red dashes, blue squares and green triangles���`a
���`cplt���aoa.���`dplot���`a(���`at���`a,���`a ���`at���`a,���`a ���bs1a'���bs1cr--���bs1a'���`a,���`a ���`at���`a,���`a ���`at���aoa*���aoa*���bmia2���`a,���`a ���bs1a'���bs1bbs���bs1a'���`a,���`a ���`at���`a,���`a ���`at���aoa*���aoa*���bmia3���`a,���`a ���bs1a'���bs1bg^���bs1a'���`a)���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
���`a
���bc1xM#############################################################################���`a
���bc1a#���`a
���bc1x# .. admonition:: References���`a
���bc1a#���`a
���bc1xN#    The use of the following functions, methods, classes and modules is shown���`a
���bc1u#    in this example:���`a
���bc1a#���`a
���bc1x=#    - `matplotlib.axes.Axes.plot` / `matplotlib.pyplot.plot`���`a
`dNone�