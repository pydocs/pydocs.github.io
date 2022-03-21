������������bsdxm"""
===========
Multi Image
===========

Make a set of images with a single colormap, norm, and colorbar.
"""���`a
���`a
���bkndfrom���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����`a ���bknfimport���`a ���`fcolors���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���`a
���`bnp���aoa.���`frandom���aoa.���`dseed���`a(���bmih19680801���`a)���`a
���`bNr���`a ���aoa=���`a ���bmia3���`a
���`bNc���`a ���aoa=���`a ���bmia2���`a
���`a
���`cfig���`a,���`a ���`caxs���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`bNr���`a,���`a ���`bNc���`a)���`a
���`cfig���aoa.���`hsuptitle���`a(���bs1a'���bs1oMultiple images���bs1a'���`a)���`a
���`a
���`fimages���`a ���aoa=���`a ���`a[���`a]���`a
���akcfor���`a ���`ai���`a ���bowbin���`a ���bnberange���`a(���`bNr���`a)���`a:���`a
���`d    ���akcfor���`a ���`aj���`a ���bowbin���`a ���bnberange���`a(���`bNc���`a)���`a:���`a
���`h        ���bc1xC# Generate data with a range that varies from one plot to the next.���`a
���`h        ���`ddata���`a ���aoa=���`a ���`a(���`a(���bmia1���`a ���aoa+���`a ���`ai���`a ���aoa+���`a ���`aj���`a)���`a ���aoa/���`a ���bmib10���`a)���`a ���aoa*���`a ���`bnp���aoa.���`frandom���aoa.���`drand���`a(���bmib10���`a,���`a ���bmib20���`a)���`a
���`h        ���`fimages���aoa.���`fappend���`a(���`caxs���`a[���`ai���`a,���`a ���`aj���`a]���aoa.���`fimshow���`a(���`ddata���`a)���`a)���`a
���`h        ���`caxs���`a[���`ai���`a,���`a ���`aj���`a]���aoa.���`klabel_outer���`a(���`a)���`a
���`a
���bc1xH# Find the min and max of all colors for use in setting the color scale.���`a
���`dvmin���`a ���aoa=���`a ���bnbcmin���`a(���`eimage���aoa.���`iget_array���`a(���`a)���aoa.���`cmin���`a(���`a)���`a ���akcfor���`a ���`eimage���`a ���bowbin���`a ���`fimages���`a)���`a
���`dvmax���`a ���aoa=���`a ���bnbcmax���`a(���`eimage���aoa.���`iget_array���`a(���`a)���aoa.���`cmax���`a(���`a)���`a ���akcfor���`a ���`eimage���`a ���bowbin���`a ���`fimages���`a)���`a
���`dnorm���`a ���aoa=���`a ���`fcolors���aoa.���`iNormalize���`a(���`dvmin���aoa=���`dvmin���`a,���`a ���`dvmax���aoa=���`dvmax���`a)���`a
���akcfor���`a ���`bim���`a ���bowbin���`a ���`fimages���`a:���`a
���`d    ���`bim���aoa.���`hset_norm���`a(���`dnorm���`a)���`a
���`a
���`cfig���aoa.���`hcolorbar���`a(���`fimages���`a[���bmia0���`a]���`a,���`a ���`bax���aoa=���`caxs���`a,���`a ���`korientation���aoa=���bs1a'���bs1jhorizontal���bs1a'���`a,���`a ���`hfraction���aoa=���bmfb.1���`a)���`a
���`a
���`a
���bc1xJ# Make images respond to changes in the norm of other images (e.g. via the���`a
���bc1xM# "edit axis, curves and images parameters" GUI on Qt), but be careful not to���`a
���bc1u# recurse infinitely!���`a
���akcdef���`a ���bnffupdate���`a(���`mchanged_image���`a)���`a:���`a
���`d    ���akcfor���`a ���`bim���`a ���bowbin���`a ���`fimages���`a:���`a
���`h        ���akbif���`a ���`a(���`mchanged_image���aoa.���`hget_cmap���`a(���`a)���`a ���aob!=���`a ���`bim���aoa.���`hget_cmap���`a(���`a)���`a
���`p                ���bowbor���`a ���`mchanged_image���aoa.���`hget_clim���`a(���`a)���`a ���aob!=���`a ���`bim���aoa.���`hget_clim���`a(���`a)���`a)���`a:���`a
���`l            ���`bim���aoa.���`hset_cmap���`a(���`mchanged_image���aoa.���`hget_cmap���`a(���`a)���`a)���`a
���`l            ���`bim���aoa.���`hset_clim���`a(���`mchanged_image���aoa.���`hget_clim���`a(���`a)���`a)���`a
���`a
���`a
���akcfor���`a ���`bim���`a ���bowbin���`a ���`fimages���`a:���`a
���`d    ���`bim���aoa.���`icallbacks���aoa.���`gconnect���`a(���bs1a'���bs1gchanged���bs1a'���`a,���`a ���`fupdate���`a)���`a
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
���bc1xA#    - `matplotlib.axes.Axes.imshow` / `matplotlib.pyplot.imshow`���`a
���bc1xI#    - `matplotlib.figure.Figure.colorbar` / `matplotlib.pyplot.colorbar`���`a
���bc1x$#    - `matplotlib.colors.Normalize`���`a
���bc1x.#    - `matplotlib.cm.ScalarMappable.set_cmap`���`a
���bc1x.#    - `matplotlib.cm.ScalarMappable.set_norm`���`a
���bc1x.#    - `matplotlib.cm.ScalarMappable.set_clim`���`a
���bc1x2#    - `matplotlib.cbook.CallbackRegistry.connect`���`a
`dNone�