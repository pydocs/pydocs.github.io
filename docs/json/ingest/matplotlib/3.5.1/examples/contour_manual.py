��������~���bsdx�"""
==============
Manual Contour
==============

Example of displaying your own contour lines and polygons using ContourSet.
"""���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���bkndfrom���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnngcontour���`a ���bknfimport���`a ���`jContourSet���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnbcm���`a ���akbas���`a ���bnnbcm���`a
���`a
���`a
���bc1xO###############################################################################���`a
���bc1x<# Contour lines for each level are a list/tuple of polygons.���`a
���`flines0���`a ���aoa=���`a ���`a[���`a[���`a[���bmia0���`a,���`a ���bmia0���`a]���`a,���`a ���`a[���bmia0���`a,���`a ���bmia4���`a]���`a]���`a]���`a
���`flines1���`a ���aoa=���`a ���`a[���`a[���`a[���bmia2���`a,���`a ���bmia0���`a]���`a,���`a ���`a[���bmia1���`a,���`a ���bmia2���`a]���`a,���`a ���`a[���bmia1���`a,���`a ���bmia3���`a]���`a]���`a]���`a
���`flines2���`a ���aoa=���`a ���`a[���`a[���`a[���bmia3���`a,���`a ���bmia0���`a]���`a,���`a ���`a[���bmia3���`a,���`a ���bmia2���`a]���`a]���`a,���`a ���`a[���`a[���bmia3���`a,���`a ���bmia3���`a]���`a,���`a ���`a[���bmia3���`a,���`a ���bmia4���`a]���`a]���`a]���`b  ���bc1q# Note two lines.���`a
���`a
���bc1xO###############################################################################���`a
���bc1xG# Filled contours between two levels are also a list/tuple of polygons.���`a
���bc1x3# Points can be ordered clockwise or anticlockwise.���`a
���`hfilled01���`a ���aoa=���`a ���`a[���`a[���`a[���bmia0���`a,���`a ���bmia0���`a]���`a,���`a ���`a[���bmia0���`a,���`a ���bmia4���`a]���`a,���`a ���`a[���bmia1���`a,���`a ���bmia3���`a]���`a,���`a ���`a[���bmia1���`a,���`a ���bmia2���`a]���`a,���`a ���`a[���bmia2���`a,���`a ���bmia0���`a]���`a]���`a]���`a
���`hfilled12���`a ���aoa=���`a ���`a[���`a[���`a[���bmia2���`a,���`a ���bmia0���`a]���`a,���`a ���`a[���bmia3���`a,���`a ���bmia0���`a]���`a,���`a ���`a[���bmia3���`a,���`a ���bmia2���`a]���`a,���`a ���`a[���bmia1���`a,���`a ���bmia3���`a]���`a,���`a ���`a[���bmia1���`a,���`a ���bmia2���`a]���`a]���`a,���`c   ���bc1t# Note two polygons.���`a
���`l            ���`a[���`a[���bmia1���`a,���`a ���bmia4���`a]���`a,���`a ���`a[���bmia3���`a,���`a ���bmia4���`a]���`a,���`a ���`a[���bmia3���`a,���`a ���bmia3���`a]���`a]���`a]���`a
���`a
���bc1xO###############################################################################���`a
���`a
���`cfig���`a,���`a ���`bax���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`a)���`a
���`a
���bc1x$# Filled contours using filled=True.���`a
���`bcs���`a ���aoa=���`a ���`jContourSet���`a(���`bax���`a,���`a ���`a[���bmia0���`a,���`a ���bmia1���`a,���`a ���bmia2���`a]���`a,���`a ���`a[���`hfilled01���`a,���`a ���`hfilled12���`a]���`a,���`a ���`ffilled���aoa=���bkcdTrue���`a,���`a ���`dcmap���aoa=���`bcm���aoa.���`dbone���`a)���`a
���`dcbar���`a ���aoa=���`a ���`cfig���aoa.���`hcolorbar���`a(���`bcs���`a)���`a
���`a
���bc1x# Contour lines (non-filled).���`a
���`elines���`a ���aoa=���`a ���`jContourSet���`a(���`a
���`d    ���`bax���`a,���`a ���`a[���bmia0���`a,���`a ���bmia1���`a,���`a ���bmia2���`a]���`a,���`a ���`a[���`flines0���`a,���`a ���`flines1���`a,���`a ���`flines2���`a]���`a,���`a ���`dcmap���aoa=���`bcm���aoa.���`dcool���`a,���`a ���`jlinewidths���aoa=���bmia3���`a)���`a
���`dcbar���aoa.���`iadd_lines���`a(���`elines���`a)���`a
���`a
���`bax���aoa.���`cset���`a(���`dxlim���aoa=���`a(���aoa-���bmfc0.5���`a,���`a ���bmfc3.5���`a)���`a,���`a ���`dylim���aoa=���`a(���aoa-���bmfc0.5���`a,���`a ���bmfc4.5���`a)���`a,���`a
���`g       ���`etitle���aoa=���bs1a'���bs1wUser-specified contours���bs1a'���`a)���`a
���`a
���bc1xO###############################################################################���`a
���bc1xL# Multiple filled contour lines can be specified in a single list of polygon���`a
���bc1xM# vertices along with a list of vertex kinds (code types) as described in the���`a
���bc1xC# Path class.  This is particularly useful for polygons with holes.���`a
���bc1x7# Here a code type of 1 is a MOVETO, and 2 is a LINETO.���`a
���`a
���`cfig���`a,���`a ���`bax���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`a)���`a
���`hfilled01���`a ���aoa=���`a ���`a[���`a[���`a[���bmia0���`a,���`a ���bmia0���`a]���`a,���`a ���`a[���bmia3���`a,���`a ���bmia0���`a]���`a,���`a ���`a[���bmia3���`a,���`a ���bmia3���`a]���`a,���`a ���`a[���bmia0���`a,���`a ���bmia3���`a]���`a,���`a ���`a[���bmia1���`a,���`a ���bmia1���`a]���`a,���`a ���`a[���bmia1���`a,���`a ���bmia2���`a]���`a,���`a ���`a[���bmia2���`a,���`a ���bmia2���`a]���`a,���`a ���`a[���bmia2���`a,���`a ���bmia1���`a]���`a]���`a]���`a
���`gkinds01���`a ���aoa=���`a ���`a[���`a[���bmia1���`a,���`a ���bmia2���`a,���`a ���bmia2���`a,���`a ���bmia2���`a,���`a ���bmia1���`a,���`a ���bmia2���`a,���`a ���bmia2���`a,���`a ���bmia2���`a]���`a]���`a
���`bcs���`a ���aoa=���`a ���`jContourSet���`a(���`bax���`a,���`a ���`a[���bmia0���`a,���`a ���bmia1���`a]���`a,���`a ���`a[���`hfilled01���`a]���`a,���`a ���`a[���`gkinds01���`a]���`a,���`a ���`ffilled���aoa=���bkcdTrue���`a)���`a
���`dcbar���`a ���aoa=���`a ���`cfig���aoa.���`hcolorbar���`a(���`bcs���`a)���`a
���`a
���`bax���aoa.���`cset���`a(���`dxlim���aoa=���`a(���aoa-���bmfc0.5���`a,���`a ���bmfc3.5���`a)���`a,���`a ���`dylim���aoa=���`a(���aoa-���bmfc0.5���`a,���`a ���bmfc3.5���`a)���`a,���`a
���`g       ���`etitle���aoa=���bs1a'���bs1x)User specified filled contours with holes���bs1a'���`a)���`a
���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
`dNone�