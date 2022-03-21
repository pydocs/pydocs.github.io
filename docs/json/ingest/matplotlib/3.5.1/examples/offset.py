������������bsdy�"""
=========================
Automatic Text Offsetting
=========================

This example demonstrates mplot3d's offset text display.
As one rotates the 3D figure, the offsets should remain oriented the
same way as the axis label, and should also be located "away"
from the center of the plot.

This demo triggers the display of the offset text for the x and
y axis by adding 1e5 to X and Y. Anything less would not
automatically trigger it.
"""���`a
���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���`a
���`a
���`bax���`a ���aoa=���`a ���`cplt���aoa.���`ffigure���`a(���`a)���aoa.���`kadd_subplot���`a(���`jprojection���aoa=���bs1a'���bs1b3d���bs1a'���`a)���`a
���`a
���`aX���`a,���`a ���`aY���`a ���aoa=���`a ���`bnp���aoa.���`emgrid���`a[���bmia0���`a:���bmia6���aoa*���`bnp���aoa.���`bpi���`a:���bmfd0.25���`a,���`a ���bmia0���`a:���bmia4���aoa*���`bnp���aoa.���`bpi���`a:���bmfd0.25���`a]���`a
���`aZ���`a ���aoa=���`a ���`bnp���aoa.���`dsqrt���`a(���`bnp���aoa.���`cabs���`a(���`bnp���aoa.���`ccos���`a(���`aX���`a)���`a ���aoa+���`a ���`bnp���aoa.���`ccos���`a(���`aY���`a)���`a)���`a)���`a
���`a
���`bax���aoa.���`lplot_surface���`a(���`aX���`a ���aoa+���`a ���bmfc1e5���`a,���`a ���`aY���`a ���aoa+���`a ���bmfc1e5���`a,���`a ���`aZ���`a,���`a ���`dcmap���aoa=���bs1a'���bs1fautumn���bs1a'���`a,���`a ���`gcstride���aoa=���bmia2���`a,���`a ���`grstride���aoa=���bmia2���`a)���`a
���`a
���`bax���aoa.���`jset_xlabel���`a(���bs2a"���bs2gX label���bs2a"���`a)���`a
���`bax���aoa.���`jset_ylabel���`a(���bs2a"���bs2gY label���bs2a"���`a)���`a
���`bax���aoa.���`jset_zlabel���`a(���bs2a"���bs2gZ label���bs2a"���`a)���`a
���`bax���aoa.���`hset_zlim���`a(���bmia0���`a,���`a ���bmia2���`a)���`a
���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
`dNone�