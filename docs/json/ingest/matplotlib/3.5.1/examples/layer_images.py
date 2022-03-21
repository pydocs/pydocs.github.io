Ù¯‚Ù´ƒ™bÙ±‚bsdxc"""
============
Layer Images
============

Layer images above one another using alpha blending
"""Ù±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnnfpyplotÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnncpltÙ±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„enumpyÙ „enumpyf1.22.3fmoduleenumpyfmoduleõÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnnbnpÙ±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚akcdefÙ±‚`a Ù±‚bnfefunc3Ù±‚`a(Ù±‚`axÙ±‚`a,Ù±‚`a Ù±‚`ayÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`d    Ù±‚akfreturnÙ±‚`a Ù±‚`a(Ù±‚bmia1Ù±‚`a Ù±‚aoa-Ù±‚`a Ù±‚`axÙ±‚`a Ù±‚aoa/Ù±‚`a Ù±‚bmia2Ù±‚`a Ù±‚aoa+Ù±‚`a Ù±‚`axÙ±‚aoa*Ù±‚aoa*Ù±‚bmia5Ù±‚`a Ù±‚aoa+Ù±‚`a Ù±‚`ayÙ±‚aoa*Ù±‚aoa*Ù±‚bmia3Ù±‚`a)Ù±‚`a Ù±‚aoa*Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`cexpÙ±‚`a(Ù±‚aoa-Ù±‚`a(Ù±‚`axÙ±‚aoa*Ù±‚aoa*Ù±‚bmia2Ù±‚`a Ù±‚aoa+Ù±‚`a Ù±‚`ayÙ±‚aoa*Ù±‚aoa*Ù±‚bmia2Ù±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚bc1x/# make these smaller to increase the resolutionÙ±‚`a
Ù±‚`bdxÙ±‚`a,Ù±‚`a Ù±‚`bdyÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bmfd0.05Ù±‚`a,Ù±‚`a Ù±‚bmfd0.05Ù±‚`a
Ù±‚`a
Ù±‚`axÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`farangeÙ±‚`a(Ù±‚aoa-Ù±‚bmfc3.0Ù±‚`a,Ù±‚`a Ù±‚bmfc3.0Ù±‚`a,Ù±‚`a Ù±‚`bdxÙ±‚`a)Ù±‚`a
Ù±‚`ayÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`farangeÙ±‚`a(Ù±‚aoa-Ù±‚bmfc3.0Ù±‚`a,Ù±‚`a Ù±‚bmfc3.0Ù±‚`a,Ù±‚`a Ù±‚`bdyÙ±‚`a)Ù±‚`a
Ù±‚`aXÙ±‚`a,Ù±‚`a Ù±‚`aYÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`hmeshgridÙ±‚`a(Ù±‚`axÙ±‚`a,Ù±‚`a Ù±‚`ayÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚bc1xA# when layering multiple images, the images need to have the sameÙ±‚`a
Ù±‚bc1xC# extent.  This does not mean they need to have the same shape, butÙ±‚`a
Ù±‚bc1xF# they both need to render to the same coordinate system determined byÙ±‚`a
Ù±‚bc1xC# xmin, xmax, ymin, ymax.  Note if you use different interpolationsÙ±‚`a
Ù±‚bc1x@# for the images their apparent extent could be different due toÙ±‚`a
Ù±‚bc1x# interpolation edge effectsÙ±‚`a
Ù±‚`a
Ù±‚`fextentÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`cminÙ±‚`a(Ù±‚`axÙ±‚`a)Ù±‚`a,Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`cmaxÙ±‚`a(Ù±‚`axÙ±‚`a)Ù±‚`a,Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`cminÙ±‚`a(Ù±‚`ayÙ±‚`a)Ù±‚`a,Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`cmaxÙ±‚`a(Ù±‚`ayÙ±‚`a)Ù±‚`a
Ù±‚`cfigÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cpltÙ±‚aoa.Ù±‚`ffigureÙ±‚`a(Ù±‚`gframeonÙ±‚aoa=Ù±‚bkceFalseÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`bZ1Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`caddÙ±‚aoa.Ù±‚`eouterÙ±‚`a(Ù±‚bnberangeÙ±‚`a(Ù±‚bmia8Ù±‚`a)Ù±‚`a,Ù±‚`a Ù±‚bnberangeÙ±‚`a(Ù±‚bmia8Ù±‚`a)Ù±‚`a)Ù±‚`a Ù±‚aoa%Ù±‚`a Ù±‚bmia2Ù±‚`b  Ù±‚bc1l# chessboardÙ±‚`a
Ù±‚`cim1Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cpltÙ±‚aoa.Ù±‚`fimshowÙ±‚`a(Ù±‚`bZ1Ù±‚`a,Ù±‚`a Ù±‚`dcmapÙ±‚aoa=Ù±‚`cpltÙ±‚aoa.Ù±‚`bcmÙ±‚aoa.Ù±‚`dgrayÙ±‚`a,Ù±‚`a Ù±‚`minterpolationÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1gnearestÙ±‚bs1a'Ù±‚`a,Ù±‚`a
Ù±‚`q                 Ù±‚`fextentÙ±‚aoa=Ù±‚`fextentÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`bZ2Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`efunc3Ù±‚`a(Ù±‚`aXÙ±‚`a,Ù±‚`a Ù±‚`aYÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`cim2Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cpltÙ±‚aoa.Ù±‚`fimshowÙ±‚`a(Ù±‚`bZ2Ù±‚`a,Ù±‚`a Ù±‚`dcmapÙ±‚aoa=Ù±‚`cpltÙ±‚aoa.Ù±‚`bcmÙ±‚aoa.Ù±‚`gviridisÙ±‚`a,Ù±‚`a Ù±‚`ealphaÙ±‚aoa=Ù±‚bmfb.9Ù±‚`a,Ù±‚`a Ù±‚`minterpolationÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1hbilinearÙ±‚bs1a'Ù±‚`a,Ù±‚`a
Ù±‚`q                 Ù±‚`fextentÙ±‚aoa=Ù±‚`fextentÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`cpltÙ±‚aoa.Ù±‚`dshowÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚bc1xM#############################################################################Ù±‚`a
Ù±‚bc1a#Ù±‚`a
Ù±‚bc1x# .. admonition:: ReferencesÙ±‚`a
Ù±‚bc1a#Ù±‚`a
Ù±‚bc1xN#    The use of the following functions, methods, classes and modules is shownÙ±‚`a
Ù±‚bc1u#    in this example:Ù±‚`a
Ù±‚bc1a#Ù±‚`a
Ù±‚bc1xA#    - `matplotlib.axes.Axes.imshow` / `matplotlib.pyplot.imshow`Ù±‚`a
`dNoneö