��������h���bsdx�"""
========
Colorbar
========

Use `~.figure.Figure.colorbar` by specifying the mappable object (here
the `~.matplotlib.image.AxesImage` returned by `~.axes.Axes.imshow`)
and the axes to attach the colorbar to.
"""���`a
���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���`a
���bc1x# setup some generic data���`a
���`aN���`a ���aoa=���`a ���bmib37���`a
���`ax���`a,���`a ���`ay���`a ���aoa=���`a ���`bnp���aoa.���`emgrid���`a[���`a:���`aN���`a,���`a ���`a:���`aN���`a]���`a
���`aZ���`a ���aoa=���`a ���`a(���`bnp���aoa.���`ccos���`a(���`ax���aoa*���bmfc0.2���`a)���`a ���aoa+���`a ���`bnp���aoa.���`csin���`a(���`ay���aoa*���bmfc0.3���`a)���`a)���`a
���`a
���bc1x9# mask out the negative and positive values, respectively���`a
���`dZpos���`a ���aoa=���`a ���`bnp���aoa.���`bma���aoa.���`kmasked_less���`a(���`aZ���`a,���`a ���bmia0���`a)���`a
���`dZneg���`a ���aoa=���`a ���`bnp���aoa.���`bma���aoa.���`nmasked_greater���`a(���`aZ���`a,���`a ���bmia0���`a)���`a
���`a
���`cfig���`a,���`a ���`a(���`cax1���`a,���`a ���`cax2���`a,���`a ���`cax3���`a)���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`gfigsize���aoa=���`a(���bmib13���`a,���`a ���bmia3���`a)���`a,���`a ���`encols���aoa=���bmia3���`a)���`a
���`a
���bc1x*# plot just the positive data and save the���`a
���bc1x0# color "mappable" object returned by ax1.imshow���`a
���`cpos���`a ���aoa=���`a ���`cax1���aoa.���`fimshow���`a(���`dZpos���`a,���`a ���`dcmap���aoa=���bs1a'���bs1eBlues���bs1a'���`a,���`a ���`minterpolation���aoa=���bs1a'���bs1dnone���bs1a'���`a)���`a
���`a
���bc1x-# add the colorbar using the figure's method,���`a
���bc1x0# telling which mappable we're talking about and���`a
���bc1x%# which axes object it should be near���`a
���`cfig���aoa.���`hcolorbar���`a(���`cpos���`a,���`a ���`bax���aoa=���`cax1���`a)���`a
���`a
���bc1x/# repeat everything above for the negative data���`a
���bc1x:# you can specify location, anchor and shrink the colorbar���`a
���`cneg���`a ���aoa=���`a ���`cax2���aoa.���`fimshow���`a(���`dZneg���`a,���`a ���`dcmap���aoa=���bs1a'���bs1fReds_r���bs1a'���`a,���`a ���`minterpolation���aoa=���bs1a'���bs1dnone���bs1a'���`a)���`a
���`cfig���aoa.���`hcolorbar���`a(���`cneg���`a,���`a ���`bax���aoa=���`cax2���`a,���`a ���`hlocation���aoa=���bs1a'���bs1eright���bs1a'���`a,���`a ���`fanchor���aoa=���`a(���bmia0���`a,���`a ���bmfc0.3���`a)���`a,���`a ���`fshrink���aoa=���bmfc0.7���`a)���`a
���`a
���bc1x8# Plot both positive and negative values between +/- 1.2���`a
���`opos_neg_clipped���`a ���aoa=���`a ���`cax3���aoa.���`fimshow���`a(���`aZ���`a,���`a ���`dcmap���aoa=���bs1a'���bs1dRdBu���bs1a'���`a,���`a ���`dvmin���aoa=���aoa-���bmfc1.2���`a,���`a ���`dvmax���aoa=���bmfc1.2���`a,���`a
���`x                             ���`minterpolation���aoa=���bs1a'���bs1dnone���bs1a'���`a)���`a
���bc1x<# Add minorticks on the colorbar to make it easy to read the���`a
���bc1x# values off the colorbar.���`a
���`dcbar���`a ���aoa=���`a ���`cfig���aoa.���`hcolorbar���`a(���`opos_neg_clipped���`a,���`a ���`bax���aoa=���`cax3���`a,���`a ���`fextend���aoa=���bs1a'���bs1dboth���bs1a'���`a)���`a
���`dcbar���aoa.���`mminorticks_on���`a(���`a)���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
���`a
���bc1xM#############################################################################���`a
���bc1a#���`a
���bc1x# .. admonition:: References���`a
���bc1a#���`a
���bc1xN#    The use of the following functions, methods, classes and modules is shown���`a
���bc1u#    in this example:���`a
���bc1a#���`a
���bc1xA#    - `matplotlib.axes.Axes.imshow` / `matplotlib.pyplot.imshow`���`a
���bc1xI#    - `matplotlib.figure.Figure.colorbar` / `matplotlib.pyplot.colorbar`���`a
���bc1x3#    - `matplotlib.colorbar.Colorbar.minorticks_on`���`a
���bc1x4#    - `matplotlib.colorbar.Colorbar.minorticks_off`���`a
`dNone�