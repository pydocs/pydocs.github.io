��������G���bsdx�"""
============================
Contourf and log color scale
============================

Demonstrate use of a log color scale in contourf
"""���`a
���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���bkndfrom���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���bknfimport���`a ���`bma���`a
���bkndfrom���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����`a ���bknfimport���`a ���`fticker���`a,���`a ���`bcm���`a
���`a
���`aN���`a ���aoa=���`a ���bmic100���`a
���`ax���`a ���aoa=���`a ���`bnp���aoa.���`hlinspace���`a(���aoa-���bmfc3.0���`a,���`a ���bmfc3.0���`a,���`a ���`aN���`a)���`a
���`ay���`a ���aoa=���`a ���`bnp���aoa.���`hlinspace���`a(���aoa-���bmfc2.0���`a,���`a ���bmfc2.0���`a,���`a ���`aN���`a)���`a
���`a
���`aX���`a,���`a ���`aY���`a ���aoa=���`a ���`bnp���aoa.���`hmeshgrid���`a(���`ax���`a,���`a ���`ay���`a)���`a
���`a
���bc1x%# A low hump with a spike coming out.���`a
���bc1xK# Needs to have z/colour axis on a log scale so we see both hump and spike.���`a
���bc1x$# linear scale only shows the spike.���`a
���`bZ1���`a ���aoa=���`a ���`bnp���aoa.���`cexp���`a(���aoa-���`aX���aoa*���aoa*���bmia2���`a ���aoa-���`a ���`aY���aoa*���aoa*���bmia2���`a)���`a
���`bZ2���`a ���aoa=���`a ���`bnp���aoa.���`cexp���`a(���aoa-���`a(���`aX���`a ���aoa*���`a ���bmib10���`a)���aoa*���aoa*���bmia2���`a ���aoa-���`a ���`a(���`aY���`a ���aoa*���`a ���bmib10���`a)���aoa*���aoa*���bmia2���`a)���`a
���`az���`a ���aoa=���`a ���`bZ1���`a ���aoa+���`a ���bmib50���`a ���aoa*���`a ���`bZ2���`a
���`a
���bc1xM# Put in some negative values (lower left corner) to cause trouble with logs:���`a
���`az���`a[���`a:���bmia5���`a,���`a ���`a:���bmia5���`a]���`a ���aoa=���`a ���aoa-���bmia1���`a
���`a
���bc1x@# The following is not strictly essential, but it will eliminate���`a
���bc1x0# a warning.  Comment it out to see the warning.���`a
���`az���`a ���aoa=���`a ���`bma���aoa.���`lmasked_where���`a(���`az���`a ���aoa<���aoa=���`a ���bmia0���`a,���`a ���`az���`a)���`a
���`a
���`a
���bc1x2# Automatic selection of levels works; setting the���`a
���bc1x0# log locator tells contourf to use a log scale:���`a
���`cfig���`a,���`a ���`bax���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`a)���`a
���`bcs���`a ���aoa=���`a ���`bax���aoa.���`hcontourf���`a(���`aX���`a,���`a ���`aY���`a,���`a ���`az���`a,���`a ���`glocator���aoa=���`fticker���aoa.���`jLogLocator���`a(���`a)���`a,���`a ���`dcmap���aoa=���`bcm���aoa.���`fPuBu_r���`a)���`a
���`a
���bc1x0# Alternatively, you can manually set the levels���`a
���bc1o# and the norm:���`a
���bc1x4# lev_exp = np.arange(np.floor(np.log10(z.min())-1),���`a
���bc1x2#                    np.ceil(np.log10(z.max())+1))���`a
���bc1x# levs = np.power(10, lev_exp)���`a
���bc1x8# cs = ax.contourf(X, Y, z, levs, norm=colors.LogNorm())���`a
���`a
���`dcbar���`a ���aoa=���`a ���`cfig���aoa.���`hcolorbar���`a(���`bcs���`a)���`a
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
���bc1xE#    - `matplotlib.axes.Axes.contourf` / `matplotlib.pyplot.contourf`���`a
���bc1xI#    - `matplotlib.figure.Figure.colorbar` / `matplotlib.pyplot.colorbar`���`a
���bc1xA#    - `matplotlib.axes.Axes.legend` / `matplotlib.pyplot.legend`���`a
���bc1x%#    - `matplotlib.ticker.LogLocator`���`a
`dNone�