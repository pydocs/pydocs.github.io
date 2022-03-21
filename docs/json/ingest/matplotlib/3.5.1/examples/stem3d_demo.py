Ù¯‚Ù´ƒ™RÙ±‚bsdx¥"""
=======
3D stem
=======

Demonstration of a stem plot in 3D, which plots vertical lines from a baseline
to the *z*-coordinate and places a marker at the tip.
"""Ù±‚`a
Ù±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnnfpyplotÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnncpltÙ±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„enumpyÙ „enumpyf1.22.3fmoduleenumpyfmoduleõÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnnbnpÙ±‚`a
Ù±‚`a
Ù±‚`ethetaÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`hlinspaceÙ±‚`a(Ù±‚bmia0Ù±‚`a,Ù±‚`a Ù±‚bmia2Ù±‚aoa*Ù±‚`bnpÙ±‚aoa.Ù±‚`bpiÙ±‚`a)Ù±‚`a
Ù±‚`axÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`ccosÙ±‚`a(Ù±‚`ethetaÙ±‚`a Ù±‚aoa-Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`bpiÙ±‚aoa/Ù±‚bmia2Ù±‚`a)Ù±‚`a
Ù±‚`ayÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`csinÙ±‚`a(Ù±‚`ethetaÙ±‚`a Ù±‚aoa-Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`bpiÙ±‚aoa/Ù±‚bmia2Ù±‚`a)Ù±‚`a
Ù±‚`azÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`ethetaÙ±‚`a
Ù±‚`a
Ù±‚`cfigÙ±‚`a,Ù±‚`a Ù±‚`baxÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cpltÙ±‚aoa.Ù±‚`hsubplotsÙ±‚`a(Ù±‚`jsubplot_kwÙ±‚aoa=Ù±‚bnbddictÙ±‚`a(Ù±‚`jprojectionÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1b3dÙ±‚bs1a'Ù±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`dstemÙ±‚`a(Ù±‚`axÙ±‚`a,Ù±‚`a Ù±‚`ayÙ±‚`a,Ù±‚`a Ù±‚`azÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`cpltÙ±‚aoa.Ù±‚`dshowÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚bc1xM#############################################################################Ù±‚`a
Ù±‚bc1a#Ù±‚`a
Ù±‚bc1xL# The position of the baseline can be adapted using *bottom*. The parametersÙ±‚`a
Ù±‚bc1xN# *linefmt*, *markerfmt*, and *basefmt* control basic format properties of theÙ±‚`a
Ù±‚bc1xM# plot. However, in contrast to `~.axes3d.Axes3D.plot` not all properties areÙ±‚`a
Ù±‚bc1xN# configurable via keyword arguments. For more advanced control adapt the lineÙ±‚`a
Ù±‚bc1x # objects returned by `.stem3D`.Ù±‚`a
Ù±‚`a
Ù±‚`cfigÙ±‚`a,Ù±‚`a Ù±‚`baxÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cpltÙ±‚aoa.Ù±‚`hsubplotsÙ±‚`a(Ù±‚`jsubplot_kwÙ±‚aoa=Ù±‚bnbddictÙ±‚`a(Ù±‚`jprojectionÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1b3dÙ±‚bs1a'Ù±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`jmarkerlineÙ±‚`a,Ù±‚`a Ù±‚`istemlinesÙ±‚`a,Ù±‚`a Ù±‚`hbaselineÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`baxÙ±‚aoa.Ù±‚`dstemÙ±‚`a(Ù±‚`a
Ù±‚`d    Ù±‚`axÙ±‚`a,Ù±‚`a Ù±‚`ayÙ±‚`a,Ù±‚`a Ù±‚`azÙ±‚`a,Ù±‚`a Ù±‚`glinefmtÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1dgreyÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`imarkerfmtÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1aDÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`fbottomÙ±‚aoa=Ù±‚`bnpÙ±‚aoa.Ù±‚`bpiÙ±‚`a)Ù±‚`a
Ù±‚`jmarkerlineÙ±‚aoa.Ù±‚`sset_markerfacecolorÙ±‚`a(Ù±‚bs1a'Ù±‚bs1dnoneÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`cpltÙ±‚aoa.Ù±‚`dshowÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚bc1xM#############################################################################Ù±‚`a
Ù±‚bc1a#Ù±‚`a
Ù±‚bc1xO# The orientation of the stems and baseline can be changed using *orientation*.Ù±‚`a
Ù±‚bc1xJ# This determines in which direction the stems are projected from the headÙ±‚`a
Ù±‚bc1x(# points, towards the *bottom* baseline.Ù±‚`a
Ù±‚bc1a#Ù±‚`a
Ù±‚bc1xM# For examples, by setting ``orientation='x'``, the stems are projected alongÙ±‚`a
Ù±‚bc1x;# the *x*-direction, and the baseline is in the *yz*-plane.Ù±‚`a
Ù±‚`a
Ù±‚`cfigÙ±‚`a,Ù±‚`a Ù±‚`baxÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cpltÙ±‚aoa.Ù±‚`hsubplotsÙ±‚`a(Ù±‚`jsubplot_kwÙ±‚aoa=Ù±‚bnbddictÙ±‚`a(Ù±‚`jprojectionÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1b3dÙ±‚bs1a'Ù±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`jmarkerlineÙ±‚`a,Ù±‚`a Ù±‚`istemlinesÙ±‚`a,Ù±‚`a Ù±‚`hbaselineÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`baxÙ±‚aoa.Ù±‚`dstemÙ±‚`a(Ù±‚`axÙ±‚`a,Ù±‚`a Ù±‚`ayÙ±‚`a,Ù±‚`a Ù±‚`azÙ±‚`a,Ù±‚`a Ù±‚`fbottomÙ±‚aoa=Ù±‚aoa-Ù±‚bmia1Ù±‚`a,Ù±‚`a Ù±‚`korientationÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1axÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`csetÙ±‚`a(Ù±‚`fxlabelÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1axÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`fylabelÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1ayÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`fzlabelÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1azÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`cpltÙ±‚aoa.Ù±‚`dshowÙ±‚`a(Ù±‚`a)Ù±‚`a
`dNoneö