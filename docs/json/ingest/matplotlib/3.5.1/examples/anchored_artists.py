������������bsdy'"""
================
Anchored Artists
================

This example illustrates the use of the anchored objects without the
helper classes found in :mod:`mpl_toolkits.axes_grid1`. This version
of the figure is similar to the one found in
:doc:`/gallery/axes_grid1/simple_anchored_artists`, but it is
implemented using only the matplotlib namespace, without the help
of additional toolkits.

.. redirect-from:: /gallery/userdemo/anchored_box01
.. redirect-from:: /gallery/userdemo/anchored_box02
.. redirect-from:: /gallery/userdemo/anchored_box03
"""���`a
���`a
���bkndfrom���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����`a ���bknfimport���`a ���`fpyplot���`a ���akbas���`a ���`cplt���`a
���bkndfrom���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnelines���`a ���bknfimport���`a ���`fLine2D���`a
���bkndfrom���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnngpatches���`a ���bknfimport���`a ���`fCircle���`a,���`a ���`gEllipse���`a
���bkndfrom���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnioffsetbox���`a ���bknfimport���`a ���`a(���`a
���`d    ���`qAnchoredOffsetbox���`a,���`a ���`oAuxTransformBox���`a,���`a ���`kDrawingArea���`a,���`a ���`hTextArea���`a,���`a ���`gVPacker���`a)���`a
���`a
���`a
���akcdef���`a ���bnfidraw_text���`a(���`bax���`a)���`a:���`a
���`d    ���bsdxF"""Draw a text-box anchored to the upper-left corner of the figure."""���`a
���`d    ���`cbox���`a ���aoa=���`a ���`qAnchoredOffsetbox���`a(���`echild���aoa=���`hTextArea���`a(���bs2a"���bs2iFigure 1a���bs2a"���`a)���`a,���`a
���`x                            ���`cloc���aoa=���bs2a"���bs2jupper left���bs2a"���`a,���`a ���`gframeon���aoa=���bkcdTrue���`a)���`a
���`d    ���`cbox���aoa.���`epatch���aoa.���`lset_boxstyle���`a(���bs2a"���bs2xround,pad=0.,rounding_size=0.2���bs2a"���`a)���`a
���`d    ���`bax���aoa.���`jadd_artist���`a(���`cbox���`a)���`a
���`a
���`a
���akcdef���`a ���bnfldraw_circles���`a(���`bax���`a)���`a:���`a
���`d    ���bsdx'"""Draw circles in axes coordinates."""���`a
���`d    ���`darea���`a ���aoa=���`a ���`kDrawingArea���`a(���bmib40���`a,���`a ���bmib20���`a,���`a ���bmia0���`a,���`a ���bmia0���`a)���`a
���`d    ���`darea���aoa.���`jadd_artist���`a(���`fCircle���`a(���`a(���bmib10���`a,���`a ���bmib10���`a)���`a,���`a ���bmib10���`a,���`a ���`bfc���aoa=���bs2a"���bs2htab:blue���bs2a"���`a)���`a)���`a
���`d    ���`darea���aoa.���`jadd_artist���`a(���`fCircle���`a(���`a(���bmib30���`a,���`a ���bmib10���`a)���`a,���`a ���bmia5���`a,���`a ���`bfc���aoa=���bs2a"���bs2gtab:red���bs2a"���`a)���`a)���`a
���`d    ���`cbox���`a ���aoa=���`a ���`qAnchoredOffsetbox���`a(���`a
���`h        ���`echild���aoa=���`darea���`a,���`a ���`cloc���aoa=���bs2a"���bs2kupper right���bs2a"���`a,���`a ���`cpad���aoa=���bmia0���`a,���`a ���`gframeon���aoa=���bkceFalse���`a)���`a
���`d    ���`bax���aoa.���`jadd_artist���`a(���`cbox���`a)���`a
���`a
���`a
���akcdef���`a ���bnfldraw_ellipse���`a(���`bax���`a)���`a:���`a
���`d    ���bsdxD"""Draw an ellipse of width=0.1, height=0.15 in data coordinates."""���`a
���`d    ���`jaux_tr_box���`a ���aoa=���`a ���`oAuxTransformBox���`a(���`bax���aoa.���`itransData���`a)���`a
���`d    ���`jaux_tr_box���aoa.���`jadd_artist���`a(���`gEllipse���`a(���`a(���bmia0���`a,���`a ���bmia0���`a)���`a,���`a ���`ewidth���aoa=���bmfc0.1���`a,���`a ���`fheight���aoa=���bmfd0.15���`a)���`a)���`a
���`d    ���`cbox���`a ���aoa=���`a ���`qAnchoredOffsetbox���`a(���`echild���aoa=���`jaux_tr_box���`a,���`a ���`cloc���aoa=���bs2a"���bs2jlower left���bs2a"���`a,���`a ���`gframeon���aoa=���bkcdTrue���`a)���`a
���`d    ���`bax���aoa.���`jadd_artist���`a(���`cbox���`a)���`a
���`a
���`a
���akeclass���`a ���bncoAnchoredSizeBar���`a(���`qAnchoredOffsetbox���`a)���`a:���`a
���`d    ���akcdef���`a ���bfmh__init__���`a(���bbpdself���`a,���`a ���`itransform���`a,���`a ���`dsize���`a,���`a ���`elabel���`a,���`a ���`cloc���`a,���`a
���`q                 ���`cpad���aoa=���bmfc0.1���`a,���`a ���`iborderpad���aoa=���bmfc0.1���`a,���`a ���`csep���aoa=���bmia2���`a,���`a ���`dprop���aoa=���bkcdNone���`a,���`a ���`gframeon���aoa=���bkcdTrue���`a)���`a:���`a
���`h        ���bsdx�"""
        Draw a horizontal bar with the size in data coordinate of the given
        axes. A label will be drawn underneath (center-aligned).

        pad, borderpad in fraction of the legend font size (or prop)
        sep in points.
        """���`a
���`h        ���bbpdself���aoa.���`hsize_bar���`a ���aoa=���`a ���`oAuxTransformBox���`a(���`itransform���`a)���`a
���`h        ���bbpdself���aoa.���`hsize_bar���aoa.���`jadd_artist���`a(���`fLine2D���`a(���`a[���bmia0���`a,���`a ���`dsize���`a]���`a,���`a ���`a[���bmia0���`a,���`a ���bmia0���`a]���`a,���`a ���`ecolor���aoa=���bs2a"���bs2eblack���bs2a"���`a)���`a)���`a
���`h        ���bbpdself���aoa.���`itxt_label���`a ���aoa=���`a ���`hTextArea���`a(���`elabel���`a)���`a
���`h        ���bbpdself���aoa.���`d_box���`a ���aoa=���`a ���`gVPacker���`a(���`hchildren���aoa=���`a[���bbpdself���aoa.���`hsize_bar���`a,���`a ���bbpdself���aoa.���`itxt_label���`a]���`a,���`a
���`x                            ���`ealign���aoa=���bs2a"���bs2fcenter���bs2a"���`a,���`a
���`x                            ���`cpad���aoa=���bmia0���`a,���`a ���`csep���aoa=���`csep���`a)���`a
���`h        ���bnbesuper���`a(���`a)���aoa.���bfmh__init__���`a(���`cloc���`a,���`a ���`cpad���aoa=���`cpad���`a,���`a ���`iborderpad���aoa=���`iborderpad���`a,���`a
���`x                         ���`echild���aoa=���bbpdself���aoa.���`d_box���`a,���`a ���`dprop���aoa=���`dprop���`a,���`a ���`gframeon���aoa=���`gframeon���`a)���`a
���`a
���`a
���akcdef���`a ���bnfldraw_sizebar���`a(���`bax���`a)���`a:���`a
���`d    ���bsdxp"""
    Draw a horizontal bar with length of 0.1 in data coordinates,
    with a fixed label underneath.
    """���`a
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
���`bax���aoa.���`jset_aspect���`a(���bmia1���`a)���`a
���`a
���`idraw_text���`a(���`bax���`a)���`a
���`ldraw_circles���`a(���`bax���`a)���`a
���`ldraw_ellipse���`a(���`bax���`a)���`a
���`ldraw_sizebar���`a(���`bax���`a)���`a
���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
`dNone�