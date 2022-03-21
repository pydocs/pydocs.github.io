��������9���bsdx�"""
=========================
3D surface (checkerboard)
=========================

Demonstrates plotting a 3D surface colored in a checkerboard pattern.
"""���`a
���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���bkndfrom���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfticker���`a ���bknfimport���`a ���`mLinearLocator���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���`a
���`a
���`bax���`a ���aoa=���`a ���`cplt���aoa.���`ffigure���`a(���`a)���aoa.���`kadd_subplot���`a(���`jprojection���aoa=���bs1a'���bs1b3d���bs1a'���`a)���`a
���`a
���bc1l# Make data.���`a
���`aX���`a ���aoa=���`a ���`bnp���aoa.���`farange���`a(���aoa-���bmia5���`a,���`a ���bmia5���`a,���`a ���bmfd0.25���`a)���`a
���`dxlen���`a ���aoa=���`a ���bnbclen���`a(���`aX���`a)���`a
���`aY���`a ���aoa=���`a ���`bnp���aoa.���`farange���`a(���aoa-���bmia5���`a,���`a ���bmia5���`a,���`a ���bmfd0.25���`a)���`a
���`dylen���`a ���aoa=���`a ���bnbclen���`a(���`aY���`a)���`a
���`aX���`a,���`a ���`aY���`a ���aoa=���`a ���`bnp���aoa.���`hmeshgrid���`a(���`aX���`a,���`a ���`aY���`a)���`a
���`aR���`a ���aoa=���`a ���`bnp���aoa.���`dsqrt���`a(���`aX���aoa*���aoa*���bmia2���`a ���aoa+���`a ���`aY���aoa*���aoa*���bmia2���`a)���`a
���`aZ���`a ���aoa=���`a ���`bnp���aoa.���`csin���`a(���`aR���`a)���`a
���`a
���bc1xK# Create an empty array of strings with the same shape as the meshgrid, and���`a
���bc1x8# populate it with two colors in a checkerboard pattern.���`a
���`jcolortuple���`a ���aoa=���`a ���`a(���bs1a'���bs1ay���bs1a'���`a,���`a ���bs1a'���bs1ab���bs1a'���`a)���`a
���`fcolors���`a ���aoa=���`a ���`bnp���aoa.���`eempty���`a(���`aX���aoa.���`eshape���`a,���`a ���`edtype���aoa=���bnbcstr���`a)���`a
���akcfor���`a ���`ay���`a ���bowbin���`a ���bnberange���`a(���`dylen���`a)���`a:���`a
���`d    ���akcfor���`a ���`ax���`a ���bowbin���`a ���bnberange���`a(���`dxlen���`a)���`a:���`a
���`h        ���`fcolors���`a[���`ay���`a,���`a ���`ax���`a]���`a ���aoa=���`a ���`jcolortuple���`a[���`a(���`ax���`a ���aoa+���`a ���`ay���`a)���`a ���aoa%���`a ���bnbclen���`a(���`jcolortuple���`a)���`a]���`a
���`a
���bc1xA# Plot the surface with face colors taken from the array we made.���`a
���`dsurf���`a ���aoa=���`a ���`bax���aoa.���`lplot_surface���`a(���`aX���`a,���`a ���`aY���`a,���`a ���`aZ���`a,���`a ���`jfacecolors���aoa=���`fcolors���`a,���`a ���`ilinewidth���aoa=���bmia0���`a)���`a
���`a
���bc1w# Customize the z axis.���`a
���`bax���aoa.���`hset_zlim���`a(���aoa-���bmia1���`a,���`a ���bmia1���`a)���`a
���`bax���aoa.���`ezaxis���aoa.���`qset_major_locator���`a(���`mLinearLocator���`a(���bmia6���`a)���`a)���`a
���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
`dNone�