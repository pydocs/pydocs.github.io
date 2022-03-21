������������bsdy�"""
=========
Step Demo
=========

This example demonstrates the use of `.pyplot.step` for piece-wise constant
curves. In particular, it illustrates the effect of the parameter *where*
on the step position.

.. note::

    For the common case that you know the edge positions, use `.pyplot.stairs`
    instead.

The circular markers created with `.pyplot.plot` show the actual data
positions so that it's easier to see the effect of *where*.

"""���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���`a
���`ax���`a ���aoa=���`a ���`bnp���aoa.���`farange���`a(���bmib14���`a)���`a
���`ay���`a ���aoa=���`a ���`bnp���aoa.���`csin���`a(���`ax���`a ���aoa/���`a ���bmia2���`a)���`a
���`a
���`cplt���aoa.���`dstep���`a(���`ax���`a,���`a ���`ay���`a ���aoa+���`a ���bmia2���`a,���`a ���`elabel���aoa=���bs1a'���bs1mpre (default)���bs1a'���`a)���`a
���`cplt���aoa.���`dplot���`a(���`ax���`a,���`a ���`ay���`a ���aoa+���`a ���bmia2���`a,���`a ���bs1a'���bs1co--���bs1a'���`a,���`a ���`ecolor���aoa=���bs1a'���bs1dgrey���bs1a'���`a,���`a ���`ealpha���aoa=���bmfc0.3���`a)���`a
���`a
���`cplt���aoa.���`dstep���`a(���`ax���`a,���`a ���`ay���`a ���aoa+���`a ���bmia1���`a,���`a ���`ewhere���aoa=���bs1a'���bs1cmid���bs1a'���`a,���`a ���`elabel���aoa=���bs1a'���bs1cmid���bs1a'���`a)���`a
���`cplt���aoa.���`dplot���`a(���`ax���`a,���`a ���`ay���`a ���aoa+���`a ���bmia1���`a,���`a ���bs1a'���bs1co--���bs1a'���`a,���`a ���`ecolor���aoa=���bs1a'���bs1dgrey���bs1a'���`a,���`a ���`ealpha���aoa=���bmfc0.3���`a)���`a
���`a
���`cplt���aoa.���`dstep���`a(���`ax���`a,���`a ���`ay���`a,���`a ���`ewhere���aoa=���bs1a'���bs1dpost���bs1a'���`a,���`a ���`elabel���aoa=���bs1a'���bs1dpost���bs1a'���`a)���`a
���`cplt���aoa.���`dplot���`a(���`ax���`a,���`a ���`ay���`a,���`a ���bs1a'���bs1co--���bs1a'���`a,���`a ���`ecolor���aoa=���bs1a'���bs1dgrey���bs1a'���`a,���`a ���`ealpha���aoa=���bmfc0.3���`a)���`a
���`a
���`cplt���aoa.���`dgrid���`a(���`daxis���aoa=���bs1a'���bs1ax���bs1a'���`a,���`a ���`ecolor���aoa=���bs1a'���bs1d0.95���bs1a'���`a)���`a
���`cplt���aoa.���`flegend���`a(���`etitle���aoa=���bs1a'���bs1pParameter where:���bs1a'���`a)���`a
���`cplt���aoa.���`etitle���`a(���bs1a'���bs1splt.step(where=...)���bs1a'���`a)���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
���`a
���bc1xM#############################################################################���`a
���bc1xK# The same behavior can be achieved by using the ``drawstyle`` parameter of���`a
���bc1q# `.pyplot.plot`.���`a
���`a
���`cplt���aoa.���`dplot���`a(���`ax���`a,���`a ���`ay���`a ���aoa+���`a ���bmia2���`a,���`a ���`idrawstyle���aoa=���bs1a'���bs1esteps���bs1a'���`a,���`a ���`elabel���aoa=���bs1a'���bs1rsteps (=steps-pre)���bs1a'���`a)���`a
���`cplt���aoa.���`dplot���`a(���`ax���`a,���`a ���`ay���`a ���aoa+���`a ���bmia2���`a,���`a ���bs1a'���bs1co--���bs1a'���`a,���`a ���`ecolor���aoa=���bs1a'���bs1dgrey���bs1a'���`a,���`a ���`ealpha���aoa=���bmfc0.3���`a)���`a
���`a
���`cplt���aoa.���`dplot���`a(���`ax���`a,���`a ���`ay���`a ���aoa+���`a ���bmia1���`a,���`a ���`idrawstyle���aoa=���bs1a'���bs1isteps-mid���bs1a'���`a,���`a ���`elabel���aoa=���bs1a'���bs1isteps-mid���bs1a'���`a)���`a
���`cplt���aoa.���`dplot���`a(���`ax���`a,���`a ���`ay���`a ���aoa+���`a ���bmia1���`a,���`a ���bs1a'���bs1co--���bs1a'���`a,���`a ���`ecolor���aoa=���bs1a'���bs1dgrey���bs1a'���`a,���`a ���`ealpha���aoa=���bmfc0.3���`a)���`a
���`a
���`cplt���aoa.���`dplot���`a(���`ax���`a,���`a ���`ay���`a,���`a ���`idrawstyle���aoa=���bs1a'���bs1jsteps-post���bs1a'���`a,���`a ���`elabel���aoa=���bs1a'���bs1jsteps-post���bs1a'���`a)���`a
���`cplt���aoa.���`dplot���`a(���`ax���`a,���`a ���`ay���`a,���`a ���bs1a'���bs1co--���bs1a'���`a,���`a ���`ecolor���aoa=���bs1a'���bs1dgrey���bs1a'���`a,���`a ���`ealpha���aoa=���bmfc0.3���`a)���`a
���`a
���`cplt���aoa.���`dgrid���`a(���`daxis���aoa=���bs1a'���bs1ax���bs1a'���`a,���`a ���`ecolor���aoa=���bs1a'���bs1d0.95���bs1a'���`a)���`a
���`cplt���aoa.���`flegend���`a(���`etitle���aoa=���bs1a'���bs1tParameter drawstyle:���bs1a'���`a)���`a
���`cplt���aoa.���`etitle���`a(���bs1a'���bs1wplt.plot(drawstyle=...)���bs1a'���`a)���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
���`a
���bc1xM#############################################################################���`a
���bc1a#���`a
���bc1x# .. admonition:: References���`a
���bc1a#���`a
���bc1xN#    The use of the following functions, methods, classes and modules is shown���`a
���bc1u#    in this example:���`a
���bc1a#���`a
���bc1x=#    - `matplotlib.axes.Axes.step` / `matplotlib.pyplot.step`���`a
���bc1x=#    - `matplotlib.axes.Axes.plot` / `matplotlib.pyplot.plot`���`a
`dNone�