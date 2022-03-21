������������bsdy"""
=========================================
prop_cycle property markevery in rcParams
=========================================

This example demonstrates a working solution to issue #8576, providing full
support of the markevery property for axes.prop_cycle assignments through
rcParams. Makes use of the same list of markevery cases from the
:doc:`markevery demo
</gallery/lines_bars_and_markers/markevery_demo>`.

Renders a plot with shifted-sine curves along each column with
a unique markevery value for each sine curve.
"""���`a
���bkndfrom���`a ���bnnfcycler���`a ���bknfimport���`a ���`fcycler���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����`a ���akbas���`a ���bnncmpl���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���`a
���bc1x:# Define a list of markevery cases and color cases to plot���`a
���`ecases���`a ���aoa=���`a ���`a[���bkcdNone���`a,���`a
���`i         ���bmia8���`a,���`a
���`i         ���`a(���bmib30���`a,���`a ���bmia8���`a)���`a,���`a
���`i         ���`a[���bmib16���`a,���`a ���bmib24���`a,���`a ���bmib30���`a]���`a,���`a
���`i         ���`a[���bmia0���`a,���`a ���aoa-���bmia1���`a]���`a,���`a
���`i         ���bnbeslice���`a(���bmic100���`a,���`a ���bmic200���`a,���`a ���bmia3���`a)���`a,���`a
���`i         ���bmfc0.1���`a,���`a
���`i         ���bmfc0.3���`a,���`a
���`i         ���bmfc1.5���`a,���`a
���`i         ���`a(���bmfc0.0���`a,���`a ���bmfc0.1���`a)���`a,���`a
���`i         ���`a(���bmfd0.45���`a,���`a ���bmfc0.1���`a)���`a]���`a
���`a
���`fcolors���`a ���aoa=���`a ���`a[���bs1a'���bs1g#1f77b4���bs1a'���`a,���`a
���`j          ���bs1a'���bs1g#ff7f0e���bs1a'���`a,���`a
���`j          ���bs1a'���bs1g#2ca02c���bs1a'���`a,���`a
���`j          ���bs1a'���bs1g#d62728���bs1a'���`a,���`a
���`j          ���bs1a'���bs1g#9467bd���bs1a'���`a,���`a
���`j          ���bs1a'���bs1g#8c564b���bs1a'���`a,���`a
���`j          ���bs1a'���bs1g#e377c2���bs1a'���`a,���`a
���`j          ���bs1a'���bs1g#7f7f7f���bs1a'���`a,���`a
���`j          ���bs1a'���bs1g#bcbd22���bs1a'���`a,���`a
���`j          ���bs1a'���bs1g#17becf���bs1a'���`a,���`a
���`j          ���bs1a'���bs1g#1a55FF���bs1a'���`a]���`a
���`a
���bc1xN# Configure rcParams axes.prop_cycle to simultaneously cycle cases and colors.���`a
���`cmpl���aoa.���`hrcParams���`a[���bs1a'���bs1oaxes.prop_cycle���bs1a'���`a]���`a ���aoa=���`a ���`fcycler���`a(���`imarkevery���aoa=���`ecases���`a,���`a ���`ecolor���aoa=���`fcolors���`a)���`a
���`a
���bc1x # Create data points and offsets���`a
���`ax���`a ���aoa=���`a ���`bnp���aoa.���`hlinspace���`a(���bmia0���`a,���`a ���bmia2���`a ���aoa*���`a ���`bnp���aoa.���`bpi���`a)���`a
���`goffsets���`a ���aoa=���`a ���`bnp���aoa.���`hlinspace���`a(���bmia0���`a,���`a ���bmia2���`a ���aoa*���`a ���`bnp���aoa.���`bpi���`a,���`a ���bmib11���`a,���`a ���`hendpoint���aoa=���bkceFalse���`a)���`a
���`byy���`a ���aoa=���`a ���`bnp���aoa.���`itranspose���`a(���`a[���`bnp���aoa.���`csin���`a(���`ax���`a ���aoa+���`a ���`cphi���`a)���`a ���akcfor���`a ���`cphi���`a ���bowbin���`a ���`goffsets���`a]���`a)���`a
���`a
���bc1x-# Set the plot curve with markers and a title���`a
���`cfig���`a ���aoa=���`a ���`cplt���aoa.���`ffigure���`a(���`a)���`a
���`bax���`a ���aoa=���`a ���`cfig���aoa.���`hadd_axes���`a(���`a[���bmfc0.1���`a,���`a ���bmfc0.1���`a,���`a ���bmfc0.6���`a,���`a ���bmfd0.75���`a]���`a)���`a
���`a
���akcfor���`a ���`ai���`a ���bowbin���`a ���bnberange���`a(���bnbclen���`a(���`ecases���`a)���`a)���`a:���`a
���`d    ���`bax���aoa.���`dplot���`a(���`byy���`a[���`a:���`a,���`a ���`ai���`a]���`a,���`a ���`fmarker���aoa=���bs1a'���bs1ao���bs1a'���`a,���`a ���`elabel���aoa=���bnbcstr���`a(���`ecases���`a[���`ai���`a]���`a)���`a)���`a
���`d    ���`bax���aoa.���`flegend���`a(���`nbbox_to_anchor���aoa=���`a(���bmfd1.05���`a,���`a ���bmia1���`a)���`a,���`a ���`cloc���aoa=���bs1a'���bs1jupper left���bs1a'���`a,���`a ���`mborderaxespad���aoa=���bmfb0.���`a)���`a
���`a
���`cplt���aoa.���`etitle���`a(���bs1a'���bs1x1Support for axes.prop_cycle cycler with markevery���bs1a'���`a)���`a
���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
`dNone�