�����������bsdxu"""
============
3D errorbars
============

An example of using errorbars with upper and lower limits in mplot3d.
"""���`a
���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���`a
���`bax���`a ���aoa=���`a ���`cplt���aoa.���`ffigure���`a(���`a)���aoa.���`kadd_subplot���`a(���`jprojection���aoa=���bs1a'���bs1b3d���bs1a'���`a)���`a
���`a
���bc1x# setting up a parametric curve���`a
���`at���`a ���aoa=���`a ���`bnp���aoa.���`farange���`a(���bmia0���`a,���`a ���bmia2���aoa*���`bnp���aoa.���`bpi���aoa+���bmfb.1���`a,���`a ���bmfd0.01���`a)���`a
���`ax���`a,���`a ���`ay���`a,���`a ���`az���`a ���aoa=���`a ���`bnp���aoa.���`csin���`a(���`at���`a)���`a,���`a ���`bnp���aoa.���`ccos���`a(���bmia3���aoa*���`at���`a)���`a,���`a ���`bnp���aoa.���`csin���`a(���bmia5���aoa*���`at���`a)���`a
���`a
���`eestep���`a ���aoa=���`a ���bmib15���`a
���`ai���`a ���aoa=���`a ���`bnp���aoa.���`farange���`a(���`at���aoa.���`dsize���`a)���`a
���`gzuplims���`a ���aoa=���`a ���`a(���`ai���`a ���aoa%���`a ���`eestep���`a ���aob==���`a ���bmia0���`a)���`a ���aoa&���`a ���`a(���`ai���`a ���aoa/���aoa/���`a ���`eestep���`a ���aoa%���`a ���bmia3���`a ���aob==���`a ���bmia0���`a)���`a
���`gzlolims���`a ���aoa=���`a ���`a(���`ai���`a ���aoa%���`a ���`eestep���`a ���aob==���`a ���bmia0���`a)���`a ���aoa&���`a ���`a(���`ai���`a ���aoa/���aoa/���`a ���`eestep���`a ���aoa%���`a ���bmia3���`a ���aob==���`a ���bmia2���`a)���`a
���`a
���`bax���aoa.���`herrorbar���`a(���`ax���`a,���`a ���`ay���`a,���`a ���`az���`a,���`a ���bmfc0.2���`a,���`a ���`gzuplims���aoa=���`gzuplims���`a,���`a ���`gzlolims���aoa=���`gzlolims���`a,���`a ���`jerrorevery���aoa=���`eestep���`a)���`a
���`a
���`bax���aoa.���`jset_xlabel���`a(���bs2a"���bs2gX label���bs2a"���`a)���`a
���`bax���aoa.���`jset_ylabel���`a(���bs2a"���bs2gY label���bs2a"���`a)���`a
���`bax���aoa.���`jset_zlabel���`a(���bs2a"���bs2gZ label���bs2a"���`a)���`a
���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
`dNone�