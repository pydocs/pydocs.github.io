��������R���bsdx�"""
=======
3D stem
=======

Demonstration of a stem plot in 3D, which plots vertical lines from a baseline
to the *z*-coordinate and places a marker at the tip.
"""���`a
���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���`a
���`etheta���`a ���aoa=���`a ���`bnp���aoa.���`hlinspace���`a(���bmia0���`a,���`a ���bmia2���aoa*���`bnp���aoa.���`bpi���`a)���`a
���`ax���`a ���aoa=���`a ���`bnp���aoa.���`ccos���`a(���`etheta���`a ���aoa-���`a ���`bnp���aoa.���`bpi���aoa/���bmia2���`a)���`a
���`ay���`a ���aoa=���`a ���`bnp���aoa.���`csin���`a(���`etheta���`a ���aoa-���`a ���`bnp���aoa.���`bpi���aoa/���bmia2���`a)���`a
���`az���`a ���aoa=���`a ���`etheta���`a
���`a
���`cfig���`a,���`a ���`bax���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`jsubplot_kw���aoa=���bnbddict���`a(���`jprojection���aoa=���bs1a'���bs1b3d���bs1a'���`a)���`a)���`a
���`bax���aoa.���`dstem���`a(���`ax���`a,���`a ���`ay���`a,���`a ���`az���`a)���`a
���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
���`a
���bc1xM#############################################################################���`a
���bc1a#���`a
���bc1xL# The position of the baseline can be adapted using *bottom*. The parameters���`a
���bc1xN# *linefmt*, *markerfmt*, and *basefmt* control basic format properties of the���`a
���bc1xM# plot. However, in contrast to `~.axes3d.Axes3D.plot` not all properties are���`a
���bc1xN# configurable via keyword arguments. For more advanced control adapt the line���`a
���bc1x # objects returned by `.stem3D`.���`a
���`a
���`cfig���`a,���`a ���`bax���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`jsubplot_kw���aoa=���bnbddict���`a(���`jprojection���aoa=���bs1a'���bs1b3d���bs1a'���`a)���`a)���`a
���`jmarkerline���`a,���`a ���`istemlines���`a,���`a ���`hbaseline���`a ���aoa=���`a ���`bax���aoa.���`dstem���`a(���`a
���`d    ���`ax���`a,���`a ���`ay���`a,���`a ���`az���`a,���`a ���`glinefmt���aoa=���bs1a'���bs1dgrey���bs1a'���`a,���`a ���`imarkerfmt���aoa=���bs1a'���bs1aD���bs1a'���`a,���`a ���`fbottom���aoa=���`bnp���aoa.���`bpi���`a)���`a
���`jmarkerline���aoa.���`sset_markerfacecolor���`a(���bs1a'���bs1dnone���bs1a'���`a)���`a
���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
���`a
���bc1xM#############################################################################���`a
���bc1a#���`a
���bc1xO# The orientation of the stems and baseline can be changed using *orientation*.���`a
���bc1xJ# This determines in which direction the stems are projected from the head���`a
���bc1x(# points, towards the *bottom* baseline.���`a
���bc1a#���`a
���bc1xM# For examples, by setting ``orientation='x'``, the stems are projected along���`a
���bc1x;# the *x*-direction, and the baseline is in the *yz*-plane.���`a
���`a
���`cfig���`a,���`a ���`bax���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`jsubplot_kw���aoa=���bnbddict���`a(���`jprojection���aoa=���bs1a'���bs1b3d���bs1a'���`a)���`a)���`a
���`jmarkerline���`a,���`a ���`istemlines���`a,���`a ���`hbaseline���`a ���aoa=���`a ���`bax���aoa.���`dstem���`a(���`ax���`a,���`a ���`ay���`a,���`a ���`az���`a,���`a ���`fbottom���aoa=���aoa-���bmia1���`a,���`a ���`korientation���aoa=���bs1a'���bs1ax���bs1a'���`a)���`a
���`bax���aoa.���`cset���`a(���`fxlabel���aoa=���bs1a'���bs1ax���bs1a'���`a,���`a ���`fylabel���aoa=���bs1a'���bs1ay���bs1a'���`a,���`a ���`fzlabel���aoa=���bs1a'���bs1az���bs1a'���`a)���`a
���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
`dNone�