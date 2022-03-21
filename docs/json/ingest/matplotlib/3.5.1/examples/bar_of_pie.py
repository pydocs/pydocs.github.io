ŸØÇÅŸ¥ÉôQŸ±ÇbsdyY"""
==========
Bar of pie
==========

Make a "bar of pie" chart where the first slice of the pie is
"exploded" into a bar chart with a further breakdown of said slice's
characteristics. The example demonstrates using a figure with multiple
sets of axes and using the axes patches list to add two ConnectionPatches
to link the subplot charts.
"""Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±ÇbknfimportŸ±Ç`a Ÿ±ÇbnnŸ¢ÑjmatplotlibŸ†Ñjmatplotlibe3.5.1fmodulejmatplotlibfmoduleıŸ±Çbnna.Ÿ±ÇbnnfpyplotŸ±Ç`a Ÿ±ÇakbasŸ±Ç`a Ÿ±ÇbnncpltŸ±Ç`a
Ÿ±ÇbkndfromŸ±Ç`a Ÿ±ÇbnnŸ¢ÑjmatplotlibŸ†Ñjmatplotlibe3.5.1fmodulejmatplotlibfmoduleıŸ±Çbnna.Ÿ±ÇbnngpatchesŸ±Ç`a Ÿ±ÇbknfimportŸ±Ç`a Ÿ±Ç`oConnectionPatchŸ±Ç`a
Ÿ±ÇbknfimportŸ±Ç`a Ÿ±ÇbnnŸ¢ÑenumpyŸ†Ñenumpyf1.22.3fmoduleenumpyfmoduleıŸ±Ç`a Ÿ±ÇakbasŸ±Ç`a Ÿ±ÇbnnbnpŸ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1x%# make figure and assign axis objectsŸ±Ç`a
Ÿ±Ç`cfigŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`a(Ÿ±Ç`cax1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`cax2Ÿ±Ç`a)Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`hsubplotsŸ±Ç`a(Ÿ±Çbmia1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia2Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`gfigsizeŸ±Çaoa=Ÿ±Ç`a(Ÿ±Çbmia9Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia5Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cfigŸ±Çaoa.Ÿ±Ç`osubplots_adjustŸ±Ç`a(Ÿ±Ç`fwspaceŸ±Çaoa=Ÿ±Çbmia0Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1v# pie chart parametersŸ±Ç`a
Ÿ±Ç`fratiosŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`a[Ÿ±Çbmfc.27Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfc.56Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfc.17Ÿ±Ç`a]Ÿ±Ç`a
Ÿ±Ç`flabelsŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`a[Ÿ±Çbs1a'Ÿ±Çbs1gApproveŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1jDisapproveŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1iUndecidedŸ±Çbs1a'Ÿ±Ç`a]Ÿ±Ç`a
Ÿ±Ç`gexplodeŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`a[Ÿ±Çbmfc0.1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia0Ÿ±Ç`a]Ÿ±Ç`a
Ÿ±Çbc1x3# rotate so that first wedge is split by the x-axisŸ±Ç`a
Ÿ±Ç`eangleŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Çaoa-Ÿ±Çbmic180Ÿ±Ç`a Ÿ±Çaoa*Ÿ±Ç`a Ÿ±Ç`fratiosŸ±Ç`a[Ÿ±Çbmia0Ÿ±Ç`a]Ÿ±Ç`a
Ÿ±Ç`cax1Ÿ±Çaoa.Ÿ±Ç`cpieŸ±Ç`a(Ÿ±Ç`fratiosŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`gautopctŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbsie%1.1fŸ±Çbsib%%Ÿ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`jstartangleŸ±Çaoa=Ÿ±Ç`eangleŸ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±Ç`flabelsŸ±Çaoa=Ÿ±Ç`flabelsŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`gexplodeŸ±Çaoa=Ÿ±Ç`gexplodeŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1v# bar chart parametersŸ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`dxposŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Çbmia0Ÿ±Ç`a
Ÿ±Ç`fbottomŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Çbmia0Ÿ±Ç`a
Ÿ±Ç`fratiosŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`a[Ÿ±Çbmfc.33Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfc.54Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfc.07Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfc.06Ÿ±Ç`a]Ÿ±Ç`a
Ÿ±Ç`ewidthŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Çbmfb.2Ÿ±Ç`a
Ÿ±Ç`fcolorsŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`a[Ÿ±Ç`a[Ÿ±Çbmfb.1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfb.3Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfb.5Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`a[Ÿ±Çbmfb.1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfb.3Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfb.3Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`a[Ÿ±Çbmfb.1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfb.3Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfb.7Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`a[Ÿ±Çbmfb.1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfb.3Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfb.9Ÿ±Ç`a]Ÿ±Ç`a]Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±ÇakcforŸ±Ç`a Ÿ±Ç`ajŸ±Ç`a Ÿ±ÇbowbinŸ±Ç`a Ÿ±ÇbnberangeŸ±Ç`a(Ÿ±ÇbnbclenŸ±Ç`a(Ÿ±Ç`fratiosŸ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`fheightŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`fratiosŸ±Ç`a[Ÿ±Ç`ajŸ±Ç`a]Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`cax2Ÿ±Çaoa.Ÿ±Ç`cbarŸ±Ç`a(Ÿ±Ç`dxposŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`fheightŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ewidthŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`fbottomŸ±Çaoa=Ÿ±Ç`fbottomŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ecolorŸ±Çaoa=Ÿ±Ç`fcolorsŸ±Ç`a[Ÿ±Ç`ajŸ±Ç`a]Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`dyposŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`fbottomŸ±Ç`a Ÿ±Çaoa+Ÿ±Ç`a Ÿ±Ç`cax2Ÿ±Çaoa.Ÿ±Ç`gpatchesŸ±Ç`a[Ÿ±Ç`ajŸ±Ç`a]Ÿ±Çaoa.Ÿ±Ç`jget_heightŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a Ÿ±Çaoa/Ÿ±Ç`a Ÿ±Çbmia2Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`fbottomŸ±Ç`a Ÿ±Çaoa+Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`fheightŸ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`cax2Ÿ±Çaoa.Ÿ±Ç`dtextŸ±Ç`a(Ÿ±Ç`dxposŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dyposŸ±Ç`a,Ÿ±Ç`a Ÿ±Çbs2a"Ÿ±Çbsib%dŸ±Çbsib%%Ÿ±Çbs2a"Ÿ±Ç`a Ÿ±Çaoa%Ÿ±Ç`a Ÿ±Ç`a(Ÿ±Ç`cax2Ÿ±Çaoa.Ÿ±Ç`gpatchesŸ±Ç`a[Ÿ±Ç`ajŸ±Ç`a]Ÿ±Çaoa.Ÿ±Ç`jget_heightŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a Ÿ±Çaoa*Ÿ±Ç`a Ÿ±Çbmic100Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`m             Ÿ±Ç`bhaŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1fcenterŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`cax2Ÿ±Çaoa.Ÿ±Ç`iset_titleŸ±Ç`a(Ÿ±Çbs1a'Ÿ±Çbs1pAge of approversŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cax2Ÿ±Çaoa.Ÿ±Ç`flegendŸ±Ç`a(Ÿ±Ç`a(Ÿ±Çbs1a'Ÿ±Çbs1e50-65Ÿ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1gOver 65Ÿ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1e35-49Ÿ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1hUnder 35Ÿ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cax2Ÿ±Çaoa.Ÿ±Ç`daxisŸ±Ç`a(Ÿ±Çbs1a'Ÿ±Çbs1coffŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cax2Ÿ±Çaoa.Ÿ±Ç`hset_xlimŸ±Ç`a(Ÿ±Çaoa-Ÿ±Ç`a Ÿ±Çbmfc2.5Ÿ±Ç`a Ÿ±Çaoa*Ÿ±Ç`a Ÿ±Ç`ewidthŸ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfc2.5Ÿ±Ç`a Ÿ±Çaoa*Ÿ±Ç`a Ÿ±Ç`ewidthŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1x9# use ConnectionPatch to draw lines between the two plotsŸ±Ç`a
Ÿ±Çbc1t# get the wedge dataŸ±Ç`a
Ÿ±Ç`ftheta1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ftheta2Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cax1Ÿ±Çaoa.Ÿ±Ç`gpatchesŸ±Ç`a[Ÿ±Çbmia0Ÿ±Ç`a]Ÿ±Çaoa.Ÿ±Ç`ftheta1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`cax1Ÿ±Çaoa.Ÿ±Ç`gpatchesŸ±Ç`a[Ÿ±Çbmia0Ÿ±Ç`a]Ÿ±Çaoa.Ÿ±Ç`ftheta2Ÿ±Ç`a
Ÿ±Ç`fcenterŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`arŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cax1Ÿ±Çaoa.Ÿ±Ç`gpatchesŸ±Ç`a[Ÿ±Çbmia0Ÿ±Ç`a]Ÿ±Çaoa.Ÿ±Ç`fcenterŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`cax1Ÿ±Çaoa.Ÿ±Ç`gpatchesŸ±Ç`a[Ÿ±Çbmia0Ÿ±Ç`a]Ÿ±Çaoa.Ÿ±Ç`arŸ±Ç`a
Ÿ±Ç`jbar_heightŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±ÇbnbcsumŸ±Ç`a(Ÿ±Ç`a[Ÿ±Ç`ditemŸ±Çaoa.Ÿ±Ç`jget_heightŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a Ÿ±ÇakcforŸ±Ç`a Ÿ±Ç`ditemŸ±Ç`a Ÿ±ÇbowbinŸ±Ç`a Ÿ±Ç`cax2Ÿ±Çaoa.Ÿ±Ç`gpatchesŸ±Ç`a]Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1x# draw top connecting lineŸ±Ç`a
Ÿ±Ç`axŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`arŸ±Ç`a Ÿ±Çaoa*Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`ccosŸ±Ç`a(Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`bpiŸ±Ç`a Ÿ±Çaoa/Ÿ±Ç`a Ÿ±Çbmic180Ÿ±Ç`a Ÿ±Çaoa*Ÿ±Ç`a Ÿ±Ç`ftheta2Ÿ±Ç`a)Ÿ±Ç`a Ÿ±Çaoa+Ÿ±Ç`a Ÿ±Ç`fcenterŸ±Ç`a[Ÿ±Çbmia0Ÿ±Ç`a]Ÿ±Ç`a
Ÿ±Ç`ayŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`arŸ±Ç`a Ÿ±Çaoa*Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`csinŸ±Ç`a(Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`bpiŸ±Ç`a Ÿ±Çaoa/Ÿ±Ç`a Ÿ±Çbmic180Ÿ±Ç`a Ÿ±Çaoa*Ÿ±Ç`a Ÿ±Ç`ftheta2Ÿ±Ç`a)Ÿ±Ç`a Ÿ±Çaoa+Ÿ±Ç`a Ÿ±Ç`fcenterŸ±Ç`a[Ÿ±Çbmia1Ÿ±Ç`a]Ÿ±Ç`a
Ÿ±Ç`cconŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`oConnectionPatchŸ±Ç`a(Ÿ±Ç`cxyAŸ±Çaoa=Ÿ±Ç`a(Ÿ±Çaoa-Ÿ±Ç`ewidthŸ±Ç`a Ÿ±Çaoa/Ÿ±Ç`a Ÿ±Çbmia2Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`jbar_heightŸ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`gcoordsAŸ±Çaoa=Ÿ±Ç`cax2Ÿ±Çaoa.Ÿ±Ç`itransDataŸ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`v                      Ÿ±Ç`cxyBŸ±Çaoa=Ÿ±Ç`a(Ÿ±Ç`axŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ayŸ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`gcoordsBŸ±Çaoa=Ÿ±Ç`cax1Ÿ±Çaoa.Ÿ±Ç`itransDataŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cconŸ±Çaoa.Ÿ±Ç`iset_colorŸ±Ç`a(Ÿ±Ç`a[Ÿ±Çbmia0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia0Ÿ±Ç`a]Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cconŸ±Çaoa.Ÿ±Ç`mset_linewidthŸ±Ç`a(Ÿ±Çbmia4Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cax2Ÿ±Çaoa.Ÿ±Ç`jadd_artistŸ±Ç`a(Ÿ±Ç`cconŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1x# draw bottom connecting lineŸ±Ç`a
Ÿ±Ç`axŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`arŸ±Ç`a Ÿ±Çaoa*Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`ccosŸ±Ç`a(Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`bpiŸ±Ç`a Ÿ±Çaoa/Ÿ±Ç`a Ÿ±Çbmic180Ÿ±Ç`a Ÿ±Çaoa*Ÿ±Ç`a Ÿ±Ç`ftheta1Ÿ±Ç`a)Ÿ±Ç`a Ÿ±Çaoa+Ÿ±Ç`a Ÿ±Ç`fcenterŸ±Ç`a[Ÿ±Çbmia0Ÿ±Ç`a]Ÿ±Ç`a
Ÿ±Ç`ayŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`arŸ±Ç`a Ÿ±Çaoa*Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`csinŸ±Ç`a(Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`bpiŸ±Ç`a Ÿ±Çaoa/Ÿ±Ç`a Ÿ±Çbmic180Ÿ±Ç`a Ÿ±Çaoa*Ÿ±Ç`a Ÿ±Ç`ftheta1Ÿ±Ç`a)Ÿ±Ç`a Ÿ±Çaoa+Ÿ±Ç`a Ÿ±Ç`fcenterŸ±Ç`a[Ÿ±Çbmia1Ÿ±Ç`a]Ÿ±Ç`a
Ÿ±Ç`cconŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`oConnectionPatchŸ±Ç`a(Ÿ±Ç`cxyAŸ±Çaoa=Ÿ±Ç`a(Ÿ±Çaoa-Ÿ±Ç`ewidthŸ±Ç`a Ÿ±Çaoa/Ÿ±Ç`a Ÿ±Çbmia2Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia0Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`gcoordsAŸ±Çaoa=Ÿ±Ç`cax2Ÿ±Çaoa.Ÿ±Ç`itransDataŸ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`v                      Ÿ±Ç`cxyBŸ±Çaoa=Ÿ±Ç`a(Ÿ±Ç`axŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ayŸ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`gcoordsBŸ±Çaoa=Ÿ±Ç`cax1Ÿ±Çaoa.Ÿ±Ç`itransDataŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cconŸ±Çaoa.Ÿ±Ç`iset_colorŸ±Ç`a(Ÿ±Ç`a[Ÿ±Çbmia0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia0Ÿ±Ç`a]Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cax2Ÿ±Çaoa.Ÿ±Ç`jadd_artistŸ±Ç`a(Ÿ±Ç`cconŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cconŸ±Çaoa.Ÿ±Ç`mset_linewidthŸ±Ç`a(Ÿ±Çbmia4Ÿ±Ç`a)Ÿ±Ç`a
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
Ÿ±Çbc1x;#    - `matplotlib.axes.Axes.bar` / `matplotlib.pyplot.bar`Ÿ±Ç`a
Ÿ±Çbc1x;#    - `matplotlib.axes.Axes.pie` / `matplotlib.pyplot.pie`Ÿ±Ç`a
Ÿ±Çbc1x+#    - `matplotlib.patches.ConnectionPatch`Ÿ±Ç`a
`dNoneˆ