Ù¯‚Ù´ƒ˜Ù±‚bsdx–"""
============================
Clipping images with patches
============================

Demo of image that's been clipped by a circular patch.
"""Ù±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnnfpyplotÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnncpltÙ±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnngpatchesÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnngpatchesÙ±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnnecbookÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnnecbookÙ±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚akdwithÙ±‚`a Ù±‚`ecbookÙ±‚aoa.Ù±‚`oget_sample_dataÙ±‚`a(Ù±‚bs1a'Ù±‚bs1pgrace_hopper.jpgÙ±‚bs1a'Ù±‚`a)Ù±‚`a Ù±‚akbasÙ±‚`a Ù±‚`jimage_fileÙ±‚`a:Ù±‚`a
Ù±‚`d    Ù±‚`eimageÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cpltÙ±‚aoa.Ù±‚`fimreadÙ±‚`a(Ù±‚`jimage_fileÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`cfigÙ±‚`a,Ù±‚`a Ù±‚`baxÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cpltÙ±‚aoa.Ù±‚`hsubplotsÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`bimÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`baxÙ±‚aoa.Ù±‚`fimshowÙ±‚`a(Ù±‚`eimageÙ±‚`a)Ù±‚`a
Ù±‚`epatchÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`gpatchesÙ±‚aoa.Ù±‚`fCircleÙ±‚`a(Ù±‚`a(Ù±‚bmic260Ù±‚`a,Ù±‚`a Ù±‚bmic200Ù±‚`a)Ù±‚`a,Ù±‚`a Ù±‚`fradiusÙ±‚aoa=Ù±‚bmic200Ù±‚`a,Ù±‚`a Ù±‚`itransformÙ±‚aoa=Ù±‚`baxÙ±‚aoa.Ù±‚`itransDataÙ±‚`a)Ù±‚`a
Ù±‚`bimÙ±‚aoa.Ù±‚`mset_clip_pathÙ±‚`a(Ù±‚`epatchÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`daxisÙ±‚`a(Ù±‚bs1a'Ù±‚bs1coffÙ±‚bs1a'Ù±‚`a)Ù±‚`a
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
Ù±‚bc1x/#    - `matplotlib.artist.Artist.set_clip_path`Ù±‚`a
`dNoneö