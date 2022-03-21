������������bsdyT"""
===================================
Snapping Sliders to Discrete Values
===================================

You can snap slider values to discrete values using the ``valstep`` argument.

In this example the Freq slider is constrained to be multiples of pi, and the
Amp slider uses an array as the ``valstep`` argument to more densely sample
the first part of its range.

See :doc:`/gallery/widgets/slider_demo` for an example of using
a ``Slider`` to control a single float.

See :doc:`/gallery/widgets/range_slider` for an example of using
a ``RangeSlider`` to define a range of values.
"""���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���bkndfrom���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnngwidgets���`a ���bknfimport���`a ���`fSlider���`a,���`a ���`fButton���`a
���`a
���`at���`a ���aoa=���`a ���`bnp���aoa.���`farange���`a(���bmfc0.0���`a,���`a ���bmfc1.0���`a,���`a ���bmfe0.001���`a)���`a
���`ba0���`a ���aoa=���`a ���bmia5���`a
���`bf0���`a ���aoa=���`a ���bmia3���`a
���`as���`a ���aoa=���`a ���`ba0���`a ���aoa*���`a ���`bnp���aoa.���`csin���`a(���bmia2���`a ���aoa*���`a ���`bnp���aoa.���`bpi���`a ���aoa*���`a ���`bf0���`a ���aoa*���`a ���`at���`a)���`a
���`a
���`cfig���`a,���`a ���`bax���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`a)���`a
���`cplt���aoa.���`osubplots_adjust���`a(���`fbottom���aoa=���bmfd0.25���`a)���`a
���`al���`a,���`a ���aoa=���`a ���`cplt���aoa.���`dplot���`a(���`at���`a,���`a ���`as���`a,���`a ���`blw���aoa=���bmia2���`a)���`a
���`a
���`gax_freq���`a ���aoa=���`a ���`cplt���aoa.���`daxes���`a(���`a[���bmfd0.25���`a,���`a ���bmfc0.1���`a,���`a ���bmfd0.65���`a,���`a ���bmfd0.03���`a]���`a)���`a
���`fax_amp���`a ���aoa=���`a ���`cplt���aoa.���`daxes���`a(���`a[���bmfd0.25���`a,���`a ���bmfd0.15���`a,���`a ���bmfd0.65���`a,���`a ���bmfd0.03���`a]���`a)���`a
���`a
���bc1x'# define the values to use for snapping���`a
���`rallowed_amplitudes���`a ���aoa=���`a ���`bnp���aoa.���`kconcatenate���`a(���`a[���`bnp���aoa.���`hlinspace���`a(���bmfb.1���`a,���`a ���bmia5���`a,���`a ���bmic100���`a)���`a,���`a ���`a[���bmia6���`a,���`a ���bmia7���`a,���`a ���bmia8���`a,���`a ���bmia9���`a]���`a]���`a)���`a
���`a
���bc1t# create the sliders���`a
���`dsamp���`a ���aoa=���`a ���`fSlider���`a(���`a
���`d    ���`fax_amp���`a,���`a ���bs2a"���bs2cAmp���bs2a"���`a,���`a ���bmfc0.1���`a,���`a ���bmfc9.0���`a,���`a
���`d    ���`gvalinit���aoa=���`ba0���`a,���`a ���`gvalstep���aoa=���`rallowed_amplitudes���`a,���`a
���`d    ���`ecolor���aoa=���bs2a"���bs2egreen���bs2a"���`a
���`a)���`a
���`a
���`esfreq���`a ���aoa=���`a ���`fSlider���`a(���`a
���`d    ���`gax_freq���`a,���`a ���bs2a"���bs2dFreq���bs2a"���`a,���`a ���bmia0���`a,���`a ���bmib10���aoa*���`bnp���aoa.���`bpi���`a,���`a
���`d    ���`gvalinit���aoa=���bmia2���aoa*���`bnp���aoa.���`bpi���`a,���`a ���`gvalstep���aoa=���`bnp���aoa.���`bpi���`a,���`a
���`d    ���`iinitcolor���aoa=���bs1a'���bs1dnone���bs1a'���`b  ���bc1x/# Remove the line marking the valinit position.���`a
���`a)���`a
���`a
���`a
���akcdef���`a ���bnffupdate���`a(���`cval���`a)���`a:���`a
���`d    ���`camp���`a ���aoa=���`a ���`dsamp���aoa.���`cval���`a
���`d    ���`dfreq���`a ���aoa=���`a ���`esfreq���aoa.���`cval���`a
���`d    ���`al���aoa.���`iset_ydata���`a(���`camp���aoa*���`bnp���aoa.���`csin���`a(���bmia2���aoa*���`bnp���aoa.���`bpi���aoa*���`dfreq���aoa*���`at���`a)���`a)���`a
���`d    ���`cfig���aoa.���`fcanvas���aoa.���`idraw_idle���`a(���`a)���`a
���`a
���`a
���`esfreq���aoa.���`jon_changed���`a(���`fupdate���`a)���`a
���`dsamp���aoa.���`jon_changed���`a(���`fupdate���`a)���`a
���`a
���`hax_reset���`a ���aoa=���`a ���`cplt���aoa.���`daxes���`a(���`a[���bmfc0.8���`a,���`a ���bmfe0.025���`a,���`a ���bmfc0.1���`a,���`a ���bmfd0.04���`a]���`a)���`a
���`fbutton���`a ���aoa=���`a ���`fButton���`a(���`hax_reset���`a,���`a ���bs1a'���bs1eReset���bs1a'���`a,���`a ���`jhovercolor���aoa=���bs1a'���bs1e0.975���bs1a'���`a)���`a
���`a
���`a
���akcdef���`a ���bnfereset���`a(���`eevent���`a)���`a:���`a
���`d    ���`esfreq���aoa.���`ereset���`a(���`a)���`a
���`d    ���`dsamp���aoa.���`ereset���`a(���`a)���`a
���`fbutton���aoa.���`jon_clicked���`a(���`ereset���`a)���`a
���`a
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
���bc1x"#    - `matplotlib.widgets.Slider`���`a
���bc1x"#    - `matplotlib.widgets.Button`���`a
`dNone�