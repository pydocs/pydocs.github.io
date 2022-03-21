�����������bsdyg"""
================================
Reference for Matplotlib artists
================================

This example displays several of Matplotlib's graphics primitives (artists)
drawn using matplotlib API. A full list of artists and the documentation is
available at :ref:`the artist API <artist-api>`.

Copyright (c) 2010, Bartosz Telenczuk
BSD License
"""���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnndpath���`a ���akbas���`a ���bnnempath���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnelines���`a ���akbas���`a ���bnnfmlines���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnngpatches���`a ���akbas���`a ���bnnhmpatches���`a
���bkndfrom���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnkcollections���`a ���bknfimport���`a ���`oPatchCollection���`a
���`a
���`a
���akcdef���`a ���bnfelabel���`a(���`bxy���`a,���`a ���`dtext���`a)���`a:���`a
���`d    ���`ay���`a ���aoa=���`a ���`bxy���`a[���bmia1���`a]���`a ���aoa-���`a ���bmfd0.15���`b  ���bc1x7# shift y-value for label so that it's below the artist���`a
���`d    ���`cplt���aoa.���`dtext���`a(���`bxy���`a[���bmia0���`a]���`a,���`a ���`ay���`a,���`a ���`dtext���`a,���`a ���`bha���aoa=���bs2a"���bs2fcenter���bs2a"���`a,���`a ���`ffamily���aoa=���bs1a'���bs1jsans-serif���bs1a'���`a,���`a ���`dsize���aoa=���bmib14���`a)���`a
���`a
���`a
���`cfig���`a,���`a ���`bax���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`a)���`a
���bc1x%# create 3x3 grid to plot the artists���`a
���`dgrid���`a ���aoa=���`a ���`bnp���aoa.���`emgrid���`a[���bmfc0.2���`a:���bmfc0.8���`a:���bmia3���`aj���`a,���`a ���bmfc0.2���`a:���bmfc0.8���`a:���bmia3���`aj���`a]���aoa.���`greshape���`a(���bmia2���`a,���`a ���aoa-���bmia1���`a)���aoa.���`aT���`a
���`a
���`gpatches���`a ���aoa=���`a ���`a[���`a]���`a
���`a
���bc1n# add a circle���`a
���`fcircle���`a ���aoa=���`a ���`hmpatches���aoa.���`fCircle���`a(���`dgrid���`a[���bmia0���`a]���`a,���`a ���bmfc0.1���`a,���`a ���`bec���aoa=���bs2a"���bs2dnone���bs2a"���`a)���`a
���`gpatches���aoa.���`fappend���`a(���`fcircle���`a)���`a
���`elabel���`a(���`dgrid���`a[���bmia0���`a]���`a,���`a ���bs2a"���bs2fCircle���bs2a"���`a)���`a
���`a
���bc1q# add a rectangle���`a
���`drect���`a ���aoa=���`a ���`hmpatches���aoa.���`iRectangle���`a(���`dgrid���`a[���bmia1���`a]���`a ���aoa-���`a ���`a[���bmfe0.025���`a,���`a ���bmfd0.05���`a]���`a,���`a ���bmfd0.05���`a,���`a ���bmfc0.1���`a,���`a ���`bec���aoa=���bs2a"���bs2dnone���bs2a"���`a)���`a
���`gpatches���aoa.���`fappend���`a(���`drect���`a)���`a
���`elabel���`a(���`dgrid���`a[���bmia1���`a]���`a,���`a ���bs2a"���bs2iRectangle���bs2a"���`a)���`a
���`a
���bc1m# add a wedge���`a
���`ewedge���`a ���aoa=���`a ���`hmpatches���aoa.���`eWedge���`a(���`dgrid���`a[���bmia2���`a]���`a,���`a ���bmfc0.1���`a,���`a ���bmib30���`a,���`a ���bmic270���`a,���`a ���`bec���aoa=���bs2a"���bs2dnone���bs2a"���`a)���`a
���`gpatches���aoa.���`fappend���`a(���`ewedge���`a)���`a
���`elabel���`a(���`dgrid���`a[���bmia2���`a]���`a,���`a ���bs2a"���bs2eWedge���bs2a"���`a)���`a
���`a
���bc1o# add a Polygon���`a
���`gpolygon���`a ���aoa=���`a ���`hmpatches���aoa.���`nRegularPolygon���`a(���`dgrid���`a[���bmia3���`a]���`a,���`a ���bmia5���`a,���`a ���bmfc0.1���`a)���`a
���`gpatches���aoa.���`fappend���`a(���`gpolygon���`a)���`a
���`elabel���`a(���`dgrid���`a[���bmia3���`a]���`a,���`a ���bs2a"���bs2gPolygon���bs2a"���`a)���`a
���`a
���bc1p# add an ellipse���`a
���`gellipse���`a ���aoa=���`a ���`hmpatches���aoa.���`gEllipse���`a(���`dgrid���`a[���bmia4���`a]���`a,���`a ���bmfc0.2���`a,���`a ���bmfc0.1���`a)���`a
���`gpatches���aoa.���`fappend���`a(���`gellipse���`a)���`a
���`elabel���`a(���`dgrid���`a[���bmia4���`a]���`a,���`a ���bs2a"���bs2gEllipse���bs2a"���`a)���`a
���`a
���bc1n# add an arrow���`a
���`earrow���`a ���aoa=���`a ���`hmpatches���aoa.���`eArrow���`a(���`dgrid���`a[���bmia5���`a,���`a ���bmia0���`a]���`a ���aoa-���`a ���bmfd0.05���`a,���`a ���`dgrid���`a[���bmia5���`a,���`a ���bmia1���`a]���`a ���aoa-���`a ���bmfd0.05���`a,���`a ���bmfc0.1���`a,���`a ���bmfc0.1���`a,���`a
���`w                       ���`ewidth���aoa=���bmfc0.1���`a)���`a
���`gpatches���aoa.���`fappend���`a(���`earrow���`a)���`a
���`elabel���`a(���`dgrid���`a[���bmia5���`a]���`a,���`a ���bs2a"���bs2eArrow���bs2a"���`a)���`a
���`a
���bc1r# add a path patch���`a
���`dPath���`a ���aoa=���`a ���`empath���aoa.���`dPath���`a
���`ipath_data���`a ���aoa=���`a ���`a[���`a
���`d    ���`a(���`dPath���aoa.���`fMOVETO���`a,���`a ���`a[���bmfe0.018���`a,���`a ���aoa-���bmfd0.11���`a]���`a)���`a,���`a
���`d    ���`a(���`dPath���aoa.���`fCURVE4���`a,���`a ���`a[���aoa-���bmfe0.031���`a,���`a ���aoa-���bmfe0.051���`a]���`a)���`a,���`a
���`d    ���`a(���`dPath���aoa.���`fCURVE4���`a,���`a ���`a[���aoa-���bmfe0.115���`a,���`a ���bmfe0.073���`a]���`a)���`a,���`a
���`d    ���`a(���`dPath���aoa.���`fCURVE4���`a,���`a ���`a[���aoa-���bmfd0.03���`a,���`a ���bmfe0.073���`a]���`a)���`a,���`a
���`d    ���`a(���`dPath���aoa.���`fLINETO���`a,���`a ���`a[���aoa-���bmfe0.011���`a,���`a ���bmfe0.039���`a]���`a)���`a,���`a
���`d    ���`a(���`dPath���aoa.���`fCURVE4���`a,���`a ���`a[���bmfe0.043���`a,���`a ���bmfe0.121���`a]���`a)���`a,���`a
���`d    ���`a(���`dPath���aoa.���`fCURVE4���`a,���`a ���`a[���bmfe0.075���`a,���`a ���aoa-���bmfe0.005���`a]���`a)���`a,���`a
���`d    ���`a(���`dPath���aoa.���`fCURVE4���`a,���`a ���`a[���bmfe0.035���`a,���`a ���aoa-���bmfe0.027���`a]���`a)���`a,���`a
���`d    ���`a(���`dPath���aoa.���`iCLOSEPOLY���`a,���`a ���`a[���bmfe0.018���`a,���`a ���aoa-���bmfd0.11���`a]���`a)���`a]���`a
���`ecodes���`a,���`a ���`everts���`a ���aoa=���`a ���bnbczip���`a(���aoa*���`ipath_data���`a)���`a
���`dpath���`a ���aoa=���`a ���`empath���aoa.���`dPath���`a(���`everts���`a ���aoa+���`a ���`dgrid���`a[���bmia6���`a]���`a,���`a ���`ecodes���`a)���`a
���`epatch���`a ���aoa=���`a ���`hmpatches���aoa.���`iPathPatch���`a(���`dpath���`a)���`a
���`gpatches���aoa.���`fappend���`a(���`epatch���`a)���`a
���`elabel���`a(���`dgrid���`a[���bmia6���`a]���`a,���`a ���bs2a"���bs2iPathPatch���bs2a"���`a)���`a
���`a
���bc1q# add a fancy box���`a
���`hfancybox���`a ���aoa=���`a ���`hmpatches���aoa.���`nFancyBboxPatch���`a(���`a
���`d    ���`dgrid���`a[���bmia7���`a]���`a ���aoa-���`a ���`a[���bmfe0.025���`a,���`a ���bmfd0.05���`a]���`a,���`a ���bmfd0.05���`a,���`a ���bmfc0.1���`a,���`a
���`d    ���`hboxstyle���aoa=���`hmpatches���aoa.���`hBoxStyle���`a(���bs2a"���bs2eRound���bs2a"���`a,���`a ���`cpad���aoa=���bmfd0.02���`a)���`a)���`a
���`gpatches���aoa.���`fappend���`a(���`hfancybox���`a)���`a
���`elabel���`a(���`dgrid���`a[���bmia7���`a]���`a,���`a ���bs2a"���bs2nFancyBboxPatch���bs2a"���`a)���`a
���`a
���bc1l# add a line���`a
���`ax���`a,���`a ���`ay���`a ���aoa=���`a ���`a(���`a[���aoa-���bmfd0.06���`a,���`a ���bmfc0.0���`a,���`a ���bmfc0.1���`a]���`a,���`a ���`a[���bmfd0.05���`a,���`a ���aoa-���bmfd0.05���`a,���`a ���bmfd0.05���`a]���`a)���`a
���`dline���`a ���aoa=���`a ���`fmlines���aoa.���`fLine2D���`a(���`ax���`a ���aoa+���`a ���`dgrid���`a[���bmia8���`a,���`a ���bmia0���`a]���`a,���`a ���`ay���`a ���aoa+���`a ���`dgrid���`a[���bmia8���`a,���`a ���bmia1���`a]���`a,���`a ���`blw���aoa=���bmfb5.���`a,���`a ���`ealpha���aoa=���bmfc0.3���`a)���`a
���`elabel���`a(���`dgrid���`a[���bmia8���`a]���`a,���`a ���bs2a"���bs2fLine2D���bs2a"���`a)���`a
���`a
���`fcolors���`a ���aoa=���`a ���`bnp���aoa.���`hlinspace���`a(���bmia0���`a,���`a ���bmia1���`a,���`a ���bnbclen���`a(���`gpatches���`a)���`a)���`a
���`jcollection���`a ���aoa=���`a ���`oPatchCollection���`a(���`gpatches���`a,���`a ���`dcmap���aoa=���`cplt���aoa.���`bcm���aoa.���`chsv���`a,���`a ���`ealpha���aoa=���bmfc0.3���`a)���`a
���`jcollection���aoa.���`iset_array���`a(���`fcolors���`a)���`a
���`bax���aoa.���`nadd_collection���`a(���`jcollection���`a)���`a
���`bax���aoa.���`hadd_line���`a(���`dline���`a)���`a
���`a
���`cplt���aoa.���`daxis���`a(���bs1a'���bs1eequal���bs1a'���`a)���`a
���`cplt���aoa.���`daxis���`a(���bs1a'���bs1coff���bs1a'���`a)���`a
���`cplt���aoa.���`ltight_layout���`a(���`a)���`a
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
���bc1x#    - `matplotlib.lines`���`a
���bc1x #    - `matplotlib.lines.Line2D`���`a
���bc1x#    - `matplotlib.patches`���`a
���bc1x"#    - `matplotlib.patches.Circle`���`a
���bc1x##    - `matplotlib.patches.Ellipse`���`a
���bc1x!#    - `matplotlib.patches.Wedge`���`a
���bc1x%#    - `matplotlib.patches.Rectangle`���`a
���bc1x!#    - `matplotlib.patches.Arrow`���`a
���bc1x%#    - `matplotlib.patches.PathPatch`���`a
���bc1x*#    - `matplotlib.patches.FancyBboxPatch`���`a
���bc1x*#    - `matplotlib.patches.RegularPolygon`���`a
���bc1x#    - `matplotlib.collections`���`a
���bc1x/#    - `matplotlib.collections.PatchCollection`���`a
���bc1x/#    - `matplotlib.cm.ScalarMappable.set_array`���`a
���bc1x,#    - `matplotlib.axes.Axes.add_collection`���`a
���bc1x&#    - `matplotlib.axes.Axes.add_line`���`a
`dNone�