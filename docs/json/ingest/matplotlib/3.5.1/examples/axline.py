��������q���bsdyx"""
==============
Infinite lines
==============

`~.axes.Axes.axvline` and `~.axes.Axes.axhline` draw infinite vertical /
horizontal lines, at given *x* / *y* positions. They are usually used to mark
special data values, e.g. in this example the center and limit values of the
sigmoid function.

`~.axes.Axes.axline` draws infinite straight lines in arbitrary directions.
"""���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���`a
���`at���`a ���aoa=���`a ���`bnp���aoa.���`hlinspace���`a(���aoa-���bmib10���`a,���`a ���bmib10���`a,���`a ���bmic100���`a)���`a
���`csig���`a ���aoa=���`a ���bmia1���`a ���aoa/���`a ���`a(���bmia1���`a ���aoa+���`a ���`bnp���aoa.���`cexp���`a(���aoa-���`at���`a)���`a)���`a
���`a
���`cplt���aoa.���`gaxhline���`a(���`ay���aoa=���bmia0���`a,���`a ���`ecolor���aoa=���bs2a"���bs2eblack���bs2a"���`a,���`a ���`ilinestyle���aoa=���bs2a"���bs2b--���bs2a"���`a)���`a
���`cplt���aoa.���`gaxhline���`a(���`ay���aoa=���bmfc0.5���`a,���`a ���`ecolor���aoa=���bs2a"���bs2eblack���bs2a"���`a,���`a ���`ilinestyle���aoa=���bs2a"���bs2a:���bs2a"���`a)���`a
���`cplt���aoa.���`gaxhline���`a(���`ay���aoa=���bmfc1.0���`a,���`a ���`ecolor���aoa=���bs2a"���bs2eblack���bs2a"���`a,���`a ���`ilinestyle���aoa=���bs2a"���bs2b--���bs2a"���`a)���`a
���`cplt���aoa.���`gaxvline���`a(���`ecolor���aoa=���bs2a"���bs2dgrey���bs2a"���`a)���`a
���`cplt���aoa.���`faxline���`a(���`a(���bmia0���`a,���`a ���bmfc0.5���`a)���`a,���`a ���`eslope���aoa=���bmfd0.25���`a,���`a ���`ecolor���aoa=���bs2a"���bs2eblack���bs2a"���`a,���`a ���`ilinestyle���aoa=���`a(���bmia0���`a,���`a ���`a(���bmia5���`a,���`a ���bmia5���`a)���`a)���`a)���`a
���`cplt���aoa.���`dplot���`a(���`at���`a,���`a ���`csig���`a,���`a ���`ilinewidth���aoa=���bmia2���`a,���`a ���`elabel���aoa=���bsaar���bs2a"���bs2a$���bs2a\���bs2ksigma(t) = ���bs2a\���bs2dfrac���bsic{1}���bs2a{���bs2f1 + e^���bs2a{���bs2e-t}}$���bs2a"���`a)���`a
���`cplt���aoa.���`dxlim���`a(���aoa-���bmib10���`a,���`a ���bmib10���`a)���`a
���`cplt���aoa.���`fxlabel���`a(���bs2a"���bs2at���bs2a"���`a)���`a
���`cplt���aoa.���`flegend���`a(���`hfontsize���aoa=���bmib14���`a)���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
���`a
���bc1xN##############################################################################���`a
���bc1xM# `~.axes.Axes.axline` can also be used with a ``transform`` parameter, which���`a
���bc1xL# applies to the point, but not to the slope. This can be useful for drawing���`a
���bc1xF# diagonal grid lines with a fixed slope, which stay in place when the���`a
���bc1x# plot limits are moved.���`a
���`a
���akcfor���`a ���`cpos���`a ���bowbin���`a ���`bnp���aoa.���`hlinspace���`a(���aoa-���bmia2���`a,���`a ���bmia1���`a,���`a ���bmib10���`a)���`a:���`a
���`d    ���`cplt���aoa.���`faxline���`a(���`a(���`cpos���`a,���`a ���bmia0���`a)���`a,���`a ���`eslope���aoa=���bmfc0.5���`a,���`a ���`ecolor���aoa=���bs1a'���bs1ak���bs1a'���`a,���`a ���`itransform���aoa=���`cplt���aoa.���`cgca���`a(���`a)���aoa.���`itransAxes���`a)���`a
���`a
���`cplt���aoa.���`dylim���`a(���`a[���bmia0���`a,���`a ���bmia1���`a]���`a)���`a
���`cplt���aoa.���`dxlim���`a(���`a[���bmia0���`a,���`a ���bmia1���`a]���`a)���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
���`a
���bc1xM#############################################################################���`a
���bc1a#���`a
���bc1x# .. admonition:: References���`a
���bc1a#���`a
���bc1xN#    The use of the following functions, methods, classes and modules is shown���`a
���bc1u#    in this example:���`a
���bc1a#���`a
���bc1xC#    - `matplotlib.axes.Axes.axhline` / `matplotlib.pyplot.axhline`���`a
���bc1xC#    - `matplotlib.axes.Axes.axvline` / `matplotlib.pyplot.axvline`���`a
���bc1xA#    - `matplotlib.axes.Axes.axline` / `matplotlib.pyplot.axline`���`a
`dNone�