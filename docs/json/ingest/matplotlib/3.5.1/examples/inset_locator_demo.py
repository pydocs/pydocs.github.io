ŸØÇÅŸ¥ÉôPŸ±ÇbsdxA"""
==================
Inset Locator Demo
==================

"""Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1xO###############################################################################Ÿ±Ç`a
Ÿ±Çbc1x<# The `.inset_locator`'s `~.inset_locator.inset_axes` allowsŸ±Ç`a
Ÿ±Çbc1xL# easily placing insets in the corners of the axes by specifying a width andŸ±Ç`a
Ÿ±Çbc1xI# height and optionally a location (loc) that accepts locations as codes,Ÿ±Ç`a
Ÿ±Çbc1x,# similar to `~matplotlib.axes.Axes.legend`.Ÿ±Ç`a
Ÿ±Çbc1x?# By default, the inset is offset by some points from the axes,Ÿ±Ç`a
Ÿ±Çbc1x+# controlled via the *borderpad* parameter.Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±ÇbknfimportŸ±Ç`a Ÿ±ÇbnnŸ¢ÑjmatplotlibŸ†Ñjmatplotlibe3.5.1fmodulejmatplotlibfmoduleıŸ±Çbnna.Ÿ±ÇbnnfpyplotŸ±Ç`a Ÿ±ÇakbasŸ±Ç`a Ÿ±ÇbnncpltŸ±Ç`a
Ÿ±ÇbkndfromŸ±Ç`a Ÿ±Çbnnlmpl_toolkitsŸ±Çbnna.Ÿ±Çbnnjaxes_grid1Ÿ±Çbnna.Ÿ±Çbnnminset_locatorŸ±Ç`a Ÿ±ÇbknfimportŸ±Ç`a Ÿ±Ç`jinset_axesŸ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`cfigŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`a(Ÿ±Ç`baxŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`cax2Ÿ±Ç`a)Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`hsubplotsŸ±Ç`a(Ÿ±Çbmia1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia2Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`gfigsizeŸ±Çaoa=Ÿ±Ç`a[Ÿ±Çbmfc5.5Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfc2.8Ÿ±Ç`a]Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1x8# Create inset of width 1.3 inches and height 0.9 inchesŸ±Ç`a
Ÿ±Çbc1x%# at the default upper right locationŸ±Ç`a
Ÿ±Ç`eaxinsŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`jinset_axesŸ±Ç`a(Ÿ±Ç`baxŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ewidthŸ±Çaoa=Ÿ±Çbmfc1.3Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`fheightŸ±Çaoa=Ÿ±Çbmfc0.9Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1xK# Create inset of width 30% and height 40% of the parent axes' bounding boxŸ±Ç`a
Ÿ±Çbc1x"# at the lower left corner (loc=3)Ÿ±Ç`a
Ÿ±Ç`faxins2Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`jinset_axesŸ±Ç`a(Ÿ±Ç`baxŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ewidthŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2b30Ÿ±Çbs2a%Ÿ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`fheightŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2b40Ÿ±Çbs2a%Ÿ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`clocŸ±Çaoa=Ÿ±Çbmia3Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1x=# Create inset of mixed specifications in the second subplot;Ÿ±Ç`a
Ÿ±Çbc1x/# width is 30% of parent axes' bounding box andŸ±Ç`a
Ÿ±Çbc1x3# height is 1 inch at the upper left corner (loc=2)Ÿ±Ç`a
Ÿ±Ç`faxins3Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`jinset_axesŸ±Ç`a(Ÿ±Ç`cax2Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ewidthŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2b30Ÿ±Çbs2a%Ÿ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`fheightŸ±Çaoa=Ÿ±Çbmfb1.Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`clocŸ±Çaoa=Ÿ±Çbmia2Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1xJ# Create an inset in the lower right corner (loc=4) with borderpad=1, i.e.Ÿ±Ç`a
Ÿ±Çbc1xH# 10 points padding (as 10pt is the default fontsize) to the parent axesŸ±Ç`a
Ÿ±Ç`faxins4Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`jinset_axesŸ±Ç`a(Ÿ±Ç`cax2Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ewidthŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2b20Ÿ±Çbs2a%Ÿ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`fheightŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2b20Ÿ±Çbs2a%Ÿ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`clocŸ±Çaoa=Ÿ±Çbmia4Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`iborderpadŸ±Çaoa=Ÿ±Çbmia1Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1x# Turn ticklabels of insets offŸ±Ç`a
Ÿ±ÇakcforŸ±Ç`a Ÿ±Ç`caxiŸ±Ç`a Ÿ±ÇbowbinŸ±Ç`a Ÿ±Ç`a[Ÿ±Ç`eaxinsŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`faxins2Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`faxins3Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`faxins4Ÿ±Ç`a]Ÿ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`caxiŸ±Çaoa.Ÿ±Ç`ktick_paramsŸ±Ç`a(Ÿ±Ç`ilabelleftŸ±Çaoa=Ÿ±ÇbkceFalseŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`klabelbottomŸ±Çaoa=Ÿ±ÇbkceFalseŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`dshowŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1xO###############################################################################Ÿ±Ç`a
Ÿ±Çbc1xM# The parameters *bbox_to_anchor* and *bbox_transform* can be used for a moreŸ±Ç`a
Ÿ±Çbc1xK# fine grained control over the inset position and size or even to positionŸ±Ç`a
Ÿ±Çbc1x.# the inset at completely arbitrary positions.Ÿ±Ç`a
Ÿ±Çbc1xL# The *bbox_to_anchor* sets the bounding box in coordinates according to theŸ±Ç`a
Ÿ±Çbc1s# *bbox_transform*.Ÿ±Ç`a
Ÿ±Çbc1a#Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`cfigŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`ffigureŸ±Ç`a(Ÿ±Ç`gfigsizeŸ±Çaoa=Ÿ±Ç`a[Ÿ±Çbmfc5.5Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfc2.8Ÿ±Ç`a]Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`baxŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cfigŸ±Çaoa.Ÿ±Ç`kadd_subplotŸ±Ç`a(Ÿ±Çbmic121Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1xI# We use the axes transform as bbox_transform. Therefore the bounding boxŸ±Ç`a
Ÿ±Çbc1xL# needs to be specified in axes coordinates ((0, 0) is the lower left cornerŸ±Ç`a
Ÿ±Çbc1x1# of the axes, (1, 1) is the upper right corner).Ÿ±Ç`a
Ÿ±Çbc1xM# The bounding box (.2, .4, .6, .5) starts at (.2, .4) and ranges to (.8, .9)Ÿ±Ç`a
Ÿ±Çbc1w# in those coordinates.Ÿ±Ç`a
Ÿ±Çbc1xJ# Inside of this bounding box an inset of half the bounding box' width andŸ±Ç`a
Ÿ±Çbc1xN# three quarters of the bounding box' height is created. The lower left cornerŸ±Ç`a
Ÿ±Çbc1xO# of the inset is aligned to the lower left corner of the bounding box (loc=3).Ÿ±Ç`a
Ÿ±Çbc1xH# The inset is then offset by the default 0.5 in units of the font size.Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`eaxinsŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`jinset_axesŸ±Ç`a(Ÿ±Ç`baxŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ewidthŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2b50Ÿ±Çbs2a%Ÿ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`fheightŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2b75Ÿ±Çbs2a%Ÿ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`s                   Ÿ±Ç`nbbox_to_anchorŸ±Çaoa=Ÿ±Ç`a(Ÿ±Çbmfb.2Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfb.4Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfb.6Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfb.5Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`s                   Ÿ±Ç`nbbox_transformŸ±Çaoa=Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`itransAxesŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`clocŸ±Çaoa=Ÿ±Çbmia3Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1xD# For visualization purposes we mark the bounding box by a rectangleŸ±Ç`a
Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`iadd_patchŸ±Ç`a(Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`iRectangleŸ±Ç`a(Ÿ±Ç`a(Ÿ±Çbmfb.2Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfb.4Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfb.6Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfb.5Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`blsŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2b--Ÿ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`becŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2acŸ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`bfcŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2dnoneŸ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`x                           Ÿ±Ç`itransformŸ±Çaoa=Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`itransAxesŸ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1xM# We set the axis limits to something other than the default, in order to notŸ±Ç`a
Ÿ±Çbc1x=# distract from the fact that axes coordinates are used here.Ÿ±Ç`a
Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`csetŸ±Ç`a(Ÿ±Ç`dxlimŸ±Çaoa=Ÿ±Ç`a(Ÿ±Çbmia0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmib10Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dylimŸ±Çaoa=Ÿ±Ç`a(Ÿ±Çbmia0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmib10Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1xM# Note how the two following insets are created at the same positions, one byŸ±Ç`a
Ÿ±Çbc1xG# use of the default parent axes' bbox and the other via a bbox in axesŸ±Ç`a
Ÿ±Çbc1x+# coordinates and the respective transform.Ÿ±Ç`a
Ÿ±Ç`cax2Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cfigŸ±Çaoa.Ÿ±Ç`kadd_subplotŸ±Ç`a(Ÿ±Çbmic222Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`faxins2Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`jinset_axesŸ±Ç`a(Ÿ±Ç`cax2Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ewidthŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2b30Ÿ±Çbs2a%Ÿ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`fheightŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2b50Ÿ±Çbs2a%Ÿ±Çbs2a"Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`cax3Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cfigŸ±Çaoa.Ÿ±Ç`kadd_subplotŸ±Ç`a(Ÿ±Çbmic224Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`faxins3Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`jinset_axesŸ±Ç`a(Ÿ±Ç`cax3Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ewidthŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2c100Ÿ±Çbs2a%Ÿ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`fheightŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2c100Ÿ±Çbs2a%Ÿ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`t                    Ÿ±Ç`nbbox_to_anchorŸ±Çaoa=Ÿ±Ç`a(Ÿ±Çbmfb.7Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfb.5Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfb.3Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfb.5Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`t                    Ÿ±Ç`nbbox_transformŸ±Çaoa=Ÿ±Ç`cax3Ÿ±Çaoa.Ÿ±Ç`itransAxesŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1xD# For visualization purposes we mark the bounding box by a rectangleŸ±Ç`a
Ÿ±Ç`cax2Ÿ±Çaoa.Ÿ±Ç`iadd_patchŸ±Ç`a(Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`iRectangleŸ±Ç`a(Ÿ±Ç`a(Ÿ±Çbmia0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia0Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`blsŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2b--Ÿ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`blwŸ±Çaoa=Ÿ±Çbmia2Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`becŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2acŸ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`bfcŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2dnoneŸ±Çbs2a"Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cax3Ÿ±Çaoa.Ÿ±Ç`iadd_patchŸ±Ç`a(Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`iRectangleŸ±Ç`a(Ÿ±Ç`a(Ÿ±Çbmfb.7Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfb.5Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfb.3Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfb.5Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`blsŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2b--Ÿ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`blwŸ±Çaoa=Ÿ±Çbmia2Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`x                            Ÿ±Ç`becŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2acŸ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`bfcŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2dnoneŸ±Çbs2a"Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1u# Turn ticklabels offŸ±Ç`a
Ÿ±ÇakcforŸ±Ç`a Ÿ±Ç`caxiŸ±Ç`a Ÿ±ÇbowbinŸ±Ç`a Ÿ±Ç`a[Ÿ±Ç`faxins2Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`faxins3Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`cax2Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`cax3Ÿ±Ç`a]Ÿ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`caxiŸ±Çaoa.Ÿ±Ç`ktick_paramsŸ±Ç`a(Ÿ±Ç`ilabelleftŸ±Çaoa=Ÿ±ÇbkceFalseŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`klabelbottomŸ±Çaoa=Ÿ±ÇbkceFalseŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`dshowŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1xO###############################################################################Ÿ±Ç`a
Ÿ±Çbc1xO# In the above the axes transform together with 4-tuple bounding boxes has beenŸ±Ç`a
Ÿ±Çbc1xL# used as it mostly is useful to specify an inset relative to the axes it isŸ±Ç`a
Ÿ±Çbc1xJ# an inset to. However other use cases are equally possible. The followingŸ±Ç`a
Ÿ±Çbc1x!# example examines some of those.Ÿ±Ç`a
Ÿ±Çbc1a#Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`cfigŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`ffigureŸ±Ç`a(Ÿ±Ç`gfigsizeŸ±Çaoa=Ÿ±Ç`a[Ÿ±Çbmfc5.5Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfc2.8Ÿ±Ç`a]Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`baxŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cfigŸ±Çaoa.Ÿ±Ç`kadd_subplotŸ±Ç`a(Ÿ±Çbmic131Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1x"# Create an inset outside the axesŸ±Ç`a
Ÿ±Ç`eaxinsŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`jinset_axesŸ±Ç`a(Ÿ±Ç`baxŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ewidthŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2c100Ÿ±Çbs2a%Ÿ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`fheightŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2c100Ÿ±Çbs2a%Ÿ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`s                   Ÿ±Ç`nbbox_to_anchorŸ±Çaoa=Ÿ±Ç`a(Ÿ±Çbmfd1.05Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfb.6Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfb.5Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfb.4Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`s                   Ÿ±Ç`nbbox_transformŸ±Çaoa=Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`itransAxesŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`clocŸ±Çaoa=Ÿ±Çbmia2Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`iborderpadŸ±Çaoa=Ÿ±Çbmia0Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`eaxinsŸ±Çaoa.Ÿ±Ç`ktick_paramsŸ±Ç`a(Ÿ±Ç`dleftŸ±Çaoa=Ÿ±ÇbkceFalseŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`erightŸ±Çaoa=Ÿ±ÇbkcdTrueŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ilabelleftŸ±Çaoa=Ÿ±ÇbkceFalseŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`jlabelrightŸ±Çaoa=Ÿ±ÇbkcdTrueŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1xG# Create an inset with a 2-tuple bounding box. Note that this creates aŸ±Ç`a
Ÿ±Çbc1xB# bbox without extent. This hence only makes sense when specifyingŸ±Ç`a
Ÿ±Çbc1x.# width and height in absolute units (inches).Ÿ±Ç`a
Ÿ±Ç`faxins2Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`jinset_axesŸ±Ç`a(Ÿ±Ç`baxŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ewidthŸ±Çaoa=Ÿ±Çbmfc0.5Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`fheightŸ±Çaoa=Ÿ±Çbmfc0.4Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`t                    Ÿ±Ç`nbbox_to_anchorŸ±Çaoa=Ÿ±Ç`a(Ÿ±Çbmfd0.33Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd0.25Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`t                    Ÿ±Ç`nbbox_transformŸ±Çaoa=Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`itransAxesŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`clocŸ±Çaoa=Ÿ±Çbmia3Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`iborderpadŸ±Çaoa=Ÿ±Çbmia0Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`cax2Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cfigŸ±Çaoa.Ÿ±Ç`kadd_subplotŸ±Ç`a(Ÿ±Çbmic133Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cax2Ÿ±Çaoa.Ÿ±Ç`jset_xscaleŸ±Ç`a(Ÿ±Çbs2a"Ÿ±Çbs2clogŸ±Çbs2a"Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cax2Ÿ±Çaoa.Ÿ±Ç`csetŸ±Ç`a(Ÿ±Ç`dxlimŸ±Çaoa=Ÿ±Ç`a(Ÿ±Çbmfd1e-6Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfc1e6Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dylimŸ±Çaoa=Ÿ±Ç`a(Ÿ±Çaoa-Ÿ±Çbmia2Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia6Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1xB# Create inset in data coordinates using ax.transData as transformŸ±Ç`a
Ÿ±Ç`faxins3Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`jinset_axesŸ±Ç`a(Ÿ±Ç`cax2Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ewidthŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2c100Ÿ±Çbs2a%Ÿ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`fheightŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2c100Ÿ±Çbs2a%Ÿ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`t                    Ÿ±Ç`nbbox_to_anchorŸ±Çaoa=Ÿ±Ç`a(Ÿ±Çbmfd1e-2Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia2Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfc1e3Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia3Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`t                    Ÿ±Ç`nbbox_transformŸ±Çaoa=Ÿ±Ç`cax2Ÿ±Çaoa.Ÿ±Ç`itransDataŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`clocŸ±Çaoa=Ÿ±Çbmia2Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`iborderpadŸ±Çaoa=Ÿ±Çbmia0Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1xL# Create an inset horizontally centered in figure coordinates and verticallyŸ±Ç`a
Ÿ±Çbc1x!# bound to line up with the axes.Ÿ±Ç`a
Ÿ±ÇbkndfromŸ±Ç`a Ÿ±ÇbnnŸ¢ÑjmatplotlibŸ†Ñjmatplotlibe3.5.1fmodulejmatplotlibfmoduleıŸ±Çbnna.Ÿ±ÇbnnjtransformsŸ±Ç`a Ÿ±ÇbknfimportŸ±Ç`a Ÿ±Ç`xblended_transform_factoryŸ±Ç`b  Ÿ±Çbc1f# noqaŸ±Ç`a
Ÿ±Ç`itransformŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`xblended_transform_factoryŸ±Ç`a(Ÿ±Ç`cfigŸ±Çaoa.Ÿ±Ç`ktransFigureŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`cax2Ÿ±Çaoa.Ÿ±Ç`itransAxesŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`faxins4Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`jinset_axesŸ±Ç`a(Ÿ±Ç`cax2Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ewidthŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2b16Ÿ±Çbs2a%Ÿ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`fheightŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2b34Ÿ±Çbs2a%Ÿ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`t                    Ÿ±Ç`nbbox_to_anchorŸ±Çaoa=Ÿ±Ç`a(Ÿ±Çbmia0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia1Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`t                    Ÿ±Ç`nbbox_transformŸ±Çaoa=Ÿ±Ç`itransformŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`clocŸ±Çaoa=Ÿ±Çbmia8Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`iborderpadŸ±Çaoa=Ÿ±Çbmia0Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`dshowŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
`dNoneˆ