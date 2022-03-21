������������bsdy�"""
==============
Secondary Axis
==============

Sometimes we want a secondary axis on a plot, for instance to convert
radians to degrees on the same plot.  We can do this by making a child
axes with only one axis visible via `.axes.Axes.secondary_xaxis` and
`.axes.Axes.secondary_yaxis`.  This secondary axis can have a different scale
than the main axis by providing both a forward and an inverse conversion
function in a tuple to the *functions* keyword argument:
"""���`a
���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���bknfimport���`a ���bnnhdatetime���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnedates���`a ���akbas���`a ���bnnfmdates���`a
���bkndfrom���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfticker���`a ���bknfimport���`a ���`pAutoMinorLocator���`a
���`a
���`cfig���`a,���`a ���`bax���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`rconstrained_layout���aoa=���bkcdTrue���`a)���`a
���`ax���`a ���aoa=���`a ���`bnp���aoa.���`farange���`a(���bmia0���`a,���`a ���bmic360���`a,���`a ���bmia1���`a)���`a
���`ay���`a ���aoa=���`a ���`bnp���aoa.���`csin���`a(���bmia2���`a ���aoa*���`a ���`ax���`a ���aoa*���`a ���`bnp���aoa.���`bpi���`a ���aoa/���`a ���bmic180���`a)���`a
���`bax���aoa.���`dplot���`a(���`ax���`a,���`a ���`ay���`a)���`a
���`bax���aoa.���`jset_xlabel���`a(���bs1a'���bs1oangle [degrees]���bs1a'���`a)���`a
���`bax���aoa.���`jset_ylabel���`a(���bs1a'���bs1fsignal���bs1a'���`a)���`a
���`bax���aoa.���`iset_title���`a(���bs1a'���bs1iSine wave���bs1a'���`a)���`a
���`a
���`a
���akcdef���`a ���bnfgdeg2rad���`a(���`ax���`a)���`a:���`a
���`d    ���akfreturn���`a ���`ax���`a ���aoa*���`a ���`bnp���aoa.���`bpi���`a ���aoa/���`a ���bmic180���`a
���`a
���`a
���akcdef���`a ���bnfgrad2deg���`a(���`ax���`a)���`a:���`a
���`d    ���akfreturn���`a ���`ax���`a ���aoa*���`a ���bmic180���`a ���aoa/���`a ���`bnp���aoa.���`bpi���`a
���`a
���`a
���`esecax���`a ���aoa=���`a ���`bax���aoa.���`osecondary_xaxis���`a(���bs1a'���bs1ctop���bs1a'���`a,���`a ���`ifunctions���aoa=���`a(���`gdeg2rad���`a,���`a ���`grad2deg���`a)���`a)���`a
���`esecax���aoa.���`jset_xlabel���`a(���bs1a'���bs1kangle [rad]���bs1a'���`a)���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
���`a
���bc1xK###########################################################################���`a
���bc1xC# Here is the case of converting from wavenumber to wavelength in a���`a
���bc1p# log-log scale.���`a
���bc1a#���`a
���bc1k# .. note::���`a
���bc1a#���`a
���bc1xJ#   In this case, the xscale of the parent is logarithmic, so the child is���`a
���bc1x#   made logarithmic as well.���`a
���`a
���`cfig���`a,���`a ���`bax���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`rconstrained_layout���aoa=���bkcdTrue���`a)���`a
���`ax���`a ���aoa=���`a ���`bnp���aoa.���`farange���`a(���bmfd0.02���`a,���`a ���bmia1���`a,���`a ���bmfd0.02���`a)���`a
���`bnp���aoa.���`frandom���aoa.���`dseed���`a(���bmih19680801���`a)���`a
���`ay���`a ���aoa=���`a ���`bnp���aoa.���`frandom���aoa.���`erandn���`a(���bnbclen���`a(���`ax���`a)���`a)���`a ���aoa*���aoa*���`a ���bmia2���`a
���`bax���aoa.���`floglog���`a(���`ax���`a,���`a ���`ay���`a)���`a
���`bax���aoa.���`jset_xlabel���`a(���bs1a'���bs1ff [Hz]���bs1a'���`a)���`a
���`bax���aoa.���`jset_ylabel���`a(���bs1a'���bs1cPSD���bs1a'���`a)���`a
���`bax���aoa.���`iset_title���`a(���bs1a'���bs1oRandom spectrum���bs1a'���`a)���`a
���`a
���`a
���akcdef���`a ���bnfhone_over���`a(���`ax���`a)���`a:���`a
���`d    ���bsdx,"""Vectorized 1/x, treating x==0 manually"""���`a
���`d    ���`ax���`a ���aoa=���`a ���`bnp���aoa.���`earray���`a(���`ax���`a)���aoa.���`fastype���`a(���bnbefloat���`a)���`a
���`d    ���`inear_zero���`a ���aoa=���`a ���`bnp���aoa.���`gisclose���`a(���`ax���`a,���`a ���bmia0���`a)���`a
���`d    ���`ax���`a[���`inear_zero���`a]���`a ���aoa=���`a ���`bnp���aoa.���`cinf���`a
���`d    ���`ax���`a[���aoa~���`inear_zero���`a]���`a ���aoa=���`a ���bmia1���`a ���aoa/���`a ���`ax���`a[���aoa~���`inear_zero���`a]���`a
���`d    ���akfreturn���`a ���`ax���`a
���`a
���`a
���bc1x'# the function "1/x" is its own inverse���`a
���`ginverse���`a ���aoa=���`a ���`hone_over���`a
���`a
���`a
���`esecax���`a ���aoa=���`a ���`bax���aoa.���`osecondary_xaxis���`a(���bs1a'���bs1ctop���bs1a'���`a,���`a ���`ifunctions���aoa=���`a(���`hone_over���`a,���`a ���`ginverse���`a)���`a)���`a
���`esecax���aoa.���`jset_xlabel���`a(���bs1a'���bs1jperiod [s]���bs1a'���`a)���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
���`a
���bc1xK###########################################################################���`a
���bc1xH# Sometime we want to relate the axes in a transform that is ad-hoc from���`a
���bc1xD# the data, and is derived empirically.  In that case we can set the���`a
���bc1xO# forward and inverse transforms functions to be linear interpolations from the���`a
���bc1x# one data set to the other.���`a
���bc1a#���`a
���bc1k# .. note::���`a
���bc1a#���`a
���bc1xG#   In order to properly handle the data margins, the mapping functions���`a
���bc1xO#   (``forward`` and ``inverse`` in this example) need to be defined beyond the���`a
���bc1x#   nominal plot limits.���`a
���bc1a#���`a
���bc1xK#   In the specific case of the numpy linear interpolation, `numpy.interp`,���`a
���bc1xL#   this condition can be arbitrarily enforced by providing optional keyword���`a
���bc1xI#   arguments *left*, *right* such that values outside the data range are���`a
���bc1x(#   mapped well outside the plot limits.���`a
���`a
���`cfig���`a,���`a ���`bax���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`rconstrained_layout���aoa=���bkcdTrue���`a)���`a
���`exdata���`a ���aoa=���`a ���`bnp���aoa.���`farange���`a(���bmia1���`a,���`a ���bmib11���`a,���`a ���bmfc0.4���`a)���`a
���`eydata���`a ���aoa=���`a ���`bnp���aoa.���`frandom���aoa.���`erandn���`a(���bnbclen���`a(���`exdata���`a)���`a)���`a
���`bax���aoa.���`dplot���`a(���`exdata���`a,���`a ���`eydata���`a,���`a ���`elabel���aoa=���bs1a'���bs1lPlotted data���bs1a'���`a)���`a
���`a
���`dxold���`a ���aoa=���`a ���`bnp���aoa.���`farange���`a(���bmia0���`a,���`a ���bmib11���`a,���`a ���bmfc0.2���`a)���`a
���bc1xI# fake data set relating x coordinate to another data-derived coordinate.���`a
���bc1x'# xnew must be monotonic, so we sort...���`a
���`dxnew���`a ���aoa=���`a ���`bnp���aoa.���`dsort���`a(���bmib10���`a ���aoa*���`a ���`bnp���aoa.���`cexp���`a(���aoa-���`dxold���`a ���aoa/���`a ���bmia4���`a)���`a ���aoa+���`a ���`bnp���aoa.���`frandom���aoa.���`erandn���`a(���bnbclen���`a(���`dxold���`a)���`a)���`a ���aoa/���`a ���bmia3���`a)���`a
���`a
���`bax���aoa.���`dplot���`a(���`dxold���`a[���bmia3���`a:���`a]���`a,���`a ���`dxnew���`a[���bmia3���`a:���`a]���`a,���`a ���`elabel���aoa=���bs1a'���bs1nTransform data���bs1a'���`a)���`a
���`bax���aoa.���`jset_xlabel���`a(���bs1a'���bs1eX [m]���bs1a'���`a)���`a
���`bax���aoa.���`flegend���`a(���`a)���`a
���`a
���`a
���akcdef���`a ���bnfgforward���`a(���`ax���`a)���`a:���`a
���`d    ���akfreturn���`a ���`bnp���aoa.���`finterp���`a(���`ax���`a,���`a ���`dxold���`a,���`a ���`dxnew���`a)���`a
���`a
���`a
���akcdef���`a ���bnfginverse���`a(���`ax���`a)���`a:���`a
���`d    ���akfreturn���`a ���`bnp���aoa.���`finterp���`a(���`ax���`a,���`a ���`dxnew���`a,���`a ���`dxold���`a)���`a
���`a
���`a
���`esecax���`a ���aoa=���`a ���`bax���aoa.���`osecondary_xaxis���`a(���bs1a'���bs1ctop���bs1a'���`a,���`a ���`ifunctions���aoa=���`a(���`gforward���`a,���`a ���`ginverse���`a)���`a)���`a
���`esecax���aoa.���`exaxis���aoa.���`qset_minor_locator���`a(���`pAutoMinorLocator���`a(���`a)���`a)���`a
���`esecax���aoa.���`jset_xlabel���`a(���bs1a'���bs1c$X_���bsig{other}���bs1a$���bs1a'���`a)���`a
���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
���`a
���bc1xK###########################################################################���`a
���bc1xG# A final example translates np.datetime64 to yearday on the x axis and���`a
���bc1xC# from Celsius to Fahrenheit on the y axis.  Note the addition of a���`a
���bc1x?# third y axis, and that it can be placed using a float for the���`a
���bc1s# location argument���`a
���`a
���`edates���`a ���aoa=���`a ���`a[���`hdatetime���aoa.���`hdatetime���`a(���bmid2018���`a,���`a ���bmia1���`a,���`a ���bmia1���`a)���`a ���aoa+���`a ���`hdatetime���aoa.���`itimedelta���`a(���`ehours���aoa=���`ak���`a ���aoa*���`a ���bmia6���`a)���`a
���`i         ���akcfor���`a ���`ak���`a ���bowbin���`a ���bnberange���`a(���bmic240���`a)���`a]���`a
���`ktemperature���`a ���aoa=���`a ���`bnp���aoa.���`frandom���aoa.���`erandn���`a(���bnbclen���`a(���`edates���`a)���`a)���`a ���aoa*���`a ���bmia4���`a ���aoa+���`a ���bmfc6.7���`a
���`cfig���`a,���`a ���`bax���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`rconstrained_layout���aoa=���bkcdTrue���`a)���`a
���`a
���`bax���aoa.���`dplot���`a(���`edates���`a,���`a ���`ktemperature���`a)���`a
���`bax���aoa.���`jset_ylabel���`a(���bsaar���bs1a'���bs1b$T���bs1a\���bs1g [^oC]$���bs1a'���`a)���`a
���`cplt���aoa.���`fxticks���`a(���`hrotation���aoa=���bmib70���`a)���`a
���`a
���`a
���akcdef���`a ���bnfidate2yday���`a(���`ax���`a)���`a:���`a
���`d    ���bsdx:"""Convert matplotlib datenum to days since 2018-01-01."""���`a
���`d    ���`ay���`a ���aoa=���`a ���`ax���`a ���aoa-���`a ���`fmdates���aoa.���`hdate2num���`a(���`hdatetime���aoa.���`hdatetime���`a(���bmid2018���`a,���`a ���bmia1���`a,���`a ���bmia1���`a)���`a)���`a
���`d    ���akfreturn���`a ���`ay���`a
���`a
���`a
���akcdef���`a ���bnfiyday2date���`a(���`ax���`a)���`a:���`a
���`d    ���bsdx@"""Return a matplotlib datenum for *x* days after 2018-01-01."""���`a
���`d    ���`ay���`a ���aoa=���`a ���`ax���`a ���aoa+���`a ���`fmdates���aoa.���`hdate2num���`a(���`hdatetime���aoa.���`hdatetime���`a(���bmid2018���`a,���`a ���bmia1���`a,���`a ���bmia1���`a)���`a)���`a
���`d    ���akfreturn���`a ���`ay���`a
���`a
���`a
���`gsecax_x���`a ���aoa=���`a ���`bax���aoa.���`osecondary_xaxis���`a(���bs1a'���bs1ctop���bs1a'���`a,���`a ���`ifunctions���aoa=���`a(���`idate2yday���`a,���`a ���`iyday2date���`a)���`a)���`a
���`gsecax_x���aoa.���`jset_xlabel���`a(���bs1a'���bs1kyday [2018]���bs1a'���`a)���`a
���`a
���`a
���akcdef���`a ���bnfucelsius_to_fahrenheit���`a(���`ax���`a)���`a:���`a
���`d    ���akfreturn���`a ���`ax���`a ���aoa*���`a ���bmfc1.8���`a ���aoa+���`a ���bmib32���`a
���`a
���`a
���akcdef���`a ���bnfufahrenheit_to_celsius���`a(���`ax���`a)���`a:���`a
���`d    ���akfreturn���`a ���`a(���`ax���`a ���aoa-���`a ���bmib32���`a)���`a ���aoa/���`a ���bmfc1.8���`a
���`a
���`a
���`gsecax_y���`a ���aoa=���`a ���`bax���aoa.���`osecondary_yaxis���`a(���`a
���`d    ���bs1a'���bs1eright���bs1a'���`a,���`a ���`ifunctions���aoa=���`a(���`ucelsius_to_fahrenheit���`a,���`a ���`ufahrenheit_to_celsius���`a)���`a)���`a
���`gsecax_y���aoa.���`jset_ylabel���`a(���bsaar���bs1a'���bs1b$T���bs1a\���bs1g [^oF]$���bs1a'���`a)���`a
���`a
���`a
���akcdef���`a ���bnfrcelsius_to_anomaly���`a(���`ax���`a)���`a:���`a
���`d    ���akfreturn���`a ���`a(���`ax���`a ���aoa-���`a ���`bnp���aoa.���`dmean���`a(���`ktemperature���`a)���`a)���`a
���`a
���`a
���akcdef���`a ���bnfranomaly_to_celsius���`a(���`ax���`a)���`a:���`a
���`d    ���akfreturn���`a ���`a(���`ax���`a ���aoa+���`a ���`bnp���aoa.���`dmean���`a(���`ktemperature���`a)���`a)���`a
���`a
���`a
���bc1x"# use of a float for the position:���`a
���`hsecax_y2���`a ���aoa=���`a ���`bax���aoa.���`osecondary_yaxis���`a(���`a
���`d    ���bmfc1.2���`a,���`a ���`ifunctions���aoa=���`a(���`rcelsius_to_anomaly���`a,���`a ���`ranomaly_to_celsius���`a)���`a)���`a
���`hsecax_y2���aoa.���`jset_ylabel���`a(���bsaar���bs1a'���bs1e$T - ���bs1a\���bs1hoverline���bsic{T}���bs1a\���bs1g [^oC]$���bs1a'���`a)���`a
���`a
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
���bc1x-#    - `matplotlib.axes.Axes.secondary_xaxis`���`a
���bc1x-#    - `matplotlib.axes.Axes.secondary_yaxis`���`a
`dNone�