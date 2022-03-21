������������bsdy�"""
=============================
Subplots spacings and margins
=============================

Adjusting the spacing of margins and subplots using `.pyplot.subplots_adjust`.

.. note::
   There is also a tool window to adjust the margins and spacings of displayed
   figures interactively.  It can be opened via the toolbar or by calling
   `.pyplot.subplot_tool`.

.. redirect-from:: /gallery/subplots_axes_and_figures/subplot_toolbar
"""���`a
���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���`a
���bc1x)# Fixing random state for reproducibility���`a
���`bnp���aoa.���`frandom���aoa.���`dseed���`a(���bmih19680801���`a)���`a
���`a
���`cplt���aoa.���`gsubplot���`a(���bmic211���`a)���`a
���`cplt���aoa.���`fimshow���`a(���`bnp���aoa.���`frandom���aoa.���`frandom���`a(���`a(���bmic100���`a,���`a ���bmic100���`a)���`a)���`a)���`a
���`cplt���aoa.���`gsubplot���`a(���bmic212���`a)���`a
���`cplt���aoa.���`fimshow���`a(���`bnp���aoa.���`frandom���aoa.���`frandom���`a(���`a(���bmic100���`a,���`a ���bmic100���`a)���`a)���`a)���`a
���`a
���`cplt���aoa.���`osubplots_adjust���`a(���`fbottom���aoa=���bmfc0.1���`a,���`a ���`eright���aoa=���bmfc0.8���`a,���`a ���`ctop���aoa=���bmfc0.9���`a)���`a
���`ccax���`a ���aoa=���`a ���`cplt���aoa.���`daxes���`a(���`a[���bmfd0.85���`a,���`a ���bmfc0.1���`a,���`a ���bmfe0.075���`a,���`a ���bmfc0.8���`a]���`a)���`a
���`cplt���aoa.���`hcolorbar���`a(���`ccax���aoa=���`ccax���`a)���`a
���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
`dNone�