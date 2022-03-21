������������bsdyM"""
=======================================================
Using Gridspec to make multi-column/row subplot layouts
=======================================================

`.GridSpec` is a flexible way to layout
subplot grids.  Here is an example with a 3x3 grid, and
axes spanning all three columns, two columns, and two rows.

"""���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���bkndfrom���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnhgridspec���`a ���bknfimport���`a ���`hGridSpec���`a
���`a
���`a
���akcdef���`a ���bnfkformat_axes���`a(���`cfig���`a)���`a:���`a
���`d    ���akcfor���`a ���`ai���`a,���`a ���`bax���`a ���bowbin���`a ���bnbienumerate���`a(���`cfig���aoa.���`daxes���`a)���`a:���`a
���`h        ���`bax���aoa.���`dtext���`a(���bmfc0.5���`a,���`a ���bmfc0.5���`a,���`a ���bs2a"���bs2bax���bsib%d���bs2a"���`a ���aoa%���`a ���`a(���`ai���aoa+���bmia1���`a)���`a,���`a ���`bva���aoa=���bs2a"���bs2fcenter���bs2a"���`a,���`a ���`bha���aoa=���bs2a"���bs2fcenter���bs2a"���`a)���`a
���`h        ���`bax���aoa.���`ktick_params���`a(���`klabelbottom���aoa=���bkceFalse���`a,���`a ���`ilabelleft���aoa=���bkceFalse���`a)���`a
���`a
���`cfig���`a ���aoa=���`a ���`cplt���aoa.���`ffigure���`a(���`rconstrained_layout���aoa=���bkcdTrue���`a)���`a
���`a
���`bgs���`a ���aoa=���`a ���`hGridSpec���`a(���bmia3���`a,���`a ���bmia3���`a,���`a ���`ffigure���aoa=���`cfig���`a)���`a
���`cax1���`a ���aoa=���`a ���`cfig���aoa.���`kadd_subplot���`a(���`bgs���`a[���bmia0���`a,���`a ���`a:���`a]���`a)���`a
���bc1xG# identical to ax1 = plt.subplot(gs.new_subplotspec((0, 0), colspan=3))���`a
���`cax2���`a ���aoa=���`a ���`cfig���aoa.���`kadd_subplot���`a(���`bgs���`a[���bmia1���`a,���`a ���`a:���aoa-���bmia1���`a]���`a)���`a
���`cax3���`a ���aoa=���`a ���`cfig���aoa.���`kadd_subplot���`a(���`bgs���`a[���bmia1���`a:���`a,���`a ���aoa-���bmia1���`a]���`a)���`a
���`cax4���`a ���aoa=���`a ���`cfig���aoa.���`kadd_subplot���`a(���`bgs���`a[���aoa-���bmia1���`a,���`a ���bmia0���`a]���`a)���`a
���`cax5���`a ���aoa=���`a ���`cfig���aoa.���`kadd_subplot���`a(���`bgs���`a[���aoa-���bmia1���`a,���`a ���aoa-���bmia2���`a]���`a)���`a
���`a
���`cfig���aoa.���`hsuptitle���`a(���bs2a"���bs2hGridSpec���bs2a"���`a)���`a
���`kformat_axes���`a(���`cfig���`a)���`a
���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
`dNone�