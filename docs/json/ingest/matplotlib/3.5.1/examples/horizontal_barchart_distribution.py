��������`���bsdy"""
=============================================
Discrete distribution as horizontal bar chart
=============================================

Stacked bar charts can be used to visualize discrete distributions.

This example visualizes the result of a survey in which people could rate
their agreement to questions on a five-element scale.

The horizontal stacking is achieved by calling `~.Axes.barh()` for each
category and passing the starting point as the cumulative sum of the
already drawn bars via the parameter ``left``.
"""���`a
���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���`a
���`a
���`ncategory_names���`a ���aoa=���`a ���`a[���bs1a'���bs1qStrongly disagree���bs1a'���`a,���`a ���bs1a'���bs1hDisagree���bs1a'���`a,���`a
���`r                  ���bs1a'���bs1xNeither agree nor disagree���bs1a'���`a,���`a ���bs1a'���bs1eAgree���bs1a'���`a,���`a ���bs1a'���bs1nStrongly agree���bs1a'���`a]���`a
���`gresults���`a ���aoa=���`a ���`a{���`a
���`d    ���bs1a'���bs1jQuestion 1���bs1a'���`a:���`a ���`a[���bmib10���`a,���`a ���bmib15���`a,���`a ���bmib17���`a,���`a ���bmib32���`a,���`a ���bmib26���`a]���`a,���`a
���`d    ���bs1a'���bs1jQuestion 2���bs1a'���`a:���`a ���`a[���bmib26���`a,���`a ���bmib22���`a,���`a ���bmib29���`a,���`a ���bmib10���`a,���`a ���bmib13���`a]���`a,���`a
���`d    ���bs1a'���bs1jQuestion 3���bs1a'���`a:���`a ���`a[���bmib35���`a,���`a ���bmib37���`a,���`a ���bmia7���`a,���`a ���bmia2���`a,���`a ���bmib19���`a]���`a,���`a
���`d    ���bs1a'���bs1jQuestion 4���bs1a'���`a:���`a ���`a[���bmib32���`a,���`a ���bmib11���`a,���`a ���bmia9���`a,���`a ���bmib15���`a,���`a ���bmib33���`a]���`a,���`a
���`d    ���bs1a'���bs1jQuestion 5���bs1a'���`a:���`a ���`a[���bmib21���`a,���`a ���bmib29���`a,���`a ���bmia5���`a,���`a ���bmia5���`a,���`a ���bmib40���`a]���`a,���`a
���`d    ���bs1a'���bs1jQuestion 6���bs1a'���`a:���`a ���`a[���bmia8���`a,���`a ���bmib19���`a,���`a ���bmia5���`a,���`a ���bmib30���`a,���`a ���bmib38���`a]���`a
���`a}���`a
���`a
���`a
���akcdef���`a ���bnffsurvey���`a(���`gresults���`a,���`a ���`ncategory_names���`a)���`a:���`a
���`d    ���bsdyC"""
    Parameters
    ----------
    results : dict
        A mapping from question labels to a list of answers per category.
        It is assumed all lists contain the same number of entries and that
        it matches the length of *category_names*.
    category_names : list of str
        The category labels.
    """���`a
���`d    ���`flabels���`a ���aoa=���`a ���bnbdlist���`a(���`gresults���aoa.���`dkeys���`a(���`a)���`a)���`a
���`d    ���`ddata���`a ���aoa=���`a ���`bnp���aoa.���`earray���`a(���bnbdlist���`a(���`gresults���aoa.���`fvalues���`a(���`a)���`a)���`a)���`a
���`d    ���`hdata_cum���`a ���aoa=���`a ���`ddata���aoa.���`fcumsum���`a(���`daxis���aoa=���bmia1���`a)���`a
���`d    ���`ocategory_colors���`a ���aoa=���`a ���`cplt���aoa.���`icolormaps���`a[���bs1a'���bs1fRdYlGn���bs1a'���`a]���`a(���`a
���`h        ���`bnp���aoa.���`hlinspace���`a(���bmfd0.15���`a,���`a ���bmfd0.85���`a,���`a ���`ddata���aoa.���`eshape���`a[���bmia1���`a]���`a)���`a)���`a
���`a
���`d    ���`cfig���`a,���`a ���`bax���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`gfigsize���aoa=���`a(���bmfc9.2���`a,���`a ���bmia5���`a)���`a)���`a
���`d    ���`bax���aoa.���`linvert_yaxis���`a(���`a)���`a
���`d    ���`bax���aoa.���`exaxis���aoa.���`kset_visible���`a(���bkceFalse���`a)���`a
���`d    ���`bax���aoa.���`hset_xlim���`a(���bmia0���`a,���`a ���`bnp���aoa.���`csum���`a(���`ddata���`a,���`a ���`daxis���aoa=���bmia1���`a)���aoa.���`cmax���`a(���`a)���`a)���`a
���`a
���`d    ���akcfor���`a ���`ai���`a,���`a ���`a(���`gcolname���`a,���`a ���`ecolor���`a)���`a ���bowbin���`a ���bnbienumerate���`a(���bnbczip���`a(���`ncategory_names���`a,���`a ���`ocategory_colors���`a)���`a)���`a:���`a
���`h        ���`fwidths���`a ���aoa=���`a ���`ddata���`a[���`a:���`a,���`a ���`ai���`a]���`a
���`h        ���`fstarts���`a ���aoa=���`a ���`hdata_cum���`a[���`a:���`a,���`a ���`ai���`a]���`a ���aoa-���`a ���`fwidths���`a
���`h        ���`erects���`a ���aoa=���`a ���`bax���aoa.���`dbarh���`a(���`flabels���`a,���`a ���`fwidths���`a,���`a ���`dleft���aoa=���`fstarts���`a,���`a ���`fheight���aoa=���bmfc0.5���`a,���`a
���`x                        ���`elabel���aoa=���`gcolname���`a,���`a ���`ecolor���aoa=���`ecolor���`a)���`a
���`a
���`h        ���`ar���`a,���`a ���`ag���`a,���`a ���`ab���`a,���`a ���`a_���`a ���aoa=���`a ���`ecolor���`a
���`h        ���`jtext_color���`a ���aoa=���`a ���bs1a'���bs1ewhite���bs1a'���`a ���akbif���`a ���`ar���`a ���aoa*���`a ���`ag���`a ���aoa*���`a ���`ab���`a ���aoa<���`a ���bmfc0.5���`a ���akdelse���`a ���bs1a'���bs1hdarkgrey���bs1a'���`a
���`h        ���`bax���aoa.���`ibar_label���`a(���`erects���`a,���`a ���`jlabel_type���aoa=���bs1a'���bs1fcenter���bs1a'���`a,���`a ���`ecolor���aoa=���`jtext_color���`a)���`a
���`d    ���`bax���aoa.���`flegend���`a(���`dncol���aoa=���bnbclen���`a(���`ncategory_names���`a)���`a,���`a ���`nbbox_to_anchor���aoa=���`a(���bmia0���`a,���`a ���bmia1���`a)���`a,���`a
���`n              ���`cloc���aoa=���bs1a'���bs1jlower left���bs1a'���`a,���`a ���`hfontsize���aoa=���bs1a'���bs1esmall���bs1a'���`a)���`a
���`a
���`d    ���akfreturn���`a ���`cfig���`a,���`a ���`bax���`a
���`a
���`a
���`fsurvey���`a(���`gresults���`a,���`a ���`ncategory_names���`a)���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
���`a
���bc1xM#############################################################################���`a
���bc1a#���`a
���bc1x# .. admonition:: References���`a
���bc1a#���`a
���bc1xN#    The use of the following functions, methods, classes and modules is shown���`a
���bc1u#    in this example:���`a
���bc1a#���`a
���bc1x=#    - `matplotlib.axes.Axes.barh` / `matplotlib.pyplot.barh`���`a
���bc1xG#    - `matplotlib.axes.Axes.bar_label` / `matplotlib.pyplot.bar_label`���`a
���bc1xA#    - `matplotlib.axes.Axes.legend` / `matplotlib.pyplot.legend`���`a
`dNone�