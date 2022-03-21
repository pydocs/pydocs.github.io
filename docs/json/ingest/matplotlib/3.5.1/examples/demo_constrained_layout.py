��������s���bsdy�"""
=====================================
Resizing axes with constrained layout
=====================================

Constrained layout attempts to resize subplots in
a figure so that there are no overlaps between axes objects and labels
on the axes.

See :doc:`/tutorials/intermediate/constrainedlayout_guide` for more details and
:doc:`/tutorials/intermediate/tight_layout_guide` for an alternative.

"""���`a
���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���`a
���`a
���akcdef���`a ���bnflexample_plot���`a(���`bax���`a)���`a:���`a
���`d    ���`bax���aoa.���`dplot���`a(���`a[���bmia1���`a,���`a ���bmia2���`a]���`a)���`a
���`d    ���`bax���aoa.���`jset_xlabel���`a(���bs1a'���bs1gx-label���bs1a'���`a,���`a ���`hfontsize���aoa=���bmib12���`a)���`a
���`d    ���`bax���aoa.���`jset_ylabel���`a(���bs1a'���bs1gy-label���bs1a'���`a,���`a ���`hfontsize���aoa=���bmib12���`a)���`a
���`d    ���`bax���aoa.���`iset_title���`a(���bs1a'���bs1eTitle���bs1a'���`a,���`a ���`hfontsize���aoa=���bmib14���`a)���`a
���`a
���`a
���bc1xO###############################################################################���`a
���bc1xB# If we don't use constrained_layout, then labels overlap the axes���`a
���`a
���`cfig���`a,���`a ���`caxs���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`enrows���aoa=���bmia2���`a,���`a ���`encols���aoa=���bmia2���`a,���`a ���`rconstrained_layout���aoa=���bkceFalse���`a)���`a
���`a
���akcfor���`a ���`bax���`a ���bowbin���`a ���`caxs���aoa.���`dflat���`a:���`a
���`d    ���`lexample_plot���`a(���`bax���`a)���`a
���`a
���bc1xO###############################################################################���`a
���bc1x;# adding ``constrained_layout=True`` automatically adjusts.���`a
���`a
���`cfig���`a,���`a ���`caxs���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`enrows���aoa=���bmia2���`a,���`a ���`encols���aoa=���bmia2���`a,���`a ���`rconstrained_layout���aoa=���bkcdTrue���`a)���`a
���`a
���akcfor���`a ���`bax���`a ���bowbin���`a ���`caxs���aoa.���`dflat���`a:���`a
���`d    ���`lexample_plot���`a(���`bax���`a)���`a
���`a
���bc1xO###############################################################################���`a
���bc1x=# Below is a more complicated example using nested gridspecs.���`a
���`a
���`cfig���`a ���aoa=���`a ���`cplt���aoa.���`ffigure���`a(���`rconstrained_layout���aoa=���bkcdTrue���`a)���`a
���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnhgridspec���`a ���akbas���`a ���bnnhgridspec���`a
���`a
���`cgs0���`a ���aoa=���`a ���`hgridspec���aoa.���`hGridSpec���`a(���bmia1���`a,���`a ���bmia2���`a,���`a ���`ffigure���aoa=���`cfig���`a)���`a
���`a
���`cgs1���`a ���aoa=���`a ���`hgridspec���aoa.���`wGridSpecFromSubplotSpec���`a(���bmia3���`a,���`a ���bmia1���`a,���`a ���`lsubplot_spec���aoa=���`cgs0���`a[���bmia0���`a]���`a)���`a
���akcfor���`a ���`an���`a ���bowbin���`a ���bnberange���`a(���bmia3���`a)���`a:���`a
���`d    ���`bax���`a ���aoa=���`a ���`cfig���aoa.���`kadd_subplot���`a(���`cgs1���`a[���`an���`a]���`a)���`a
���`d    ���`lexample_plot���`a(���`bax���`a)���`a
���`a
���`a
���`cgs2���`a ���aoa=���`a ���`hgridspec���aoa.���`wGridSpecFromSubplotSpec���`a(���bmia2���`a,���`a ���bmia1���`a,���`a ���`lsubplot_spec���aoa=���`cgs0���`a[���bmia1���`a]���`a)���`a
���akcfor���`a ���`an���`a ���bowbin���`a ���bnberange���`a(���bmia2���`a)���`a:���`a
���`d    ���`bax���`a ���aoa=���`a ���`cfig���aoa.���`kadd_subplot���`a(���`cgs2���`a[���`an���`a]���`a)���`a
���`d    ���`lexample_plot���`a(���`bax���`a)���`a
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
���bc1x%#    - `matplotlib.gridspec.GridSpec`���`a
���bc1x4#    - `matplotlib.gridspec.GridSpecFromSubplotSpec`���`a
`dNone�