Ù¯‚Ù´ƒ™Ù±‚bsdxÃ"""
==============================
Filling the area between lines
==============================

This example shows how to use `~.axes.Axes.fill_between` to color the area
between two lines.
"""Ù±‚`a
Ù±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnnfpyplotÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnncpltÙ±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„enumpyÙ „enumpyf1.22.3fmoduleenumpyfmoduleõÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnnbnpÙ±‚`a
Ù±‚`a
Ù±‚bc1xO###############################################################################Ù±‚`a
Ù±‚bc1a#Ù±‚`a
Ù±‚bc1m# Basic usageÙ±‚`a
Ù±‚bc1m# -----------Ù±‚`a
Ù±‚bc1xF# The parameters *y1* and *y2* can be scalars, indicating a horizontalÙ±‚`a
Ù±‚bc1xL# boundary at the given y-values. If only *y1* is given, *y2* defaults to 0.Ù±‚`a
Ù±‚`a
Ù±‚`axÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`farangeÙ±‚`a(Ù±‚bmfc0.0Ù±‚`a,Ù±‚`a Ù±‚bmia2Ù±‚`a,Ù±‚`a Ù±‚bmfd0.01Ù±‚`a)Ù±‚`a
Ù±‚`by1Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`csinÙ±‚`a(Ù±‚bmia2Ù±‚`a Ù±‚aoa*Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`bpiÙ±‚`a Ù±‚aoa*Ù±‚`a Ù±‚`axÙ±‚`a)Ù±‚`a
Ù±‚`by2Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bmfc0.8Ù±‚`a Ù±‚aoa*Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`csinÙ±‚`a(Ù±‚bmia4Ù±‚`a Ù±‚aoa*Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`bpiÙ±‚`a Ù±‚aoa*Ù±‚`a Ù±‚`axÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`cfigÙ±‚`a,Ù±‚`a Ù±‚`a(Ù±‚`cax1Ù±‚`a,Ù±‚`a Ù±‚`cax2Ù±‚`a,Ù±‚`a Ù±‚`cax3Ù±‚`a)Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cpltÙ±‚aoa.Ù±‚`hsubplotsÙ±‚`a(Ù±‚bmia3Ù±‚`a,Ù±‚`a Ù±‚bmia1Ù±‚`a,Ù±‚`a Ù±‚`fsharexÙ±‚aoa=Ù±‚bkcdTrueÙ±‚`a,Ù±‚`a Ù±‚`gfigsizeÙ±‚aoa=Ù±‚`a(Ù±‚bmia6Ù±‚`a,Ù±‚`a Ù±‚bmia6Ù±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`cax1Ù±‚aoa.Ù±‚`lfill_betweenÙ±‚`a(Ù±‚`axÙ±‚`a,Ù±‚`a Ù±‚`by1Ù±‚`a)Ù±‚`a
Ù±‚`cax1Ù±‚aoa.Ù±‚`iset_titleÙ±‚`a(Ù±‚bs1a'Ù±‚bs1ufill between y1 and 0Ù±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`cax2Ù±‚aoa.Ù±‚`lfill_betweenÙ±‚`a(Ù±‚`axÙ±‚`a,Ù±‚`a Ù±‚`by1Ù±‚`a,Ù±‚`a Ù±‚bmia1Ù±‚`a)Ù±‚`a
Ù±‚`cax2Ù±‚aoa.Ù±‚`iset_titleÙ±‚`a(Ù±‚bs1a'Ù±‚bs1ufill between y1 and 1Ù±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`cax3Ù±‚aoa.Ù±‚`lfill_betweenÙ±‚`a(Ù±‚`axÙ±‚`a,Ù±‚`a Ù±‚`by1Ù±‚`a,Ù±‚`a Ù±‚`by2Ù±‚`a)Ù±‚`a
Ù±‚`cax3Ù±‚aoa.Ù±‚`iset_titleÙ±‚`a(Ù±‚bs1a'Ù±‚bs1vfill between y1 and y2Ù±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`cax3Ù±‚aoa.Ù±‚`jset_xlabelÙ±‚`a(Ù±‚bs1a'Ù±‚bs1axÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`cfigÙ±‚aoa.Ù±‚`ltight_layoutÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚bc1xO###############################################################################Ù±‚`a
Ù±‚bc1a#Ù±‚`a
Ù±‚bc1x# Example: Confidence bandsÙ±‚`a
Ù±‚bc1x# -------------------------Ù±‚`a
Ù±‚bc1xJ# A common application for `~.axes.Axes.fill_between` is the indication ofÙ±‚`a
Ù±‚bc1s# confidence bands.Ù±‚`a
Ù±‚bc1a#Ù±‚`a
Ù±‚bc1xK# `~.axes.Axes.fill_between` uses the colors of the color cycle as the fillÙ±‚`a
Ù±‚bc1xD# color. These may be a bit strong when applied to fill areas. It isÙ±‚`a
Ù±‚bc1xI# therefore often a good practice to lighten the color by making the areaÙ±‚`a
Ù±‚bc1x!# semi-transparent using *alpha*.Ù±‚`a
Ù±‚`a
Ù±‚bc1x%# sphinx_gallery_thumbnail_number = 2Ù±‚`a
Ù±‚`a
Ù±‚`aNÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bmib21Ù±‚`a
Ù±‚`axÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`hlinspaceÙ±‚`a(Ù±‚bmia0Ù±‚`a,Ù±‚`a Ù±‚bmib10Ù±‚`a,Ù±‚`a Ù±‚bmib11Ù±‚`a)Ù±‚`a
Ù±‚`ayÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`a[Ù±‚bmfc3.9Ù±‚`a,Ù±‚`a Ù±‚bmfc4.4Ù±‚`a,Ù±‚`a Ù±‚bmfd10.8Ù±‚`a,Ù±‚`a Ù±‚bmfd10.3Ù±‚`a,Ù±‚`a Ù±‚bmfd11.2Ù±‚`a,Ù±‚`a Ù±‚bmfd13.1Ù±‚`a,Ù±‚`a Ù±‚bmfd14.1Ù±‚`a,Ù±‚`b  Ù±‚bmfc9.9Ù±‚`a,Ù±‚`a Ù±‚bmfd13.9Ù±‚`a,Ù±‚`a Ù±‚bmfd15.1Ù±‚`a,Ù±‚`a Ù±‚bmfd12.5Ù±‚`a]Ù±‚`a
Ù±‚`a
Ù±‚bc1x># fit a linear curve an estimate its y-values and their error.Ù±‚`a
Ù±‚`aaÙ±‚`a,Ù±‚`a Ù±‚`abÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`gpolyfitÙ±‚`a(Ù±‚`axÙ±‚`a,Ù±‚`a Ù±‚`ayÙ±‚`a,Ù±‚`a Ù±‚`cdegÙ±‚aoa=Ù±‚bmia1Ù±‚`a)Ù±‚`a
Ù±‚`ey_estÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`aaÙ±‚`a Ù±‚aoa*Ù±‚`a Ù±‚`axÙ±‚`a Ù±‚aoa+Ù±‚`a Ù±‚`abÙ±‚`a
Ù±‚`ey_errÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`axÙ±‚aoa.Ù±‚`cstdÙ±‚`a(Ù±‚`a)Ù±‚`a Ù±‚aoa*Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`dsqrtÙ±‚`a(Ù±‚bmia1Ù±‚aoa/Ù±‚bnbclenÙ±‚`a(Ù±‚`axÙ±‚`a)Ù±‚`a Ù±‚aoa+Ù±‚`a
Ù±‚`x                          Ù±‚`a(Ù±‚`axÙ±‚`a Ù±‚aoa-Ù±‚`a Ù±‚`axÙ±‚aoa.Ù±‚`dmeanÙ±‚`a(Ù±‚`a)Ù±‚`a)Ù±‚aoa*Ù±‚aoa*Ù±‚bmia2Ù±‚`a Ù±‚aoa/Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`csumÙ±‚`a(Ù±‚`a(Ù±‚`axÙ±‚`a Ù±‚aoa-Ù±‚`a Ù±‚`axÙ±‚aoa.Ù±‚`dmeanÙ±‚`a(Ù±‚`a)Ù±‚`a)Ù±‚aoa*Ù±‚aoa*Ù±‚bmia2Ù±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`cfigÙ±‚`a,Ù±‚`a Ù±‚`baxÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cpltÙ±‚aoa.Ù±‚`hsubplotsÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`dplotÙ±‚`a(Ù±‚`axÙ±‚`a,Ù±‚`a Ù±‚`ey_estÙ±‚`a,Ù±‚`a Ù±‚bs1a'Ù±‚bs1a-Ù±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`lfill_betweenÙ±‚`a(Ù±‚`axÙ±‚`a,Ù±‚`a Ù±‚`ey_estÙ±‚`a Ù±‚aoa-Ù±‚`a Ù±‚`ey_errÙ±‚`a,Ù±‚`a Ù±‚`ey_estÙ±‚`a Ù±‚aoa+Ù±‚`a Ù±‚`ey_errÙ±‚`a,Ù±‚`a Ù±‚`ealphaÙ±‚aoa=Ù±‚bmfc0.2Ù±‚`a)Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`dplotÙ±‚`a(Ù±‚`axÙ±‚`a,Ù±‚`a Ù±‚`ayÙ±‚`a,Ù±‚`a Ù±‚bs1a'Ù±‚bs1aoÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`ecolorÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1itab:brownÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚bc1xO###############################################################################Ù±‚`a
Ù±‚bc1a#Ù±‚`a
Ù±‚bc1x(# Selectively filling horizontal regionsÙ±‚`a
Ù±‚bc1x(# --------------------------------------Ù±‚`a
Ù±‚bc1xN# The parameter *where* allows to specify the x-ranges to fill. It's a booleanÙ±‚`a
Ù±‚bc1x"# array with the same size as *x*.Ù±‚`a
Ù±‚bc1a#Ù±‚`a
Ù±‚bc1xJ# Only x-ranges of contiguous *True* sequences are filled. As a result theÙ±‚`a
Ù±‚bc1xK# range between neighboring *True* and *False* values is never filled. ThisÙ±‚`a
Ù±‚bc1xN# often undesired when the data points should represent a contiguous quantity.Ù±‚`a
Ù±‚bc1xD# It is therefore recommended to set ``interpolate=True`` unless theÙ±‚`a
Ù±‚bc1xN# x-distance of the data points is fine enough so that the above effect is notÙ±‚`a
Ù±‚bc1xK# noticeable. Interpolation approximates the actual x position at which theÙ±‚`a
Ù±‚bc1xD# *where* condition will change and extends the filling up to there.Ù±‚`a
Ù±‚`a
Ù±‚`axÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`earrayÙ±‚`a(Ù±‚`a[Ù±‚bmia0Ù±‚`a,Ù±‚`a Ù±‚bmia1Ù±‚`a,Ù±‚`a Ù±‚bmia2Ù±‚`a,Ù±‚`a Ù±‚bmia3Ù±‚`a]Ù±‚`a)Ù±‚`a
Ù±‚`by1Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`earrayÙ±‚`a(Ù±‚`a[Ù±‚bmfc0.8Ù±‚`a,Ù±‚`a Ù±‚bmfc0.8Ù±‚`a,Ù±‚`a Ù±‚bmfc0.2Ù±‚`a,Ù±‚`a Ù±‚bmfc0.2Ù±‚`a]Ù±‚`a)Ù±‚`a
Ù±‚`by2Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`earrayÙ±‚`a(Ù±‚`a[Ù±‚bmia0Ù±‚`a,Ù±‚`a Ù±‚bmia0Ù±‚`a,Ù±‚`a Ù±‚bmia1Ù±‚`a,Ù±‚`a Ù±‚bmia1Ù±‚`a]Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`cfigÙ±‚`a,Ù±‚`a Ù±‚`a(Ù±‚`cax1Ù±‚`a,Ù±‚`a Ù±‚`cax2Ù±‚`a)Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cpltÙ±‚aoa.Ù±‚`hsubplotsÙ±‚`a(Ù±‚bmia2Ù±‚`a,Ù±‚`a Ù±‚bmia1Ù±‚`a,Ù±‚`a Ù±‚`fsharexÙ±‚aoa=Ù±‚bkcdTrueÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`cax1Ù±‚aoa.Ù±‚`iset_titleÙ±‚`a(Ù±‚bs1a'Ù±‚bs1sinterpolation=FalseÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`cax1Ù±‚aoa.Ù±‚`dplotÙ±‚`a(Ù±‚`axÙ±‚`a,Ù±‚`a Ù±‚`by1Ù±‚`a,Ù±‚`a Ù±‚bs1a'Ù±‚bs1co--Ù±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`cax1Ù±‚aoa.Ù±‚`dplotÙ±‚`a(Ù±‚`axÙ±‚`a,Ù±‚`a Ù±‚`by2Ù±‚`a,Ù±‚`a Ù±‚bs1a'Ù±‚bs1co--Ù±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`cax1Ù±‚aoa.Ù±‚`lfill_betweenÙ±‚`a(Ù±‚`axÙ±‚`a,Ù±‚`a Ù±‚`by1Ù±‚`a,Ù±‚`a Ù±‚`by2Ù±‚`a,Ù±‚`a Ù±‚`ewhereÙ±‚aoa=Ù±‚`a(Ù±‚`by1Ù±‚`a Ù±‚aoa>Ù±‚`a Ù±‚`by2Ù±‚`a)Ù±‚`a,Ù±‚`a Ù±‚`ecolorÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1bC0Ù±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`ealphaÙ±‚aoa=Ù±‚bmfc0.3Ù±‚`a)Ù±‚`a
Ù±‚`cax1Ù±‚aoa.Ù±‚`lfill_betweenÙ±‚`a(Ù±‚`axÙ±‚`a,Ù±‚`a Ù±‚`by1Ù±‚`a,Ù±‚`a Ù±‚`by2Ù±‚`a,Ù±‚`a Ù±‚`ewhereÙ±‚aoa=Ù±‚`a(Ù±‚`by1Ù±‚`a Ù±‚aoa<Ù±‚`a Ù±‚`by2Ù±‚`a)Ù±‚`a,Ù±‚`a Ù±‚`ecolorÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1bC1Ù±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`ealphaÙ±‚aoa=Ù±‚bmfc0.3Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`cax2Ù±‚aoa.Ù±‚`iset_titleÙ±‚`a(Ù±‚bs1a'Ù±‚bs1rinterpolation=TrueÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`cax2Ù±‚aoa.Ù±‚`dplotÙ±‚`a(Ù±‚`axÙ±‚`a,Ù±‚`a Ù±‚`by1Ù±‚`a,Ù±‚`a Ù±‚bs1a'Ù±‚bs1co--Ù±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`cax2Ù±‚aoa.Ù±‚`dplotÙ±‚`a(Ù±‚`axÙ±‚`a,Ù±‚`a Ù±‚`by2Ù±‚`a,Ù±‚`a Ù±‚bs1a'Ù±‚bs1co--Ù±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`cax2Ù±‚aoa.Ù±‚`lfill_betweenÙ±‚`a(Ù±‚`axÙ±‚`a,Ù±‚`a Ù±‚`by1Ù±‚`a,Ù±‚`a Ù±‚`by2Ù±‚`a,Ù±‚`a Ù±‚`ewhereÙ±‚aoa=Ù±‚`a(Ù±‚`by1Ù±‚`a Ù±‚aoa>Ù±‚`a Ù±‚`by2Ù±‚`a)Ù±‚`a,Ù±‚`a Ù±‚`ecolorÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1bC0Ù±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`ealphaÙ±‚aoa=Ù±‚bmfc0.3Ù±‚`a,Ù±‚`a
Ù±‚`q                 Ù±‚`kinterpolateÙ±‚aoa=Ù±‚bkcdTrueÙ±‚`a)Ù±‚`a
Ù±‚`cax2Ù±‚aoa.Ù±‚`lfill_betweenÙ±‚`a(Ù±‚`axÙ±‚`a,Ù±‚`a Ù±‚`by1Ù±‚`a,Ù±‚`a Ù±‚`by2Ù±‚`a,Ù±‚`a Ù±‚`ewhereÙ±‚aoa=Ù±‚`a(Ù±‚`by1Ù±‚`a Ù±‚aoa<Ù±‚aoa=Ù±‚`a Ù±‚`by2Ù±‚`a)Ù±‚`a,Ù±‚`a Ù±‚`ecolorÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1bC1Ù±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`ealphaÙ±‚aoa=Ù±‚bmfc0.3Ù±‚`a,Ù±‚`a
Ù±‚`q                 Ù±‚`kinterpolateÙ±‚aoa=Ù±‚bkcdTrueÙ±‚`a)Ù±‚`a
Ù±‚`cfigÙ±‚aoa.Ù±‚`ltight_layoutÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚bc1xO###############################################################################Ù±‚`a
Ù±‚bc1a#Ù±‚`a
Ù±‚bc1k# .. note::Ù±‚`a
Ù±‚bc1a#Ù±‚`a
Ù±‚bc1xM#    Similar gaps will occur if *y1* or *y2* are masked arrays. Since missingÙ±‚`a
Ù±‚bc1xM#    values cannot be approximated, *interpolate* has no effect in this case.Ù±‚`a
Ù±‚bc1xJ#    The gaps around masked values can only be reduced by adding more dataÙ±‚`a
Ù±‚bc1x'#    points close to the masked values.Ù±‚`a
Ù±‚`a
Ù±‚bc1xO###############################################################################Ù±‚`a
Ù±‚bc1a#Ù±‚`a
Ù±‚bc1x># Selectively marking horizontal regions across the whole AxesÙ±‚`a
Ù±‚bc1x># ------------------------------------------------------------Ù±‚`a
Ù±‚bc1xN# The same selection mechanism can be applied to fill the full vertical heightÙ±‚`a
Ù±‚bc1xE# of the axes. To be independent of y-limits, we add a transform thatÙ±‚`a
Ù±‚bc1xF# interprets the x-values in data coorindates and the y-values in axesÙ±‚`a
Ù±‚bc1n# coordinates.Ù±‚`a
Ù±‚bc1a#Ù±‚`a
Ù±‚bc1xI# The following example marks the regions in which the y-data are above aÙ±‚`a
Ù±‚bc1r# given threshold.Ù±‚`a
Ù±‚`a
Ù±‚`cfigÙ±‚`a,Ù±‚`a Ù±‚`baxÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cpltÙ±‚aoa.Ù±‚`hsubplotsÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`axÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`farangeÙ±‚`a(Ù±‚bmia0Ù±‚`a,Ù±‚`a Ù±‚bmia4Ù±‚`a Ù±‚aoa*Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`bpiÙ±‚`a,Ù±‚`a Ù±‚bmfd0.01Ù±‚`a)Ù±‚`a
Ù±‚`ayÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`csinÙ±‚`a(Ù±‚`axÙ±‚`a)Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`dplotÙ±‚`a(Ù±‚`axÙ±‚`a,Ù±‚`a Ù±‚`ayÙ±‚`a,Ù±‚`a Ù±‚`ecolorÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1eblackÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`ithresholdÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bmfd0.75Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`gaxhlineÙ±‚`a(Ù±‚`ithresholdÙ±‚`a,Ù±‚`a Ù±‚`ecolorÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1egreenÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`blwÙ±‚aoa=Ù±‚bmia2Ù±‚`a,Ù±‚`a Ù±‚`ealphaÙ±‚aoa=Ù±‚bmfc0.7Ù±‚`a)Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`lfill_betweenÙ±‚`a(Ù±‚`axÙ±‚`a,Ù±‚`a Ù±‚bmia0Ù±‚`a,Ù±‚`a Ù±‚bmia1Ù±‚`a,Ù±‚`a Ù±‚`ewhereÙ±‚aoa=Ù±‚`ayÙ±‚`a Ù±‚aoa>Ù±‚`a Ù±‚`ithresholdÙ±‚`a,Ù±‚`a
Ù±‚`p                Ù±‚`ecolorÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1egreenÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`ealphaÙ±‚aoa=Ù±‚bmfc0.5Ù±‚`a,Ù±‚`a Ù±‚`itransformÙ±‚aoa=Ù±‚`baxÙ±‚aoa.Ù±‚`sget_xaxis_transformÙ±‚`a(Ù±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚bc1xM#############################################################################Ù±‚`a
Ù±‚bc1a#Ù±‚`a
Ù±‚bc1x# .. admonition:: ReferencesÙ±‚`a
Ù±‚bc1a#Ù±‚`a
Ù±‚bc1xN#    The use of the following functions, methods, classes and modules is shownÙ±‚`a
Ù±‚bc1u#    in this example:Ù±‚`a
Ù±‚bc1a#Ù±‚`a
Ù±‚bc1xM#    - `matplotlib.axes.Axes.fill_between` / `matplotlib.pyplot.fill_between`Ù±‚`a
Ù±‚bc1x1#    - `matplotlib.axes.Axes.get_xaxis_transform`Ù±‚`a
`dNoneö