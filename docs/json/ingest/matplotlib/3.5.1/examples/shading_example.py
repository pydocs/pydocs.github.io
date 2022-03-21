��������P���bsdy"""
===============
Shading example
===============

Example showing how to make shaded relief plots like Mathematica_ or
`Generic Mapping Tools`_.

.. _Mathematica: http://reference.wolfram.com/mathematica/ref/ReliefPlot.html
.. _Generic Mapping Tools: https://gmt.soest.hawaii.edu/
"""���`a
���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���bkndfrom���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����`a ���bknfimport���`a ���`ecbook���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���bkndfrom���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfcolors���`a ���bknfimport���`a ���`kLightSource���`a
���`a
���`a
���akcdef���`a ���bnfdmain���`a(���`a)���`a:���`a
���`d    ���bc1k# Test data���`a
���`d    ���`ax���`a,���`a ���`ay���`a ���aoa=���`a ���`bnp���aoa.���`emgrid���`a[���aoa-���bmia5���`a:���bmia5���`a:���bmfd0.05���`a,���`a ���aoa-���bmia5���`a:���bmia5���`a:���bmfd0.05���`a]���`a
���`d    ���`az���`a ���aoa=���`a ���bmia5���`a ���aoa*���`a ���`a(���`bnp���aoa.���`dsqrt���`a(���`ax���aoa*���aoa*���bmia2���`a ���aoa+���`a ���`ay���aoa*���aoa*���bmia2���`a)���`a ���aoa+���`a ���`bnp���aoa.���`csin���`a(���`ax���aoa*���aoa*���bmia2���`a ���aoa+���`a ���`ay���aoa*���aoa*���bmia2���`a)���`a)���`a
���`a
���`d    ���`cdem���`a ���aoa=���`a ���`ecbook���aoa.���`oget_sample_data���`a(���bs1a'���bs1wjacksboro_fault_dem.npz���bs1a'���`a,���`a ���`gnp_load���aoa=���bkcdTrue���`a)���`a
���`d    ���`delev���`a ���aoa=���`a ���`cdem���`a[���bs1a'���bs1ielevation���bs1a'���`a]���`a
���`a
���`d    ���`cfig���`a ���aoa=���`a ���`gcompare���`a(���`az���`a,���`a ���`cplt���aoa.���`bcm���aoa.���`fcopper���`a)���`a
���`d    ���`cfig���aoa.���`hsuptitle���`a(���bs1a'���bs1x,HSV Blending Looks Best with Smooth Surfaces���bs1a'���`a,���`a ���`ay���aoa=���bmfd0.95���`a)���`a
���`a
���`d    ���`cfig���`a ���aoa=���`a ���`gcompare���`a(���`delev���`a,���`a ���`cplt���aoa.���`bcm���aoa.���`jgist_earth���`a,���`a ���`bve���aoa=���bmfd0.05���`a)���`a
���`d    ���`cfig���aoa.���`hsuptitle���`a(���bs1a'���bs1x/Overlay Blending Looks Best with Rough Surfaces���bs1a'���`a,���`a ���`ay���aoa=���bmfd0.95���`a)���`a
���`a
���`d    ���`cplt���aoa.���`dshow���`a(���`a)���`a
���`a
���`a
���akcdef���`a ���bnfgcompare���`a(���`az���`a,���`a ���`dcmap���`a,���`a ���`bve���aoa=���bmia1���`a)���`a:���`a
���`d    ���bc1x # Create subplots and hide ticks���`a
���`d    ���`cfig���`a,���`a ���`caxs���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`encols���aoa=���bmia2���`a,���`a ���`enrows���aoa=���bmia2���`a)���`a
���`d    ���akcfor���`a ���`bax���`a ���bowbin���`a ���`caxs���aoa.���`dflat���`a:���`a
���`h        ���`bax���aoa.���`cset���`a(���`fxticks���aoa=���`a[���`a]���`a,���`a ���`fyticks���aoa=���`a[���`a]���`a)���`a
���`a
���`d    ���bc1x)# Illuminate the scene from the northwest���`a
���`d    ���`bls���`a ���aoa=���`a ���`kLightSource���`a(���`eazdeg���aoa=���bmic315���`a,���`a ���`faltdeg���aoa=���bmib45���`a)���`a
���`a
���`d    ���`caxs���`a[���bmia0���`a,���`a ���bmia0���`a]���aoa.���`fimshow���`a(���`az���`a,���`a ���`dcmap���aoa=���`dcmap���`a)���`a
���`d    ���`caxs���`a[���bmia0���`a,���`a ���bmia0���`a]���aoa.���`cset���`a(���`fxlabel���aoa=���bs1a'���bs1pColormapped Data���bs1a'���`a)���`a
���`a
���`d    ���`caxs���`a[���bmia0���`a,���`a ���bmia1���`a]���aoa.���`fimshow���`a(���`bls���aoa.���`ihillshade���`a(���`az���`a,���`a ���`ivert_exag���aoa=���`bve���`a)���`a,���`a ���`dcmap���aoa=���bs1a'���bs1dgray���bs1a'���`a)���`a
���`d    ���`caxs���`a[���bmia0���`a,���`a ���bmia1���`a]���aoa.���`cset���`a(���`fxlabel���aoa=���bs1a'���bs1vIllumination Intensity���bs1a'���`a)���`a
���`a
���`d    ���`crgb���`a ���aoa=���`a ���`bls���aoa.���`eshade���`a(���`az���`a,���`a ���`dcmap���aoa=���`dcmap���`a,���`a ���`ivert_exag���aoa=���`bve���`a,���`a ���`jblend_mode���aoa=���bs1a'���bs1chsv���bs1a'���`a)���`a
���`d    ���`caxs���`a[���bmia1���`a,���`a ���bmia0���`a]���aoa.���`fimshow���`a(���`crgb���`a)���`a
���`d    ���`caxs���`a[���bmia1���`a,���`a ���bmia0���`a]���aoa.���`cset���`a(���`fxlabel���aoa=���bs1a'���bs1lBlend Mode: ���bs1a"���bs1chsv���bs1a"���bs1j (default)���bs1a'���`a)���`a
���`a
���`d    ���`crgb���`a ���aoa=���`a ���`bls���aoa.���`eshade���`a(���`az���`a,���`a ���`dcmap���aoa=���`dcmap���`a,���`a ���`ivert_exag���aoa=���`bve���`a,���`a ���`jblend_mode���aoa=���bs1a'���bs1goverlay���bs1a'���`a)���`a
���`d    ���`caxs���`a[���bmia1���`a,���`a ���bmia1���`a]���aoa.���`fimshow���`a(���`crgb���`a)���`a
���`d    ���`caxs���`a[���bmia1���`a,���`a ���bmia1���`a]���aoa.���`cset���`a(���`fxlabel���aoa=���bs1a'���bs1lBlend Mode: ���bs1a"���bs1goverlay���bs1a"���bs1a'���`a)���`a
���`a
���`d    ���akfreturn���`a ���`cfig���`a
���`a
���`a
���akbif���`a ���bvmh__name__���`a ���aob==���`a ���bs1a'���bs1h__main__���bs1a'���`a:���`a
���`d    ���`dmain���`a(���`a)���`a
���`a
���bc1xM#############################################################################���`a
���bc1a#���`a
���bc1x# .. admonition:: References���`a
���bc1a#���`a
���bc1xN#    The use of the following functions, methods, classes and modules is shown���`a
���bc1u#    in this example:���`a
���bc1a#���`a
���bc1x&#    - `matplotlib.colors.LightSource`���`a
���bc1xA#    - `matplotlib.axes.Axes.imshow` / `matplotlib.pyplot.imshow`���`a
`dNone�