��������#���bsdx)"""
==========
Ribbon Box
==========

"""���`a
���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���`a
���bkndfrom���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����`a ���bknfimport���`a ���`ecbook���`a,���`a ���`fcolors���`a ���akbas���`a ���`gmcolors���`a
���bkndfrom���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnneimage���`a ���bknfimport���`a ���`iAxesImage���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���bkndfrom���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnjtransforms���`a ���bknfimport���`a ���`dBbox���`a,���`a ���`oTransformedBbox���`a,���`a ���`oBboxTransformTo���`a
���`a
���`a
���akeclass���`a ���bnciRibbonBox���`a:���`a
���`a
���`d    ���`noriginal_image���`a ���aoa=���`a ���`cplt���aoa.���`fimread���`a(���`a
���`h        ���`ecbook���aoa.���`oget_sample_data���`a(���bs2a"���bs2xMinduka_Present_Blue_Pack.png���bs2a"���`a)���`a)���`a
���`d    ���`lcut_location���`a ���aoa=���`a ���bmib70���`a
���`d    ���`gb_and_h���`a ���aoa=���`a ���`noriginal_image���`a[���`a:���`a,���`a ���`a:���`a,���`a ���bmia2���`a:���bmia3���`a]���`a
���`d    ���`ecolor���`a ���aoa=���`a ���`noriginal_image���`a[���`a:���`a,���`a ���`a:���`a,���`a ���bmia2���`a:���bmia3���`a]���`a ���aoa-���`a ���`noriginal_image���`a[���`a:���`a,���`a ���`a:���`a,���`a ���bmia0���`a:���bmia1���`a]���`a
���`d    ���`ealpha���`a ���aoa=���`a ���`noriginal_image���`a[���`a:���`a,���`a ���`a:���`a,���`a ���bmia3���`a:���bmia4���`a]���`a
���`d    ���`bnx���`a ���aoa=���`a ���`noriginal_image���aoa.���`eshape���`a[���bmia1���`a]���`a
���`a
���`d    ���akcdef���`a ���bfmh__init__���`a(���bbpdself���`a,���`a ���`ecolor���`a)���`a:���`a
���`h        ���`crgb���`a ���aoa=���`a ���`gmcolors���aoa.���`gto_rgba���`a(���`ecolor���`a)���`a[���`a:���bmia3���`a]���`a
���`h        ���bbpdself���aoa.���`bim���`a ���aoa=���`a ���`bnp���aoa.���`fdstack���`a(���`a
���`l            ���`a[���bbpdself���aoa.���`gb_and_h���`a ���aoa-���`a ���bbpdself���aoa.���`ecolor���`a ���aoa*���`a ���`a(���bmia1���`a ���aoa-���`a ���`bnp���aoa.���`earray���`a(���`crgb���`a)���`a)���`a,���`a ���bbpdself���aoa.���`ealpha���`a]���`a)���`a
���`a
���`d    ���akcdef���`a ���bnfsget_stretched_image���`a(���bbpdself���`a,���`a ���`nstretch_factor���`a)���`a:���`a
���`h        ���`nstretch_factor���`a ���aoa=���`a ���bnbcmax���`a(���`nstretch_factor���`a,���`a ���bmia1���`a)���`a
���`h        ���`bny���`a,���`a ���`bnx���`a,���`a ���`cnch���`a ���aoa=���`a ���bbpdself���aoa.���`bim���aoa.���`eshape���`a
���`h        ���`cny2���`a ���aoa=���`a ���bnbcint���`a(���`bny���aoa*���`nstretch_factor���`a)���`a
���`h        ���akfreturn���`a ���`bnp���aoa.���`fvstack���`a(���`a
���`l            ���`a[���bbpdself���aoa.���`bim���`a[���`a:���bbpdself���aoa.���`lcut_location���`a]���`a,���`a
���`m             ���`bnp���aoa.���`lbroadcast_to���`a(���`a
���`q                 ���bbpdself���aoa.���`bim���`a[���bbpdself���aoa.���`lcut_location���`a]���`a,���`a ���`a(���`cny2���`a ���aoa-���`a ���`bny���`a,���`a ���`bnx���`a,���`a ���`cnch���`a)���`a)���`a,���`a
���`m             ���bbpdself���aoa.���`bim���`a[���bbpdself���aoa.���`lcut_location���`a:���`a]���`a]���`a)���`a
���`a
���`a
���akeclass���`a ���bncnRibbonBoxImage���`a(���`iAxesImage���`a)���`a:���`a
���`d    ���`fzorder���`a ���aoa=���`a ���bmia1���`a
���`a
���`d    ���akcdef���`a ���bfmh__init__���`a(���bbpdself���`a,���`a ���`bax���`a,���`a ���`dbbox���`a,���`a ���`ecolor���`a,���`a ���aoa*���`a,���`a ���`fextent���aoa=���`a(���bmia0���`a,���`a ���bmia1���`a,���`a ���bmia0���`a,���`a ���bmia1���`a)���`a,���`a ���aoa*���aoa*���`fkwargs���`a)���`a:���`a
���`h        ���bnbesuper���`a(���`a)���aoa.���bfmh__init__���`a(���`bax���`a,���`a ���`fextent���aoa=���`fextent���`a,���`a ���aoa*���aoa*���`fkwargs���`a)���`a
���`h        ���bbpdself���aoa.���`e_bbox���`a ���aoa=���`a ���`dbbox���`a
���`h        ���bbpdself���aoa.���`j_ribbonbox���`a ���aoa=���`a ���`iRibbonBox���`a(���`ecolor���`a)���`a
���`h        ���bbpdself���aoa.���`mset_transform���`a(���`oBboxTransformTo���`a(���`dbbox���`a)���`a)���`a
���`a
���`d    ���akcdef���`a ���bnfddraw���`a(���bbpdself���`a,���`a ���`hrenderer���`a,���`a ���aoa*���`dargs���`a,���`a ���aoa*���aoa*���`fkwargs���`a)���`a:���`a
���`h        ���`nstretch_factor���`a ���aoa=���`a ���bbpdself���aoa.���`e_bbox���aoa.���`fheight���`a ���aoa/���`a ���bbpdself���aoa.���`e_bbox���aoa.���`ewidth���`a
���`a
���`h        ���`bny���`a ���aoa=���`a ���bnbcint���`a(���`nstretch_factor���aoa*���bbpdself���aoa.���`j_ribbonbox���aoa.���`bnx���`a)���`a
���`h        ���akbif���`a ���bbpdself���aoa.���`iget_array���`a(���`a)���`a ���bowbis���`a ���bkcdNone���`a ���bowbor���`a ���bbpdself���aoa.���`iget_array���`a(���`a)���aoa.���`eshape���`a[���bmia0���`a]���`a ���aob!=���`a ���`bny���`a:���`a
���`l            ���`carr���`a ���aoa=���`a ���bbpdself���aoa.���`j_ribbonbox���aoa.���`sget_stretched_image���`a(���`nstretch_factor���`a)���`a
���`l            ���bbpdself���aoa.���`iset_array���`a(���`carr���`a)���`a
���`a
���`h        ���bnbesuper���`a(���`a)���aoa.���`ddraw���`a(���`hrenderer���`a,���`a ���aoa*���`dargs���`a,���`a ���aoa*���aoa*���`fkwargs���`a)���`a
���`a
���`a
���akcdef���`a ���bnfdmain���`a(���`a)���`a:���`a
���`d    ���`cfig���`a,���`a ���`bax���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`a)���`a
���`a
���`d    ���`eyears���`a ���aoa=���`a ���`bnp���aoa.���`farange���`a(���bmid2004���`a,���`a ���bmid2009���`a)���`a
���`d    ���`gheights���`a ���aoa=���`a ���`a[���bmid7900���`a,���`a ���bmid8100���`a,���`a ���bmid7900���`a,���`a ���bmid6900���`a,���`a ���bmid2800���`a]���`a
���`d    ���`jbox_colors���`a ���aoa=���`a ���`a[���`a
���`h        ���`a(���bmfc0.8���`a,���`a ���bmfc0.2���`a,���`a ���bmfc0.2���`a)���`a,���`a
���`h        ���`a(���bmfc0.2���`a,���`a ���bmfc0.8���`a,���`a ���bmfc0.2���`a)���`a,���`a
���`h        ���`a(���bmfc0.2���`a,���`a ���bmfc0.2���`a,���`a ���bmfc0.8���`a)���`a,���`a
���`h        ���`a(���bmfc0.7���`a,���`a ���bmfc0.5���`a,���`a ���bmfc0.8���`a)���`a,���`a
���`h        ���`a(���bmfc0.3���`a,���`a ���bmfc0.8���`a,���`a ���bmfc0.7���`a)���`a,���`a
���`d    ���`a]���`a
���`a
���`d    ���akcfor���`a ���`dyear���`a,���`a ���`ah���`a,���`a ���`bbc���`a ���bowbin���`a ���bnbczip���`a(���`eyears���`a,���`a ���`gheights���`a,���`a ���`jbox_colors���`a)���`a:���`a
���`h        ���`ebbox0���`a ���aoa=���`a ���`dBbox���aoa.���`lfrom_extents���`a(���`dyear���`a ���aoa-���`a ���bmfc0.4���`a,���`a ���bmfb0.���`a,���`a ���`dyear���`a ���aoa+���`a ���bmfc0.4���`a,���`a ���`ah���`a)���`a
���`h        ���`dbbox���`a ���aoa=���`a ���`oTransformedBbox���`a(���`ebbox0���`a,���`a ���`bax���aoa.���`itransData���`a)���`a
���`h        ���`bax���aoa.���`jadd_artist���`a(���`nRibbonBoxImage���`a(���`bax���`a,���`a ���`dbbox���`a,���`a ���`bbc���`a,���`a ���`minterpolation���aoa=���bs2a"���bs2gbicubic���bs2a"���`a)���`a)���`a
���`h        ���`bax���aoa.���`hannotate���`a(���bnbcstr���`a(���`ah���`a)���`a,���`a ���`a(���`dyear���`a,���`a ���`ah���`a)���`a,���`a ���`bva���aoa=���bs2a"���bs2fbottom���bs2a"���`a,���`a ���`bha���aoa=���bs2a"���bs2fcenter���bs2a"���`a)���`a
���`a
���`d    ���`bax���aoa.���`hset_xlim���`a(���`eyears���`a[���bmia0���`a]���`a ���aoa-���`a ���bmfc0.5���`a,���`a ���`eyears���`a[���aoa-���bmia1���`a]���`a ���aoa+���`a ���bmfc0.5���`a)���`a
���`d    ���`bax���aoa.���`hset_ylim���`a(���bmia0���`a,���`a ���bmie10000���`a)���`a
���`a
���`d    ���`sbackground_gradient���`a ���aoa=���`a ���`bnp���aoa.���`ezeros���`a(���`a(���bmia2���`a,���`a ���bmia2���`a,���`a ���bmia4���`a)���`a)���`a
���`d    ���`sbackground_gradient���`a[���`a:���`a,���`a ���`a:���`a,���`a ���`a:���bmia3���`a]���`a ���aoa=���`a ���`a[���bmia1���`a,���`a ���bmia1���`a,���`a ���bmia0���`a]���`a
���`d    ���`sbackground_gradient���`a[���`a:���`a,���`a ���`a:���`a,���`a ���bmia3���`a]���`a ���aoa=���`a ���`a[���`a[���bmfc0.1���`a,���`a ���bmfc0.3���`a]���`a,���`a ���`a[���bmfc0.3���`a,���`a ���bmfc0.5���`a]���`a]���`b  ���bc1o# alpha channel���`a
���`d    ���`bax���aoa.���`fimshow���`a(���`sbackground_gradient���`a,���`a ���`minterpolation���aoa=���bs2a"���bs2gbicubic���bs2a"���`a,���`a ���`fzorder���aoa=���bmfc0.1���`a,���`a
���`n              ���`fextent���aoa=���`a(���bmia0���`a,���`a ���bmia1���`a,���`a ���bmia0���`a,���`a ���bmia1���`a)���`a,���`a ���`itransform���aoa=���`bax���aoa.���`itransAxes���`a,���`a ���`faspect���aoa=���bs2a"���bs2dauto���bs2a"���`a)���`a
���`a
���`d    ���`cplt���aoa.���`dshow���`a(���`a)���`a
���`a
���`a
���`dmain���`a(���`a)���`a
`dNone�