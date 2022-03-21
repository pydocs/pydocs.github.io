������������bsdyg"""
======================================
Radar chart (aka spider or star chart)
======================================

This example creates a radar chart, also known as a spider or star chart [1]_.

Although this example allows a frame of either 'circle' or 'polygon', polygon
frames don't have proper gridlines (the lines are circles instead of polygons).
It's possible to get a polygon grid by setting GRIDLINE_INTERPOLATION_STEPS in
matplotlib.axis to the desired number of vertices, but the orientation of the
polygon is not aligned with the radial axes.

.. [1] https://en.wikipedia.org/wiki/Radar_chart
"""���`a
���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���bkndfrom���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnngpatches���`a ���bknfimport���`a ���`fCircle���`a,���`a ���`nRegularPolygon���`a
���bkndfrom���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnndpath���`a ���bknfimport���`a ���`dPath���`a
���bkndfrom���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnkprojections���bnna.���bnnepolar���`a ���bknfimport���`a ���`iPolarAxes���`a
���bkndfrom���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnkprojections���`a ���bknfimport���`a ���`sregister_projection���`a
���bkndfrom���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfspines���`a ���bknfimport���`a ���`eSpine���`a
���bkndfrom���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnjtransforms���`a ���bknfimport���`a ���`hAffine2D���`a
���`a
���`a
���akcdef���`a ���bnfmradar_factory���`a(���`hnum_vars���`a,���`a ���`eframe���aoa=���bs1a'���bs1fcircle���bs1a'���`a)���`a:���`a
���`d    ���bsdy)"""
    Create a radar chart with `num_vars` axes.

    This function creates a RadarAxes projection and registers it.

    Parameters
    ----------
    num_vars : int
        Number of variables for radar chart.
    frame : {'circle', 'polygon'}
        Shape of frame surrounding axes.

    """���`a
���`d    ���bc1x%# calculate evenly-spaced axis angles���`a
���`d    ���`etheta���`a ���aoa=���`a ���`bnp���aoa.���`hlinspace���`a(���bmia0���`a,���`a ���bmia2���aoa*���`bnp���aoa.���`bpi���`a,���`a ���`hnum_vars���`a,���`a ���`hendpoint���aoa=���bkceFalse���`a)���`a
���`a
���`d    ���akeclass���`a ���bnciRadarAxes���`a(���`iPolarAxes���`a)���`a:���`a
���`a
���`h        ���`dname���`a ���aoa=���`a ���bs1a'���bs1eradar���bs1a'���`a
���`h        ���bc1x0# use 1 line segment to connect specified points���`a
���`h        ���`jRESOLUTION���`a ���aoa=���`a ���bmia1���`a
���`a
���`h        ���akcdef���`a ���bfmh__init__���`a(���bbpdself���`a,���`a ���aoa*���`dargs���`a,���`a ���aoa*���aoa*���`fkwargs���`a)���`a:���`a
���`l            ���bnbesuper���`a(���`a)���aoa.���bfmh__init__���`a(���aoa*���`dargs���`a,���`a ���aoa*���aoa*���`fkwargs���`a)���`a
���`l            ���bc1x4# rotate plot such that the first axis is at the top���`a
���`l            ���bbpdself���aoa.���`wset_theta_zero_location���`a(���bs1a'���bs1aN���bs1a'���`a)���`a
���`a
���`h        ���akcdef���`a ���bnfdfill���`a(���bbpdself���`a,���`a ���aoa*���`dargs���`a,���`a ���`fclosed���aoa=���bkcdTrue���`a,���`a ���aoa*���aoa*���`fkwargs���`a)���`a:���`a
���`l            ���bsdx5"""Override fill so that line is closed by default"""���`a
���`l            ���akfreturn���`a ���bnbesuper���`a(���`a)���aoa.���`dfill���`a(���`fclosed���aoa=���`fclosed���`a,���`a ���aoa*���`dargs���`a,���`a ���aoa*���aoa*���`fkwargs���`a)���`a
���`a
���`h        ���akcdef���`a ���bnfdplot���`a(���bbpdself���`a,���`a ���aoa*���`dargs���`a,���`a ���aoa*���aoa*���`fkwargs���`a)���`a:���`a
���`l            ���bsdx5"""Override plot so that line is closed by default"""���`a
���`l            ���`elines���`a ���aoa=���`a ���bnbesuper���`a(���`a)���aoa.���`dplot���`a(���aoa*���`dargs���`a,���`a ���aoa*���aoa*���`fkwargs���`a)���`a
���`l            ���akcfor���`a ���`dline���`a ���bowbin���`a ���`elines���`a:���`a
���`p                ���bbpdself���aoa.���`k_close_line���`a(���`dline���`a)���`a
���`a
���`h        ���akcdef���`a ���bnfk_close_line���`a(���bbpdself���`a,���`a ���`dline���`a)���`a:���`a
���`l            ���`ax���`a,���`a ���`ay���`a ���aoa=���`a ���`dline���aoa.���`hget_data���`a(���`a)���`a
���`l            ���bc1x-# FIXME: markers at x[0], y[0] get doubled-up���`a
���`l            ���akbif���`a ���`ax���`a[���bmia0���`a]���`a ���aob!=���`a ���`ax���`a[���aoa-���bmia1���`a]���`a:���`a
���`p                ���`ax���`a ���aoa=���`a ���`bnp���aoa.���`fappend���`a(���`ax���`a,���`a ���`ax���`a[���bmia0���`a]���`a)���`a
���`p                ���`ay���`a ���aoa=���`a ���`bnp���aoa.���`fappend���`a(���`ay���`a,���`a ���`ay���`a[���bmia0���`a]���`a)���`a
���`p                ���`dline���aoa.���`hset_data���`a(���`ax���`a,���`a ���`ay���`a)���`a
���`a
���`h        ���akcdef���`a ���bnfmset_varlabels���`a(���bbpdself���`a,���`a ���`flabels���`a)���`a:���`a
���`l            ���bbpdself���aoa.���`nset_thetagrids���`a(���`bnp���aoa.���`gdegrees���`a(���`etheta���`a)���`a,���`a ���`flabels���`a)���`a
���`a
���`h        ���akcdef���`a ���bnfo_gen_axes_patch���`a(���bbpdself���`a)���`a:���`a
���`l            ���bc1xA# The Axes patch must be centered at (0.5, 0.5) and of radius 0.5���`a
���`l            ���bc1v# in axes coordinates.���`a
���`l            ���akbif���`a ���`eframe���`a ���aob==���`a ���bs1a'���bs1fcircle���bs1a'���`a:���`a
���`p                ���akfreturn���`a ���`fCircle���`a(���`a(���bmfc0.5���`a,���`a ���bmfc0.5���`a)���`a,���`a ���bmfc0.5���`a)���`a
���`l            ���akdelif���`a ���`eframe���`a ���aob==���`a ���bs1a'���bs1gpolygon���bs1a'���`a:���`a
���`p                ���akfreturn���`a ���`nRegularPolygon���`a(���`a(���bmfc0.5���`a,���`a ���bmfc0.5���`a)���`a,���`a ���`hnum_vars���`a,���`a
���`x&                                      ���`fradius���aoa=���bmfb.5���`a,���`a ���`iedgecolor���aoa=���bs2a"���bs2ak���bs2a"���`a)���`a
���`l            ���akdelse���`a:���`a
���`p                ���akeraise���`a ���bnejValueError���`a(���bs2a"���bs2rUnknown value for ���bs2a'���bs2eframe���bs2a'���bs2b: ���bsib%s���bs2a"���`a ���aoa%���`a ���`eframe���`a)���`a
���`a
���`h        ���akcdef���`a ���bnfp_gen_axes_spines���`a(���bbpdself���`a)���`a:���`a
���`l            ���akbif���`a ���`eframe���`a ���aob==���`a ���bs1a'���bs1fcircle���bs1a'���`a:���`a
���`p                ���akfreturn���`a ���bnbesuper���`a(���`a)���aoa.���`p_gen_axes_spines���`a(���`a)���`a
���`l            ���akdelif���`a ���`eframe���`a ���aob==���`a ���bs1a'���bs1gpolygon���bs1a'���`a:���`a
���`p                ���bc1x<# spine_type must be 'left'/'right'/'top'/'bottom'/'circle'.���`a
���`p                ���`espine���`a ���aoa=���`a ���`eSpine���`a(���`daxes���aoa=���bbpdself���`a,���`a
���`x                              ���`jspine_type���aoa=���bs1a'���bs1fcircle���bs1a'���`a,���`a
���`x                              ���`dpath���aoa=���`dPath���aoa.���`tunit_regular_polygon���`a(���`hnum_vars���`a)���`a)���`a
���`p                ���bc1x># unit_regular_polygon gives a polygon of radius 1 centered at���`a
���`p                ���bc1x># (0, 0) but we want a polygon of radius 0.5 centered at (0.5,���`a
���`p                ���bc1x# 0.5) in axes coordinates.���`a
���`p                ���`espine���aoa.���`mset_transform���`a(���`hAffine2D���`a(���`a)���aoa.���`escale���`a(���bmfb.5���`a)���aoa.���`itranslate���`a(���bmfb.5���`a,���`a ���bmfb.5���`a)���`a
���`x$                                    ���aoa+���`a ���bbpdself���aoa.���`itransAxes���`a)���`a
���`p                ���akfreturn���`a ���`a{���bs1a'���bs1epolar���bs1a'���`a:���`a ���`espine���`a}���`a
���`l            ���akdelse���`a:���`a
���`p                ���akeraise���`a ���bnejValueError���`a(���bs2a"���bs2rUnknown value for ���bs2a'���bs2eframe���bs2a'���bs2b: ���bsib%s���bs2a"���`a ���aoa%���`a ���`eframe���`a)���`a
���`a
���`d    ���`sregister_projection���`a(���`iRadarAxes���`a)���`a
���`d    ���akfreturn���`a ���`etheta���`a
���`a
���`a
���akcdef���`a ���bnflexample_data���`a(���`a)���`a:���`a
���`d    ���bc1xI# The following data is from the Denver Aerosol Sources and Health study.���`a
���`d    ���bc1x(# See doi:10.1016/j.atmosenv.2008.12.017���`a
���`d    ���bc1a#���`a
���`d    ���bc1xB# The data are pollution source profile estimates for five modeled���`a
���`d    ���bc1xJ# pollution sources (e.g., cars, wood-burning, etc) that emit 7-9 chemical���`a
���`d    ���bc1xG# species. The radar charts are experimented with here to see if we can���`a
���`d    ���bc1xE# nicely visualize how the modeled source profiles change across four���`a
���`d    ���bc1l# scenarios:���`a
���`d    ���bc1xD#  1) No gas-phase species present, just seven particulate counts on���`a
���`d    ���bc1m#     Sulfate���`a
���`d    ���bc1m#     Nitrate���`a
���`d    ���bc1x#     Elemental Carbon (EC)���`a
���`d    ���bc1x$#     Organic Carbon fraction 1 (OC)���`a
���`d    ���bc1x%#     Organic Carbon fraction 2 (OC2)���`a
���`d    ���bc1x%#     Organic Carbon fraction 3 (OC3)���`a
���`d    ���bc1x##     Pyrolized Organic Carbon (OP)���`a
���`d    ���bc1x7#  2)Inclusion of gas-phase specie carbon monoxide (CO)���`a
���`d    ���bc1x.#  3)Inclusion of gas-phase specie ozone (O3).���`a
���`d    ���bc1x6#  4)Inclusion of both gas-phase species is present...���`a
���`d    ���`ddata���`a ���aoa=���`a ���`a[���`a
���`h        ���`a[���bs1a'���bs1gSulfate���bs1a'���`a,���`a ���bs1a'���bs1gNitrate���bs1a'���`a,���`a ���bs1a'���bs1bEC���bs1a'���`a,���`a ���bs1a'���bs1cOC1���bs1a'���`a,���`a ���bs1a'���bs1cOC2���bs1a'���`a,���`a ���bs1a'���bs1cOC3���bs1a'���`a,���`a ���bs1a'���bs1bOP���bs1a'���`a,���`a ���bs1a'���bs1bCO���bs1a'���`a,���`a ���bs1a'���bs1bO3���bs1a'���`a]���`a,���`a
���`h        ���`a(���bs1a'���bs1hBasecase���bs1a'���`a,���`a ���`a[���`a
���`l            ���`a[���bmfd0.88���`a,���`a ���bmfd0.01���`a,���`a ���bmfd0.03���`a,���`a ���bmfd0.03���`a,���`a ���bmfd0.00���`a,���`a ���bmfd0.06���`a,���`a ���bmfd0.01���`a,���`a ���bmfd0.00���`a,���`a ���bmfd0.00���`a]���`a,���`a
���`l            ���`a[���bmfd0.07���`a,���`a ���bmfd0.95���`a,���`a ���bmfd0.04���`a,���`a ���bmfd0.05���`a,���`a ���bmfd0.00���`a,���`a ���bmfd0.02���`a,���`a ���bmfd0.01���`a,���`a ���bmfd0.00���`a,���`a ���bmfd0.00���`a]���`a,���`a
���`l            ���`a[���bmfd0.01���`a,���`a ���bmfd0.02���`a,���`a ���bmfd0.85���`a,���`a ���bmfd0.19���`a,���`a ���bmfd0.05���`a,���`a ���bmfd0.10���`a,���`a ���bmfd0.00���`a,���`a ���bmfd0.00���`a,���`a ���bmfd0.00���`a]���`a,���`a
���`l            ���`a[���bmfd0.02���`a,���`a ���bmfd0.01���`a,���`a ���bmfd0.07���`a,���`a ���bmfd0.01���`a,���`a ���bmfd0.21���`a,���`a ���bmfd0.12���`a,���`a ���bmfd0.98���`a,���`a ���bmfd0.00���`a,���`a ���bmfd0.00���`a]���`a,���`a
���`l            ���`a[���bmfd0.01���`a,���`a ���bmfd0.01���`a,���`a ���bmfd0.02���`a,���`a ���bmfd0.71���`a,���`a ���bmfd0.74���`a,���`a ���bmfd0.70���`a,���`a ���bmfd0.00���`a,���`a ���bmfd0.00���`a,���`a ���bmfd0.00���`a]���`a]���`a)���`a,���`a
���`h        ���`a(���bs1a'���bs1gWith CO���bs1a'���`a,���`a ���`a[���`a
���`l            ���`a[���bmfd0.88���`a,���`a ���bmfd0.02���`a,���`a ���bmfd0.02���`a,���`a ���bmfd0.02���`a,���`a ���bmfd0.00���`a,���`a ���bmfd0.05���`a,���`a ���bmfd0.00���`a,���`a ���bmfd0.05���`a,���`a ���bmfd0.00���`a]���`a,���`a
���`l            ���`a[���bmfd0.08���`a,���`a ���bmfd0.94���`a,���`a ���bmfd0.04���`a,���`a ���bmfd0.02���`a,���`a ���bmfd0.00���`a,���`a ���bmfd0.01���`a,���`a ���bmfd0.12���`a,���`a ���bmfd0.04���`a,���`a ���bmfd0.00���`a]���`a,���`a
���`l            ���`a[���bmfd0.01���`a,���`a ���bmfd0.01���`a,���`a ���bmfd0.79���`a,���`a ���bmfd0.10���`a,���`a ���bmfd0.00���`a,���`a ���bmfd0.05���`a,���`a ���bmfd0.00���`a,���`a ���bmfd0.31���`a,���`a ���bmfd0.00���`a]���`a,���`a
���`l            ���`a[���bmfd0.00���`a,���`a ���bmfd0.02���`a,���`a ���bmfd0.03���`a,���`a ���bmfd0.38���`a,���`a ���bmfd0.31���`a,���`a ���bmfd0.31���`a,���`a ���bmfd0.00���`a,���`a ���bmfd0.59���`a,���`a ���bmfd0.00���`a]���`a,���`a
���`l            ���`a[���bmfd0.02���`a,���`a ���bmfd0.02���`a,���`a ���bmfd0.11���`a,���`a ���bmfd0.47���`a,���`a ���bmfd0.69���`a,���`a ���bmfd0.58���`a,���`a ���bmfd0.88���`a,���`a ���bmfd0.00���`a,���`a ���bmfd0.00���`a]���`a]���`a)���`a,���`a
���`h        ���`a(���bs1a'���bs1gWith O3���bs1a'���`a,���`a ���`a[���`a
���`l            ���`a[���bmfd0.89���`a,���`a ���bmfd0.01���`a,���`a ���bmfd0.07���`a,���`a ���bmfd0.00���`a,���`a ���bmfd0.00���`a,���`a ���bmfd0.05���`a,���`a ���bmfd0.00���`a,���`a ���bmfd0.00���`a,���`a ���bmfd0.03���`a]���`a,���`a
���`l            ���`a[���bmfd0.07���`a,���`a ���bmfd0.95���`a,���`a ���bmfd0.05���`a,���`a ���bmfd0.04���`a,���`a ���bmfd0.00���`a,���`a ���bmfd0.02���`a,���`a ���bmfd0.12���`a,���`a ���bmfd0.00���`a,���`a ���bmfd0.00���`a]���`a,���`a
���`l            ���`a[���bmfd0.01���`a,���`a ���bmfd0.02���`a,���`a ���bmfd0.86���`a,���`a ���bmfd0.27���`a,���`a ���bmfd0.16���`a,���`a ���bmfd0.19���`a,���`a ���bmfd0.00���`a,���`a ���bmfd0.00���`a,���`a ���bmfd0.00���`a]���`a,���`a
���`l            ���`a[���bmfd0.01���`a,���`a ���bmfd0.03���`a,���`a ���bmfd0.00���`a,���`a ���bmfd0.32���`a,���`a ���bmfd0.29���`a,���`a ���bmfd0.27���`a,���`a ���bmfd0.00���`a,���`a ���bmfd0.00���`a,���`a ���bmfd0.95���`a]���`a,���`a
���`l            ���`a[���bmfd0.02���`a,���`a ���bmfd0.00���`a,���`a ���bmfd0.03���`a,���`a ���bmfd0.37���`a,���`a ���bmfd0.56���`a,���`a ���bmfd0.47���`a,���`a ���bmfd0.87���`a,���`a ���bmfd0.00���`a,���`a ���bmfd0.00���`a]���`a]���`a)���`a,���`a
���`h        ���`a(���bs1a'���bs1gCO & O3���bs1a'���`a,���`a ���`a[���`a
���`l            ���`a[���bmfd0.87���`a,���`a ���bmfd0.01���`a,���`a ���bmfd0.08���`a,���`a ���bmfd0.00���`a,���`a ���bmfd0.00���`a,���`a ���bmfd0.04���`a,���`a ���bmfd0.00���`a,���`a ���bmfd0.00���`a,���`a ���bmfd0.01���`a]���`a,���`a
���`l            ���`a[���bmfd0.09���`a,���`a ���bmfd0.95���`a,���`a ���bmfd0.02���`a,���`a ���bmfd0.03���`a,���`a ���bmfd0.00���`a,���`a ���bmfd0.01���`a,���`a ���bmfd0.13���`a,���`a ���bmfd0.06���`a,���`a ���bmfd0.00���`a]���`a,���`a
���`l            ���`a[���bmfd0.01���`a,���`a ���bmfd0.02���`a,���`a ���bmfd0.71���`a,���`a ���bmfd0.24���`a,���`a ���bmfd0.13���`a,���`a ���bmfd0.16���`a,���`a ���bmfd0.00���`a,���`a ���bmfd0.50���`a,���`a ���bmfd0.00���`a]���`a,���`a
���`l            ���`a[���bmfd0.01���`a,���`a ���bmfd0.03���`a,���`a ���bmfd0.00���`a,���`a ���bmfd0.28���`a,���`a ���bmfd0.24���`a,���`a ���bmfd0.23���`a,���`a ���bmfd0.00���`a,���`a ���bmfd0.44���`a,���`a ���bmfd0.88���`a]���`a,���`a
���`l            ���`a[���bmfd0.02���`a,���`a ���bmfd0.00���`a,���`a ���bmfd0.18���`a,���`a ���bmfd0.45���`a,���`a ���bmfd0.64���`a,���`a ���bmfd0.55���`a,���`a ���bmfd0.86���`a,���`a ���bmfd0.00���`a,���`a ���bmfd0.16���`a]���`a]���`a)���`a
���`d    ���`a]���`a
���`d    ���akfreturn���`a ���`ddata���`a
���`a
���`a
���akbif���`a ���bvmh__name__���`a ���aob==���`a ���bs1a'���bs1h__main__���bs1a'���`a:���`a
���`d    ���`aN���`a ���aoa=���`a ���bmia9���`a
���`d    ���`etheta���`a ���aoa=���`a ���`mradar_factory���`a(���`aN���`a,���`a ���`eframe���aoa=���bs1a'���bs1gpolygon���bs1a'���`a)���`a
���`a
���`d    ���`ddata���`a ���aoa=���`a ���`lexample_data���`a(���`a)���`a
���`d    ���`lspoke_labels���`a ���aoa=���`a ���`ddata���aoa.���`cpop���`a(���bmia0���`a)���`a
���`a
���`d    ���`cfig���`a,���`a ���`caxs���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`gfigsize���aoa=���`a(���bmia9���`a,���`a ���bmia9���`a)���`a,���`a ���`enrows���aoa=���bmia2���`a,���`a ���`encols���aoa=���bmia2���`a,���`a
���`x                            ���`jsubplot_kw���aoa=���bnbddict���`a(���`jprojection���aoa=���bs1a'���bs1eradar���bs1a'���`a)���`a)���`a
���`d    ���`cfig���aoa.���`osubplots_adjust���`a(���`fwspace���aoa=���bmfd0.25���`a,���`a ���`fhspace���aoa=���bmfd0.20���`a,���`a ���`ctop���aoa=���bmfd0.85���`a,���`a ���`fbottom���aoa=���bmfd0.05���`a)���`a
���`a
���`d    ���`fcolors���`a ���aoa=���`a ���`a[���bs1a'���bs1ab���bs1a'���`a,���`a ���bs1a'���bs1ar���bs1a'���`a,���`a ���bs1a'���bs1ag���bs1a'���`a,���`a ���bs1a'���bs1am���bs1a'���`a,���`a ���bs1a'���bs1ay���bs1a'���`a]���`a
���`d    ���bc1x<# Plot the four cases from the example data on separate axes���`a
���`d    ���akcfor���`a ���`bax���`a,���`a ���`a(���`etitle���`a,���`a ���`icase_data���`a)���`a ���bowbin���`a ���bnbczip���`a(���`caxs���aoa.���`dflat���`a,���`a ���`ddata���`a)���`a:���`a
���`h        ���`bax���aoa.���`jset_rgrids���`a(���`a[���bmfc0.2���`a,���`a ���bmfc0.4���`a,���`a ���bmfc0.6���`a,���`a ���bmfc0.8���`a]���`a)���`a
���`h        ���`bax���aoa.���`iset_title���`a(���`etitle���`a,���`a ���`fweight���aoa=���bs1a'���bs1dbold���bs1a'���`a,���`a ���`dsize���aoa=���bs1a'���bs1fmedium���bs1a'���`a,���`a ���`hposition���aoa=���`a(���bmfc0.5���`a,���`a ���bmfc1.1���`a)���`a,���`a
���`u                     ���`shorizontalalignment���aoa=���bs1a'���bs1fcenter���bs1a'���`a,���`a ���`qverticalalignment���aoa=���bs1a'���bs1fcenter���bs1a'���`a)���`a
���`h        ���akcfor���`a ���`ad���`a,���`a ���`ecolor���`a ���bowbin���`a ���bnbczip���`a(���`icase_data���`a,���`a ���`fcolors���`a)���`a:���`a
���`l            ���`bax���aoa.���`dplot���`a(���`etheta���`a,���`a ���`ad���`a,���`a ���`ecolor���aoa=���`ecolor���`a)���`a
���`l            ���`bax���aoa.���`dfill���`a(���`etheta���`a,���`a ���`ad���`a,���`a ���`ifacecolor���aoa=���`ecolor���`a,���`a ���`ealpha���aoa=���bmfd0.25���`a)���`a
���`h        ���`bax���aoa.���`mset_varlabels���`a(���`lspoke_labels���`a)���`a
���`a
���`d    ���bc1x&# add legend relative to top-left plot���`a
���`d    ���`flabels���`a ���aoa=���`a ���`a(���bs1a'���bs1hFactor 1���bs1a'���`a,���`a ���bs1a'���bs1hFactor 2���bs1a'���`a,���`a ���bs1a'���bs1hFactor 3���bs1a'���`a,���`a ���bs1a'���bs1hFactor 4���bs1a'���`a,���`a ���bs1a'���bs1hFactor 5���bs1a'���`a)���`a
���`d    ���`flegend���`a ���aoa=���`a ���`caxs���`a[���bmia0���`a,���`a ���bmia0���`a]���aoa.���`flegend���`a(���`flabels���`a,���`a ���`cloc���aoa=���`a(���bmfc0.9���`a,���`a ���bmfc.95���`a)���`a,���`a
���`x                              ���`llabelspacing���aoa=���bmfc0.1���`a,���`a ���`hfontsize���aoa=���bs1a'���bs1esmall���bs1a'���`a)���`a
���`a
���`d    ���`cfig���aoa.���`dtext���`a(���bmfc0.5���`a,���`a ���bmfe0.965���`a,���`a ���bs1a'���bs1x05-Factor Solution Profiles Across Four Scenarios���bs1a'���`a,���`a
���`m             ���`shorizontalalignment���aoa=���bs1a'���bs1fcenter���bs1a'���`a,���`a ���`ecolor���aoa=���bs1a'���bs1eblack���bs1a'���`a,���`a ���`fweight���aoa=���bs1a'���bs1dbold���bs1a'���`a,���`a
���`m             ���`dsize���aoa=���bs1a'���bs1elarge���bs1a'���`a)���`a
���`a
���`d    ���`cplt���aoa.���`dshow���`a(���`a)���`a
���`a
���`a
���bc1xM#############################################################################���`a
���bc1a#���`a
���bc1x# .. admonition:: References���`a
���bc1a#���`a
���bc1xN#    The use of the following functions, methods, classes and modules is shown���`a
���bc1u#    in this example:���`a
���bc1a#���`a
���bc1x#    - `matplotlib.path`���`a
���bc1x#    - `matplotlib.path.Path`���`a
���bc1x#    - `matplotlib.spines`���`a
���bc1x #    - `matplotlib.spines.Spine`���`a
���bc1x#    - `matplotlib.projections`���`a
���bc1x%#    - `matplotlib.projections.polar`���`a
���bc1x/#    - `matplotlib.projections.polar.PolarAxes`���`a
���bc1x3#    - `matplotlib.projections.register_projection`���`a
`dNone�