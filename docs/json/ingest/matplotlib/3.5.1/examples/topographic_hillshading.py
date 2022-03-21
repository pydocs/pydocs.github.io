������������bsdy�"""
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
"""���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���bkndfrom���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnecbook���`a ���bknfimport���`a ���`oget_sample_data���`a
���bkndfrom���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfcolors���`a ���bknfimport���`a ���`kLightSource���`a
���`a
���`a
���`cdem���`a ���aoa=���`a ���`oget_sample_data���`a(���bs1a'���bs1wjacksboro_fault_dem.npz���bs1a'���`a,���`a ���`gnp_load���aoa=���bkcdTrue���`a)���`a
���`az���`a ���aoa=���`a ���`cdem���`a[���bs1a'���bs1ielevation���bs1a'���`a]���`a
���bc1xO# -- Optional dx and dy for accurate vertical exaggeration --------------------���`a
���bc1xO# If you need topographically accurate vertical exaggeration, or you don't want���`a
���bc1xM# to guess at what *vert_exag* should be, you'll need to specify the cellsize���`a
���bc1xN# of the grid (i.e. the *dx* and *dy* parameters).  Otherwise, any *vert_exag*���`a
���bc1xK# value you specify will be relative to the grid spacing of your input data���`a
���bc1xN# (in other words, *dx* and *dy* default to 1.0, and *vert_exag* is calculated���`a
���bc1xO# relative to those parameters).  Similarly, *dx* and *dy* are assumed to be in���`a
���bc1xN# the same units as your input z-values.  Therefore, we'll need to convert the���`a
���bc1x1# given dx and dy from decimal degrees to meters.���`a
���`bdx���`a,���`a ���`bdy���`a ���aoa=���`a ���`cdem���`a[���bs1a'���bs1bdx���bs1a'���`a]���`a,���`a ���`cdem���`a[���bs1a'���bs1bdy���bs1a'���`a]���`a
���`bdy���`a ���aoa=���`a ���bmif111200���`a ���aoa*���`a ���`bdy���`a
���`bdx���`a ���aoa=���`a ���bmif111200���`a ���aoa*���`a ���`bdx���`a ���aoa*���`a ���`bnp���aoa.���`ccos���`a(���`bnp���aoa.���`gradians���`a(���`cdem���`a[���bs1a'���bs1dymin���bs1a'���`a]���`a)���`a)���`a
���bc1xO# -----------------------------------------------------------------------------���`a
���`a
���bc1xC# Shade from the northwest, with the sun 45 degrees from horizontal���`a
���`bls���`a ���aoa=���`a ���`kLightSource���`a(���`eazdeg���aoa=���bmic315���`a,���`a ���`faltdeg���aoa=���bmib45���`a)���`a
���`dcmap���`a ���aoa=���`a ���`cplt���aoa.���`bcm���aoa.���`jgist_earth���`a
���`a
���`cfig���`a,���`a ���`caxs���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`enrows���aoa=���bmia4���`a,���`a ���`encols���aoa=���bmia3���`a,���`a ���`gfigsize���aoa=���`a(���bmia8���`a,���`a ���bmia9���`a)���`a)���`a
���`cplt���aoa.���`dsetp���`a(���`caxs���aoa.���`dflat���`a,���`a ���`fxticks���aoa=���`a[���`a]���`a,���`a ���`fyticks���aoa=���`a[���`a]���`a)���`a
���`a
���bc1xE# Vary vertical exaggeration and blend mode and plot all combinations���`a
���akcfor���`a ���`ccol���`a,���`a ���`bve���`a ���bowbin���`a ���bnbczip���`a(���`caxs���aoa.���`aT���`a,���`a ���`a[���bmfc0.1���`a,���`a ���bmia1���`a,���`a ���bmib10���`a]���`a)���`a:���`a
���`d    ���bc1x5# Show the hillshade intensity image in the first row���`a
���`d    ���`ccol���`a[���bmia0���`a]���aoa.���`fimshow���`a(���`bls���aoa.���`ihillshade���`a(���`az���`a,���`a ���`ivert_exag���aoa=���`bve���`a,���`a ���`bdx���aoa=���`bdx���`a,���`a ���`bdy���aoa=���`bdy���`a)���`a,���`a ���`dcmap���aoa=���bs1a'���bs1dgray���bs1a'���`a)���`a
���`a
���`d    ���bc1xK# Place hillshaded plots with different blend modes in the rest of the rows���`a
���`d    ���akcfor���`a ���`bax���`a,���`a ���`dmode���`a ���bowbin���`a ���bnbczip���`a(���`ccol���`a[���bmia1���`a:���`a]���`a,���`a ���`a[���bs1a'���bs1chsv���bs1a'���`a,���`a ���bs1a'���bs1goverlay���bs1a'���`a,���`a ���bs1a'���bs1dsoft���bs1a'���`a]���`a)���`a:���`a
���`h        ���`crgb���`a ���aoa=���`a ���`bls���aoa.���`eshade���`a(���`az���`a,���`a ���`dcmap���aoa=���`dcmap���`a,���`a ���`jblend_mode���aoa=���`dmode���`a,���`a
���`w                       ���`ivert_exag���aoa=���`bve���`a,���`a ���`bdx���aoa=���`bdx���`a,���`a ���`bdy���aoa=���`bdy���`a)���`a
���`h        ���`bax���aoa.���`fimshow���`a(���`crgb���`a)���`a
���`a
���bc1x# Label rows and columns���`a
���akcfor���`a ���`bax���`a,���`a ���`bve���`a ���bowbin���`a ���bnbczip���`a(���`caxs���`a[���bmia0���`a]���`a,���`a ���`a[���bmfc0.1���`a,���`a ���bmia1���`a,���`a ���bmib10���`a]���`a)���`a:���`a
���`d    ���`bax���aoa.���`iset_title���`a(���bs1a'���bsic{0}���bs1a'���aoa.���`fformat���`a(���`bve���`a)���`a,���`a ���`dsize���aoa=���bmib18���`a)���`a
���akcfor���`a ���`bax���`a,���`a ���`dmode���`a ���bowbin���`a ���bnbczip���`a(���`caxs���`a[���`a:���`a,���`a ���bmia0���`a]���`a,���`a ���`a[���bs1a'���bs1iHillshade���bs1a'���`a,���`a ���bs1a'���bs1chsv���bs1a'���`a,���`a ���bs1a'���bs1goverlay���bs1a'���`a,���`a ���bs1a'���bs1dsoft���bs1a'���`a]���`a)���`a:���`a
���`d    ���`bax���aoa.���`jset_ylabel���`a(���`dmode���`a,���`a ���`dsize���aoa=���bmib18���`a)���`a
���`a
���bc1q# Group labels...���`a
���`caxs���`a[���bmia0���`a,���`a ���bmia1���`a]���aoa.���`hannotate���`a(���bs1a'���bs1uVertical Exaggeration���bs1a'���`a,���`a ���`a(���bmfc0.5���`a,���`a ���bmia1���`a)���`a,���`a ���`fxytext���aoa=���`a(���bmia0���`a,���`a ���bmib30���`a)���`a,���`a
���`s                   ���`jtextcoords���aoa=���bs1a'���bs1moffset points���bs1a'���`a,���`a ���`hxycoords���aoa=���bs1a'���bs1maxes fraction���bs1a'���`a,���`a
���`s                   ���`bha���aoa=���bs1a'���bs1fcenter���bs1a'���`a,���`a ���`bva���aoa=���bs1a'���bs1fbottom���bs1a'���`a,���`a ���`dsize���aoa=���bmib20���`a)���`a
���`caxs���`a[���bmia2���`a,���`a ���bmia0���`a]���aoa.���`hannotate���`a(���bs1a'���bs1jBlend Mode���bs1a'���`a,���`a ���`a(���bmia0���`a,���`a ���bmfc0.5���`a)���`a,���`a ���`fxytext���aoa=���`a(���aoa-���bmib30���`a,���`a ���bmia0���`a)���`a,���`a
���`s                   ���`jtextcoords���aoa=���bs1a'���bs1moffset points���bs1a'���`a,���`a ���`hxycoords���aoa=���bs1a'���bs1maxes fraction���bs1a'���`a,���`a
���`s                   ���`bha���aoa=���bs1a'���bs1eright���bs1a'���`a,���`a ���`bva���aoa=���bs1a'���bs1fcenter���bs1a'���`a,���`a ���`dsize���aoa=���bmib20���`a,���`a ���`hrotation���aoa=���bmib90���`a)���`a
���`cfig���aoa.���`osubplots_adjust���`a(���`fbottom���aoa=���bmfd0.05���`a,���`a ���`eright���aoa=���bmfd0.95���`a)���`a
���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
`dNone�