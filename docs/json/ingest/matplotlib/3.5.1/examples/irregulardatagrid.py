ŸØÇÅŸ¥ÉôTŸ±Çbsdyè"""
=======================================
Contour plot of irregularly spaced data
=======================================

Comparison of a contour plot of irregularly spaced data interpolated
on a regular grid versus a tricontour plot for an unstructured triangular grid.

Since `~.axes.Axes.contour` and `~.axes.Axes.contourf` expect the data to live
on a regular grid, plotting a contour plot of irregularly spaced data requires
different methods. The two options are:

* Interpolate the data to a regular grid first. This can be done with on-board
  means, e.g. via `~.tri.LinearTriInterpolator` or using external functionality
  e.g. via `scipy.interpolate.griddata`. Then plot the interpolated data with
  the usual `~.axes.Axes.contour`.
* Directly use `~.axes.Axes.tricontour` or `~.axes.Axes.tricontourf` which will
  perform a triangulation internally.

This example shows both methods in action.
"""Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±ÇbknfimportŸ±Ç`a Ÿ±ÇbnnŸ¢ÑjmatplotlibŸ†Ñjmatplotlibe3.5.1fmodulejmatplotlibfmoduleıŸ±Çbnna.Ÿ±ÇbnnfpyplotŸ±Ç`a Ÿ±ÇakbasŸ±Ç`a Ÿ±ÇbnncpltŸ±Ç`a
Ÿ±ÇbknfimportŸ±Ç`a Ÿ±ÇbnnŸ¢ÑjmatplotlibŸ†Ñjmatplotlibe3.5.1fmodulejmatplotlibfmoduleıŸ±Çbnna.Ÿ±ÇbnnctriŸ±Ç`a Ÿ±ÇakbasŸ±Ç`a Ÿ±ÇbnnctriŸ±Ç`a
Ÿ±ÇbknfimportŸ±Ç`a Ÿ±ÇbnnŸ¢ÑenumpyŸ†Ñenumpyf1.22.3fmoduleenumpyfmoduleıŸ±Ç`a Ÿ±ÇakbasŸ±Ç`a Ÿ±ÇbnnbnpŸ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`frandomŸ±Çaoa.Ÿ±Ç`dseedŸ±Ç`a(Ÿ±Çbmih19680801Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`dnptsŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Çbmic200Ÿ±Ç`a
Ÿ±Ç`fngridxŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Çbmic100Ÿ±Ç`a
Ÿ±Ç`fngridyŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Çbmic200Ÿ±Ç`a
Ÿ±Ç`axŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`frandomŸ±Çaoa.Ÿ±Ç`guniformŸ±Ç`a(Ÿ±Çaoa-Ÿ±Çbmia2Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia2Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dnptsŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`ayŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`frandomŸ±Çaoa.Ÿ±Ç`guniformŸ±Ç`a(Ÿ±Çaoa-Ÿ±Çbmia2Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia2Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dnptsŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`azŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`axŸ±Ç`a Ÿ±Çaoa*Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`cexpŸ±Ç`a(Ÿ±Çaoa-Ÿ±Ç`axŸ±Çaoa*Ÿ±Çaoa*Ÿ±Çbmia2Ÿ±Ç`a Ÿ±Çaoa-Ÿ±Ç`a Ÿ±Ç`ayŸ±Çaoa*Ÿ±Çaoa*Ÿ±Çbmia2Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`cfigŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`a(Ÿ±Ç`cax1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`cax2Ÿ±Ç`a)Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`hsubplotsŸ±Ç`a(Ÿ±Ç`enrowsŸ±Çaoa=Ÿ±Çbmia2Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1x# -----------------------Ÿ±Ç`a
Ÿ±Çbc1x# Interpolation on a gridŸ±Ç`a
Ÿ±Çbc1x# -----------------------Ÿ±Ç`a
Ÿ±Çbc1x7# A contour plot of irregularly spaced data coordinatesŸ±Ç`a
Ÿ±Çbc1x# via interpolation on a grid.Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1x# Create grid values first.Ÿ±Ç`a
Ÿ±Ç`bxiŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`hlinspaceŸ±Ç`a(Ÿ±Çaoa-Ÿ±Çbmfc2.1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfc2.1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`fngridxŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`byiŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`hlinspaceŸ±Ç`a(Ÿ±Çaoa-Ÿ±Çbmfc2.1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfc2.1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`fngridyŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1xE# Linearly interpolate the data (x, y) on a grid defined by (xi, yi).Ÿ±Ç`a
Ÿ±Ç`ftriangŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`ctriŸ±Çaoa.Ÿ±Ç`mTriangulationŸ±Ç`a(Ÿ±Ç`axŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ayŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`linterpolatorŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`ctriŸ±Çaoa.Ÿ±Ç`uLinearTriInterpolatorŸ±Ç`a(Ÿ±Ç`ftriangŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`azŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`bXiŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`bYiŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`hmeshgridŸ±Ç`a(Ÿ±Ç`bxiŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`byiŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`bziŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`linterpolatorŸ±Ç`a(Ÿ±Ç`bXiŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`bYiŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1xJ# Note that scipy.interpolate provides means to interpolate data on a gridŸ±Ç`a
Ÿ±Çbc1xI# as well. The following would be an alternative to the four lines above:Ÿ±Ç`a
Ÿ±Çbc1x(# from scipy.interpolate import griddataŸ±Ç`a
Ÿ±Çbc1xG# zi = griddata((x, y), z, (xi[None, :], yi[:, None]), method='linear')Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`cax1Ÿ±Çaoa.Ÿ±Ç`gcontourŸ±Ç`a(Ÿ±Ç`bxiŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`byiŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`bziŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`flevelsŸ±Çaoa=Ÿ±Çbmib14Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`jlinewidthsŸ±Çaoa=Ÿ±Çbmfc0.5Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`fcolorsŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1akŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`ecntr1Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cax1Ÿ±Çaoa.Ÿ±Ç`hcontourfŸ±Ç`a(Ÿ±Ç`bxiŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`byiŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`bziŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`flevelsŸ±Çaoa=Ÿ±Çbmib14Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dcmapŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2fRdBu_rŸ±Çbs2a"Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`cfigŸ±Çaoa.Ÿ±Ç`hcolorbarŸ±Ç`a(Ÿ±Ç`ecntr1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`baxŸ±Çaoa=Ÿ±Ç`cax1Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cax1Ÿ±Çaoa.Ÿ±Ç`dplotŸ±Ç`a(Ÿ±Ç`axŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ayŸ±Ç`a,Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1bkoŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`bmsŸ±Çaoa=Ÿ±Çbmia3Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cax1Ÿ±Çaoa.Ÿ±Ç`csetŸ±Ç`a(Ÿ±Ç`dxlimŸ±Çaoa=Ÿ±Ç`a(Ÿ±Çaoa-Ÿ±Çbmia2Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia2Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dylimŸ±Çaoa=Ÿ±Ç`a(Ÿ±Çaoa-Ÿ±Çbmia2Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia2Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cax1Ÿ±Çaoa.Ÿ±Ç`iset_titleŸ±Ç`a(Ÿ±Çbs1a'Ÿ±Çbs1rgrid and contour (Ÿ±Çbsib%dŸ±Çbs1i points, Ÿ±Çbsib%dŸ±Çbs1m grid points)Ÿ±Çbs1a'Ÿ±Ç`a Ÿ±Çaoa%Ÿ±Ç`a
Ÿ±Ç`n              Ÿ±Ç`a(Ÿ±Ç`dnptsŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`fngridxŸ±Ç`a Ÿ±Çaoa*Ÿ±Ç`a Ÿ±Ç`fngridyŸ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1l# ----------Ÿ±Ç`a
Ÿ±Çbc1l# TricontourŸ±Ç`a
Ÿ±Çbc1l# ----------Ÿ±Ç`a
Ÿ±Çbc1x?# Directly supply the unordered, irregularly spaced coordinatesŸ±Ç`a
Ÿ±Çbc1p# to tricontour.Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`cax2Ÿ±Çaoa.Ÿ±Ç`jtricontourŸ±Ç`a(Ÿ±Ç`axŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ayŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`azŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`flevelsŸ±Çaoa=Ÿ±Çbmib14Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`jlinewidthsŸ±Çaoa=Ÿ±Çbmfc0.5Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`fcolorsŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1akŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`ecntr2Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cax2Ÿ±Çaoa.Ÿ±Ç`ktricontourfŸ±Ç`a(Ÿ±Ç`axŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ayŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`azŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`flevelsŸ±Çaoa=Ÿ±Çbmib14Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dcmapŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2fRdBu_rŸ±Çbs2a"Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`cfigŸ±Çaoa.Ÿ±Ç`hcolorbarŸ±Ç`a(Ÿ±Ç`ecntr2Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`baxŸ±Çaoa=Ÿ±Ç`cax2Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cax2Ÿ±Çaoa.Ÿ±Ç`dplotŸ±Ç`a(Ÿ±Ç`axŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ayŸ±Ç`a,Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1bkoŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`bmsŸ±Çaoa=Ÿ±Çbmia3Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cax2Ÿ±Çaoa.Ÿ±Ç`csetŸ±Ç`a(Ÿ±Ç`dxlimŸ±Çaoa=Ÿ±Ç`a(Ÿ±Çaoa-Ÿ±Çbmia2Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia2Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dylimŸ±Çaoa=Ÿ±Ç`a(Ÿ±Çaoa-Ÿ±Çbmia2Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia2Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cax2Ÿ±Çaoa.Ÿ±Ç`iset_titleŸ±Ç`a(Ÿ±Çbs1a'Ÿ±Çbs1ltricontour (Ÿ±Çbsib%dŸ±Çbs1h points)Ÿ±Çbs1a'Ÿ±Ç`a Ÿ±Çaoa%Ÿ±Ç`a Ÿ±Ç`dnptsŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`osubplots_adjustŸ±Ç`a(Ÿ±Ç`fhspaceŸ±Çaoa=Ÿ±Çbmfc0.5Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`dshowŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1xM#############################################################################Ÿ±Ç`a
Ÿ±Çbc1a#Ÿ±Ç`a
Ÿ±Çbc1x# .. admonition:: ReferencesŸ±Ç`a
Ÿ±Çbc1a#Ÿ±Ç`a
Ÿ±Çbc1xN#    The use of the following functions, methods, classes and modules is shownŸ±Ç`a
Ÿ±Çbc1u#    in this example:Ÿ±Ç`a
Ÿ±Çbc1a#Ÿ±Ç`a
Ÿ±Çbc1xC#    - `matplotlib.axes.Axes.contour` / `matplotlib.pyplot.contour`Ÿ±Ç`a
Ÿ±Çbc1xE#    - `matplotlib.axes.Axes.contourf` / `matplotlib.pyplot.contourf`Ÿ±Ç`a
Ÿ±Çbc1xI#    - `matplotlib.axes.Axes.tricontour` / `matplotlib.pyplot.tricontour`Ÿ±Ç`a
Ÿ±Çbc1xK#    - `matplotlib.axes.Axes.tricontourf` / `matplotlib.pyplot.tricontourf`Ÿ±Ç`a
`dNoneˆ