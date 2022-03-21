��������q���bsdy�"""
=================================
Box plots with custom fill colors
=================================

This plot illustrates how to create two types of box plots
(rectangular and notched), and how to fill them with custom
colors by accessing the properties of the artists of the
box plots. Additionally, the ``labels`` parameter is used to
provide x-tick labels for each sample.

A good general reference on boxplots and their history can be found
here: http://vita.had.co.nz/papers/boxplots.pdf
"""���`a
���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���`a
���bc1r# Random test data���`a
���`bnp���aoa.���`frandom���aoa.���`dseed���`a(���bmih19680801���`a)���`a
���`hall_data���`a ���aoa=���`a ���`a[���`bnp���aoa.���`frandom���aoa.���`fnormal���`a(���bmia0���`a,���`a ���`cstd���`a,���`a ���`dsize���aoa=���bmic100���`a)���`a ���akcfor���`a ���`cstd���`a ���bowbin���`a ���bnberange���`a(���bmia1���`a,���`a ���bmia4���`a)���`a]���`a
���`flabels���`a ���aoa=���`a ���`a[���bs1a'���bs1bx1���bs1a'���`a,���`a ���bs1a'���bs1bx2���bs1a'���`a,���`a ���bs1a'���bs1bx3���bs1a'���`a]���`a
���`a
���`cfig���`a,���`a ���`a(���`cax1���`a,���`a ���`cax2���`a)���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`enrows���aoa=���bmia1���`a,���`a ���`encols���aoa=���bmia2���`a,���`a ���`gfigsize���aoa=���`a(���bmia9���`a,���`a ���bmia4���`a)���`a)���`a
���`a
���bc1v# rectangular box plot���`a
���`fbplot1���`a ���aoa=���`a ���`cax1���aoa.���`gboxplot���`a(���`hall_data���`a,���`a
���`u                     ���`dvert���aoa=���bkcdTrue���`a,���`b  ���bc1x# vertical box alignment���`a
���`u                     ���`lpatch_artist���aoa=���bkcdTrue���`a,���`b  ���bc1q# fill with color���`a
���`u                     ���`flabels���aoa=���`flabels���`a)���`b  ���bc1x# will be used to label x-ticks���`a
���`cax1���aoa.���`iset_title���`a(���bs1a'���bs1tRectangular box plot���bs1a'���`a)���`a
���`a
���bc1v# notch shape box plot���`a
���`fbplot2���`a ���aoa=���`a ���`cax2���aoa.���`gboxplot���`a(���`hall_data���`a,���`a
���`u                     ���`enotch���aoa=���bkcdTrue���`a,���`b  ���bc1m# notch shape���`a
���`u                     ���`dvert���aoa=���bkcdTrue���`a,���`b  ���bc1x# vertical box alignment���`a
���`u                     ���`lpatch_artist���aoa=���bkcdTrue���`a,���`b  ���bc1q# fill with color���`a
���`u                     ���`flabels���aoa=���`flabels���`a)���`b  ���bc1x# will be used to label x-ticks���`a
���`cax2���aoa.���`iset_title���`a(���bs1a'���bs1pNotched box plot���bs1a'���`a)���`a
���`a
���bc1r# fill with colors���`a
���`fcolors���`a ���aoa=���`a ���`a[���bs1a'���bs1dpink���bs1a'���`a,���`a ���bs1a'���bs1ilightblue���bs1a'���`a,���`a ���bs1a'���bs1jlightgreen���bs1a'���`a]���`a
���akcfor���`a ���`ebplot���`a ���bowbin���`a ���`a(���`fbplot1���`a,���`a ���`fbplot2���`a)���`a:���`a
���`d    ���akcfor���`a ���`epatch���`a,���`a ���`ecolor���`a ���bowbin���`a ���bnbczip���`a(���`ebplot���`a[���bs1a'���bs1eboxes���bs1a'���`a]���`a,���`a ���`fcolors���`a)���`a:���`a
���`h        ���`epatch���aoa.���`mset_facecolor���`a(���`ecolor���`a)���`a
���`a
���bc1x# adding horizontal grid lines���`a
���akcfor���`a ���`bax���`a ���bowbin���`a ���`a[���`cax1���`a,���`a ���`cax2���`a]���`a:���`a
���`d    ���`bax���aoa.���`eyaxis���aoa.���`dgrid���`a(���bkcdTrue���`a)���`a
���`d    ���`bax���aoa.���`jset_xlabel���`a(���bs1a'���bs1vThree separate samples���bs1a'���`a)���`a
���`d    ���`bax���aoa.���`jset_ylabel���`a(���bs1a'���bs1oObserved values���bs1a'���`a)���`a
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
���bc1xC#    - `matplotlib.axes.Axes.boxplot` / `matplotlib.pyplot.boxplot`���`a
`dNone�