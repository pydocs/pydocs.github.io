��������v���bsdx�"""
=========================
Hatch-filled histograms
=========================

Hatching capabilities for plotting histograms.
"""���`a
���`a
���bknfimport���`a ���bnniitertools���`a
���bkndfrom���`a ���bnnifunctools���`a ���bknfimport���`a ���`gpartial���`a
���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfticker���`a ���akbas���`a ���bnngmticker���`a
���bkndfrom���`a ���bnnfcycler���`a ���bknfimport���`a ���`fcycler���`a
���`a
���`a
���akcdef���`a ���bnfkfilled_hist���`a(���`bax���`a,���`a ���`eedges���`a,���`a ���`fvalues���`a,���`a ���`gbottoms���aoa=���bkcdNone���`a,���`a ���`korientation���aoa=���bs1a'���bs1av���bs1a'���`a,���`a
���`p                ���aoa*���aoa*���`fkwargs���`a)���`a:���`a
���`d    ���bsdy�"""
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
    """���`a
���`d    ���bnbeprint���`a(���`korientation���`a)���`a
���`d    ���akbif���`a ���`korientation���`a ���bowcnot���`a ���bowbin���`a ���bs1a'���bs1bhv���bs1a'���`a:���`a
���`h        ���akeraise���`a ���bnejValueError���`a(���bs2a"���bs2worientation must be in ���bs2b{{���bs2a'���bs2ah���bs2a'���bs2b, ���bs2a'���bs2av���bs2a'���bs2c}} ���bs2a"���`a
���`x                         ���bs2a"���bs2dnot ���bsic{o}���bs2a"���aoa.���`fformat���`a(���`ao���aoa=���`korientation���`a)���`a)���`a
���`a
���`d    ���`fkwargs���aoa.���`jsetdefault���`a(���bs1a'���bs1dstep���bs1a'���`a,���`a ���bs1a'���bs1dpost���bs1a'���`a)���`a
���`d    ���`fkwargs���aoa.���`jsetdefault���`a(���bs1a'���bs1ealpha���bs1a'���`a,���`a ���bmfc0.7���`a)���`a
���`d    ���`eedges���`a ���aoa=���`a ���`bnp���aoa.���`gasarray���`a(���`eedges���`a)���`a
���`d    ���`fvalues���`a ���aoa=���`a ���`bnp���aoa.���`gasarray���`a(���`fvalues���`a)���`a
���`d    ���akbif���`a ���bnbclen���`a(���`eedges���`a)���`a ���aoa-���`a ���bmia1���`a ���aob!=���`a ���bnbclen���`a(���`fvalues���`a)���`a:���`a
���`h        ���akeraise���`a ���bnejValueError���`a(���bs1a'���bs1x/Must provide one more bin edge than value not: ���bs1a'���`a
���`x                         ���bs1a'���bs1llen(edges): ���bsid{lb}���bs1n len(values): ���bsid{lv}���bs1a'���aoa.���`fformat���`a(���`a
���`x                             ���`blb���aoa=���bnbclen���`a(���`eedges���`a)���`a,���`a ���`blv���aoa=���bnbclen���`a(���`fvalues���`a)���`a)���`a)���`a
���`a
���`d    ���akbif���`a ���`gbottoms���`a ���bowbis���`a ���bkcdNone���`a:���`a
���`h        ���`gbottoms���`a ���aoa=���`a ���bmia0���`a
���`d    ���`gbottoms���`a ���aoa=���`a ���`bnp���aoa.���`lbroadcast_to���`a(���`gbottoms���`a,���`a ���`fvalues���aoa.���`eshape���`a)���`a
���`a
���`d    ���`fvalues���`a ���aoa=���`a ���`bnp���aoa.���`fappend���`a(���`fvalues���`a,���`a ���`fvalues���`a[���aoa-���bmia1���`a]���`a)���`a
���`d    ���`gbottoms���`a ���aoa=���`a ���`bnp���aoa.���`fappend���`a(���`gbottoms���`a,���`a ���`gbottoms���`a[���aoa-���bmia1���`a]���`a)���`a
���`d    ���akbif���`a ���`korientation���`a ���aob==���`a ���bs1a'���bs1ah���bs1a'���`a:���`a
���`h        ���akfreturn���`a ���`bax���aoa.���`mfill_betweenx���`a(���`eedges���`a,���`a ���`fvalues���`a,���`a ���`gbottoms���`a,���`a
���`x                                 ���aoa*���aoa*���`fkwargs���`a)���`a
���`d    ���akdelif���`a ���`korientation���`a ���aob==���`a ���bs1a'���bs1av���bs1a'���`a:���`a
���`h        ���akfreturn���`a ���`bax���aoa.���`lfill_between���`a(���`eedges���`a,���`a ���`fvalues���`a,���`a ���`gbottoms���`a,���`a
���`x                               ���aoa*���aoa*���`fkwargs���`a)���`a
���`d    ���akdelse���`a:���`a
���`h        ���akeraise���`a ���bnenAssertionError���`a(���bs2a"���bs2xyou should never be here���bs2a"���`a)���`a
���`a
���`a
���akcdef���`a ���bnfjstack_hist���`a(���`bax���`a,���`a ���`lstacked_data���`a,���`a ���`isty_cycle���`a,���`a ���`gbottoms���aoa=���bkcdNone���`a,���`a
���`o               ���`ihist_func���aoa=���bkcdNone���`a,���`a ���`flabels���aoa=���bkcdNone���`a,���`a
���`o               ���`iplot_func���aoa=���bkcdNone���`a,���`a ���`kplot_kwargs���aoa=���bkcdNone���`a)���`a:���`a
���`d    ���bsdy�"""
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
    """���`a
���`d    ���bc1x$# deal with default binning function���`a
���`d    ���akbif���`a ���`ihist_func���`a ���bowbis���`a ���bkcdNone���`a:���`a
���`h        ���`ihist_func���`a ���aoa=���`a ���`bnp���aoa.���`ihistogram���`a
���`a
���`d    ���bc1x%# deal with default plotting function���`a
���`d    ���akbif���`a ���`iplot_func���`a ���bowbis���`a ���bkcdNone���`a:���`a
���`h        ���`iplot_func���`a ���aoa=���`a ���`kfilled_hist���`a
���`a
���`d    ���bc1s# deal with default���`a
���`d    ���akbif���`a ���`kplot_kwargs���`a ���bowbis���`a ���bkcdNone���`a:���`a
���`h        ���`kplot_kwargs���`a ���aoa=���`a ���`a{���`a}���`a
���`d    ���bnbeprint���`a(���`kplot_kwargs���`a)���`a
���`d    ���akctry���`a:���`a
���`h        ���`fl_keys���`a ���aoa=���`a ���`lstacked_data���aoa.���`dkeys���`a(���`a)���`a
���`h        ���`jlabel_data���`a ���aoa=���`a ���bkcdTrue���`a
���`h        ���akbif���`a ���`flabels���`a ���bowbis���`a ���bkcdNone���`a:���`a
���`l            ���`flabels���`a ���aoa=���`a ���`fl_keys���`a
���`a
���`d    ���akfexcept���`a ���bnenAttributeError���`a:���`a
���`h        ���`jlabel_data���`a ���aoa=���`a ���bkceFalse���`a
���`h        ���akbif���`a ���`flabels���`a ���bowbis���`a ���bkcdNone���`a:���`a
���`l            ���`flabels���`a ���aoa=���`a ���`iitertools���aoa.���`frepeat���`a(���bkcdNone���`a)���`a
���`a
���`d    ���akbif���`a ���`jlabel_data���`a:���`a
���`h        ���`iloop_iter���`a ���aoa=���`a ���bnbienumerate���`a(���`a(���`lstacked_data���`a[���`clab���`a]���`a,���`a ���`clab���`a,���`a ���`as���`a)���`a
���`x                              ���akcfor���`a ���`clab���`a,���`a ���`as���`a ���bowbin���`a ���bnbczip���`a(���`flabels���`a,���`a ���`isty_cycle���`a)���`a)���`a
���`d    ���akdelse���`a:���`a
���`h        ���`iloop_iter���`a ���aoa=���`a ���bnbienumerate���`a(���bnbczip���`a(���`lstacked_data���`a,���`a ���`flabels���`a,���`a ���`isty_cycle���`a)���`a)���`a
���`a
���`d    ���`darts���`a ���aoa=���`a ���`a{���`a}���`a
���`d    ���akcfor���`a ���`aj���`a,���`a ���`a(���`ddata���`a,���`a ���`elabel���`a,���`a ���`csty���`a)���`a ���bowbin���`a ���`iloop_iter���`a:���`a
���`h        ���akbif���`a ���`elabel���`a ���bowbis���`a ���bkcdNone���`a:���`a
���`l            ���`elabel���`a ���aoa=���`a ���bs1a'���bs1idflt set ���bsic{n}���bs1a'���aoa.���`fformat���`a(���`an���aoa=���`aj���`a)���`a
���`h        ���`elabel���`a ���aoa=���`a ���`csty���aoa.���`cpop���`a(���bs1a'���bs1elabel���bs1a'���`a,���`a ���`elabel���`a)���`a
���`h        ���`dvals���`a,���`a ���`eedges���`a ���aoa=���`a ���`ihist_func���`a(���`ddata���`a)���`a
���`h        ���akbif���`a ���`gbottoms���`a ���bowbis���`a ���bkcdNone���`a:���`a
���`l            ���`gbottoms���`a ���aoa=���`a ���`bnp���aoa.���`jzeros_like���`a(���`dvals���`a)���`a
���`h        ���`ctop���`a ���aoa=���`a ���`gbottoms���`a ���aoa+���`a ���`dvals���`a
���`h        ���bnbeprint���`a(���`csty���`a)���`a
���`h        ���`csty���aoa.���`fupdate���`a(���`kplot_kwargs���`a)���`a
���`h        ���bnbeprint���`a(���`csty���`a)���`a
���`h        ���`cret���`a ���aoa=���`a ���`iplot_func���`a(���`bax���`a,���`a ���`eedges���`a,���`a ���`ctop���`a,���`a ���`gbottoms���aoa=���`gbottoms���`a,���`a
���`x                        ���`elabel���aoa=���`elabel���`a,���`a ���aoa*���aoa*���`csty���`a)���`a
���`h        ���`gbottoms���`a ���aoa=���`a ���`ctop���`a
���`h        ���`darts���`a[���`elabel���`a]���`a ���aoa=���`a ���`cret���`a
���`d    ���`bax���aoa.���`flegend���`a(���`hfontsize���aoa=���bmib10���`a)���`a
���`d    ���akfreturn���`a ���`darts���`a
���`a
���`a
���bc1x)# set up histogram function to fixed bins���`a
���`eedges���`a ���aoa=���`a ���`bnp���aoa.���`hlinspace���`a(���aoa-���bmia3���`a,���`a ���bmia3���`a,���`a ���bmib20���`a,���`a ���`hendpoint���aoa=���bkcdTrue���`a)���`a
���`ihist_func���`a ���aoa=���`a ���`gpartial���`a(���`bnp���aoa.���`ihistogram���`a,���`a ���`dbins���aoa=���`eedges���`a)���`a
���`a
���bc1u# set up style cycles���`a
���`kcolor_cycle���`a ���aoa=���`a ���`fcycler���`a(���`ifacecolor���aoa=���`cplt���aoa.���`hrcParams���`a[���bs1a'���bs1oaxes.prop_cycle���bs1a'���`a]���`a[���`a:���bmia4���`a]���`a)���`a
���`klabel_cycle���`a ���aoa=���`a ���`fcycler���`a(���`elabel���aoa=���`a[���bs1a'���bs1dset ���bsic{n}���bs1a'���aoa.���`fformat���`a(���`an���aoa=���`an���`a)���`a ���akcfor���`a ���`an���`a ���bowbin���`a ���bnberange���`a(���bmia4���`a)���`a]���`a)���`a
���`khatch_cycle���`a ���aoa=���`a ���`fcycler���`a(���`ehatch���aoa=���`a[���bs1a'���bs1a/���bs1a'���`a,���`a ���bs1a'���bs1a*���bs1a'���`a,���`a ���bs1a'���bs1a+���bs1a'���`a,���`a ���bs1a'���bs1a|���bs1a'���`a]���`a)���`a
���`a
���bc1x)# Fixing random state for reproducibility���`a
���`bnp���aoa.���`frandom���aoa.���`dseed���`a(���bmih19680801���`a)���`a
���`a
���`jstack_data���`a ���aoa=���`a ���`bnp���aoa.���`frandom���aoa.���`erandn���`a(���bmia4���`a,���`a ���bmie12250���`a)���`a
���`idict_data���`a ���aoa=���`a ���bnbddict���`a(���bnbczip���`a(���`a(���`ac���`a[���bs1a'���bs1elabel���bs1a'���`a]���`a ���akcfor���`a ���`ac���`a ���bowbin���`a ���`klabel_cycle���`a)���`a,���`a ���`jstack_data���`a)���`a)���`a
���`a
���bc1xO###############################################################################���`a
���bc1x# Work with plain arrays���`a
���`a
���`cfig���`a,���`a ���`a(���`cax1���`a,���`a ���`cax2���`a)���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���bmia1���`a,���`a ���bmia2���`a,���`a ���`gfigsize���aoa=���`a(���bmia9���`a,���`a ���bmfc4.5���`a)���`a,���`a ���`ltight_layout���aoa=���bkcdTrue���`a)���`a
���`darts���`a ���aoa=���`a ���`jstack_hist���`a(���`cax1���`a,���`a ���`jstack_data���`a,���`a ���`kcolor_cycle���`a ���aoa+���`a ���`klabel_cycle���`a ���aoa+���`a ���`khatch_cycle���`a,���`a
���`r                  ���`ihist_func���aoa=���`ihist_func���`a)���`a
���`a
���`darts���`a ���aoa=���`a ���`jstack_hist���`a(���`cax2���`a,���`a ���`jstack_data���`a,���`a ���`kcolor_cycle���`a,���`a
���`r                  ���`ihist_func���aoa=���`ihist_func���`a,���`a
���`r                  ���`kplot_kwargs���aoa=���bnbddict���`a(���`iedgecolor���aoa=���bs1a'���bs1aw���bs1a'���`a,���`a ���`korientation���aoa=���bs1a'���bs1ah���bs1a'���`a)���`a)���`a
���`cax1���aoa.���`jset_ylabel���`a(���bs1a'���bs1fcounts���bs1a'���`a)���`a
���`cax1���aoa.���`jset_xlabel���`a(���bs1a'���bs1ax���bs1a'���`a)���`a
���`cax2���aoa.���`jset_xlabel���`a(���bs1a'���bs1fcounts���bs1a'���`a)���`a
���`cax2���aoa.���`jset_ylabel���`a(���bs1a'���bs1ax���bs1a'���`a)���`a
���`a
���bc1xO###############################################################################���`a
���bc1x# Work with labeled data���`a
���`a
���`cfig���`a,���`a ���`a(���`cax1���`a,���`a ���`cax2���`a)���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���bmia1���`a,���`a ���bmia2���`a,���`a ���`gfigsize���aoa=���`a(���bmia9���`a,���`a ���bmfc4.5���`a)���`a,���`a
���`x                               ���`ltight_layout���aoa=���bkcdTrue���`a,���`a ���`fsharey���aoa=���bkcdTrue���`a)���`a
���`a
���`darts���`a ���aoa=���`a ���`jstack_hist���`a(���`cax1���`a,���`a ���`idict_data���`a,���`a ���`kcolor_cycle���`a ���aoa+���`a ���`khatch_cycle���`a,���`a
���`r                  ���`ihist_func���aoa=���`ihist_func���`a)���`a
���`a
���`darts���`a ���aoa=���`a ���`jstack_hist���`a(���`cax2���`a,���`a ���`idict_data���`a,���`a ���`kcolor_cycle���`a ���aoa+���`a ���`khatch_cycle���`a,���`a
���`r                  ���`ihist_func���aoa=���`ihist_func���`a,���`a ���`flabels���aoa=���`a[���bs1a'���bs1eset 0���bs1a'���`a,���`a ���bs1a'���bs1eset 3���bs1a'���`a]���`a)���`a
���`cax1���aoa.���`exaxis���aoa.���`qset_major_locator���`a(���`gmticker���aoa.���`kMaxNLocator���`a(���bmia5���`a)���`a)���`a
���`cax1���aoa.���`jset_xlabel���`a(���bs1a'���bs1fcounts���bs1a'���`a)���`a
���`cax1���aoa.���`jset_ylabel���`a(���bs1a'���bs1ax���bs1a'���`a)���`a
���`cax2���aoa.���`jset_ylabel���`a(���bs1a'���bs1ax���bs1a'���`a)���`a
���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
���`a
���bc1xM#############################################################################���`a
���bc1a#���`a
���bc1x# .. admonition:: References���`a
���bc1a#���`a
���bc1xN#    The use of the following functions, methods, classes and modules is shown���`a
���bc1u#    in this example:���`a
���bc1a#���`a
���bc1xO#    - `matplotlib.axes.Axes.fill_betweenx` / `matplotlib.pyplot.fill_betweenx`���`a
���bc1xM#    - `matplotlib.axes.Axes.fill_between` / `matplotlib.pyplot.fill_between`���`a
���bc1x/#    - `matplotlib.axis.Axis.set_major_locator`���`a
`dNone�