������������bsdx�"""
==================
Quiver Simple Demo
==================

A simple example of a `~.axes.Axes.quiver` plot with a `~.axes.Axes.quiverkey`.

For more advanced options refer to
:doc:`/gallery/images_contours_and_fields/quiver_demo`.
"""���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���`a
���`aX���`a ���aoa=���`a ���`bnp���aoa.���`farange���`a(���aoa-���bmib10���`a,���`a ���bmib10���`a,���`a ���bmia1���`a)���`a
���`aY���`a ���aoa=���`a ���`bnp���aoa.���`farange���`a(���aoa-���bmib10���`a,���`a ���bmib10���`a,���`a ���bmia1���`a)���`a
���`aU���`a,���`a ���`aV���`a ���aoa=���`a ���`bnp���aoa.���`hmeshgrid���`a(���`aX���`a,���`a ���`aY���`a)���`a
���`a
���`cfig���`a,���`a ���`bax���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`a)���`a
���`aq���`a ���aoa=���`a ���`bax���aoa.���`fquiver���`a(���`aX���`a,���`a ���`aY���`a,���`a ���`aU���`a,���`a ���`aV���`a)���`a
���`bax���aoa.���`iquiverkey���`a(���`aq���`a,���`a ���`aX���aoa=���bmfc0.3���`a,���`a ���`aY���aoa=���bmfc1.1���`a,���`a ���`aU���aoa=���bmib10���`a,���`a
���`m             ���`elabel���aoa=���bs1a'���bs1wQuiver key, length = 10���bs1a'���`a,���`a ���`hlabelpos���aoa=���bs1a'���bs1aE���bs1a'���`a)���`a
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
���bc1xA#    - `matplotlib.axes.Axes.quiver` / `matplotlib.pyplot.quiver`���`a
���bc1xG#    - `matplotlib.axes.Axes.quiverkey` / `matplotlib.pyplot.quiverkey`���`a
`dNone�