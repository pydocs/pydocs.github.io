������������bsdx�"""
==========
pcolormesh
==========

`.axes.Axes.pcolormesh` allows you to generate 2D image-style plots.  Note it
is faster than the similar `~.axes.Axes.pcolor`.

"""���`a
���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���bkndfrom���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfcolors���`a ���bknfimport���`a ���`lBoundaryNorm���`a
���bkndfrom���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfticker���`a ���bknfimport���`a ���`kMaxNLocator���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���`a
���bc1xO###############################################################################���`a
���bc1r# Basic pcolormesh���`a
���bc1r# ----------------���`a
���bc1a#���`a
���bc1xL# We usually specify a pcolormesh by defining the edge of quadrilaterals and���`a
���bc1xK# the value of the quadrilateral.  Note that here *x* and *y* each have one���`a
���bc1x3# extra element than Z in the respective dimension.���`a
���`a
���`bnp���aoa.���`frandom���aoa.���`dseed���`a(���bmih19680801���`a)���`a
���`aZ���`a ���aoa=���`a ���`bnp���aoa.���`frandom���aoa.���`drand���`a(���bmia6���`a,���`a ���bmib10���`a)���`a
���`ax���`a ���aoa=���`a ���`bnp���aoa.���`farange���`a(���aoa-���bmfc0.5���`a,���`a ���bmib10���`a,���`a ���bmia1���`a)���`b  ���bc1j# len = 11���`a
���`ay���`a ���aoa=���`a ���`bnp���aoa.���`farange���`a(���bmfc4.5���`a,���`a ���bmib11���`a,���`a ���bmia1���`a)���`b  ���bc1i# len = 7���`a
���`a
���`cfig���`a,���`a ���`bax���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`a)���`a
���`bax���aoa.���`jpcolormesh���`a(���`ax���`a,���`a ���`ay���`a,���`a ���`aZ���`a)���`a
���`a
���bc1xO###############################################################################���`a
���bc1x# Non-rectilinear pcolormesh���`a
���bc1x# --------------------------���`a
���bc1a#���`a
���bc1xA# Note that we can also specify matrices for *X* and *Y* and have���`a
���bc1x!# non-rectilinear quadrilaterals.���`a
���`a
���`ax���`a ���aoa=���`a ���`bnp���aoa.���`farange���`a(���aoa-���bmfc0.5���`a,���`a ���bmib10���`a,���`a ���bmia1���`a)���`b  ���bc1j# len = 11���`a
���`ay���`a ���aoa=���`a ���`bnp���aoa.���`farange���`a(���bmfc4.5���`a,���`a ���bmib11���`a,���`a ���bmia1���`a)���`b  ���bc1i# len = 7���`a
���`aX���`a,���`a ���`aY���`a ���aoa=���`a ���`bnp���aoa.���`hmeshgrid���`a(���`ax���`a,���`a ���`ay���`a)���`a
���`aX���`a ���aoa=���`a ���`aX���`a ���aoa+���`a ���bmfc0.2���`a ���aoa*���`a ���`aY���`b  ���bc1w# tilt the coordinates.���`a
���`aY���`a ���aoa=���`a ���`aY���`a ���aoa+���`a ���bmfc0.3���`a ���aoa*���`a ���`aX���`a
���`a
���`cfig���`a,���`a ���`bax���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`a)���`a
���`bax���aoa.���`jpcolormesh���`a(���`aX���`a,���`a ���`aY���`a,���`a ���`aZ���`a)���`a
���`a
���bc1xO###############################################################################���`a
���bc1v# Centered Coordinates���`a
���bc1w# ---------------------���`a
���bc1a#���`a
���bc1xF# Often a user wants to pass *X* and *Y* with the same sizes as *Z* to���`a
���bc1xH# `.axes.Axes.pcolormesh`. This is also allowed if ``shading='auto'`` is���`a
���bc1xC# passed (default set by :rc:`pcolor.shading`). Pre Matplotlib 3.3,���`a
���bc1xJ# ``shading='flat'`` would drop the last column and row of *Z*; while that���`a
���bc1xK# is still allowed for back compatibility purposes, a DeprecationWarning is���`a
���bc1xL# raised. If this is really what you want, then simply drop the last row and���`a
���bc1w# column of Z manually:���`a
���`a
���`ax���`a ���aoa=���`a ���`bnp���aoa.���`farange���`a(���bmib10���`a)���`b  ���bc1j# len = 10���`a
���`ay���`a ���aoa=���`a ���`bnp���aoa.���`farange���`a(���bmia6���`a)���`b  ���bc1i# len = 6���`a
���`aX���`a,���`a ���`aY���`a ���aoa=���`a ���`bnp���aoa.���`hmeshgrid���`a(���`ax���`a,���`a ���`ay���`a)���`a
���`a
���`cfig���`a,���`a ���`caxs���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���bmia2���`a,���`a ���bmia1���`a,���`a ���`fsharex���aoa=���bkcdTrue���`a,���`a ���`fsharey���aoa=���bkcdTrue���`a)���`a
���`caxs���`a[���bmia0���`a]���aoa.���`jpcolormesh���`a(���`aX���`a,���`a ���`aY���`a,���`a ���`aZ���`a,���`a ���`dvmin���aoa=���`bnp���aoa.���`cmin���`a(���`aZ���`a)���`a,���`a ���`dvmax���aoa=���`bnp���aoa.���`cmax���`a(���`aZ���`a)���`a,���`a ���`gshading���aoa=���bs1a'���bs1dauto���bs1a'���`a)���`a
���`caxs���`a[���bmia0���`a]���aoa.���`iset_title���`a(���bs2a"���bs2hshading=���bs2a'���bs2dauto���bs2a'���bs2c = ���bs2a'���bs2gnearest���bs2a'���bs2a"���`a)���`a
���`caxs���`a[���bmia1���`a]���aoa.���`jpcolormesh���`a(���`aX���`a,���`a ���`aY���`a,���`a ���`aZ���`a[���`a:���aoa-���bmia1���`a,���`a ���`a:���aoa-���bmia1���`a]���`a,���`a ���`dvmin���aoa=���`bnp���aoa.���`cmin���`a(���`aZ���`a)���`a,���`a ���`dvmax���aoa=���`bnp���aoa.���`cmax���`a(���`aZ���`a)���`a,���`a
���`r                  ���`gshading���aoa=���bs1a'���bs1dflat���bs1a'���`a)���`a
���`caxs���`a[���bmia1���`a]���aoa.���`iset_title���`a(���bs2a"���bs2hshading=���bs2a'���bs2dflat���bs2a'���bs2a"���`a)���`a
���`a
���bc1xO###############################################################################���`a
���bc1x# Making levels using Norms���`a
���bc1x# -------------------------���`a
���bc1a#���`a
���bc1xC# Shows how to combine Normalization and Colormap instances to draw���`a
���bc1x:# "levels" in `.axes.Axes.pcolor`, `.axes.Axes.pcolormesh`���`a
���bc1x1# and `.axes.Axes.imshow` type plots in a similar���`a
���bc1x9# way to the levels keyword argument to contour/contourf.���`a
���`a
���bc1x/# make these smaller to increase the resolution���`a
���`bdx���`a,���`a ���`bdy���`a ���aoa=���`a ���bmfd0.05���`a,���`a ���bmfd0.05���`a
���`a
���bc1x*# generate 2 2d grids for the x & y bounds���`a
���`ay���`a,���`a ���`ax���`a ���aoa=���`a ���`bnp���aoa.���`emgrid���`a[���bnbeslice���`a(���bmia1���`a,���`a ���bmia5���`a ���aoa+���`a ���`bdy���`a,���`a ���`bdy���`a)���`a,���`a
���`p                ���bnbeslice���`a(���bmia1���`a,���`a ���bmia5���`a ���aoa+���`a ���`bdx���`a,���`a ���`bdx���`a)���`a]���`a
���`a
���`az���`a ���aoa=���`a ���`bnp���aoa.���`csin���`a(���`ax���`a)���aoa*���aoa*���bmib10���`a ���aoa+���`a ���`bnp���aoa.���`ccos���`a(���bmib10���`a ���aoa+���`a ���`ay���aoa*���`ax���`a)���`a ���aoa*���`a ���`bnp���aoa.���`ccos���`a(���`ax���`a)���`a
���`a
���bc1xE# x and y are bounds, so z should be the value *inside* those bounds.���`a
���bc1x4# Therefore, remove the last value from the z array.���`a
���`az���`a ���aoa=���`a ���`az���`a[���`a:���aoa-���bmia1���`a,���`a ���`a:���aoa-���bmia1���`a]���`a
���`flevels���`a ���aoa=���`a ���`kMaxNLocator���`a(���`enbins���aoa=���bmib15���`a)���aoa.���`ktick_values���`a(���`az���aoa.���`cmin���`a(���`a)���`a,���`a ���`az���aoa.���`cmax���`a(���`a)���`a)���`a
���`a
���`a
���bc1xH# pick the desired colormap, sensible levels, and define a normalization���`a
���bc1xD# instance which takes data values and translates those into levels.���`a
���`dcmap���`a ���aoa=���`a ���`cplt���aoa.���`icolormaps���`a[���bs1a'���bs1dPiYG���bs1a'���`a]���`a
���`dnorm���`a ���aoa=���`a ���`lBoundaryNorm���`a(���`flevels���`a,���`a ���`gncolors���aoa=���`dcmap���aoa.���`aN���`a,���`a ���`dclip���aoa=���bkcdTrue���`a)���`a
���`a
���`cfig���`a,���`a ���`a(���`cax0���`a,���`a ���`cax1���`a)���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`enrows���aoa=���bmia2���`a)���`a
���`a
���`bim���`a ���aoa=���`a ���`cax0���aoa.���`jpcolormesh���`a(���`ax���`a,���`a ���`ay���`a,���`a ���`az���`a,���`a ���`dcmap���aoa=���`dcmap���`a,���`a ���`dnorm���aoa=���`dnorm���`a)���`a
���`cfig���aoa.���`hcolorbar���`a(���`bim���`a,���`a ���`bax���aoa=���`cax0���`a)���`a
���`cax0���aoa.���`iset_title���`a(���bs1a'���bs1vpcolormesh with levels���bs1a'���`a)���`a
���`a
���`a
���bc1xC# contours are *point* based plots, so convert our bound into point���`a
���bc1i# centers���`a
���`bcf���`a ���aoa=���`a ���`cax1���aoa.���`hcontourf���`a(���`ax���`a[���`a:���aoa-���bmia1���`a,���`a ���`a:���aoa-���bmia1���`a]���`a ���aoa+���`a ���`bdx���aoa/���bmfb2.���`a,���`a
���`r                  ���`ay���`a[���`a:���aoa-���bmia1���`a,���`a ���`a:���aoa-���bmia1���`a]���`a ���aoa+���`a ���`bdy���aoa/���bmfb2.���`a,���`a ���`az���`a,���`a ���`flevels���aoa=���`flevels���`a,���`a
���`r                  ���`dcmap���aoa=���`dcmap���`a)���`a
���`cfig���aoa.���`hcolorbar���`a(���`bcf���`a,���`a ���`bax���aoa=���`cax1���`a)���`a
���`cax1���aoa.���`iset_title���`a(���bs1a'���bs1tcontourf with levels���bs1a'���`a)���`a
���`a
���bc1xF# adjust spacing between subplots so `ax1` title and `ax0` tick labels���`a
���bc1o# don't overlap���`a
���`cfig���aoa.���`ltight_layout���`a(���`a)���`a
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
���bc1xI#    - `matplotlib.axes.Axes.pcolormesh` / `matplotlib.pyplot.pcolormesh`���`a
���bc1xE#    - `matplotlib.axes.Axes.contourf` / `matplotlib.pyplot.contourf`���`a
���bc1xI#    - `matplotlib.figure.Figure.colorbar` / `matplotlib.pyplot.colorbar`���`a
���bc1x'#    - `matplotlib.colors.BoundaryNorm`���`a
���bc1x&#    - `matplotlib.ticker.MaxNLocator`���`a
`dNone�