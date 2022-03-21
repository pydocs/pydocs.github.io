��������M���bsdy^"""
==========================
Labeling a pie and a donut
==========================

Welcome to the Matplotlib bakery. We will create a pie and a donut
chart through the `pie method <matplotlib.axes.Axes.pie>` and
show how to label them with a `legend <matplotlib.axes.Axes.legend>`
as well as with `annotations <matplotlib.axes.Axes.annotate>`.
"""���`a
���`a
���bc1xO###############################################################################���`a
���bc1xJ# As usual we would start by defining the imports and create a figure with���`a
���bc1k# subplots.���`a
���bc1xK# Now it's time for the pie. Starting with a pie recipe, we create the data���`a
���bc1x# and a list of labels from it.���`a
���bc1a#���`a
���bc1xJ# We can provide a function to the ``autopct`` argument, which will expand���`a
���bc1xH# automatic percentage labeling by showing absolute values; we calculate���`a
���bc1xE# the latter back from relative data and the known sum of all values.���`a
���bc1a#���`a
���bc1xM# We then create the pie and store the returned objects for later.  The first���`a
���bc1xL# returned element of the returned tuple is a list of the wedges.  Those are���`a
���bc1xO# `matplotlib.patches.Wedge` patches, which can directly be used as the handles���`a
���bc1xO# for a legend. We can use the legend's ``bbox_to_anchor`` argument to position���`a
���bc1xO# the legend outside of the pie. Here we use the axes coordinates ``(1, 0, 0.5,���`a
���bc1xJ# 1)`` together with the location ``"center left"``; i.e. the left central���`a
���bc1xL# point of the legend will be at the left central point of the bounding box,���`a
���bc1x?# spanning from ``(1, 0)`` to ``(1.5, 1)`` in axes coordinates.���`a
���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���`a
���`cfig���`a,���`a ���`bax���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`gfigsize���aoa=���`a(���bmia6���`a,���`a ���bmia3���`a)���`a,���`a ���`jsubplot_kw���aoa=���bnbddict���`a(���`faspect���aoa=���bs2a"���bs2eequal���bs2a"���`a)���`a)���`a
���`a
���`frecipe���`a ���aoa=���`a ���`a[���bs2a"���bs2k375 g flour���bs2a"���`a,���`a
���`j          ���bs2a"���bs2j75 g sugar���bs2a"���`a,���`a
���`j          ���bs2a"���bs2l250 g butter���bs2a"���`a,���`a
���`j          ���bs2a"���bs2m300 g berries���bs2a"���`a]���`a
���`a
���`ddata���`a ���aoa=���`a ���`a[���bnbefloat���`a(���`ax���aoa.���`esplit���`a(���`a)���`a[���bmia0���`a]���`a)���`a ���akcfor���`a ���`ax���`a ���bowbin���`a ���`frecipe���`a]���`a
���`kingredients���`a ���aoa=���`a ���`a[���`ax���aoa.���`esplit���`a(���`a)���`a[���aoa-���bmia1���`a]���`a ���akcfor���`a ���`ax���`a ���bowbin���`a ���`frecipe���`a]���`a
���`a
���`a
���akcdef���`a ���bnfdfunc���`a(���`cpct���`a,���`a ���`gallvals���`a)���`a:���`a
���`d    ���`habsolute���`a ���aoa=���`a ���bnbcint���`a(���`bnp���aoa.���`eround���`a(���`cpct���aoa/���bmfd100.���aoa*���`bnp���aoa.���`csum���`a(���`gallvals���`a)���`a)���`a)���`a
���`d    ���akfreturn���`a ���bs2a"���bsif{:.1f}���bs2a%���bseb\n���bs2a(���bsid{:d}���bs2c g)���bs2a"���aoa.���`fformat���`a(���`cpct���`a,���`a ���`habsolute���`a)���`a
���`a
���`a
���`fwedges���`a,���`a ���`etexts���`a,���`a ���`iautotexts���`a ���aoa=���`a ���`bax���aoa.���`cpie���`a(���`ddata���`a,���`a ���`gautopct���aoa=���akflambda���`a ���`cpct���`a:���`a ���`dfunc���`a(���`cpct���`a,���`a ���`ddata���`a)���`a,���`a
���`x"                                  ���`itextprops���aoa=���bnbddict���`a(���`ecolor���aoa=���bs2a"���bs2aw���bs2a"���`a)���`a)���`a
���`a
���`bax���aoa.���`flegend���`a(���`fwedges���`a,���`a ���`kingredients���`a,���`a
���`j          ���`etitle���aoa=���bs2a"���bs2kIngredients���bs2a"���`a,���`a
���`j          ���`cloc���aoa=���bs2a"���bs2kcenter left���bs2a"���`a,���`a
���`j          ���`nbbox_to_anchor���aoa=���`a(���bmia1���`a,���`a ���bmia0���`a,���`a ���bmfc0.5���`a,���`a ���bmia1���`a)���`a)���`a
���`a
���`cplt���aoa.���`dsetp���`a(���`iautotexts���`a,���`a ���`dsize���aoa=���bmia8���`a,���`a ���`fweight���aoa=���bs2a"���bs2dbold���bs2a"���`a)���`a
���`a
���`bax���aoa.���`iset_title���`a(���bs2a"���bs2xMatplotlib bakery: A pie���bs2a"���`a)���`a
���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
���`a
���`a
���bc1xO###############################################################################���`a
���bc1xJ# Now it's time for the donut. Starting with a donut recipe, we transcribe���`a
���bc1xL# the data to numbers (converting 1 egg to 50 g), and directly plot the pie.���`a
���bc1x5# The pie? Wait... it's going to be donut, is it not?���`a
���bc1xM# Well, as we see here, the donut is a pie, having a certain ``width`` set to���`a
���bc1xJ# the wedges, which is different from its radius. It's as easy as it gets.���`a
���bc1x/# This is done via the ``wedgeprops`` argument.���`a
���bc1a#���`a
���bc1x&# We then want to label the wedges via���`a
���bc1xE# `annotations <matplotlib.axes.Axes.annotate>`. We first create some���`a
���bc1xG# dictionaries of common properties, which we can later pass as keyword���`a
���bc1x8# argument. We then iterate over all wedges and for each���`a
���bc1a#���`a
���bc1x.# * calculate the angle of the wedge's center,���`a
���bc1xF# * from that obtain the coordinates of the point at that angle on the���`a
���bc1r#   circumference,���`a
���bc1xK# * determine the horizontal alignment of the text, depending on which side���`a
���bc1x!#   of the circle the point lies,���`a
���bc1xN# * update the connection style with the obtained angle to have the annotation���`a
���bc1x(#   arrow point outwards from the donut,���`a
���bc1x:# * finally, create the annotation with all the previously���`a
���bc1x#   determined parameters.���`a
���`a
���`a
���`cfig���`a,���`a ���`bax���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`gfigsize���aoa=���`a(���bmia6���`a,���`a ���bmia3���`a)���`a,���`a ���`jsubplot_kw���aoa=���bnbddict���`a(���`faspect���aoa=���bs2a"���bs2eequal���bs2a"���`a)���`a)���`a
���`a
���`frecipe���`a ���aoa=���`a ���`a[���bs2a"���bs2k225 g flour���bs2a"���`a,���`a
���`j          ���bs2a"���bs2j90 g sugar���bs2a"���`a,���`a
���`j          ���bs2a"���bs2e1 egg���bs2a"���`a,���`a
���`j          ���bs2a"���bs2k60 g butter���bs2a"���`a,���`a
���`j          ���bs2a"���bs2k100 ml milk���bs2a"���`a,���`a
���`j          ���bs2a"���bs2t1/2 package of yeast���bs2a"���`a]���`a
���`a
���`ddata���`a ���aoa=���`a ���`a[���bmic225���`a,���`a ���bmib90���`a,���`a ���bmib50���`a,���`a ���bmib60���`a,���`a ���bmic100���`a,���`a ���bmia5���`a]���`a
���`a
���`fwedges���`a,���`a ���`etexts���`a ���aoa=���`a ���`bax���aoa.���`cpie���`a(���`ddata���`a,���`a ���`jwedgeprops���aoa=���bnbddict���`a(���`ewidth���aoa=���bmfc0.5���`a)���`a,���`a ���`jstartangle���aoa=���aoa-���bmib40���`a)���`a
���`a
���`jbbox_props���`a ���aoa=���`a ���bnbddict���`a(���`hboxstyle���aoa=���bs2a"���bs2nsquare,pad=0.3���bs2a"���`a,���`a ���`bfc���aoa=���bs2a"���bs2aw���bs2a"���`a,���`a ���`bec���aoa=���bs2a"���bs2ak���bs2a"���`a,���`a ���`blw���aoa=���bmfd0.72���`a)���`a
���`bkw���`a ���aoa=���`a ���bnbddict���`a(���`jarrowprops���aoa=���bnbddict���`a(���`jarrowstyle���aoa=���bs2a"���bs2a-���bs2a"���`a)���`a,���`a
���`j          ���`dbbox���aoa=���`jbbox_props���`a,���`a ���`fzorder���aoa=���bmia0���`a,���`a ���`bva���aoa=���bs2a"���bs2fcenter���bs2a"���`a)���`a
���`a
���akcfor���`a ���`ai���`a,���`a ���`ap���`a ���bowbin���`a ���bnbienumerate���`a(���`fwedges���`a)���`a:���`a
���`d    ���`cang���`a ���aoa=���`a ���`a(���`ap���aoa.���`ftheta2���`a ���aoa-���`a ���`ap���aoa.���`ftheta1���`a)���aoa/���bmfb2.���`a ���aoa+���`a ���`ap���aoa.���`ftheta1���`a
���`d    ���`ay���`a ���aoa=���`a ���`bnp���aoa.���`csin���`a(���`bnp���aoa.���`gdeg2rad���`a(���`cang���`a)���`a)���`a
���`d    ���`ax���`a ���aoa=���`a ���`bnp���aoa.���`ccos���`a(���`bnp���aoa.���`gdeg2rad���`a(���`cang���`a)���`a)���`a
���`d    ���`shorizontalalignment���`a ���aoa=���`a ���`a{���aoa-���bmia1���`a:���`a ���bs2a"���bs2eright���bs2a"���`a,���`a ���bmia1���`a:���`a ���bs2a"���bs2dleft���bs2a"���`a}���`a[���bnbcint���`a(���`bnp���aoa.���`dsign���`a(���`ax���`a)���`a)���`a]���`a
���`d    ���`oconnectionstyle���`a ���aoa=���`a ���bs2a"���bs2vangle,angleA=0,angleB=���bsib{}���bs2a"���aoa.���`fformat���`a(���`cang���`a)���`a
���`d    ���`bkw���`a[���bs2a"���bs2jarrowprops���bs2a"���`a]���aoa.���`fupdate���`a(���`a{���bs2a"���bs2oconnectionstyle���bs2a"���`a:���`a ���`oconnectionstyle���`a}���`a)���`a
���`d    ���`bax���aoa.���`hannotate���`a(���`frecipe���`a[���`ai���`a]���`a,���`a ���`bxy���aoa=���`a(���`ax���`a,���`a ���`ay���`a)���`a,���`a ���`fxytext���aoa=���`a(���bmfd1.35���aoa*���`bnp���aoa.���`dsign���`a(���`ax���`a)���`a,���`a ���bmfc1.4���aoa*���`ay���`a)���`a,���`a
���`p                ���`shorizontalalignment���aoa=���`shorizontalalignment���`a,���`a ���aoa*���aoa*���`bkw���`a)���`a
���`a
���`bax���aoa.���`iset_title���`a(���bs2a"���bs2xMatplotlib bakery: A donut���bs2a"���`a)���`a
���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
���`a
���bc1xO###############################################################################���`a
���bc1xN# And here it is, the donut. Note however, that if we were to use this recipe,���`a
���bc1xH# the ingredients would suffice for around 6 donuts - producing one huge���`a
���bc1x7# donut is untested and might result in kitchen errors.���`a
���`a
���`a
���bc1xM#############################################################################���`a
���bc1a#���`a
���bc1x# .. admonition:: References���`a
���bc1a#���`a
���bc1xN#    The use of the following functions, methods, classes and modules is shown���`a
���bc1u#    in this example:���`a
���bc1a#���`a
���bc1x;#    - `matplotlib.axes.Axes.pie` / `matplotlib.pyplot.pie`���`a
���bc1xA#    - `matplotlib.axes.Axes.legend` / `matplotlib.pyplot.legend`���`a
`dNone�