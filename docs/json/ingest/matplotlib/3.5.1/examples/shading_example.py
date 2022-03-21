ŸØÇÅŸ¥ÉôPŸ±Çbsdy"""
===============
Shading example
===============

Example showing how to make shaded relief plots like Mathematica_ or
`Generic Mapping Tools`_.

.. _Mathematica: http://reference.wolfram.com/mathematica/ref/ReliefPlot.html
.. _Generic Mapping Tools: https://gmt.soest.hawaii.edu/
"""Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±ÇbknfimportŸ±Ç`a Ÿ±ÇbnnŸ¢ÑenumpyŸ†Ñenumpyf1.22.3fmoduleenumpyfmoduleıŸ±Ç`a Ÿ±ÇakbasŸ±Ç`a Ÿ±ÇbnnbnpŸ±Ç`a
Ÿ±ÇbkndfromŸ±Ç`a Ÿ±ÇbnnŸ¢ÑjmatplotlibŸ†Ñjmatplotlibe3.5.1fmodulejmatplotlibfmoduleıŸ±Ç`a Ÿ±ÇbknfimportŸ±Ç`a Ÿ±Ç`ecbookŸ±Ç`a
Ÿ±ÇbknfimportŸ±Ç`a Ÿ±ÇbnnŸ¢ÑjmatplotlibŸ†Ñjmatplotlibe3.5.1fmodulejmatplotlibfmoduleıŸ±Çbnna.Ÿ±ÇbnnfpyplotŸ±Ç`a Ÿ±ÇakbasŸ±Ç`a Ÿ±ÇbnncpltŸ±Ç`a
Ÿ±ÇbkndfromŸ±Ç`a Ÿ±ÇbnnŸ¢ÑjmatplotlibŸ†Ñjmatplotlibe3.5.1fmodulejmatplotlibfmoduleıŸ±Çbnna.Ÿ±ÇbnnfcolorsŸ±Ç`a Ÿ±ÇbknfimportŸ±Ç`a Ÿ±Ç`kLightSourceŸ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±ÇakcdefŸ±Ç`a Ÿ±ÇbnfdmainŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Çbc1k# Test dataŸ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`axŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ayŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`emgridŸ±Ç`a[Ÿ±Çaoa-Ÿ±Çbmia5Ÿ±Ç`a:Ÿ±Çbmia5Ÿ±Ç`a:Ÿ±Çbmfd0.05Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çaoa-Ÿ±Çbmia5Ÿ±Ç`a:Ÿ±Çbmia5Ÿ±Ç`a:Ÿ±Çbmfd0.05Ÿ±Ç`a]Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`azŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Çbmia5Ÿ±Ç`a Ÿ±Çaoa*Ÿ±Ç`a Ÿ±Ç`a(Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`dsqrtŸ±Ç`a(Ÿ±Ç`axŸ±Çaoa*Ÿ±Çaoa*Ÿ±Çbmia2Ÿ±Ç`a Ÿ±Çaoa+Ÿ±Ç`a Ÿ±Ç`ayŸ±Çaoa*Ÿ±Çaoa*Ÿ±Çbmia2Ÿ±Ç`a)Ÿ±Ç`a Ÿ±Çaoa+Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`csinŸ±Ç`a(Ÿ±Ç`axŸ±Çaoa*Ÿ±Çaoa*Ÿ±Çbmia2Ÿ±Ç`a Ÿ±Çaoa+Ÿ±Ç`a Ÿ±Ç`ayŸ±Çaoa*Ÿ±Çaoa*Ÿ±Çbmia2Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`cdemŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`ecbookŸ±Çaoa.Ÿ±Ç`oget_sample_dataŸ±Ç`a(Ÿ±Çbs1a'Ÿ±Çbs1wjacksboro_fault_dem.npzŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`gnp_loadŸ±Çaoa=Ÿ±ÇbkcdTrueŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`delevŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cdemŸ±Ç`a[Ÿ±Çbs1a'Ÿ±Çbs1ielevationŸ±Çbs1a'Ÿ±Ç`a]Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`cfigŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`gcompareŸ±Ç`a(Ÿ±Ç`azŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`bcmŸ±Çaoa.Ÿ±Ç`fcopperŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`cfigŸ±Çaoa.Ÿ±Ç`hsuptitleŸ±Ç`a(Ÿ±Çbs1a'Ÿ±Çbs1x,HSV Blending Looks Best with Smooth SurfacesŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ayŸ±Çaoa=Ÿ±Çbmfd0.95Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`cfigŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`gcompareŸ±Ç`a(Ÿ±Ç`delevŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`bcmŸ±Çaoa.Ÿ±Ç`jgist_earthŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`bveŸ±Çaoa=Ÿ±Çbmfd0.05Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`cfigŸ±Çaoa.Ÿ±Ç`hsuptitleŸ±Ç`a(Ÿ±Çbs1a'Ÿ±Çbs1x/Overlay Blending Looks Best with Rough SurfacesŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ayŸ±Çaoa=Ÿ±Çbmfd0.95Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`dshowŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±ÇakcdefŸ±Ç`a Ÿ±ÇbnfgcompareŸ±Ç`a(Ÿ±Ç`azŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dcmapŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`bveŸ±Çaoa=Ÿ±Çbmia1Ÿ±Ç`a)Ÿ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Çbc1x # Create subplots and hide ticksŸ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`cfigŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`caxsŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`hsubplotsŸ±Ç`a(Ÿ±Ç`encolsŸ±Çaoa=Ÿ±Çbmia2Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`enrowsŸ±Çaoa=Ÿ±Çbmia2Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±ÇakcforŸ±Ç`a Ÿ±Ç`baxŸ±Ç`a Ÿ±ÇbowbinŸ±Ç`a Ÿ±Ç`caxsŸ±Çaoa.Ÿ±Ç`dflatŸ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`csetŸ±Ç`a(Ÿ±Ç`fxticksŸ±Çaoa=Ÿ±Ç`a[Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`fyticksŸ±Çaoa=Ÿ±Ç`a[Ÿ±Ç`a]Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Çbc1x)# Illuminate the scene from the northwestŸ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`blsŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`kLightSourceŸ±Ç`a(Ÿ±Ç`eazdegŸ±Çaoa=Ÿ±Çbmic315Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`faltdegŸ±Çaoa=Ÿ±Çbmib45Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`caxsŸ±Ç`a[Ÿ±Çbmia0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia0Ÿ±Ç`a]Ÿ±Çaoa.Ÿ±Ç`fimshowŸ±Ç`a(Ÿ±Ç`azŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dcmapŸ±Çaoa=Ÿ±Ç`dcmapŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`caxsŸ±Ç`a[Ÿ±Çbmia0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia0Ÿ±Ç`a]Ÿ±Çaoa.Ÿ±Ç`csetŸ±Ç`a(Ÿ±Ç`fxlabelŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1pColormapped DataŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`caxsŸ±Ç`a[Ÿ±Çbmia0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia1Ÿ±Ç`a]Ÿ±Çaoa.Ÿ±Ç`fimshowŸ±Ç`a(Ÿ±Ç`blsŸ±Çaoa.Ÿ±Ç`ihillshadeŸ±Ç`a(Ÿ±Ç`azŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ivert_exagŸ±Çaoa=Ÿ±Ç`bveŸ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dcmapŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1dgrayŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`caxsŸ±Ç`a[Ÿ±Çbmia0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia1Ÿ±Ç`a]Ÿ±Çaoa.Ÿ±Ç`csetŸ±Ç`a(Ÿ±Ç`fxlabelŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1vIllumination IntensityŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`crgbŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`blsŸ±Çaoa.Ÿ±Ç`eshadeŸ±Ç`a(Ÿ±Ç`azŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dcmapŸ±Çaoa=Ÿ±Ç`dcmapŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ivert_exagŸ±Çaoa=Ÿ±Ç`bveŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`jblend_modeŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1chsvŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`caxsŸ±Ç`a[Ÿ±Çbmia1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia0Ÿ±Ç`a]Ÿ±Çaoa.Ÿ±Ç`fimshowŸ±Ç`a(Ÿ±Ç`crgbŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`caxsŸ±Ç`a[Ÿ±Çbmia1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia0Ÿ±Ç`a]Ÿ±Çaoa.Ÿ±Ç`csetŸ±Ç`a(Ÿ±Ç`fxlabelŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1lBlend Mode: Ÿ±Çbs1a"Ÿ±Çbs1chsvŸ±Çbs1a"Ÿ±Çbs1j (default)Ÿ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`crgbŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`blsŸ±Çaoa.Ÿ±Ç`eshadeŸ±Ç`a(Ÿ±Ç`azŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dcmapŸ±Çaoa=Ÿ±Ç`dcmapŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ivert_exagŸ±Çaoa=Ÿ±Ç`bveŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`jblend_modeŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1goverlayŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`caxsŸ±Ç`a[Ÿ±Çbmia1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia1Ÿ±Ç`a]Ÿ±Çaoa.Ÿ±Ç`fimshowŸ±Ç`a(Ÿ±Ç`crgbŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`caxsŸ±Ç`a[Ÿ±Çbmia1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia1Ÿ±Ç`a]Ÿ±Çaoa.Ÿ±Ç`csetŸ±Ç`a(Ÿ±Ç`fxlabelŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1lBlend Mode: Ÿ±Çbs1a"Ÿ±Çbs1goverlayŸ±Çbs1a"Ÿ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±ÇakfreturnŸ±Ç`a Ÿ±Ç`cfigŸ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±ÇakbifŸ±Ç`a Ÿ±Çbvmh__name__Ÿ±Ç`a Ÿ±Çaob==Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1h__main__Ÿ±Çbs1a'Ÿ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`dmainŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1xM#############################################################################Ÿ±Ç`a
Ÿ±Çbc1a#Ÿ±Ç`a
Ÿ±Çbc1x# .. admonition:: ReferencesŸ±Ç`a
Ÿ±Çbc1a#Ÿ±Ç`a
Ÿ±Çbc1xN#    The use of the following functions, methods, classes and modules is shownŸ±Ç`a
Ÿ±Çbc1u#    in this example:Ÿ±Ç`a
Ÿ±Çbc1a#Ÿ±Ç`a
Ÿ±Çbc1x&#    - `matplotlib.colors.LightSource`Ÿ±Ç`a
Ÿ±Çbc1xA#    - `matplotlib.axes.Axes.imshow` / `matplotlib.pyplot.imshow`Ÿ±Ç`a
`dNoneˆ