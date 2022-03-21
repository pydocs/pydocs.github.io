��������k���bsdy"""
==================================
Showing RGB channels using RGBAxes
==================================

`~.axes_grid1.axes_rgb.RGBAxes` creates a layout of 4 Axes for displaying RGB
channels: one large Axes for the RGB image and 3 smaller Axes for the R, G, B
channels.
"""���`a
���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���bkndfrom���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����`a ���bknfimport���`a ���`ecbook���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���bkndfrom���`a ���bnnlmpl_toolkits���bnna.���bnnjaxes_grid1���bnna.���bnnhaxes_rgb���`a ���bknfimport���`a ���`mmake_rgb_axes���`a,���`a ���`gRGBAxes���`a
���`a
���`a
���akcdef���`a ���bnfgget_rgb���`a(���`a)���`a:���`a
���`d    ���`aZ���`a ���aoa=���`a ���`ecbook���aoa.���`oget_sample_data���`a(���bs2a"���bs2xaxes_grid/bivariate_normal.npy���bs2a"���`a,���`a ���`gnp_load���aoa=���bkcdTrue���`a)���`a
���`d    ���`aZ���`a[���`aZ���`a ���aoa<���`a ���bmia0���`a]���`a ���aoa=���`a ���bmfb0.���`a
���`d    ���`aZ���`a ���aoa=���`a ���`aZ���`a ���aoa/���`a ���`aZ���aoa.���`cmax���`a(���`a)���`a
���`a
���`d    ���`aR���`a ���aoa=���`a ���`aZ���`a[���`a:���bmib13���`a,���`a ���`a:���bmib13���`a]���`a
���`d    ���`aG���`a ���aoa=���`a ���`aZ���`a[���bmia2���`a:���`a,���`a ���bmia2���`a:���`a]���`a
���`d    ���`aB���`a ���aoa=���`a ���`aZ���`a[���`a:���bmib13���`a,���`a ���bmia2���`a:���`a]���`a
���`a
���`d    ���akfreturn���`a ���`aR���`a,���`a ���`aG���`a,���`a ���`aB���`a
���`a
���`a
���akcdef���`a ���bnfimake_cube���`a(���`ar���`a,���`a ���`ag���`a,���`a ���`ab���`a)���`a:���`a
���`d    ���`bny���`a,���`a ���`bnx���`a ���aoa=���`a ���`ar���aoa.���`eshape���`a
���`d    ���`aR���`a ���aoa=���`a ���`bnp���aoa.���`ezeros���`a(���`a(���`bny���`a,���`a ���`bnx���`a,���`a ���bmia3���`a)���`a)���`a
���`d    ���`aR���`a[���`a:���`a,���`a ���`a:���`a,���`a ���bmia0���`a]���`a ���aoa=���`a ���`ar���`a
���`d    ���`aG���`a ���aoa=���`a ���`bnp���aoa.���`jzeros_like���`a(���`aR���`a)���`a
���`d    ���`aG���`a[���`a:���`a,���`a ���`a:���`a,���`a ���bmia1���`a]���`a ���aoa=���`a ���`ag���`a
���`d    ���`aB���`a ���aoa=���`a ���`bnp���aoa.���`jzeros_like���`a(���`aR���`a)���`a
���`d    ���`aB���`a[���`a:���`a,���`a ���`a:���`a,���`a ���bmia2���`a]���`a ���aoa=���`a ���`ab���`a
���`a
���`d    ���`cRGB���`a ���aoa=���`a ���`aR���`a ���aoa+���`a ���`aG���`a ���aoa+���`a ���`aB���`a
���`a
���`d    ���akfreturn���`a ���`aR���`a,���`a ���`aG���`a,���`a ���`aB���`a,���`a ���`cRGB���`a
���`a
���`a
���akcdef���`a ���bnfidemo_rgb1���`a(���`a)���`a:���`a
���`d    ���`cfig���`a ���aoa=���`a ���`cplt���aoa.���`ffigure���`a(���`a)���`a
���`d    ���`bax���`a ���aoa=���`a ���`gRGBAxes���`a(���`cfig���`a,���`a ���`a[���bmfc0.1���`a,���`a ���bmfc0.1���`a,���`a ���bmfc0.8���`a,���`a ���bmfc0.8���`a]���`a,���`a ���`cpad���aoa=���bmfc0.0���`a)���`a
���`d    ���`ar���`a,���`a ���`ag���`a,���`a ���`ab���`a ���aoa=���`a ���`gget_rgb���`a(���`a)���`a
���`d    ���`bax���aoa.���`jimshow_rgb���`a(���`ar���`a,���`a ���`ag���`a,���`a ���`ab���`a)���`a
���`a
���`a
���akcdef���`a ���bnfidemo_rgb2���`a(���`a)���`a:���`a
���`d    ���`cfig���`a,���`a ���`bax���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`a)���`a
���`d    ���`dax_r���`a,���`a ���`dax_g���`a,���`a ���`dax_b���`a ���aoa=���`a ���`mmake_rgb_axes���`a(���`bax���`a,���`a ���`cpad���aoa=���bmfd0.02���`a)���`a
���`a
���`d    ���`ar���`a,���`a ���`ag���`a,���`a ���`ab���`a ���aoa=���`a ���`gget_rgb���`a(���`a)���`a
���`d    ���`dim_r���`a,���`a ���`dim_g���`a,���`a ���`dim_b���`a,���`a ���`fim_rgb���`a ���aoa=���`a ���`imake_cube���`a(���`ar���`a,���`a ���`ag���`a,���`a ���`ab���`a)���`a
���`d    ���`bax���aoa.���`fimshow���`a(���`fim_rgb���`a)���`a
���`d    ���`dax_r���aoa.���`fimshow���`a(���`dim_r���`a)���`a
���`d    ���`dax_g���aoa.���`fimshow���`a(���`dim_g���`a)���`a
���`d    ���`dax_b���aoa.���`fimshow���`a(���`dim_b���`a)���`a
���`a
���`d    ���akcfor���`a ���`bax���`a ���bowbin���`a ���`cfig���aoa.���`daxes���`a:���`a
���`h        ���`bax���aoa.���`ktick_params���`a(���`daxis���aoa=���bs1a'���bs1dboth���bs1a'���`a,���`a ���`idirection���aoa=���bs1a'���bs1bin���bs1a'���`a)���`a
���`h        ���`bax���aoa.���`fspines���`a[���`a:���`a]���aoa.���`iset_color���`a(���bs2a"���bs2aw���bs2a"���`a)���`a
���`h        ���akcfor���`a ���`dtick���`a ���bowbin���`a ���`bax���aoa.���`exaxis���aoa.���`oget_major_ticks���`a(���`a)���`a ���aoa+���`a ���`bax���aoa.���`eyaxis���aoa.���`oget_major_ticks���`a(���`a)���`a:���`a
���`l            ���`dtick���aoa.���`itick1line���aoa.���`sset_markeredgecolor���`a(���bs2a"���bs2aw���bs2a"���`a)���`a
���`l            ���`dtick���aoa.���`itick2line���aoa.���`sset_markeredgecolor���`a(���bs2a"���bs2aw���bs2a"���`a)���`a
���`a
���`a
���`idemo_rgb1���`a(���`a)���`a
���`idemo_rgb2���`a(���`a)���`a
���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
`dNone�