ŸØÇÅŸ¥ÉôsŸ±Çbsdy◊"""
==================================================
Using histograms to plot a cumulative distribution
==================================================

This shows how to plot a cumulative, normalized histogram as a
step function in order to visualize the empirical cumulative
distribution function (CDF) of a sample. We also show the theoretical CDF.

A couple of other options to the ``hist`` function are demonstrated. Namely, we
use the *normed* parameter to normalize the histogram and a couple of different
options to the *cumulative* parameter. The *normed* parameter takes a boolean
value. When ``True``, the bin heights are scaled such that the total area of
the histogram is 1. The *cumulative* keyword argument is a little more nuanced.
Like *normed*, you can pass it True or False, but you can also pass it -1 to
reverse the distribution.

Since we're showing a normalized and cumulative histogram, these curves
are effectively the cumulative distribution functions (CDFs) of the
samples. In engineering, empirical CDFs are sometimes called
"non-exceedance" curves. In other words, you can look at the
y-value for a given-x-value to get the probability of and observation
from the sample not exceeding that x-value. For example, the value of
225 on the x-axis corresponds to about 0.85 on the y-axis, so there's an
85% chance that an observation in the sample does not exceed 225.
Conversely, setting, ``cumulative`` to -1 as is done in the
last series for this example, creates a "exceedance" curve.

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
Ÿ±Ç`bmuŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Çbmic200Ÿ±Ç`a
Ÿ±Ç`esigmaŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Çbmib25Ÿ±Ç`a
Ÿ±Ç`fn_binsŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Çbmib50Ÿ±Ç`a
Ÿ±Ç`axŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`frandomŸ±Çaoa.Ÿ±Ç`fnormalŸ±Ç`a(Ÿ±Ç`bmuŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`esigmaŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dsizeŸ±Çaoa=Ÿ±Çbmic100Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`cfigŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`baxŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`hsubplotsŸ±Ç`a(Ÿ±Ç`gfigsizeŸ±Çaoa=Ÿ±Ç`a(Ÿ±Çbmia8Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia4Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1x# plot the cumulative histogramŸ±Ç`a
Ÿ±Ç`anŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dbinsŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`gpatchesŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`dhistŸ±Ç`a(Ÿ±Ç`axŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`fn_binsŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`gdensityŸ±Çaoa=Ÿ±ÇbkcdTrueŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`hhisttypeŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1dstepŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`x                           Ÿ±Ç`jcumulativeŸ±Çaoa=Ÿ±ÇbkcdTrueŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`elabelŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1iEmpiricalŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1x/# Add a line showing the expected distribution.Ÿ±Ç`a
Ÿ±Ç`ayŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`a(Ÿ±Ç`a(Ÿ±Çbmia1Ÿ±Ç`a Ÿ±Çaoa/Ÿ±Ç`a Ÿ±Ç`a(Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`dsqrtŸ±Ç`a(Ÿ±Çbmia2Ÿ±Ç`a Ÿ±Çaoa*Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`bpiŸ±Ç`a)Ÿ±Ç`a Ÿ±Çaoa*Ÿ±Ç`a Ÿ±Ç`esigmaŸ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a Ÿ±Çaoa*Ÿ±Ç`a
Ÿ±Ç`e     Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`cexpŸ±Ç`a(Ÿ±Çaoa-Ÿ±Çbmfc0.5Ÿ±Ç`a Ÿ±Çaoa*Ÿ±Ç`a Ÿ±Ç`a(Ÿ±Çbmia1Ÿ±Ç`a Ÿ±Çaoa/Ÿ±Ç`a Ÿ±Ç`esigmaŸ±Ç`a Ÿ±Çaoa*Ÿ±Ç`a Ÿ±Ç`a(Ÿ±Ç`dbinsŸ±Ç`a Ÿ±Çaoa-Ÿ±Ç`a Ÿ±Ç`bmuŸ±Ç`a)Ÿ±Ç`a)Ÿ±Çaoa*Ÿ±Çaoa*Ÿ±Çbmia2Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`ayŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`ayŸ±Çaoa.Ÿ±Ç`fcumsumŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`ayŸ±Ç`a Ÿ±Çaoa/Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`ayŸ±Ç`a[Ÿ±Çaoa-Ÿ±Çbmia1Ÿ±Ç`a]Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`dplotŸ±Ç`a(Ÿ±Ç`dbinsŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ayŸ±Ç`a,Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1ck--Ÿ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ilinewidthŸ±Çaoa=Ÿ±Çbmfc1.5Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`elabelŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1kTheoreticalŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1x*# Overlay a reversed cumulative histogram.Ÿ±Ç`a
Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`dhistŸ±Ç`a(Ÿ±Ç`axŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dbinsŸ±Çaoa=Ÿ±Ç`dbinsŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`gdensityŸ±Çaoa=Ÿ±ÇbkcdTrueŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`hhisttypeŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1dstepŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`jcumulativeŸ±Çaoa=Ÿ±Çaoa-Ÿ±Çbmia1Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±Ç`elabelŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1mReversed emp.Ÿ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1t# tidy up the figureŸ±Ç`a
Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`dgridŸ±Ç`a(Ÿ±ÇbkcdTrueŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`flegendŸ±Ç`a(Ÿ±Ç`clocŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1erightŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`iset_titleŸ±Ç`a(Ÿ±Çbs1a'Ÿ±Çbs1xCumulative step histogramsŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`jset_xlabelŸ±Ç`a(Ÿ±Çbs1a'Ÿ±Çbs1tAnnual rainfall (mm)Ÿ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`jset_ylabelŸ±Ç`a(Ÿ±Çbs1a'Ÿ±Çbs1xLikelihood of occurrenceŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
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