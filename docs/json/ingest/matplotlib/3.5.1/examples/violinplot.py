�������� ���bsdy�"""
==================
Violin plot basics
==================

Violin plots are similar to histograms and box plots in that they show
an abstract representation of the probability distribution of the
sample. Rather than showing counts of data points that fall into bins
or order statistics, violin plots use kernel density estimation (KDE) to
compute an empirical distribution of the sample. That computation
is controlled by several parameters. This example demonstrates how to
modify the number of points at which the KDE is evaluated (``points``)
and how to modify the band-width of the KDE (``bw_method``).

For more information on violin plots and KDE, the scikit-learn docs
have a great section: https://scikit-learn.org/stable/modules/density.html
"""���`a
���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���`a
���bc1x)# Fixing random state for reproducibility���`a
���`bnp���aoa.���`frandom���aoa.���`dseed���`a(���bmih19680801���`a)���`a
���`a
���`a
���bc1k# fake data���`a
���`bfs���`a ���aoa=���`a ���bmib10���`b  ���bc1j# fontsize���`a
���`cpos���`a ���aoa=���`a ���`a[���bmia1���`a,���`a ���bmia2���`a,���`a ���bmia4���`a,���`a ���bmia5���`a,���`a ���bmia7���`a,���`a ���bmia8���`a]���`a
���`ddata���`a ���aoa=���`a ���`a[���`bnp���aoa.���`frandom���aoa.���`fnormal���`a(���bmia0���`a,���`a ���`cstd���`a,���`a ���`dsize���aoa=���bmic100���`a)���`a ���akcfor���`a ���`cstd���`a ���bowbin���`a ���`cpos���`a]���`a
���`a
���`cfig���`a,���`a ���`caxs���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`enrows���aoa=���bmia2���`a,���`a ���`encols���aoa=���bmia5���`a,���`a ���`gfigsize���aoa=���`a(���bmib10���`a,���`a ���bmia6���`a)���`a)���`a
���`a
���`caxs���`a[���bmia0���`a,���`a ���bmia0���`a]���aoa.���`jviolinplot���`a(���`ddata���`a,���`a ���`cpos���`a,���`a ���`fpoints���aoa=���bmib20���`a,���`a ���`fwidths���aoa=���bmfc0.3���`a,���`a
���`u                     ���`ishowmeans���aoa=���bkcdTrue���`a,���`a ���`kshowextrema���aoa=���bkcdTrue���`a,���`a ���`kshowmedians���aoa=���bkcdTrue���`a)���`a
���`caxs���`a[���bmia0���`a,���`a ���bmia0���`a]���aoa.���`iset_title���`a(���bs1a'���bs1sCustom violinplot 1���bs1a'���`a,���`a ���`hfontsize���aoa=���`bfs���`a)���`a
���`a
���`caxs���`a[���bmia0���`a,���`a ���bmia1���`a]���aoa.���`jviolinplot���`a(���`ddata���`a,���`a ���`cpos���`a,���`a ���`fpoints���aoa=���bmib40���`a,���`a ���`fwidths���aoa=���bmfc0.5���`a,���`a
���`u                     ���`ishowmeans���aoa=���bkcdTrue���`a,���`a ���`kshowextrema���aoa=���bkcdTrue���`a,���`a ���`kshowmedians���aoa=���bkcdTrue���`a,���`a
���`u                     ���`ibw_method���aoa=���bs1a'���bs1isilverman���bs1a'���`a)���`a
���`caxs���`a[���bmia0���`a,���`a ���bmia1���`a]���aoa.���`iset_title���`a(���bs1a'���bs1sCustom violinplot 2���bs1a'���`a,���`a ���`hfontsize���aoa=���`bfs���`a)���`a
���`a
���`caxs���`a[���bmia0���`a,���`a ���bmia2���`a]���aoa.���`jviolinplot���`a(���`ddata���`a,���`a ���`cpos���`a,���`a ���`fpoints���aoa=���bmib60���`a,���`a ���`fwidths���aoa=���bmfc0.7���`a,���`a ���`ishowmeans���aoa=���bkcdTrue���`a,���`a
���`u                     ���`kshowextrema���aoa=���bkcdTrue���`a,���`a ���`kshowmedians���aoa=���bkcdTrue���`a,���`a ���`ibw_method���aoa=���bmfc0.5���`a)���`a
���`caxs���`a[���bmia0���`a,���`a ���bmia2���`a]���aoa.���`iset_title���`a(���bs1a'���bs1sCustom violinplot 3���bs1a'���`a,���`a ���`hfontsize���aoa=���`bfs���`a)���`a
���`a
���`caxs���`a[���bmia0���`a,���`a ���bmia3���`a]���aoa.���`jviolinplot���`a(���`ddata���`a,���`a ���`cpos���`a,���`a ���`fpoints���aoa=���bmib60���`a,���`a ���`fwidths���aoa=���bmfc0.7���`a,���`a ���`ishowmeans���aoa=���bkcdTrue���`a,���`a
���`u                     ���`kshowextrema���aoa=���bkcdTrue���`a,���`a ���`kshowmedians���aoa=���bkcdTrue���`a,���`a ���`ibw_method���aoa=���bmfc0.5���`a,���`a
���`u                     ���`iquantiles���aoa=���`a[���`a[���bmfc0.1���`a]���`a,���`a ���`a[���`a]���`a,���`a ���`a[���`a]���`a,���`a ���`a[���bmfe0.175���`a,���`a ���bmfe0.954���`a]���`a,���`a ���`a[���bmfd0.75���`a]���`a,���`a ���`a[���bmfd0.25���`a]���`a]���`a)���`a
���`caxs���`a[���bmia0���`a,���`a ���bmia3���`a]���aoa.���`iset_title���`a(���bs1a'���bs1sCustom violinplot 4���bs1a'���`a,���`a ���`hfontsize���aoa=���`bfs���`a)���`a
���`a
���`caxs���`a[���bmia0���`a,���`a ���bmia4���`a]���aoa.���`jviolinplot���`a(���`ddata���`a[���aoa-���bmia1���`a:���`a]���`a,���`a ���`cpos���`a[���aoa-���bmia1���`a:���`a]���`a,���`a ���`fpoints���aoa=���bmib60���`a,���`a ���`fwidths���aoa=���bmfc0.7���`a,���`a
���`u                     ���`ishowmeans���aoa=���bkcdTrue���`a,���`a ���`kshowextrema���aoa=���bkcdTrue���`a,���`a ���`kshowmedians���aoa=���bkcdTrue���`a,���`a
���`u                     ���`iquantiles���aoa=���`a[���bmfd0.05���`a,���`a ���bmfc0.1���`a,���`a ���bmfc0.8���`a,���`a ���bmfc0.9���`a]���`a,���`a ���`ibw_method���aoa=���bmfc0.5���`a)���`a
���`caxs���`a[���bmia0���`a,���`a ���bmia4���`a]���aoa.���`iset_title���`a(���bs1a'���bs1sCustom violinplot 5���bs1a'���`a,���`a ���`hfontsize���aoa=���`bfs���`a)���`a
���`a
���`caxs���`a[���bmia1���`a,���`a ���bmia0���`a]���aoa.���`jviolinplot���`a(���`ddata���`a,���`a ���`cpos���`a,���`a ���`fpoints���aoa=���bmib80���`a,���`a ���`dvert���aoa=���bkceFalse���`a,���`a ���`fwidths���aoa=���bmfc0.7���`a,���`a
���`u                     ���`ishowmeans���aoa=���bkcdTrue���`a,���`a ���`kshowextrema���aoa=���bkcdTrue���`a,���`a ���`kshowmedians���aoa=���bkcdTrue���`a)���`a
���`caxs���`a[���bmia1���`a,���`a ���bmia0���`a]���aoa.���`iset_title���`a(���bs1a'���bs1sCustom violinplot 6���bs1a'���`a,���`a ���`hfontsize���aoa=���`bfs���`a)���`a
���`a
���`caxs���`a[���bmia1���`a,���`a ���bmia1���`a]���aoa.���`jviolinplot���`a(���`ddata���`a,���`a ���`cpos���`a,���`a ���`fpoints���aoa=���bmic100���`a,���`a ���`dvert���aoa=���bkceFalse���`a,���`a ���`fwidths���aoa=���bmfc0.9���`a,���`a
���`u                     ���`ishowmeans���aoa=���bkcdTrue���`a,���`a ���`kshowextrema���aoa=���bkcdTrue���`a,���`a ���`kshowmedians���aoa=���bkcdTrue���`a,���`a
���`u                     ���`ibw_method���aoa=���bs1a'���bs1isilverman���bs1a'���`a)���`a
���`caxs���`a[���bmia1���`a,���`a ���bmia1���`a]���aoa.���`iset_title���`a(���bs1a'���bs1sCustom violinplot 7���bs1a'���`a,���`a ���`hfontsize���aoa=���`bfs���`a)���`a
���`a
���`caxs���`a[���bmia1���`a,���`a ���bmia2���`a]���aoa.���`jviolinplot���`a(���`ddata���`a,���`a ���`cpos���`a,���`a ���`fpoints���aoa=���bmic200���`a,���`a ���`dvert���aoa=���bkceFalse���`a,���`a ���`fwidths���aoa=���bmfc1.1���`a,���`a
���`u                     ���`ishowmeans���aoa=���bkcdTrue���`a,���`a ���`kshowextrema���aoa=���bkcdTrue���`a,���`a ���`kshowmedians���aoa=���bkcdTrue���`a,���`a
���`u                     ���`ibw_method���aoa=���bmfc0.5���`a)���`a
���`caxs���`a[���bmia1���`a,���`a ���bmia2���`a]���aoa.���`iset_title���`a(���bs1a'���bs1sCustom violinplot 8���bs1a'���`a,���`a ���`hfontsize���aoa=���`bfs���`a)���`a
���`a
���`caxs���`a[���bmia1���`a,���`a ���bmia3���`a]���aoa.���`jviolinplot���`a(���`ddata���`a,���`a ���`cpos���`a,���`a ���`fpoints���aoa=���bmic200���`a,���`a ���`dvert���aoa=���bkceFalse���`a,���`a ���`fwidths���aoa=���bmfc1.1���`a,���`a
���`u                     ���`ishowmeans���aoa=���bkcdTrue���`a,���`a ���`kshowextrema���aoa=���bkcdTrue���`a,���`a ���`kshowmedians���aoa=���bkcdTrue���`a,���`a
���`u                     ���`iquantiles���aoa=���`a[���`a[���bmfc0.1���`a]���`a,���`a ���`a[���`a]���`a,���`a ���`a[���`a]���`a,���`a ���`a[���bmfe0.175���`a,���`a ���bmfe0.954���`a]���`a,���`a ���`a[���bmfd0.75���`a]���`a,���`a ���`a[���bmfd0.25���`a]���`a]���`a,���`a
���`u                     ���`ibw_method���aoa=���bmfc0.5���`a)���`a
���`caxs���`a[���bmia1���`a,���`a ���bmia3���`a]���aoa.���`iset_title���`a(���bs1a'���bs1sCustom violinplot 9���bs1a'���`a,���`a ���`hfontsize���aoa=���`bfs���`a)���`a
���`a
���`caxs���`a[���bmia1���`a,���`a ���bmia4���`a]���aoa.���`jviolinplot���`a(���`ddata���`a[���aoa-���bmia1���`a:���`a]���`a,���`a ���`cpos���`a[���aoa-���bmia1���`a:���`a]���`a,���`a ���`fpoints���aoa=���bmic200���`a,���`a ���`dvert���aoa=���bkceFalse���`a,���`a ���`fwidths���aoa=���bmfc1.1���`a,���`a
���`u                     ���`ishowmeans���aoa=���bkcdTrue���`a,���`a ���`kshowextrema���aoa=���bkcdTrue���`a,���`a ���`kshowmedians���aoa=���bkcdTrue���`a,���`a
���`u                     ���`iquantiles���aoa=���`a[���bmfd0.05���`a,���`a ���bmfc0.1���`a,���`a ���bmfc0.8���`a,���`a ���bmfc0.9���`a]���`a,���`a ���`ibw_method���aoa=���bmfc0.5���`a)���`a
���`caxs���`a[���bmia1���`a,���`a ���bmia4���`a]���aoa.���`iset_title���`a(���bs1a'���bs1tCustom violinplot 10���bs1a'���`a,���`a ���`hfontsize���aoa=���`bfs���`a)���`a
���`a
���`a
���akcfor���`a ���`bax���`a ���bowbin���`a ���`caxs���aoa.���`dflat���`a:���`a
���`d    ���`bax���aoa.���`oset_yticklabels���`a(���`a[���`a]���`a)���`a
���`a
���`cfig���aoa.���`hsuptitle���`a(���bs2a"���bs2xViolin Plotting Examples���bs2a"���`a)���`a
���`cfig���aoa.���`osubplots_adjust���`a(���`fhspace���aoa=���bmfc0.4���`a)���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
���`a
���bc1xM#############################################################################���`a
���bc1a#���`a
���bc1x# .. admonition:: References���`a
���bc1a#���`a
���bc1xN#    The use of the following functions, methods, classes and modules is shown���`a
���bc1u#    in this example:���`a
���bc1a#���`a
���bc1xI#    - `matplotlib.axes.Axes.violinplot` / `matplotlib.pyplot.violinplot`���`a
`dNone�