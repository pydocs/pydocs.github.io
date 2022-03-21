������������bsdyL"""
=================
Annotating a plot
=================

This example shows how to annotate a plot with an arrow pointing to provided
coordinates. We modify the defaults of the arrow, to "shrink" it.

For a complete overview of the annotation capabilities, also see the
:doc:`annotation tutorial</tutorials/text/annotations>`.
"""���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���`a
���`cfig���`a,���`a ���`bax���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`a)���`a
���`a
���`at���`a ���aoa=���`a ���`bnp���aoa.���`farange���`a(���bmfc0.0���`a,���`a ���bmfc5.0���`a,���`a ���bmfd0.01���`a)���`a
���`as���`a ���aoa=���`a ���`bnp���aoa.���`ccos���`a(���bmia2���aoa*���`bnp���aoa.���`bpi���aoa*���`at���`a)���`a
���`dline���`a,���`a ���aoa=���`a ���`bax���aoa.���`dplot���`a(���`at���`a,���`a ���`as���`a,���`a ���`blw���aoa=���bmia2���`a)���`a
���`a
���`bax���aoa.���`hannotate���`a(���bs1a'���bs1ilocal max���bs1a'���`a,���`a ���`bxy���aoa=���`a(���bmia2���`a,���`a ���bmia1���`a)���`a,���`a ���`fxytext���aoa=���`a(���bmia3���`a,���`a ���bmfc1.5���`a)���`a,���`a
���`l            ���`jarrowprops���aoa=���bnbddict���`a(���`ifacecolor���aoa=���bs1a'���bs1eblack���bs1a'���`a,���`a ���`fshrink���aoa=���bmfd0.05���`a)���`a,���`a
���`l            ���`a)���`a
���`bax���aoa.���`hset_ylim���`a(���aoa-���bmia2���`a,���`a ���bmia2���`a)���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
���`a
���bc1xM#############################################################################���`a
���bc1a#���`a
���bc1x# .. admonition:: References���`a
���bc1a#���`a
���bc1xN#    The use of the following functions, methods, classes and modules is shown���`a
���bc1u#    in this example:���`a
���bc1a#���`a
���bc1xE#    - `matplotlib.axes.Axes.annotate` / `matplotlib.pyplot.annotate`���`a
`dNone�