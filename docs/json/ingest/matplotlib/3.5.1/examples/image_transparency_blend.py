ŸØÇÅŸ¥ÉôŸ±ÇbsdyÀ"""
==========================================
Blend transparency with color in 2D images
==========================================

Blend transparency with color to highlight parts of data with imshow.

A common use for `matplotlib.pyplot.imshow` is to plot a 2D statistical
map. The function makes it easy to visualize a 2D matrix as an image and add
transparency to the output. For example, one can plot a statistic (such as a
t-statistic) and color the transparency of each pixel according to its p-value.
This example demonstrates how you can achieve this effect.

First we will generate some data, in this case, we'll create two 2D "blobs"
in a 2D grid. One blob will be positive, and the other negative.
"""Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1x%# sphinx_gallery_thumbnail_number = 3Ÿ±Ç`a
Ÿ±ÇbknfimportŸ±Ç`a Ÿ±ÇbnnŸ¢ÑenumpyŸ†Ñenumpyf1.22.3fmoduleenumpyfmoduleıŸ±Ç`a Ÿ±ÇakbasŸ±Ç`a Ÿ±ÇbnnbnpŸ±Ç`a
Ÿ±ÇbknfimportŸ±Ç`a Ÿ±ÇbnnŸ¢ÑjmatplotlibŸ†Ñjmatplotlibe3.5.1fmodulejmatplotlibfmoduleıŸ±Çbnna.Ÿ±ÇbnnfpyplotŸ±Ç`a Ÿ±ÇakbasŸ±Ç`a Ÿ±ÇbnncpltŸ±Ç`a
Ÿ±ÇbkndfromŸ±Ç`a Ÿ±ÇbnnŸ¢ÑjmatplotlibŸ†Ñjmatplotlibe3.5.1fmodulejmatplotlibfmoduleıŸ±Çbnna.Ÿ±ÇbnnfcolorsŸ±Ç`a Ÿ±ÇbknfimportŸ±Ç`a Ÿ±Ç`iNormalizeŸ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±ÇakcdefŸ±Ç`a Ÿ±Çbnfjnormal_pdfŸ±Ç`a(Ÿ±Ç`axŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dmeanŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`cvarŸ±Ç`a)Ÿ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±ÇakfreturnŸ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`cexpŸ±Ç`a(Ÿ±Çaoa-Ÿ±Ç`a(Ÿ±Ç`axŸ±Ç`a Ÿ±Çaoa-Ÿ±Ç`a Ÿ±Ç`dmeanŸ±Ç`a)Ÿ±Çaoa*Ÿ±Çaoa*Ÿ±Çbmia2Ÿ±Ç`a Ÿ±Çaoa/Ÿ±Ç`a Ÿ±Ç`a(Ÿ±Çbmia2Ÿ±Çaoa*Ÿ±Ç`cvarŸ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1x1# Generate the space in which the blobs will liveŸ±Ç`a
Ÿ±Ç`dxminŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dxmaxŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dyminŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dymaxŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`a(Ÿ±Çbmia0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmic100Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmic100Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`fn_binsŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Çbmic100Ÿ±Ç`a
Ÿ±Ç`bxxŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`hlinspaceŸ±Ç`a(Ÿ±Ç`dxminŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dxmaxŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`fn_binsŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`byyŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`hlinspaceŸ±Ç`a(Ÿ±Ç`dyminŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dymaxŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`fn_binsŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1xH# Generate the blobs. The range of the values is roughly -.0002 to .0002Ÿ±Ç`a
Ÿ±Ç`jmeans_highŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`a[Ÿ±Çbmib20Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmib50Ÿ±Ç`a]Ÿ±Ç`a
Ÿ±Ç`imeans_lowŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`a[Ÿ±Çbmib50Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmib60Ÿ±Ç`a]Ÿ±Ç`a
Ÿ±Ç`cvarŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`a[Ÿ±Çbmic150Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmic200Ÿ±Ç`a]Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`lgauss_x_highŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`jnormal_pdfŸ±Ç`a(Ÿ±Ç`bxxŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`jmeans_highŸ±Ç`a[Ÿ±Çbmia0Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`cvarŸ±Ç`a[Ÿ±Çbmia0Ÿ±Ç`a]Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`lgauss_y_highŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`jnormal_pdfŸ±Ç`a(Ÿ±Ç`byyŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`jmeans_highŸ±Ç`a[Ÿ±Çbmia1Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`cvarŸ±Ç`a[Ÿ±Çbmia0Ÿ±Ç`a]Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`kgauss_x_lowŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`jnormal_pdfŸ±Ç`a(Ÿ±Ç`bxxŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`imeans_lowŸ±Ç`a[Ÿ±Çbmia0Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`cvarŸ±Ç`a[Ÿ±Çbmia1Ÿ±Ç`a]Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`kgauss_y_lowŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`jnormal_pdfŸ±Ç`a(Ÿ±Ç`byyŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`imeans_lowŸ±Ç`a[Ÿ±Çbmia1Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`cvarŸ±Ç`a[Ÿ±Çbmia1Ÿ±Ç`a]Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`gweightsŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`a(Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`eouterŸ±Ç`a(Ÿ±Ç`lgauss_y_highŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`lgauss_x_highŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`k           Ÿ±Çaoa-Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`eouterŸ±Ç`a(Ÿ±Ç`kgauss_y_lowŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`kgauss_x_lowŸ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1xE# We'll also create a grey background into which the pixels will fadeŸ±Ç`a
Ÿ±Ç`egreysŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`dfullŸ±Ç`a(Ÿ±Ç`a(Ÿ±Çaoa*Ÿ±Ç`gweightsŸ±Çaoa.Ÿ±Ç`eshapeŸ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia3Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmib70Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`edtypeŸ±Çaoa=Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`euint8Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1xE# First we'll plot these blobs using ``imshow`` without transparency.Ÿ±Ç`a
Ÿ±Ç`dvmaxŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`cabsŸ±Ç`a(Ÿ±Ç`gweightsŸ±Ç`a)Ÿ±Çaoa.Ÿ±Ç`cmaxŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`mimshow_kwargsŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`a{Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Çbs1a'Ÿ±Çbs1dvmaxŸ±Çbs1a'Ÿ±Ç`a:Ÿ±Ç`a Ÿ±Ç`dvmaxŸ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Çbs1a'Ÿ±Çbs1dvminŸ±Çbs1a'Ÿ±Ç`a:Ÿ±Ç`a Ÿ±Çaoa-Ÿ±Ç`dvmaxŸ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Çbs1a'Ÿ±Çbs1dcmapŸ±Çbs1a'Ÿ±Ç`a:Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1fRdYlBuŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Çbs1a'Ÿ±Çbs1fextentŸ±Çbs1a'Ÿ±Ç`a:Ÿ±Ç`a Ÿ±Ç`a(Ÿ±Ç`dxminŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dxmaxŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dyminŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dymaxŸ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`a}Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`cfigŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`baxŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`hsubplotsŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`fimshowŸ±Ç`a(Ÿ±Ç`egreysŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`fimshowŸ±Ç`a(Ÿ±Ç`gweightsŸ±Ç`a,Ÿ±Ç`a Ÿ±Çaoa*Ÿ±Çaoa*Ÿ±Ç`mimshow_kwargsŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`lset_axis_offŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1xO###############################################################################Ÿ±Ç`a
Ÿ±Çbc1x# Blending in transparencyŸ±Ç`a
Ÿ±Çbc1x# ========================Ÿ±Ç`a
Ÿ±Çbc1a#Ÿ±Ç`a
Ÿ±Çbc1xB# The simplest way to include transparency when plotting data withŸ±Ç`a
Ÿ±Çbc1xF# `matplotlib.pyplot.imshow` is to pass an array matching the shape ofŸ±Ç`a
Ÿ±Çbc1xJ# the data to the ``alpha`` argument. For example, we'll create a gradientŸ±Ç`a
Ÿ±Çbc1x"# moving from left to right below.Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1xL# Create an alpha channel of linearly increasing values moving to the right.Ÿ±Ç`a
Ÿ±Ç`falphasŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`donesŸ±Ç`a(Ÿ±Ç`gweightsŸ±Çaoa.Ÿ±Ç`eshapeŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`falphasŸ±Ç`a[Ÿ±Ç`a:Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmib30Ÿ±Ç`a:Ÿ±Ç`a]Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`hlinspaceŸ±Ç`a(Ÿ±Çbmia1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmib70Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1x# Create the figure and imageŸ±Ç`a
Ÿ±Çbc1x9# Note that the absolute values may be slightly differentŸ±Ç`a
Ÿ±Ç`cfigŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`baxŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`hsubplotsŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`fimshowŸ±Ç`a(Ÿ±Ç`egreysŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`fimshowŸ±Ç`a(Ÿ±Ç`gweightsŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ealphaŸ±Çaoa=Ÿ±Ç`falphasŸ±Ç`a,Ÿ±Ç`a Ÿ±Çaoa*Ÿ±Çaoa*Ÿ±Ç`mimshow_kwargsŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`lset_axis_offŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1xO###############################################################################Ÿ±Ç`a
Ÿ±Çbc1x<# Using transparency to highlight values with high amplitudeŸ±Ç`a
Ÿ±Çbc1x<# ==========================================================Ÿ±Ç`a
Ÿ±Çbc1a#Ÿ±Ç`a
Ÿ±Çbc1xM# Finally, we'll recreate the same plot, but this time we'll use transparencyŸ±Ç`a
Ÿ±Çbc1xN# to highlight the extreme values in the data. This is often used to highlightŸ±Ç`a
Ÿ±Çbc1xG# data points with smaller p-values. We'll also add in contour lines toŸ±Ç`a
Ÿ±Çbc1x# highlight the image values.Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1x0# Create an alpha channel based on weight valuesŸ±Ç`a
Ÿ±Çbc1xG# Any value whose absolute value is > .0001 will have zero transparencyŸ±Ç`a
Ÿ±Ç`falphasŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`iNormalizeŸ±Ç`a(Ÿ±Çbmia0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfb.3Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dclipŸ±Çaoa=Ÿ±ÇbkcdTrueŸ±Ç`a)Ÿ±Ç`a(Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`cabsŸ±Ç`a(Ÿ±Ç`gweightsŸ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`falphasŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`dclipŸ±Ç`a(Ÿ±Ç`falphasŸ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfb.4Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia1Ÿ±Ç`a)Ÿ±Ç`b  Ÿ±Çbc1x)# alpha value clipped at the bottom at .4Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1x# Create the figure and imageŸ±Ç`a
Ÿ±Çbc1x9# Note that the absolute values may be slightly differentŸ±Ç`a
Ÿ±Ç`cfigŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`baxŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`hsubplotsŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`fimshowŸ±Ç`a(Ÿ±Ç`egreysŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`fimshowŸ±Ç`a(Ÿ±Ç`gweightsŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ealphaŸ±Çaoa=Ÿ±Ç`falphasŸ±Ç`a,Ÿ±Ç`a Ÿ±Çaoa*Ÿ±Çaoa*Ÿ±Ç`mimshow_kwargsŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1x:# Add contour lines to further highlight different levels.Ÿ±Ç`a
Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`gcontourŸ±Ç`a(Ÿ±Ç`gweightsŸ±Ç`a[Ÿ±Ç`a:Ÿ±Ç`a:Ÿ±Çaoa-Ÿ±Çbmia1Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`flevelsŸ±Çaoa=Ÿ±Ç`a[Ÿ±Çaoa-Ÿ±Çbmfb.1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfb.1Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`fcolorsŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1akŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`jlinestylesŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1a-Ÿ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`lset_axis_offŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`dshowŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`gcontourŸ±Ç`a(Ÿ±Ç`gweightsŸ±Ç`a[Ÿ±Ç`a:Ÿ±Ç`a:Ÿ±Çaoa-Ÿ±Çbmia1Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`flevelsŸ±Çaoa=Ÿ±Ç`a[Ÿ±Çaoa-Ÿ±Çbmfe.0001Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfe.0001Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`fcolorsŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1akŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`jlinestylesŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1a-Ÿ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`lset_axis_offŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`dshowŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1xM#############################################################################Ÿ±Ç`a
Ÿ±Çbc1a#Ÿ±Ç`a
Ÿ±Çbc1x# .. admonition:: ReferencesŸ±Ç`a
Ÿ±Çbc1a#Ÿ±Ç`a
Ÿ±Çbc1xN#    The use of the following functions, methods, classes and modules is shownŸ±Ç`a
Ÿ±Çbc1u#    in this example:Ÿ±Ç`a
Ÿ±Çbc1a#Ÿ±Ç`a
Ÿ±Çbc1xA#    - `matplotlib.axes.Axes.imshow` / `matplotlib.pyplot.imshow`Ÿ±Ç`a
Ÿ±Çbc1xC#    - `matplotlib.axes.Axes.contour` / `matplotlib.pyplot.contour`Ÿ±Ç`a
Ÿ±Çbc1x$#    - `matplotlib.colors.Normalize`Ÿ±Ç`a
Ÿ±Çbc1x*#    - `matplotlib.axes.Axes.set_axis_off`Ÿ±Ç`a
`dNoneˆ