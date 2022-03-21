������������bsdx�"""
=================
Nested pie charts
=================

The following examples show two ways to build a nested pie chart
in Matplotlib. Such charts are often referred to as donut charts.

"""���`a
���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���`a
���bc1xO###############################################################################���`a
���bc1xA# The most straightforward way to build a pie chart is to use the���`a
���bc1x%# `~matplotlib.axes.Axes.pie` method.���`a
���bc1a#���`a
���bc1xD# In this case, pie takes values corresponding to counts in a group.���`a
���bc1xE# We'll first generate some fake data, corresponding to three groups.���`a
���bc1xB# In the inner circle, we'll treat each number as belonging to its���`a
���bc1xE# own group. In the outer circle, we'll plot them as members of their���`a
���bc1t# original 3 groups.���`a
���bc1a#���`a
���bc1xE# The effect of the donut shape is achieved by setting a ``width`` to���`a
���bc1x5# the pie's wedges through the *wedgeprops* argument.���`a
���`a
���`a
���`cfig���`a,���`a ���`bax���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`a)���`a
���`a
���`dsize���`a ���aoa=���`a ���bmfc0.3���`a
���`dvals���`a ���aoa=���`a ���`bnp���aoa.���`earray���`a(���`a[���`a[���bmfc60.���`a,���`a ���bmfc32.���`a]���`a,���`a ���`a[���bmfc37.���`a,���`a ���bmfc40.���`a]���`a,���`a ���`a[���bmfc29.���`a,���`a ���bmfc10.���`a]���`a]���`a)���`a
���`a
���`dcmap���`a ���aoa=���`a ���`cplt���aoa.���`icolormaps���`a[���bs2a"���bs2ftab20c���bs2a"���`a]���`a
���`louter_colors���`a ���aoa=���`a ���`dcmap���`a(���`bnp���aoa.���`farange���`a(���bmia3���`a)���aoa*���bmia4���`a)���`a
���`linner_colors���`a ���aoa=���`a ���`dcmap���`a(���`a[���bmia1���`a,���`a ���bmia2���`a,���`a ���bmia5���`a,���`a ���bmia6���`a,���`a ���bmia9���`a,���`a ���bmib10���`a]���`a)���`a
���`a
���`bax���aoa.���`cpie���`a(���`dvals���aoa.���`csum���`a(���`daxis���aoa=���bmia1���`a)���`a,���`a ���`fradius���aoa=���bmia1���`a,���`a ���`fcolors���aoa=���`louter_colors���`a,���`a
���`g       ���`jwedgeprops���aoa=���bnbddict���`a(���`ewidth���aoa=���`dsize���`a,���`a ���`iedgecolor���aoa=���bs1a'���bs1aw���bs1a'���`a)���`a)���`a
���`a
���`bax���aoa.���`cpie���`a(���`dvals���aoa.���`gflatten���`a(���`a)���`a,���`a ���`fradius���aoa=���bmia1���aoa-���`dsize���`a,���`a ���`fcolors���aoa=���`linner_colors���`a,���`a
���`g       ���`jwedgeprops���aoa=���bnbddict���`a(���`ewidth���aoa=���`dsize���`a,���`a ���`iedgecolor���aoa=���bs1a'���bs1aw���bs1a'���`a)���`a)���`a
���`a
���`bax���aoa.���`cset���`a(���`faspect���aoa=���bs2a"���bs2eequal���bs2a"���`a,���`a ���`etitle���aoa=���bs1a'���bs1vPie plot with `ax.pie`���bs1a'���`a)���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
���`a
���bc1xO###############################################################################���`a
���bc1xD# However, you can accomplish the same output by using a bar plot on���`a
���bc1xH# axes with a polar coordinate system. This may give more flexibility on���`a
���bc1x# the exact design of the plot.���`a
���bc1a#���`a
���bc1xH# In this case, we need to map x-values of the bar chart onto radians of���`a
���bc1xB# a circle. The cumulative sum of the values are used as the edges���`a
���bc1n# of the bars.���`a
���`a
���`cfig���`a,���`a ���`bax���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`jsubplot_kw���aoa=���bnbddict���`a(���`jprojection���aoa=���bs2a"���bs2epolar���bs2a"���`a)���`a)���`a
���`a
���`dsize���`a ���aoa=���`a ���bmfc0.3���`a
���`dvals���`a ���aoa=���`a ���`bnp���aoa.���`earray���`a(���`a[���`a[���bmfc60.���`a,���`a ���bmfc32.���`a]���`a,���`a ���`a[���bmfc37.���`a,���`a ���bmfc40.���`a]���`a,���`a ���`a[���bmfc29.���`a,���`a ���bmfc10.���`a]���`a]���`a)���`a
���bc1x# Normalize vals to 2 pi���`a
���`hvalsnorm���`a ���aoa=���`a ���`dvals���aoa/���`bnp���aoa.���`csum���`a(���`dvals���`a)���aoa*���bmia2���aoa*���`bnp���aoa.���`bpi���`a
���bc1x'# Obtain the ordinates of the bar edges���`a
���`hvalsleft���`a ���aoa=���`a ���`bnp���aoa.���`fcumsum���`a(���`bnp���aoa.���`fappend���`a(���bmia0���`a,���`a ���`hvalsnorm���aoa.���`gflatten���`a(���`a)���`a[���`a:���aoa-���bmia1���`a]���`a)���`a)���aoa.���`greshape���`a(���`dvals���aoa.���`eshape���`a)���`a
���`a
���`dcmap���`a ���aoa=���`a ���`cplt���aoa.���`icolormaps���`a[���bs2a"���bs2ftab20c���bs2a"���`a]���`a
���`louter_colors���`a ���aoa=���`a ���`dcmap���`a(���`bnp���aoa.���`farange���`a(���bmia3���`a)���aoa*���bmia4���`a)���`a
���`linner_colors���`a ���aoa=���`a ���`dcmap���`a(���`a[���bmia1���`a,���`a ���bmia2���`a,���`a ���bmia5���`a,���`a ���bmia6���`a,���`a ���bmia9���`a,���`a ���bmib10���`a]���`a)���`a
���`a
���`bax���aoa.���`cbar���`a(���`ax���aoa=���`hvalsleft���`a[���`a:���`a,���`a ���bmia0���`a]���`a,���`a
���`g       ���`ewidth���aoa=���`hvalsnorm���aoa.���`csum���`a(���`daxis���aoa=���bmia1���`a)���`a,���`a ���`fbottom���aoa=���bmia1���aoa-���`dsize���`a,���`a ���`fheight���aoa=���`dsize���`a,���`a
���`g       ���`ecolor���aoa=���`louter_colors���`a,���`a ���`iedgecolor���aoa=���bs1a'���bs1aw���bs1a'���`a,���`a ���`ilinewidth���aoa=���bmia1���`a,���`a ���`ealign���aoa=���bs2a"���bs2dedge���bs2a"���`a)���`a
���`a
���`bax���aoa.���`cbar���`a(���`ax���aoa=���`hvalsleft���aoa.���`gflatten���`a(���`a)���`a,���`a
���`g       ���`ewidth���aoa=���`hvalsnorm���aoa.���`gflatten���`a(���`a)���`a,���`a ���`fbottom���aoa=���bmia1���aoa-���bmia2���aoa*���`dsize���`a,���`a ���`fheight���aoa=���`dsize���`a,���`a
���`g       ���`ecolor���aoa=���`linner_colors���`a,���`a ���`iedgecolor���aoa=���bs1a'���bs1aw���bs1a'���`a,���`a ���`ilinewidth���aoa=���bmia1���`a,���`a ���`ealign���aoa=���bs2a"���bs2dedge���bs2a"���`a)���`a
���`a
���`bax���aoa.���`cset���`a(���`etitle���aoa=���bs2a"���bs2x,Pie plot with `ax.bar` and polar coordinates���bs2a"���`a)���`a
���`bax���aoa.���`lset_axis_off���`a(���`a)���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
���`a
���bc1xM#############################################################################���`a
���bc1a#���`a
���bc1x# .. admonition:: References���`a
���bc1a#���`a
���bc1xN#    The use of the following functions, methods, classes and modules is shown���`a
���bc1u#    in this example:���`a
���bc1a#���`a
���bc1x;#    - `matplotlib.axes.Axes.pie` / `matplotlib.pyplot.pie`���`a
���bc1x;#    - `matplotlib.axes.Axes.bar` / `matplotlib.pyplot.bar`���`a
���bc1x%#    - `matplotlib.projections.polar`���`a
���bc1x4#    - ``Axes.set`` (`matplotlib.artist.Artist.set`)���`a
���bc1x*#    - `matplotlib.axes.Axes.set_axis_off`���`a
`dNone�