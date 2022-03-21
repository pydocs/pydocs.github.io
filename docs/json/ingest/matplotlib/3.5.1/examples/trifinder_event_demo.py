��������"���bsdy"""
====================
Trifinder Event Demo
====================

Example showing the use of a TriFinder object.  As the mouse is moved over the
triangulation, the triangle under the cursor is highlighted and the index of
the triangle is displayed in the plot title.
"""���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���bkndfrom���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnctri���`a ���bknfimport���`a ���`mTriangulation���`a
���bkndfrom���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnngpatches���`a ���bknfimport���`a ���`gPolygon���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���`a
���`a
���akcdef���`a ���bnfnupdate_polygon���`a(���`ctri���`a)���`a:���`a
���`d    ���akbif���`a ���`ctri���`a ���aob==���`a ���aoa-���bmia1���`a:���`a
���`h        ���`fpoints���`a ���aoa=���`a ���`a[���bmia0���`a,���`a ���bmia0���`a,���`a ���bmia0���`a]���`a
���`d    ���akdelse���`a:���`a
���`h        ���`fpoints���`a ���aoa=���`a ���`ftriang���aoa.���`itriangles���`a[���`ctri���`a]���`a
���`d    ���`bxs���`a ���aoa=���`a ���`ftriang���aoa.���`ax���`a[���`fpoints���`a]���`a
���`d    ���`bys���`a ���aoa=���`a ���`ftriang���aoa.���`ay���`a[���`fpoints���`a]���`a
���`d    ���`gpolygon���aoa.���`fset_xy���`a(���`bnp���aoa.���`lcolumn_stack���`a(���`a[���`bxs���`a,���`a ���`bys���`a]���`a)���`a)���`a
���`a
���`a
���akcdef���`a ���bnfmon_mouse_move���`a(���`eevent���`a)���`a:���`a
���`d    ���akbif���`a ���`eevent���aoa.���`finaxes���`a ���bowbis���`a ���bkcdNone���`a:���`a
���`h        ���`ctri���`a ���aoa=���`a ���aoa-���bmia1���`a
���`d    ���akdelse���`a:���`a
���`h        ���`ctri���`a ���aoa=���`a ���`itrifinder���`a(���`eevent���aoa.���`exdata���`a,���`a ���`eevent���aoa.���`eydata���`a)���`a
���`d    ���`nupdate_polygon���`a(���`ctri���`a)���`a
���`d    ���`bax���aoa.���`iset_title���`a(���bsaaf���bs1a'���bs1lIn triangle ���bsia{���`ctri���bsia}���bs1a'���`a)���`a
���`d    ���`eevent���aoa.���`fcanvas���aoa.���`ddraw���`a(���`a)���`a
���`a
���`a
���bc1x# Create a Triangulation.���`a
���`hn_angles���`a ���aoa=���`a ���bmib16���`a
���`gn_radii���`a ���aoa=���`a ���bmia5���`a
���`jmin_radius���`a ���aoa=���`a ���bmfd0.25���`a
���`eradii���`a ���aoa=���`a ���`bnp���aoa.���`hlinspace���`a(���`jmin_radius���`a,���`a ���bmfd0.95���`a,���`a ���`gn_radii���`a)���`a
���`fangles���`a ���aoa=���`a ���`bnp���aoa.���`hlinspace���`a(���bmia0���`a,���`a ���bmia2���`a ���aoa*���`a ���`bnp���aoa.���`bpi���`a,���`a ���`hn_angles���`a,���`a ���`hendpoint���aoa=���bkceFalse���`a)���`a
���`fangles���`a ���aoa=���`a ���`bnp���aoa.���`frepeat���`a(���`fangles���`a[���aoa.���aoa.���aoa.���`a,���`a ���`bnp���aoa.���`gnewaxis���`a]���`a,���`a ���`gn_radii���`a,���`a ���`daxis���aoa=���bmia1���`a)���`a
���`fangles���`a[���`a:���`a,���`a ���bmia1���`a:���`a:���bmia2���`a]���`a ���aoa+���aoa=���`a ���`bnp���aoa.���`bpi���`a ���aoa/���`a ���`hn_angles���`a
���`ax���`a ���aoa=���`a ���`a(���`eradii���aoa*���`bnp���aoa.���`ccos���`a(���`fangles���`a)���`a)���aoa.���`gflatten���`a(���`a)���`a
���`ay���`a ���aoa=���`a ���`a(���`eradii���aoa*���`bnp���aoa.���`csin���`a(���`fangles���`a)���`a)���aoa.���`gflatten���`a(���`a)���`a
���`ftriang���`a ���aoa=���`a ���`mTriangulation���`a(���`ax���`a,���`a ���`ay���`a)���`a
���`ftriang���aoa.���`hset_mask���`a(���`bnp���aoa.���`ehypot���`a(���`ax���`a[���`ftriang���aoa.���`itriangles���`a]���aoa.���`dmean���`a(���`daxis���aoa=���bmia1���`a)���`a,���`a
���`x                         ���`ay���`a[���`ftriang���aoa.���`itriangles���`a]���aoa.���`dmean���`a(���`daxis���aoa=���bmia1���`a)���`a)���`a
���`p                ���aoa<���`a ���`jmin_radius���`a)���`a
���`a
���bc1x3# Use the triangulation's default TriFinder object.���`a
���`itrifinder���`a ���aoa=���`a ���`ftriang���aoa.���`mget_trifinder���`a(���`a)���`a
���`a
���bc1x# Setup plot and callbacks.���`a
���`cfig���`a,���`a ���`bax���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`jsubplot_kw���aoa=���`a{���bs1a'���bs1faspect���bs1a'���`a:���`a ���bs1a'���bs1eequal���bs1a'���`a}���`a)���`a
���`bax���aoa.���`gtriplot���`a(���`ftriang���`a,���`a ���bs1a'���bs1cbo-���bs1a'���`a)���`a
���`gpolygon���`a ���aoa=���`a ���`gPolygon���`a(���`a[���`a[���bmia0���`a,���`a ���bmia0���`a]���`a,���`a ���`a[���bmia0���`a,���`a ���bmia0���`a]���`a]���`a,���`a ���`ifacecolor���aoa=���bs1a'���bs1ay���bs1a'���`a)���`b  ���bc1x# dummy data for (xs, ys)���`a
���`nupdate_polygon���`a(���aoa-���bmia1���`a)���`a
���`bax���aoa.���`iadd_patch���`a(���`gpolygon���`a)���`a
���`cfig���aoa.���`fcanvas���aoa.���`kmpl_connect���`a(���bs1a'���bs1smotion_notify_event���bs1a'���`a,���`a ���`mon_mouse_move���`a)���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
`dNone�