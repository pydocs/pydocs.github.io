ŸØÇÅŸ¥ÉôŸ±Çbsdy """
======================================
Projecting filled contour onto a graph
======================================

Demonstrates displaying a 3D surface while also projecting filled contour
'profiles' onto the 'walls' of the graph.

See contour3d_demo2 for the unfilled version.
"""Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±ÇbkndfromŸ±Ç`a Ÿ±Çbnnlmpl_toolkitsŸ±Çbnna.Ÿ±Çbnngmplot3dŸ±Ç`a Ÿ±ÇbknfimportŸ±Ç`a Ÿ±Ç`faxes3dŸ±Ç`a
Ÿ±ÇbknfimportŸ±Ç`a Ÿ±ÇbnnŸ¢ÑjmatplotlibŸ†Ñjmatplotlibe3.5.1fmodulejmatplotlibfmoduleıŸ±Çbnna.Ÿ±ÇbnnfpyplotŸ±Ç`a Ÿ±ÇakbasŸ±Ç`a Ÿ±ÇbnncpltŸ±Ç`a
Ÿ±ÇbkndfromŸ±Ç`a Ÿ±ÇbnnŸ¢ÑjmatplotlibŸ†Ñjmatplotlibe3.5.1fmodulejmatplotlibfmoduleıŸ±Ç`a Ÿ±ÇbknfimportŸ±Ç`a Ÿ±Ç`bcmŸ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`baxŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`ffigureŸ±Ç`a(Ÿ±Ç`a)Ÿ±Çaoa.Ÿ±Ç`kadd_subplotŸ±Ç`a(Ÿ±Ç`jprojectionŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1b3dŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`aXŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`aYŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`aZŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`faxes3dŸ±Çaoa.Ÿ±Ç`mget_test_dataŸ±Ç`a(Ÿ±Çbmfd0.05Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1u# Plot the 3D surfaceŸ±Ç`a
Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`lplot_surfaceŸ±Ç`a(Ÿ±Ç`aXŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`aYŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`aZŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`grstrideŸ±Çaoa=Ÿ±Çbmia8Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`gcstrideŸ±Çaoa=Ÿ±Çbmia8Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ealphaŸ±Çaoa=Ÿ±Çbmfc0.3Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1xK# Plot projections of the contours for each dimension.  By choosing offsetsŸ±Ç`a
Ÿ±Çbc1xL# that match the appropriate axes limits, the projected contours will sit onŸ±Ç`a
Ÿ±Çbc1x# the 'walls' of the graphŸ±Ç`a
Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`hcontourfŸ±Ç`a(Ÿ±Ç`aXŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`aYŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`aZŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dzdirŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1azŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`foffsetŸ±Çaoa=Ÿ±Çaoa-Ÿ±Çbmic100Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dcmapŸ±Çaoa=Ÿ±Ç`bcmŸ±Çaoa.Ÿ±Ç`hcoolwarmŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`hcontourfŸ±Ç`a(Ÿ±Ç`aXŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`aYŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`aZŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dzdirŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1axŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`foffsetŸ±Çaoa=Ÿ±Çaoa-Ÿ±Çbmib40Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dcmapŸ±Çaoa=Ÿ±Ç`bcmŸ±Çaoa.Ÿ±Ç`hcoolwarmŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`hcontourfŸ±Ç`a(Ÿ±Ç`aXŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`aYŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`aZŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dzdirŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1ayŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`foffsetŸ±Çaoa=Ÿ±Çbmib40Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dcmapŸ±Çaoa=Ÿ±Ç`bcmŸ±Çaoa.Ÿ±Ç`hcoolwarmŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`csetŸ±Ç`a(Ÿ±Ç`dxlimŸ±Çaoa=Ÿ±Ç`a(Ÿ±Çaoa-Ÿ±Çbmib40Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmib40Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dylimŸ±Çaoa=Ÿ±Ç`a(Ÿ±Çaoa-Ÿ±Çbmib40Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmib40Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dzlimŸ±Çaoa=Ÿ±Ç`a(Ÿ±Çaoa-Ÿ±Çbmic100Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmic100Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`g       Ÿ±Ç`fxlabelŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1aXŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`fylabelŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1aYŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`fzlabelŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1aZŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`dshowŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
`dNoneˆ