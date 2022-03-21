������������bsdx�"""
===========
Pcolor Demo
===========

Generating images with `~.axes.Axes.pcolor`.

Pcolor allows you to generate 2D image-style plots. Below we will show how
to do so in Matplotlib.
"""���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���bkndfrom���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfcolors���`a ���bknfimport���`a ���`gLogNorm���`a
���`a
���`a
���bc1x)# Fixing random state for reproducibility���`a
���`bnp���aoa.���`frandom���aoa.���`dseed���`a(���bmih19680801���`a)���`a
���`a
���bc1xO###############################################################################���`a
���bc1v# A simple pcolor demo���`a
���bc1v# --------------------���`a
���`a
���`aZ���`a ���aoa=���`a ���`bnp���aoa.���`frandom���aoa.���`drand���`a(���bmia6���`a,���`a ���bmib10���`a)���`a
���`a
���`cfig���`a,���`a ���`a(���`cax0���`a,���`a ���`cax1���`a)���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���bmia2���`a,���`a ���bmia1���`a)���`a
���`a
���`ac���`a ���aoa=���`a ���`cax0���aoa.���`fpcolor���`a(���`aZ���`a)���`a
���`cax0���aoa.���`iset_title���`a(���bs1a'���bs1qdefault: no edges���bs1a'���`a)���`a
���`a
���`ac���`a ���aoa=���`a ���`cax1���aoa.���`fpcolor���`a(���`aZ���`a,���`a ���`jedgecolors���aoa=���bs1a'���bs1ak���bs1a'���`a,���`a ���`jlinewidths���aoa=���bmia4���`a)���`a
���`cax1���aoa.���`iset_title���`a(���bs1a'���bs1kthick edges���bs1a'���`a)���`a
���`a
���`cfig���aoa.���`ltight_layout���`a(���`a)���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
���`a
���bc1xO###############################################################################���`a
���bc1x)# Comparing pcolor with similar functions���`a
���bc1x)# ---------------------------------------���`a
���bc1a#���`a
���bc1x9# Demonstrates similarities between `~.axes.Axes.pcolor`,���`a
���bc1x4# `~.axes.Axes.pcolormesh`, `~.axes.Axes.imshow` and���`a
���bc1x;# `~.axes.Axes.pcolorfast` for drawing quadrilateral grids.���`a
���bc1xN# Note that we call ``imshow`` with ``aspect="auto"`` so that it doesn't force���`a
���bc1xC# the data pixels to be square (the default is ``aspect="equal"``).���`a
���`a
���bc1x/# make these smaller to increase the resolution���`a
���`bdx���`a,���`a ���`bdy���`a ���aoa=���`a ���bmfd0.15���`a,���`a ���bmfd0.05���`a
���`a
���bc1x*# generate 2 2d grids for the x & y bounds���`a
���`ay���`a,���`a ���`ax���`a ���aoa=���`a ���`bnp���aoa.���`emgrid���`a[���aoa-���bmia3���`a:���bmia3���aoa+���`bdy���`a:���`bdy���`a,���`a ���aoa-���bmia3���`a:���bmia3���aoa+���`bdx���`a:���`bdx���`a]���`a
���`az���`a ���aoa=���`a ���`a(���bmia1���`a ���aoa-���`a ���`ax���aoa/���bmia2���`a ���aoa+���`a ���`ax���aoa*���aoa*���bmia5���`a ���aoa+���`a ���`ay���aoa*���aoa*���bmia3���`a)���`a ���aoa*���`a ���`bnp���aoa.���`cexp���`a(���aoa-���`ax���aoa*���aoa*���bmia2���`a ���aoa-���`a ���`ay���aoa*���aoa*���bmia2���`a)���`a
���bc1xE# x and y are bounds, so z should be the value *inside* those bounds.���`a
���bc1x4# Therefore, remove the last value from the z array.���`a
���`az���`a ���aoa=���`a ���`az���`a[���`a:���aoa-���bmia1���`a,���`a ���`a:���aoa-���bmia1���`a]���`a
���`ez_min���`a,���`a ���`ez_max���`a ���aoa=���`a ���aoa-���bnbcabs���`a(���`az���`a)���aoa.���`cmax���`a(���`a)���`a,���`a ���bnbcabs���`a(���`az���`a)���aoa.���`cmax���`a(���`a)���`a
���`a
���`cfig���`a,���`a ���`caxs���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���bmia2���`a,���`a ���bmia2���`a)���`a
���`a
���`bax���`a ���aoa=���`a ���`caxs���`a[���bmia0���`a,���`a ���bmia0���`a]���`a
���`ac���`a ���aoa=���`a ���`bax���aoa.���`fpcolor���`a(���`ax���`a,���`a ���`ay���`a,���`a ���`az���`a,���`a ���`dcmap���aoa=���bs1a'���bs1dRdBu���bs1a'���`a,���`a ���`dvmin���aoa=���`ez_min���`a,���`a ���`dvmax���aoa=���`ez_max���`a)���`a
���`bax���aoa.���`iset_title���`a(���bs1a'���bs1fpcolor���bs1a'���`a)���`a
���`cfig���aoa.���`hcolorbar���`a(���`ac���`a,���`a ���`bax���aoa=���`bax���`a)���`a
���`a
���`bax���`a ���aoa=���`a ���`caxs���`a[���bmia0���`a,���`a ���bmia1���`a]���`a
���`ac���`a ���aoa=���`a ���`bax���aoa.���`jpcolormesh���`a(���`ax���`a,���`a ���`ay���`a,���`a ���`az���`a,���`a ���`dcmap���aoa=���bs1a'���bs1dRdBu���bs1a'���`a,���`a ���`dvmin���aoa=���`ez_min���`a,���`a ���`dvmax���aoa=���`ez_max���`a)���`a
���`bax���aoa.���`iset_title���`a(���bs1a'���bs1jpcolormesh���bs1a'���`a)���`a
���`cfig���aoa.���`hcolorbar���`a(���`ac���`a,���`a ���`bax���aoa=���`bax���`a)���`a
���`a
���`bax���`a ���aoa=���`a ���`caxs���`a[���bmia1���`a,���`a ���bmia0���`a]���`a
���`ac���`a ���aoa=���`a ���`bax���aoa.���`fimshow���`a(���`az���`a,���`a ���`dcmap���aoa=���bs1a'���bs1dRdBu���bs1a'���`a,���`a ���`dvmin���aoa=���`ez_min���`a,���`a ���`dvmax���aoa=���`ez_max���`a,���`a
���`n              ���`fextent���aoa=���`a[���`ax���aoa.���`cmin���`a(���`a)���`a,���`a ���`ax���aoa.���`cmax���`a(���`a)���`a,���`a ���`ay���aoa.���`cmin���`a(���`a)���`a,���`a ���`ay���aoa.���`cmax���`a(���`a)���`a]���`a,���`a
���`n              ���`minterpolation���aoa=���bs1a'���bs1gnearest���bs1a'���`a,���`a ���`forigin���aoa=���bs1a'���bs1elower���bs1a'���`a,���`a ���`faspect���aoa=���bs1a'���bs1dauto���bs1a'���`a)���`a
���`bax���aoa.���`iset_title���`a(���bs1a'���bs1wimage (nearest, aspect=���bs1a"���bs1dauto���bs1a"���bs1a)���bs1a'���`a)���`a
���`cfig���aoa.���`hcolorbar���`a(���`ac���`a,���`a ���`bax���aoa=���`bax���`a)���`a
���`a
���`bax���`a ���aoa=���`a ���`caxs���`a[���bmia1���`a,���`a ���bmia1���`a]���`a
���`ac���`a ���aoa=���`a ���`bax���aoa.���`jpcolorfast���`a(���`ax���`a,���`a ���`ay���`a,���`a ���`az���`a,���`a ���`dcmap���aoa=���bs1a'���bs1dRdBu���bs1a'���`a,���`a ���`dvmin���aoa=���`ez_min���`a,���`a ���`dvmax���aoa=���`ez_max���`a)���`a
���`bax���aoa.���`iset_title���`a(���bs1a'���bs1jpcolorfast���bs1a'���`a)���`a
���`cfig���aoa.���`hcolorbar���`a(���`ac���`a,���`a ���`bax���aoa=���`bax���`a)���`a
���`a
���`cfig���aoa.���`ltight_layout���`a(���`a)���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
���`a
���`a
���bc1xO###############################################################################���`a
���bc1x# Pcolor with a log scale���`a
���bc1x# -----------------------���`a
���bc1a#���`a
���bc1x4# The following shows pcolor plots with a log scale.���`a
���`a
���`aN���`a ���aoa=���`a ���bmic100���`a
���`aX���`a,���`a ���`aY���`a ���aoa=���`a ���`bnp���aoa.���`hmeshgrid���`a(���`bnp���aoa.���`hlinspace���`a(���aoa-���bmia3���`a,���`a ���bmia3���`a,���`a ���`aN���`a)���`a,���`a ���`bnp���aoa.���`hlinspace���`a(���aoa-���bmia2���`a,���`a ���bmia2���`a,���`a ���`aN���`a)���`a)���`a
���`a
���bc1x%# A low hump with a spike coming out.���`a
���bc1xK# Needs to have z/colour axis on a log scale so we see both hump and spike.���`a
���bc1x$# linear scale only shows the spike.���`a
���`bZ1���`a ���aoa=���`a ���`bnp���aoa.���`cexp���`a(���aoa-���`aX���aoa*���aoa*���bmia2���`a ���aoa-���`a ���`aY���aoa*���aoa*���bmia2���`a)���`a
���`bZ2���`a ���aoa=���`a ���`bnp���aoa.���`cexp���`a(���aoa-���`a(���`aX���`a ���aoa*���`a ���bmib10���`a)���aoa*���aoa*���bmia2���`a ���aoa-���`a ���`a(���`aY���`a ���aoa*���`a ���bmib10���`a)���aoa*���aoa*���bmia2���`a)���`a
���`aZ���`a ���aoa=���`a ���`bZ1���`a ���aoa+���`a ���bmib50���`a ���aoa*���`a ���`bZ2���`a
���`a
���`cfig���`a,���`a ���`a(���`cax0���`a,���`a ���`cax1���`a)���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���bmia2���`a,���`a ���bmia1���`a)���`a
���`a
���`ac���`a ���aoa=���`a ���`cax0���aoa.���`fpcolor���`a(���`aX���`a,���`a ���`aY���`a,���`a ���`aZ���`a,���`a ���`gshading���aoa=���bs1a'���bs1dauto���bs1a'���`a,���`a
���`o               ���`dnorm���aoa=���`gLogNorm���`a(���`dvmin���aoa=���`aZ���aoa.���`cmin���`a(���`a)���`a,���`a ���`dvmax���aoa=���`aZ���aoa.���`cmax���`a(���`a)���`a)���`a,���`a ���`dcmap���aoa=���bs1a'���bs1fPuBu_r���bs1a'���`a)���`a
���`cfig���aoa.���`hcolorbar���`a(���`ac���`a,���`a ���`bax���aoa=���`cax0���`a)���`a
���`a
���`ac���`a ���aoa=���`a ���`cax1���aoa.���`fpcolor���`a(���`aX���`a,���`a ���`aY���`a,���`a ���`aZ���`a,���`a ���`dcmap���aoa=���bs1a'���bs1fPuBu_r���bs1a'���`a,���`a ���`gshading���aoa=���bs1a'���bs1dauto���bs1a'���`a)���`a
���`cfig���aoa.���`hcolorbar���`a(���`ac���`a,���`a ���`bax���aoa=���`cax1���`a)���`a
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
���bc1xA#    - `matplotlib.axes.Axes.pcolor` / `matplotlib.pyplot.pcolor`���`a
���bc1xI#    - `matplotlib.axes.Axes.pcolormesh` / `matplotlib.pyplot.pcolormesh`���`a
���bc1x(#    - `matplotlib.axes.Axes.pcolorfast`���`a
���bc1xA#    - `matplotlib.axes.Axes.imshow` / `matplotlib.pyplot.imshow`���`a
���bc1xI#    - `matplotlib.figure.Figure.colorbar` / `matplotlib.pyplot.colorbar`���`a
���bc1x"#    - `matplotlib.colors.LogNorm`���`a
`dNone�