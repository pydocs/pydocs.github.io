������������bsdx�"""
============
axhspan Demo
============

Create lines or rectangles that span the axes in either the horizontal or
vertical direction, and lines than span the axes with an arbitrary orientation.
"""���`a
���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���`a
���`at���`a ���aoa=���`a ���`bnp���aoa.���`farange���`a(���aoa-���bmia1���`a,���`a ���bmia2���`a,���`a ���bmfc.01���`a)���`a
���`as���`a ���aoa=���`a ���`bnp���aoa.���`csin���`a(���bmia2���`a ���aoa*���`a ���`bnp���aoa.���`bpi���`a ���aoa*���`a ���`at���`a)���`a
���`a
���`cfig���`a,���`a ���`bax���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`a)���`a
���`a
���`bax���aoa.���`dplot���`a(���`at���`a,���`a ���`as���`a)���`a
���bc1x9# Thick red horizontal line at y=0 that spans the xrange.���`a
���`bax���aoa.���`gaxhline���`a(���`ilinewidth���aoa=���bmia8���`a,���`a ���`ecolor���aoa=���bs1a'���bs1g#d62728���bs1a'���`a)���`a
���bc1x/# Horizontal line at y=1 that spans the xrange.���`a
���`bax���aoa.���`gaxhline���`a(���`ay���aoa=���bmia1���`a)���`a
���bc1x-# Vertical line at x=1 that spans the yrange.���`a
���`bax���aoa.���`gaxvline���`a(���`ax���aoa=���bmia1���`a)���`a
���bc1xN# Thick blue vertical line at x=0 that spans the upper quadrant of the yrange.���`a
���`bax���aoa.���`gaxvline���`a(���`ax���aoa=���bmia0���`a,���`a ���`dymin���aoa=���bmfd0.75���`a,���`a ���`ilinewidth���aoa=���bmia8���`a,���`a ���`ecolor���aoa=���bs1a'���bs1g#1f77b4���bs1a'���`a)���`a
���bc1x?# Default hline at y=.5 that spans the middle half of the axes.���`a
���`bax���aoa.���`gaxhline���`a(���`ay���aoa=���bmfb.5���`a,���`a ���`dxmin���aoa=���bmfd0.25���`a,���`a ���`dxmax���aoa=���bmfd0.75���`a)���`a
���bc1x5# Infinite black line going through (0, 0) to (1, 1).���`a
���`bax���aoa.���`faxline���`a(���`a(���bmia0���`a,���`a ���bmia0���`a)���`a,���`a ���`a(���bmia1���`a,���`a ���bmia1���`a)���`a,���`a ���`ecolor���aoa=���bs1a'���bs1ak���bs1a'���`a)���`a
���bc1xD# 50%-gray rectangle spanning the axes' width from y=0.25 to y=0.75.���`a
���`bax���aoa.���`gaxhspan���`a(���bmfd0.25���`a,���`a ���bmfd0.75���`a,���`a ���`ifacecolor���aoa=���bs1a'���bs1c0.5���bs1a'���`a)���`a
���bc1xB# Green rectangle spanning the axes' height from x=1.25 to x=1.55.���`a
���`bax���aoa.���`gaxvspan���`a(���bmfd1.25���`a,���`a ���bmfd1.55���`a,���`a ���`ifacecolor���aoa=���bs1a'���bs1g#2ca02c���bs1a'���`a)���`a
���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
`dNone�