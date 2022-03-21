������������bsdyW"""
===================
3D box surface plot
===================

Given data on a gridded volume ``X``, ``Y``, ``Z``, this example plots the
data values on the volume surfaces.

The strategy is to select the data from each surface and plot
contours separately using `.axes3d.Axes3D.contourf` with appropriate
parameters *zdir* and *offset*.
"""���`a
���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���`a
���bc1s# Define dimensions���`a
���`bNx���`a,���`a ���`bNy���`a,���`a ���`bNz���`a ���aoa=���`a ���bmic100���`a,���`a ���bmic300���`a,���`a ���bmic500���`a
���`aX���`a,���`a ���`aY���`a,���`a ���`aZ���`a ���aoa=���`a ���`bnp���aoa.���`hmeshgrid���`a(���`bnp���aoa.���`farange���`a(���`bNx���`a)���`a,���`a ���`bnp���aoa.���`farange���`a(���`bNy���`a)���`a,���`a ���aoa-���`bnp���aoa.���`farange���`a(���`bNz���`a)���`a)���`a
���`a
���bc1r# Create fake data���`a
���`ddata���`a ���aoa=���`a ���`a(���`a(���`a(���`aX���aoa+���bmic100���`a)���aoa*���aoa*���bmia2���`a ���aoa+���`a ���`a(���`aY���aoa-���bmib20���`a)���aoa*���aoa*���bmia2���`a ���aoa+���`a ���bmia2���aoa*���`aZ���`a)���aoa/���bmid1000���aoa+���bmia1���`a)���`a
���`a
���`bkw���`a ���aoa=���`a ���`a{���`a
���`d    ���bs1a'���bs1dvmin���bs1a'���`a:���`a ���`ddata���aoa.���`cmin���`a(���`a)���`a,���`a
���`d    ���bs1a'���bs1dvmax���bs1a'���`a:���`a ���`ddata���aoa.���`cmax���`a(���`a)���`a,���`a
���`d    ���bs1a'���bs1flevels���bs1a'���`a:���`a ���`bnp���aoa.���`hlinspace���`a(���`ddata���aoa.���`cmin���`a(���`a)���`a,���`a ���`ddata���aoa.���`cmax���`a(���`a)���`a,���`a ���bmib10���`a)���`a,���`a
���`a}���`a
���`a
���bc1x# Create a figure with 3D ax���`a
���`cfig���`a ���aoa=���`a ���`cplt���aoa.���`ffigure���`a(���`gfigsize���aoa=���`a(���bmia5���`a,���`a ���bmia4���`a)���`a)���`a
���`bax���`a ���aoa=���`a ���`cfig���aoa.���`kadd_subplot���`a(���bmic111���`a,���`a ���`jprojection���aoa=���bs1a'���bs1b3d���bs1a'���`a)���`a
���`a
���bc1w# Plot contour surfaces���`a
���`a_���`a ���aoa=���`a ���`bax���aoa.���`hcontourf���`a(���`a
���`d    ���`aX���`a[���`a:���`a,���`a ���`a:���`a,���`a ���bmia0���`a]���`a,���`a ���`aY���`a[���`a:���`a,���`a ���`a:���`a,���`a ���bmia0���`a]���`a,���`a ���`ddata���`a[���`a:���`a,���`a ���`a:���`a,���`a ���bmia0���`a]���`a,���`a
���`d    ���`dzdir���aoa=���bs1a'���bs1az���bs1a'���`a,���`a ���`foffset���aoa=���bmia0���`a,���`a ���aoa*���aoa*���`bkw���`a
���`a)���`a
���`a_���`a ���aoa=���`a ���`bax���aoa.���`hcontourf���`a(���`a
���`d    ���`aX���`a[���bmia0���`a,���`a ���`a:���`a,���`a ���`a:���`a]���`a,���`a ���`ddata���`a[���bmia0���`a,���`a ���`a:���`a,���`a ���`a:���`a]���`a,���`a ���`aZ���`a[���bmia0���`a,���`a ���`a:���`a,���`a ���`a:���`a]���`a,���`a
���`d    ���`dzdir���aoa=���bs1a'���bs1ay���bs1a'���`a,���`a ���`foffset���aoa=���bmia0���`a,���`a ���aoa*���aoa*���`bkw���`a
���`a)���`a
���`aC���`a ���aoa=���`a ���`bax���aoa.���`hcontourf���`a(���`a
���`d    ���`ddata���`a[���`a:���`a,���`a ���aoa-���bmia1���`a,���`a ���`a:���`a]���`a,���`a ���`aY���`a[���`a:���`a,���`a ���aoa-���bmia1���`a,���`a ���`a:���`a]���`a,���`a ���`aZ���`a[���`a:���`a,���`a ���aoa-���bmia1���`a,���`a ���`a:���`a]���`a,���`a
���`d    ���`dzdir���aoa=���bs1a'���bs1ax���bs1a'���`a,���`a ���`foffset���aoa=���`aX���aoa.���`cmax���`a(���`a)���`a,���`a ���aoa*���aoa*���`bkw���`a
���`a)���`a
���bc1d# --���`a
���`a
���`a
���bc1x*# Set limits of the plot from coord limits���`a
���`dxmin���`a,���`a ���`dxmax���`a ���aoa=���`a ���`aX���aoa.���`cmin���`a(���`a)���`a,���`a ���`aX���aoa.���`cmax���`a(���`a)���`a
���`dymin���`a,���`a ���`dymax���`a ���aoa=���`a ���`aY���aoa.���`cmin���`a(���`a)���`a,���`a ���`aY���aoa.���`cmax���`a(���`a)���`a
���`dzmin���`a,���`a ���`dzmax���`a ���aoa=���`a ���`aZ���aoa.���`cmin���`a(���`a)���`a,���`a ���`aZ���aoa.���`cmax���`a(���`a)���`a
���`bax���aoa.���`cset���`a(���`dxlim���aoa=���`a[���`dxmin���`a,���`a ���`dxmax���`a]���`a,���`a ���`dylim���aoa=���`a[���`dymin���`a,���`a ���`dymax���`a]���`a,���`a ���`dzlim���aoa=���`a[���`dzmin���`a,���`a ���`dzmax���`a]���`a)���`a
���`a
���bc1l# Plot edges���`a
���`hedges_kw���`a ���aoa=���`a ���bnbddict���`a(���`ecolor���aoa=���bs1a'���bs1c0.4���bs1a'���`a,���`a ���`ilinewidth���aoa=���bmia1���`a,���`a ���`fzorder���aoa=���bmfc1e3���`a)���`a
���`bax���aoa.���`dplot���`a(���`a[���`dxmax���`a,���`a ���`dxmax���`a]���`a,���`a ���`a[���`dymin���`a,���`a ���`dymax���`a]���`a,���`a ���bmia0���`a,���`a ���aoa*���aoa*���`hedges_kw���`a)���`a
���`bax���aoa.���`dplot���`a(���`a[���`dxmin���`a,���`a ���`dxmax���`a]���`a,���`a ���`a[���`dymin���`a,���`a ���`dymin���`a]���`a,���`a ���bmia0���`a,���`a ���aoa*���aoa*���`hedges_kw���`a)���`a
���`bax���aoa.���`dplot���`a(���`a[���`dxmax���`a,���`a ���`dxmax���`a]���`a,���`a ���`a[���`dymin���`a,���`a ���`dymin���`a]���`a,���`a ���`a[���`dzmin���`a,���`a ���`dzmax���`a]���`a,���`a ���aoa*���aoa*���`hedges_kw���`a)���`a
���`a
���bc1w# Set labels and zticks���`a
���`bax���aoa.���`cset���`a(���`a
���`d    ���`fxlabel���aoa=���bs1a'���bs1fX [km]���bs1a'���`a,���`a
���`d    ���`fylabel���aoa=���bs1a'���bs1fY [km]���bs1a'���`a,���`a
���`d    ���`fzlabel���aoa=���bs1a'���bs1eZ [m]���bs1a'���`a,���`a
���`d    ���`fzticks���aoa=���`a[���bmia0���`a,���`a ���aoa-���bmic150���`a,���`a ���aoa-���bmic300���`a,���`a ���aoa-���bmic450���`a]���`a,���`a
���`a)���`a
���`a
���bc1x# Set distance and angle view���`a
���`bax���aoa.���`iview_init���`a(���bmib40���`a,���`a ���aoa-���bmib30���`a)���`a
���`bax���aoa.���`ddist���`a ���aoa=���`a ���bmib11���`a
���`a
���bc1j# Colorbar���`a
���`cfig���aoa.���`hcolorbar���`a(���`aC���`a,���`a ���`bax���aoa=���`bax���`a,���`a ���`hfraction���aoa=���bmfd0.02���`a,���`a ���`cpad���aoa=���bmfc0.1���`a,���`a ���`elabel���aoa=���bs1a'���bs1lName [units]���bs1a'���`a)���`a
���`a
���bc1m# Show Figure���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
`dNone�