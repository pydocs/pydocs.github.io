ŸØÇÅŸ¥ÉôGŸ±Çbsdy-"""
=======================================
Advanced quiver and quiverkey functions
=======================================

Demonstrates some more advanced options for `~.axes.Axes.quiver`.  For a simple
example refer to :doc:`/gallery/images_contours_and_fields/quiver_simple_demo`.

Note: The plot autoscaling does not take into account the arrows, so
those on the boundaries may reach out of the picture.  This is not an easy
problem to solve in a perfectly general way.  The recommended workaround is to
manually set the Axes limits in such a case.
"""Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±ÇbknfimportŸ±Ç`a Ÿ±ÇbnnŸ¢ÑjmatplotlibŸ†Ñjmatplotlibe3.5.1fmodulejmatplotlibfmoduleıŸ±Çbnna.Ÿ±ÇbnnfpyplotŸ±Ç`a Ÿ±ÇakbasŸ±Ç`a Ÿ±ÇbnncpltŸ±Ç`a
Ÿ±ÇbknfimportŸ±Ç`a Ÿ±ÇbnnŸ¢ÑenumpyŸ†Ñenumpyf1.22.3fmoduleenumpyfmoduleıŸ±Ç`a Ÿ±ÇakbasŸ±Ç`a Ÿ±ÇbnnbnpŸ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`aXŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`aYŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`hmeshgridŸ±Ç`a(Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`farangeŸ±Ç`a(Ÿ±Çbmia0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia2Ÿ±Ç`a Ÿ±Çaoa*Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`bpiŸ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfb.2Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`farangeŸ±Ç`a(Ÿ±Çbmia0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia2Ÿ±Ç`a Ÿ±Çaoa*Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`bpiŸ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfb.2Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`aUŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`ccosŸ±Ç`a(Ÿ±Ç`aXŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`aVŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`csinŸ±Ç`a(Ÿ±Ç`aYŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1xO###############################################################################Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`dfig1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`cax1Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`hsubplotsŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cax1Ÿ±Çaoa.Ÿ±Ç`iset_titleŸ±Ç`a(Ÿ±Çbs1a'Ÿ±Çbs1x&Arrows scale with plot width, not viewŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`aQŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cax1Ÿ±Çaoa.Ÿ±Ç`fquiverŸ±Ç`a(Ÿ±Ç`aXŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`aYŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`aUŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`aVŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`eunitsŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1ewidthŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`bqkŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cax1Ÿ±Çaoa.Ÿ±Ç`iquiverkeyŸ±Ç`a(Ÿ±Ç`aQŸ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfc0.9Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfc0.9Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia2Ÿ±Ç`a,Ÿ±Ç`a Ÿ±ÇbsaarŸ±Çbs1a'Ÿ±Çbs1c$2 Ÿ±Çbs1a\Ÿ±Çbs1dfracŸ±Çbsic{m}Ÿ±Çbsic{s}Ÿ±Çbs1a$Ÿ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`hlabelposŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1aEŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`s                   Ÿ±Ç`kcoordinatesŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1ffigureŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1xO###############################################################################Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`dfig2Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`cax2Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`hsubplotsŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cax2Ÿ±Çaoa.Ÿ±Ç`iset_titleŸ±Ç`a(Ÿ±Çbs2a"Ÿ±Çbs2fpivot=Ÿ±Çbs2a'Ÿ±Çbs2cmidŸ±Çbs2a'Ÿ±Çbs2x; every third arrow; units=Ÿ±Çbs2a'Ÿ±Çbs2finchesŸ±Çbs2a'Ÿ±Çbs2a"Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`aQŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cax2Ÿ±Çaoa.Ÿ±Ç`fquiverŸ±Ç`a(Ÿ±Ç`aXŸ±Ç`a[Ÿ±Ç`a:Ÿ±Ç`a:Ÿ±Çbmia3Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`a:Ÿ±Ç`a:Ÿ±Çbmia3Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`aYŸ±Ç`a[Ÿ±Ç`a:Ÿ±Ç`a:Ÿ±Çbmia3Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`a:Ÿ±Ç`a:Ÿ±Çbmia3Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`aUŸ±Ç`a[Ÿ±Ç`a:Ÿ±Ç`a:Ÿ±Çbmia3Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`a:Ÿ±Ç`a:Ÿ±Çbmia3Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`aVŸ±Ç`a[Ÿ±Ç`a:Ÿ±Ç`a:Ÿ±Çbmia3Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`a:Ÿ±Ç`a:Ÿ±Çbmia3Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`o               Ÿ±Ç`epivotŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1cmidŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`eunitsŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1finchesŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`bqkŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cax2Ÿ±Çaoa.Ÿ±Ç`iquiverkeyŸ±Ç`a(Ÿ±Ç`aQŸ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfc0.9Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfc0.9Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±ÇbsaarŸ±Çbs1a'Ÿ±Çbs1c$1 Ÿ±Çbs1a\Ÿ±Çbs1dfracŸ±Çbsic{m}Ÿ±Çbsic{s}Ÿ±Çbs1a$Ÿ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`hlabelposŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1aEŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`s                   Ÿ±Ç`kcoordinatesŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1ffigureŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cax2Ÿ±Çaoa.Ÿ±Ç`gscatterŸ±Ç`a(Ÿ±Ç`aXŸ±Ç`a[Ÿ±Ç`a:Ÿ±Ç`a:Ÿ±Çbmia3Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`a:Ÿ±Ç`a:Ÿ±Çbmia3Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`aYŸ±Ç`a[Ÿ±Ç`a:Ÿ±Ç`a:Ÿ±Çbmia3Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`a:Ÿ±Ç`a:Ÿ±Çbmia3Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ecolorŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1arŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`asŸ±Çaoa=Ÿ±Çbmia5Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1xO###############################################################################Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1x%# sphinx_gallery_thumbnail_number = 3Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`dfig3Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`cax3Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`hsubplotsŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cax3Ÿ±Çaoa.Ÿ±Ç`iset_titleŸ±Ç`a(Ÿ±Çbs2a"Ÿ±Çbs2fpivot=Ÿ±Çbs2a'Ÿ±Çbs2ctipŸ±Çbs2a'Ÿ±Çbs2t; scales with x viewŸ±Çbs2a"Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`aMŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`ehypotŸ±Ç`a(Ÿ±Ç`aUŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`aVŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`aQŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cax3Ÿ±Çaoa.Ÿ±Ç`fquiverŸ±Ç`a(Ÿ±Ç`aXŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`aYŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`aUŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`aVŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`aMŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`eunitsŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1axŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`epivotŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1ctipŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ewidthŸ±Çaoa=Ÿ±Çbmfe0.022Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`o               Ÿ±Ç`escaleŸ±Çaoa=Ÿ±Çbmia1Ÿ±Ç`a Ÿ±Çaoa/Ÿ±Ç`a Ÿ±Çbmfd0.15Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`bqkŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cax3Ÿ±Çaoa.Ÿ±Ç`iquiverkeyŸ±Ç`a(Ÿ±Ç`aQŸ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfc0.9Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfc0.9Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±ÇbsaarŸ±Çbs1a'Ÿ±Çbs1c$1 Ÿ±Çbs1a\Ÿ±Çbs1dfracŸ±Çbsic{m}Ÿ±Çbsic{s}Ÿ±Çbs1a$Ÿ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`hlabelposŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1aEŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`s                   Ÿ±Ç`kcoordinatesŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1ffigureŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cax3Ÿ±Çaoa.Ÿ±Ç`gscatterŸ±Ç`a(Ÿ±Ç`aXŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`aYŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ecolorŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1c0.5Ÿ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`asŸ±Çaoa=Ÿ±Çbmia1Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`dshowŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1xM#############################################################################Ÿ±Ç`a
Ÿ±Çbc1a#Ÿ±Ç`a
Ÿ±Çbc1x# .. admonition:: ReferencesŸ±Ç`a
Ÿ±Çbc1a#Ÿ±Ç`a
Ÿ±Çbc1xN#    The use of the following functions, methods, classes and modules is shownŸ±Ç`a
Ÿ±Çbc1u#    in this example:Ÿ±Ç`a
Ÿ±Çbc1a#Ÿ±Ç`a
Ÿ±Çbc1xA#    - `matplotlib.axes.Axes.quiver` / `matplotlib.pyplot.quiver`Ÿ±Ç`a
Ÿ±Çbc1xG#    - `matplotlib.axes.Axes.quiverkey` / `matplotlib.pyplot.quiverkey`Ÿ±Ç`a
`dNoneˆ