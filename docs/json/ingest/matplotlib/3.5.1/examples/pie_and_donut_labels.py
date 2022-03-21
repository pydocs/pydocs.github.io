ŸØÇÅŸ¥ÉôMŸ±Çbsdy^"""
==========================
Labeling a pie and a donut
==========================

Welcome to the Matplotlib bakery. We will create a pie and a donut
chart through the `pie method <matplotlib.axes.Axes.pie>` and
show how to label them with a `legend <matplotlib.axes.Axes.legend>`
as well as with `annotations <matplotlib.axes.Axes.annotate>`.
"""Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1xO###############################################################################Ÿ±Ç`a
Ÿ±Çbc1xJ# As usual we would start by defining the imports and create a figure withŸ±Ç`a
Ÿ±Çbc1k# subplots.Ÿ±Ç`a
Ÿ±Çbc1xK# Now it's time for the pie. Starting with a pie recipe, we create the dataŸ±Ç`a
Ÿ±Çbc1x# and a list of labels from it.Ÿ±Ç`a
Ÿ±Çbc1a#Ÿ±Ç`a
Ÿ±Çbc1xJ# We can provide a function to the ``autopct`` argument, which will expandŸ±Ç`a
Ÿ±Çbc1xH# automatic percentage labeling by showing absolute values; we calculateŸ±Ç`a
Ÿ±Çbc1xE# the latter back from relative data and the known sum of all values.Ÿ±Ç`a
Ÿ±Çbc1a#Ÿ±Ç`a
Ÿ±Çbc1xM# We then create the pie and store the returned objects for later.  The firstŸ±Ç`a
Ÿ±Çbc1xL# returned element of the returned tuple is a list of the wedges.  Those areŸ±Ç`a
Ÿ±Çbc1xO# `matplotlib.patches.Wedge` patches, which can directly be used as the handlesŸ±Ç`a
Ÿ±Çbc1xO# for a legend. We can use the legend's ``bbox_to_anchor`` argument to positionŸ±Ç`a
Ÿ±Çbc1xO# the legend outside of the pie. Here we use the axes coordinates ``(1, 0, 0.5,Ÿ±Ç`a
Ÿ±Çbc1xJ# 1)`` together with the location ``"center left"``; i.e. the left centralŸ±Ç`a
Ÿ±Çbc1xL# point of the legend will be at the left central point of the bounding box,Ÿ±Ç`a
Ÿ±Çbc1x?# spanning from ``(1, 0)`` to ``(1.5, 1)`` in axes coordinates.Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±ÇbknfimportŸ±Ç`a Ÿ±ÇbnnŸ¢ÑenumpyŸ†Ñenumpyf1.22.3fmoduleenumpyfmoduleıŸ±Ç`a Ÿ±ÇakbasŸ±Ç`a Ÿ±ÇbnnbnpŸ±Ç`a
Ÿ±ÇbknfimportŸ±Ç`a Ÿ±ÇbnnŸ¢ÑjmatplotlibŸ†Ñjmatplotlibe3.5.1fmodulejmatplotlibfmoduleıŸ±Çbnna.Ÿ±ÇbnnfpyplotŸ±Ç`a Ÿ±ÇakbasŸ±Ç`a Ÿ±ÇbnncpltŸ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`cfigŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`baxŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`hsubplotsŸ±Ç`a(Ÿ±Ç`gfigsizeŸ±Çaoa=Ÿ±Ç`a(Ÿ±Çbmia6Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia3Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`jsubplot_kwŸ±Çaoa=Ÿ±ÇbnbddictŸ±Ç`a(Ÿ±Ç`faspectŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2eequalŸ±Çbs2a"Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`frecipeŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`a[Ÿ±Çbs2a"Ÿ±Çbs2k375 g flourŸ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`j          Ÿ±Çbs2a"Ÿ±Çbs2j75 g sugarŸ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`j          Ÿ±Çbs2a"Ÿ±Çbs2l250 g butterŸ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`j          Ÿ±Çbs2a"Ÿ±Çbs2m300 g berriesŸ±Çbs2a"Ÿ±Ç`a]Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`ddataŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`a[Ÿ±ÇbnbefloatŸ±Ç`a(Ÿ±Ç`axŸ±Çaoa.Ÿ±Ç`esplitŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a[Ÿ±Çbmia0Ÿ±Ç`a]Ÿ±Ç`a)Ÿ±Ç`a Ÿ±ÇakcforŸ±Ç`a Ÿ±Ç`axŸ±Ç`a Ÿ±ÇbowbinŸ±Ç`a Ÿ±Ç`frecipeŸ±Ç`a]Ÿ±Ç`a
Ÿ±Ç`kingredientsŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`a[Ÿ±Ç`axŸ±Çaoa.Ÿ±Ç`esplitŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a[Ÿ±Çaoa-Ÿ±Çbmia1Ÿ±Ç`a]Ÿ±Ç`a Ÿ±ÇakcforŸ±Ç`a Ÿ±Ç`axŸ±Ç`a Ÿ±ÇbowbinŸ±Ç`a Ÿ±Ç`frecipeŸ±Ç`a]Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±ÇakcdefŸ±Ç`a Ÿ±ÇbnfdfuncŸ±Ç`a(Ÿ±Ç`cpctŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`gallvalsŸ±Ç`a)Ÿ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`habsoluteŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±ÇbnbcintŸ±Ç`a(Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`eroundŸ±Ç`a(Ÿ±Ç`cpctŸ±Çaoa/Ÿ±Çbmfd100.Ÿ±Çaoa*Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`csumŸ±Ç`a(Ÿ±Ç`gallvalsŸ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±ÇakfreturnŸ±Ç`a Ÿ±Çbs2a"Ÿ±Çbsif{:.1f}Ÿ±Çbs2a%Ÿ±Çbseb\nŸ±Çbs2a(Ÿ±Çbsid{:d}Ÿ±Çbs2c g)Ÿ±Çbs2a"Ÿ±Çaoa.Ÿ±Ç`fformatŸ±Ç`a(Ÿ±Ç`cpctŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`habsoluteŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`fwedgesŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`etextsŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`iautotextsŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`cpieŸ±Ç`a(Ÿ±Ç`ddataŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`gautopctŸ±Çaoa=Ÿ±ÇakflambdaŸ±Ç`a Ÿ±Ç`cpctŸ±Ç`a:Ÿ±Ç`a Ÿ±Ç`dfuncŸ±Ç`a(Ÿ±Ç`cpctŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ddataŸ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`x"                                  Ÿ±Ç`itextpropsŸ±Çaoa=Ÿ±ÇbnbddictŸ±Ç`a(Ÿ±Ç`ecolorŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2awŸ±Çbs2a"Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`flegendŸ±Ç`a(Ÿ±Ç`fwedgesŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`kingredientsŸ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`j          Ÿ±Ç`etitleŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2kIngredientsŸ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`j          Ÿ±Ç`clocŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2kcenter leftŸ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`j          Ÿ±Ç`nbbox_to_anchorŸ±Çaoa=Ÿ±Ç`a(Ÿ±Çbmia1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfc0.5Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia1Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`dsetpŸ±Ç`a(Ÿ±Ç`iautotextsŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dsizeŸ±Çaoa=Ÿ±Çbmia8Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`fweightŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2dboldŸ±Çbs2a"Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`iset_titleŸ±Ç`a(Ÿ±Çbs2a"Ÿ±Çbs2xMatplotlib bakery: A pieŸ±Çbs2a"Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`dshowŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1xO###############################################################################Ÿ±Ç`a
Ÿ±Çbc1xJ# Now it's time for the donut. Starting with a donut recipe, we transcribeŸ±Ç`a
Ÿ±Çbc1xL# the data to numbers (converting 1 egg to 50 g), and directly plot the pie.Ÿ±Ç`a
Ÿ±Çbc1x5# The pie? Wait... it's going to be donut, is it not?Ÿ±Ç`a
Ÿ±Çbc1xM# Well, as we see here, the donut is a pie, having a certain ``width`` set toŸ±Ç`a
Ÿ±Çbc1xJ# the wedges, which is different from its radius. It's as easy as it gets.Ÿ±Ç`a
Ÿ±Çbc1x/# This is done via the ``wedgeprops`` argument.Ÿ±Ç`a
Ÿ±Çbc1a#Ÿ±Ç`a
Ÿ±Çbc1x&# We then want to label the wedges viaŸ±Ç`a
Ÿ±Çbc1xE# `annotations <matplotlib.axes.Axes.annotate>`. We first create someŸ±Ç`a
Ÿ±Çbc1xG# dictionaries of common properties, which we can later pass as keywordŸ±Ç`a
Ÿ±Çbc1x8# argument. We then iterate over all wedges and for eachŸ±Ç`a
Ÿ±Çbc1a#Ÿ±Ç`a
Ÿ±Çbc1x.# * calculate the angle of the wedge's center,Ÿ±Ç`a
Ÿ±Çbc1xF# * from that obtain the coordinates of the point at that angle on theŸ±Ç`a
Ÿ±Çbc1r#   circumference,Ÿ±Ç`a
Ÿ±Çbc1xK# * determine the horizontal alignment of the text, depending on which sideŸ±Ç`a
Ÿ±Çbc1x!#   of the circle the point lies,Ÿ±Ç`a
Ÿ±Çbc1xN# * update the connection style with the obtained angle to have the annotationŸ±Ç`a
Ÿ±Çbc1x(#   arrow point outwards from the donut,Ÿ±Ç`a
Ÿ±Çbc1x:# * finally, create the annotation with all the previouslyŸ±Ç`a
Ÿ±Çbc1x#   determined parameters.Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`cfigŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`baxŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`hsubplotsŸ±Ç`a(Ÿ±Ç`gfigsizeŸ±Çaoa=Ÿ±Ç`a(Ÿ±Çbmia6Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia3Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`jsubplot_kwŸ±Çaoa=Ÿ±ÇbnbddictŸ±Ç`a(Ÿ±Ç`faspectŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2eequalŸ±Çbs2a"Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`frecipeŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`a[Ÿ±Çbs2a"Ÿ±Çbs2k225 g flourŸ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`j          Ÿ±Çbs2a"Ÿ±Çbs2j90 g sugarŸ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`j          Ÿ±Çbs2a"Ÿ±Çbs2e1 eggŸ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`j          Ÿ±Çbs2a"Ÿ±Çbs2k60 g butterŸ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`j          Ÿ±Çbs2a"Ÿ±Çbs2k100 ml milkŸ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`j          Ÿ±Çbs2a"Ÿ±Çbs2t1/2 package of yeastŸ±Çbs2a"Ÿ±Ç`a]Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`ddataŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`a[Ÿ±Çbmic225Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmib90Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmib50Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmib60Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmic100Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia5Ÿ±Ç`a]Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`fwedgesŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`etextsŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`cpieŸ±Ç`a(Ÿ±Ç`ddataŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`jwedgepropsŸ±Çaoa=Ÿ±ÇbnbddictŸ±Ç`a(Ÿ±Ç`ewidthŸ±Çaoa=Ÿ±Çbmfc0.5Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`jstartangleŸ±Çaoa=Ÿ±Çaoa-Ÿ±Çbmib40Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`jbbox_propsŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±ÇbnbddictŸ±Ç`a(Ÿ±Ç`hboxstyleŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2nsquare,pad=0.3Ÿ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`bfcŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2awŸ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`becŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2akŸ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`blwŸ±Çaoa=Ÿ±Çbmfd0.72Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`bkwŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±ÇbnbddictŸ±Ç`a(Ÿ±Ç`jarrowpropsŸ±Çaoa=Ÿ±ÇbnbddictŸ±Ç`a(Ÿ±Ç`jarrowstyleŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2a-Ÿ±Çbs2a"Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`j          Ÿ±Ç`dbboxŸ±Çaoa=Ÿ±Ç`jbbox_propsŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`fzorderŸ±Çaoa=Ÿ±Çbmia0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`bvaŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2fcenterŸ±Çbs2a"Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±ÇakcforŸ±Ç`a Ÿ±Ç`aiŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`apŸ±Ç`a Ÿ±ÇbowbinŸ±Ç`a Ÿ±ÇbnbienumerateŸ±Ç`a(Ÿ±Ç`fwedgesŸ±Ç`a)Ÿ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`cangŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`a(Ÿ±Ç`apŸ±Çaoa.Ÿ±Ç`ftheta2Ÿ±Ç`a Ÿ±Çaoa-Ÿ±Ç`a Ÿ±Ç`apŸ±Çaoa.Ÿ±Ç`ftheta1Ÿ±Ç`a)Ÿ±Çaoa/Ÿ±Çbmfb2.Ÿ±Ç`a Ÿ±Çaoa+Ÿ±Ç`a Ÿ±Ç`apŸ±Çaoa.Ÿ±Ç`ftheta1Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`ayŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`csinŸ±Ç`a(Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`gdeg2radŸ±Ç`a(Ÿ±Ç`cangŸ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`axŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`ccosŸ±Ç`a(Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`gdeg2radŸ±Ç`a(Ÿ±Ç`cangŸ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`shorizontalalignmentŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`a{Ÿ±Çaoa-Ÿ±Çbmia1Ÿ±Ç`a:Ÿ±Ç`a Ÿ±Çbs2a"Ÿ±Çbs2erightŸ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia1Ÿ±Ç`a:Ÿ±Ç`a Ÿ±Çbs2a"Ÿ±Çbs2dleftŸ±Çbs2a"Ÿ±Ç`a}Ÿ±Ç`a[Ÿ±ÇbnbcintŸ±Ç`a(Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`dsignŸ±Ç`a(Ÿ±Ç`axŸ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a]Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`oconnectionstyleŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Çbs2a"Ÿ±Çbs2vangle,angleA=0,angleB=Ÿ±Çbsib{}Ÿ±Çbs2a"Ÿ±Çaoa.Ÿ±Ç`fformatŸ±Ç`a(Ÿ±Ç`cangŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`bkwŸ±Ç`a[Ÿ±Çbs2a"Ÿ±Çbs2jarrowpropsŸ±Çbs2a"Ÿ±Ç`a]Ÿ±Çaoa.Ÿ±Ç`fupdateŸ±Ç`a(Ÿ±Ç`a{Ÿ±Çbs2a"Ÿ±Çbs2oconnectionstyleŸ±Çbs2a"Ÿ±Ç`a:Ÿ±Ç`a Ÿ±Ç`oconnectionstyleŸ±Ç`a}Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`hannotateŸ±Ç`a(Ÿ±Ç`frecipeŸ±Ç`a[Ÿ±Ç`aiŸ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`bxyŸ±Çaoa=Ÿ±Ç`a(Ÿ±Ç`axŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ayŸ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`fxytextŸ±Çaoa=Ÿ±Ç`a(Ÿ±Çbmfd1.35Ÿ±Çaoa*Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`dsignŸ±Ç`a(Ÿ±Ç`axŸ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfc1.4Ÿ±Çaoa*Ÿ±Ç`ayŸ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`p                Ÿ±Ç`shorizontalalignmentŸ±Çaoa=Ÿ±Ç`shorizontalalignmentŸ±Ç`a,Ÿ±Ç`a Ÿ±Çaoa*Ÿ±Çaoa*Ÿ±Ç`bkwŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`iset_titleŸ±Ç`a(Ÿ±Çbs2a"Ÿ±Çbs2xMatplotlib bakery: A donutŸ±Çbs2a"Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`dshowŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1xO###############################################################################Ÿ±Ç`a
Ÿ±Çbc1xN# And here it is, the donut. Note however, that if we were to use this recipe,Ÿ±Ç`a
Ÿ±Çbc1xH# the ingredients would suffice for around 6 donuts - producing one hugeŸ±Ç`a
Ÿ±Çbc1x7# donut is untested and might result in kitchen errors.Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1xM#############################################################################Ÿ±Ç`a
Ÿ±Çbc1a#Ÿ±Ç`a
Ÿ±Çbc1x# .. admonition:: ReferencesŸ±Ç`a
Ÿ±Çbc1a#Ÿ±Ç`a
Ÿ±Çbc1xN#    The use of the following functions, methods, classes and modules is shownŸ±Ç`a
Ÿ±Çbc1u#    in this example:Ÿ±Ç`a
Ÿ±Çbc1a#Ÿ±Ç`a
Ÿ±Çbc1x;#    - `matplotlib.axes.Axes.pie` / `matplotlib.pyplot.pie`Ÿ±Ç`a
Ÿ±Çbc1xA#    - `matplotlib.axes.Axes.legend` / `matplotlib.pyplot.legend`Ÿ±Ç`a
`dNoneˆ