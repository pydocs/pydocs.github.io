Ù¯‚Ù´ƒ˜ƒÙ±‚bsdxš"""
===
MRI
===

This example illustrates how to read an image (of an MRI) into a NumPy
array, and display it in greyscale using `~.axes.Axes.imshow`.
"""Ù±‚`a
Ù±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnnfpyplotÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnncpltÙ±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnnecbookÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnnecbookÙ±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„enumpyÙ „enumpyf1.22.3fmoduleenumpyfmoduleõÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnnbnpÙ±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚bc1x## Data are 256x256 16 bit integers.Ù±‚`a
Ù±‚akdwithÙ±‚`a Ù±‚`ecbookÙ±‚aoa.Ù±‚`oget_sample_dataÙ±‚`a(Ù±‚bs1a'Ù±‚bs1ls1045.ima.gzÙ±‚bs1a'Ù±‚`a)Ù±‚`a Ù±‚akbasÙ±‚`a Ù±‚`edfileÙ±‚`a:Ù±‚`a
Ù±‚`d    Ù±‚`bimÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`jfrombufferÙ±‚`a(Ù±‚`edfileÙ±‚aoa.Ù±‚`dreadÙ±‚`a(Ù±‚`a)Ù±‚`a,Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`fuint16Ù±‚`a)Ù±‚aoa.Ù±‚`greshapeÙ±‚`a(Ù±‚`a(Ù±‚bmic256Ù±‚`a,Ù±‚`a Ù±‚bmic256Ù±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`cfigÙ±‚`a,Ù±‚`a Ù±‚`baxÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cpltÙ±‚aoa.Ù±‚`hsubplotsÙ±‚`a(Ù±‚`cnumÙ±‚aoa=Ù±‚bs2a"Ù±‚bs2hMRI_demoÙ±‚bs2a"Ù±‚`a)Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`fimshowÙ±‚`a(Ù±‚`bimÙ±‚`a,Ù±‚`a Ù±‚`dcmapÙ±‚aoa=Ù±‚bs2a"Ù±‚bs2dgrayÙ±‚bs2a"Ù±‚`a)Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`daxisÙ±‚`a(Ù±‚bs1a'Ù±‚bs1coffÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`cpltÙ±‚aoa.Ù±‚`dshowÙ±‚`a(Ù±‚`a)Ù±‚`a
`dNoneö