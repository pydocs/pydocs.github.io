��������M���bsdyC"""
=====================================================
The histogram (hist) function with multiple data sets
=====================================================

Plot histogram with multiple sample sets and demonstrate:

* Use of legend with multiple sample sets
* Stacked bars
* Step curve with no fill
* Data sets of different sample sizes

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
���`a
���`fn_bins���`a ���aoa=���`a ���bmib10���`a
���`ax���`a ���aoa=���`a ���`bnp���aoa.���`frandom���aoa.���`erandn���`a(���bmid1000���`a,���`a ���bmia3���`a)���`a
���`a
���`cfig���`a,���`a ���`a(���`a(���`cax0���`a,���`a ���`cax1���`a)���`a,���`a ���`a(���`cax2���`a,���`a ���`cax3���`a)���`a)���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`enrows���aoa=���bmia2���`a,���`a ���`encols���aoa=���bmia2���`a)���`a
���`a
���`fcolors���`a ���aoa=���`a ���`a[���bs1a'���bs1cred���bs1a'���`a,���`a ���bs1a'���bs1ctan���bs1a'���`a,���`a ���bs1a'���bs1dlime���bs1a'���`a]���`a
���`cax0���aoa.���`dhist���`a(���`ax���`a,���`a ���`fn_bins���`a,���`a ���`gdensity���aoa=���bkcdTrue���`a,���`a ���`hhisttype���aoa=���bs1a'���bs1cbar���bs1a'���`a,���`a ���`ecolor���aoa=���`fcolors���`a,���`a ���`elabel���aoa=���`fcolors���`a)���`a
���`cax0���aoa.���`flegend���`a(���`dprop���aoa=���`a{���bs1a'���bs1dsize���bs1a'���`a:���`a ���bmib10���`a}���`a)���`a
���`cax0���aoa.���`iset_title���`a(���bs1a'���bs1pbars with legend���bs1a'���`a)���`a
���`a
���`cax1���aoa.���`dhist���`a(���`ax���`a,���`a ���`fn_bins���`a,���`a ���`gdensity���aoa=���bkcdTrue���`a,���`a ���`hhisttype���aoa=���bs1a'���bs1cbar���bs1a'���`a,���`a ���`gstacked���aoa=���bkcdTrue���`a)���`a
���`cax1���aoa.���`iset_title���`a(���bs1a'���bs1kstacked bar���bs1a'���`a)���`a
���`a
���`cax2���aoa.���`dhist���`a(���`ax���`a,���`a ���`fn_bins���`a,���`a ���`hhisttype���aoa=���bs1a'���bs1dstep���bs1a'���`a,���`a ���`gstacked���aoa=���bkcdTrue���`a,���`a ���`dfill���aoa=���bkceFalse���`a)���`a
���`cax2���aoa.���`iset_title���`a(���bs1a'���bs1ustack step (unfilled)���bs1a'���`a)���`a
���`a
���bc1x?# Make a multiple-histogram of data-sets with different length.���`a
���`gx_multi���`a ���aoa=���`a ���`a[���`bnp���aoa.���`frandom���aoa.���`erandn���`a(���`an���`a)���`a ���akcfor���`a ���`an���`a ���bowbin���`a ���`a[���bmie10000���`a,���`a ���bmid5000���`a,���`a ���bmid2000���`a]���`a]���`a
���`cax3���aoa.���`dhist���`a(���`gx_multi���`a,���`a ���`fn_bins���`a,���`a ���`hhisttype���aoa=���bs1a'���bs1cbar���bs1a'���`a)���`a
���`cax3���aoa.���`iset_title���`a(���bs1a'���bs1vdifferent sample sizes���bs1a'���`a)���`a
���`a
���`cfig���aoa.���`ltight_layout���`a(���`a)���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
���`a
���bc1xM#############################################################################���`a
���bc1a#���`a
���bc1x# .. admonition:: References���`a
���bc1a#���`a
���bc1xN#    The use of the following functions, methods, classes and modules is shown���`a
���bc1u#    in this example:���`a
���bc1a#���`a
���bc1x=#    - `matplotlib.axes.Axes.hist` / `matplotlib.pyplot.hist`���`a
`dNone�