ŸØÇÅŸ¥ÉôŸ±Çbsdx…"""
======================================
Long chain of connections using Sankey
======================================

Demonstrate/test the Sankey class by producing a long chain of connections.
"""Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±ÇbknfimportŸ±Ç`a Ÿ±ÇbnnŸ¢ÑjmatplotlibŸ†Ñjmatplotlibe3.5.1fmodulejmatplotlibfmoduleıŸ±Çbnna.Ÿ±ÇbnnfpyplotŸ±Ç`a Ÿ±ÇakbasŸ±Ç`a Ÿ±ÇbnncpltŸ±Ç`a
Ÿ±ÇbkndfromŸ±Ç`a Ÿ±ÇbnnŸ¢ÑjmatplotlibŸ†Ñjmatplotlibe3.5.1fmodulejmatplotlibfmoduleıŸ±Çbnna.Ÿ±ÇbnnfsankeyŸ±Ç`a Ÿ±ÇbknfimportŸ±Ç`a Ÿ±Ç`fSankeyŸ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`nlinks_per_sideŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Çbmia6Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±ÇakcdefŸ±Ç`a Ÿ±ÇbnfdsideŸ±Ç`a(Ÿ±Ç`fsankeyŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`anŸ±Çaoa=Ÿ±Çbmia1Ÿ±Ç`a)Ÿ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Çbsdx"""Generate a side chain."""Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`epriorŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±ÇbnbclenŸ±Ç`a(Ÿ±Ç`fsankeyŸ±Çaoa.Ÿ±Ç`hdiagramsŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±ÇakcforŸ±Ç`a Ÿ±Ç`aiŸ±Ç`a Ÿ±ÇbowbinŸ±Ç`a Ÿ±ÇbnberangeŸ±Ç`a(Ÿ±Çbmia0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia2Ÿ±Çaoa*Ÿ±Ç`anŸ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia2Ÿ±Ç`a)Ÿ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±Ç`fsankeyŸ±Çaoa.Ÿ±Ç`caddŸ±Ç`a(Ÿ±Ç`eflowsŸ±Çaoa=Ÿ±Ç`a[Ÿ±Çbmia1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çaoa-Ÿ±Çbmia1Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`lorientationsŸ±Çaoa=Ÿ±Ç`a[Ÿ±Çaoa-Ÿ±Çbmia1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çaoa-Ÿ±Çbmia1Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`s                   Ÿ±Ç`jpatchlabelŸ±Çaoa=Ÿ±ÇbnbcstrŸ±Ç`a(Ÿ±Ç`epriorŸ±Ç`a Ÿ±Çaoa+Ÿ±Ç`a Ÿ±Ç`aiŸ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`s                   Ÿ±Ç`epriorŸ±Çaoa=Ÿ±Ç`epriorŸ±Ç`a Ÿ±Çaoa+Ÿ±Ç`a Ÿ±Ç`aiŸ±Ç`a Ÿ±Çaoa-Ÿ±Ç`a Ÿ±Çbmia1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`gconnectŸ±Çaoa=Ÿ±Ç`a(Ÿ±Çbmia1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia0Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ealphaŸ±Çaoa=Ÿ±Çbmfc0.5Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±Ç`fsankeyŸ±Çaoa.Ÿ±Ç`caddŸ±Ç`a(Ÿ±Ç`eflowsŸ±Çaoa=Ÿ±Ç`a[Ÿ±Çbmia1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çaoa-Ÿ±Çbmia1Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`lorientationsŸ±Çaoa=Ÿ±Ç`a[Ÿ±Çbmia1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia1Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`s                   Ÿ±Ç`jpatchlabelŸ±Çaoa=Ÿ±ÇbnbcstrŸ±Ç`a(Ÿ±Ç`epriorŸ±Ç`a Ÿ±Çaoa+Ÿ±Ç`a Ÿ±Ç`aiŸ±Ç`a Ÿ±Çaoa+Ÿ±Ç`a Ÿ±Çbmia1Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`s                   Ÿ±Ç`epriorŸ±Çaoa=Ÿ±Ç`epriorŸ±Ç`a Ÿ±Çaoa+Ÿ±Ç`a Ÿ±Ç`aiŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`gconnectŸ±Çaoa=Ÿ±Ç`a(Ÿ±Çbmia1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia0Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ealphaŸ±Çaoa=Ÿ±Çbmfc0.5Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±ÇakcdefŸ±Ç`a Ÿ±ÇbnffcornerŸ±Ç`a(Ÿ±Ç`fsankeyŸ±Ç`a)Ÿ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Çbsdx"""Generate a corner link."""Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`epriorŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±ÇbnbclenŸ±Ç`a(Ÿ±Ç`fsankeyŸ±Çaoa.Ÿ±Ç`hdiagramsŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`fsankeyŸ±Çaoa.Ÿ±Ç`caddŸ±Ç`a(Ÿ±Ç`eflowsŸ±Çaoa=Ÿ±Ç`a[Ÿ±Çbmia1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çaoa-Ÿ±Çbmia1Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`lorientationsŸ±Çaoa=Ÿ±Ç`a[Ÿ±Çbmia0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia1Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`o               Ÿ±Ç`jpatchlabelŸ±Çaoa=Ÿ±ÇbnbcstrŸ±Ç`a(Ÿ±Ç`epriorŸ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ifacecolorŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1akŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`o               Ÿ±Ç`epriorŸ±Çaoa=Ÿ±Ç`epriorŸ±Ç`a Ÿ±Çaoa-Ÿ±Ç`a Ÿ±Çbmia1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`gconnectŸ±Çaoa=Ÿ±Ç`a(Ÿ±Çbmia1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia0Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ealphaŸ±Çaoa=Ÿ±Çbmfc0.5Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`cfigŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`ffigureŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`baxŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cfigŸ±Çaoa.Ÿ±Ç`kadd_subplotŸ±Ç`a(Ÿ±Çbmia1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`fxticksŸ±Çaoa=Ÿ±Ç`a[Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`fyticksŸ±Çaoa=Ÿ±Ç`a[Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`u                     Ÿ±Ç`etitleŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2xWhy would you want to do this?Ÿ±Çbseb\nŸ±Çbs2p(But you could.)Ÿ±Çbs2a"Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`fsankeyŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`fSankeyŸ±Ç`a(Ÿ±Ç`baxŸ±Çaoa=Ÿ±Ç`baxŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dunitŸ±Çaoa=Ÿ±ÇbkcdNoneŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`fsankeyŸ±Çaoa.Ÿ±Ç`caddŸ±Ç`a(Ÿ±Ç`eflowsŸ±Çaoa=Ÿ±Ç`a[Ÿ±Çbmia1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çaoa-Ÿ±Çbmia1Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`lorientationsŸ±Çaoa=Ÿ±Ç`a[Ÿ±Çbmia0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia1Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`k           Ÿ±Ç`jpatchlabelŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2a0Ÿ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ifacecolorŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1akŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`k           Ÿ±Ç`hrotationŸ±Çaoa=Ÿ±Çbmib45Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`dsideŸ±Ç`a(Ÿ±Ç`fsankeyŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`anŸ±Çaoa=Ÿ±Ç`nlinks_per_sideŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`fcornerŸ±Ç`a(Ÿ±Ç`fsankeyŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`dsideŸ±Ç`a(Ÿ±Ç`fsankeyŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`anŸ±Çaoa=Ÿ±Ç`nlinks_per_sideŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`fcornerŸ±Ç`a(Ÿ±Ç`fsankeyŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`dsideŸ±Ç`a(Ÿ±Ç`fsankeyŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`anŸ±Çaoa=Ÿ±Ç`nlinks_per_sideŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`fcornerŸ±Ç`a(Ÿ±Ç`fsankeyŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`dsideŸ±Ç`a(Ÿ±Ç`fsankeyŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`anŸ±Çaoa=Ÿ±Ç`nlinks_per_sideŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`fsankeyŸ±Çaoa.Ÿ±Ç`ffinishŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Çbc1i# Notice:Ÿ±Ç`a
Ÿ±Çbc1xE# 1. The alignment doesn't drift significantly (if at all; with 16007Ÿ±Ç`a
Ÿ±Çbc1x)#    subdiagrams there is still closure).Ÿ±Ç`a
Ÿ±Çbc1xK# 2. The first diagram is rotated 45 deg, so all other diagrams are rotatedŸ±Ç`a
Ÿ±Çbc1q#    accordingly.Ÿ±Ç`a
Ÿ±Ç`a
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
Ÿ±Çbc1x#    - `matplotlib.sankey`Ÿ±Ç`a
Ÿ±Çbc1x!#    - `matplotlib.sankey.Sankey`Ÿ±Ç`a
Ÿ±Çbc1x%#    - `matplotlib.sankey.Sankey.add`Ÿ±Ç`a
Ÿ±Çbc1x(#    - `matplotlib.sankey.Sankey.finish`Ÿ±Ç`a
`dNoneˆ