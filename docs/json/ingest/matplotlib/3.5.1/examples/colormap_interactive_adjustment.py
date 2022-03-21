������������bsdyJ"""
========================================
Interactive Adjustment of Colormap Range
========================================

Demonstration of how a colorbar can be used to interactively adjust the
range of colormapping on an image. To use the interactive feature, you must
be in either zoom mode (magnifying glass toolbar button) or
pan mode (4-way arrow toolbar button) and click inside the colorbar.

When zooming, the bounding box of the zoom region defines the new vmin and
vmax of the norm. Zooming using the right mouse button will expand the
vmin and vmax proportionally to the selected region, in the same manner that
one can zoom out on an axis. When panning, the vmin and vmax of the norm are
both shifted according to the direction of movement. The
Home/Back/Forward buttons can also be used to get back to a previous state.
"""���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���`a
���`at���`a ���aoa=���`a ���`bnp���aoa.���`hlinspace���`a(���bmia0���`a,���`a ���bmia2���`a ���aoa*���`a ���`bnp���aoa.���`bpi���`a,���`a ���bmid1024���`a)���`a
���`fdata2d���`a ���aoa=���`a ���`bnp���aoa.���`csin���`a(���`at���`a)���`a[���`a:���`a,���`a ���`bnp���aoa.���`gnewaxis���`a]���`a ���aoa*���`a ���`bnp���aoa.���`ccos���`a(���`at���`a)���`a[���`bnp���aoa.���`gnewaxis���`a,���`a ���`a:���`a]���`a
���`a
���`cfig���`a,���`a ���`bax���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`a)���`a
���`bim���`a ���aoa=���`a ���`bax���aoa.���`fimshow���`a(���`fdata2d���`a)���`a
���`bax���aoa.���`iset_title���`a(���bs1a'���bs1x.Pan on the colorbar to shift the color mapping���bseb\n���bs1a'���`a
���`m             ���bs1a'���bs1x/Zoom on the colorbar to scale the color mapping���bs1a'���`a)���`a
���`a
���`cfig���aoa.���`hcolorbar���`a(���`bim���`a,���`a ���`bax���aoa=���`bax���`a,���`a ���`elabel���aoa=���bs1a'���bs1tInteractive colorbar���bs1a'���`a)���`a
���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
`dNone�