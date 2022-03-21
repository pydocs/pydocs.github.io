��������e���bsdyk"""
===============
Hinton diagrams
===============

Hinton diagrams are useful for visualizing the values of a 2D array (e.g.
a weight matrix): Positive and negative values are represented by white and
black squares, respectively, and the size of each square represents the
magnitude of each value.

Initial idea from David Warde-Farley on the SciPy Cookbook
"""���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���`a
���`a
���akcdef���`a ���bnffhinton���`a(���`fmatrix���`a,���`a ���`jmax_weight���aoa=���bkcdNone���`a,���`a ���`bax���aoa=���bkcdNone���`a)���`a:���`a
���`d    ���bsdx:"""Draw Hinton diagram for visualizing a weight matrix."""���`a
���`d    ���`bax���`a ���aoa=���`a ���`bax���`a ���akbif���`a ���`bax���`a ���bowbis���`a ���bowcnot���`a ���bkcdNone���`a ���akdelse���`a ���`cplt���aoa.���`cgca���`a(���`a)���`a
���`a
���`d    ���akbif���`a ���bowcnot���`a ���`jmax_weight���`a:���`a
���`h        ���`jmax_weight���`a ���aoa=���`a ���bmia2���`a ���aoa*���aoa*���`a ���`bnp���aoa.���`dceil���`a(���`bnp���aoa.���`dlog2���`a(���`bnp���aoa.���`cabs���`a(���`fmatrix���`a)���aoa.���`cmax���`a(���`a)���`a)���`a)���`a
���`a
���`d    ���`bax���aoa.���`epatch���aoa.���`mset_facecolor���`a(���bs1a'���bs1dgray���bs1a'���`a)���`a
���`d    ���`bax���aoa.���`jset_aspect���`a(���bs1a'���bs1eequal���bs1a'���`a,���`a ���bs1a'���bs1cbox���bs1a'���`a)���`a
���`d    ���`bax���aoa.���`exaxis���aoa.���`qset_major_locator���`a(���`cplt���aoa.���`kNullLocator���`a(���`a)���`a)���`a
���`d    ���`bax���aoa.���`eyaxis���aoa.���`qset_major_locator���`a(���`cplt���aoa.���`kNullLocator���`a(���`a)���`a)���`a
���`a
���`d    ���akcfor���`a ���`a(���`ax���`a,���`a ���`ay���`a)���`a,���`a ���`aw���`a ���bowbin���`a ���`bnp���aoa.���`kndenumerate���`a(���`fmatrix���`a)���`a:���`a
���`h        ���`ecolor���`a ���aoa=���`a ���bs1a'���bs1ewhite���bs1a'���`a ���akbif���`a ���`aw���`a ���aoa>���`a ���bmia0���`a ���akdelse���`a ���bs1a'���bs1eblack���bs1a'���`a
���`h        ���`dsize���`a ���aoa=���`a ���`bnp���aoa.���`dsqrt���`a(���bnbcabs���`a(���`aw���`a)���`a ���aoa/���`a ���`jmax_weight���`a)���`a
���`h        ���`drect���`a ���aoa=���`a ���`cplt���aoa.���`iRectangle���`a(���`a[���`ax���`a ���aoa-���`a ���`dsize���`a ���aoa/���`a ���bmia2���`a,���`a ���`ay���`a ���aoa-���`a ���`dsize���`a ���aoa/���`a ���bmia2���`a]���`a,���`a ���`dsize���`a,���`a ���`dsize���`a,���`a
���`x                             ���`ifacecolor���aoa=���`ecolor���`a,���`a ���`iedgecolor���aoa=���`ecolor���`a)���`a
���`h        ���`bax���aoa.���`iadd_patch���`a(���`drect���`a)���`a
���`a
���`d    ���`bax���aoa.���`nautoscale_view���`a(���`a)���`a
���`d    ���`bax���aoa.���`linvert_yaxis���`a(���`a)���`a
���`a
���`a
���akbif���`a ���bvmh__name__���`a ���aob==���`a ���bs1a'���bs1h__main__���bs1a'���`a:���`a
���`d    ���bc1x)# Fixing random state for reproducibility���`a
���`d    ���`bnp���aoa.���`frandom���aoa.���`dseed���`a(���bmih19680801���`a)���`a
���`a
���`d    ���`fhinton���`a(���`bnp���aoa.���`frandom���aoa.���`drand���`a(���bmib20���`a,���`a ���bmib20���`a)���`a ���aoa-���`a ���bmfc0.5���`a)���`a
���`d    ���`cplt���aoa.���`dshow���`a(���`a)���`a
`dNone�