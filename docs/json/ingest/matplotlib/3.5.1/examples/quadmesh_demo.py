������������bsdx�"""
=============
QuadMesh Demo
=============

`~.axes.Axes.pcolormesh` uses a `~matplotlib.collections.QuadMesh`,
a faster generalization of `~.axes.Axes.pcolor`, but with some restrictions.

This demo illustrates a bug in quadmesh with masked data.
"""���`a
���`a
���bkndfrom���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����`a ���bknfimport���`a ���`fpyplot���`a ���akbas���`a ���`cplt���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���`a
���`an���`a ���aoa=���`a ���bmib12���`a
���`ax���`a ���aoa=���`a ���`bnp���aoa.���`hlinspace���`a(���aoa-���bmfc1.5���`a,���`a ���bmfc1.5���`a,���`a ���`an���`a)���`a
���`ay���`a ���aoa=���`a ���`bnp���aoa.���`hlinspace���`a(���aoa-���bmfc1.5���`a,���`a ���bmfc1.5���`a,���`a ���`an���`a ���aoa*���`a ���bmia2���`a)���`a
���`aX���`a,���`a ���`aY���`a ���aoa=���`a ���`bnp���aoa.���`hmeshgrid���`a(���`ax���`a,���`a ���`ay���`a)���`a
���`bQx���`a ���aoa=���`a ���`bnp���aoa.���`ccos���`a(���`aY���`a)���`a ���aoa-���`a ���`bnp���aoa.���`ccos���`a(���`aX���`a)���`a
���`bQz���`a ���aoa=���`a ���`bnp���aoa.���`csin���`a(���`aY���`a)���`a ���aoa+���`a ���`bnp���aoa.���`csin���`a(���`aX���`a)���`a
���`aZ���`a ���aoa=���`a ���`bnp���aoa.���`dsqrt���`a(���`aX���aoa*���aoa*���bmia2���`a ���aoa+���`a ���`aY���aoa*���aoa*���bmia2���`a)���`a ���aoa/���`a ���bmia5���`a
���`aZ���`a ���aoa=���`a ���`a(���`aZ���`a ���aoa-���`a ���`aZ���aoa.���`cmin���`a(���`a)���`a)���`a ���aoa/���`a ���`a(���`aZ���aoa.���`cmax���`a(���`a)���`a ���aoa-���`a ���`aZ���aoa.���`cmin���`a(���`a)���`a)���`a
���`a
���bc1x,# The color array can include masked values.���`a
���`bZm���`a ���aoa=���`a ���`bnp���aoa.���`bma���aoa.���`lmasked_where���`a(���`bnp���aoa.���`cabs���`a(���`bQz���`a)���`a ���aoa<���`a ���bmfc0.5���`a ���aoa*���`a ���`bnp���aoa.���`cmax���`a(���`bQz���`a)���`a,���`a ���`aZ���`a)���`a
���`a
���`cfig���`a,���`a ���`caxs���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`enrows���aoa=���bmia1���`a,���`a ���`encols���aoa=���bmia3���`a)���`a
���`caxs���`a[���bmia0���`a]���aoa.���`jpcolormesh���`a(���`bQx���`a,���`a ���`bQz���`a,���`a ���`aZ���`a,���`a ���`gshading���aoa=���bs1a'���bs1ggouraud���bs1a'���`a)���`a
���`caxs���`a[���bmia0���`a]���aoa.���`iset_title���`a(���bs1a'���bs1uWithout masked values���bs1a'���`a)���`a
���`a
���bc1x1# You can control the color of the masked region.���`a
���`dcmap���`a ���aoa=���`a ���`cplt���aoa.���`icolormaps���`a[���`cplt���aoa.���`hrcParams���`a[���bs1a'���bs1jimage.cmap���bs1a'���`a]���`a]���aoa.���`mwith_extremes���`a(���`cbad���aoa=���bs1a'���bs1ay���bs1a'���`a)���`a
���`caxs���`a[���bmia1���`a]���aoa.���`jpcolormesh���`a(���`bQx���`a,���`a ���`bQz���`a,���`a ���`bZm���`a,���`a ���`gshading���aoa=���bs1a'���bs1ggouraud���bs1a'���`a,���`a ���`dcmap���aoa=���`dcmap���`a)���`a
���`caxs���`a[���bmia1���`a]���aoa.���`iset_title���`a(���bs1a'���bs1rWith masked values���bs1a'���`a)���`a
���`a
���bc1x+# Or use the default, which is transparent.���`a
���`caxs���`a[���bmia2���`a]���aoa.���`jpcolormesh���`a(���`bQx���`a,���`a ���`bQz���`a,���`a ���`bZm���`a,���`a ���`gshading���aoa=���bs1a'���bs1ggouraud���bs1a'���`a)���`a
���`caxs���`a[���bmia2���`a]���aoa.���`iset_title���`a(���bs1a'���bs1rWith masked values���bs1a'���`a)���`a
���`a
���`cfig���aoa.���`ltight_layout���`a(���`a)���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
���`a
���bc1xM#############################################################################���`a
���bc1a#���`a
���bc1x# .. admonition:: References���`a
���bc1a#���`a
���bc1xN#    The use of the following functions, methods, classes and modules is shown���`a
���bc1u#    in this example:���`a
���bc1a#���`a
���bc1xI#    - `matplotlib.axes.Axes.pcolormesh` / `matplotlib.pyplot.pcolormesh`���`a
`dNone�