Ù¯‚Ù´ƒ™OÙ±‚bsdyB"""
==============================================
Including upper and lower limits in error bars
==============================================

In matplotlib, errors bars can have "limits". Applying limits to the
error bars essentially makes the error unidirectional. Because of that,
upper and lower limits can be applied in both the y- and x-directions
via the ``uplims``, ``lolims``, ``xuplims``, and ``xlolims`` parameters,
respectively. These parameters can be scalar or boolean arrays.

For example, if ``xlolims`` is ``True``, the x-error bars will only
extend from the data towards increasing values. If ``uplims`` is an
array filled with ``False`` except for the 4th and 7th values, all of the
y-error bars will be bidirectional, except the 4th and 7th bars, which
will extend from the data towards decreasing y-values.
"""Ù±‚`a
Ù±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„enumpyÙ „enumpyf1.22.3fmoduleenumpyfmoduleõÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnnbnpÙ±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnnfpyplotÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnncpltÙ±‚`a
Ù±‚`a
Ù±‚bc1n# example dataÙ±‚`a
Ù±‚`axÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`earrayÙ±‚`a(Ù±‚`a[Ù±‚bmfc0.5Ù±‚`a,Ù±‚`a Ù±‚bmfc1.0Ù±‚`a,Ù±‚`a Ù±‚bmfc1.5Ù±‚`a,Ù±‚`a Ù±‚bmfc2.0Ù±‚`a,Ù±‚`a Ù±‚bmfc2.5Ù±‚`a,Ù±‚`a Ù±‚bmfc3.0Ù±‚`a,Ù±‚`a Ù±‚bmfc3.5Ù±‚`a,Ù±‚`a Ù±‚bmfc4.0Ù±‚`a,Ù±‚`a Ù±‚bmfc4.5Ù±‚`a,Ù±‚`a Ù±‚bmfc5.0Ù±‚`a]Ù±‚`a)Ù±‚`a
Ù±‚`ayÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`cexpÙ±‚`a(Ù±‚aoa-Ù±‚`axÙ±‚`a)Ù±‚`a
Ù±‚`dxerrÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bmfc0.1Ù±‚`a
Ù±‚`dyerrÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bmfc0.2Ù±‚`a
Ù±‚`a
Ù±‚bc1x## lower & upper limits of the errorÙ±‚`a
Ù±‚`flolimsÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`earrayÙ±‚`a(Ù±‚`a[Ù±‚bmia0Ù±‚`a,Ù±‚`a Ù±‚bmia0Ù±‚`a,Ù±‚`a Ù±‚bmia1Ù±‚`a,Ù±‚`a Ù±‚bmia0Ù±‚`a,Ù±‚`a Ù±‚bmia1Ù±‚`a,Ù±‚`a Ù±‚bmia0Ù±‚`a,Ù±‚`a Ù±‚bmia0Ù±‚`a,Ù±‚`a Ù±‚bmia0Ù±‚`a,Ù±‚`a Ù±‚bmia1Ù±‚`a,Ù±‚`a Ù±‚bmia0Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`edtypeÙ±‚aoa=Ù±‚bnbdboolÙ±‚`a)Ù±‚`a
Ù±‚`fuplimsÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`earrayÙ±‚`a(Ù±‚`a[Ù±‚bmia0Ù±‚`a,Ù±‚`a Ù±‚bmia1Ù±‚`a,Ù±‚`a Ù±‚bmia0Ù±‚`a,Ù±‚`a Ù±‚bmia0Ù±‚`a,Ù±‚`a Ù±‚bmia0Ù±‚`a,Ù±‚`a Ù±‚bmia1Ù±‚`a,Ù±‚`a Ù±‚bmia0Ù±‚`a,Ù±‚`a Ù±‚bmia0Ù±‚`a,Ù±‚`a Ù±‚bmia0Ù±‚`a,Ù±‚`a Ù±‚bmia1Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`edtypeÙ±‚aoa=Ù±‚bnbdboolÙ±‚`a)Ù±‚`a
Ù±‚`blsÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bs1a'Ù±‚bs1fdottedÙ±‚bs1a'Ù±‚`a
Ù±‚`a
Ù±‚`cfigÙ±‚`a,Ù±‚`a Ù±‚`baxÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cpltÙ±‚aoa.Ù±‚`hsubplotsÙ±‚`a(Ù±‚`gfigsizeÙ±‚aoa=Ù±‚`a(Ù±‚bmia7Ù±‚`a,Ù±‚`a Ù±‚bmia4Ù±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚bc1u# standard error barsÙ±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`herrorbarÙ±‚`a(Ù±‚`axÙ±‚`a,Ù±‚`a Ù±‚`ayÙ±‚`a,Ù±‚`a Ù±‚`dxerrÙ±‚aoa=Ù±‚`dxerrÙ±‚`a,Ù±‚`a Ù±‚`dyerrÙ±‚aoa=Ù±‚`dyerrÙ±‚`a,Ù±‚`a Ù±‚`ilinestyleÙ±‚aoa=Ù±‚`blsÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚bc1x# including upper limitsÙ±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`herrorbarÙ±‚`a(Ù±‚`axÙ±‚`a,Ù±‚`a Ù±‚`ayÙ±‚`a Ù±‚aoa+Ù±‚`a Ù±‚bmfc0.5Ù±‚`a,Ù±‚`a Ù±‚`dxerrÙ±‚aoa=Ù±‚`dxerrÙ±‚`a,Ù±‚`a Ù±‚`dyerrÙ±‚aoa=Ù±‚`dyerrÙ±‚`a,Ù±‚`a Ù±‚`fuplimsÙ±‚aoa=Ù±‚`fuplimsÙ±‚`a,Ù±‚`a
Ù±‚`l            Ù±‚`ilinestyleÙ±‚aoa=Ù±‚`blsÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚bc1x# including lower limitsÙ±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`herrorbarÙ±‚`a(Ù±‚`axÙ±‚`a,Ù±‚`a Ù±‚`ayÙ±‚`a Ù±‚aoa+Ù±‚`a Ù±‚bmfc1.0Ù±‚`a,Ù±‚`a Ù±‚`dxerrÙ±‚aoa=Ù±‚`dxerrÙ±‚`a,Ù±‚`a Ù±‚`dyerrÙ±‚aoa=Ù±‚`dyerrÙ±‚`a,Ù±‚`a Ù±‚`flolimsÙ±‚aoa=Ù±‚`flolimsÙ±‚`a,Ù±‚`a
Ù±‚`l            Ù±‚`ilinestyleÙ±‚aoa=Ù±‚`blsÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚bc1x"# including upper and lower limitsÙ±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`herrorbarÙ±‚`a(Ù±‚`axÙ±‚`a,Ù±‚`a Ù±‚`ayÙ±‚`a Ù±‚aoa+Ù±‚`a Ù±‚bmfc1.5Ù±‚`a,Ù±‚`a Ù±‚`dxerrÙ±‚aoa=Ù±‚`dxerrÙ±‚`a,Ù±‚`a Ù±‚`dyerrÙ±‚aoa=Ù±‚`dyerrÙ±‚`a,Ù±‚`a
Ù±‚`l            Ù±‚`flolimsÙ±‚aoa=Ù±‚`flolimsÙ±‚`a,Ù±‚`a Ù±‚`fuplimsÙ±‚aoa=Ù±‚`fuplimsÙ±‚`a,Ù±‚`a
Ù±‚`l            Ù±‚`fmarkerÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1aoÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`jmarkersizeÙ±‚aoa=Ù±‚bmia8Ù±‚`a,Ù±‚`a
Ù±‚`l            Ù±‚`ilinestyleÙ±‚aoa=Ù±‚`blsÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚bc1x9# Plot a series with lower and upper limits in both x & yÙ±‚`a
Ù±‚bc1x'# constant x-error with varying y-errorÙ±‚`a
Ù±‚`dxerrÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bmfc0.2Ù±‚`a
Ù±‚`dyerrÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`ifull_likeÙ±‚`a(Ù±‚`axÙ±‚`a,Ù±‚`a Ù±‚bmfc0.2Ù±‚`a)Ù±‚`a
Ù±‚`dyerrÙ±‚`a[Ù±‚`a[Ù±‚bmia3Ù±‚`a,Ù±‚`a Ù±‚bmia6Ù±‚`a]Ù±‚`a]Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bmfc0.3Ù±‚`a
Ù±‚`a
Ù±‚bc1x0# mock up some limits by modifying previous dataÙ±‚`a
Ù±‚`gxlolimsÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`flolimsÙ±‚`a
Ù±‚`gxuplimsÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`fuplimsÙ±‚`a
Ù±‚`flolimsÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`jzeros_likeÙ±‚`a(Ù±‚`axÙ±‚`a)Ù±‚`a
Ù±‚`fuplimsÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`jzeros_likeÙ±‚`a(Ù±‚`axÙ±‚`a)Ù±‚`a
Ù±‚`flolimsÙ±‚`a[Ù±‚`a[Ù±‚bmia6Ù±‚`a]Ù±‚`a]Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bkcdTrueÙ±‚`b  Ù±‚bc1x# only limited at this indexÙ±‚`a
Ù±‚`fuplimsÙ±‚`a[Ù±‚`a[Ù±‚bmia3Ù±‚`a]Ù±‚`a]Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bkcdTrueÙ±‚`b  Ù±‚bc1x# only limited at this indexÙ±‚`a
Ù±‚`a
Ù±‚bc1q# do the plottingÙ±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`herrorbarÙ±‚`a(Ù±‚`axÙ±‚`a,Ù±‚`a Ù±‚`ayÙ±‚`a Ù±‚aoa+Ù±‚`a Ù±‚bmfc2.1Ù±‚`a,Ù±‚`a Ù±‚`dxerrÙ±‚aoa=Ù±‚`dxerrÙ±‚`a,Ù±‚`a Ù±‚`dyerrÙ±‚aoa=Ù±‚`dyerrÙ±‚`a,Ù±‚`a
Ù±‚`l            Ù±‚`gxlolimsÙ±‚aoa=Ù±‚`gxlolimsÙ±‚`a,Ù±‚`a Ù±‚`gxuplimsÙ±‚aoa=Ù±‚`gxuplimsÙ±‚`a,Ù±‚`a
Ù±‚`l            Ù±‚`fuplimsÙ±‚aoa=Ù±‚`fuplimsÙ±‚`a,Ù±‚`a Ù±‚`flolimsÙ±‚aoa=Ù±‚`flolimsÙ±‚`a,Ù±‚`a
Ù±‚`l            Ù±‚`fmarkerÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1aoÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`jmarkersizeÙ±‚aoa=Ù±‚bmia8Ù±‚`a,Ù±‚`a
Ù±‚`l            Ù±‚`ilinestyleÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1dnoneÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚bc1t# tidy up the figureÙ±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`hset_xlimÙ±‚`a(Ù±‚`a(Ù±‚bmia0Ù±‚`a,Ù±‚`a Ù±‚bmfc5.5Ù±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`iset_titleÙ±‚`a(Ù±‚bs1a'Ù±‚bs1xErrorbar upper and lower limitsÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`cpltÙ±‚aoa.Ù±‚`dshowÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚bc1xM#############################################################################Ù±‚`a
Ù±‚bc1a#Ù±‚`a
Ù±‚bc1x# .. admonition:: ReferencesÙ±‚`a
Ù±‚bc1a#Ù±‚`a
Ù±‚bc1xN#    The use of the following functions, methods, classes and modules is shownÙ±‚`a
Ù±‚bc1u#    in this example:Ù±‚`a
Ù±‚bc1a#Ù±‚`a
Ù±‚bc1xE#    - `matplotlib.axes.Axes.errorbar` / `matplotlib.pyplot.errorbar`Ù±‚`a
`dNoneö