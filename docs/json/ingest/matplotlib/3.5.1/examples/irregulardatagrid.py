��������T���bsdy�"""
=======================================
Contour plot of irregularly spaced data
=======================================

Comparison of a contour plot of irregularly spaced data interpolated
on a regular grid versus a tricontour plot for an unstructured triangular grid.

Since `~.axes.Axes.contour` and `~.axes.Axes.contourf` expect the data to live
on a regular grid, plotting a contour plot of irregularly spaced data requires
different methods. The two options are:

* Interpolate the data to a regular grid first. This can be done with on-board
  means, e.g. via `~.tri.LinearTriInterpolator` or using external functionality
  e.g. via `scipy.interpolate.griddata`. Then plot the interpolated data with
  the usual `~.axes.Axes.contour`.
* Directly use `~.axes.Axes.tricontour` or `~.axes.Axes.tricontourf` which will
  perform a triangulation internally.

This example shows both methods in action.
"""���`a
���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnctri���`a ���akbas���`a ���bnnctri���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���`a
���`bnp���aoa.���`frandom���aoa.���`dseed���`a(���bmih19680801���`a)���`a
���`dnpts���`a ���aoa=���`a ���bmic200���`a
���`fngridx���`a ���aoa=���`a ���bmic100���`a
���`fngridy���`a ���aoa=���`a ���bmic200���`a
���`ax���`a ���aoa=���`a ���`bnp���aoa.���`frandom���aoa.���`guniform���`a(���aoa-���bmia2���`a,���`a ���bmia2���`a,���`a ���`dnpts���`a)���`a
���`ay���`a ���aoa=���`a ���`bnp���aoa.���`frandom���aoa.���`guniform���`a(���aoa-���bmia2���`a,���`a ���bmia2���`a,���`a ���`dnpts���`a)���`a
���`az���`a ���aoa=���`a ���`ax���`a ���aoa*���`a ���`bnp���aoa.���`cexp���`a(���aoa-���`ax���aoa*���aoa*���bmia2���`a ���aoa-���`a ���`ay���aoa*���aoa*���bmia2���`a)���`a
���`a
���`cfig���`a,���`a ���`a(���`cax1���`a,���`a ���`cax2���`a)���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`enrows���aoa=���bmia2���`a)���`a
���`a
���bc1x# -----------------------���`a
���bc1x# Interpolation on a grid���`a
���bc1x# -----------------------���`a
���bc1x7# A contour plot of irregularly spaced data coordinates���`a
���bc1x# via interpolation on a grid.���`a
���`a
���bc1x# Create grid values first.���`a
���`bxi���`a ���aoa=���`a ���`bnp���aoa.���`hlinspace���`a(���aoa-���bmfc2.1���`a,���`a ���bmfc2.1���`a,���`a ���`fngridx���`a)���`a
���`byi���`a ���aoa=���`a ���`bnp���aoa.���`hlinspace���`a(���aoa-���bmfc2.1���`a,���`a ���bmfc2.1���`a,���`a ���`fngridy���`a)���`a
���`a
���bc1xE# Linearly interpolate the data (x, y) on a grid defined by (xi, yi).���`a
���`ftriang���`a ���aoa=���`a ���`ctri���aoa.���`mTriangulation���`a(���`ax���`a,���`a ���`ay���`a)���`a
���`linterpolator���`a ���aoa=���`a ���`ctri���aoa.���`uLinearTriInterpolator���`a(���`ftriang���`a,���`a ���`az���`a)���`a
���`bXi���`a,���`a ���`bYi���`a ���aoa=���`a ���`bnp���aoa.���`hmeshgrid���`a(���`bxi���`a,���`a ���`byi���`a)���`a
���`bzi���`a ���aoa=���`a ���`linterpolator���`a(���`bXi���`a,���`a ���`bYi���`a)���`a
���`a
���bc1xJ# Note that scipy.interpolate provides means to interpolate data on a grid���`a
���bc1xI# as well. The following would be an alternative to the four lines above:���`a
���bc1x(# from scipy.interpolate import griddata���`a
���bc1xG# zi = griddata((x, y), z, (xi[None, :], yi[:, None]), method='linear')���`a
���`a
���`cax1���aoa.���`gcontour���`a(���`bxi���`a,���`a ���`byi���`a,���`a ���`bzi���`a,���`a ���`flevels���aoa=���bmib14���`a,���`a ���`jlinewidths���aoa=���bmfc0.5���`a,���`a ���`fcolors���aoa=���bs1a'���bs1ak���bs1a'���`a)���`a
���`ecntr1���`a ���aoa=���`a ���`cax1���aoa.���`hcontourf���`a(���`bxi���`a,���`a ���`byi���`a,���`a ���`bzi���`a,���`a ���`flevels���aoa=���bmib14���`a,���`a ���`dcmap���aoa=���bs2a"���bs2fRdBu_r���bs2a"���`a)���`a
���`a
���`cfig���aoa.���`hcolorbar���`a(���`ecntr1���`a,���`a ���`bax���aoa=���`cax1���`a)���`a
���`cax1���aoa.���`dplot���`a(���`ax���`a,���`a ���`ay���`a,���`a ���bs1a'���bs1bko���bs1a'���`a,���`a ���`bms���aoa=���bmia3���`a)���`a
���`cax1���aoa.���`cset���`a(���`dxlim���aoa=���`a(���aoa-���bmia2���`a,���`a ���bmia2���`a)���`a,���`a ���`dylim���aoa=���`a(���aoa-���bmia2���`a,���`a ���bmia2���`a)���`a)���`a
���`cax1���aoa.���`iset_title���`a(���bs1a'���bs1rgrid and contour (���bsib%d���bs1i points, ���bsib%d���bs1m grid points)���bs1a'���`a ���aoa%���`a
���`n              ���`a(���`dnpts���`a,���`a ���`fngridx���`a ���aoa*���`a ���`fngridy���`a)���`a)���`a
���`a
���bc1l# ----------���`a
���bc1l# Tricontour���`a
���bc1l# ----------���`a
���bc1x?# Directly supply the unordered, irregularly spaced coordinates���`a
���bc1p# to tricontour.���`a
���`a
���`cax2���aoa.���`jtricontour���`a(���`ax���`a,���`a ���`ay���`a,���`a ���`az���`a,���`a ���`flevels���aoa=���bmib14���`a,���`a ���`jlinewidths���aoa=���bmfc0.5���`a,���`a ���`fcolors���aoa=���bs1a'���bs1ak���bs1a'���`a)���`a
���`ecntr2���`a ���aoa=���`a ���`cax2���aoa.���`ktricontourf���`a(���`ax���`a,���`a ���`ay���`a,���`a ���`az���`a,���`a ���`flevels���aoa=���bmib14���`a,���`a ���`dcmap���aoa=���bs2a"���bs2fRdBu_r���bs2a"���`a)���`a
���`a
���`cfig���aoa.���`hcolorbar���`a(���`ecntr2���`a,���`a ���`bax���aoa=���`cax2���`a)���`a
���`cax2���aoa.���`dplot���`a(���`ax���`a,���`a ���`ay���`a,���`a ���bs1a'���bs1bko���bs1a'���`a,���`a ���`bms���aoa=���bmia3���`a)���`a
���`cax2���aoa.���`cset���`a(���`dxlim���aoa=���`a(���aoa-���bmia2���`a,���`a ���bmia2���`a)���`a,���`a ���`dylim���aoa=���`a(���aoa-���bmia2���`a,���`a ���bmia2���`a)���`a)���`a
���`cax2���aoa.���`iset_title���`a(���bs1a'���bs1ltricontour (���bsib%d���bs1h points)���bs1a'���`a ���aoa%���`a ���`dnpts���`a)���`a
���`a
���`cplt���aoa.���`osubplots_adjust���`a(���`fhspace���aoa=���bmfc0.5���`a)���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
���`a
���bc1xM#############################################################################���`a
���bc1a#���`a
���bc1x# .. admonition:: References���`a
���bc1a#���`a
���bc1xN#    The use of the following functions, methods, classes and modules is shown���`a
���bc1u#    in this example:���`a
���bc1a#���`a
���bc1xC#    - `matplotlib.axes.Axes.contour` / `matplotlib.pyplot.contour`���`a
���bc1xE#    - `matplotlib.axes.Axes.contourf` / `matplotlib.pyplot.contourf`���`a
���bc1xI#    - `matplotlib.axes.Axes.tricontour` / `matplotlib.pyplot.tricontour`���`a
���bc1xK#    - `matplotlib.axes.Axes.tricontourf` / `matplotlib.pyplot.tricontourf`���`a
`dNone�