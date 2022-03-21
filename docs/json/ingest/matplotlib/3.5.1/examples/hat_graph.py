��������5���bsdx�"""
=========
Hat graph
=========
This example shows how to create a `hat graph`_ and how to annotate it with
labels.

.. _hat graph: https://doi.org/10.1186/s41235-019-0182-3
"""���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���`a
���`a
���akcdef���`a ���bnfihat_graph���`a(���`bax���`a,���`a ���`gxlabels���`a,���`a ���`fvalues���`a,���`a ���`lgroup_labels���`a)���`a:���`a
���`d    ���bsdy�"""
    Create a hat graph.

    Parameters
    ----------
    ax : matplotlib.axes.Axes
        The Axes to plot into.
    xlabels : list of str
        The category names to be displayed on the x-axis.
    values : (M, N) array-like
        The data values.
        Rows are the groups (len(group_labels) == M).
        Columns are the categories (len(xlabels) == N).
    group_labels : list of str
        The group labels displayed in the legend.
    """���`a
���`a
���`d    ���akcdef���`a ���bnfjlabel_bars���`a(���`gheights���`a,���`a ���`erects���`a)���`a:���`a
���`h        ���bsdx-"""Attach a text label on top of each bar."""���`a
���`h        ���akcfor���`a ���`fheight���`a,���`a ���`drect���`a ���bowbin���`a ���bnbczip���`a(���`gheights���`a,���`a ���`erects���`a)���`a:���`a
���`l            ���`bax���aoa.���`hannotate���`a(���bsaaf���bs1a'���bsia{���`fheight���bsia}���bs1a'���`a,���`a
���`x                        ���`bxy���aoa=���`a(���`drect���aoa.���`eget_x���`a(���`a)���`a ���aoa+���`a ���`drect���aoa.���`iget_width���`a(���`a)���`a ���aoa/���`a ���bmia2���`a,���`a ���`fheight���`a)���`a,���`a
���`x                        ���`fxytext���aoa=���`a(���bmia0���`a,���`a ���bmia4���`a)���`a,���`b  ���bc1x# 4 points vertical offset.���`a
���`x                        ���`jtextcoords���aoa=���bs1a'���bs1moffset points���bs1a'���`a,���`a
���`x                        ���`bha���aoa=���bs1a'���bs1fcenter���bs1a'���`a,���`a ���`bva���aoa=���bs1a'���bs1fbottom���bs1a'���`a)���`a
���`a
���`d    ���`fvalues���`a ���aoa=���`a ���`bnp���aoa.���`gasarray���`a(���`fvalues���`a)���`a
���`d    ���`ax���`a ���aoa=���`a ���`bnp���aoa.���`farange���`a(���`fvalues���aoa.���`eshape���`a[���bmia1���`a]���`a)���`a
���`d    ���`bax���aoa.���`jset_xticks���`a(���`ax���`a,���`a ���`flabels���aoa=���`gxlabels���`a)���`a
���`d    ���`gspacing���`a ���aoa=���`a ���bmfc0.3���`b  ���bc1x# spacing between hat groups���`a
���`d    ���`ewidth���`a ���aoa=���`a ���`a(���bmia1���`a ���aoa-���`a ���`gspacing���`a)���`a ���aoa/���`a ���`fvalues���aoa.���`eshape���`a[���bmia0���`a]���`a
���`d    ���`hheights0���`a ���aoa=���`a ���`fvalues���`a[���bmia0���`a]���`a
���`d    ���akcfor���`a ���`ai���`a,���`a ���`a(���`gheights���`a,���`a ���`kgroup_label���`a)���`a ���bowbin���`a ���bnbienumerate���`a(���bnbczip���`a(���`fvalues���`a,���`a ���`lgroup_labels���`a)���`a)���`a:���`a
���`h        ���`estyle���`a ���aoa=���`a ���`a{���bs1a'���bs1dfill���bs1a'���`a:���`a ���bkceFalse���`a}���`a ���akbif���`a ���`ai���`a ���aob==���`a ���bmia0���`a ���akdelse���`a ���`a{���bs1a'���bs1iedgecolor���bs1a'���`a:���`a ���bs1a'���bs1eblack���bs1a'���`a}���`a
���`h        ���`erects���`a ���aoa=���`a ���`bax���aoa.���`cbar���`a(���`ax���`a ���aoa-���`a ���`gspacing���aoa/���bmia2���`a ���aoa+���`a ���`ai���`a ���aoa*���`a ���`ewidth���`a,���`a ���`gheights���`a ���aoa-���`a ���`hheights0���`a,���`a
���`w                       ���`ewidth���`a,���`a ���`fbottom���aoa=���`hheights0���`a,���`a ���`elabel���aoa=���`kgroup_label���`a,���`a ���aoa*���aoa*���`estyle���`a)���`a
���`h        ���`jlabel_bars���`a(���`gheights���`a,���`a ���`erects���`a)���`a
���`a
���`a
���bc1x8# initialise labels and a numpy array make sure you have���`a
���bc1x-# N labels of N number of values in the array���`a
���`gxlabels���`a ���aoa=���`a ���`a[���bs1a'���bs1aI���bs1a'���`a,���`a ���bs1a'���bs1bII���bs1a'���`a,���`a ���bs1a'���bs1cIII���bs1a'���`a,���`a ���bs1a'���bs1bIV���bs1a'���`a,���`a ���bs1a'���bs1aV���bs1a'���`a]���`a
���`gplayerA���`a ���aoa=���`a ���`bnp���aoa.���`earray���`a(���`a[���bmia5���`a,���`a ���bmib15���`a,���`a ���bmib22���`a,���`a ���bmib20���`a,���`a ���bmib25���`a]���`a)���`a
���`gplayerB���`a ���aoa=���`a ���`bnp���aoa.���`earray���`a(���`a[���bmib25���`a,���`a ���bmib32���`a,���`a ���bmib34���`a,���`a ���bmib30���`a,���`a ���bmib27���`a]���`a)���`a
���`a
���`cfig���`a,���`a ���`bax���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`a)���`a
���`ihat_graph���`a(���`bax���`a,���`a ���`gxlabels���`a,���`a ���`a[���`gplayerA���`a,���`a ���`gplayerB���`a]���`a,���`a ���`a[���bs1a'���bs1hPlayer A���bs1a'���`a,���`a ���bs1a'���bs1hPlayer B���bs1a'���`a]���`a)���`a
���`a
���bc1xE# Add some text for labels, title and custom x-axis tick labels, etc.���`a
���`bax���aoa.���`jset_xlabel���`a(���bs1a'���bs1eGames���bs1a'���`a)���`a
���`bax���aoa.���`jset_ylabel���`a(���bs1a'���bs1eScore���bs1a'���`a)���`a
���`bax���aoa.���`hset_ylim���`a(���bmia0���`a,���`a ���bmib60���`a)���`a
���`bax���aoa.���`iset_title���`a(���bs1a'���bs1x$Scores by number of game and players���bs1a'���`a)���`a
���`bax���aoa.���`flegend���`a(���`a)���`a
���`a
���`cfig���aoa.���`ltight_layout���`a(���`a)���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
���bc1xM#############################################################################���`a
���bc1a#���`a
���bc1x# .. admonition:: References���`a
���bc1a#���`a
���bc1xN#    The use of the following functions, methods, classes and modules is shown���`a
���bc1u#    in this example:���`a
���bc1a#���`a
���bc1x;#    - `matplotlib.axes.Axes.bar` / `matplotlib.pyplot.bar`���`a
���bc1xE#    - `matplotlib.axes.Axes.annotate` / `matplotlib.pyplot.annotate`���`a
`dNone�