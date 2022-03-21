������������bsdy�"""
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
"""���`a
���`a
���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���bkndfrom���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnngpatches���`a ���bknfimport���`a ���`gEllipse���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnjtransforms���`a ���akbas���`a ���bnnjtransforms���`a
���`a
���`a
���bc1xM#############################################################################���`a
���bc1a#���`a
���bc1x# The plotting function itself���`a
���bc1x# """"""""""""""""""""""""""""���`a
���bc1a#���`a
���bc1xK# This function plots the confidence ellipse of the covariance of the given���`a
���bc1xE# array-like variables x and y. The ellipse is plotted into the given���`a
���bc1q# axes-object ax.���`a
���bc1a#���`a
���bc1xL# The radiuses of the ellipse can be controlled by n_std which is the number���`a
���bc1xH# of standard deviations. The default value is 3 which makes the ellipse���`a
���bc1xA# enclose 98.9% of the points if the data is normally distributed���`a
���bc1xD# like in these examples (3 standard deviations in 1-D contain 99.7%���`a
���bc1x2# of the data, which is 98.9% of the data in 2-D).���`a
���`a
���`a
���akcdef���`a ���bnfrconfidence_ellipse���`a(���`ax���`a,���`a ���`ay���`a,���`a ���`bax���`a,���`a ���`en_std���aoa=���bmfc3.0���`a,���`a ���`ifacecolor���aoa=���bs1a'���bs1dnone���bs1a'���`a,���`a ���aoa*���aoa*���`fkwargs���`a)���`a:���`a
���`d    ���bsdy�"""
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
    """���`a
���`d    ���akbif���`a ���`ax���aoa.���`dsize���`a ���aob!=���`a ���`ay���aoa.���`dsize���`a:���`a
���`h        ���akeraise���`a ���bnejValueError���`a(���bs2a"���bs2xx and y must be the same size���bs2a"���`a)���`a
���`a
���`d    ���`ccov���`a ���aoa=���`a ���`bnp���aoa.���`ccov���`a(���`ax���`a,���`a ���`ay���`a)���`a
���`d    ���`gpearson���`a ���aoa=���`a ���`ccov���`a[���bmia0���`a,���`a ���bmia1���`a]���aoa/���`bnp���aoa.���`dsqrt���`a(���`ccov���`a[���bmia0���`a,���`a ���bmia0���`a]���`a ���aoa*���`a ���`ccov���`a[���bmia1���`a,���`a ���bmia1���`a]���`a)���`a
���`d    ���bc1x8# Using a special case to obtain the eigenvalues of this���`a
���`d    ���bc1x# two-dimensionl dataset.���`a
���`d    ���`lell_radius_x���`a ���aoa=���`a ���`bnp���aoa.���`dsqrt���`a(���bmia1���`a ���aoa+���`a ���`gpearson���`a)���`a
���`d    ���`lell_radius_y���`a ���aoa=���`a ���`bnp���aoa.���`dsqrt���`a(���bmia1���`a ���aoa-���`a ���`gpearson���`a)���`a
���`d    ���`gellipse���`a ���aoa=���`a ���`gEllipse���`a(���`a(���bmia0���`a,���`a ���bmia0���`a)���`a,���`a ���`ewidth���aoa=���`lell_radius_x���`a ���aoa*���`a ���bmia2���`a,���`a ���`fheight���aoa=���`lell_radius_y���`a ���aoa*���`a ���bmia2���`a,���`a
���`v                      ���`ifacecolor���aoa=���`ifacecolor���`a,���`a ���aoa*���aoa*���`fkwargs���`a)���`a
���`a
���`d    ���bc1x/# Calculating the stdandard deviation of x from���`a
���`d    ���bc1x0# the squareroot of the variance and multiplying���`a
���`d    ���bc1x/# with the given number of standard deviations.���`a
���`d    ���`gscale_x���`a ���aoa=���`a ���`bnp���aoa.���`dsqrt���`a(���`ccov���`a[���bmia0���`a,���`a ���bmia0���`a]���`a)���`a ���aoa*���`a ���`en_std���`a
���`d    ���`fmean_x���`a ���aoa=���`a ���`bnp���aoa.���`dmean���`a(���`ax���`a)���`a
���`a
���`d    ���bc1x.# calculating the stdandard deviation of y ...���`a
���`d    ���`gscale_y���`a ���aoa=���`a ���`bnp���aoa.���`dsqrt���`a(���`ccov���`a[���bmia1���`a,���`a ���bmia1���`a]���`a)���`a ���aoa*���`a ���`en_std���`a
���`d    ���`fmean_y���`a ���aoa=���`a ���`bnp���aoa.���`dmean���`a(���`ay���`a)���`a
���`a
���`d    ���`ftransf���`a ���aoa=���`a ���`jtransforms���aoa.���`hAffine2D���`a(���`a)���`a ���`b\
���`h        ���aoa.���`jrotate_deg���`a(���bmib45���`a)���`a ���`b\
���`h        ���aoa.���`escale���`a(���`gscale_x���`a,���`a ���`gscale_y���`a)���`a ���`b\
���`h        ���aoa.���`itranslate���`a(���`fmean_x���`a,���`a ���`fmean_y���`a)���`a
���`a
���`d    ���`gellipse���aoa.���`mset_transform���`a(���`ftransf���`a ���aoa+���`a ���`bax���aoa.���`itransData���`a)���`a
���`d    ���akfreturn���`a ���`bax���aoa.���`iadd_patch���`a(���`gellipse���`a)���`a
���`a
���`a
���bc1xM#############################################################################���`a
���bc1a#���`a
���bc1x2# A helper function to create a correlated dataset���`a
���bc1x2# """"""""""""""""""""""""""""""""""""""""""""""""���`a
���bc1a#���`a
���bc1x<# Creates a random two-dimesional dataset with the specified���`a
���bc1x3# two-dimensional mean (mu) and dimensions (scale).���`a
���bc1x># The correlation can be controlled by the param 'dependency',���`a
���bc1o# a 2x2 matrix.���`a
���`a
���akcdef���`a ���bnfvget_correlated_dataset���`a(���`an���`a,���`a ���`jdependency���`a,���`a ���`bmu���`a,���`a ���`escale���`a)���`a:���`a
���`d    ���`flatent���`a ���aoa=���`a ���`bnp���aoa.���`frandom���aoa.���`erandn���`a(���`an���`a,���`a ���bmia2���`a)���`a
���`d    ���`idependent���`a ���aoa=���`a ���`flatent���aoa.���`cdot���`a(���`jdependency���`a)���`a
���`d    ���`fscaled���`a ���aoa=���`a ���`idependent���`a ���aoa*���`a ���`escale���`a
���`d    ���`rscaled_with_offset���`a ���aoa=���`a ���`fscaled���`a ���aoa+���`a ���`bmu���`a
���`d    ���bc1x/# return x and y of the new, correlated dataset���`a
���`d    ���akfreturn���`a ���`rscaled_with_offset���`a[���`a:���`a,���`a ���bmia0���`a]���`a,���`a ���`rscaled_with_offset���`a[���`a:���`a,���`a ���bmia1���`a]���`a
���`a
���`a
���bc1xM#############################################################################���`a
���bc1a#���`a
���bc1x)# Positive, negative and weak correlation���`a
���bc1x)# """""""""""""""""""""""""""""""""""""""���`a
���bc1a#���`a
���bc1xE# Note that the shape for the weak correlation (right) is an ellipse,���`a
���bc1x6# not a circle because x and y are differently scaled.���`a
���bc1x=# However, the fact that x and y are uncorrelated is shown by���`a
���bc1x># the axes of the ellipse being aligned with the x- and y-axis���`a
���bc1x# of the coordinate system.���`a
���`a
���`bnp���aoa.���`frandom���aoa.���`dseed���`a(���bmia0���`a)���`a
���`a
���`jPARAMETERS���`a ���aoa=���`a ���`a{���`a
���`d    ���bs1a'���bs1tPositive correlation���bs1a'���`a:���`a ���`a[���`a[���bmfd0.85���`a,���`a ���bmfd0.35���`a]���`a,���`a
���`x                             ���`a[���bmfd0.15���`a,���`a ���aoa-���bmfd0.65���`a]���`a]���`a,���`a
���`d    ���bs1a'���bs1tNegative correlation���bs1a'���`a:���`a ���`a[���`a[���bmfc0.9���`a,���`a ���aoa-���bmfc0.4���`a]���`a,���`a
���`x                             ���`a[���bmfc0.1���`a,���`a ���aoa-���bmfc0.6���`a]���`a]���`a,���`a
���`d    ���bs1a'���bs1pWeak correlation���bs1a'���`a:���`a ���`a[���`a[���bmia1���`a,���`a ���bmia0���`a]���`a,���`a
���`x                         ���`a[���bmia0���`a,���`a ���bmia1���`a]���`a]���`a,���`a
���`a}���`a
���`a
���`bmu���`a ���aoa=���`a ���bmia2���`a,���`a ���bmia4���`a
���`escale���`a ���aoa=���`a ���bmia3���`a,���`a ���bmia5���`a
���`a
���`cfig���`a,���`a ���`caxs���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���bmia1���`a,���`a ���bmia3���`a,���`a ���`gfigsize���aoa=���`a(���bmia9���`a,���`a ���bmia3���`a)���`a)���`a
���akcfor���`a ���`bax���`a,���`a ���`a(���`etitle���`a,���`a ���`jdependency���`a)���`a ���bowbin���`a ���bnbczip���`a(���`caxs���`a,���`a ���`jPARAMETERS���aoa.���`eitems���`a(���`a)���`a)���`a:���`a
���`d    ���`ax���`a,���`a ���`ay���`a ���aoa=���`a ���`vget_correlated_dataset���`a(���bmic800���`a,���`a ���`jdependency���`a,���`a ���`bmu���`a,���`a ���`escale���`a)���`a
���`d    ���`bax���aoa.���`gscatter���`a(���`ax���`a,���`a ���`ay���`a,���`a ���`as���aoa=���bmfc0.5���`a)���`a
���`a
���`d    ���`bax���aoa.���`gaxvline���`a(���`ac���aoa=���bs1a'���bs1dgrey���bs1a'���`a,���`a ���`blw���aoa=���bmia1���`a)���`a
���`d    ���`bax���aoa.���`gaxhline���`a(���`ac���aoa=���bs1a'���bs1dgrey���bs1a'���`a,���`a ���`blw���aoa=���bmia1���`a)���`a
���`a
���`d    ���`rconfidence_ellipse���`a(���`ax���`a,���`a ���`ay���`a,���`a ���`bax���`a,���`a ���`iedgecolor���aoa=���bs1a'���bs1cred���bs1a'���`a)���`a
���`a
���`d    ���`bax���aoa.���`gscatter���`a(���`bmu���`a[���bmia0���`a]���`a,���`a ���`bmu���`a[���bmia1���`a]���`a,���`a ���`ac���aoa=���bs1a'���bs1cred���bs1a'���`a,���`a ���`as���aoa=���bmia3���`a)���`a
���`d    ���`bax���aoa.���`iset_title���`a(���`etitle���`a)���`a
���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
���`a
���`a
���bc1xM#############################################################################���`a
���bc1a#���`a
���bc1x)# Different number of standard deviations���`a
���bc1x)# """""""""""""""""""""""""""""""""""""""���`a
���bc1a#���`a
���bc1x6# A plot with n_std = 3 (blue), 2 (purple) and 1 (red)���`a
���`a
���`cfig���`a,���`a ���`gax_nstd���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`gfigsize���aoa=���`a(���bmia6���`a,���`a ���bmia6���`a)���`a)���`a
���`a
���`odependency_nstd���`a ���aoa=���`a ���`a[���`a[���bmfc0.8���`a,���`a ���bmfd0.75���`a]���`a,���`a
���`s                   ���`a[���aoa-���bmfc0.2���`a,���`a ���bmfd0.35���`a]���`a]���`a
���`bmu���`a ���aoa=���`a ���bmia0���`a,���`a ���bmia0���`a
���`escale���`a ���aoa=���`a ���bmia8���`a,���`a ���bmia5���`a
���`a
���`gax_nstd���aoa.���`gaxvline���`a(���`ac���aoa=���bs1a'���bs1dgrey���bs1a'���`a,���`a ���`blw���aoa=���bmia1���`a)���`a
���`gax_nstd���aoa.���`gaxhline���`a(���`ac���aoa=���bs1a'���bs1dgrey���bs1a'���`a,���`a ���`blw���aoa=���bmia1���`a)���`a
���`a
���`ax���`a,���`a ���`ay���`a ���aoa=���`a ���`vget_correlated_dataset���`a(���bmic500���`a,���`a ���`odependency_nstd���`a,���`a ���`bmu���`a,���`a ���`escale���`a)���`a
���`gax_nstd���aoa.���`gscatter���`a(���`ax���`a,���`a ���`ay���`a,���`a ���`as���aoa=���bmfc0.5���`a)���`a
���`a
���`rconfidence_ellipse���`a(���`ax���`a,���`a ���`ay���`a,���`a ���`gax_nstd���`a,���`a ���`en_std���aoa=���bmia1���`a,���`a
���`s                   ���`elabel���aoa=���bsaar���bs1a'���bs1b$1���bs1a\���bs1fsigma$���bs1a'���`a,���`a ���`iedgecolor���aoa=���bs1a'���bs1ifirebrick���bs1a'���`a)���`a
���`rconfidence_ellipse���`a(���`ax���`a,���`a ���`ay���`a,���`a ���`gax_nstd���`a,���`a ���`en_std���aoa=���bmia2���`a,���`a
���`s                   ���`elabel���aoa=���bsaar���bs1a'���bs1b$2���bs1a\���bs1fsigma$���bs1a'���`a,���`a ���`iedgecolor���aoa=���bs1a'���bs1gfuchsia���bs1a'���`a,���`a ���`ilinestyle���aoa=���bs1a'���bs1b--���bs1a'���`a)���`a
���`rconfidence_ellipse���`a(���`ax���`a,���`a ���`ay���`a,���`a ���`gax_nstd���`a,���`a ���`en_std���aoa=���bmia3���`a,���`a
���`s                   ���`elabel���aoa=���bsaar���bs1a'���bs1b$3���bs1a\���bs1fsigma$���bs1a'���`a,���`a ���`iedgecolor���aoa=���bs1a'���bs1dblue���bs1a'���`a,���`a ���`ilinestyle���aoa=���bs1a'���bs1a:���bs1a'���`a)���`a
���`a
���`gax_nstd���aoa.���`gscatter���`a(���`bmu���`a[���bmia0���`a]���`a,���`a ���`bmu���`a[���bmia1���`a]���`a,���`a ���`ac���aoa=���bs1a'���bs1cred���bs1a'���`a,���`a ���`as���aoa=���bmia3���`a)���`a
���`gax_nstd���aoa.���`iset_title���`a(���bs1a'���bs1xDifferent standard deviations���bs1a'���`a)���`a
���`gax_nstd���aoa.���`flegend���`a(���`a)���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
���`a
���`a
���bc1xM#############################################################################���`a
���bc1a#���`a
���bc1x# Using the keyword arguments���`a
���bc1x# """""""""""""""""""""""""""���`a
���bc1a#���`a
���bc1xM# Use the keyword arguments specified for `matplotlib.patches.Patch` in order���`a
���bc1x1# to have the ellipse rendered in different ways.���`a
���`a
���`cfig���`a,���`a ���`iax_kwargs���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`gfigsize���aoa=���`a(���bmia6���`a,���`a ���bmia6���`a)���`a)���`a
���`qdependency_kwargs���`a ���aoa=���`a ���`a[���`a[���aoa-���bmfc0.8���`a,���`a ���bmfc0.5���`a]���`a,���`a
���`u                     ���`a[���aoa-���bmfc0.2���`a,���`a ���bmfc0.5���`a]���`a]���`a
���`bmu���`a ���aoa=���`a ���bmia2���`a,���`a ���aoa-���bmia3���`a
���`escale���`a ���aoa=���`a ���bmia6���`a,���`a ���bmia5���`a
���`a
���`iax_kwargs���aoa.���`gaxvline���`a(���`ac���aoa=���bs1a'���bs1dgrey���bs1a'���`a,���`a ���`blw���aoa=���bmia1���`a)���`a
���`iax_kwargs���aoa.���`gaxhline���`a(���`ac���aoa=���bs1a'���bs1dgrey���bs1a'���`a,���`a ���`blw���aoa=���bmia1���`a)���`a
���`a
���`ax���`a,���`a ���`ay���`a ���aoa=���`a ���`vget_correlated_dataset���`a(���bmic500���`a,���`a ���`qdependency_kwargs���`a,���`a ���`bmu���`a,���`a ���`escale���`a)���`a
���bc1x8# Plot the ellipse with zorder=0 in order to demonstrate���`a
���bc1x0# its transparency (caused by the use of alpha).���`a
���`rconfidence_ellipse���`a(���`ax���`a,���`a ���`ay���`a,���`a ���`iax_kwargs���`a,���`a
���`s                   ���`ealpha���aoa=���bmfc0.5���`a,���`a ���`ifacecolor���aoa=���bs1a'���bs1dpink���bs1a'���`a,���`a ���`iedgecolor���aoa=���bs1a'���bs1fpurple���bs1a'���`a,���`a ���`fzorder���aoa=���bmia0���`a)���`a
���`a
���`iax_kwargs���aoa.���`gscatter���`a(���`ax���`a,���`a ���`ay���`a,���`a ���`as���aoa=���bmfc0.5���`a)���`a
���`iax_kwargs���aoa.���`gscatter���`a(���`bmu���`a[���bmia0���`a]���`a,���`a ���`bmu���`a[���bmia1���`a]���`a,���`a ���`ac���aoa=���bs1a'���bs1cred���bs1a'���`a,���`a ���`as���aoa=���bmia3���`a)���`a
���`iax_kwargs���aoa.���`iset_title���`a(���bs1a'���bs1wUsing keyword arguments���bs1a'���`a)���`a
���`a
���`cfig���aoa.���`osubplots_adjust���`a(���`fhspace���aoa=���bmfd0.25���`a)���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
���`a
���bc1xM#############################################################################���`a
���bc1a#���`a
���bc1x# .. admonition:: References���`a
���bc1a#���`a
���bc1xN#    The use of the following functions, methods, classes and modules is shown���`a
���bc1u#    in this example:���`a
���bc1a#���`a
���bc1x'#    - `matplotlib.transforms.Affine2D`���`a
���bc1x##    - `matplotlib.patches.Ellipse`���`a
`dNone�