��������H���bsdx�"""
============================
Circles, Wedges and Polygons
============================

This example demonstrates how to use `.collections.PatchCollection`.
"""���`a
���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���bkndfrom���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnngpatches���`a ���bknfimport���`a ���`fCircle���`a,���`a ���`eWedge���`a,���`a ���`gPolygon���`a
���bkndfrom���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnkcollections���`a ���bknfimport���`a ���`oPatchCollection���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���`a
���bc1x)# Fixing random state for reproducibility���`a
���`bnp���aoa.���`frandom���aoa.���`dseed���`a(���bmih19680801���`a)���`a
���`a
���`a
���`cfig���`a,���`a ���`bax���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`a)���`a
���`a
���`jresolution���`a ���aoa=���`a ���bmib50���`b  ���bc1x# the number of vertices���`a
���`aN���`a ���aoa=���`a ���bmia3���`a
���`ax���`a ���aoa=���`a ���`bnp���aoa.���`frandom���aoa.���`drand���`a(���`aN���`a)���`a
���`ay���`a ���aoa=���`a ���`bnp���aoa.���`frandom���aoa.���`drand���`a(���`aN���`a)���`a
���`eradii���`a ���aoa=���`a ���bmfc0.1���aoa*���`bnp���aoa.���`frandom���aoa.���`drand���`a(���`aN���`a)���`a
���`gpatches���`a ���aoa=���`a ���`a[���`a]���`a
���akcfor���`a ���`bx1���`a,���`a ���`by1���`a,���`a ���`ar���`a ���bowbin���`a ���bnbczip���`a(���`ax���`a,���`a ���`ay���`a,���`a ���`eradii���`a)���`a:���`a
���`d    ���`fcircle���`a ���aoa=���`a ���`fCircle���`a(���`a(���`bx1���`a,���`a ���`by1���`a)���`a,���`a ���`ar���`a)���`a
���`d    ���`gpatches���aoa.���`fappend���`a(���`fcircle���`a)���`a
���`a
���`ax���`a ���aoa=���`a ���`bnp���aoa.���`frandom���aoa.���`drand���`a(���`aN���`a)���`a
���`ay���`a ���aoa=���`a ���`bnp���aoa.���`frandom���aoa.���`drand���`a(���`aN���`a)���`a
���`eradii���`a ���aoa=���`a ���bmfc0.1���aoa*���`bnp���aoa.���`frandom���aoa.���`drand���`a(���`aN���`a)���`a
���`ftheta1���`a ���aoa=���`a ���bmfe360.0���aoa*���`bnp���aoa.���`frandom���aoa.���`drand���`a(���`aN���`a)���`a
���`ftheta2���`a ���aoa=���`a ���bmfe360.0���aoa*���`bnp���aoa.���`frandom���aoa.���`drand���`a(���`aN���`a)���`a
���akcfor���`a ���`bx1���`a,���`a ���`by1���`a,���`a ���`ar���`a,���`a ���`bt1���`a,���`a ���`bt2���`a ���bowbin���`a ���bnbczip���`a(���`ax���`a,���`a ���`ay���`a,���`a ���`eradii���`a,���`a ���`ftheta1���`a,���`a ���`ftheta2���`a)���`a:���`a
���`d    ���`ewedge���`a ���aoa=���`a ���`eWedge���`a(���`a(���`bx1���`a,���`a ���`by1���`a)���`a,���`a ���`ar���`a,���`a ���`bt1���`a,���`a ���`bt2���`a)���`a
���`d    ���`gpatches���aoa.���`fappend���`a(���`ewedge���`a)���`a
���`a
���bc1x## Some limiting conditions on Wedge���`a
���`gpatches���`a ���aoa+���aoa=���`a ���`a[���`a
���`d    ���`eWedge���`a(���`a(���bmfb.3���`a,���`a ���bmfb.7���`a)���`a,���`a ���bmfb.1���`a,���`a ���bmia0���`a,���`a ���bmic360���`a)���`a,���`m             ���bc1m# Full circle���`a
���`d    ���`eWedge���`a(���`a(���bmfb.7���`a,���`a ���bmfb.8���`a)���`a,���`a ���bmfb.2���`a,���`a ���bmia0���`a,���`a ���bmic360���`a,���`a ���`ewidth���aoa=���bmfd0.05���`a)���`a,���`b  ���bc1k# Full ring���`a
���`d    ���`eWedge���`a(���`a(���bmfb.8���`a,���`a ���bmfb.3���`a)���`a,���`a ���bmfb.2���`a,���`a ���bmia0���`a,���`a ���bmib45���`a)���`a,���`n              ���bc1m# Full sector���`a
���`d    ���`eWedge���`a(���`a(���bmfb.8���`a,���`a ���bmfb.3���`a)���`a,���`a ���bmfb.2���`a,���`a ���bmib45���`a,���`a ���bmib90���`a,���`a ���`ewidth���aoa=���bmfd0.10���`a)���`a,���`b  ���bc1m# Ring sector���`a
���`a]���`a
���`a
���akcfor���`a ���`ai���`a ���bowbin���`a ���bnberange���`a(���`aN���`a)���`a:���`a
���`d    ���`gpolygon���`a ���aoa=���`a ���`gPolygon���`a(���`bnp���aoa.���`frandom���aoa.���`drand���`a(���`aN���`a,���`a ���bmia2���`a)���`a,���`a ���bkcdTrue���`a)���`a
���`d    ���`gpatches���aoa.���`fappend���`a(���`gpolygon���`a)���`a
���`a
���`fcolors���`a ���aoa=���`a ���bmic100���`a ���aoa*���`a ���`bnp���aoa.���`frandom���aoa.���`drand���`a(���bnbclen���`a(���`gpatches���`a)���`a)���`a
���`ap���`a ���aoa=���`a ���`oPatchCollection���`a(���`gpatches���`a,���`a ���`ealpha���aoa=���bmfc0.4���`a)���`a
���`ap���aoa.���`iset_array���`a(���`fcolors���`a)���`a
���`bax���aoa.���`nadd_collection���`a(���`ap���`a)���`a
���`cfig���aoa.���`hcolorbar���`a(���`ap���`a,���`a ���`bax���aoa=���`bax���`a)���`a
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
���bc1x#    - `matplotlib.patches`���`a
���bc1x"#    - `matplotlib.patches.Circle`���`a
���bc1x!#    - `matplotlib.patches.Wedge`���`a
���bc1x##    - `matplotlib.patches.Polygon`���`a
���bc1x/#    - `matplotlib.collections.PatchCollection`���`a
���bc1x4#    - `matplotlib.collections.Collection.set_array`���`a
���bc1x,#    - `matplotlib.axes.Axes.add_collection`���`a
���bc1x*#    - `matplotlib.figure.Figure.colorbar`���`a
`dNone�