������������bsdya"""
================================================================
Demo of the histogram function's different ``histtype`` settings
================================================================

* Histogram with step curve that has a color fill.
* Histogram with step curve with no fill.
* Histogram with custom and unequal bin widths.
* Two histograms with stacked bars.

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
���`dmu_x���`a ���aoa=���`a ���bmic200���`a
���`gsigma_x���`a ���aoa=���`a ���bmib25���`a
���`ax���`a ���aoa=���`a ���`bnp���aoa.���`frandom���aoa.���`fnormal���`a(���`dmu_x���`a,���`a ���`gsigma_x���`a,���`a ���`dsize���aoa=���bmic100���`a)���`a
���`a
���`dmu_w���`a ���aoa=���`a ���bmic200���`a
���`gsigma_w���`a ���aoa=���`a ���bmib10���`a
���`aw���`a ���aoa=���`a ���`bnp���aoa.���`frandom���aoa.���`fnormal���`a(���`dmu_w���`a,���`a ���`gsigma_w���`a,���`a ���`dsize���aoa=���bmic100���`a)���`a
���`a
���`cfig���`a,���`a ���`caxs���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`enrows���aoa=���bmia2���`a,���`a ���`encols���aoa=���bmia2���`a)���`a
���`a
���`caxs���`a[���bmia0���`a,���`a ���bmia0���`a]���aoa.���`dhist���`a(���`ax���`a,���`a ���bmib20���`a,���`a ���`gdensity���aoa=���bkcdTrue���`a,���`a ���`hhisttype���aoa=���bs1a'���bs1jstepfilled���bs1a'���`a,���`a ���`ifacecolor���aoa=���bs1a'���bs1ag���bs1a'���`a,���`a
���`o               ���`ealpha���aoa=���bmfd0.75���`a)���`a
���`caxs���`a[���bmia0���`a,���`a ���bmia0���`a]���aoa.���`iset_title���`a(���bs1a'���bs1jstepfilled���bs1a'���`a)���`a
���`a
���`caxs���`a[���bmia0���`a,���`a ���bmia1���`a]���aoa.���`dhist���`a(���`ax���`a,���`a ���bmib20���`a,���`a ���`gdensity���aoa=���bkcdTrue���`a,���`a ���`hhisttype���aoa=���bs1a'���bs1dstep���bs1a'���`a,���`a ���`ifacecolor���aoa=���bs1a'���bs1ag���bs1a'���`a,���`a
���`o               ���`ealpha���aoa=���bmfd0.75���`a)���`a
���`caxs���`a[���bmia0���`a,���`a ���bmia1���`a]���aoa.���`iset_title���`a(���bs1a'���bs1dstep���bs1a'���`a)���`a
���`a
���`caxs���`a[���bmia1���`a,���`a ���bmia0���`a]���aoa.���`dhist���`a(���`ax���`a,���`a ���`gdensity���aoa=���bkcdTrue���`a,���`a ���`hhisttype���aoa=���bs1a'���bs1jbarstacked���bs1a'���`a,���`a ���`frwidth���aoa=���bmfc0.8���`a)���`a
���`caxs���`a[���bmia1���`a,���`a ���bmia0���`a]���aoa.���`dhist���`a(���`aw���`a,���`a ���`gdensity���aoa=���bkcdTrue���`a,���`a ���`hhisttype���aoa=���bs1a'���bs1jbarstacked���bs1a'���`a,���`a ���`frwidth���aoa=���bmfc0.8���`a)���`a
���`caxs���`a[���bmia1���`a,���`a ���bmia0���`a]���aoa.���`iset_title���`a(���bs1a'���bs1jbarstacked���bs1a'���`a)���`a
���`a
���bc1xC# Create a histogram by providing the bin edges (unequally spaced).���`a
���`dbins���`a ���aoa=���`a ���`a[���bmic100���`a,���`a ���bmic150���`a,���`a ���bmic180���`a,���`a ���bmic195���`a,���`a ���bmic205���`a,���`a ���bmic220���`a,���`a ���bmic250���`a,���`a ���bmic300���`a]���`a
���`caxs���`a[���bmia1���`a,���`a ���bmia1���`a]���aoa.���`dhist���`a(���`ax���`a,���`a ���`dbins���`a,���`a ���`gdensity���aoa=���bkcdTrue���`a,���`a ���`hhisttype���aoa=���bs1a'���bs1cbar���bs1a'���`a,���`a ���`frwidth���aoa=���bmfc0.8���`a)���`a
���`caxs���`a[���bmia1���`a,���`a ���bmia1���`a]���aoa.���`iset_title���`a(���bs1a'���bs1qbar, unequal bins���bs1a'���`a)���`a
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