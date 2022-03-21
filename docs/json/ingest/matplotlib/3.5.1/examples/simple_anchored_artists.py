������������bsdyZ"""
=======================
Simple Anchored Artists
=======================

This example illustrates the use of the anchored helper classes found in
:mod:`matplotlib.offsetbox` and in :mod:`mpl_toolkits.axes_grid1`.
An implementation of a similar figure, but without use of the toolkit,
can be found in :doc:`/gallery/misc/anchored_artists`.
"""���`a
���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���`a
���`a
���akcdef���`a ���bnfidraw_text���`a(���`bax���`a)���`a:���`a
���`d    ���bsdxn"""
    Draw two text-boxes, anchored by different corners to the upper-left
    corner of the figure.
    """���`a
���`d    ���bkndfrom���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnioffsetbox���`a ���bknfimport���`a ���`lAnchoredText���`a
���`d    ���`bat���`a ���aoa=���`a ���`lAnchoredText���`a(���bs2a"���bs2iFigure 1a���bs2a"���`a,���`a
���`v                      ���`cloc���aoa=���bs1a'���bs1jupper left���bs1a'���`a,���`a ���`dprop���aoa=���bnbddict���`a(���`dsize���aoa=���bmia8���`a)���`a,���`a ���`gframeon���aoa=���bkcdTrue���`a,���`a
���`v                      ���`a)���`a
���`d    ���`bat���aoa.���`epatch���aoa.���`lset_boxstyle���`a(���bs2a"���bs2xround,pad=0.,rounding_size=0.2���bs2a"���`a)���`a
���`d    ���`bax���aoa.���`jadd_artist���`a(���`bat���`a)���`a
���`a
���`d    ���`cat2���`a ���aoa=���`a ���`lAnchoredText���`a(���bs2a"���bs2kFigure 1(b)���bs2a"���`a,���`a
���`w                       ���`cloc���aoa=���bs1a'���bs1jlower left���bs1a'���`a,���`a ���`dprop���aoa=���bnbddict���`a(���`dsize���aoa=���bmia8���`a)���`a,���`a ���`gframeon���aoa=���bkcdTrue���`a,���`a
���`w                       ���`nbbox_to_anchor���aoa=���`a(���bmfb0.���`a,���`a ���bmfb1.���`a)���`a,���`a
���`w                       ���`nbbox_transform���aoa=���`bax���aoa.���`itransAxes���`a
���`w                       ���`a)���`a
���`d    ���`cat2���aoa.���`epatch���aoa.���`lset_boxstyle���`a(���bs2a"���bs2xround,pad=0.,rounding_size=0.2���bs2a"���`a)���`a
���`d    ���`bax���aoa.���`jadd_artist���`a(���`cat2���`a)���`a
���`a
���`a
���akcdef���`a ���bnfkdraw_circle���`a(���`bax���`a)���`a:���`a
���`d    ���bsdx1"""
    Draw a circle in axis coordinates
    """���`a
���`d    ���bkndfrom���`a ���bnnlmpl_toolkits���bnna.���bnnjaxes_grid1���bnna.���bnnpanchored_artists���`a ���bknfimport���`a ���`sAnchoredDrawingArea���`a
���`d    ���bkndfrom���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnngpatches���`a ���bknfimport���`a ���`fCircle���`a
���`d    ���`cada���`a ���aoa=���`a ���`sAnchoredDrawingArea���`a(���bmib20���`a,���`a ���bmib20���`a,���`a ���bmia0���`a,���`a ���bmia0���`a,���`a
���`x                              ���`cloc���aoa=���bs1a'���bs1kupper right���bs1a'���`a,���`a ���`cpad���aoa=���bmfb0.���`a,���`a ���`gframeon���aoa=���bkceFalse���`a)���`a
���`d    ���`ap���`a ���aoa=���`a ���`fCircle���`a(���`a(���bmib10���`a,���`a ���bmib10���`a)���`a,���`a ���bmib10���`a)���`a
���`d    ���`cada���aoa.���`bda���aoa.���`jadd_artist���`a(���`ap���`a)���`a
���`d    ���`bax���aoa.���`jadd_artist���`a(���`cada���`a)���`a
���`a
���`a
���akcdef���`a ���bnfldraw_ellipse���`a(���`bax���`a)���`a:���`a
���`d    ���bsdxM"""
    Draw an ellipse of width=0.1, height=0.15 in data coordinates
    """���`a
���`d    ���bkndfrom���`a ���bnnlmpl_toolkits���bnna.���bnnjaxes_grid1���bnna.���bnnpanchored_artists���`a ���bknfimport���`a ���`oAnchoredEllipse���`a
���`d    ���`bae���`a ���aoa=���`a ���`oAnchoredEllipse���`a(���`bax���aoa.���`itransData���`a,���`a ���`ewidth���aoa=���bmfc0.1���`a,���`a ���`fheight���aoa=���bmfd0.15���`a,���`a ���`eangle���aoa=���bmfb0.���`a,���`a
���`x                         ���`cloc���aoa=���bs1a'���bs1jlower left���bs1a'���`a,���`a ���`cpad���aoa=���bmfc0.5���`a,���`a ���`iborderpad���aoa=���bmfc0.4���`a,���`a
���`x                         ���`gframeon���aoa=���bkcdTrue���`a)���`a
���`a
���`d    ���`bax���aoa.���`jadd_artist���`a(���`bae���`a)���`a
���`a
���`a
���akcdef���`a ���bnfldraw_sizebar���`a(���`bax���`a)���`a:���`a
���`d    ���bsdxp"""
    Draw a horizontal bar with length of 0.1 in data coordinates,
    with a fixed label underneath.
    """���`a
���`d    ���bkndfrom���`a ���bnnlmpl_toolkits���bnna.���bnnjaxes_grid1���bnna.���bnnpanchored_artists���`a ���bknfimport���`a ���`oAnchoredSizeBar���`a
���`d    ���`casb���`a ���aoa=���`a ���`oAnchoredSizeBar���`a(���`bax���aoa.���`itransData���`a,���`a
���`x                          ���bmfc0.1���`a,���`a
���`x                          ���bsaar���bs2a"���bs2c1$^���bs2a{���bs2a\���bs2gprime}$���bs2a"���`a,���`a
���`x                          ���`cloc���aoa=���bs1a'���bs1llower center���bs1a'���`a,���`a
���`x                          ���`cpad���aoa=���bmfc0.1���`a,���`a ���`iborderpad���aoa=���bmfc0.5���`a,���`a ���`csep���aoa=���bmia5���`a,���`a
���`x                          ���`gframeon���aoa=���bkceFalse���`a)���`a
���`d    ���`bax���aoa.���`jadd_artist���`a(���`casb���`a)���`a
���`a
���`a
���`cfig���`a,���`a ���`bax���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`a)���`a
���`bax���aoa.���`jset_aspect���`a(���bmfb1.���`a)���`a
���`a
���`idraw_text���`a(���`bax���`a)���`a
���`kdraw_circle���`a(���`bax���`a)���`a
���`ldraw_ellipse���`a(���`bax���`a)���`a
���`ldraw_sizebar���`a(���`bax���`a)���`a
���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
`dNone�