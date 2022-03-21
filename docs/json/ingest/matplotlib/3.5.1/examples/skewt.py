������������bsdy """
===========================================================
SkewT-logP diagram: using transforms and custom projections
===========================================================

This serves as an intensive exercise of Matplotlib's transforms and custom
projection API. This example produces a so-called SkewT-logP diagram, which is
a common plot in meteorology for displaying vertical profiles of temperature.
As far as Matplotlib is concerned, the complexity comes from having X and Y
axes that are not orthogonal. This is handled by including a skew component to
the basic Axes transforms. Additional complexity comes in handling the fact
that the upper and lower X-axes have different data ranges, which necessitates
a bunch of custom classes for ticks, spines, and axis to handle this.
"""���`a
���`a
���bkndfrom���`a ���bnnjcontextlib���`a ���bknfimport���`a ���`iExitStack���`a
���`a
���bkndfrom���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnndaxes���`a ���bknfimport���`a ���`dAxes���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnjtransforms���`a ���akbas���`a ���bnnjtransforms���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnndaxis���`a ���akbas���`a ���bnnemaxis���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfspines���`a ���akbas���`a ���bnngmspines���`a
���bkndfrom���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnkprojections���`a ���bknfimport���`a ���`sregister_projection���`a
���`a
���`a
���bc1xI# The sole purpose of this class is to look at the upper, lower, or total���`a
���bc1xI# interval as appropriate and see what parts of the tick to draw, if any.���`a
���akeclass���`a ���bnciSkewXTick���`a(���`emaxis���aoa.���`eXTick���`a)���`a:���`a
���`d    ���akcdef���`a ���bnfddraw���`a(���bbpdself���`a,���`a ���`hrenderer���`a)���`a:���`a
���`h        ���bc1xG# When adding the callbacks with `stack.callback`, we fetch the current���`a
���`h        ���bc1xG# visibility state of the artist with `get_visible`; the ExitStack will���`a
���`h        ���bc1xE# restore these states (`set_visible`) at the end of the block (after���`a
���`h        ���bc1l# the draw).���`a
���`h        ���akdwith���`a ���`iExitStack���`a(���`a)���`a ���akbas���`a ���`estack���`a:���`a
���`l            ���akcfor���`a ���`fartist���`a ���bowbin���`a ���`a[���bbpdself���aoa.���`hgridline���`a,���`a ���bbpdself���aoa.���`itick1line���`a,���`a ���bbpdself���aoa.���`itick2line���`a,���`a
���`x                           ���bbpdself���aoa.���`flabel1���`a,���`a ���bbpdself���aoa.���`flabel2���`a]���`a:���`a
���`p                ���`estack���aoa.���`hcallback���`a(���`fartist���aoa.���`kset_visible���`a,���`a ���`fartist���aoa.���`kget_visible���`a(���`a)���`a)���`a
���`l            ���`kneeds_lower���`a ���aoa=���`a ���`jtransforms���aoa.���`qinterval_contains���`a(���`a
���`p                ���bbpdself���aoa.���`daxes���aoa.���`jlower_xlim���`a,���`a ���bbpdself���aoa.���`gget_loc���`a(���`a)���`a)���`a
���`l            ���`kneeds_upper���`a ���aoa=���`a ���`jtransforms���aoa.���`qinterval_contains���`a(���`a
���`p                ���bbpdself���aoa.���`daxes���aoa.���`jupper_xlim���`a,���`a ���bbpdself���aoa.���`gget_loc���`a(���`a)���`a)���`a
���`l            ���bbpdself���aoa.���`itick1line���aoa.���`kset_visible���`a(���`a
���`p                ���bbpdself���aoa.���`itick1line���aoa.���`kget_visible���`a(���`a)���`a ���bowcand���`a ���`kneeds_lower���`a)���`a
���`l            ���bbpdself���aoa.���`flabel1���aoa.���`kset_visible���`a(���`a
���`p                ���bbpdself���aoa.���`flabel1���aoa.���`kget_visible���`a(���`a)���`a ���bowcand���`a ���`kneeds_lower���`a)���`a
���`l            ���bbpdself���aoa.���`itick2line���aoa.���`kset_visible���`a(���`a
���`p                ���bbpdself���aoa.���`itick2line���aoa.���`kget_visible���`a(���`a)���`a ���bowcand���`a ���`kneeds_upper���`a)���`a
���`l            ���bbpdself���aoa.���`flabel2���aoa.���`kset_visible���`a(���`a
���`p                ���bbpdself���aoa.���`flabel2���aoa.���`kget_visible���`a(���`a)���`a ���bowcand���`a ���`kneeds_upper���`a)���`a
���`l            ���bnbesuper���`a(���`a)���aoa.���`ddraw���`a(���`hrenderer���`a)���`a
���`a
���`d    ���akcdef���`a ���bnfqget_view_interval���`a(���bbpdself���`a)���`a:���`a
���`h        ���akfreturn���`a ���bbpdself���aoa.���`daxes���aoa.���`exaxis���aoa.���`qget_view_interval���`a(���`a)���`a
���`a
���`a
���bc1xJ# This class exists to provide two separate sets of intervals to the tick,���`a
���bc1x0# as well as create instances of the custom tick���`a
���akeclass���`a ���bnciSkewXAxis���`a(���`emaxis���aoa.���`eXAxis���`a)���`a:���`a
���`d    ���akcdef���`a ���bnfi_get_tick���`a(���bbpdself���`a,���`a ���`emajor���`a)���`a:���`a
���`h        ���akfreturn���`a ���`iSkewXTick���`a(���bbpdself���aoa.���`daxes���`a,���`a ���bkcdNone���`a,���`a ���`emajor���aoa=���`emajor���`a)���`a
���`a
���`d    ���akcdef���`a ���bnfqget_view_interval���`a(���bbpdself���`a)���`a:���`a
���`h        ���akfreturn���`a ���bbpdself���aoa.���`daxes���aoa.���`jupper_xlim���`a[���bmia0���`a]���`a,���`a ���bbpdself���aoa.���`daxes���aoa.���`jlower_xlim���`a[���bmia1���`a]���`a
���`a
���`a
���bc1x?# This class exists to calculate the separate data range of the���`a
���bc1xD# upper X-axis and draw the spine there. It also provides this range���`a
���bc1x0# to the X-axis artist for ticking and gridlines���`a
���akeclass���`a ���bnciSkewSpine���`a(���`gmspines���aoa.���`eSpine���`a)���`a:���`a
���`d    ���akcdef���`a ���bnfp_adjust_location���`a(���bbpdself���`a)���`a:���`a
���`h        ���`cpts���`a ���aoa=���`a ���bbpdself���aoa.���`e_path���aoa.���`hvertices���`a
���`h        ���akbif���`a ���bbpdself���aoa.���`jspine_type���`a ���aob==���`a ���bs1a'���bs1ctop���bs1a'���`a:���`a
���`l            ���`cpts���`a[���`a:���`a,���`a ���bmia0���`a]���`a ���aoa=���`a ���bbpdself���aoa.���`daxes���aoa.���`jupper_xlim���`a
���`h        ���akdelse���`a:���`a
���`l            ���`cpts���`a[���`a:���`a,���`a ���bmia0���`a]���`a ���aoa=���`a ���bbpdself���aoa.���`daxes���aoa.���`jlower_xlim���`a
���`a
���`a
���bc1xK# This class handles registration of the skew-xaxes as a projection as well���`a
���bc1xK# as setting up the appropriate transformations. It also overrides standard���`a
���bc1x+# spines and axes instances as appropriate.���`a
���akeclass���`a ���bnciSkewXAxes���`a(���`dAxes���`a)���`a:���`a
���`d    ���bc1x?# The projection must specify a name.  This will be used be the���`a
���`d    ���bc1xF# user to select the projection, i.e. ``subplot(projection='skewx')``.���`a
���`d    ���`dname���`a ���aoa=���`a ���bs1a'���bs1eskewx���bs1a'���`a
���`a
���`d    ���akcdef���`a ���bnfj_init_axis���`a(���bbpdself���`a)���`a:���`a
���`h        ���bc1x9# Taken from Axes and modified to use our modified X-axis���`a
���`h        ���bbpdself���aoa.���`exaxis���`a ���aoa=���`a ���`iSkewXAxis���`a(���bbpdself���`a)���`a
���`h        ���bbpdself���aoa.���`fspines���aoa.���`ctop���aoa.���`mregister_axis���`a(���bbpdself���aoa.���`exaxis���`a)���`a
���`h        ���bbpdself���aoa.���`fspines���aoa.���`fbottom���aoa.���`mregister_axis���`a(���bbpdself���aoa.���`exaxis���`a)���`a
���`h        ���bbpdself���aoa.���`eyaxis���`a ���aoa=���`a ���`emaxis���aoa.���`eYAxis���`a(���bbpdself���`a)���`a
���`h        ���bbpdself���aoa.���`fspines���aoa.���`dleft���aoa.���`mregister_axis���`a(���bbpdself���aoa.���`eyaxis���`a)���`a
���`h        ���bbpdself���aoa.���`fspines���aoa.���`eright���aoa.���`mregister_axis���`a(���bbpdself���aoa.���`eyaxis���`a)���`a
���`a
���`d    ���akcdef���`a ���bnfp_gen_axes_spines���`a(���bbpdself���`a)���`a:���`a
���`h        ���`fspines���`a ���aoa=���`a ���`a{���bs1a'���bs1ctop���bs1a'���`a:���`a ���`iSkewSpine���aoa.���`llinear_spine���`a(���bbpdself���`a,���`a ���bs1a'���bs1ctop���bs1a'���`a)���`a,���`a
���`r                  ���bs1a'���bs1fbottom���bs1a'���`a:���`a ���`gmspines���aoa.���`eSpine���aoa.���`llinear_spine���`a(���bbpdself���`a,���`a ���bs1a'���bs1fbottom���bs1a'���`a)���`a,���`a
���`r                  ���bs1a'���bs1dleft���bs1a'���`a:���`a ���`gmspines���aoa.���`eSpine���aoa.���`llinear_spine���`a(���bbpdself���`a,���`a ���bs1a'���bs1dleft���bs1a'���`a)���`a,���`a
���`r                  ���bs1a'���bs1eright���bs1a'���`a:���`a ���`gmspines���aoa.���`eSpine���aoa.���`llinear_spine���`a(���bbpdself���`a,���`a ���bs1a'���bs1eright���bs1a'���`a)���`a}���`a
���`h        ���akfreturn���`a ���`fspines���`a
���`a
���`d    ���akcdef���`a ���bnfw_set_lim_and_transforms���`a(���bbpdself���`a)���`a:���`a
���`h        ���bsdx�"""
        This is called once when the plot is created to set up all the
        transforms for the data, text and grids.
        """���`a
���`h        ���`crot���`a ���aoa=���`a ���bmib30���`a
���`a
���`h        ���bc1x;# Get the standard transform setup from the Axes base class���`a
���`h        ���bnbesuper���`a(���`a)���aoa.���`w_set_lim_and_transforms���`a(���`a)���`a
���`a
���`h        ���bc1xA# Need to put the skew in the middle, after the scale and limits,���`a
���`h        ���bc1x># but before the transAxes. This way, the skew is done in Axes���`a
���`h        ���bc1xD# coordinates thus performing the transform around the proper origin���`a
���`h        ���bc1xF# We keep the pre-transAxes transform around for other users, like the���`a
���`h        ���bc1x# spines for finding bounds���`a
���`h        ���bbpdself���aoa.���`otransDataToAxes���`a ���aoa=���`a ���`a(���`a
���`l            ���bbpdself���aoa.���`jtransScale���`a
���`l            ���aoa+���`a ���bbpdself���aoa.���`ktransLimits���`a
���`l            ���aoa+���`a ���`jtransforms���aoa.���`hAffine2D���`a(���`a)���aoa.���`hskew_deg���`a(���`crot���`a,���`a ���bmia0���`a)���`a
���`h        ���`a)���`a
���`h        ���bc1x/# Create the full transform from Data to Pixels���`a
���`h        ���bbpdself���aoa.���`itransData���`a ���aoa=���`a ���bbpdself���aoa.���`otransDataToAxes���`a ���aoa+���`a ���bbpdself���aoa.���`itransAxes���`a
���`a
���`h        ���bc1xE# Blended transforms like this need to have the skewing applied using���`a
���`h        ���bc1x(# both axes, in axes coords like before.���`a
���`h        ���bbpdself���aoa.���`p_xaxis_transform���`a ���aoa=���`a ���`a(���`a
���`l            ���`jtransforms���aoa.���`xblended_transform_factory���`a(���`a
���`p                ���bbpdself���aoa.���`jtransScale���`a ���aoa+���`a ���bbpdself���aoa.���`ktransLimits���`a,���`a
���`p                ���`jtransforms���aoa.���`qIdentityTransform���`a(���`a)���`a)���`a
���`l            ���aoa+���`a ���`jtransforms���aoa.���`hAffine2D���`a(���`a)���aoa.���`hskew_deg���`a(���`crot���`a,���`a ���bmia0���`a)���`a
���`l            ���aoa+���`a ���bbpdself���aoa.���`itransAxes���`a
���`h        ���`a)���`a
���`a
���`d    ���bndi@property���`a
���`d    ���akcdef���`a ���bnfjlower_xlim���`a(���bbpdself���`a)���`a:���`a
���`h        ���akfreturn���`a ���bbpdself���aoa.���`daxes���aoa.���`gviewLim���aoa.���`iintervalx���`a
���`a
���`d    ���bndi@property���`a
���`d    ���akcdef���`a ���bnfjupper_xlim���`a(���bbpdself���`a)���`a:���`a
���`h        ���`cpts���`a ���aoa=���`a ���`a[���`a[���bmfb0.���`a,���`a ���bmfb1.���`a]���`a,���`a ���`a[���bmfb1.���`a,���`a ���bmfb1.���`a]���`a]���`a
���`h        ���akfreturn���`a ���bbpdself���aoa.���`otransDataToAxes���aoa.���`hinverted���`a(���`a)���aoa.���`itransform���`a(���`cpts���`a)���`a[���`a:���`a,���`a ���bmia0���`a]���`a
���`a
���`a
���bc1xH# Now register the projection with matplotlib so the user can select it.���`a
���`sregister_projection���`a(���`iSkewXAxes���`a)���`a
���`a
���akbif���`a ���bvmh__name__���`a ���aob==���`a ���bs1a'���bs1h__main__���bs1a'���`a:���`a
���`d    ���bc1x8# Now make a simple example using the custom projection.���`a
���`d    ���bkndfrom���`a ���bnnbio���`a ���bknfimport���`a ���`hStringIO���`a
���`d    ���bkndfrom���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfticker���`a ���bknfimport���`a ���`a(���`oMultipleLocator���`a,���`a ���`mNullFormatter���`a,���`a
���`x#                                   ���`oScalarFormatter���`a)���`a
���`d    ���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���`d    ���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���`a
���`d    ���bc1t# Some example data.���`a
���`d    ���`hdata_txt���`a ���aoa=���`a ���bs1c'''���bs1a
���bs1x"        978.0    345    7.8    0.8���bs1a
���bs1x"        971.0    404    7.2    0.2���bs1a
���bs1x"        946.7    610    5.2   -1.8���bs1a
���bs1x"        944.0    634    5.0   -2.0���bs1a
���bs1x"        925.0    798    3.4   -2.6���bs1a
���bs1x"        911.8    914    2.4   -2.7���bs1a
���bs1x"        906.0    966    2.0   -2.7���bs1a
���bs1x"        877.9   1219    0.4   -3.2���bs1a
���bs1x"        850.0   1478   -1.3   -3.7���bs1a
���bs1x"        841.0   1563   -1.9   -3.8���bs1a
���bs1x"        823.0   1736    1.4   -0.7���bs1a
���bs1x"        813.6   1829    4.5    1.2���bs1a
���bs1x"        809.0   1875    6.0    2.2���bs1a
���bs1x"        798.0   1988    7.4   -0.6���bs1a
���bs1x"        791.0   2061    7.6   -1.4���bs1a
���bs1x"        783.9   2134    7.0   -1.7���bs1a
���bs1x"        755.1   2438    4.8   -3.1���bs1a
���bs1x"        727.3   2743    2.5   -4.4���bs1a
���bs1x"        700.5   3048    0.2   -5.8���bs1a
���bs1x"        700.0   3054    0.2   -5.8���bs1a
���bs1x"        698.0   3077    0.0   -6.0���bs1a
���bs1x"        687.0   3204   -0.1   -7.1���bs1a
���bs1x"        648.9   3658   -3.2  -10.9���bs1a
���bs1x"        631.0   3881   -4.7  -12.7���bs1a
���bs1x"        600.7   4267   -6.4  -16.7���bs1a
���bs1x"        592.0   4381   -6.9  -17.9���bs1a
���bs1x"        577.6   4572   -8.1  -19.6���bs1a
���bs1x"        555.3   4877  -10.0  -22.3���bs1a
���bs1x"        536.0   5151  -11.7  -24.7���bs1a
���bs1x"        533.8   5182  -11.9  -25.0���bs1a
���bs1x"        500.0   5680  -15.9  -29.9���bs1a
���bs1x"        472.3   6096  -19.7  -33.4���bs1a
���bs1x"        453.0   6401  -22.4  -36.0���bs1a
���bs1x"        400.0   7310  -30.7  -43.7���bs1a
���bs1x"        399.7   7315  -30.8  -43.8���bs1a
���bs1x"        387.0   7543  -33.1  -46.1���bs1a
���bs1x"        382.7   7620  -33.8  -46.8���bs1a
���bs1x"        342.0   8398  -40.5  -53.5���bs1a
���bs1x"        320.4   8839  -43.7  -56.7���bs1a
���bs1x"        318.0   8890  -44.1  -57.1���bs1a
���bs1x"        310.0   9060  -44.7  -58.7���bs1a
���bs1x"        306.1   9144  -43.9  -57.9���bs1a
���bs1x"        305.0   9169  -43.7  -57.7���bs1a
���bs1x"        300.0   9280  -43.5  -57.5���bs1a
���bs1x"        292.0   9462  -43.7  -58.7���bs1a
���bs1x"        276.0   9838  -47.1  -62.1���bs1a
���bs1x"        264.0  10132  -47.5  -62.5���bs1a
���bs1x"        251.0  10464  -49.7  -64.7���bs1a
���bs1x"        250.0  10490  -49.7  -64.7���bs1a
���bs1x"        247.0  10569  -48.7  -63.7���bs1a
���bs1x"        244.0  10649  -48.9  -63.9���bs1a
���bs1x"        243.3  10668  -48.9  -63.9���bs1a
���bs1x"        220.0  11327  -50.3  -65.3���bs1a
���bs1x"        212.0  11569  -50.5  -65.5���bs1a
���bs1x"        210.0  11631  -49.7  -64.7���bs1a
���bs1x"        200.0  11950  -49.9  -64.9���bs1a
���bs1x"        194.0  12149  -49.9  -64.9���bs1a
���bs1x"        183.0  12529  -51.3  -66.3���bs1a
���bs1x"        164.0  13233  -55.3  -68.3���bs1a
���bs1x"        152.0  13716  -56.5  -69.5���bs1a
���bs1x"        150.0  13800  -57.1  -70.1���bs1a
���bs1x"        136.0  14414  -60.5  -72.5���bs1a
���bs1x"        132.0  14600  -60.1  -72.1���bs1a
���bs1x"        131.4  14630  -60.2  -72.2���bs1a
���bs1x"        128.0  14792  -60.9  -72.9���bs1a
���bs1x"        125.0  14939  -60.1  -72.1���bs1a
���bs1x"        119.0  15240  -62.2  -73.8���bs1a
���bs1x"        112.0  15616  -64.9  -75.9���bs1a
���bs1x"        108.0  15838  -64.1  -75.1���bs1a
���bs1x"        107.8  15850  -64.1  -75.1���bs1a
���bs1x"        105.0  16010  -64.7  -75.7���bs1a
���bs1x"        103.0  16128  -62.9  -73.9���bs1a
���bs1x"        100.0  16310  -62.5  -73.5���bs1a
���bs1d    ���bs1c'''���`a
���`a
���`d    ���bc1p# Parse the data���`a
���`d    ���`jsound_data���`a ���aoa=���`a ���`hStringIO���`a(���`hdata_txt���`a)���`a
���`d    ���`ap���`a,���`a ���`ah���`a,���`a ���`aT���`a,���`a ���`bTd���`a ���aoa=���`a ���`bnp���aoa.���`gloadtxt���`a(���`jsound_data���`a,���`a ���`funpack���aoa=���bkcdTrue���`a)���`a
���`a
���`d    ���bc1xC# Create a new figure. The dimensions here give a good aspect ratio���`a
���`d    ���`cfig���`a ���aoa=���`a ���`cplt���aoa.���`ffigure���`a(���`gfigsize���aoa=���`a(���bmff6.5875���`a,���`a ���bmff6.2125���`a)���`a)���`a
���`d    ���`bax���`a ���aoa=���`a ���`cfig���aoa.���`kadd_subplot���`a(���`jprojection���aoa=���bs1a'���bs1eskewx���bs1a'���`a)���`a
���`a
���`d    ���`cplt���aoa.���`dgrid���`a(���bkcdTrue���`a)���`a
���`a
���`d    ���bc1xC# Plot the data using normal plotting functions, in this case using���`a
���`d    ���bc1xB# log scaling in Y, as dictated by the typical meteorological plot���`a
���`d    ���`bax���aoa.���`hsemilogy���`a(���`aT���`a,���`a ���`ap���`a,���`a ���`ecolor���aoa=���bs1a'���bs1bC3���bs1a'���`a)���`a
���`d    ���`bax���aoa.���`hsemilogy���`a(���`bTd���`a,���`a ���`ap���`a,���`a ���`ecolor���aoa=���bs1a'���bs1bC2���bs1a'���`a)���`a
���`a
���`d    ���bc1x,# An example of a slanted line at constant X���`a
���`d    ���`al���`a ���aoa=���`a ���`bax���aoa.���`gaxvline���`a(���bmia0���`a,���`a ���`ecolor���aoa=���bs1a'���bs1bC0���bs1a'���`a)���`a
���`a
���`d    ���bc1x6# Disables the log-formatting that comes with semilogy���`a
���`d    ���`bax���aoa.���`eyaxis���aoa.���`sset_major_formatter���`a(���`oScalarFormatter���`a(���`a)���`a)���`a
���`d    ���`bax���aoa.���`eyaxis���aoa.���`sset_minor_formatter���`a(���`mNullFormatter���`a(���`a)���`a)���`a
���`d    ���`bax���aoa.���`jset_yticks���`a(���`bnp���aoa.���`hlinspace���`a(���bmic100���`a,���`a ���bmid1000���`a,���`a ���bmib10���`a)���`a)���`a
���`d    ���`bax���aoa.���`hset_ylim���`a(���bmid1050���`a,���`a ���bmic100���`a)���`a
���`a
���`d    ���`bax���aoa.���`exaxis���aoa.���`qset_major_locator���`a(���`oMultipleLocator���`a(���bmib10���`a)���`a)���`a
���`d    ���`bax���aoa.���`hset_xlim���`a(���aoa-���bmib50���`a,���`a ���bmib50���`a)���`a
���`a
���`d    ���`cplt���aoa.���`dshow���`a(���`a)���`a
���`a
���`a
���bc1xM#############################################################################���`a
���bc1a#���`a
���bc1x# .. admonition:: References���`a
���bc1a#���`a
���bc1xN#    The use of the following functions, methods, classes and modules is shown���`a
���bc1u#    in this example:���`a
���bc1a#���`a
���bc1x#    - `matplotlib.transforms`���`a
���bc1x#    - `matplotlib.spines`���`a
���bc1x #    - `matplotlib.spines.Spine`���`a
���bc1x.#    - `matplotlib.spines.Spine.register_axis`���`a
���bc1x#    - `matplotlib.projections`���`a
���bc1x3#    - `matplotlib.projections.register_projection`���`a
`dNone�