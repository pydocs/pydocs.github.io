Ù¯‚Ù´ƒ™Ù±‚bsdy2"""
=====================
Time Series Histogram
=====================

This example demonstrates how to efficiently visualize large numbers of time
series in a way that could potentially reveal hidden substructure and patterns
that are not immediately obvious, and display them in a visually appealing way.

In this example, we generate multiple sinusoidal "signal" series that are
buried under a larger number of random walk "noise/background" series. For an
unbiased Gaussian random walk with standard deviation of Ïƒ, the RMS deviation
from the origin after n steps is Ïƒ*sqrt(n). So in order to keep the sinusoids
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
"""Ù±‚`a
Ù±‚bkndfromÙ±‚`a Ù±‚bnndcopyÙ±‚`a Ù±‚bknfimportÙ±‚`a Ù±‚`dcopyÙ±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnndtimeÙ±‚`a
Ù±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„enumpyÙ „enumpyf1.22.3fmoduleenumpyfmoduleõÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnnbnpÙ±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„enumpyÙ „enumpyf1.22.3fmoduleenumpyfmoduleõÙ±‚bnna.Ù±‚bnnfmatlibÙ±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnnfpyplotÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnncpltÙ±‚`a
Ù±‚bkndfromÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnnfcolorsÙ±‚`a Ù±‚bknfimportÙ±‚`a Ù±‚`gLogNormÙ±‚`a
Ù±‚`a
Ù±‚`cfigÙ±‚`a,Ù±‚`a Ù±‚`daxesÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cpltÙ±‚aoa.Ù±‚`hsubplotsÙ±‚`a(Ù±‚`enrowsÙ±‚aoa=Ù±‚bmia3Ù±‚`a,Ù±‚`a Ù±‚`gfigsizeÙ±‚aoa=Ù±‚`a(Ù±‚bmia6Ù±‚`a,Ù±‚`a Ù±‚bmia8Ù±‚`a)Ù±‚`a,Ù±‚`a Ù±‚`rconstrained_layoutÙ±‚aoa=Ù±‚bkcdTrueÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚bc1xA# Make some data; a 1D random walk + small fraction of sine wavesÙ±‚`a
Ù±‚`jnum_seriesÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bmid1000Ù±‚`a
Ù±‚`jnum_pointsÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bmic100Ù±‚`a
Ù±‚`cSNRÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bmfd0.10Ù±‚`b  Ù±‚bc1w# Signal to Noise RatioÙ±‚`a
Ù±‚`axÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`hlinspaceÙ±‚`a(Ù±‚bmia0Ù±‚`a,Ù±‚`a Ù±‚bmia4Ù±‚`a Ù±‚aoa*Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`bpiÙ±‚`a,Ù±‚`a Ù±‚`jnum_pointsÙ±‚`a)Ù±‚`a
Ù±‚bc1x)# Generate unbiased Gaussian random walksÙ±‚`a
Ù±‚`aYÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`fcumsumÙ±‚`a(Ù±‚`bnpÙ±‚aoa.Ù±‚`frandomÙ±‚aoa.Ù±‚`erandnÙ±‚`a(Ù±‚`jnum_seriesÙ±‚`a,Ù±‚`a Ù±‚`jnum_pointsÙ±‚`a)Ù±‚`a,Ù±‚`a Ù±‚`daxisÙ±‚aoa=Ù±‚aoa-Ù±‚bmia1Ù±‚`a)Ù±‚`a
Ù±‚bc1x# Generate sinusoidal signalsÙ±‚`a
Ù±‚`jnum_signalÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bnbcintÙ±‚`a(Ù±‚bnberoundÙ±‚`a(Ù±‚`cSNRÙ±‚`a Ù±‚aoa*Ù±‚`a Ù±‚`jnum_seriesÙ±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`cphiÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`a(Ù±‚`bnpÙ±‚aoa.Ù±‚`bpiÙ±‚`a Ù±‚aoa/Ù±‚`a Ù±‚bmia8Ù±‚`a)Ù±‚`a Ù±‚aoa*Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`frandomÙ±‚aoa.Ù±‚`erandnÙ±‚`a(Ù±‚`jnum_signalÙ±‚`a,Ù±‚`a Ù±‚bmia1Ù±‚`a)Ù±‚`b  Ù±‚bc1u# small random offsetÙ±‚`a
Ù±‚`aYÙ±‚`a[Ù±‚aoa-Ù±‚`jnum_signalÙ±‚`a:Ù±‚`a]Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`a(Ù±‚`a
Ù±‚`d    Ù±‚`bnpÙ±‚aoa.Ù±‚`dsqrtÙ±‚`a(Ù±‚`bnpÙ±‚aoa.Ù±‚`farangeÙ±‚`a(Ù±‚`jnum_pointsÙ±‚`a)Ù±‚`a)Ù±‚`a[Ù±‚bkcdNoneÙ±‚`a,Ù±‚`a Ù±‚`a:Ù±‚`a]Ù±‚`b  Ù±‚bc1x # random walk RMS scaling factorÙ±‚`a
Ù±‚`d    Ù±‚aoa*Ù±‚`a Ù±‚`a(Ù±‚`bnpÙ±‚aoa.Ù±‚`csinÙ±‚`a(Ù±‚`axÙ±‚`a[Ù±‚bkcdNoneÙ±‚`a,Ù±‚`a Ù±‚`a:Ù±‚`a]Ù±‚`a Ù±‚aoa-Ù±‚`a Ù±‚`cphiÙ±‚`a)Ù±‚`a
Ù±‚`g       Ù±‚aoa+Ù±‚`a Ù±‚bmfd0.05Ù±‚`a Ù±‚aoa*Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`frandomÙ±‚aoa.Ù±‚`erandnÙ±‚`a(Ù±‚`jnum_signalÙ±‚`a,Ù±‚`a Ù±‚`jnum_pointsÙ±‚`a)Ù±‚`a)Ù±‚`b  Ù±‚bc1t# small random noiseÙ±‚`a
Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚bc1xM# Plot series using `plot` and a small value of `alpha`. With this view it isÙ±‚`a
Ù±‚bc1xG# very difficult to observe the sinusoidal behavior because of how manyÙ±‚`a
Ù±‚bc1xM# overlapping series there are. It also takes a bit of time to run because soÙ±‚`a
Ù±‚bc1x/# many individual artists need to be generated.Ù±‚`a
Ù±‚`cticÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`dtimeÙ±‚aoa.Ù±‚`dtimeÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`daxesÙ±‚`a[Ù±‚bmia0Ù±‚`a]Ù±‚aoa.Ù±‚`dplotÙ±‚`a(Ù±‚`axÙ±‚`a,Ù±‚`a Ù±‚`aYÙ±‚aoa.Ù±‚`aTÙ±‚`a,Ù±‚`a Ù±‚`ecolorÙ±‚aoa=Ù±‚bs2a"Ù±‚bs2bC0Ù±‚bs2a"Ù±‚`a,Ù±‚`a Ù±‚`ealphaÙ±‚aoa=Ù±‚bmfc0.1Ù±‚`a)Ù±‚`a
Ù±‚`ctocÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`dtimeÙ±‚aoa.Ù±‚`dtimeÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`daxesÙ±‚`a[Ù±‚bmia0Ù±‚`a]Ù±‚aoa.Ù±‚`iset_titleÙ±‚`a(Ù±‚bs2a"Ù±‚bs2tLine plot with alphaÙ±‚bs2a"Ù±‚`a)Ù±‚`a
Ù±‚bnbeprintÙ±‚`a(Ù±‚bsaafÙ±‚bs2a"Ù±‚bsia{Ù±‚`ctocÙ±‚aoa-Ù±‚`cticÙ±‚bsia:Ù±‚bs2c.3fÙ±‚bsia}Ù±‚bs2m sec. elapsedÙ±‚bs2a"Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚bc1xN# Now we will convert the multiple time series into a histogram. Not only willÙ±‚`a
Ù±‚bc1xM# the hidden signal be more visible, but it is also a much quicker procedure.Ù±‚`a
Ù±‚`cticÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`dtimeÙ±‚aoa.Ù±‚`dtimeÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚bc1x=# Linearly interpolate between the points in each time seriesÙ±‚`a
Ù±‚`hnum_fineÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bmic800Ù±‚`a
Ù±‚`fx_fineÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`hlinspaceÙ±‚`a(Ù±‚`axÙ±‚aoa.Ù±‚`cminÙ±‚`a(Ù±‚`a)Ù±‚`a,Ù±‚`a Ù±‚`axÙ±‚aoa.Ù±‚`cmaxÙ±‚`a(Ù±‚`a)Ù±‚`a,Ù±‚`a Ù±‚`hnum_fineÙ±‚`a)Ù±‚`a
Ù±‚`fy_fineÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`eemptyÙ±‚`a(Ù±‚`a(Ù±‚`jnum_seriesÙ±‚`a,Ù±‚`a Ù±‚`hnum_fineÙ±‚`a)Ù±‚`a,Ù±‚`a Ù±‚`edtypeÙ±‚aoa=Ù±‚bnbefloatÙ±‚`a)Ù±‚`a
Ù±‚akcforÙ±‚`a Ù±‚`aiÙ±‚`a Ù±‚bowbinÙ±‚`a Ù±‚bnberangeÙ±‚`a(Ù±‚`jnum_seriesÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`d    Ù±‚`fy_fineÙ±‚`a[Ù±‚`aiÙ±‚`a,Ù±‚`a Ù±‚`a:Ù±‚`a]Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`finterpÙ±‚`a(Ù±‚`fx_fineÙ±‚`a,Ù±‚`a Ù±‚`axÙ±‚`a,Ù±‚`a Ù±‚`aYÙ±‚`a[Ù±‚`aiÙ±‚`a,Ù±‚`a Ù±‚`a:Ù±‚`a]Ù±‚`a)Ù±‚`a
Ù±‚`fy_fineÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`fy_fineÙ±‚aoa.Ù±‚`gflattenÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`fx_fineÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`fmatlibÙ±‚aoa.Ù±‚`frepmatÙ±‚`a(Ù±‚`fx_fineÙ±‚`a,Ù±‚`a Ù±‚`jnum_seriesÙ±‚`a,Ù±‚`a Ù±‚bmia1Ù±‚`a)Ù±‚aoa.Ù±‚`gflattenÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚bc1x8# Plot (x, y) points in 2d histogram with log colorscaleÙ±‚`a
Ù±‚bc1xK# It is pretty evident that there is some kind of structure under the noiseÙ±‚`a
Ù±‚bc1x/# You can tune vmax to make signal more visibleÙ±‚`a
Ù±‚`dcmapÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`dcopyÙ±‚`a(Ù±‚`cpltÙ±‚aoa.Ù±‚`bcmÙ±‚aoa.Ù±‚`fplasmaÙ±‚`a)Ù±‚`a
Ù±‚`dcmapÙ±‚aoa.Ù±‚`gset_badÙ±‚`a(Ù±‚`dcmapÙ±‚`a(Ù±‚bmia0Ù±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`ahÙ±‚`a,Ù±‚`a Ù±‚`fxedgesÙ±‚`a,Ù±‚`a Ù±‚`fyedgesÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`khistogram2dÙ±‚`a(Ù±‚`fx_fineÙ±‚`a,Ù±‚`a Ù±‚`fy_fineÙ±‚`a,Ù±‚`a Ù±‚`dbinsÙ±‚aoa=Ù±‚`a[Ù±‚bmic400Ù±‚`a,Ù±‚`a Ù±‚bmic100Ù±‚`a]Ù±‚`a)Ù±‚`a
Ù±‚`cpcmÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`daxesÙ±‚`a[Ù±‚bmia1Ù±‚`a]Ù±‚aoa.Ù±‚`jpcolormeshÙ±‚`a(Ù±‚`fxedgesÙ±‚`a,Ù±‚`a Ù±‚`fyedgesÙ±‚`a,Ù±‚`a Ù±‚`ahÙ±‚aoa.Ù±‚`aTÙ±‚`a,Ù±‚`a Ù±‚`dcmapÙ±‚aoa=Ù±‚`dcmapÙ±‚`a,Ù±‚`a
Ù±‚`x                         Ù±‚`dnormÙ±‚aoa=Ù±‚`gLogNormÙ±‚`a(Ù±‚`dvmaxÙ±‚aoa=Ù±‚bmfe1.5e2Ù±‚`a)Ù±‚`a,Ù±‚`a Ù±‚`jrasterizedÙ±‚aoa=Ù±‚bkcdTrueÙ±‚`a)Ù±‚`a
Ù±‚`cfigÙ±‚aoa.Ù±‚`hcolorbarÙ±‚`a(Ù±‚`cpcmÙ±‚`a,Ù±‚`a Ù±‚`baxÙ±‚aoa=Ù±‚`daxesÙ±‚`a[Ù±‚bmia1Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`elabelÙ±‚aoa=Ù±‚bs2a"Ù±‚bs2h# pointsÙ±‚bs2a"Ù±‚`a,Ù±‚`a Ù±‚`cpadÙ±‚aoa=Ù±‚bmia0Ù±‚`a)Ù±‚`a
Ù±‚`daxesÙ±‚`a[Ù±‚bmia1Ù±‚`a]Ù±‚aoa.Ù±‚`iset_titleÙ±‚`a(Ù±‚bs2a"Ù±‚bs2x 2d histogram and log color scaleÙ±‚bs2a"Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚bc1x%# Same data but on linear color scaleÙ±‚`a
Ù±‚`cpcmÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`daxesÙ±‚`a[Ù±‚bmia2Ù±‚`a]Ù±‚aoa.Ù±‚`jpcolormeshÙ±‚`a(Ù±‚`fxedgesÙ±‚`a,Ù±‚`a Ù±‚`fyedgesÙ±‚`a,Ù±‚`a Ù±‚`ahÙ±‚aoa.Ù±‚`aTÙ±‚`a,Ù±‚`a Ù±‚`dcmapÙ±‚aoa=Ù±‚`dcmapÙ±‚`a,Ù±‚`a
Ù±‚`x                         Ù±‚`dvmaxÙ±‚aoa=Ù±‚bmfe1.5e2Ù±‚`a,Ù±‚`a Ù±‚`jrasterizedÙ±‚aoa=Ù±‚bkcdTrueÙ±‚`a)Ù±‚`a
Ù±‚`cfigÙ±‚aoa.Ù±‚`hcolorbarÙ±‚`a(Ù±‚`cpcmÙ±‚`a,Ù±‚`a Ù±‚`baxÙ±‚aoa=Ù±‚`daxesÙ±‚`a[Ù±‚bmia2Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`elabelÙ±‚aoa=Ù±‚bs2a"Ù±‚bs2h# pointsÙ±‚bs2a"Ù±‚`a,Ù±‚`a Ù±‚`cpadÙ±‚aoa=Ù±‚bmia0Ù±‚`a)Ù±‚`a
Ù±‚`daxesÙ±‚`a[Ù±‚bmia2Ù±‚`a]Ù±‚aoa.Ù±‚`iset_titleÙ±‚`a(Ù±‚bs2a"Ù±‚bs2x#2d histogram and linear color scaleÙ±‚bs2a"Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`ctocÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`dtimeÙ±‚aoa.Ù±‚`dtimeÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚bnbeprintÙ±‚`a(Ù±‚bsaafÙ±‚bs2a"Ù±‚bsia{Ù±‚`ctocÙ±‚aoa-Ù±‚`cticÙ±‚bsia:Ù±‚bs2c.3fÙ±‚bsia}Ù±‚bs2m sec. elapsedÙ±‚bs2a"Ù±‚`a)Ù±‚`a
Ù±‚`cpltÙ±‚aoa.Ù±‚`dshowÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚bc1xM#############################################################################Ù±‚`a
Ù±‚bc1a#Ù±‚`a
Ù±‚bc1x# .. admonition:: ReferencesÙ±‚`a
Ù±‚bc1a#Ù±‚`a
Ù±‚bc1xN#    The use of the following functions, methods, classes and modules is shownÙ±‚`a
Ù±‚bc1u#    in this example:Ù±‚`a
Ù±‚bc1a#Ù±‚`a
Ù±‚bc1xI#    - `matplotlib.axes.Axes.pcolormesh` / `matplotlib.pyplot.pcolormesh`Ù±‚`a
Ù±‚bc1x*#    - `matplotlib.figure.Figure.colorbar`Ù±‚`a
`dNoneö