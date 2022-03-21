��������|���bsdx�"""
================
Connect Simple01
================

A `.ConnectionPatch` can be used to draw a line (possibly with arrow head)
between points defined in different coordinate systems and/or axes.
"""���`a
���`a
���bkndfrom���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnngpatches���`a ���bknfimport���`a ���`oConnectionPatch���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���`a
���`cfig���`a,���`a ���`a(���`cax1���`a,���`a ���`cax2���`a)���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���bmia1���`a,���`a ���bmia2���`a,���`a ���`gfigsize���aoa=���`a(���bmia6���`a,���`a ���bmia3���`a)���`a)���`a
���`a
���bc1x<# Draw a simple arrow between two points in axes coordinates���`a
���bc1w# within a single axes.���`a
���`cxyA���`a ���aoa=���`a ���`a(���bmfc0.2���`a,���`a ���bmfc0.2���`a)���`a
���`cxyB���`a ���aoa=���`a ���`a(���bmfc0.8���`a,���`a ���bmfc0.8���`a)���`a
���`gcoordsA���`a ���aoa=���`a ���bs2a"���bs2ddata���bs2a"���`a
���`gcoordsB���`a ���aoa=���`a ���bs2a"���bs2ddata���bs2a"���`a
���`ccon���`a ���aoa=���`a ���`oConnectionPatch���`a(���`cxyA���`a,���`a ���`cxyB���`a,���`a ���`gcoordsA���`a,���`a ���`gcoordsB���`a,���`a
���`v                      ���`jarrowstyle���aoa=���bs2a"���bs2c-|>���bs2a"���`a,���`a ���`gshrinkA���aoa=���bmia5���`a,���`a ���`gshrinkB���aoa=���bmia5���`a,���`a
���`v                      ���`nmutation_scale���aoa=���bmib20���`a,���`a ���`bfc���aoa=���bs2a"���bs2aw���bs2a"���`a)���`a
���`cax1���aoa.���`dplot���`a(���`a[���`cxyA���`a[���bmia0���`a]���`a,���`a ���`cxyB���`a[���bmia0���`a]���`a]���`a,���`a ���`a[���`cxyA���`a[���bmia1���`a]���`a,���`a ���`cxyB���`a[���bmia1���`a]���`a]���`a,���`a ���bs2a"���bs2ao���bs2a"���`a)���`a
���`cax1���aoa.���`jadd_artist���`a(���`ccon���`a)���`a
���`a
���bc1x;# Draw an arrow between the same point in data coordinates,���`a
���bc1x# but in different axes.���`a
���`bxy���`a ���aoa=���`a ���`a(���bmfc0.3���`a,���`a ���bmfc0.2���`a)���`a
���`ccon���`a ���aoa=���`a ���`oConnectionPatch���`a(���`a
���`d    ���`cxyA���aoa=���`bxy���`a,���`a ���`gcoordsA���aoa=���`cax2���aoa.���`itransData���`a,���`a
���`d    ���`cxyB���aoa=���`bxy���`a,���`a ���`gcoordsB���aoa=���`cax1���aoa.���`itransData���`a,���`a
���`d    ���`jarrowstyle���aoa=���bs2a"���bs2b->���bs2a"���`a,���`a ���`gshrinkB���aoa=���bmia5���`a)���`a
���`cfig���aoa.���`jadd_artist���`a(���`ccon���`a)���`a
���`a
���bc1xK# Draw a line between the different points, defined in different coordinate���`a
���bc1j# systems.���`a
���`ccon���`a ���aoa=���`a ���`oConnectionPatch���`a(���`a
���`d    ���bc1u# in axes coordinates���`a
���`d    ���`cxyA���aoa=���`a(���bmfc0.6���`a,���`a ���bmfc1.0���`a)���`a,���`a ���`gcoordsA���aoa=���`cax2���aoa.���`itransAxes���`a,���`a
���`d    ���bc1x.# x in axes coordinates, y in data coordinates���`a
���`d    ���`cxyB���aoa=���`a(���bmfc0.0���`a,���`a ���bmfc0.2���`a)���`a,���`a ���`gcoordsB���aoa=���`cax2���aoa.���`sget_yaxis_transform���`a(���`a)���`a,���`a
���`d    ���`jarrowstyle���aoa=���bs2a"���bs2a-���bs2a"���`a)���`a
���`cax2���aoa.���`jadd_artist���`a(���`ccon���`a)���`a
���`a
���`cax1���aoa.���`hset_xlim���`a(���bmia0���`a,���`a ���bmia1���`a)���`a
���`cax1���aoa.���`hset_ylim���`a(���bmia0���`a,���`a ���bmia1���`a)���`a
���`cax2���aoa.���`hset_xlim���`a(���bmia0���`a,���`a ���bmfb.5���`a)���`a
���`cax2���aoa.���`hset_ylim���`a(���bmia0���`a,���`a ���bmfb.5���`a)���`a
���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
`dNone�