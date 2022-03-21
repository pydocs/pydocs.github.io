�����������bsdy�"""
==================
Anscombe's quartet
==================

`Anscombe's quartet`_ is a group of datasets (x, y) that have the same mean,
standard deviation, and regression line, but which are qualitatively different.

It is often used to illustrate the importance of looking at a set of data
graphically and not only relying on basic statistic properties.

.. _Anscombe's quartet: https://en.wikipedia.org/wiki/Anscombe%27s_quartet
"""���`a
���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���`a
���`ax���`a ���aoa=���`a ���`a[���bmib10���`a,���`a ���bmia8���`a,���`a ���bmib13���`a,���`a ���bmia9���`a,���`a ���bmib11���`a,���`a ���bmib14���`a,���`a ���bmia6���`a,���`a ���bmia4���`a,���`a ���bmib12���`a,���`a ���bmia7���`a,���`a ���bmia5���`a]���`a
���`by1���`a ���aoa=���`a ���`a[���bmfd8.04���`a,���`a ���bmfd6.95���`a,���`a ���bmfd7.58���`a,���`a ���bmfd8.81���`a,���`a ���bmfd8.33���`a,���`a ���bmfd9.96���`a,���`a ���bmfd7.24���`a,���`a ���bmfd4.26���`a,���`a ���bmfe10.84���`a,���`a ���bmfd4.82���`a,���`a ���bmfd5.68���`a]���`a
���`by2���`a ���aoa=���`a ���`a[���bmfd9.14���`a,���`a ���bmfd8.14���`a,���`a ���bmfd8.74���`a,���`a ���bmfd8.77���`a,���`a ���bmfd9.26���`a,���`a ���bmfd8.10���`a,���`a ���bmfd6.13���`a,���`a ���bmfd3.10���`a,���`a ���bmfd9.13���`a,���`a ���bmfd7.26���`a,���`a ���bmfd4.74���`a]���`a
���`by3���`a ���aoa=���`a ���`a[���bmfd7.46���`a,���`a ���bmfd6.77���`a,���`a ���bmfe12.74���`a,���`a ���bmfd7.11���`a,���`a ���bmfd7.81���`a,���`a ���bmfd8.84���`a,���`a ���bmfd6.08���`a,���`a ���bmfd5.39���`a,���`a ���bmfd8.15���`a,���`a ���bmfd6.42���`a,���`a ���bmfd5.73���`a]���`a
���`bx4���`a ���aoa=���`a ���`a[���bmia8���`a,���`a ���bmia8���`a,���`a ���bmia8���`a,���`a ���bmia8���`a,���`a ���bmia8���`a,���`a ���bmia8���`a,���`a ���bmia8���`a,���`a ���bmib19���`a,���`a ���bmia8���`a,���`a ���bmia8���`a,���`a ���bmia8���`a]���`a
���`by4���`a ���aoa=���`a ���`a[���bmfd6.58���`a,���`a ���bmfd5.76���`a,���`a ���bmfd7.71���`a,���`a ���bmfd8.84���`a,���`a ���bmfd8.47���`a,���`a ���bmfd7.04���`a,���`a ���bmfd5.25���`a,���`a ���bmfe12.50���`a,���`a ���bmfd5.56���`a,���`a ���bmfd7.91���`a,���`a ���bmfd6.89���`a]���`a
���`a
���`hdatasets���`a ���aoa=���`a ���`a{���`a
���`d    ���bs1a'���bs1aI���bs1a'���`a:���`a ���`a(���`ax���`a,���`a ���`by1���`a)���`a,���`a
���`d    ���bs1a'���bs1bII���bs1a'���`a:���`a ���`a(���`ax���`a,���`a ���`by2���`a)���`a,���`a
���`d    ���bs1a'���bs1cIII���bs1a'���`a:���`a ���`a(���`ax���`a,���`a ���`by3���`a)���`a,���`a
���`d    ���bs1a'���bs1bIV���bs1a'���`a:���`a ���`a(���`bx4���`a,���`a ���`by4���`a)���`a
���`a}���`a
���`a
���`cfig���`a,���`a ���`caxs���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���bmia2���`a,���`a ���bmia2���`a,���`a ���`fsharex���aoa=���bkcdTrue���`a,���`a ���`fsharey���aoa=���bkcdTrue���`a,���`a ���`gfigsize���aoa=���`a(���bmia6���`a,���`a ���bmia6���`a)���`a,���`a
���`x                        ���`kgridspec_kw���aoa=���`a{���bs1a'���bs1fwspace���bs1a'���`a:���`a ���bmfd0.08���`a,���`a ���bs1a'���bs1fhspace���bs1a'���`a:���`a ���bmfd0.08���`a}���`a)���`a
���`caxs���`a[���bmia0���`a,���`a ���bmia0���`a]���aoa.���`cset���`a(���`dxlim���aoa=���`a(���bmia0���`a,���`a ���bmib20���`a)���`a,���`a ���`dylim���aoa=���`a(���bmia2���`a,���`a ���bmib14���`a)���`a)���`a
���`caxs���`a[���bmia0���`a,���`a ���bmia0���`a]���aoa.���`cset���`a(���`fxticks���aoa=���`a(���bmia0���`a,���`a ���bmib10���`a,���`a ���bmib20���`a)���`a,���`a ���`fyticks���aoa=���`a(���bmia4���`a,���`a ���bmia8���`a,���`a ���bmib12���`a)���`a)���`a
���`a
���akcfor���`a ���`bax���`a,���`a ���`a(���`elabel���`a,���`a ���`a(���`ax���`a,���`a ���`ay���`a)���`a)���`a ���bowbin���`a ���bnbczip���`a(���`caxs���aoa.���`dflat���`a,���`a ���`hdatasets���aoa.���`eitems���`a(���`a)���`a)���`a:���`a
���`d    ���`bax���aoa.���`dtext���`a(���bmfc0.1���`a,���`a ���bmfc0.9���`a,���`a ���`elabel���`a,���`a ���`hfontsize���aoa=���bmib20���`a,���`a ���`itransform���aoa=���`bax���aoa.���`itransAxes���`a,���`a ���`bva���aoa=���bs1a'���bs1ctop���bs1a'���`a)���`a
���`d    ���`bax���aoa.���`ktick_params���`a(���`idirection���aoa=���bs1a'���bs1bin���bs1a'���`a,���`a ���`ctop���aoa=���bkcdTrue���`a,���`a ���`eright���aoa=���bkcdTrue���`a)���`a
���`d    ���`bax���aoa.���`dplot���`a(���`ax���`a,���`a ���`ay���`a,���`a ���bs1a'���bs1ao���bs1a'���`a)���`a
���`a
���`d    ���bc1s# linear regression���`a
���`d    ���`bp1���`a,���`a ���`bp0���`a ���aoa=���`a ���`bnp���aoa.���`gpolyfit���`a(���`ax���`a,���`a ���`ay���`a,���`a ���`cdeg���aoa=���bmia1���`a)���`b  ���bc1r# slope, intercept���`a
���`d    ���`bax���aoa.���`faxline���`a(���`cxy1���aoa=���`a(���bmia0���`a,���`a ���`bp0���`a)���`a,���`a ���`eslope���aoa=���`bp1���`a,���`a ���`ecolor���aoa=���bs1a'���bs1ar���bs1a'���`a,���`a ���`blw���aoa=���bmia2���`a)���`a
���`a
���`d    ���bc1x!# add text box for the statistics���`a
���`d    ���`estats���`a ���aoa=���`a ���`a(���bsaaf���bs1a'���bs1a$���bseb\\���bs1fmu$ = ���bsia{���`bnp���aoa.���`dmean���`a(���`ay���`a)���bsia:���bs1c.2f���bsia}���bseb\n���bs1a'���`a
���`m             ���bsaaf���bs1a'���bs1a$���bseb\\���bs1isigma$ = ���bsia{���`bnp���aoa.���`cstd���`a(���`ay���`a)���bsia:���bs1c.2f���bsia}���bseb\n���bs1a'���`a
���`m             ���bsaaf���bs1a'���bs1f$r$ = ���bsia{���`bnp���aoa.���`hcorrcoef���`a(���`ax���`a,���`a ���`ay���`a)���`a[���bmia0���`a]���`a[���bmia1���`a]���bsia:���bs1c.2f���bsia}���bs1a'���`a)���`a
���`d    ���`dbbox���`a ���aoa=���`a ���bnbddict���`a(���`hboxstyle���aoa=���bs1a'���bs1eround���bs1a'���`a,���`a ���`bfc���aoa=���bs1a'���bs1nblanchedalmond���bs1a'���`a,���`a ���`bec���aoa=���bs1a'���bs1forange���bs1a'���`a,���`a ���`ealpha���aoa=���bmfc0.5���`a)���`a
���`d    ���`bax���aoa.���`dtext���`a(���bmfd0.95���`a,���`a ���bmfd0.07���`a,���`a ���`estats���`a,���`a ���`hfontsize���aoa=���bmia9���`a,���`a ���`dbbox���aoa=���`dbbox���`a,���`a
���`l            ���`itransform���aoa=���`bax���aoa.���`itransAxes���`a,���`a ���`shorizontalalignment���aoa=���bs1a'���bs1eright���bs1a'���`a)���`a
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
���bc1xA#    - `matplotlib.axes.Axes.axline` / `matplotlib.pyplot.axline`���`a
���bc1x=#    - `matplotlib.axes.Axes.text` / `matplotlib.pyplot.text`���`a
���bc1xJ#    - `matplotlib.axes.Axes.tick_params` / matplotlib.pyplot.tick_params`���`a
`dNone�