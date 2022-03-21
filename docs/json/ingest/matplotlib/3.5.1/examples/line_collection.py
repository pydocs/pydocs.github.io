��������Y���bsdx�"""
===============
Line Collection
===============

Plotting lines with Matplotlib.

`~matplotlib.collections.LineCollection` allows one to plot multiple
lines on a figure. Below we show off some of its properties.
"""���`a
���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���bkndfrom���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnkcollections���`a ���bknfimport���`a ���`nLineCollection���`a
���bkndfrom���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����`a ���bknfimport���`a ���`fcolors���`a ���akbas���`a ���`gmcolors���`a
���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���`a
���bc1xB# In order to efficiently plot many lines in a single set of axes,���`a
���bc1xD# Matplotlib has the ability to add the lines all at once. Here is a���`a
���bc1x(# simple example showing how it is done.���`a
���`a
���`ax���`a ���aoa=���`a ���`bnp���aoa.���`farange���`a(���bmic100���`a)���`a
���bc1x'# Here are many sets of y to plot vs. x���`a
���`bys���`a ���aoa=���`a ���`ax���`a[���`a:���bmib50���`a,���`a ���`bnp���aoa.���`gnewaxis���`a]���`a ���aoa+���`a ���`ax���`a[���`bnp���aoa.���`gnewaxis���`a,���`a ���`a:���`a]���`a
���`a
���`dsegs���`a ���aoa=���`a ���`bnp���aoa.���`ezeros���`a(���`a(���bmib50���`a,���`a ���bmic100���`a,���`a ���bmia2���`a)���`a)���`a
���`dsegs���`a[���`a:���`a,���`a ���`a:���`a,���`a ���bmia1���`a]���`a ���aoa=���`a ���`bys���`a
���`dsegs���`a[���`a:���`a,���`a ���`a:���`a,���`a ���bmia0���`a]���`a ���aoa=���`a ���`ax���`a
���`a
���bc1x0# Mask some values to test masked array support:���`a
���`dsegs���`a ���aoa=���`a ���`bnp���aoa.���`bma���aoa.���`lmasked_where���`a(���`a(���`dsegs���`a ���aoa>���`a ���bmib50���`a)���`a ���aoa&���`a ���`a(���`dsegs���`a ���aoa<���`a ���bmib60���`a)���`a,���`a ���`dsegs���`a)���`a
���`a
���bc1x!# We need to set the plot limits.���`a
���`cfig���`a,���`a ���`bax���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`a)���`a
���`bax���aoa.���`hset_xlim���`a(���`ax���aoa.���`cmin���`a(���`a)���`a,���`a ���`ax���aoa.���`cmax���`a(���`a)���`a)���`a
���`bax���aoa.���`hset_ylim���`a(���`bys���aoa.���`cmin���`a(���`a)���`a,���`a ���`bys���aoa.���`cmax���`a(���`a)���`a)���`a
���`a
���bc1x&# *colors* is sequence of rgba tuples.���`a
���bc1x@# *linestyle* is a string or dash tuple. Legal string values are���`a
���bc1xJ# solid|dashed|dashdot|dotted.  The dash tuple is (offset, onoffseq) where���`a
���bc1xM# onoffseq is an even length tuple of on and off ink in points.  If linestyle���`a
���bc1x# is omitted, 'solid' is used.���`a
���bc1xC# See `matplotlib.collections.LineCollection` for more information.���`a
���`fcolors���`a ���aoa=���`a ���`a[���`gmcolors���aoa.���`gto_rgba���`a(���`ac���`a)���`a
���`j          ���akcfor���`a ���`ac���`a ���bowbin���`a ���`cplt���aoa.���`hrcParams���`a[���bs1a'���bs1oaxes.prop_cycle���bs1a'���`a]���aoa.���`fby_key���`a(���`a)���`a[���bs1a'���bs1ecolor���bs1a'���`a]���`a]���`a
���`a
���`mline_segments���`a ���aoa=���`a ���`nLineCollection���`a(���`dsegs���`a,���`a ���`jlinewidths���aoa=���`a(���bmfc0.5���`a,���`a ���bmia1���`a,���`a ���bmfc1.5���`a,���`a ���bmia2���`a)���`a,���`a
���`x                               ���`fcolors���aoa=���`fcolors���`a,���`a ���`ilinestyle���aoa=���bs1a'���bs1esolid���bs1a'���`a)���`a
���`bax���aoa.���`nadd_collection���`a(���`mline_segments���`a)���`a
���`bax���aoa.���`iset_title���`a(���bs1a'���bs1x"Line collection with masked arrays���bs1a'���`a)���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
���`a
���bc1xO###############################################################################���`a
���bc1xB# In order to efficiently plot many lines in a single set of axes,���`a
���bc1xD# Matplotlib has the ability to add the lines all at once. Here is a���`a
���bc1x(# simple example showing how it is done.���`a
���`a
���`aN���`a ���aoa=���`a ���bmib50���`a
���`ax���`a ���aoa=���`a ���`bnp���aoa.���`farange���`a(���`aN���`a)���`a
���bc1x'# Here are many sets of y to plot vs. x���`a
���`bys���`a ���aoa=���`a ���`a[���`ax���`a ���aoa+���`a ���`ai���`a ���akcfor���`a ���`ai���`a ���bowbin���`a ���`ax���`a]���`a
���`a
���bc1x9# We need to set the plot limits, they will not autoscale���`a
���`cfig���`a,���`a ���`bax���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`a)���`a
���`bax���aoa.���`hset_xlim���`a(���`bnp���aoa.���`cmin���`a(���`ax���`a)���`a,���`a ���`bnp���aoa.���`cmax���`a(���`ax���`a)���`a)���`a
���`bax���aoa.���`hset_ylim���`a(���`bnp���aoa.���`cmin���`a(���`bys���`a)���`a,���`a ���`bnp���aoa.���`cmax���`a(���`bys���`a)���`a)���`a
���`a
���bc1x## colors is sequence of rgba tuples���`a
���bc1x># linestyle is a string or dash tuple. Legal string values are���`a
���bc1xM#          solid|dashed|dashdot|dotted.  The dash tuple is (offset, onoffseq)���`a
���bc1xN#          where onoffseq is an even length tuple of on and off ink in points.���`a
���bc1x3#          If linestyle is omitted, 'solid' is used���`a
���bc1xB# See `matplotlib.collections.LineCollection` for more information���`a
���`a
���bc1x"# Make a sequence of (x, y) pairs.���`a
���`mline_segments���`a ���aoa=���`a ���`nLineCollection���`a(���`a[���`bnp���aoa.���`lcolumn_stack���`a(���`a[���`ax���`a,���`a ���`ay���`a]���`a)���`a ���akcfor���`a ���`ay���`a ���bowbin���`a ���`bys���`a]���`a,���`a
���`x                               ���`jlinewidths���aoa=���`a(���bmfc0.5���`a,���`a ���bmia1���`a,���`a ���bmfc1.5���`a,���`a ���bmia2���`a)���`a,���`a
���`x                               ���`jlinestyles���aoa=���bs1a'���bs1esolid���bs1a'���`a)���`a
���`mline_segments���aoa.���`iset_array���`a(���`ax���`a)���`a
���`bax���aoa.���`nadd_collection���`a(���`mline_segments���`a)���`a
���`daxcb���`a ���aoa=���`a ���`cfig���aoa.���`hcolorbar���`a(���`mline_segments���`a)���`a
���`daxcb���aoa.���`iset_label���`a(���bs1a'���bs1kLine Number���bs1a'���`a)���`a
���`bax���aoa.���`iset_title���`a(���bs1a'���bs1x"Line Collection with mapped colors���bs1a'���`a)���`a
���`cplt���aoa.���`csci���`a(���`mline_segments���`a)���`b  ���bc1x3# This allows interactive changing of the colormap.���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
���`a
���bc1xM#############################################################################���`a
���bc1a#���`a
���bc1x# .. admonition:: References���`a
���bc1a#���`a
���bc1xN#    The use of the following functions, methods, classes and modules is shown���`a
���bc1u#    in this example:���`a
���bc1a#���`a
���bc1x#    - `matplotlib.collections`���`a
���bc1x.#    - `matplotlib.collections.LineCollection`���`a
���bc1x/#    - `matplotlib.cm.ScalarMappable.set_array`���`a
���bc1x,#    - `matplotlib.axes.Axes.add_collection`���`a
���bc1xI#    - `matplotlib.figure.Figure.colorbar` / `matplotlib.pyplot.colorbar`���`a
���bc1x#    - `matplotlib.pyplot.sci`���`a
`dNone�