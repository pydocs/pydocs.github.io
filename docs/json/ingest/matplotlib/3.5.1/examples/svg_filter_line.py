ŸØÇÅŸ¥Éô\Ÿ±Çbsdx‘"""
===============
SVG Filter Line
===============

Demonstrate SVG filtering effects which might be used with Matplotlib.

Note that the filtering effects are only effective if your SVG renderer
support it.
"""Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±ÇbknfimportŸ±Ç`a Ÿ±ÇbnnbioŸ±Ç`a
Ÿ±ÇbknfimportŸ±Ç`a Ÿ±ÇbnncxmlŸ±Çbnna.Ÿ±ÇbnneetreeŸ±Çbnna.Ÿ±ÇbnnkElementTreeŸ±Ç`a Ÿ±ÇakbasŸ±Ç`a Ÿ±ÇbnnbETŸ±Ç`a
Ÿ±Ç`a
Ÿ±ÇbknfimportŸ±Ç`a Ÿ±ÇbnnŸ¢ÑjmatplotlibŸ†Ñjmatplotlibe3.5.1fmodulejmatplotlibfmoduleıŸ±Çbnna.Ÿ±ÇbnnfpyplotŸ±Ç`a Ÿ±ÇakbasŸ±Ç`a Ÿ±ÇbnncpltŸ±Ç`a
Ÿ±ÇbknfimportŸ±Ç`a Ÿ±ÇbnnŸ¢ÑjmatplotlibŸ†Ñjmatplotlibe3.5.1fmodulejmatplotlibfmoduleıŸ±Çbnna.Ÿ±ÇbnnjtransformsŸ±Ç`a Ÿ±ÇakbasŸ±Ç`a Ÿ±ÇbnnkmtransformsŸ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`dfig1Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`ffigureŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`baxŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`dfig1Ÿ±Çaoa.Ÿ±Ç`hadd_axesŸ±Ç`a(Ÿ±Ç`a[Ÿ±Çbmfc0.1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfc0.1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfc0.8Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfc0.8Ÿ±Ç`a]Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1l# draw linesŸ±Ç`a
Ÿ±Ç`bl1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`dplotŸ±Ç`a(Ÿ±Ç`a[Ÿ±Çbmfc0.1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfc0.5Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfc0.9Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`a[Ÿ±Çbmfc0.1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfc0.9Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfc0.5Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs2a"Ÿ±Çbs2cbo-Ÿ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`n              Ÿ±Ç`cmecŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2abŸ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`blwŸ±Çaoa=Ÿ±Çbmia5Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`bmsŸ±Çaoa=Ÿ±Çbmib10Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`elabelŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2fLine 1Ÿ±Çbs2a"Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`bl2Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`dplotŸ±Ç`a(Ÿ±Ç`a[Ÿ±Çbmfc0.1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfc0.5Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfc0.9Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`a[Ÿ±Çbmfc0.5Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfc0.2Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfc0.7Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs2a"Ÿ±Çbs2crs-Ÿ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`n              Ÿ±Ç`cmecŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2arŸ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`blwŸ±Çaoa=Ÿ±Çbmia5Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`bmsŸ±Çaoa=Ÿ±Çbmib10Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`elabelŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2fLine 2Ÿ±Çbs2a"Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±ÇakcforŸ±Ç`a Ÿ±Ç`alŸ±Ç`a Ÿ±ÇbowbinŸ±Ç`a Ÿ±Ç`a[Ÿ±Ç`bl1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`bl2Ÿ±Ç`a]Ÿ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Çbc1xB# draw shadows with same lines with slight offset and gray colors.Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`bxxŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`alŸ±Çaoa.Ÿ±Ç`iget_xdataŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`byyŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`alŸ±Çaoa.Ÿ±Ç`iget_ydataŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`fshadowŸ±Ç`a,Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`dplotŸ±Ç`a(Ÿ±Ç`bxxŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`byyŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`fshadowŸ±Çaoa.Ÿ±Ç`kupdate_fromŸ±Ç`a(Ÿ±Ç`alŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Çbc1n# adjust colorŸ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`fshadowŸ±Çaoa.Ÿ±Ç`iset_colorŸ±Ç`a(Ÿ±Çbs2a"Ÿ±Çbs2c0.2Ÿ±Çbs2a"Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Çbc1xA# adjust zorder of the shadow lines so that it is drawn below theŸ±Ç`a
Ÿ±Ç`d    Ÿ±Çbc1p# original linesŸ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`fshadowŸ±Çaoa.Ÿ±Ç`jset_zorderŸ±Ç`a(Ÿ±Ç`alŸ±Çaoa.Ÿ±Ç`jget_zorderŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a Ÿ±Çaoa-Ÿ±Ç`a Ÿ±Çbmfc0.5Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Çbc1r# offset transformŸ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`botŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`kmtransformsŸ±Çaoa.Ÿ±Ç`koffset_copyŸ±Ç`a(Ÿ±Ç`alŸ±Çaoa.Ÿ±Ç`mget_transformŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dfig1Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`x!                                 Ÿ±Ç`axŸ±Çaoa=Ÿ±Çbmfc4.0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ayŸ±Çaoa=Ÿ±Çaoa-Ÿ±Çbmfc6.0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`eunitsŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1fpointsŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`fshadowŸ±Çaoa.Ÿ±Ç`mset_transformŸ±Ç`a(Ÿ±Ç`botŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Çbc1x# set the id for a later useŸ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`fshadowŸ±Çaoa.Ÿ±Ç`gset_gidŸ±Ç`a(Ÿ±Ç`alŸ±Çaoa.Ÿ±Ç`iget_labelŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a Ÿ±Çaoa+Ÿ±Ç`a Ÿ±Çbs2a"Ÿ±Çbs2g_shadowŸ±Çbs2a"Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`hset_xlimŸ±Ç`a(Ÿ±Çbmfb0.Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfb1.Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`hset_ylimŸ±Ç`a(Ÿ±Çbmfb0.Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfb1.Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1x6# save the figure as a bytes string in the svg format.Ÿ±Ç`a
Ÿ±Ç`afŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bioŸ±Çaoa.Ÿ±Ç`gBytesIOŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`gsavefigŸ±Ç`a(Ÿ±Ç`afŸ±Ç`a,Ÿ±Ç`a Ÿ±ÇbnbfformatŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2csvgŸ±Çbs2a"Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1x'# filter definition for a gaussian blurŸ±Ç`a
Ÿ±Ç`jfilter_defŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Çbs2c"""Ÿ±Çbs2a
Ÿ±Çbs2n  <defs xmlns=Ÿ±Çbs2a'Ÿ±Çbs2xhttp://www.w3.org/2000/svgŸ±Çbs2a'Ÿ±Çbs2a
Ÿ±Çbs2t        xmlns:xlink=Ÿ±Çbs2a'Ÿ±Çbs2xhttp://www.w3.org/1999/xlinkŸ±Çbs2a'Ÿ±Çbs2a>Ÿ±Çbs2a
Ÿ±Çbs2o    <filter id=Ÿ±Çbs2a'Ÿ±Çbs2jdropshadowŸ±Çbs2a'Ÿ±Çbs2h height=Ÿ±Çbs2a'Ÿ±Çbs2c1.2Ÿ±Çbs2a'Ÿ±Çbs2g width=Ÿ±Çbs2a'Ÿ±Çbs2c1.2Ÿ±Çbs2a'Ÿ±Çbs2a>Ÿ±Çbs2a
Ÿ±Çbs2x      <feGaussianBlur result=Ÿ±Çbs2a'Ÿ±Çbs2dblurŸ±Çbs2a'Ÿ±Çbs2n stdDeviation=Ÿ±Çbs2a'Ÿ±Çbs2a3Ÿ±Çbs2a'Ÿ±Çbs2b/>Ÿ±Çbs2a
Ÿ±Çbs2m    </filter>Ÿ±Çbs2a
Ÿ±Çbs2i  </defs>Ÿ±Çbs2a
Ÿ±Çbs2c"""Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1w# read in the saved svgŸ±Ç`a
Ÿ±Ç`dtreeŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`exmlidŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bETŸ±Çaoa.Ÿ±Ç`eXMLIDŸ±Ç`a(Ÿ±Ç`afŸ±Çaoa.Ÿ±Ç`hgetvalueŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1x3# insert the filter definition in the svg dom tree.Ÿ±Ç`a
Ÿ±Ç`dtreeŸ±Çaoa.Ÿ±Ç`finsertŸ±Ç`a(Ÿ±Çbmia0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`bETŸ±Çaoa.Ÿ±Ç`cXMLŸ±Ç`a(Ÿ±Ç`jfilter_defŸ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±ÇakcforŸ±Ç`a Ÿ±Ç`alŸ±Ç`a Ÿ±ÇbowbinŸ±Ç`a Ÿ±Ç`a[Ÿ±Ç`bl1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`bl2Ÿ±Ç`a]Ÿ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Çbc1x'# pick up the svg element with given idŸ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`fshadowŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`exmlidŸ±Ç`a[Ÿ±Ç`alŸ±Çaoa.Ÿ±Ç`iget_labelŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a Ÿ±Çaoa+Ÿ±Ç`a Ÿ±Çbs2a"Ÿ±Çbs2g_shadowŸ±Çbs2a"Ÿ±Ç`a]Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Çbc1u# apply shadow filterŸ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`fshadowŸ±Çaoa.Ÿ±Ç`csetŸ±Ç`a(Ÿ±Çbs2a"Ÿ±Çbs2ffilterŸ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1purl(#dropshadow)Ÿ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`bfnŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Çbs2a"Ÿ±Çbs2ssvg_filter_line.svgŸ±Çbs2a"Ÿ±Ç`a
Ÿ±ÇbnbeprintŸ±Ç`a(Ÿ±ÇbsaafŸ±Çbs2a"Ÿ±Çbs2gSaving Ÿ±Çbs2a'Ÿ±Çbsia{Ÿ±Ç`bfnŸ±Çbsia}Ÿ±Çbs2a'Ÿ±Çbs2a"Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`bETŸ±Çaoa.Ÿ±Ç`kElementTreeŸ±Ç`a(Ÿ±Ç`dtreeŸ±Ç`a)Ÿ±Çaoa.Ÿ±Ç`ewriteŸ±Ç`a(Ÿ±Ç`bfnŸ±Ç`a)Ÿ±Ç`a
`dNoneˆ