��������A���bsdyS"""
================
Nested Gridspecs
================

GridSpecs can be nested, so that a subplot from a parent GridSpec can
set the position for a nested grid of subplots.

Note that the same functionality can be achieved more directly with
`~.figure.FigureBase.subfigures`; see
:doc:`/gallery/subplots_axes_and_figures/subfigures`.

"""���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnhgridspec���`a ���akbas���`a ���bnnhgridspec���`a
���`a
���`a
���akcdef���`a ���bnfkformat_axes���`a(���`cfig���`a)���`a:���`a
���`d    ���akcfor���`a ���`ai���`a,���`a ���`bax���`a ���bowbin���`a ���bnbienumerate���`a(���`cfig���aoa.���`daxes���`a)���`a:���`a
���`h        ���`bax���aoa.���`dtext���`a(���bmfc0.5���`a,���`a ���bmfc0.5���`a,���`a ���bs2a"���bs2bax���bsib%d���bs2a"���`a ���aoa%���`a ���`a(���`ai���aoa+���bmia1���`a)���`a,���`a ���`bva���aoa=���bs2a"���bs2fcenter���bs2a"���`a,���`a ���`bha���aoa=���bs2a"���bs2fcenter���bs2a"���`a)���`a
���`h        ���`bax���aoa.���`ktick_params���`a(���`klabelbottom���aoa=���bkceFalse���`a,���`a ���`ilabelleft���aoa=���bkceFalse���`a)���`a
���`a
���`a
���bc1x# gridspec inside gridspec���`a
���`cfig���`a ���aoa=���`a ���`cplt���aoa.���`ffigure���`a(���`a)���`a
���`a
���`cgs0���`a ���aoa=���`a ���`hgridspec���aoa.���`hGridSpec���`a(���bmia1���`a,���`a ���bmia2���`a,���`a ���`ffigure���aoa=���`cfig���`a)���`a
���`a
���`dgs00���`a ���aoa=���`a ���`hgridspec���aoa.���`wGridSpecFromSubplotSpec���`a(���bmia3���`a,���`a ���bmia3���`a,���`a ���`lsubplot_spec���aoa=���`cgs0���`a[���bmia0���`a]���`a)���`a
���`a
���`cax1���`a ���aoa=���`a ���`cfig���aoa.���`kadd_subplot���`a(���`dgs00���`a[���`a:���aoa-���bmia1���`a,���`a ���`a:���`a]���`a)���`a
���`cax2���`a ���aoa=���`a ���`cfig���aoa.���`kadd_subplot���`a(���`dgs00���`a[���aoa-���bmia1���`a,���`a ���`a:���aoa-���bmia1���`a]���`a)���`a
���`cax3���`a ���aoa=���`a ���`cfig���aoa.���`kadd_subplot���`a(���`dgs00���`a[���aoa-���bmia1���`a,���`a ���aoa-���bmia1���`a]���`a)���`a
���`a
���bc1xO# the following syntax does the same as the GridSpecFromSubplotSpec call above:���`a
���`dgs01���`a ���aoa=���`a ���`cgs0���`a[���bmia1���`a]���aoa.���`ksubgridspec���`a(���bmia3���`a,���`a ���bmia3���`a)���`a
���`a
���`cax4���`a ���aoa=���`a ���`cfig���aoa.���`kadd_subplot���`a(���`dgs01���`a[���`a:���`a,���`a ���`a:���aoa-���bmia1���`a]���`a)���`a
���`cax5���`a ���aoa=���`a ���`cfig���aoa.���`kadd_subplot���`a(���`dgs01���`a[���`a:���aoa-���bmia1���`a,���`a ���aoa-���bmia1���`a]���`a)���`a
���`cax6���`a ���aoa=���`a ���`cfig���aoa.���`kadd_subplot���`a(���`dgs01���`a[���aoa-���bmia1���`a,���`a ���aoa-���bmia1���`a]���`a)���`a
���`a
���`cplt���aoa.���`hsuptitle���`a(���bs2a"���bs2xGridSpec Inside GridSpec���bs2a"���`a)���`a
���`kformat_axes���`a(���`cfig���`a)���`a
���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
`dNone�