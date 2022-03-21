������������bsdy?"""
=================================
3D surface with polar coordinates
=================================

Demonstrates plotting a surface defined in polar coordinates.
Uses the reversed version of the YlGnBu colormap.
Also demonstrates writing axis labels with latex math mode.

Example contributed by Armin Moser.
"""���`a
���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���`a
���`a
���`cfig���`a ���aoa=���`a ���`cplt���aoa.���`ffigure���`a(���`a)���`a
���`bax���`a ���aoa=���`a ���`cfig���aoa.���`kadd_subplot���`a(���`jprojection���aoa=���bs1a'���bs1b3d���bs1a'���`a)���`a
���`a
���bc1xC# Create the mesh in polar coordinates and compute corresponding Z.���`a
���`ar���`a ���aoa=���`a ���`bnp���aoa.���`hlinspace���`a(���bmia0���`a,���`a ���bmfd1.25���`a,���`a ���bmib50���`a)���`a
���`ap���`a ���aoa=���`a ���`bnp���aoa.���`hlinspace���`a(���bmia0���`a,���`a ���bmia2���aoa*���`bnp���aoa.���`bpi���`a,���`a ���bmib50���`a)���`a
���`aR���`a,���`a ���`aP���`a ���aoa=���`a ���`bnp���aoa.���`hmeshgrid���`a(���`ar���`a,���`a ���`ap���`a)���`a
���`aZ���`a ���aoa=���`a ���`a(���`a(���`aR���aoa*���aoa*���bmia2���`a ���aoa-���`a ���bmia1���`a)���aoa*���aoa*���bmia2���`a)���`a
���`a
���bc1x+# Express the mesh in the cartesian system.���`a
���`aX���`a,���`a ���`aY���`a ���aoa=���`a ���`aR���aoa*���`bnp���aoa.���`ccos���`a(���`aP���`a)���`a,���`a ���`aR���aoa*���`bnp���aoa.���`csin���`a(���`aP���`a)���`a
���`a
���bc1s# Plot the surface.���`a
���`bax���aoa.���`lplot_surface���`a(���`aX���`a,���`a ���`aY���`a,���`a ���`aZ���`a,���`a ���`dcmap���aoa=���`cplt���aoa.���`bcm���aoa.���`hYlGnBu_r���`a)���`a
���`a
���bc1x-# Tweak the limits and add latex math labels.���`a
���`bax���aoa.���`hset_zlim���`a(���bmia0���`a,���`a ���bmia1���`a)���`a
���`bax���aoa.���`jset_xlabel���`a(���bsaar���bs1a'���bs1a$���bs1a\���bs1dphi_���bs1a\���bs1fmathrm���bsif{real}���bs1a$���bs1a'���`a)���`a
���`bax���aoa.���`jset_ylabel���`a(���bsaar���bs1a'���bs1a$���bs1a\���bs1dphi_���bs1a\���bs1fmathrm���bsid{im}���bs1a$���bs1a'���`a)���`a
���`bax���aoa.���`jset_zlabel���`a(���bsaar���bs1a'���bs1c$V(���bs1a\���bs1ephi)$���bs1a'���`a)���`a
���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
`dNone�