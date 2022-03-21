������������bsdy$"""
=============
Check Buttons
=============

Turning visual elements on and off with check buttons.

This program shows the use of 'Check Buttons' which is similar to
check boxes. There are 3 different sine waves shown and we can choose which
waves are displayed with the check buttons.
"""���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���bkndfrom���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnngwidgets���`a ���bknfimport���`a ���`lCheckButtons���`a
���`a
���`at���`a ���aoa=���`a ���`bnp���aoa.���`farange���`a(���bmfc0.0���`a,���`a ���bmfc2.0���`a,���`a ���bmfd0.01���`a)���`a
���`bs0���`a ���aoa=���`a ���`bnp���aoa.���`csin���`a(���bmia2���aoa*���`bnp���aoa.���`bpi���aoa*���`at���`a)���`a
���`bs1���`a ���aoa=���`a ���`bnp���aoa.���`csin���`a(���bmia4���aoa*���`bnp���aoa.���`bpi���aoa*���`at���`a)���`a
���`bs2���`a ���aoa=���`a ���`bnp���aoa.���`csin���`a(���bmia6���aoa*���`bnp���aoa.���`bpi���aoa*���`at���`a)���`a
���`a
���`cfig���`a,���`a ���`bax���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`a)���`a
���`bl0���`a,���`a ���aoa=���`a ���`bax���aoa.���`dplot���`a(���`at���`a,���`a ���`bs0���`a,���`a ���`gvisible���aoa=���bkceFalse���`a,���`a ���`blw���aoa=���bmia2���`a,���`a ���`ecolor���aoa=���bs1a'���bs1ak���bs1a'���`a,���`a ���`elabel���aoa=���bs1a'���bs1d2 Hz���bs1a'���`a)���`a
���`bl1���`a,���`a ���aoa=���`a ���`bax���aoa.���`dplot���`a(���`at���`a,���`a ���`bs1���`a,���`a ���`blw���aoa=���bmia2���`a,���`a ���`ecolor���aoa=���bs1a'���bs1ar���bs1a'���`a,���`a ���`elabel���aoa=���bs1a'���bs1d4 Hz���bs1a'���`a)���`a
���`bl2���`a,���`a ���aoa=���`a ���`bax���aoa.���`dplot���`a(���`at���`a,���`a ���`bs2���`a,���`a ���`blw���aoa=���bmia2���`a,���`a ���`ecolor���aoa=���bs1a'���bs1ag���bs1a'���`a,���`a ���`elabel���aoa=���bs1a'���bs1d6 Hz���bs1a'���`a)���`a
���`cplt���aoa.���`osubplots_adjust���`a(���`dleft���aoa=���bmfc0.2���`a)���`a
���`a
���`elines���`a ���aoa=���`a ���`a[���`bl0���`a,���`a ���`bl1���`a,���`a ���`bl2���`a]���`a
���`a
���bc1xB# Make checkbuttons with all plotted lines with correct visibility���`a
���`crax���`a ���aoa=���`a ���`cplt���aoa.���`daxes���`a(���`a[���bmfd0.05���`a,���`a ���bmfc0.4���`a,���`a ���bmfc0.1���`a,���`a ���bmfd0.15���`a]���`a)���`a
���`flabels���`a ���aoa=���`a ���`a[���bnbcstr���`a(���`dline���aoa.���`iget_label���`a(���`a)���`a)���`a ���akcfor���`a ���`dline���`a ���bowbin���`a ���`elines���`a]���`a
���`jvisibility���`a ���aoa=���`a ���`a[���`dline���aoa.���`kget_visible���`a(���`a)���`a ���akcfor���`a ���`dline���`a ���bowbin���`a ���`elines���`a]���`a
���`echeck���`a ���aoa=���`a ���`lCheckButtons���`a(���`crax���`a,���`a ���`flabels���`a,���`a ���`jvisibility���`a)���`a
���`a
���`a
���akcdef���`a ���bnfdfunc���`a(���`elabel���`a)���`a:���`a
���`d    ���`eindex���`a ���aoa=���`a ���`flabels���aoa.���`eindex���`a(���`elabel���`a)���`a
���`d    ���`elines���`a[���`eindex���`a]���aoa.���`kset_visible���`a(���bowcnot���`a ���`elines���`a[���`eindex���`a]���aoa.���`kget_visible���`a(���`a)���`a)���`a
���`d    ���`cplt���aoa.���`ddraw���`a(���`a)���`a
���`a
���`echeck���aoa.���`jon_clicked���`a(���`dfunc���`a)���`a
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
���bc1x(#    - `matplotlib.widgets.CheckButtons`���`a
`dNone�