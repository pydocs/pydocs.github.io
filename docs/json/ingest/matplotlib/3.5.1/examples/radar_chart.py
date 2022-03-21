ŸØÇÅŸ¥ÉôπŸ±Çbsdyg"""
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
"""Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±ÇbknfimportŸ±Ç`a Ÿ±ÇbnnŸ¢ÑenumpyŸ†Ñenumpyf1.22.3fmoduleenumpyfmoduleıŸ±Ç`a Ÿ±ÇakbasŸ±Ç`a Ÿ±ÇbnnbnpŸ±Ç`a
Ÿ±Ç`a
Ÿ±ÇbknfimportŸ±Ç`a Ÿ±ÇbnnŸ¢ÑjmatplotlibŸ†Ñjmatplotlibe3.5.1fmodulejmatplotlibfmoduleıŸ±Çbnna.Ÿ±ÇbnnfpyplotŸ±Ç`a Ÿ±ÇakbasŸ±Ç`a Ÿ±ÇbnncpltŸ±Ç`a
Ÿ±ÇbkndfromŸ±Ç`a Ÿ±ÇbnnŸ¢ÑjmatplotlibŸ†Ñjmatplotlibe3.5.1fmodulejmatplotlibfmoduleıŸ±Çbnna.Ÿ±ÇbnngpatchesŸ±Ç`a Ÿ±ÇbknfimportŸ±Ç`a Ÿ±Ç`fCircleŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`nRegularPolygonŸ±Ç`a
Ÿ±ÇbkndfromŸ±Ç`a Ÿ±ÇbnnŸ¢ÑjmatplotlibŸ†Ñjmatplotlibe3.5.1fmodulejmatplotlibfmoduleıŸ±Çbnna.Ÿ±ÇbnndpathŸ±Ç`a Ÿ±ÇbknfimportŸ±Ç`a Ÿ±Ç`dPathŸ±Ç`a
Ÿ±ÇbkndfromŸ±Ç`a Ÿ±ÇbnnŸ¢ÑjmatplotlibŸ†Ñjmatplotlibe3.5.1fmodulejmatplotlibfmoduleıŸ±Çbnna.Ÿ±ÇbnnkprojectionsŸ±Çbnna.Ÿ±ÇbnnepolarŸ±Ç`a Ÿ±ÇbknfimportŸ±Ç`a Ÿ±Ç`iPolarAxesŸ±Ç`a
Ÿ±ÇbkndfromŸ±Ç`a Ÿ±ÇbnnŸ¢ÑjmatplotlibŸ†Ñjmatplotlibe3.5.1fmodulejmatplotlibfmoduleıŸ±Çbnna.Ÿ±ÇbnnkprojectionsŸ±Ç`a Ÿ±ÇbknfimportŸ±Ç`a Ÿ±Ç`sregister_projectionŸ±Ç`a
Ÿ±ÇbkndfromŸ±Ç`a Ÿ±ÇbnnŸ¢ÑjmatplotlibŸ†Ñjmatplotlibe3.5.1fmodulejmatplotlibfmoduleıŸ±Çbnna.Ÿ±ÇbnnfspinesŸ±Ç`a Ÿ±ÇbknfimportŸ±Ç`a Ÿ±Ç`eSpineŸ±Ç`a
Ÿ±ÇbkndfromŸ±Ç`a Ÿ±ÇbnnŸ¢ÑjmatplotlibŸ†Ñjmatplotlibe3.5.1fmodulejmatplotlibfmoduleıŸ±Çbnna.Ÿ±ÇbnnjtransformsŸ±Ç`a Ÿ±ÇbknfimportŸ±Ç`a Ÿ±Ç`hAffine2DŸ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±ÇakcdefŸ±Ç`a Ÿ±Çbnfmradar_factoryŸ±Ç`a(Ÿ±Ç`hnum_varsŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`eframeŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1fcircleŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Çbsdy)"""
    Create a radar chart with `num_vars` axes.

    This function creates a RadarAxes projection and registers it.

    Parameters
    ----------
    num_vars : int
        Number of variables for radar chart.
    frame : {'circle', 'polygon'}
        Shape of frame surrounding axes.

    """Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Çbc1x%# calculate evenly-spaced axis anglesŸ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`ethetaŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`hlinspaceŸ±Ç`a(Ÿ±Çbmia0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia2Ÿ±Çaoa*Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`bpiŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`hnum_varsŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`hendpointŸ±Çaoa=Ÿ±ÇbkceFalseŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±ÇakeclassŸ±Ç`a Ÿ±ÇbnciRadarAxesŸ±Ç`a(Ÿ±Ç`iPolarAxesŸ±Ç`a)Ÿ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±Ç`dnameŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1eradarŸ±Çbs1a'Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±Çbc1x0# use 1 line segment to connect specified pointsŸ±Ç`a
Ÿ±Ç`h        Ÿ±Ç`jRESOLUTIONŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Çbmia1Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±ÇakcdefŸ±Ç`a Ÿ±Çbfmh__init__Ÿ±Ç`a(Ÿ±ÇbbpdselfŸ±Ç`a,Ÿ±Ç`a Ÿ±Çaoa*Ÿ±Ç`dargsŸ±Ç`a,Ÿ±Ç`a Ÿ±Çaoa*Ÿ±Çaoa*Ÿ±Ç`fkwargsŸ±Ç`a)Ÿ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`l            Ÿ±ÇbnbesuperŸ±Ç`a(Ÿ±Ç`a)Ÿ±Çaoa.Ÿ±Çbfmh__init__Ÿ±Ç`a(Ÿ±Çaoa*Ÿ±Ç`dargsŸ±Ç`a,Ÿ±Ç`a Ÿ±Çaoa*Ÿ±Çaoa*Ÿ±Ç`fkwargsŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`l            Ÿ±Çbc1x4# rotate plot such that the first axis is at the topŸ±Ç`a
Ÿ±Ç`l            Ÿ±ÇbbpdselfŸ±Çaoa.Ÿ±Ç`wset_theta_zero_locationŸ±Ç`a(Ÿ±Çbs1a'Ÿ±Çbs1aNŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±ÇakcdefŸ±Ç`a Ÿ±ÇbnfdfillŸ±Ç`a(Ÿ±ÇbbpdselfŸ±Ç`a,Ÿ±Ç`a Ÿ±Çaoa*Ÿ±Ç`dargsŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`fclosedŸ±Çaoa=Ÿ±ÇbkcdTrueŸ±Ç`a,Ÿ±Ç`a Ÿ±Çaoa*Ÿ±Çaoa*Ÿ±Ç`fkwargsŸ±Ç`a)Ÿ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`l            Ÿ±Çbsdx5"""Override fill so that line is closed by default"""Ÿ±Ç`a
Ÿ±Ç`l            Ÿ±ÇakfreturnŸ±Ç`a Ÿ±ÇbnbesuperŸ±Ç`a(Ÿ±Ç`a)Ÿ±Çaoa.Ÿ±Ç`dfillŸ±Ç`a(Ÿ±Ç`fclosedŸ±Çaoa=Ÿ±Ç`fclosedŸ±Ç`a,Ÿ±Ç`a Ÿ±Çaoa*Ÿ±Ç`dargsŸ±Ç`a,Ÿ±Ç`a Ÿ±Çaoa*Ÿ±Çaoa*Ÿ±Ç`fkwargsŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±ÇakcdefŸ±Ç`a Ÿ±ÇbnfdplotŸ±Ç`a(Ÿ±ÇbbpdselfŸ±Ç`a,Ÿ±Ç`a Ÿ±Çaoa*Ÿ±Ç`dargsŸ±Ç`a,Ÿ±Ç`a Ÿ±Çaoa*Ÿ±Çaoa*Ÿ±Ç`fkwargsŸ±Ç`a)Ÿ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`l            Ÿ±Çbsdx5"""Override plot so that line is closed by default"""Ÿ±Ç`a
Ÿ±Ç`l            Ÿ±Ç`elinesŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±ÇbnbesuperŸ±Ç`a(Ÿ±Ç`a)Ÿ±Çaoa.Ÿ±Ç`dplotŸ±Ç`a(Ÿ±Çaoa*Ÿ±Ç`dargsŸ±Ç`a,Ÿ±Ç`a Ÿ±Çaoa*Ÿ±Çaoa*Ÿ±Ç`fkwargsŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`l            Ÿ±ÇakcforŸ±Ç`a Ÿ±Ç`dlineŸ±Ç`a Ÿ±ÇbowbinŸ±Ç`a Ÿ±Ç`elinesŸ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`p                Ÿ±ÇbbpdselfŸ±Çaoa.Ÿ±Ç`k_close_lineŸ±Ç`a(Ÿ±Ç`dlineŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±ÇakcdefŸ±Ç`a Ÿ±Çbnfk_close_lineŸ±Ç`a(Ÿ±ÇbbpdselfŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dlineŸ±Ç`a)Ÿ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`l            Ÿ±Ç`axŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ayŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`dlineŸ±Çaoa.Ÿ±Ç`hget_dataŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`l            Ÿ±Çbc1x-# FIXME: markers at x[0], y[0] get doubled-upŸ±Ç`a
Ÿ±Ç`l            Ÿ±ÇakbifŸ±Ç`a Ÿ±Ç`axŸ±Ç`a[Ÿ±Çbmia0Ÿ±Ç`a]Ÿ±Ç`a Ÿ±Çaob!=Ÿ±Ç`a Ÿ±Ç`axŸ±Ç`a[Ÿ±Çaoa-Ÿ±Çbmia1Ÿ±Ç`a]Ÿ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`p                Ÿ±Ç`axŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`fappendŸ±Ç`a(Ÿ±Ç`axŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`axŸ±Ç`a[Ÿ±Çbmia0Ÿ±Ç`a]Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`p                Ÿ±Ç`ayŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`fappendŸ±Ç`a(Ÿ±Ç`ayŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ayŸ±Ç`a[Ÿ±Çbmia0Ÿ±Ç`a]Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`p                Ÿ±Ç`dlineŸ±Çaoa.Ÿ±Ç`hset_dataŸ±Ç`a(Ÿ±Ç`axŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ayŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±ÇakcdefŸ±Ç`a Ÿ±Çbnfmset_varlabelsŸ±Ç`a(Ÿ±ÇbbpdselfŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`flabelsŸ±Ç`a)Ÿ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`l            Ÿ±ÇbbpdselfŸ±Çaoa.Ÿ±Ç`nset_thetagridsŸ±Ç`a(Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`gdegreesŸ±Ç`a(Ÿ±Ç`ethetaŸ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`flabelsŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±ÇakcdefŸ±Ç`a Ÿ±Çbnfo_gen_axes_patchŸ±Ç`a(Ÿ±ÇbbpdselfŸ±Ç`a)Ÿ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`l            Ÿ±Çbc1xA# The Axes patch must be centered at (0.5, 0.5) and of radius 0.5Ÿ±Ç`a
Ÿ±Ç`l            Ÿ±Çbc1v# in axes coordinates.Ÿ±Ç`a
Ÿ±Ç`l            Ÿ±ÇakbifŸ±Ç`a Ÿ±Ç`eframeŸ±Ç`a Ÿ±Çaob==Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1fcircleŸ±Çbs1a'Ÿ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`p                Ÿ±ÇakfreturnŸ±Ç`a Ÿ±Ç`fCircleŸ±Ç`a(Ÿ±Ç`a(Ÿ±Çbmfc0.5Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfc0.5Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfc0.5Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`l            Ÿ±ÇakdelifŸ±Ç`a Ÿ±Ç`eframeŸ±Ç`a Ÿ±Çaob==Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1gpolygonŸ±Çbs1a'Ÿ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`p                Ÿ±ÇakfreturnŸ±Ç`a Ÿ±Ç`nRegularPolygonŸ±Ç`a(Ÿ±Ç`a(Ÿ±Çbmfc0.5Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfc0.5Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`hnum_varsŸ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`x&                                      Ÿ±Ç`fradiusŸ±Çaoa=Ÿ±Çbmfb.5Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`iedgecolorŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2akŸ±Çbs2a"Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`l            Ÿ±ÇakdelseŸ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`p                Ÿ±ÇakeraiseŸ±Ç`a Ÿ±ÇbnejValueErrorŸ±Ç`a(Ÿ±Çbs2a"Ÿ±Çbs2rUnknown value for Ÿ±Çbs2a'Ÿ±Çbs2eframeŸ±Çbs2a'Ÿ±Çbs2b: Ÿ±Çbsib%sŸ±Çbs2a"Ÿ±Ç`a Ÿ±Çaoa%Ÿ±Ç`a Ÿ±Ç`eframeŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±ÇakcdefŸ±Ç`a Ÿ±Çbnfp_gen_axes_spinesŸ±Ç`a(Ÿ±ÇbbpdselfŸ±Ç`a)Ÿ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`l            Ÿ±ÇakbifŸ±Ç`a Ÿ±Ç`eframeŸ±Ç`a Ÿ±Çaob==Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1fcircleŸ±Çbs1a'Ÿ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`p                Ÿ±ÇakfreturnŸ±Ç`a Ÿ±ÇbnbesuperŸ±Ç`a(Ÿ±Ç`a)Ÿ±Çaoa.Ÿ±Ç`p_gen_axes_spinesŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`l            Ÿ±ÇakdelifŸ±Ç`a Ÿ±Ç`eframeŸ±Ç`a Ÿ±Çaob==Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1gpolygonŸ±Çbs1a'Ÿ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`p                Ÿ±Çbc1x<# spine_type must be 'left'/'right'/'top'/'bottom'/'circle'.Ÿ±Ç`a
Ÿ±Ç`p                Ÿ±Ç`espineŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`eSpineŸ±Ç`a(Ÿ±Ç`daxesŸ±Çaoa=Ÿ±ÇbbpdselfŸ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`x                              Ÿ±Ç`jspine_typeŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1fcircleŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`x                              Ÿ±Ç`dpathŸ±Çaoa=Ÿ±Ç`dPathŸ±Çaoa.Ÿ±Ç`tunit_regular_polygonŸ±Ç`a(Ÿ±Ç`hnum_varsŸ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`p                Ÿ±Çbc1x># unit_regular_polygon gives a polygon of radius 1 centered atŸ±Ç`a
Ÿ±Ç`p                Ÿ±Çbc1x># (0, 0) but we want a polygon of radius 0.5 centered at (0.5,Ÿ±Ç`a
Ÿ±Ç`p                Ÿ±Çbc1x# 0.5) in axes coordinates.Ÿ±Ç`a
Ÿ±Ç`p                Ÿ±Ç`espineŸ±Çaoa.Ÿ±Ç`mset_transformŸ±Ç`a(Ÿ±Ç`hAffine2DŸ±Ç`a(Ÿ±Ç`a)Ÿ±Çaoa.Ÿ±Ç`escaleŸ±Ç`a(Ÿ±Çbmfb.5Ÿ±Ç`a)Ÿ±Çaoa.Ÿ±Ç`itranslateŸ±Ç`a(Ÿ±Çbmfb.5Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfb.5Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`x$                                    Ÿ±Çaoa+Ÿ±Ç`a Ÿ±ÇbbpdselfŸ±Çaoa.Ÿ±Ç`itransAxesŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`p                Ÿ±ÇakfreturnŸ±Ç`a Ÿ±Ç`a{Ÿ±Çbs1a'Ÿ±Çbs1epolarŸ±Çbs1a'Ÿ±Ç`a:Ÿ±Ç`a Ÿ±Ç`espineŸ±Ç`a}Ÿ±Ç`a
Ÿ±Ç`l            Ÿ±ÇakdelseŸ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`p                Ÿ±ÇakeraiseŸ±Ç`a Ÿ±ÇbnejValueErrorŸ±Ç`a(Ÿ±Çbs2a"Ÿ±Çbs2rUnknown value for Ÿ±Çbs2a'Ÿ±Çbs2eframeŸ±Çbs2a'Ÿ±Çbs2b: Ÿ±Çbsib%sŸ±Çbs2a"Ÿ±Ç`a Ÿ±Çaoa%Ÿ±Ç`a Ÿ±Ç`eframeŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`sregister_projectionŸ±Ç`a(Ÿ±Ç`iRadarAxesŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±ÇakfreturnŸ±Ç`a Ÿ±Ç`ethetaŸ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±ÇakcdefŸ±Ç`a Ÿ±Çbnflexample_dataŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Çbc1xI# The following data is from the Denver Aerosol Sources and Health study.Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Çbc1x(# See doi:10.1016/j.atmosenv.2008.12.017Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Çbc1a#Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Çbc1xB# The data are pollution source profile estimates for five modeledŸ±Ç`a
Ÿ±Ç`d    Ÿ±Çbc1xJ# pollution sources (e.g., cars, wood-burning, etc) that emit 7-9 chemicalŸ±Ç`a
Ÿ±Ç`d    Ÿ±Çbc1xG# species. The radar charts are experimented with here to see if we canŸ±Ç`a
Ÿ±Ç`d    Ÿ±Çbc1xE# nicely visualize how the modeled source profiles change across fourŸ±Ç`a
Ÿ±Ç`d    Ÿ±Çbc1l# scenarios:Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Çbc1xD#  1) No gas-phase species present, just seven particulate counts onŸ±Ç`a
Ÿ±Ç`d    Ÿ±Çbc1m#     SulfateŸ±Ç`a
Ÿ±Ç`d    Ÿ±Çbc1m#     NitrateŸ±Ç`a
Ÿ±Ç`d    Ÿ±Çbc1x#     Elemental Carbon (EC)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Çbc1x$#     Organic Carbon fraction 1 (OC)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Çbc1x%#     Organic Carbon fraction 2 (OC2)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Çbc1x%#     Organic Carbon fraction 3 (OC3)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Çbc1x##     Pyrolized Organic Carbon (OP)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Çbc1x7#  2)Inclusion of gas-phase specie carbon monoxide (CO)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Çbc1x.#  3)Inclusion of gas-phase specie ozone (O3).Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Çbc1x6#  4)Inclusion of both gas-phase species is present...Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`ddataŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`a[Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±Ç`a[Ÿ±Çbs1a'Ÿ±Çbs1gSulfateŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1gNitrateŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1bECŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1cOC1Ÿ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1cOC2Ÿ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1cOC3Ÿ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1bOPŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1bCOŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1bO3Ÿ±Çbs1a'Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±Ç`a(Ÿ±Çbs1a'Ÿ±Çbs1hBasecaseŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`a[Ÿ±Ç`a
Ÿ±Ç`l            Ÿ±Ç`a[Ÿ±Çbmfd0.88Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd0.01Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd0.03Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd0.03Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd0.00Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd0.06Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd0.01Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd0.00Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd0.00Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`l            Ÿ±Ç`a[Ÿ±Çbmfd0.07Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd0.95Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd0.04Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd0.05Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd0.00Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd0.02Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd0.01Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd0.00Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd0.00Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`l            Ÿ±Ç`a[Ÿ±Çbmfd0.01Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd0.02Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd0.85Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd0.19Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd0.05Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd0.10Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd0.00Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd0.00Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd0.00Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`l            Ÿ±Ç`a[Ÿ±Çbmfd0.02Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd0.01Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd0.07Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd0.01Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd0.21Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd0.12Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd0.98Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd0.00Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd0.00Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`l            Ÿ±Ç`a[Ÿ±Çbmfd0.01Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd0.01Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd0.02Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd0.71Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd0.74Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd0.70Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd0.00Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd0.00Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd0.00Ÿ±Ç`a]Ÿ±Ç`a]Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±Ç`a(Ÿ±Çbs1a'Ÿ±Çbs1gWith COŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`a[Ÿ±Ç`a
Ÿ±Ç`l            Ÿ±Ç`a[Ÿ±Çbmfd0.88Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd0.02Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd0.02Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd0.02Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd0.00Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd0.05Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd0.00Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd0.05Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd0.00Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`l            Ÿ±Ç`a[Ÿ±Çbmfd0.08Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd0.94Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd0.04Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd0.02Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd0.00Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd0.01Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd0.12Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd0.04Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd0.00Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`l            Ÿ±Ç`a[Ÿ±Çbmfd0.01Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd0.01Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd0.79Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd0.10Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd0.00Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd0.05Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd0.00Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd0.31Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd0.00Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`l            Ÿ±Ç`a[Ÿ±Çbmfd0.00Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd0.02Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd0.03Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd0.38Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd0.31Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd0.31Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd0.00Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd0.59Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd0.00Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`l            Ÿ±Ç`a[Ÿ±Çbmfd0.02Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd0.02Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd0.11Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd0.47Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd0.69Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd0.58Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd0.88Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd0.00Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd0.00Ÿ±Ç`a]Ÿ±Ç`a]Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±Ç`a(Ÿ±Çbs1a'Ÿ±Çbs1gWith O3Ÿ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`a[Ÿ±Ç`a
Ÿ±Ç`l            Ÿ±Ç`a[Ÿ±Çbmfd0.89Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd0.01Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd0.07Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd0.00Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd0.00Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd0.05Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd0.00Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd0.00Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd0.03Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`l            Ÿ±Ç`a[Ÿ±Çbmfd0.07Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd0.95Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd0.05Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd0.04Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd0.00Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd0.02Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd0.12Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd0.00Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd0.00Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`l            Ÿ±Ç`a[Ÿ±Çbmfd0.01Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd0.02Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd0.86Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd0.27Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd0.16Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd0.19Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd0.00Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd0.00Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd0.00Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`l            Ÿ±Ç`a[Ÿ±Çbmfd0.01Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd0.03Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd0.00Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd0.32Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd0.29Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd0.27Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd0.00Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd0.00Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd0.95Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`l            Ÿ±Ç`a[Ÿ±Çbmfd0.02Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd0.00Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd0.03Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd0.37Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd0.56Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd0.47Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd0.87Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd0.00Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd0.00Ÿ±Ç`a]Ÿ±Ç`a]Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±Ç`a(Ÿ±Çbs1a'Ÿ±Çbs1gCO & O3Ÿ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`a[Ÿ±Ç`a
Ÿ±Ç`l            Ÿ±Ç`a[Ÿ±Çbmfd0.87Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd0.01Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd0.08Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd0.00Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd0.00Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd0.04Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd0.00Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd0.00Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd0.01Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`l            Ÿ±Ç`a[Ÿ±Çbmfd0.09Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd0.95Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd0.02Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd0.03Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd0.00Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd0.01Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd0.13Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd0.06Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd0.00Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`l            Ÿ±Ç`a[Ÿ±Çbmfd0.01Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd0.02Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd0.71Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd0.24Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd0.13Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd0.16Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd0.00Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd0.50Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd0.00Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`l            Ÿ±Ç`a[Ÿ±Çbmfd0.01Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd0.03Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd0.00Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd0.28Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd0.24Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd0.23Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd0.00Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd0.44Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd0.88Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`l            Ÿ±Ç`a[Ÿ±Çbmfd0.02Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd0.00Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd0.18Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd0.45Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd0.64Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd0.55Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd0.86Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd0.00Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd0.16Ÿ±Ç`a]Ÿ±Ç`a]Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`a]Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±ÇakfreturnŸ±Ç`a Ÿ±Ç`ddataŸ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±ÇakbifŸ±Ç`a Ÿ±Çbvmh__name__Ÿ±Ç`a Ÿ±Çaob==Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1h__main__Ÿ±Çbs1a'Ÿ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`aNŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Çbmia9Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`ethetaŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`mradar_factoryŸ±Ç`a(Ÿ±Ç`aNŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`eframeŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1gpolygonŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`ddataŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`lexample_dataŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`lspoke_labelsŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`ddataŸ±Çaoa.Ÿ±Ç`cpopŸ±Ç`a(Ÿ±Çbmia0Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`cfigŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`caxsŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`hsubplotsŸ±Ç`a(Ÿ±Ç`gfigsizeŸ±Çaoa=Ÿ±Ç`a(Ÿ±Çbmia9Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia9Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`enrowsŸ±Çaoa=Ÿ±Çbmia2Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`encolsŸ±Çaoa=Ÿ±Çbmia2Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`x                            Ÿ±Ç`jsubplot_kwŸ±Çaoa=Ÿ±ÇbnbddictŸ±Ç`a(Ÿ±Ç`jprojectionŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1eradarŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`cfigŸ±Çaoa.Ÿ±Ç`osubplots_adjustŸ±Ç`a(Ÿ±Ç`fwspaceŸ±Çaoa=Ÿ±Çbmfd0.25Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`fhspaceŸ±Çaoa=Ÿ±Çbmfd0.20Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ctopŸ±Çaoa=Ÿ±Çbmfd0.85Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`fbottomŸ±Çaoa=Ÿ±Çbmfd0.05Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`fcolorsŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`a[Ÿ±Çbs1a'Ÿ±Çbs1abŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1arŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1agŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1amŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1ayŸ±Çbs1a'Ÿ±Ç`a]Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Çbc1x<# Plot the four cases from the example data on separate axesŸ±Ç`a
Ÿ±Ç`d    Ÿ±ÇakcforŸ±Ç`a Ÿ±Ç`baxŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`a(Ÿ±Ç`etitleŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`icase_dataŸ±Ç`a)Ÿ±Ç`a Ÿ±ÇbowbinŸ±Ç`a Ÿ±ÇbnbczipŸ±Ç`a(Ÿ±Ç`caxsŸ±Çaoa.Ÿ±Ç`dflatŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ddataŸ±Ç`a)Ÿ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`jset_rgridsŸ±Ç`a(Ÿ±Ç`a[Ÿ±Çbmfc0.2Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfc0.4Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfc0.6Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfc0.8Ÿ±Ç`a]Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`iset_titleŸ±Ç`a(Ÿ±Ç`etitleŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`fweightŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1dboldŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dsizeŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1fmediumŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`hpositionŸ±Çaoa=Ÿ±Ç`a(Ÿ±Çbmfc0.5Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfc1.1Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`u                     Ÿ±Ç`shorizontalalignmentŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1fcenterŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`qverticalalignmentŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1fcenterŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±ÇakcforŸ±Ç`a Ÿ±Ç`adŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ecolorŸ±Ç`a Ÿ±ÇbowbinŸ±Ç`a Ÿ±ÇbnbczipŸ±Ç`a(Ÿ±Ç`icase_dataŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`fcolorsŸ±Ç`a)Ÿ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`l            Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`dplotŸ±Ç`a(Ÿ±Ç`ethetaŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`adŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ecolorŸ±Çaoa=Ÿ±Ç`ecolorŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`l            Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`dfillŸ±Ç`a(Ÿ±Ç`ethetaŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`adŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ifacecolorŸ±Çaoa=Ÿ±Ç`ecolorŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ealphaŸ±Çaoa=Ÿ±Çbmfd0.25Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`mset_varlabelsŸ±Ç`a(Ÿ±Ç`lspoke_labelsŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Çbc1x&# add legend relative to top-left plotŸ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`flabelsŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`a(Ÿ±Çbs1a'Ÿ±Çbs1hFactor 1Ÿ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1hFactor 2Ÿ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1hFactor 3Ÿ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1hFactor 4Ÿ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1hFactor 5Ÿ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`flegendŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`caxsŸ±Ç`a[Ÿ±Çbmia0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia0Ÿ±Ç`a]Ÿ±Çaoa.Ÿ±Ç`flegendŸ±Ç`a(Ÿ±Ç`flabelsŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`clocŸ±Çaoa=Ÿ±Ç`a(Ÿ±Çbmfc0.9Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfc.95Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`x                              Ÿ±Ç`llabelspacingŸ±Çaoa=Ÿ±Çbmfc0.1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`hfontsizeŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1esmallŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`cfigŸ±Çaoa.Ÿ±Ç`dtextŸ±Ç`a(Ÿ±Çbmfc0.5Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfe0.965Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1x05-Factor Solution Profiles Across Four ScenariosŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`m             Ÿ±Ç`shorizontalalignmentŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1fcenterŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ecolorŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1eblackŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`fweightŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1dboldŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`m             Ÿ±Ç`dsizeŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1elargeŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`dshowŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1xM#############################################################################Ÿ±Ç`a
Ÿ±Çbc1a#Ÿ±Ç`a
Ÿ±Çbc1x# .. admonition:: ReferencesŸ±Ç`a
Ÿ±Çbc1a#Ÿ±Ç`a
Ÿ±Çbc1xN#    The use of the following functions, methods, classes and modules is shownŸ±Ç`a
Ÿ±Çbc1u#    in this example:Ÿ±Ç`a
Ÿ±Çbc1a#Ÿ±Ç`a
Ÿ±Çbc1x#    - `matplotlib.path`Ÿ±Ç`a
Ÿ±Çbc1x#    - `matplotlib.path.Path`Ÿ±Ç`a
Ÿ±Çbc1x#    - `matplotlib.spines`Ÿ±Ç`a
Ÿ±Çbc1x #    - `matplotlib.spines.Spine`Ÿ±Ç`a
Ÿ±Çbc1x#    - `matplotlib.projections`Ÿ±Ç`a
Ÿ±Çbc1x%#    - `matplotlib.projections.polar`Ÿ±Ç`a
Ÿ±Çbc1x/#    - `matplotlib.projections.polar.PolarAxes`Ÿ±Ç`a
Ÿ±Çbc1x3#    - `matplotlib.projections.register_projection`Ÿ±Ç`a
`dNoneˆ