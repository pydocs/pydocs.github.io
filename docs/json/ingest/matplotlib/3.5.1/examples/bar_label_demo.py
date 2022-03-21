Ù¯‚Ù´ƒ™ŞÙ±‚bsdyu"""
==============
Bar Label Demo
==============

This example shows how to use the `~.Axes.bar_label` helper function
to create bar chart labels.

See also the :doc:`grouped bar
</gallery/lines_bars_and_markers/barchart>`,
:doc:`stacked bar
</gallery/lines_bars_and_markers/bar_stacked>` and
:doc:`horizontal bar chart
</gallery/lines_bars_and_markers/barh>` examples.
"""Ù±‚`a
Ù±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnnfpyplotÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnncpltÙ±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„enumpyÙ „enumpyf1.22.3fmoduleenumpyfmoduleõÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnnbnpÙ±‚`a
Ù±‚`a
Ù±‚bc1xO###############################################################################Ù±‚`a
Ù±‚bc1q# Define the dataÙ±‚`a
Ù±‚`a
Ù±‚`aNÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bmia5Ù±‚`a
Ù±‚`hmenMeansÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`a(Ù±‚bmib20Ù±‚`a,Ù±‚`a Ù±‚bmib35Ù±‚`a,Ù±‚`a Ù±‚bmib30Ù±‚`a,Ù±‚`a Ù±‚bmib35Ù±‚`a,Ù±‚`a Ù±‚aoa-Ù±‚bmib27Ù±‚`a)Ù±‚`a
Ù±‚`jwomenMeansÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`a(Ù±‚bmib25Ù±‚`a,Ù±‚`a Ù±‚bmib32Ù±‚`a,Ù±‚`a Ù±‚bmib34Ù±‚`a,Ù±‚`a Ù±‚bmib20Ù±‚`a,Ù±‚`a Ù±‚aoa-Ù±‚bmib25Ù±‚`a)Ù±‚`a
Ù±‚`fmenStdÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`a(Ù±‚bmia2Ù±‚`a,Ù±‚`a Ù±‚bmia3Ù±‚`a,Ù±‚`a Ù±‚bmia4Ù±‚`a,Ù±‚`a Ù±‚bmia1Ù±‚`a,Ù±‚`a Ù±‚bmia2Ù±‚`a)Ù±‚`a
Ù±‚`hwomenStdÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`a(Ù±‚bmia3Ù±‚`a,Ù±‚`a Ù±‚bmia5Ù±‚`a,Ù±‚`a Ù±‚bmia2Ù±‚`a,Ù±‚`a Ù±‚bmia3Ù±‚`a,Ù±‚`a Ù±‚bmia3Ù±‚`a)Ù±‚`a
Ù±‚`cindÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`farangeÙ±‚`a(Ù±‚`aNÙ±‚`a)Ù±‚`d    Ù±‚bc1x # the x locations for the groupsÙ±‚`a
Ù±‚`ewidthÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bmfd0.35Ù±‚`g       Ù±‚bc1x4# the width of the bars: can also be len(x) sequenceÙ±‚`a
Ù±‚`a
Ù±‚bc1xO###############################################################################Ù±‚`a
Ù±‚bc1x"# Stacked bar plot with error barsÙ±‚`a
Ù±‚`a
Ù±‚`cfigÙ±‚`a,Ù±‚`a Ù±‚`baxÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cpltÙ±‚aoa.Ù±‚`hsubplotsÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`bp1Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`baxÙ±‚aoa.Ù±‚`cbarÙ±‚`a(Ù±‚`cindÙ±‚`a,Ù±‚`a Ù±‚`hmenMeansÙ±‚`a,Ù±‚`a Ù±‚`ewidthÙ±‚`a,Ù±‚`a Ù±‚`dyerrÙ±‚aoa=Ù±‚`fmenStdÙ±‚`a,Ù±‚`a Ù±‚`elabelÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1cMenÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`bp2Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`baxÙ±‚aoa.Ù±‚`cbarÙ±‚`a(Ù±‚`cindÙ±‚`a,Ù±‚`a Ù±‚`jwomenMeansÙ±‚`a,Ù±‚`a Ù±‚`ewidthÙ±‚`a,Ù±‚`a
Ù±‚`l            Ù±‚`fbottomÙ±‚aoa=Ù±‚`hmenMeansÙ±‚`a,Ù±‚`a Ù±‚`dyerrÙ±‚aoa=Ù±‚`hwomenStdÙ±‚`a,Ù±‚`a Ù±‚`elabelÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1eWomenÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`gaxhlineÙ±‚`a(Ù±‚bmia0Ù±‚`a,Ù±‚`a Ù±‚`ecolorÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1dgreyÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`ilinewidthÙ±‚aoa=Ù±‚bmfc0.8Ù±‚`a)Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`jset_ylabelÙ±‚`a(Ù±‚bs1a'Ù±‚bs1fScoresÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`iset_titleÙ±‚`a(Ù±‚bs1a'Ù±‚bs1xScores by group and genderÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`jset_xticksÙ±‚`a(Ù±‚`cindÙ±‚`a,Ù±‚`a Ù±‚`flabelsÙ±‚aoa=Ù±‚`a[Ù±‚bs1a'Ù±‚bs1bG1Ù±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚bs1a'Ù±‚bs1bG2Ù±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚bs1a'Ù±‚bs1bG3Ù±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚bs1a'Ù±‚bs1bG4Ù±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚bs1a'Ù±‚bs1bG5Ù±‚bs1a'Ù±‚`a]Ù±‚`a)Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`flegendÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚bc1x># Label with label_type 'center' instead of the default 'edge'Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`ibar_labelÙ±‚`a(Ù±‚`bp1Ù±‚`a,Ù±‚`a Ù±‚`jlabel_typeÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1fcenterÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`ibar_labelÙ±‚`a(Ù±‚`bp2Ù±‚`a,Ù±‚`a Ù±‚`jlabel_typeÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1fcenterÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`ibar_labelÙ±‚`a(Ù±‚`bp2Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`cpltÙ±‚aoa.Ù±‚`dshowÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚bc1xO###############################################################################Ù±‚`a
Ù±‚bc1v# Horizontal bar chartÙ±‚`a
Ù±‚`a
Ù±‚bc1x)# Fixing random state for reproducibilityÙ±‚`a
Ù±‚`bnpÙ±‚aoa.Ù±‚`frandomÙ±‚aoa.Ù±‚`dseedÙ±‚`a(Ù±‚bmih19680801Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚bc1n# Example dataÙ±‚`a
Ù±‚`fpeopleÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`a(Ù±‚bs1a'Ù±‚bs1cTomÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚bs1a'Ù±‚bs1dDickÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚bs1a'Ù±‚bs1eHarryÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚bs1a'Ù±‚bs1dSlimÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚bs1a'Ù±‚bs1cJimÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`ey_posÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`farangeÙ±‚`a(Ù±‚bnbclenÙ±‚`a(Ù±‚`fpeopleÙ±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`kperformanceÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bmia3Ù±‚`a Ù±‚aoa+Ù±‚`a Ù±‚bmib10Ù±‚`a Ù±‚aoa*Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`frandomÙ±‚aoa.Ù±‚`drandÙ±‚`a(Ù±‚bnbclenÙ±‚`a(Ù±‚`fpeopleÙ±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`eerrorÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`frandomÙ±‚aoa.Ù±‚`drandÙ±‚`a(Ù±‚bnbclenÙ±‚`a(Ù±‚`fpeopleÙ±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`cfigÙ±‚`a,Ù±‚`a Ù±‚`baxÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cpltÙ±‚aoa.Ù±‚`hsubplotsÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`ehbarsÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`baxÙ±‚aoa.Ù±‚`dbarhÙ±‚`a(Ù±‚`ey_posÙ±‚`a,Ù±‚`a Ù±‚`kperformanceÙ±‚`a,Ù±‚`a Ù±‚`dxerrÙ±‚aoa=Ù±‚`eerrorÙ±‚`a,Ù±‚`a Ù±‚`ealignÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1fcenterÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`jset_yticksÙ±‚`a(Ù±‚`ey_posÙ±‚`a,Ù±‚`a Ù±‚`flabelsÙ±‚aoa=Ù±‚`fpeopleÙ±‚`a)Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`linvert_yaxisÙ±‚`a(Ù±‚`a)Ù±‚`b  Ù±‚bc1x# labels read top-to-bottomÙ±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`jset_xlabelÙ±‚`a(Ù±‚bs1a'Ù±‚bs1kPerformanceÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`iset_titleÙ±‚`a(Ù±‚bs1a'Ù±‚bs1x!How fast do you want to go today?Ù±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚bc1x'# Label with specially formatted floatsÙ±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`ibar_labelÙ±‚`a(Ù±‚`ehbarsÙ±‚`a,Ù±‚`a Ù±‚`cfmtÙ±‚aoa=Ù±‚bs1a'Ù±‚bsid%.2fÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`hset_xlimÙ±‚`a(Ù±‚`erightÙ±‚aoa=Ù±‚bmib15Ù±‚`a)Ù±‚`b  Ù±‚bc1x# adjust xlim to fit labelsÙ±‚`a
Ù±‚`a
Ù±‚`cpltÙ±‚aoa.Ù±‚`dshowÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚bc1xO###############################################################################Ù±‚`a
Ù±‚bc1xB# Some of the more advanced things that one can do with bar labelsÙ±‚`a
Ù±‚`a
Ù±‚`cfigÙ±‚`a,Ù±‚`a Ù±‚`baxÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cpltÙ±‚aoa.Ù±‚`hsubplotsÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`ehbarsÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`baxÙ±‚aoa.Ù±‚`dbarhÙ±‚`a(Ù±‚`ey_posÙ±‚`a,Ù±‚`a Ù±‚`kperformanceÙ±‚`a,Ù±‚`a Ù±‚`dxerrÙ±‚aoa=Ù±‚`eerrorÙ±‚`a,Ù±‚`a Ù±‚`ealignÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1fcenterÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`jset_yticksÙ±‚`a(Ù±‚`ey_posÙ±‚`a,Ù±‚`a Ù±‚`flabelsÙ±‚aoa=Ù±‚`fpeopleÙ±‚`a)Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`linvert_yaxisÙ±‚`a(Ù±‚`a)Ù±‚`b  Ù±‚bc1x# labels read top-to-bottomÙ±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`jset_xlabelÙ±‚`a(Ù±‚bs1a'Ù±‚bs1kPerformanceÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`iset_titleÙ±‚`a(Ù±‚bs1a'Ù±‚bs1x!How fast do you want to go today?Ù±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚bc1x@# Label with given captions, custom padding and annotate optionsÙ±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`ibar_labelÙ±‚`a(Ù±‚`ehbarsÙ±‚`a,Ù±‚`a Ù±‚`flabelsÙ±‚aoa=Ù±‚`a[Ù±‚bs1a'Ù±‚bs1bÂ±Ù±‚bsid%.2fÙ±‚bs1a'Ù±‚`a Ù±‚aoa%Ù±‚`a Ù±‚`aeÙ±‚`a Ù±‚akcforÙ±‚`a Ù±‚`aeÙ±‚`a Ù±‚bowbinÙ±‚`a Ù±‚`eerrorÙ±‚`a]Ù±‚`a,Ù±‚`a
Ù±‚`m             Ù±‚`gpaddingÙ±‚aoa=Ù±‚bmia8Ù±‚`a,Ù±‚`a Ù±‚`ecolorÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1abÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`hfontsizeÙ±‚aoa=Ù±‚bmib14Ù±‚`a)Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`hset_xlimÙ±‚`a(Ù±‚`erightÙ±‚aoa=Ù±‚bmib16Ù±‚`a)Ù±‚`a
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
Ù±‚bc1x;#    - `matplotlib.axes.Axes.bar` / `matplotlib.pyplot.bar`Ù±‚`a
Ù±‚bc1x=#    - `matplotlib.axes.Axes.barh` / `matplotlib.pyplot.barh`Ù±‚`a
Ù±‚bc1xG#    - `matplotlib.axes.Axes.bar_label` / `matplotlib.pyplot.bar_label`Ù±‚`a
`dNoneö