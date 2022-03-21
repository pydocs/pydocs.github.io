ŸØÇÅŸ¥ÉôÇŸ±Çbsdx¬"""
=================
Nested pie charts
=================

The following examples show two ways to build a nested pie chart
in Matplotlib. Such charts are often referred to as donut charts.

"""Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±ÇbknfimportŸ±Ç`a Ÿ±ÇbnnŸ¢ÑjmatplotlibŸ†Ñjmatplotlibe3.5.1fmodulejmatplotlibfmoduleıŸ±Çbnna.Ÿ±ÇbnnfpyplotŸ±Ç`a Ÿ±ÇakbasŸ±Ç`a Ÿ±ÇbnncpltŸ±Ç`a
Ÿ±ÇbknfimportŸ±Ç`a Ÿ±ÇbnnŸ¢ÑenumpyŸ†Ñenumpyf1.22.3fmoduleenumpyfmoduleıŸ±Ç`a Ÿ±ÇakbasŸ±Ç`a Ÿ±ÇbnnbnpŸ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1xO###############################################################################Ÿ±Ç`a
Ÿ±Çbc1xA# The most straightforward way to build a pie chart is to use theŸ±Ç`a
Ÿ±Çbc1x%# `~matplotlib.axes.Axes.pie` method.Ÿ±Ç`a
Ÿ±Çbc1a#Ÿ±Ç`a
Ÿ±Çbc1xD# In this case, pie takes values corresponding to counts in a group.Ÿ±Ç`a
Ÿ±Çbc1xE# We'll first generate some fake data, corresponding to three groups.Ÿ±Ç`a
Ÿ±Çbc1xB# In the inner circle, we'll treat each number as belonging to itsŸ±Ç`a
Ÿ±Çbc1xE# own group. In the outer circle, we'll plot them as members of theirŸ±Ç`a
Ÿ±Çbc1t# original 3 groups.Ÿ±Ç`a
Ÿ±Çbc1a#Ÿ±Ç`a
Ÿ±Çbc1xE# The effect of the donut shape is achieved by setting a ``width`` toŸ±Ç`a
Ÿ±Çbc1x5# the pie's wedges through the *wedgeprops* argument.Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`cfigŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`baxŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`hsubplotsŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`dsizeŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Çbmfc0.3Ÿ±Ç`a
Ÿ±Ç`dvalsŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`earrayŸ±Ç`a(Ÿ±Ç`a[Ÿ±Ç`a[Ÿ±Çbmfc60.Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfc32.Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`a[Ÿ±Çbmfc37.Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfc40.Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`a[Ÿ±Çbmfc29.Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfc10.Ÿ±Ç`a]Ÿ±Ç`a]Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`dcmapŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`icolormapsŸ±Ç`a[Ÿ±Çbs2a"Ÿ±Çbs2ftab20cŸ±Çbs2a"Ÿ±Ç`a]Ÿ±Ç`a
Ÿ±Ç`louter_colorsŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`dcmapŸ±Ç`a(Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`farangeŸ±Ç`a(Ÿ±Çbmia3Ÿ±Ç`a)Ÿ±Çaoa*Ÿ±Çbmia4Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`linner_colorsŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`dcmapŸ±Ç`a(Ÿ±Ç`a[Ÿ±Çbmia1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia2Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia5Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia6Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia9Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmib10Ÿ±Ç`a]Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`cpieŸ±Ç`a(Ÿ±Ç`dvalsŸ±Çaoa.Ÿ±Ç`csumŸ±Ç`a(Ÿ±Ç`daxisŸ±Çaoa=Ÿ±Çbmia1Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`fradiusŸ±Çaoa=Ÿ±Çbmia1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`fcolorsŸ±Çaoa=Ÿ±Ç`louter_colorsŸ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`g       Ÿ±Ç`jwedgepropsŸ±Çaoa=Ÿ±ÇbnbddictŸ±Ç`a(Ÿ±Ç`ewidthŸ±Çaoa=Ÿ±Ç`dsizeŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`iedgecolorŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1awŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`cpieŸ±Ç`a(Ÿ±Ç`dvalsŸ±Çaoa.Ÿ±Ç`gflattenŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`fradiusŸ±Çaoa=Ÿ±Çbmia1Ÿ±Çaoa-Ÿ±Ç`dsizeŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`fcolorsŸ±Çaoa=Ÿ±Ç`linner_colorsŸ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`g       Ÿ±Ç`jwedgepropsŸ±Çaoa=Ÿ±ÇbnbddictŸ±Ç`a(Ÿ±Ç`ewidthŸ±Çaoa=Ÿ±Ç`dsizeŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`iedgecolorŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1awŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`csetŸ±Ç`a(Ÿ±Ç`faspectŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2eequalŸ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`etitleŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1vPie plot with `ax.pie`Ÿ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`dshowŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1xO###############################################################################Ÿ±Ç`a
Ÿ±Çbc1xD# However, you can accomplish the same output by using a bar plot onŸ±Ç`a
Ÿ±Çbc1xH# axes with a polar coordinate system. This may give more flexibility onŸ±Ç`a
Ÿ±Çbc1x# the exact design of the plot.Ÿ±Ç`a
Ÿ±Çbc1a#Ÿ±Ç`a
Ÿ±Çbc1xH# In this case, we need to map x-values of the bar chart onto radians ofŸ±Ç`a
Ÿ±Çbc1xB# a circle. The cumulative sum of the values are used as the edgesŸ±Ç`a
Ÿ±Çbc1n# of the bars.Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`cfigŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`baxŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`hsubplotsŸ±Ç`a(Ÿ±Ç`jsubplot_kwŸ±Çaoa=Ÿ±ÇbnbddictŸ±Ç`a(Ÿ±Ç`jprojectionŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2epolarŸ±Çbs2a"Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`dsizeŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Çbmfc0.3Ÿ±Ç`a
Ÿ±Ç`dvalsŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`earrayŸ±Ç`a(Ÿ±Ç`a[Ÿ±Ç`a[Ÿ±Çbmfc60.Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfc32.Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`a[Ÿ±Çbmfc37.Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfc40.Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`a[Ÿ±Çbmfc29.Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfc10.Ÿ±Ç`a]Ÿ±Ç`a]Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Çbc1x# Normalize vals to 2 piŸ±Ç`a
Ÿ±Ç`hvalsnormŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`dvalsŸ±Çaoa/Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`csumŸ±Ç`a(Ÿ±Ç`dvalsŸ±Ç`a)Ÿ±Çaoa*Ÿ±Çbmia2Ÿ±Çaoa*Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`bpiŸ±Ç`a
Ÿ±Çbc1x'# Obtain the ordinates of the bar edgesŸ±Ç`a
Ÿ±Ç`hvalsleftŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`fcumsumŸ±Ç`a(Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`fappendŸ±Ç`a(Ÿ±Çbmia0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`hvalsnormŸ±Çaoa.Ÿ±Ç`gflattenŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a[Ÿ±Ç`a:Ÿ±Çaoa-Ÿ±Çbmia1Ÿ±Ç`a]Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Çaoa.Ÿ±Ç`greshapeŸ±Ç`a(Ÿ±Ç`dvalsŸ±Çaoa.Ÿ±Ç`eshapeŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`dcmapŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`icolormapsŸ±Ç`a[Ÿ±Çbs2a"Ÿ±Çbs2ftab20cŸ±Çbs2a"Ÿ±Ç`a]Ÿ±Ç`a
Ÿ±Ç`louter_colorsŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`dcmapŸ±Ç`a(Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`farangeŸ±Ç`a(Ÿ±Çbmia3Ÿ±Ç`a)Ÿ±Çaoa*Ÿ±Çbmia4Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`linner_colorsŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`dcmapŸ±Ç`a(Ÿ±Ç`a[Ÿ±Çbmia1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia2Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia5Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia6Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia9Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmib10Ÿ±Ç`a]Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`cbarŸ±Ç`a(Ÿ±Ç`axŸ±Çaoa=Ÿ±Ç`hvalsleftŸ±Ç`a[Ÿ±Ç`a:Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia0Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`g       Ÿ±Ç`ewidthŸ±Çaoa=Ÿ±Ç`hvalsnormŸ±Çaoa.Ÿ±Ç`csumŸ±Ç`a(Ÿ±Ç`daxisŸ±Çaoa=Ÿ±Çbmia1Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`fbottomŸ±Çaoa=Ÿ±Çbmia1Ÿ±Çaoa-Ÿ±Ç`dsizeŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`fheightŸ±Çaoa=Ÿ±Ç`dsizeŸ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`g       Ÿ±Ç`ecolorŸ±Çaoa=Ÿ±Ç`louter_colorsŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`iedgecolorŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1awŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ilinewidthŸ±Çaoa=Ÿ±Çbmia1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ealignŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2dedgeŸ±Çbs2a"Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`cbarŸ±Ç`a(Ÿ±Ç`axŸ±Çaoa=Ÿ±Ç`hvalsleftŸ±Çaoa.Ÿ±Ç`gflattenŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`g       Ÿ±Ç`ewidthŸ±Çaoa=Ÿ±Ç`hvalsnormŸ±Çaoa.Ÿ±Ç`gflattenŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`fbottomŸ±Çaoa=Ÿ±Çbmia1Ÿ±Çaoa-Ÿ±Çbmia2Ÿ±Çaoa*Ÿ±Ç`dsizeŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`fheightŸ±Çaoa=Ÿ±Ç`dsizeŸ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`g       Ÿ±Ç`ecolorŸ±Çaoa=Ÿ±Ç`linner_colorsŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`iedgecolorŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1awŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ilinewidthŸ±Çaoa=Ÿ±Çbmia1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ealignŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2dedgeŸ±Çbs2a"Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`csetŸ±Ç`a(Ÿ±Ç`etitleŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2x,Pie plot with `ax.bar` and polar coordinatesŸ±Çbs2a"Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`lset_axis_offŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`dshowŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1xM#############################################################################Ÿ±Ç`a
Ÿ±Çbc1a#Ÿ±Ç`a
Ÿ±Çbc1x# .. admonition:: ReferencesŸ±Ç`a
Ÿ±Çbc1a#Ÿ±Ç`a
Ÿ±Çbc1xN#    The use of the following functions, methods, classes and modules is shownŸ±Ç`a
Ÿ±Çbc1u#    in this example:Ÿ±Ç`a
Ÿ±Çbc1a#Ÿ±Ç`a
Ÿ±Çbc1x;#    - `matplotlib.axes.Axes.pie` / `matplotlib.pyplot.pie`Ÿ±Ç`a
Ÿ±Çbc1x;#    - `matplotlib.axes.Axes.bar` / `matplotlib.pyplot.bar`Ÿ±Ç`a
Ÿ±Çbc1x%#    - `matplotlib.projections.polar`Ÿ±Ç`a
Ÿ±Çbc1x4#    - ``Axes.set`` (`matplotlib.artist.Artist.set`)Ÿ±Ç`a
Ÿ±Çbc1x*#    - `matplotlib.axes.Axes.set_axis_off`Ÿ±Ç`a
`dNoneˆ