ŸØÇÅŸ¥ÉôdŸ±ÇbsdxŸ"""
=======================
Left ventricle bullseye
=======================

This example demonstrates how to create the 17 segment model for the left
ventricle recommended by the American Heart Association (AHA).
"""Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±ÇbknfimportŸ±Ç`a Ÿ±ÇbnnŸ¢ÑenumpyŸ†Ñenumpyf1.22.3fmoduleenumpyfmoduleıŸ±Ç`a Ÿ±ÇakbasŸ±Ç`a Ÿ±ÇbnnbnpŸ±Ç`a
Ÿ±ÇbknfimportŸ±Ç`a Ÿ±ÇbnnŸ¢ÑjmatplotlibŸ†Ñjmatplotlibe3.5.1fmodulejmatplotlibfmoduleıŸ±Ç`a Ÿ±ÇakbasŸ±Ç`a Ÿ±ÇbnncmplŸ±Ç`a
Ÿ±ÇbknfimportŸ±Ç`a Ÿ±ÇbnnŸ¢ÑjmatplotlibŸ†Ñjmatplotlibe3.5.1fmodulejmatplotlibfmoduleıŸ±Çbnna.Ÿ±ÇbnnfpyplotŸ±Ç`a Ÿ±ÇakbasŸ±Ç`a Ÿ±ÇbnncpltŸ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±ÇakcdefŸ±Ç`a Ÿ±Çbnfmbullseye_plotŸ±Ç`a(Ÿ±Ç`baxŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ddataŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`hseg_boldŸ±Çaoa=Ÿ±ÇbkcdNoneŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dcmapŸ±Çaoa=Ÿ±ÇbkcdNoneŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dnormŸ±Çaoa=Ÿ±ÇbkcdNoneŸ±Ç`a)Ÿ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Çbsdy‡"""
    Bullseye representation for the left ventricle.

    Parameters
    ----------
    ax : axes
    data : list of int and float
        The intensity values for each of the 17 segments
    seg_bold : list of int, optional
        A list with the segments to highlight
    cmap : ColorMap or None, optional
        Optional argument to set the desired colormap
    norm : Normalize or None, optional
        Optional argument to normalize data into the [0.0, 1.0] range

    Notes
    -----
    This function creates the 17 segment model for the left ventricle according
    to the American Heart Association (AHA) [1]_

    References
    ----------
    .. [1] M. D. Cerqueira, N. J. Weissman, V. Dilsizian, A. K. Jacobs,
        S. Kaul, W. K. Laskey, D. J. Pennell, J. A. Rumberger, T. Ryan,
        and M. S. Verani, "Standardized myocardial segmentation and
        nomenclature for tomographic imaging of the heart",
        Circulation, vol. 105, no. 4, pp. 539-542, 2002.
    """Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±ÇakbifŸ±Ç`a Ÿ±Ç`hseg_boldŸ±Ç`a Ÿ±ÇbowbisŸ±Ç`a Ÿ±ÇbkcdNoneŸ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±Ç`hseg_boldŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`a[Ÿ±Ç`a]Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`ilinewidthŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Çbmia2Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`ddataŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`eravelŸ±Ç`a(Ÿ±Ç`ddataŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±ÇakbifŸ±Ç`a Ÿ±Ç`dcmapŸ±Ç`a Ÿ±ÇbowbisŸ±Ç`a Ÿ±ÇbkcdNoneŸ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±Ç`dcmapŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`bcmŸ±Çaoa.Ÿ±Ç`gviridisŸ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±ÇakbifŸ±Ç`a Ÿ±Ç`dnormŸ±Ç`a Ÿ±ÇbowbisŸ±Ç`a Ÿ±ÇbkcdNoneŸ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±Ç`dnormŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cmplŸ±Çaoa.Ÿ±Ç`fcolorsŸ±Çaoa.Ÿ±Ç`iNormalizeŸ±Ç`a(Ÿ±Ç`dvminŸ±Çaoa=Ÿ±Ç`ddataŸ±Çaoa.Ÿ±Ç`cminŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dvmaxŸ±Çaoa=Ÿ±Ç`ddataŸ±Çaoa.Ÿ±Ç`cmaxŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`ethetaŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`hlinspaceŸ±Ç`a(Ÿ±Çbmia0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia2Ÿ±Ç`a Ÿ±Çaoa*Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`bpiŸ±Ç`a,Ÿ±Ç`a Ÿ±Çbmic768Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`arŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`hlinspaceŸ±Ç`a(Ÿ±Çbmfc0.2Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia4Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Çbc1x%# Create the bound for the segment 17Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±ÇakcforŸ±Ç`a Ÿ±Ç`aiŸ±Ç`a Ÿ±ÇbowbinŸ±Ç`a Ÿ±ÇbnberangeŸ±Ç`a(Ÿ±Ç`arŸ±Çaoa.Ÿ±Ç`eshapeŸ±Ç`a[Ÿ±Çbmia0Ÿ±Ç`a]Ÿ±Ç`a)Ÿ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`dplotŸ±Ç`a(Ÿ±Ç`ethetaŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`frepeatŸ±Ç`a(Ÿ±Ç`arŸ±Ç`a[Ÿ±Ç`aiŸ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ethetaŸ±Çaoa.Ÿ±Ç`eshapeŸ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1b-kŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`blwŸ±Çaoa=Ÿ±Ç`ilinewidthŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Çbc1x)# Create the bounds for the segments 1-12Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±ÇakcforŸ±Ç`a Ÿ±Ç`aiŸ±Ç`a Ÿ±ÇbowbinŸ±Ç`a Ÿ±ÇbnberangeŸ±Ç`a(Ÿ±Çbmia6Ÿ±Ç`a)Ÿ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±Ç`gtheta_iŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`gdeg2radŸ±Ç`a(Ÿ±Ç`aiŸ±Ç`a Ÿ±Çaoa*Ÿ±Ç`a Ÿ±Çbmib60Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`dplotŸ±Ç`a(Ÿ±Ç`a[Ÿ±Ç`gtheta_iŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`gtheta_iŸ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`a[Ÿ±Ç`arŸ±Ç`a[Ÿ±Çbmia1Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia1Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1b-kŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`blwŸ±Çaoa=Ÿ±Ç`ilinewidthŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Çbc1x*# Create the bounds for the segments 13-16Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±ÇakcforŸ±Ç`a Ÿ±Ç`aiŸ±Ç`a Ÿ±ÇbowbinŸ±Ç`a Ÿ±ÇbnberangeŸ±Ç`a(Ÿ±Çbmia4Ÿ±Ç`a)Ÿ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±Ç`gtheta_iŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`gdeg2radŸ±Ç`a(Ÿ±Ç`aiŸ±Ç`a Ÿ±Çaoa*Ÿ±Ç`a Ÿ±Çbmib90Ÿ±Ç`a Ÿ±Çaoa-Ÿ±Ç`a Ÿ±Çbmib45Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`dplotŸ±Ç`a(Ÿ±Ç`a[Ÿ±Ç`gtheta_iŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`gtheta_iŸ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`a[Ÿ±Ç`arŸ±Ç`a[Ÿ±Çbmia0Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`arŸ±Ç`a[Ÿ±Çbmia1Ÿ±Ç`a]Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1b-kŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`blwŸ±Çaoa=Ÿ±Ç`ilinewidthŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Çbc1w# Fill the segments 1-6Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`br0Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`arŸ±Ç`a[Ÿ±Çbmia2Ÿ±Ç`a:Ÿ±Çbmia4Ÿ±Ç`a]Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`br0Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`frepeatŸ±Ç`a(Ÿ±Ç`br0Ÿ±Ç`a[Ÿ±Ç`a:Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`gnewaxisŸ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmic128Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`daxisŸ±Çaoa=Ÿ±Çbmia1Ÿ±Ç`a)Ÿ±Çaoa.Ÿ±Ç`aTŸ±Ç`a
Ÿ±Ç`d    Ÿ±ÇakcforŸ±Ç`a Ÿ±Ç`aiŸ±Ç`a Ÿ±ÇbowbinŸ±Ç`a Ÿ±ÇbnberangeŸ±Ç`a(Ÿ±Çbmia6Ÿ±Ç`a)Ÿ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±Çbc1x## First segment start at 60 degreesŸ±Ç`a
Ÿ±Ç`h        Ÿ±Ç`ftheta0Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`ethetaŸ±Ç`a[Ÿ±Ç`aiŸ±Ç`a Ÿ±Çaoa*Ÿ±Ç`a Ÿ±Çbmic128Ÿ±Ç`a:Ÿ±Ç`aiŸ±Ç`a Ÿ±Çaoa*Ÿ±Ç`a Ÿ±Çbmic128Ÿ±Ç`a Ÿ±Çaoa+Ÿ±Ç`a Ÿ±Çbmic128Ÿ±Ç`a]Ÿ±Ç`a Ÿ±Çaoa+Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`gdeg2radŸ±Ç`a(Ÿ±Çbmib60Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±Ç`ftheta0Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`frepeatŸ±Ç`a(Ÿ±Ç`ftheta0Ÿ±Ç`a[Ÿ±Ç`a:Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`gnewaxisŸ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia2Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`daxisŸ±Çaoa=Ÿ±Çbmia1Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±Ç`azŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`donesŸ±Ç`a(Ÿ±Ç`a(Ÿ±Çbmic128Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia2Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a Ÿ±Çaoa*Ÿ±Ç`a Ÿ±Ç`ddataŸ±Ç`a[Ÿ±Ç`aiŸ±Ç`a]Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`jpcolormeshŸ±Ç`a(Ÿ±Ç`ftheta0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`br0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`azŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dcmapŸ±Çaoa=Ÿ±Ç`dcmapŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dnormŸ±Çaoa=Ÿ±Ç`dnormŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`gshadingŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1dautoŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±ÇakbifŸ±Ç`a Ÿ±Ç`aiŸ±Ç`a Ÿ±Çaoa+Ÿ±Ç`a Ÿ±Çbmia1Ÿ±Ç`a Ÿ±ÇbowbinŸ±Ç`a Ÿ±Ç`hseg_boldŸ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`l            Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`dplotŸ±Ç`a(Ÿ±Ç`ftheta0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`br0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1b-kŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`blwŸ±Çaoa=Ÿ±Ç`ilinewidthŸ±Ç`a Ÿ±Çaoa+Ÿ±Ç`a Ÿ±Çbmia2Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`l            Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`dplotŸ±Ç`a(Ÿ±Ç`ftheta0Ÿ±Ç`a[Ÿ±Çbmia0Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`a[Ÿ±Ç`arŸ±Ç`a[Ÿ±Çbmia2Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`arŸ±Ç`a[Ÿ±Çbmia3Ÿ±Ç`a]Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1b-kŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`blwŸ±Çaoa=Ÿ±Ç`ilinewidthŸ±Ç`a Ÿ±Çaoa+Ÿ±Ç`a Ÿ±Çbmia1Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`l            Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`dplotŸ±Ç`a(Ÿ±Ç`ftheta0Ÿ±Ç`a[Ÿ±Çaoa-Ÿ±Çbmia1Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`a[Ÿ±Ç`arŸ±Ç`a[Ÿ±Çbmia2Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`arŸ±Ç`a[Ÿ±Çbmia3Ÿ±Ç`a]Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1b-kŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`blwŸ±Çaoa=Ÿ±Ç`ilinewidthŸ±Ç`a Ÿ±Çaoa+Ÿ±Ç`a Ÿ±Çbmia1Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Çbc1x# Fill the segments 7-12Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`br0Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`arŸ±Ç`a[Ÿ±Çbmia1Ÿ±Ç`a:Ÿ±Çbmia3Ÿ±Ç`a]Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`br0Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`frepeatŸ±Ç`a(Ÿ±Ç`br0Ÿ±Ç`a[Ÿ±Ç`a:Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`gnewaxisŸ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmic128Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`daxisŸ±Çaoa=Ÿ±Çbmia1Ÿ±Ç`a)Ÿ±Çaoa.Ÿ±Ç`aTŸ±Ç`a
Ÿ±Ç`d    Ÿ±ÇakcforŸ±Ç`a Ÿ±Ç`aiŸ±Ç`a Ÿ±ÇbowbinŸ±Ç`a Ÿ±ÇbnberangeŸ±Ç`a(Ÿ±Çbmia6Ÿ±Ç`a)Ÿ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±Çbc1x## First segment start at 60 degreesŸ±Ç`a
Ÿ±Ç`h        Ÿ±Ç`ftheta0Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`ethetaŸ±Ç`a[Ÿ±Ç`aiŸ±Ç`a Ÿ±Çaoa*Ÿ±Ç`a Ÿ±Çbmic128Ÿ±Ç`a:Ÿ±Ç`aiŸ±Ç`a Ÿ±Çaoa*Ÿ±Ç`a Ÿ±Çbmic128Ÿ±Ç`a Ÿ±Çaoa+Ÿ±Ç`a Ÿ±Çbmic128Ÿ±Ç`a]Ÿ±Ç`a Ÿ±Çaoa+Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`gdeg2radŸ±Ç`a(Ÿ±Çbmib60Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±Ç`ftheta0Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`frepeatŸ±Ç`a(Ÿ±Ç`ftheta0Ÿ±Ç`a[Ÿ±Ç`a:Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`gnewaxisŸ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia2Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`daxisŸ±Çaoa=Ÿ±Çbmia1Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±Ç`azŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`donesŸ±Ç`a(Ÿ±Ç`a(Ÿ±Çbmic128Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia2Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a Ÿ±Çaoa*Ÿ±Ç`a Ÿ±Ç`ddataŸ±Ç`a[Ÿ±Ç`aiŸ±Ç`a Ÿ±Çaoa+Ÿ±Ç`a Ÿ±Çbmia6Ÿ±Ç`a]Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`jpcolormeshŸ±Ç`a(Ÿ±Ç`ftheta0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`br0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`azŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dcmapŸ±Çaoa=Ÿ±Ç`dcmapŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dnormŸ±Çaoa=Ÿ±Ç`dnormŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`gshadingŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1dautoŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±ÇakbifŸ±Ç`a Ÿ±Ç`aiŸ±Ç`a Ÿ±Çaoa+Ÿ±Ç`a Ÿ±Çbmia7Ÿ±Ç`a Ÿ±ÇbowbinŸ±Ç`a Ÿ±Ç`hseg_boldŸ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`l            Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`dplotŸ±Ç`a(Ÿ±Ç`ftheta0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`br0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1b-kŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`blwŸ±Çaoa=Ÿ±Ç`ilinewidthŸ±Ç`a Ÿ±Çaoa+Ÿ±Ç`a Ÿ±Çbmia2Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`l            Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`dplotŸ±Ç`a(Ÿ±Ç`ftheta0Ÿ±Ç`a[Ÿ±Çbmia0Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`a[Ÿ±Ç`arŸ±Ç`a[Ÿ±Çbmia1Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`arŸ±Ç`a[Ÿ±Çbmia2Ÿ±Ç`a]Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1b-kŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`blwŸ±Çaoa=Ÿ±Ç`ilinewidthŸ±Ç`a Ÿ±Çaoa+Ÿ±Ç`a Ÿ±Çbmia1Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`l            Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`dplotŸ±Ç`a(Ÿ±Ç`ftheta0Ÿ±Ç`a[Ÿ±Çaoa-Ÿ±Çbmia1Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`a[Ÿ±Ç`arŸ±Ç`a[Ÿ±Çbmia1Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`arŸ±Ç`a[Ÿ±Çbmia2Ÿ±Ç`a]Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1b-kŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`blwŸ±Çaoa=Ÿ±Ç`ilinewidthŸ±Ç`a Ÿ±Çaoa+Ÿ±Ç`a Ÿ±Çbmia1Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Çbc1x# Fill the segments 13-16Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`br0Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`arŸ±Ç`a[Ÿ±Çbmia0Ÿ±Ç`a:Ÿ±Çbmia2Ÿ±Ç`a]Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`br0Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`frepeatŸ±Ç`a(Ÿ±Ç`br0Ÿ±Ç`a[Ÿ±Ç`a:Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`gnewaxisŸ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmic192Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`daxisŸ±Çaoa=Ÿ±Çbmia1Ÿ±Ç`a)Ÿ±Çaoa.Ÿ±Ç`aTŸ±Ç`a
Ÿ±Ç`d    Ÿ±ÇakcforŸ±Ç`a Ÿ±Ç`aiŸ±Ç`a Ÿ±ÇbowbinŸ±Ç`a Ÿ±ÇbnberangeŸ±Ç`a(Ÿ±Çbmia4Ÿ±Ç`a)Ÿ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±Çbc1x## First segment start at 45 degreesŸ±Ç`a
Ÿ±Ç`h        Ÿ±Ç`ftheta0Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`ethetaŸ±Ç`a[Ÿ±Ç`aiŸ±Ç`a Ÿ±Çaoa*Ÿ±Ç`a Ÿ±Çbmic192Ÿ±Ç`a:Ÿ±Ç`aiŸ±Ç`a Ÿ±Çaoa*Ÿ±Ç`a Ÿ±Çbmic192Ÿ±Ç`a Ÿ±Çaoa+Ÿ±Ç`a Ÿ±Çbmic192Ÿ±Ç`a]Ÿ±Ç`a Ÿ±Çaoa+Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`gdeg2radŸ±Ç`a(Ÿ±Çbmib45Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±Ç`ftheta0Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`frepeatŸ±Ç`a(Ÿ±Ç`ftheta0Ÿ±Ç`a[Ÿ±Ç`a:Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`gnewaxisŸ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia2Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`daxisŸ±Çaoa=Ÿ±Çbmia1Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±Ç`azŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`donesŸ±Ç`a(Ÿ±Ç`a(Ÿ±Çbmic192Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia2Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a Ÿ±Çaoa*Ÿ±Ç`a Ÿ±Ç`ddataŸ±Ç`a[Ÿ±Ç`aiŸ±Ç`a Ÿ±Çaoa+Ÿ±Ç`a Ÿ±Çbmib12Ÿ±Ç`a]Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`jpcolormeshŸ±Ç`a(Ÿ±Ç`ftheta0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`br0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`azŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dcmapŸ±Çaoa=Ÿ±Ç`dcmapŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dnormŸ±Çaoa=Ÿ±Ç`dnormŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`gshadingŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1dautoŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±ÇakbifŸ±Ç`a Ÿ±Ç`aiŸ±Ç`a Ÿ±Çaoa+Ÿ±Ç`a Ÿ±Çbmib13Ÿ±Ç`a Ÿ±ÇbowbinŸ±Ç`a Ÿ±Ç`hseg_boldŸ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`l            Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`dplotŸ±Ç`a(Ÿ±Ç`ftheta0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`br0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1b-kŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`blwŸ±Çaoa=Ÿ±Ç`ilinewidthŸ±Ç`a Ÿ±Çaoa+Ÿ±Ç`a Ÿ±Çbmia2Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`l            Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`dplotŸ±Ç`a(Ÿ±Ç`ftheta0Ÿ±Ç`a[Ÿ±Çbmia0Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`a[Ÿ±Ç`arŸ±Ç`a[Ÿ±Çbmia0Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`arŸ±Ç`a[Ÿ±Çbmia1Ÿ±Ç`a]Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1b-kŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`blwŸ±Çaoa=Ÿ±Ç`ilinewidthŸ±Ç`a Ÿ±Çaoa+Ÿ±Ç`a Ÿ±Çbmia1Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`l            Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`dplotŸ±Ç`a(Ÿ±Ç`ftheta0Ÿ±Ç`a[Ÿ±Çaoa-Ÿ±Çbmia1Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`a[Ÿ±Ç`arŸ±Ç`a[Ÿ±Çbmia0Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`arŸ±Ç`a[Ÿ±Çbmia1Ÿ±Ç`a]Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1b-kŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`blwŸ±Çaoa=Ÿ±Ç`ilinewidthŸ±Ç`a Ÿ±Çaoa+Ÿ±Ç`a Ÿ±Çbmia1Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Çbc1v# Fill the segments 17Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±ÇakbifŸ±Ç`a Ÿ±Ç`ddataŸ±Çaoa.Ÿ±Ç`dsizeŸ±Ç`a Ÿ±Çaob==Ÿ±Ç`a Ÿ±Çbmib17Ÿ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±Ç`br0Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`earrayŸ±Ç`a(Ÿ±Ç`a[Ÿ±Çbmia0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`arŸ±Ç`a[Ÿ±Çbmia0Ÿ±Ç`a]Ÿ±Ç`a]Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±Ç`br0Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`frepeatŸ±Ç`a(Ÿ±Ç`br0Ÿ±Ç`a[Ÿ±Ç`a:Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`gnewaxisŸ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ethetaŸ±Çaoa.Ÿ±Ç`dsizeŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`daxisŸ±Çaoa=Ÿ±Çbmia1Ÿ±Ç`a)Ÿ±Çaoa.Ÿ±Ç`aTŸ±Ç`a
Ÿ±Ç`h        Ÿ±Ç`ftheta0Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`frepeatŸ±Ç`a(Ÿ±Ç`ethetaŸ±Ç`a[Ÿ±Ç`a:Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`gnewaxisŸ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia2Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`daxisŸ±Çaoa=Ÿ±Çbmia1Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±Ç`azŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`donesŸ±Ç`a(Ÿ±Ç`a(Ÿ±Ç`ethetaŸ±Çaoa.Ÿ±Ç`dsizeŸ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia2Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a Ÿ±Çaoa*Ÿ±Ç`a Ÿ±Ç`ddataŸ±Ç`a[Ÿ±Çbmib16Ÿ±Ç`a]Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`jpcolormeshŸ±Ç`a(Ÿ±Ç`ftheta0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`br0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`azŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dcmapŸ±Çaoa=Ÿ±Ç`dcmapŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dnormŸ±Çaoa=Ÿ±Ç`dnormŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`gshadingŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1dautoŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±ÇakbifŸ±Ç`a Ÿ±Çbmib17Ÿ±Ç`a Ÿ±ÇbowbinŸ±Ç`a Ÿ±Ç`hseg_boldŸ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`l            Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`dplotŸ±Ç`a(Ÿ±Ç`ftheta0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`br0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1b-kŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`blwŸ±Çaoa=Ÿ±Ç`ilinewidthŸ±Ç`a Ÿ±Çaoa+Ÿ±Ç`a Ÿ±Çbmia2Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`hset_ylimŸ±Ç`a(Ÿ±Ç`a[Ÿ±Çbmia0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia1Ÿ±Ç`a]Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`oset_yticklabelsŸ±Ç`a(Ÿ±Ç`a[Ÿ±Ç`a]Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`oset_xticklabelsŸ±Ç`a(Ÿ±Ç`a[Ÿ±Ç`a]Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1v# Create the fake dataŸ±Ç`a
Ÿ±Ç`ddataŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`farangeŸ±Ç`a(Ÿ±Çbmib17Ÿ±Ç`a)Ÿ±Ç`a Ÿ±Çaoa+Ÿ±Ç`a Ÿ±Çbmia1Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1x4# Make a figure and axes with dimensions as desired.Ÿ±Ç`a
Ÿ±Ç`cfigŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`baxŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`hsubplotsŸ±Ç`a(Ÿ±Ç`gfigsizeŸ±Çaoa=Ÿ±Ç`a(Ÿ±Çbmib12Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia8Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`enrowsŸ±Çaoa=Ÿ±Çbmia1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`encolsŸ±Çaoa=Ÿ±Çbmia3Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`w                       Ÿ±Ç`jsubplot_kwŸ±Çaoa=Ÿ±ÇbnbddictŸ±Ç`a(Ÿ±Ç`jprojectionŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1epolarŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cfigŸ±Çaoa.Ÿ±Ç`fcanvasŸ±Çaoa.Ÿ±Ç`gmanagerŸ±Çaoa.Ÿ±Ç`pset_window_titleŸ±Ç`a(Ÿ±Çbs1a'Ÿ±Çbs1xLeft Ventricle Bulls Eyes (AHA)Ÿ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1x## Create the axis for the colorbarsŸ±Ç`a
Ÿ±Ç`caxlŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cfigŸ±Çaoa.Ÿ±Ç`hadd_axesŸ±Ç`a(Ÿ±Ç`a[Ÿ±Çbmfd0.14Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd0.15Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfc0.2Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd0.05Ÿ±Ç`a]Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`daxl2Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cfigŸ±Çaoa.Ÿ±Ç`hadd_axesŸ±Ç`a(Ÿ±Ç`a[Ÿ±Çbmfd0.41Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd0.15Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfc0.2Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd0.05Ÿ±Ç`a]Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`daxl3Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cfigŸ±Çaoa.Ÿ±Ç`hadd_axesŸ±Ç`a(Ÿ±Ç`a[Ÿ±Çbmfd0.69Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd0.15Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfc0.2Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd0.05Ÿ±Ç`a]Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1x?# Set the colormap and norm to correspond to the data for whichŸ±Ç`a
Ÿ±Çbc1x# the colorbar will be used.Ÿ±Ç`a
Ÿ±Ç`dcmapŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cmplŸ±Çaoa.Ÿ±Ç`bcmŸ±Çaoa.Ÿ±Ç`gviridisŸ±Ç`a
Ÿ±Ç`dnormŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cmplŸ±Çaoa.Ÿ±Ç`fcolorsŸ±Çaoa.Ÿ±Ç`iNormalizeŸ±Ç`a(Ÿ±Ç`dvminŸ±Çaoa=Ÿ±Çbmia1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dvmaxŸ±Çaoa=Ÿ±Çbmib17Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Çbc1xI# Create an empty ScalarMappable to set the colorbar's colormap and norm.Ÿ±Ç`a
Ÿ±Çbc1xH# The following gives a basic continuous colorbar with ticks and labels.Ÿ±Ç`a
Ÿ±Ç`cfigŸ±Çaoa.Ÿ±Ç`hcolorbarŸ±Ç`a(Ÿ±Ç`cmplŸ±Çaoa.Ÿ±Ç`bcmŸ±Çaoa.Ÿ±Ç`nScalarMappableŸ±Ç`a(Ÿ±Ç`dcmapŸ±Çaoa=Ÿ±Ç`dcmapŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dnormŸ±Çaoa=Ÿ±Ç`dnormŸ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`m             Ÿ±Ç`ccaxŸ±Çaoa=Ÿ±Ç`caxlŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`korientationŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1jhorizontalŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`elabelŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1jSome UnitsŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1x$# And again for the second colorbar.Ÿ±Ç`a
Ÿ±Ç`ecmap2Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cmplŸ±Çaoa.Ÿ±Ç`bcmŸ±Çaoa.Ÿ±Ç`dcoolŸ±Ç`a
Ÿ±Ç`enorm2Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cmplŸ±Çaoa.Ÿ±Ç`fcolorsŸ±Çaoa.Ÿ±Ç`iNormalizeŸ±Ç`a(Ÿ±Ç`dvminŸ±Çaoa=Ÿ±Çbmia1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dvmaxŸ±Çaoa=Ÿ±Çbmib17Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cfigŸ±Çaoa.Ÿ±Ç`hcolorbarŸ±Ç`a(Ÿ±Ç`cmplŸ±Çaoa.Ÿ±Ç`bcmŸ±Çaoa.Ÿ±Ç`nScalarMappableŸ±Ç`a(Ÿ±Ç`dcmapŸ±Çaoa=Ÿ±Ç`ecmap2Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dnormŸ±Çaoa=Ÿ±Ç`enorm2Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`m             Ÿ±Ç`ccaxŸ±Çaoa=Ÿ±Ç`daxl2Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`korientationŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1jhorizontalŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`elabelŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1pSome other unitsŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1x?# The second example illustrates the use of a ListedColormap, aŸ±Ç`a
Ÿ±Çbc1x@# BoundaryNorm, and extended ends to show the "over" and "under"Ÿ±Ç`a
Ÿ±Çbc1o# value colors.Ÿ±Ç`a
Ÿ±Ç`ecmap3Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`a(Ÿ±Ç`cmplŸ±Çaoa.Ÿ±Ç`fcolorsŸ±Çaoa.Ÿ±Ç`nListedColormapŸ±Ç`a(Ÿ±Ç`a[Ÿ±Çbs1a'Ÿ±Çbs1arŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1agŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1abŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1acŸ±Çbs1a'Ÿ±Ç`a]Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`i         Ÿ±Çaoa.Ÿ±Ç`mwith_extremesŸ±Ç`a(Ÿ±Ç`doverŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1d0.35Ÿ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`eunderŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1d0.75Ÿ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Çbc1xE# If a ListedColormap is used, the length of the bounds array must beŸ±Ç`a
Ÿ±Çbc1xD# one greater than the length of the color list.  The bounds must beŸ±Ç`a
Ÿ±Çbc1x# monotonically increasing.Ÿ±Ç`a
Ÿ±Ç`fboundsŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`a[Ÿ±Çbmia2Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia3Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia7Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia9Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmib15Ÿ±Ç`a]Ÿ±Ç`a
Ÿ±Ç`enorm3Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cmplŸ±Çaoa.Ÿ±Ç`fcolorsŸ±Çaoa.Ÿ±Ç`lBoundaryNormŸ±Ç`a(Ÿ±Ç`fboundsŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ecmap3Ÿ±Çaoa.Ÿ±Ç`aNŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cfigŸ±Çaoa.Ÿ±Ç`hcolorbarŸ±Ç`a(Ÿ±Ç`cmplŸ±Çaoa.Ÿ±Ç`bcmŸ±Çaoa.Ÿ±Ç`nScalarMappableŸ±Ç`a(Ÿ±Ç`dcmapŸ±Çaoa=Ÿ±Ç`ecmap3Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dnormŸ±Çaoa=Ÿ±Ç`enorm3Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`m             Ÿ±Ç`ccaxŸ±Çaoa=Ÿ±Ç`daxl3Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`m             Ÿ±Çbc1x9# to use 'extend', you must specify two extra boundaries:Ÿ±Ç`a
Ÿ±Ç`m             Ÿ±Ç`jboundariesŸ±Çaoa=Ÿ±Ç`a[Ÿ±Çbmia0Ÿ±Ç`a]Ÿ±Ç`a Ÿ±Çaoa+Ÿ±Ç`a Ÿ±Ç`fboundsŸ±Ç`a Ÿ±Çaoa+Ÿ±Ç`a Ÿ±Ç`a[Ÿ±Çbmib18Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`m             Ÿ±Ç`fextendŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1dbothŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`m             Ÿ±Ç`eticksŸ±Çaoa=Ÿ±Ç`fboundsŸ±Ç`a,Ÿ±Ç`b  Ÿ±Çbc1j# optionalŸ±Ç`a
Ÿ±Ç`m             Ÿ±Ç`gspacingŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1lproportionalŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`m             Ÿ±Ç`korientationŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1jhorizontalŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`m             Ÿ±Ç`elabelŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1x$Discrete intervals, some other unitsŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1x# Create the 17 segment modelŸ±Ç`a
Ÿ±Ç`mbullseye_plotŸ±Ç`a(Ÿ±Ç`baxŸ±Ç`a[Ÿ±Çbmia0Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ddataŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dcmapŸ±Çaoa=Ÿ±Ç`dcmapŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dnormŸ±Çaoa=Ÿ±Ç`dnormŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`baxŸ±Ç`a[Ÿ±Çbmia0Ÿ±Ç`a]Ÿ±Çaoa.Ÿ±Ç`iset_titleŸ±Ç`a(Ÿ±Çbs1a'Ÿ±Çbs1oBulls Eye (AHA)Ÿ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`mbullseye_plotŸ±Ç`a(Ÿ±Ç`baxŸ±Ç`a[Ÿ±Çbmia1Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ddataŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dcmapŸ±Çaoa=Ÿ±Ç`ecmap2Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dnormŸ±Çaoa=Ÿ±Ç`enorm2Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`baxŸ±Ç`a[Ÿ±Çbmia1Ÿ±Ç`a]Ÿ±Çaoa.Ÿ±Ç`iset_titleŸ±Ç`a(Ÿ±Çbs1a'Ÿ±Çbs1oBulls Eye (AHA)Ÿ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`mbullseye_plotŸ±Ç`a(Ÿ±Ç`baxŸ±Ç`a[Ÿ±Çbmia2Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ddataŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`hseg_boldŸ±Çaoa=Ÿ±Ç`a[Ÿ±Çbmia3Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia5Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia6Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmib11Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmib12Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmib16Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`n              Ÿ±Ç`dcmapŸ±Çaoa=Ÿ±Ç`ecmap3Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dnormŸ±Çaoa=Ÿ±Ç`enorm3Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`baxŸ±Ç`a[Ÿ±Çbmia2Ÿ±Ç`a]Ÿ±Çaoa.Ÿ±Ç`iset_titleŸ±Ç`a(Ÿ±Çbs1a'Ÿ±Çbs1x&Segments [3, 5, 6, 11, 12, 16] in boldŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`dshowŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
`dNoneˆ