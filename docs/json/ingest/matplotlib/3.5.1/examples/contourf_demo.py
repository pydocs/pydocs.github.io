������������bsdx~"""
=============
Contourf Demo
=============

How to use the `.axes.Axes.contourf` method to create filled contour plots.
"""���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���`a
���`forigin���`a ���aoa=���`a ���bs1a'���bs1elower���bs1a'���`a
���`a
���`edelta���`a ���aoa=���`a ���bmfe0.025���`a
���`a
���`ax���`a ���aoa=���`a ���`ay���`a ���aoa=���`a ���`bnp���aoa.���`farange���`a(���aoa-���bmfc3.0���`a,���`a ���bmfd3.01���`a,���`a ���`edelta���`a)���`a
���`aX���`a,���`a ���`aY���`a ���aoa=���`a ���`bnp���aoa.���`hmeshgrid���`a(���`ax���`a,���`a ���`ay���`a)���`a
���`bZ1���`a ���aoa=���`a ���`bnp���aoa.���`cexp���`a(���aoa-���`aX���aoa*���aoa*���bmia2���`a ���aoa-���`a ���`aY���aoa*���aoa*���bmia2���`a)���`a
���`bZ2���`a ���aoa=���`a ���`bnp���aoa.���`cexp���`a(���aoa-���`a(���`aX���`a ���aoa-���`a ���bmia1���`a)���aoa*���aoa*���bmia2���`a ���aoa-���`a ���`a(���`aY���`a ���aoa-���`a ���bmia1���`a)���aoa*���aoa*���bmia2���`a)���`a
���`aZ���`a ���aoa=���`a ���`a(���`bZ1���`a ���aoa-���`a ���`bZ2���`a)���`a ���aoa*���`a ���bmia2���`a
���`a
���`bnr���`a,���`a ���`bnc���`a ���aoa=���`a ���`aZ���aoa.���`eshape���`a
���`a
���bc1x# put NaNs in one corner:���`a
���`aZ���`a[���aoa-���`bnr���`a ���aoa/���aoa/���`a ���bmia6���`a:���`a,���`a ���aoa-���`bnc���`a ���aoa/���aoa/���`a ���bmia6���`a:���`a]���`a ���aoa=���`a ���`bnp���aoa.���`cnan���`a
���bc1x'# contourf will convert these to masked���`a
���`a
���`a
���`aZ���`a ���aoa=���`a ���`bnp���aoa.���`bma���aoa.���`earray���`a(���`aZ���`a)���`a
���bc1v# mask another corner:���`a
���`aZ���`a[���`a:���`bnr���`a ���aoa/���aoa/���`a ���bmia6���`a,���`a ���`a:���`bnc���`a ���aoa/���aoa/���`a ���bmia6���`a]���`a ���aoa=���`a ���`bnp���aoa.���`bma���aoa.���`fmasked���`a
���`a
���bc1x# mask a circle in the middle:���`a
���`hinterior���`a ���aoa=���`a ���`bnp���aoa.���`dsqrt���`a(���`aX���aoa*���aoa*���bmia2���`a ���aoa+���`a ���`aY���aoa*���aoa*���bmia2���`a)���`a ���aoa<���`a ���bmfc0.5���`a
���`aZ���`a[���`hinterior���`a]���`a ���aoa=���`a ���`bnp���aoa.���`bma���aoa.���`fmasked���`a
���`a
���bc1xM#############################################################################���`a
���bc1x# Automatic contour levels���`a
���bc1x# ------------------------���`a
���bc1xN# We are using automatic selection of contour levels; this is usually not such���`a
���bc1xM# a good idea, because they don't occur on nice boundaries, but we do it here���`a
���bc1x# for purposes of illustration.���`a
���`a
���`dfig1���`a,���`a ���`cax2���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`rconstrained_layout���aoa=���bkcdTrue���`a)���`a
���`bCS���`a ���aoa=���`a ���`cax2���aoa.���`hcontourf���`a(���`aX���`a,���`a ���`aY���`a,���`a ���`aZ���`a,���`a ���bmib10���`a,���`a ���`dcmap���aoa=���`cplt���aoa.���`bcm���aoa.���`dbone���`a,���`a ���`forigin���aoa=���`forigin���`a)���`a
���`a
���bc1xK# Note that in the following, we explicitly pass in a subset of the contour���`a
���bc1xG# levels used for the filled contours.  Alternatively, we could pass in���`a
���bc1xJ# additional levels to provide extra resolution, or leave out the *levels*���`a
���bc1x5# keyword argument to use all of the original levels.���`a
���`a
���`cCS2���`a ���aoa=���`a ���`cax2���aoa.���`gcontour���`a(���`bCS���`a,���`a ���`flevels���aoa=���`bCS���aoa.���`flevels���`a[���`a:���`a:���bmia2���`a]���`a,���`a ���`fcolors���aoa=���bs1a'���bs1ar���bs1a'���`a,���`a ���`forigin���aoa=���`forigin���`a)���`a
���`a
���`cax2���aoa.���`iset_title���`a(���bs1a'���bs1xNonsense (3 masked regions)���bs1a'���`a)���`a
���`cax2���aoa.���`jset_xlabel���`a(���bs1a'���bs1sword length anomaly���bs1a'���`a)���`a
���`cax2���aoa.���`jset_ylabel���`a(���bs1a'���bs1wsentence length anomaly���bs1a'���`a)���`a
���`a
���bc1xC# Make a colorbar for the ContourSet returned by the contourf call.���`a
���`dcbar���`a ���aoa=���`a ���`dfig1���aoa.���`hcolorbar���`a(���`bCS���`a)���`a
���`dcbar���aoa.���`bax���aoa.���`jset_ylabel���`a(���bs1a'���bs1uverbosity coefficient���bs1a'���`a)���`a
���bc1x-# Add the contour line levels to the colorbar���`a
���`dcbar���aoa.���`iadd_lines���`a(���`cCS2���`a)���`a
���`a
���bc1xM#############################################################################���`a
���bc1x# Explicit contour levels���`a
���bc1x# -----------------------���`a
���bc1xJ# Now make a contour plot with the levels specified, and with the colormap���`a
���bc1x0# generated automatically from a list of colors.���`a
���`a
���`dfig2���`a,���`a ���`cax2���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`rconstrained_layout���aoa=���bkcdTrue���`a)���`a
���`flevels���`a ���aoa=���`a ���`a[���aoa-���bmfc1.5���`a,���`a ���aoa-���bmia1���`a,���`a ���aoa-���bmfc0.5���`a,���`a ���bmia0���`a,���`a ���bmfc0.5���`a,���`a ���bmia1���`a]���`a
���`cCS3���`a ���aoa=���`a ���`cax2���aoa.���`hcontourf���`a(���`aX���`a,���`a ���`aY���`a,���`a ���`aZ���`a,���`a ���`flevels���`a,���`a
���`s                   ���`fcolors���aoa=���`a(���bs1a'���bs1ar���bs1a'���`a,���`a ���bs1a'���bs1ag���bs1a'���`a,���`a ���bs1a'���bs1ab���bs1a'���`a)���`a,���`a
���`s                   ���`forigin���aoa=���`forigin���`a,���`a
���`s                   ���`fextend���aoa=���bs1a'���bs1dboth���bs1a'���`a)���`a
���bc1x:# Our data range extends outside the range of levels; make���`a
���bc1x;# data below the lowest contour level yellow, and above the���`a
���bc1u# highest level cyan:���`a
���`cCS3���aoa.���`dcmap���aoa.���`iset_under���`a(���bs1a'���bs1fyellow���bs1a'���`a)���`a
���`cCS3���aoa.���`dcmap���aoa.���`hset_over���`a(���bs1a'���bs1dcyan���bs1a'���`a)���`a
���`a
���`cCS4���`a ���aoa=���`a ���`cax2���aoa.���`gcontour���`a(���`aX���`a,���`a ���`aY���`a,���`a ���`aZ���`a,���`a ���`flevels���`a,���`a
���`r                  ���`fcolors���aoa=���`a(���bs1a'���bs1ak���bs1a'���`a,���`a)���`a,���`a
���`r                  ���`jlinewidths���aoa=���`a(���bmia3���`a,���`a)���`a,���`a
���`r                  ���`forigin���aoa=���`forigin���`a)���`a
���`cax2���aoa.���`iset_title���`a(���bs1a'���bs1x Listed colors (3 masked regions)���bs1a'���`a)���`a
���`cax2���aoa.���`fclabel���`a(���`cCS4���`a,���`a ���`cfmt���aoa=���bs1a'���bsie%2.1f���bs1a'���`a,���`a ���`fcolors���aoa=���bs1a'���bs1aw���bs1a'���`a,���`a ���`hfontsize���aoa=���bmib14���`a)���`a
���`a
���bc1x6# Notice that the colorbar gets all the information it���`a
���bc1x(# needs from the ContourSet object, CS3.���`a
���`dfig2���aoa.���`hcolorbar���`a(���`cCS3���`a)���`a
���`a
���bc1xM#############################################################################���`a
���bc1t# Extension settings���`a
���bc1t# ------------------���`a
���bc1x.# Illustrate all 4 possible "extend" settings:���`a
���`gextends���`a ���aoa=���`a ���`a[���bs2a"���bs2gneither���bs2a"���`a,���`a ���bs2a"���bs2dboth���bs2a"���`a,���`a ���bs2a"���bs2cmin���bs2a"���`a,���`a ���bs2a"���bs2cmax���bs2a"���`a]���`a
���`dcmap���`a ���aoa=���`a ���`cplt���aoa.���`icolormaps���`a[���bs2a"���bs2fwinter���bs2a"���`a]���aoa.���`mwith_extremes���`a(���`eunder���aoa=���bs2a"���bs2gmagenta���bs2a"���`a,���`a ���`dover���aoa=���bs2a"���bs2fyellow���bs2a"���`a)���`a
���bc1x<# Note: contouring simply excludes masked or nan regions, so���`a
���bc1x># instead of using the "bad" colormap value for them, it draws���`a
���bc1x=# nothing at all in them.  Therefore the following would have���`a
���bc1l# no effect:���`a
���bc1u# cmap.set_bad("red")���`a
���`a
���`cfig���`a,���`a ���`caxs���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���bmia2���`a,���`a ���bmia2���`a,���`a ���`rconstrained_layout���aoa=���bkcdTrue���`a)���`a
���`a
���akcfor���`a ���`bax���`a,���`a ���`fextend���`a ���bowbin���`a ���bnbczip���`a(���`caxs���aoa.���`dflat���`a,���`a ���`gextends���`a)���`a:���`a
���`d    ���`bcs���`a ���aoa=���`a ���`bax���aoa.���`hcontourf���`a(���`aX���`a,���`a ���`aY���`a,���`a ���`aZ���`a,���`a ���`flevels���`a,���`a ���`dcmap���aoa=���`dcmap���`a,���`a ���`fextend���aoa=���`fextend���`a,���`a ���`forigin���aoa=���`forigin���`a)���`a
���`d    ���`cfig���aoa.���`hcolorbar���`a(���`bcs���`a,���`a ���`bax���aoa=���`bax���`a,���`a ���`fshrink���aoa=���bmfc0.9���`a)���`a
���`d    ���`bax���aoa.���`iset_title���`a(���bs2a"���bs2iextend = ���bsib%s���bs2a"���`a ���aoa%���`a ���`fextend���`a)���`a
���`d    ���`bax���aoa.���`nlocator_params���`a(���`enbins���aoa=���bmia4���`a)���`a
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
���bc1xC#    - `matplotlib.axes.Axes.contour` / `matplotlib.pyplot.contour`���`a
���bc1xE#    - `matplotlib.axes.Axes.contourf` / `matplotlib.pyplot.contourf`���`a
���bc1xA#    - `matplotlib.axes.Axes.clabel` / `matplotlib.pyplot.clabel`���`a
���bc1xI#    - `matplotlib.figure.Figure.colorbar` / `matplotlib.pyplot.colorbar`���`a
���bc1x##    - `matplotlib.colors.Colormap`���`a
���bc1x+#    - `matplotlib.colors.Colormap.set_bad`���`a
���bc1x-#    - `matplotlib.colors.Colormap.set_under`���`a
���bc1x,#    - `matplotlib.colors.Colormap.set_over`���`a
`dNone�