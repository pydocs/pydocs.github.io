ŸØÇÅŸ¥ÉôôŸ±Çbsdy˚"""
=======================
Topographic hillshading
=======================

Demonstrates the visual effect of varying blend mode and vertical exaggeration
on "hillshaded" plots.

Note that the "overlay" and "soft" blend modes work well for complex surfaces
such as this example, while the default "hsv" blend mode works best for smooth
surfaces such as many mathematical functions.

In most cases, hillshading is used purely for visual purposes, and *dx*/*dy*
can be safely ignored. In that case, you can tweak *vert_exag* (vertical
exaggeration) by trial and error to give the desired visual effect. However,
this example demonstrates how to use the *dx* and *dy* keyword arguments to
ensure that the *vert_exag* parameter is the true vertical exaggeration.
"""Ÿ±Ç`a
Ÿ±ÇbknfimportŸ±Ç`a Ÿ±ÇbnnŸ¢ÑenumpyŸ†Ñenumpyf1.22.3fmoduleenumpyfmoduleıŸ±Ç`a Ÿ±ÇakbasŸ±Ç`a Ÿ±ÇbnnbnpŸ±Ç`a
Ÿ±ÇbknfimportŸ±Ç`a Ÿ±ÇbnnŸ¢ÑjmatplotlibŸ†Ñjmatplotlibe3.5.1fmodulejmatplotlibfmoduleıŸ±Çbnna.Ÿ±ÇbnnfpyplotŸ±Ç`a Ÿ±ÇakbasŸ±Ç`a Ÿ±ÇbnncpltŸ±Ç`a
Ÿ±ÇbkndfromŸ±Ç`a Ÿ±ÇbnnŸ¢ÑjmatplotlibŸ†Ñjmatplotlibe3.5.1fmodulejmatplotlibfmoduleıŸ±Çbnna.Ÿ±ÇbnnecbookŸ±Ç`a Ÿ±ÇbknfimportŸ±Ç`a Ÿ±Ç`oget_sample_dataŸ±Ç`a
Ÿ±ÇbkndfromŸ±Ç`a Ÿ±ÇbnnŸ¢ÑjmatplotlibŸ†Ñjmatplotlibe3.5.1fmodulejmatplotlibfmoduleıŸ±Çbnna.Ÿ±ÇbnnfcolorsŸ±Ç`a Ÿ±ÇbknfimportŸ±Ç`a Ÿ±Ç`kLightSourceŸ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`cdemŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`oget_sample_dataŸ±Ç`a(Ÿ±Çbs1a'Ÿ±Çbs1wjacksboro_fault_dem.npzŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`gnp_loadŸ±Çaoa=Ÿ±ÇbkcdTrueŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`azŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cdemŸ±Ç`a[Ÿ±Çbs1a'Ÿ±Çbs1ielevationŸ±Çbs1a'Ÿ±Ç`a]Ÿ±Ç`a
Ÿ±Çbc1xO# -- Optional dx and dy for accurate vertical exaggeration --------------------Ÿ±Ç`a
Ÿ±Çbc1xO# If you need topographically accurate vertical exaggeration, or you don't wantŸ±Ç`a
Ÿ±Çbc1xM# to guess at what *vert_exag* should be, you'll need to specify the cellsizeŸ±Ç`a
Ÿ±Çbc1xN# of the grid (i.e. the *dx* and *dy* parameters).  Otherwise, any *vert_exag*Ÿ±Ç`a
Ÿ±Çbc1xK# value you specify will be relative to the grid spacing of your input dataŸ±Ç`a
Ÿ±Çbc1xN# (in other words, *dx* and *dy* default to 1.0, and *vert_exag* is calculatedŸ±Ç`a
Ÿ±Çbc1xO# relative to those parameters).  Similarly, *dx* and *dy* are assumed to be inŸ±Ç`a
Ÿ±Çbc1xN# the same units as your input z-values.  Therefore, we'll need to convert theŸ±Ç`a
Ÿ±Çbc1x1# given dx and dy from decimal degrees to meters.Ÿ±Ç`a
Ÿ±Ç`bdxŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`bdyŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cdemŸ±Ç`a[Ÿ±Çbs1a'Ÿ±Çbs1bdxŸ±Çbs1a'Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`cdemŸ±Ç`a[Ÿ±Çbs1a'Ÿ±Çbs1bdyŸ±Çbs1a'Ÿ±Ç`a]Ÿ±Ç`a
Ÿ±Ç`bdyŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Çbmif111200Ÿ±Ç`a Ÿ±Çaoa*Ÿ±Ç`a Ÿ±Ç`bdyŸ±Ç`a
Ÿ±Ç`bdxŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Çbmif111200Ÿ±Ç`a Ÿ±Çaoa*Ÿ±Ç`a Ÿ±Ç`bdxŸ±Ç`a Ÿ±Çaoa*Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`ccosŸ±Ç`a(Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`gradiansŸ±Ç`a(Ÿ±Ç`cdemŸ±Ç`a[Ÿ±Çbs1a'Ÿ±Çbs1dyminŸ±Çbs1a'Ÿ±Ç`a]Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Çbc1xO# -----------------------------------------------------------------------------Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1xC# Shade from the northwest, with the sun 45 degrees from horizontalŸ±Ç`a
Ÿ±Ç`blsŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`kLightSourceŸ±Ç`a(Ÿ±Ç`eazdegŸ±Çaoa=Ÿ±Çbmic315Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`faltdegŸ±Çaoa=Ÿ±Çbmib45Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`dcmapŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`bcmŸ±Çaoa.Ÿ±Ç`jgist_earthŸ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`cfigŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`caxsŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`hsubplotsŸ±Ç`a(Ÿ±Ç`enrowsŸ±Çaoa=Ÿ±Çbmia4Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`encolsŸ±Çaoa=Ÿ±Çbmia3Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`gfigsizeŸ±Çaoa=Ÿ±Ç`a(Ÿ±Çbmia8Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia9Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`dsetpŸ±Ç`a(Ÿ±Ç`caxsŸ±Çaoa.Ÿ±Ç`dflatŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`fxticksŸ±Çaoa=Ÿ±Ç`a[Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`fyticksŸ±Çaoa=Ÿ±Ç`a[Ÿ±Ç`a]Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1xE# Vary vertical exaggeration and blend mode and plot all combinationsŸ±Ç`a
Ÿ±ÇakcforŸ±Ç`a Ÿ±Ç`ccolŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`bveŸ±Ç`a Ÿ±ÇbowbinŸ±Ç`a Ÿ±ÇbnbczipŸ±Ç`a(Ÿ±Ç`caxsŸ±Çaoa.Ÿ±Ç`aTŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`a[Ÿ±Çbmfc0.1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmib10Ÿ±Ç`a]Ÿ±Ç`a)Ÿ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Çbc1x5# Show the hillshade intensity image in the first rowŸ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`ccolŸ±Ç`a[Ÿ±Çbmia0Ÿ±Ç`a]Ÿ±Çaoa.Ÿ±Ç`fimshowŸ±Ç`a(Ÿ±Ç`blsŸ±Çaoa.Ÿ±Ç`ihillshadeŸ±Ç`a(Ÿ±Ç`azŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ivert_exagŸ±Çaoa=Ÿ±Ç`bveŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`bdxŸ±Çaoa=Ÿ±Ç`bdxŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`bdyŸ±Çaoa=Ÿ±Ç`bdyŸ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dcmapŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1dgrayŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Çbc1xK# Place hillshaded plots with different blend modes in the rest of the rowsŸ±Ç`a
Ÿ±Ç`d    Ÿ±ÇakcforŸ±Ç`a Ÿ±Ç`baxŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dmodeŸ±Ç`a Ÿ±ÇbowbinŸ±Ç`a Ÿ±ÇbnbczipŸ±Ç`a(Ÿ±Ç`ccolŸ±Ç`a[Ÿ±Çbmia1Ÿ±Ç`a:Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`a[Ÿ±Çbs1a'Ÿ±Çbs1chsvŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1goverlayŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1dsoftŸ±Çbs1a'Ÿ±Ç`a]Ÿ±Ç`a)Ÿ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±Ç`crgbŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`blsŸ±Çaoa.Ÿ±Ç`eshadeŸ±Ç`a(Ÿ±Ç`azŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dcmapŸ±Çaoa=Ÿ±Ç`dcmapŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`jblend_modeŸ±Çaoa=Ÿ±Ç`dmodeŸ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`w                       Ÿ±Ç`ivert_exagŸ±Çaoa=Ÿ±Ç`bveŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`bdxŸ±Çaoa=Ÿ±Ç`bdxŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`bdyŸ±Çaoa=Ÿ±Ç`bdyŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`fimshowŸ±Ç`a(Ÿ±Ç`crgbŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1x# Label rows and columnsŸ±Ç`a
Ÿ±ÇakcforŸ±Ç`a Ÿ±Ç`baxŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`bveŸ±Ç`a Ÿ±ÇbowbinŸ±Ç`a Ÿ±ÇbnbczipŸ±Ç`a(Ÿ±Ç`caxsŸ±Ç`a[Ÿ±Çbmia0Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`a[Ÿ±Çbmfc0.1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmib10Ÿ±Ç`a]Ÿ±Ç`a)Ÿ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`iset_titleŸ±Ç`a(Ÿ±Çbs1a'Ÿ±Çbsic{0}Ÿ±Çbs1a'Ÿ±Çaoa.Ÿ±Ç`fformatŸ±Ç`a(Ÿ±Ç`bveŸ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dsizeŸ±Çaoa=Ÿ±Çbmib18Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±ÇakcforŸ±Ç`a Ÿ±Ç`baxŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dmodeŸ±Ç`a Ÿ±ÇbowbinŸ±Ç`a Ÿ±ÇbnbczipŸ±Ç`a(Ÿ±Ç`caxsŸ±Ç`a[Ÿ±Ç`a:Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia0Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`a[Ÿ±Çbs1a'Ÿ±Çbs1iHillshadeŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1chsvŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1goverlayŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1dsoftŸ±Çbs1a'Ÿ±Ç`a]Ÿ±Ç`a)Ÿ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`jset_ylabelŸ±Ç`a(Ÿ±Ç`dmodeŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dsizeŸ±Çaoa=Ÿ±Çbmib18Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1q# Group labels...Ÿ±Ç`a
Ÿ±Ç`caxsŸ±Ç`a[Ÿ±Çbmia0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia1Ÿ±Ç`a]Ÿ±Çaoa.Ÿ±Ç`hannotateŸ±Ç`a(Ÿ±Çbs1a'Ÿ±Çbs1uVertical ExaggerationŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`a(Ÿ±Çbmfc0.5Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia1Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`fxytextŸ±Çaoa=Ÿ±Ç`a(Ÿ±Çbmia0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmib30Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`s                   Ÿ±Ç`jtextcoordsŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1moffset pointsŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`hxycoordsŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1maxes fractionŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`s                   Ÿ±Ç`bhaŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1fcenterŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`bvaŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1fbottomŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dsizeŸ±Çaoa=Ÿ±Çbmib20Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`caxsŸ±Ç`a[Ÿ±Çbmia2Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia0Ÿ±Ç`a]Ÿ±Çaoa.Ÿ±Ç`hannotateŸ±Ç`a(Ÿ±Çbs1a'Ÿ±Çbs1jBlend ModeŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`a(Ÿ±Çbmia0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfc0.5Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`fxytextŸ±Çaoa=Ÿ±Ç`a(Ÿ±Çaoa-Ÿ±Çbmib30Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia0Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`s                   Ÿ±Ç`jtextcoordsŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1moffset pointsŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`hxycoordsŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1maxes fractionŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`s                   Ÿ±Ç`bhaŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1erightŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`bvaŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1fcenterŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dsizeŸ±Çaoa=Ÿ±Çbmib20Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`hrotationŸ±Çaoa=Ÿ±Çbmib90Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cfigŸ±Çaoa.Ÿ±Ç`osubplots_adjustŸ±Ç`a(Ÿ±Ç`fbottomŸ±Çaoa=Ÿ±Çbmfd0.05Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`erightŸ±Çaoa=Ÿ±Çbmfd0.95Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`dshowŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
`dNoneˆ