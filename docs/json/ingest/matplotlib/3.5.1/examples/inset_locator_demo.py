��������P���bsdxA"""
==================
Inset Locator Demo
==================

"""���`a
���`a
���bc1xO###############################################################################���`a
���bc1x<# The `.inset_locator`'s `~.inset_locator.inset_axes` allows���`a
���bc1xL# easily placing insets in the corners of the axes by specifying a width and���`a
���bc1xI# height and optionally a location (loc) that accepts locations as codes,���`a
���bc1x,# similar to `~matplotlib.axes.Axes.legend`.���`a
���bc1x?# By default, the inset is offset by some points from the axes,���`a
���bc1x+# controlled via the *borderpad* parameter.���`a
���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���bkndfrom���`a ���bnnlmpl_toolkits���bnna.���bnnjaxes_grid1���bnna.���bnnminset_locator���`a ���bknfimport���`a ���`jinset_axes���`a
���`a
���`a
���`cfig���`a,���`a ���`a(���`bax���`a,���`a ���`cax2���`a)���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���bmia1���`a,���`a ���bmia2���`a,���`a ���`gfigsize���aoa=���`a[���bmfc5.5���`a,���`a ���bmfc2.8���`a]���`a)���`a
���`a
���bc1x8# Create inset of width 1.3 inches and height 0.9 inches���`a
���bc1x%# at the default upper right location���`a
���`eaxins���`a ���aoa=���`a ���`jinset_axes���`a(���`bax���`a,���`a ���`ewidth���aoa=���bmfc1.3���`a,���`a ���`fheight���aoa=���bmfc0.9���`a)���`a
���`a
���bc1xK# Create inset of width 30% and height 40% of the parent axes' bounding box���`a
���bc1x"# at the lower left corner (loc=3)���`a
���`faxins2���`a ���aoa=���`a ���`jinset_axes���`a(���`bax���`a,���`a ���`ewidth���aoa=���bs2a"���bs2b30���bs2a%���bs2a"���`a,���`a ���`fheight���aoa=���bs2a"���bs2b40���bs2a%���bs2a"���`a,���`a ���`cloc���aoa=���bmia3���`a)���`a
���`a
���bc1x=# Create inset of mixed specifications in the second subplot;���`a
���bc1x/# width is 30% of parent axes' bounding box and���`a
���bc1x3# height is 1 inch at the upper left corner (loc=2)���`a
���`faxins3���`a ���aoa=���`a ���`jinset_axes���`a(���`cax2���`a,���`a ���`ewidth���aoa=���bs2a"���bs2b30���bs2a%���bs2a"���`a,���`a ���`fheight���aoa=���bmfb1.���`a,���`a ���`cloc���aoa=���bmia2���`a)���`a
���`a
���bc1xJ# Create an inset in the lower right corner (loc=4) with borderpad=1, i.e.���`a
���bc1xH# 10 points padding (as 10pt is the default fontsize) to the parent axes���`a
���`faxins4���`a ���aoa=���`a ���`jinset_axes���`a(���`cax2���`a,���`a ���`ewidth���aoa=���bs2a"���bs2b20���bs2a%���bs2a"���`a,���`a ���`fheight���aoa=���bs2a"���bs2b20���bs2a%���bs2a"���`a,���`a ���`cloc���aoa=���bmia4���`a,���`a ���`iborderpad���aoa=���bmia1���`a)���`a
���`a
���bc1x# Turn ticklabels of insets off���`a
���akcfor���`a ���`caxi���`a ���bowbin���`a ���`a[���`eaxins���`a,���`a ���`faxins2���`a,���`a ���`faxins3���`a,���`a ���`faxins4���`a]���`a:���`a
���`d    ���`caxi���aoa.���`ktick_params���`a(���`ilabelleft���aoa=���bkceFalse���`a,���`a ���`klabelbottom���aoa=���bkceFalse���`a)���`a
���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
���`a
���`a
���bc1xO###############################################################################���`a
���bc1xM# The parameters *bbox_to_anchor* and *bbox_transform* can be used for a more���`a
���bc1xK# fine grained control over the inset position and size or even to position���`a
���bc1x.# the inset at completely arbitrary positions.���`a
���bc1xL# The *bbox_to_anchor* sets the bounding box in coordinates according to the���`a
���bc1s# *bbox_transform*.���`a
���bc1a#���`a
���`a
���`cfig���`a ���aoa=���`a ���`cplt���aoa.���`ffigure���`a(���`gfigsize���aoa=���`a[���bmfc5.5���`a,���`a ���bmfc2.8���`a]���`a)���`a
���`bax���`a ���aoa=���`a ���`cfig���aoa.���`kadd_subplot���`a(���bmic121���`a)���`a
���`a
���bc1xI# We use the axes transform as bbox_transform. Therefore the bounding box���`a
���bc1xL# needs to be specified in axes coordinates ((0, 0) is the lower left corner���`a
���bc1x1# of the axes, (1, 1) is the upper right corner).���`a
���bc1xM# The bounding box (.2, .4, .6, .5) starts at (.2, .4) and ranges to (.8, .9)���`a
���bc1w# in those coordinates.���`a
���bc1xJ# Inside of this bounding box an inset of half the bounding box' width and���`a
���bc1xN# three quarters of the bounding box' height is created. The lower left corner���`a
���bc1xO# of the inset is aligned to the lower left corner of the bounding box (loc=3).���`a
���bc1xH# The inset is then offset by the default 0.5 in units of the font size.���`a
���`a
���`eaxins���`a ���aoa=���`a ���`jinset_axes���`a(���`bax���`a,���`a ���`ewidth���aoa=���bs2a"���bs2b50���bs2a%���bs2a"���`a,���`a ���`fheight���aoa=���bs2a"���bs2b75���bs2a%���bs2a"���`a,���`a
���`s                   ���`nbbox_to_anchor���aoa=���`a(���bmfb.2���`a,���`a ���bmfb.4���`a,���`a ���bmfb.6���`a,���`a ���bmfb.5���`a)���`a,���`a
���`s                   ���`nbbox_transform���aoa=���`bax���aoa.���`itransAxes���`a,���`a ���`cloc���aoa=���bmia3���`a)���`a
���`a
���bc1xD# For visualization purposes we mark the bounding box by a rectangle���`a
���`bax���aoa.���`iadd_patch���`a(���`cplt���aoa.���`iRectangle���`a(���`a(���bmfb.2���`a,���`a ���bmfb.4���`a)���`a,���`a ���bmfb.6���`a,���`a ���bmfb.5���`a,���`a ���`bls���aoa=���bs2a"���bs2b--���bs2a"���`a,���`a ���`bec���aoa=���bs2a"���bs2ac���bs2a"���`a,���`a ���`bfc���aoa=���bs2a"���bs2dnone���bs2a"���`a,���`a
���`x                           ���`itransform���aoa=���`bax���aoa.���`itransAxes���`a)���`a)���`a
���`a
���bc1xM# We set the axis limits to something other than the default, in order to not���`a
���bc1x=# distract from the fact that axes coordinates are used here.���`a
���`bax���aoa.���`cset���`a(���`dxlim���aoa=���`a(���bmia0���`a,���`a ���bmib10���`a)���`a,���`a ���`dylim���aoa=���`a(���bmia0���`a,���`a ���bmib10���`a)���`a)���`a
���`a
���`a
���bc1xM# Note how the two following insets are created at the same positions, one by���`a
���bc1xG# use of the default parent axes' bbox and the other via a bbox in axes���`a
���bc1x+# coordinates and the respective transform.���`a
���`cax2���`a ���aoa=���`a ���`cfig���aoa.���`kadd_subplot���`a(���bmic222���`a)���`a
���`faxins2���`a ���aoa=���`a ���`jinset_axes���`a(���`cax2���`a,���`a ���`ewidth���aoa=���bs2a"���bs2b30���bs2a%���bs2a"���`a,���`a ���`fheight���aoa=���bs2a"���bs2b50���bs2a%���bs2a"���`a)���`a
���`a
���`cax3���`a ���aoa=���`a ���`cfig���aoa.���`kadd_subplot���`a(���bmic224���`a)���`a
���`faxins3���`a ���aoa=���`a ���`jinset_axes���`a(���`cax3���`a,���`a ���`ewidth���aoa=���bs2a"���bs2c100���bs2a%���bs2a"���`a,���`a ���`fheight���aoa=���bs2a"���bs2c100���bs2a%���bs2a"���`a,���`a
���`t                    ���`nbbox_to_anchor���aoa=���`a(���bmfb.7���`a,���`a ���bmfb.5���`a,���`a ���bmfb.3���`a,���`a ���bmfb.5���`a)���`a,���`a
���`t                    ���`nbbox_transform���aoa=���`cax3���aoa.���`itransAxes���`a)���`a
���`a
���bc1xD# For visualization purposes we mark the bounding box by a rectangle���`a
���`cax2���aoa.���`iadd_patch���`a(���`cplt���aoa.���`iRectangle���`a(���`a(���bmia0���`a,���`a ���bmia0���`a)���`a,���`a ���bmia1���`a,���`a ���bmia1���`a,���`a ���`bls���aoa=���bs2a"���bs2b--���bs2a"���`a,���`a ���`blw���aoa=���bmia2���`a,���`a ���`bec���aoa=���bs2a"���bs2ac���bs2a"���`a,���`a ���`bfc���aoa=���bs2a"���bs2dnone���bs2a"���`a)���`a)���`a
���`cax3���aoa.���`iadd_patch���`a(���`cplt���aoa.���`iRectangle���`a(���`a(���bmfb.7���`a,���`a ���bmfb.5���`a)���`a,���`a ���bmfb.3���`a,���`a ���bmfb.5���`a,���`a ���`bls���aoa=���bs2a"���bs2b--���bs2a"���`a,���`a ���`blw���aoa=���bmia2���`a,���`a
���`x                            ���`bec���aoa=���bs2a"���bs2ac���bs2a"���`a,���`a ���`bfc���aoa=���bs2a"���bs2dnone���bs2a"���`a)���`a)���`a
���`a
���bc1u# Turn ticklabels off���`a
���akcfor���`a ���`caxi���`a ���bowbin���`a ���`a[���`faxins2���`a,���`a ���`faxins3���`a,���`a ���`cax2���`a,���`a ���`cax3���`a]���`a:���`a
���`d    ���`caxi���aoa.���`ktick_params���`a(���`ilabelleft���aoa=���bkceFalse���`a,���`a ���`klabelbottom���aoa=���bkceFalse���`a)���`a
���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
���`a
���`a
���bc1xO###############################################################################���`a
���bc1xO# In the above the axes transform together with 4-tuple bounding boxes has been���`a
���bc1xL# used as it mostly is useful to specify an inset relative to the axes it is���`a
���bc1xJ# an inset to. However other use cases are equally possible. The following���`a
���bc1x!# example examines some of those.���`a
���bc1a#���`a
���`a
���`cfig���`a ���aoa=���`a ���`cplt���aoa.���`ffigure���`a(���`gfigsize���aoa=���`a[���bmfc5.5���`a,���`a ���bmfc2.8���`a]���`a)���`a
���`bax���`a ���aoa=���`a ���`cfig���aoa.���`kadd_subplot���`a(���bmic131���`a)���`a
���`a
���bc1x"# Create an inset outside the axes���`a
���`eaxins���`a ���aoa=���`a ���`jinset_axes���`a(���`bax���`a,���`a ���`ewidth���aoa=���bs2a"���bs2c100���bs2a%���bs2a"���`a,���`a ���`fheight���aoa=���bs2a"���bs2c100���bs2a%���bs2a"���`a,���`a
���`s                   ���`nbbox_to_anchor���aoa=���`a(���bmfd1.05���`a,���`a ���bmfb.6���`a,���`a ���bmfb.5���`a,���`a ���bmfb.4���`a)���`a,���`a
���`s                   ���`nbbox_transform���aoa=���`bax���aoa.���`itransAxes���`a,���`a ���`cloc���aoa=���bmia2���`a,���`a ���`iborderpad���aoa=���bmia0���`a)���`a
���`eaxins���aoa.���`ktick_params���`a(���`dleft���aoa=���bkceFalse���`a,���`a ���`eright���aoa=���bkcdTrue���`a,���`a ���`ilabelleft���aoa=���bkceFalse���`a,���`a ���`jlabelright���aoa=���bkcdTrue���`a)���`a
���`a
���bc1xG# Create an inset with a 2-tuple bounding box. Note that this creates a���`a
���bc1xB# bbox without extent. This hence only makes sense when specifying���`a
���bc1x.# width and height in absolute units (inches).���`a
���`faxins2���`a ���aoa=���`a ���`jinset_axes���`a(���`bax���`a,���`a ���`ewidth���aoa=���bmfc0.5���`a,���`a ���`fheight���aoa=���bmfc0.4���`a,���`a
���`t                    ���`nbbox_to_anchor���aoa=���`a(���bmfd0.33���`a,���`a ���bmfd0.25���`a)���`a,���`a
���`t                    ���`nbbox_transform���aoa=���`bax���aoa.���`itransAxes���`a,���`a ���`cloc���aoa=���bmia3���`a,���`a ���`iborderpad���aoa=���bmia0���`a)���`a
���`a
���`a
���`cax2���`a ���aoa=���`a ���`cfig���aoa.���`kadd_subplot���`a(���bmic133���`a)���`a
���`cax2���aoa.���`jset_xscale���`a(���bs2a"���bs2clog���bs2a"���`a)���`a
���`cax2���aoa.���`cset���`a(���`dxlim���aoa=���`a(���bmfd1e-6���`a,���`a ���bmfc1e6���`a)���`a,���`a ���`dylim���aoa=���`a(���aoa-���bmia2���`a,���`a ���bmia6���`a)���`a)���`a
���`a
���bc1xB# Create inset in data coordinates using ax.transData as transform���`a
���`faxins3���`a ���aoa=���`a ���`jinset_axes���`a(���`cax2���`a,���`a ���`ewidth���aoa=���bs2a"���bs2c100���bs2a%���bs2a"���`a,���`a ���`fheight���aoa=���bs2a"���bs2c100���bs2a%���bs2a"���`a,���`a
���`t                    ���`nbbox_to_anchor���aoa=���`a(���bmfd1e-2���`a,���`a ���bmia2���`a,���`a ���bmfc1e3���`a,���`a ���bmia3���`a)���`a,���`a
���`t                    ���`nbbox_transform���aoa=���`cax2���aoa.���`itransData���`a,���`a ���`cloc���aoa=���bmia2���`a,���`a ���`iborderpad���aoa=���bmia0���`a)���`a
���`a
���bc1xL# Create an inset horizontally centered in figure coordinates and vertically���`a
���bc1x!# bound to line up with the axes.���`a
���bkndfrom���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnjtransforms���`a ���bknfimport���`a ���`xblended_transform_factory���`b  ���bc1f# noqa���`a
���`itransform���`a ���aoa=���`a ���`xblended_transform_factory���`a(���`cfig���aoa.���`ktransFigure���`a,���`a ���`cax2���aoa.���`itransAxes���`a)���`a
���`faxins4���`a ���aoa=���`a ���`jinset_axes���`a(���`cax2���`a,���`a ���`ewidth���aoa=���bs2a"���bs2b16���bs2a%���bs2a"���`a,���`a ���`fheight���aoa=���bs2a"���bs2b34���bs2a%���bs2a"���`a,���`a
���`t                    ���`nbbox_to_anchor���aoa=���`a(���bmia0���`a,���`a ���bmia0���`a,���`a ���bmia1���`a,���`a ���bmia1���`a)���`a,���`a
���`t                    ���`nbbox_transform���aoa=���`itransform���`a,���`a ���`cloc���aoa=���bmia8���`a,���`a ���`iborderpad���aoa=���bmia0���`a)���`a
���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
`dNone�