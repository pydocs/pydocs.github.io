Ù¯‚Ù´ƒ™ÍÙ±‚bsdyû"""
=======================
Boxplot drawer function
=======================

This example demonstrates how to pass pre-computed box plot
statistics to the box plot drawer. The first figure demonstrates
how to remove and add individual components (note that the
mean is the only value not shown by default). The second
figure demonstrates how the styles of the artists can
be customized.

A good general reference on boxplots and their history can be found
here: http://vita.had.co.nz/papers/boxplots.pdf
"""Ù±‚`a
Ù±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„enumpyÙ „enumpyf1.22.3fmoduleenumpyfmoduleõÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnnbnpÙ±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnnfpyplotÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnncpltÙ±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnnecbookÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnnecbookÙ±‚`a
Ù±‚`a
Ù±‚bc1k# fake dataÙ±‚`a
Ù±‚`bnpÙ±‚aoa.Ù±‚`frandomÙ±‚aoa.Ù±‚`dseedÙ±‚`a(Ù±‚bmih19680801Ù±‚`a)Ù±‚`a
Ù±‚`ddataÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`frandomÙ±‚aoa.Ù±‚`ilognormalÙ±‚`a(Ù±‚`dsizeÙ±‚aoa=Ù±‚`a(Ù±‚bmib37Ù±‚`a,Ù±‚`a Ù±‚bmia4Ù±‚`a)Ù±‚`a,Ù±‚`a Ù±‚`dmeanÙ±‚aoa=Ù±‚bmfc1.5Ù±‚`a,Ù±‚`a Ù±‚`esigmaÙ±‚aoa=Ù±‚bmfd1.75Ù±‚`a)Ù±‚`a
Ù±‚`flabelsÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bnbdlistÙ±‚`a(Ù±‚bs1a'Ù±‚bs1dABCDÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚bc1x# compute the boxplot statsÙ±‚`a
Ù±‚`estatsÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`ecbookÙ±‚aoa.Ù±‚`mboxplot_statsÙ±‚`a(Ù±‚`ddataÙ±‚`a,Ù±‚`a Ù±‚`flabelsÙ±‚aoa=Ù±‚`flabelsÙ±‚`a,Ù±‚`a Ù±‚`ibootstrapÙ±‚aoa=Ù±‚bmie10000Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚bc1xO###############################################################################Ù±‚`a
Ù±‚bc1xH# After we've computed the stats, we can go through and change anything.Ù±‚`a
Ù±‚bc1xH# Just to prove it, I'll set the median of each set to the median of allÙ±‚`a
Ù±‚bc1x # the data, and double the meansÙ±‚`a
Ù±‚`a
Ù±‚akcforÙ±‚`a Ù±‚`anÙ±‚`a Ù±‚bowbinÙ±‚`a Ù±‚bnberangeÙ±‚`a(Ù±‚bnbclenÙ±‚`a(Ù±‚`estatsÙ±‚`a)Ù±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`d    Ù±‚`estatsÙ±‚`a[Ù±‚`anÙ±‚`a]Ù±‚`a[Ù±‚bs1a'Ù±‚bs1cmedÙ±‚bs1a'Ù±‚`a]Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`fmedianÙ±‚`a(Ù±‚`ddataÙ±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`estatsÙ±‚`a[Ù±‚`anÙ±‚`a]Ù±‚`a[Ù±‚bs1a'Ù±‚bs1dmeanÙ±‚bs1a'Ù±‚`a]Ù±‚`a Ù±‚aoa*Ù±‚aoa=Ù±‚`a Ù±‚bmia2Ù±‚`a
Ù±‚`a
Ù±‚bnbeprintÙ±‚`a(Ù±‚bnbdlistÙ±‚`a(Ù±‚`estatsÙ±‚`a[Ù±‚bmia0Ù±‚`a]Ù±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`bfsÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bmib10Ù±‚`b  Ù±‚bc1j# fontsizeÙ±‚`a
Ù±‚`a
Ù±‚bc1xO###############################################################################Ù±‚`a
Ù±‚bc1x># Demonstrate how to toggle the display of different elements:Ù±‚`a
Ù±‚`a
Ù±‚`cfigÙ±‚`a,Ù±‚`a Ù±‚`caxsÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cpltÙ±‚aoa.Ù±‚`hsubplotsÙ±‚`a(Ù±‚`enrowsÙ±‚aoa=Ù±‚bmia2Ù±‚`a,Ù±‚`a Ù±‚`encolsÙ±‚aoa=Ù±‚bmia3Ù±‚`a,Ù±‚`a Ù±‚`gfigsizeÙ±‚aoa=Ù±‚`a(Ù±‚bmia6Ù±‚`a,Ù±‚`a Ù±‚bmia6Ù±‚`a)Ù±‚`a,Ù±‚`a Ù±‚`fshareyÙ±‚aoa=Ù±‚bkcdTrueÙ±‚`a)Ù±‚`a
Ù±‚`caxsÙ±‚`a[Ù±‚bmia0Ù±‚`a,Ù±‚`a Ù±‚bmia0Ù±‚`a]Ù±‚aoa.Ù±‚`cbxpÙ±‚`a(Ù±‚`estatsÙ±‚`a)Ù±‚`a
Ù±‚`caxsÙ±‚`a[Ù±‚bmia0Ù±‚`a,Ù±‚`a Ù±‚bmia0Ù±‚`a]Ù±‚aoa.Ù±‚`iset_titleÙ±‚`a(Ù±‚bs1a'Ù±‚bs1gDefaultÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`hfontsizeÙ±‚aoa=Ù±‚`bfsÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`caxsÙ±‚`a[Ù±‚bmia0Ù±‚`a,Ù±‚`a Ù±‚bmia1Ù±‚`a]Ù±‚aoa.Ù±‚`cbxpÙ±‚`a(Ù±‚`estatsÙ±‚`a,Ù±‚`a Ù±‚`ishowmeansÙ±‚aoa=Ù±‚bkcdTrueÙ±‚`a)Ù±‚`a
Ù±‚`caxsÙ±‚`a[Ù±‚bmia0Ù±‚`a,Ù±‚`a Ù±‚bmia1Ù±‚`a]Ù±‚aoa.Ù±‚`iset_titleÙ±‚`a(Ù±‚bs1a'Ù±‚bs1nshowmeans=TrueÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`hfontsizeÙ±‚aoa=Ù±‚`bfsÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`caxsÙ±‚`a[Ù±‚bmia0Ù±‚`a,Ù±‚`a Ù±‚bmia2Ù±‚`a]Ù±‚aoa.Ù±‚`cbxpÙ±‚`a(Ù±‚`estatsÙ±‚`a,Ù±‚`a Ù±‚`ishowmeansÙ±‚aoa=Ù±‚bkcdTrueÙ±‚`a,Ù±‚`a Ù±‚`hmeanlineÙ±‚aoa=Ù±‚bkcdTrueÙ±‚`a)Ù±‚`a
Ù±‚`caxsÙ±‚`a[Ù±‚bmia0Ù±‚`a,Ù±‚`a Ù±‚bmia2Ù±‚`a]Ù±‚aoa.Ù±‚`iset_titleÙ±‚`a(Ù±‚bs1a'Ù±‚bs1oshowmeans=True,Ù±‚bseb\nÙ±‚bs1mmeanline=TrueÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`hfontsizeÙ±‚aoa=Ù±‚`bfsÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`caxsÙ±‚`a[Ù±‚bmia1Ù±‚`a,Ù±‚`a Ù±‚bmia0Ù±‚`a]Ù±‚aoa.Ù±‚`cbxpÙ±‚`a(Ù±‚`estatsÙ±‚`a,Ù±‚`a Ù±‚`gshowboxÙ±‚aoa=Ù±‚bkceFalseÙ±‚`a,Ù±‚`a Ù±‚`hshowcapsÙ±‚aoa=Ù±‚bkceFalseÙ±‚`a)Ù±‚`a
Ù±‚`ktufte_titleÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bs1a'Ù±‚bs1kTufte StyleÙ±‚bseb\nÙ±‚bs1o(showbox=False,Ù±‚bseb\nÙ±‚bs1oshowcaps=False)Ù±‚bs1a'Ù±‚`a
Ù±‚`caxsÙ±‚`a[Ù±‚bmia1Ù±‚`a,Ù±‚`a Ù±‚bmia0Ù±‚`a]Ù±‚aoa.Ù±‚`iset_titleÙ±‚`a(Ù±‚`ktufte_titleÙ±‚`a,Ù±‚`a Ù±‚`hfontsizeÙ±‚aoa=Ù±‚`bfsÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`caxsÙ±‚`a[Ù±‚bmia1Ù±‚`a,Ù±‚`a Ù±‚bmia1Ù±‚`a]Ù±‚aoa.Ù±‚`cbxpÙ±‚`a(Ù±‚`estatsÙ±‚`a,Ù±‚`a Ù±‚`kshownotchesÙ±‚aoa=Ù±‚bkcdTrueÙ±‚`a)Ù±‚`a
Ù±‚`caxsÙ±‚`a[Ù±‚bmia1Ù±‚`a,Ù±‚`a Ù±‚bmia1Ù±‚`a]Ù±‚aoa.Ù±‚`iset_titleÙ±‚`a(Ù±‚bs1a'Ù±‚bs1jnotch=TrueÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`hfontsizeÙ±‚aoa=Ù±‚`bfsÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`caxsÙ±‚`a[Ù±‚bmia1Ù±‚`a,Ù±‚`a Ù±‚bmia2Ù±‚`a]Ù±‚aoa.Ù±‚`cbxpÙ±‚`a(Ù±‚`estatsÙ±‚`a,Ù±‚`a Ù±‚`jshowfliersÙ±‚aoa=Ù±‚bkceFalseÙ±‚`a)Ù±‚`a
Ù±‚`caxsÙ±‚`a[Ù±‚bmia1Ù±‚`a,Ù±‚`a Ù±‚bmia2Ù±‚`a]Ù±‚aoa.Ù±‚`iset_titleÙ±‚`a(Ù±‚bs1a'Ù±‚bs1pshowfliers=FalseÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`hfontsizeÙ±‚aoa=Ù±‚`bfsÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚akcforÙ±‚`a Ù±‚`baxÙ±‚`a Ù±‚bowbinÙ±‚`a Ù±‚`caxsÙ±‚aoa.Ù±‚`dflatÙ±‚`a:Ù±‚`a
Ù±‚`d    Ù±‚`baxÙ±‚aoa.Ù±‚`jset_yscaleÙ±‚`a(Ù±‚bs1a'Ù±‚bs1clogÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`baxÙ±‚aoa.Ù±‚`oset_yticklabelsÙ±‚`a(Ù±‚`a[Ù±‚`a]Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`cfigÙ±‚aoa.Ù±‚`osubplots_adjustÙ±‚`a(Ù±‚`fhspaceÙ±‚aoa=Ù±‚bmfc0.4Ù±‚`a)Ù±‚`a
Ù±‚`cpltÙ±‚aoa.Ù±‚`dshowÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚bc1xO###############################################################################Ù±‚`a
Ù±‚bc1x># Demonstrate how to customize the display different elements:Ù±‚`a
Ù±‚`a
Ù±‚`hboxpropsÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bnbddictÙ±‚`a(Ù±‚`ilinestyleÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1b--Ù±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`ilinewidthÙ±‚aoa=Ù±‚bmia3Ù±‚`a,Ù±‚`a Ù±‚`ecolorÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1mdarkgoldenrodÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`jflierpropsÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bnbddictÙ±‚`a(Ù±‚`fmarkerÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1aoÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`omarkerfacecolorÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1egreenÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`jmarkersizeÙ±‚aoa=Ù±‚bmib12Ù±‚`a,Ù±‚`a
Ù±‚`r                  Ù±‚`ilinestyleÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1dnoneÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`kmedianpropsÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bnbddictÙ±‚`a(Ù±‚`ilinestyleÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1b-.Ù±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`ilinewidthÙ±‚aoa=Ù±‚bmfc2.5Ù±‚`a,Ù±‚`a Ù±‚`ecolorÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1ifirebrickÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`nmeanpointpropsÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bnbddictÙ±‚`a(Ù±‚`fmarkerÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1aDÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`omarkeredgecolorÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1eblackÙ±‚bs1a'Ù±‚`a,Ù±‚`a
Ù±‚`v                      Ù±‚`omarkerfacecolorÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1ifirebrickÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`mmeanlinepropsÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bnbddictÙ±‚`a(Ù±‚`ilinestyleÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1b--Ù±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`ilinewidthÙ±‚aoa=Ù±‚bmfc2.5Ù±‚`a,Ù±‚`a Ù±‚`ecolorÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1fpurpleÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`cfigÙ±‚`a,Ù±‚`a Ù±‚`caxsÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cpltÙ±‚aoa.Ù±‚`hsubplotsÙ±‚`a(Ù±‚`enrowsÙ±‚aoa=Ù±‚bmia2Ù±‚`a,Ù±‚`a Ù±‚`encolsÙ±‚aoa=Ù±‚bmia2Ù±‚`a,Ù±‚`a Ù±‚`gfigsizeÙ±‚aoa=Ù±‚`a(Ù±‚bmia6Ù±‚`a,Ù±‚`a Ù±‚bmia6Ù±‚`a)Ù±‚`a,Ù±‚`a Ù±‚`fshareyÙ±‚aoa=Ù±‚bkcdTrueÙ±‚`a)Ù±‚`a
Ù±‚`caxsÙ±‚`a[Ù±‚bmia0Ù±‚`a,Ù±‚`a Ù±‚bmia0Ù±‚`a]Ù±‚aoa.Ù±‚`cbxpÙ±‚`a(Ù±‚`estatsÙ±‚`a,Ù±‚`a Ù±‚`hboxpropsÙ±‚aoa=Ù±‚`hboxpropsÙ±‚`a)Ù±‚`a
Ù±‚`caxsÙ±‚`a[Ù±‚bmia0Ù±‚`a,Ù±‚`a Ù±‚bmia0Ù±‚`a]Ù±‚aoa.Ù±‚`iset_titleÙ±‚`a(Ù±‚bs1a'Ù±‚bs1oCustom boxpropsÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`hfontsizeÙ±‚aoa=Ù±‚`bfsÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`caxsÙ±‚`a[Ù±‚bmia0Ù±‚`a,Ù±‚`a Ù±‚bmia1Ù±‚`a]Ù±‚aoa.Ù±‚`cbxpÙ±‚`a(Ù±‚`estatsÙ±‚`a,Ù±‚`a Ù±‚`jflierpropsÙ±‚aoa=Ù±‚`jflierpropsÙ±‚`a,Ù±‚`a Ù±‚`kmedianpropsÙ±‚aoa=Ù±‚`kmedianpropsÙ±‚`a)Ù±‚`a
Ù±‚`caxsÙ±‚`a[Ù±‚bmia0Ù±‚`a,Ù±‚`a Ù±‚bmia1Ù±‚`a]Ù±‚aoa.Ù±‚`iset_titleÙ±‚`a(Ù±‚bs1a'Ù±‚bs1rCustom medianpropsÙ±‚bseb\nÙ±‚bs1nand flierpropsÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`hfontsizeÙ±‚aoa=Ù±‚`bfsÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`caxsÙ±‚`a[Ù±‚bmia1Ù±‚`a,Ù±‚`a Ù±‚bmia0Ù±‚`a]Ù±‚aoa.Ù±‚`cbxpÙ±‚`a(Ù±‚`estatsÙ±‚`a,Ù±‚`a Ù±‚`imeanpropsÙ±‚aoa=Ù±‚`nmeanpointpropsÙ±‚`a,Ù±‚`a Ù±‚`hmeanlineÙ±‚aoa=Ù±‚bkceFalseÙ±‚`a,Ù±‚`a
Ù±‚`n              Ù±‚`ishowmeansÙ±‚aoa=Ù±‚bkcdTrueÙ±‚`a)Ù±‚`a
Ù±‚`caxsÙ±‚`a[Ù±‚bmia1Ù±‚`a,Ù±‚`a Ù±‚bmia0Ù±‚`a]Ù±‚aoa.Ù±‚`iset_titleÙ±‚`a(Ù±‚bs1a'Ù±‚bs1kCustom meanÙ±‚bseb\nÙ±‚bs1has pointÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`hfontsizeÙ±‚aoa=Ù±‚`bfsÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`caxsÙ±‚`a[Ù±‚bmia1Ù±‚`a,Ù±‚`a Ù±‚bmia1Ù±‚`a]Ù±‚aoa.Ù±‚`cbxpÙ±‚`a(Ù±‚`estatsÙ±‚`a,Ù±‚`a Ù±‚`imeanpropsÙ±‚aoa=Ù±‚`mmeanlinepropsÙ±‚`a,Ù±‚`a Ù±‚`hmeanlineÙ±‚aoa=Ù±‚bkcdTrueÙ±‚`a,Ù±‚`a
Ù±‚`n              Ù±‚`ishowmeansÙ±‚aoa=Ù±‚bkcdTrueÙ±‚`a)Ù±‚`a
Ù±‚`caxsÙ±‚`a[Ù±‚bmia1Ù±‚`a,Ù±‚`a Ù±‚bmia1Ù±‚`a]Ù±‚aoa.Ù±‚`iset_titleÙ±‚`a(Ù±‚bs1a'Ù±‚bs1kCustom meanÙ±‚bseb\nÙ±‚bs1gas lineÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`hfontsizeÙ±‚aoa=Ù±‚`bfsÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚akcforÙ±‚`a Ù±‚`baxÙ±‚`a Ù±‚bowbinÙ±‚`a Ù±‚`caxsÙ±‚aoa.Ù±‚`dflatÙ±‚`a:Ù±‚`a
Ù±‚`d    Ù±‚`baxÙ±‚aoa.Ù±‚`jset_yscaleÙ±‚`a(Ù±‚bs1a'Ù±‚bs1clogÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`baxÙ±‚aoa.Ù±‚`oset_yticklabelsÙ±‚`a(Ù±‚`a[Ù±‚`a]Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`cfigÙ±‚aoa.Ù±‚`hsuptitleÙ±‚`a(Ù±‚bs2a"Ù±‚bs2qI never said theyÙ±‚bs2a'Ù±‚bs2kd be prettyÙ±‚bs2a"Ù±‚`a)Ù±‚`a
Ù±‚`cfigÙ±‚aoa.Ù±‚`osubplots_adjustÙ±‚`a(Ù±‚`fhspaceÙ±‚aoa=Ù±‚bmfc0.4Ù±‚`a)Ù±‚`a
Ù±‚`cpltÙ±‚aoa.Ù±‚`dshowÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚bc1xM#############################################################################Ù±‚`a
Ù±‚bc1a#Ù±‚`a
Ù±‚bc1x# .. admonition:: ReferencesÙ±‚`a
Ù±‚bc1a#Ù±‚`a
Ù±‚bc1xN#    The use of the following functions, methods, classes and modules is shownÙ±‚`a
Ù±‚bc1u#    in this example:Ù±‚`a
Ù±‚bc1a#Ù±‚`a
Ù±‚bc1x!#    - `matplotlib.axes.Axes.bxp`Ù±‚`a
Ù±‚bc1x'#    - `matplotlib.cbook.boxplot_stats`Ù±‚`a
`dNoneö