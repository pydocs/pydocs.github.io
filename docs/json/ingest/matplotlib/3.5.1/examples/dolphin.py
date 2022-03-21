ŸØÇÅŸ¥ÉôŸ±Çbsdx«"""
========
Dolphins
========

This example shows how to draw, and manipulate shapes given vertices
and nodes using the `~.path.Path`, `~.patches.PathPatch` and
`~matplotlib.transforms` classes.
"""Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±ÇbknfimportŸ±Ç`a Ÿ±ÇbnnŸ¢ÑjmatplotlibŸ†Ñjmatplotlibe3.5.1fmodulejmatplotlibfmoduleıŸ±Çbnna.Ÿ±ÇbnnbcmŸ±Ç`a Ÿ±ÇakbasŸ±Ç`a Ÿ±ÇbnnbcmŸ±Ç`a
Ÿ±ÇbknfimportŸ±Ç`a Ÿ±ÇbnnŸ¢ÑjmatplotlibŸ†Ñjmatplotlibe3.5.1fmodulejmatplotlibfmoduleıŸ±Çbnna.Ÿ±ÇbnnfpyplotŸ±Ç`a Ÿ±ÇakbasŸ±Ç`a Ÿ±ÇbnncpltŸ±Ç`a
Ÿ±ÇbkndfromŸ±Ç`a Ÿ±ÇbnnŸ¢ÑjmatplotlibŸ†Ñjmatplotlibe3.5.1fmodulejmatplotlibfmoduleıŸ±Çbnna.Ÿ±ÇbnngpatchesŸ±Ç`a Ÿ±ÇbknfimportŸ±Ç`a Ÿ±Ç`fCircleŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`iPathPatchŸ±Ç`a
Ÿ±ÇbkndfromŸ±Ç`a Ÿ±ÇbnnŸ¢ÑjmatplotlibŸ†Ñjmatplotlibe3.5.1fmodulejmatplotlibfmoduleıŸ±Çbnna.Ÿ±ÇbnndpathŸ±Ç`a Ÿ±ÇbknfimportŸ±Ç`a Ÿ±Ç`dPathŸ±Ç`a
Ÿ±ÇbkndfromŸ±Ç`a Ÿ±ÇbnnŸ¢ÑjmatplotlibŸ†Ñjmatplotlibe3.5.1fmodulejmatplotlibfmoduleıŸ±Çbnna.Ÿ±ÇbnnjtransformsŸ±Ç`a Ÿ±ÇbknfimportŸ±Ç`a Ÿ±Ç`hAffine2DŸ±Ç`a
Ÿ±ÇbknfimportŸ±Ç`a Ÿ±ÇbnnŸ¢ÑenumpyŸ†Ñenumpyf1.22.3fmoduleenumpyfmoduleıŸ±Ç`a Ÿ±ÇakbasŸ±Ç`a Ÿ±ÇbnnbnpŸ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1x)# Fixing random state for reproducibilityŸ±Ç`a
Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`frandomŸ±Çaoa.Ÿ±Ç`dseedŸ±Ç`a(Ÿ±Çbmih19680801Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`arŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`frandomŸ±Çaoa.Ÿ±Ç`drandŸ±Ç`a(Ÿ±Çbmib50Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`atŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`frandomŸ±Çaoa.Ÿ±Ç`drandŸ±Ç`a(Ÿ±Çbmib50Ÿ±Ç`a)Ÿ±Ç`a Ÿ±Çaoa*Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`bpiŸ±Ç`a Ÿ±Çaoa*Ÿ±Ç`a Ÿ±Çbmfc2.0Ÿ±Ç`a
Ÿ±Ç`axŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`arŸ±Ç`a Ÿ±Çaoa*Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`ccosŸ±Ç`a(Ÿ±Ç`atŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`ayŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`arŸ±Ç`a Ÿ±Çaoa*Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`csinŸ±Ç`a(Ÿ±Ç`atŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`cfigŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`baxŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`hsubplotsŸ±Ç`a(Ÿ±Ç`gfigsizeŸ±Çaoa=Ÿ±Ç`a(Ÿ±Çbmia6Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia6Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`fcircleŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`fCircleŸ±Ç`a(Ÿ±Ç`a(Ÿ±Çbmia0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia0Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ifacecolorŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1dnoneŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`p                Ÿ±Ç`iedgecolorŸ±Çaoa=Ÿ±Ç`a(Ÿ±Çbmia0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfc0.8Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfc0.8Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ilinewidthŸ±Çaoa=Ÿ±Çbmia3Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ealphaŸ±Çaoa=Ÿ±Çbmfc0.5Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`iadd_patchŸ±Ç`a(Ÿ±Ç`fcircleŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`bimŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`fimshowŸ±Ç`a(Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`frandomŸ±Çaoa.Ÿ±Ç`frandomŸ±Ç`a(Ÿ±Ç`a(Ÿ±Çbmic100Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmic100Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`p                Ÿ±Ç`foriginŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1elowerŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dcmapŸ±Çaoa=Ÿ±Ç`bcmŸ±Çaoa.Ÿ±Ç`fwinterŸ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`p                Ÿ±Ç`minterpolationŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1hspline36Ÿ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`p                Ÿ±Ç`fextentŸ±Çaoa=Ÿ±Ç`a(Ÿ±Ç`a[Ÿ±Çaoa-Ÿ±Çbmia1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çaoa-Ÿ±Çbmia1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia1Ÿ±Ç`a]Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`bimŸ±Çaoa.Ÿ±Ç`mset_clip_pathŸ±Ç`a(Ÿ±Ç`fcircleŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`dplotŸ±Ç`a(Ÿ±Ç`axŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ayŸ±Ç`a,Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1aoŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ecolorŸ±Çaoa=Ÿ±Ç`a(Ÿ±Çbmfc0.9Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfc0.9Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfc1.0Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ealphaŸ±Çaoa=Ÿ±Çbmfc0.8Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1x4# Dolphin from OpenClipart library by Andy FitzsimonŸ±Ç`a
Ÿ±Çbc1xD#   <cc:License rdf:about="http://web.resource.org/cc/PublicDomain">Ÿ±Ç`a
Ÿ±Çbc1xJ#     <cc:permits rdf:resource="http://web.resource.org/cc/Reproduction"/>Ÿ±Ç`a
Ÿ±Çbc1xJ#     <cc:permits rdf:resource="http://web.resource.org/cc/Distribution"/>Ÿ±Ç`a
Ÿ±Çbc1xM#     <cc:permits rdf:resource="http://web.resource.org/cc/DerivativeWorks"/>Ÿ±Ç`a
Ÿ±Çbc1q#   </cc:License>Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`gdolphinŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Çbs2c"""Ÿ±Çbs2a
Ÿ±Çbs2xEM -0.59739425,160.18173 C -0.62740401,160.18885 -0.57867129,160.11183Ÿ±Çbs2a
Ÿ±Çbs2xB-0.57867129,160.11183 C -0.57867129,160.11183 -0.5438361,159.89315Ÿ±Çbs2a
Ÿ±Çbs2xC-0.39514638,159.81496 C -0.24645668,159.73678 -0.18316813,159.71981Ÿ±Çbs2a
Ÿ±Çbs2xC-0.18316813,159.71981 C -0.18316813,159.71981 -0.10322971,159.58124Ÿ±Çbs2a
Ÿ±Çbs2xF-0.057804323,159.58725 C -0.029723983,159.58913 -0.061841603,159.60356Ÿ±Çbs2a
Ÿ±Çbs2xF-0.071265813,159.62815 C -0.080250183,159.65325 -0.082918513,159.70554Ÿ±Çbs2a
Ÿ±Çbs2xF-0.061841203,159.71248 C -0.040763903,159.7194 -0.0066711426,159.71091Ÿ±Çbs2a
Ÿ±Çbs2xA0.077336307,159.73612 C 0.16879567,159.76377 0.28380306,159.86448Ÿ±Çbs2a
Ÿ±Çbs2x=0.31516668,159.91533 C 0.3465303,159.96618 0.5011127,160.1771Ÿ±Çbs2a
Ÿ±Çbs2x>0.5011127,160.1771 C 0.63668998,160.19238 0.67763022,160.31259Ÿ±Çbs2a
Ÿ±Çbs2x@0.66556395,160.32668 C 0.65339985,160.34212 0.66350443,160.33642Ÿ±Çbs2a
Ÿ±Çbs2x>0.64907098,160.33088 C 0.63463742,160.32533 0.61309688,160.297Ÿ±Çbs2a
Ÿ±Çbs2x?0.5789627,160.29339 C 0.54348657,160.28968 0.52329693,160.27674Ÿ±Çbs2a
Ÿ±Çbs2x@0.50728856,160.27737 C 0.49060916,160.27795 0.48965803,160.31565Ÿ±Çbs2a
Ÿ±Çbs2x?0.46114204,160.33673 C 0.43329696,160.35786 0.4570711,160.39871Ÿ±Çbs2a
Ÿ±Çbs2x?0.43309565,160.40685 C 0.4105108,160.41442 0.39416631,160.33027Ÿ±Çbs2a
Ÿ±Çbs2x>0.3954995,160.2935 C 0.39683269,160.25672 0.43807996,160.21522Ÿ±Çbs2a
Ÿ±Çbs2x?0.44567915,160.19734 C 0.45327833,160.17946 0.27946869,159.9424Ÿ±Çbs2a
Ÿ±Çbs2xD-0.061852613,159.99845 C -0.083965233,160.0427 -0.26176109,160.06683Ÿ±Çbs2a
Ÿ±Çbs2xC-0.26176109,160.06683 C -0.30127962,160.07028 -0.21167141,160.09731Ÿ±Çbs2a
Ÿ±Çbs2xB-0.24649368,160.1011 C -0.32642366,160.11569 -0.34521187,160.06895Ÿ±Çbs2a
Ÿ±Çbs2x@-0.40622293,160.0819 C -0.467234,160.09485 -0.56738444,160.17461Ÿ±Çbs2a
Ÿ±Çbs2u-0.59739425,160.18173Ÿ±Çbs2a
Ÿ±Çbs2c"""Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`hverticesŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`a[Ÿ±Ç`a]Ÿ±Ç`a
Ÿ±Ç`ecodesŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`a[Ÿ±Ç`a]Ÿ±Ç`a
Ÿ±Ç`epartsŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`gdolphinŸ±Çaoa.Ÿ±Ç`esplitŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`aiŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Çbmia0Ÿ±Ç`a
Ÿ±Ç`hcode_mapŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`a{Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Çbs1a'Ÿ±Çbs1aMŸ±Çbs1a'Ÿ±Ç`a:Ÿ±Ç`a Ÿ±Ç`dPathŸ±Çaoa.Ÿ±Ç`fMOVETOŸ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Çbs1a'Ÿ±Çbs1aCŸ±Çbs1a'Ÿ±Ç`a:Ÿ±Ç`a Ÿ±Ç`dPathŸ±Çaoa.Ÿ±Ç`fCURVE4Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Çbs1a'Ÿ±Çbs1aLŸ±Çbs1a'Ÿ±Ç`a:Ÿ±Ç`a Ÿ±Ç`dPathŸ±Çaoa.Ÿ±Ç`fLINETOŸ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`a}Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±ÇakewhileŸ±Ç`a Ÿ±Ç`aiŸ±Ç`a Ÿ±Çaoa<Ÿ±Ç`a Ÿ±ÇbnbclenŸ±Ç`a(Ÿ±Ç`epartsŸ±Ç`a)Ÿ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`ipath_codeŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`hcode_mapŸ±Ç`a[Ÿ±Ç`epartsŸ±Ç`a[Ÿ±Ç`aiŸ±Ç`a]Ÿ±Ç`a]Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`gnpointsŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`dPathŸ±Çaoa.Ÿ±Ç`uNUM_VERTICES_FOR_CODEŸ±Ç`a[Ÿ±Ç`ipath_codeŸ±Ç`a]Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`ecodesŸ±Çaoa.Ÿ±Ç`fextendŸ±Ç`a(Ÿ±Ç`a[Ÿ±Ç`ipath_codeŸ±Ç`a]Ÿ±Ç`a Ÿ±Çaoa*Ÿ±Ç`a Ÿ±Ç`gnpointsŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`hverticesŸ±Çaoa.Ÿ±Ç`fextendŸ±Ç`a(Ÿ±Ç`a[Ÿ±Ç`a[Ÿ±Çaoa*Ÿ±ÇbnbcmapŸ±Ç`a(Ÿ±ÇbnbefloatŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ayŸ±Çaoa.Ÿ±Ç`esplitŸ±Ç`a(Ÿ±Çbs1a'Ÿ±Çbs1a,Ÿ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a]Ÿ±Ç`a
Ÿ±Ç`u                     Ÿ±ÇakcforŸ±Ç`a Ÿ±Ç`ayŸ±Ç`a Ÿ±ÇbowbinŸ±Ç`a Ÿ±Ç`epartsŸ±Ç`a[Ÿ±Ç`aiŸ±Ç`a Ÿ±Çaoa+Ÿ±Ç`a Ÿ±Çbmia1Ÿ±Ç`a:Ÿ±Ç`a]Ÿ±Ç`a[Ÿ±Ç`a:Ÿ±Ç`gnpointsŸ±Ç`a]Ÿ±Ç`a]Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`aiŸ±Ç`a Ÿ±Çaoa+Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`gnpointsŸ±Ç`a Ÿ±Çaoa+Ÿ±Ç`a Ÿ±Çbmia1Ÿ±Ç`a
Ÿ±Ç`hverticesŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`earrayŸ±Ç`a(Ÿ±Ç`hverticesŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`hverticesŸ±Ç`a[Ÿ±Ç`a:Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia1Ÿ±Ç`a]Ÿ±Ç`a Ÿ±Çaoa-Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Çbmic160Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`ldolphin_pathŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`dPathŸ±Ç`a(Ÿ±Ç`hverticesŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ecodesŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`mdolphin_patchŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`iPathPatchŸ±Ç`a(Ÿ±Ç`ldolphin_pathŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ifacecolorŸ±Çaoa=Ÿ±Ç`a(Ÿ±Çbmfc0.6Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfc0.6Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfc0.6Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`x                          Ÿ±Ç`iedgecolorŸ±Çaoa=Ÿ±Ç`a(Ÿ±Çbmfc0.0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfc0.0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfc0.0Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`iadd_patchŸ±Ç`a(Ÿ±Ç`mdolphin_patchŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`hverticesŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`hAffine2DŸ±Ç`a(Ÿ±Ç`a)Ÿ±Çaoa.Ÿ±Ç`jrotate_degŸ±Ç`a(Ÿ±Çbmib60Ÿ±Ç`a)Ÿ±Çaoa.Ÿ±Ç`itransformŸ±Ç`a(Ÿ±Ç`hverticesŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`mdolphin_path2Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`dPathŸ±Ç`a(Ÿ±Ç`hverticesŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ecodesŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`ndolphin_patch2Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`iPathPatchŸ±Ç`a(Ÿ±Ç`mdolphin_path2Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ifacecolorŸ±Çaoa=Ÿ±Ç`a(Ÿ±Çbmfc0.5Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfc0.5Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfc0.5Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`x                           Ÿ±Ç`iedgecolorŸ±Çaoa=Ÿ±Ç`a(Ÿ±Çbmfc0.0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfc0.0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfc0.0Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`iadd_patchŸ±Ç`a(Ÿ±Ç`ndolphin_patch2Ÿ±Ç`a)Ÿ±Ç`a
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
Ÿ±Çbc1x#    - `matplotlib.path`Ÿ±Ç`a
Ÿ±Çbc1x#    - `matplotlib.path.Path`Ÿ±Ç`a
Ÿ±Çbc1x#    - `matplotlib.patches`Ÿ±Ç`a
Ÿ±Çbc1x%#    - `matplotlib.patches.PathPatch`Ÿ±Ç`a
Ÿ±Çbc1x"#    - `matplotlib.patches.Circle`Ÿ±Ç`a
Ÿ±Çbc1x'#    - `matplotlib.axes.Axes.add_patch`Ÿ±Ç`a
Ÿ±Çbc1x#    - `matplotlib.transforms`Ÿ±Ç`a
Ÿ±Çbc1x'#    - `matplotlib.transforms.Affine2D`Ÿ±Ç`a
Ÿ±Çbc1x2#    - `matplotlib.transforms.Affine2D.rotate_deg`Ÿ±Ç`a
`dNoneˆ