������������bsdy�"""
==========================================
Producing multiple histograms side by side
==========================================

This example plots horizontal histograms of different samples along
a categorical x-axis. Additionally, the histograms are plotted to
be symmetrical about their x-position, thus making them very similar
to violin plots.

To make this highly specialized plot, we can't use the standard ``hist``
method. Instead we use ``barh`` to draw the horizontal bars directly. The
vertical positions and lengths of the bars are computed via the
``np.histogram`` function. The histograms for all the samples are
computed using the same range (min and max values) and number of bins,
so that the bins for each sample are in the same vertical positions.

Selecting different bin counts and sizes can significantly affect the
shape of a histogram. The Astropy docs have a great section on how to
select these parameters:
http://docs.astropy.org/en/stable/visualization/histogram.html
"""���`a
���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���`a
���`bnp���aoa.���`frandom���aoa.���`dseed���`a(���bmih19680801���`a)���`a
���`nnumber_of_bins���`a ���aoa=���`a ���bmib20���`a
���`a
���bc1x*# An example of three data sets to compare���`a
���`unumber_of_data_points���`a ���aoa=���`a ���bmic387���`a
���`flabels���`a ���aoa=���`a ���`a[���bs2a"���bs2aA���bs2a"���`a,���`a ���bs2a"���bs2aB���bs2a"���`a,���`a ���bs2a"���bs2aC���bs2a"���`a]���`a
���`idata_sets���`a ���aoa=���`a ���`a[���`bnp���aoa.���`frandom���aoa.���`fnormal���`a(���bmia0���`a,���`a ���bmia1���`a,���`a ���`unumber_of_data_points���`a)���`a,���`a
���`m             ���`bnp���aoa.���`frandom���aoa.���`fnormal���`a(���bmia6���`a,���`a ���bmia1���`a,���`a ���`unumber_of_data_points���`a)���`a,���`a
���`m             ���`bnp���aoa.���`frandom���aoa.���`fnormal���`a(���aoa-���bmia3���`a,���`a ���bmia1���`a,���`a ���`unumber_of_data_points���`a)���`a]���`a
���`a
���bc1x%# Computed quantities to aid plotting���`a
���`jhist_range���`a ���aoa=���`a ���`a(���`bnp���aoa.���`cmin���`a(���`idata_sets���`a)���`a,���`a ���`bnp���aoa.���`cmax���`a(���`idata_sets���`a)���`a)���`a
���`pbinned_data_sets���`a ���aoa=���`a ���`a[���`a
���`d    ���`bnp���aoa.���`ihistogram���`a(���`ad���`a,���`a ���bnberange���aoa=���`jhist_range���`a,���`a ���`dbins���aoa=���`nnumber_of_bins���`a)���`a[���bmia0���`a]���`a
���`d    ���akcfor���`a ���`ad���`a ���bowbin���`a ���`idata_sets���`a
���`a]���`a
���`obinned_maximums���`a ���aoa=���`a ���`bnp���aoa.���`cmax���`a(���`pbinned_data_sets���`a,���`a ���`daxis���aoa=���bmia1���`a)���`a
���`kx_locations���`a ���aoa=���`a ���`bnp���aoa.���`farange���`a(���bmia0���`a,���`a ���bnbcsum���`a(���`obinned_maximums���`a)���`a,���`a ���`bnp���aoa.���`cmax���`a(���`obinned_maximums���`a)���`a)���`a
���`a
���bc1x6# The bin_edges are the same for all of the histograms���`a
���`ibin_edges���`a ���aoa=���`a ���`bnp���aoa.���`hlinspace���`a(���`jhist_range���`a[���bmia0���`a]���`a,���`a ���`jhist_range���`a[���bmia1���`a]���`a,���`a ���`nnumber_of_bins���`a ���aoa+���`a ���bmia1���`a)���`a
���`gcenters���`a ���aoa=���`a ���bmfc0.5���`a ���aoa*���`a ���`a(���`ibin_edges���`a ���aoa+���`a ���`bnp���aoa.���`droll���`a(���`ibin_edges���`a,���`a ���bmia1���`a)���`a)���`a[���`a:���aoa-���bmia1���`a]���`a
���`gheights���`a ���aoa=���`a ���`bnp���aoa.���`ddiff���`a(���`ibin_edges���`a)���`a
���`a
���bc1x'# Cycle through and plot each histogram���`a
���`cfig���`a,���`a ���`bax���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`a)���`a
���akcfor���`a ���`ex_loc���`a,���`a ���`kbinned_data���`a ���bowbin���`a ���bnbczip���`a(���`kx_locations���`a,���`a ���`pbinned_data_sets���`a)���`a:���`a
���`d    ���`elefts���`a ���aoa=���`a ���`ex_loc���`a ���aoa-���`a ���bmfc0.5���`a ���aoa*���`a ���`kbinned_data���`a
���`d    ���`bax���aoa.���`dbarh���`a(���`gcenters���`a,���`a ���`kbinned_data���`a,���`a ���`fheight���aoa=���`gheights���`a,���`a ���`dleft���aoa=���`elefts���`a)���`a
���`a
���`bax���aoa.���`jset_xticks���`a(���`kx_locations���`a,���`a ���`flabels���`a)���`a
���`a
���`bax���aoa.���`jset_ylabel���`a(���bs2a"���bs2kData values���bs2a"���`a)���`a
���`bax���aoa.���`jset_xlabel���`a(���bs2a"���bs2iData sets���bs2a"���`a)���`a
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
���bc1x=#    - `matplotlib.axes.Axes.barh` / `matplotlib.pyplot.barh`���`a
`dNone�