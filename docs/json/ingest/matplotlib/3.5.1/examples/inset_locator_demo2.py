��������=���bsdy("""
===================
Inset Locator Demo2
===================

This Demo shows how to create a zoomed inset via `.zoomed_inset_axes`.
In the first subplot an `.AnchoredSizeBar` shows the zoom effect.
In the second subplot a connection to the region of interest is
created via `.mark_inset`.
"""���`a
���`a
���bkndfrom���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����`a ���bknfimport���`a ���`ecbook���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���bkndfrom���`a ���bnnlmpl_toolkits���bnna.���bnnjaxes_grid1���bnna.���bnnminset_locator���`a ���bknfimport���`a ���`qzoomed_inset_axes���`a,���`a ���`jmark_inset���`a
���bkndfrom���`a ���bnnlmpl_toolkits���bnna.���bnnjaxes_grid1���bnna.���bnnpanchored_artists���`a ���bknfimport���`a ���`oAnchoredSizeBar���`a
���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���`a
���`a
���akcdef���`a ���bnfnget_demo_image���`a(���`a)���`a:���`a
���`d    ���`az���`a ���aoa=���`a ���`ecbook���aoa.���`oget_sample_data���`a(���bs2a"���bs2xaxes_grid/bivariate_normal.npy���bs2a"���`a,���`a ���`gnp_load���aoa=���bkcdTrue���`a)���`a
���`d    ���bc1x# z is a numpy array of 15x15���`a
���`d    ���akfreturn���`a ���`az���`a,���`a ���`a(���aoa-���bmia3���`a,���`a ���bmia4���`a,���`a ���aoa-���bmia4���`a,���`a ���bmia3���`a)���`a
���`a
���`cfig���`a,���`a ���`a(���`bax���`a,���`a ���`cax2���`a)���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`encols���aoa=���bmia2���`a,���`a ���`gfigsize���aoa=���`a[���bmia6���`a,���`a ���bmia3���`a]���`a)���`a
���`a
���`a
���bc1x2# First subplot, showing an inset with a size bar.���`a
���`bax���aoa.���`jset_aspect���`a(���bmia1���`a)���`a
���`a
���`eaxins���`a ���aoa=���`a ���`qzoomed_inset_axes���`a(���`bax���`a,���`a ���`dzoom���aoa=���bmfc0.5���`a,���`a ���`cloc���aoa=���bs1a'���bs1kupper right���bs1a'���`a)���`a
���bc1x+# fix the number of ticks on the inset axes���`a
���`eaxins���aoa.���`eyaxis���aoa.���`qget_major_locator���`a(���`a)���aoa.���`jset_params���`a(���`enbins���aoa=���bmia7���`a)���`a
���`eaxins���aoa.���`exaxis���aoa.���`qget_major_locator���`a(���`a)���aoa.���`jset_params���`a(���`enbins���aoa=���bmia7���`a)���`a
���`eaxins���aoa.���`ktick_params���`a(���`ilabelleft���aoa=���bkceFalse���`a,���`a ���`klabelbottom���aoa=���bkceFalse���`a)���`a
���`a
���`a
���akcdef���`a ���bnfkadd_sizebar���`a(���`bax���`a,���`a ���`dsize���`a)���`a:���`a
���`d    ���`casb���`a ���aoa=���`a ���`oAnchoredSizeBar���`a(���`bax���aoa.���`itransData���`a,���`a
���`x                          ���`dsize���`a,���`a
���`x                          ���bnbcstr���`a(���`dsize���`a)���`a,���`a
���`x                          ���`cloc���aoa=���bmia8���`a,���`a
���`x                          ���`cpad���aoa=���bmfc0.1���`a,���`a ���`iborderpad���aoa=���bmfc0.5���`a,���`a ���`csep���aoa=���bmia5���`a,���`a
���`x                          ���`gframeon���aoa=���bkceFalse���`a)���`a
���`d    ���`bax���aoa.���`jadd_artist���`a(���`casb���`a)���`a
���`a
���`kadd_sizebar���`a(���`bax���`a,���`a ���bmfc0.5���`a)���`a
���`kadd_sizebar���`a(���`eaxins���`a,���`a ���bmfc0.5���`a)���`a
���`a
���`a
���bc1x5# Second subplot, showing an image with an inset zoom���`a
���bc1t# and a marked inset���`a
���`aZ���`a,���`a ���`fextent���`a ���aoa=���`a ���`nget_demo_image���`a(���`a)���`a
���`bZ2���`a ���aoa=���`a ���`bnp���aoa.���`ezeros���`a(���`a(���bmic150���`a,���`a ���bmic150���`a)���`a)���`a
���`bny���`a,���`a ���`bnx���`a ���aoa=���`a ���`aZ���aoa.���`eshape���`a
���`bZ2���`a[���bmib30���`a:���bmib30���aoa+���`bny���`a,���`a ���bmib30���`a:���bmib30���aoa+���`bnx���`a]���`a ���aoa=���`a ���`aZ���`a
���`a
���`cax2���aoa.���`fimshow���`a(���`bZ2���`a,���`a ���`fextent���aoa=���`fextent���`a,���`a ���`forigin���aoa=���bs2a"���bs2elower���bs2a"���`a)���`a
���`a
���`faxins2���`a ���aoa=���`a ���`qzoomed_inset_axes���`a(���`cax2���`a,���`a ���`dzoom���aoa=���bmia6���`a,���`a ���`cloc���aoa=���bmia1���`a)���`a
���`faxins2���aoa.���`fimshow���`a(���`bZ2���`a,���`a ���`fextent���aoa=���`fextent���`a,���`a ���`forigin���aoa=���bs2a"���bs2elower���bs2a"���`a)���`a
���`a
���bc1x"# sub region of the original image���`a
���`bx1���`a,���`a ���`bx2���`a,���`a ���`by1���`a,���`a ���`by2���`a ���aoa=���`a ���aoa-���bmfc1.5���`a,���`a ���aoa-���bmfc0.9���`a,���`a ���aoa-���bmfc2.5���`a,���`a ���aoa-���bmfc1.9���`a
���`faxins2���aoa.���`hset_xlim���`a(���`bx1���`a,���`a ���`bx2���`a)���`a
���`faxins2���aoa.���`hset_ylim���`a(���`by1���`a,���`a ���`by2���`a)���`a
���bc1x+# fix the number of ticks on the inset axes���`a
���`faxins2���aoa.���`eyaxis���aoa.���`qget_major_locator���`a(���`a)���aoa.���`jset_params���`a(���`enbins���aoa=���bmia7���`a)���`a
���`faxins2���aoa.���`exaxis���aoa.���`qget_major_locator���`a(���`a)���aoa.���`jset_params���`a(���`enbins���aoa=���bmia7���`a)���`a
���`faxins2���aoa.���`ktick_params���`a(���`ilabelleft���aoa=���bkceFalse���`a,���`a ���`klabelbottom���aoa=���bkceFalse���`a)���`a
���`a
���bc1xD# draw a bbox of the region of the inset axes in the parent axes and���`a
���bc1x;# connecting lines between the bbox and the inset axes area���`a
���`jmark_inset���`a(���`cax2���`a,���`a ���`faxins2���`a,���`a ���`dloc1���aoa=���bmia2���`a,���`a ���`dloc2���aoa=���bmia4���`a,���`a ���`bfc���aoa=���bs2a"���bs2dnone���bs2a"���`a,���`a ���`bec���aoa=���bs2a"���bs2c0.5���bs2a"���`a)���`a
���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
`dNone�