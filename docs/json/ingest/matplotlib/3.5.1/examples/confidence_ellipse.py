ŸØÇÅŸ¥ÉôùŸ±ÇbsdyÆ"""
======================================================
Plot a confidence ellipse of a two-dimensional dataset
======================================================

This example shows how to plot a confidence ellipse of a
two-dimensional dataset, using its pearson correlation coefficient.

The approach that is used to obtain the correct geometry is
explained and proved here:

https://carstenschelp.github.io/2018/09/14/Plot_Confidence_Ellipse_001.html

The method avoids the use of an iterative eigen decomposition algorithm
and makes use of the fact that a normalized covariance matrix (composed of
pearson correlation coefficients and ones) is particularly easy to handle.
"""Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±ÇbknfimportŸ±Ç`a Ÿ±ÇbnnŸ¢ÑenumpyŸ†Ñenumpyf1.22.3fmoduleenumpyfmoduleıŸ±Ç`a Ÿ±ÇakbasŸ±Ç`a Ÿ±ÇbnnbnpŸ±Ç`a
Ÿ±ÇbknfimportŸ±Ç`a Ÿ±ÇbnnŸ¢ÑjmatplotlibŸ†Ñjmatplotlibe3.5.1fmodulejmatplotlibfmoduleıŸ±Çbnna.Ÿ±ÇbnnfpyplotŸ±Ç`a Ÿ±ÇakbasŸ±Ç`a Ÿ±ÇbnncpltŸ±Ç`a
Ÿ±ÇbkndfromŸ±Ç`a Ÿ±ÇbnnŸ¢ÑjmatplotlibŸ†Ñjmatplotlibe3.5.1fmodulejmatplotlibfmoduleıŸ±Çbnna.Ÿ±ÇbnngpatchesŸ±Ç`a Ÿ±ÇbknfimportŸ±Ç`a Ÿ±Ç`gEllipseŸ±Ç`a
Ÿ±ÇbknfimportŸ±Ç`a Ÿ±ÇbnnŸ¢ÑjmatplotlibŸ†Ñjmatplotlibe3.5.1fmodulejmatplotlibfmoduleıŸ±Çbnna.Ÿ±ÇbnnjtransformsŸ±Ç`a Ÿ±ÇakbasŸ±Ç`a Ÿ±ÇbnnjtransformsŸ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1xM#############################################################################Ÿ±Ç`a
Ÿ±Çbc1a#Ÿ±Ç`a
Ÿ±Çbc1x# The plotting function itselfŸ±Ç`a
Ÿ±Çbc1x# """"""""""""""""""""""""""""Ÿ±Ç`a
Ÿ±Çbc1a#Ÿ±Ç`a
Ÿ±Çbc1xK# This function plots the confidence ellipse of the covariance of the givenŸ±Ç`a
Ÿ±Çbc1xE# array-like variables x and y. The ellipse is plotted into the givenŸ±Ç`a
Ÿ±Çbc1q# axes-object ax.Ÿ±Ç`a
Ÿ±Çbc1a#Ÿ±Ç`a
Ÿ±Çbc1xL# The radiuses of the ellipse can be controlled by n_std which is the numberŸ±Ç`a
Ÿ±Çbc1xH# of standard deviations. The default value is 3 which makes the ellipseŸ±Ç`a
Ÿ±Çbc1xA# enclose 98.9% of the points if the data is normally distributedŸ±Ç`a
Ÿ±Çbc1xD# like in these examples (3 standard deviations in 1-D contain 99.7%Ÿ±Ç`a
Ÿ±Çbc1x2# of the data, which is 98.9% of the data in 2-D).Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±ÇakcdefŸ±Ç`a Ÿ±Çbnfrconfidence_ellipseŸ±Ç`a(Ÿ±Ç`axŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ayŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`baxŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`en_stdŸ±Çaoa=Ÿ±Çbmfc3.0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ifacecolorŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1dnoneŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çaoa*Ÿ±Çaoa*Ÿ±Ç`fkwargsŸ±Ç`a)Ÿ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Çbsdy‘"""
    Create a plot of the covariance confidence ellipse of *x* and *y*.

    Parameters
    ----------
    x, y : array-like, shape (n, )
        Input data.

    ax : matplotlib.axes.Axes
        The axes object to draw the ellipse into.

    n_std : float
        The number of standard deviations to determine the ellipse's radiuses.

    **kwargs
        Forwarded to `~matplotlib.patches.Ellipse`

    Returns
    -------
    matplotlib.patches.Ellipse
    """Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±ÇakbifŸ±Ç`a Ÿ±Ç`axŸ±Çaoa.Ÿ±Ç`dsizeŸ±Ç`a Ÿ±Çaob!=Ÿ±Ç`a Ÿ±Ç`ayŸ±Çaoa.Ÿ±Ç`dsizeŸ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±ÇakeraiseŸ±Ç`a Ÿ±ÇbnejValueErrorŸ±Ç`a(Ÿ±Çbs2a"Ÿ±Çbs2xx and y must be the same sizeŸ±Çbs2a"Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`ccovŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`ccovŸ±Ç`a(Ÿ±Ç`axŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ayŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`gpearsonŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`ccovŸ±Ç`a[Ÿ±Çbmia0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia1Ÿ±Ç`a]Ÿ±Çaoa/Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`dsqrtŸ±Ç`a(Ÿ±Ç`ccovŸ±Ç`a[Ÿ±Çbmia0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia0Ÿ±Ç`a]Ÿ±Ç`a Ÿ±Çaoa*Ÿ±Ç`a Ÿ±Ç`ccovŸ±Ç`a[Ÿ±Çbmia1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia1Ÿ±Ç`a]Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Çbc1x8# Using a special case to obtain the eigenvalues of thisŸ±Ç`a
Ÿ±Ç`d    Ÿ±Çbc1x# two-dimensionl dataset.Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`lell_radius_xŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`dsqrtŸ±Ç`a(Ÿ±Çbmia1Ÿ±Ç`a Ÿ±Çaoa+Ÿ±Ç`a Ÿ±Ç`gpearsonŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`lell_radius_yŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`dsqrtŸ±Ç`a(Ÿ±Çbmia1Ÿ±Ç`a Ÿ±Çaoa-Ÿ±Ç`a Ÿ±Ç`gpearsonŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`gellipseŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`gEllipseŸ±Ç`a(Ÿ±Ç`a(Ÿ±Çbmia0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia0Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ewidthŸ±Çaoa=Ÿ±Ç`lell_radius_xŸ±Ç`a Ÿ±Çaoa*Ÿ±Ç`a Ÿ±Çbmia2Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`fheightŸ±Çaoa=Ÿ±Ç`lell_radius_yŸ±Ç`a Ÿ±Çaoa*Ÿ±Ç`a Ÿ±Çbmia2Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`v                      Ÿ±Ç`ifacecolorŸ±Çaoa=Ÿ±Ç`ifacecolorŸ±Ç`a,Ÿ±Ç`a Ÿ±Çaoa*Ÿ±Çaoa*Ÿ±Ç`fkwargsŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Çbc1x/# Calculating the stdandard deviation of x fromŸ±Ç`a
Ÿ±Ç`d    Ÿ±Çbc1x0# the squareroot of the variance and multiplyingŸ±Ç`a
Ÿ±Ç`d    Ÿ±Çbc1x/# with the given number of standard deviations.Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`gscale_xŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`dsqrtŸ±Ç`a(Ÿ±Ç`ccovŸ±Ç`a[Ÿ±Çbmia0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia0Ÿ±Ç`a]Ÿ±Ç`a)Ÿ±Ç`a Ÿ±Çaoa*Ÿ±Ç`a Ÿ±Ç`en_stdŸ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`fmean_xŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`dmeanŸ±Ç`a(Ÿ±Ç`axŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Çbc1x.# calculating the stdandard deviation of y ...Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`gscale_yŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`dsqrtŸ±Ç`a(Ÿ±Ç`ccovŸ±Ç`a[Ÿ±Çbmia1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia1Ÿ±Ç`a]Ÿ±Ç`a)Ÿ±Ç`a Ÿ±Çaoa*Ÿ±Ç`a Ÿ±Ç`en_stdŸ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`fmean_yŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`dmeanŸ±Ç`a(Ÿ±Ç`ayŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`ftransfŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`jtransformsŸ±Çaoa.Ÿ±Ç`hAffine2DŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a Ÿ±Ç`b\
Ÿ±Ç`h        Ÿ±Çaoa.Ÿ±Ç`jrotate_degŸ±Ç`a(Ÿ±Çbmib45Ÿ±Ç`a)Ÿ±Ç`a Ÿ±Ç`b\
Ÿ±Ç`h        Ÿ±Çaoa.Ÿ±Ç`escaleŸ±Ç`a(Ÿ±Ç`gscale_xŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`gscale_yŸ±Ç`a)Ÿ±Ç`a Ÿ±Ç`b\
Ÿ±Ç`h        Ÿ±Çaoa.Ÿ±Ç`itranslateŸ±Ç`a(Ÿ±Ç`fmean_xŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`fmean_yŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`gellipseŸ±Çaoa.Ÿ±Ç`mset_transformŸ±Ç`a(Ÿ±Ç`ftransfŸ±Ç`a Ÿ±Çaoa+Ÿ±Ç`a Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`itransDataŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±ÇakfreturnŸ±Ç`a Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`iadd_patchŸ±Ç`a(Ÿ±Ç`gellipseŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1xM#############################################################################Ÿ±Ç`a
Ÿ±Çbc1a#Ÿ±Ç`a
Ÿ±Çbc1x2# A helper function to create a correlated datasetŸ±Ç`a
Ÿ±Çbc1x2# """"""""""""""""""""""""""""""""""""""""""""""""Ÿ±Ç`a
Ÿ±Çbc1a#Ÿ±Ç`a
Ÿ±Çbc1x<# Creates a random two-dimesional dataset with the specifiedŸ±Ç`a
Ÿ±Çbc1x3# two-dimensional mean (mu) and dimensions (scale).Ÿ±Ç`a
Ÿ±Çbc1x># The correlation can be controlled by the param 'dependency',Ÿ±Ç`a
Ÿ±Çbc1o# a 2x2 matrix.Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±ÇakcdefŸ±Ç`a Ÿ±Çbnfvget_correlated_datasetŸ±Ç`a(Ÿ±Ç`anŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`jdependencyŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`bmuŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`escaleŸ±Ç`a)Ÿ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`flatentŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`frandomŸ±Çaoa.Ÿ±Ç`erandnŸ±Ç`a(Ÿ±Ç`anŸ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia2Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`idependentŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`flatentŸ±Çaoa.Ÿ±Ç`cdotŸ±Ç`a(Ÿ±Ç`jdependencyŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`fscaledŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`idependentŸ±Ç`a Ÿ±Çaoa*Ÿ±Ç`a Ÿ±Ç`escaleŸ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`rscaled_with_offsetŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`fscaledŸ±Ç`a Ÿ±Çaoa+Ÿ±Ç`a Ÿ±Ç`bmuŸ±Ç`a
Ÿ±Ç`d    Ÿ±Çbc1x/# return x and y of the new, correlated datasetŸ±Ç`a
Ÿ±Ç`d    Ÿ±ÇakfreturnŸ±Ç`a Ÿ±Ç`rscaled_with_offsetŸ±Ç`a[Ÿ±Ç`a:Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia0Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`rscaled_with_offsetŸ±Ç`a[Ÿ±Ç`a:Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia1Ÿ±Ç`a]Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1xM#############################################################################Ÿ±Ç`a
Ÿ±Çbc1a#Ÿ±Ç`a
Ÿ±Çbc1x)# Positive, negative and weak correlationŸ±Ç`a
Ÿ±Çbc1x)# """""""""""""""""""""""""""""""""""""""Ÿ±Ç`a
Ÿ±Çbc1a#Ÿ±Ç`a
Ÿ±Çbc1xE# Note that the shape for the weak correlation (right) is an ellipse,Ÿ±Ç`a
Ÿ±Çbc1x6# not a circle because x and y are differently scaled.Ÿ±Ç`a
Ÿ±Çbc1x=# However, the fact that x and y are uncorrelated is shown byŸ±Ç`a
Ÿ±Çbc1x># the axes of the ellipse being aligned with the x- and y-axisŸ±Ç`a
Ÿ±Çbc1x# of the coordinate system.Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`frandomŸ±Çaoa.Ÿ±Ç`dseedŸ±Ç`a(Ÿ±Çbmia0Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`jPARAMETERSŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`a{Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Çbs1a'Ÿ±Çbs1tPositive correlationŸ±Çbs1a'Ÿ±Ç`a:Ÿ±Ç`a Ÿ±Ç`a[Ÿ±Ç`a[Ÿ±Çbmfd0.85Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd0.35Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`x                             Ÿ±Ç`a[Ÿ±Çbmfd0.15Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çaoa-Ÿ±Çbmfd0.65Ÿ±Ç`a]Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Çbs1a'Ÿ±Çbs1tNegative correlationŸ±Çbs1a'Ÿ±Ç`a:Ÿ±Ç`a Ÿ±Ç`a[Ÿ±Ç`a[Ÿ±Çbmfc0.9Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çaoa-Ÿ±Çbmfc0.4Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`x                             Ÿ±Ç`a[Ÿ±Çbmfc0.1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çaoa-Ÿ±Çbmfc0.6Ÿ±Ç`a]Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Çbs1a'Ÿ±Çbs1pWeak correlationŸ±Çbs1a'Ÿ±Ç`a:Ÿ±Ç`a Ÿ±Ç`a[Ÿ±Ç`a[Ÿ±Çbmia1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia0Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`x                         Ÿ±Ç`a[Ÿ±Çbmia0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia1Ÿ±Ç`a]Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`a}Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`bmuŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Çbmia2Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia4Ÿ±Ç`a
Ÿ±Ç`escaleŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Çbmia3Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia5Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`cfigŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`caxsŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`hsubplotsŸ±Ç`a(Ÿ±Çbmia1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia3Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`gfigsizeŸ±Çaoa=Ÿ±Ç`a(Ÿ±Çbmia9Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia3Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±ÇakcforŸ±Ç`a Ÿ±Ç`baxŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`a(Ÿ±Ç`etitleŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`jdependencyŸ±Ç`a)Ÿ±Ç`a Ÿ±ÇbowbinŸ±Ç`a Ÿ±ÇbnbczipŸ±Ç`a(Ÿ±Ç`caxsŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`jPARAMETERSŸ±Çaoa.Ÿ±Ç`eitemsŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`axŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ayŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`vget_correlated_datasetŸ±Ç`a(Ÿ±Çbmic800Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`jdependencyŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`bmuŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`escaleŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`gscatterŸ±Ç`a(Ÿ±Ç`axŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ayŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`asŸ±Çaoa=Ÿ±Çbmfc0.5Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`gaxvlineŸ±Ç`a(Ÿ±Ç`acŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1dgreyŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`blwŸ±Çaoa=Ÿ±Çbmia1Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`gaxhlineŸ±Ç`a(Ÿ±Ç`acŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1dgreyŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`blwŸ±Çaoa=Ÿ±Çbmia1Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`rconfidence_ellipseŸ±Ç`a(Ÿ±Ç`axŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ayŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`baxŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`iedgecolorŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1credŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`gscatterŸ±Ç`a(Ÿ±Ç`bmuŸ±Ç`a[Ÿ±Çbmia0Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`bmuŸ±Ç`a[Ÿ±Çbmia1Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`acŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1credŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`asŸ±Çaoa=Ÿ±Çbmia3Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`iset_titleŸ±Ç`a(Ÿ±Ç`etitleŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`dshowŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1xM#############################################################################Ÿ±Ç`a
Ÿ±Çbc1a#Ÿ±Ç`a
Ÿ±Çbc1x)# Different number of standard deviationsŸ±Ç`a
Ÿ±Çbc1x)# """""""""""""""""""""""""""""""""""""""Ÿ±Ç`a
Ÿ±Çbc1a#Ÿ±Ç`a
Ÿ±Çbc1x6# A plot with n_std = 3 (blue), 2 (purple) and 1 (red)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`cfigŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`gax_nstdŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`hsubplotsŸ±Ç`a(Ÿ±Ç`gfigsizeŸ±Çaoa=Ÿ±Ç`a(Ÿ±Çbmia6Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia6Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`odependency_nstdŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`a[Ÿ±Ç`a[Ÿ±Çbmfc0.8Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd0.75Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`s                   Ÿ±Ç`a[Ÿ±Çaoa-Ÿ±Çbmfc0.2Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd0.35Ÿ±Ç`a]Ÿ±Ç`a]Ÿ±Ç`a
Ÿ±Ç`bmuŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Çbmia0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia0Ÿ±Ç`a
Ÿ±Ç`escaleŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Çbmia8Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia5Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`gax_nstdŸ±Çaoa.Ÿ±Ç`gaxvlineŸ±Ç`a(Ÿ±Ç`acŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1dgreyŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`blwŸ±Çaoa=Ÿ±Çbmia1Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`gax_nstdŸ±Çaoa.Ÿ±Ç`gaxhlineŸ±Ç`a(Ÿ±Ç`acŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1dgreyŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`blwŸ±Çaoa=Ÿ±Çbmia1Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`axŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ayŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`vget_correlated_datasetŸ±Ç`a(Ÿ±Çbmic500Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`odependency_nstdŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`bmuŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`escaleŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`gax_nstdŸ±Çaoa.Ÿ±Ç`gscatterŸ±Ç`a(Ÿ±Ç`axŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ayŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`asŸ±Çaoa=Ÿ±Çbmfc0.5Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`rconfidence_ellipseŸ±Ç`a(Ÿ±Ç`axŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ayŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`gax_nstdŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`en_stdŸ±Çaoa=Ÿ±Çbmia1Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`s                   Ÿ±Ç`elabelŸ±Çaoa=Ÿ±ÇbsaarŸ±Çbs1a'Ÿ±Çbs1b$1Ÿ±Çbs1a\Ÿ±Çbs1fsigma$Ÿ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`iedgecolorŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1ifirebrickŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`rconfidence_ellipseŸ±Ç`a(Ÿ±Ç`axŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ayŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`gax_nstdŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`en_stdŸ±Çaoa=Ÿ±Çbmia2Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`s                   Ÿ±Ç`elabelŸ±Çaoa=Ÿ±ÇbsaarŸ±Çbs1a'Ÿ±Çbs1b$2Ÿ±Çbs1a\Ÿ±Çbs1fsigma$Ÿ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`iedgecolorŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1gfuchsiaŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ilinestyleŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1b--Ÿ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`rconfidence_ellipseŸ±Ç`a(Ÿ±Ç`axŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ayŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`gax_nstdŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`en_stdŸ±Çaoa=Ÿ±Çbmia3Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`s                   Ÿ±Ç`elabelŸ±Çaoa=Ÿ±ÇbsaarŸ±Çbs1a'Ÿ±Çbs1b$3Ÿ±Çbs1a\Ÿ±Çbs1fsigma$Ÿ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`iedgecolorŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1dblueŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ilinestyleŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1a:Ÿ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`gax_nstdŸ±Çaoa.Ÿ±Ç`gscatterŸ±Ç`a(Ÿ±Ç`bmuŸ±Ç`a[Ÿ±Çbmia0Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`bmuŸ±Ç`a[Ÿ±Çbmia1Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`acŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1credŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`asŸ±Çaoa=Ÿ±Çbmia3Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`gax_nstdŸ±Çaoa.Ÿ±Ç`iset_titleŸ±Ç`a(Ÿ±Çbs1a'Ÿ±Çbs1xDifferent standard deviationsŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`gax_nstdŸ±Çaoa.Ÿ±Ç`flegendŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`dshowŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1xM#############################################################################Ÿ±Ç`a
Ÿ±Çbc1a#Ÿ±Ç`a
Ÿ±Çbc1x# Using the keyword argumentsŸ±Ç`a
Ÿ±Çbc1x# """""""""""""""""""""""""""Ÿ±Ç`a
Ÿ±Çbc1a#Ÿ±Ç`a
Ÿ±Çbc1xM# Use the keyword arguments specified for `matplotlib.patches.Patch` in orderŸ±Ç`a
Ÿ±Çbc1x1# to have the ellipse rendered in different ways.Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`cfigŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`iax_kwargsŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`hsubplotsŸ±Ç`a(Ÿ±Ç`gfigsizeŸ±Çaoa=Ÿ±Ç`a(Ÿ±Çbmia6Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia6Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`qdependency_kwargsŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`a[Ÿ±Ç`a[Ÿ±Çaoa-Ÿ±Çbmfc0.8Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfc0.5Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`u                     Ÿ±Ç`a[Ÿ±Çaoa-Ÿ±Çbmfc0.2Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfc0.5Ÿ±Ç`a]Ÿ±Ç`a]Ÿ±Ç`a
Ÿ±Ç`bmuŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Çbmia2Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çaoa-Ÿ±Çbmia3Ÿ±Ç`a
Ÿ±Ç`escaleŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Çbmia6Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia5Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`iax_kwargsŸ±Çaoa.Ÿ±Ç`gaxvlineŸ±Ç`a(Ÿ±Ç`acŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1dgreyŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`blwŸ±Çaoa=Ÿ±Çbmia1Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`iax_kwargsŸ±Çaoa.Ÿ±Ç`gaxhlineŸ±Ç`a(Ÿ±Ç`acŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1dgreyŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`blwŸ±Çaoa=Ÿ±Çbmia1Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`axŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ayŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`vget_correlated_datasetŸ±Ç`a(Ÿ±Çbmic500Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`qdependency_kwargsŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`bmuŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`escaleŸ±Ç`a)Ÿ±Ç`a
Ÿ±Çbc1x8# Plot the ellipse with zorder=0 in order to demonstrateŸ±Ç`a
Ÿ±Çbc1x0# its transparency (caused by the use of alpha).Ÿ±Ç`a
Ÿ±Ç`rconfidence_ellipseŸ±Ç`a(Ÿ±Ç`axŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ayŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`iax_kwargsŸ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`s                   Ÿ±Ç`ealphaŸ±Çaoa=Ÿ±Çbmfc0.5Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ifacecolorŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1dpinkŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`iedgecolorŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1fpurpleŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`fzorderŸ±Çaoa=Ÿ±Çbmia0Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`iax_kwargsŸ±Çaoa.Ÿ±Ç`gscatterŸ±Ç`a(Ÿ±Ç`axŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ayŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`asŸ±Çaoa=Ÿ±Çbmfc0.5Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`iax_kwargsŸ±Çaoa.Ÿ±Ç`gscatterŸ±Ç`a(Ÿ±Ç`bmuŸ±Ç`a[Ÿ±Çbmia0Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`bmuŸ±Ç`a[Ÿ±Çbmia1Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`acŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1credŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`asŸ±Çaoa=Ÿ±Çbmia3Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`iax_kwargsŸ±Çaoa.Ÿ±Ç`iset_titleŸ±Ç`a(Ÿ±Çbs1a'Ÿ±Çbs1wUsing keyword argumentsŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`cfigŸ±Çaoa.Ÿ±Ç`osubplots_adjustŸ±Ç`a(Ÿ±Ç`fhspaceŸ±Çaoa=Ÿ±Çbmfd0.25Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`dshowŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1xM#############################################################################Ÿ±Ç`a
Ÿ±Çbc1a#Ÿ±Ç`a
Ÿ±Çbc1x# .. admonition:: ReferencesŸ±Ç`a
Ÿ±Çbc1a#Ÿ±Ç`a
Ÿ±Çbc1xN#    The use of the following functions, methods, classes and modules is shownŸ±Ç`a
Ÿ±Çbc1u#    in this example:Ÿ±Ç`a
Ÿ±Çbc1a#Ÿ±Ç`a
Ÿ±Çbc1x'#    - `matplotlib.transforms.Affine2D`Ÿ±Ç`a
Ÿ±Çbc1x##    - `matplotlib.patches.Ellipse`Ÿ±Ç`a
`dNoneˆ