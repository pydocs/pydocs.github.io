������������bsdx�"""
===============
Marker examples
===============

Example with different ways to specify markers.

For a list of all markers see also the `matplotlib.markers` documentation.
"""���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���`a
���bc1x)# Fixing random state for reproducibility���`a
���`bnp���aoa.���`frandom���aoa.���`dseed���`a(���bmih19680801���`a)���`a
���`a
���`ax���`a ���aoa=���`a ���`bnp���aoa.���`frandom���aoa.���`drand���`a(���bmib10���`a)���`a
���`ay���`a ���aoa=���`a ���`bnp���aoa.���`frandom���aoa.���`drand���`a(���bmib10���`a)���`a
���`az���`a ���aoa=���`a ���`bnp���aoa.���`dsqrt���`a(���`ax���aoa*���aoa*���bmia2���`a ���aoa+���`a ���`ay���aoa*���aoa*���bmia2���`a)���`a
���`a
���`cfig���`a,���`a ���`caxs���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���bmia2���`a,���`a ���bmia3���`a,���`a ���`fsharex���aoa=���bkcdTrue���`a,���`a ���`fsharey���aoa=���bkcdTrue���`a)���`a
���`a
���bc1o# marker symbol���`a
���`caxs���`a[���bmia0���`a,���`a ���bmia0���`a]���aoa.���`gscatter���`a(���`ax���`a,���`a ���`ay���`a,���`a ���`as���aoa=���bmib80���`a,���`a ���`ac���aoa=���`az���`a,���`a ���`fmarker���aoa=���bs2a"���bs2a>���bs2a"���`a)���`a
���`caxs���`a[���bmia0���`a,���`a ���bmia0���`a]���aoa.���`iset_title���`a(���bs2a"���bs2gmarker=���bs2a'���bs2a>���bs2a'���bs2a"���`a)���`a
���`a
���bc1q# marker from TeX���`a
���`caxs���`a[���bmia0���`a,���`a ���bmia1���`a]���aoa.���`gscatter���`a(���`ax���`a,���`a ���`ay���`a,���`a ���`as���aoa=���bmib80���`a,���`a ���`ac���aoa=���`az���`a,���`a ���`fmarker���aoa=���bsaar���bs1a'���bs1a$���bs1a\���bs1falpha$���bs1a'���`a)���`a
���`caxs���`a[���bmia0���`a,���`a ���bmia1���`a]���aoa.���`iset_title���`a(���bsaar���bs2a"���bs2hmarker=r���bs2a'���bs2a\���bs2a$���bs2a\���bs2ealpha���bs2a\���bs2a$���bs2a'���bs2a"���`a)���`a
���`a
���bc1r# marker from path���`a
���`everts���`a ���aoa=���`a ���`a[���`a[���aoa-���bmia1���`a,���`a ���aoa-���bmia1���`a]���`a,���`a ���`a[���bmia1���`a,���`a ���aoa-���bmia1���`a]���`a,���`a ���`a[���bmia1���`a,���`a ���bmia1���`a]���`a,���`a ���`a[���aoa-���bmia1���`a,���`a ���aoa-���bmia1���`a]���`a]���`a
���`caxs���`a[���bmia0���`a,���`a ���bmia2���`a]���aoa.���`gscatter���`a(���`ax���`a,���`a ���`ay���`a,���`a ���`as���aoa=���bmib80���`a,���`a ���`ac���aoa=���`az���`a,���`a ���`fmarker���aoa=���`everts���`a)���`a
���`caxs���`a[���bmia0���`a,���`a ���bmia2���`a]���aoa.���`iset_title���`a(���bs2a"���bs2lmarker=verts���bs2a"���`a)���`a
���`a
���bc1x# regular polygon marker���`a
���`caxs���`a[���bmia1���`a,���`a ���bmia0���`a]���aoa.���`gscatter���`a(���`ax���`a,���`a ���`ay���`a,���`a ���`as���aoa=���bmib80���`a,���`a ���`ac���aoa=���`az���`a,���`a ���`fmarker���aoa=���`a(���bmia5���`a,���`a ���bmia0���`a)���`a)���`a
���`caxs���`a[���bmia1���`a,���`a ���bmia0���`a]���aoa.���`iset_title���`a(���bs2a"���bs2mmarker=(5, 0)���bs2a"���`a)���`a
���`a
���bc1u# regular star marker���`a
���`caxs���`a[���bmia1���`a,���`a ���bmia1���`a]���aoa.���`gscatter���`a(���`ax���`a,���`a ���`ay���`a,���`a ���`as���aoa=���bmib80���`a,���`a ���`ac���aoa=���`az���`a,���`a ���`fmarker���aoa=���`a(���bmia5���`a,���`a ���bmia1���`a)���`a)���`a
���`caxs���`a[���bmia1���`a,���`a ���bmia1���`a]���aoa.���`iset_title���`a(���bs2a"���bs2mmarker=(5, 1)���bs2a"���`a)���`a
���`a
���bc1x# regular asterisk marker���`a
���`caxs���`a[���bmia1���`a,���`a ���bmia2���`a]���aoa.���`gscatter���`a(���`ax���`a,���`a ���`ay���`a,���`a ���`as���aoa=���bmib80���`a,���`a ���`ac���aoa=���`az���`a,���`a ���`fmarker���aoa=���`a(���bmia5���`a,���`a ���bmia2���`a)���`a)���`a
���`caxs���`a[���bmia1���`a,���`a ���bmia2���`a]���aoa.���`iset_title���`a(���bs2a"���bs2mmarker=(5, 2)���bs2a"���`a)���`a
���`a
���`cplt���aoa.���`ltight_layout���`a(���`a)���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
`dNone�