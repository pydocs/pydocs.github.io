������������bsdx�"""
========================
3D surface (solid color)
========================

Demonstrates a very basic plot of a 3D surface using a solid color.
"""���`a
���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���`a
���`a
���`cfig���`a ���aoa=���`a ���`cplt���aoa.���`ffigure���`a(���`a)���`a
���`bax���`a ���aoa=���`a ���`cfig���aoa.���`kadd_subplot���`a(���`jprojection���aoa=���bs1a'���bs1b3d���bs1a'���`a)���`a
���`a
���bc1k# Make data���`a
���`au���`a ���aoa=���`a ���`bnp���aoa.���`hlinspace���`a(���bmia0���`a,���`a ���bmia2���`a ���aoa*���`a ���`bnp���aoa.���`bpi���`a,���`a ���bmic100���`a)���`a
���`av���`a ���aoa=���`a ���`bnp���aoa.���`hlinspace���`a(���bmia0���`a,���`a ���`bnp���aoa.���`bpi���`a,���`a ���bmic100���`a)���`a
���`ax���`a ���aoa=���`a ���bmib10���`a ���aoa*���`a ���`bnp���aoa.���`eouter���`a(���`bnp���aoa.���`ccos���`a(���`au���`a)���`a,���`a ���`bnp���aoa.���`csin���`a(���`av���`a)���`a)���`a
���`ay���`a ���aoa=���`a ���bmib10���`a ���aoa*���`a ���`bnp���aoa.���`eouter���`a(���`bnp���aoa.���`csin���`a(���`au���`a)���`a,���`a ���`bnp���aoa.���`csin���`a(���`av���`a)���`a)���`a
���`az���`a ���aoa=���`a ���bmib10���`a ���aoa*���`a ���`bnp���aoa.���`eouter���`a(���`bnp���aoa.���`dones���`a(���`bnp���aoa.���`dsize���`a(���`au���`a)���`a)���`a,���`a ���`bnp���aoa.���`ccos���`a(���`av���`a)���`a)���`a
���`a
���bc1r# Plot the surface���`a
���`bax���aoa.���`lplot_surface���`a(���`ax���`a,���`a ���`ay���`a,���`a ���`az���`a)���`a
���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
`dNone�