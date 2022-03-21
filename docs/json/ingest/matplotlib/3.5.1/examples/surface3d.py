�����������bsdy%"""
=====================
3D surface (colormap)
=====================

Demonstrates plotting a 3D surface colored with the coolwarm colormap.
The surface is made opaque by using antialiased=False.

Also demonstrates using the LinearLocator and custom formatting for the
z axis tick labels.
"""���`a
���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���bkndfrom���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����`a ���bknfimport���`a ���`bcm���`a
���bkndfrom���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfticker���`a ���bknfimport���`a ���`mLinearLocator���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���`a
���`cfig���`a,���`a ���`bax���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`jsubplot_kw���aoa=���`a{���bs2a"���bs2jprojection���bs2a"���`a:���`a ���bs2a"���bs2b3d���bs2a"���`a}���`a)���`a
���`a
���bc1l# Make data.���`a
���`aX���`a ���aoa=���`a ���`bnp���aoa.���`farange���`a(���aoa-���bmia5���`a,���`a ���bmia5���`a,���`a ���bmfd0.25���`a)���`a
���`aY���`a ���aoa=���`a ���`bnp���aoa.���`farange���`a(���aoa-���bmia5���`a,���`a ���bmia5���`a,���`a ���bmfd0.25���`a)���`a
���`aX���`a,���`a ���`aY���`a ���aoa=���`a ���`bnp���aoa.���`hmeshgrid���`a(���`aX���`a,���`a ���`aY���`a)���`a
���`aR���`a ���aoa=���`a ���`bnp���aoa.���`dsqrt���`a(���`aX���aoa*���aoa*���bmia2���`a ���aoa+���`a ���`aY���aoa*���aoa*���bmia2���`a)���`a
���`aZ���`a ���aoa=���`a ���`bnp���aoa.���`csin���`a(���`aR���`a)���`a
���`a
���bc1s# Plot the surface.���`a
���`dsurf���`a ���aoa=���`a ���`bax���aoa.���`lplot_surface���`a(���`aX���`a,���`a ���`aY���`a,���`a ���`aZ���`a,���`a ���`dcmap���aoa=���`bcm���aoa.���`hcoolwarm���`a,���`a
���`w                       ���`ilinewidth���aoa=���bmia0���`a,���`a ���`kantialiased���aoa=���bkceFalse���`a)���`a
���`a
���bc1w# Customize the z axis.���`a
���`bax���aoa.���`hset_zlim���`a(���aoa-���bmfd1.01���`a,���`a ���bmfd1.01���`a)���`a
���`bax���aoa.���`ezaxis���aoa.���`qset_major_locator���`a(���`mLinearLocator���`a(���bmib10���`a)���`a)���`a
���bc1x,# A StrMethodFormatter is used automatically���`a
���`bax���aoa.���`ezaxis���aoa.���`sset_major_formatter���`a(���bs1a'���bsih{x:.02f}���bs1a'���`a)���`a
���`a
���bc1x.# Add a color bar which maps values to colors.���`a
���`cfig���aoa.���`hcolorbar���`a(���`dsurf���`a,���`a ���`fshrink���aoa=���bmfc0.5���`a,���`a ���`faspect���aoa=���bmia5���`a)���`a
���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
���`a
���`a
���bc1xM#############################################################################���`a
���bc1a#���`a
���bc1x# .. admonition:: References���`a
���bc1a#���`a
���bc1xN#    The use of the following functions, methods, classes and modules is shown���`a
���bc1u#    in this example:���`a
���bc1a#���`a
���bc1x##    - `matplotlib.pyplot.subplots`���`a
���bc1x1#    - `matplotlib.axis.Axis.set_major_formatter`���`a
���bc1x/#    - `matplotlib.axis.Axis.set_major_locator`���`a
���bc1x(#    - `matplotlib.ticker.LinearLocator`���`a
���bc1x-#    - `matplotlib.ticker.StrMethodFormatter`���`a
`dNone�