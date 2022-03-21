ŸØÇÅŸ¥Éô_Ÿ±ÇbsaarŸ±ÇbsdyÕ"""
==================
Text Rotation Mode
==================

This example illustrates the effect of ``rotation_mode`` on the positioning
of rotated text.

Rotated `.Text`\s are created by passing the parameter ``rotation`` to
the constructor or the axes' method `~.axes.Axes.text`.

The actual positioning depends on the additional parameters
``horizontalalignment``, ``verticalalignment`` and ``rotation_mode``.
``rotation_mode`` determines the order of rotation and alignment:

- ``rotation_mode='default'`` (or None) first rotates the text and then aligns
  the bounding box of the rotated text.
- ``rotation_mode='anchor'`` aligns the unrotated text and then rotates the
  text around the point of alignment.
"""Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±ÇbknfimportŸ±Ç`a Ÿ±ÇbnnŸ¢ÑjmatplotlibŸ†Ñjmatplotlibe3.5.1fmodulejmatplotlibfmoduleıŸ±Çbnna.Ÿ±ÇbnnfpyplotŸ±Ç`a Ÿ±ÇakbasŸ±Ç`a Ÿ±ÇbnncpltŸ±Ç`a
Ÿ±ÇbknfimportŸ±Ç`a Ÿ±ÇbnnŸ¢ÑenumpyŸ†Ñenumpyf1.22.3fmoduleenumpyfmoduleıŸ±Ç`a Ÿ±ÇakbasŸ±Ç`a Ÿ±ÇbnnbnpŸ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±ÇakcdefŸ±Ç`a Ÿ±Çbnfrtest_rotation_modeŸ±Ç`a(Ÿ±Ç`cfigŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dmodeŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`psubplot_locationŸ±Ç`a)Ÿ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`gha_listŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`a[Ÿ±Çbs2a"Ÿ±Çbs2dleftŸ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs2a"Ÿ±Çbs2fcenterŸ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs2a"Ÿ±Çbs2erightŸ±Çbs2a"Ÿ±Ç`a]Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`gva_listŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`a[Ÿ±Çbs2a"Ÿ±Çbs2ctopŸ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs2a"Ÿ±Çbs2fcenterŸ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs2a"Ÿ±Çbs2hbaselineŸ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs2a"Ÿ±Çbs2fbottomŸ±Çbs2a"Ÿ±Ç`a]Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`caxsŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`eemptyŸ±Ç`a(Ÿ±Ç`a(Ÿ±ÇbnbclenŸ±Ç`a(Ÿ±Ç`gva_listŸ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±ÇbnbclenŸ±Ç`a(Ÿ±Ç`gha_listŸ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±ÇbnbfobjectŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`bgsŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`psubplot_locationŸ±Çaoa.Ÿ±Ç`ksubgridspecŸ±Ç`a(Ÿ±Çaoa*Ÿ±Ç`caxsŸ±Çaoa.Ÿ±Ç`eshapeŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`fhspaceŸ±Çaoa=Ÿ±Çbmia0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`fwspaceŸ±Çaoa=Ÿ±Çbmia0Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`caxsŸ±Ç`a[Ÿ±Çbmia0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia0Ÿ±Ç`a]Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cfigŸ±Çaoa.Ÿ±Ç`kadd_subplotŸ±Ç`a(Ÿ±Ç`bgsŸ±Ç`a[Ÿ±Çbmia0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia0Ÿ±Ç`a]Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±ÇakcforŸ±Ç`a Ÿ±Ç`aiŸ±Ç`a Ÿ±ÇbowbinŸ±Ç`a Ÿ±ÇbnberangeŸ±Ç`a(Ÿ±ÇbnbclenŸ±Ç`a(Ÿ±Ç`gva_listŸ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±ÇakcforŸ±Ç`a Ÿ±Ç`ajŸ±Ç`a Ÿ±ÇbowbinŸ±Ç`a Ÿ±ÇbnberangeŸ±Ç`a(Ÿ±ÇbnbclenŸ±Ç`a(Ÿ±Ç`gha_listŸ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`l            Ÿ±ÇakbifŸ±Ç`a Ÿ±Ç`a(Ÿ±Ç`aiŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ajŸ±Ç`a)Ÿ±Ç`a Ÿ±Çaob==Ÿ±Ç`a Ÿ±Ç`a(Ÿ±Çbmia0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia0Ÿ±Ç`a)Ÿ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`p                Ÿ±ÇakhcontinueŸ±Ç`b  Ÿ±Çbc1n# Already set.Ÿ±Ç`a
Ÿ±Ç`l            Ÿ±Ç`caxsŸ±Ç`a[Ÿ±Ç`aiŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ajŸ±Ç`a]Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cfigŸ±Çaoa.Ÿ±Ç`kadd_subplotŸ±Ç`a(Ÿ±Ç`a
Ÿ±Ç`p                Ÿ±Ç`bgsŸ±Ç`a[Ÿ±Ç`aiŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ajŸ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`fsharexŸ±Çaoa=Ÿ±Ç`caxsŸ±Ç`a[Ÿ±Çbmia0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia0Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`fshareyŸ±Çaoa=Ÿ±Ç`caxsŸ±Ç`a[Ÿ±Çbmia0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia0Ÿ±Ç`a]Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±ÇakcforŸ±Ç`a Ÿ±Ç`baxŸ±Ç`a Ÿ±ÇbowbinŸ±Ç`a Ÿ±Ç`caxsŸ±Çaoa.Ÿ±Ç`dflatŸ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`csetŸ±Ç`a(Ÿ±Ç`faspectŸ±Çaoa=Ÿ±Çbmia1Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Çbc1r# labels and titleŸ±Ç`a
Ÿ±Ç`d    Ÿ±ÇakcforŸ±Ç`a Ÿ±Ç`bhaŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`baxŸ±Ç`a Ÿ±ÇbowbinŸ±Ç`a Ÿ±ÇbnbczipŸ±Ç`a(Ÿ±Ç`gha_listŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`caxsŸ±Ç`a[Ÿ±Çaoa-Ÿ±Çbmia1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`a:Ÿ±Ç`a]Ÿ±Ç`a)Ÿ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`jset_xlabelŸ±Ç`a(Ÿ±Ç`bhaŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±ÇakcforŸ±Ç`a Ÿ±Ç`bvaŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`baxŸ±Ç`a Ÿ±ÇbowbinŸ±Ç`a Ÿ±ÇbnbczipŸ±Ç`a(Ÿ±Ç`gva_listŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`caxsŸ±Ç`a[Ÿ±Ç`a:Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia0Ÿ±Ç`a]Ÿ±Ç`a)Ÿ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`jset_ylabelŸ±Ç`a(Ÿ±Ç`bvaŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`caxsŸ±Ç`a[Ÿ±Çbmia0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia1Ÿ±Ç`a]Ÿ±Çaoa.Ÿ±Ç`iset_titleŸ±Ç`a(Ÿ±ÇbsaafŸ±Çbs2a"Ÿ±Çbs2nrotation_mode=Ÿ±Çbs2a'Ÿ±Çbsia{Ÿ±Ç`dmodeŸ±Çbsia}Ÿ±Çbs2a'Ÿ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dsizeŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2elargeŸ±Çbs2a"Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`bkwŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`a(Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±Ç`a{Ÿ±Ç`a}Ÿ±Ç`a Ÿ±ÇakbifŸ±Ç`a Ÿ±Ç`dmodeŸ±Ç`a Ÿ±Çaob==Ÿ±Ç`a Ÿ±Çbs2a"Ÿ±Çbs2gdefaultŸ±Çbs2a"Ÿ±Ç`a Ÿ±ÇakdelseŸ±Ç`a
Ÿ±Ç`h        Ÿ±Ç`a{Ÿ±Çbs2a"Ÿ±Çbs2dbboxŸ±Çbs2a"Ÿ±Ç`a:Ÿ±Ç`a Ÿ±ÇbnbddictŸ±Ç`a(Ÿ±Ç`hboxstyleŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2msquare,pad=0.Ÿ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`becŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2dnoneŸ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`bfcŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2bC1Ÿ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ealphaŸ±Çaoa=Ÿ±Çbmfc0.3Ÿ±Ç`a)Ÿ±Ç`a}Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Çbc1x-# use a different text alignment in each axesŸ±Ç`a
Ÿ±Ç`d    Ÿ±ÇakcforŸ±Ç`a Ÿ±Ç`aiŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`bvaŸ±Ç`a Ÿ±ÇbowbinŸ±Ç`a Ÿ±ÇbnbienumerateŸ±Ç`a(Ÿ±Ç`gva_listŸ±Ç`a)Ÿ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±ÇakcforŸ±Ç`a Ÿ±Ç`ajŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`bhaŸ±Ç`a Ÿ±ÇbowbinŸ±Ç`a Ÿ±ÇbnbienumerateŸ±Ç`a(Ÿ±Ç`gha_listŸ±Ç`a)Ÿ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`l            Ÿ±Ç`baxŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`caxsŸ±Ç`a[Ÿ±Ç`aiŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ajŸ±Ç`a]Ÿ±Ç`a
Ÿ±Ç`l            Ÿ±Çbc1u# prepare axes layoutŸ±Ç`a
Ÿ±Ç`l            Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`csetŸ±Ç`a(Ÿ±Ç`fxticksŸ±Çaoa=Ÿ±Ç`a[Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`fyticksŸ±Çaoa=Ÿ±Ç`a[Ÿ±Ç`a]Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`l            Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`gaxvlineŸ±Ç`a(Ÿ±Çbmfc0.5Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ecolorŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2gskyblueŸ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`fzorderŸ±Çaoa=Ÿ±Çbmia0Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`l            Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`gaxhlineŸ±Ç`a(Ÿ±Çbmfc0.5Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ecolorŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2gskyblueŸ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`fzorderŸ±Çaoa=Ÿ±Çbmia0Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`l            Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`dplotŸ±Ç`a(Ÿ±Çbmfc0.5Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfc0.5Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ecolorŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2bC0Ÿ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`fmarkerŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2aoŸ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`fzorderŸ±Çaoa=Ÿ±Çbmia1Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`l            Ÿ±Çbc1x/# add text with rotation and alignment settingsŸ±Ç`a
Ÿ±Ç`l            Ÿ±Ç`btxŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`dtextŸ±Ç`a(Ÿ±Çbmfc0.5Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfc0.5Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs2a"Ÿ±Çbs2cTpgŸ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`x                         Ÿ±Ç`dsizeŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2gx-largeŸ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`hrotationŸ±Çaoa=Ÿ±Çbmib40Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`x                         Ÿ±Ç`shorizontalalignmentŸ±Çaoa=Ÿ±Ç`bhaŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`qverticalalignmentŸ±Çaoa=Ÿ±Ç`bvaŸ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`x                         Ÿ±Ç`mrotation_modeŸ±Çaoa=Ÿ±Ç`dmodeŸ±Ç`a,Ÿ±Ç`a Ÿ±Çaoa*Ÿ±Çaoa*Ÿ±Ç`bkwŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±ÇakbifŸ±Ç`a Ÿ±Ç`dmodeŸ±Ç`a Ÿ±Çaob==Ÿ±Ç`a Ÿ±Çbs2a"Ÿ±Çbs2gdefaultŸ±Çbs2a"Ÿ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±Çbc1p# highlight bboxŸ±Ç`a
Ÿ±Ç`h        Ÿ±Ç`cfigŸ±Çaoa.Ÿ±Ç`fcanvasŸ±Çaoa.Ÿ±Ç`ddrawŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±ÇakcforŸ±Ç`a Ÿ±Ç`baxŸ±Ç`a Ÿ±ÇbowbinŸ±Ç`a Ÿ±Ç`caxsŸ±Çaoa.Ÿ±Ç`dflatŸ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`l            Ÿ±Ç`dtextŸ±Ç`a,Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`etextsŸ±Ç`a
Ÿ±Ç`l            Ÿ±Ç`bbbŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`dtextŸ±Çaoa.Ÿ±Ç`qget_window_extentŸ±Ç`a(Ÿ±Ç`a)Ÿ±Çaoa.Ÿ±Ç`ktransformedŸ±Ç`a(Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`itransDataŸ±Çaoa.Ÿ±Ç`hinvertedŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`l            Ÿ±Ç`drectŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`iRectangleŸ±Ç`a(Ÿ±Ç`a(Ÿ±Ç`bbbŸ±Çaoa.Ÿ±Ç`bx0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`bbbŸ±Çaoa.Ÿ±Ç`by0Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`bbbŸ±Çaoa.Ÿ±Ç`ewidthŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`bbbŸ±Çaoa.Ÿ±Ç`fheightŸ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`x!                                 Ÿ±Ç`ifacecolorŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2bC1Ÿ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ealphaŸ±Çaoa=Ÿ±Çbmfc0.3Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`fzorderŸ±Çaoa=Ÿ±Çbmia2Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`l            Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`iadd_patchŸ±Ç`a(Ÿ±Ç`drectŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`cfigŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`ffigureŸ±Ç`a(Ÿ±Ç`gfigsizeŸ±Çaoa=Ÿ±Ç`a(Ÿ±Çbmia8Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia5Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`bgsŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cfigŸ±Çaoa.Ÿ±Ç`ladd_gridspecŸ±Ç`a(Ÿ±Çbmia1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia2Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`rtest_rotation_modeŸ±Ç`a(Ÿ±Ç`cfigŸ±Ç`a,Ÿ±Ç`a Ÿ±Çbs2a"Ÿ±Çbs2gdefaultŸ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`bgsŸ±Ç`a[Ÿ±Çbmia0Ÿ±Ç`a]Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`rtest_rotation_modeŸ±Ç`a(Ÿ±Ç`cfigŸ±Ç`a,Ÿ±Ç`a Ÿ±Çbs2a"Ÿ±Çbs2fanchorŸ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`bgsŸ±Ç`a[Ÿ±Çbmia1Ÿ±Ç`a]Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`dshowŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1xM#############################################################################Ÿ±Ç`a
Ÿ±Çbc1a#Ÿ±Ç`a
Ÿ±Çbc1x# .. admonition:: ReferencesŸ±Ç`a
Ÿ±Çbc1a#Ÿ±Ç`a
Ÿ±Çbc1xN#    The use of the following functions, methods, classes and modules is shownŸ±Ç`a
Ÿ±Çbc1u#    in this example:Ÿ±Ç`a
Ÿ±Çbc1a#Ÿ±Ç`a
Ÿ±Çbc1x=#    - `matplotlib.axes.Axes.text` / `matplotlib.pyplot.text`Ÿ±Ç`a
`dNoneˆ