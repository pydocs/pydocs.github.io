Ù¯‚Ù´ƒ™lÙ±‚bsdy¬"""
======================
transforms.offset_copy
======================

This illustrates the use of `.transforms.offset_copy` to
make a transform that positions a drawing element such as
a text string at a specified offset in screen coordinates
(dots or inches) relative to a location given in any
coordinates.

Every Artist (Text, Line2D, etc.) has a transform that can be
set when the Artist is created, such as by the corresponding
pyplot function.  By default this is usually the Axes.transData
transform, going from data units to screen pixels.  We can
use the `.offset_copy` function to make a modified copy of
this transform, where the modification consists of an
offset.
"""Ù±‚`a
Ù±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnnfpyplotÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnncpltÙ±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnnjtransformsÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnnkmtransformsÙ±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„enumpyÙ „enumpyf1.22.3fmoduleenumpyfmoduleõÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnnbnpÙ±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚`bxsÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`farangeÙ±‚`a(Ù±‚bmia7Ù±‚`a)Ù±‚`a
Ù±‚`bysÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bxsÙ±‚aoa*Ù±‚aoa*Ù±‚bmia2Ù±‚`a
Ù±‚`a
Ù±‚`cfigÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cpltÙ±‚aoa.Ù±‚`ffigureÙ±‚`a(Ù±‚`gfigsizeÙ±‚aoa=Ù±‚`a(Ù±‚bmia5Ù±‚`a,Ù±‚`a Ù±‚bmib10Ù±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`baxÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cpltÙ±‚aoa.Ù±‚`gsubplotÙ±‚`a(Ù±‚bmia2Ù±‚`a,Ù±‚`a Ù±‚bmia1Ù±‚`a,Ù±‚`a Ù±‚bmia1Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚bc1x4# If we want the same offset for each text instance,Ù±‚`a
Ù±‚bc1x1# we only need to make one transform.  To get theÙ±‚`a
Ù±‚bc1x=# transform argument to offset_copy, we need to make the axesÙ±‚`a
Ù±‚bc1x:# first; the subplot function above is one way to do this.Ù±‚`a
Ù±‚`ltrans_offsetÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`kmtransformsÙ±‚aoa.Ù±‚`koffset_copyÙ±‚`a(Ù±‚`baxÙ±‚aoa.Ù±‚`itransDataÙ±‚`a,Ù±‚`a Ù±‚`cfigÙ±‚aoa=Ù±‚`cfigÙ±‚`a,Ù±‚`a
Ù±‚`x'                                       Ù±‚`axÙ±‚aoa=Ù±‚bmfd0.05Ù±‚`a,Ù±‚`a Ù±‚`ayÙ±‚aoa=Ù±‚bmfd0.10Ù±‚`a,Ù±‚`a Ù±‚`eunitsÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1finchesÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚akcforÙ±‚`a Ù±‚`axÙ±‚`a,Ù±‚`a Ù±‚`ayÙ±‚`a Ù±‚bowbinÙ±‚`a Ù±‚bnbczipÙ±‚`a(Ù±‚`bxsÙ±‚`a,Ù±‚`a Ù±‚`bysÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`d    Ù±‚`cpltÙ±‚aoa.Ù±‚`dplotÙ±‚`a(Ù±‚`axÙ±‚`a,Ù±‚`a Ù±‚`ayÙ±‚`a,Ù±‚`a Ù±‚bs1a'Ù±‚bs1broÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`cpltÙ±‚aoa.Ù±‚`dtextÙ±‚`a(Ù±‚`axÙ±‚`a,Ù±‚`a Ù±‚`ayÙ±‚`a,Ù±‚`a Ù±‚bs1a'Ù±‚bsib%dÙ±‚bs1b, Ù±‚bsib%dÙ±‚bs1a'Ù±‚`a Ù±‚aoa%Ù±‚`a Ù±‚`a(Ù±‚bnbcintÙ±‚`a(Ù±‚`axÙ±‚`a)Ù±‚`a,Ù±‚`a Ù±‚bnbcintÙ±‚`a(Ù±‚`ayÙ±‚`a)Ù±‚`a)Ù±‚`a,Ù±‚`a Ù±‚`itransformÙ±‚aoa=Ù±‚`ltrans_offsetÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚bc1x)# offset_copy works for polar plots also.Ù±‚`a
Ù±‚`baxÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cpltÙ±‚aoa.Ù±‚`gsubplotÙ±‚`a(Ù±‚bmia2Ù±‚`a,Ù±‚`a Ù±‚bmia1Ù±‚`a,Ù±‚`a Ù±‚bmia2Ù±‚`a,Ù±‚`a Ù±‚`jprojectionÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1epolarÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`ltrans_offsetÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`kmtransformsÙ±‚aoa.Ù±‚`koffset_copyÙ±‚`a(Ù±‚`baxÙ±‚aoa.Ù±‚`itransDataÙ±‚`a,Ù±‚`a Ù±‚`cfigÙ±‚aoa=Ù±‚`cfigÙ±‚`a,Ù±‚`a
Ù±‚`x'                                       Ù±‚`ayÙ±‚aoa=Ù±‚bmia6Ù±‚`a,Ù±‚`a Ù±‚`eunitsÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1ddotsÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚akcforÙ±‚`a Ù±‚`axÙ±‚`a,Ù±‚`a Ù±‚`ayÙ±‚`a Ù±‚bowbinÙ±‚`a Ù±‚bnbczipÙ±‚`a(Ù±‚`bxsÙ±‚`a,Ù±‚`a Ù±‚`bysÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`d    Ù±‚`cpltÙ±‚aoa.Ù±‚`epolarÙ±‚`a(Ù±‚`axÙ±‚`a,Ù±‚`a Ù±‚`ayÙ±‚`a,Ù±‚`a Ù±‚bs1a'Ù±‚bs1broÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`cpltÙ±‚aoa.Ù±‚`dtextÙ±‚`a(Ù±‚`axÙ±‚`a,Ù±‚`a Ù±‚`ayÙ±‚`a,Ù±‚`a Ù±‚bs1a'Ù±‚bsib%dÙ±‚bs1b, Ù±‚bsib%dÙ±‚bs1a'Ù±‚`a Ù±‚aoa%Ù±‚`a Ù±‚`a(Ù±‚bnbcintÙ±‚`a(Ù±‚`axÙ±‚`a)Ù±‚`a,Ù±‚`a Ù±‚bnbcintÙ±‚`a(Ù±‚`ayÙ±‚`a)Ù±‚`a)Ù±‚`a,Ù±‚`a
Ù±‚`m             Ù±‚`itransformÙ±‚aoa=Ù±‚`ltrans_offsetÙ±‚`a,Ù±‚`a
Ù±‚`m             Ù±‚`shorizontalalignmentÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1fcenterÙ±‚bs1a'Ù±‚`a,Ù±‚`a
Ù±‚`m             Ù±‚`qverticalalignmentÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1fbottomÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`cpltÙ±‚aoa.Ù±‚`dshowÙ±‚`a(Ù±‚`a)Ù±‚`a
`dNoneö