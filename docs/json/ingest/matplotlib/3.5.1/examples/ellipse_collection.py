�����������bsdy#"""
==================
Ellipse Collection
==================

Drawing a collection of ellipses. While this would equally be possible using
a `~.collections.EllipseCollection` or `~.collections.PathCollection`, the use
of an `~.collections.EllipseCollection` allows for much shorter code.
"""���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���bkndfrom���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnkcollections���`a ���bknfimport���`a ���`qEllipseCollection���`a
���`a
���`ax���`a ���aoa=���`a ���`bnp���aoa.���`farange���`a(���bmib10���`a)���`a
���`ay���`a ���aoa=���`a ���`bnp���aoa.���`farange���`a(���bmib15���`a)���`a
���`aX���`a,���`a ���`aY���`a ���aoa=���`a ���`bnp���aoa.���`hmeshgrid���`a(���`ax���`a,���`a ���`ay���`a)���`a
���`a
���`bXY���`a ���aoa=���`a ���`bnp���aoa.���`lcolumn_stack���`a(���`a(���`aX���aoa.���`eravel���`a(���`a)���`a,���`a ���`aY���aoa.���`eravel���`a(���`a)���`a)���`a)���`a
���`a
���`bww���`a ���aoa=���`a ���`aX���`a ���aoa/���`a ���bmfd10.0���`a
���`bhh���`a ���aoa=���`a ���`aY���`a ���aoa/���`a ���bmfd15.0���`a
���`baa���`a ���aoa=���`a ���`aX���`a ���aoa*���`a ���bmia9���`a
���`a
���`a
���`cfig���`a,���`a ���`bax���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`a)���`a
���`a
���`bec���`a ���aoa=���`a ���`qEllipseCollection���`a(���`bww���`a,���`a ���`bhh���`a,���`a ���`baa���`a,���`a ���`eunits���aoa=���bs1a'���bs1ax���bs1a'���`a,���`a ���`goffsets���aoa=���`bXY���`a,���`a
���`w                       ���`ktransOffset���aoa=���`bax���aoa.���`itransData���`a)���`a
���`bec���aoa.���`iset_array���`a(���`a(���`aX���`a ���aoa+���`a ���`aY���`a)���aoa.���`eravel���`a(���`a)���`a)���`a
���`bax���aoa.���`nadd_collection���`a(���`bec���`a)���`a
���`bax���aoa.���`nautoscale_view���`a(���`a)���`a
���`bax���aoa.���`jset_xlabel���`a(���bs1a'���bs1aX���bs1a'���`a)���`a
���`bax���aoa.���`jset_ylabel���`a(���bs1a'���bs1ay���bs1a'���`a)���`a
���`dcbar���`a ���aoa=���`a ���`cplt���aoa.���`hcolorbar���`a(���`bec���`a)���`a
���`dcbar���aoa.���`iset_label���`a(���bs1a'���bs1cX+Y���bs1a'���`a)���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
���`a
���bc1xM#############################################################################���`a
���bc1a#���`a
���bc1x# .. admonition:: References���`a
���bc1a#���`a
���bc1xN#    The use of the following functions, methods, classes and modules is shown���`a
���bc1u#    in this example:���`a
���bc1a#���`a
���bc1x#    - `matplotlib.collections`���`a
���bc1x1#    - `matplotlib.collections.EllipseCollection`���`a
���bc1x,#    - `matplotlib.axes.Axes.add_collection`���`a
���bc1x,#    - `matplotlib.axes.Axes.autoscale_view`���`a
���bc1x/#    - `matplotlib.cm.ScalarMappable.set_array`���`a
`dNone�