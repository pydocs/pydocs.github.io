��������f���bsdxx"""
================
Polygon Selector
================

Shows how one can select indices of a polygon interactively.
"""���`a
���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���`a
���bkndfrom���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnngwidgets���`a ���bknfimport���`a ���`oPolygonSelector���`a
���bkndfrom���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnndpath���`a ���bknfimport���`a ���`dPath���`a
���`a
���`a
���akeclass���`a ���bnctSelectFromCollection���`a:���`a
���`d    ���bsdy0"""
    Select indices from a matplotlib collection using `PolygonSelector`.

    Selected indices are saved in the `ind` attribute. This tool fades out the
    points that are not part of the selection (i.e., reduces their alpha
    values). If your collection has alpha < 1, this tool will permanently
    alter the alpha values.

    Note that this tool selects collection objects based on their *origins*
    (i.e., `offsets`).

    Parameters
    ----------
    ax : `~matplotlib.axes.Axes`
        Axes to interact with.
    collection : `matplotlib.collections.Collection` subclass
        Collection you want to select from.
    alpha_other : 0 <= float <= 1
        To highlight a selection, this tool sets all selected points to an
        alpha value of 1 and non-selected points to *alpha_other*.
    """���`a
���`a
���`d    ���akcdef���`a ���bfmh__init__���`a(���bbpdself���`a,���`a ���`bax���`a,���`a ���`jcollection���`a,���`a ���`kalpha_other���aoa=���bmfc0.3���`a)���`a:���`a
���`h        ���bbpdself���aoa.���`fcanvas���`a ���aoa=���`a ���`bax���aoa.���`ffigure���aoa.���`fcanvas���`a
���`h        ���bbpdself���aoa.���`jcollection���`a ���aoa=���`a ���`jcollection���`a
���`h        ���bbpdself���aoa.���`kalpha_other���`a ���aoa=���`a ���`kalpha_other���`a
���`a
���`h        ���bbpdself���aoa.���`cxys���`a ���aoa=���`a ���`jcollection���aoa.���`kget_offsets���`a(���`a)���`a
���`h        ���bbpdself���aoa.���`dNpts���`a ���aoa=���`a ���bnbclen���`a(���bbpdself���aoa.���`cxys���`a)���`a
���`a
���`h        ���bc1x5# Ensure that we have separate colors for each object���`a
���`h        ���bbpdself���aoa.���`bfc���`a ���aoa=���`a ���`jcollection���aoa.���`nget_facecolors���`a(���`a)���`a
���`h        ���akbif���`a ���bnbclen���`a(���bbpdself���aoa.���`bfc���`a)���`a ���aob==���`a ���bmia0���`a:���`a
���`l            ���akeraise���`a ���bnejValueError���`a(���bs1a'���bs1x Collection must have a facecolor���bs1a'���`a)���`a
���`h        ���akdelif���`a ���bnbclen���`a(���bbpdself���aoa.���`bfc���`a)���`a ���aob==���`a ���bmia1���`a:���`a
���`l            ���bbpdself���aoa.���`bfc���`a ���aoa=���`a ���`bnp���aoa.���`dtile���`a(���bbpdself���aoa.���`bfc���`a,���`a ���`a(���bbpdself���aoa.���`dNpts���`a,���`a ���bmia1���`a)���`a)���`a
���`a
���`h        ���bbpdself���aoa.���`dpoly���`a ���aoa=���`a ���`oPolygonSelector���`a(���`bax���`a,���`a ���bbpdself���aoa.���`honselect���`a)���`a
���`h        ���bbpdself���aoa.���`cind���`a ���aoa=���`a ���`a[���`a]���`a
���`a
���`d    ���akcdef���`a ���bnfhonselect���`a(���bbpdself���`a,���`a ���`everts���`a)���`a:���`a
���`h        ���`dpath���`a ���aoa=���`a ���`dPath���`a(���`everts���`a)���`a
���`h        ���bbpdself���aoa.���`cind���`a ���aoa=���`a ���`bnp���aoa.���`gnonzero���`a(���`dpath���aoa.���`ocontains_points���`a(���bbpdself���aoa.���`cxys���`a)���`a)���`a[���bmia0���`a]���`a
���`h        ���bbpdself���aoa.���`bfc���`a[���`a:���`a,���`a ���aoa-���bmia1���`a]���`a ���aoa=���`a ���bbpdself���aoa.���`kalpha_other���`a
���`h        ���bbpdself���aoa.���`bfc���`a[���bbpdself���aoa.���`cind���`a,���`a ���aoa-���bmia1���`a]���`a ���aoa=���`a ���bmia1���`a
���`h        ���bbpdself���aoa.���`jcollection���aoa.���`nset_facecolors���`a(���bbpdself���aoa.���`bfc���`a)���`a
���`h        ���bbpdself���aoa.���`fcanvas���aoa.���`idraw_idle���`a(���`a)���`a
���`a
���`d    ���akcdef���`a ���bnfjdisconnect���`a(���bbpdself���`a)���`a:���`a
���`h        ���bbpdself���aoa.���`dpoly���aoa.���`qdisconnect_events���`a(���`a)���`a
���`h        ���bbpdself���aoa.���`bfc���`a[���`a:���`a,���`a ���aoa-���bmia1���`a]���`a ���aoa=���`a ���bmia1���`a
���`h        ���bbpdself���aoa.���`jcollection���aoa.���`nset_facecolors���`a(���bbpdself���aoa.���`bfc���`a)���`a
���`h        ���bbpdself���aoa.���`fcanvas���aoa.���`idraw_idle���`a(���`a)���`a
���`a
���`a
���akbif���`a ���bvmh__name__���`a ���aob==���`a ���bs1a'���bs1h__main__���bs1a'���`a:���`a
���`d    ���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���`a
���`d    ���`cfig���`a,���`a ���`bax���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`a)���`a
���`d    ���`igrid_size���`a ���aoa=���`a ���bmia5���`a
���`d    ���`fgrid_x���`a ���aoa=���`a ���`bnp���aoa.���`dtile���`a(���`bnp���aoa.���`farange���`a(���`igrid_size���`a)���`a,���`a ���`igrid_size���`a)���`a
���`d    ���`fgrid_y���`a ���aoa=���`a ���`bnp���aoa.���`frepeat���`a(���`bnp���aoa.���`farange���`a(���`igrid_size���`a)���`a,���`a ���`igrid_size���`a)���`a
���`d    ���`cpts���`a ���aoa=���`a ���`bax���aoa.���`gscatter���`a(���`fgrid_x���`a,���`a ���`fgrid_y���`a)���`a
���`a
���`d    ���`hselector���`a ���aoa=���`a ���`tSelectFromCollection���`a(���`bax���`a,���`a ���`cpts���`a)���`a
���`a
���`d    ���bnbeprint���`a(���bs2a"���bs2x?Select points in the figure by enclosing them within a polygon.���bs2a"���`a)���`a
���`d    ���bnbeprint���`a(���bs2a"���bs2jPress the ���bs2a'���bs2cesc���bs2a'���bs2x key to start a new polygon.���bs2a"���`a)���`a
���`d    ���bnbeprint���`a(���bs2a"���bs2pTry holding the ���bs2a'���bs2eshift���bs2a'���bs2x! key to move all of the vertices.���bs2a"���`a)���`a
���`d    ���bnbeprint���`a(���bs2a"���bs2pTry holding the ���bs2a'���bs2dctrl���bs2a'���bs2x key to move a single vertex.���bs2a"���`a)���`a
���`a
���`d    ���`cplt���aoa.���`dshow���`a(���`a)���`a
���`a
���`d    ���`hselector���aoa.���`jdisconnect���`a(���`a)���`a
���`a
���`d    ���bc1xE# After figure is closed print the coordinates of the selected points���`a
���`d    ���bnbeprint���`a(���bs1a'���bseb\n���bs1pSelected points:���bs1a'���`a)���`a
���`d    ���bnbeprint���`a(���`hselector���aoa.���`cxys���`a[���`hselector���aoa.���`cind���`a]���`a)���`a
���`a
���bc1xM#############################################################################���`a
���bc1a#���`a
���bc1x# .. admonition:: References���`a
���bc1a#���`a
���bc1xN#    The use of the following functions, methods, classes and modules is shown���`a
���bc1u#    in this example:���`a
���bc1a#���`a
���bc1x+#    - `matplotlib.widgets.PolygonSelector`���`a
���bc1x#    - `matplotlib.path.Path`���`a
`dNone�