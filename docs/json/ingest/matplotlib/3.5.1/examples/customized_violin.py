������������bsdy5"""
=========================
Violin plot customization
=========================

This example demonstrates how to fully customize violin plots. The first plot
shows the default style by providing only the data. The second plot first
limits what Matplotlib draws with additional keyword arguments. Then a
simplified representation of a box plot is drawn on top. Lastly, the styles of
the artists of the violins are modified.

For more information on violin plots, the scikit-learn docs have a great
section: https://scikit-learn.org/stable/modules/density.html
"""���`a
���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���`a
���`a
���akcdef���`a ���bnfoadjacent_values���`a(���`dvals���`a,���`a ���`bq1���`a,���`a ���`bq3���`a)���`a:���`a
���`d    ���`tupper_adjacent_value���`a ���aoa=���`a ���`bq3���`a ���aoa+���`a ���`a(���`bq3���`a ���aoa-���`a ���`bq1���`a)���`a ���aoa*���`a ���bmfc1.5���`a
���`d    ���`tupper_adjacent_value���`a ���aoa=���`a ���`bnp���aoa.���`dclip���`a(���`tupper_adjacent_value���`a,���`a ���`bq3���`a,���`a ���`dvals���`a[���aoa-���bmia1���`a]���`a)���`a
���`a
���`d    ���`tlower_adjacent_value���`a ���aoa=���`a ���`bq1���`a ���aoa-���`a ���`a(���`bq3���`a ���aoa-���`a ���`bq1���`a)���`a ���aoa*���`a ���bmfc1.5���`a
���`d    ���`tlower_adjacent_value���`a ���aoa=���`a ���`bnp���aoa.���`dclip���`a(���`tlower_adjacent_value���`a,���`a ���`dvals���`a[���bmia0���`a]���`a,���`a ���`bq1���`a)���`a
���`d    ���akfreturn���`a ���`tlower_adjacent_value���`a,���`a ���`tupper_adjacent_value���`a
���`a
���`a
���akcdef���`a ���bnfnset_axis_style���`a(���`bax���`a,���`a ���`flabels���`a)���`a:���`a
���`d    ���`bax���aoa.���`exaxis���aoa.���`oset_tick_params���`a(���`idirection���aoa=���bs1a'���bs1cout���bs1a'���`a)���`a
���`d    ���`bax���aoa.���`exaxis���aoa.���`rset_ticks_position���`a(���bs1a'���bs1fbottom���bs1a'���`a)���`a
���`d    ���`bax���aoa.���`jset_xticks���`a(���`bnp���aoa.���`farange���`a(���bmia1���`a,���`a ���bnbclen���`a(���`flabels���`a)���`a ���aoa+���`a ���bmia1���`a)���`a,���`a ���`flabels���aoa=���`flabels���`a)���`a
���`d    ���`bax���aoa.���`hset_xlim���`a(���bmfd0.25���`a,���`a ���bnbclen���`a(���`flabels���`a)���`a ���aoa+���`a ���bmfd0.75���`a)���`a
���`d    ���`bax���aoa.���`jset_xlabel���`a(���bs1a'���bs1kSample name���bs1a'���`a)���`a
���`a
���`a
���bc1r# create test data���`a
���`bnp���aoa.���`frandom���aoa.���`dseed���`a(���bmih19680801���`a)���`a
���`ddata���`a ���aoa=���`a ���`a[���bnbfsorted���`a(���`bnp���aoa.���`frandom���aoa.���`fnormal���`a(���bmia0���`a,���`a ���`cstd���`a,���`a ���bmic100���`a)���`a)���`a ���akcfor���`a ���`cstd���`a ���bowbin���`a ���bnberange���`a(���bmia1���`a,���`a ���bmia5���`a)���`a]���`a
���`a
���`cfig���`a,���`a ���`a(���`cax1���`a,���`a ���`cax2���`a)���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`enrows���aoa=���bmia1���`a,���`a ���`encols���aoa=���bmia2���`a,���`a ���`gfigsize���aoa=���`a(���bmia9���`a,���`a ���bmia4���`a)���`a,���`a ���`fsharey���aoa=���bkcdTrue���`a)���`a
���`a
���`cax1���aoa.���`iset_title���`a(���bs1a'���bs1sDefault violin plot���bs1a'���`a)���`a
���`cax1���aoa.���`jset_ylabel���`a(���bs1a'���bs1oObserved values���bs1a'���`a)���`a
���`cax1���aoa.���`jviolinplot���`a(���`ddata���`a)���`a
���`a
���`cax2���aoa.���`iset_title���`a(���bs1a'���bs1vCustomized violin plot���bs1a'���`a)���`a
���`eparts���`a ���aoa=���`a ���`cax2���aoa.���`jviolinplot���`a(���`a
���`h        ���`ddata���`a,���`a ���`ishowmeans���aoa=���bkceFalse���`a,���`a ���`kshowmedians���aoa=���bkceFalse���`a,���`a
���`h        ���`kshowextrema���aoa=���bkceFalse���`a)���`a
���`a
���akcfor���`a ���`bpc���`a ���bowbin���`a ���`eparts���`a[���bs1a'���bs1fbodies���bs1a'���`a]���`a:���`a
���`d    ���`bpc���aoa.���`mset_facecolor���`a(���bs1a'���bs1g#D43F3A���bs1a'���`a)���`a
���`d    ���`bpc���aoa.���`mset_edgecolor���`a(���bs1a'���bs1eblack���bs1a'���`a)���`a
���`d    ���`bpc���aoa.���`iset_alpha���`a(���bmia1���`a)���`a
���`a
���`iquartile1���`a,���`a ���`gmedians���`a,���`a ���`iquartile3���`a ���aoa=���`a ���`bnp���aoa.���`jpercentile���`a(���`ddata���`a,���`a ���`a[���bmib25���`a,���`a ���bmib50���`a,���`a ���bmib75���`a]���`a,���`a ���`daxis���aoa=���bmia1���`a)���`a
���`hwhiskers���`a ���aoa=���`a ���`bnp���aoa.���`earray���`a(���`a[���`a
���`d    ���`oadjacent_values���`a(���`lsorted_array���`a,���`a ���`bq1���`a,���`a ���`bq3���`a)���`a
���`d    ���akcfor���`a ���`lsorted_array���`a,���`a ���`bq1���`a,���`a ���`bq3���`a ���bowbin���`a ���bnbczip���`a(���`ddata���`a,���`a ���`iquartile1���`a,���`a ���`iquartile3���`a)���`a]���`a)���`a
���`lwhiskers_min���`a,���`a ���`lwhiskers_max���`a ���aoa=���`a ���`hwhiskers���`a[���`a:���`a,���`a ���bmia0���`a]���`a,���`a ���`hwhiskers���`a[���`a:���`a,���`a ���bmia1���`a]���`a
���`a
���`dinds���`a ���aoa=���`a ���`bnp���aoa.���`farange���`a(���bmia1���`a,���`a ���bnbclen���`a(���`gmedians���`a)���`a ���aoa+���`a ���bmia1���`a)���`a
���`cax2���aoa.���`gscatter���`a(���`dinds���`a,���`a ���`gmedians���`a,���`a ���`fmarker���aoa=���bs1a'���bs1ao���bs1a'���`a,���`a ���`ecolor���aoa=���bs1a'���bs1ewhite���bs1a'���`a,���`a ���`as���aoa=���bmib30���`a,���`a ���`fzorder���aoa=���bmia3���`a)���`a
���`cax2���aoa.���`fvlines���`a(���`dinds���`a,���`a ���`iquartile1���`a,���`a ���`iquartile3���`a,���`a ���`ecolor���aoa=���bs1a'���bs1ak���bs1a'���`a,���`a ���`ilinestyle���aoa=���bs1a'���bs1a-���bs1a'���`a,���`a ���`blw���aoa=���bmia5���`a)���`a
���`cax2���aoa.���`fvlines���`a(���`dinds���`a,���`a ���`lwhiskers_min���`a,���`a ���`lwhiskers_max���`a,���`a ���`ecolor���aoa=���bs1a'���bs1ak���bs1a'���`a,���`a ���`ilinestyle���aoa=���bs1a'���bs1a-���bs1a'���`a,���`a ���`blw���aoa=���bmia1���`a)���`a
���`a
���bc1x# set style for the axes���`a
���`flabels���`a ���aoa=���`a ���`a[���bs1a'���bs1aA���bs1a'���`a,���`a ���bs1a'���bs1aB���bs1a'���`a,���`a ���bs1a'���bs1aC���bs1a'���`a,���`a ���bs1a'���bs1aD���bs1a'���`a]���`a
���akcfor���`a ���`bax���`a ���bowbin���`a ���`a[���`cax1���`a,���`a ���`cax2���`a]���`a:���`a
���`d    ���`nset_axis_style���`a(���`bax���`a,���`a ���`flabels���`a)���`a
���`a
���`cplt���aoa.���`osubplots_adjust���`a(���`fbottom���aoa=���bmfd0.15���`a,���`a ���`fwspace���aoa=���bmfd0.05���`a)���`a
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
���bc1xA#    - `matplotlib.axes.Axes.vlines` / `matplotlib.pyplot.vlines`���`a
`dNone�