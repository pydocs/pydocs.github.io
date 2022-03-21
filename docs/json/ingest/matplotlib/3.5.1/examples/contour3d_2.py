Ù¯‚Ù´ƒ˜dÙ±‚bsdyb"""
============================================================================
Demonstrates plotting contour (level) curves in 3D using the extend3d option
============================================================================

This modification of the contour3d_demo example uses extend3d=True to
extend the curves vertically into 'ribbons'.
"""Ù±‚`a
Ù±‚`a
Ù±‚bkndfromÙ±‚`a Ù±‚bnnlmpl_toolkitsÙ±‚bnna.Ù±‚bnngmplot3dÙ±‚`a Ù±‚bknfimportÙ±‚`a Ù±‚`faxes3dÙ±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnnfpyplotÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnncpltÙ±‚`a
Ù±‚bkndfromÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚`a Ù±‚bknfimportÙ±‚`a Ù±‚`bcmÙ±‚`a
Ù±‚`a
Ù±‚`baxÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cpltÙ±‚aoa.Ù±‚`ffigureÙ±‚`a(Ù±‚`a)Ù±‚aoa.Ù±‚`kadd_subplotÙ±‚`a(Ù±‚`jprojectionÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1b3dÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`aXÙ±‚`a,Ù±‚`a Ù±‚`aYÙ±‚`a,Ù±‚`a Ù±‚`aZÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`faxes3dÙ±‚aoa.Ù±‚`mget_test_dataÙ±‚`a(Ù±‚bmfd0.05Ù±‚`a)Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`gcontourÙ±‚`a(Ù±‚`aXÙ±‚`a,Ù±‚`a Ù±‚`aYÙ±‚`a,Ù±‚`a Ù±‚`aZÙ±‚`a,Ù±‚`a Ù±‚`hextend3dÙ±‚aoa=Ù±‚bkcdTrueÙ±‚`a,Ù±‚`a Ù±‚`dcmapÙ±‚aoa=Ù±‚`bcmÙ±‚aoa.Ù±‚`hcoolwarmÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`cpltÙ±‚aoa.Ù±‚`dshowÙ±‚`a(Ù±‚`a)Ù±‚`a
`dNoneö