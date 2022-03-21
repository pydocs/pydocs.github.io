��������{���bsdy"""
=========================================================
Line, Poly and RegularPoly Collection with autoscaling
=========================================================

For the first two subplots, we will use spirals.  Their size will be set in
plot units, not data units.  Their positions will be set in data units by using
the *offsets* and *transOffset* keyword arguments of the `.LineCollection` and
`.PolyCollection`.

The third subplot will make regular polygons, with the same
type of scaling and positioning as in the first two.

The last subplot illustrates the use of "offsets=(xo, yo)",
that is, a single tuple instead of a list of tuples, to generate
successively offset curves, with the offset given in data
units.  This behavior is available only for the LineCollection.
"""���`a
���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���bkndfrom���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����`a ���bknfimport���`a ���`kcollections���`a,���`a ���`fcolors���`a,���`a ���`jtransforms���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���`a
���`fnverts���`a ���aoa=���`a ���bmib50���`a
���`dnpts���`a ���aoa=���`a ���bmic100���`a
���`a
���bc1s# Make some spirals���`a
���`ar���`a ���aoa=���`a ���`bnp���aoa.���`farange���`a(���`fnverts���`a)���`a
���`etheta���`a ���aoa=���`a ���`bnp���aoa.���`hlinspace���`a(���bmia0���`a,���`a ���bmia2���aoa*���`bnp���aoa.���`bpi���`a,���`a ���`fnverts���`a)���`a
���`bxx���`a ���aoa=���`a ���`ar���`a ���aoa*���`a ���`bnp���aoa.���`csin���`a(���`etheta���`a)���`a
���`byy���`a ���aoa=���`a ���`ar���`a ���aoa*���`a ���`bnp���aoa.���`ccos���`a(���`etheta���`a)���`a
���`fspiral���`a ���aoa=���`a ���`bnp���aoa.���`lcolumn_stack���`a(���`a[���`bxx���`a,���`a ���`byy���`a]���`a)���`a
���`a
���bc1x)# Fixing random state for reproducibility���`a
���`brs���`a ���aoa=���`a ���`bnp���aoa.���`frandom���aoa.���`kRandomState���`a(���bmih19680801���`a)���`a
���`a
���bc1s# Make some offsets���`a
���`cxyo���`a ���aoa=���`a ���`brs���aoa.���`erandn���`a(���`dnpts���`a,���`a ���bmia2���`a)���`a
���`a
���bc1x;# Make a list of colors cycling through the default series.���`a
���`fcolors���`a ���aoa=���`a ���`a[���`fcolors���aoa.���`gto_rgba���`a(���`ac���`a)���`a
���`j          ���akcfor���`a ���`ac���`a ���bowbin���`a ���`cplt���aoa.���`hrcParams���`a[���bs1a'���bs1oaxes.prop_cycle���bs1a'���`a]���aoa.���`fby_key���`a(���`a)���`a[���bs1a'���bs1ecolor���bs1a'���`a]���`a]���`a
���`a
���`cfig���`a,���`a ���`a(���`a(���`cax1���`a,���`a ���`cax2���`a)���`a,���`a ���`a(���`cax3���`a,���`a ���`cax4���`a)���`a)���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���bmia2���`a,���`a ���bmia2���`a)���`a
���`cfig���aoa.���`osubplots_adjust���`a(���`ctop���aoa=���bmfd0.92���`a,���`a ���`dleft���aoa=���bmfd0.07���`a,���`a ���`eright���aoa=���bmfd0.97���`a,���`a
���`t                    ���`fhspace���aoa=���bmfc0.3���`a,���`a ���`fwspace���aoa=���bmfc0.3���`a)���`a
���`a
���`a
���`ccol���`a ���aoa=���`a ���`kcollections���aoa.���`nLineCollection���`a(���`a[���`fspiral���`a]���`a,���`a ���`goffsets���aoa=���`cxyo���`a,���`a
���`x!                                 ���`ktransOffset���aoa=���`cax1���aoa.���`itransData���`a)���`a
���`etrans���`a ���aoa=���`a ���`cfig���aoa.���`odpi_scale_trans���`a ���aoa+���`a ���`jtransforms���aoa.���`hAffine2D���`a(���`a)���aoa.���`escale���`a(���bmfc1.0���aoa/���bmfd72.0���`a)���`a
���`ccol���aoa.���`mset_transform���`a(���`etrans���`a)���`b  ���bc1x # the points to pixels transform���`a
���bc1x8# Note: the first argument to the collection initializer���`a
���bc1x<# must be a list of sequences of (x, y) tuples; we have only���`a
���bc1x6# one sequence, but we still have to put it in a list.���`a
���`cax1���aoa.���`nadd_collection���`a(���`ccol���`a,���`a ���`gautolim���aoa=���bkcdTrue���`a)���`a
���bc1x9# autolim=True enables autoscaling.  For collections with���`a
���bc1x:# offsets like this, it is neither efficient nor accurate,���`a
���bc1x;# but it is good enough to generate a plot that you can use���`a
���bc1x;# as a starting point.  If you know beforehand the range of���`a
���bc1x9# x and y that you want to show, it is better to set them���`a
���bc1xL# explicitly, leave out the *autolim* keyword argument (or set it to False),���`a
���bc1x1# and omit the 'ax1.autoscale_view()' call below.���`a
���`a
���bc1x@# Make a transform for the line segments such that their size is���`a
���bc1r# given in points:���`a
���`ccol���aoa.���`iset_color���`a(���`fcolors���`a)���`a
���`a
���`cax1���aoa.���`nautoscale_view���`a(���`a)���`b  ���bc1x.# See comment above, after ax1.add_collection.���`a
���`cax1���aoa.���`iset_title���`a(���bs1a'���bs1xLineCollection using offsets���bs1a'���`a)���`a
���`a
���`a
���bc1x.# The same data as above, but fill the curves.���`a
���`ccol���`a ���aoa=���`a ���`kcollections���aoa.���`nPolyCollection���`a(���`a[���`fspiral���`a]���`a,���`a ���`goffsets���aoa=���`cxyo���`a,���`a
���`x!                                 ���`ktransOffset���aoa=���`cax2���aoa.���`itransData���`a)���`a
���`etrans���`a ���aoa=���`a ���`jtransforms���aoa.���`hAffine2D���`a(���`a)���aoa.���`escale���`a(���`cfig���aoa.���`cdpi���aoa/���bmfd72.0���`a)���`a
���`ccol���aoa.���`mset_transform���`a(���`etrans���`a)���`b  ���bc1x # the points to pixels transform���`a
���`cax2���aoa.���`nadd_collection���`a(���`ccol���`a,���`a ���`gautolim���aoa=���bkcdTrue���`a)���`a
���`ccol���aoa.���`iset_color���`a(���`fcolors���`a)���`a
���`a
���`a
���`cax2���aoa.���`nautoscale_view���`a(���`a)���`a
���`cax2���aoa.���`iset_title���`a(���bs1a'���bs1xPolyCollection using offsets���bs1a'���`a)���`a
���`a
���bc1x# 7-sided regular polygons���`a
���`a
���`ccol���`a ���aoa=���`a ���`kcollections���aoa.���`uRegularPolyCollection���`a(���`a
���`d    ���bmia7���`a,���`a ���`esizes���aoa=���`bnp���aoa.���`cabs���`a(���`bxx���`a)���`a ���aoa*���`a ���bmfd10.0���`a,���`a ���`goffsets���aoa=���`cxyo���`a,���`a ���`ktransOffset���aoa=���`cax3���aoa.���`itransData���`a)���`a
���`etrans���`a ���aoa=���`a ���`jtransforms���aoa.���`hAffine2D���`a(���`a)���aoa.���`escale���`a(���`cfig���aoa.���`cdpi���`a ���aoa/���`a ���bmfd72.0���`a)���`a
���`ccol���aoa.���`mset_transform���`a(���`etrans���`a)���`b  ���bc1x # the points to pixels transform���`a
���`cax3���aoa.���`nadd_collection���`a(���`ccol���`a,���`a ���`gautolim���aoa=���bkcdTrue���`a)���`a
���`ccol���aoa.���`iset_color���`a(���`fcolors���`a)���`a
���`cax3���aoa.���`nautoscale_view���`a(���`a)���`a
���`cax3���aoa.���`iset_title���`a(���bs1a'���bs1x#RegularPolyCollection using offsets���bs1a'���`a)���`a
���`a
���`a
���bc1x;# Simulate a series of ocean current profiles, successively���`a
���bc1x># offset by 0.1 m/s so that they form what is sometimes called���`a
���bc1x)# a "waterfall" plot or a "stagger" plot.���`a
���`a
���`fnverts���`a ���aoa=���`a ���bmib60���`a
���`gncurves���`a ���aoa=���`a ���bmib20���`a
���`doffs���`a ���aoa=���`a ���`a(���bmfc0.1���`a,���`a ���bmfc0.0���`a)���`a
���`a
���`byy���`a ���aoa=���`a ���`bnp���aoa.���`hlinspace���`a(���bmia0���`a,���`a ���bmia2���aoa*���`bnp���aoa.���`bpi���`a,���`a ���`fnverts���`a)���`a
���`bym���`a ���aoa=���`a ���`bnp���aoa.���`cmax���`a(���`byy���`a)���`a
���`bxx���`a ���aoa=���`a ���`a(���bmfc0.2���`a ���aoa+���`a ���`a(���`bym���`a ���aoa-���`a ���`byy���`a)���`a ���aoa/���`a ���`bym���`a)���`a ���aoa*���aoa*���`a ���bmia2���`a ���aoa*���`a ���`bnp���aoa.���`ccos���`a(���`byy���`a ���aoa-���`a ���bmfc0.4���`a)���`a ���aoa*���`a ���bmfc0.5���`a
���`dsegs���`a ���aoa=���`a ���`a[���`a]���`a
���akcfor���`a ���`ai���`a ���bowbin���`a ���bnberange���`a(���`gncurves���`a)���`a:���`a
���`d    ���`cxxx���`a ���aoa=���`a ���`bxx���`a ���aoa+���`a ���bmfd0.02���aoa*���`brs���aoa.���`erandn���`a(���`fnverts���`a)���`a
���`d    ���`ecurve���`a ���aoa=���`a ���`bnp���aoa.���`lcolumn_stack���`a(���`a[���`cxxx���`a,���`a ���`byy���`a ���aoa*���`a ���bmic100���`a]���`a)���`a
���`d    ���`dsegs���aoa.���`fappend���`a(���`ecurve���`a)���`a
���`a
���`ccol���`a ���aoa=���`a ���`kcollections���aoa.���`nLineCollection���`a(���`dsegs���`a,���`a ���`goffsets���aoa=���`doffs���`a)���`a
���`cax4���aoa.���`nadd_collection���`a(���`ccol���`a,���`a ���`gautolim���aoa=���bkcdTrue���`a)���`a
���`ccol���aoa.���`iset_color���`a(���`fcolors���`a)���`a
���`cax4���aoa.���`nautoscale_view���`a(���`a)���`a
���`cax4���aoa.���`iset_title���`a(���bs1a'���bs1wSuccessive data offsets���bs1a'���`a)���`a
���`cax4���aoa.���`jset_xlabel���`a(���bs1a'���bs1xZonal velocity component (m/s)���bs1a'���`a)���`a
���`cax4���aoa.���`jset_ylabel���`a(���bs1a'���bs1iDepth (m)���bs1a'���`a)���`a
���bc1x0# Reverse the y-axis so depth increases downward���`a
���`cax4���aoa.���`hset_ylim���`a(���`cax4���aoa.���`hget_ylim���`a(���`a)���`a[���`a:���`a:���aoa-���bmia1���`a]���`a)���`a
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
���bc1x!#    - `matplotlib.figure.Figure`���`a
���bc1x#    - `matplotlib.collections`���`a
���bc1x.#    - `matplotlib.collections.LineCollection`���`a
���bc1x5#    - `matplotlib.collections.RegularPolyCollection`���`a
���bc1x,#    - `matplotlib.axes.Axes.add_collection`���`a
���bc1x,#    - `matplotlib.axes.Axes.autoscale_view`���`a
���bc1x'#    - `matplotlib.transforms.Affine2D`���`a
���bc1x-#    - `matplotlib.transforms.Affine2D.scale`���`a
`dNone�