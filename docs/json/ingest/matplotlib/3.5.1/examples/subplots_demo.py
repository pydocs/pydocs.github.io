������������bsdy�"""
=================================================
Creating multiple subplots using ``plt.subplots``
=================================================

`.pyplot.subplots` creates a figure and a grid of subplots with a single call,
while providing reasonable control over how the individual plots are created.
For more advanced use cases you can use `.GridSpec` for a more general subplot
layout or `.Figure.add_subplot` for adding subplots at arbitrary locations
within the figure.
"""���`a
���`a
���bc1x&# sphinx_gallery_thumbnail_number = 11���`a
���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���`a
���bc1x# Some example data to display���`a
���`ax���`a ���aoa=���`a ���`bnp���aoa.���`hlinspace���`a(���bmia0���`a,���`a ���bmia2���`a ���aoa*���`a ���`bnp���aoa.���`bpi���`a,���`a ���bmic400���`a)���`a
���`ay���`a ���aoa=���`a ���`bnp���aoa.���`csin���`a(���`ax���`a ���aoa*���aoa*���`a ���bmia2���`a)���`a
���`a
���bc1xO###############################################################################���`a
���bc1x # A figure with just one subplot���`a
���bc1x # """"""""""""""""""""""""""""""���`a
���bc1a#���`a
���bc1xC# ``subplots()`` without arguments returns a `.Figure` and a single���`a
���bc1p# `~.axes.Axes`.���`a
���bc1a#���`a
���bc1xH# This is actually the simplest and recommended way of creating a single���`a
���bc1r# Figure and Axes.���`a
���`a
���`cfig���`a,���`a ���`bax���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`a)���`a
���`bax���aoa.���`dplot���`a(���`ax���`a,���`a ���`ay���`a)���`a
���`bax���aoa.���`iset_title���`a(���bs1a'���bs1mA single plot���bs1a'���`a)���`a
���`a
���bc1xO###############################################################################���`a
���bc1x$# Stacking subplots in one direction���`a
���bc1x$# """"""""""""""""""""""""""""""""""���`a
���bc1a#���`a
���bc1xM# The first two optional arguments of `.pyplot.subplots` define the number of���`a
���bc1x'# rows and columns of the subplot grid.���`a
���bc1a#���`a
���bc1xO# When stacking in one direction only, the returned ``axs`` is a 1D numpy array���`a
���bc1x&# containing the list of created Axes.���`a
���`a
���`cfig���`a,���`a ���`caxs���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���bmia2���`a)���`a
���`cfig���aoa.���`hsuptitle���`a(���bs1a'���bs1xVertically stacked subplots���bs1a'���`a)���`a
���`caxs���`a[���bmia0���`a]���aoa.���`dplot���`a(���`ax���`a,���`a ���`ay���`a)���`a
���`caxs���`a[���bmia1���`a]���aoa.���`dplot���`a(���`ax���`a,���`a ���aoa-���`ay���`a)���`a
���`a
���bc1xO###############################################################################���`a
���bc1xO# If you are creating just a few Axes, it's handy to unpack them immediately to���`a
���bc1xL# dedicated variables for each Axes. That way, we can use ``ax1`` instead of���`a
���bc1x# the more verbose ``axs[0]``.���`a
���`a
���`cfig���`a,���`a ���`a(���`cax1���`a,���`a ���`cax2���`a)���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���bmia2���`a)���`a
���`cfig���aoa.���`hsuptitle���`a(���bs1a'���bs1xVertically stacked subplots���bs1a'���`a)���`a
���`cax1���aoa.���`dplot���`a(���`ax���`a,���`a ���`ay���`a)���`a
���`cax2���aoa.���`dplot���`a(���`ax���`a,���`a ���aoa-���`ay���`a)���`a
���`a
���bc1xO###############################################################################���`a
���bc1xO# To obtain side-by-side subplots, pass parameters ``1, 2`` for one row and two���`a
���bc1j# columns.���`a
���`a
���`cfig���`a,���`a ���`a(���`cax1���`a,���`a ���`cax2���`a)���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���bmia1���`a,���`a ���bmia2���`a)���`a
���`cfig���aoa.���`hsuptitle���`a(���bs1a'���bs1xHorizontally stacked subplots���bs1a'���`a)���`a
���`cax1���aoa.���`dplot���`a(���`ax���`a,���`a ���`ay���`a)���`a
���`cax2���aoa.���`dplot���`a(���`ax���`a,���`a ���aoa-���`ay���`a)���`a
���`a
���bc1xO###############################################################################���`a
���bc1x%# Stacking subplots in two directions���`a
���bc1x%# """""""""""""""""""""""""""""""""""���`a
���bc1a#���`a
���bc1xL# When stacking in two directions, the returned ``axs`` is a 2D NumPy array.���`a
���bc1a#���`a
���bc1xK# If you have to set parameters for each subplot it's handy to iterate over���`a
���bc1x:# all subplots in a 2D grid using ``for ax in axs.flat:``.���`a
���`a
���`cfig���`a,���`a ���`caxs���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���bmia2���`a,���`a ���bmia2���`a)���`a
���`caxs���`a[���bmia0���`a,���`a ���bmia0���`a]���aoa.���`dplot���`a(���`ax���`a,���`a ���`ay���`a)���`a
���`caxs���`a[���bmia0���`a,���`a ���bmia0���`a]���aoa.���`iset_title���`a(���bs1a'���bs1kAxis [0, 0]���bs1a'���`a)���`a
���`caxs���`a[���bmia0���`a,���`a ���bmia1���`a]���aoa.���`dplot���`a(���`ax���`a,���`a ���`ay���`a,���`a ���bs1a'���bs1jtab:orange���bs1a'���`a)���`a
���`caxs���`a[���bmia0���`a,���`a ���bmia1���`a]���aoa.���`iset_title���`a(���bs1a'���bs1kAxis [0, 1]���bs1a'���`a)���`a
���`caxs���`a[���bmia1���`a,���`a ���bmia0���`a]���aoa.���`dplot���`a(���`ax���`a,���`a ���aoa-���`ay���`a,���`a ���bs1a'���bs1itab:green���bs1a'���`a)���`a
���`caxs���`a[���bmia1���`a,���`a ���bmia0���`a]���aoa.���`iset_title���`a(���bs1a'���bs1kAxis [1, 0]���bs1a'���`a)���`a
���`caxs���`a[���bmia1���`a,���`a ���bmia1���`a]���aoa.���`dplot���`a(���`ax���`a,���`a ���aoa-���`ay���`a,���`a ���bs1a'���bs1gtab:red���bs1a'���`a)���`a
���`caxs���`a[���bmia1���`a,���`a ���bmia1���`a]���aoa.���`iset_title���`a(���bs1a'���bs1kAxis [1, 1]���bs1a'���`a)���`a
���`a
���akcfor���`a ���`bax���`a ���bowbin���`a ���`caxs���aoa.���`dflat���`a:���`a
���`d    ���`bax���aoa.���`cset���`a(���`fxlabel���aoa=���bs1a'���bs1gx-label���bs1a'���`a,���`a ���`fylabel���aoa=���bs1a'���bs1gy-label���bs1a'���`a)���`a
���`a
���bc1xJ# Hide x labels and tick labels for top plots and y ticks for right plots.���`a
���akcfor���`a ���`bax���`a ���bowbin���`a ���`caxs���aoa.���`dflat���`a:���`a
���`d    ���`bax���aoa.���`klabel_outer���`a(���`a)���`a
���`a
���bc1xO###############################################################################���`a
���bc1xL# You can use tuple-unpacking also in 2D to assign all subplots to dedicated���`a
���bc1l# variables:���`a
���`a
���`cfig���`a,���`a ���`a(���`a(���`cax1���`a,���`a ���`cax2���`a)���`a,���`a ���`a(���`cax3���`a,���`a ���`cax4���`a)���`a)���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���bmia2���`a,���`a ���bmia2���`a)���`a
���`cfig���aoa.���`hsuptitle���`a(���bs1a'���bs1xSharing x per column, y per row���bs1a'���`a)���`a
���`cax1���aoa.���`dplot���`a(���`ax���`a,���`a ���`ay���`a)���`a
���`cax2���aoa.���`dplot���`a(���`ax���`a,���`a ���`ay���aoa*���aoa*���bmia2���`a,���`a ���bs1a'���bs1jtab:orange���bs1a'���`a)���`a
���`cax3���aoa.���`dplot���`a(���`ax���`a,���`a ���aoa-���`ay���`a,���`a ���bs1a'���bs1itab:green���bs1a'���`a)���`a
���`cax4���aoa.���`dplot���`a(���`ax���`a,���`a ���aoa-���`ay���aoa*���aoa*���bmia2���`a,���`a ���bs1a'���bs1gtab:red���bs1a'���`a)���`a
���`a
���akcfor���`a ���`bax���`a ���bowbin���`a ���`cfig���aoa.���`hget_axes���`a(���`a)���`a:���`a
���`d    ���`bax���aoa.���`klabel_outer���`a(���`a)���`a
���`a
���bc1xO###############################################################################���`a
���bc1n# Sharing axes���`a
���bc1n# """"""""""""���`a
���bc1a#���`a
���bc1xG# By default, each Axes is scaled individually. Thus, if the ranges are���`a
���bc1x9# different the tick values of the subplots do not align.���`a
���`a
���`cfig���`a,���`a ���`a(���`cax1���`a,���`a ���`cax2���`a)���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���bmia2���`a)���`a
���`cfig���aoa.���`hsuptitle���`a(���bs1a'���bs1x.Axes values are scaled individually by default���bs1a'���`a)���`a
���`cax1���aoa.���`dplot���`a(���`ax���`a,���`a ���`ay���`a)���`a
���`cax2���aoa.���`dplot���`a(���`ax���`a ���aoa+���`a ���bmia1���`a,���`a ���aoa-���`ay���`a)���`a
���`a
���bc1xO###############################################################################���`a
���bc1xL# You can use *sharex* or *sharey* to align the horizontal or vertical axis.���`a
���`a
���`cfig���`a,���`a ���`a(���`cax1���`a,���`a ���`cax2���`a)���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���bmia2���`a,���`a ���`fsharex���aoa=���bkcdTrue���`a)���`a
���`cfig���aoa.���`hsuptitle���`a(���bs1a'���bs1xAligning x-axis using sharex���bs1a'���`a)���`a
���`cax1���aoa.���`dplot���`a(���`ax���`a,���`a ���`ay���`a)���`a
���`cax2���aoa.���`dplot���`a(���`ax���`a ���aoa+���`a ���bmia1���`a,���`a ���aoa-���`ay���`a)���`a
���`a
���bc1xO###############################################################################���`a
���bc1xL# Setting *sharex* or *sharey* to ``True`` enables global sharing across the���`a
���bc1xJ# whole grid, i.e. also the y-axes of vertically stacked subplots have the���`a
���bc1x(# same scale when using ``sharey=True``.���`a
���`a
���`cfig���`a,���`a ���`caxs���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���bmia3���`a,���`a ���`fsharex���aoa=���bkcdTrue���`a,���`a ���`fsharey���aoa=���bkcdTrue���`a)���`a
���`cfig���aoa.���`hsuptitle���`a(���bs1a'���bs1qSharing both axes���bs1a'���`a)���`a
���`caxs���`a[���bmia0���`a]���aoa.���`dplot���`a(���`ax���`a,���`a ���`ay���`a ���aoa*���aoa*���`a ���bmia2���`a)���`a
���`caxs���`a[���bmia1���`a]���aoa.���`dplot���`a(���`ax���`a,���`a ���bmfc0.3���`a ���aoa*���`a ���`ay���`a,���`a ���bs1a'���bs1ao���bs1a'���`a)���`a
���`caxs���`a[���bmia2���`a]���aoa.���`dplot���`a(���`ax���`a,���`a ���`ay���`a,���`a ���bs1a'���bs1a+���bs1a'���`a)���`a
���`a
���bc1xO###############################################################################���`a
���bc1xK# For subplots that are sharing axes one set of tick labels is enough. Tick���`a
���bc1xJ# labels of inner Axes are automatically removed by *sharex* and *sharey*.���`a
���bc1xA# Still there remains an unused empty space between the subplots.���`a
���bc1a#���`a
���bc1xJ# To precisely control the positioning of the subplots, one can explicitly���`a
���bc1xE# create a `.GridSpec` with `.Figure.add_gridspec`, and then call its���`a
���bc1xJ# `~.GridSpecBase.subplots` method.  For example, we can reduce the height���`a
���bc1x=# between vertical subplots using ``add_gridspec(hspace=0)``.���`a
���bc1a#���`a
���bc1xK# `.label_outer` is a handy method to remove labels and ticks from subplots���`a
���bc1x'# that are not at the edge of the grid.���`a
���`a
���`cfig���`a ���aoa=���`a ���`cplt���aoa.���`ffigure���`a(���`a)���`a
���`bgs���`a ���aoa=���`a ���`cfig���aoa.���`ladd_gridspec���`a(���bmia3���`a,���`a ���`fhspace���aoa=���bmia0���`a)���`a
���`caxs���`a ���aoa=���`a ���`bgs���aoa.���`hsubplots���`a(���`fsharex���aoa=���bkcdTrue���`a,���`a ���`fsharey���aoa=���bkcdTrue���`a)���`a
���`cfig���aoa.���`hsuptitle���`a(���bs1a'���bs1qSharing both axes���bs1a'���`a)���`a
���`caxs���`a[���bmia0���`a]���aoa.���`dplot���`a(���`ax���`a,���`a ���`ay���`a ���aoa*���aoa*���`a ���bmia2���`a)���`a
���`caxs���`a[���bmia1���`a]���aoa.���`dplot���`a(���`ax���`a,���`a ���bmfc0.3���`a ���aoa*���`a ���`ay���`a,���`a ���bs1a'���bs1ao���bs1a'���`a)���`a
���`caxs���`a[���bmia2���`a]���aoa.���`dplot���`a(���`ax���`a,���`a ���`ay���`a,���`a ���bs1a'���bs1a+���bs1a'���`a)���`a
���`a
���bc1x8# Hide x labels and tick labels for all but bottom plot.���`a
���akcfor���`a ���`bax���`a ���bowbin���`a ���`caxs���`a:���`a
���`d    ���`bax���aoa.���`klabel_outer���`a(���`a)���`a
���`a
���bc1xO###############################################################################���`a
���bc1xJ# Apart from ``True`` and ``False``, both *sharex* and *sharey* accept the���`a
���bc1xD# values 'row' and 'col' to share the values only per row or column.���`a
���`a
���`cfig���`a ���aoa=���`a ���`cplt���aoa.���`ffigure���`a(���`a)���`a
���`bgs���`a ���aoa=���`a ���`cfig���aoa.���`ladd_gridspec���`a(���bmia2���`a,���`a ���bmia2���`a,���`a ���`fhspace���aoa=���bmia0���`a,���`a ���`fwspace���aoa=���bmia0���`a)���`a
���`a(���`cax1���`a,���`a ���`cax2���`a)���`a,���`a ���`a(���`cax3���`a,���`a ���`cax4���`a)���`a ���aoa=���`a ���`bgs���aoa.���`hsubplots���`a(���`fsharex���aoa=���bs1a'���bs1ccol���bs1a'���`a,���`a ���`fsharey���aoa=���bs1a'���bs1crow���bs1a'���`a)���`a
���`cfig���aoa.���`hsuptitle���`a(���bs1a'���bs1xSharing x per column, y per row���bs1a'���`a)���`a
���`cax1���aoa.���`dplot���`a(���`ax���`a,���`a ���`ay���`a)���`a
���`cax2���aoa.���`dplot���`a(���`ax���`a,���`a ���`ay���aoa*���aoa*���bmia2���`a,���`a ���bs1a'���bs1jtab:orange���bs1a'���`a)���`a
���`cax3���aoa.���`dplot���`a(���`ax���`a ���aoa+���`a ���bmia1���`a,���`a ���aoa-���`ay���`a,���`a ���bs1a'���bs1itab:green���bs1a'���`a)���`a
���`cax4���aoa.���`dplot���`a(���`ax���`a ���aoa+���`a ���bmia2���`a,���`a ���aoa-���`ay���aoa*���aoa*���bmia2���`a,���`a ���bs1a'���bs1gtab:red���bs1a'���`a)���`a
���`a
���akcfor���`a ���`bax���`a ���bowbin���`a ���`caxs���aoa.���`dflat���`a:���`a
���`d    ���`bax���aoa.���`klabel_outer���`a(���`a)���`a
���`a
���bc1xO###############################################################################���`a
���bc1xH# If you want a more complex sharing structure, you can first create the���`a
���bc1xD# grid of axes with no sharing, and then call `.axes.Axes.sharex` or���`a
���bc1x7# `.axes.Axes.sharey` to add sharing info a posteriori.���`a
���`a
���`cfig���`a,���`a ���`caxs���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���bmia2���`a,���`a ���bmia2���`a)���`a
���`caxs���`a[���bmia0���`a,���`a ���bmia0���`a]���aoa.���`dplot���`a(���`ax���`a,���`a ���`ay���`a)���`a
���`caxs���`a[���bmia0���`a,���`a ���bmia0���`a]���aoa.���`iset_title���`a(���bs2a"���bs2dmain���bs2a"���`a)���`a
���`caxs���`a[���bmia1���`a,���`a ���bmia0���`a]���aoa.���`dplot���`a(���`ax���`a,���`a ���`ay���aoa*���aoa*���bmia2���`a)���`a
���`caxs���`a[���bmia1���`a,���`a ���bmia0���`a]���aoa.���`iset_title���`a(���bs2a"���bs2rshares x with main���bs2a"���`a)���`a
���`caxs���`a[���bmia1���`a,���`a ���bmia0���`a]���aoa.���`fsharex���`a(���`caxs���`a[���bmia0���`a,���`a ���bmia0���`a]���`a)���`a
���`caxs���`a[���bmia0���`a,���`a ���bmia1���`a]���aoa.���`dplot���`a(���`ax���`a ���aoa+���`a ���bmia1���`a,���`a ���`ay���`a ���aoa+���`a ���bmia1���`a)���`a
���`caxs���`a[���bmia0���`a,���`a ���bmia1���`a]���aoa.���`iset_title���`a(���bs2a"���bs2iunrelated���bs2a"���`a)���`a
���`caxs���`a[���bmia1���`a,���`a ���bmia1���`a]���aoa.���`dplot���`a(���`ax���`a ���aoa+���`a ���bmia2���`a,���`a ���`ay���`a ���aoa+���`a ���bmia2���`a)���`a
���`caxs���`a[���bmia1���`a,���`a ���bmia1���`a]���aoa.���`iset_title���`a(���bs2a"���bs2nalso unrelated���bs2a"���`a)���`a
���`cfig���aoa.���`ltight_layout���`a(���`a)���`a
���`a
���bc1xO###############################################################################���`a
���bc1l# Polar axes���`a
���bc1l# """"""""""���`a
���bc1a#���`a
���bc1xG# The parameter *subplot_kw* of `.pyplot.subplots` controls the subplot���`a
���bc1xN# properties (see also `.Figure.add_subplot`). In particular, this can be used���`a
���bc1x!# to create a grid of polar Axes.���`a
���`a
���`cfig���`a,���`a ���`a(���`cax1���`a,���`a ���`cax2���`a)���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���bmia1���`a,���`a ���bmia2���`a,���`a ���`jsubplot_kw���aoa=���bnbddict���`a(���`jprojection���aoa=���bs1a'���bs1epolar���bs1a'���`a)���`a)���`a
���`cax1���aoa.���`dplot���`a(���`ax���`a,���`a ���`ay���`a)���`a
���`cax2���aoa.���`dplot���`a(���`ax���`a,���`a ���`ay���`a ���aoa*���aoa*���`a ���bmia2���`a)���`a
���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
`dNone�