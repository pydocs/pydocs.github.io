�������� ���bsdx�"""
============
Mouse Cursor
============

This example sets an alternative cursor on a figure canvas.

Note, this is an interactive example, and must be run to see the effect.
"""���`a
���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���bkndfrom���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnmbackend_tools���`a ���bknfimport���`a ���`gCursors���`a
���`a
���`a
���`cfig���`a,���`a ���`caxs���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���bnbclen���`a(���`gCursors���`a)���`a,���`a ���`gfigsize���aoa=���`a(���bmia6���`a,���`a ���bnbclen���`a(���`gCursors���`a)���`a ���aoa+���`a ���bmfc0.5���`a)���`a,���`a
���`x                        ���`kgridspec_kw���aoa=���`a{���bs1a'���bs1fhspace���bs1a'���`a:���`a ���bmia0���`a}���`a)���`a
���`cfig���aoa.���`hsuptitle���`a(���bs1a'���bs1x+Hover over an Axes to see alternate Cursors���bs1a'���`a)���`a
���`a
���akcfor���`a ���`fcursor���`a,���`a ���`bax���`a ���bowbin���`a ���bnbczip���`a(���`gCursors���`a,���`a ���`caxs���`a)���`a:���`a
���`d    ���`bax���aoa.���`mcursor_to_use���`a ���aoa=���`a ���`fcursor���`a
���`d    ���`bax���aoa.���`dtext���`a(���bmfc0.5���`a,���`a ���bmfc0.5���`a,���`a ���`fcursor���aoa.���`dname���`a,���`a
���`l            ���`shorizontalalignment���aoa=���bs1a'���bs1fcenter���bs1a'���`a,���`a ���`qverticalalignment���aoa=���bs1a'���bs1fcenter���bs1a'���`a)���`a
���`d    ���`bax���aoa.���`cset���`a(���`fxticks���aoa=���`a[���`a]���`a,���`a ���`fyticks���aoa=���`a[���`a]���`a)���`a
���`a
���`a
���akcdef���`a ���bnfehover���`a(���`eevent���`a)���`a:���`a
���`d    ���akbif���`a ���`cfig���aoa.���`fcanvas���aoa.���`jwidgetlock���aoa.���`flocked���`a(���`a)���`a:���`a
���`h        ���bc1x<# Don't do anything if the zoom/pan tools have been enabled.���`a
���`h        ���akfreturn���`a
���`a
���`d    ���`cfig���aoa.���`fcanvas���aoa.���`jset_cursor���`a(���`a
���`h        ���`eevent���aoa.���`finaxes���aoa.���`mcursor_to_use���`a ���akbif���`a ���`eevent���aoa.���`finaxes���`a ���akdelse���`a ���`gCursors���aoa.���`gPOINTER���`a)���`a
���`a
���`a
���`cfig���aoa.���`fcanvas���aoa.���`kmpl_connect���`a(���bs1a'���bs1smotion_notify_event���bs1a'���`a,���`a ���`ehover���`a)���`a
���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
���`a
���bc1xM#############################################################################���`a
���bc1a#���`a
���bc1x# .. admonition:: References���`a
���bc1a#���`a
���bc1xN#    The use of the following functions, methods, classes and modules is shown���`a
���bc1u#    in this example:���`a
���bc1a#���`a
���bc1x=#    - `matplotlib.backend_bases.FigureCanvasBase.set_cursor`���`a
`dNone�