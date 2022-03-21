������������bsdyn"""
=====================
Curvilinear grid demo
=====================

Custom grid and ticklines.

This example demonstrates how to use
`~.grid_helper_curvelinear.GridHelperCurveLinear` to define custom grids and
ticklines by applying a transformation on the grid.  This can be used, as
shown on the second plot, to create polar projections in a rectangular box.
"""���`a
���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���bkndfrom���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnkprojections���`a ���bknfimport���`a ���`iPolarAxes���`a
���bkndfrom���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnjtransforms���`a ���bknfimport���`a ���`hAffine2D���`a
���`a
���bkndfrom���`a ���bnnlmpl_toolkits���bnna.���bnnjaxisartist���`a ���bknfimport���`a ���`langle_helper���`a,���`a ���`dAxes���`a,���`a ���`hHostAxes���`a
���bkndfrom���`a ���bnnlmpl_toolkits���bnna.���bnnjaxisartist���bnna.���bnnwgrid_helper_curvelinear���`a ���bknfimport���`a ���`a(���`a
���`d    ���`uGridHelperCurveLinear���`a)���`a
���`a
���`a
���akcdef���`a ���bnfqcurvelinear_test1���`a(���`cfig���`a)���`a:���`a
���`d    ���bsdx*"""
    Grid for custom transform.
    """���`a
���`a
���`d    ���akcdef���`a ���bnfbtr���`a(���`ax���`a,���`a ���`ay���`a)���`a:���`a ���akfreturn���`a ���`ax���`a,���`a ���`ay���`a ���aoa-���`a ���`ax���`a
���`d    ���akcdef���`a ���bnffinv_tr���`a(���`ax���`a,���`a ���`ay���`a)���`a:���`a ���akfreturn���`a ���`ax���`a,���`a ���`ay���`a ���aoa+���`a ���`ax���`a
���`a
���`d    ���`kgrid_helper���`a ���aoa=���`a ���`uGridHelperCurveLinear���`a(���`a(���`btr���`a,���`a ���`finv_tr���`a)���`a)���`a
���`a
���`d    ���`cax1���`a ���aoa=���`a ���`cfig���aoa.���`kadd_subplot���`a(���bmia1���`a,���`a ���bmia2���`a,���`a ���bmia1���`a,���`a ���`jaxes_class���aoa=���`dAxes���`a,���`a ���`kgrid_helper���aoa=���`kgrid_helper���`a)���`a
���`d    ���bc1xE# ax1 will have ticks and gridlines defined by the given transform (+���`a
���`d    ���bc1xE# transData of the Axes).  Note that the transform of the Axes itself���`a
���`d    ���bc1x;# (i.e., transData) is not affected by the given transform.���`a
���`d    ���`bxx���`a,���`a ���`byy���`a ���aoa=���`a ���`btr���`a(���`bnp���aoa.���`earray���`a(���`a[���bmia3���`a,���`a ���bmia6���`a]���`a)���`a,���`a ���`bnp���aoa.���`earray���`a(���`a[���bmia5���`a,���`a ���bmib10���`a]���`a)���`a)���`a
���`d    ���`cax1���aoa.���`dplot���`a(���`bxx���`a,���`a ���`byy���`a)���`a
���`a
���`d    ���`cax1���aoa.���`jset_aspect���`a(���bmia1���`a)���`a
���`d    ���`cax1���aoa.���`hset_xlim���`a(���bmia0���`a,���`a ���bmib10���`a)���`a
���`d    ���`cax1���aoa.���`hset_ylim���`a(���bmia0���`a,���`a ���bmib10���`a)���`a
���`a
���`d    ���`cax1���aoa.���`daxis���`a[���bs2a"���bs2at���bs2a"���`a]���`a ���aoa=���`a ���`cax1���aoa.���`qnew_floating_axis���`a(���bmia0���`a,���`a ���bmia3���`a)���`a
���`d    ���`cax1���aoa.���`daxis���`a[���bs2a"���bs2bt2���bs2a"���`a]���`a ���aoa=���`a ���`cax1���aoa.���`qnew_floating_axis���`a(���bmia1���`a,���`a ���bmia7���`a)���`a
���`d    ���`cax1���aoa.���`dgrid���`a(���bkcdTrue���`a,���`a ���`fzorder���aoa=���bmia0���`a)���`a
���`a
���`a
���akcdef���`a ���bnfqcurvelinear_test2���`a(���`cfig���`a)���`a:���`a
���`d    ���bsdx;"""
    Polar projection, but in a rectangular box.
    """���`a
���`a
���`d    ���bc1xH# PolarAxes.PolarTransform takes radian. However, we want our coordinate���`a
���`d    ���bc1r# system in degree���`a
���`d    ���`btr���`a ���aoa=���`a ���`hAffine2D���`a(���`a)���aoa.���`escale���`a(���`bnp���aoa.���`bpi���aoa/���bmic180���`a,���`a ���bmia1���`a)���`a ���aoa+���`a ���`iPolarAxes���aoa.���`nPolarTransform���`a(���`a)���`a
���`d    ���bc1x@# Polar projection, which involves cycle, and also has limits in���`a
���`d    ���bc1x># its coordinates, needs a special method to find the extremes���`a
���`d    ���bc1x/# (min, max of the coordinate within the view).���`a
���`d    ���`nextreme_finder���`a ���aoa=���`a ���`langle_helper���aoa.���`rExtremeFinderCycle���`a(���`a
���`h        ���`bnx���aoa=���bmib20���`a,���`a ���`bny���aoa=���bmib20���`a,���`b  ���bc1x.# Number of sampling points in each direction.���`a
���`h        ���`ilon_cycle���aoa=���bmic360���`a,���`a ���`ilat_cycle���aoa=���bkcdNone���`a,���`a
���`h        ���`jlon_minmax���aoa=���bkcdNone���`a,���`a ���`jlat_minmax���aoa=���`a(���bmia0���`a,���`a ���`bnp���aoa.���`cinf���`a)���`a,���`a
���`d    ���`a)���`a
���`d    ���bc1xK# Find grid values appropriate for the coordinate (degree, minute, second).���`a
���`d    ���`mgrid_locator1���`a ���aoa=���`a ���`langle_helper���aoa.���`jLocatorDMS���`a(���bmib12���`a)���`a
���`d    ���bc1xE# Use an appropriate formatter.  Note that the acceptable Locator and���`a
���`d    ���bc1xF# Formatter classes are a bit different than that of Matplotlib, which���`a
���`d    ���bc1xD# cannot directly be used here (this may be possible in the future).���`a
���`d    ���`otick_formatter1���`a ���aoa=���`a ���`langle_helper���aoa.���`lFormatterDMS���`a(���`a)���`a
���`a
���`d    ���`kgrid_helper���`a ���aoa=���`a ���`uGridHelperCurveLinear���`a(���`a
���`h        ���`btr���`a,���`a ���`nextreme_finder���aoa=���`nextreme_finder���`a,���`a
���`h        ���`mgrid_locator1���aoa=���`mgrid_locator1���`a,���`a ���`otick_formatter1���aoa=���`otick_formatter1���`a)���`a
���`d    ���`cax1���`a ���aoa=���`a ���`cfig���aoa.���`kadd_subplot���`a(���`a
���`h        ���bmia1���`a,���`a ���bmia2���`a,���`a ���bmia2���`a,���`a ���`jaxes_class���aoa=���`hHostAxes���`a,���`a ���`kgrid_helper���aoa=���`kgrid_helper���`a)���`a
���`a
���`d    ���bc1x0# make ticklabels of right and top axis visible.���`a
���`d    ���`cax1���aoa.���`daxis���`a[���bs2a"���bs2eright���bs2a"���`a]���aoa.���`pmajor_ticklabels���aoa.���`kset_visible���`a(���bkcdTrue���`a)���`a
���`d    ���`cax1���aoa.���`daxis���`a[���bs2a"���bs2ctop���bs2a"���`a]���aoa.���`pmajor_ticklabels���aoa.���`kset_visible���`a(���bkcdTrue���`a)���`a
���`d    ���bc1x<# let right axis shows ticklabels for 1st coordinate (angle)���`a
���`d    ���`cax1���aoa.���`daxis���`a[���bs2a"���bs2eright���bs2a"���`a]���aoa.���`jget_helper���`a(���`a)���aoa.���`onth_coord_ticks���`a ���aoa=���`a ���bmia0���`a
���`d    ���bc1x># let bottom axis shows ticklabels for 2nd coordinate (radius)���`a
���`d    ���`cax1���aoa.���`daxis���`a[���bs2a"���bs2fbottom���bs2a"���`a]���aoa.���`jget_helper���`a(���`a)���aoa.���`onth_coord_ticks���`a ���aoa=���`a ���bmia1���`a
���`a
���`d    ���`cax1���aoa.���`jset_aspect���`a(���bmia1���`a)���`a
���`d    ���`cax1���aoa.���`hset_xlim���`a(���aoa-���bmia5���`a,���`a ���bmib12���`a)���`a
���`d    ���`cax1���aoa.���`hset_ylim���`a(���aoa-���bmia5���`a,���`a ���bmib10���`a)���`a
���`a
���`d    ���`cax1���aoa.���`dgrid���`a(���bkcdTrue���`a,���`a ���`fzorder���aoa=���bmia0���`a)���`a
���`a
���`d    ���bc1x&# A parasite axes with given transform���`a
���`d    ���`cax2���`a ���aoa=���`a ���`cax1���aoa.���`lget_aux_axes���`a(���`btr���`a)���`a
���`d    ���bc1x/# note that ax2.transData == tr + ax1.transData���`a
���`d    ���bc1xA# Anything you draw in ax2 will match the ticks and grids of ax1.���`a
���`d    ���`cax1���aoa.���`iparasites���aoa.���`fappend���`a(���`cax2���`a)���`a
���`d    ���`cax2���aoa.���`dplot���`a(���`bnp���aoa.���`hlinspace���`a(���bmia0���`a,���`a ���bmib30���`a,���`a ���bmib51���`a)���`a,���`a ���`bnp���aoa.���`hlinspace���`a(���bmib10���`a,���`a ���bmib10���`a,���`a ���bmib51���`a)���`a,���`a ���`ilinewidth���aoa=���bmia2���`a)���`a
���`a
���`d    ���`cax2���aoa.���`fpcolor���`a(���`bnp���aoa.���`hlinspace���`a(���bmia0���`a,���`a ���bmib90���`a,���`a ���bmia4���`a)���`a,���`a ���`bnp���aoa.���`hlinspace���`a(���bmia0���`a,���`a ���bmib10���`a,���`a ���bmia4���`a)���`a,���`a
���`o               ���`bnp���aoa.���`farange���`a(���bmia9���`a)���aoa.���`greshape���`a(���`a(���bmia3���`a,���`a ���bmia3���`a)���`a)���`a)���`a
���`d    ���`cax2���aoa.���`gcontour���`a(���`bnp���aoa.���`hlinspace���`a(���bmia0���`a,���`a ���bmib90���`a,���`a ���bmia4���`a)���`a,���`a ���`bnp���aoa.���`hlinspace���`a(���bmia0���`a,���`a ���bmib10���`a,���`a ���bmia4���`a)���`a,���`a
���`p                ���`bnp���aoa.���`farange���`a(���bmib16���`a)���aoa.���`greshape���`a(���`a(���bmia4���`a,���`a ���bmia4���`a)���`a)���`a,���`a ���`fcolors���aoa=���bs2a"���bs2ak���bs2a"���`a)���`a
���`a
���`a
���akbif���`a ���bvmh__name__���`a ���aob==���`a ���bs2a"���bs2h__main__���bs2a"���`a:���`a
���`d    ���`cfig���`a ���aoa=���`a ���`cplt���aoa.���`ffigure���`a(���`gfigsize���aoa=���`a(���bmia7���`a,���`a ���bmia4���`a)���`a)���`a
���`a
���`d    ���`qcurvelinear_test1���`a(���`cfig���`a)���`a
���`d    ���`qcurvelinear_test2���`a(���`cfig���`a)���`a
���`a
���`d    ���`cplt���aoa.���`dshow���`a(���`a)���`a
`dNone�