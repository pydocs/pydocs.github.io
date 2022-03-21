Ù¯‚Ù´ƒ™±Ù±‚bsdy	"""
==============
SVG Filter Pie
==============

Demonstrate SVG filtering effects which might be used with Matplotlib.
The pie chart drawing code is borrowed from pie_demo.py

Note that the filtering effects are only effective if your SVG renderer
support it.
"""Ù±‚`a
Ù±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnbioÙ±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnncxmlÙ±‚bnna.Ù±‚bnneetreeÙ±‚bnna.Ù±‚bnnkElementTreeÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnnbETÙ±‚`a
Ù±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnnfpyplotÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnncpltÙ±‚`a
Ù±‚bkndfromÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnngpatchesÙ±‚`a Ù±‚bknfimportÙ±‚`a Ù±‚`fShadowÙ±‚`a
Ù±‚`a
Ù±‚bc1x# make a square figure and axesÙ±‚`a
Ù±‚`cfigÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cpltÙ±‚aoa.Ù±‚`ffigureÙ±‚`a(Ù±‚`gfigsizeÙ±‚aoa=Ù±‚`a(Ù±‚bmia6Ù±‚`a,Ù±‚`a Ù±‚bmia6Ù±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`baxÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cfigÙ±‚aoa.Ù±‚`hadd_axesÙ±‚`a(Ù±‚`a[Ù±‚bmfc0.1Ù±‚`a,Ù±‚`a Ù±‚bmfc0.1Ù±‚`a,Ù±‚`a Ù±‚bmfc0.8Ù±‚`a,Ù±‚`a Ù±‚bmfc0.8Ù±‚`a]Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`flabelsÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bs1a'Ù±‚bs1eFrogsÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚bs1a'Ù±‚bs1dHogsÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚bs1a'Ù±‚bs1dDogsÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚bs1a'Ù±‚bs1dLogsÙ±‚bs1a'Ù±‚`a
Ù±‚`efracsÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`a[Ù±‚bmib15Ù±‚`a,Ù±‚`a Ù±‚bmib30Ù±‚`a,Ù±‚`a Ù±‚bmib45Ù±‚`a,Ù±‚`a Ù±‚bmib10Ù±‚`a]Ù±‚`a
Ù±‚`a
Ù±‚`gexplodeÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`a(Ù±‚bmia0Ù±‚`a,Ù±‚`a Ù±‚bmfd0.05Ù±‚`a,Ù±‚`a Ù±‚bmia0Ù±‚`a,Ù±‚`a Ù±‚bmia0Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚bc1xF# We want to draw the shadow for each pie but we will not use "shadow"Ù±‚`a
Ù±‚bc1xA# option as it doesn't save the references to the shadow patches.Ù±‚`a
Ù±‚`dpiesÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`baxÙ±‚aoa.Ù±‚`cpieÙ±‚`a(Ù±‚`efracsÙ±‚`a,Ù±‚`a Ù±‚`gexplodeÙ±‚aoa=Ù±‚`gexplodeÙ±‚`a,Ù±‚`a Ù±‚`flabelsÙ±‚aoa=Ù±‚`flabelsÙ±‚`a,Ù±‚`a Ù±‚`gautopctÙ±‚aoa=Ù±‚bs1a'Ù±‚bsie%1.1fÙ±‚bsib%%Ù±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚akcforÙ±‚`a Ù±‚`awÙ±‚`a Ù±‚bowbinÙ±‚`a Ù±‚`dpiesÙ±‚`a[Ù±‚bmia0Ù±‚`a]Ù±‚`a:Ù±‚`a
Ù±‚`d    Ù±‚bc1x# set the id with the label.Ù±‚`a
Ù±‚`d    Ù±‚`awÙ±‚aoa.Ù±‚`gset_gidÙ±‚`a(Ù±‚`awÙ±‚aoa.Ù±‚`iget_labelÙ±‚`a(Ù±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚bc1x+# we don't want to draw the edge of the pieÙ±‚`a
Ù±‚`d    Ù±‚`awÙ±‚aoa.Ù±‚`mset_edgecolorÙ±‚`a(Ù±‚bs2a"Ù±‚bs2dnoneÙ±‚bs2a"Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚akcforÙ±‚`a Ù±‚`awÙ±‚`a Ù±‚bowbinÙ±‚`a Ù±‚`dpiesÙ±‚`a[Ù±‚bmia0Ù±‚`a]Ù±‚`a:Ù±‚`a
Ù±‚`d    Ù±‚bc1u# create shadow patchÙ±‚`a
Ù±‚`d    Ù±‚`asÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`fShadowÙ±‚`a(Ù±‚`awÙ±‚`a,Ù±‚`a Ù±‚aoa-Ù±‚bmfd0.01Ù±‚`a,Ù±‚`a Ù±‚aoa-Ù±‚bmfd0.01Ù±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`asÙ±‚aoa.Ù±‚`gset_gidÙ±‚`a(Ù±‚`awÙ±‚aoa.Ù±‚`gget_gidÙ±‚`a(Ù±‚`a)Ù±‚`a Ù±‚aoa+Ù±‚`a Ù±‚bs2a"Ù±‚bs2g_shadowÙ±‚bs2a"Ù±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`asÙ±‚aoa.Ù±‚`jset_zorderÙ±‚`a(Ù±‚`awÙ±‚aoa.Ù±‚`jget_zorderÙ±‚`a(Ù±‚`a)Ù±‚`a Ù±‚aoa-Ù±‚`a Ù±‚bmfc0.1Ù±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`baxÙ±‚aoa.Ù±‚`iadd_patchÙ±‚`a(Ù±‚`asÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚bc1f# saveÙ±‚`a
Ù±‚`afÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bioÙ±‚aoa.Ù±‚`gBytesIOÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`cpltÙ±‚aoa.Ù±‚`gsavefigÙ±‚`a(Ù±‚`afÙ±‚`a,Ù±‚`a Ù±‚bnbfformatÙ±‚aoa=Ù±‚bs2a"Ù±‚bs2csvgÙ±‚bs2a"Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚bc1xI# Filter definition for shadow using a gaussian blur and lighting effect.Ù±‚`a
Ù±‚bc1xJ# The lighting filter is copied from http://www.w3.org/TR/SVG/filters.htmlÙ±‚`a
Ù±‚`a
Ù±‚bc1xF# I tested it with Inkscape and Firefox3. "Gaussian blur" is supportedÙ±‚`a
Ù±‚bc1x># in both, but the lighting effect only in Inkscape. Also noteÙ±‚`a
Ù±‚bc1x5# that, Inkscape's exporting also may not support it.Ù±‚`a
Ù±‚`a
Ù±‚`jfilter_defÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bs2c"""Ù±‚bs2a
Ù±‚bs2n  <defs xmlns=Ù±‚bs2a'Ù±‚bs2xhttp://www.w3.org/2000/svgÙ±‚bs2a'Ù±‚bs2a
Ù±‚bs2t        xmlns:xlink=Ù±‚bs2a'Ù±‚bs2xhttp://www.w3.org/1999/xlinkÙ±‚bs2a'Ù±‚bs2a>Ù±‚bs2a
Ù±‚bs2o    <filter id=Ù±‚bs2a'Ù±‚bs2jdropshadowÙ±‚bs2a'Ù±‚bs2h height=Ù±‚bs2a'Ù±‚bs2c1.2Ù±‚bs2a'Ù±‚bs2g width=Ù±‚bs2a'Ù±‚bs2c1.2Ù±‚bs2a'Ù±‚bs2a>Ù±‚bs2a
Ù±‚bs2x      <feGaussianBlur result=Ù±‚bs2a'Ù±‚bs2dblurÙ±‚bs2a'Ù±‚bs2n stdDeviation=Ù±‚bs2a'Ù±‚bs2a2Ù±‚bs2a'Ù±‚bs2b/>Ù±‚bs2a
Ù±‚bs2m    </filter>Ù±‚bs2a
Ù±‚bs2a
Ù±‚bs2o    <filter id=Ù±‚bs2a'Ù±‚bs2hMyFilterÙ±‚bs2a'Ù±‚bs2m filterUnits=Ù±‚bs2a'Ù±‚bs2qobjectBoundingBoxÙ±‚bs2a'Ù±‚bs2a
Ù±‚bs2n            x=Ù±‚bs2a'Ù±‚bs2a0Ù±‚bs2a'Ù±‚bs2c y=Ù±‚bs2a'Ù±‚bs2a0Ù±‚bs2a'Ù±‚bs2g width=Ù±‚bs2a'Ù±‚bs2a1Ù±‚bs2a'Ù±‚bs2h height=Ù±‚bs2a'Ù±‚bs2a1Ù±‚bs2a'Ù±‚bs2a>Ù±‚bs2a
Ù±‚bs2x      <feGaussianBlur in=Ù±‚bs2a'Ù±‚bs2kSourceAlphaÙ±‚bs2a'Ù±‚bs2n stdDeviation=Ù±‚bs2a'Ù±‚bs2a4Ù±‚bs2a%Ù±‚bs2a'Ù±‚bs2h result=Ù±‚bs2a'Ù±‚bs2dblurÙ±‚bs2a'Ù±‚bs2b/>Ù±‚bs2a
Ù±‚bs2s      <feOffset in=Ù±‚bs2a'Ù±‚bs2dblurÙ±‚bs2a'Ù±‚bs2d dx=Ù±‚bs2a'Ù±‚bs2a4Ù±‚bs2a%Ù±‚bs2a'Ù±‚bs2d dy=Ù±‚bs2a'Ù±‚bs2a4Ù±‚bs2a%Ù±‚bs2a'Ù±‚bs2h result=Ù±‚bs2a'Ù±‚bs2joffsetBlurÙ±‚bs2a'Ù±‚bs2b/>Ù±‚bs2a
Ù±‚bs2x      <feSpecularLighting in=Ù±‚bs2a'Ù±‚bs2dblurÙ±‚bs2a'Ù±‚bs2n surfaceScale=Ù±‚bs2a'Ù±‚bs2a5Ù±‚bs2a'Ù±‚bs2r specularConstant=Ù±‚bs2a'Ù±‚bs2c.75Ù±‚bs2a'Ù±‚bs2a
Ù±‚bs2x           specularExponent=Ù±‚bs2a'Ù±‚bs2b20Ù±‚bs2a'Ù±‚bs2p lighting-color=Ù±‚bs2a'Ù±‚bs2g#bbbbbbÙ±‚bs2a'Ù±‚bs2h result=Ù±‚bs2a'Ù±‚bs2gspecOutÙ±‚bs2a'Ù±‚bs2a>Ù±‚bs2a
Ù±‚bs2x        <fePointLight x=Ù±‚bs2a'Ù±‚bs2e-5000Ù±‚bs2a%Ù±‚bs2a'Ù±‚bs2c y=Ù±‚bs2a'Ù±‚bs2f-10000Ù±‚bs2a%Ù±‚bs2a'Ù±‚bs2c z=Ù±‚bs2a'Ù±‚bs2e20000Ù±‚bs2a%Ù±‚bs2a'Ù±‚bs2b/>Ù±‚bs2a
Ù±‚bs2x      </feSpecularLighting>Ù±‚bs2a
Ù±‚bs2v      <feComposite in=Ù±‚bs2a'Ù±‚bs2gspecOutÙ±‚bs2a'Ù±‚bs2e in2=Ù±‚bs2a'Ù±‚bs2kSourceAlphaÙ±‚bs2a'Ù±‚bs2a
Ù±‚bs2x                   operator=Ù±‚bs2a'Ù±‚bs2binÙ±‚bs2a'Ù±‚bs2h result=Ù±‚bs2a'Ù±‚bs2gspecOutÙ±‚bs2a'Ù±‚bs2b/>Ù±‚bs2a
Ù±‚bs2v      <feComposite in=Ù±‚bs2a'Ù±‚bs2mSourceGraphicÙ±‚bs2a'Ù±‚bs2e in2=Ù±‚bs2a'Ù±‚bs2gspecOutÙ±‚bs2a'Ù±‚bs2j operator=Ù±‚bs2a'Ù±‚bs2jarithmeticÙ±‚bs2a'Ù±‚bs2a
Ù±‚bs2g    k1=Ù±‚bs2a'Ù±‚bs2a0Ù±‚bs2a'Ù±‚bs2d k2=Ù±‚bs2a'Ù±‚bs2a1Ù±‚bs2a'Ù±‚bs2d k3=Ù±‚bs2a'Ù±‚bs2a1Ù±‚bs2a'Ù±‚bs2d k4=Ù±‚bs2a'Ù±‚bs2a0Ù±‚bs2a'Ù±‚bs2b/>Ù±‚bs2a
Ù±‚bs2m    </filter>Ù±‚bs2a
Ù±‚bs2i  </defs>Ù±‚bs2a
Ù±‚bs2c"""Ù±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚`dtreeÙ±‚`a,Ù±‚`a Ù±‚`exmlidÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bETÙ±‚aoa.Ù±‚`eXMLIDÙ±‚`a(Ù±‚`afÙ±‚aoa.Ù±‚`hgetvalueÙ±‚`a(Ù±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚bc1x3# insert the filter definition in the svg dom tree.Ù±‚`a
Ù±‚`dtreeÙ±‚aoa.Ù±‚`finsertÙ±‚`a(Ù±‚bmia0Ù±‚`a,Ù±‚`a Ù±‚`bETÙ±‚aoa.Ù±‚`cXMLÙ±‚`a(Ù±‚`jfilter_defÙ±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚akcforÙ±‚`a Ù±‚`aiÙ±‚`a,Ù±‚`a Ù±‚`hpie_nameÙ±‚`a Ù±‚bowbinÙ±‚`a Ù±‚bnbienumerateÙ±‚`a(Ù±‚`flabelsÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`d    Ù±‚`cpieÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`exmlidÙ±‚`a[Ù±‚`hpie_nameÙ±‚`a]Ù±‚`a
Ù±‚`d    Ù±‚`cpieÙ±‚aoa.Ù±‚`csetÙ±‚`a(Ù±‚bs2a"Ù±‚bs2ffilterÙ±‚bs2a"Ù±‚`a,Ù±‚`a Ù±‚bs1a'Ù±‚bs1nurl(#MyFilter)Ù±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚`fshadowÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`exmlidÙ±‚`a[Ù±‚`hpie_nameÙ±‚`a Ù±‚aoa+Ù±‚`a Ù±‚bs2a"Ù±‚bs2g_shadowÙ±‚bs2a"Ù±‚`a]Ù±‚`a
Ù±‚`d    Ù±‚`fshadowÙ±‚aoa.Ù±‚`csetÙ±‚`a(Ù±‚bs2a"Ù±‚bs2ffilterÙ±‚bs2a"Ù±‚`a,Ù±‚`a Ù±‚bs1a'Ù±‚bs1purl(#dropshadow)Ù±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`bfnÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bs2a"Ù±‚bs2rsvg_filter_pie.svgÙ±‚bs2a"Ù±‚`a
Ù±‚bnbeprintÙ±‚`a(Ù±‚bsaafÙ±‚bs2a"Ù±‚bs2gSaving Ù±‚bs2a'Ù±‚bsia{Ù±‚`bfnÙ±‚bsia}Ù±‚bs2a'Ù±‚bs2a"Ù±‚`a)Ù±‚`a
Ù±‚`bETÙ±‚aoa.Ù±‚`kElementTreeÙ±‚`a(Ù±‚`dtreeÙ±‚`a)Ù±‚aoa.Ù±‚`ewriteÙ±‚`a(Ù±‚`bfnÙ±‚`a)Ù±‚`a
`dNoneö