��������S���bsdyS"""
==============================
Figure size in different units
==============================

The native figure size unit in Matplotlib is inches, deriving from print
industry standards. However, users may need to specify their figures in other
units like centimeters or pixels. This example illustrates how to do this
efficiently.
"""���`a
���`a
���bc1x%# sphinx_gallery_thumbnail_number = 2���`a
���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���`ktext_kwargs���`a ���aoa=���`a ���bnbddict���`a(���`bha���aoa=���bs1a'���bs1fcenter���bs1a'���`a,���`a ���`bva���aoa=���bs1a'���bs1fcenter���bs1a'���`a,���`a ���`hfontsize���aoa=���bmib28���`a,���`a ���`ecolor���aoa=���bs1a'���bs1bC1���bs1a'���`a)���`a
���`a
���bc1xN##############################################################################���`a
���bc1x!# Figure size in inches (default)���`a
���bc1x!# -------------------------------���`a
���bc1a#���`a
���`cplt���aoa.���`hsubplots���`a(���`gfigsize���aoa=���`a(���bmia6���`a,���`a ���bmia2���`a)���`a)���`a
���`cplt���aoa.���`dtext���`a(���bmfc0.5���`a,���`a ���bmfc0.5���`a,���`a ���bs1a'���bs1s6 inches x 2 inches���bs1a'���`a,���`a ���aoa*���aoa*���`ktext_kwargs���`a)���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
���`a
���`a
���bc1xM#############################################################################���`a
���bc1x# Figure size in centimeter���`a
���bc1x# -------------------------���`a
���bc1xJ# Multiplying centimeter-based numbers with a conversion factor from cm to���`a
���bc1xL# inches, gives the right numbers. Naming the conversion factor ``cm`` makes���`a
���bc1xJ# the conversion almost look like appending a unit to the number, which is���`a
���bc1r# nicely readable.���`a
���bc1a#���`a
���`bcm���`a ���aoa=���`a ���bmia1���aoa/���bmfd2.54���`b  ���bc1w# centimeters in inches���`a
���`cplt���aoa.���`hsubplots���`a(���`gfigsize���aoa=���`a(���bmib15���aoa*���`bcm���`a,���`a ���bmia5���aoa*���`bcm���`a)���`a)���`a
���`cplt���aoa.���`dtext���`a(���bmfc0.5���`a,���`a ���bmfc0.5���`a,���`a ���bs1a'���bs1j15cm x 5cm���bs1a'���`a,���`a ���aoa*���aoa*���`ktext_kwargs���`a)���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
���`a
���`a
���bc1xM#############################################################################���`a
���bc1v# Figure size in pixel���`a
���bc1v# --------------------���`a
���bc1x2# Similarly, one can use a conversion from pixels.���`a
���bc1a#���`a
���bc1xE# Note that you could break this if you use `~.pyplot.savefig` with a���`a
���bc1x# different explicit dpi value.���`a
���bc1a#���`a
���`bpx���`a ���aoa=���`a ���bmia1���aoa/���`cplt���aoa.���`hrcParams���`a[���bs1a'���bs1jfigure.dpi���bs1a'���`a]���`b  ���bc1q# pixel in inches���`a
���`cplt���aoa.���`hsubplots���`a(���`gfigsize���aoa=���`a(���bmic600���aoa*���`bpx���`a,���`a ���bmic200���aoa*���`bpx���`a)���`a)���`a
���`cplt���aoa.���`dtext���`a(���bmfc0.5���`a,���`a ���bmfc0.5���`a,���`a ���bs1a'���bs1m600px x 200px���bs1a'���`a,���`a ���aoa*���aoa*���`ktext_kwargs���`a)���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
���`a
���bc1xM#############################################################################���`a
���bc1xK# Quick interactive work is usually rendered to the screen, making pixels a���`a
���bc1xI# good size of unit. But defining the conversion factor may feel a little���`a
���bc1x# tedious for quick iterations.���`a
���bc1a#���`a
���bc1xK# Because of the default ``rcParams['figure.dpi'] = 100``, one can mentally���`a
���bc1x,# divide the needed pixel value by 100 [#]_:���`a
���bc1a#���`a
���`cplt���aoa.���`hsubplots���`a(���`gfigsize���aoa=���`a(���bmia6���`a,���`a ���bmia2���`a)���`a)���`a
���`cplt���aoa.���`dtext���`a(���bmfc0.5���`a,���`a ���bmfc0.5���`a,���`a ���bs1a'���bs1m600px x 200px���bs1a'���`a,���`a ���aoa*���aoa*���`ktext_kwargs���`a)���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
���`a
���bc1xM#############################################################################���`a
���bc1xM# .. [#] Unfortunately, this does not work well for the ``matplotlib inline``���`a
���bc1xL#        backend in Jupyter because that backend uses a different default of���`a
���bc1xK#        ``rcParams['figure.dpi'] = 72``. Additionally, it saves the figure���`a
���bc1xK#        with ``bbox_inches='tight'``, which crops the figure and makes the���`a
���bc1x##        actual size unpredictable.���`a
���`a
���bc1xM#############################################################################���`a
���bc1a#���`a
���bc1x# .. admonition:: References���`a
���bc1a#���`a
���bc1xN#    The use of the following functions, methods, classes and modules is shown���`a
���bc1u#    in this example:���`a
���bc1a#���`a
���bc1x!#    - `matplotlib.pyplot.figure`���`a
���bc1x##    - `matplotlib.pyplot.subplots`���`a
���bc1x)#    - `matplotlib.pyplot.subplot_mosaic`���`a
`dNone�