������������bsdys"""
======================================
Thresholding an Image with RangeSlider
======================================

Using the RangeSlider widget to control the thresholding of an image.

The RangeSlider widget can be used similarly to the `.widgets.Slider`
widget. The major difference is that RangeSlider's ``val`` attribute
is a tuple of floats ``(lower val, upper val)`` rather than a single float.

See :doc:`/gallery/widgets/slider_demo` for an example of using
a ``Slider`` to control a single float.

See :doc:`/gallery/widgets/slider_snap_demo` for an example of having
the ``Slider`` snap to discrete values.
"""���`a
���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���bkndfrom���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnngwidgets���`a ���bknfimport���`a ���`kRangeSlider���`a
���`a
���bc1w# generate a fake image���`a
���`bnp���aoa.���`frandom���aoa.���`dseed���`a(���bmih19680801���`a)���`a
���`aN���`a ���aoa=���`a ���bmic128���`a
���`cimg���`a ���aoa=���`a ���`bnp���aoa.���`frandom���aoa.���`erandn���`a(���`aN���`a,���`a ���`aN���`a)���`a
���`a
���`cfig���`a,���`a ���`caxs���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���bmia1���`a,���`a ���bmia2���`a,���`a ���`gfigsize���aoa=���`a(���bmib10���`a,���`a ���bmia5���`a)���`a)���`a
���`cplt���aoa.���`osubplots_adjust���`a(���`fbottom���aoa=���bmfd0.25���`a)���`a
���`a
���`bim���`a ���aoa=���`a ���`caxs���`a[���bmia0���`a]���aoa.���`fimshow���`a(���`cimg���`a)���`a
���`caxs���`a[���bmia1���`a]���aoa.���`dhist���`a(���`cimg���aoa.���`gflatten���`a(���`a)���`a,���`a ���`dbins���aoa=���bs1a'���bs1dauto���bs1a'���`a)���`a
���`caxs���`a[���bmia1���`a]���aoa.���`iset_title���`a(���bs1a'���bs1xHistogram of pixel intensities���bs1a'���`a)���`a
���`a
���bc1x# Create the RangeSlider���`a
���`islider_ax���`a ���aoa=���`a ���`cplt���aoa.���`daxes���`a(���`a[���bmfd0.20���`a,���`a ���bmfc0.1���`a,���`a ���bmfd0.60���`a,���`a ���bmfd0.03���`a]���`a)���`a
���`fslider���`a ���aoa=���`a ���`kRangeSlider���`a(���`islider_ax���`a,���`a ���bs2a"���bs2iThreshold���bs2a"���`a,���`a ���`cimg���aoa.���`cmin���`a(���`a)���`a,���`a ���`cimg���aoa.���`cmax���`a(���`a)���`a)���`a
���`a
���bc1x,# Create the Vertical lines on the histogram���`a
���`plower_limit_line���`a ���aoa=���`a ���`caxs���`a[���bmia1���`a]���aoa.���`gaxvline���`a(���`fslider���aoa.���`cval���`a[���bmia0���`a]���`a,���`a ���`ecolor���aoa=���bs1a'���bs1ak���bs1a'���`a)���`a
���`pupper_limit_line���`a ���aoa=���`a ���`caxs���`a[���bmia1���`a]���aoa.���`gaxvline���`a(���`fslider���aoa.���`cval���`a[���bmia1���`a]���`a,���`a ���`ecolor���aoa=���bs1a'���bs1ak���bs1a'���`a)���`a
���`a
���`a
���akcdef���`a ���bnffupdate���`a(���`cval���`a)���`a:���`a
���`d    ���bc1x6# The val passed to a callback by the RangeSlider will���`a
���`d    ���bc1x# be a tuple of (min, max)���`a
���`a
���`d    ���bc1x# Update the image's colormap���`a
���`d    ���`bim���aoa.���`dnorm���aoa.���`dvmin���`a ���aoa=���`a ���`cval���`a[���bmia0���`a]���`a
���`d    ���`bim���aoa.���`dnorm���aoa.���`dvmax���`a ���aoa=���`a ���`cval���`a[���bmia1���`a]���`a
���`a
���`d    ���bc1x+# Update the position of the vertical lines���`a
���`d    ���`plower_limit_line���aoa.���`iset_xdata���`a(���`a[���`cval���`a[���bmia0���`a]���`a,���`a ���`cval���`a[���bmia0���`a]���`a]���`a)���`a
���`d    ���`pupper_limit_line���aoa.���`iset_xdata���`a(���`a[���`cval���`a[���bmia1���`a]���`a,���`a ���`cval���`a[���bmia1���`a]���`a]���`a)���`a
���`a
���`d    ���bc1x(# Redraw the figure to ensure it updates���`a
���`d    ���`cfig���aoa.���`fcanvas���aoa.���`idraw_idle���`a(���`a)���`a
���`a
���`a
���`fslider���aoa.���`jon_changed���`a(���`fupdate���`a)���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
���`a
���bc1xM#############################################################################���`a
���bc1a#���`a
���bc1x# .. admonition:: References���`a
���bc1a#���`a
���bc1xN#    The use of the following functions, methods, classes and modules is shown���`a
���bc1u#    in this example:���`a
���bc1a#���`a
���bc1x'#    - `matplotlib.widgets.RangeSlider`���`a
`dNone�