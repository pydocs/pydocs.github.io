������������bsdxU"""
==========
Axes Grid2
==========

Grid of images with shared xaxis and yaxis.
"""���`a
���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���bkndfrom���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����`a ���bknfimport���`a ���`ecbook���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfcolors���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���bkndfrom���`a ���bnnlmpl_toolkits���bnna.���bnnjaxes_grid1���`a ���bknfimport���`a ���`iImageGrid���`a
���`a
���`a
���akcdef���`a ���bnfoadd_inner_title���`a(���`bax���`a,���`a ���`etitle���`a,���`a ���`cloc���`a,���`a ���aoa*���aoa*���`fkwargs���`a)���`a:���`a
���`d    ���bkndfrom���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnioffsetbox���`a ���bknfimport���`a ���`lAnchoredText���`a
���`d    ���bkndfrom���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnkpatheffects���`a ���bknfimport���`a ���`jwithStroke���`a
���`d    ���`dprop���`a ���aoa=���`a ���bnbddict���`a(���`lpath_effects���aoa=���`a[���`jwithStroke���`a(���`jforeground���aoa=���bs1a'���bs1aw���bs1a'���`a,���`a ���`ilinewidth���aoa=���bmia3���`a)���`a]���`a,���`a
���`p                ���`dsize���aoa=���`cplt���aoa.���`hrcParams���`a[���bs1a'���bs1olegend.fontsize���bs1a'���`a]���`a)���`a
���`d    ���`bat���`a ���aoa=���`a ���`lAnchoredText���`a(���`etitle���`a,���`a ���`cloc���aoa=���`cloc���`a,���`a ���`dprop���aoa=���`dprop���`a,���`a
���`v                      ���`cpad���aoa=���bmfb0.���`a,���`a ���`iborderpad���aoa=���bmfc0.5���`a,���`a
���`v                      ���`gframeon���aoa=���bkceFalse���`a,���`a ���aoa*���aoa*���`fkwargs���`a)���`a
���`d    ���`bax���aoa.���`jadd_artist���`a(���`bat���`a)���`a
���`d    ���akfreturn���`a ���`bat���`a
���`a
���`a
���`cfig���`a ���aoa=���`a ���`cplt���aoa.���`ffigure���`a(���`gfigsize���aoa=���`a(���bmia6���`a,���`a ���bmia6���`a)���`a)���`a
���`a
���bc1p# Prepare images���`a
���`aZ���`a ���aoa=���`a ���`ecbook���aoa.���`oget_sample_data���`a(���bs2a"���bs2xaxes_grid/bivariate_normal.npy���bs2a"���`a,���`a ���`gnp_load���aoa=���bkcdTrue���`a)���`a
���`fextent���`a ���aoa=���`a ���`a(���aoa-���bmia3���`a,���`a ���bmia4���`a,���`a ���aoa-���bmia4���`a,���`a ���bmia3���`a)���`a
���`bZS���`a ���aoa=���`a ���`a[���`aZ���`a[���`ai���`a:���`a:���bmia3���`a,���`a ���`a:���`a]���`a ���akcfor���`a ���`ai���`a ���bowbin���`a ���bnberange���`a(���bmia3���`a)���`a]���`a
���`fextent���`a ���aoa=���`a ���`fextent���`a[���bmia0���`a]���`a,���`a ���`fextent���`a[���bmia1���`a]���aoa/���bmfb3.���`a,���`a ���`fextent���`a[���bmia2���`a]���`a,���`a ���`fextent���`a[���bmia3���`a]���`a
���`a
���bc1x'# *** Demo 1: colorbar at each axes ***���`a
���`dgrid���`a ���aoa=���`a ���`iImageGrid���`a(���`cfig���`a,���`a ���bmic211���`a,���`b  ���bc1x# similar to subplot(211)���`a
���`q                 ���`knrows_ncols���aoa=���`a(���bmia1���`a,���`a ���bmia3���`a)���`a,���`a
���`q                 ���`haxes_pad���aoa=���bmfd0.05���`a,���`a
���`q                 ���`jlabel_mode���aoa=���bs2a"���bs2a1���bs2a"���`a,���`a
���`q                 ���`ishare_all���aoa=���bkcdTrue���`a,���`a
���`q                 ���`mcbar_location���aoa=���bs2a"���bs2ctop���bs2a"���`a,���`a
���`q                 ���`icbar_mode���aoa=���bs2a"���bs2deach���bs2a"���`a,���`a
���`q                 ���`icbar_size���aoa=���bs2a"���bs2a7���bs2a%���bs2a"���`a,���`a
���`q                 ���`hcbar_pad���aoa=���bs2a"���bs2a1���bs2a%���bs2a"���`a,���`a
���`q                 ���`a)���`a
���`a
���akcfor���`a ���`ai���`a,���`a ���`a(���`bax���`a,���`a ���`az���`a)���`a ���bowbin���`a ���bnbienumerate���`a(���bnbczip���`a(���`dgrid���`a,���`a ���`bZS���`a)���`a)���`a:���`a
���`d    ���`bim���`a ���aoa=���`a ���`bax���aoa.���`fimshow���`a(���`az���`a,���`a ���`forigin���aoa=���bs2a"���bs2elower���bs2a"���`a,���`a ���`fextent���aoa=���`fextent���`a)���`a
���`d    ���`bcb���`a ���aoa=���`a ���`bax���aoa.���`ccax���aoa.���`hcolorbar���`a(���`bim���`a)���`a
���`d    ���bc1x# Changing the colorbar ticks���`a
���`d    ���akbif���`a ���`ai���`a ���bowbin���`a ���`a[���bmia1���`a,���`a ���bmia2���`a]���`a:���`a
���`h        ���`bcb���aoa.���`iset_ticks���`a(���`a[���aoa-���bmia1���`a,���`a ���bmia0���`a,���`a ���bmia1���`a]���`a)���`a
���`a
���akcfor���`a ���`bax���`a,���`a ���`him_title���`a ���bowbin���`a ���bnbczip���`a(���`dgrid���`a,���`a ���`a[���bs2a"���bs2gImage 1���bs2a"���`a,���`a ���bs2a"���bs2gImage 2���bs2a"���`a,���`a ���bs2a"���bs2gImage 3���bs2a"���`a]���`a)���`a:���`a
���`d    ���`at���`a ���aoa=���`a ���`oadd_inner_title���`a(���`bax���`a,���`a ���`him_title���`a,���`a ���`cloc���aoa=���bs1a'���bs1jlower left���bs1a'���`a)���`a
���`d    ���`at���aoa.���`epatch���aoa.���`iset_alpha���`a(���bmfc0.5���`a)���`a
���`a
���akcfor���`a ���`bax���`a,���`a ���`az���`a ���bowbin���`a ���bnbczip���`a(���`dgrid���`a,���`a ���`bZS���`a)���`a:���`a
���`d    ���`bax���aoa.���`ccax���aoa.���`ltoggle_label���`a(���bkcdTrue���`a)���`a
���`a
���`dgrid���`a[���bmia0���`a]���aoa.���`jset_xticks���`a(���`a[���aoa-���bmia2���`a,���`a ���bmia0���`a]���`a)���`a
���`dgrid���`a[���bmia0���`a]���aoa.���`jset_yticks���`a(���`a[���aoa-���bmia2���`a,���`a ���bmia0���`a,���`a ���bmia2���`a]���`a)���`a
���`a
���bc1x!# *** Demo 2: shared colorbar ***���`a
���`egrid2���`a ���aoa=���`a ���`iImageGrid���`a(���`cfig���`a,���`a ���bmic212���`a,���`a
���`r                  ���`knrows_ncols���aoa=���`a(���bmia1���`a,���`a ���bmia3���`a)���`a,���`a
���`r                  ���`haxes_pad���aoa=���bmfd0.05���`a,���`a
���`r                  ���`jlabel_mode���aoa=���bs2a"���bs2a1���bs2a"���`a,���`a
���`r                  ���`ishare_all���aoa=���bkcdTrue���`a,���`a
���`r                  ���`mcbar_location���aoa=���bs2a"���bs2eright���bs2a"���`a,���`a
���`r                  ���`icbar_mode���aoa=���bs2a"���bs2fsingle���bs2a"���`a,���`a
���`r                  ���`icbar_size���aoa=���bs2a"���bs2b10���bs2a%���bs2a"���`a,���`a
���`r                  ���`hcbar_pad���aoa=���bmfd0.05���`a,���`a
���`r                  ���`a)���`a
���`a
���`egrid2���`a[���bmia0���`a]���aoa.���`jset_xlabel���`a(���bs2a"���bs2aX���bs2a"���`a)���`a
���`egrid2���`a[���bmia0���`a]���aoa.���`jset_ylabel���`a(���bs2a"���bs2aY���bs2a"���`a)���`a
���`a
���`dvmax���`a,���`a ���`dvmin���`a ���aoa=���`a ���`bnp���aoa.���`cmax���`a(���`bZS���`a)���`a,���`a ���`bnp���aoa.���`cmin���`a(���`bZS���`a)���`a
���`dnorm���`a ���aoa=���`a ���`���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����aoa.���`fcolors���aoa.���`iNormalize���`a(���`dvmax���aoa=���`dvmax���`a,���`a ���`dvmin���aoa=���`dvmin���`a)���`a
���`a
���akcfor���`a ���`bax���`a,���`a ���`az���`a ���bowbin���`a ���bnbczip���`a(���`egrid2���`a,���`a ���`bZS���`a)���`a:���`a
���`d    ���`bim���`a ���aoa=���`a ���`bax���aoa.���`fimshow���`a(���`az���`a,���`a ���`dnorm���aoa=���`dnorm���`a,���`a ���`forigin���aoa=���bs2a"���bs2elower���bs2a"���`a,���`a ���`fextent���aoa=���`fextent���`a)���`a
���`a
���bc1xC# With cbar_mode="single", cax attribute of all axes are identical.���`a
���`bax���aoa.���`ccax���aoa.���`hcolorbar���`a(���`bim���`a)���`a
���`bax���aoa.���`ccax���aoa.���`ltoggle_label���`a(���bkcdTrue���`a)���`a
���`a
���akcfor���`a ���`bax���`a,���`a ���`him_title���`a ���bowbin���`a ���bnbczip���`a(���`egrid2���`a,���`a ���`a[���bs2a"���bs2c(a)���bs2a"���`a,���`a ���bs2a"���bs2c(b)���bs2a"���`a,���`a ���bs2a"���bs2c(c)���bs2a"���`a]���`a)���`a:���`a
���`d    ���`at���`a ���aoa=���`a ���`oadd_inner_title���`a(���`bax���`a,���`a ���`him_title���`a,���`a ���`cloc���aoa=���bs1a'���bs1jupper left���bs1a'���`a)���`a
���`d    ���`at���aoa.���`epatch���aoa.���`fset_ec���`a(���bs2a"���bs2dnone���bs2a"���`a)���`a
���`d    ���`at���aoa.���`epatch���aoa.���`iset_alpha���`a(���bmfc0.5���`a)���`a
���`a
���`egrid2���`a[���bmia0���`a]���aoa.���`jset_xticks���`a(���`a[���aoa-���bmia2���`a,���`a ���bmia0���`a]���`a)���`a
���`egrid2���`a[���bmia0���`a]���aoa.���`jset_yticks���`a(���`a[���aoa-���bmia2���`a,���`a ���bmia0���`a,���`a ���bmia2���`a]���`a)���`a
���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
`dNone�