������������bsdx�"""
===============================
Per-row or per-column colorbars
===============================

This example shows how to use one common colorbar for each row or column
of an image grid.
"""���`a
���`a
���bkndfrom���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����`a ���bknfimport���`a ���`ecbook���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���bkndfrom���`a ���bnnlmpl_toolkits���bnna.���bnnjaxes_grid1���`a ���bknfimport���`a ���`hAxesGrid���`a
���`a
���`a
���akcdef���`a ���bnfnget_demo_image���`a(���`a)���`a:���`a
���`d    ���`az���`a ���aoa=���`a ���`ecbook���aoa.���`oget_sample_data���`a(���bs2a"���bs2xaxes_grid/bivariate_normal.npy���bs2a"���`a,���`a ���`gnp_load���aoa=���bkcdTrue���`a)���`a
���`d    ���bc1x# z is a numpy array of 15x15���`a
���`d    ���akfreturn���`a ���`az���`a,���`a ���`a(���aoa-���bmia3���`a,���`a ���bmia4���`a,���`a ���aoa-���bmia4���`a,���`a ���bmia3���`a)���`a
���`a
���`a
���akcdef���`a ���bnfpdemo_bottom_cbar���`a(���`cfig���`a)���`a:���`a
���`d    ���bsdxE"""
    A grid of 2x2 images with a colorbar for each column.
    """���`a
���`d    ���`dgrid���`a ���aoa=���`a ���`hAxesGrid���`a(���`cfig���`a,���`a ���bmic121���`a,���`b  ���bc1x# similar to subplot(121)���`a
���`t                    ���`knrows_ncols���aoa=���`a(���bmia2���`a,���`a ���bmia2���`a)���`a,���`a
���`t                    ���`haxes_pad���aoa=���bmfd0.10���`a,���`a
���`t                    ���`ishare_all���aoa=���bkcdTrue���`a,���`a
���`t                    ���`jlabel_mode���aoa=���bs2a"���bs2a1���bs2a"���`a,���`a
���`t                    ���`mcbar_location���aoa=���bs2a"���bs2fbottom���bs2a"���`a,���`a
���`t                    ���`icbar_mode���aoa=���bs2a"���bs2dedge���bs2a"���`a,���`a
���`t                    ���`hcbar_pad���aoa=���bmfd0.25���`a,���`a
���`t                    ���`icbar_size���aoa=���bs2a"���bs2b15���bs2a%���bs2a"���`a,���`a
���`t                    ���`idirection���aoa=���bs2a"���bs2fcolumn���bs2a"���`a
���`t                    ���`a)���`a
���`a
���`d    ���`aZ���`a,���`a ���`fextent���`a ���aoa=���`a ���`nget_demo_image���`a(���`a)���`a
���`d    ���`ecmaps���`a ���aoa=���`a ���`a[���bs2a"���bs2fautumn���bs2a"���`a,���`a ���bs2a"���bs2fsummer���bs2a"���`a]���`a
���`d    ���akcfor���`a ���`ai���`a ���bowbin���`a ���bnberange���`a(���bmia4���`a)���`a:���`a
���`h        ���`bim���`a ���aoa=���`a ���`dgrid���`a[���`ai���`a]���aoa.���`fimshow���`a(���`aZ���`a,���`a ���`fextent���aoa=���`fextent���`a,���`a ���`dcmap���aoa=���`ecmaps���`a[���`ai���aoa/���aoa/���bmia2���`a]���`a)���`a
���`h        ���akbif���`a ���`ai���`a ���aoa%���`a ���bmia2���`a:���`a
���`l            ���`dgrid���aoa.���`icbar_axes���`a[���`ai���aoa/���aoa/���bmia2���`a]���aoa.���`hcolorbar���`a(���`bim���`a)���`a
���`a
���`d    ���akcfor���`a ���`ccax���`a ���bowbin���`a ���`dgrid���aoa.���`icbar_axes���`a:���`a
���`h        ���`ccax���aoa.���`ltoggle_label���`a(���bkcdTrue���`a)���`a
���`h        ���`ccax���aoa.���`daxis���`a[���`ccax���aoa.���`korientation���`a]���aoa.���`iset_label���`a(���bs2a"���bs2cBar���bs2a"���`a)���`a
���`a
���`d    ���bc1x,# This affects all axes as share_all = True.���`a
���`d    ���`dgrid���aoa.���`haxes_llc���aoa.���`jset_xticks���`a(���`a[���aoa-���bmia2���`a,���`a ���bmia0���`a,���`a ���bmia2���`a]���`a)���`a
���`d    ���`dgrid���aoa.���`haxes_llc���aoa.���`jset_yticks���`a(���`a[���aoa-���bmia2���`a,���`a ���bmia0���`a,���`a ���bmia2���`a]���`a)���`a
���`a
���`a
���akcdef���`a ���bnfodemo_right_cbar���`a(���`cfig���`a)���`a:���`a
���`d    ���bsdxD"""
    A grid of 2x2 images. Each row has its own colorbar.
    """���`a
���`d    ���`dgrid���`a ���aoa=���`a ���`hAxesGrid���`a(���`cfig���`a,���`a ���bmic122���`a,���`b  ���bc1x# similar to subplot(122)���`a
���`t                    ���`knrows_ncols���aoa=���`a(���bmia2���`a,���`a ���bmia2���`a)���`a,���`a
���`t                    ���`haxes_pad���aoa=���bmfd0.10���`a,���`a
���`t                    ���`jlabel_mode���aoa=���bs2a"���bs2a1���bs2a"���`a,���`a
���`t                    ���`ishare_all���aoa=���bkcdTrue���`a,���`a
���`t                    ���`mcbar_location���aoa=���bs2a"���bs2eright���bs2a"���`a,���`a
���`t                    ���`icbar_mode���aoa=���bs2a"���bs2dedge���bs2a"���`a,���`a
���`t                    ���`icbar_size���aoa=���bs2a"���bs2a7���bs2a%���bs2a"���`a,���`a
���`t                    ���`hcbar_pad���aoa=���bs2a"���bs2a2���bs2a%���bs2a"���`a,���`a
���`t                    ���`a)���`a
���`d    ���`aZ���`a,���`a ���`fextent���`a ���aoa=���`a ���`nget_demo_image���`a(���`a)���`a
���`d    ���`ecmaps���`a ���aoa=���`a ���`a[���bs2a"���bs2fspring���bs2a"���`a,���`a ���bs2a"���bs2fwinter���bs2a"���`a]���`a
���`d    ���akcfor���`a ���`ai���`a ���bowbin���`a ���bnberange���`a(���bmia4���`a)���`a:���`a
���`h        ���`bim���`a ���aoa=���`a ���`dgrid���`a[���`ai���`a]���aoa.���`fimshow���`a(���`aZ���`a,���`a ���`fextent���aoa=���`fextent���`a,���`a ���`dcmap���aoa=���`ecmaps���`a[���`ai���aoa/���aoa/���bmia2���`a]���`a)���`a
���`h        ���akbif���`a ���`ai���`a ���aoa%���`a ���bmia2���`a:���`a
���`l            ���`dgrid���aoa.���`icbar_axes���`a[���`ai���aoa/���aoa/���bmia2���`a]���aoa.���`hcolorbar���`a(���`bim���`a)���`a
���`a
���`d    ���akcfor���`a ���`ccax���`a ���bowbin���`a ���`dgrid���aoa.���`icbar_axes���`a:���`a
���`h        ���`ccax���aoa.���`ltoggle_label���`a(���bkcdTrue���`a)���`a
���`h        ���`ccax���aoa.���`daxis���`a[���`ccax���aoa.���`korientation���`a]���aoa.���`iset_label���`a(���bs1a'���bs1cFoo���bs1a'���`a)���`a
���`a
���`d    ���bc1x8# This affects all axes because we set share_all = True.���`a
���`d    ���`dgrid���aoa.���`haxes_llc���aoa.���`jset_xticks���`a(���`a[���aoa-���bmia2���`a,���`a ���bmia0���`a,���`a ���bmia2���`a]���`a)���`a
���`d    ���`dgrid���aoa.���`haxes_llc���aoa.���`jset_yticks���`a(���`a[���aoa-���bmia2���`a,���`a ���bmia0���`a,���`a ���bmia2���`a]���`a)���`a
���`a
���`a
���`cfig���`a ���aoa=���`a ���`cplt���aoa.���`ffigure���`a(���`gfigsize���aoa=���`a(���bmfc5.5���`a,���`a ���bmfc2.5���`a)���`a)���`a
���`cfig���aoa.���`osubplots_adjust���`a(���`dleft���aoa=���bmfd0.05���`a,���`a ���`eright���aoa=���bmfd0.93���`a)���`a
���`a
���`pdemo_bottom_cbar���`a(���`cfig���`a)���`a
���`odemo_right_cbar���`a(���`cfig���`a)���`a
���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
`dNone�