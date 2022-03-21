�����������bsdx�"""
================
Annotation Polar
================

This example shows how to create an annotation on a polar graph.

For a complete overview of the annotation capabilities, also see the
:doc:`annotation tutorial</tutorials/text/annotations>`.
"""���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���`a
���`cfig���`a ���aoa=���`a ���`cplt���aoa.���`ffigure���`a(���`a)���`a
���`bax���`a ���aoa=���`a ���`cfig���aoa.���`kadd_subplot���`a(���`jprojection���aoa=���bs1a'���bs1epolar���bs1a'���`a)���`a
���`ar���`a ���aoa=���`a ���`bnp���aoa.���`farange���`a(���bmia0���`a,���`a ���bmia1���`a,���`a ���bmfe0.001���`a)���`a
���`etheta���`a ���aoa=���`a ���bmia2���`a ���aoa*���`a ���bmia2���aoa*���`bnp���aoa.���`bpi���`a ���aoa*���`a ���`ar���`a
���`dline���`a,���`a ���aoa=���`a ���`bax���aoa.���`dplot���`a(���`etheta���`a,���`a ���`ar���`a,���`a ���`ecolor���aoa=���bs1a'���bs1g#ee8d18���bs1a'���`a,���`a ���`blw���aoa=���bmia3���`a)���`a
���`a
���`cind���`a ���aoa=���`a ���bmic800���`a
���`ethisr���`a,���`a ���`ithistheta���`a ���aoa=���`a ���`ar���`a[���`cind���`a]���`a,���`a ���`etheta���`a[���`cind���`a]���`a
���`bax���aoa.���`dplot���`a(���`a[���`ithistheta���`a]���`a,���`a ���`a[���`ethisr���`a]���`a,���`a ���bs1a'���bs1ao���bs1a'���`a)���`a
���`bax���aoa.���`hannotate���`a(���bs1a'���bs1ra polar annotation���bs1a'���`a,���`a
���`l            ���`bxy���aoa=���`a(���`ithistheta���`a,���`a ���`ethisr���`a)���`a,���`b  ���bc1o# theta, radius���`a
���`l            ���`fxytext���aoa=���`a(���bmfd0.05���`a,���`a ���bmfd0.05���`a)���`a,���`d    ���bc1t# fraction, fraction���`a
���`l            ���`jtextcoords���aoa=���bs1a'���bs1ofigure fraction���bs1a'���`a,���`a
���`l            ���`jarrowprops���aoa=���bnbddict���`a(���`ifacecolor���aoa=���bs1a'���bs1eblack���bs1a'���`a,���`a ���`fshrink���aoa=���bmfd0.05���`a)���`a,���`a
���`l            ���`shorizontalalignment���aoa=���bs1a'���bs1dleft���bs1a'���`a,���`a
���`l            ���`qverticalalignment���aoa=���bs1a'���bs1fbottom���bs1a'���`a,���`a
���`l            ���`a)���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
���`a
���bc1xM#############################################################################���`a
���bc1a#���`a
���bc1x# .. admonition:: References���`a
���bc1a#���`a
���bc1xN#    The use of the following functions, methods, classes and modules is shown���`a
���bc1u#    in this example:���`a
���bc1a#���`a
���bc1x%#    - `matplotlib.projections.polar`���`a
���bc1xE#    - `matplotlib.axes.Axes.annotate` / `matplotlib.pyplot.annotate`���`a
`dNone�