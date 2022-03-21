ŸØÇÅŸ¥Éô&Ÿ±Çbsdy"""
==============
BboxImage Demo
==============

A `~matplotlib.image.BboxImage` can be used to position an image according to
a bounding box. This demo shows how to show an image inside a `.text.Text`'s
bounding box as well as how to manually create a bounding box for the image.
"""Ÿ±Ç`a
Ÿ±ÇbknfimportŸ±Ç`a Ÿ±ÇbnnŸ¢ÑjmatplotlibŸ†Ñjmatplotlibe3.5.1fmodulejmatplotlibfmoduleıŸ±Çbnna.Ÿ±ÇbnnfpyplotŸ±Ç`a Ÿ±ÇakbasŸ±Ç`a Ÿ±ÇbnncpltŸ±Ç`a
Ÿ±ÇbknfimportŸ±Ç`a Ÿ±ÇbnnŸ¢ÑenumpyŸ†Ñenumpyf1.22.3fmoduleenumpyfmoduleıŸ±Ç`a Ÿ±ÇakbasŸ±Ç`a Ÿ±ÇbnnbnpŸ±Ç`a
Ÿ±ÇbkndfromŸ±Ç`a Ÿ±ÇbnnŸ¢ÑjmatplotlibŸ†Ñjmatplotlibe3.5.1fmodulejmatplotlibfmoduleıŸ±Çbnna.Ÿ±ÇbnneimageŸ±Ç`a Ÿ±ÇbknfimportŸ±Ç`a Ÿ±Ç`iBboxImageŸ±Ç`a
Ÿ±ÇbkndfromŸ±Ç`a Ÿ±ÇbnnŸ¢ÑjmatplotlibŸ†Ñjmatplotlibe3.5.1fmodulejmatplotlibfmoduleıŸ±Çbnna.Ÿ±ÇbnnjtransformsŸ±Ç`a Ÿ±ÇbknfimportŸ±Ç`a Ÿ±Ç`dBboxŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`oTransformedBboxŸ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`cfigŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`a(Ÿ±Ç`cax1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`cax2Ÿ±Ç`a)Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`hsubplotsŸ±Ç`a(Ÿ±Ç`encolsŸ±Çaoa=Ÿ±Çbmia2Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1x# ----------------------------Ÿ±Ç`a
Ÿ±Çbc1x# Create a BboxImage with TextŸ±Ç`a
Ÿ±Çbc1x# ----------------------------Ÿ±Ç`a
Ÿ±Ç`ctxtŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cax1Ÿ±Çaoa.Ÿ±Ç`dtextŸ±Ç`a(Ÿ±Çbmfc0.5Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfc0.5Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs2a"Ÿ±Çbs2dtestŸ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dsizeŸ±Çaoa=Ÿ±Çbmib30Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`bhaŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2fcenterŸ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ecolorŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2awŸ±Çbs2a"Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`fkwargsŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±ÇbnbddictŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`jbbox_imageŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`iBboxImageŸ±Ç`a(Ÿ±Ç`ctxtŸ±Çaoa.Ÿ±Ç`qget_window_extentŸ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`w                       Ÿ±Ç`dnormŸ±Çaoa=Ÿ±ÇbkcdNoneŸ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`w                       Ÿ±Ç`foriginŸ±Çaoa=Ÿ±ÇbkcdNoneŸ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`w                       Ÿ±Ç`gclip_onŸ±Çaoa=Ÿ±ÇbkceFalseŸ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`w                       Ÿ±Çaoa*Ÿ±Çaoa*Ÿ±Ç`fkwargsŸ±Ç`a
Ÿ±Ç`w                       Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`aaŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`farangeŸ±Ç`a(Ÿ±Çbmic256Ÿ±Ç`a)Ÿ±Çaoa.Ÿ±Ç`greshapeŸ±Ç`a(Ÿ±Çbmia1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmic256Ÿ±Ç`a)Ÿ±Çaoa/Ÿ±Çbmfd256.Ÿ±Ç`a
Ÿ±Ç`jbbox_imageŸ±Çaoa.Ÿ±Ç`hset_dataŸ±Ç`a(Ÿ±Ç`aaŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cax1Ÿ±Çaoa.Ÿ±Ç`jadd_artistŸ±Ç`a(Ÿ±Ç`jbbox_imageŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1x&# ------------------------------------Ÿ±Ç`a
Ÿ±Çbc1x&# Create a BboxImage for each colormapŸ±Ç`a
Ÿ±Çbc1x&# ------------------------------------Ÿ±Ç`a
Ÿ±Ç`aaŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`hlinspaceŸ±Ç`a(Ÿ±Çbmia0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmic256Ÿ±Ç`a)Ÿ±Çaoa.Ÿ±Ç`greshapeŸ±Ç`a(Ÿ±Çbmia1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çaoa-Ÿ±Çbmia1Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`aaŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`fvstackŸ±Ç`a(Ÿ±Ç`a(Ÿ±Ç`aaŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`aaŸ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1x1# List of all colormaps; skip reversed colormaps.Ÿ±Ç`a
Ÿ±Ç`jcmap_namesŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±ÇbnbfsortedŸ±Ç`a(Ÿ±Ç`amŸ±Ç`a Ÿ±ÇakcforŸ±Ç`a Ÿ±Ç`amŸ±Ç`a Ÿ±ÇbowbinŸ±Ç`a Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`icolormapsŸ±Ç`a Ÿ±ÇakbifŸ±Ç`a Ÿ±ÇbowcnotŸ±Ç`a Ÿ±Ç`amŸ±Çaoa.Ÿ±Ç`hendswithŸ±Ç`a(Ÿ±Çbs2a"Ÿ±Çbs2b_rŸ±Çbs2a"Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`dncolŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Çbmia2Ÿ±Ç`a
Ÿ±Ç`dnrowŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±ÇbnbclenŸ±Ç`a(Ÿ±Ç`jcmap_namesŸ±Ç`a)Ÿ±Ç`a Ÿ±Çaoa/Ÿ±Çaoa/Ÿ±Ç`a Ÿ±Ç`dncolŸ±Ç`a Ÿ±Çaoa+Ÿ±Ç`a Ÿ±Çbmia1Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`mxpad_fractionŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Çbmfc0.3Ÿ±Ç`a
Ÿ±Ç`bdxŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Çbmia1Ÿ±Ç`a Ÿ±Çaoa/Ÿ±Ç`a Ÿ±Ç`a(Ÿ±Ç`dncolŸ±Ç`a Ÿ±Çaoa+Ÿ±Ç`a Ÿ±Ç`mxpad_fractionŸ±Ç`a Ÿ±Çaoa*Ÿ±Ç`a Ÿ±Ç`a(Ÿ±Ç`dncolŸ±Ç`a Ÿ±Çaoa-Ÿ±Ç`a Ÿ±Çbmia1Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`mypad_fractionŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Çbmfc0.3Ÿ±Ç`a
Ÿ±Ç`bdyŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Çbmia1Ÿ±Ç`a Ÿ±Çaoa/Ÿ±Ç`a Ÿ±Ç`a(Ÿ±Ç`dnrowŸ±Ç`a Ÿ±Çaoa+Ÿ±Ç`a Ÿ±Ç`mypad_fractionŸ±Ç`a Ÿ±Çaoa*Ÿ±Ç`a Ÿ±Ç`a(Ÿ±Ç`dnrowŸ±Ç`a Ÿ±Çaoa-Ÿ±Ç`a Ÿ±Çbmia1Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±ÇakcforŸ±Ç`a Ÿ±Ç`aiŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`icmap_nameŸ±Ç`a Ÿ±ÇbowbinŸ±Ç`a Ÿ±ÇbnbienumerateŸ±Ç`a(Ÿ±Ç`jcmap_namesŸ±Ç`a)Ÿ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`bixŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`biyŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±ÇbnbfdivmodŸ±Ç`a(Ÿ±Ç`aiŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dnrowŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`ebbox0Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`dBboxŸ±Çaoa.Ÿ±Ç`kfrom_boundsŸ±Ç`a(Ÿ±Ç`bixŸ±Çaoa*Ÿ±Ç`bdxŸ±Çaoa*Ÿ±Ç`a(Ÿ±Çbmia1Ÿ±Ç`a Ÿ±Çaoa+Ÿ±Ç`a Ÿ±Ç`mxpad_fractionŸ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`x                             Ÿ±Çbmfb1.Ÿ±Ç`a Ÿ±Çaoa-Ÿ±Ç`a Ÿ±Ç`biyŸ±Çaoa*Ÿ±Ç`bdyŸ±Çaoa*Ÿ±Ç`a(Ÿ±Çbmia1Ÿ±Ç`a Ÿ±Çaoa+Ÿ±Ç`a Ÿ±Ç`mypad_fractionŸ±Ç`a)Ÿ±Ç`a Ÿ±Çaoa-Ÿ±Ç`a Ÿ±Ç`bdyŸ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`x                             Ÿ±Ç`bdxŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`bdyŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`dbboxŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`oTransformedBboxŸ±Ç`a(Ÿ±Ç`ebbox0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`cax2Ÿ±Çaoa.Ÿ±Ç`itransAxesŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`jbbox_imageŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`iBboxImageŸ±Ç`a(Ÿ±Ç`dbboxŸ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`x                           Ÿ±Ç`dcmapŸ±Çaoa=Ÿ±Ç`icmap_nameŸ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`x                           Ÿ±Ç`dnormŸ±Çaoa=Ÿ±ÇbkcdNoneŸ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`x                           Ÿ±Ç`foriginŸ±Çaoa=Ÿ±ÇbkcdNoneŸ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`x                           Ÿ±Çaoa*Ÿ±Çaoa*Ÿ±Ç`fkwargsŸ±Ç`a
Ÿ±Ç`x                           Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`jbbox_imageŸ±Çaoa.Ÿ±Ç`hset_dataŸ±Ç`a(Ÿ±Ç`aaŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`cax2Ÿ±Çaoa.Ÿ±Ç`jadd_artistŸ±Ç`a(Ÿ±Ç`jbbox_imageŸ±Ç`a)Ÿ±Ç`a
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
Ÿ±Çbc1x##    - `matplotlib.image.BboxImage`Ÿ±Ç`a
Ÿ±Çbc1x##    - `matplotlib.transforms.Bbox`Ÿ±Ç`a
Ÿ±Çbc1x.#    - `matplotlib.transforms.TransformedBbox`Ÿ±Ç`a
Ÿ±Çbc1x#    - `matplotlib.text.Text`Ÿ±Ç`a
`dNoneˆ