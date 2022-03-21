������������bsdyQ"""
===============
Basic pie chart
===============

Demo of a basic pie chart plus a few additional features.

In addition to the basic pie chart, this demo shows a few optional features:

* slice labels
* auto-labeling the percentage
* offsetting a slice with "explode"
* drop-shadow
* custom start angle

Note about the custom start angle:

The default ``startangle`` is 0, which would start the "Frogs" slice on the
positive x-axis. This example sets ``startangle = 90`` such that everything is
rotated counter-clockwise by 90 degrees, and the frog slice starts on the
positive y-axis.
"""���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���`a
���bc1xL# Pie chart, where the slices will be ordered and plotted counter-clockwise:���`a
���`flabels���`a ���aoa=���`a ���bs1a'���bs1eFrogs���bs1a'���`a,���`a ���bs1a'���bs1dHogs���bs1a'���`a,���`a ���bs1a'���bs1dDogs���bs1a'���`a,���`a ���bs1a'���bs1dLogs���bs1a'���`a
���`esizes���`a ���aoa=���`a ���`a[���bmib15���`a,���`a ���bmib30���`a,���`a ���bmib45���`a,���`a ���bmib10���`a]���`a
���`gexplode���`a ���aoa=���`a ���`a(���bmia0���`a,���`a ���bmfc0.1���`a,���`a ���bmia0���`a,���`a ���bmia0���`a)���`b  ���bc1x,# only "explode" the 2nd slice (i.e. 'Hogs')���`a
���`a
���`dfig1���`a,���`a ���`cax1���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`a)���`a
���`cax1���aoa.���`cpie���`a(���`esizes���`a,���`a ���`gexplode���aoa=���`gexplode���`a,���`a ���`flabels���aoa=���`flabels���`a,���`a ���`gautopct���aoa=���bs1a'���bsie%1.1f���bsib%%���bs1a'���`a,���`a
���`h        ���`fshadow���aoa=���bkcdTrue���`a,���`a ���`jstartangle���aoa=���bmib90���`a)���`a
���`cax1���aoa.���`daxis���`a(���bs1a'���bs1eequal���bs1a'���`a)���`b  ���bc1x;# Equal aspect ratio ensures that pie is drawn as a circle.���`a
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
���bc1x;#    - `matplotlib.axes.Axes.pie` / `matplotlib.pyplot.pie`���`a
`dNone�