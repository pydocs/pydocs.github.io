Ù¯‚Ù´ƒ˜ùÙ±‚bsdxÉ"""
============
axhspan Demo
============

Create lines or rectangles that span the axes in either the horizontal or
vertical direction, and lines than span the axes with an arbitrary orientation.
"""Ù±‚`a
Ù±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„enumpyÙ „enumpyf1.22.3fmoduleenumpyfmoduleõÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnnbnpÙ±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnnfpyplotÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnncpltÙ±‚`a
Ù±‚`a
Ù±‚`atÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`farangeÙ±‚`a(Ù±‚aoa-Ù±‚bmia1Ù±‚`a,Ù±‚`a Ù±‚bmia2Ù±‚`a,Ù±‚`a Ù±‚bmfc.01Ù±‚`a)Ù±‚`a
Ù±‚`asÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`csinÙ±‚`a(Ù±‚bmia2Ù±‚`a Ù±‚aoa*Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`bpiÙ±‚`a Ù±‚aoa*Ù±‚`a Ù±‚`atÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`cfigÙ±‚`a,Ù±‚`a Ù±‚`baxÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cpltÙ±‚aoa.Ù±‚`hsubplotsÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`dplotÙ±‚`a(Ù±‚`atÙ±‚`a,Ù±‚`a Ù±‚`asÙ±‚`a)Ù±‚`a
Ù±‚bc1x9# Thick red horizontal line at y=0 that spans the xrange.Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`gaxhlineÙ±‚`a(Ù±‚`ilinewidthÙ±‚aoa=Ù±‚bmia8Ù±‚`a,Ù±‚`a Ù±‚`ecolorÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1g#d62728Ù±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚bc1x/# Horizontal line at y=1 that spans the xrange.Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`gaxhlineÙ±‚`a(Ù±‚`ayÙ±‚aoa=Ù±‚bmia1Ù±‚`a)Ù±‚`a
Ù±‚bc1x-# Vertical line at x=1 that spans the yrange.Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`gaxvlineÙ±‚`a(Ù±‚`axÙ±‚aoa=Ù±‚bmia1Ù±‚`a)Ù±‚`a
Ù±‚bc1xN# Thick blue vertical line at x=0 that spans the upper quadrant of the yrange.Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`gaxvlineÙ±‚`a(Ù±‚`axÙ±‚aoa=Ù±‚bmia0Ù±‚`a,Ù±‚`a Ù±‚`dyminÙ±‚aoa=Ù±‚bmfd0.75Ù±‚`a,Ù±‚`a Ù±‚`ilinewidthÙ±‚aoa=Ù±‚bmia8Ù±‚`a,Ù±‚`a Ù±‚`ecolorÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1g#1f77b4Ù±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚bc1x?# Default hline at y=.5 that spans the middle half of the axes.Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`gaxhlineÙ±‚`a(Ù±‚`ayÙ±‚aoa=Ù±‚bmfb.5Ù±‚`a,Ù±‚`a Ù±‚`dxminÙ±‚aoa=Ù±‚bmfd0.25Ù±‚`a,Ù±‚`a Ù±‚`dxmaxÙ±‚aoa=Ù±‚bmfd0.75Ù±‚`a)Ù±‚`a
Ù±‚bc1x5# Infinite black line going through (0, 0) to (1, 1).Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`faxlineÙ±‚`a(Ù±‚`a(Ù±‚bmia0Ù±‚`a,Ù±‚`a Ù±‚bmia0Ù±‚`a)Ù±‚`a,Ù±‚`a Ù±‚`a(Ù±‚bmia1Ù±‚`a,Ù±‚`a Ù±‚bmia1Ù±‚`a)Ù±‚`a,Ù±‚`a Ù±‚`ecolorÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1akÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚bc1xD# 50%-gray rectangle spanning the axes' width from y=0.25 to y=0.75.Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`gaxhspanÙ±‚`a(Ù±‚bmfd0.25Ù±‚`a,Ù±‚`a Ù±‚bmfd0.75Ù±‚`a,Ù±‚`a Ù±‚`ifacecolorÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1c0.5Ù±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚bc1xB# Green rectangle spanning the axes' height from x=1.25 to x=1.55.Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`gaxvspanÙ±‚`a(Ù±‚bmfd1.25Ù±‚`a,Ù±‚`a Ù±‚bmfd1.55Ù±‚`a,Ù±‚`a Ù±‚`ifacecolorÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1g#2ca02cÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`cpltÙ±‚aoa.Ù±‚`dshowÙ±‚`a(Ù±‚`a)Ù±‚`a
`dNoneö