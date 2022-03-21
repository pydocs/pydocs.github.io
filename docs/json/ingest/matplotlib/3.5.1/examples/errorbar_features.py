ŸØÇÅŸ¥Éò‡Ÿ±Çbsdy‚"""
=======================================
Different ways of specifying error bars
=======================================

Errors can be specified as a constant value (as shown in
:doc:`/gallery/statistics/errorbar`). However, this example demonstrates
how they vary by specifying arrays of error values.

If the raw ``x`` and ``y`` data have length N, there are two options:

Array of shape (N,):
    Error varies for each point, but the error values are
    symmetric (i.e. the lower and upper values are equal).

Array of shape (2, N):
    Error varies for each point, and the lower and upper limits
    (in that order) are different (asymmetric case)

In addition, this example demonstrates how to use log
scale with error bars.
"""Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±ÇbknfimportŸ±Ç`a Ÿ±ÇbnnŸ¢ÑenumpyŸ†Ñenumpyf1.22.3fmoduleenumpyfmoduleıŸ±Ç`a Ÿ±ÇakbasŸ±Ç`a Ÿ±ÇbnnbnpŸ±Ç`a
Ÿ±ÇbknfimportŸ±Ç`a Ÿ±ÇbnnŸ¢ÑjmatplotlibŸ†Ñjmatplotlibe3.5.1fmodulejmatplotlibfmoduleıŸ±Çbnna.Ÿ±ÇbnnfpyplotŸ±Ç`a Ÿ±ÇakbasŸ±Ç`a Ÿ±ÇbnncpltŸ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1n# example dataŸ±Ç`a
Ÿ±Ç`axŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`farangeŸ±Ç`a(Ÿ±Çbmfc0.1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia4Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfc0.5Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`ayŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`cexpŸ±Ç`a(Ÿ±Çaoa-Ÿ±Ç`axŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1x4# example error bar values that vary with x-positionŸ±Ç`a
Ÿ±Ç`eerrorŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Çbmfc0.1Ÿ±Ç`a Ÿ±Çaoa+Ÿ±Ç`a Ÿ±Çbmfc0.2Ÿ±Ç`a Ÿ±Çaoa*Ÿ±Ç`a Ÿ±Ç`axŸ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`cfigŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`a(Ÿ±Ç`cax0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`cax1Ÿ±Ç`a)Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`hsubplotsŸ±Ç`a(Ÿ±Ç`enrowsŸ±Çaoa=Ÿ±Çbmia2Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`fsharexŸ±Çaoa=Ÿ±ÇbkcdTrueŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cax0Ÿ±Çaoa.Ÿ±Ç`herrorbarŸ±Ç`a(Ÿ±Ç`axŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ayŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dyerrŸ±Çaoa=Ÿ±Ç`eerrorŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`cfmtŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1b-oŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cax0Ÿ±Çaoa.Ÿ±Ç`iset_titleŸ±Ç`a(Ÿ±Çbs1a'Ÿ±Çbs1xvariable, symmetric errorŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1x/# error bar values w/ different -/+ errors thatŸ±Ç`a
Ÿ±Çbc1x# also vary with the x-positionŸ±Ç`a
Ÿ±Ç`klower_errorŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Çbmfc0.4Ÿ±Ç`a Ÿ±Çaoa*Ÿ±Ç`a Ÿ±Ç`eerrorŸ±Ç`a
Ÿ±Ç`kupper_errorŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`eerrorŸ±Ç`a
Ÿ±Ç`pasymmetric_errorŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`a[Ÿ±Ç`klower_errorŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`kupper_errorŸ±Ç`a]Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`cax1Ÿ±Çaoa.Ÿ±Ç`herrorbarŸ±Ç`a(Ÿ±Ç`axŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ayŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dxerrŸ±Çaoa=Ÿ±Ç`pasymmetric_errorŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`cfmtŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1aoŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cax1Ÿ±Çaoa.Ÿ±Ç`iset_titleŸ±Ç`a(Ÿ±Çbs1a'Ÿ±Çbs1xvariable, asymmetric errorŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cax1Ÿ±Çaoa.Ÿ±Ç`jset_yscaleŸ±Ç`a(Ÿ±Çbs1a'Ÿ±Çbs1clogŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`dshowŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1xM#############################################################################Ÿ±Ç`a
Ÿ±Çbc1a#Ÿ±Ç`a
Ÿ±Çbc1x# .. admonition:: ReferencesŸ±Ç`a
Ÿ±Çbc1a#Ÿ±Ç`a
Ÿ±Çbc1xN#    The use of the following functions, methods, classes and modules is shownŸ±Ç`a
Ÿ±Çbc1u#    in this example:Ÿ±Ç`a
Ÿ±Çbc1a#Ÿ±Ç`a
Ÿ±Çbc1xE#    - `matplotlib.axes.Axes.errorbar` / `matplotlib.pyplot.errorbar`Ÿ±Ç`a
`dNoneˆ