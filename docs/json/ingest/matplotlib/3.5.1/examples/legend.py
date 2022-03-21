������������bsdx�"""
===============================
Legend using pre-defined labels
===============================

Defining legend labels with plots.
"""���`a
���`a
���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���`a
���bc1v# Make some fake data.���`a
���`aa���`a ���aoa=���`a ���`ab���`a ���aoa=���`a ���`bnp���aoa.���`farange���`a(���bmia0���`a,���`a ���bmia3���`a,���`a ���bmfc.02���`a)���`a
���`ac���`a ���aoa=���`a ���`bnp���aoa.���`cexp���`a(���`aa���`a)���`a
���`ad���`a ���aoa=���`a ���`ac���`a[���`a:���`a:���aoa-���bmia1���`a]���`a
���`a
���bc1x'# Create plots with pre-defined labels.���`a
���`cfig���`a,���`a ���`bax���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`a)���`a
���`bax���aoa.���`dplot���`a(���`aa���`a,���`a ���`ac���`a,���`a ���bs1a'���bs1ck--���bs1a'���`a,���`a ���`elabel���aoa=���bs1a'���bs1lModel length���bs1a'���`a)���`a
���`bax���aoa.���`dplot���`a(���`aa���`a,���`a ���`ad���`a,���`a ���bs1a'���bs1bk:���bs1a'���`a,���`a ���`elabel���aoa=���bs1a'���bs1kData length���bs1a'���`a)���`a
���`bax���aoa.���`dplot���`a(���`aa���`a,���`a ���`ac���`a ���aoa+���`a ���`ad���`a,���`a ���bs1a'���bs1ak���bs1a'���`a,���`a ���`elabel���aoa=���bs1a'���bs1tTotal message length���bs1a'���`a)���`a
���`a
���`flegend���`a ���aoa=���`a ���`bax���aoa.���`flegend���`a(���`cloc���aoa=���bs1a'���bs1lupper center���bs1a'���`a,���`a ���`fshadow���aoa=���bkcdTrue���`a,���`a ���`hfontsize���aoa=���bs1a'���bs1gx-large���bs1a'���`a)���`a
���`a
���bc1x-# Put a nicer background color on the legend.���`a
���`flegend���aoa.���`iget_frame���`a(���`a)���aoa.���`mset_facecolor���`a(���bs1a'���bs1bC0���bs1a'���`a)���`a
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
���bc1x=#    - `matplotlib.axes.Axes.plot` / `matplotlib.pyplot.plot`���`a
���bc1xA#    - `matplotlib.axes.Axes.legend` / `matplotlib.pyplot.legend`���`a
`dNone�