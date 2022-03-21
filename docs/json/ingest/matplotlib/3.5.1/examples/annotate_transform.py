��������k���bsdy"""
==================
Annotate Transform
==================

This example shows how to use different coordinate systems for annotations.
For a complete overview of the annotation capabilities, also see the
:doc:`annotation tutorial</tutorials/text/annotations>`.
"""���`a
���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���`a
���`ax���`a ���aoa=���`a ���`bnp���aoa.���`farange���`a(���bmia0���`a,���`a ���bmib10���`a,���`a ���bmfe0.005���`a)���`a
���`ay���`a ���aoa=���`a ���`bnp���aoa.���`cexp���`a(���aoa-���`ax���aoa/���bmfb2.���`a)���`a ���aoa*���`a ���`bnp���aoa.���`csin���`a(���bmia2���aoa*���`bnp���aoa.���`bpi���aoa*���`ax���`a)���`a
���`a
���`cfig���`a,���`a ���`bax���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`a)���`a
���`bax���aoa.���`dplot���`a(���`ax���`a,���`a ���`ay���`a)���`a
���`bax���aoa.���`hset_xlim���`a(���bmia0���`a,���`a ���bmib10���`a)���`a
���`bax���aoa.���`hset_ylim���`a(���aoa-���bmia1���`a,���`a ���bmia1���`a)���`a
���`a
���`exdata���`a,���`a ���`eydata���`a ���aoa=���`a ���bmia5���`a,���`a ���bmia0���`a
���`hxdisplay���`a,���`a ���`hydisplay���`a ���aoa=���`a ���`bax���aoa.���`itransData���aoa.���`itransform���`a(���`a(���`exdata���`a,���`a ���`eydata���`a)���`a)���`a
���`a
���`dbbox���`a ���aoa=���`a ���bnbddict���`a(���`hboxstyle���aoa=���bs2a"���bs2eround���bs2a"���`a,���`a ���`bfc���aoa=���bs2a"���bs2c0.8���bs2a"���`a)���`a
���`jarrowprops���`a ���aoa=���`a ���bnbddict���`a(���`a
���`d    ���`jarrowstyle���aoa=���bs2a"���bs2b->���bs2a"���`a,���`a
���`d    ���`oconnectionstyle���aoa=���bs2a"���bs2xangle,angleA=0,angleB=90,rad=10���bs2a"���`a)���`a
���`a
���`foffset���`a ���aoa=���`a ���bmib72���`a
���`bax���aoa.���`hannotate���`a(���`a
���`d    ���bsaaf���bs1a'���bs1hdata = (���bsia{���`exdata���bsia:���bs1c.1f���bsia}���bs1b, ���bsia{���`eydata���bsia:���bs1c.1f���bsia}���bs1a)���bs1a'���`a,���`a
���`d    ���`a(���`exdata���`a,���`a ���`eydata���`a)���`a,���`a
���`d    ���`fxytext���aoa=���`a(���aoa-���bmia2���aoa*���`foffset���`a,���`a ���`foffset���`a)���`a,���`a ���`jtextcoords���aoa=���bs1a'���bs1moffset points���bs1a'���`a,���`a
���`d    ���`dbbox���aoa=���`dbbox���`a,���`a ���`jarrowprops���aoa=���`jarrowprops���`a)���`a
���`bax���aoa.���`hannotate���`a(���`a
���`d    ���bsaaf���bs1a'���bs1kdisplay = (���bsia{���`hxdisplay���bsia:���bs1c.1f���bsia}���bs1b, ���bsia{���`hydisplay���bsia:���bs1c.1f���bsia}���bs1a)���bs1a'���`a,���`a
���`d    ���`bxy���aoa=���`a(���`hxdisplay���`a,���`a ���`hydisplay���`a)���`a,���`a ���`hxycoords���aoa=���bs1a'���bs1mfigure pixels���bs1a'���`a,���`a
���`d    ���`fxytext���aoa=���`a(���bmfc0.5���aoa*���`foffset���`a,���`a ���aoa-���`foffset���`a)���`a,���`a ���`jtextcoords���aoa=���bs1a'���bs1moffset points���bs1a'���`a,���`a
���`d    ���`dbbox���aoa=���`dbbox���`a,���`a ���`jarrowprops���aoa=���`jarrowprops���`a)���`a
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
���bc1x2#    - `matplotlib.transforms.Transform.transform`���`a
���bc1xE#    - `matplotlib.axes.Axes.annotate` / `matplotlib.pyplot.annotate`���`a
`dNone�