ŸØÇÅŸ¥ÉôvŸ±Çbsdyí"""
===============================
Resizing axes with tight layout
===============================

`~.figure.Figure.tight_layout` attempts to resize subplots in
a figure so that there are no overlaps between axes objects and labels
on the axes.

See :doc:`/tutorials/intermediate/tight_layout_guide` for more details and
:doc:`/tutorials/intermediate/constrainedlayout_guide` for an alternative.

"""Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±ÇbknfimportŸ±Ç`a Ÿ±ÇbnnŸ¢ÑjmatplotlibŸ†Ñjmatplotlibe3.5.1fmodulejmatplotlibfmoduleıŸ±Çbnna.Ÿ±ÇbnnfpyplotŸ±Ç`a Ÿ±ÇakbasŸ±Ç`a Ÿ±ÇbnncpltŸ±Ç`a
Ÿ±ÇbknfimportŸ±Ç`a Ÿ±ÇbnniitertoolsŸ±Ç`a
Ÿ±ÇbknfimportŸ±Ç`a Ÿ±ÇbnnhwarningsŸ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`ifontsizesŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`iitertoolsŸ±Çaoa.Ÿ±Ç`ecycleŸ±Ç`a(Ÿ±Ç`a[Ÿ±Çbmia8Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmib16Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmib24Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmib32Ÿ±Ç`a]Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±ÇakcdefŸ±Ç`a Ÿ±Çbnflexample_plotŸ±Ç`a(Ÿ±Ç`baxŸ±Ç`a)Ÿ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`dplotŸ±Ç`a(Ÿ±Ç`a[Ÿ±Çbmia1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia2Ÿ±Ç`a]Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`jset_xlabelŸ±Ç`a(Ÿ±Çbs1a'Ÿ±Çbs1gx-labelŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`hfontsizeŸ±Çaoa=Ÿ±ÇbnbdnextŸ±Ç`a(Ÿ±Ç`ifontsizesŸ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`jset_ylabelŸ±Ç`a(Ÿ±Çbs1a'Ÿ±Çbs1gy-labelŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`hfontsizeŸ±Çaoa=Ÿ±ÇbnbdnextŸ±Ç`a(Ÿ±Ç`ifontsizesŸ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`iset_titleŸ±Ç`a(Ÿ±Çbs1a'Ÿ±Çbs1eTitleŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`hfontsizeŸ±Çaoa=Ÿ±ÇbnbdnextŸ±Ç`a(Ÿ±Ç`ifontsizesŸ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1xO###############################################################################Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`cfigŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`baxŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`hsubplotsŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`lexample_plotŸ±Ç`a(Ÿ±Ç`baxŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cfigŸ±Çaoa.Ÿ±Ç`ltight_layoutŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1xO###############################################################################Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`cfigŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`a(Ÿ±Ç`a(Ÿ±Ç`cax1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`cax2Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`a(Ÿ±Ç`cax3Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`cax4Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`hsubplotsŸ±Ç`a(Ÿ±Ç`enrowsŸ±Çaoa=Ÿ±Çbmia2Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`encolsŸ±Çaoa=Ÿ±Çbmia2Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`lexample_plotŸ±Ç`a(Ÿ±Ç`cax1Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`lexample_plotŸ±Ç`a(Ÿ±Ç`cax2Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`lexample_plotŸ±Ç`a(Ÿ±Ç`cax3Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`lexample_plotŸ±Ç`a(Ÿ±Ç`cax4Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cfigŸ±Çaoa.Ÿ±Ç`ltight_layoutŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1xO###############################################################################Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`cfigŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`a(Ÿ±Ç`cax1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`cax2Ÿ±Ç`a)Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`hsubplotsŸ±Ç`a(Ÿ±Ç`enrowsŸ±Çaoa=Ÿ±Çbmia2Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`encolsŸ±Çaoa=Ÿ±Çbmia1Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`lexample_plotŸ±Ç`a(Ÿ±Ç`cax1Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`lexample_plotŸ±Ç`a(Ÿ±Ç`cax2Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cfigŸ±Çaoa.Ÿ±Ç`ltight_layoutŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1xO###############################################################################Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`cfigŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`a(Ÿ±Ç`cax1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`cax2Ÿ±Ç`a)Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`hsubplotsŸ±Ç`a(Ÿ±Ç`enrowsŸ±Çaoa=Ÿ±Çbmia1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`encolsŸ±Çaoa=Ÿ±Çbmia2Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`lexample_plotŸ±Ç`a(Ÿ±Ç`cax1Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`lexample_plotŸ±Ç`a(Ÿ±Ç`cax2Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cfigŸ±Çaoa.Ÿ±Ç`ltight_layoutŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1xO###############################################################################Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`cfigŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`caxsŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`hsubplotsŸ±Ç`a(Ÿ±Ç`enrowsŸ±Çaoa=Ÿ±Çbmia3Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`encolsŸ±Çaoa=Ÿ±Çbmia3Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±ÇakcforŸ±Ç`a Ÿ±Ç`baxŸ±Ç`a Ÿ±ÇbowbinŸ±Ç`a Ÿ±Ç`caxsŸ±Çaoa.Ÿ±Ç`dflatŸ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`lexample_plotŸ±Ç`a(Ÿ±Ç`baxŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cfigŸ±Çaoa.Ÿ±Ç`ltight_layoutŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1xO###############################################################################Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`ffigureŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cax1Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`gsubplotŸ±Ç`a(Ÿ±Çbmic221Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cax2Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`gsubplotŸ±Ç`a(Ÿ±Çbmic223Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cax3Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`gsubplotŸ±Ç`a(Ÿ±Çbmic122Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`lexample_plotŸ±Ç`a(Ÿ±Ç`cax1Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`lexample_plotŸ±Ç`a(Ÿ±Ç`cax2Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`lexample_plotŸ±Ç`a(Ÿ±Ç`cax3Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`ltight_layoutŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1xO###############################################################################Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`ffigureŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cax1Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`lsubplot2gridŸ±Ç`a(Ÿ±Ç`a(Ÿ±Çbmia3Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia3Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`a(Ÿ±Çbmia0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia0Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cax2Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`lsubplot2gridŸ±Ç`a(Ÿ±Ç`a(Ÿ±Çbmia3Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia3Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`a(Ÿ±Çbmia0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia1Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`gcolspanŸ±Çaoa=Ÿ±Çbmia2Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cax3Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`lsubplot2gridŸ±Ç`a(Ÿ±Ç`a(Ÿ±Çbmia3Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia3Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`a(Ÿ±Çbmia1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia0Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`gcolspanŸ±Çaoa=Ÿ±Çbmia2Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`growspanŸ±Çaoa=Ÿ±Çbmia2Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cax4Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`lsubplot2gridŸ±Ç`a(Ÿ±Ç`a(Ÿ±Çbmia3Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia3Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`a(Ÿ±Çbmia1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia2Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`growspanŸ±Çaoa=Ÿ±Çbmia2Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`lexample_plotŸ±Ç`a(Ÿ±Ç`cax1Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`lexample_plotŸ±Ç`a(Ÿ±Ç`cax2Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`lexample_plotŸ±Ç`a(Ÿ±Ç`cax3Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`lexample_plotŸ±Ç`a(Ÿ±Ç`cax4Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`ltight_layoutŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1xO###############################################################################Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`cfigŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`ffigureŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`cgs1Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cfigŸ±Çaoa.Ÿ±Ç`ladd_gridspecŸ±Ç`a(Ÿ±Çbmia3Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia1Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cax1Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cfigŸ±Çaoa.Ÿ±Ç`kadd_subplotŸ±Ç`a(Ÿ±Ç`cgs1Ÿ±Ç`a[Ÿ±Çbmia0Ÿ±Ç`a]Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cax2Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cfigŸ±Çaoa.Ÿ±Ç`kadd_subplotŸ±Ç`a(Ÿ±Ç`cgs1Ÿ±Ç`a[Ÿ±Çbmia1Ÿ±Ç`a]Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cax3Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cfigŸ±Çaoa.Ÿ±Ç`kadd_subplotŸ±Ç`a(Ÿ±Ç`cgs1Ÿ±Ç`a[Ÿ±Çbmia2Ÿ±Ç`a]Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`lexample_plotŸ±Ç`a(Ÿ±Ç`cax1Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`lexample_plotŸ±Ç`a(Ÿ±Ç`cax2Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`lexample_plotŸ±Ç`a(Ÿ±Ç`cax3Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cgs1Ÿ±Çaoa.Ÿ±Ç`ltight_layoutŸ±Ç`a(Ÿ±Ç`cfigŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`drectŸ±Çaoa=Ÿ±Ç`a[Ÿ±ÇbkcdNoneŸ±Ç`a,Ÿ±Ç`a Ÿ±ÇbkcdNoneŸ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd0.45Ÿ±Ç`a,Ÿ±Ç`a Ÿ±ÇbkcdNoneŸ±Ç`a]Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`cgs2Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cfigŸ±Çaoa.Ÿ±Ç`ladd_gridspecŸ±Ç`a(Ÿ±Çbmia2Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia1Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cax4Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cfigŸ±Çaoa.Ÿ±Ç`kadd_subplotŸ±Ç`a(Ÿ±Ç`cgs2Ÿ±Ç`a[Ÿ±Çbmia0Ÿ±Ç`a]Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cax5Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cfigŸ±Çaoa.Ÿ±Ç`kadd_subplotŸ±Ç`a(Ÿ±Ç`cgs2Ÿ±Ç`a[Ÿ±Çbmia1Ÿ±Ç`a]Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`lexample_plotŸ±Ç`a(Ÿ±Ç`cax4Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`lexample_plotŸ±Ç`a(Ÿ±Ç`cax5Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±ÇakdwithŸ±Ç`a Ÿ±Ç`hwarningsŸ±Çaoa.Ÿ±Ç`ncatch_warningsŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Çbc1xE# gs2.tight_layout cannot handle the subplots from the first gridspecŸ±Ç`a
Ÿ±Ç`d    Ÿ±Çbc1xH# (gs1), so it will raise a warning. We are going to match the gridspecsŸ±Ç`a
Ÿ±Ç`d    Ÿ±Çbc1x-# manually so we can filter the warning away.Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`hwarningsŸ±Çaoa.Ÿ±Ç`lsimplefilterŸ±Ç`a(Ÿ±Çbs2a"Ÿ±Çbs2fignoreŸ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a Ÿ±ÇbnekUserWarningŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`cgs2Ÿ±Çaoa.Ÿ±Ç`ltight_layoutŸ±Ç`a(Ÿ±Ç`cfigŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`drectŸ±Çaoa=Ÿ±Ç`a[Ÿ±Çbmfd0.45Ÿ±Ç`a,Ÿ±Ç`a Ÿ±ÇbkcdNoneŸ±Ç`a,Ÿ±Ç`a Ÿ±ÇbkcdNoneŸ±Ç`a,Ÿ±Ç`a Ÿ±ÇbkcdNoneŸ±Ç`a]Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1x0# now match the top and bottom of two gridspecs.Ÿ±Ç`a
Ÿ±Ç`ctopŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±ÇbnbcminŸ±Ç`a(Ÿ±Ç`cgs1Ÿ±Çaoa.Ÿ±Ç`ctopŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`cgs2Ÿ±Çaoa.Ÿ±Ç`ctopŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`fbottomŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±ÇbnbcmaxŸ±Ç`a(Ÿ±Ç`cgs1Ÿ±Çaoa.Ÿ±Ç`fbottomŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`cgs2Ÿ±Çaoa.Ÿ±Ç`fbottomŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`cgs1Ÿ±Çaoa.Ÿ±Ç`fupdateŸ±Ç`a(Ÿ±Ç`ctopŸ±Çaoa=Ÿ±Ç`ctopŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`fbottomŸ±Çaoa=Ÿ±Ç`fbottomŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cgs2Ÿ±Çaoa.Ÿ±Ç`fupdateŸ±Ç`a(Ÿ±Ç`ctopŸ±Çaoa=Ÿ±Ç`ctopŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`fbottomŸ±Çaoa=Ÿ±Ç`fbottomŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`dshowŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1xM#############################################################################Ÿ±Ç`a
Ÿ±Çbc1a#Ÿ±Ç`a
Ÿ±Çbc1x# .. admonition:: ReferencesŸ±Ç`a
Ÿ±Çbc1a#Ÿ±Ç`a
Ÿ±Çbc1xN#    The use of the following functions, methods, classes and modules is shownŸ±Ç`a
Ÿ±Çbc1u#    in this example:Ÿ±Ç`a
Ÿ±Çbc1a#Ÿ±Ç`a
Ÿ±Çbc1x0#    - `matplotlib.figure.Figure.tight_layout` /Ÿ±Ç`a
Ÿ±Çbc1x'#      `matplotlib.pyplot.tight_layout`Ÿ±Ç`a
Ÿ±Çbc1x.#    - `matplotlib.figure.Figure.add_gridspec`Ÿ±Ç`a
Ÿ±Çbc1x-#    - `matplotlib.figure.Figure.add_subplot`Ÿ±Ç`a
Ÿ±Çbc1x'#    - `matplotlib.pyplot.subplot2grid`Ÿ±Ç`a
`dNoneˆ