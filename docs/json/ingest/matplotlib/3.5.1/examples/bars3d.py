�����������bsdx�"""
========================================
Create 2D bar graphs in different planes
========================================

Demonstrates making a 3D plot which has 2D bar graphs projected onto
planes y=0, y=1, etc.
"""���`a
���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���`a
���bc1x)# Fixing random state for reproducibility���`a
���`bnp���aoa.���`frandom���aoa.���`dseed���`a(���bmih19680801���`a)���`a
���`a
���`a
���`cfig���`a ���aoa=���`a ���`cplt���aoa.���`ffigure���`a(���`a)���`a
���`bax���`a ���aoa=���`a ���`cfig���aoa.���`kadd_subplot���`a(���`jprojection���aoa=���bs1a'���bs1b3d���bs1a'���`a)���`a
���`a
���`fcolors���`a ���aoa=���`a ���`a[���bs1a'���bs1ar���bs1a'���`a,���`a ���bs1a'���bs1ag���bs1a'���`a,���`a ���bs1a'���bs1ab���bs1a'���`a,���`a ���bs1a'���bs1ay���bs1a'���`a]���`a
���`fyticks���`a ���aoa=���`a ���`a[���bmia3���`a,���`a ���bmia2���`a,���`a ���bmia1���`a,���`a ���bmia0���`a]���`a
���akcfor���`a ���`ac���`a,���`a ���`ak���`a ���bowbin���`a ���bnbczip���`a(���`fcolors���`a,���`a ���`fyticks���`a)���`a:���`a
���`d    ���bc1x/# Generate the random data for the y=k 'layer'.���`a
���`d    ���`bxs���`a ���aoa=���`a ���`bnp���aoa.���`farange���`a(���bmib20���`a)���`a
���`d    ���`bys���`a ���aoa=���`a ���`bnp���aoa.���`frandom���aoa.���`drand���`a(���bmib20���`a)���`a
���`a
���`d    ���bc1xK# You can provide either a single color or an array with the same length as���`a
���`d    ���bc1xJ# xs and ys. To demonstrate this, we color the first bar of each set cyan.���`a
���`d    ���`bcs���`a ���aoa=���`a ���`a[���`ac���`a]���`a ���aoa*���`a ���bnbclen���`a(���`bxs���`a)���`a
���`d    ���`bcs���`a[���bmia0���`a]���`a ���aoa=���`a ���bs1a'���bs1ac���bs1a'���`a
���`a
���`d    ���bc1xJ# Plot the bar graph given by xs and ys on the plane y=k with 80% opacity.���`a
���`d    ���`bax���aoa.���`cbar���`a(���`bxs���`a,���`a ���`bys���`a,���`a ���`bzs���aoa=���`ak���`a,���`a ���`dzdir���aoa=���bs1a'���bs1ay���bs1a'���`a,���`a ���`ecolor���aoa=���`bcs���`a,���`a ���`ealpha���aoa=���bmfc0.8���`a)���`a
���`a
���`bax���aoa.���`jset_xlabel���`a(���bs1a'���bs1aX���bs1a'���`a)���`a
���`bax���aoa.���`jset_ylabel���`a(���bs1a'���bs1aY���bs1a'���`a)���`a
���`bax���aoa.���`jset_zlabel���`a(���bs1a'���bs1aZ���bs1a'���`a)���`a
���`a
���bc1xK# On the y axis let's only label the discrete values that we have data for.���`a
���`bax���aoa.���`jset_yticks���`a(���`fyticks���`a)���`a
���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
`dNone�