��������d���bsdxS"""
========================
Anchored Direction Arrow
========================

"""���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���bkndfrom���`a ���bnnlmpl_toolkits���bnna.���bnnjaxes_grid1���bnna.���bnnpanchored_artists���`a ���bknfimport���`a ���`wAnchoredDirectionArrows���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnlfont_manager���`a ���akbas���`a ���bnnbfm���`a
���`a
���`a
���bc1x)# Fixing random state for reproducibility���`a
���`bnp���aoa.���`frandom���aoa.���`dseed���`a(���bmih19680801���`a)���`a
���`a
���`cfig���`a,���`a ���`bax���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`a)���`a
���`bax���aoa.���`fimshow���`a(���`bnp���aoa.���`frandom���aoa.���`frandom���`a(���`a(���bmib10���`a,���`a ���bmib10���`a)���`a)���`a)���`a
���`a
���bc1p# Simple example���`a
���`lsimple_arrow���`a ���aoa=���`a ���`wAnchoredDirectionArrows���`a(���`bax���aoa.���`itransAxes���`a,���`a ���bs1a'���bs1aX���bs1a'���`a,���`a ���bs1a'���bs1aY���bs1a'���`a)���`a
���`bax���aoa.���`jadd_artist���`a(���`lsimple_arrow���`a)���`a
���`a
���bc1u# High contrast arrow���`a
���`thigh_contrast_part_1���`a ���aoa=���`a ���`wAnchoredDirectionArrows���`a(���`a
���`x                            ���`bax���aoa.���`itransAxes���`a,���`a
���`x                            ���bs1a'���bs1c111���bs1a'���`a,���`a ���bsaar���bs1a'���bs1c11$���bs1a\���bs1hoverline���bsic{2}���bs1a$���bs1a'���`a,���`a
���`x                            ���`cloc���aoa=���bs1a'���bs1kupper right���bs1a'���`a,���`a
���`x                            ���`karrow_props���aoa=���`a{���bs1a'���bs1bec���bs1a'���`a:���`a ���bs1a'���bs1aw���bs1a'���`a,���`a ���bs1a'���bs1bfc���bs1a'���`a:���`a ���bs1a'���bs1dnone���bs1a'���`a,���`a ���bs1a'���bs1ealpha���bs1a'���`a:���`a ���bmia1���`a,���`a
���`x)                                         ���bs1a'���bs1blw���bs1a'���`a:���`a ���bmia2���`a}���`a
���`x                            ���`a)���`a
���`bax���aoa.���`jadd_artist���`a(���`thigh_contrast_part_1���`a)���`a
���`a
���`thigh_contrast_part_2���`a ���aoa=���`a ���`wAnchoredDirectionArrows���`a(���`a
���`x                            ���`bax���aoa.���`itransAxes���`a,���`a
���`x                            ���bs1a'���bs1c111���bs1a'���`a,���`a ���bsaar���bs1a'���bs1c11$���bs1a\���bs1hoverline���bsic{2}���bs1a$���bs1a'���`a,���`a
���`x                            ���`cloc���aoa=���bs1a'���bs1kupper right���bs1a'���`a,���`a
���`x                            ���`karrow_props���aoa=���`a{���bs1a'���bs1bec���bs1a'���`a:���`a ���bs1a'���bs1dnone���bs1a'���`a,���`a ���bs1a'���bs1bfc���bs1a'���`a:���`a ���bs1a'���bs1ak���bs1a'���`a}���`a,���`a
���`x                            ���`jtext_props���aoa=���`a{���bs1a'���bs1bec���bs1a'���`a:���`a ���bs1a'���bs1aw���bs1a'���`a,���`a ���bs1a'���bs1bfc���bs1a'���`a:���`a ���bs1a'���bs1ak���bs1a'���`a,���`a ���bs1a'���bs1blw���bs1a'���`a:���`a ���bmfc0.4���`a}���`a
���`x                            ���`a)���`a
���`bax���aoa.���`jadd_artist���`a(���`thigh_contrast_part_2���`a)���`a
���`a
���bc1o# Rotated arrow���`a
���`ifontprops���`a ���aoa=���`a ���`bfm���aoa.���`nFontProperties���`a(���`ffamily���aoa=���bs1a'���bs1eserif���bs1a'���`a)���`a
���`a
���`nroatated_arrow���`a ���aoa=���`a ���`wAnchoredDirectionArrows���`a(���`a
���`t                    ���`bax���aoa.���`itransAxes���`a,���`a
���`t                    ���bs1a'���bs1b30���bs1a'���`a,���`a ���bs1a'���bs1c120���bs1a'���`a,���`a
���`t                    ���`cloc���aoa=���bs1a'���bs1fcenter���bs1a'���`a,���`a
���`t                    ���`ecolor���aoa=���bs1a'���bs1aw���bs1a'���`a,���`a
���`t                    ���`eangle���aoa=���bmib30���`a,���`a
���`t                    ���`nfontproperties���aoa=���`ifontprops���`a
���`t                    ���`a)���`a
���`bax���aoa.���`jadd_artist���`a(���`nroatated_arrow���`a)���`a
���`a
���bc1x# Altering arrow directions���`a
���`ba1���`a ���aoa=���`a ���`wAnchoredDirectionArrows���`a(���`a
���`h        ���`bax���aoa.���`itransAxes���`a,���`a ���bs1a'���bs1aA���bs1a'���`a,���`a ���bs1a'���bs1aB���bs1a'���`a,���`a ���`cloc���aoa=���bs1a'���bs1llower center���bs1a'���`a,���`a
���`h        ���`flength���aoa=���aoa-���bmfd0.15���`a,���`a
���`h        ���`esep_x���aoa=���bmfd0.03���`a,���`a ���`esep_y���aoa=���bmfd0.03���`a,���`a
���`h        ���`ecolor���aoa=���bs1a'���bs1ar���bs1a'���`a
���`d    ���`a)���`a
���`bax���aoa.���`jadd_artist���`a(���`ba1���`a)���`a
���`a
���`ba2���`a ���aoa=���`a ���`wAnchoredDirectionArrows���`a(���`a
���`h        ���`bax���aoa.���`itransAxes���`a,���`a ���bs1a'���bs1aA���bs1a'���`a,���`a ���bs1a'���bs1b B���bs1a'���`a,���`a ���`cloc���aoa=���bs1a'���bs1jlower left���bs1a'���`a,���`a
���`h        ���`laspect_ratio���aoa=���aoa-���bmia1���`a,���`a
���`h        ���`esep_x���aoa=���bmfd0.01���`a,���`a ���`esep_y���aoa=���aoa-���bmfd0.02���`a,���`a
���`h        ���`ecolor���aoa=���bs1a'���bs1forange���bs1a'���`a
���`h        ���`a)���`a
���`bax���aoa.���`jadd_artist���`a(���`ba2���`a)���`a
���`a
���`a
���`ba3���`a ���aoa=���`a ���`wAnchoredDirectionArrows���`a(���`a
���`h        ���`bax���aoa.���`itransAxes���`a,���`a ���bs1a'���bs1b A���bs1a'���`a,���`a ���bs1a'���bs1aB���bs1a'���`a,���`a ���`cloc���aoa=���bs1a'���bs1klower right���bs1a'���`a,���`a
���`h        ���`flength���aoa=���aoa-���bmfd0.15���`a,���`a
���`h        ���`laspect_ratio���aoa=���aoa-���bmia1���`a,���`a
���`h        ���`esep_y���aoa=���aoa-���bmfc0.1���`a,���`a ���`esep_x���aoa=���bmfd0.04���`a,���`a
���`h        ���`ecolor���aoa=���bs1a'���bs1dcyan���bs1a'���`a
���`h        ���`a)���`a
���`bax���aoa.���`jadd_artist���`a(���`ba3���`a)���`a
���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
`dNone�