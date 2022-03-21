������������bsdy """
========
Boxplots
========

Visualizing boxplots with matplotlib.

The following examples show off how to visualize boxplots with
Matplotlib. There are many options to control their appearance and
the statistics that they use to summarize the data.
"""���`a
���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���bkndfrom���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnngpatches���`a ���bknfimport���`a ���`gPolygon���`a
���`a
���`a
���bc1x)# Fixing random state for reproducibility���`a
���`bnp���aoa.���`frandom���aoa.���`dseed���`a(���bmih19680801���`a)���`a
���`a
���bc1s# fake up some data���`a
���`fspread���`a ���aoa=���`a ���`bnp���aoa.���`frandom���aoa.���`drand���`a(���bmib50���`a)���`a ���aoa*���`a ���bmic100���`a
���`fcenter���`a ���aoa=���`a ���`bnp���aoa.���`dones���`a(���bmib25���`a)���`a ���aoa*���`a ���bmib50���`a
���`jflier_high���`a ���aoa=���`a ���`bnp���aoa.���`frandom���aoa.���`drand���`a(���bmib10���`a)���`a ���aoa*���`a ���bmic100���`a ���aoa+���`a ���bmic100���`a
���`iflier_low���`a ���aoa=���`a ���`bnp���aoa.���`frandom���aoa.���`drand���`a(���bmib10���`a)���`a ���aoa*���`a ���aoa-���bmic100���`a
���`ddata���`a ���aoa=���`a ���`bnp���aoa.���`kconcatenate���`a(���`a(���`fspread���`a,���`a ���`fcenter���`a,���`a ���`jflier_high���`a,���`a ���`iflier_low���`a)���`a)���`a
���`a
���`cfig���`a,���`a ���`caxs���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���bmia2���`a,���`a ���bmia3���`a)���`a
���`a
���bc1l# basic plot���`a
���`caxs���`a[���bmia0���`a,���`a ���bmia0���`a]���aoa.���`gboxplot���`a(���`ddata���`a)���`a
���`caxs���`a[���bmia0���`a,���`a ���bmia0���`a]���aoa.���`iset_title���`a(���bs1a'���bs1jbasic plot���bs1a'���`a)���`a
���`a
���bc1n# notched plot���`a
���`caxs���`a[���bmia0���`a,���`a ���bmia1���`a]���aoa.���`gboxplot���`a(���`ddata���`a,���`a ���bmia1���`a)���`a
���`caxs���`a[���bmia0���`a,���`a ���bmia1���`a]���aoa.���`iset_title���`a(���bs1a'���bs1lnotched plot���bs1a'���`a)���`a
���`a
���bc1x# change outlier point symbols���`a
���`caxs���`a[���bmia0���`a,���`a ���bmia2���`a]���aoa.���`gboxplot���`a(���`ddata���`a,���`a ���bmia0���`a,���`a ���bs1a'���bs1bgD���bs1a'���`a)���`a
���`caxs���`a[���bmia0���`a,���`a ���bmia2���`a]���aoa.���`iset_title���`a(���bs1a'���bs1nchange outlier���bseb\n���bs1mpoint symbols���bs1a'���`a)���`a
���`a
���bc1x# don't show outlier points���`a
���`caxs���`a[���bmia1���`a,���`a ���bmia0���`a]���aoa.���`gboxplot���`a(���`ddata���`a,���`a ���bmia0���`a,���`a ���bs1a'���bs1a'���`a)���`a
���`caxs���`a[���bmia1���`a,���`a ���bmia0���`a]���aoa.���`iset_title���`a(���bs2a"���bs2cdon���bs2a'���bs2ft show���bseb\n���bs2noutlier points���bs2a"���`a)���`a
���`a
���bc1r# horizontal boxes���`a
���`caxs���`a[���bmia1���`a,���`a ���bmia1���`a]���aoa.���`gboxplot���`a(���`ddata���`a,���`a ���bmia0���`a,���`a ���bs1a'���bs1brs���bs1a'���`a,���`a ���bmia0���`a)���`a
���`caxs���`a[���bmia1���`a,���`a ���bmia1���`a]���aoa.���`iset_title���`a(���bs1a'���bs1phorizontal boxes���bs1a'���`a)���`a
���`a
���bc1w# change whisker length���`a
���`caxs���`a[���bmia1���`a,���`a ���bmia2���`a]���aoa.���`gboxplot���`a(���`ddata���`a,���`a ���bmia0���`a,���`a ���bs1a'���bs1brs���bs1a'���`a,���`a ���bmia0���`a,���`a ���bmfd0.75���`a)���`a
���`caxs���`a[���bmia1���`a,���`a ���bmia2���`a]���aoa.���`iset_title���`a(���bs1a'���bs1uchange whisker length���bs1a'���`a)���`a
���`a
���`cfig���aoa.���`osubplots_adjust���`a(���`dleft���aoa=���bmfd0.08���`a,���`a ���`eright���aoa=���bmfd0.98���`a,���`a ���`fbottom���aoa=���bmfd0.05���`a,���`a ���`ctop���aoa=���bmfc0.9���`a,���`a
���`t                    ���`fhspace���aoa=���bmfc0.4���`a,���`a ���`fwspace���aoa=���bmfc0.3���`a)���`a
���`a
���bc1x# fake up some more data���`a
���`fspread���`a ���aoa=���`a ���`bnp���aoa.���`frandom���aoa.���`drand���`a(���bmib50���`a)���`a ���aoa*���`a ���bmic100���`a
���`fcenter���`a ���aoa=���`a ���`bnp���aoa.���`dones���`a(���bmib25���`a)���`a ���aoa*���`a ���bmib40���`a
���`jflier_high���`a ���aoa=���`a ���`bnp���aoa.���`frandom���aoa.���`drand���`a(���bmib10���`a)���`a ���aoa*���`a ���bmic100���`a ���aoa+���`a ���bmic100���`a
���`iflier_low���`a ���aoa=���`a ���`bnp���aoa.���`frandom���aoa.���`drand���`a(���bmib10���`a)���`a ���aoa*���`a ���aoa-���bmic100���`a
���`bd2���`a ���aoa=���`a ���`bnp���aoa.���`kconcatenate���`a(���`a(���`fspread���`a,���`a ���`fcenter���`a,���`a ���`jflier_high���`a,���`a ���`iflier_low���`a)���`a)���`a
���bc1x:# Making a 2-D array only works if all the columns are the���`a
���bc1x9# same length.  If they are not, then use a list instead.���`a
���bc1x:# This is actually more efficient because boxplot converts���`a
���bc1x7# a 2-D array into a list of vectors internally anyway.���`a
���`ddata���`a ���aoa=���`a ���`a[���`ddata���`a,���`a ���`bd2���`a,���`a ���`bd2���`a[���`a:���`a:���bmia2���`a]���`a]���`a
���`a
���bc1x # Multiple box plots on one Axes���`a
���`cfig���`a,���`a ���`bax���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`a)���`a
���`bax���aoa.���`gboxplot���`a(���`ddata���`a)���`a
���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
���`a
���`a
���bc1xO###############################################################################���`a
���bc1xJ# Below we'll generate data from five different probability distributions,���`a
���bc1xF# each with different characteristics. We want to play with how an IID���`a
���bc1x=# bootstrap resample of the data preserves the distributional���`a
���bc1xE# properties of the original sample, and a boxplot is one visual tool���`a
���bc1x# to make this assessment���`a
���`a
���`lrandom_dists���`a ���aoa=���`a ���`a[���bs1a'���bs1lNormal(1, 1)���bs1a'���`a,���`a ���bs1a'���bs1oLognormal(1, 1)���bs1a'���`a,���`a ���bs1a'���bs1fExp(1)���bs1a'���`a,���`a ���bs1a'���bs1lGumbel(6, 4)���bs1a'���`a,���`a
���`p                ���bs1a'���bs1tTriangular(2, 9, 11)���bs1a'���`a]���`a
���`aN���`a ���aoa=���`a ���bmic500���`a
���`a
���`dnorm���`a ���aoa=���`a ���`bnp���aoa.���`frandom���aoa.���`fnormal���`a(���bmia1���`a,���`a ���bmia1���`a,���`a ���`aN���`a)���`a
���`dlogn���`a ���aoa=���`a ���`bnp���aoa.���`frandom���aoa.���`ilognormal���`a(���bmia1���`a,���`a ���bmia1���`a,���`a ���`aN���`a)���`a
���`dexpo���`a ���aoa=���`a ���`bnp���aoa.���`frandom���aoa.���`kexponential���`a(���bmia1���`a,���`a ���`aN���`a)���`a
���`dgumb���`a ���aoa=���`a ���`bnp���aoa.���`frandom���aoa.���`fgumbel���`a(���bmia6���`a,���`a ���bmia4���`a,���`a ���`aN���`a)���`a
���`dtria���`a ���aoa=���`a ���`bnp���aoa.���`frandom���aoa.���`jtriangular���`a(���bmia2���`a,���`a ���bmia9���`a,���`a ���bmib11���`a,���`a ���`aN���`a)���`a
���`a
���bc1xK# Generate some random indices that we'll use to resample the original data���`a
���bc1xK# arrays. For code brevity, just use the same random indices for each array���`a
���`qbootstrap_indices���`a ���aoa=���`a ���`bnp���aoa.���`frandom���aoa.���`grandint���`a(���bmia0���`a,���`a ���`aN���`a,���`a ���`aN���`a)���`a
���`ddata���`a ���aoa=���`a ���`a[���`a
���`d    ���`dnorm���`a,���`a ���`dnorm���`a[���`qbootstrap_indices���`a]���`a,���`a
���`d    ���`dlogn���`a,���`a ���`dlogn���`a[���`qbootstrap_indices���`a]���`a,���`a
���`d    ���`dexpo���`a,���`a ���`dexpo���`a[���`qbootstrap_indices���`a]���`a,���`a
���`d    ���`dgumb���`a,���`a ���`dgumb���`a[���`qbootstrap_indices���`a]���`a,���`a
���`d    ���`dtria���`a,���`a ���`dtria���`a[���`qbootstrap_indices���`a]���`a,���`a
���`a]���`a
���`a
���`cfig���`a,���`a ���`cax1���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`gfigsize���aoa=���`a(���bmib10���`a,���`a ���bmia6���`a)���`a)���`a
���`cfig���aoa.���`fcanvas���aoa.���`gmanager���aoa.���`pset_window_title���`a(���bs1a'���bs1qA Boxplot Example���bs1a'���`a)���`a
���`cfig���aoa.���`osubplots_adjust���`a(���`dleft���aoa=���bmfe0.075���`a,���`a ���`eright���aoa=���bmfd0.95���`a,���`a ���`ctop���aoa=���bmfc0.9���`a,���`a ���`fbottom���aoa=���bmfd0.25���`a)���`a
���`a
���`bbp���`a ���aoa=���`a ���`cax1���aoa.���`gboxplot���`a(���`ddata���`a,���`a ���`enotch���aoa=���bmia0���`a,���`a ���`csym���aoa=���bs1a'���bs1a+���bs1a'���`a,���`a ���`dvert���aoa=���bmia1���`a,���`a ���`dwhis���aoa=���bmfc1.5���`a)���`a
���`cplt���aoa.���`dsetp���`a(���`bbp���`a[���bs1a'���bs1eboxes���bs1a'���`a]���`a,���`a ���`ecolor���aoa=���bs1a'���bs1eblack���bs1a'���`a)���`a
���`cplt���aoa.���`dsetp���`a(���`bbp���`a[���bs1a'���bs1hwhiskers���bs1a'���`a]���`a,���`a ���`ecolor���aoa=���bs1a'���bs1eblack���bs1a'���`a)���`a
���`cplt���aoa.���`dsetp���`a(���`bbp���`a[���bs1a'���bs1ffliers���bs1a'���`a]���`a,���`a ���`ecolor���aoa=���bs1a'���bs1cred���bs1a'���`a,���`a ���`fmarker���aoa=���bs1a'���bs1a+���bs1a'���`a)���`a
���`a
���bc1xD# Add a horizontal grid to the plot, but make it very light in color���`a
���bc1xA# so we can use it for reading data values but not be distracting���`a
���`cax1���aoa.���`eyaxis���aoa.���`dgrid���`a(���bkcdTrue���`a,���`a ���`ilinestyle���aoa=���bs1a'���bs1a-���bs1a'���`a,���`a ���`ewhich���aoa=���bs1a'���bs1emajor���bs1a'���`a,���`a ���`ecolor���aoa=���bs1a'���bs1ilightgrey���bs1a'���`a,���`a
���`o               ���`ealpha���aoa=���bmfc0.5���`a)���`a
���`a
���`cax1���aoa.���`cset���`a(���`a
���`d    ���`iaxisbelow���aoa=���bkcdTrue���`a,���`b  ���bc1x## Hide the grid behind plot objects���`a
���`d    ���`etitle���aoa=���bs1a'���bs1x@Comparison of IID Bootstrap Resampling Across Five Distributions���bs1a'���`a,���`a
���`d    ���`fxlabel���aoa=���bs1a'���bs1lDistribution���bs1a'���`a,���`a
���`d    ���`fylabel���aoa=���bs1a'���bs1eValue���bs1a'���`a,���`a
���`a)���`a
���`a
���bc1x(# Now fill the boxes with desired colors���`a
���`jbox_colors���`a ���aoa=���`a ���`a[���bs1a'���bs1idarkkhaki���bs1a'���`a,���`a ���bs1a'���bs1iroyalblue���bs1a'���`a]���`a
���`inum_boxes���`a ���aoa=���`a ���bnbclen���`a(���`ddata���`a)���`a
���`gmedians���`a ���aoa=���`a ���`bnp���aoa.���`eempty���`a(���`inum_boxes���`a)���`a
���akcfor���`a ���`ai���`a ���bowbin���`a ���bnberange���`a(���`inum_boxes���`a)���`a:���`a
���`d    ���`cbox���`a ���aoa=���`a ���`bbp���`a[���bs1a'���bs1eboxes���bs1a'���`a]���`a[���`ai���`a]���`a
���`d    ���`ebox_x���`a ���aoa=���`a ���`a[���`a]���`a
���`d    ���`ebox_y���`a ���aoa=���`a ���`a[���`a]���`a
���`d    ���akcfor���`a ���`aj���`a ���bowbin���`a ���bnberange���`a(���bmia5���`a)���`a:���`a
���`h        ���`ebox_x���aoa.���`fappend���`a(���`cbox���aoa.���`iget_xdata���`a(���`a)���`a[���`aj���`a]���`a)���`a
���`h        ���`ebox_y���aoa.���`fappend���`a(���`cbox���aoa.���`iget_ydata���`a(���`a)���`a[���`aj���`a]���`a)���`a
���`d    ���`jbox_coords���`a ���aoa=���`a ���`bnp���aoa.���`lcolumn_stack���`a(���`a[���`ebox_x���`a,���`a ���`ebox_y���`a]���`a)���`a
���`d    ���bc1x-# Alternate between Dark Khaki and Royal Blue���`a
���`d    ���`cax1���aoa.���`iadd_patch���`a(���`gPolygon���`a(���`jbox_coords���`a,���`a ���`ifacecolor���aoa=���`jbox_colors���`a[���`ai���`a ���aoa%���`a ���bmia2���`a]���`a)���`a)���`a
���`d    ���bc1x<# Now draw the median lines back over what we just filled in���`a
���`d    ���`cmed���`a ���aoa=���`a ���`bbp���`a[���bs1a'���bs1gmedians���bs1a'���`a]���`a[���`ai���`a]���`a
���`d    ���`hmedian_x���`a ���aoa=���`a ���`a[���`a]���`a
���`d    ���`hmedian_y���`a ���aoa=���`a ���`a[���`a]���`a
���`d    ���akcfor���`a ���`aj���`a ���bowbin���`a ���bnberange���`a(���bmia2���`a)���`a:���`a
���`h        ���`hmedian_x���aoa.���`fappend���`a(���`cmed���aoa.���`iget_xdata���`a(���`a)���`a[���`aj���`a]���`a)���`a
���`h        ���`hmedian_y���aoa.���`fappend���`a(���`cmed���aoa.���`iget_ydata���`a(���`a)���`a[���`aj���`a]���`a)���`a
���`h        ���`cax1���aoa.���`dplot���`a(���`hmedian_x���`a,���`a ���`hmedian_y���`a,���`a ���bs1a'���bs1ak���bs1a'���`a)���`a
���`d    ���`gmedians���`a[���`ai���`a]���`a ���aoa=���`a ���`hmedian_y���`a[���bmia0���`a]���`a
���`d    ���bc1xB# Finally, overplot the sample averages, with horizontal alignment���`a
���`d    ���bc1x# in the center of each box���`a
���`d    ���`cax1���aoa.���`dplot���`a(���`bnp���aoa.���`gaverage���`a(���`cmed���aoa.���`iget_xdata���`a(���`a)���`a)���`a,���`a ���`bnp���aoa.���`gaverage���`a(���`ddata���`a[���`ai���`a]���`a)���`a,���`a
���`m             ���`ecolor���aoa=���bs1a'���bs1aw���bs1a'���`a,���`a ���`fmarker���aoa=���bs1a'���bs1a*���bs1a'���`a,���`a ���`omarkeredgecolor���aoa=���bs1a'���bs1ak���bs1a'���`a)���`a
���`a
���bc1x%# Set the axes ranges and axes labels���`a
���`cax1���aoa.���`hset_xlim���`a(���bmfc0.5���`a,���`a ���`inum_boxes���`a ���aoa+���`a ���bmfc0.5���`a)���`a
���`ctop���`a ���aoa=���`a ���bmib40���`a
���`fbottom���`a ���aoa=���`a ���aoa-���bmia5���`a
���`cax1���aoa.���`hset_ylim���`a(���`fbottom���`a,���`a ���`ctop���`a)���`a
���`cax1���aoa.���`oset_xticklabels���`a(���`bnp���aoa.���`frepeat���`a(���`lrandom_dists���`a,���`a ���bmia2���`a)���`a,���`a
���`t                    ���`hrotation���aoa=���bmib45���`a,���`a ���`hfontsize���aoa=���bmia8���`a)���`a
���`a
���bc1xC# Due to the Y-axis scale being different across samples, it can be���`a
���bc1xF# hard to compare differences in medians across the samples. Add upper���`a
���bc1xA# X-axis tick labels with the sample medians to aid in comparison���`a
���bc1x,# (just use two decimal places of precision)���`a
���`cpos���`a ���aoa=���`a ���`bnp���aoa.���`farange���`a(���`inum_boxes���`a)���`a ���aoa+���`a ���bmia1���`a
���`lupper_labels���`a ���aoa=���`a ���`a[���bnbcstr���`a(���bnberound���`a(���`as���`a,���`a ���bmia2���`a)���`a)���`a ���akcfor���`a ���`as���`a ���bowbin���`a ���`gmedians���`a]���`a
���`gweights���`a ���aoa=���`a ���`a[���bs1a'���bs1dbold���bs1a'���`a,���`a ���bs1a'���bs1hsemibold���bs1a'���`a]���`a
���akcfor���`a ���`dtick���`a,���`a ���`elabel���`a ���bowbin���`a ���bnbczip���`a(���bnberange���`a(���`inum_boxes���`a)���`a,���`a ���`cax1���aoa.���`oget_xticklabels���`a(���`a)���`a)���`a:���`a
���`d    ���`ak���`a ���aoa=���`a ���`dtick���`a ���aoa%���`a ���bmia2���`a
���`d    ���`cax1���aoa.���`dtext���`a(���`cpos���`a[���`dtick���`a]���`a,���`a ���bmfc.95���`a,���`a ���`lupper_labels���`a[���`dtick���`a]���`a,���`a
���`m             ���`itransform���aoa=���`cax1���aoa.���`sget_xaxis_transform���`a(���`a)���`a,���`a
���`m             ���`shorizontalalignment���aoa=���bs1a'���bs1fcenter���bs1a'���`a,���`a ���`dsize���aoa=���bs1a'���bs1gx-small���bs1a'���`a,���`a
���`m             ���`fweight���aoa=���`gweights���`a[���`ak���`a]���`a,���`a ���`ecolor���aoa=���`jbox_colors���`a[���`ak���`a]���`a)���`a
���`a
���bc1x# Finally, add a basic legend���`a
���`cfig���aoa.���`dtext���`a(���bmfd0.80���`a,���`a ���bmfd0.08���`a,���`a ���bsaaf���bs1a'���bsia{���`aN���bsia}���bs1o Random Numbers���bs1a'���`a,���`a
���`i         ���`obackgroundcolor���aoa=���`jbox_colors���`a[���bmia0���`a]���`a,���`a ���`ecolor���aoa=���bs1a'���bs1eblack���bs1a'���`a,���`a ���`fweight���aoa=���bs1a'���bs1eroman���bs1a'���`a,���`a
���`i         ���`dsize���aoa=���bs1a'���bs1gx-small���bs1a'���`a)���`a
���`cfig���aoa.���`dtext���`a(���bmfd0.80���`a,���`a ���bmfe0.045���`a,���`a ���bs1a'���bs1vIID Bootstrap Resample���bs1a'���`a,���`a
���`i         ���`obackgroundcolor���aoa=���`jbox_colors���`a[���bmia1���`a]���`a,���`a
���`i         ���`ecolor���aoa=���bs1a'���bs1ewhite���bs1a'���`a,���`a ���`fweight���aoa=���bs1a'���bs1eroman���bs1a'���`a,���`a ���`dsize���aoa=���bs1a'���bs1gx-small���bs1a'���`a)���`a
���`cfig���aoa.���`dtext���`a(���bmfd0.80���`a,���`a ���bmfe0.015���`a,���`a ���bs1a'���bs1a*���bs1a'���`a,���`a ���`ecolor���aoa=���bs1a'���bs1ewhite���bs1a'���`a,���`a ���`obackgroundcolor���aoa=���bs1a'���bs1fsilver���bs1a'���`a,���`a
���`i         ���`fweight���aoa=���bs1a'���bs1eroman���bs1a'���`a,���`a ���`dsize���aoa=���bs1a'���bs1fmedium���bs1a'���`a)���`a
���`cfig���aoa.���`dtext���`a(���bmfe0.815���`a,���`a ���bmfe0.013���`a,���`a ���bs1a'���bs1n Average Value���bs1a'���`a,���`a ���`ecolor���aoa=���bs1a'���bs1eblack���bs1a'���`a,���`a ���`fweight���aoa=���bs1a'���bs1eroman���bs1a'���`a,���`a
���`i         ���`dsize���aoa=���bs1a'���bs1gx-small���bs1a'���`a)���`a
���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
���`a
���bc1xO###############################################################################���`a
���bc1xD# Here we write a custom function to bootstrap confidence intervals.���`a
���bc1xO# We can then use the boxplot along with this function to show these intervals.���`a
���`a
���`a
���akcdef���`a ���bnfqfake_bootstrapper���`a(���`an���`a)���`a:���`a
���`d    ���bsdx�"""
    This is just a placeholder for the user's method of
    bootstrapping the median and its confidence intervals.

    Returns an arbitrary median and confidence interval packed into a tuple.
    """���`a
���`d    ���akbif���`a ���`an���`a ���aob==���`a ���bmia1���`a:���`a
���`h        ���`cmed���`a ���aoa=���`a ���bmfc0.1���`a
���`h        ���`bci���`a ���aoa=���`a ���`a(���aoa-���bmfd0.25���`a,���`a ���bmfd0.25���`a)���`a
���`d    ���akdelse���`a:���`a
���`h        ���`cmed���`a ���aoa=���`a ���bmfc0.2���`a
���`h        ���`bci���`a ���aoa=���`a ���`a(���aoa-���bmfd0.35���`a,���`a ���bmfd0.50���`a)���`a
���`d    ���akfreturn���`a ���`cmed���`a,���`a ���`bci���`a
���`a
���`cinc���`a ���aoa=���`a ���bmfc0.1���`a
���`be1���`a ���aoa=���`a ���`bnp���aoa.���`frandom���aoa.���`fnormal���`a(���bmia0���`a,���`a ���bmia1���`a,���`a ���`dsize���aoa=���bmic500���`a)���`a
���`be2���`a ���aoa=���`a ���`bnp���aoa.���`frandom���aoa.���`fnormal���`a(���bmia0���`a,���`a ���bmia1���`a,���`a ���`dsize���aoa=���bmic500���`a)���`a
���`be3���`a ���aoa=���`a ���`bnp���aoa.���`frandom���aoa.���`fnormal���`a(���bmia0���`a,���`a ���bmia1���`a ���aoa+���`a ���`cinc���`a,���`a ���`dsize���aoa=���bmic500���`a)���`a
���`be4���`a ���aoa=���`a ���`bnp���aoa.���`frandom���aoa.���`fnormal���`a(���bmia0���`a,���`a ���bmia1���`a ���aoa+���`a ���bmia2���aoa*���`cinc���`a,���`a ���`dsize���aoa=���bmic500���`a)���`a
���`a
���`jtreatments���`a ���aoa=���`a ���`a[���`be1���`a,���`a ���`be2���`a,���`a ���`be3���`a,���`a ���`be4���`a]���`a
���`dmed1���`a,���`a ���`cci1���`a ���aoa=���`a ���`qfake_bootstrapper���`a(���bmia1���`a)���`a
���`dmed2���`a,���`a ���`cci2���`a ���aoa=���`a ���`qfake_bootstrapper���`a(���bmia2���`a)���`a
���`gmedians���`a ���aoa=���`a ���`a[���bkcdNone���`a,���`a ���bkcdNone���`a,���`a ���`dmed1���`a,���`a ���`dmed2���`a]���`a
���`nconf_intervals���`a ���aoa=���`a ���`a[���bkcdNone���`a,���`a ���bkcdNone���`a,���`a ���`cci1���`a,���`a ���`cci2���`a]���`a
���`a
���`cfig���`a,���`a ���`bax���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`a)���`a
���`cpos���`a ���aoa=���`a ���`bnp���aoa.���`farange���`a(���bnbclen���`a(���`jtreatments���`a)���`a)���`a ���aoa+���`a ���bmia1���`a
���`bbp���`a ���aoa=���`a ���`bax���aoa.���`gboxplot���`a(���`jtreatments���`a,���`a ���`csym���aoa=���bs1a'���bs1bk+���bs1a'���`a,���`a ���`ipositions���aoa=���`cpos���`a,���`a
���`p                ���`enotch���aoa=���bmia1���`a,���`a ���`ibootstrap���aoa=���bmid5000���`a,���`a
���`p                ���`kusermedians���aoa=���`gmedians���`a,���`a
���`p                ���`nconf_intervals���aoa=���`nconf_intervals���`a)���`a
���`a
���`bax���aoa.���`jset_xlabel���`a(���bs1a'���bs1itreatment���bs1a'���`a)���`a
���`bax���aoa.���`jset_ylabel���`a(���bs1a'���bs1hresponse���bs1a'���`a)���`a
���`cplt���aoa.���`dsetp���`a(���`bbp���`a[���bs1a'���bs1hwhiskers���bs1a'���`a]���`a,���`a ���`ecolor���aoa=���bs1a'���bs1ak���bs1a'���`a,���`a ���`ilinestyle���aoa=���bs1a'���bs1a-���bs1a'���`a)���`a
���`cplt���aoa.���`dsetp���`a(���`bbp���`a[���bs1a'���bs1ffliers���bs1a'���`a]���`a,���`a ���`jmarkersize���aoa=���bmfc3.0���`a)���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
���`a
���bc1xM#############################################################################���`a
���bc1a#���`a
���bc1x# .. admonition:: References���`a
���bc1a#���`a
���bc1xN#    The use of the following functions, methods, classes and modules is shown���`a
���bc1u#    in this example:���`a
���bc1a#���`a
���bc1xC#    - `matplotlib.axes.Axes.boxplot` / `matplotlib.pyplot.boxplot`���`a
���bc1x@#    - `matplotlib.artist.Artist.set` / `matplotlib.pyplot.setp`���`a
`dNone�