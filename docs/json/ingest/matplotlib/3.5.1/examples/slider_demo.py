������������bsdyV"""
======
Slider
======

In this example, sliders are used to control the frequency and amplitude of
a sine wave.

See :doc:`/gallery/widgets/slider_snap_demo` for an example of having
the ``Slider`` snap to discrete values.

See :doc:`/gallery/widgets/range_slider` for an example of using
a ``RangeSlider`` to define a range of values.
"""���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���bkndfrom���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnngwidgets���`a ���bknfimport���`a ���`fSlider���`a,���`a ���`fButton���`a
���`a
���`a
���bc1x)# The parametrized function to be plotted���`a
���akcdef���`a ���bnfaf���`a(���`at���`a,���`a ���`iamplitude���`a,���`a ���`ifrequency���`a)���`a:���`a
���`d    ���akfreturn���`a ���`iamplitude���`a ���aoa*���`a ���`bnp���aoa.���`csin���`a(���bmia2���`a ���aoa*���`a ���`bnp���aoa.���`bpi���`a ���aoa*���`a ���`ifrequency���`a ���aoa*���`a ���`at���`a)���`a
���`a
���`at���`a ���aoa=���`a ���`bnp���aoa.���`hlinspace���`a(���bmia0���`a,���`a ���bmia1���`a,���`a ���bmid1000���`a)���`a
���`a
���bc1x# Define initial parameters���`a
���`ninit_amplitude���`a ���aoa=���`a ���bmia5���`a
���`ninit_frequency���`a ���aoa=���`a ���bmia3���`a
���`a
���bc1x8# Create the figure and the line that we will manipulate���`a
���`cfig���`a,���`a ���`bax���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`a)���`a
���`dline���`a,���`a ���aoa=���`a ���`cplt���aoa.���`dplot���`a(���`at���`a,���`a ���`af���`a(���`at���`a,���`a ���`ninit_amplitude���`a,���`a ���`ninit_frequency���`a)���`a,���`a ���`blw���aoa=���bmia2���`a)���`a
���`bax���aoa.���`jset_xlabel���`a(���bs1a'���bs1hTime [s]���bs1a'���`a)���`a
���`a
���bc1x3# adjust the main plot to make room for the sliders���`a
���`cplt���aoa.���`osubplots_adjust���`a(���`dleft���aoa=���bmfd0.25���`a,���`a ���`fbottom���aoa=���bmfd0.25���`a)���`a
���`a
���bc1x4# Make a horizontal slider to control the frequency.���`a
���`faxfreq���`a ���aoa=���`a ���`cplt���aoa.���`daxes���`a(���`a[���bmfd0.25���`a,���`a ���bmfc0.1���`a,���`a ���bmfd0.65���`a,���`a ���bmfd0.03���`a]���`a)���`a
���`kfreq_slider���`a ���aoa=���`a ���`fSlider���`a(���`a
���`d    ���`bax���aoa=���`faxfreq���`a,���`a
���`d    ���`elabel���aoa=���bs1a'���bs1nFrequency [Hz]���bs1a'���`a,���`a
���`d    ���`fvalmin���aoa=���bmfc0.1���`a,���`a
���`d    ���`fvalmax���aoa=���bmib30���`a,���`a
���`d    ���`gvalinit���aoa=���`ninit_frequency���`a,���`a
���`a)���`a
���`a
���bc1x<# Make a vertically oriented slider to control the amplitude���`a
���`eaxamp���`a ���aoa=���`a ���`cplt���aoa.���`daxes���`a(���`a[���bmfc0.1���`a,���`a ���bmfd0.25���`a,���`a ���bmff0.0225���`a,���`a ���bmfd0.63���`a]���`a)���`a
���`jamp_slider���`a ���aoa=���`a ���`fSlider���`a(���`a
���`d    ���`bax���aoa=���`eaxamp���`a,���`a
���`d    ���`elabel���aoa=���bs2a"���bs2iAmplitude���bs2a"���`a,���`a
���`d    ���`fvalmin���aoa=���bmia0���`a,���`a
���`d    ���`fvalmax���aoa=���bmib10���`a,���`a
���`d    ���`gvalinit���aoa=���`ninit_amplitude���`a,���`a
���`d    ���`korientation���aoa=���bs2a"���bs2hvertical���bs2a"���`a
���`a)���`a
���`a
���`a
���bc1x<# The function to be called anytime a slider's value changes���`a
���akcdef���`a ���bnffupdate���`a(���`cval���`a)���`a:���`a
���`d    ���`dline���aoa.���`iset_ydata���`a(���`af���`a(���`at���`a,���`a ���`jamp_slider���aoa.���`cval���`a,���`a ���`kfreq_slider���aoa.���`cval���`a)���`a)���`a
���`d    ���`cfig���aoa.���`fcanvas���aoa.���`idraw_idle���`a(���`a)���`a
���`a
���`a
���bc1x/# register the update function with each slider���`a
���`kfreq_slider���aoa.���`jon_changed���`a(���`fupdate���`a)���`a
���`jamp_slider���aoa.���`jon_changed���`a(���`fupdate���`a)���`a
���`a
���bc1xN# Create a `matplotlib.widgets.Button` to reset the sliders to initial values.���`a
���`gresetax���`a ���aoa=���`a ���`cplt���aoa.���`daxes���`a(���`a[���bmfc0.8���`a,���`a ���bmfe0.025���`a,���`a ���bmfc0.1���`a,���`a ���bmfd0.04���`a]���`a)���`a
���`fbutton���`a ���aoa=���`a ���`fButton���`a(���`gresetax���`a,���`a ���bs1a'���bs1eReset���bs1a'���`a,���`a ���`jhovercolor���aoa=���bs1a'���bs1e0.975���bs1a'���`a)���`a
���`a
���`a
���akcdef���`a ���bnfereset���`a(���`eevent���`a)���`a:���`a
���`d    ���`kfreq_slider���aoa.���`ereset���`a(���`a)���`a
���`d    ���`jamp_slider���aoa.���`ereset���`a(���`a)���`a
���`fbutton���aoa.���`jon_clicked���`a(���`ereset���`a)���`a
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
���bc1x"#    - `matplotlib.widgets.Button`���`a
���bc1x"#    - `matplotlib.widgets.Slider`���`a
`dNone�