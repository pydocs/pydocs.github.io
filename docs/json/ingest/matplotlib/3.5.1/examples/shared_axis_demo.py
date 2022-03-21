������������bsdy
"""
===========
Shared Axis
===========

You can share the x or y axis limits for one axis with another by
passing an axes instance as a *sharex* or *sharey* keyword argument.

Changing the axis limits on one axes will be reflected automatically
in the other, and vice-versa, so when you navigate with the toolbar
the axes will follow each other on their shared axes.  Ditto for
changes in the axis scaling (e.g., log vs. linear).  However, it is
possible to have differences in tick labeling, e.g., you can selectively
turn off the tick labels on one axes.

The example below shows how to customize the tick labels on the
various axes.  Shared axes share the tick locator, tick formatter,
view limits, and transformation (e.g., log, linear).  But the ticklabels
themselves do not share properties.  This is a feature and not a bug,
because you may want to make the tick labels smaller on the upper
axes, e.g., in the example below.

If you want to turn off the ticklabels for a given axes (e.g., on
subplot(211) or subplot(212), you cannot do the standard trick::

   setp(ax2, xticklabels=[])

because this changes the tick Formatter, which is shared among all
axes.  But you can alter the visibility of the labels, which is a
property::

  setp(ax2.get_xticklabels(), visible=False)

"""���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���`a
���`at���`a ���aoa=���`a ���`bnp���aoa.���`farange���`a(���bmfd0.01���`a,���`a ���bmfc5.0���`a,���`a ���bmfd0.01���`a)���`a
���`bs1���`a ���aoa=���`a ���`bnp���aoa.���`csin���`a(���bmia2���`a ���aoa*���`a ���`bnp���aoa.���`bpi���`a ���aoa*���`a ���`at���`a)���`a
���`bs2���`a ���aoa=���`a ���`bnp���aoa.���`cexp���`a(���aoa-���`at���`a)���`a
���`bs3���`a ���aoa=���`a ���`bnp���aoa.���`csin���`a(���bmia4���`a ���aoa*���`a ���`bnp���aoa.���`bpi���`a ���aoa*���`a ���`at���`a)���`a
���`a
���`cax1���`a ���aoa=���`a ���`cplt���aoa.���`gsubplot���`a(���bmic311���`a)���`a
���`cplt���aoa.���`dplot���`a(���`at���`a,���`a ���`bs1���`a)���`a
���`cplt���aoa.���`ktick_params���`a(���bs1a'���bs1ax���bs1a'���`a,���`a ���`ilabelsize���aoa=���bmia6���`a)���`a
���`a
���bc1n# share x only���`a
���`cax2���`a ���aoa=���`a ���`cplt���aoa.���`gsubplot���`a(���bmic312���`a,���`a ���`fsharex���aoa=���`cax1���`a)���`a
���`cplt���aoa.���`dplot���`a(���`at���`a,���`a ���`bs2���`a)���`a
���bc1x"# make these tick labels invisible���`a
���`cplt���aoa.���`ktick_params���`a(���bs1a'���bs1ax���bs1a'���`a,���`a ���`klabelbottom���aoa=���bkceFalse���`a)���`a
���`a
���bc1o# share x and y���`a
���`cax3���`a ���aoa=���`a ���`cplt���aoa.���`gsubplot���`a(���bmic313���`a,���`a ���`fsharex���aoa=���`cax1���`a,���`a ���`fsharey���aoa=���`cax1���`a)���`a
���`cplt���aoa.���`dplot���`a(���`at���`a,���`a ���`bs3���`a)���`a
���`cplt���aoa.���`dxlim���`a(���bmfd0.01���`a,���`a ���bmfc5.0���`a)���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
`dNone�