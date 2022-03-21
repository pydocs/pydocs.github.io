�����������bsdy """
======================================
Projecting filled contour onto a graph
======================================

Demonstrates displaying a 3D surface while also projecting filled contour
'profiles' onto the 'walls' of the graph.

See contour3d_demo2 for the unfilled version.
"""���`a
���`a
���bkndfrom���`a ���bnnlmpl_toolkits���bnna.���bnngmplot3d���`a ���bknfimport���`a ���`faxes3d���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���bkndfrom���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����`a ���bknfimport���`a ���`bcm���`a
���`a
���`bax���`a ���aoa=���`a ���`cplt���aoa.���`ffigure���`a(���`a)���aoa.���`kadd_subplot���`a(���`jprojection���aoa=���bs1a'���bs1b3d���bs1a'���`a)���`a
���`aX���`a,���`a ���`aY���`a,���`a ���`aZ���`a ���aoa=���`a ���`faxes3d���aoa.���`mget_test_data���`a(���bmfd0.05���`a)���`a
���`a
���bc1u# Plot the 3D surface���`a
���`bax���aoa.���`lplot_surface���`a(���`aX���`a,���`a ���`aY���`a,���`a ���`aZ���`a,���`a ���`grstride���aoa=���bmia8���`a,���`a ���`gcstride���aoa=���bmia8���`a,���`a ���`ealpha���aoa=���bmfc0.3���`a)���`a
���`a
���bc1xK# Plot projections of the contours for each dimension.  By choosing offsets���`a
���bc1xL# that match the appropriate axes limits, the projected contours will sit on���`a
���bc1x# the 'walls' of the graph���`a
���`bax���aoa.���`hcontourf���`a(���`aX���`a,���`a ���`aY���`a,���`a ���`aZ���`a,���`a ���`dzdir���aoa=���bs1a'���bs1az���bs1a'���`a,���`a ���`foffset���aoa=���aoa-���bmic100���`a,���`a ���`dcmap���aoa=���`bcm���aoa.���`hcoolwarm���`a)���`a
���`bax���aoa.���`hcontourf���`a(���`aX���`a,���`a ���`aY���`a,���`a ���`aZ���`a,���`a ���`dzdir���aoa=���bs1a'���bs1ax���bs1a'���`a,���`a ���`foffset���aoa=���aoa-���bmib40���`a,���`a ���`dcmap���aoa=���`bcm���aoa.���`hcoolwarm���`a)���`a
���`bax���aoa.���`hcontourf���`a(���`aX���`a,���`a ���`aY���`a,���`a ���`aZ���`a,���`a ���`dzdir���aoa=���bs1a'���bs1ay���bs1a'���`a,���`a ���`foffset���aoa=���bmib40���`a,���`a ���`dcmap���aoa=���`bcm���aoa.���`hcoolwarm���`a)���`a
���`a
���`bax���aoa.���`cset���`a(���`dxlim���aoa=���`a(���aoa-���bmib40���`a,���`a ���bmib40���`a)���`a,���`a ���`dylim���aoa=���`a(���aoa-���bmib40���`a,���`a ���bmib40���`a)���`a,���`a ���`dzlim���aoa=���`a(���aoa-���bmic100���`a,���`a ���bmic100���`a)���`a,���`a
���`g       ���`fxlabel���aoa=���bs1a'���bs1aX���bs1a'���`a,���`a ���`fylabel���aoa=���bs1a'���bs1aY���bs1a'���`a,���`a ���`fzlabel���aoa=���bs1a'���bs1aZ���bs1a'���`a)���`a
���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
`dNone�