��������,���bsdx�"""
==================
Figure legend demo
==================

Instead of plotting a legend on each axis, a legend for all the artists on all
the sub-axes of a figure can be plotted instead.
"""���`a
���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���`a
���`cfig���`a,���`a ���`caxs���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���bmia1���`a,���`a ���bmia2���`a)���`a
���`a
���`ax���`a ���aoa=���`a ���`bnp���aoa.���`farange���`a(���bmfc0.0���`a,���`a ���bmfc2.0���`a,���`a ���bmfd0.02���`a)���`a
���`by1���`a ���aoa=���`a ���`bnp���aoa.���`csin���`a(���bmia2���`a ���aoa*���`a ���`bnp���aoa.���`bpi���`a ���aoa*���`a ���`ax���`a)���`a
���`by2���`a ���aoa=���`a ���`bnp���aoa.���`cexp���`a(���aoa-���`ax���`a)���`a
���`bl1���`a,���`a ���aoa=���`a ���`caxs���`a[���bmia0���`a]���aoa.���`dplot���`a(���`ax���`a,���`a ���`by1���`a)���`a
���`bl2���`a,���`a ���aoa=���`a ���`caxs���`a[���bmia0���`a]���aoa.���`dplot���`a(���`ax���`a,���`a ���`by2���`a,���`a ���`fmarker���aoa=���bs1a'���bs1ao���bs1a'���`a)���`a
���`a
���`by3���`a ���aoa=���`a ���`bnp���aoa.���`csin���`a(���bmia4���`a ���aoa*���`a ���`bnp���aoa.���`bpi���`a ���aoa*���`a ���`ax���`a)���`a
���`by4���`a ���aoa=���`a ���`bnp���aoa.���`cexp���`a(���aoa-���bmia2���`a ���aoa*���`a ���`ax���`a)���`a
���`bl3���`a,���`a ���aoa=���`a ���`caxs���`a[���bmia1���`a]���aoa.���`dplot���`a(���`ax���`a,���`a ���`by3���`a,���`a ���`ecolor���aoa=���bs1a'���bs1itab:green���bs1a'���`a)���`a
���`bl4���`a,���`a ���aoa=���`a ���`caxs���`a[���bmia1���`a]���aoa.���`dplot���`a(���`ax���`a,���`a ���`by4���`a,���`a ���`ecolor���aoa=���bs1a'���bs1gtab:red���bs1a'���`a,���`a ���`fmarker���aoa=���bs1a'���bs1a^���bs1a'���`a)���`a
���`a
���`cfig���aoa.���`flegend���`a(���`a(���`bl1���`a,���`a ���`bl2���`a)���`a,���`a ���`a(���bs1a'���bs1fLine 1���bs1a'���`a,���`a ���bs1a'���bs1fLine 2���bs1a'���`a)���`a,���`a ���bs1a'���bs1jupper left���bs1a'���`a)���`a
���`cfig���aoa.���`flegend���`a(���`a(���`bl3���`a,���`a ���`bl4���`a)���`a,���`a ���`a(���bs1a'���bs1fLine 3���bs1a'���`a,���`a ���bs1a'���bs1fLine 4���bs1a'���`a)���`a,���`a ���bs1a'���bs1kupper right���bs1a'���`a)���`a
���`a
���`cplt���aoa.���`ltight_layout���`a(���`a)���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
`dNone�