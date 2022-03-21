ŸØÇÅŸ¥Éô•Ÿ±Çbsdya"""
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
"""Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±ÇbknfimportŸ±Ç`a Ÿ±ÇbnnŸ¢ÑenumpyŸ†Ñenumpyf1.22.3fmoduleenumpyfmoduleıŸ±Ç`a Ÿ±ÇakbasŸ±Ç`a Ÿ±ÇbnnbnpŸ±Ç`a
Ÿ±ÇbknfimportŸ±Ç`a Ÿ±ÇbnnŸ¢ÑjmatplotlibŸ†Ñjmatplotlibe3.5.1fmodulejmatplotlibfmoduleıŸ±Çbnna.Ÿ±ÇbnnfpyplotŸ±Ç`a Ÿ±ÇakbasŸ±Ç`a Ÿ±ÇbnncpltŸ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`frandomŸ±Çaoa.Ÿ±Ç`dseedŸ±Ç`a(Ÿ±Çbmih19680801Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`dmu_xŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Çbmic200Ÿ±Ç`a
Ÿ±Ç`gsigma_xŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Çbmib25Ÿ±Ç`a
Ÿ±Ç`axŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`frandomŸ±Çaoa.Ÿ±Ç`fnormalŸ±Ç`a(Ÿ±Ç`dmu_xŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`gsigma_xŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dsizeŸ±Çaoa=Ÿ±Çbmic100Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`dmu_wŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Çbmic200Ÿ±Ç`a
Ÿ±Ç`gsigma_wŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Çbmib10Ÿ±Ç`a
Ÿ±Ç`awŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`frandomŸ±Çaoa.Ÿ±Ç`fnormalŸ±Ç`a(Ÿ±Ç`dmu_wŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`gsigma_wŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dsizeŸ±Çaoa=Ÿ±Çbmic100Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`cfigŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`caxsŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`hsubplotsŸ±Ç`a(Ÿ±Ç`enrowsŸ±Çaoa=Ÿ±Çbmia2Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`encolsŸ±Çaoa=Ÿ±Çbmia2Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`caxsŸ±Ç`a[Ÿ±Çbmia0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia0Ÿ±Ç`a]Ÿ±Çaoa.Ÿ±Ç`dhistŸ±Ç`a(Ÿ±Ç`axŸ±Ç`a,Ÿ±Ç`a Ÿ±Çbmib20Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`gdensityŸ±Çaoa=Ÿ±ÇbkcdTrueŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`hhisttypeŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1jstepfilledŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ifacecolorŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1agŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`o               Ÿ±Ç`ealphaŸ±Çaoa=Ÿ±Çbmfd0.75Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`caxsŸ±Ç`a[Ÿ±Çbmia0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia0Ÿ±Ç`a]Ÿ±Çaoa.Ÿ±Ç`iset_titleŸ±Ç`a(Ÿ±Çbs1a'Ÿ±Çbs1jstepfilledŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`caxsŸ±Ç`a[Ÿ±Çbmia0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia1Ÿ±Ç`a]Ÿ±Çaoa.Ÿ±Ç`dhistŸ±Ç`a(Ÿ±Ç`axŸ±Ç`a,Ÿ±Ç`a Ÿ±Çbmib20Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`gdensityŸ±Çaoa=Ÿ±ÇbkcdTrueŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`hhisttypeŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1dstepŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ifacecolorŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1agŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`o               Ÿ±Ç`ealphaŸ±Çaoa=Ÿ±Çbmfd0.75Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`caxsŸ±Ç`a[Ÿ±Çbmia0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia1Ÿ±Ç`a]Ÿ±Çaoa.Ÿ±Ç`iset_titleŸ±Ç`a(Ÿ±Çbs1a'Ÿ±Çbs1dstepŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`caxsŸ±Ç`a[Ÿ±Çbmia1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia0Ÿ±Ç`a]Ÿ±Çaoa.Ÿ±Ç`dhistŸ±Ç`a(Ÿ±Ç`axŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`gdensityŸ±Çaoa=Ÿ±ÇbkcdTrueŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`hhisttypeŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1jbarstackedŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`frwidthŸ±Çaoa=Ÿ±Çbmfc0.8Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`caxsŸ±Ç`a[Ÿ±Çbmia1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia0Ÿ±Ç`a]Ÿ±Çaoa.Ÿ±Ç`dhistŸ±Ç`a(Ÿ±Ç`awŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`gdensityŸ±Çaoa=Ÿ±ÇbkcdTrueŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`hhisttypeŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1jbarstackedŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`frwidthŸ±Çaoa=Ÿ±Çbmfc0.8Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`caxsŸ±Ç`a[Ÿ±Çbmia1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia0Ÿ±Ç`a]Ÿ±Çaoa.Ÿ±Ç`iset_titleŸ±Ç`a(Ÿ±Çbs1a'Ÿ±Çbs1jbarstackedŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1xC# Create a histogram by providing the bin edges (unequally spaced).Ÿ±Ç`a
Ÿ±Ç`dbinsŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`a[Ÿ±Çbmic100Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmic150Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmic180Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmic195Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmic205Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmic220Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmic250Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmic300Ÿ±Ç`a]Ÿ±Ç`a
Ÿ±Ç`caxsŸ±Ç`a[Ÿ±Çbmia1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia1Ÿ±Ç`a]Ÿ±Çaoa.Ÿ±Ç`dhistŸ±Ç`a(Ÿ±Ç`axŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dbinsŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`gdensityŸ±Çaoa=Ÿ±ÇbkcdTrueŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`hhisttypeŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1cbarŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`frwidthŸ±Çaoa=Ÿ±Çbmfc0.8Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`caxsŸ±Ç`a[Ÿ±Çbmia1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia1Ÿ±Ç`a]Ÿ±Çaoa.Ÿ±Ç`iset_titleŸ±Ç`a(Ÿ±Çbs1a'Ÿ±Çbs1qbar, unequal binsŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`cfigŸ±Çaoa.Ÿ±Ç`ltight_layoutŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`dshowŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1xM#############################################################################Ÿ±Ç`a
Ÿ±Çbc1a#Ÿ±Ç`a
Ÿ±Çbc1x# .. admonition:: ReferencesŸ±Ç`a
Ÿ±Çbc1a#Ÿ±Ç`a
Ÿ±Çbc1xN#    The use of the following functions, methods, classes and modules is shownŸ±Ç`a
Ÿ±Çbc1u#    in this example:Ÿ±Ç`a
Ÿ±Çbc1a#Ÿ±Ç`a
Ÿ±Çbc1x=#    - `matplotlib.axes.Axes.hist` / `matplotlib.pyplot.hist`Ÿ±Ç`a
`dNoneˆ