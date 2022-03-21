��������R���bsdxQ"""
==========
Histograms
==========

How to plot histograms with Matplotlib.
"""���`a
���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���bkndfrom���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����`a ���bknfimport���`a ���`fcolors���`a
���bkndfrom���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfticker���`a ���bknfimport���`a ���`pPercentFormatter���`a
���`a
���bc1xH# Create a random number generator with a fixed seed for reproducibility���`a
���`crng���`a ���aoa=���`a ���`bnp���aoa.���`frandom���aoa.���`kdefault_rng���`a(���bmih19680801���`a)���`a
���`a
���bc1xO###############################################################################���`a
���bc1x+# Generate data and plot a simple histogram���`a
���bc1x+# -----------------------------------------���`a
���bc1a#���`a
���bc1xN# To generate a 1D histogram we only need a single vector of numbers. For a 2D���`a
���bc1xK# histogram we'll need a second vector. We'll generate both below, and show���`a
���bc1x # the histogram for each vector.���`a
���`a
���`hN_points���`a ���aoa=���`a ���bmif100000���`a
���`fn_bins���`a ���aoa=���`a ���bmib20���`a
���`a
���bc1x## Generate two normal distributions���`a
���`edist1���`a ���aoa=���`a ���`crng���aoa.���`ostandard_normal���`a(���`hN_points���`a)���`a
���`edist2���`a ���aoa=���`a ���bmfc0.4���`a ���aoa*���`a ���`crng���aoa.���`ostandard_normal���`a(���`hN_points���`a)���`a ���aoa+���`a ���bmia5���`a
���`a
���`cfig���`a,���`a ���`caxs���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���bmia1���`a,���`a ���bmia2���`a,���`a ���`fsharey���aoa=���bkcdTrue���`a,���`a ���`ltight_layout���aoa=���bkcdTrue���`a)���`a
���`a
���bc1xA# We can set the number of bins with the *bins* keyword argument.���`a
���`caxs���`a[���bmia0���`a]���aoa.���`dhist���`a(���`edist1���`a,���`a ���`dbins���aoa=���`fn_bins���`a)���`a
���`caxs���`a[���bmia1���`a]���aoa.���`dhist���`a(���`edist2���`a,���`a ���`dbins���aoa=���`fn_bins���`a)���`a
���`a
���`a
���bc1xO###############################################################################���`a
���bc1x# Updating histogram colors���`a
���bc1x# -------------------------���`a
���bc1a#���`a
���bc1xN# The histogram method returns (among other things) a ``patches`` object. This���`a
���bc1xL# gives us access to the properties of the objects drawn. Using this, we can���`a
���bc1xF# edit the histogram to our liking. Let's change the color of each bar���`a
���bc1w# based on its y value.���`a
���`a
���`cfig���`a,���`a ���`caxs���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���bmia1���`a,���`a ���bmia2���`a,���`a ���`ltight_layout���aoa=���bkcdTrue���`a)���`a
���`a
���bc1x@# N is the count in each bin, bins is the lower-limit of the bin���`a
���`aN���`a,���`a ���`dbins���`a,���`a ���`gpatches���`a ���aoa=���`a ���`caxs���`a[���bmia0���`a]���aoa.���`dhist���`a(���`edist1���`a,���`a ���`dbins���aoa=���`fn_bins���`a)���`a
���`a
���bc1x:# We'll color code by height, but you could use any scalar���`a
���`efracs���`a ���aoa=���`a ���`aN���`a ���aoa/���`a ���`aN���aoa.���`cmax���`a(���`a)���`a
���`a
���bc1xJ# we need to normalize the data to 0..1 for the full range of the colormap���`a
���`dnorm���`a ���aoa=���`a ���`fcolors���aoa.���`iNormalize���`a(���`efracs���aoa.���`cmin���`a(���`a)���`a,���`a ���`efracs���aoa.���`cmax���`a(���`a)���`a)���`a
���`a
���bc1xK# Now, we'll loop through our objects and set the color of each accordingly���`a
���akcfor���`a ���`hthisfrac���`a,���`a ���`ithispatch���`a ���bowbin���`a ���bnbczip���`a(���`efracs���`a,���`a ���`gpatches���`a)���`a:���`a
���`d    ���`ecolor���`a ���aoa=���`a ���`cplt���aoa.���`bcm���aoa.���`gviridis���`a(���`dnorm���`a(���`hthisfrac���`a)���`a)���`a
���`d    ���`ithispatch���aoa.���`mset_facecolor���`a(���`ecolor���`a)���`a
���`a
���bc1x@# We can also normalize our inputs by the total number of counts���`a
���`caxs���`a[���bmia1���`a]���aoa.���`dhist���`a(���`edist1���`a,���`a ���`dbins���aoa=���`fn_bins���`a,���`a ���`gdensity���aoa=���bkcdTrue���`a)���`a
���`a
���bc1x0# Now we format the y-axis to display percentage���`a
���`caxs���`a[���bmia1���`a]���aoa.���`eyaxis���aoa.���`sset_major_formatter���`a(���`pPercentFormatter���`a(���`dxmax���aoa=���bmia1���`a)���`a)���`a
���`a
���`a
���bc1xO###############################################################################���`a
���bc1u# Plot a 2D histogram���`a
���bc1u# -------------------���`a
���bc1a#���`a
���bc1xH# To plot a 2D histogram, one only needs two vectors of the same length,���`a
���bc1x.# corresponding to each axis of the histogram.���`a
���`a
���`cfig���`a,���`a ���`bax���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`ltight_layout���aoa=���bkcdTrue���`a)���`a
���`dhist���`a ���aoa=���`a ���`bax���aoa.���`fhist2d���`a(���`edist1���`a,���`a ���`edist2���`a)���`a
���`a
���`a
���bc1xO###############################################################################���`a
���bc1x# Customizing your histogram���`a
���bc1x# --------------------------���`a
���bc1a#���`a
���bc1xG# Customizing a 2D histogram is similar to the 1D case, you can control���`a
���bc1x@# visual components such as the bin size or color normalization.���`a
���`a
���`cfig���`a,���`a ���`caxs���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���bmia3���`a,���`a ���bmia1���`a,���`a ���`gfigsize���aoa=���`a(���bmia5���`a,���`a ���bmib15���`a)���`a,���`a ���`fsharex���aoa=���bkcdTrue���`a,���`a ���`fsharey���aoa=���bkcdTrue���`a,���`a
���`x                        ���`ltight_layout���aoa=���bkcdTrue���`a)���`a
���`a
���bc1x1# We can increase the number of bins on each axis���`a
���`caxs���`a[���bmia0���`a]���aoa.���`fhist2d���`a(���`edist1���`a,���`a ���`edist2���`a,���`a ���`dbins���aoa=���bmib40���`a)���`a
���`a
���bc1x/# As well as define normalization of the colors���`a
���`caxs���`a[���bmia1���`a]���aoa.���`fhist2d���`a(���`edist1���`a,���`a ���`edist2���`a,���`a ���`dbins���aoa=���bmib40���`a,���`a ���`dnorm���aoa=���`fcolors���aoa.���`gLogNorm���`a(���`a)���`a)���`a
���`a
���bc1x9# We can also define custom numbers of bins for each axis���`a
���`caxs���`a[���bmia2���`a]���aoa.���`fhist2d���`a(���`edist1���`a,���`a ���`edist2���`a,���`a ���`dbins���aoa=���`a(���bmib80���`a,���`a ���bmib10���`a)���`a,���`a ���`dnorm���aoa=���`fcolors���aoa.���`gLogNorm���`a(���`a)���`a)���`a
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
���bc1x=#    - `matplotlib.axes.Axes.hist` / `matplotlib.pyplot.hist`���`a
���bc1x!#    - `matplotlib.pyplot.hist2d`���`a
���bc1x+#    - `matplotlib.ticker.PercentFormatter`���`a
`dNone�