������������bsdx�"""
===============
Pyplot Mathtext
===============

Use mathematical expressions in text labels. For an overview over MathText
see :doc:`/tutorials/text/mathtext`.
"""���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���`at���`a ���aoa=���`a ���`bnp���aoa.���`farange���`a(���bmfc0.0���`a,���`a ���bmfc2.0���`a,���`a ���bmfd0.01���`a)���`a
���`as���`a ���aoa=���`a ���`bnp���aoa.���`csin���`a(���bmia2���aoa*���`bnp���aoa.���`bpi���aoa*���`at���`a)���`a
���`a
���`cplt���aoa.���`dplot���`a(���`at���`a,���`a ���`as���`a)���`a
���`cplt���aoa.���`etitle���`a(���bsaar���bs1a'���bs1a$���bs1a\���bs1jalpha_i > ���bs1a\���bs1gbeta_i$���bs1a'���`a,���`a ���`hfontsize���aoa=���bmib20���`a)���`a
���`cplt���aoa.���`dtext���`a(���bmia1���`a,���`a ���aoa-���bmfc0.6���`a,���`a ���bsaar���bs1a'���bs1a$���bs1a\���bs1dsum_���bs1a{���bs1ei=0}^���bs1a\���bs1jinfty x_i$���bs1a'���`a,���`a ���`hfontsize���aoa=���bmib20���`a)���`a
���`cplt���aoa.���`dtext���`a(���bmfc0.6���`a,���`a ���bmfc0.6���`a,���`a ���bsaar���bs1a'���bs1a$���bs1a\���bs1gmathcal���bsic{A}���bs1a\���bs1fmathrm���bsie{sin}���bs1c(2 ���bs1a\���bs1iomega t)$���bs1a'���`a,���`a
���`i         ���`hfontsize���aoa=���bmib20���`a)���`a
���`cplt���aoa.���`fxlabel���`a(���bs1a'���bs1htime (s)���bs1a'���`a)���`a
���`cplt���aoa.���`fylabel���`a(���bs1a'���bs1jvolts (mV)���bs1a'���`a)���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
���`a
���bc1xM#############################################################################���`a
���bc1a#���`a
���bc1x# .. admonition:: References���`a
���bc1a#���`a
���bc1xN#    The use of the following functions, methods, classes and modules is shown���`a
���bc1u#    in this example:���`a
���bc1a#���`a
���bc1x=#    - `matplotlib.axes.Axes.text` / `matplotlib.pyplot.text`���`a
`dNone�