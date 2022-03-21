�����������bsdy2"""
=====================
Time Series Histogram
=====================

This example demonstrates how to efficiently visualize large numbers of time
series in a way that could potentially reveal hidden substructure and patterns
that are not immediately obvious, and display them in a visually appealing way.

In this example, we generate multiple sinusoidal "signal" series that are
buried under a larger number of random walk "noise/background" series. For an
unbiased Gaussian random walk with standard deviation of σ, the RMS deviation
from the origin after n steps is σ*sqrt(n). So in order to keep the sinusoids
visible on the same scale as the random walks, we scale the amplitude by the
random walk RMS. In addition, we also introduce a small random offset ``phi``
to shift the sines left/right, and some additive random noise to shift
individual data points up/down to make the signal a bit more "realistic" (you
wouldn't expect a perfect sine wave to appear in your data).

The first plot shows the typical way of visualizing multiple time series by
overlaying them on top of each other with ``plt.plot`` and a small value of
``alpha``. The second and third plots show how to reinterpret the data as a 2d
histogram, with optional interpolation between data points, by using
``np.histogram2d`` and ``plt.pcolormesh``.
"""���`a
���bkndfrom���`a ���bnndcopy���`a ���bknfimport���`a ���`dcopy���`a
���bknfimport���`a ���bnndtime���`a
���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����bnna.���bnnfmatlib���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���bkndfrom���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfcolors���`a ���bknfimport���`a ���`gLogNorm���`a
���`a
���`cfig���`a,���`a ���`daxes���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`enrows���aoa=���bmia3���`a,���`a ���`gfigsize���aoa=���`a(���bmia6���`a,���`a ���bmia8���`a)���`a,���`a ���`rconstrained_layout���aoa=���bkcdTrue���`a)���`a
���`a
���bc1xA# Make some data; a 1D random walk + small fraction of sine waves���`a
���`jnum_series���`a ���aoa=���`a ���bmid1000���`a
���`jnum_points���`a ���aoa=���`a ���bmic100���`a
���`cSNR���`a ���aoa=���`a ���bmfd0.10���`b  ���bc1w# Signal to Noise Ratio���`a
���`ax���`a ���aoa=���`a ���`bnp���aoa.���`hlinspace���`a(���bmia0���`a,���`a ���bmia4���`a ���aoa*���`a ���`bnp���aoa.���`bpi���`a,���`a ���`jnum_points���`a)���`a
���bc1x)# Generate unbiased Gaussian random walks���`a
���`aY���`a ���aoa=���`a ���`bnp���aoa.���`fcumsum���`a(���`bnp���aoa.���`frandom���aoa.���`erandn���`a(���`jnum_series���`a,���`a ���`jnum_points���`a)���`a,���`a ���`daxis���aoa=���aoa-���bmia1���`a)���`a
���bc1x# Generate sinusoidal signals���`a
���`jnum_signal���`a ���aoa=���`a ���bnbcint���`a(���bnberound���`a(���`cSNR���`a ���aoa*���`a ���`jnum_series���`a)���`a)���`a
���`cphi���`a ���aoa=���`a ���`a(���`bnp���aoa.���`bpi���`a ���aoa/���`a ���bmia8���`a)���`a ���aoa*���`a ���`bnp���aoa.���`frandom���aoa.���`erandn���`a(���`jnum_signal���`a,���`a ���bmia1���`a)���`b  ���bc1u# small random offset���`a
���`aY���`a[���aoa-���`jnum_signal���`a:���`a]���`a ���aoa=���`a ���`a(���`a
���`d    ���`bnp���aoa.���`dsqrt���`a(���`bnp���aoa.���`farange���`a(���`jnum_points���`a)���`a)���`a[���bkcdNone���`a,���`a ���`a:���`a]���`b  ���bc1x # random walk RMS scaling factor���`a
���`d    ���aoa*���`a ���`a(���`bnp���aoa.���`csin���`a(���`ax���`a[���bkcdNone���`a,���`a ���`a:���`a]���`a ���aoa-���`a ���`cphi���`a)���`a
���`g       ���aoa+���`a ���bmfd0.05���`a ���aoa*���`a ���`bnp���aoa.���`frandom���aoa.���`erandn���`a(���`jnum_signal���`a,���`a ���`jnum_points���`a)���`a)���`b  ���bc1t# small random noise���`a
���`a)���`a
���`a
���`a
���bc1xM# Plot series using `plot` and a small value of `alpha`. With this view it is���`a
���bc1xG# very difficult to observe the sinusoidal behavior because of how many���`a
���bc1xM# overlapping series there are. It also takes a bit of time to run because so���`a
���bc1x/# many individual artists need to be generated.���`a
���`ctic���`a ���aoa=���`a ���`dtime���aoa.���`dtime���`a(���`a)���`a
���`daxes���`a[���bmia0���`a]���aoa.���`dplot���`a(���`ax���`a,���`a ���`aY���aoa.���`aT���`a,���`a ���`ecolor���aoa=���bs2a"���bs2bC0���bs2a"���`a,���`a ���`ealpha���aoa=���bmfc0.1���`a)���`a
���`ctoc���`a ���aoa=���`a ���`dtime���aoa.���`dtime���`a(���`a)���`a
���`daxes���`a[���bmia0���`a]���aoa.���`iset_title���`a(���bs2a"���bs2tLine plot with alpha���bs2a"���`a)���`a
���bnbeprint���`a(���bsaaf���bs2a"���bsia{���`ctoc���aoa-���`ctic���bsia:���bs2c.3f���bsia}���bs2m sec. elapsed���bs2a"���`a)���`a
���`a
���`a
���bc1xN# Now we will convert the multiple time series into a histogram. Not only will���`a
���bc1xM# the hidden signal be more visible, but it is also a much quicker procedure.���`a
���`ctic���`a ���aoa=���`a ���`dtime���aoa.���`dtime���`a(���`a)���`a
���bc1x=# Linearly interpolate between the points in each time series���`a
���`hnum_fine���`a ���aoa=���`a ���bmic800���`a
���`fx_fine���`a ���aoa=���`a ���`bnp���aoa.���`hlinspace���`a(���`ax���aoa.���`cmin���`a(���`a)���`a,���`a ���`ax���aoa.���`cmax���`a(���`a)���`a,���`a ���`hnum_fine���`a)���`a
���`fy_fine���`a ���aoa=���`a ���`bnp���aoa.���`eempty���`a(���`a(���`jnum_series���`a,���`a ���`hnum_fine���`a)���`a,���`a ���`edtype���aoa=���bnbefloat���`a)���`a
���akcfor���`a ���`ai���`a ���bowbin���`a ���bnberange���`a(���`jnum_series���`a)���`a:���`a
���`d    ���`fy_fine���`a[���`ai���`a,���`a ���`a:���`a]���`a ���aoa=���`a ���`bnp���aoa.���`finterp���`a(���`fx_fine���`a,���`a ���`ax���`a,���`a ���`aY���`a[���`ai���`a,���`a ���`a:���`a]���`a)���`a
���`fy_fine���`a ���aoa=���`a ���`fy_fine���aoa.���`gflatten���`a(���`a)���`a
���`fx_fine���`a ���aoa=���`a ���`bnp���aoa.���`fmatlib���aoa.���`frepmat���`a(���`fx_fine���`a,���`a ���`jnum_series���`a,���`a ���bmia1���`a)���aoa.���`gflatten���`a(���`a)���`a
���`a
���`a
���bc1x8# Plot (x, y) points in 2d histogram with log colorscale���`a
���bc1xK# It is pretty evident that there is some kind of structure under the noise���`a
���bc1x/# You can tune vmax to make signal more visible���`a
���`dcmap���`a ���aoa=���`a ���`dcopy���`a(���`cplt���aoa.���`bcm���aoa.���`fplasma���`a)���`a
���`dcmap���aoa.���`gset_bad���`a(���`dcmap���`a(���bmia0���`a)���`a)���`a
���`ah���`a,���`a ���`fxedges���`a,���`a ���`fyedges���`a ���aoa=���`a ���`bnp���aoa.���`khistogram2d���`a(���`fx_fine���`a,���`a ���`fy_fine���`a,���`a ���`dbins���aoa=���`a[���bmic400���`a,���`a ���bmic100���`a]���`a)���`a
���`cpcm���`a ���aoa=���`a ���`daxes���`a[���bmia1���`a]���aoa.���`jpcolormesh���`a(���`fxedges���`a,���`a ���`fyedges���`a,���`a ���`ah���aoa.���`aT���`a,���`a ���`dcmap���aoa=���`dcmap���`a,���`a
���`x                         ���`dnorm���aoa=���`gLogNorm���`a(���`dvmax���aoa=���bmfe1.5e2���`a)���`a,���`a ���`jrasterized���aoa=���bkcdTrue���`a)���`a
���`cfig���aoa.���`hcolorbar���`a(���`cpcm���`a,���`a ���`bax���aoa=���`daxes���`a[���bmia1���`a]���`a,���`a ���`elabel���aoa=���bs2a"���bs2h# points���bs2a"���`a,���`a ���`cpad���aoa=���bmia0���`a)���`a
���`daxes���`a[���bmia1���`a]���aoa.���`iset_title���`a(���bs2a"���bs2x 2d histogram and log color scale���bs2a"���`a)���`a
���`a
���bc1x%# Same data but on linear color scale���`a
���`cpcm���`a ���aoa=���`a ���`daxes���`a[���bmia2���`a]���aoa.���`jpcolormesh���`a(���`fxedges���`a,���`a ���`fyedges���`a,���`a ���`ah���aoa.���`aT���`a,���`a ���`dcmap���aoa=���`dcmap���`a,���`a
���`x                         ���`dvmax���aoa=���bmfe1.5e2���`a,���`a ���`jrasterized���aoa=���bkcdTrue���`a)���`a
���`cfig���aoa.���`hcolorbar���`a(���`cpcm���`a,���`a ���`bax���aoa=���`daxes���`a[���bmia2���`a]���`a,���`a ���`elabel���aoa=���bs2a"���bs2h# points���bs2a"���`a,���`a ���`cpad���aoa=���bmia0���`a)���`a
���`daxes���`a[���bmia2���`a]���aoa.���`iset_title���`a(���bs2a"���bs2x#2d histogram and linear color scale���bs2a"���`a)���`a
���`a
���`ctoc���`a ���aoa=���`a ���`dtime���aoa.���`dtime���`a(���`a)���`a
���bnbeprint���`a(���bsaaf���bs2a"���bsia{���`ctoc���aoa-���`ctic���bsia:���bs2c.3f���bsia}���bs2m sec. elapsed���bs2a"���`a)���`a
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
���bc1x*#    - `matplotlib.figure.Figure.colorbar`���`a
`dNone�