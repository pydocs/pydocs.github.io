������������bsaar���bsdxv"""
================
Nested GridSpecs
================

This example demonstrates the use of nested `.GridSpec`\s.
"""���`a
���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���`a
���`a
���akcdef���`a ���bnfksquiggle_xy���`a(���`aa���`a,���`a ���`ab���`a,���`a ���`ac���`a,���`a ���`ad���`a)���`a:���`a
���`d    ���`ai���`a ���aoa=���`a ���`bnp���aoa.���`farange���`a(���bmfc0.0���`a,���`a ���bmia2���aoa*���`bnp���aoa.���`bpi���`a,���`a ���bmfd0.05���`a)���`a
���`d    ���akfreturn���`a ���`bnp���aoa.���`csin���`a(���`ai���aoa*���`aa���`a)���aoa*���`bnp���aoa.���`ccos���`a(���`ai���aoa*���`ab���`a)���`a,���`a ���`bnp���aoa.���`csin���`a(���`ai���aoa*���`ac���`a)���aoa*���`bnp���aoa.���`ccos���`a(���`ai���aoa*���`ad���`a)���`a
���`a
���`a
���`cfig���`a ���aoa=���`a ���`cplt���aoa.���`ffigure���`a(���`gfigsize���aoa=���`a(���bmia8���`a,���`a ���bmia8���`a)���`a)���`a
���`jouter_grid���`a ���aoa=���`a ���`cfig���aoa.���`ladd_gridspec���`a(���bmia4���`a,���`a ���bmia4���`a,���`a ���`fwspace���aoa=���bmia0���`a,���`a ���`fhspace���aoa=���bmia0���`a)���`a
���`a
���akcfor���`a ���`aa���`a ���bowbin���`a ���bnberange���`a(���bmia4���`a)���`a:���`a
���`d    ���akcfor���`a ���`ab���`a ���bowbin���`a ���bnberange���`a(���bmia4���`a)���`a:���`a
���`h        ���bc1x# gridspec inside gridspec���`a
���`h        ���`jinner_grid���`a ���aoa=���`a ���`jouter_grid���`a[���`aa���`a,���`a ���`ab���`a]���aoa.���`ksubgridspec���`a(���bmia3���`a,���`a ���bmia3���`a,���`a ���`fwspace���aoa=���bmia0���`a,���`a ���`fhspace���aoa=���bmia0���`a)���`a
���`h        ���`caxs���`a ���aoa=���`a ���`jinner_grid���aoa.���`hsubplots���`a(���`a)���`b  ���bc1x)# Create all subplots for the inner grid.���`a
���`h        ���akcfor���`a ���`a(���`ac���`a,���`a ���`ad���`a)���`a,���`a ���`bax���`a ���bowbin���`a ���`bnp���aoa.���`kndenumerate���`a(���`caxs���`a)���`a:���`a
���`l            ���`bax���aoa.���`dplot���`a(���aoa*���`ksquiggle_xy���`a(���`aa���`a ���aoa+���`a ���bmia1���`a,���`a ���`ab���`a ���aoa+���`a ���bmia1���`a,���`a ���`ac���`a ���aoa+���`a ���bmia1���`a,���`a ���`ad���`a ���aoa+���`a ���bmia1���`a)���`a)���`a
���`l            ���`bax���aoa.���`cset���`a(���`fxticks���aoa=���`a[���`a]���`a,���`a ���`fyticks���aoa=���`a[���`a]���`a)���`a
���`a
���bc1x# show only the outside spines���`a
���akcfor���`a ���`bax���`a ���bowbin���`a ���`cfig���aoa.���`hget_axes���`a(���`a)���`a:���`a
���`d    ���`bss���`a ���aoa=���`a ���`bax���aoa.���`oget_subplotspec���`a(���`a)���`a
���`d    ���`bax���aoa.���`fspines���aoa.���`ctop���aoa.���`kset_visible���`a(���`bss���aoa.���`lis_first_row���`a(���`a)���`a)���`a
���`d    ���`bax���aoa.���`fspines���aoa.���`fbottom���aoa.���`kset_visible���`a(���`bss���aoa.���`kis_last_row���`a(���`a)���`a)���`a
���`d    ���`bax���aoa.���`fspines���aoa.���`dleft���aoa.���`kset_visible���`a(���`bss���aoa.���`lis_first_col���`a(���`a)���`a)���`a
���`d    ���`bax���aoa.���`fspines���aoa.���`eright���aoa.���`kset_visible���`a(���`bss���aoa.���`kis_last_col���`a(���`a)���`a)���`a
���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
`dNone�