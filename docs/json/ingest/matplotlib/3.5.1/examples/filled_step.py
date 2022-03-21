ŸØÇÅŸ¥ÉôvŸ±ÇbsdxÉ"""
=========================
Hatch-filled histograms
=========================

Hatching capabilities for plotting histograms.
"""Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±ÇbknfimportŸ±Ç`a Ÿ±ÇbnniitertoolsŸ±Ç`a
Ÿ±ÇbkndfromŸ±Ç`a Ÿ±ÇbnnifunctoolsŸ±Ç`a Ÿ±ÇbknfimportŸ±Ç`a Ÿ±Ç`gpartialŸ±Ç`a
Ÿ±Ç`a
Ÿ±ÇbknfimportŸ±Ç`a Ÿ±ÇbnnŸ¢ÑenumpyŸ†Ñenumpyf1.22.3fmoduleenumpyfmoduleıŸ±Ç`a Ÿ±ÇakbasŸ±Ç`a Ÿ±ÇbnnbnpŸ±Ç`a
Ÿ±ÇbknfimportŸ±Ç`a Ÿ±ÇbnnŸ¢ÑjmatplotlibŸ†Ñjmatplotlibe3.5.1fmodulejmatplotlibfmoduleıŸ±Çbnna.Ÿ±ÇbnnfpyplotŸ±Ç`a Ÿ±ÇakbasŸ±Ç`a Ÿ±ÇbnncpltŸ±Ç`a
Ÿ±ÇbknfimportŸ±Ç`a Ÿ±ÇbnnŸ¢ÑjmatplotlibŸ†Ñjmatplotlibe3.5.1fmodulejmatplotlibfmoduleıŸ±Çbnna.Ÿ±ÇbnnftickerŸ±Ç`a Ÿ±ÇakbasŸ±Ç`a Ÿ±ÇbnngmtickerŸ±Ç`a
Ÿ±ÇbkndfromŸ±Ç`a Ÿ±ÇbnnfcyclerŸ±Ç`a Ÿ±ÇbknfimportŸ±Ç`a Ÿ±Ç`fcyclerŸ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±ÇakcdefŸ±Ç`a Ÿ±Çbnfkfilled_histŸ±Ç`a(Ÿ±Ç`baxŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`eedgesŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`fvaluesŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`gbottomsŸ±Çaoa=Ÿ±ÇbkcdNoneŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`korientationŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1avŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`p                Ÿ±Çaoa*Ÿ±Çaoa*Ÿ±Ç`fkwargsŸ±Ç`a)Ÿ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±ÇbsdyË"""
    Draw a histogram as a stepped patch.

    Parameters
    ----------
    ax : Axes
        The axes to plot to

    edges : array
        A length n+1 array giving the left edges of each bin and the
        right edge of the last bin.

    values : array
        A length n array of bin counts or values

    bottoms : float or array, optional
        A length n array of the bottom of the bars.  If None, zero is used.

    orientation : {'v', 'h'}
       Orientation of the histogram.  'v' (default) has
       the bars increasing in the positive y-direction.

    **kwargs
        Extra keyword arguments are passed through to `.fill_between`.

    Returns
    -------
    ret : PolyCollection
        Artist added to the Axes
    """Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±ÇbnbeprintŸ±Ç`a(Ÿ±Ç`korientationŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±ÇakbifŸ±Ç`a Ÿ±Ç`korientationŸ±Ç`a Ÿ±ÇbowcnotŸ±Ç`a Ÿ±ÇbowbinŸ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1bhvŸ±Çbs1a'Ÿ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±ÇakeraiseŸ±Ç`a Ÿ±ÇbnejValueErrorŸ±Ç`a(Ÿ±Çbs2a"Ÿ±Çbs2worientation must be in Ÿ±Çbs2b{{Ÿ±Çbs2a'Ÿ±Çbs2ahŸ±Çbs2a'Ÿ±Çbs2b, Ÿ±Çbs2a'Ÿ±Çbs2avŸ±Çbs2a'Ÿ±Çbs2c}} Ÿ±Çbs2a"Ÿ±Ç`a
Ÿ±Ç`x                         Ÿ±Çbs2a"Ÿ±Çbs2dnot Ÿ±Çbsic{o}Ÿ±Çbs2a"Ÿ±Çaoa.Ÿ±Ç`fformatŸ±Ç`a(Ÿ±Ç`aoŸ±Çaoa=Ÿ±Ç`korientationŸ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`fkwargsŸ±Çaoa.Ÿ±Ç`jsetdefaultŸ±Ç`a(Ÿ±Çbs1a'Ÿ±Çbs1dstepŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1dpostŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`fkwargsŸ±Çaoa.Ÿ±Ç`jsetdefaultŸ±Ç`a(Ÿ±Çbs1a'Ÿ±Çbs1ealphaŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfc0.7Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`eedgesŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`gasarrayŸ±Ç`a(Ÿ±Ç`eedgesŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`fvaluesŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`gasarrayŸ±Ç`a(Ÿ±Ç`fvaluesŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±ÇakbifŸ±Ç`a Ÿ±ÇbnbclenŸ±Ç`a(Ÿ±Ç`eedgesŸ±Ç`a)Ÿ±Ç`a Ÿ±Çaoa-Ÿ±Ç`a Ÿ±Çbmia1Ÿ±Ç`a Ÿ±Çaob!=Ÿ±Ç`a Ÿ±ÇbnbclenŸ±Ç`a(Ÿ±Ç`fvaluesŸ±Ç`a)Ÿ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±ÇakeraiseŸ±Ç`a Ÿ±ÇbnejValueErrorŸ±Ç`a(Ÿ±Çbs1a'Ÿ±Çbs1x/Must provide one more bin edge than value not: Ÿ±Çbs1a'Ÿ±Ç`a
Ÿ±Ç`x                         Ÿ±Çbs1a'Ÿ±Çbs1llen(edges): Ÿ±Çbsid{lb}Ÿ±Çbs1n len(values): Ÿ±Çbsid{lv}Ÿ±Çbs1a'Ÿ±Çaoa.Ÿ±Ç`fformatŸ±Ç`a(Ÿ±Ç`a
Ÿ±Ç`x                             Ÿ±Ç`blbŸ±Çaoa=Ÿ±ÇbnbclenŸ±Ç`a(Ÿ±Ç`eedgesŸ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`blvŸ±Çaoa=Ÿ±ÇbnbclenŸ±Ç`a(Ÿ±Ç`fvaluesŸ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±ÇakbifŸ±Ç`a Ÿ±Ç`gbottomsŸ±Ç`a Ÿ±ÇbowbisŸ±Ç`a Ÿ±ÇbkcdNoneŸ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±Ç`gbottomsŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Çbmia0Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`gbottomsŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`lbroadcast_toŸ±Ç`a(Ÿ±Ç`gbottomsŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`fvaluesŸ±Çaoa.Ÿ±Ç`eshapeŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`fvaluesŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`fappendŸ±Ç`a(Ÿ±Ç`fvaluesŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`fvaluesŸ±Ç`a[Ÿ±Çaoa-Ÿ±Çbmia1Ÿ±Ç`a]Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`gbottomsŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`fappendŸ±Ç`a(Ÿ±Ç`gbottomsŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`gbottomsŸ±Ç`a[Ÿ±Çaoa-Ÿ±Çbmia1Ÿ±Ç`a]Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±ÇakbifŸ±Ç`a Ÿ±Ç`korientationŸ±Ç`a Ÿ±Çaob==Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1ahŸ±Çbs1a'Ÿ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±ÇakfreturnŸ±Ç`a Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`mfill_betweenxŸ±Ç`a(Ÿ±Ç`eedgesŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`fvaluesŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`gbottomsŸ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`x                                 Ÿ±Çaoa*Ÿ±Çaoa*Ÿ±Ç`fkwargsŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±ÇakdelifŸ±Ç`a Ÿ±Ç`korientationŸ±Ç`a Ÿ±Çaob==Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1avŸ±Çbs1a'Ÿ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±ÇakfreturnŸ±Ç`a Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`lfill_betweenŸ±Ç`a(Ÿ±Ç`eedgesŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`fvaluesŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`gbottomsŸ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`x                               Ÿ±Çaoa*Ÿ±Çaoa*Ÿ±Ç`fkwargsŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±ÇakdelseŸ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±ÇakeraiseŸ±Ç`a Ÿ±ÇbnenAssertionErrorŸ±Ç`a(Ÿ±Çbs2a"Ÿ±Çbs2xyou should never be hereŸ±Çbs2a"Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±ÇakcdefŸ±Ç`a Ÿ±Çbnfjstack_histŸ±Ç`a(Ÿ±Ç`baxŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`lstacked_dataŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`isty_cycleŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`gbottomsŸ±Çaoa=Ÿ±ÇbkcdNoneŸ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`o               Ÿ±Ç`ihist_funcŸ±Çaoa=Ÿ±ÇbkcdNoneŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`flabelsŸ±Çaoa=Ÿ±ÇbkcdNoneŸ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`o               Ÿ±Ç`iplot_funcŸ±Çaoa=Ÿ±ÇbkcdNoneŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`kplot_kwargsŸ±Çaoa=Ÿ±ÇbkcdNoneŸ±Ç`a)Ÿ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Çbsdy¥"""
    Parameters
    ----------
    ax : axes.Axes
        The axes to add artists too

    stacked_data : array or Mapping
        A (M, N) shaped array.  The first dimension will be iterated over to
        compute histograms row-wise

    sty_cycle : Cycler or operable of dict
        Style to apply to each set

    bottoms : array, default: 0
        The initial positions of the bottoms.

    hist_func : callable, optional
        Must have signature `bin_vals, bin_edges = f(data)`.
        `bin_edges` expected to be one longer than `bin_vals`

    labels : list of str, optional
        The label for each set.

        If not given and stacked data is an array defaults to 'default set {n}'

        If *stacked_data* is a mapping, and *labels* is None, default to the
        keys.

        If *stacked_data* is a mapping and *labels* is given then only the
        columns listed will be plotted.

    plot_func : callable, optional
        Function to call to draw the histogram must have signature:

          ret = plot_func(ax, edges, top, bottoms=bottoms,
                          label=label, **kwargs)

    plot_kwargs : dict, optional
        Any extra keyword arguments to pass through to the plotting function.
        This will be the same for all calls to the plotting function and will
        override the values in *sty_cycle*.

    Returns
    -------
    arts : dict
        Dictionary of artists keyed on their labels
    """Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Çbc1x$# deal with default binning functionŸ±Ç`a
Ÿ±Ç`d    Ÿ±ÇakbifŸ±Ç`a Ÿ±Ç`ihist_funcŸ±Ç`a Ÿ±ÇbowbisŸ±Ç`a Ÿ±ÇbkcdNoneŸ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±Ç`ihist_funcŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`ihistogramŸ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Çbc1x%# deal with default plotting functionŸ±Ç`a
Ÿ±Ç`d    Ÿ±ÇakbifŸ±Ç`a Ÿ±Ç`iplot_funcŸ±Ç`a Ÿ±ÇbowbisŸ±Ç`a Ÿ±ÇbkcdNoneŸ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±Ç`iplot_funcŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`kfilled_histŸ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Çbc1s# deal with defaultŸ±Ç`a
Ÿ±Ç`d    Ÿ±ÇakbifŸ±Ç`a Ÿ±Ç`kplot_kwargsŸ±Ç`a Ÿ±ÇbowbisŸ±Ç`a Ÿ±ÇbkcdNoneŸ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±Ç`kplot_kwargsŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`a{Ÿ±Ç`a}Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±ÇbnbeprintŸ±Ç`a(Ÿ±Ç`kplot_kwargsŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±ÇakctryŸ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±Ç`fl_keysŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`lstacked_dataŸ±Çaoa.Ÿ±Ç`dkeysŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±Ç`jlabel_dataŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±ÇbkcdTrueŸ±Ç`a
Ÿ±Ç`h        Ÿ±ÇakbifŸ±Ç`a Ÿ±Ç`flabelsŸ±Ç`a Ÿ±ÇbowbisŸ±Ç`a Ÿ±ÇbkcdNoneŸ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`l            Ÿ±Ç`flabelsŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`fl_keysŸ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±ÇakfexceptŸ±Ç`a Ÿ±ÇbnenAttributeErrorŸ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±Ç`jlabel_dataŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±ÇbkceFalseŸ±Ç`a
Ÿ±Ç`h        Ÿ±ÇakbifŸ±Ç`a Ÿ±Ç`flabelsŸ±Ç`a Ÿ±ÇbowbisŸ±Ç`a Ÿ±ÇbkcdNoneŸ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`l            Ÿ±Ç`flabelsŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`iitertoolsŸ±Çaoa.Ÿ±Ç`frepeatŸ±Ç`a(Ÿ±ÇbkcdNoneŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±ÇakbifŸ±Ç`a Ÿ±Ç`jlabel_dataŸ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±Ç`iloop_iterŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±ÇbnbienumerateŸ±Ç`a(Ÿ±Ç`a(Ÿ±Ç`lstacked_dataŸ±Ç`a[Ÿ±Ç`clabŸ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`clabŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`asŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`x                              Ÿ±ÇakcforŸ±Ç`a Ÿ±Ç`clabŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`asŸ±Ç`a Ÿ±ÇbowbinŸ±Ç`a Ÿ±ÇbnbczipŸ±Ç`a(Ÿ±Ç`flabelsŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`isty_cycleŸ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±ÇakdelseŸ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±Ç`iloop_iterŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±ÇbnbienumerateŸ±Ç`a(Ÿ±ÇbnbczipŸ±Ç`a(Ÿ±Ç`lstacked_dataŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`flabelsŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`isty_cycleŸ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`dartsŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`a{Ÿ±Ç`a}Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±ÇakcforŸ±Ç`a Ÿ±Ç`ajŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`a(Ÿ±Ç`ddataŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`elabelŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`cstyŸ±Ç`a)Ÿ±Ç`a Ÿ±ÇbowbinŸ±Ç`a Ÿ±Ç`iloop_iterŸ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±ÇakbifŸ±Ç`a Ÿ±Ç`elabelŸ±Ç`a Ÿ±ÇbowbisŸ±Ç`a Ÿ±ÇbkcdNoneŸ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`l            Ÿ±Ç`elabelŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1idflt set Ÿ±Çbsic{n}Ÿ±Çbs1a'Ÿ±Çaoa.Ÿ±Ç`fformatŸ±Ç`a(Ÿ±Ç`anŸ±Çaoa=Ÿ±Ç`ajŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±Ç`elabelŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cstyŸ±Çaoa.Ÿ±Ç`cpopŸ±Ç`a(Ÿ±Çbs1a'Ÿ±Çbs1elabelŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`elabelŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±Ç`dvalsŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`eedgesŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`ihist_funcŸ±Ç`a(Ÿ±Ç`ddataŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±ÇakbifŸ±Ç`a Ÿ±Ç`gbottomsŸ±Ç`a Ÿ±ÇbowbisŸ±Ç`a Ÿ±ÇbkcdNoneŸ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`l            Ÿ±Ç`gbottomsŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`jzeros_likeŸ±Ç`a(Ÿ±Ç`dvalsŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±Ç`ctopŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`gbottomsŸ±Ç`a Ÿ±Çaoa+Ÿ±Ç`a Ÿ±Ç`dvalsŸ±Ç`a
Ÿ±Ç`h        Ÿ±ÇbnbeprintŸ±Ç`a(Ÿ±Ç`cstyŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±Ç`cstyŸ±Çaoa.Ÿ±Ç`fupdateŸ±Ç`a(Ÿ±Ç`kplot_kwargsŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±ÇbnbeprintŸ±Ç`a(Ÿ±Ç`cstyŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±Ç`cretŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`iplot_funcŸ±Ç`a(Ÿ±Ç`baxŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`eedgesŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ctopŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`gbottomsŸ±Çaoa=Ÿ±Ç`gbottomsŸ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`x                        Ÿ±Ç`elabelŸ±Çaoa=Ÿ±Ç`elabelŸ±Ç`a,Ÿ±Ç`a Ÿ±Çaoa*Ÿ±Çaoa*Ÿ±Ç`cstyŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±Ç`gbottomsŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`ctopŸ±Ç`a
Ÿ±Ç`h        Ÿ±Ç`dartsŸ±Ç`a[Ÿ±Ç`elabelŸ±Ç`a]Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cretŸ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`flegendŸ±Ç`a(Ÿ±Ç`hfontsizeŸ±Çaoa=Ÿ±Çbmib10Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±ÇakfreturnŸ±Ç`a Ÿ±Ç`dartsŸ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1x)# set up histogram function to fixed binsŸ±Ç`a
Ÿ±Ç`eedgesŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`hlinspaceŸ±Ç`a(Ÿ±Çaoa-Ÿ±Çbmia3Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia3Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmib20Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`hendpointŸ±Çaoa=Ÿ±ÇbkcdTrueŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`ihist_funcŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`gpartialŸ±Ç`a(Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`ihistogramŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dbinsŸ±Çaoa=Ÿ±Ç`eedgesŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1u# set up style cyclesŸ±Ç`a
Ÿ±Ç`kcolor_cycleŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`fcyclerŸ±Ç`a(Ÿ±Ç`ifacecolorŸ±Çaoa=Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`hrcParamsŸ±Ç`a[Ÿ±Çbs1a'Ÿ±Çbs1oaxes.prop_cycleŸ±Çbs1a'Ÿ±Ç`a]Ÿ±Ç`a[Ÿ±Ç`a:Ÿ±Çbmia4Ÿ±Ç`a]Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`klabel_cycleŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`fcyclerŸ±Ç`a(Ÿ±Ç`elabelŸ±Çaoa=Ÿ±Ç`a[Ÿ±Çbs1a'Ÿ±Çbs1dset Ÿ±Çbsic{n}Ÿ±Çbs1a'Ÿ±Çaoa.Ÿ±Ç`fformatŸ±Ç`a(Ÿ±Ç`anŸ±Çaoa=Ÿ±Ç`anŸ±Ç`a)Ÿ±Ç`a Ÿ±ÇakcforŸ±Ç`a Ÿ±Ç`anŸ±Ç`a Ÿ±ÇbowbinŸ±Ç`a Ÿ±ÇbnberangeŸ±Ç`a(Ÿ±Çbmia4Ÿ±Ç`a)Ÿ±Ç`a]Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`khatch_cycleŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`fcyclerŸ±Ç`a(Ÿ±Ç`ehatchŸ±Çaoa=Ÿ±Ç`a[Ÿ±Çbs1a'Ÿ±Çbs1a/Ÿ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1a*Ÿ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1a+Ÿ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1a|Ÿ±Çbs1a'Ÿ±Ç`a]Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1x)# Fixing random state for reproducibilityŸ±Ç`a
Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`frandomŸ±Çaoa.Ÿ±Ç`dseedŸ±Ç`a(Ÿ±Çbmih19680801Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`jstack_dataŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`frandomŸ±Çaoa.Ÿ±Ç`erandnŸ±Ç`a(Ÿ±Çbmia4Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmie12250Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`idict_dataŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±ÇbnbddictŸ±Ç`a(Ÿ±ÇbnbczipŸ±Ç`a(Ÿ±Ç`a(Ÿ±Ç`acŸ±Ç`a[Ÿ±Çbs1a'Ÿ±Çbs1elabelŸ±Çbs1a'Ÿ±Ç`a]Ÿ±Ç`a Ÿ±ÇakcforŸ±Ç`a Ÿ±Ç`acŸ±Ç`a Ÿ±ÇbowbinŸ±Ç`a Ÿ±Ç`klabel_cycleŸ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`jstack_dataŸ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1xO###############################################################################Ÿ±Ç`a
Ÿ±Çbc1x# Work with plain arraysŸ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`cfigŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`a(Ÿ±Ç`cax1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`cax2Ÿ±Ç`a)Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`hsubplotsŸ±Ç`a(Ÿ±Çbmia1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia2Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`gfigsizeŸ±Çaoa=Ÿ±Ç`a(Ÿ±Çbmia9Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfc4.5Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ltight_layoutŸ±Çaoa=Ÿ±ÇbkcdTrueŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`dartsŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`jstack_histŸ±Ç`a(Ÿ±Ç`cax1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`jstack_dataŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`kcolor_cycleŸ±Ç`a Ÿ±Çaoa+Ÿ±Ç`a Ÿ±Ç`klabel_cycleŸ±Ç`a Ÿ±Çaoa+Ÿ±Ç`a Ÿ±Ç`khatch_cycleŸ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`r                  Ÿ±Ç`ihist_funcŸ±Çaoa=Ÿ±Ç`ihist_funcŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`dartsŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`jstack_histŸ±Ç`a(Ÿ±Ç`cax2Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`jstack_dataŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`kcolor_cycleŸ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`r                  Ÿ±Ç`ihist_funcŸ±Çaoa=Ÿ±Ç`ihist_funcŸ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`r                  Ÿ±Ç`kplot_kwargsŸ±Çaoa=Ÿ±ÇbnbddictŸ±Ç`a(Ÿ±Ç`iedgecolorŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1awŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`korientationŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1ahŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cax1Ÿ±Çaoa.Ÿ±Ç`jset_ylabelŸ±Ç`a(Ÿ±Çbs1a'Ÿ±Çbs1fcountsŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cax1Ÿ±Çaoa.Ÿ±Ç`jset_xlabelŸ±Ç`a(Ÿ±Çbs1a'Ÿ±Çbs1axŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cax2Ÿ±Çaoa.Ÿ±Ç`jset_xlabelŸ±Ç`a(Ÿ±Çbs1a'Ÿ±Çbs1fcountsŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cax2Ÿ±Çaoa.Ÿ±Ç`jset_ylabelŸ±Ç`a(Ÿ±Çbs1a'Ÿ±Çbs1axŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1xO###############################################################################Ÿ±Ç`a
Ÿ±Çbc1x# Work with labeled dataŸ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`cfigŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`a(Ÿ±Ç`cax1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`cax2Ÿ±Ç`a)Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`hsubplotsŸ±Ç`a(Ÿ±Çbmia1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia2Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`gfigsizeŸ±Çaoa=Ÿ±Ç`a(Ÿ±Çbmia9Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfc4.5Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`x                               Ÿ±Ç`ltight_layoutŸ±Çaoa=Ÿ±ÇbkcdTrueŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`fshareyŸ±Çaoa=Ÿ±ÇbkcdTrueŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`dartsŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`jstack_histŸ±Ç`a(Ÿ±Ç`cax1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`idict_dataŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`kcolor_cycleŸ±Ç`a Ÿ±Çaoa+Ÿ±Ç`a Ÿ±Ç`khatch_cycleŸ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`r                  Ÿ±Ç`ihist_funcŸ±Çaoa=Ÿ±Ç`ihist_funcŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`dartsŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`jstack_histŸ±Ç`a(Ÿ±Ç`cax2Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`idict_dataŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`kcolor_cycleŸ±Ç`a Ÿ±Çaoa+Ÿ±Ç`a Ÿ±Ç`khatch_cycleŸ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`r                  Ÿ±Ç`ihist_funcŸ±Çaoa=Ÿ±Ç`ihist_funcŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`flabelsŸ±Çaoa=Ÿ±Ç`a[Ÿ±Çbs1a'Ÿ±Çbs1eset 0Ÿ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1eset 3Ÿ±Çbs1a'Ÿ±Ç`a]Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cax1Ÿ±Çaoa.Ÿ±Ç`exaxisŸ±Çaoa.Ÿ±Ç`qset_major_locatorŸ±Ç`a(Ÿ±Ç`gmtickerŸ±Çaoa.Ÿ±Ç`kMaxNLocatorŸ±Ç`a(Ÿ±Çbmia5Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cax1Ÿ±Çaoa.Ÿ±Ç`jset_xlabelŸ±Ç`a(Ÿ±Çbs1a'Ÿ±Çbs1fcountsŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cax1Ÿ±Çaoa.Ÿ±Ç`jset_ylabelŸ±Ç`a(Ÿ±Çbs1a'Ÿ±Çbs1axŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cax2Ÿ±Çaoa.Ÿ±Ç`jset_ylabelŸ±Ç`a(Ÿ±Çbs1a'Ÿ±Çbs1axŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
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
Ÿ±Çbc1xO#    - `matplotlib.axes.Axes.fill_betweenx` / `matplotlib.pyplot.fill_betweenx`Ÿ±Ç`a
Ÿ±Çbc1xM#    - `matplotlib.axes.Axes.fill_between` / `matplotlib.pyplot.fill_between`Ÿ±Ç`a
Ÿ±Çbc1x/#    - `matplotlib.axis.Axis.set_major_locator`Ÿ±Ç`a
`dNoneˆ