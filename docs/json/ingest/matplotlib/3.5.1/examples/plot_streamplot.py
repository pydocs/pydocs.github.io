��������	���bsdy�"""
==========
Streamplot
==========

A stream plot, or streamline plot, is used to display 2D vector fields. This
example shows a few features of the `~.axes.Axes.streamplot` function:

* Varying the color along a streamline.
* Varying the density of streamlines.
* Varying the line width along a streamline.
* Controlling the starting points of streamlines.
* Streamlines skipping masked regions and NaN values.
"""���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnhgridspec���`a ���akbas���`a ���bnnhgridspec���`a
���`a
���`aw���`a ���aoa=���`a ���bmia3���`a
���`aY���`a,���`a ���`aX���`a ���aoa=���`a ���`bnp���aoa.���`emgrid���`a[���aoa-���`aw���`a:���`aw���`a:���bmic100���`aj���`a,���`a ���aoa-���`aw���`a:���`aw���`a:���bmic100���`aj���`a]���`a
���`aU���`a ���aoa=���`a ���aoa-���bmia1���`a ���aoa-���`a ���`aX���aoa*���aoa*���bmia2���`a ���aoa+���`a ���`aY���`a
���`aV���`a ���aoa=���`a ���bmia1���`a ���aoa+���`a ���`aX���`a ���aoa-���`a ���`aY���aoa*���aoa*���bmia2���`a
���`espeed���`a ���aoa=���`a ���`bnp���aoa.���`dsqrt���`a(���`aU���aoa*���aoa*���bmia2���`a ���aoa+���`a ���`aV���aoa*���aoa*���bmia2���`a)���`a
���`a
���`cfig���`a ���aoa=���`a ���`cplt���aoa.���`ffigure���`a(���`gfigsize���aoa=���`a(���bmia7���`a,���`a ���bmia9���`a)���`a)���`a
���`bgs���`a ���aoa=���`a ���`hgridspec���aoa.���`hGridSpec���`a(���`enrows���aoa=���bmia3���`a,���`a ���`encols���aoa=���bmia2���`a,���`a ���`mheight_ratios���aoa=���`a[���bmia1���`a,���`a ���bmia1���`a,���`a ���bmia2���`a]���`a)���`a
���`a
���bc1x%#  Varying density along a streamline���`a
���`cax0���`a ���aoa=���`a ���`cfig���aoa.���`kadd_subplot���`a(���`bgs���`a[���bmia0���`a,���`a ���bmia0���`a]���`a)���`a
���`cax0���aoa.���`jstreamplot���`a(���`aX���`a,���`a ���`aY���`a,���`a ���`aU���`a,���`a ���`aV���`a,���`a ���`gdensity���aoa=���`a[���bmfc0.5���`a,���`a ���bmia1���`a]���`a)���`a
���`cax0���aoa.���`iset_title���`a(���bs1a'���bs1oVarying Density���bs1a'���`a)���`a
���`a
���bc1x"# Varying color along a streamline���`a
���`cax1���`a ���aoa=���`a ���`cfig���aoa.���`kadd_subplot���`a(���`bgs���`a[���bmia0���`a,���`a ���bmia1���`a]���`a)���`a
���`dstrm���`a ���aoa=���`a ���`cax1���aoa.���`jstreamplot���`a(���`aX���`a,���`a ���`aY���`a,���`a ���`aU���`a,���`a ���`aV���`a,���`a ���`ecolor���aoa=���`aU���`a,���`a ���`ilinewidth���aoa=���bmia2���`a,���`a ���`dcmap���aoa=���bs1a'���bs1fautumn���bs1a'���`a)���`a
���`cfig���aoa.���`hcolorbar���`a(���`dstrm���aoa.���`elines���`a)���`a
���`cax1���aoa.���`iset_title���`a(���bs1a'���bs1mVarying Color���bs1a'���`a)���`a
���`a
���bc1x(#  Varying line width along a streamline���`a
���`cax2���`a ���aoa=���`a ���`cfig���aoa.���`kadd_subplot���`a(���`bgs���`a[���bmia1���`a,���`a ���bmia0���`a]���`a)���`a
���`blw���`a ���aoa=���`a ���bmia5���aoa*���`espeed���`a ���aoa/���`a ���`espeed���aoa.���`cmax���`a(���`a)���`a
���`cax2���aoa.���`jstreamplot���`a(���`aX���`a,���`a ���`aY���`a,���`a ���`aU���`a,���`a ���`aV���`a,���`a ���`gdensity���aoa=���bmfc0.6���`a,���`a ���`ecolor���aoa=���bs1a'���bs1ak���bs1a'���`a,���`a ���`ilinewidth���aoa=���`blw���`a)���`a
���`cax2���aoa.���`iset_title���`a(���bs1a'���bs1rVarying Line Width���bs1a'���`a)���`a
���`a
���bc1x4# Controlling the starting points of the streamlines���`a
���`kseed_points���`a ���aoa=���`a ���`bnp���aoa.���`earray���`a(���`a[���`a[���aoa-���bmia2���`a,���`a ���aoa-���bmia1���`a,���`a ���bmia0���`a,���`a ���bmia1���`a,���`a ���bmia2���`a,���`a ���aoa-���bmia1���`a]���`a,���`a ���`a[���aoa-���bmia2���`a,���`a ���aoa-���bmia1���`a,���`b  ���bmia0���`a,���`a ���bmia1���`a,���`a ���bmia2���`a,���`a ���bmia2���`a]���`a]���`a)���`a
���`a
���`cax3���`a ���aoa=���`a ���`cfig���aoa.���`kadd_subplot���`a(���`bgs���`a[���bmia1���`a,���`a ���bmia1���`a]���`a)���`a
���`dstrm���`a ���aoa=���`a ���`cax3���aoa.���`jstreamplot���`a(���`aX���`a,���`a ���`aY���`a,���`a ���`aU���`a,���`a ���`aV���`a,���`a ���`ecolor���aoa=���`aU���`a,���`a ���`ilinewidth���aoa=���bmia2���`a,���`a
���`v                      ���`dcmap���aoa=���bs1a'���bs1fautumn���bs1a'���`a,���`a ���`lstart_points���aoa=���`kseed_points���aoa.���`aT���`a)���`a
���`cfig���aoa.���`hcolorbar���`a(���`dstrm���aoa.���`elines���`a)���`a
���`cax3���aoa.���`iset_title���`a(���bs1a'���bs1xControlling Starting Points���bs1a'���`a)���`a
���`a
���bc1x3# Displaying the starting points with blue symbols.���`a
���`cax3���aoa.���`dplot���`a(���`kseed_points���`a[���bmia0���`a]���`a,���`a ���`kseed_points���`a[���bmia1���`a]���`a,���`a ���bs1a'���bs1bbo���bs1a'���`a)���`a
���`cax3���aoa.���`cset���`a(���`dxlim���aoa=���`a(���aoa-���`aw���`a,���`a ���`aw���`a)���`a,���`a ���`dylim���aoa=���`a(���aoa-���`aw���`a,���`a ���`aw���`a)���`a)���`a
���`a
���bc1o# Create a mask���`a
���`dmask���`a ���aoa=���`a ���`bnp���aoa.���`ezeros���`a(���`aU���aoa.���`eshape���`a,���`a ���`edtype���aoa=���bnbdbool���`a)���`a
���`dmask���`a[���bmib40���`a:���bmib60���`a,���`a ���bmib40���`a:���bmib60���`a]���`a ���aoa=���`a ���bkcdTrue���`a
���`aU���`a[���`a:���bmib20���`a,���`a ���`a:���bmib20���`a]���`a ���aoa=���`a ���`bnp���aoa.���`cnan���`a
���`aU���`a ���aoa=���`a ���`bnp���aoa.���`bma���aoa.���`earray���`a(���`aU���`a,���`a ���`dmask���aoa=���`dmask���`a)���`a
���`a
���`cax4���`a ���aoa=���`a ���`cfig���aoa.���`kadd_subplot���`a(���`bgs���`a[���bmia2���`a:���`a,���`a ���`a:���`a]���`a)���`a
���`cax4���aoa.���`jstreamplot���`a(���`aX���`a,���`a ���`aY���`a,���`a ���`aU���`a,���`a ���`aV���`a,���`a ���`ecolor���aoa=���bs1a'���bs1ar���bs1a'���`a)���`a
���`cax4���aoa.���`iset_title���`a(���bs1a'���bs1wStreamplot with Masking���bs1a'���`a)���`a
���`a
���`cax4���aoa.���`fimshow���`a(���aoa~���`dmask���`a,���`a ���`fextent���aoa=���`a(���aoa-���`aw���`a,���`a ���`aw���`a,���`a ���aoa-���`aw���`a,���`a ���`aw���`a)���`a,���`a ���`ealpha���aoa=���bmfc0.5���`a,���`a ���`dcmap���aoa=���bs1a'���bs1dgray���bs1a'���`a,���`a ���`faspect���aoa=���bs1a'���bs1dauto���bs1a'���`a)���`a
���`cax4���aoa.���`jset_aspect���`a(���bs1a'���bs1eequal���bs1a'���`a)���`a
���`a
���`cplt���aoa.���`ltight_layout���`a(���`a)���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
���bc1xM#############################################################################���`a
���bc1a#���`a
���bc1x# .. admonition:: References���`a
���bc1a#���`a
���bc1xN#    The use of the following functions, methods, classes and modules is shown���`a
���bc1u#    in this example:���`a
���bc1a#���`a
���bc1xI#    - `matplotlib.axes.Axes.streamplot` / `matplotlib.pyplot.streamplot`���`a
���bc1x%#    - `matplotlib.gridspec.GridSpec`���`a
`dNone�