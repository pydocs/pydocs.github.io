Ù¯‚Ù´ƒ™£Ù±‚bsdyì"""
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
"""Ù±‚`a
Ù±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„enumpyÙ „enumpyf1.22.3fmoduleenumpyfmoduleõÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnnbnpÙ±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnnfpyplotÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnncpltÙ±‚`a
Ù±‚`a
Ù±‚`bnpÙ±‚aoa.Ù±‚`frandomÙ±‚aoa.Ù±‚`dseedÙ±‚`a(Ù±‚bmih19680801Ù±‚`a)Ù±‚`a
Ù±‚`nnumber_of_binsÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bmib20Ù±‚`a
Ù±‚`a
Ù±‚bc1x*# An example of three data sets to compareÙ±‚`a
Ù±‚`unumber_of_data_pointsÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bmic387Ù±‚`a
Ù±‚`flabelsÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`a[Ù±‚bs2a"Ù±‚bs2aAÙ±‚bs2a"Ù±‚`a,Ù±‚`a Ù±‚bs2a"Ù±‚bs2aBÙ±‚bs2a"Ù±‚`a,Ù±‚`a Ù±‚bs2a"Ù±‚bs2aCÙ±‚bs2a"Ù±‚`a]Ù±‚`a
Ù±‚`idata_setsÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`a[Ù±‚`bnpÙ±‚aoa.Ù±‚`frandomÙ±‚aoa.Ù±‚`fnormalÙ±‚`a(Ù±‚bmia0Ù±‚`a,Ù±‚`a Ù±‚bmia1Ù±‚`a,Ù±‚`a Ù±‚`unumber_of_data_pointsÙ±‚`a)Ù±‚`a,Ù±‚`a
Ù±‚`m             Ù±‚`bnpÙ±‚aoa.Ù±‚`frandomÙ±‚aoa.Ù±‚`fnormalÙ±‚`a(Ù±‚bmia6Ù±‚`a,Ù±‚`a Ù±‚bmia1Ù±‚`a,Ù±‚`a Ù±‚`unumber_of_data_pointsÙ±‚`a)Ù±‚`a,Ù±‚`a
Ù±‚`m             Ù±‚`bnpÙ±‚aoa.Ù±‚`frandomÙ±‚aoa.Ù±‚`fnormalÙ±‚`a(Ù±‚aoa-Ù±‚bmia3Ù±‚`a,Ù±‚`a Ù±‚bmia1Ù±‚`a,Ù±‚`a Ù±‚`unumber_of_data_pointsÙ±‚`a)Ù±‚`a]Ù±‚`a
Ù±‚`a
Ù±‚bc1x%# Computed quantities to aid plottingÙ±‚`a
Ù±‚`jhist_rangeÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`a(Ù±‚`bnpÙ±‚aoa.Ù±‚`cminÙ±‚`a(Ù±‚`idata_setsÙ±‚`a)Ù±‚`a,Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`cmaxÙ±‚`a(Ù±‚`idata_setsÙ±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`pbinned_data_setsÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`a[Ù±‚`a
Ù±‚`d    Ù±‚`bnpÙ±‚aoa.Ù±‚`ihistogramÙ±‚`a(Ù±‚`adÙ±‚`a,Ù±‚`a Ù±‚bnberangeÙ±‚aoa=Ù±‚`jhist_rangeÙ±‚`a,Ù±‚`a Ù±‚`dbinsÙ±‚aoa=Ù±‚`nnumber_of_binsÙ±‚`a)Ù±‚`a[Ù±‚bmia0Ù±‚`a]Ù±‚`a
Ù±‚`d    Ù±‚akcforÙ±‚`a Ù±‚`adÙ±‚`a Ù±‚bowbinÙ±‚`a Ù±‚`idata_setsÙ±‚`a
Ù±‚`a]Ù±‚`a
Ù±‚`obinned_maximumsÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`cmaxÙ±‚`a(Ù±‚`pbinned_data_setsÙ±‚`a,Ù±‚`a Ù±‚`daxisÙ±‚aoa=Ù±‚bmia1Ù±‚`a)Ù±‚`a
Ù±‚`kx_locationsÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`farangeÙ±‚`a(Ù±‚bmia0Ù±‚`a,Ù±‚`a Ù±‚bnbcsumÙ±‚`a(Ù±‚`obinned_maximumsÙ±‚`a)Ù±‚`a,Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`cmaxÙ±‚`a(Ù±‚`obinned_maximumsÙ±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚bc1x6# The bin_edges are the same for all of the histogramsÙ±‚`a
Ù±‚`ibin_edgesÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`hlinspaceÙ±‚`a(Ù±‚`jhist_rangeÙ±‚`a[Ù±‚bmia0Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`jhist_rangeÙ±‚`a[Ù±‚bmia1Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`nnumber_of_binsÙ±‚`a Ù±‚aoa+Ù±‚`a Ù±‚bmia1Ù±‚`a)Ù±‚`a
Ù±‚`gcentersÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bmfc0.5Ù±‚`a Ù±‚aoa*Ù±‚`a Ù±‚`a(Ù±‚`ibin_edgesÙ±‚`a Ù±‚aoa+Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`drollÙ±‚`a(Ù±‚`ibin_edgesÙ±‚`a,Ù±‚`a Ù±‚bmia1Ù±‚`a)Ù±‚`a)Ù±‚`a[Ù±‚`a:Ù±‚aoa-Ù±‚bmia1Ù±‚`a]Ù±‚`a
Ù±‚`gheightsÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`ddiffÙ±‚`a(Ù±‚`ibin_edgesÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚bc1x'# Cycle through and plot each histogramÙ±‚`a
Ù±‚`cfigÙ±‚`a,Ù±‚`a Ù±‚`baxÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cpltÙ±‚aoa.Ù±‚`hsubplotsÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚akcforÙ±‚`a Ù±‚`ex_locÙ±‚`a,Ù±‚`a Ù±‚`kbinned_dataÙ±‚`a Ù±‚bowbinÙ±‚`a Ù±‚bnbczipÙ±‚`a(Ù±‚`kx_locationsÙ±‚`a,Ù±‚`a Ù±‚`pbinned_data_setsÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`d    Ù±‚`eleftsÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`ex_locÙ±‚`a Ù±‚aoa-Ù±‚`a Ù±‚bmfc0.5Ù±‚`a Ù±‚aoa*Ù±‚`a Ù±‚`kbinned_dataÙ±‚`a
Ù±‚`d    Ù±‚`baxÙ±‚aoa.Ù±‚`dbarhÙ±‚`a(Ù±‚`gcentersÙ±‚`a,Ù±‚`a Ù±‚`kbinned_dataÙ±‚`a,Ù±‚`a Ù±‚`fheightÙ±‚aoa=Ù±‚`gheightsÙ±‚`a,Ù±‚`a Ù±‚`dleftÙ±‚aoa=Ù±‚`eleftsÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`jset_xticksÙ±‚`a(Ù±‚`kx_locationsÙ±‚`a,Ù±‚`a Ù±‚`flabelsÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`jset_ylabelÙ±‚`a(Ù±‚bs2a"Ù±‚bs2kData valuesÙ±‚bs2a"Ù±‚`a)Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`jset_xlabelÙ±‚`a(Ù±‚bs2a"Ù±‚bs2iData setsÙ±‚bs2a"Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`cpltÙ±‚aoa.Ù±‚`dshowÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚bc1xM#############################################################################Ù±‚`a
Ù±‚bc1a#Ù±‚`a
Ù±‚bc1x# .. admonition:: ReferencesÙ±‚`a
Ù±‚bc1a#Ù±‚`a
Ù±‚bc1xN#    The use of the following functions, methods, classes and modules is shownÙ±‚`a
Ù±‚bc1u#    in this example:Ù±‚`a
Ù±‚bc1a#Ù±‚`a
Ù±‚bc1x=#    - `matplotlib.axes.Axes.barh` / `matplotlib.pyplot.barh`Ù±‚`a
`dNoneö