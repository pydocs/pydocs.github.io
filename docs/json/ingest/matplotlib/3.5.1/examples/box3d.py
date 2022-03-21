ŸØÇÅŸ¥Éô˘Ÿ±ÇbsdyW"""
===================
3D box surface plot
===================

Given data on a gridded volume ``X``, ``Y``, ``Z``, this example plots the
data values on the volume surfaces.

The strategy is to select the data from each surface and plot
contours separately using `.axes3d.Axes3D.contourf` with appropriate
parameters *zdir* and *offset*.
"""Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±ÇbknfimportŸ±Ç`a Ÿ±ÇbnnŸ¢ÑjmatplotlibŸ†Ñjmatplotlibe3.5.1fmodulejmatplotlibfmoduleıŸ±Çbnna.Ÿ±ÇbnnfpyplotŸ±Ç`a Ÿ±ÇakbasŸ±Ç`a Ÿ±ÇbnncpltŸ±Ç`a
Ÿ±ÇbknfimportŸ±Ç`a Ÿ±ÇbnnŸ¢ÑenumpyŸ†Ñenumpyf1.22.3fmoduleenumpyfmoduleıŸ±Ç`a Ÿ±ÇakbasŸ±Ç`a Ÿ±ÇbnnbnpŸ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1s# Define dimensionsŸ±Ç`a
Ÿ±Ç`bNxŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`bNyŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`bNzŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Çbmic100Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmic300Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmic500Ÿ±Ç`a
Ÿ±Ç`aXŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`aYŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`aZŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`hmeshgridŸ±Ç`a(Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`farangeŸ±Ç`a(Ÿ±Ç`bNxŸ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`farangeŸ±Ç`a(Ÿ±Ç`bNyŸ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çaoa-Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`farangeŸ±Ç`a(Ÿ±Ç`bNzŸ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1r# Create fake dataŸ±Ç`a
Ÿ±Ç`ddataŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`a(Ÿ±Ç`a(Ÿ±Ç`a(Ÿ±Ç`aXŸ±Çaoa+Ÿ±Çbmic100Ÿ±Ç`a)Ÿ±Çaoa*Ÿ±Çaoa*Ÿ±Çbmia2Ÿ±Ç`a Ÿ±Çaoa+Ÿ±Ç`a Ÿ±Ç`a(Ÿ±Ç`aYŸ±Çaoa-Ÿ±Çbmib20Ÿ±Ç`a)Ÿ±Çaoa*Ÿ±Çaoa*Ÿ±Çbmia2Ÿ±Ç`a Ÿ±Çaoa+Ÿ±Ç`a Ÿ±Çbmia2Ÿ±Çaoa*Ÿ±Ç`aZŸ±Ç`a)Ÿ±Çaoa/Ÿ±Çbmid1000Ÿ±Çaoa+Ÿ±Çbmia1Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`bkwŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`a{Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Çbs1a'Ÿ±Çbs1dvminŸ±Çbs1a'Ÿ±Ç`a:Ÿ±Ç`a Ÿ±Ç`ddataŸ±Çaoa.Ÿ±Ç`cminŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Çbs1a'Ÿ±Çbs1dvmaxŸ±Çbs1a'Ÿ±Ç`a:Ÿ±Ç`a Ÿ±Ç`ddataŸ±Çaoa.Ÿ±Ç`cmaxŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Çbs1a'Ÿ±Çbs1flevelsŸ±Çbs1a'Ÿ±Ç`a:Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`hlinspaceŸ±Ç`a(Ÿ±Ç`ddataŸ±Çaoa.Ÿ±Ç`cminŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ddataŸ±Çaoa.Ÿ±Ç`cmaxŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmib10Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`a}Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1x# Create a figure with 3D axŸ±Ç`a
Ÿ±Ç`cfigŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`ffigureŸ±Ç`a(Ÿ±Ç`gfigsizeŸ±Çaoa=Ÿ±Ç`a(Ÿ±Çbmia5Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia4Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`baxŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cfigŸ±Çaoa.Ÿ±Ç`kadd_subplotŸ±Ç`a(Ÿ±Çbmic111Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`jprojectionŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1b3dŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1w# Plot contour surfacesŸ±Ç`a
Ÿ±Ç`a_Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`hcontourfŸ±Ç`a(Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`aXŸ±Ç`a[Ÿ±Ç`a:Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`a:Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia0Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`aYŸ±Ç`a[Ÿ±Ç`a:Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`a:Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia0Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ddataŸ±Ç`a[Ÿ±Ç`a:Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`a:Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia0Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`dzdirŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1azŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`foffsetŸ±Çaoa=Ÿ±Çbmia0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çaoa*Ÿ±Çaoa*Ÿ±Ç`bkwŸ±Ç`a
Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a_Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`hcontourfŸ±Ç`a(Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`aXŸ±Ç`a[Ÿ±Çbmia0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`a:Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`a:Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ddataŸ±Ç`a[Ÿ±Çbmia0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`a:Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`a:Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`aZŸ±Ç`a[Ÿ±Çbmia0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`a:Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`a:Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`dzdirŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1ayŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`foffsetŸ±Çaoa=Ÿ±Çbmia0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çaoa*Ÿ±Çaoa*Ÿ±Ç`bkwŸ±Ç`a
Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`aCŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`hcontourfŸ±Ç`a(Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`ddataŸ±Ç`a[Ÿ±Ç`a:Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çaoa-Ÿ±Çbmia1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`a:Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`aYŸ±Ç`a[Ÿ±Ç`a:Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çaoa-Ÿ±Çbmia1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`a:Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`aZŸ±Ç`a[Ÿ±Ç`a:Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çaoa-Ÿ±Çbmia1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`a:Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`dzdirŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1axŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`foffsetŸ±Çaoa=Ÿ±Ç`aXŸ±Çaoa.Ÿ±Ç`cmaxŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çaoa*Ÿ±Çaoa*Ÿ±Ç`bkwŸ±Ç`a
Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Çbc1d# --Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1x*# Set limits of the plot from coord limitsŸ±Ç`a
Ÿ±Ç`dxminŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dxmaxŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`aXŸ±Çaoa.Ÿ±Ç`cminŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`aXŸ±Çaoa.Ÿ±Ç`cmaxŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`dyminŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dymaxŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`aYŸ±Çaoa.Ÿ±Ç`cminŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`aYŸ±Çaoa.Ÿ±Ç`cmaxŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`dzminŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dzmaxŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`aZŸ±Çaoa.Ÿ±Ç`cminŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`aZŸ±Çaoa.Ÿ±Ç`cmaxŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`csetŸ±Ç`a(Ÿ±Ç`dxlimŸ±Çaoa=Ÿ±Ç`a[Ÿ±Ç`dxminŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dxmaxŸ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dylimŸ±Çaoa=Ÿ±Ç`a[Ÿ±Ç`dyminŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dymaxŸ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dzlimŸ±Çaoa=Ÿ±Ç`a[Ÿ±Ç`dzminŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dzmaxŸ±Ç`a]Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1l# Plot edgesŸ±Ç`a
Ÿ±Ç`hedges_kwŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±ÇbnbddictŸ±Ç`a(Ÿ±Ç`ecolorŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1c0.4Ÿ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ilinewidthŸ±Çaoa=Ÿ±Çbmia1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`fzorderŸ±Çaoa=Ÿ±Çbmfc1e3Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`dplotŸ±Ç`a(Ÿ±Ç`a[Ÿ±Ç`dxmaxŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dxmaxŸ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`a[Ÿ±Ç`dyminŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dymaxŸ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çaoa*Ÿ±Çaoa*Ÿ±Ç`hedges_kwŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`dplotŸ±Ç`a(Ÿ±Ç`a[Ÿ±Ç`dxminŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dxmaxŸ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`a[Ÿ±Ç`dyminŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dyminŸ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çaoa*Ÿ±Çaoa*Ÿ±Ç`hedges_kwŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`dplotŸ±Ç`a(Ÿ±Ç`a[Ÿ±Ç`dxmaxŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dxmaxŸ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`a[Ÿ±Ç`dyminŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dyminŸ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`a[Ÿ±Ç`dzminŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dzmaxŸ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çaoa*Ÿ±Çaoa*Ÿ±Ç`hedges_kwŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1w# Set labels and zticksŸ±Ç`a
Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`csetŸ±Ç`a(Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`fxlabelŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1fX [km]Ÿ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`fylabelŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1fY [km]Ÿ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`fzlabelŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1eZ [m]Ÿ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`fzticksŸ±Çaoa=Ÿ±Ç`a[Ÿ±Çbmia0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çaoa-Ÿ±Çbmic150Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çaoa-Ÿ±Çbmic300Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çaoa-Ÿ±Çbmic450Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1x# Set distance and angle viewŸ±Ç`a
Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`iview_initŸ±Ç`a(Ÿ±Çbmib40Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çaoa-Ÿ±Çbmib30Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`ddistŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Çbmib11Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1j# ColorbarŸ±Ç`a
Ÿ±Ç`cfigŸ±Çaoa.Ÿ±Ç`hcolorbarŸ±Ç`a(Ÿ±Ç`aCŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`baxŸ±Çaoa=Ÿ±Ç`baxŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`hfractionŸ±Çaoa=Ÿ±Çbmfd0.02Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`cpadŸ±Çaoa=Ÿ±Çbmfc0.1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`elabelŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1lName [units]Ÿ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1m# Show FigureŸ±Ç`a
Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`dshowŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
`dNoneˆ