��������a���bsdxL"""
========
Log Demo
========

Examples of plots with logarithmic axes.
"""���`a
���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���`a
���bc1s# Data for plotting���`a
���`at���`a ���aoa=���`a ���`bnp���aoa.���`farange���`a(���bmfd0.01���`a,���`a ���bmfd20.0���`a,���`a ���bmfd0.01���`a)���`a
���`a
���bc1o# Create figure���`a
���`cfig���`a,���`a ���`a(���`a(���`cax1���`a,���`a ���`cax2���`a)���`a,���`a ���`a(���`cax3���`a,���`a ���`cax4���`a)���`a)���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���bmia2���`a,���`a ���bmia2���`a)���`a
���`a
���bc1l# log y axis���`a
���`cax1���aoa.���`hsemilogy���`a(���`at���`a,���`a ���`bnp���aoa.���`cexp���`a(���aoa-���`at���`a ���aoa/���`a ���bmfc5.0���`a)���`a)���`a
���`cax1���aoa.���`cset���`a(���`etitle���aoa=���bs1a'���bs1hsemilogy���bs1a'���`a)���`a
���`cax1���aoa.���`dgrid���`a(���`a)���`a
���`a
���bc1l# log x axis���`a
���`cax2���aoa.���`hsemilogx���`a(���`at���`a,���`a ���`bnp���aoa.���`csin���`a(���bmia2���`a ���aoa*���`a ���`bnp���aoa.���`bpi���`a ���aoa*���`a ���`at���`a)���`a)���`a
���`cax2���aoa.���`cset���`a(���`etitle���aoa=���bs1a'���bs1hsemilogx���bs1a'���`a)���`a
���`cax2���aoa.���`dgrid���`a(���`a)���`a
���`a
���bc1r# log x and y axis���`a
���`cax3���aoa.���`floglog���`a(���`at���`a,���`a ���bmib20���`a ���aoa*���`a ���`bnp���aoa.���`cexp���`a(���aoa-���`at���`a ���aoa/���`a ���bmfd10.0���`a)���`a)���`a
���`cax3���aoa.���`jset_xscale���`a(���bs1a'���bs1clog���bs1a'���`a,���`a ���`dbase���aoa=���bmia2���`a)���`a
���`cax3���aoa.���`cset���`a(���`etitle���aoa=���bs1a'���bs1rloglog base 2 on x���bs1a'���`a)���`a
���`cax3���aoa.���`dgrid���`a(���`a)���`a
���`a
���bc1x*# With errorbars: clip non-positive values���`a
���bc1x# Use new data for plotting���`a
���`ax���`a ���aoa=���`a ���bmfd10.0���aoa*���aoa*���`bnp���aoa.���`hlinspace���`a(���bmfc0.0���`a,���`a ���bmfc2.0���`a,���`a ���bmib20���`a)���`a
���`ay���`a ���aoa=���`a ���`ax���aoa*���aoa*���bmfc2.0���`a
���`a
���`cax4���aoa.���`jset_xscale���`a(���bs2a"���bs2clog���bs2a"���`a,���`a ���`knonpositive���aoa=���bs1a'���bs1dclip���bs1a'���`a)���`a
���`cax4���aoa.���`jset_yscale���`a(���bs2a"���bs2clog���bs2a"���`a,���`a ���`knonpositive���aoa=���bs1a'���bs1dclip���bs1a'���`a)���`a
���`cax4���aoa.���`cset���`a(���`etitle���aoa=���bs1a'���bs1uErrorbars go negative���bs1a'���`a)���`a
���`cax4���aoa.���`herrorbar���`a(���`ax���`a,���`a ���`ay���`a,���`a ���`dxerr���aoa=���bmfc0.1���`a ���aoa*���`a ���`ax���`a,���`a ���`dyerr���aoa=���bmfc5.0���`a ���aoa+���`a ���bmfd0.75���`a ���aoa*���`a ���`ay���`a)���`a
���bc1xG# ylim must be set after errorbar to allow errorbar to autoscale limits���`a
���`cax4���aoa.���`hset_ylim���`a(���`fbottom���aoa=���bmfc0.1���`a)���`a
���`a
���`cfig���aoa.���`ltight_layout���`a(���`a)���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
`dNone�