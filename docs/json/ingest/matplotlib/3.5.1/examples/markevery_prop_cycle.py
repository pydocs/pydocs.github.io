ŸØÇÅŸ¥ÉôÆŸ±Çbsdy"""
=========================================
prop_cycle property markevery in rcParams
=========================================

This example demonstrates a working solution to issue #8576, providing full
support of the markevery property for axes.prop_cycle assignments through
rcParams. Makes use of the same list of markevery cases from the
:doc:`markevery demo
</gallery/lines_bars_and_markers/markevery_demo>`.

Renders a plot with shifted-sine curves along each column with
a unique markevery value for each sine curve.
"""Ÿ±Ç`a
Ÿ±ÇbkndfromŸ±Ç`a Ÿ±ÇbnnfcyclerŸ±Ç`a Ÿ±ÇbknfimportŸ±Ç`a Ÿ±Ç`fcyclerŸ±Ç`a
Ÿ±ÇbknfimportŸ±Ç`a Ÿ±ÇbnnŸ¢ÑenumpyŸ†Ñenumpyf1.22.3fmoduleenumpyfmoduleıŸ±Ç`a Ÿ±ÇakbasŸ±Ç`a Ÿ±ÇbnnbnpŸ±Ç`a
Ÿ±ÇbknfimportŸ±Ç`a Ÿ±ÇbnnŸ¢ÑjmatplotlibŸ†Ñjmatplotlibe3.5.1fmodulejmatplotlibfmoduleıŸ±Ç`a Ÿ±ÇakbasŸ±Ç`a Ÿ±ÇbnncmplŸ±Ç`a
Ÿ±ÇbknfimportŸ±Ç`a Ÿ±ÇbnnŸ¢ÑjmatplotlibŸ†Ñjmatplotlibe3.5.1fmodulejmatplotlibfmoduleıŸ±Çbnna.Ÿ±ÇbnnfpyplotŸ±Ç`a Ÿ±ÇakbasŸ±Ç`a Ÿ±ÇbnncpltŸ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1x:# Define a list of markevery cases and color cases to plotŸ±Ç`a
Ÿ±Ç`ecasesŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`a[Ÿ±ÇbkcdNoneŸ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`i         Ÿ±Çbmia8Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`i         Ÿ±Ç`a(Ÿ±Çbmib30Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia8Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`i         Ÿ±Ç`a[Ÿ±Çbmib16Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmib24Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmib30Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`i         Ÿ±Ç`a[Ÿ±Çbmia0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çaoa-Ÿ±Çbmia1Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`i         Ÿ±ÇbnbesliceŸ±Ç`a(Ÿ±Çbmic100Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmic200Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia3Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`i         Ÿ±Çbmfc0.1Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`i         Ÿ±Çbmfc0.3Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`i         Ÿ±Çbmfc1.5Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`i         Ÿ±Ç`a(Ÿ±Çbmfc0.0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfc0.1Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`i         Ÿ±Ç`a(Ÿ±Çbmfd0.45Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfc0.1Ÿ±Ç`a)Ÿ±Ç`a]Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`fcolorsŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`a[Ÿ±Çbs1a'Ÿ±Çbs1g#1f77b4Ÿ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`j          Ÿ±Çbs1a'Ÿ±Çbs1g#ff7f0eŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`j          Ÿ±Çbs1a'Ÿ±Çbs1g#2ca02cŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`j          Ÿ±Çbs1a'Ÿ±Çbs1g#d62728Ÿ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`j          Ÿ±Çbs1a'Ÿ±Çbs1g#9467bdŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`j          Ÿ±Çbs1a'Ÿ±Çbs1g#8c564bŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`j          Ÿ±Çbs1a'Ÿ±Çbs1g#e377c2Ÿ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`j          Ÿ±Çbs1a'Ÿ±Çbs1g#7f7f7fŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`j          Ÿ±Çbs1a'Ÿ±Çbs1g#bcbd22Ÿ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`j          Ÿ±Çbs1a'Ÿ±Çbs1g#17becfŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`j          Ÿ±Çbs1a'Ÿ±Çbs1g#1a55FFŸ±Çbs1a'Ÿ±Ç`a]Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1xN# Configure rcParams axes.prop_cycle to simultaneously cycle cases and colors.Ÿ±Ç`a
Ÿ±Ç`cmplŸ±Çaoa.Ÿ±Ç`hrcParamsŸ±Ç`a[Ÿ±Çbs1a'Ÿ±Çbs1oaxes.prop_cycleŸ±Çbs1a'Ÿ±Ç`a]Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`fcyclerŸ±Ç`a(Ÿ±Ç`imarkeveryŸ±Çaoa=Ÿ±Ç`ecasesŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ecolorŸ±Çaoa=Ÿ±Ç`fcolorsŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1x # Create data points and offsetsŸ±Ç`a
Ÿ±Ç`axŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`hlinspaceŸ±Ç`a(Ÿ±Çbmia0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia2Ÿ±Ç`a Ÿ±Çaoa*Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`bpiŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`goffsetsŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`hlinspaceŸ±Ç`a(Ÿ±Çbmia0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia2Ÿ±Ç`a Ÿ±Çaoa*Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`bpiŸ±Ç`a,Ÿ±Ç`a Ÿ±Çbmib11Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`hendpointŸ±Çaoa=Ÿ±ÇbkceFalseŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`byyŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`itransposeŸ±Ç`a(Ÿ±Ç`a[Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`csinŸ±Ç`a(Ÿ±Ç`axŸ±Ç`a Ÿ±Çaoa+Ÿ±Ç`a Ÿ±Ç`cphiŸ±Ç`a)Ÿ±Ç`a Ÿ±ÇakcforŸ±Ç`a Ÿ±Ç`cphiŸ±Ç`a Ÿ±ÇbowbinŸ±Ç`a Ÿ±Ç`goffsetsŸ±Ç`a]Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1x-# Set the plot curve with markers and a titleŸ±Ç`a
Ÿ±Ç`cfigŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`ffigureŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`baxŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cfigŸ±Çaoa.Ÿ±Ç`hadd_axesŸ±Ç`a(Ÿ±Ç`a[Ÿ±Çbmfc0.1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfc0.1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfc0.6Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd0.75Ÿ±Ç`a]Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±ÇakcforŸ±Ç`a Ÿ±Ç`aiŸ±Ç`a Ÿ±ÇbowbinŸ±Ç`a Ÿ±ÇbnberangeŸ±Ç`a(Ÿ±ÇbnbclenŸ±Ç`a(Ÿ±Ç`ecasesŸ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`dplotŸ±Ç`a(Ÿ±Ç`byyŸ±Ç`a[Ÿ±Ç`a:Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`aiŸ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`fmarkerŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1aoŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`elabelŸ±Çaoa=Ÿ±ÇbnbcstrŸ±Ç`a(Ÿ±Ç`ecasesŸ±Ç`a[Ÿ±Ç`aiŸ±Ç`a]Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`flegendŸ±Ç`a(Ÿ±Ç`nbbox_to_anchorŸ±Çaoa=Ÿ±Ç`a(Ÿ±Çbmfd1.05Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia1Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`clocŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1jupper leftŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`mborderaxespadŸ±Çaoa=Ÿ±Çbmfb0.Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`etitleŸ±Ç`a(Ÿ±Çbs1a'Ÿ±Çbs1x1Support for axes.prop_cycle cycler with markeveryŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`dshowŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
`dNoneˆ