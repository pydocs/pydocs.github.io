�����������bsdy�"""
==========================
Creating adjacent subplots
==========================

To create plots that share a common axis (visually) you can set the hspace
between the subplots to zero. Passing sharex=True when creating the subplots
will automatically turn off all x ticks and labels except those on the bottom
axis.

In this example the plots share a common x axis but you can follow the same
logic to supply a common y axis.
"""���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���`a
���`at���`a ���aoa=���`a ���`bnp���aoa.���`farange���`a(���bmfc0.0���`a,���`a ���bmfc2.0���`a,���`a ���bmfd0.01���`a)���`a
���`a
���`bs1���`a ���aoa=���`a ���`bnp���aoa.���`csin���`a(���bmia2���`a ���aoa*���`a ���`bnp���aoa.���`bpi���`a ���aoa*���`a ���`at���`a)���`a
���`bs2���`a ���aoa=���`a ���`bnp���aoa.���`cexp���`a(���aoa-���`at���`a)���`a
���`bs3���`a ���aoa=���`a ���`bs1���`a ���aoa*���`a ���`bs2���`a
���`a
���`cfig���`a,���`a ���`caxs���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���bmia3���`a,���`a ���bmia1���`a,���`a ���`fsharex���aoa=���bkcdTrue���`a)���`a
���bc1x&# Remove horizontal space between axes���`a
���`cfig���aoa.���`osubplots_adjust���`a(���`fhspace���aoa=���bmia0���`a)���`a
���`a
���bc1x5# Plot each graph, and manually set the y tick values���`a
���`caxs���`a[���bmia0���`a]���aoa.���`dplot���`a(���`at���`a,���`a ���`bs1���`a)���`a
���`caxs���`a[���bmia0���`a]���aoa.���`jset_yticks���`a(���`bnp���aoa.���`farange���`a(���aoa-���bmfc0.9���`a,���`a ���bmfc1.0���`a,���`a ���bmfc0.4���`a)���`a)���`a
���`caxs���`a[���bmia0���`a]���aoa.���`hset_ylim���`a(���aoa-���bmia1���`a,���`a ���bmia1���`a)���`a
���`a
���`caxs���`a[���bmia1���`a]���aoa.���`dplot���`a(���`at���`a,���`a ���`bs2���`a)���`a
���`caxs���`a[���bmia1���`a]���aoa.���`jset_yticks���`a(���`bnp���aoa.���`farange���`a(���bmfc0.1���`a,���`a ���bmfc1.0���`a,���`a ���bmfc0.2���`a)���`a)���`a
���`caxs���`a[���bmia1���`a]���aoa.���`hset_ylim���`a(���bmia0���`a,���`a ���bmia1���`a)���`a
���`a
���`caxs���`a[���bmia2���`a]���aoa.���`dplot���`a(���`at���`a,���`a ���`bs3���`a)���`a
���`caxs���`a[���bmia2���`a]���aoa.���`jset_yticks���`a(���`bnp���aoa.���`farange���`a(���aoa-���bmfc0.9���`a,���`a ���bmfc1.0���`a,���`a ���bmfc0.4���`a)���`a)���`a
���`caxs���`a[���bmia2���`a]���aoa.���`hset_ylim���`a(���aoa-���bmia1���`a,���`a ���bmia1���`a)���`a
���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
`dNone�