�����������bsdxa"""
==============
3D scatterplot
==============

Demonstration of a basic scatterplot in 3D.
"""���`a
���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���`a
���bc1x)# Fixing random state for reproducibility���`a
���`bnp���aoa.���`frandom���aoa.���`dseed���`a(���bmih19680801���`a)���`a
���`a
���`a
���akcdef���`a ���bnfirandrange���`a(���`an���`a,���`a ���`dvmin���`a,���`a ���`dvmax���`a)���`a:���`a
���`d    ���bsdx�"""
    Helper function to make an array of random numbers having shape (n, )
    with each number distributed Uniform(vmin, vmax).
    """���`a
���`d    ���akfreturn���`a ���`a(���`dvmax���`a ���aoa-���`a ���`dvmin���`a)���aoa*���`bnp���aoa.���`frandom���aoa.���`drand���`a(���`an���`a)���`a ���aoa+���`a ���`dvmin���`a
���`a
���`cfig���`a ���aoa=���`a ���`cplt���aoa.���`ffigure���`a(���`a)���`a
���`bax���`a ���aoa=���`a ���`cfig���aoa.���`kadd_subplot���`a(���`jprojection���aoa=���bs1a'���bs1b3d���bs1a'���`a)���`a
���`a
���`an���`a ���aoa=���`a ���bmic100���`a
���`a
���bc1xK# For each set of style and range settings, plot n random points in the box���`a
���bc1x># defined by x in [23, 32], y in [0, 100], z in [zlow, zhigh].���`a
���akcfor���`a ���`am���`a,���`a ���`dzlow���`a,���`a ���`ezhigh���`a ���bowbin���`a ���`a[���`a(���bs1a'���bs1ao���bs1a'���`a,���`a ���aoa-���bmib50���`a,���`a ���aoa-���bmib25���`a)���`a,���`a ���`a(���bs1a'���bs1a^���bs1a'���`a,���`a ���aoa-���bmib30���`a,���`a ���aoa-���bmia5���`a)���`a]���`a:���`a
���`d    ���`bxs���`a ���aoa=���`a ���`irandrange���`a(���`an���`a,���`a ���bmib23���`a,���`a ���bmib32���`a)���`a
���`d    ���`bys���`a ���aoa=���`a ���`irandrange���`a(���`an���`a,���`a ���bmia0���`a,���`a ���bmic100���`a)���`a
���`d    ���`bzs���`a ���aoa=���`a ���`irandrange���`a(���`an���`a,���`a ���`dzlow���`a,���`a ���`ezhigh���`a)���`a
���`d    ���`bax���aoa.���`gscatter���`a(���`bxs���`a,���`a ���`bys���`a,���`a ���`bzs���`a,���`a ���`fmarker���aoa=���`am���`a)���`a
���`a
���`bax���aoa.���`jset_xlabel���`a(���bs1a'���bs1gX Label���bs1a'���`a)���`a
���`bax���aoa.���`jset_ylabel���`a(���bs1a'���bs1gY Label���bs1a'���`a)���`a
���`bax���aoa.���`jset_zlabel���`a(���bs1a'���bs1gZ Label���bs1a'���`a)���`a
���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
`dNone�