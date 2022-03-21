������������bsdyu"""
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
"""���`a
���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���`a
���bc1xO###############################################################################���`a
���bc1q# Define the data���`a
���`a
���`aN���`a ���aoa=���`a ���bmia5���`a
���`hmenMeans���`a ���aoa=���`a ���`a(���bmib20���`a,���`a ���bmib35���`a,���`a ���bmib30���`a,���`a ���bmib35���`a,���`a ���aoa-���bmib27���`a)���`a
���`jwomenMeans���`a ���aoa=���`a ���`a(���bmib25���`a,���`a ���bmib32���`a,���`a ���bmib34���`a,���`a ���bmib20���`a,���`a ���aoa-���bmib25���`a)���`a
���`fmenStd���`a ���aoa=���`a ���`a(���bmia2���`a,���`a ���bmia3���`a,���`a ���bmia4���`a,���`a ���bmia1���`a,���`a ���bmia2���`a)���`a
���`hwomenStd���`a ���aoa=���`a ���`a(���bmia3���`a,���`a ���bmia5���`a,���`a ���bmia2���`a,���`a ���bmia3���`a,���`a ���bmia3���`a)���`a
���`cind���`a ���aoa=���`a ���`bnp���aoa.���`farange���`a(���`aN���`a)���`d    ���bc1x # the x locations for the groups���`a
���`ewidth���`a ���aoa=���`a ���bmfd0.35���`g       ���bc1x4# the width of the bars: can also be len(x) sequence���`a
���`a
���bc1xO###############################################################################���`a
���bc1x"# Stacked bar plot with error bars���`a
���`a
���`cfig���`a,���`a ���`bax���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`a)���`a
���`a
���`bp1���`a ���aoa=���`a ���`bax���aoa.���`cbar���`a(���`cind���`a,���`a ���`hmenMeans���`a,���`a ���`ewidth���`a,���`a ���`dyerr���aoa=���`fmenStd���`a,���`a ���`elabel���aoa=���bs1a'���bs1cMen���bs1a'���`a)���`a
���`bp2���`a ���aoa=���`a ���`bax���aoa.���`cbar���`a(���`cind���`a,���`a ���`jwomenMeans���`a,���`a ���`ewidth���`a,���`a
���`l            ���`fbottom���aoa=���`hmenMeans���`a,���`a ���`dyerr���aoa=���`hwomenStd���`a,���`a ���`elabel���aoa=���bs1a'���bs1eWomen���bs1a'���`a)���`a
���`a
���`bax���aoa.���`gaxhline���`a(���bmia0���`a,���`a ���`ecolor���aoa=���bs1a'���bs1dgrey���bs1a'���`a,���`a ���`ilinewidth���aoa=���bmfc0.8���`a)���`a
���`bax���aoa.���`jset_ylabel���`a(���bs1a'���bs1fScores���bs1a'���`a)���`a
���`bax���aoa.���`iset_title���`a(���bs1a'���bs1xScores by group and gender���bs1a'���`a)���`a
���`bax���aoa.���`jset_xticks���`a(���`cind���`a,���`a ���`flabels���aoa=���`a[���bs1a'���bs1bG1���bs1a'���`a,���`a ���bs1a'���bs1bG2���bs1a'���`a,���`a ���bs1a'���bs1bG3���bs1a'���`a,���`a ���bs1a'���bs1bG4���bs1a'���`a,���`a ���bs1a'���bs1bG5���bs1a'���`a]���`a)���`a
���`bax���aoa.���`flegend���`a(���`a)���`a
���`a
���bc1x># Label with label_type 'center' instead of the default 'edge'���`a
���`bax���aoa.���`ibar_label���`a(���`bp1���`a,���`a ���`jlabel_type���aoa=���bs1a'���bs1fcenter���bs1a'���`a)���`a
���`bax���aoa.���`ibar_label���`a(���`bp2���`a,���`a ���`jlabel_type���aoa=���bs1a'���bs1fcenter���bs1a'���`a)���`a
���`bax���aoa.���`ibar_label���`a(���`bp2���`a)���`a
���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
���`a
���bc1xO###############################################################################���`a
���bc1v# Horizontal bar chart���`a
���`a
���bc1x)# Fixing random state for reproducibility���`a
���`bnp���aoa.���`frandom���aoa.���`dseed���`a(���bmih19680801���`a)���`a
���`a
���bc1n# Example data���`a
���`fpeople���`a ���aoa=���`a ���`a(���bs1a'���bs1cTom���bs1a'���`a,���`a ���bs1a'���bs1dDick���bs1a'���`a,���`a ���bs1a'���bs1eHarry���bs1a'���`a,���`a ���bs1a'���bs1dSlim���bs1a'���`a,���`a ���bs1a'���bs1cJim���bs1a'���`a)���`a
���`ey_pos���`a ���aoa=���`a ���`bnp���aoa.���`farange���`a(���bnbclen���`a(���`fpeople���`a)���`a)���`a
���`kperformance���`a ���aoa=���`a ���bmia3���`a ���aoa+���`a ���bmib10���`a ���aoa*���`a ���`bnp���aoa.���`frandom���aoa.���`drand���`a(���bnbclen���`a(���`fpeople���`a)���`a)���`a
���`eerror���`a ���aoa=���`a ���`bnp���aoa.���`frandom���aoa.���`drand���`a(���bnbclen���`a(���`fpeople���`a)���`a)���`a
���`a
���`cfig���`a,���`a ���`bax���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`a)���`a
���`a
���`ehbars���`a ���aoa=���`a ���`bax���aoa.���`dbarh���`a(���`ey_pos���`a,���`a ���`kperformance���`a,���`a ���`dxerr���aoa=���`eerror���`a,���`a ���`ealign���aoa=���bs1a'���bs1fcenter���bs1a'���`a)���`a
���`bax���aoa.���`jset_yticks���`a(���`ey_pos���`a,���`a ���`flabels���aoa=���`fpeople���`a)���`a
���`bax���aoa.���`linvert_yaxis���`a(���`a)���`b  ���bc1x# labels read top-to-bottom���`a
���`bax���aoa.���`jset_xlabel���`a(���bs1a'���bs1kPerformance���bs1a'���`a)���`a
���`bax���aoa.���`iset_title���`a(���bs1a'���bs1x!How fast do you want to go today?���bs1a'���`a)���`a
���`a
���bc1x'# Label with specially formatted floats���`a
���`bax���aoa.���`ibar_label���`a(���`ehbars���`a,���`a ���`cfmt���aoa=���bs1a'���bsid%.2f���bs1a'���`a)���`a
���`bax���aoa.���`hset_xlim���`a(���`eright���aoa=���bmib15���`a)���`b  ���bc1x# adjust xlim to fit labels���`a
���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
���`a
���bc1xO###############################################################################���`a
���bc1xB# Some of the more advanced things that one can do with bar labels���`a
���`a
���`cfig���`a,���`a ���`bax���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`a)���`a
���`a
���`ehbars���`a ���aoa=���`a ���`bax���aoa.���`dbarh���`a(���`ey_pos���`a,���`a ���`kperformance���`a,���`a ���`dxerr���aoa=���`eerror���`a,���`a ���`ealign���aoa=���bs1a'���bs1fcenter���bs1a'���`a)���`a
���`bax���aoa.���`jset_yticks���`a(���`ey_pos���`a,���`a ���`flabels���aoa=���`fpeople���`a)���`a
���`bax���aoa.���`linvert_yaxis���`a(���`a)���`b  ���bc1x# labels read top-to-bottom���`a
���`bax���aoa.���`jset_xlabel���`a(���bs1a'���bs1kPerformance���bs1a'���`a)���`a
���`bax���aoa.���`iset_title���`a(���bs1a'���bs1x!How fast do you want to go today?���bs1a'���`a)���`a
���`a
���bc1x@# Label with given captions, custom padding and annotate options���`a
���`bax���aoa.���`ibar_label���`a(���`ehbars���`a,���`a ���`flabels���aoa=���`a[���bs1a'���bs1b±���bsid%.2f���bs1a'���`a ���aoa%���`a ���`ae���`a ���akcfor���`a ���`ae���`a ���bowbin���`a ���`eerror���`a]���`a,���`a
���`m             ���`gpadding���aoa=���bmia8���`a,���`a ���`ecolor���aoa=���bs1a'���bs1ab���bs1a'���`a,���`a ���`hfontsize���aoa=���bmib14���`a)���`a
���`bax���aoa.���`hset_xlim���`a(���`eright���aoa=���bmib16���`a)���`a
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
���bc1x;#    - `matplotlib.axes.Axes.bar` / `matplotlib.pyplot.bar`���`a
���bc1x=#    - `matplotlib.axes.Axes.barh` / `matplotlib.pyplot.barh`���`a
���bc1xG#    - `matplotlib.axes.Axes.bar_label` / `matplotlib.pyplot.bar_label`���`a
`dNone�