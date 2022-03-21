��������$���bsdxf"""
==============
Triinterp Demo
==============

Interpolation from triangular grid to quad grid.
"""���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnctri���`a ���akbas���`a ���bnndmtri���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���`a
���bc1w# Create triangulation.���`a
���`ax���`a ���aoa=���`a ���`bnp���aoa.���`gasarray���`a(���`a[���bmia0���`a,���`a ���bmia1���`a,���`a ���bmia2���`a,���`a ���bmia3���`a,���`a ���bmfc0.5���`a,���`a ���bmfc1.5���`a,���`a ���bmfc2.5���`a,���`a ���bmia1���`a,���`a ���bmia2���`a,���`a ���bmfc1.5���`a]���`a)���`a
���`ay���`a ���aoa=���`a ���`bnp���aoa.���`gasarray���`a(���`a[���bmia0���`a,���`a ���bmia0���`a,���`a ���bmia0���`a,���`a ���bmia0���`a,���`a ���bmfc1.0���`a,���`a ���bmfc1.0���`a,���`a ���bmfc1.0���`a,���`a ���bmia2���`a,���`a ���bmia2���`a,���`a ���bmfc3.0���`a]���`a)���`a
���`itriangles���`a ���aoa=���`a ���`a[���`a[���bmia0���`a,���`a ���bmia1���`a,���`a ���bmia4���`a]���`a,���`a ���`a[���bmia1���`a,���`a ���bmia2���`a,���`a ���bmia5���`a]���`a,���`a ���`a[���bmia2���`a,���`a ���bmia3���`a,���`a ���bmia6���`a]���`a,���`a ���`a[���bmia1���`a,���`a ���bmia5���`a,���`a ���bmia4���`a]���`a,���`a ���`a[���bmia2���`a,���`a ���bmia6���`a,���`a ���bmia5���`a]���`a,���`a ���`a[���bmia4���`a,���`a ���bmia5���`a,���`a ���bmia7���`a]���`a,���`a
���`m             ���`a[���bmia5���`a,���`a ���bmia6���`a,���`a ���bmia8���`a]���`a,���`a ���`a[���bmia5���`a,���`a ���bmia8���`a,���`a ���bmia7���`a]���`a,���`a ���`a[���bmia7���`a,���`a ���bmia8���`a,���`a ���bmia9���`a]���`a]���`a
���`ftriang���`a ���aoa=���`a ���`dmtri���aoa.���`mTriangulation���`a(���`ax���`a,���`a ���`ay���`a,���`a ���`itriangles���`a)���`a
���`a
���bc1x,# Interpolate to regularly-spaced quad grid.���`a
���`az���`a ���aoa=���`a ���`bnp���aoa.���`ccos���`a(���bmfc1.5���`a ���aoa*���`a ���`ax���`a)���`a ���aoa*���`a ���`bnp���aoa.���`ccos���`a(���bmfc1.5���`a ���aoa*���`a ���`ay���`a)���`a
���`bxi���`a,���`a ���`byi���`a ���aoa=���`a ���`bnp���aoa.���`hmeshgrid���`a(���`bnp���aoa.���`hlinspace���`a(���bmia0���`a,���`a ���bmia3���`a,���`a ���bmib20���`a)���`a,���`a ���`bnp���aoa.���`hlinspace���`a(���bmia0���`a,���`a ���bmia3���`a,���`a ���bmib20���`a)���`a)���`a
���`a
���`jinterp_lin���`a ���aoa=���`a ���`dmtri���aoa.���`uLinearTriInterpolator���`a(���`ftriang���`a,���`a ���`az���`a)���`a
���`fzi_lin���`a ���aoa=���`a ���`jinterp_lin���`a(���`bxi���`a,���`a ���`byi���`a)���`a
���`a
���`qinterp_cubic_geom���`a ���aoa=���`a ���`dmtri���aoa.���`tCubicTriInterpolator���`a(���`ftriang���`a,���`a ���`az���`a,���`a ���`dkind���aoa=���bs1a'���bs1dgeom���bs1a'���`a)���`a
���`mzi_cubic_geom���`a ���aoa=���`a ���`qinterp_cubic_geom���`a(���`bxi���`a,���`a ���`byi���`a)���`a
���`a
���`rinterp_cubic_min_E���`a ���aoa=���`a ���`dmtri���aoa.���`tCubicTriInterpolator���`a(���`ftriang���`a,���`a ���`az���`a,���`a ���`dkind���aoa=���bs1a'���bs1emin_E���bs1a'���`a)���`a
���`nzi_cubic_min_E���`a ���aoa=���`a ���`rinterp_cubic_min_E���`a(���`bxi���`a,���`a ���`byi���`a)���`a
���`a
���bc1s# Set up the figure���`a
���`cfig���`a,���`a ���`caxs���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`enrows���aoa=���bmia2���`a,���`a ���`encols���aoa=���bmia2���`a)���`a
���`caxs���`a ���aoa=���`a ���`caxs���aoa.���`gflatten���`a(���`a)���`a
���`a
���bc1x# Plot the triangulation.���`a
���`caxs���`a[���bmia0���`a]���aoa.���`ktricontourf���`a(���`ftriang���`a,���`a ���`az���`a)���`a
���`caxs���`a[���bmia0���`a]���aoa.���`gtriplot���`a(���`ftriang���`a,���`a ���bs1a'���bs1cko-���bs1a'���`a)���`a
���`caxs���`a[���bmia0���`a]���aoa.���`iset_title���`a(���bs1a'���bs1oTriangular grid���bs1a'���`a)���`a
���`a
���bc1x)# Plot linear interpolation to quad grid.���`a
���`caxs���`a[���bmia1���`a]���aoa.���`hcontourf���`a(���`bxi���`a,���`a ���`byi���`a,���`a ���`fzi_lin���`a)���`a
���`caxs���`a[���bmia1���`a]���aoa.���`dplot���`a(���`bxi���`a,���`a ���`byi���`a,���`a ���bs1a'���bs1bk-���bs1a'���`a,���`a ���`blw���aoa=���bmfc0.5���`a,���`a ���`ealpha���aoa=���bmfc0.5���`a)���`a
���`caxs���`a[���bmia1���`a]���aoa.���`dplot���`a(���`bxi���aoa.���`aT���`a,���`a ���`byi���aoa.���`aT���`a,���`a ���bs1a'���bs1bk-���bs1a'���`a,���`a ���`blw���aoa=���bmfc0.5���`a,���`a ���`ealpha���aoa=���bmfc0.5���`a)���`a
���`caxs���`a[���bmia1���`a]���aoa.���`iset_title���`a(���bs2a"���bs2tLinear interpolation���bs2a"���`a)���`a
���`a
���bc1x2# Plot cubic interpolation to quad grid, kind=geom���`a
���`caxs���`a[���bmia2���`a]���aoa.���`hcontourf���`a(���`bxi���`a,���`a ���`byi���`a,���`a ���`mzi_cubic_geom���`a)���`a
���`caxs���`a[���bmia2���`a]���aoa.���`dplot���`a(���`bxi���`a,���`a ���`byi���`a,���`a ���bs1a'���bs1bk-���bs1a'���`a,���`a ���`blw���aoa=���bmfc0.5���`a,���`a ���`ealpha���aoa=���bmfc0.5���`a)���`a
���`caxs���`a[���bmia2���`a]���aoa.���`dplot���`a(���`bxi���aoa.���`aT���`a,���`a ���`byi���aoa.���`aT���`a,���`a ���bs1a'���bs1bk-���bs1a'���`a,���`a ���`blw���aoa=���bmfc0.5���`a,���`a ���`ealpha���aoa=���bmfc0.5���`a)���`a
���`caxs���`a[���bmia2���`a]���aoa.���`iset_title���`a(���bs2a"���bs2tCubic interpolation,���bseb\n���bs2ekind=���bs2a'���bs2dgeom���bs2a'���bs2a"���`a)���`a
���`a
���bc1x3# Plot cubic interpolation to quad grid, kind=min_E���`a
���`caxs���`a[���bmia3���`a]���aoa.���`hcontourf���`a(���`bxi���`a,���`a ���`byi���`a,���`a ���`nzi_cubic_min_E���`a)���`a
���`caxs���`a[���bmia3���`a]���aoa.���`dplot���`a(���`bxi���`a,���`a ���`byi���`a,���`a ���bs1a'���bs1bk-���bs1a'���`a,���`a ���`blw���aoa=���bmfc0.5���`a,���`a ���`ealpha���aoa=���bmfc0.5���`a)���`a
���`caxs���`a[���bmia3���`a]���aoa.���`dplot���`a(���`bxi���aoa.���`aT���`a,���`a ���`byi���aoa.���`aT���`a,���`a ���bs1a'���bs1bk-���bs1a'���`a,���`a ���`blw���aoa=���bmfc0.5���`a,���`a ���`ealpha���aoa=���bmfc0.5���`a)���`a
���`caxs���`a[���bmia3���`a]���aoa.���`iset_title���`a(���bs2a"���bs2tCubic interpolation,���bseb\n���bs2ekind=���bs2a'���bs2emin_E���bs2a'���bs2a"���`a)���`a
���`a
���`cfig���aoa.���`ltight_layout���`a(���`a)���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
���`a
���bc1xM#############################################################################���`a
���bc1a#���`a
���bc1x# .. admonition:: References���`a
���bc1a#���`a
���bc1xN#    The use of the following functions, methods, classes and modules is shown���`a
���bc1u#    in this example:���`a
���bc1a#���`a
���bc1xK#    - `matplotlib.axes.Axes.tricontourf` / `matplotlib.pyplot.tricontourf`���`a
���bc1xC#    - `matplotlib.axes.Axes.triplot` / `matplotlib.pyplot.triplot`���`a
���bc1xE#    - `matplotlib.axes.Axes.contourf` / `matplotlib.pyplot.contourf`���`a
���bc1x=#    - `matplotlib.axes.Axes.plot` / `matplotlib.pyplot.plot`���`a
���bc1w#    - `matplotlib.tri`���`a
���bc1x-#    - `matplotlib.tri.LinearTriInterpolator`���`a
���bc1x,#    - `matplotlib.tri.CubicTriInterpolator`���`a
���bc1x%#    - `matplotlib.tri.Triangulation`���`a
`dNone�