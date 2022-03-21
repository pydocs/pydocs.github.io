Ù¯‚Ù´ƒ™Ù±‚bsdy("""
==============================
Plotting masked and NaN values
==============================

Sometimes you need to plot data with missing values.

One possibility is to simply remove undesired data points. The line plotted
through the remaining data will be continuous, and not indicate where the
missing data is located.

If it is useful to have gaps in the line where the data is missing, then the
undesired points can be indicated using a `masked array`_ or by setting their
values to NaN. No marker will be drawn where either x or y are masked and, if
plotting with a line, it will be broken there.

.. _masked array:
   https://numpy.org/doc/stable/reference/maskedarray.generic.html

The following example illustrates the three cases:

1) Removing points.
2) Masking points.
3) Setting to NaN.
"""Ù±‚`a
Ù±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnnfpyplotÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnncpltÙ±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„enumpyÙ „enumpyf1.22.3fmoduleenumpyfmoduleõÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnnbnpÙ±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚`axÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`hlinspaceÙ±‚`a(Ù±‚aoa-Ù±‚`bnpÙ±‚aoa.Ù±‚`bpiÙ±‚aoa/Ù±‚bmia2Ù±‚`a,Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`bpiÙ±‚aoa/Ù±‚bmia2Ù±‚`a,Ù±‚`a Ù±‚bmib31Ù±‚`a)Ù±‚`a
Ù±‚`ayÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`ccosÙ±‚`a(Ù±‚`axÙ±‚`a)Ù±‚aoa*Ù±‚aoa*Ù±‚bmia3Ù±‚`a
Ù±‚`a
Ù±‚bc1x # 1) remove points where y > 0.7Ù±‚`a
Ù±‚`bx2Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`axÙ±‚`a[Ù±‚`ayÙ±‚`a Ù±‚aoa<Ù±‚aoa=Ù±‚`a Ù±‚bmfc0.7Ù±‚`a]Ù±‚`a
Ù±‚`by2Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`ayÙ±‚`a[Ù±‚`ayÙ±‚`a Ù±‚aoa<Ù±‚aoa=Ù±‚`a Ù±‚bmfc0.7Ù±‚`a]Ù±‚`a
Ù±‚`a
Ù±‚bc1x# 2) mask points where y > 0.7Ù±‚`a
Ù±‚`by3Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`bmaÙ±‚aoa.Ù±‚`lmasked_whereÙ±‚`a(Ù±‚`ayÙ±‚`a Ù±‚aoa>Ù±‚`a Ù±‚bmfc0.7Ù±‚`a,Ù±‚`a Ù±‚`ayÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚bc1x# 3) set to NaN where y > 0.7Ù±‚`a
Ù±‚`by4Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`ayÙ±‚aoa.Ù±‚`dcopyÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`by4Ù±‚`a[Ù±‚`by3Ù±‚`a Ù±‚aoa>Ù±‚`a Ù±‚bmfc0.7Ù±‚`a]Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`cnanÙ±‚`a
Ù±‚`a
Ù±‚`cpltÙ±‚aoa.Ù±‚`dplotÙ±‚`a(Ù±‚`axÙ±‚aoa*Ù±‚bmfc0.1Ù±‚`a,Ù±‚`a Ù±‚`ayÙ±‚`a,Ù±‚`a Ù±‚bs1a'Ù±‚bs1bo-Ù±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`ecolorÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1ilightgreyÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`elabelÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1gNo maskÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`cpltÙ±‚aoa.Ù±‚`dplotÙ±‚`a(Ù±‚`bx2Ù±‚aoa*Ù±‚bmfc0.4Ù±‚`a,Ù±‚`a Ù±‚`by2Ù±‚`a,Ù±‚`a Ù±‚bs1a'Ù±‚bs1bo-Ù±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`elabelÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1nPoints removedÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`cpltÙ±‚aoa.Ù±‚`dplotÙ±‚`a(Ù±‚`axÙ±‚aoa*Ù±‚bmfc0.7Ù±‚`a,Ù±‚`a Ù±‚`by3Ù±‚`a,Ù±‚`a Ù±‚bs1a'Ù±‚bs1bo-Ù±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`elabelÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1mMasked valuesÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`cpltÙ±‚aoa.Ù±‚`dplotÙ±‚`a(Ù±‚`axÙ±‚aoa*Ù±‚bmfc1.0Ù±‚`a,Ù±‚`a Ù±‚`by4Ù±‚`a,Ù±‚`a Ù±‚bs1a'Ù±‚bs1bo-Ù±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`elabelÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1jNaN valuesÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`cpltÙ±‚aoa.Ù±‚`flegendÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`cpltÙ±‚aoa.Ù±‚`etitleÙ±‚`a(Ù±‚bs1a'Ù±‚bs1sMasked and NaN dataÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`cpltÙ±‚aoa.Ù±‚`dshowÙ±‚`a(Ù±‚`a)Ù±‚`a
`dNoneö