��������7���bsdy�"""
===========
Zoom Window
===========

This example shows how to connect events in one window, for example, a mouse
press, to another figure window.

If you click on a point in the first window, the z and y limits of the second
will be adjusted so that the center of the zoom in the second window will be
the (x, y) coordinates of the clicked point.

Note the diameter of the circles in the scatter are defined in points**2, so
their size is independent of the zoom.
"""���`a
���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���`a
���`a
���bc1x)# Fixing random state for reproducibility���`a
���`bnp���aoa.���`frandom���aoa.���`dseed���`a(���bmih19680801���`a)���`a
���`a
���`ffigsrc���`a,���`a ���`eaxsrc���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`a)���`a
���`gfigzoom���`a,���`a ���`faxzoom���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`a)���`a
���`eaxsrc���aoa.���`cset���`a(���`dxlim���aoa=���`a(���bmia0���`a,���`a ���bmia1���`a)���`a,���`a ���`dylim���aoa=���`a(���bmia0���`a,���`a ���bmia1���`a)���`a,���`a ���`lautoscale_on���aoa=���bkceFalse���`a,���`a
���`j          ���`etitle���aoa=���bs1a'���bs1mClick to zoom���bs1a'���`a)���`a
���`faxzoom���aoa.���`cset���`a(���`dxlim���aoa=���`a(���bmfd0.45���`a,���`a ���bmfd0.55���`a)���`a,���`a ���`dylim���aoa=���`a(���bmfc0.4���`a,���`a ���bmfc0.6���`a)���`a,���`a ���`lautoscale_on���aoa=���bkceFalse���`a,���`a
���`k           ���`etitle���aoa=���bs1a'���bs1kZoom window���bs1a'���`a)���`a
���`a
���`ax���`a,���`a ���`ay���`a,���`a ���`as���`a,���`a ���`ac���`a ���aoa=���`a ���`bnp���aoa.���`frandom���aoa.���`drand���`a(���bmia4���`a,���`a ���bmic200���`a)���`a
���`as���`a ���aoa*���aoa=���`a ���bmic200���`a
���`a
���`eaxsrc���aoa.���`gscatter���`a(���`ax���`a,���`a ���`ay���`a,���`a ���`as���`a,���`a ���`ac���`a)���`a
���`faxzoom���aoa.���`gscatter���`a(���`ax���`a,���`a ���`ay���`a,���`a ���`as���`a,���`a ���`ac���`a)���`a
���`a
���`a
���akcdef���`a ���bnfhon_press���`a(���`eevent���`a)���`a:���`a
���`d    ���akbif���`a ���`eevent���aoa.���`fbutton���`a ���aob!=���`a ���bmia1���`a:���`a
���`h        ���akfreturn���`a
���`d    ���`ax���`a,���`a ���`ay���`a ���aoa=���`a ���`eevent���aoa.���`exdata���`a,���`a ���`eevent���aoa.���`eydata���`a
���`d    ���`faxzoom���aoa.���`hset_xlim���`a(���`ax���`a ���aoa-���`a ���bmfc0.1���`a,���`a ���`ax���`a ���aoa+���`a ���bmfc0.1���`a)���`a
���`d    ���`faxzoom���aoa.���`hset_ylim���`a(���`ay���`a ���aoa-���`a ���bmfc0.1���`a,���`a ���`ay���`a ���aoa+���`a ���bmfc0.1���`a)���`a
���`d    ���`gfigzoom���aoa.���`fcanvas���aoa.���`ddraw���`a(���`a)���`a
���`a
���`ffigsrc���aoa.���`fcanvas���aoa.���`kmpl_connect���`a(���bs1a'���bs1rbutton_press_event���bs1a'���`a,���`a ���`hon_press���`a)���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
`dNone�