��������Q���bsdyY"""
==========
Bar of pie
==========

Make a "bar of pie" chart where the first slice of the pie is
"exploded" into a bar chart with a further breakdown of said slice's
characteristics. The example demonstrates using a figure with multiple
sets of axes and using the axes patches list to add two ConnectionPatches
to link the subplot charts.
"""���`a
���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���bkndfrom���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnngpatches���`a ���bknfimport���`a ���`oConnectionPatch���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���`a
���bc1x%# make figure and assign axis objects���`a
���`cfig���`a,���`a ���`a(���`cax1���`a,���`a ���`cax2���`a)���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���bmia1���`a,���`a ���bmia2���`a,���`a ���`gfigsize���aoa=���`a(���bmia9���`a,���`a ���bmia5���`a)���`a)���`a
���`cfig���aoa.���`osubplots_adjust���`a(���`fwspace���aoa=���bmia0���`a)���`a
���`a
���bc1v# pie chart parameters���`a
���`fratios���`a ���aoa=���`a ���`a[���bmfc.27���`a,���`a ���bmfc.56���`a,���`a ���bmfc.17���`a]���`a
���`flabels���`a ���aoa=���`a ���`a[���bs1a'���bs1gApprove���bs1a'���`a,���`a ���bs1a'���bs1jDisapprove���bs1a'���`a,���`a ���bs1a'���bs1iUndecided���bs1a'���`a]���`a
���`gexplode���`a ���aoa=���`a ���`a[���bmfc0.1���`a,���`a ���bmia0���`a,���`a ���bmia0���`a]���`a
���bc1x3# rotate so that first wedge is split by the x-axis���`a
���`eangle���`a ���aoa=���`a ���aoa-���bmic180���`a ���aoa*���`a ���`fratios���`a[���bmia0���`a]���`a
���`cax1���aoa.���`cpie���`a(���`fratios���`a,���`a ���`gautopct���aoa=���bs1a'���bsie%1.1f���bsib%%���bs1a'���`a,���`a ���`jstartangle���aoa=���`eangle���`a,���`a
���`h        ���`flabels���aoa=���`flabels���`a,���`a ���`gexplode���aoa=���`gexplode���`a)���`a
���`a
���bc1v# bar chart parameters���`a
���`a
���`dxpos���`a ���aoa=���`a ���bmia0���`a
���`fbottom���`a ���aoa=���`a ���bmia0���`a
���`fratios���`a ���aoa=���`a ���`a[���bmfc.33���`a,���`a ���bmfc.54���`a,���`a ���bmfc.07���`a,���`a ���bmfc.06���`a]���`a
���`ewidth���`a ���aoa=���`a ���bmfb.2���`a
���`fcolors���`a ���aoa=���`a ���`a[���`a[���bmfb.1���`a,���`a ���bmfb.3���`a,���`a ���bmfb.5���`a]���`a,���`a ���`a[���bmfb.1���`a,���`a ���bmfb.3���`a,���`a ���bmfb.3���`a]���`a,���`a ���`a[���bmfb.1���`a,���`a ���bmfb.3���`a,���`a ���bmfb.7���`a]���`a,���`a ���`a[���bmfb.1���`a,���`a ���bmfb.3���`a,���`a ���bmfb.9���`a]���`a]���`a
���`a
���akcfor���`a ���`aj���`a ���bowbin���`a ���bnberange���`a(���bnbclen���`a(���`fratios���`a)���`a)���`a:���`a
���`d    ���`fheight���`a ���aoa=���`a ���`fratios���`a[���`aj���`a]���`a
���`d    ���`cax2���aoa.���`cbar���`a(���`dxpos���`a,���`a ���`fheight���`a,���`a ���`ewidth���`a,���`a ���`fbottom���aoa=���`fbottom���`a,���`a ���`ecolor���aoa=���`fcolors���`a[���`aj���`a]���`a)���`a
���`d    ���`dypos���`a ���aoa=���`a ���`fbottom���`a ���aoa+���`a ���`cax2���aoa.���`gpatches���`a[���`aj���`a]���aoa.���`jget_height���`a(���`a)���`a ���aoa/���`a ���bmia2���`a
���`d    ���`fbottom���`a ���aoa+���aoa=���`a ���`fheight���`a
���`d    ���`cax2���aoa.���`dtext���`a(���`dxpos���`a,���`a ���`dypos���`a,���`a ���bs2a"���bsib%d���bsib%%���bs2a"���`a ���aoa%���`a ���`a(���`cax2���aoa.���`gpatches���`a[���`aj���`a]���aoa.���`jget_height���`a(���`a)���`a ���aoa*���`a ���bmic100���`a)���`a,���`a
���`m             ���`bha���aoa=���bs1a'���bs1fcenter���bs1a'���`a)���`a
���`a
���`cax2���aoa.���`iset_title���`a(���bs1a'���bs1pAge of approvers���bs1a'���`a)���`a
���`cax2���aoa.���`flegend���`a(���`a(���bs1a'���bs1e50-65���bs1a'���`a,���`a ���bs1a'���bs1gOver 65���bs1a'���`a,���`a ���bs1a'���bs1e35-49���bs1a'���`a,���`a ���bs1a'���bs1hUnder 35���bs1a'���`a)���`a)���`a
���`cax2���aoa.���`daxis���`a(���bs1a'���bs1coff���bs1a'���`a)���`a
���`cax2���aoa.���`hset_xlim���`a(���aoa-���`a ���bmfc2.5���`a ���aoa*���`a ���`ewidth���`a,���`a ���bmfc2.5���`a ���aoa*���`a ���`ewidth���`a)���`a
���`a
���bc1x9# use ConnectionPatch to draw lines between the two plots���`a
���bc1t# get the wedge data���`a
���`ftheta1���`a,���`a ���`ftheta2���`a ���aoa=���`a ���`cax1���aoa.���`gpatches���`a[���bmia0���`a]���aoa.���`ftheta1���`a,���`a ���`cax1���aoa.���`gpatches���`a[���bmia0���`a]���aoa.���`ftheta2���`a
���`fcenter���`a,���`a ���`ar���`a ���aoa=���`a ���`cax1���aoa.���`gpatches���`a[���bmia0���`a]���aoa.���`fcenter���`a,���`a ���`cax1���aoa.���`gpatches���`a[���bmia0���`a]���aoa.���`ar���`a
���`jbar_height���`a ���aoa=���`a ���bnbcsum���`a(���`a[���`ditem���aoa.���`jget_height���`a(���`a)���`a ���akcfor���`a ���`ditem���`a ���bowbin���`a ���`cax2���aoa.���`gpatches���`a]���`a)���`a
���`a
���bc1x# draw top connecting line���`a
���`ax���`a ���aoa=���`a ���`ar���`a ���aoa*���`a ���`bnp���aoa.���`ccos���`a(���`bnp���aoa.���`bpi���`a ���aoa/���`a ���bmic180���`a ���aoa*���`a ���`ftheta2���`a)���`a ���aoa+���`a ���`fcenter���`a[���bmia0���`a]���`a
���`ay���`a ���aoa=���`a ���`ar���`a ���aoa*���`a ���`bnp���aoa.���`csin���`a(���`bnp���aoa.���`bpi���`a ���aoa/���`a ���bmic180���`a ���aoa*���`a ���`ftheta2���`a)���`a ���aoa+���`a ���`fcenter���`a[���bmia1���`a]���`a
���`ccon���`a ���aoa=���`a ���`oConnectionPatch���`a(���`cxyA���aoa=���`a(���aoa-���`ewidth���`a ���aoa/���`a ���bmia2���`a,���`a ���`jbar_height���`a)���`a,���`a ���`gcoordsA���aoa=���`cax2���aoa.���`itransData���`a,���`a
���`v                      ���`cxyB���aoa=���`a(���`ax���`a,���`a ���`ay���`a)���`a,���`a ���`gcoordsB���aoa=���`cax1���aoa.���`itransData���`a)���`a
���`ccon���aoa.���`iset_color���`a(���`a[���bmia0���`a,���`a ���bmia0���`a,���`a ���bmia0���`a]���`a)���`a
���`ccon���aoa.���`mset_linewidth���`a(���bmia4���`a)���`a
���`cax2���aoa.���`jadd_artist���`a(���`ccon���`a)���`a
���`a
���bc1x# draw bottom connecting line���`a
���`ax���`a ���aoa=���`a ���`ar���`a ���aoa*���`a ���`bnp���aoa.���`ccos���`a(���`bnp���aoa.���`bpi���`a ���aoa/���`a ���bmic180���`a ���aoa*���`a ���`ftheta1���`a)���`a ���aoa+���`a ���`fcenter���`a[���bmia0���`a]���`a
���`ay���`a ���aoa=���`a ���`ar���`a ���aoa*���`a ���`bnp���aoa.���`csin���`a(���`bnp���aoa.���`bpi���`a ���aoa/���`a ���bmic180���`a ���aoa*���`a ���`ftheta1���`a)���`a ���aoa+���`a ���`fcenter���`a[���bmia1���`a]���`a
���`ccon���`a ���aoa=���`a ���`oConnectionPatch���`a(���`cxyA���aoa=���`a(���aoa-���`ewidth���`a ���aoa/���`a ���bmia2���`a,���`a ���bmia0���`a)���`a,���`a ���`gcoordsA���aoa=���`cax2���aoa.���`itransData���`a,���`a
���`v                      ���`cxyB���aoa=���`a(���`ax���`a,���`a ���`ay���`a)���`a,���`a ���`gcoordsB���aoa=���`cax1���aoa.���`itransData���`a)���`a
���`ccon���aoa.���`iset_color���`a(���`a[���bmia0���`a,���`a ���bmia0���`a,���`a ���bmia0���`a]���`a)���`a
���`cax2���aoa.���`jadd_artist���`a(���`ccon���`a)���`a
���`ccon���aoa.���`mset_linewidth���`a(���bmia4���`a)���`a
���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
���`a
���bc1xM#############################################################################���`a
���bc1a#���`a
���bc1x# .. admonition:: References���`a
���bc1a#���`a
���bc1xN#    The use of the following functions, methods, classes and modules is shown���`a
���bc1u#    in this example:���`a
���bc1a#���`a
���bc1x;#    - `matplotlib.axes.Axes.bar` / `matplotlib.pyplot.bar`���`a
���bc1x;#    - `matplotlib.axes.Axes.pie` / `matplotlib.pyplot.pie`���`a
���bc1x+#    - `matplotlib.patches.ConnectionPatch`���`a
`dNone�