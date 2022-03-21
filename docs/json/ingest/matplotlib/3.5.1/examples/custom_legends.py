Ù¯‚Ù´ƒ™ìÙ±‚bsdy_"""
========================
Composing Custom Legends
========================

Composing custom legends piece-by-piece.

.. note::

   For more information on creating and customizing legends, see the following
   pages:

   * :doc:`/tutorials/intermediate/legend_guide`
   * :doc:`/gallery/text_labels_and_annotations/legend_demo`

Sometimes you don't want a legend that is explicitly tied to data that
you have plotted. For example, say you have plotted 10 lines, but don't
want a legend item to show up for each one. If you simply plot the lines
and call ``ax.legend()``, you will get the following:
"""Ù±‚`a
Ù±‚bc1x%# sphinx_gallery_thumbnail_number = 2Ù±‚`a
Ù±‚bkndfromÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚`a Ù±‚bknfimportÙ±‚`a Ù±‚`hrcParamsÙ±‚`a,Ù±‚`a Ù±‚`fcyclerÙ±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnnfpyplotÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnncpltÙ±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„enumpyÙ „enumpyf1.22.3fmoduleenumpyfmoduleõÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnnbnpÙ±‚`a
Ù±‚`a
Ù±‚bc1x)# Fixing random state for reproducibilityÙ±‚`a
Ù±‚`bnpÙ±‚aoa.Ù±‚`frandomÙ±‚aoa.Ù±‚`dseedÙ±‚`a(Ù±‚bmih19680801Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`aNÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bmib10Ù±‚`a
Ù±‚`ddataÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`a(Ù±‚`bnpÙ±‚aoa.Ù±‚`igeomspaceÙ±‚`a(Ù±‚bmia1Ù±‚`a,Ù±‚`a Ù±‚bmib10Ù±‚`a,Ù±‚`a Ù±‚bmic100Ù±‚`a)Ù±‚`a Ù±‚aoa+Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`frandomÙ±‚aoa.Ù±‚`erandnÙ±‚`a(Ù±‚`aNÙ±‚`a,Ù±‚`a Ù±‚bmic100Ù±‚`a)Ù±‚`a)Ù±‚aoa.Ù±‚`aTÙ±‚`a
Ù±‚`dcmapÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cpltÙ±‚aoa.Ù±‚`bcmÙ±‚aoa.Ù±‚`hcoolwarmÙ±‚`a
Ù±‚`hrcParamsÙ±‚`a[Ù±‚bs1a'Ù±‚bs1oaxes.prop_cycleÙ±‚bs1a'Ù±‚`a]Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`fcyclerÙ±‚`a(Ù±‚`ecolorÙ±‚aoa=Ù±‚`dcmapÙ±‚`a(Ù±‚`bnpÙ±‚aoa.Ù±‚`hlinspaceÙ±‚`a(Ù±‚bmia0Ù±‚`a,Ù±‚`a Ù±‚bmia1Ù±‚`a,Ù±‚`a Ù±‚`aNÙ±‚`a)Ù±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`cfigÙ±‚`a,Ù±‚`a Ù±‚`baxÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cpltÙ±‚aoa.Ù±‚`hsubplotsÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`elinesÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`baxÙ±‚aoa.Ù±‚`dplotÙ±‚`a(Ù±‚`ddataÙ±‚`a)Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`flegendÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚bc1xN##############################################################################Ù±‚`a
Ù±‚bc1x+# Note that no legend entries were created.Ù±‚`a
Ù±‚bc1xL# In this case, we can compose a legend using Matplotlib objects that aren'tÙ±‚`a
Ù±‚bc1x<# explicitly tied to the data that was plotted. For example:Ù±‚`a
Ù±‚`a
Ù±‚bkndfromÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnnelinesÙ±‚`a Ù±‚bknfimportÙ±‚`a Ù±‚`fLine2DÙ±‚`a
Ù±‚`lcustom_linesÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`a[Ù±‚`fLine2DÙ±‚`a(Ù±‚`a[Ù±‚bmia0Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`a[Ù±‚bmia0Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`ecolorÙ±‚aoa=Ù±‚`dcmapÙ±‚`a(Ù±‚bmfb0.Ù±‚`a)Ù±‚`a,Ù±‚`a Ù±‚`blwÙ±‚aoa=Ù±‚bmia4Ù±‚`a)Ù±‚`a,Ù±‚`a
Ù±‚`p                Ù±‚`fLine2DÙ±‚`a(Ù±‚`a[Ù±‚bmia0Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`a[Ù±‚bmia0Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`ecolorÙ±‚aoa=Ù±‚`dcmapÙ±‚`a(Ù±‚bmfb.5Ù±‚`a)Ù±‚`a,Ù±‚`a Ù±‚`blwÙ±‚aoa=Ù±‚bmia4Ù±‚`a)Ù±‚`a,Ù±‚`a
Ù±‚`p                Ù±‚`fLine2DÙ±‚`a(Ù±‚`a[Ù±‚bmia0Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`a[Ù±‚bmia0Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`ecolorÙ±‚aoa=Ù±‚`dcmapÙ±‚`a(Ù±‚bmfb1.Ù±‚`a)Ù±‚`a,Ù±‚`a Ù±‚`blwÙ±‚aoa=Ù±‚bmia4Ù±‚`a)Ù±‚`a]Ù±‚`a
Ù±‚`a
Ù±‚`cfigÙ±‚`a,Ù±‚`a Ù±‚`baxÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cpltÙ±‚aoa.Ù±‚`hsubplotsÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`elinesÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`baxÙ±‚aoa.Ù±‚`dplotÙ±‚`a(Ù±‚`ddataÙ±‚`a)Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`flegendÙ±‚`a(Ù±‚`lcustom_linesÙ±‚`a,Ù±‚`a Ù±‚`a[Ù±‚bs1a'Ù±‚bs1dColdÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚bs1a'Ù±‚bs1fMediumÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚bs1a'Ù±‚bs1cHotÙ±‚bs1a'Ù±‚`a]Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚bc1xO###############################################################################Ù±‚`a
Ù±‚bc1xN# There are many other Matplotlib objects that can be used in this way. In theÙ±‚`a
Ù±‚bc1x,# code below we've listed a few common ones.Ù±‚`a
Ù±‚`a
Ù±‚bkndfromÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnngpatchesÙ±‚`a Ù±‚bknfimportÙ±‚`a Ù±‚`ePatchÙ±‚`a
Ù±‚bkndfromÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnnelinesÙ±‚`a Ù±‚bknfimportÙ±‚`a Ù±‚`fLine2DÙ±‚`a
Ù±‚`a
Ù±‚`olegend_elementsÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`a[Ù±‚`fLine2DÙ±‚`a(Ù±‚`a[Ù±‚bmia0Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`a[Ù±‚bmia0Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`ecolorÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1abÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`blwÙ±‚aoa=Ù±‚bmia4Ù±‚`a,Ù±‚`a Ù±‚`elabelÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1dLineÙ±‚bs1a'Ù±‚`a)Ù±‚`a,Ù±‚`a
Ù±‚`s                   Ù±‚`fLine2DÙ±‚`a(Ù±‚`a[Ù±‚bmia0Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`a[Ù±‚bmia0Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`fmarkerÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1aoÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`ecolorÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1awÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`elabelÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1gScatterÙ±‚bs1a'Ù±‚`a,Ù±‚`a
Ù±‚`x                          Ù±‚`omarkerfacecolorÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1agÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`jmarkersizeÙ±‚aoa=Ù±‚bmib15Ù±‚`a)Ù±‚`a,Ù±‚`a
Ù±‚`s                   Ù±‚`ePatchÙ±‚`a(Ù±‚`ifacecolorÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1forangeÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`iedgecolorÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1arÙ±‚bs1a'Ù±‚`a,Ù±‚`a
Ù±‚`x                         Ù±‚`elabelÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1kColor PatchÙ±‚bs1a'Ù±‚`a)Ù±‚`a]Ù±‚`a
Ù±‚`a
Ù±‚bc1s# Create the figureÙ±‚`a
Ù±‚`cfigÙ±‚`a,Ù±‚`a Ù±‚`baxÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cpltÙ±‚aoa.Ù±‚`hsubplotsÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`flegendÙ±‚`a(Ù±‚`ghandlesÙ±‚aoa=Ù±‚`olegend_elementsÙ±‚`a,Ù±‚`a Ù±‚`clocÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1fcenterÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`cpltÙ±‚aoa.Ù±‚`dshowÙ±‚`a(Ù±‚`a)Ù±‚`a
`dNoneö