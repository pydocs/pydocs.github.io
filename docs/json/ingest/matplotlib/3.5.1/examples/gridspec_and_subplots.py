������������bsdyj"""
==================================================
Combining two subplots using subplots and GridSpec
==================================================

Sometimes we want to combine two subplots in an axes layout created with
`~.Figure.subplots`.  We can get the `~.gridspec.GridSpec` from the axes
and then remove the covered axes and fill the gap with a new bigger axes.
Here we create a layout with the bottom two axes in the last column combined.

To start with this layout (rather than removing the overlapping axes) use
`~.pyplot.subplot_mosaic`.

See also :doc:`/tutorials/intermediate/arranging_axes`.
"""���`a
���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���`a
���`cfig���`a,���`a ���`caxs���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`encols���aoa=���bmia3���`a,���`a ���`enrows���aoa=���bmia3���`a)���`a
���`bgs���`a ���aoa=���`a ���`caxs���`a[���bmia1���`a,���`a ���bmia2���`a]���aoa.���`lget_gridspec���`a(���`a)���`a
���bc1x# remove the underlying axes���`a
���akcfor���`a ���`bax���`a ���bowbin���`a ���`caxs���`a[���bmia1���`a:���`a,���`a ���aoa-���bmia1���`a]���`a:���`a
���`d    ���`bax���aoa.���`fremove���`a(���`a)���`a
���`eaxbig���`a ���aoa=���`a ���`cfig���aoa.���`kadd_subplot���`a(���`bgs���`a[���bmia1���`a:���`a,���`a ���aoa-���bmia1���`a]���`a)���`a
���`eaxbig���aoa.���`hannotate���`a(���bs1a'���bs1iBig Axes ���bseb\n���bs1pGridSpec[1:, -1]���bs1a'���`a,���`a ���`a(���bmfc0.1���`a,���`a ���bmfc0.5���`a)���`a,���`a
���`o               ���`hxycoords���aoa=���bs1a'���bs1maxes fraction���bs1a'���`a,���`a ���`bva���aoa=���bs1a'���bs1fcenter���bs1a'���`a)���`a
���`a
���`cfig���aoa.���`ltight_layout���`a(���`a)���`a
���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
`dNone�