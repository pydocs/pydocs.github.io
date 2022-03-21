��������G���bsdy-"""
=======================================
Advanced quiver and quiverkey functions
=======================================

Demonstrates some more advanced options for `~.axes.Axes.quiver`.  For a simple
example refer to :doc:`/gallery/images_contours_and_fields/quiver_simple_demo`.

Note: The plot autoscaling does not take into account the arrows, so
those on the boundaries may reach out of the picture.  This is not an easy
problem to solve in a perfectly general way.  The recommended workaround is to
manually set the Axes limits in such a case.
"""���`a
���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���`a
���`aX���`a,���`a ���`aY���`a ���aoa=���`a ���`bnp���aoa.���`hmeshgrid���`a(���`bnp���aoa.���`farange���`a(���bmia0���`a,���`a ���bmia2���`a ���aoa*���`a ���`bnp���aoa.���`bpi���`a,���`a ���bmfb.2���`a)���`a,���`a ���`bnp���aoa.���`farange���`a(���bmia0���`a,���`a ���bmia2���`a ���aoa*���`a ���`bnp���aoa.���`bpi���`a,���`a ���bmfb.2���`a)���`a)���`a
���`aU���`a ���aoa=���`a ���`bnp���aoa.���`ccos���`a(���`aX���`a)���`a
���`aV���`a ���aoa=���`a ���`bnp���aoa.���`csin���`a(���`aY���`a)���`a
���`a
���bc1xO###############################################################################���`a
���`a
���`dfig1���`a,���`a ���`cax1���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`a)���`a
���`cax1���aoa.���`iset_title���`a(���bs1a'���bs1x&Arrows scale with plot width, not view���bs1a'���`a)���`a
���`aQ���`a ���aoa=���`a ���`cax1���aoa.���`fquiver���`a(���`aX���`a,���`a ���`aY���`a,���`a ���`aU���`a,���`a ���`aV���`a,���`a ���`eunits���aoa=���bs1a'���bs1ewidth���bs1a'���`a)���`a
���`bqk���`a ���aoa=���`a ���`cax1���aoa.���`iquiverkey���`a(���`aQ���`a,���`a ���bmfc0.9���`a,���`a ���bmfc0.9���`a,���`a ���bmia2���`a,���`a ���bsaar���bs1a'���bs1c$2 ���bs1a\���bs1dfrac���bsic{m}���bsic{s}���bs1a$���bs1a'���`a,���`a ���`hlabelpos���aoa=���bs1a'���bs1aE���bs1a'���`a,���`a
���`s                   ���`kcoordinates���aoa=���bs1a'���bs1ffigure���bs1a'���`a)���`a
���`a
���bc1xO###############################################################################���`a
���`a
���`dfig2���`a,���`a ���`cax2���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`a)���`a
���`cax2���aoa.���`iset_title���`a(���bs2a"���bs2fpivot=���bs2a'���bs2cmid���bs2a'���bs2x; every third arrow; units=���bs2a'���bs2finches���bs2a'���bs2a"���`a)���`a
���`aQ���`a ���aoa=���`a ���`cax2���aoa.���`fquiver���`a(���`aX���`a[���`a:���`a:���bmia3���`a,���`a ���`a:���`a:���bmia3���`a]���`a,���`a ���`aY���`a[���`a:���`a:���bmia3���`a,���`a ���`a:���`a:���bmia3���`a]���`a,���`a ���`aU���`a[���`a:���`a:���bmia3���`a,���`a ���`a:���`a:���bmia3���`a]���`a,���`a ���`aV���`a[���`a:���`a:���bmia3���`a,���`a ���`a:���`a:���bmia3���`a]���`a,���`a
���`o               ���`epivot���aoa=���bs1a'���bs1cmid���bs1a'���`a,���`a ���`eunits���aoa=���bs1a'���bs1finches���bs1a'���`a)���`a
���`bqk���`a ���aoa=���`a ���`cax2���aoa.���`iquiverkey���`a(���`aQ���`a,���`a ���bmfc0.9���`a,���`a ���bmfc0.9���`a,���`a ���bmia1���`a,���`a ���bsaar���bs1a'���bs1c$1 ���bs1a\���bs1dfrac���bsic{m}���bsic{s}���bs1a$���bs1a'���`a,���`a ���`hlabelpos���aoa=���bs1a'���bs1aE���bs1a'���`a,���`a
���`s                   ���`kcoordinates���aoa=���bs1a'���bs1ffigure���bs1a'���`a)���`a
���`cax2���aoa.���`gscatter���`a(���`aX���`a[���`a:���`a:���bmia3���`a,���`a ���`a:���`a:���bmia3���`a]���`a,���`a ���`aY���`a[���`a:���`a:���bmia3���`a,���`a ���`a:���`a:���bmia3���`a]���`a,���`a ���`ecolor���aoa=���bs1a'���bs1ar���bs1a'���`a,���`a ���`as���aoa=���bmia5���`a)���`a
���`a
���bc1xO###############################################################################���`a
���`a
���bc1x%# sphinx_gallery_thumbnail_number = 3���`a
���`a
���`dfig3���`a,���`a ���`cax3���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`a)���`a
���`cax3���aoa.���`iset_title���`a(���bs2a"���bs2fpivot=���bs2a'���bs2ctip���bs2a'���bs2t; scales with x view���bs2a"���`a)���`a
���`aM���`a ���aoa=���`a ���`bnp���aoa.���`ehypot���`a(���`aU���`a,���`a ���`aV���`a)���`a
���`aQ���`a ���aoa=���`a ���`cax3���aoa.���`fquiver���`a(���`aX���`a,���`a ���`aY���`a,���`a ���`aU���`a,���`a ���`aV���`a,���`a ���`aM���`a,���`a ���`eunits���aoa=���bs1a'���bs1ax���bs1a'���`a,���`a ���`epivot���aoa=���bs1a'���bs1ctip���bs1a'���`a,���`a ���`ewidth���aoa=���bmfe0.022���`a,���`a
���`o               ���`escale���aoa=���bmia1���`a ���aoa/���`a ���bmfd0.15���`a)���`a
���`bqk���`a ���aoa=���`a ���`cax3���aoa.���`iquiverkey���`a(���`aQ���`a,���`a ���bmfc0.9���`a,���`a ���bmfc0.9���`a,���`a ���bmia1���`a,���`a ���bsaar���bs1a'���bs1c$1 ���bs1a\���bs1dfrac���bsic{m}���bsic{s}���bs1a$���bs1a'���`a,���`a ���`hlabelpos���aoa=���bs1a'���bs1aE���bs1a'���`a,���`a
���`s                   ���`kcoordinates���aoa=���bs1a'���bs1ffigure���bs1a'���`a)���`a
���`cax3���aoa.���`gscatter���`a(���`aX���`a,���`a ���`aY���`a,���`a ���`ecolor���aoa=���bs1a'���bs1c0.5���bs1a'���`a,���`a ���`as���aoa=���bmia1���`a)���`a
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
���bc1xA#    - `matplotlib.axes.Axes.quiver` / `matplotlib.pyplot.quiver`���`a
���bc1xG#    - `matplotlib.axes.Axes.quiverkey` / `matplotlib.pyplot.quiverkey`���`a
`dNone�