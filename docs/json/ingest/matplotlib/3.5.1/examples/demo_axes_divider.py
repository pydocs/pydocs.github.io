��������}���bsdx�"""
============
Axes Divider
============

Axes divider to calculate location of axes and
create a divider for them using existing axes instances.
"""���`a
���`a
���bkndfrom���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����`a ���bknfimport���`a ���`ecbook���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���`a
���`a
���akcdef���`a ���bnfnget_demo_image���`a(���`a)���`a:���`a
���`d    ���`az���`a ���aoa=���`a ���`ecbook���aoa.���`oget_sample_data���`a(���bs2a"���bs2xaxes_grid/bivariate_normal.npy���bs2a"���`a,���`a ���`gnp_load���aoa=���bkcdTrue���`a)���`a
���`d    ���bc1x# z is a numpy array of 15x15���`a
���`d    ���akfreturn���`a ���`az���`a,���`a ���`a(���aoa-���bmia3���`a,���`a ���bmia4���`a,���`a ���aoa-���bmia4���`a,���`a ���bmia3���`a)���`a
���`a
���`a
���akcdef���`a ���bnfqdemo_simple_image���`a(���`bax���`a)���`a:���`a
���`d    ���`aZ���`a,���`a ���`fextent���`a ���aoa=���`a ���`nget_demo_image���`a(���`a)���`a
���`a
���`d    ���`bim���`a ���aoa=���`a ���`bax���aoa.���`fimshow���`a(���`aZ���`a,���`a ���`fextent���aoa=���`fextent���`a)���`a
���`d    ���`bcb���`a ���aoa=���`a ���`cplt���aoa.���`hcolorbar���`a(���`bim���`a)���`a
���`d    ���`bcb���aoa.���`bax���aoa.���`eyaxis���aoa.���`oset_tick_params���`a(���`jlabelright���aoa=���bkceFalse���`a)���`a
���`a
���`a
���akcdef���`a ���bnfxdemo_locatable_axes_hard���`a(���`cfig���`a)���`a:���`a
���`a
���`d    ���bkndfrom���`a ���bnnlmpl_toolkits���bnna.���bnnjaxes_grid1���`a ���bknfimport���`a ���`nSubplotDivider���`a,���`a ���`dSize���`a
���`d    ���bkndfrom���`a ���bnnlmpl_toolkits���bnna.���bnnjaxes_grid1���bnna.���bnnhmpl_axes���`a ���bknfimport���`a ���`dAxes���`a
���`a
���`d    ���`gdivider���`a ���aoa=���`a ���`nSubplotDivider���`a(���`cfig���`a,���`a ���bmia2���`a,���`a ���bmia2���`a,���`a ���bmia2���`a,���`a ���`faspect���aoa=���bkcdTrue���`a)���`a
���`a
���`d    ���bc1p# axes for image���`a
���`d    ���`bax���`a ���aoa=���`a ���`cfig���aoa.���`hadd_axes���`a(���`gdivider���aoa.���`lget_position���`a(���`a)���`a,���`a ���`jaxes_class���aoa=���`dAxes���`a)���`a
���`a
���`d    ���bc1s# axes for colorbar���`a
���`d    ���bc1xK# (the label prevents Axes.add_axes from incorrectly believing that the two���`a
���`d    ���bc1t# axes are the same)���`a
���`d    ���`eax_cb���`a ���aoa=���`a ���`cfig���aoa.���`hadd_axes���`a(���`gdivider���aoa.���`lget_position���`a(���`a)���`a,���`a ���`jaxes_class���aoa=���`dAxes���`a,���`a ���`elabel���aoa=���bs2a"���bs2bcb���bs2a"���`a)���`a
���`a
���`d    ���`ah���`a ���aoa=���`a ���`a[���`dSize���aoa.���`eAxesX���`a(���`bax���`a)���`a,���`b  ���bc1k# main axes���`a
���`i         ���`dSize���aoa.���`eFixed���`a(���bmfd0.05���`a)���`a,���`b  ���bc1s# padding, 0.1 inch���`a
���`i         ���`dSize���aoa.���`eFixed���`a(���bmfc0.2���`a)���`a,���`b  ���bc1t# colorbar, 0.3 inch���`a
���`i         ���`a]���`a
���`a
���`d    ���`av���`a ���aoa=���`a ���`a[���`dSize���aoa.���`eAxesY���`a(���`bax���`a)���`a]���`a
���`a
���`d    ���`gdivider���aoa.���`nset_horizontal���`a(���`ah���`a)���`a
���`d    ���`gdivider���aoa.���`lset_vertical���`a(���`av���`a)���`a
���`a
���`d    ���`bax���aoa.���`pset_axes_locator���`a(���`gdivider���aoa.���`knew_locator���`a(���`bnx���aoa=���bmia0���`a,���`a ���`bny���aoa=���bmia0���`a)���`a)���`a
���`d    ���`eax_cb���aoa.���`pset_axes_locator���`a(���`gdivider���aoa.���`knew_locator���`a(���`bnx���aoa=���bmia2���`a,���`a ���`bny���aoa=���bmia0���`a)���`a)���`a
���`a
���`d    ���`eax_cb���aoa.���`daxis���`a[���bs2a"���bs2dleft���bs2a"���`a]���aoa.���`ftoggle���`a(���bnbcall���aoa=���bkceFalse���`a)���`a
���`d    ���`eax_cb���aoa.���`daxis���`a[���bs2a"���bs2eright���bs2a"���`a]���aoa.���`ftoggle���`a(���`eticks���aoa=���bkcdTrue���`a)���`a
���`a
���`d    ���`aZ���`a,���`a ���`fextent���`a ���aoa=���`a ���`nget_demo_image���`a(���`a)���`a
���`a
���`d    ���`bim���`a ���aoa=���`a ���`bax���aoa.���`fimshow���`a(���`aZ���`a,���`a ���`fextent���aoa=���`fextent���`a)���`a
���`d    ���`cplt���aoa.���`hcolorbar���`a(���`bim���`a,���`a ���`ccax���aoa=���`eax_cb���`a)���`a
���`d    ���`eax_cb���aoa.���`eyaxis���aoa.���`oset_tick_params���`a(���`jlabelright���aoa=���bkceFalse���`a)���`a
���`a
���`a
���akcdef���`a ���bnfxdemo_locatable_axes_easy���`a(���`bax���`a)���`a:���`a
���`d    ���bkndfrom���`a ���bnnlmpl_toolkits���bnna.���bnnjaxes_grid1���`a ���bknfimport���`a ���`smake_axes_locatable���`a
���`a
���`d    ���`gdivider���`a ���aoa=���`a ���`smake_axes_locatable���`a(���`bax���`a)���`a
���`a
���`d    ���`eax_cb���`a ���aoa=���`a ���`gdivider���aoa.���`nnew_horizontal���`a(���`dsize���aoa=���bs2a"���bs2a5���bs2a%���bs2a"���`a,���`a ���`cpad���aoa=���bmfd0.05���`a)���`a
���`d    ���`cfig���`a ���aoa=���`a ���`bax���aoa.���`jget_figure���`a(���`a)���`a
���`d    ���`cfig���aoa.���`hadd_axes���`a(���`eax_cb���`a)���`a
���`a
���`d    ���`aZ���`a,���`a ���`fextent���`a ���aoa=���`a ���`nget_demo_image���`a(���`a)���`a
���`d    ���`bim���`a ���aoa=���`a ���`bax���aoa.���`fimshow���`a(���`aZ���`a,���`a ���`fextent���aoa=���`fextent���`a)���`a
���`a
���`d    ���`cplt���aoa.���`hcolorbar���`a(���`bim���`a,���`a ���`ccax���aoa=���`eax_cb���`a)���`a
���`d    ���`eax_cb���aoa.���`eyaxis���aoa.���`jtick_right���`a(���`a)���`a
���`d    ���`eax_cb���aoa.���`eyaxis���aoa.���`oset_tick_params���`a(���`jlabelright���aoa=���bkceFalse���`a)���`a
���`a
���`a
���akcdef���`a ���bnfxdemo_images_side_by_side���`a(���`bax���`a)���`a:���`a
���`d    ���bkndfrom���`a ���bnnlmpl_toolkits���bnna.���bnnjaxes_grid1���`a ���bknfimport���`a ���`smake_axes_locatable���`a
���`a
���`d    ���`gdivider���`a ���aoa=���`a ���`smake_axes_locatable���`a(���`bax���`a)���`a
���`a
���`d    ���`aZ���`a,���`a ���`fextent���`a ���aoa=���`a ���`nget_demo_image���`a(���`a)���`a
���`d    ���`cax2���`a ���aoa=���`a ���`gdivider���aoa.���`nnew_horizontal���`a(���`dsize���aoa=���bs2a"���bs2c100���bs2a%���bs2a"���`a,���`a ���`cpad���aoa=���bmfd0.05���`a)���`a
���`d    ���`dfig1���`a ���aoa=���`a ���`bax���aoa.���`jget_figure���`a(���`a)���`a
���`d    ���`dfig1���aoa.���`hadd_axes���`a(���`cax2���`a)���`a
���`a
���`d    ���`bax���aoa.���`fimshow���`a(���`aZ���`a,���`a ���`fextent���aoa=���`fextent���`a)���`a
���`d    ���`cax2���aoa.���`fimshow���`a(���`aZ���`a,���`a ���`fextent���aoa=���`fextent���`a)���`a
���`d    ���`cax2���aoa.���`eyaxis���aoa.���`oset_tick_params���`a(���`ilabelleft���aoa=���bkceFalse���`a)���`a
���`a
���`a
���akcdef���`a ���bnfddemo���`a(���`a)���`a:���`a
���`a
���`d    ���`cfig���`a ���aoa=���`a ���`cplt���aoa.���`ffigure���`a(���`gfigsize���aoa=���`a(���bmia6���`a,���`a ���bmia6���`a)���`a)���`a
���`a
���`d    ���bc1h# PLOT 1���`a
���`d    ���bc1x# simple image & colorbar���`a
���`d    ���`bax���`a ���aoa=���`a ���`cfig���aoa.���`kadd_subplot���`a(���bmia2���`a,���`a ���bmia2���`a,���`a ���bmia1���`a)���`a
���`d    ���`qdemo_simple_image���`a(���`bax���`a)���`a
���`a
���`d    ���bc1h# PLOT 2���`a
���`d    ���bc1xD# image and colorbar whose location is adjusted in the drawing time.���`a
���`d    ���bc1l# a hard way���`a
���`a
���`d    ���`xdemo_locatable_axes_hard���`a(���`cfig���`a)���`a
���`a
���`d    ���bc1h# PLOT 3���`a
���`d    ���bc1xD# image and colorbar whose location is adjusted in the drawing time.���`a
���`d    ���bc1l# a easy way���`a
���`a
���`d    ���`bax���`a ���aoa=���`a ���`cfig���aoa.���`kadd_subplot���`a(���bmia2���`a,���`a ���bmia2���`a,���`a ���bmia3���`a)���`a
���`d    ���`xdemo_locatable_axes_easy���`a(���`bax���`a)���`a
���`a
���`d    ���bc1h# PLOT 4���`a
���`d    ���bc1x-# two images side by side with fixed padding.���`a
���`a
���`d    ���`bax���`a ���aoa=���`a ���`cfig���aoa.���`kadd_subplot���`a(���bmia2���`a,���`a ���bmia2���`a,���`a ���bmia4���`a)���`a
���`d    ���`xdemo_images_side_by_side���`a(���`bax���`a)���`a
���`a
���`d    ���`cplt���aoa.���`dshow���`a(���`a)���`a
���`a
���`a
���`ddemo���`a(���`a)���`a
`dNone�