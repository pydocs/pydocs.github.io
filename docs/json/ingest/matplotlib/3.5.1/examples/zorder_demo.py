������������bsdy�"""
===========
Zorder Demo
===========

The drawing order of artists is determined by their ``zorder`` attribute, which
is a floating point number. Artists with higher ``zorder`` are drawn on top.
You can change the order for individual artists by setting their ``zorder``.
The default value depends on the type of the Artist:

================================================================    =======
Artist                                                              Z-order
================================================================    =======
Images (`.AxesImage`, `.FigureImage`, `.BboxImage`)                 0
`.Patch`, `.PatchCollection`                                        1
`.Line2D`, `.LineCollection` (including minor ticks, grid lines)    2
Major ticks                                                         2.01
`.Text` (including axes labels and titles)                          3
`.Legend`                                                           5
================================================================    =======

Any call to a plotting method can set a value for the zorder of that particular
item explicitly.

.. note::

   `~.axes.Axes.set_axisbelow` and :rc:`axes.axisbelow` are convenient helpers
   for setting the zorder of ticks and grid lines.

Drawing is done per `~.axes.Axes` at a time. If you have overlapping Axes, all
elements of the second Axes are drawn on top of the first Axes, irrespective of
their relative zorder.
"""���`a
���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���`a
���`ar���`a ���aoa=���`a ���`bnp���aoa.���`hlinspace���`a(���bmfc0.3���`a,���`a ���bmia1���`a,���`a ���bmib30���`a)���`a
���`etheta���`a ���aoa=���`a ���`bnp���aoa.���`hlinspace���`a(���bmia0���`a,���`a ���bmia4���aoa*���`bnp���aoa.���`bpi���`a,���`a ���bmib30���`a)���`a
���`ax���`a ���aoa=���`a ���`ar���`a ���aoa*���`a ���`bnp���aoa.���`csin���`a(���`etheta���`a)���`a
���`ay���`a ���aoa=���`a ���`ar���`a ���aoa*���`a ���`bnp���aoa.���`ccos���`a(���`etheta���`a)���`a
���`a
���bc1xO###############################################################################���`a
���bc1xL# The following example contains a `.Line2D` created by `~.axes.Axes.plot()`���`a
���bc1xI# and the dots (a `.PatchCollection`) created by `~.axes.Axes.scatter()`.���`a
���bc1x@# Hence, by default the dots are below the line (first subplot).���`a
���bc1xJ# In the second subplot, the ``zorder`` is set explicitly to move the dots���`a
���bc1u# on top of the line.���`a
���`a
���`cfig���`a,���`a ���`a(���`cax1���`a,���`a ���`cax2���`a)���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���bmia1���`a,���`a ���bmia2���`a,���`a ���`gfigsize���aoa=���`a(���bmia6���`a,���`a ���bmfc3.2���`a)���`a)���`a
���`a
���`cax1���aoa.���`dplot���`a(���`ax���`a,���`a ���`ay���`a,���`a ���bs1a'���bs1bC3���bs1a'���`a,���`a ���`blw���aoa=���bmia3���`a)���`a
���`cax1���aoa.���`gscatter���`a(���`ax���`a,���`a ���`ay���`a,���`a ���`as���aoa=���bmic120���`a)���`a
���`cax1���aoa.���`iset_title���`a(���bs1a'���bs1tLines on top of dots���bs1a'���`a)���`a
���`a
���`cax2���aoa.���`dplot���`a(���`ax���`a,���`a ���`ay���`a,���`a ���bs1a'���bs1bC3���bs1a'���`a,���`a ���`blw���aoa=���bmia3���`a)���`a
���`cax2���aoa.���`gscatter���`a(���`ax���`a,���`a ���`ay���`a,���`a ���`as���aoa=���bmic120���`a,���`a ���`fzorder���aoa=���bmfc2.5���`a)���`b  ���bc1x# move dots on top of line���`a
���`cax2���aoa.���`iset_title���`a(���bs1a'���bs1tDots on top of lines���bs1a'���`a)���`a
���`a
���`cplt���aoa.���`ltight_layout���`a(���`a)���`a
���`a
���bc1xO###############################################################################���`a
���bc1xM# Many functions that create a visible object accepts a ``zorder`` parameter.���`a
���bc1xJ# Alternatively, you can call ``set_order()`` on the created object later.���`a
���`a
���`ax���`a ���aoa=���`a ���`bnp���aoa.���`hlinspace���`a(���bmia0���`a,���`a ���bmfc7.5���`a,���`a ���bmic100���`a)���`a
���`cplt���aoa.���`hrcParams���`a[���bs1a'���bs1olines.linewidth���bs1a'���`a]���`a ���aoa=���`a ���bmia5���`a
���`cplt���aoa.���`ffigure���`a(���`a)���`a
���`cplt���aoa.���`dplot���`a(���`ax���`a,���`a ���`bnp���aoa.���`csin���`a(���`ax���`a)���`a,���`a ���`elabel���aoa=���bs1a'���bs1hzorder=2���bs1a'���`a,���`a ���`fzorder���aoa=���bmia2���`a)���`b  ���bc1h# bottom���`a
���`cplt���aoa.���`dplot���`a(���`ax���`a,���`a ���`bnp���aoa.���`csin���`a(���`ax���aoa+���bmfc0.5���`a)���`a,���`a ���`elabel���aoa=���bs1a'���bs1hzorder=3���bs1a'���`a,���`b  ���`fzorder���aoa=���bmia3���`a)���`a
���`cplt���aoa.���`gaxhline���`a(���bmia0���`a,���`a ���`elabel���aoa=���bs1a'���bs1jzorder=2.5���bs1a'���`a,���`a ���`ecolor���aoa=���bs1a'���bs1ilightgrey���bs1a'���`a,���`a ���`fzorder���aoa=���bmfc2.5���`a)���`a
���`cplt���aoa.���`etitle���`a(���bs1a'���bs1xCustom order of elements���bs1a'���`a)���`a
���`al���`a ���aoa=���`a ���`cplt���aoa.���`flegend���`a(���`cloc���aoa=���bs1a'���bs1kupper right���bs1a'���`a)���`a
���`al���aoa.���`jset_zorder���`a(���bmfc2.5���`a)���`b  ���bc1x%# legend between blue and orange line���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
`dNone�