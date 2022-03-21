ŸØÇÅŸ¥Éô}Ÿ±Çbsdxî"""
===================
Drawing fancy boxes
===================

The following examples show how to plot boxes with different visual properties.
"""Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±ÇbknfimportŸ±Ç`a Ÿ±ÇbnnginspectŸ±Ç`a
Ÿ±Ç`a
Ÿ±ÇbknfimportŸ±Ç`a Ÿ±ÇbnnŸ¢ÑjmatplotlibŸ†Ñjmatplotlibe3.5.1fmodulejmatplotlibfmoduleıŸ±Çbnna.Ÿ±ÇbnnfpyplotŸ±Ç`a Ÿ±ÇakbasŸ±Ç`a Ÿ±ÇbnncpltŸ±Ç`a
Ÿ±ÇbknfimportŸ±Ç`a Ÿ±ÇbnnŸ¢ÑjmatplotlibŸ†Ñjmatplotlibe3.5.1fmodulejmatplotlibfmoduleıŸ±Çbnna.Ÿ±ÇbnnjtransformsŸ±Ç`a Ÿ±ÇakbasŸ±Ç`a Ÿ±ÇbnnkmtransformsŸ±Ç`a
Ÿ±ÇbknfimportŸ±Ç`a Ÿ±ÇbnnŸ¢ÑjmatplotlibŸ†Ñjmatplotlibe3.5.1fmodulejmatplotlibfmoduleıŸ±Çbnna.Ÿ±ÇbnngpatchesŸ±Ç`a Ÿ±ÇakbasŸ±Ç`a Ÿ±ÇbnnfmpatchŸ±Ç`a
Ÿ±ÇbkndfromŸ±Ç`a Ÿ±ÇbnnŸ¢ÑjmatplotlibŸ†Ñjmatplotlibe3.5.1fmodulejmatplotlibfmoduleıŸ±Çbnna.Ÿ±ÇbnngpatchesŸ±Ç`a Ÿ±ÇbknfimportŸ±Ç`a Ÿ±Ç`nFancyBboxPatchŸ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1xO###############################################################################Ÿ±Ç`a
Ÿ±Çbc1x3# First we'll show some sample boxes with fancybox.Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`fstylesŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`fmpatchŸ±Çaoa.Ÿ±Ç`hBoxStyleŸ±Çaoa.Ÿ±Ç`jget_stylesŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`dncolŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Çbmia2Ÿ±Ç`a
Ÿ±Ç`dnrowŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`a(Ÿ±ÇbnbclenŸ±Ç`a(Ÿ±Ç`fstylesŸ±Ç`a)Ÿ±Ç`a Ÿ±Çaoa+Ÿ±Ç`a Ÿ±Çbmia1Ÿ±Ç`a)Ÿ±Ç`a Ÿ±Çaoa/Ÿ±Çaoa/Ÿ±Ç`a Ÿ±Ç`dncolŸ±Ç`a
Ÿ±Ç`caxsŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`a(Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`ffigureŸ±Ç`a(Ÿ±Ç`gfigsizeŸ±Çaoa=Ÿ±Ç`a(Ÿ±Çbmia3Ÿ±Ç`a Ÿ±Çaoa*Ÿ±Ç`a Ÿ±Ç`dncolŸ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia1Ÿ±Ç`a Ÿ±Çaoa+Ÿ±Ç`a Ÿ±Ç`dnrowŸ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`g       Ÿ±Çaoa.Ÿ±Ç`ladd_gridspecŸ±Ç`a(Ÿ±Çbmia1Ÿ±Ç`a Ÿ±Çaoa+Ÿ±Ç`a Ÿ±Ç`dnrowŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dncolŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`fwspaceŸ±Çaoa=Ÿ±Çbmfb.5Ÿ±Ç`a)Ÿ±Çaoa.Ÿ±Ç`hsubplotsŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±ÇakcforŸ±Ç`a Ÿ±Ç`baxŸ±Ç`a Ÿ±ÇbowbinŸ±Ç`a Ÿ±Ç`caxsŸ±Çaoa.Ÿ±Ç`dflatŸ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`lset_axis_offŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±ÇakcforŸ±Ç`a Ÿ±Ç`baxŸ±Ç`a Ÿ±ÇbowbinŸ±Ç`a Ÿ±Ç`caxsŸ±Ç`a[Ÿ±Çbmia0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`a:Ÿ±Ç`a]Ÿ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`dtextŸ±Ç`a(Ÿ±Çbmfb.2Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfb.5Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs2a"Ÿ±Çbs2hboxstyleŸ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`l            Ÿ±Ç`itransformŸ±Çaoa=Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`itransAxesŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dsizeŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2elargeŸ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ecolorŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2htab:blueŸ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`l            Ÿ±Ç`shorizontalalignmentŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2erightŸ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`qverticalalignmentŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2fcenterŸ±Çbs2a"Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`dtextŸ±Ç`a(Ÿ±Çbmfb.4Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfb.5Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs2a"Ÿ±Çbs2rdefault parametersŸ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`l            Ÿ±Ç`itransformŸ±Çaoa=Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`itransAxesŸ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`l            Ÿ±Ç`shorizontalalignmentŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2dleftŸ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`qverticalalignmentŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2fcenterŸ±Çbs2a"Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±ÇakcforŸ±Ç`a Ÿ±Ç`baxŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`a(Ÿ±Ç`istylenameŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`hstyleclsŸ±Ç`a)Ÿ±Ç`a Ÿ±ÇbowbinŸ±Ç`a Ÿ±ÇbnbczipŸ±Ç`a(Ÿ±Ç`caxsŸ±Ç`a[Ÿ±Çbmia1Ÿ±Ç`a:Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`a:Ÿ±Ç`a]Ÿ±Çaoa.Ÿ±Ç`aTŸ±Çaoa.Ÿ±Ç`dflatŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`fstylesŸ±Çaoa.Ÿ±Ç`eitemsŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`dtextŸ±Ç`a(Ÿ±Çbmfb.2Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfb.5Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`istylenameŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dbboxŸ±Çaoa=Ÿ±ÇbnbddictŸ±Ç`a(Ÿ±Ç`hboxstyleŸ±Çaoa=Ÿ±Ç`istylenameŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`bfcŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2awŸ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`becŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2akŸ±Çbs2a"Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`l            Ÿ±Ç`itransformŸ±Çaoa=Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`itransAxesŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dsizeŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2elargeŸ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ecolorŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2htab:blueŸ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`l            Ÿ±Ç`shorizontalalignmentŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2erightŸ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`qverticalalignmentŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2fcenterŸ±Çbs2a"Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`dtextŸ±Ç`a(Ÿ±Çbmfb.4Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfb.5Ÿ±Ç`a,Ÿ±Ç`a Ÿ±ÇbnbcstrŸ±Ç`a(Ÿ±Ç`ginspectŸ±Çaoa.Ÿ±Ç`isignatureŸ±Ç`a(Ÿ±Ç`hstyleclsŸ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a[Ÿ±Çbmia1Ÿ±Ç`a:Ÿ±Çaoa-Ÿ±Çbmia1Ÿ±Ç`a]Ÿ±Çaoa.Ÿ±Ç`greplaceŸ±Ç`a(Ÿ±Çbs2a"Ÿ±Çbs2b, Ÿ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs2a"Ÿ±Çbseb\nŸ±Çbs2a"Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`l            Ÿ±Ç`itransformŸ±Çaoa=Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`itransAxesŸ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`l            Ÿ±Ç`shorizontalalignmentŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2dleftŸ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`qverticalalignmentŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2fcenterŸ±Çbs2a"Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1xO###############################################################################Ÿ±Ç`a
Ÿ±Çbc1x3# Next we'll show off multiple fancy boxes at once.Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±ÇakcdefŸ±Ç`a Ÿ±Çbnfvadd_fancy_patch_aroundŸ±Ç`a(Ÿ±Ç`baxŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`bbbŸ±Ç`a,Ÿ±Ç`a Ÿ±Çaoa*Ÿ±Çaoa*Ÿ±Ç`fkwargsŸ±Ç`a)Ÿ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`efancyŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`nFancyBboxPatchŸ±Ç`a(Ÿ±Ç`a(Ÿ±Ç`bbbŸ±Çaoa.Ÿ±Ç`dxminŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`bbbŸ±Çaoa.Ÿ±Ç`dyminŸ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`bbbŸ±Çaoa.Ÿ±Ç`ewidthŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`bbbŸ±Çaoa.Ÿ±Ç`fheightŸ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`x                           Ÿ±Ç`bfcŸ±Çaoa=Ÿ±Ç`a(Ÿ±Çbmia1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfc0.8Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfc0.5Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`becŸ±Çaoa=Ÿ±Ç`a(Ÿ±Çbmia1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfc0.5Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfc0.5Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`x                           Ÿ±Çaoa*Ÿ±Çaoa*Ÿ±Ç`fkwargsŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`iadd_patchŸ±Ç`a(Ÿ±Ç`efancyŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±ÇakfreturnŸ±Ç`a Ÿ±Ç`efancyŸ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±ÇakcdefŸ±Ç`a Ÿ±Çbnfxdraw_control_points_for_patchesŸ±Ç`a(Ÿ±Ç`baxŸ±Ç`a)Ÿ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±ÇakcforŸ±Ç`a Ÿ±Ç`epatchŸ±Ç`a Ÿ±ÇbowbinŸ±Ç`a Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`gpatchesŸ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±Ç`epatchŸ±Çaoa.Ÿ±Ç`daxesŸ±Çaoa.Ÿ±Ç`dplotŸ±Ç`a(Ÿ±Çaoa*Ÿ±Ç`epatchŸ±Çaoa.Ÿ±Ç`hget_pathŸ±Ç`a(Ÿ±Ç`a)Ÿ±Çaoa.Ÿ±Ç`hverticesŸ±Çaoa.Ÿ±Ç`aTŸ±Ç`a,Ÿ±Ç`a Ÿ±Çbs2a"Ÿ±Çbs2a.Ÿ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`x                        Ÿ±Ç`acŸ±Çaoa=Ÿ±Ç`epatchŸ±Çaoa.Ÿ±Ç`mget_edgecolorŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`cfigŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`caxsŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`hsubplotsŸ±Ç`a(Ÿ±Çbmia2Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia2Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`gfigsizeŸ±Çaoa=Ÿ±Ç`a(Ÿ±Çbmia8Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia8Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1x7# Bbox object around which the fancy box will be drawn.Ÿ±Ç`a
Ÿ±Ç`bbbŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`kmtransformsŸ±Çaoa.Ÿ±Ç`dBboxŸ±Ç`a(Ÿ±Ç`a[Ÿ±Ç`a[Ÿ±Çbmfc0.3Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfc0.4Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`a[Ÿ±Çbmfc0.7Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfc0.6Ÿ±Ç`a]Ÿ±Ç`a]Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`baxŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`caxsŸ±Ç`a[Ÿ±Çbmia0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia0Ÿ±Ç`a]Ÿ±Ç`a
Ÿ±Çbc1x)# a fancy box with round corners. pad=0.1Ÿ±Ç`a
Ÿ±Ç`efancyŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`vadd_fancy_patch_aroundŸ±Ç`a(Ÿ±Ç`baxŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`bbbŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`hboxstyleŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2mround,pad=0.1Ÿ±Çbs2a"Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`csetŸ±Ç`a(Ÿ±Ç`dxlimŸ±Çaoa=Ÿ±Ç`a(Ÿ±Çbmia0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia1Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dylimŸ±Çaoa=Ÿ±Ç`a(Ÿ±Çbmia0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia1Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`faspectŸ±Çaoa=Ÿ±Çbmia1Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`g       Ÿ±Ç`etitleŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1iboxstyle=Ÿ±Çbs1a"Ÿ±Çbs1mround,pad=0.1Ÿ±Çbs1a"Ÿ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`baxŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`caxsŸ±Ç`a[Ÿ±Çbmia0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia1Ÿ±Ç`a]Ÿ±Ç`a
Ÿ±Çbc1x?# bbox=round has two optional arguments: pad and rounding_size.Ÿ±Ç`a
Ÿ±Çbc1x,# They can be set during the initialization.Ÿ±Ç`a
Ÿ±Ç`efancyŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`vadd_fancy_patch_aroundŸ±Ç`a(Ÿ±Ç`baxŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`bbbŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`hboxstyleŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2mround,pad=0.1Ÿ±Çbs2a"Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Çbc1xJ# The boxstyle and its argument can be later modified with set_boxstyle().Ÿ±Ç`a
Ÿ±Çbc1xM# Note that the old attributes are simply forgotten even if the boxstyle nameŸ±Ç`a
Ÿ±Çbc1j# is same.Ÿ±Ç`a
Ÿ±Ç`efancyŸ±Çaoa.Ÿ±Ç`lset_boxstyleŸ±Ç`a(Ÿ±Çbs2a"Ÿ±Çbs2xround,pad=0.1,rounding_size=0.2Ÿ±Çbs2a"Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Çbc1x=# or: fancy.set_boxstyle("round", pad=0.1, rounding_size=0.2)Ÿ±Ç`a
Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`csetŸ±Ç`a(Ÿ±Ç`dxlimŸ±Çaoa=Ÿ±Ç`a(Ÿ±Çbmia0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia1Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dylimŸ±Çaoa=Ÿ±Ç`a(Ÿ±Çbmia0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia1Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`faspectŸ±Çaoa=Ÿ±Çbmia1Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`g       Ÿ±Ç`etitleŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1iboxstyle=Ÿ±Çbs1a"Ÿ±Çbs1xround,pad=0.1,rounding_size=0.2Ÿ±Çbs1a"Ÿ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`baxŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`caxsŸ±Ç`a[Ÿ±Çbmia1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia0Ÿ±Ç`a]Ÿ±Ç`a
Ÿ±Çbc1xL# mutation_scale determines the overall scale of the mutation, i.e. both padŸ±Ç`a
Ÿ±Çbc1x6# and rounding_size is scaled according to this value.Ÿ±Ç`a
Ÿ±Ç`efancyŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`vadd_fancy_patch_aroundŸ±Ç`a(Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`baxŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`bbbŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`hboxstyleŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2mround,pad=0.1Ÿ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`nmutation_scaleŸ±Çaoa=Ÿ±Çbmia2Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`csetŸ±Ç`a(Ÿ±Ç`dxlimŸ±Çaoa=Ÿ±Ç`a(Ÿ±Çbmia0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia1Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dylimŸ±Çaoa=Ÿ±Ç`a(Ÿ±Çbmia0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia1Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`faspectŸ±Çaoa=Ÿ±Çbmia1Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`g       Ÿ±Ç`etitleŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1iboxstyle=Ÿ±Çbs1a"Ÿ±Çbs1mround,pad=0.1Ÿ±Çbs1a"Ÿ±Çbseb\nŸ±Çbs1q mutation_scale=2Ÿ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`baxŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`caxsŸ±Ç`a[Ÿ±Çbmia1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia1Ÿ±Ç`a]Ÿ±Ç`a
Ÿ±Çbc1xO# When the aspect ratio of the axes is not 1, the fancy box may not be what youŸ±Ç`a
Ÿ±Çbc1s# expected (green).Ÿ±Ç`a
Ÿ±Ç`efancyŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`vadd_fancy_patch_aroundŸ±Ç`a(Ÿ±Ç`baxŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`bbbŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`hboxstyleŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2mround,pad=0.2Ÿ±Çbs2a"Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`efancyŸ±Çaoa.Ÿ±Ç`csetŸ±Ç`a(Ÿ±Ç`ifacecolorŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2dnoneŸ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`iedgecolorŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2egreenŸ±Çbs2a"Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Çbc1x@# You can compensate this by setting the mutation_aspect (pink).Ÿ±Ç`a
Ÿ±Ç`efancyŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`vadd_fancy_patch_aroundŸ±Ç`a(Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`baxŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`bbbŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`hboxstyleŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2mround,pad=0.3Ÿ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`omutation_aspectŸ±Çaoa=Ÿ±Çbmfc0.5Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`csetŸ±Ç`a(Ÿ±Ç`dxlimŸ±Çaoa=Ÿ±Ç`a(Ÿ±Çaoa-Ÿ±Çbmfb.5Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfc1.5Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dylimŸ±Çaoa=Ÿ±Ç`a(Ÿ±Çbmia0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia1Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`faspectŸ±Çaoa=Ÿ±Çbmia2Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`g       Ÿ±Ç`etitleŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1iboxstyle=Ÿ±Çbs1a"Ÿ±Çbs1mround,pad=0.3Ÿ±Çbs1a"Ÿ±Çbseb\nŸ±Çbs1rmutation_aspect=.5Ÿ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±ÇakcforŸ±Ç`a Ÿ±Ç`baxŸ±Ç`a Ÿ±ÇbowbinŸ±Ç`a Ÿ±Ç`caxsŸ±Çaoa.Ÿ±Ç`dflatŸ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`xdraw_control_points_for_patchesŸ±Ç`a(Ÿ±Ç`baxŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Çbc1x<# Draw the original bbox (using boxstyle=square with pad=0).Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`efancyŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`vadd_fancy_patch_aroundŸ±Ç`a(Ÿ±Ç`baxŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`bbbŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`hboxstyleŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2lsquare,pad=0Ÿ±Çbs2a"Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`efancyŸ±Çaoa.Ÿ±Ç`csetŸ±Ç`a(Ÿ±Ç`iedgecolorŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2eblackŸ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ifacecolorŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2dnoneŸ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`fzorderŸ±Çaoa=Ÿ±Çbmib10Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`cfigŸ±Çaoa.Ÿ±Ç`ltight_layoutŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
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
Ÿ±Çbc1x#    - `matplotlib.patches`Ÿ±Ç`a
Ÿ±Çbc1x*#    - `matplotlib.patches.FancyBboxPatch`Ÿ±Ç`a
Ÿ±Çbc1x$#    - `matplotlib.patches.BoxStyle`Ÿ±Ç`a
Ÿ±Çbc1x1#    - ``matplotlib.patches.BoxStyle.get_styles``Ÿ±Ç`a
Ÿ±Çbc1x##    - `matplotlib.transforms.Bbox`Ÿ±Ç`a
Ÿ±Çbc1x&#    - `matplotlib.figure.Figure.text`Ÿ±Ç`a
Ÿ±Çbc1x"#    - `matplotlib.axes.Axes.text`Ÿ±Ç`a
`dNoneˆ