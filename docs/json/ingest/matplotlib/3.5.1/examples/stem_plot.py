������������bsdx�"""
=========
Stem Plot
=========

`~.pyplot.stem` plots vertical lines from a baseline to the y-coordinate and
places a marker at the tip.
"""���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���`a
���`ax���`a ���aoa=���`a ���`bnp���aoa.���`hlinspace���`a(���bmfc0.1���`a,���`a ���bmia2���`a ���aoa*���`a ���`bnp���aoa.���`bpi���`a,���`a ���bmib41���`a)���`a
���`ay���`a ���aoa=���`a ���`bnp���aoa.���`cexp���`a(���`bnp���aoa.���`csin���`a(���`ax���`a)���`a)���`a
���`a
���`cplt���aoa.���`dstem���`a(���`ax���`a,���`a ���`ay���`a)���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
���`a
���bc1xM#############################################################################���`a
���bc1a#���`a
���bc1x=# The position of the baseline can be adapted using *bottom*.���`a
���bc1xK# The parameters *linefmt*, *markerfmt*, and *basefmt* control basic format���`a
���bc1xI# properties of the plot. However, in contrast to `~.pyplot.plot` not all���`a
���bc1xF# properties are configurable via keyword arguments. For more advanced���`a
���bc1x7# control adapt the line objects returned by `.pyplot`.���`a
���`a
���`jmarkerline���`a,���`a ���`istemlines���`a,���`a ���`hbaseline���`a ���aoa=���`a ���`cplt���aoa.���`dstem���`a(���`a
���`d    ���`ax���`a,���`a ���`ay���`a,���`a ���`glinefmt���aoa=���bs1a'���bs1dgrey���bs1a'���`a,���`a ���`imarkerfmt���aoa=���bs1a'���bs1aD���bs1a'���`a,���`a ���`fbottom���aoa=���bmfc1.1���`a)���`a
���`jmarkerline���aoa.���`sset_markerfacecolor���`a(���bs1a'���bs1dnone���bs1a'���`a)���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
���`a
���bc1xM#############################################################################���`a
���bc1a#���`a
���bc1x# .. admonition:: References���`a
���bc1a#���`a
���bc1xN#    The use of the following functions, methods, classes and modules is shown���`a
���bc1u#    in this example:���`a
���bc1a#���`a
���bc1x=#    - `matplotlib.axes.Axes.stem` / `matplotlib.pyplot.stem`���`a
`dNone�