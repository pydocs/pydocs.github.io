������������bsdxt"""
===================================
Make Room For Ylabel Using Axesgrid
===================================

"""���`a
���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���`a
���bkndfrom���`a ���bnnlmpl_toolkits���bnna.���bnnjaxes_grid1���`a ���bknfimport���`a ���`smake_axes_locatable���`a
���bkndfrom���`a ���bnnlmpl_toolkits���bnna.���bnnjaxes_grid1���bnna.���bnnlaxes_divider���`a ���bknfimport���`a ���`xmake_axes_area_auto_adjustable���`a
���`a
���`a
���`cplt���aoa.���`ffigure���`a(���`a)���`a
���`bax���`a ���aoa=���`a ���`cplt���aoa.���`daxes���`a(���`a[���bmia0���`a,���`a ���bmia0���`a,���`a ���bmia1���`a,���`a ���bmia1���`a]���`a)���`a
���`a
���`bax���aoa.���`jset_yticks���`a(���`a[���bmfc0.5���`a]���`a,���`a ���`flabels���aoa=���`a[���bs2a"���bs2overy long label���bs2a"���`a]���`a)���`a
���`a
���`xmake_axes_area_auto_adjustable���`a(���`bax���`a)���`a
���`a
���bc1xO###############################################################################���`a
���`a
���`a
���`cplt���aoa.���`ffigure���`a(���`a)���`a
���`cax1���`a ���aoa=���`a ���`cplt���aoa.���`daxes���`a(���`a[���bmia0���`a,���`a ���bmia0���`a,���`a ���bmia1���`a,���`a ���bmfc0.5���`a]���`a)���`a
���`cax2���`a ���aoa=���`a ���`cplt���aoa.���`daxes���`a(���`a[���bmia0���`a,���`a ���bmfc0.5���`a,���`a ���bmia1���`a,���`a ���bmfc0.5���`a]���`a)���`a
���`a
���`cax1���aoa.���`jset_yticks���`a(���`a[���bmfc0.5���`a]���`a,���`a ���`flabels���aoa=���`a[���bs2a"���bs2overy long label���bs2a"���`a]���`a)���`a
���`cax1���aoa.���`jset_ylabel���`a(���bs2a"���bs2gY label���bs2a"���`a)���`a
���`a
���`cax2���aoa.���`iset_title���`a(���bs2a"���bs2eTitle���bs2a"���`a)���`a
���`a
���`xmake_axes_area_auto_adjustable���`a(���`cax1���`a,���`a ���`cpad���aoa=���bmfc0.1���`a,���`a ���`huse_axes���aoa=���`a[���`cax1���`a,���`a ���`cax2���`a]���`a)���`a
���`xmake_axes_area_auto_adjustable���`a(���`cax2���`a,���`a ���`cpad���aoa=���bmfc0.1���`a,���`a ���`huse_axes���aoa=���`a[���`cax1���`a,���`a ���`cax2���`a]���`a)���`a
���`a
���bc1xO###############################################################################���`a
���`a
���`a
���`cfig���`a ���aoa=���`a ���`cplt���aoa.���`ffigure���`a(���`a)���`a
���`cax1���`a ���aoa=���`a ���`cplt���aoa.���`daxes���`a(���`a[���bmia0���`a,���`a ���bmia0���`a,���`a ���bmia1���`a,���`a ���bmia1���`a]���`a)���`a
���`gdivider���`a ���aoa=���`a ���`smake_axes_locatable���`a(���`cax1���`a)���`a
���`a
���`cax2���`a ���aoa=���`a ���`gdivider���aoa.���`nnew_horizontal���`a(���bs2a"���bs2c100���bs2a%���bs2a"���`a,���`a ���`cpad���aoa=���bmfc0.3���`a,���`a ���`fsharey���aoa=���`cax1���`a)���`a
���`cax2���aoa.���`ktick_params���`a(���`ilabelleft���aoa=���bkceFalse���`a)���`a
���`cfig���aoa.���`hadd_axes���`a(���`cax2���`a)���`a
���`a
���`gdivider���aoa.���`xadd_auto_adjustable_area���`a(���`huse_axes���aoa=���`a[���`cax1���`a]���`a,���`a ���`cpad���aoa=���bmfc0.1���`a,���`a
���`x!                                 ���`kadjust_dirs���aoa=���`a[���bs2a"���bs2dleft���bs2a"���`a]���`a)���`a
���`gdivider���aoa.���`xadd_auto_adjustable_area���`a(���`huse_axes���aoa=���`a[���`cax2���`a]���`a,���`a ���`cpad���aoa=���bmfc0.1���`a,���`a
���`x!                                 ���`kadjust_dirs���aoa=���`a[���bs2a"���bs2eright���bs2a"���`a]���`a)���`a
���`gdivider���aoa.���`xadd_auto_adjustable_area���`a(���`huse_axes���aoa=���`a[���`cax1���`a,���`a ���`cax2���`a]���`a,���`a ���`cpad���aoa=���bmfc0.1���`a,���`a
���`x!                                 ���`kadjust_dirs���aoa=���`a[���bs2a"���bs2ctop���bs2a"���`a,���`a ���bs2a"���bs2fbottom���bs2a"���`a]���`a)���`a
���`a
���`cax1���aoa.���`jset_yticks���`a(���`a[���bmfc0.5���`a]���`a,���`a ���`flabels���aoa=���`a[���bs2a"���bs2overy long label���bs2a"���`a]���`a)���`a
���`a
���`cax2���aoa.���`iset_title���`a(���bs2a"���bs2eTitle���bs2a"���`a)���`a
���`cax2���aoa.���`jset_xlabel���`a(���bs2a"���bs2iX - Label���bs2a"���`a)���`a
���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
`dNone�