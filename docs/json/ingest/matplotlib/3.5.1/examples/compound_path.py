��������*���bsdx�"""
=============
Compound path
=============

Make a compound path -- in this case two simple polygons, a rectangle
and a triangle.  Use ``CLOSEPOLY`` and ``MOVETO`` for the different parts of
the compound path
"""���`a
���`a
���bkndfrom���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnndpath���`a ���bknfimport���`a ���`dPath���`a
���bkndfrom���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnngpatches���`a ���bknfimport���`a ���`iPathPatch���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���`a
���`hvertices���`a ���aoa=���`a ���`a[���`a]���`a
���`ecodes���`a ���aoa=���`a ���`a[���`a]���`a
���`a
���`ecodes���`a ���aoa=���`a ���`a[���`dPath���aoa.���`fMOVETO���`a]���`a ���aoa+���`a ���`a[���`dPath���aoa.���`fLINETO���`a]���aoa*���bmia3���`a ���aoa+���`a ���`a[���`dPath���aoa.���`iCLOSEPOLY���`a]���`a
���`hvertices���`a ���aoa=���`a ���`a[���`a(���bmia1���`a,���`a ���bmia1���`a)���`a,���`a ���`a(���bmia1���`a,���`a ���bmia2���`a)���`a,���`a ���`a(���bmia2���`a,���`a ���bmia2���`a)���`a,���`a ���`a(���bmia2���`a,���`a ���bmia1���`a)���`a,���`a ���`a(���bmia0���`a,���`a ���bmia0���`a)���`a]���`a
���`a
���`ecodes���`a ���aoa+���aoa=���`a ���`a[���`dPath���aoa.���`fMOVETO���`a]���`a ���aoa+���`a ���`a[���`dPath���aoa.���`fLINETO���`a]���aoa*���bmia2���`a ���aoa+���`a ���`a[���`dPath���aoa.���`iCLOSEPOLY���`a]���`a
���`hvertices���`a ���aoa+���aoa=���`a ���`a[���`a(���bmia4���`a,���`a ���bmia4���`a)���`a,���`a ���`a(���bmia5���`a,���`a ���bmia5���`a)���`a,���`a ���`a(���bmia5���`a,���`a ���bmia4���`a)���`a,���`a ���`a(���bmia0���`a,���`a ���bmia0���`a)���`a]���`a
���`a
���`dpath���`a ���aoa=���`a ���`dPath���`a(���`hvertices���`a,���`a ���`ecodes���`a)���`a
���`a
���`ipathpatch���`a ���aoa=���`a ���`iPathPatch���`a(���`dpath���`a,���`a ���`ifacecolor���aoa=���bs1a'���bs1dnone���bs1a'���`a,���`a ���`iedgecolor���aoa=���bs1a'���bs1egreen���bs1a'���`a)���`a
���`a
���`cfig���`a,���`a ���`bax���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`a)���`a
���`bax���aoa.���`iadd_patch���`a(���`ipathpatch���`a)���`a
���`bax���aoa.���`iset_title���`a(���bs1a'���bs1oA compound path���bs1a'���`a)���`a
���`a
���`bax���aoa.���`nautoscale_view���`a(���`a)���`a
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
���bc1x#    - `matplotlib.path`���`a
���bc1x#    - `matplotlib.path.Path`���`a
���bc1x#    - `matplotlib.patches`���`a
���bc1x%#    - `matplotlib.patches.PathPatch`���`a
���bc1x'#    - `matplotlib.axes.Axes.add_patch`���`a
���bc1x,#    - `matplotlib.axes.Axes.autoscale_view`���`a
`dNone�