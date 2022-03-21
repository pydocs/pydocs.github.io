��������n���bsdxo"""
===========
Broken Axis
===========

Broken axis example, where the y-axis will have a portion cut out.
"""���`a
���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���`a
���`bnp���aoa.���`frandom���aoa.���`dseed���`a(���bmih19680801���`a)���`a
���`a
���`cpts���`a ���aoa=���`a ���`bnp���aoa.���`frandom���aoa.���`drand���`a(���bmib30���`a)���aoa*���bmfb.2���`a
���bc1xG# Now let's make two outlier points which are far away from everything.���`a
���`cpts���`a[���`a[���bmia3���`a,���`a ���bmib14���`a]���`a]���`a ���aoa+���aoa=���`a ���bmfb.8���`a
���`a
���bc1xB# If we were to simply plot pts, we'd lose most of the interesting���`a
���bc1xG# details due to the outliers. So let's 'break' or 'cut-out' the y-axis���`a
���bc1xH# into two portions - use the top (ax1) for the outliers, and the bottom���`a
���bc1x3# (ax2) for the details of the majority of our data���`a
���`cfig���`a,���`a ���`a(���`cax1���`a,���`a ���`cax2���`a)���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���bmia2���`a,���`a ���bmia1���`a,���`a ���`fsharex���aoa=���bkcdTrue���`a)���`a
���`cfig���aoa.���`osubplots_adjust���`a(���`fhspace���aoa=���bmfd0.05���`a)���`b  ���bc1x# adjust space between axes���`a
���`a
���bc1x!# plot the same data on both axes���`a
���`cax1���aoa.���`dplot���`a(���`cpts���`a)���`a
���`cax2���aoa.���`dplot���`a(���`cpts���`a)���`a
���`a
���bc1x<# zoom-in / limit the view to different portions of the data���`a
���`cax1���aoa.���`hset_ylim���`a(���bmfc.78���`a,���`a ���bmfb1.���`a)���`b  ���bc1o# outliers only���`a
���`cax2���aoa.���`hset_ylim���`a(���bmia0���`a,���`a ���bmfc.22���`a)���`b  ���bc1r# most of the data���`a
���`a
���bc1x$# hide the spines between ax and ax2���`a
���`cax1���aoa.���`fspines���aoa.���`fbottom���aoa.���`kset_visible���`a(���bkceFalse���`a)���`a
���`cax2���aoa.���`fspines���aoa.���`ctop���aoa.���`kset_visible���`a(���bkceFalse���`a)���`a
���`cax1���aoa.���`exaxis���aoa.���`htick_top���`a(���`a)���`a
���`cax1���aoa.���`ktick_params���`a(���`hlabeltop���aoa=���bkceFalse���`a)���`b  ���bc1x"# don't put tick labels at the top���`a
���`cax2���aoa.���`exaxis���aoa.���`ktick_bottom���`a(���`a)���`a
���`a
���bc1x4# Now, let's turn towards the cut-out slanted lines.���`a
���bc1xD# We create line objects in axes coordinates, in which (0,0), (0,1),���`a
���bc1x4# (1,0), and (1,1) are the four corners of the axes.���`a
���bc1xL# The slanted lines themselves are markers at those locations, such that the���`a
���bc1xL# lines keep their angle and position, independent of the axes size or scale���`a
���bc1x'# Finally, we need to disable clipping.���`a
���`a
���`ad���`a ���aoa=���`a ���bmfb.5���`b  ���bc1xA# proportion of vertical to horizontal extent of the slanted line���`a
���`fkwargs���`a ���aoa=���`a ���bnbddict���`a(���`fmarker���aoa=���`a[���`a(���aoa-���bmia1���`a,���`a ���aoa-���`ad���`a)���`a,���`a ���`a(���bmia1���`a,���`a ���`ad���`a)���`a]���`a,���`a ���`jmarkersize���aoa=���bmib12���`a,���`a
���`n              ���`ilinestyle���aoa=���bs2a"���bs2dnone���bs2a"���`a,���`a ���`ecolor���aoa=���bs1a'���bs1ak���bs1a'���`a,���`a ���`cmec���aoa=���bs1a'���bs1ak���bs1a'���`a,���`a ���`cmew���aoa=���bmia1���`a,���`a ���`gclip_on���aoa=���bkceFalse���`a)���`a
���`cax1���aoa.���`dplot���`a(���`a[���bmia0���`a,���`a ���bmia1���`a]���`a,���`a ���`a[���bmia0���`a,���`a ���bmia0���`a]���`a,���`a ���`itransform���aoa=���`cax1���aoa.���`itransAxes���`a,���`a ���aoa*���aoa*���`fkwargs���`a)���`a
���`cax2���aoa.���`dplot���`a(���`a[���bmia0���`a,���`a ���bmia1���`a]���`a,���`a ���`a[���bmia1���`a,���`a ���bmia1���`a]���`a,���`a ���`itransform���aoa=���`cax2���aoa.���`itransAxes���`a,���`a ���aoa*���aoa*���`fkwargs���`a)���`a
���`a
���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
`dNone�