��������}���bsdx�"""
=======================
Equal axis aspect ratio
=======================

How to set and adjust plots with equal axis aspect ratios.
"""���`a
���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���`a
���bc1x# Plot circle of radius 3.���`a
���`a
���`ban���`a ���aoa=���`a ���`bnp���aoa.���`hlinspace���`a(���bmia0���`a,���`a ���bmia2���`a ���aoa*���`a ���`bnp���aoa.���`bpi���`a,���`a ���bmic100���`a)���`a
���`cfig���`a,���`a ���`caxs���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���bmia2���`a,���`a ���bmia2���`a)���`a
���`a
���`caxs���`a[���bmia0���`a,���`a ���bmia0���`a]���aoa.���`dplot���`a(���bmia3���`a ���aoa*���`a ���`bnp���aoa.���`ccos���`a(���`ban���`a)���`a,���`a ���bmia3���`a ���aoa*���`a ���`bnp���aoa.���`csin���`a(���`ban���`a)���`a)���`a
���`caxs���`a[���bmia0���`a,���`a ���bmia0���`a]���aoa.���`iset_title���`a(���bs1a'���bs1xnot equal, looks like ellipse���bs1a'���`a,���`a ���`hfontsize���aoa=���bmib10���`a)���`a
���`a
���`caxs���`a[���bmia0���`a,���`a ���bmia1���`a]���aoa.���`dplot���`a(���bmia3���`a ���aoa*���`a ���`bnp���aoa.���`ccos���`a(���`ban���`a)���`a,���`a ���bmia3���`a ���aoa*���`a ���`bnp���aoa.���`csin���`a(���`ban���`a)���`a)���`a
���`caxs���`a[���bmia0���`a,���`a ���bmia1���`a]���aoa.���`daxis���`a(���bs1a'���bs1eequal���bs1a'���`a)���`a
���`caxs���`a[���bmia0���`a,���`a ���bmia1���`a]���aoa.���`iset_title���`a(���bs1a'���bs1xequal, looks like circle���bs1a'���`a,���`a ���`hfontsize���aoa=���bmib10���`a)���`a
���`a
���`caxs���`a[���bmia1���`a,���`a ���bmia0���`a]���aoa.���`dplot���`a(���bmia3���`a ���aoa*���`a ���`bnp���aoa.���`ccos���`a(���`ban���`a)���`a,���`a ���bmia3���`a ���aoa*���`a ���`bnp���aoa.���`csin���`a(���`ban���`a)���`a)���`a
���`caxs���`a[���bmia1���`a,���`a ���bmia0���`a]���aoa.���`daxis���`a(���bs1a'���bs1eequal���bs1a'���`a)���`a
���`caxs���`a[���bmia1���`a,���`a ���bmia0���`a]���aoa.���`cset���`a(���`dxlim���aoa=���`a(���aoa-���bmia3���`a,���`a ���bmia3���`a)���`a,���`a ���`dylim���aoa=���`a(���aoa-���bmia3���`a,���`a ���bmia3���`a)���`a)���`a
���`caxs���`a[���bmia1���`a,���`a ���bmia0���`a]���aoa.���`iset_title���`a(���bs1a'���bs1x*still a circle, even after changing limits���bs1a'���`a,���`a ���`hfontsize���aoa=���bmib10���`a)���`a
���`a
���`caxs���`a[���bmia1���`a,���`a ���bmia1���`a]���aoa.���`dplot���`a(���bmia3���`a ���aoa*���`a ���`bnp���aoa.���`ccos���`a(���`ban���`a)���`a,���`a ���bmia3���`a ���aoa*���`a ���`bnp���aoa.���`csin���`a(���`ban���`a)���`a)���`a
���`caxs���`a[���bmia1���`a,���`a ���bmia1���`a]���aoa.���`jset_aspect���`a(���bs1a'���bs1eequal���bs1a'���`a,���`a ���bs1a'���bs1cbox���bs1a'���`a)���`a
���`caxs���`a[���bmia1���`a,���`a ���bmia1���`a]���aoa.���`iset_title���`a(���bs1a'���bs1x)still a circle, auto-adjusted data limits���bs1a'���`a,���`a ���`hfontsize���aoa=���bmib10���`a)���`a
���`a
���`cfig���aoa.���`ltight_layout���`a(���`a)���`a
���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
`dNone�