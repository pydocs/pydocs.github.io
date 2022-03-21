�����������bsdy�"""
===================================
Box plot vs. violin plot comparison
===================================

Note that although violin plots are closely related to Tukey's (1977)
box plots, they add useful information such as the distribution of the
sample data (density trace).

By default, box plots show data points outside 1.5 * the inter-quartile
range as outliers above or below the whiskers whereas violin plots show
the whole range of the data.

A good general reference on boxplots and their history can be found
here: http://vita.had.co.nz/papers/boxplots.pdf

Violin plots require matplotlib >= 1.4.

For more information on violin plots, the scikit-learn docs have a great
section: https://scikit-learn.org/stable/modules/density.html
"""���`a
���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���`a
���`cfig���`a,���`a ���`caxs���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`enrows���aoa=���bmia1���`a,���`a ���`encols���aoa=���bmia2���`a,���`a ���`gfigsize���aoa=���`a(���bmia9���`a,���`a ���bmia4���`a)���`a)���`a
���`a
���bc1x)# Fixing random state for reproducibility���`a
���`bnp���aoa.���`frandom���aoa.���`dseed���`a(���bmih19680801���`a)���`a
���`a
���`a
���bc1x # generate some random test data���`a
���`hall_data���`a ���aoa=���`a ���`a[���`bnp���aoa.���`frandom���aoa.���`fnormal���`a(���bmia0���`a,���`a ���`cstd���`a,���`a ���bmic100���`a)���`a ���akcfor���`a ���`cstd���`a ���bowbin���`a ���bnberange���`a(���bmia6���`a,���`a ���bmib10���`a)���`a]���`a
���`a
���bc1r# plot violin plot���`a
���`caxs���`a[���bmia0���`a]���aoa.���`jviolinplot���`a(���`hall_data���`a,���`a
���`r                  ���`ishowmeans���aoa=���bkceFalse���`a,���`a
���`r                  ���`kshowmedians���aoa=���bkcdTrue���`a)���`a
���`caxs���`a[���bmia0���`a]���aoa.���`iset_title���`a(���bs1a'���bs1kViolin plot���bs1a'���`a)���`a
���`a
���bc1o# plot box plot���`a
���`caxs���`a[���bmia1���`a]���aoa.���`gboxplot���`a(���`hall_data���`a)���`a
���`caxs���`a[���bmia1���`a]���aoa.���`iset_title���`a(���bs1a'���bs1hBox plot���bs1a'���`a)���`a
���`a
���bc1x# adding horizontal grid lines���`a
���akcfor���`a ���`bax���`a ���bowbin���`a ���`caxs���`a:���`a
���`d    ���`bax���aoa.���`eyaxis���aoa.���`dgrid���`a(���bkcdTrue���`a)���`a
���`d    ���`bax���aoa.���`jset_xticks���`a(���`a[���`ay���`a ���aoa+���`a ���bmia1���`a ���akcfor���`a ���`ay���`a ���bowbin���`a ���bnberange���`a(���bnbclen���`a(���`hall_data���`a)���`a)���`a]���`a,���`a
���`r                  ���`flabels���aoa=���`a[���bs1a'���bs1bx1���bs1a'���`a,���`a ���bs1a'���bs1bx2���bs1a'���`a,���`a ���bs1a'���bs1bx3���bs1a'���`a,���`a ���bs1a'���bs1bx4���bs1a'���`a]���`a)���`a
���`d    ���`bax���aoa.���`jset_xlabel���`a(���bs1a'���bs1uFour separate samples���bs1a'���`a)���`a
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
���bc1xI#    - `matplotlib.axes.Axes.violinplot` / `matplotlib.pyplot.violinplot`���`a
`dNone�