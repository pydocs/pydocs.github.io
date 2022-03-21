�����������bsdy+"""
=====================
Hatch style reference
=====================

Hatches can be added to most polygons in Matplotlib, including `~.Axes.bar`,
`~.Axes.fill_between`, `~.Axes.contourf`, and children of `~.patches.Polygon`.
They are currently supported in the PS, PDF, SVG, OSX, and Agg backends. The WX
and Cairo backends do not currently support hatching.

See also :doc:`/gallery/images_contours_and_fields/contourf_hatching` for
an example using `~.Axes.contourf`, and
:doc:`/gallery/shapes_and_collections/hatch_demo` for more usage examples.

"""���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���bkndfrom���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnngpatches���`a ���bknfimport���`a ���`iRectangle���`a
���`a
���`cfig���`a,���`a ���`caxs���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���bmia2���`a,���`a ���bmia5���`a,���`a ���`rconstrained_layout���aoa=���bkcdTrue���`a,���`a ���`gfigsize���aoa=���`a(���bmfc6.4���`a,���`a ���bmfc3.2���`a)���`a)���`a
���`a
���`ghatches���`a ���aoa=���`a ���`a[���bs1a'���bs1a/���bs1a'���`a,���`a ���bs1a'���bseb\\���bs1a'���`a,���`a ���bs1a'���bs1a|���bs1a'���`a,���`a ���bs1a'���bs1a-���bs1a'���`a,���`a ���bs1a'���bs1a+���bs1a'���`a,���`a ���bs1a'���bs1ax���bs1a'���`a,���`a ���bs1a'���bs1ao���bs1a'���`a,���`a ���bs1a'���bs1aO���bs1a'���`a,���`a ���bs1a'���bs1a.���bs1a'���`a,���`a ���bs1a'���bs1a*���bs1a'���`a]���`a
���`a
���`a
���akcdef���`a ���bnflhatches_plot���`a(���`bax���`a,���`a ���`ah���`a)���`a:���`a
���`d    ���`bax���aoa.���`iadd_patch���`a(���`iRectangle���`a(���`a(���bmia0���`a,���`a ���bmia0���`a)���`a,���`a ���bmia2���`a,���`a ���bmia2���`a,���`a ���`dfill���aoa=���bkceFalse���`a,���`a ���`ehatch���aoa=���`ah���`a)���`a)���`a
���`d    ���`bax���aoa.���`dtext���`a(���bmia1���`a,���`a ���aoa-���bmfc0.5���`a,���`a ���bsaaf���bs2a"���bs2a'���bs2a ���bsia{���`ah���bsia}���bs2a ���bs2a'���bs2a"���`a,���`a ���`dsize���aoa=���bmib15���`a,���`a ���`bha���aoa=���bs2a"���bs2fcenter���bs2a"���`a)���`a
���`d    ���`bax���aoa.���`daxis���`a(���bs1a'���bs1eequal���bs1a'���`a)���`a
���`d    ���`bax���aoa.���`daxis���`a(���bs1a'���bs1coff���bs1a'���`a)���`a
���`a
���akcfor���`a ���`bax���`a,���`a ���`ah���`a ���bowbin���`a ���bnbczip���`a(���`caxs���aoa.���`dflat���`a,���`a ���`ghatches���`a)���`a:���`a
���`d    ���`lhatches_plot���`a(���`bax���`a,���`a ���`ah���`a)���`a
���`a
���bc1xO###############################################################################���`a
���bc1x<# Hatching patterns can be repeated to increase the density.���`a
���`a
���`cfig���`a,���`a ���`caxs���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���bmia2���`a,���`a ���bmia5���`a,���`a ���`rconstrained_layout���aoa=���bkcdTrue���`a,���`a ���`gfigsize���aoa=���`a(���bmfc6.4���`a,���`a ���bmfc3.2���`a)���`a)���`a
���`a
���`ghatches���`a ���aoa=���`a ���`a[���bs1a'���bs1b//���bs1a'���`a,���`a ���bs1a'���bseb\\���bseb\\���bs1a'���`a,���`a ���bs1a'���bs1b||���bs1a'���`a,���`a ���bs1a'���bs1b--���bs1a'���`a,���`a ���bs1a'���bs1b++���bs1a'���`a,���`a ���bs1a'���bs1bxx���bs1a'���`a,���`a ���bs1a'���bs1boo���bs1a'���`a,���`a ���bs1a'���bs1bOO���bs1a'���`a,���`a ���bs1a'���bs1b..���bs1a'���`a,���`a ���bs1a'���bs1b**���bs1a'���`a]���`a
���`a
���akcfor���`a ���`bax���`a,���`a ���`ah���`a ���bowbin���`a ���bnbczip���`a(���`caxs���aoa.���`dflat���`a,���`a ���`ghatches���`a)���`a:���`a
���`d    ���`lhatches_plot���`a(���`bax���`a,���`a ���`ah���`a)���`a
���`a
���bc1xO###############################################################################���`a
���bc1xB# Hatching patterns can be combined to create additional patterns.���`a
���`a
���`cfig���`a,���`a ���`caxs���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���bmia2���`a,���`a ���bmia5���`a,���`a ���`rconstrained_layout���aoa=���bkcdTrue���`a,���`a ���`gfigsize���aoa=���`a(���bmfc6.4���`a,���`a ���bmfc3.2���`a)���`a)���`a
���`a
���`ghatches���`a ���aoa=���`a ���`a[���bs1a'���bs1b/o���bs1a'���`a,���`a ���bs1a'���bseb\\���bs1a|���bs1a'���`a,���`a ���bs1a'���bs1b|*���bs1a'���`a,���`a ���bs1a'���bs1a-���bseb\\���bs1a'���`a,���`a ���bs1a'���bs1b+o���bs1a'���`a,���`a ���bs1a'���bs1bx*���bs1a'���`a,���`a ���bs1a'���bs1bo-���bs1a'���`a,���`a ���bs1a'���bs1bO|���bs1a'���`a,���`a ���bs1a'���bs1bO.���bs1a'���`a,���`a ���bs1a'���bs1b*-���bs1a'���`a]���`a
���`a
���akcfor���`a ���`bax���`a,���`a ���`ah���`a ���bowbin���`a ���bnbczip���`a(���`caxs���aoa.���`dflat���`a,���`a ���`ghatches���`a)���`a:���`a
���`d    ���`lhatches_plot���`a(���`bax���`a,���`a ���`ah���`a)���`a
���`a
���bc1xM#############################################################################���`a
���bc1a#���`a
���bc1x# .. admonition:: References���`a
���bc1a#���`a
���bc1xN#    The use of the following functions, methods, classes and modules is shown���`a
���bc1u#    in this example:���`a
���bc1a#���`a
���bc1x#    - `matplotlib.patches`���`a
���bc1x%#    - `matplotlib.patches.Rectangle`���`a
���bc1x'#    - `matplotlib.axes.Axes.add_patch`���`a
���bc1x"#    - `matplotlib.axes.Axes.text`���`a
`dNone�