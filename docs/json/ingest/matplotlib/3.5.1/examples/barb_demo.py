������������bsdxK"""
==========
Wind Barbs
==========

Demonstration of wind barb plots.
"""���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���`a
���`ax���`a ���aoa=���`a ���`bnp���aoa.���`hlinspace���`a(���aoa-���bmia5���`a,���`a ���bmia5���`a,���`a ���bmia5���`a)���`a
���`aX���`a,���`a ���`aY���`a ���aoa=���`a ���`bnp���aoa.���`hmeshgrid���`a(���`ax���`a,���`a ���`ax���`a)���`a
���`aU���`a,���`a ���`aV���`a ���aoa=���`a ���bmib12���`a ���aoa*���`a ���`aX���`a,���`a ���bmib12���`a ���aoa*���`a ���`aY���`a
���`a
���`ddata���`a ���aoa=���`a ���`a[���`a(���aoa-���bmfc1.5���`a,���`a ���bmfb.5���`a,���`a ���aoa-���bmia6���`a,���`a ���aoa-���bmia6���`a)���`a,���`a
���`h        ���`a(���bmia1���`a,���`a ���aoa-���bmia1���`a,���`a ���aoa-���bmib46���`a,���`a ���bmib46���`a)���`a,���`a
���`h        ���`a(���aoa-���bmia3���`a,���`a ���aoa-���bmia1���`a,���`a ���bmib11���`a,���`a ���aoa-���bmib11���`a)���`a,���`a
���`h        ���`a(���bmia1���`a,���`a ���bmfc1.5���`a,���`a ���bmib80���`a,���`a ���bmib80���`a)���`a,���`a
���`h        ���`a(���bmfc0.5���`a,���`a ���bmfd0.25���`a,���`a ���bmib25���`a,���`a ���bmib15���`a)���`a,���`a
���`h        ���`a(���aoa-���bmfc1.5���`a,���`a ���aoa-���bmfc0.5���`a,���`a ���aoa-���bmia5���`a,���`a ���bmib40���`a)���`a]���`a
���`a
���`ddata���`a ���aoa=���`a ���`bnp���aoa.���`earray���`a(���`ddata���`a,���`a ���`edtype���aoa=���`a[���`a(���bs1a'���bs1ax���bs1a'���`a,���`a ���`bnp���aoa.���`gfloat32���`a)���`a,���`a ���`a(���bs1a'���bs1ay���bs1a'���`a,���`a ���`bnp���aoa.���`gfloat32���`a)���`a,���`a
���`x                             ���`a(���bs1a'���bs1au���bs1a'���`a,���`a ���`bnp���aoa.���`gfloat32���`a)���`a,���`a ���`a(���bs1a'���bs1av���bs1a'���`a,���`a ���`bnp���aoa.���`gfloat32���`a)���`a]���`a)���`a
���`a
���`dfig1���`a,���`a ���`daxs1���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`enrows���aoa=���bmia2���`a,���`a ���`encols���aoa=���bmia2���`a)���`a
���bc1x"# Default parameters, uniform grid���`a
���`daxs1���`a[���bmia0���`a,���`a ���bmia0���`a]���aoa.���`ebarbs���`a(���`aX���`a,���`a ���`aY���`a,���`a ���`aU���`a,���`a ���`aV���`a)���`a
���`a
���bc1xG# Arbitrary set of vectors, make them longer and change the pivot point���`a
���bc1x7# (point around which they're rotated) to be the middle���`a
���`daxs1���`a[���bmia0���`a,���`a ���bmia1���`a]���aoa.���`ebarbs���`a(���`a
���`d    ���`ddata���`a[���bs1a'���bs1ax���bs1a'���`a]���`a,���`a ���`ddata���`a[���bs1a'���bs1ay���bs1a'���`a]���`a,���`a ���`ddata���`a[���bs1a'���bs1au���bs1a'���`a]���`a,���`a ���`ddata���`a[���bs1a'���bs1av���bs1a'���`a]���`a,���`a ���`flength���aoa=���bmia8���`a,���`a ���`epivot���aoa=���bs1a'���bs1fmiddle���bs1a'���`a)���`a
���`a
���bc1xM# Showing colormapping with uniform grid.  Fill the circle for an empty barb,���`a
���bc1x@# don't round the values, and change some of the size parameters���`a
���`daxs1���`a[���bmia1���`a,���`a ���bmia0���`a]���aoa.���`ebarbs���`a(���`a
���`d    ���`aX���`a,���`a ���`aY���`a,���`a ���`aU���`a,���`a ���`aV���`a,���`a ���`bnp���aoa.���`dsqrt���`a(���`aU���`a ���aoa*���aoa*���`a ���bmia2���`a ���aoa+���`a ���`aV���`a ���aoa*���aoa*���`a ���bmia2���`a)���`a,���`a ���`jfill_empty���aoa=���bkcdTrue���`a,���`a ���`hrounding���aoa=���bkceFalse���`a,���`a
���`d    ���`esizes���aoa=���bnbddict���`a(���`iemptybarb���aoa=���bmfd0.25���`a,���`a ���`gspacing���aoa=���bmfc0.2���`a,���`a ���`fheight���aoa=���bmfc0.3���`a)���`a)���`a
���`a
���bc1x@# Change colors as well as the increments for parts of the barbs���`a
���`daxs1���`a[���bmia1���`a,���`a ���bmia1���`a]���aoa.���`ebarbs���`a(���`ddata���`a[���bs1a'���bs1ax���bs1a'���`a]���`a,���`a ���`ddata���`a[���bs1a'���bs1ay���bs1a'���`a]���`a,���`a ���`ddata���`a[���bs1a'���bs1au���bs1a'���`a]���`a,���`a ���`ddata���`a[���bs1a'���bs1av���bs1a'���`a]���`a,���`a ���`iflagcolor���aoa=���bs1a'���bs1ar���bs1a'���`a,���`a
���`q                 ���`ibarbcolor���aoa=���`a[���bs1a'���bs1ab���bs1a'���`a,���`a ���bs1a'���bs1ag���bs1a'���`a]���`a,���`a ���`iflip_barb���aoa=���bkcdTrue���`a,���`a
���`q                 ���`obarb_increments���aoa=���bnbddict���`a(���`dhalf���aoa=���bmib10���`a,���`a ���`dfull���aoa=���bmib20���`a,���`a ���`dflag���aoa=���bmic100���`a)���`a)���`a
���`a
���bc1x"# Masked arrays are also supported���`a
���`hmasked_u���`a ���aoa=���`a ���`bnp���aoa.���`bma���aoa.���`lmasked_array���`a(���`ddata���`a[���bs1a'���bs1au���bs1a'���`a]���`a)���`a
���`hmasked_u���`a[���bmia4���`a]���`a ���aoa=���`a ���bmid1000���`b  ���bc1x2# Bad value that should not be plotted when masked���`a
���`hmasked_u���`a[���bmia4���`a]���`a ���aoa=���`a ���`bnp���aoa.���`bma���aoa.���`fmasked���`a
���`a
���bc1xM#############################################################################���`a
���bc1xF# Identical plot to panel 2 in the first figure, but with the point at���`a
���bc1x# (0.5, 0.25) missing (masked)���`a
���`dfig2���`a,���`a ���`cax2���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`a)���`a
���`cax2���aoa.���`ebarbs���`a(���`ddata���`a[���bs1a'���bs1ax���bs1a'���`a]���`a,���`a ���`ddata���`a[���bs1a'���bs1ay���bs1a'���`a]���`a,���`a ���`hmasked_u���`a,���`a ���`ddata���`a[���bs1a'���bs1av���bs1a'���`a]���`a,���`a ���`flength���aoa=���bmia8���`a,���`a ���`epivot���aoa=���bs1a'���bs1fmiddle���bs1a'���`a)���`a
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
���bc1x?#    - `matplotlib.axes.Axes.barbs` / `matplotlib.pyplot.barbs`���`a
`dNone�