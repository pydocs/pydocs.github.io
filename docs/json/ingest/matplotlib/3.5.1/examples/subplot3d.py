��������S���bsdxs"""
====================
3D plots as subplots
====================

Demonstrate including 3D plots as subplots.
"""���`a
���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���bkndfrom���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����`a ���bknfimport���`a ���`bcm���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���`a
���bkndfrom���`a ���bnnlmpl_toolkits���bnna.���bnngmplot3d���bnna.���bnnfaxes3d���`a ���bknfimport���`a ���`mget_test_data���`a
���`a
���`a
���bc1x-# set up a figure twice as wide as it is tall���`a
���`cfig���`a ���aoa=���`a ���`cplt���aoa.���`ffigure���`a(���`gfigsize���aoa=���`cplt���aoa.���`ifigaspect���`a(���bmfc0.5���`a)���`a)���`a
���`a
���bc1o# =============���`a
���bc1o# First subplot���`a
���bc1o# =============���`a
���bc1x$# set up the axes for the first plot���`a
���`bax���`a ���aoa=���`a ���`cfig���aoa.���`kadd_subplot���`a(���bmia1���`a,���`a ���bmia2���`a,���`a ���bmia1���`a,���`a ���`jprojection���aoa=���bs1a'���bs1b3d���bs1a'���`a)���`a
���`a
���bc1x># plot a 3D surface like in the example mplot3d/surface3d_demo���`a
���`aX���`a ���aoa=���`a ���`bnp���aoa.���`farange���`a(���aoa-���bmia5���`a,���`a ���bmia5���`a,���`a ���bmfd0.25���`a)���`a
���`aY���`a ���aoa=���`a ���`bnp���aoa.���`farange���`a(���aoa-���bmia5���`a,���`a ���bmia5���`a,���`a ���bmfd0.25���`a)���`a
���`aX���`a,���`a ���`aY���`a ���aoa=���`a ���`bnp���aoa.���`hmeshgrid���`a(���`aX���`a,���`a ���`aY���`a)���`a
���`aR���`a ���aoa=���`a ���`bnp���aoa.���`dsqrt���`a(���`aX���aoa*���aoa*���bmia2���`a ���aoa+���`a ���`aY���aoa*���aoa*���bmia2���`a)���`a
���`aZ���`a ���aoa=���`a ���`bnp���aoa.���`csin���`a(���`aR���`a)���`a
���`dsurf���`a ���aoa=���`a ���`bax���aoa.���`lplot_surface���`a(���`aX���`a,���`a ���`aY���`a,���`a ���`aZ���`a,���`a ���`grstride���aoa=���bmia1���`a,���`a ���`gcstride���aoa=���bmia1���`a,���`a ���`dcmap���aoa=���`bcm���aoa.���`hcoolwarm���`a,���`a
���`w                       ���`ilinewidth���aoa=���bmia0���`a,���`a ���`kantialiased���aoa=���bkceFalse���`a)���`a
���`bax���aoa.���`hset_zlim���`a(���aoa-���bmfd1.01���`a,���`a ���bmfd1.01���`a)���`a
���`cfig���aoa.���`hcolorbar���`a(���`dsurf���`a,���`a ���`fshrink���aoa=���bmfc0.5���`a,���`a ���`faspect���aoa=���bmib10���`a)���`a
���`a
���bc1p# ==============���`a
���bc1p# Second subplot���`a
���bc1p# ==============���`a
���bc1x%# set up the axes for the second plot���`a
���`bax���`a ���aoa=���`a ���`cfig���aoa.���`kadd_subplot���`a(���bmia1���`a,���`a ���bmia2���`a,���`a ���bmia2���`a,���`a ���`jprojection���aoa=���bs1a'���bs1b3d���bs1a'���`a)���`a
���`a
���bc1x=# plot a 3D wireframe like in the example mplot3d/wire3d_demo���`a
���`aX���`a,���`a ���`aY���`a,���`a ���`aZ���`a ���aoa=���`a ���`mget_test_data���`a(���bmfd0.05���`a)���`a
���`bax���aoa.���`nplot_wireframe���`a(���`aX���`a,���`a ���`aY���`a,���`a ���`aZ���`a,���`a ���`grstride���aoa=���bmib10���`a,���`a ���`gcstride���aoa=���bmib10���`a)���`a
���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
`dNone�