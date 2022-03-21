�����������bsdx�"""
=============================
Grouped bar chart with labels
=============================

This example shows a how to create a grouped bar chart and how to annotate
bars with labels.
"""���`a
���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���`a
���`a
���`flabels���`a ���aoa=���`a ���`a[���bs1a'���bs1bG1���bs1a'���`a,���`a ���bs1a'���bs1bG2���bs1a'���`a,���`a ���bs1a'���bs1bG3���bs1a'���`a,���`a ���bs1a'���bs1bG4���bs1a'���`a,���`a ���bs1a'���bs1bG5���bs1a'���`a]���`a
���`imen_means���`a ���aoa=���`a ���`a[���bmib20���`a,���`a ���bmib34���`a,���`a ���bmib30���`a,���`a ���bmib35���`a,���`a ���bmib27���`a]���`a
���`kwomen_means���`a ���aoa=���`a ���`a[���bmib25���`a,���`a ���bmib32���`a,���`a ���bmib34���`a,���`a ���bmib20���`a,���`a ���bmib25���`a]���`a
���`a
���`ax���`a ���aoa=���`a ���`bnp���aoa.���`farange���`a(���bnbclen���`a(���`flabels���`a)���`a)���`b  ���bc1u# the label locations���`a
���`ewidth���`a ���aoa=���`a ���bmfd0.35���`b  ���bc1w# the width of the bars���`a
���`a
���`cfig���`a,���`a ���`bax���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`a)���`a
���`frects1���`a ���aoa=���`a ���`bax���aoa.���`cbar���`a(���`ax���`a ���aoa-���`a ���`ewidth���aoa/���bmia2���`a,���`a ���`imen_means���`a,���`a ���`ewidth���`a,���`a ���`elabel���aoa=���bs1a'���bs1cMen���bs1a'���`a)���`a
���`frects2���`a ���aoa=���`a ���`bax���aoa.���`cbar���`a(���`ax���`a ���aoa+���`a ���`ewidth���aoa/���bmia2���`a,���`a ���`kwomen_means���`a,���`a ���`ewidth���`a,���`a ���`elabel���aoa=���bs1a'���bs1eWomen���bs1a'���`a)���`a
���`a
���bc1xE# Add some text for labels, title and custom x-axis tick labels, etc.���`a
���`bax���aoa.���`jset_ylabel���`a(���bs1a'���bs1fScores���bs1a'���`a)���`a
���`bax���aoa.���`iset_title���`a(���bs1a'���bs1xScores by group and gender���bs1a'���`a)���`a
���`bax���aoa.���`jset_xticks���`a(���`ax���`a,���`a ���`flabels���`a)���`a
���`bax���aoa.���`flegend���`a(���`a)���`a
���`a
���`bax���aoa.���`ibar_label���`a(���`frects1���`a,���`a ���`gpadding���aoa=���bmia3���`a)���`a
���`bax���aoa.���`ibar_label���`a(���`frects2���`a,���`a ���`gpadding���aoa=���bmia3���`a)���`a
���`a
���`cfig���aoa.���`ltight_layout���`a(���`a)���`a
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
���bc1xG#    - `matplotlib.axes.Axes.bar_label` / `matplotlib.pyplot.bar_label`���`a
`dNone�