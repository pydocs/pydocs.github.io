��������+���bsdy�"""
========================================================
Building histograms using Rectangles and PolyCollections
========================================================

Using a path patch to draw rectangles.
The technique of using lots of Rectangle instances, or
the faster method of using PolyCollections, were implemented before we
had proper paths with moveto/lineto, closepoly etc in mpl.  Now that
we have them, we can draw collections of regularly shaped objects with
homogeneous properties more efficiently with a PathCollection. This
example makes a histogram -- it's more work to set up the vertex arrays
at the outset, but it should be much faster for large numbers of
objects.
"""���`a
���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnngpatches���`a ���akbas���`a ���bnngpatches���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnndpath���`a ���akbas���`a ���bnndpath���`a
���`a
���`cfig���`a,���`a ���`bax���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`a)���`a
���`a
���bc1x)# Fixing random state for reproducibility���`a
���`bnp���aoa.���`frandom���aoa.���`dseed���`a(���bmih19680801���`a)���`a
���`a
���`a
���bc1x# histogram our data with numpy���`a
���`a
���`ddata���`a ���aoa=���`a ���`bnp���aoa.���`frandom���aoa.���`erandn���`a(���bmid1000���`a)���`a
���`an���`a,���`a ���`dbins���`a ���aoa=���`a ���`bnp���aoa.���`ihistogram���`a(���`ddata���`a,���`a ���bmib50���`a)���`a
���`a
���bc1x5# get the corners of the rectangles for the histogram���`a
���`dleft���`a ���aoa=���`a ���`dbins���`a[���`a:���aoa-���bmia1���`a]���`a
���`eright���`a ���aoa=���`a ���`dbins���`a[���bmia1���`a:���`a]���`a
���`fbottom���`a ���aoa=���`a ���`bnp���aoa.���`ezeros���`a(���bnbclen���`a(���`dleft���`a)���`a)���`a
���`ctop���`a ���aoa=���`a ���`fbottom���`a ���aoa+���`a ���`an���`a
���`a
���`a
���bc1xE# we need a (numrects x numsides x 2) numpy array for the path helper���`a
���bc1x## function to build a compound path���`a
���`bXY���`a ���aoa=���`a ���`bnp���aoa.���`earray���`a(���`a[���`a[���`dleft���`a,���`a ���`dleft���`a,���`a ���`eright���`a,���`a ���`eright���`a]���`a,���`a ���`a[���`fbottom���`a,���`a ���`ctop���`a,���`a ���`ctop���`a,���`a ���`fbottom���`a]���`a]���`a)���aoa.���`aT���`a
���`a
���bc1u# get the Path object���`a
���`gbarpath���`a ���aoa=���`a ���`dpath���aoa.���`dPath���aoa.���`xmake_compound_path_from_polys���`a(���`bXY���`a)���`a
���`a
���bc1x# make a patch out of it���`a
���`epatch���`a ���aoa=���`a ���`gpatches���aoa.���`iPathPatch���`a(���`gbarpath���`a)���`a
���`bax���aoa.���`iadd_patch���`a(���`epatch���`a)���`a
���`a
���bc1x# update the view limits���`a
���`bax���aoa.���`hset_xlim���`a(���`dleft���`a[���bmia0���`a]���`a,���`a ���`eright���`a[���aoa-���bmia1���`a]���`a)���`a
���`bax���aoa.���`hset_ylim���`a(���`fbottom���aoa.���`cmin���`a(���`a)���`a,���`a ���`ctop���aoa.���`cmax���`a(���`a)���`a)���`a
���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
���`a
���bc1xM#############################################################################���`a
���bc1xK# It should be noted that instead of creating a three-dimensional array and���`a
���bc1xL# using `~.path.Path.make_compound_path_from_polys`, we could as well create���`a
���bc1xD# the compound path directly using vertices and codes as shown below���`a
���`a
���`fnrects���`a ���aoa=���`a ���bnbclen���`a(���`dleft���`a)���`a
���`fnverts���`a ���aoa=���`a ���`fnrects���aoa*���`a(���bmia1���aoa+���bmia3���aoa+���bmia1���`a)���`a
���`everts���`a ���aoa=���`a ���`bnp���aoa.���`ezeros���`a(���`a(���`fnverts���`a,���`a ���bmia2���`a)���`a)���`a
���`ecodes���`a ���aoa=���`a ���`bnp���aoa.���`dones���`a(���`fnverts���`a,���`a ���bnbcint���`a)���`a ���aoa*���`a ���`dpath���aoa.���`dPath���aoa.���`fLINETO���`a
���`ecodes���`a[���bmia0���`a:���`a:���bmia5���`a]���`a ���aoa=���`a ���`dpath���aoa.���`dPath���aoa.���`fMOVETO���`a
���`ecodes���`a[���bmia4���`a:���`a:���bmia5���`a]���`a ���aoa=���`a ���`dpath���aoa.���`dPath���aoa.���`iCLOSEPOLY���`a
���`everts���`a[���bmia0���`a:���`a:���bmia5���`a,���`a ���bmia0���`a]���`a ���aoa=���`a ���`dleft���`a
���`everts���`a[���bmia0���`a:���`a:���bmia5���`a,���`a ���bmia1���`a]���`a ���aoa=���`a ���`fbottom���`a
���`everts���`a[���bmia1���`a:���`a:���bmia5���`a,���`a ���bmia0���`a]���`a ���aoa=���`a ���`dleft���`a
���`everts���`a[���bmia1���`a:���`a:���bmia5���`a,���`a ���bmia1���`a]���`a ���aoa=���`a ���`ctop���`a
���`everts���`a[���bmia2���`a:���`a:���bmia5���`a,���`a ���bmia0���`a]���`a ���aoa=���`a ���`eright���`a
���`everts���`a[���bmia2���`a:���`a:���bmia5���`a,���`a ���bmia1���`a]���`a ���aoa=���`a ���`ctop���`a
���`everts���`a[���bmia3���`a:���`a:���bmia5���`a,���`a ���bmia0���`a]���`a ���aoa=���`a ���`eright���`a
���`everts���`a[���bmia3���`a:���`a:���bmia5���`a,���`a ���bmia1���`a]���`a ���aoa=���`a ���`fbottom���`a
���`a
���`gbarpath���`a ���aoa=���`a ���`dpath���aoa.���`dPath���`a(���`everts���`a,���`a ���`ecodes���`a)���`a
���`a
���bc1xM#############################################################################���`a
���bc1a#���`a
���bc1x# .. admonition:: References���`a
���bc1a#���`a
���bc1xN#    The use of the following functions, methods, classes and modules is shown���`a
���bc1u#    in this example:���`a
���bc1a#���`a
���bc1x#    - `matplotlib.patches`���`a
���bc1x%#    - `matplotlib.patches.PathPatch`���`a
���bc1x#    - `matplotlib.path`���`a
���bc1x#    - `matplotlib.path.Path`���`a
���bc1x;#    - `matplotlib.path.Path.make_compound_path_from_polys`���`a
���bc1x'#    - `matplotlib.axes.Axes.add_patch`���`a
���bc1x.#    - `matplotlib.collections.PathCollection`���`a
���bc1a#���`a
���bc1x)#    This example shows an alternative to���`a
���bc1a#���`a
���bc1x.#    - `matplotlib.collections.PolyCollection`���`a
���bc1x"#    - `matplotlib.axes.Axes.hist`���`a
`dNone�