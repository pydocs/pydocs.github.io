��������i���bsdx�"""
=======================
Plot 2D data on 3D plot
=======================

Demonstrates using ax.plot's zdir keyword to plot 2D data on
selective axes of a 3D plot.
"""���`a
���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���`a
���`bax���`a ���aoa=���`a ���`cplt���aoa.���`ffigure���`a(���`a)���aoa.���`kadd_subplot���`a(���`jprojection���aoa=���bs1a'���bs1b3d���bs1a'���`a)���`a
���`a
���bc1x*# Plot a sin curve using the x and y axes.���`a
���`ax���`a ���aoa=���`a ���`bnp���aoa.���`hlinspace���`a(���bmia0���`a,���`a ���bmia1���`a,���`a ���bmic100���`a)���`a
���`ay���`a ���aoa=���`a ���`bnp���aoa.���`csin���`a(���`ax���`a ���aoa*���`a ���bmia2���`a ���aoa*���`a ���`bnp���aoa.���`bpi���`a)���`a ���aoa/���`a ���bmia2���`a ���aoa+���`a ���bmfc0.5���`a
���`bax���aoa.���`dplot���`a(���`ax���`a,���`a ���`ay���`a,���`a ���`bzs���aoa=���bmia0���`a,���`a ���`dzdir���aoa=���bs1a'���bs1az���bs1a'���`a,���`a ���`elabel���aoa=���bs1a'���bs1ocurve in (x, y)���bs1a'���`a)���`a
���`a
���bc1xF# Plot scatterplot data (20 2D points per colour) on the x and z axes.���`a
���`fcolors���`a ���aoa=���`a ���`a(���bs1a'���bs1ar���bs1a'���`a,���`a ���bs1a'���bs1ag���bs1a'���`a,���`a ���bs1a'���bs1ab���bs1a'���`a,���`a ���bs1a'���bs1ak���bs1a'���`a)���`a
���`a
���bc1x)# Fixing random state for reproducibility���`a
���`bnp���aoa.���`frandom���aoa.���`dseed���`a(���bmih19680801���`a)���`a
���`a
���`ax���`a ���aoa=���`a ���`bnp���aoa.���`frandom���aoa.���`fsample���`a(���bmib20���`a ���aoa*���`a ���bnbclen���`a(���`fcolors���`a)���`a)���`a
���`ay���`a ���aoa=���`a ���`bnp���aoa.���`frandom���aoa.���`fsample���`a(���bmib20���`a ���aoa*���`a ���bnbclen���`a(���`fcolors���`a)���`a)���`a
���`fc_list���`a ���aoa=���`a ���`a[���`a]���`a
���akcfor���`a ���`ac���`a ���bowbin���`a ���`fcolors���`a:���`a
���`d    ���`fc_list���aoa.���`fextend���`a(���`a[���`ac���`a]���`a ���aoa*���`a ���bmib20���`a)���`a
���bc1xK# By using zdir='y', the y value of these points is fixed to the zs value 0���`a
���bc1x8# and the (x, y) points are plotted on the x and z axes.���`a
���`bax���aoa.���`gscatter���`a(���`ax���`a,���`a ���`ay���`a,���`a ���`bzs���aoa=���bmia0���`a,���`a ���`dzdir���aoa=���bs1a'���bs1ay���bs1a'���`a,���`a ���`ac���aoa=���`fc_list���`a,���`a ���`elabel���aoa=���bs1a'���bs1ppoints in (x, z)���bs1a'���`a)���`a
���`a
���bc1x)# Make legend, set axes limits and labels���`a
���`bax���aoa.���`flegend���`a(���`a)���`a
���`bax���aoa.���`hset_xlim���`a(���bmia0���`a,���`a ���bmia1���`a)���`a
���`bax���aoa.���`hset_ylim���`a(���bmia0���`a,���`a ���bmia1���`a)���`a
���`bax���aoa.���`hset_zlim���`a(���bmia0���`a,���`a ���bmia1���`a)���`a
���`bax���aoa.���`jset_xlabel���`a(���bs1a'���bs1aX���bs1a'���`a)���`a
���`bax���aoa.���`jset_ylabel���`a(���bs1a'���bs1aY���bs1a'���`a)���`a
���`bax���aoa.���`jset_zlabel���`a(���bs1a'���bs1aZ���bs1a'���`a)���`a
���`a
���bc1xL# Customize the view angle so it's easier to see that the scatter points lie���`a
���bc1r# on the plane y=0���`a
���`bax���aoa.���`iview_init���`a(���`delev���aoa=���bmfc20.���`a,���`a ���`dazim���aoa=���aoa-���bmib35���`a)���`a
���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
`dNone�