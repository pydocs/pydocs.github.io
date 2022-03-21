��������[���bsdyg"""
============================
pcolormesh grids and shading
============================

`.axes.Axes.pcolormesh` and `~.axes.Axes.pcolor` have a few options for
how grids are laid out and the shading between the grid points.

Generally, if *Z* has shape *(M, N)* then the grid *X* and *Y* can be
specified with either shape *(M+1, N+1)* or *(M, N)*, depending on the
argument for the ``shading`` keyword argument.  Note that below we specify
vectors *x* as either length N or N+1 and *y* as length M or M+1, and
`~.axes.Axes.pcolormesh` internally makes the mesh matrices *X* and *Y* from
the input vectors.

"""���`a
���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���`a
���bc1xO###############################################################################���`a
���bc1n# Flat Shading���`a
���bc1n# ------------���`a
���bc1a#���`a
���bc1xI# The grid specification with the least assumptions is ``shading='flat'``���`a
���bc1xO# and if the grid is one larger than the data in each dimension, i.e. has shape���`a
���bc1xO# *(M+1, N+1)*.  In that case *X* and *Y* specify the corners of quadrilaterals���`a
���bc1xK# that are colored with the values in *Z*. Here we specify the edges of the���`a
���bc1x=# *(3, 5)* quadrilaterals with *X* and *Y* that are *(4, 6)*.���`a
���`a
���`enrows���`a ���aoa=���`a ���bmia3���`a
���`encols���`a ���aoa=���`a ���bmia5���`a
���`aZ���`a ���aoa=���`a ���`bnp���aoa.���`farange���`a(���`enrows���`a ���aoa*���`a ���`encols���`a)���aoa.���`greshape���`a(���`enrows���`a,���`a ���`encols���`a)���`a
���`ax���`a ���aoa=���`a ���`bnp���aoa.���`farange���`a(���`encols���`a ���aoa+���`a ���bmia1���`a)���`a
���`ay���`a ���aoa=���`a ���`bnp���aoa.���`farange���`a(���`enrows���`a ���aoa+���`a ���bmia1���`a)���`a
���`a
���`cfig���`a,���`a ���`bax���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`a)���`a
���`bax���aoa.���`jpcolormesh���`a(���`ax���`a,���`a ���`ay���`a,���`a ���`aZ���`a,���`a ���`gshading���aoa=���bs1a'���bs1dflat���bs1a'���`a,���`a ���`dvmin���aoa=���`aZ���aoa.���`cmin���`a(���`a)���`a,���`a ���`dvmax���aoa=���`aZ���aoa.���`cmax���`a(���`a)���`a)���`a
���`a
���`a
���akcdef���`a ���bnfi_annotate���`a(���`bax���`a,���`a ���`ax���`a,���`a ���`ay���`a,���`a ���`etitle���`a)���`a:���`a
���`d    ���bc1x# this all gets repeated below:���`a
���`d    ���`aX���`a,���`a ���`aY���`a ���aoa=���`a ���`bnp���aoa.���`hmeshgrid���`a(���`ax���`a,���`a ���`ay���`a)���`a
���`d    ���`bax���aoa.���`dplot���`a(���`aX���aoa.���`dflat���`a,���`a ���`aY���aoa.���`dflat���`a,���`a ���bs1a'���bs1ao���bs1a'���`a,���`a ���`ecolor���aoa=���bs1a'���bs1am���bs1a'���`a)���`a
���`d    ���`bax���aoa.���`hset_xlim���`a(���aoa-���bmfc0.7���`a,���`a ���bmfc5.2���`a)���`a
���`d    ���`bax���aoa.���`hset_ylim���`a(���aoa-���bmfc0.7���`a,���`a ���bmfc3.2���`a)���`a
���`d    ���`bax���aoa.���`iset_title���`a(���`etitle���`a)���`a
���`a
���`i_annotate���`a(���`bax���`a,���`a ���`ax���`a,���`a ���`ay���`a,���`a ���bs2a"���bs2hshading=���bs2a'���bs2dflat���bs2a'���bs2a"���`a)���`a
���`a
���`a
���bc1xO###############################################################################���`a
���bc1x# Flat Shading, same shape grid���`a
���bc1x# -----------------------------���`a
���bc1a#���`a
���bc1xL# Often, however, data is provided where *X* and *Y* match the shape of *Z*.���`a
���bc1xO# While this makes sense for other ``shading`` types, it is no longer permitted���`a
���bc1xN# when ``shading='flat'`` (and will raise a MatplotlibDeprecationWarning as of���`a
���bc1xN# Matplotlib v3.3). Historically, Matplotlib silently dropped the last row and���`a
���bc1xM# column of *Z* in this case, to match Matlab's behavior. If this behavior is���`a
���bc1x># still desired, simply drop the last row and column manually:���`a
���`a
���`ax���`a ���aoa=���`a ���`bnp���aoa.���`farange���`a(���`encols���`a)���`b  ���bc1x # note *not* ncols + 1 as before���`a
���`ay���`a ���aoa=���`a ���`bnp���aoa.���`farange���`a(���`enrows���`a)���`a
���`cfig���`a,���`a ���`bax���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`a)���`a
���`bax���aoa.���`jpcolormesh���`a(���`ax���`a,���`a ���`ay���`a,���`a ���`aZ���`a[���`a:���aoa-���bmia1���`a,���`a ���`a:���aoa-���bmia1���`a]���`a,���`a ���`gshading���aoa=���bs1a'���bs1dflat���bs1a'���`a,���`a ���`dvmin���aoa=���`aZ���aoa.���`cmin���`a(���`a)���`a,���`a ���`dvmax���aoa=���`aZ���aoa.���`cmax���`a(���`a)���`a)���`a
���`i_annotate���`a(���`bax���`a,���`a ���`ax���`a,���`a ���`ay���`a,���`a ���bs2a"���bs2hshading=���bs2a'���bs2dflat���bs2a'���bs2t: X, Y, C same shape���bs2a"���`a)���`a
���`a
���bc1xO###############################################################################���`a
���bc1x"# Nearest Shading, same shape grid���`a
���bc1x"# --------------------------------���`a
���bc1a#���`a
���bc1xL# Usually, dropping a row and column of data is not what the user means when���`a
���bc1xK# they make *X*, *Y* and *Z* all the same shape.  For this case, Matplotlib���`a
���bc1xL# allows ``shading='nearest'`` and centers the colored quadrilaterals on the���`a
���bc1n# grid points.���`a
���bc1a#���`a
���bc1xN# If a grid that is not the correct shape is passed with ``shading='nearest'``���`a
���bc1u# an error is raised.���`a
���`a
���`cfig���`a,���`a ���`bax���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`a)���`a
���`bax���aoa.���`jpcolormesh���`a(���`ax���`a,���`a ���`ay���`a,���`a ���`aZ���`a,���`a ���`gshading���aoa=���bs1a'���bs1gnearest���bs1a'���`a,���`a ���`dvmin���aoa=���`aZ���aoa.���`cmin���`a(���`a)���`a,���`a ���`dvmax���aoa=���`aZ���aoa.���`cmax���`a(���`a)���`a)���`a
���`i_annotate���`a(���`bax���`a,���`a ���`ax���`a,���`a ���`ay���`a,���`a ���bs2a"���bs2hshading=���bs2a'���bs2gnearest���bs2a'���bs2a"���`a)���`a
���`a
���bc1xO###############################################################################���`a
���bc1n# Auto Shading���`a
���bc1n# ------------���`a
���bc1a#���`a
���bc1xO# It's possible that the user would like the code to automatically choose which���`a
���bc1xN# to use, in this case ``shading='auto'`` will decide whether to use 'flat' or���`a
���bc1x<# 'nearest' shading based on the shapes of *X*, *Y* and *Z*.���`a
���`a
���`cfig���`a,���`a ���`caxs���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���bmia2���`a,���`a ���bmia1���`a,���`a ���`rconstrained_layout���aoa=���bkcdTrue���`a)���`a
���`bax���`a ���aoa=���`a ���`caxs���`a[���bmia0���`a]���`a
���`ax���`a ���aoa=���`a ���`bnp���aoa.���`farange���`a(���`encols���`a)���`a
���`ay���`a ���aoa=���`a ���`bnp���aoa.���`farange���`a(���`enrows���`a)���`a
���`bax���aoa.���`jpcolormesh���`a(���`ax���`a,���`a ���`ay���`a,���`a ���`aZ���`a,���`a ���`gshading���aoa=���bs1a'���bs1dauto���bs1a'���`a,���`a ���`dvmin���aoa=���`aZ���aoa.���`cmin���`a(���`a)���`a,���`a ���`dvmax���aoa=���`aZ���aoa.���`cmax���`a(���`a)���`a)���`a
���`i_annotate���`a(���`bax���`a,���`a ���`ax���`a,���`a ���`ay���`a,���`a ���bs2a"���bs2hshading=���bs2a'���bs2dauto���bs2a'���bs2x; X, Y, Z: same shape (nearest)���bs2a"���`a)���`a
���`a
���`bax���`a ���aoa=���`a ���`caxs���`a[���bmia1���`a]���`a
���`ax���`a ���aoa=���`a ���`bnp���aoa.���`farange���`a(���`encols���`a ���aoa+���`a ���bmia1���`a)���`a
���`ay���`a ���aoa=���`a ���`bnp���aoa.���`farange���`a(���`enrows���`a ���aoa+���`a ���bmia1���`a)���`a
���`bax���aoa.���`jpcolormesh���`a(���`ax���`a,���`a ���`ay���`a,���`a ���`aZ���`a,���`a ���`gshading���aoa=���bs1a'���bs1dauto���bs1a'���`a,���`a ���`dvmin���aoa=���`aZ���aoa.���`cmin���`a(���`a)���`a,���`a ���`dvmax���aoa=���`aZ���aoa.���`cmax���`a(���`a)���`a)���`a
���`i_annotate���`a(���`bax���`a,���`a ���`ax���`a,���`a ���`ay���`a,���`a ���bs2a"���bs2hshading=���bs2a'���bs2dauto���bs2a'���bs2x; X, Y one larger than Z (flat)���bs2a"���`a)���`a
���`a
���bc1xO###############################################################################���`a
���bc1q# Gouraud Shading���`a
���bc1q# ---------------���`a
���bc1a#���`a
���bc1xM# `Gouraud shading <https://en.wikipedia.org/wiki/Gouraud_shading>`_ can also���`a
���bc1xN# be specified, where the color in the quadrilaterals is linearly interpolated���`a
���bc1xI# between the grid points.  The shapes of *X*, *Y*, *Z* must be the same.���`a
���`a
���`cfig���`a,���`a ���`bax���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`rconstrained_layout���aoa=���bkcdTrue���`a)���`a
���`ax���`a ���aoa=���`a ���`bnp���aoa.���`farange���`a(���`encols���`a)���`a
���`ay���`a ���aoa=���`a ���`bnp���aoa.���`farange���`a(���`enrows���`a)���`a
���`bax���aoa.���`jpcolormesh���`a(���`ax���`a,���`a ���`ay���`a,���`a ���`aZ���`a,���`a ���`gshading���aoa=���bs1a'���bs1ggouraud���bs1a'���`a,���`a ���`dvmin���aoa=���`aZ���aoa.���`cmin���`a(���`a)���`a,���`a ���`dvmax���aoa=���`aZ���aoa.���`cmax���`a(���`a)���`a)���`a
���`i_annotate���`a(���`bax���`a,���`a ���`ax���`a,���`a ���`ay���`a,���`a ���bs2a"���bs2hshading=���bs2a'���bs2ggouraud���bs2a'���bs2v; X, Y same shape as Z���bs2a"���`a)���`a
���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
���bc1xM#############################################################################���`a
���bc1a#���`a
���bc1x# .. admonition:: References���`a
���bc1a#���`a
���bc1xN#    The use of the following functions, methods, classes and modules is shown���`a
���bc1u#    in this example:���`a
���bc1a#���`a
���bc1xI#    - `matplotlib.axes.Axes.pcolormesh` / `matplotlib.pyplot.pcolormesh`���`a
`dNone�