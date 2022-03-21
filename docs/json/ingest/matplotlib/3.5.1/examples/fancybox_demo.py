��������}���bsdx�"""
===================
Drawing fancy boxes
===================

The following examples show how to plot boxes with different visual properties.
"""���`a
���`a
���bknfimport���`a ���bnnginspect���`a
���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnjtransforms���`a ���akbas���`a ���bnnkmtransforms���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnngpatches���`a ���akbas���`a ���bnnfmpatch���`a
���bkndfrom���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnngpatches���`a ���bknfimport���`a ���`nFancyBboxPatch���`a
���`a
���bc1xO###############################################################################���`a
���bc1x3# First we'll show some sample boxes with fancybox.���`a
���`a
���`fstyles���`a ���aoa=���`a ���`fmpatch���aoa.���`hBoxStyle���aoa.���`jget_styles���`a(���`a)���`a
���`dncol���`a ���aoa=���`a ���bmia2���`a
���`dnrow���`a ���aoa=���`a ���`a(���bnbclen���`a(���`fstyles���`a)���`a ���aoa+���`a ���bmia1���`a)���`a ���aoa/���aoa/���`a ���`dncol���`a
���`caxs���`a ���aoa=���`a ���`a(���`cplt���aoa.���`ffigure���`a(���`gfigsize���aoa=���`a(���bmia3���`a ���aoa*���`a ���`dncol���`a,���`a ���bmia1���`a ���aoa+���`a ���`dnrow���`a)���`a)���`a
���`g       ���aoa.���`ladd_gridspec���`a(���bmia1���`a ���aoa+���`a ���`dnrow���`a,���`a ���`dncol���`a,���`a ���`fwspace���aoa=���bmfb.5���`a)���aoa.���`hsubplots���`a(���`a)���`a)���`a
���akcfor���`a ���`bax���`a ���bowbin���`a ���`caxs���aoa.���`dflat���`a:���`a
���`d    ���`bax���aoa.���`lset_axis_off���`a(���`a)���`a
���akcfor���`a ���`bax���`a ���bowbin���`a ���`caxs���`a[���bmia0���`a,���`a ���`a:���`a]���`a:���`a
���`d    ���`bax���aoa.���`dtext���`a(���bmfb.2���`a,���`a ���bmfb.5���`a,���`a ���bs2a"���bs2hboxstyle���bs2a"���`a,���`a
���`l            ���`itransform���aoa=���`bax���aoa.���`itransAxes���`a,���`a ���`dsize���aoa=���bs2a"���bs2elarge���bs2a"���`a,���`a ���`ecolor���aoa=���bs2a"���bs2htab:blue���bs2a"���`a,���`a
���`l            ���`shorizontalalignment���aoa=���bs2a"���bs2eright���bs2a"���`a,���`a ���`qverticalalignment���aoa=���bs2a"���bs2fcenter���bs2a"���`a)���`a
���`d    ���`bax���aoa.���`dtext���`a(���bmfb.4���`a,���`a ���bmfb.5���`a,���`a ���bs2a"���bs2rdefault parameters���bs2a"���`a,���`a
���`l            ���`itransform���aoa=���`bax���aoa.���`itransAxes���`a,���`a
���`l            ���`shorizontalalignment���aoa=���bs2a"���bs2dleft���bs2a"���`a,���`a ���`qverticalalignment���aoa=���bs2a"���bs2fcenter���bs2a"���`a)���`a
���akcfor���`a ���`bax���`a,���`a ���`a(���`istylename���`a,���`a ���`hstylecls���`a)���`a ���bowbin���`a ���bnbczip���`a(���`caxs���`a[���bmia1���`a:���`a,���`a ���`a:���`a]���aoa.���`aT���aoa.���`dflat���`a,���`a ���`fstyles���aoa.���`eitems���`a(���`a)���`a)���`a:���`a
���`d    ���`bax���aoa.���`dtext���`a(���bmfb.2���`a,���`a ���bmfb.5���`a,���`a ���`istylename���`a,���`a ���`dbbox���aoa=���bnbddict���`a(���`hboxstyle���aoa=���`istylename���`a,���`a ���`bfc���aoa=���bs2a"���bs2aw���bs2a"���`a,���`a ���`bec���aoa=���bs2a"���bs2ak���bs2a"���`a)���`a,���`a
���`l            ���`itransform���aoa=���`bax���aoa.���`itransAxes���`a,���`a ���`dsize���aoa=���bs2a"���bs2elarge���bs2a"���`a,���`a ���`ecolor���aoa=���bs2a"���bs2htab:blue���bs2a"���`a,���`a
���`l            ���`shorizontalalignment���aoa=���bs2a"���bs2eright���bs2a"���`a,���`a ���`qverticalalignment���aoa=���bs2a"���bs2fcenter���bs2a"���`a)���`a
���`d    ���`bax���aoa.���`dtext���`a(���bmfb.4���`a,���`a ���bmfb.5���`a,���`a ���bnbcstr���`a(���`ginspect���aoa.���`isignature���`a(���`hstylecls���`a)���`a)���`a[���bmia1���`a:���aoa-���bmia1���`a]���aoa.���`greplace���`a(���bs2a"���bs2b, ���bs2a"���`a,���`a ���bs2a"���bseb\n���bs2a"���`a)���`a,���`a
���`l            ���`itransform���aoa=���`bax���aoa.���`itransAxes���`a,���`a
���`l            ���`shorizontalalignment���aoa=���bs2a"���bs2dleft���bs2a"���`a,���`a ���`qverticalalignment���aoa=���bs2a"���bs2fcenter���bs2a"���`a)���`a
���`a
���`a
���bc1xO###############################################################################���`a
���bc1x3# Next we'll show off multiple fancy boxes at once.���`a
���`a
���`a
���akcdef���`a ���bnfvadd_fancy_patch_around���`a(���`bax���`a,���`a ���`bbb���`a,���`a ���aoa*���aoa*���`fkwargs���`a)���`a:���`a
���`d    ���`efancy���`a ���aoa=���`a ���`nFancyBboxPatch���`a(���`a(���`bbb���aoa.���`dxmin���`a,���`a ���`bbb���aoa.���`dymin���`a)���`a,���`a ���`bbb���aoa.���`ewidth���`a,���`a ���`bbb���aoa.���`fheight���`a,���`a
���`x                           ���`bfc���aoa=���`a(���bmia1���`a,���`a ���bmfc0.8���`a,���`a ���bmia1���`a,���`a ���bmfc0.5���`a)���`a,���`a ���`bec���aoa=���`a(���bmia1���`a,���`a ���bmfc0.5���`a,���`a ���bmia1���`a,���`a ���bmfc0.5���`a)���`a,���`a
���`x                           ���aoa*���aoa*���`fkwargs���`a)���`a
���`d    ���`bax���aoa.���`iadd_patch���`a(���`efancy���`a)���`a
���`d    ���akfreturn���`a ���`efancy���`a
���`a
���`a
���akcdef���`a ���bnfxdraw_control_points_for_patches���`a(���`bax���`a)���`a:���`a
���`d    ���akcfor���`a ���`epatch���`a ���bowbin���`a ���`bax���aoa.���`gpatches���`a:���`a
���`h        ���`epatch���aoa.���`daxes���aoa.���`dplot���`a(���aoa*���`epatch���aoa.���`hget_path���`a(���`a)���aoa.���`hvertices���aoa.���`aT���`a,���`a ���bs2a"���bs2a.���bs2a"���`a,���`a
���`x                        ���`ac���aoa=���`epatch���aoa.���`mget_edgecolor���`a(���`a)���`a)���`a
���`a
���`a
���`cfig���`a,���`a ���`caxs���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���bmia2���`a,���`a ���bmia2���`a,���`a ���`gfigsize���aoa=���`a(���bmia8���`a,���`a ���bmia8���`a)���`a)���`a
���`a
���bc1x7# Bbox object around which the fancy box will be drawn.���`a
���`bbb���`a ���aoa=���`a ���`kmtransforms���aoa.���`dBbox���`a(���`a[���`a[���bmfc0.3���`a,���`a ���bmfc0.4���`a]���`a,���`a ���`a[���bmfc0.7���`a,���`a ���bmfc0.6���`a]���`a]���`a)���`a
���`a
���`bax���`a ���aoa=���`a ���`caxs���`a[���bmia0���`a,���`a ���bmia0���`a]���`a
���bc1x)# a fancy box with round corners. pad=0.1���`a
���`efancy���`a ���aoa=���`a ���`vadd_fancy_patch_around���`a(���`bax���`a,���`a ���`bbb���`a,���`a ���`hboxstyle���aoa=���bs2a"���bs2mround,pad=0.1���bs2a"���`a)���`a
���`bax���aoa.���`cset���`a(���`dxlim���aoa=���`a(���bmia0���`a,���`a ���bmia1���`a)���`a,���`a ���`dylim���aoa=���`a(���bmia0���`a,���`a ���bmia1���`a)���`a,���`a ���`faspect���aoa=���bmia1���`a,���`a
���`g       ���`etitle���aoa=���bs1a'���bs1iboxstyle=���bs1a"���bs1mround,pad=0.1���bs1a"���bs1a'���`a)���`a
���`a
���`bax���`a ���aoa=���`a ���`caxs���`a[���bmia0���`a,���`a ���bmia1���`a]���`a
���bc1x?# bbox=round has two optional arguments: pad and rounding_size.���`a
���bc1x,# They can be set during the initialization.���`a
���`efancy���`a ���aoa=���`a ���`vadd_fancy_patch_around���`a(���`bax���`a,���`a ���`bbb���`a,���`a ���`hboxstyle���aoa=���bs2a"���bs2mround,pad=0.1���bs2a"���`a)���`a
���bc1xJ# The boxstyle and its argument can be later modified with set_boxstyle().���`a
���bc1xM# Note that the old attributes are simply forgotten even if the boxstyle name���`a
���bc1j# is same.���`a
���`efancy���aoa.���`lset_boxstyle���`a(���bs2a"���bs2xround,pad=0.1,rounding_size=0.2���bs2a"���`a)���`a
���bc1x=# or: fancy.set_boxstyle("round", pad=0.1, rounding_size=0.2)���`a
���`bax���aoa.���`cset���`a(���`dxlim���aoa=���`a(���bmia0���`a,���`a ���bmia1���`a)���`a,���`a ���`dylim���aoa=���`a(���bmia0���`a,���`a ���bmia1���`a)���`a,���`a ���`faspect���aoa=���bmia1���`a,���`a
���`g       ���`etitle���aoa=���bs1a'���bs1iboxstyle=���bs1a"���bs1xround,pad=0.1,rounding_size=0.2���bs1a"���bs1a'���`a)���`a
���`a
���`bax���`a ���aoa=���`a ���`caxs���`a[���bmia1���`a,���`a ���bmia0���`a]���`a
���bc1xL# mutation_scale determines the overall scale of the mutation, i.e. both pad���`a
���bc1x6# and rounding_size is scaled according to this value.���`a
���`efancy���`a ���aoa=���`a ���`vadd_fancy_patch_around���`a(���`a
���`d    ���`bax���`a,���`a ���`bbb���`a,���`a ���`hboxstyle���aoa=���bs2a"���bs2mround,pad=0.1���bs2a"���`a,���`a ���`nmutation_scale���aoa=���bmia2���`a)���`a
���`bax���aoa.���`cset���`a(���`dxlim���aoa=���`a(���bmia0���`a,���`a ���bmia1���`a)���`a,���`a ���`dylim���aoa=���`a(���bmia0���`a,���`a ���bmia1���`a)���`a,���`a ���`faspect���aoa=���bmia1���`a,���`a
���`g       ���`etitle���aoa=���bs1a'���bs1iboxstyle=���bs1a"���bs1mround,pad=0.1���bs1a"���bseb\n���bs1q mutation_scale=2���bs1a'���`a)���`a
���`a
���`bax���`a ���aoa=���`a ���`caxs���`a[���bmia1���`a,���`a ���bmia1���`a]���`a
���bc1xO# When the aspect ratio of the axes is not 1, the fancy box may not be what you���`a
���bc1s# expected (green).���`a
���`efancy���`a ���aoa=���`a ���`vadd_fancy_patch_around���`a(���`bax���`a,���`a ���`bbb���`a,���`a ���`hboxstyle���aoa=���bs2a"���bs2mround,pad=0.2���bs2a"���`a)���`a
���`efancy���aoa.���`cset���`a(���`ifacecolor���aoa=���bs2a"���bs2dnone���bs2a"���`a,���`a ���`iedgecolor���aoa=���bs2a"���bs2egreen���bs2a"���`a)���`a
���bc1x@# You can compensate this by setting the mutation_aspect (pink).���`a
���`efancy���`a ���aoa=���`a ���`vadd_fancy_patch_around���`a(���`a
���`d    ���`bax���`a,���`a ���`bbb���`a,���`a ���`hboxstyle���aoa=���bs2a"���bs2mround,pad=0.3���bs2a"���`a,���`a ���`omutation_aspect���aoa=���bmfc0.5���`a)���`a
���`bax���aoa.���`cset���`a(���`dxlim���aoa=���`a(���aoa-���bmfb.5���`a,���`a ���bmfc1.5���`a)���`a,���`a ���`dylim���aoa=���`a(���bmia0���`a,���`a ���bmia1���`a)���`a,���`a ���`faspect���aoa=���bmia2���`a,���`a
���`g       ���`etitle���aoa=���bs1a'���bs1iboxstyle=���bs1a"���bs1mround,pad=0.3���bs1a"���bseb\n���bs1rmutation_aspect=.5���bs1a'���`a)���`a
���`a
���akcfor���`a ���`bax���`a ���bowbin���`a ���`caxs���aoa.���`dflat���`a:���`a
���`d    ���`xdraw_control_points_for_patches���`a(���`bax���`a)���`a
���`d    ���bc1x<# Draw the original bbox (using boxstyle=square with pad=0).���`a
���`d    ���`efancy���`a ���aoa=���`a ���`vadd_fancy_patch_around���`a(���`bax���`a,���`a ���`bbb���`a,���`a ���`hboxstyle���aoa=���bs2a"���bs2lsquare,pad=0���bs2a"���`a)���`a
���`d    ���`efancy���aoa.���`cset���`a(���`iedgecolor���aoa=���bs2a"���bs2eblack���bs2a"���`a,���`a ���`ifacecolor���aoa=���bs2a"���bs2dnone���bs2a"���`a,���`a ���`fzorder���aoa=���bmib10���`a)���`a
���`a
���`cfig���aoa.���`ltight_layout���`a(���`a)���`a
���`a
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
���bc1x#    - `matplotlib.patches`���`a
���bc1x*#    - `matplotlib.patches.FancyBboxPatch`���`a
���bc1x$#    - `matplotlib.patches.BoxStyle`���`a
���bc1x1#    - ``matplotlib.patches.BoxStyle.get_styles``���`a
���bc1x##    - `matplotlib.transforms.Bbox`���`a
���bc1x&#    - `matplotlib.figure.Figure.text`���`a
���bc1x"#    - `matplotlib.axes.Axes.text`���`a
`dNone�