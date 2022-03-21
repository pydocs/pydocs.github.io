��������'���bsdxu"""
==============
Scatter Masked
==============

Mask some data points and add a line demarking
masked regions.

"""���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���`a
���bc1x)# Fixing random state for reproducibility���`a
���`bnp���aoa.���`frandom���aoa.���`dseed���`a(���bmih19680801���`a)���`a
���`a
���`a
���`aN���`a ���aoa=���`a ���bmic100���`a
���`br0���`a ���aoa=���`a ���bmfc0.6���`a
���`ax���`a ���aoa=���`a ���bmfc0.9���`a ���aoa*���`a ���`bnp���aoa.���`frandom���aoa.���`drand���`a(���`aN���`a)���`a
���`ay���`a ���aoa=���`a ���bmfc0.9���`a ���aoa*���`a ���`bnp���aoa.���`frandom���aoa.���`drand���`a(���`aN���`a)���`a
���`darea���`a ���aoa=���`a ���`a(���bmib20���`a ���aoa*���`a ���`bnp���aoa.���`frandom���aoa.���`drand���`a(���`aN���`a)���`a)���aoa*���aoa*���bmia2���`b  ���bc1u# 0 to 10 point radii���`a
���`ac���`a ���aoa=���`a ���`bnp���aoa.���`dsqrt���`a(���`darea���`a)���`a
���`ar���`a ���aoa=���`a ���`bnp���aoa.���`dsqrt���`a(���`ax���`a ���aoa*���aoa*���`a ���bmia2���`a ���aoa+���`a ���`ay���`a ���aoa*���aoa*���`a ���bmia2���`a)���`a
���`earea1���`a ���aoa=���`a ���`bnp���aoa.���`bma���aoa.���`lmasked_where���`a(���`ar���`a ���aoa<���`a ���`br0���`a,���`a ���`darea���`a)���`a
���`earea2���`a ���aoa=���`a ���`bnp���aoa.���`bma���aoa.���`lmasked_where���`a(���`ar���`a ���aoa>���aoa=���`a ���`br0���`a,���`a ���`darea���`a)���`a
���`cplt���aoa.���`gscatter���`a(���`ax���`a,���`a ���`ay���`a,���`a ���`as���aoa=���`earea1���`a,���`a ���`fmarker���aoa=���bs1a'���bs1a^���bs1a'���`a,���`a ���`ac���aoa=���`ac���`a)���`a
���`cplt���aoa.���`gscatter���`a(���`ax���`a,���`a ���`ay���`a,���`a ���`as���aoa=���`earea2���`a,���`a ���`fmarker���aoa=���bs1a'���bs1ao���bs1a'���`a,���`a ���`ac���aoa=���`ac���`a)���`a
���bc1x(# Show the boundary between the regions:���`a
���`etheta���`a ���aoa=���`a ���`bnp���aoa.���`farange���`a(���bmia0���`a,���`a ���`bnp���aoa.���`bpi���`a ���aoa/���`a ���bmia2���`a,���`a ���bmfd0.01���`a)���`a
���`cplt���aoa.���`dplot���`a(���`br0���`a ���aoa*���`a ���`bnp���aoa.���`ccos���`a(���`etheta���`a)���`a,���`a ���`br0���`a ���aoa*���`a ���`bnp���aoa.���`csin���`a(���`etheta���`a)���`a)���`a
���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
`dNone�