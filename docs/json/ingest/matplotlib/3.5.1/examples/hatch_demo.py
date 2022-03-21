�����������bsdy""""
==========
Hatch demo
==========

Hatches can be added to most polygons in Matplotlib, including `~.Axes.bar`,
`~.Axes.fill_between`, `~.Axes.contourf`, and children of `~.patches.Polygon`.
They are currently supported in the PS, PDF, SVG, OSX, and Agg backends. The WX
and Cairo backends do not currently support hatching.

See also :doc:`/gallery/images_contours_and_fields/contourf_hatching` for
an example using `~.Axes.contourf`, and
:doc:`/gallery/shapes_and_collections/hatch_style_reference` for swatches
of the existing hatches.

"""���`a
���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���bkndfrom���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnngpatches���`a ���bknfimport���`a ���`gEllipse���`a,���`a ���`gPolygon���`a
���`a
���`ax���`a ���aoa=���`a ���`bnp���aoa.���`farange���`a(���bmia1���`a,���`a ���bmia5���`a)���`a
���`by1���`a ���aoa=���`a ���`bnp���aoa.���`farange���`a(���bmia1���`a,���`a ���bmia5���`a)���`a
���`by2���`a ���aoa=���`a ���`bnp���aoa.���`dones���`a(���`by1���aoa.���`eshape���`a)���`a ���aoa*���`a ���bmia4���`a
���`a
���`cfig���`a ���aoa=���`a ���`cplt���aoa.���`ffigure���`a(���`a)���`a
���`caxs���`a ���aoa=���`a ���`cfig���aoa.���`nsubplot_mosaic���`a(���`a[���`a[���bs1a'���bs1dbar1���bs1a'���`a,���`a ���bs1a'���bs1gpatches���bs1a'���`a]���`a,���`a ���`a[���bs1a'���bs1dbar2���bs1a'���`a,���`a ���bs1a'���bs1gpatches���bs1a'���`a]���`a]���`a)���`a
���`a
���`caxs���`a[���bs1a'���bs1dbar1���bs1a'���`a]���aoa.���`cbar���`a(���`ax���`a,���`a ���`by1���`a,���`a ���`iedgecolor���aoa=���bs1a'���bs1eblack���bs1a'���`a,���`a ���`ehatch���aoa=���bs2a"���bs2a/���bs2a"���`a)���`a
���`caxs���`a[���bs1a'���bs1dbar1���bs1a'���`a]���aoa.���`cbar���`a(���`ax���`a,���`a ���`by2���`a,���`a ���`fbottom���aoa=���`by1���`a,���`a ���`iedgecolor���aoa=���bs1a'���bs1eblack���bs1a'���`a,���`a ���`ehatch���aoa=���bs1a'���bs1b//���bs1a'���`a)���`a
���`a
���`caxs���`a[���bs1a'���bs1dbar2���bs1a'���`a]���aoa.���`cbar���`a(���`ax���`a,���`a ���`by1���`a,���`a ���`iedgecolor���aoa=���bs1a'���bs1eblack���bs1a'���`a,���`a ���`ehatch���aoa=���`a[���bs1a'���bs1b--���bs1a'���`a,���`a ���bs1a'���bs1a+���bs1a'���`a,���`a ���bs1a'���bs1ax���bs1a'���`a,���`a ���bs1a'���bseb\\���bs1a'���`a]���`a)���`a
���`caxs���`a[���bs1a'���bs1dbar2���bs1a'���`a]���aoa.���`cbar���`a(���`ax���`a,���`a ���`by2���`a,���`a ���`fbottom���aoa=���`by1���`a,���`a ���`iedgecolor���aoa=���bs1a'���bs1eblack���bs1a'���`a,���`a
���`p                ���`ehatch���aoa=���`a[���bs1a'���bs1a*���bs1a'���`a,���`a ���bs1a'���bs1ao���bs1a'���`a,���`a ���bs1a'���bs1aO���bs1a'���`a,���`a ���bs1a'���bs1a.���bs1a'���`a]���`a)���`a
���`a
���`ax���`a ���aoa=���`a ���`bnp���aoa.���`farange���`a(���bmia0���`a,���`a ���bmib40���`a,���`a ���bmfc0.2���`a)���`a
���`caxs���`a[���bs1a'���bs1gpatches���bs1a'���`a]���aoa.���`lfill_between���`a(���`ax���`a,���`a ���`bnp���aoa.���`csin���`a(���`ax���`a)���`a ���aoa*���`a ���bmia4���`a ���aoa+���`a ���bmib30���`a,���`a ���`by2���aoa=���bmia0���`a,���`a
���`x                            ���`ehatch���aoa=���bs1a'���bs1c///���bs1a'���`a,���`a ���`fzorder���aoa=���bmia2���`a,���`a ���`bfc���aoa=���bs1a'���bs1ac���bs1a'���`a)���`a
���`caxs���`a[���bs1a'���bs1gpatches���bs1a'���`a]���aoa.���`iadd_patch���`a(���`gEllipse���`a(���`a(���bmia4���`a,���`a ���bmib50���`a)���`a,���`a ���bmib10���`a,���`a ���bmib10���`a,���`a ���`dfill���aoa=���bkcdTrue���`a,���`a
���`x!                                 ���`ehatch���aoa=���bs1a'���bs1a*���bs1a'���`a,���`a ���`ifacecolor���aoa=���bs1a'���bs1ay���bs1a'���`a)���`a)���`a
���`caxs���`a[���bs1a'���bs1gpatches���bs1a'���`a]���aoa.���`iadd_patch���`a(���`gPolygon���`a(���`a[���`a(���bmib10���`a,���`a ���bmib20���`a)���`a,���`a ���`a(���bmib30���`a,���`a ���bmib50���`a)���`a,���`a ���`a(���bmib50���`a,���`a ���bmib10���`a)���`a]���`a,���`a
���`x!                                 ���`ehatch���aoa=���bs1a'���bseb\\���bs1d/...���bs1a'���`a,���`a ���`ifacecolor���aoa=���bs1a'���bs1ag���bs1a'���`a)���`a)���`a
���`caxs���`a[���bs1a'���bs1gpatches���bs1a'���`a]���aoa.���`hset_xlim���`a(���`a[���bmia0���`a,���`a ���bmib40���`a]���`a)���`a
���`caxs���`a[���bs1a'���bs1gpatches���bs1a'���`a]���aoa.���`hset_ylim���`a(���`a[���bmib10���`a,���`a ���bmib60���`a]���`a)���`a
���`caxs���`a[���bs1a'���bs1gpatches���bs1a'���`a]���aoa.���`jset_aspect���`a(���bmia1���`a)���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
���`a
���bc1xM#############################################################################���`a
���bc1a#���`a
���bc1x# .. admonition:: References���`a
���bc1a#���`a
���bc1xN#    The use of the following functions, methods, classes and modules is shown���`a
���bc1u#    in this example:���`a
���bc1a#���`a
���bc1x#    - `matplotlib.patches`���`a
���bc1x##    - `matplotlib.patches.Ellipse`���`a
���bc1x##    - `matplotlib.patches.Polygon`���`a
���bc1x'#    - `matplotlib.axes.Axes.add_patch`���`a
���bc1x+#    - `matplotlib.patches.Patch.set_hatch`���`a
���bc1x;#    - `matplotlib.axes.Axes.bar` / `matplotlib.pyplot.bar`���`a
`dNone�