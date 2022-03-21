������������bsdxe"""
==============
Demo Axes Grid
==============

Grid of 2x2 images with single or own colorbar.
"""���`a
���`a
���bkndfrom���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����`a ���bknfimport���`a ���`ecbook���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���bkndfrom���`a ���bnnlmpl_toolkits���bnna.���bnnjaxes_grid1���`a ���bknfimport���`a ���`iImageGrid���`a
���`a
���`a
���akcdef���`a ���bnfnget_demo_image���`a(���`a)���`a:���`a
���`d    ���`az���`a ���aoa=���`a ���`ecbook���aoa.���`oget_sample_data���`a(���bs2a"���bs2xaxes_grid/bivariate_normal.npy���bs2a"���`a,���`a ���`gnp_load���aoa=���bkcdTrue���`a)���`a
���`d    ���bc1x# z is a numpy array of 15x15���`a
���`d    ���akfreturn���`a ���`az���`a,���`a ���`a(���aoa-���bmia3���`a,���`a ���bmia4���`a,���`a ���aoa-���bmia4���`a,���`a ���bmia3���`a)���`a
���`a
���`a
���akcdef���`a ���bnfpdemo_simple_grid���`a(���`cfig���`a)���`a:���`a
���`d    ���bsdxs"""
    A grid of 2x2 images with 0.05 inch pad between images and only
    the lower-left axes is labeled.
    """���`a
���`d    ���`dgrid���`a ���aoa=���`a ���`iImageGrid���`a(���`cfig���`a,���`a ���bmic141���`a,���`b  ���bc1x# similar to subplot(141)���`a
���`u                     ���`knrows_ncols���aoa=���`a(���bmia2���`a,���`a ���bmia2���`a)���`a,���`a
���`u                     ���`haxes_pad���aoa=���bmfd0.05���`a,���`a
���`u                     ���`jlabel_mode���aoa=���bs2a"���bs2a1���bs2a"���`a,���`a
���`u                     ���`a)���`a
���`d    ���`aZ���`a,���`a ���`fextent���`a ���aoa=���`a ���`nget_demo_image���`a(���`a)���`a
���`d    ���akcfor���`a ���`bax���`a ���bowbin���`a ���`dgrid���`a:���`a
���`h        ���`bax���aoa.���`fimshow���`a(���`aZ���`a,���`a ���`fextent���aoa=���`fextent���`a)���`a
���`d    ���bc1xK# This only affects axes in first column and second row as share_all=False.���`a
���`d    ���`dgrid���aoa.���`haxes_llc���aoa.���`jset_xticks���`a(���`a[���aoa-���bmia2���`a,���`a ���bmia0���`a,���`a ���bmia2���`a]���`a)���`a
���`d    ���`dgrid���aoa.���`haxes_llc���aoa.���`jset_yticks���`a(���`a[���aoa-���bmia2���`a,���`a ���bmia0���`a,���`a ���bmia2���`a]���`a)���`a
���`a
���`a
���akcdef���`a ���bnfxdemo_grid_with_single_cbar���`a(���`cfig���`a)���`a:���`a
���`d    ���bsdx;"""
    A grid of 2x2 images with a single colorbar
    """���`a
���`d    ���`dgrid���`a ���aoa=���`a ���`iImageGrid���`a(���`cfig���`a,���`a ���bmic142���`a,���`b  ���bc1x# similar to subplot(142)���`a
���`u                     ���`knrows_ncols���aoa=���`a(���bmia2���`a,���`a ���bmia2���`a)���`a,���`a
���`u                     ���`haxes_pad���aoa=���bmfc0.0���`a,���`a
���`u                     ���`ishare_all���aoa=���bkcdTrue���`a,���`a
���`u                     ���`jlabel_mode���aoa=���bs2a"���bs2aL���bs2a"���`a,���`a
���`u                     ���`mcbar_location���aoa=���bs2a"���bs2ctop���bs2a"���`a,���`a
���`u                     ���`icbar_mode���aoa=���bs2a"���bs2fsingle���bs2a"���`a,���`a
���`u                     ���`a)���`a
���`a
���`d    ���`aZ���`a,���`a ���`fextent���`a ���aoa=���`a ���`nget_demo_image���`a(���`a)���`a
���`d    ���akcfor���`a ���`bax���`a ���bowbin���`a ���`dgrid���`a:���`a
���`h        ���`bim���`a ���aoa=���`a ���`bax���aoa.���`fimshow���`a(���`aZ���`a,���`a ���`fextent���aoa=���`fextent���`a)���`a
���`d    ���`dgrid���aoa.���`icbar_axes���`a[���bmia0���`a]���aoa.���`hcolorbar���`a(���`bim���`a)���`a
���`a
���`d    ���akcfor���`a ���`ccax���`a ���bowbin���`a ���`dgrid���aoa.���`icbar_axes���`a:���`a
���`h        ���`ccax���aoa.���`ltoggle_label���`a(���bkceFalse���`a)���`a
���`a
���`d    ���bc1x,# This affects all axes as share_all = True.���`a
���`d    ���`dgrid���aoa.���`haxes_llc���aoa.���`jset_xticks���`a(���`a[���aoa-���bmia2���`a,���`a ���bmia0���`a,���`a ���bmia2���`a]���`a)���`a
���`d    ���`dgrid���aoa.���`haxes_llc���aoa.���`jset_yticks���`a(���`a[���aoa-���bmia2���`a,���`a ���bmia0���`a,���`a ���bmia2���`a]���`a)���`a
���`a
���`a
���akcdef���`a ���bnfxdemo_grid_with_each_cbar���`a(���`cfig���`a)���`a:���`a
���`d    ���bsdxF"""
    A grid of 2x2 images. Each image has its own colorbar.
    """���`a
���`d    ���`dgrid���`a ���aoa=���`a ���`iImageGrid���`a(���`cfig���`a,���`a ���bmic143���`a,���`b  ���bc1x# similar to subplot(143)���`a
���`u                     ���`knrows_ncols���aoa=���`a(���bmia2���`a,���`a ���bmia2���`a)���`a,���`a
���`u                     ���`haxes_pad���aoa=���bmfc0.1���`a,���`a
���`u                     ���`jlabel_mode���aoa=���bs2a"���bs2a1���bs2a"���`a,���`a
���`u                     ���`ishare_all���aoa=���bkcdTrue���`a,���`a
���`u                     ���`mcbar_location���aoa=���bs2a"���bs2ctop���bs2a"���`a,���`a
���`u                     ���`icbar_mode���aoa=���bs2a"���bs2deach���bs2a"���`a,���`a
���`u                     ���`icbar_size���aoa=���bs2a"���bs2a7���bs2a%���bs2a"���`a,���`a
���`u                     ���`hcbar_pad���aoa=���bs2a"���bs2a2���bs2a%���bs2a"���`a,���`a
���`u                     ���`a)���`a
���`d    ���`aZ���`a,���`a ���`fextent���`a ���aoa=���`a ���`nget_demo_image���`a(���`a)���`a
���`d    ���akcfor���`a ���`bax���`a,���`a ���`ccax���`a ���bowbin���`a ���bnbczip���`a(���`dgrid���`a,���`a ���`dgrid���aoa.���`icbar_axes���`a)���`a:���`a
���`h        ���`bim���`a ���aoa=���`a ���`bax���aoa.���`fimshow���`a(���`aZ���`a,���`a ���`fextent���aoa=���`fextent���`a)���`a
���`h        ���`ccax���aoa.���`hcolorbar���`a(���`bim���`a)���`a
���`h        ���`ccax���aoa.���`ltoggle_label���`a(���bkceFalse���`a)���`a
���`a
���`d    ���bc1x8# This affects all axes because we set share_all = True.���`a
���`d    ���`dgrid���aoa.���`haxes_llc���aoa.���`jset_xticks���`a(���`a[���aoa-���bmia2���`a,���`a ���bmia0���`a,���`a ���bmia2���`a]���`a)���`a
���`d    ���`dgrid���aoa.���`haxes_llc���aoa.���`jset_yticks���`a(���`a[���aoa-���bmia2���`a,���`a ���bmia0���`a,���`a ���bmia2���`a]���`a)���`a
���`a
���`a
���akcdef���`a ���bnfx!demo_grid_with_each_cbar_labelled���`a(���`cfig���`a)���`a:���`a
���`d    ���bsdxF"""
    A grid of 2x2 images. Each image has its own colorbar.
    """���`a
���`d    ���`dgrid���`a ���aoa=���`a ���`iImageGrid���`a(���`cfig���`a,���`a ���bmic144���`a,���`b  ���bc1x# similar to subplot(144)���`a
���`u                     ���`knrows_ncols���aoa=���`a(���bmia2���`a,���`a ���bmia2���`a)���`a,���`a
���`u                     ���`haxes_pad���aoa=���`a(���bmfd0.45���`a,���`a ���bmfd0.15���`a)���`a,���`a
���`u                     ���`jlabel_mode���aoa=���bs2a"���bs2a1���bs2a"���`a,���`a
���`u                     ���`ishare_all���aoa=���bkcdTrue���`a,���`a
���`u                     ���`mcbar_location���aoa=���bs2a"���bs2eright���bs2a"���`a,���`a
���`u                     ���`icbar_mode���aoa=���bs2a"���bs2deach���bs2a"���`a,���`a
���`u                     ���`icbar_size���aoa=���bs2a"���bs2a7���bs2a%���bs2a"���`a,���`a
���`u                     ���`hcbar_pad���aoa=���bs2a"���bs2a2���bs2a%���bs2a"���`a,���`a
���`u                     ���`a)���`a
���`d    ���`aZ���`a,���`a ���`fextent���`a ���aoa=���`a ���`nget_demo_image���`a(���`a)���`a
���`a
���`d    ���bc1x+# Use a different colorbar range every time���`a
���`d    ���`flimits���`a ���aoa=���`a ���`a(���`a(���bmia0���`a,���`a ���bmia1���`a)���`a,���`a ���`a(���aoa-���bmia2���`a,���`a ���bmia2���`a)���`a,���`a ���`a(���aoa-���bmfc1.7���`a,���`a ���bmfc1.4���`a)���`a,���`a ���`a(���aoa-���bmfc1.5���`a,���`a ���bmia1���`a)���`a)���`a
���`d    ���akcfor���`a ���`bax���`a,���`a ���`ccax���`a,���`a ���`dvlim���`a ���bowbin���`a ���bnbczip���`a(���`dgrid���`a,���`a ���`dgrid���aoa.���`icbar_axes���`a,���`a ���`flimits���`a)���`a:���`a
���`h        ���`bim���`a ���aoa=���`a ���`bax���aoa.���`fimshow���`a(���`aZ���`a,���`a ���`fextent���aoa=���`fextent���`a,���`a ���`dvmin���aoa=���`dvlim���`a[���bmia0���`a]���`a,���`a ���`dvmax���aoa=���`dvlim���`a[���bmia1���`a]���`a)���`a
���`h        ���`bcb���`a ���aoa=���`a ���`ccax���aoa.���`hcolorbar���`a(���`bim���`a)���`a
���`h        ���`bcb���aoa.���`iset_ticks���`a(���`a(���`dvlim���`a[���bmia0���`a]���`a,���`a ���`dvlim���`a[���bmia1���`a]���`a)���`a)���`a
���`a
���`d    ���bc1x8# This affects all axes because we set share_all = True.���`a
���`d    ���`dgrid���aoa.���`haxes_llc���aoa.���`jset_xticks���`a(���`a[���aoa-���bmia2���`a,���`a ���bmia0���`a,���`a ���bmia2���`a]���`a)���`a
���`d    ���`dgrid���aoa.���`haxes_llc���aoa.���`jset_yticks���`a(���`a[���aoa-���bmia2���`a,���`a ���bmia0���`a,���`a ���bmia2���`a]���`a)���`a
���`a
���`a
���`cfig���`a ���aoa=���`a ���`cplt���aoa.���`ffigure���`a(���`gfigsize���aoa=���`a(���bmfd10.5���`a,���`a ���bmfc2.5���`a)���`a)���`a
���`cfig���aoa.���`osubplots_adjust���`a(���`dleft���aoa=���bmfd0.05���`a,���`a ���`eright���aoa=���bmfd0.95���`a)���`a
���`a
���`pdemo_simple_grid���`a(���`cfig���`a)���`a
���`xdemo_grid_with_single_cbar���`a(���`cfig���`a)���`a
���`xdemo_grid_with_each_cbar���`a(���`cfig���`a)���`a
���`x!demo_grid_with_each_cbar_labelled���`a(���`cfig���`a)���`a
���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
`dNone�