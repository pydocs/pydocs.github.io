ŸØÇÅŸ¥ÉôŸ±Çbsdx√"""
==========
Arrow Demo
==========

Three ways of drawing arrows to encode arrow "strength" (e.g., transition
probabilities in a Markov model) using arrow length, width, or alpha (opacity).
"""Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±ÇbknfimportŸ±Ç`a Ÿ±ÇbnniitertoolsŸ±Ç`a
Ÿ±Ç`a
Ÿ±ÇbknfimportŸ±Ç`a Ÿ±ÇbnnŸ¢ÑjmatplotlibŸ†Ñjmatplotlibe3.5.1fmodulejmatplotlibfmoduleıŸ±Çbnna.Ÿ±ÇbnnfpyplotŸ±Ç`a Ÿ±ÇakbasŸ±Ç`a Ÿ±ÇbnncpltŸ±Ç`a
Ÿ±ÇbknfimportŸ±Ç`a Ÿ±ÇbnnŸ¢ÑenumpyŸ†Ñenumpyf1.22.3fmoduleenumpyfmoduleıŸ±Ç`a Ÿ±ÇakbasŸ±Ç`a Ÿ±ÇbnnbnpŸ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±ÇakcdefŸ±Ç`a Ÿ±Çbnfpmake_arrow_graphŸ±Ç`a(Ÿ±Ç`baxŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ddataŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dsizeŸ±Çaoa=Ÿ±Çbmia4Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`gdisplayŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1flengthŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`eshapeŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1erightŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`u                     Ÿ±Ç`omax_arrow_widthŸ±Çaoa=Ÿ±Çbmfd0.03Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`iarrow_sepŸ±Çaoa=Ÿ±Çbmfd0.02Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ealphaŸ±Çaoa=Ÿ±Çbmfc0.5Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`u                     Ÿ±Ç`nnormalize_dataŸ±Çaoa=Ÿ±ÇbkceFalseŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`becŸ±Çaoa=Ÿ±ÇbkcdNoneŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`jlabelcolorŸ±Çaoa=Ÿ±ÇbkcdNoneŸ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`u                     Ÿ±Çaoa*Ÿ±Çaoa*Ÿ±Ç`fkwargsŸ±Ç`a)Ÿ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Çbsdyπ"""
    Makes an arrow plot.

    Parameters
    ----------
    ax
        The axes where the graph is drawn.
    data
        Dict with probabilities for the bases and pair transitions.
    size
        Size of the plot, in inches.
    display : {'length', 'width', 'alpha'}
        The arrow property to change.
    shape : {'full', 'left', 'right'}
        For full or half arrows.
    max_arrow_width : float
        Maximum width of an arrow, in data coordinates.
    arrow_sep : float
        Separation between arrows in a pair, in data coordinates.
    alpha : float
        Maximum opacity of arrows.
    **kwargs
        `.FancyArrow` properties, e.g. *linewidth* or *edgecolor*.
    """Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`csetŸ±Ç`a(Ÿ±Ç`dxlimŸ±Çaoa=Ÿ±Ç`a(Ÿ±Çaoa-Ÿ±Çbmfc0.5Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfc1.5Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dylimŸ±Çaoa=Ÿ±Ç`a(Ÿ±Çaoa-Ÿ±Çbmfc0.5Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfc1.5Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`fxticksŸ±Çaoa=Ÿ±Ç`a[Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`fyticksŸ±Çaoa=Ÿ±Ç`a[Ÿ±Ç`a]Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`dtextŸ±Ç`a(Ÿ±Çbmfc.01Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfc.01Ÿ±Ç`a,Ÿ±Ç`a Ÿ±ÇbsaafŸ±Çbs1a'Ÿ±Çbs1vflux encoded as arrow Ÿ±Çbsia{Ÿ±Ç`gdisplayŸ±Çbsia}Ÿ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`l            Ÿ±Ç`itransformŸ±Çaoa=Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`itransAxesŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`mmax_text_sizeŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`dsizeŸ±Ç`a Ÿ±Çaoa*Ÿ±Ç`a Ÿ±Çbmib12Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`mmin_text_sizeŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`dsizeŸ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`olabel_text_sizeŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`dsizeŸ±Ç`a Ÿ±Çaoa*Ÿ±Ç`a Ÿ±Çbmfc2.5Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`ebasesŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1dATGCŸ±Çbs1a'Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`fcoordsŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`a{Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±Çbs1a'Ÿ±Çbs1aAŸ±Çbs1a'Ÿ±Ç`a:Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`earrayŸ±Ç`a(Ÿ±Ç`a[Ÿ±Çbmia0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia1Ÿ±Ç`a]Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±Çbs1a'Ÿ±Çbs1aTŸ±Çbs1a'Ÿ±Ç`a:Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`earrayŸ±Ç`a(Ÿ±Ç`a[Ÿ±Çbmia1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia1Ÿ±Ç`a]Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±Çbs1a'Ÿ±Çbs1aGŸ±Çbs1a'Ÿ±Ç`a:Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`earrayŸ±Ç`a(Ÿ±Ç`a[Ÿ±Çbmia0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia0Ÿ±Ç`a]Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±Çbs1a'Ÿ±Çbs1aCŸ±Çbs1a'Ÿ±Ç`a:Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`earrayŸ±Ç`a(Ÿ±Ç`a[Ÿ±Çbmia1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia0Ÿ±Ç`a]Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`a}Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`fcolorsŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`a{Ÿ±Çbs1a'Ÿ±Çbs1aAŸ±Çbs1a'Ÿ±Ç`a:Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1arŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1aTŸ±Çbs1a'Ÿ±Ç`a:Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1akŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1aGŸ±Çbs1a'Ÿ±Ç`a:Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1agŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1aCŸ±Çbs1a'Ÿ±Ç`a:Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1abŸ±Çbs1a'Ÿ±Ç`a}Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±ÇakcforŸ±Ç`a Ÿ±Ç`dbaseŸ±Ç`a Ÿ±ÇbowbinŸ±Ç`a Ÿ±Ç`ebasesŸ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±Ç`hfontsizeŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`dclipŸ±Ç`a(Ÿ±Ç`mmax_text_sizeŸ±Ç`a Ÿ±Çaoa*Ÿ±Ç`a Ÿ±Ç`ddataŸ±Ç`a[Ÿ±Ç`dbaseŸ±Ç`a]Ÿ±Çaoa*Ÿ±Çaoa*Ÿ±Ç`a(Ÿ±Çbmia1Ÿ±Çaoa/Ÿ±Çbmia2Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`x                           Ÿ±Ç`mmin_text_sizeŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`mmax_text_sizeŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`dtextŸ±Ç`a(Ÿ±Çaoa*Ÿ±Ç`fcoordsŸ±Ç`a[Ÿ±Ç`dbaseŸ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±ÇbsaafŸ±Çbs1a'Ÿ±Çbs1a$Ÿ±Çbsia{Ÿ±Ç`dbaseŸ±Çbsia}Ÿ±Çbs1c_3$Ÿ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`p                Ÿ±Ç`ecolorŸ±Çaoa=Ÿ±Ç`fcolorsŸ±Ç`a[Ÿ±Ç`dbaseŸ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dsizeŸ±Çaoa=Ÿ±Ç`hfontsizeŸ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`p                Ÿ±Ç`shorizontalalignmentŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1fcenterŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`qverticalalignmentŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1fcenterŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`p                Ÿ±Ç`fweightŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1dboldŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`narrow_h_offsetŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Çbmfd0.25Ÿ±Ç`b  Ÿ±Çbc1x*# data coordinates, empirically determinedŸ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`pmax_arrow_lengthŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Çbmia1Ÿ±Ç`a Ÿ±Çaoa-Ÿ±Ç`a Ÿ±Çbmia2Ÿ±Ç`a Ÿ±Çaoa*Ÿ±Ç`a Ÿ±Ç`narrow_h_offsetŸ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`nmax_head_widthŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Çbmfc2.5Ÿ±Ç`a Ÿ±Çaoa*Ÿ±Ç`a Ÿ±Ç`omax_arrow_widthŸ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`omax_head_lengthŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Çbmia2Ÿ±Ç`a Ÿ±Çaoa*Ÿ±Ç`a Ÿ±Ç`omax_arrow_widthŸ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`bsfŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Çbmfc0.6Ÿ±Ç`b  Ÿ±Çbc1x/# max arrow size represents this in data coordsŸ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±ÇakbifŸ±Ç`a Ÿ±Ç`nnormalize_dataŸ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±Çbc1x@# find maximum value for rates, i.e. where keys are 2 chars longŸ±Ç`a
Ÿ±Ç`h        Ÿ±Ç`gmax_valŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±ÇbnbcmaxŸ±Ç`a(Ÿ±Ç`a(Ÿ±Ç`avŸ±Ç`a Ÿ±ÇakcforŸ±Ç`a Ÿ±Ç`akŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`avŸ±Ç`a Ÿ±ÇbowbinŸ±Ç`a Ÿ±Ç`ddataŸ±Çaoa.Ÿ±Ç`eitemsŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a Ÿ±ÇakbifŸ±Ç`a Ÿ±ÇbnbclenŸ±Ç`a(Ÿ±Ç`akŸ±Ç`a)Ÿ±Ç`a Ÿ±Çaob==Ÿ±Ç`a Ÿ±Çbmia2Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`gdefaultŸ±Çaoa=Ÿ±Çbmia0Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±Çbc1x9# divide rates by max val, multiply by arrow scale factorŸ±Ç`a
Ÿ±Ç`h        Ÿ±ÇakcforŸ±Ç`a Ÿ±Ç`akŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`avŸ±Ç`a Ÿ±ÇbowbinŸ±Ç`a Ÿ±Ç`ddataŸ±Çaoa.Ÿ±Ç`eitemsŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`l            Ÿ±Ç`ddataŸ±Ç`a[Ÿ±Ç`akŸ±Ç`a]Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`avŸ±Ç`a Ÿ±Çaoa/Ÿ±Ç`a Ÿ±Ç`gmax_valŸ±Ç`a Ÿ±Çaoa*Ÿ±Ç`a Ÿ±Ç`bsfŸ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Çbc1x3# iterate over strings 'AT', 'TA', 'AG', 'GA', etc.Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±ÇakcforŸ±Ç`a Ÿ±Ç`dpairŸ±Ç`a Ÿ±ÇbowbinŸ±Ç`a Ÿ±ÇbnbcmapŸ±Ç`a(Ÿ±Çbs1a'Ÿ±Çbs1a'Ÿ±Çaoa.Ÿ±Ç`djoinŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`iitertoolsŸ±Çaoa.Ÿ±Ç`lpermutationsŸ±Ç`a(Ÿ±Ç`ebasesŸ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia2Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±Çbc1x# set the length of the arrowŸ±Ç`a
Ÿ±Ç`h        Ÿ±ÇakbifŸ±Ç`a Ÿ±Ç`gdisplayŸ±Ç`a Ÿ±Çaob==Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1flengthŸ±Çbs1a'Ÿ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`l            Ÿ±Ç`flengthŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`a(Ÿ±Ç`omax_head_lengthŸ±Ç`a
Ÿ±Ç`v                      Ÿ±Çaoa+Ÿ±Ç`a Ÿ±Ç`ddataŸ±Ç`a[Ÿ±Ç`dpairŸ±Ç`a]Ÿ±Ç`a Ÿ±Çaoa/Ÿ±Ç`a Ÿ±Ç`bsfŸ±Ç`a Ÿ±Çaoa*Ÿ±Ç`a Ÿ±Ç`a(Ÿ±Ç`pmax_arrow_lengthŸ±Ç`a Ÿ±Çaoa-Ÿ±Ç`a Ÿ±Ç`omax_head_lengthŸ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±ÇakdelseŸ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`l            Ÿ±Ç`flengthŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`pmax_arrow_lengthŸ±Ç`a
Ÿ±Ç`h        Ÿ±Çbc1x## set the transparency of the arrowŸ±Ç`a
Ÿ±Ç`h        Ÿ±ÇakbifŸ±Ç`a Ÿ±Ç`gdisplayŸ±Ç`a Ÿ±Çaob==Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1ealphaŸ±Çbs1a'Ÿ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`l            Ÿ±Ç`ealphaŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±ÇbnbcminŸ±Ç`a(Ÿ±Ç`ddataŸ±Ç`a[Ÿ±Ç`dpairŸ±Ç`a]Ÿ±Ç`a Ÿ±Çaoa/Ÿ±Ç`a Ÿ±Ç`bsfŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ealphaŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±Çbc1x# set the width of the arrowŸ±Ç`a
Ÿ±Ç`h        Ÿ±ÇakbifŸ±Ç`a Ÿ±Ç`gdisplayŸ±Ç`a Ÿ±Çaob==Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1ewidthŸ±Çbs1a'Ÿ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`l            Ÿ±Ç`escaleŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`ddataŸ±Ç`a[Ÿ±Ç`dpairŸ±Ç`a]Ÿ±Ç`a Ÿ±Çaoa/Ÿ±Ç`a Ÿ±Ç`bsfŸ±Ç`a
Ÿ±Ç`l            Ÿ±Ç`ewidthŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`omax_arrow_widthŸ±Ç`a Ÿ±Çaoa*Ÿ±Ç`a Ÿ±Ç`escaleŸ±Ç`a
Ÿ±Ç`l            Ÿ±Ç`jhead_widthŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`nmax_head_widthŸ±Ç`a Ÿ±Çaoa*Ÿ±Ç`a Ÿ±Ç`escaleŸ±Ç`a
Ÿ±Ç`l            Ÿ±Ç`khead_lengthŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`omax_head_lengthŸ±Ç`a Ÿ±Çaoa*Ÿ±Ç`a Ÿ±Ç`escaleŸ±Ç`a
Ÿ±Ç`h        Ÿ±ÇakdelseŸ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`l            Ÿ±Ç`ewidthŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`omax_arrow_widthŸ±Ç`a
Ÿ±Ç`l            Ÿ±Ç`jhead_widthŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`nmax_head_widthŸ±Ç`a
Ÿ±Ç`l            Ÿ±Ç`khead_lengthŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`omax_head_lengthŸ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±Ç`bfcŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`fcolorsŸ±Ç`a[Ÿ±Ç`dpairŸ±Ç`a[Ÿ±Çbmia0Ÿ±Ç`a]Ÿ±Ç`a]Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±Ç`ccp0Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`fcoordsŸ±Ç`a[Ÿ±Ç`dpairŸ±Ç`a[Ÿ±Çbmia0Ÿ±Ç`a]Ÿ±Ç`a]Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±Ç`ccp1Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`fcoordsŸ±Ç`a[Ÿ±Ç`dpairŸ±Ç`a[Ÿ±Çbmia1Ÿ±Ç`a]Ÿ±Ç`a]Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±Çbc1x # unit vector in arrow directionŸ±Ç`a
Ÿ±Ç`h        Ÿ±Ç`edeltaŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`ccosŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`csinŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`a(Ÿ±Ç`ccp1Ÿ±Ç`a Ÿ±Çaoa-Ÿ±Ç`a Ÿ±Ç`ccp0Ÿ±Ç`a)Ÿ±Ç`a Ÿ±Çaoa/Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`ehypotŸ±Ç`a(Ÿ±Çaoa*Ÿ±Ç`a(Ÿ±Ç`ccp1Ÿ±Ç`a Ÿ±Çaoa-Ÿ±Ç`a Ÿ±Ç`ccp0Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±Ç`ex_posŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ey_posŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`a(Ÿ±Ç`a
Ÿ±Ç`l            Ÿ±Ç`a(Ÿ±Ç`ccp0Ÿ±Ç`a Ÿ±Çaoa+Ÿ±Ç`a Ÿ±Ç`ccp1Ÿ±Ç`a)Ÿ±Ç`a Ÿ±Çaoa/Ÿ±Ç`a Ÿ±Çbmia2Ÿ±Ç`b  Ÿ±Çbc1j# midpointŸ±Ç`a
Ÿ±Ç`l            Ÿ±Çaoa-Ÿ±Ç`a Ÿ±Ç`edeltaŸ±Ç`a Ÿ±Çaoa*Ÿ±Ç`a Ÿ±Ç`flengthŸ±Ç`a Ÿ±Çaoa/Ÿ±Ç`a Ÿ±Çbmia2Ÿ±Ç`b  Ÿ±Çbc1w# half the arrow lengthŸ±Ç`a
Ÿ±Ç`l            Ÿ±Çaoa+Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`earrayŸ±Ç`a(Ÿ±Ç`a[Ÿ±Çaoa-Ÿ±Ç`csinŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ccosŸ±Ç`a]Ÿ±Ç`a)Ÿ±Ç`a Ÿ±Çaoa*Ÿ±Ç`a Ÿ±Ç`iarrow_sepŸ±Ç`b  Ÿ±Çbc1x# shift outwards by arrow_sepŸ±Ç`a
Ÿ±Ç`h        Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`earrowŸ±Ç`a(Ÿ±Ç`a
Ÿ±Ç`l            Ÿ±Ç`ex_posŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ey_posŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ccosŸ±Ç`a Ÿ±Çaoa*Ÿ±Ç`a Ÿ±Ç`flengthŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`csinŸ±Ç`a Ÿ±Çaoa*Ÿ±Ç`a Ÿ±Ç`flengthŸ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`l            Ÿ±Ç`bfcŸ±Çaoa=Ÿ±Ç`bfcŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`becŸ±Çaoa=Ÿ±Ç`becŸ±Ç`a Ÿ±ÇbowborŸ±Ç`a Ÿ±Ç`bfcŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ealphaŸ±Çaoa=Ÿ±Ç`ealphaŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ewidthŸ±Çaoa=Ÿ±Ç`ewidthŸ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`l            Ÿ±Ç`jhead_widthŸ±Çaoa=Ÿ±Ç`jhead_widthŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`khead_lengthŸ±Çaoa=Ÿ±Ç`khead_lengthŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`eshapeŸ±Çaoa=Ÿ±Ç`eshapeŸ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`l            Ÿ±Ç`tlength_includes_headŸ±Çaoa=Ÿ±ÇbkcdTrueŸ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±Çbc1x"# figure out coordinates for text:Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±Çbc1x<# if drawing relative to base: x and y are same as for arrowŸ±Ç`a
Ÿ±Ç`h        Ÿ±Çbc1x+# dx and dy are one arrow width left and upŸ±Ç`a
Ÿ±Ç`h        Ÿ±Ç`norig_positionsŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`a{Ÿ±Ç`a
Ÿ±Ç`l            Ÿ±Çbs1a'Ÿ±Çbs1dbaseŸ±Çbs1a'Ÿ±Ç`a:Ÿ±Ç`a Ÿ±Ç`a[Ÿ±Çbmia3Ÿ±Ç`a Ÿ±Çaoa*Ÿ±Ç`a Ÿ±Ç`omax_arrow_widthŸ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia3Ÿ±Ç`a Ÿ±Çaoa*Ÿ±Ç`a Ÿ±Ç`omax_arrow_widthŸ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`l            Ÿ±Çbs1a'Ÿ±Çbs1fcenterŸ±Çbs1a'Ÿ±Ç`a:Ÿ±Ç`a Ÿ±Ç`a[Ÿ±Ç`flengthŸ±Ç`a Ÿ±Çaoa/Ÿ±Ç`a Ÿ±Çbmia2Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia3Ÿ±Ç`a Ÿ±Çaoa*Ÿ±Ç`a Ÿ±Ç`omax_arrow_widthŸ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`l            Ÿ±Çbs1a'Ÿ±Çbs1ctipŸ±Çbs1a'Ÿ±Ç`a:Ÿ±Ç`a Ÿ±Ç`a[Ÿ±Ç`flengthŸ±Ç`a Ÿ±Çaoa-Ÿ±Ç`a Ÿ±Çbmia3Ÿ±Ç`a Ÿ±Çaoa*Ÿ±Ç`a Ÿ±Ç`omax_arrow_widthŸ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia3Ÿ±Ç`a Ÿ±Çaoa*Ÿ±Ç`a Ÿ±Ç`omax_arrow_widthŸ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±Ç`a}Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±Çbc1x6# for diagonal arrows, put the label at the arrow baseŸ±Ç`a
Ÿ±Ç`h        Ÿ±Çbc1x5# for vertical or horizontal arrows, center the labelŸ±Ç`a
Ÿ±Ç`h        Ÿ±Ç`ewhereŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1dbaseŸ±Çbs1a'Ÿ±Ç`a Ÿ±ÇakbifŸ±Ç`a Ÿ±Ç`a(Ÿ±Ç`ccp0Ÿ±Ç`a Ÿ±Çaob!=Ÿ±Ç`a Ÿ±Ç`ccp1Ÿ±Ç`a)Ÿ±Çaoa.Ÿ±Ç`callŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a Ÿ±ÇakdelseŸ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1fcenterŸ±Çbs1a'Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±Çbc1x/# rotate based on direction of arrow (cos, sin)Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±Ç`aMŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`a[Ÿ±Ç`a[Ÿ±Ç`ccosŸ±Ç`a,Ÿ±Ç`a Ÿ±Çaoa-Ÿ±Ç`csinŸ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`a[Ÿ±Ç`csinŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ccosŸ±Ç`a]Ÿ±Ç`a]Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±Ç`axŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ayŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`cdotŸ±Ç`a(Ÿ±Ç`aMŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`norig_positionsŸ±Ç`a[Ÿ±Ç`ewhereŸ±Ç`a]Ÿ±Ç`a)Ÿ±Ç`a Ÿ±Çaoa+Ÿ±Ç`a Ÿ±Ç`a[Ÿ±Ç`ex_posŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ey_posŸ±Ç`a]Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±Ç`elabelŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±ÇbsaarŸ±Çbs1a'Ÿ±Çbs1c$r_Ÿ±Çbs1a{Ÿ±Çbs1a_Ÿ±Çbs1a{Ÿ±Çbs1a\Ÿ±Çbs1fmathrmŸ±Çbs1a{Ÿ±Çbsib%sŸ±Çbs1d}}}$Ÿ±Çbs1a'Ÿ±Ç`a Ÿ±Çaoa%Ÿ±Ç`a Ÿ±Ç`a(Ÿ±Ç`dpairŸ±Ç`a,Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`dtextŸ±Ç`a(Ÿ±Ç`axŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ayŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`elabelŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dsizeŸ±Çaoa=Ÿ±Ç`olabel_text_sizeŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`bhaŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1fcenterŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`bvaŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1fcenterŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`p                Ÿ±Ç`ecolorŸ±Çaoa=Ÿ±Ç`jlabelcolorŸ±Ç`a Ÿ±ÇbowborŸ±Ç`a Ÿ±Ç`bfcŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±ÇakbifŸ±Ç`a Ÿ±Çbvmh__name__Ÿ±Ç`a Ÿ±Çaob==Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1h__main__Ÿ±Çbs1a'Ÿ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`ddataŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`a{Ÿ±Ç`b  Ÿ±Çbc1k# test dataŸ±Ç`a
Ÿ±Ç`h        Ÿ±Çbs1a'Ÿ±Çbs1aAŸ±Çbs1a'Ÿ±Ç`a:Ÿ±Ç`a Ÿ±Çbmfc0.4Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1aTŸ±Çbs1a'Ÿ±Ç`a:Ÿ±Ç`a Ÿ±Çbmfc0.3Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1aGŸ±Çbs1a'Ÿ±Ç`a:Ÿ±Ç`a Ÿ±Çbmfc0.6Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1aCŸ±Çbs1a'Ÿ±Ç`a:Ÿ±Ç`a Ÿ±Çbmfc0.2Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±Çbs1a'Ÿ±Çbs1bATŸ±Çbs1a'Ÿ±Ç`a:Ÿ±Ç`a Ÿ±Çbmfc0.4Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1bACŸ±Çbs1a'Ÿ±Ç`a:Ÿ±Ç`a Ÿ±Çbmfc0.3Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1bAGŸ±Çbs1a'Ÿ±Ç`a:Ÿ±Ç`a Ÿ±Çbmfc0.2Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±Çbs1a'Ÿ±Çbs1bTAŸ±Çbs1a'Ÿ±Ç`a:Ÿ±Ç`a Ÿ±Çbmfc0.2Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1bTCŸ±Çbs1a'Ÿ±Ç`a:Ÿ±Ç`a Ÿ±Çbmfc0.3Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1bTGŸ±Çbs1a'Ÿ±Ç`a:Ÿ±Ç`a Ÿ±Çbmfc0.4Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±Çbs1a'Ÿ±Çbs1bCTŸ±Çbs1a'Ÿ±Ç`a:Ÿ±Ç`a Ÿ±Çbmfc0.2Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1bCGŸ±Çbs1a'Ÿ±Ç`a:Ÿ±Ç`a Ÿ±Çbmfc0.3Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1bCAŸ±Çbs1a'Ÿ±Ç`a:Ÿ±Ç`a Ÿ±Çbmfc0.2Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±Çbs1a'Ÿ±Çbs1bGAŸ±Çbs1a'Ÿ±Ç`a:Ÿ±Ç`a Ÿ±Çbmfc0.1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1bGTŸ±Çbs1a'Ÿ±Ç`a:Ÿ±Ç`a Ÿ±Çbmfc0.4Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1bGCŸ±Çbs1a'Ÿ±Ç`a:Ÿ±Ç`a Ÿ±Çbmfc0.1Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`a}Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`dsizeŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Çbmia4Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`cfigŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`ffigureŸ±Ç`a(Ÿ±Ç`gfigsizeŸ±Çaoa=Ÿ±Ç`a(Ÿ±Çbmia3Ÿ±Ç`a Ÿ±Çaoa*Ÿ±Ç`a Ÿ±Ç`dsizeŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dsizeŸ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`rconstrained_layoutŸ±Çaoa=Ÿ±ÇbkcdTrueŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`caxsŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cfigŸ±Çaoa.Ÿ±Ç`nsubplot_mosaicŸ±Ç`a(Ÿ±Ç`a[Ÿ±Ç`a[Ÿ±Çbs2a"Ÿ±Çbs2flengthŸ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs2a"Ÿ±Çbs2ewidthŸ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs2a"Ÿ±Çbs2ealphaŸ±Çbs2a"Ÿ±Ç`a]Ÿ±Ç`a]Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±ÇakcforŸ±Ç`a Ÿ±Ç`gdisplayŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`baxŸ±Ç`a Ÿ±ÇbowbinŸ±Ç`a Ÿ±Ç`caxsŸ±Çaoa.Ÿ±Ç`eitemsŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±Ç`pmake_arrow_graphŸ±Ç`a(Ÿ±Ç`a
Ÿ±Ç`l            Ÿ±Ç`baxŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ddataŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`gdisplayŸ±Çaoa=Ÿ±Ç`gdisplayŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ilinewidthŸ±Çaoa=Ÿ±Çbmfe0.001Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`iedgecolorŸ±Çaoa=Ÿ±ÇbkcdNoneŸ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`l            Ÿ±Ç`nnormalize_dataŸ±Çaoa=Ÿ±ÇbkcdTrueŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dsizeŸ±Çaoa=Ÿ±Ç`dsizeŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`dshowŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
`dNoneˆ