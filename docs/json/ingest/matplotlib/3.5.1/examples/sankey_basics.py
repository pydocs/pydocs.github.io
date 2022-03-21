��������2���bsdx{"""
================
The Sankey class
================

Demonstrate the Sankey class by producing three basic diagrams.
"""���`a
���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���`a
���bkndfrom���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfsankey���`a ���bknfimport���`a ���`fSankey���`a
���`a
���`a
���bc1xO###############################################################################���`a
���bc1x# Example 1 -- Mostly defaults���`a
���bc1a#���`a
���bc1xL# This demonstrates how to create a simple diagram by implicitly calling the���`a
���bc1xI# Sankey.add() method and by appending finish() to the call to the class.���`a
���`a
���`fSankey���`a(���`eflows���aoa=���`a[���bmfd0.25���`a,���`a ���bmfd0.15���`a,���`a ���bmfd0.60���`a,���`a ���aoa-���bmfd0.20���`a,���`a ���aoa-���bmfd0.15���`a,���`a ���aoa-���bmfd0.05���`a,���`a ���aoa-���bmfd0.50���`a,���`a ���aoa-���bmfd0.10���`a]���`a,���`a
���`g       ���`flabels���aoa=���`a[���bs1a'���bs1a'���`a,���`a ���bs1a'���bs1a'���`a,���`a ���bs1a'���bs1a'���`a,���`a ���bs1a'���bs1eFirst���bs1a'���`a,���`a ���bs1a'���bs1fSecond���bs1a'���`a,���`a ���bs1a'���bs1eThird���bs1a'���`a,���`a ���bs1a'���bs1fFourth���bs1a'���`a,���`a ���bs1a'���bs1eFifth���bs1a'���`a]���`a,���`a
���`g       ���`lorientations���aoa=���`a[���aoa-���bmia1���`a,���`a ���bmia1���`a,���`a ���bmia0���`a,���`a ���bmia1���`a,���`a ���bmia1���`a,���`a ���bmia1���`a,���`a ���bmia0���`a,���`a ���aoa-���bmia1���`a]���`a)���aoa.���`ffinish���`a(���`a)���`a
���`cplt���aoa.���`etitle���`a(���bs2a"���bs2x1The default settings produce a diagram like this.���bs2a"���`a)���`a
���`a
���bc1xO###############################################################################���`a
���bc1i# Notice:���`a
���bc1a#���`a
���bc1xG# 1. Axes weren't provided when Sankey() was instantiated, so they were���`a
���bc1x#    created automatically.���`a
���bc1xC# 2. The scale argument wasn't necessary since the data was already���`a
���bc1p#    normalized.���`a
���bc1x8# 3. By default, the lengths of the paths are justified.���`a
���`a
���`a
���bc1xO###############################################################################���`a
���bc1k# Example 2���`a
���bc1a#���`a
���bc1t# This demonstrates:���`a
���bc1a#���`a
���bc1x,# 1. Setting one path longer than the others���`a
���bc1x1# 2. Placing a label in the middle of the diagram���`a
���bc1x4# 3. Using the scale argument to normalize the flows���`a
���bc1x8# 4. Implicitly passing keyword arguments to PathPatch()���`a
���bc1x*# 5. Changing the angle of the arrow heads���`a
���bc1xG# 6. Changing the offset between the tips of the paths and their labels���`a
���bc1xF# 7. Formatting the numbers in the path labels and the associated unit���`a
���bc1xL# 8. Changing the appearance of the patch and the labels after the figure is���`a
���bc1l#    created���`a
���`a
���`cfig���`a ���aoa=���`a ���`cplt���aoa.���`ffigure���`a(���`a)���`a
���`bax���`a ���aoa=���`a ���`cfig���aoa.���`kadd_subplot���`a(���bmia1���`a,���`a ���bmia1���`a,���`a ���bmia1���`a,���`a ���`fxticks���aoa=���`a[���`a]���`a,���`a ���`fyticks���aoa=���`a[���`a]���`a,���`a
���`u                     ���`etitle���aoa=���bs2a"���bs2xFlow Diagram of a Widget���bs2a"���`a)���`a
���`fsankey���`a ���aoa=���`a ���`fSankey���`a(���`bax���aoa=���`bax���`a,���`a ���`escale���aoa=���bmfd0.01���`a,���`a ���`foffset���aoa=���bmfc0.2���`a,���`a ���`jhead_angle���aoa=���bmic180���`a,���`a
���`p                ���bnbfformat���aoa=���bs1a'���bsid%.0f���bs1a'���`a,���`a ���`dunit���aoa=���bs1a'���bs1a%���bs1a'���`a)���`a
���`fsankey���aoa.���`cadd���`a(���`eflows���aoa=���`a[���bmib25���`a,���`a ���bmia0���`a,���`a ���bmib60���`a,���`a ���aoa-���bmib10���`a,���`a ���aoa-���bmib20���`a,���`a ���aoa-���bmia5���`a,���`a ���aoa-���bmib15���`a,���`a ���aoa-���bmib10���`a,���`a ���aoa-���bmib40���`a]���`a,���`a
���`k           ���`flabels���aoa=���`a[���bs1a'���bs1a'���`a,���`a ���bs1a'���bs1a'���`a,���`a ���bs1a'���bs1a'���`a,���`a ���bs1a'���bs1eFirst���bs1a'���`a,���`a ���bs1a'���bs1fSecond���bs1a'���`a,���`a ���bs1a'���bs1eThird���bs1a'���`a,���`a ���bs1a'���bs1fFourth���bs1a'���`a,���`a
���`s                   ���bs1a'���bs1eFifth���bs1a'���`a,���`a ���bs1a'���bs1gHurray!���bs1a'���`a]���`a,���`a
���`k           ���`lorientations���aoa=���`a[���aoa-���bmia1���`a,���`a ���bmia1���`a,���`a ���bmia0���`a,���`a ���bmia1���`a,���`a ���bmia1���`a,���`a ���bmia1���`a,���`a ���aoa-���bmia1���`a,���`a ���aoa-���bmia1���`a,���`a ���bmia0���`a]���`a,���`a
���`k           ���`kpathlengths���aoa=���`a[���bmfd0.25���`a,���`a ���bmfd0.25���`a,���`a ���bmfd0.25���`a,���`a ���bmfd0.25���`a,���`a ���bmfd0.25���`a,���`a ���bmfc0.6���`a,���`a ���bmfd0.25���`a,���`a ���bmfd0.25���`a,���`a
���`x                        ���bmfd0.25���`a]���`a,���`a
���`k           ���`jpatchlabel���aoa=���bs2a"���bs2fWidget���bseb\n���bs2aA���bs2a"���`a)���`b  ���bc1x+# Arguments to matplotlib.patches.PathPatch���`a
���`hdiagrams���`a ���aoa=���`a ���`fsankey���aoa.���`ffinish���`a(���`a)���`a
���`hdiagrams���`a[���bmia0���`a]���aoa.���`etexts���`a[���aoa-���bmia1���`a]���aoa.���`iset_color���`a(���bs1a'���bs1ar���bs1a'���`a)���`a
���`hdiagrams���`a[���bmia0���`a]���aoa.���`dtext���aoa.���`nset_fontweight���`a(���bs1a'���bs1dbold���bs1a'���`a)���`a
���`a
���bc1xO###############################################################################���`a
���bc1i# Notice:���`a
���bc1a#���`a
���bc1xH# 1. Since the sum of the flows is nonzero, the width of the trunk isn't���`a
���bc1xJ#    uniform.  The matplotlib logging system logs this at the DEBUG level.���`a
���bc1xN# 2. The second flow doesn't appear because its value is zero.  Again, this is���`a
���bc1x#    logged at the DEBUG level.���`a
���`a
���`a
���bc1xO###############################################################################���`a
���bc1k# Example 3���`a
���bc1a#���`a
���bc1t# This demonstrates:���`a
���bc1a#���`a
���bc1x# 1. Connecting two systems���`a
���bc1x-# 2. Turning off the labels of the quantities���`a
���bc1t# 3. Adding a legend���`a
���`a
���`cfig���`a ���aoa=���`a ���`cplt���aoa.���`ffigure���`a(���`a)���`a
���`bax���`a ���aoa=���`a ���`cfig���aoa.���`kadd_subplot���`a(���bmia1���`a,���`a ���bmia1���`a,���`a ���bmia1���`a,���`a ���`fxticks���aoa=���`a[���`a]���`a,���`a ���`fyticks���aoa=���`a[���`a]���`a,���`a ���`etitle���aoa=���bs2a"���bs2kTwo Systems���bs2a"���`a)���`a
���`eflows���`a ���aoa=���`a ���`a[���bmfd0.25���`a,���`a ���bmfd0.15���`a,���`a ���bmfd0.60���`a,���`a ���aoa-���bmfd0.10���`a,���`a ���aoa-���bmfd0.05���`a,���`a ���aoa-���bmfd0.25���`a,���`a ���aoa-���bmfd0.15���`a,���`a ���aoa-���bmfd0.10���`a,���`a ���aoa-���bmfd0.35���`a]���`a
���`fsankey���`a ���aoa=���`a ���`fSankey���`a(���`bax���aoa=���`bax���`a,���`a ���`dunit���aoa=���bkcdNone���`a)���`a
���`fsankey���aoa.���`cadd���`a(���`eflows���aoa=���`eflows���`a,���`a ���`elabel���aoa=���bs1a'���bs1cone���bs1a'���`a,���`a
���`k           ���`lorientations���aoa=���`a[���aoa-���bmia1���`a,���`a ���bmia1���`a,���`a ���bmia0���`a,���`a ���bmia1���`a,���`a ���bmia1���`a,���`a ���bmia1���`a,���`a ���aoa-���bmia1���`a,���`a ���aoa-���bmia1���`a,���`a ���bmia0���`a]���`a)���`a
���`fsankey���aoa.���`cadd���`a(���`eflows���aoa=���`a[���aoa-���bmfd0.25���`a,���`a ���bmfd0.15���`a,���`a ���bmfc0.1���`a]���`a,���`a ���`elabel���aoa=���bs1a'���bs1ctwo���bs1a'���`a,���`a
���`k           ���`lorientations���aoa=���`a[���aoa-���bmia1���`a,���`a ���aoa-���bmia1���`a,���`a ���aoa-���bmia1���`a]���`a,���`a ���`eprior���aoa=���bmia0���`a,���`a ���`gconnect���aoa=���`a(���bmia0���`a,���`a ���bmia0���`a)���`a)���`a
���`hdiagrams���`a ���aoa=���`a ���`fsankey���aoa.���`ffinish���`a(���`a)���`a
���`hdiagrams���`a[���aoa-���bmia1���`a]���aoa.���`epatch���aoa.���`iset_hatch���`a(���bs1a'���bs1a/���bs1a'���`a)���`a
���`cplt���aoa.���`flegend���`a(���`a)���`a
���`a
���bc1xO###############################################################################���`a
���bc1xF# Notice that only one connection is specified, but the systems form a���`a
���bc1xG# circuit since: (1) the lengths of the paths are justified and (2) the���`a
���bc1x4# orientation and ordering of the flows is mirrored.���`a
���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
���`a
���`a
���bc1xM#############################################################################���`a
���bc1a#���`a
���bc1x# .. admonition:: References���`a
���bc1a#���`a
���bc1xN#    The use of the following functions, methods, classes and modules is shown���`a
���bc1u#    in this example:���`a
���bc1a#���`a
���bc1x#    - `matplotlib.sankey`���`a
���bc1x!#    - `matplotlib.sankey.Sankey`���`a
���bc1x%#    - `matplotlib.sankey.Sankey.add`���`a
���bc1x(#    - `matplotlib.sankey.Sankey.finish`���`a
`dNone�