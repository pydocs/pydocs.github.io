�����������bsdy�"""
==========================================
Blend transparency with color in 2D images
==========================================

Blend transparency with color to highlight parts of data with imshow.

A common use for `matplotlib.pyplot.imshow` is to plot a 2D statistical
map. The function makes it easy to visualize a 2D matrix as an image and add
transparency to the output. For example, one can plot a statistic (such as a
t-statistic) and color the transparency of each pixel according to its p-value.
This example demonstrates how you can achieve this effect.

First we will generate some data, in this case, we'll create two 2D "blobs"
in a 2D grid. One blob will be positive, and the other negative.
"""���`a
���`a
���bc1x%# sphinx_gallery_thumbnail_number = 3���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���bkndfrom���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfcolors���`a ���bknfimport���`a ���`iNormalize���`a
���`a
���`a
���akcdef���`a ���bnfjnormal_pdf���`a(���`ax���`a,���`a ���`dmean���`a,���`a ���`cvar���`a)���`a:���`a
���`d    ���akfreturn���`a ���`bnp���aoa.���`cexp���`a(���aoa-���`a(���`ax���`a ���aoa-���`a ���`dmean���`a)���aoa*���aoa*���bmia2���`a ���aoa/���`a ���`a(���bmia2���aoa*���`cvar���`a)���`a)���`a
���`a
���`a
���bc1x1# Generate the space in which the blobs will live���`a
���`dxmin���`a,���`a ���`dxmax���`a,���`a ���`dymin���`a,���`a ���`dymax���`a ���aoa=���`a ���`a(���bmia0���`a,���`a ���bmic100���`a,���`a ���bmia0���`a,���`a ���bmic100���`a)���`a
���`fn_bins���`a ���aoa=���`a ���bmic100���`a
���`bxx���`a ���aoa=���`a ���`bnp���aoa.���`hlinspace���`a(���`dxmin���`a,���`a ���`dxmax���`a,���`a ���`fn_bins���`a)���`a
���`byy���`a ���aoa=���`a ���`bnp���aoa.���`hlinspace���`a(���`dymin���`a,���`a ���`dymax���`a,���`a ���`fn_bins���`a)���`a
���`a
���bc1xH# Generate the blobs. The range of the values is roughly -.0002 to .0002���`a
���`jmeans_high���`a ���aoa=���`a ���`a[���bmib20���`a,���`a ���bmib50���`a]���`a
���`imeans_low���`a ���aoa=���`a ���`a[���bmib50���`a,���`a ���bmib60���`a]���`a
���`cvar���`a ���aoa=���`a ���`a[���bmic150���`a,���`a ���bmic200���`a]���`a
���`a
���`lgauss_x_high���`a ���aoa=���`a ���`jnormal_pdf���`a(���`bxx���`a,���`a ���`jmeans_high���`a[���bmia0���`a]���`a,���`a ���`cvar���`a[���bmia0���`a]���`a)���`a
���`lgauss_y_high���`a ���aoa=���`a ���`jnormal_pdf���`a(���`byy���`a,���`a ���`jmeans_high���`a[���bmia1���`a]���`a,���`a ���`cvar���`a[���bmia0���`a]���`a)���`a
���`a
���`kgauss_x_low���`a ���aoa=���`a ���`jnormal_pdf���`a(���`bxx���`a,���`a ���`imeans_low���`a[���bmia0���`a]���`a,���`a ���`cvar���`a[���bmia1���`a]���`a)���`a
���`kgauss_y_low���`a ���aoa=���`a ���`jnormal_pdf���`a(���`byy���`a,���`a ���`imeans_low���`a[���bmia1���`a]���`a,���`a ���`cvar���`a[���bmia1���`a]���`a)���`a
���`a
���`gweights���`a ���aoa=���`a ���`a(���`bnp���aoa.���`eouter���`a(���`lgauss_y_high���`a,���`a ���`lgauss_x_high���`a)���`a
���`k           ���aoa-���`a ���`bnp���aoa.���`eouter���`a(���`kgauss_y_low���`a,���`a ���`kgauss_x_low���`a)���`a)���`a
���`a
���bc1xE# We'll also create a grey background into which the pixels will fade���`a
���`egreys���`a ���aoa=���`a ���`bnp���aoa.���`dfull���`a(���`a(���aoa*���`gweights���aoa.���`eshape���`a,���`a ���bmia3���`a)���`a,���`a ���bmib70���`a,���`a ���`edtype���aoa=���`bnp���aoa.���`euint8���`a)���`a
���`a
���bc1xE# First we'll plot these blobs using ``imshow`` without transparency.���`a
���`dvmax���`a ���aoa=���`a ���`bnp���aoa.���`cabs���`a(���`gweights���`a)���aoa.���`cmax���`a(���`a)���`a
���`mimshow_kwargs���`a ���aoa=���`a ���`a{���`a
���`d    ���bs1a'���bs1dvmax���bs1a'���`a:���`a ���`dvmax���`a,���`a
���`d    ���bs1a'���bs1dvmin���bs1a'���`a:���`a ���aoa-���`dvmax���`a,���`a
���`d    ���bs1a'���bs1dcmap���bs1a'���`a:���`a ���bs1a'���bs1fRdYlBu���bs1a'���`a,���`a
���`d    ���bs1a'���bs1fextent���bs1a'���`a:���`a ���`a(���`dxmin���`a,���`a ���`dxmax���`a,���`a ���`dymin���`a,���`a ���`dymax���`a)���`a,���`a
���`a}���`a
���`a
���`cfig���`a,���`a ���`bax���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`a)���`a
���`bax���aoa.���`fimshow���`a(���`egreys���`a)���`a
���`bax���aoa.���`fimshow���`a(���`gweights���`a,���`a ���aoa*���aoa*���`mimshow_kwargs���`a)���`a
���`bax���aoa.���`lset_axis_off���`a(���`a)���`a
���`a
���bc1xO###############################################################################���`a
���bc1x# Blending in transparency���`a
���bc1x# ========================���`a
���bc1a#���`a
���bc1xB# The simplest way to include transparency when plotting data with���`a
���bc1xF# `matplotlib.pyplot.imshow` is to pass an array matching the shape of���`a
���bc1xJ# the data to the ``alpha`` argument. For example, we'll create a gradient���`a
���bc1x"# moving from left to right below.���`a
���`a
���bc1xL# Create an alpha channel of linearly increasing values moving to the right.���`a
���`falphas���`a ���aoa=���`a ���`bnp���aoa.���`dones���`a(���`gweights���aoa.���`eshape���`a)���`a
���`falphas���`a[���`a:���`a,���`a ���bmib30���`a:���`a]���`a ���aoa=���`a ���`bnp���aoa.���`hlinspace���`a(���bmia1���`a,���`a ���bmia0���`a,���`a ���bmib70���`a)���`a
���`a
���bc1x# Create the figure and image���`a
���bc1x9# Note that the absolute values may be slightly different���`a
���`cfig���`a,���`a ���`bax���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`a)���`a
���`bax���aoa.���`fimshow���`a(���`egreys���`a)���`a
���`bax���aoa.���`fimshow���`a(���`gweights���`a,���`a ���`ealpha���aoa=���`falphas���`a,���`a ���aoa*���aoa*���`mimshow_kwargs���`a)���`a
���`bax���aoa.���`lset_axis_off���`a(���`a)���`a
���`a
���bc1xO###############################################################################���`a
���bc1x<# Using transparency to highlight values with high amplitude���`a
���bc1x<# ==========================================================���`a
���bc1a#���`a
���bc1xM# Finally, we'll recreate the same plot, but this time we'll use transparency���`a
���bc1xN# to highlight the extreme values in the data. This is often used to highlight���`a
���bc1xG# data points with smaller p-values. We'll also add in contour lines to���`a
���bc1x# highlight the image values.���`a
���`a
���bc1x0# Create an alpha channel based on weight values���`a
���bc1xG# Any value whose absolute value is > .0001 will have zero transparency���`a
���`falphas���`a ���aoa=���`a ���`iNormalize���`a(���bmia0���`a,���`a ���bmfb.3���`a,���`a ���`dclip���aoa=���bkcdTrue���`a)���`a(���`bnp���aoa.���`cabs���`a(���`gweights���`a)���`a)���`a
���`falphas���`a ���aoa=���`a ���`bnp���aoa.���`dclip���`a(���`falphas���`a,���`a ���bmfb.4���`a,���`a ���bmia1���`a)���`b  ���bc1x)# alpha value clipped at the bottom at .4���`a
���`a
���bc1x# Create the figure and image���`a
���bc1x9# Note that the absolute values may be slightly different���`a
���`cfig���`a,���`a ���`bax���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`a)���`a
���`bax���aoa.���`fimshow���`a(���`egreys���`a)���`a
���`bax���aoa.���`fimshow���`a(���`gweights���`a,���`a ���`ealpha���aoa=���`falphas���`a,���`a ���aoa*���aoa*���`mimshow_kwargs���`a)���`a
���`a
���bc1x:# Add contour lines to further highlight different levels.���`a
���`bax���aoa.���`gcontour���`a(���`gweights���`a[���`a:���`a:���aoa-���bmia1���`a]���`a,���`a ���`flevels���aoa=���`a[���aoa-���bmfb.1���`a,���`a ���bmfb.1���`a]���`a,���`a ���`fcolors���aoa=���bs1a'���bs1ak���bs1a'���`a,���`a ���`jlinestyles���aoa=���bs1a'���bs1a-���bs1a'���`a)���`a
���`bax���aoa.���`lset_axis_off���`a(���`a)���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
���`a
���`bax���aoa.���`gcontour���`a(���`gweights���`a[���`a:���`a:���aoa-���bmia1���`a]���`a,���`a ���`flevels���aoa=���`a[���aoa-���bmfe.0001���`a,���`a ���bmfe.0001���`a]���`a,���`a ���`fcolors���aoa=���bs1a'���bs1ak���bs1a'���`a,���`a ���`jlinestyles���aoa=���bs1a'���bs1a-���bs1a'���`a)���`a
���`bax���aoa.���`lset_axis_off���`a(���`a)���`a
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
���bc1xC#    - `matplotlib.axes.Axes.contour` / `matplotlib.pyplot.contour`���`a
���bc1x$#    - `matplotlib.colors.Normalize`���`a
���bc1x*#    - `matplotlib.axes.Axes.set_axis_off`���`a
`dNone�