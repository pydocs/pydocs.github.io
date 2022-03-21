�����������bsdx�"""
========
Dolphins
========

This example shows how to draw, and manipulate shapes given vertices
and nodes using the `~.path.Path`, `~.patches.PathPatch` and
`~matplotlib.transforms` classes.
"""���`a
���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnbcm���`a ���akbas���`a ���bnnbcm���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���bkndfrom���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnngpatches���`a ���bknfimport���`a ���`fCircle���`a,���`a ���`iPathPatch���`a
���bkndfrom���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnndpath���`a ���bknfimport���`a ���`dPath���`a
���bkndfrom���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnjtransforms���`a ���bknfimport���`a ���`hAffine2D���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���`a
���bc1x)# Fixing random state for reproducibility���`a
���`bnp���aoa.���`frandom���aoa.���`dseed���`a(���bmih19680801���`a)���`a
���`a
���`a
���`ar���`a ���aoa=���`a ���`bnp���aoa.���`frandom���aoa.���`drand���`a(���bmib50���`a)���`a
���`at���`a ���aoa=���`a ���`bnp���aoa.���`frandom���aoa.���`drand���`a(���bmib50���`a)���`a ���aoa*���`a ���`bnp���aoa.���`bpi���`a ���aoa*���`a ���bmfc2.0���`a
���`ax���`a ���aoa=���`a ���`ar���`a ���aoa*���`a ���`bnp���aoa.���`ccos���`a(���`at���`a)���`a
���`ay���`a ���aoa=���`a ���`ar���`a ���aoa*���`a ���`bnp���aoa.���`csin���`a(���`at���`a)���`a
���`a
���`cfig���`a,���`a ���`bax���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`gfigsize���aoa=���`a(���bmia6���`a,���`a ���bmia6���`a)���`a)���`a
���`fcircle���`a ���aoa=���`a ���`fCircle���`a(���`a(���bmia0���`a,���`a ���bmia0���`a)���`a,���`a ���bmia1���`a,���`a ���`ifacecolor���aoa=���bs1a'���bs1dnone���bs1a'���`a,���`a
���`p                ���`iedgecolor���aoa=���`a(���bmia0���`a,���`a ���bmfc0.8���`a,���`a ���bmfc0.8���`a)���`a,���`a ���`ilinewidth���aoa=���bmia3���`a,���`a ���`ealpha���aoa=���bmfc0.5���`a)���`a
���`bax���aoa.���`iadd_patch���`a(���`fcircle���`a)���`a
���`a
���`bim���`a ���aoa=���`a ���`cplt���aoa.���`fimshow���`a(���`bnp���aoa.���`frandom���aoa.���`frandom���`a(���`a(���bmic100���`a,���`a ���bmic100���`a)���`a)���`a,���`a
���`p                ���`forigin���aoa=���bs1a'���bs1elower���bs1a'���`a,���`a ���`dcmap���aoa=���`bcm���aoa.���`fwinter���`a,���`a
���`p                ���`minterpolation���aoa=���bs1a'���bs1hspline36���bs1a'���`a,���`a
���`p                ���`fextent���aoa=���`a(���`a[���aoa-���bmia1���`a,���`a ���bmia1���`a,���`a ���aoa-���bmia1���`a,���`a ���bmia1���`a]���`a)���`a)���`a
���`bim���aoa.���`mset_clip_path���`a(���`fcircle���`a)���`a
���`a
���`cplt���aoa.���`dplot���`a(���`ax���`a,���`a ���`ay���`a,���`a ���bs1a'���bs1ao���bs1a'���`a,���`a ���`ecolor���aoa=���`a(���bmfc0.9���`a,���`a ���bmfc0.9���`a,���`a ���bmfc1.0���`a)���`a,���`a ���`ealpha���aoa=���bmfc0.8���`a)���`a
���`a
���bc1x4# Dolphin from OpenClipart library by Andy Fitzsimon���`a
���bc1xD#   <cc:License rdf:about="http://web.resource.org/cc/PublicDomain">���`a
���bc1xJ#     <cc:permits rdf:resource="http://web.resource.org/cc/Reproduction"/>���`a
���bc1xJ#     <cc:permits rdf:resource="http://web.resource.org/cc/Distribution"/>���`a
���bc1xM#     <cc:permits rdf:resource="http://web.resource.org/cc/DerivativeWorks"/>���`a
���bc1q#   </cc:License>���`a
���`a
���`gdolphin���`a ���aoa=���`a ���bs2c"""���bs2a
���bs2xEM -0.59739425,160.18173 C -0.62740401,160.18885 -0.57867129,160.11183���bs2a
���bs2xB-0.57867129,160.11183 C -0.57867129,160.11183 -0.5438361,159.89315���bs2a
���bs2xC-0.39514638,159.81496 C -0.24645668,159.73678 -0.18316813,159.71981���bs2a
���bs2xC-0.18316813,159.71981 C -0.18316813,159.71981 -0.10322971,159.58124���bs2a
���bs2xF-0.057804323,159.58725 C -0.029723983,159.58913 -0.061841603,159.60356���bs2a
���bs2xF-0.071265813,159.62815 C -0.080250183,159.65325 -0.082918513,159.70554���bs2a
���bs2xF-0.061841203,159.71248 C -0.040763903,159.7194 -0.0066711426,159.71091���bs2a
���bs2xA0.077336307,159.73612 C 0.16879567,159.76377 0.28380306,159.86448���bs2a
���bs2x=0.31516668,159.91533 C 0.3465303,159.96618 0.5011127,160.1771���bs2a
���bs2x>0.5011127,160.1771 C 0.63668998,160.19238 0.67763022,160.31259���bs2a
���bs2x@0.66556395,160.32668 C 0.65339985,160.34212 0.66350443,160.33642���bs2a
���bs2x>0.64907098,160.33088 C 0.63463742,160.32533 0.61309688,160.297���bs2a
���bs2x?0.5789627,160.29339 C 0.54348657,160.28968 0.52329693,160.27674���bs2a
���bs2x@0.50728856,160.27737 C 0.49060916,160.27795 0.48965803,160.31565���bs2a
���bs2x?0.46114204,160.33673 C 0.43329696,160.35786 0.4570711,160.39871���bs2a
���bs2x?0.43309565,160.40685 C 0.4105108,160.41442 0.39416631,160.33027���bs2a
���bs2x>0.3954995,160.2935 C 0.39683269,160.25672 0.43807996,160.21522���bs2a
���bs2x?0.44567915,160.19734 C 0.45327833,160.17946 0.27946869,159.9424���bs2a
���bs2xD-0.061852613,159.99845 C -0.083965233,160.0427 -0.26176109,160.06683���bs2a
���bs2xC-0.26176109,160.06683 C -0.30127962,160.07028 -0.21167141,160.09731���bs2a
���bs2xB-0.24649368,160.1011 C -0.32642366,160.11569 -0.34521187,160.06895���bs2a
���bs2x@-0.40622293,160.0819 C -0.467234,160.09485 -0.56738444,160.17461���bs2a
���bs2u-0.59739425,160.18173���bs2a
���bs2c"""���`a
���`a
���`hvertices���`a ���aoa=���`a ���`a[���`a]���`a
���`ecodes���`a ���aoa=���`a ���`a[���`a]���`a
���`eparts���`a ���aoa=���`a ���`gdolphin���aoa.���`esplit���`a(���`a)���`a
���`ai���`a ���aoa=���`a ���bmia0���`a
���`hcode_map���`a ���aoa=���`a ���`a{���`a
���`d    ���bs1a'���bs1aM���bs1a'���`a:���`a ���`dPath���aoa.���`fMOVETO���`a,���`a
���`d    ���bs1a'���bs1aC���bs1a'���`a:���`a ���`dPath���aoa.���`fCURVE4���`a,���`a
���`d    ���bs1a'���bs1aL���bs1a'���`a:���`a ���`dPath���aoa.���`fLINETO���`a,���`a
���`a}���`a
���`a
���akewhile���`a ���`ai���`a ���aoa<���`a ���bnbclen���`a(���`eparts���`a)���`a:���`a
���`d    ���`ipath_code���`a ���aoa=���`a ���`hcode_map���`a[���`eparts���`a[���`ai���`a]���`a]���`a
���`d    ���`gnpoints���`a ���aoa=���`a ���`dPath���aoa.���`uNUM_VERTICES_FOR_CODE���`a[���`ipath_code���`a]���`a
���`d    ���`ecodes���aoa.���`fextend���`a(���`a[���`ipath_code���`a]���`a ���aoa*���`a ���`gnpoints���`a)���`a
���`d    ���`hvertices���aoa.���`fextend���`a(���`a[���`a[���aoa*���bnbcmap���`a(���bnbefloat���`a,���`a ���`ay���aoa.���`esplit���`a(���bs1a'���bs1a,���bs1a'���`a)���`a)���`a]���`a
���`u                     ���akcfor���`a ���`ay���`a ���bowbin���`a ���`eparts���`a[���`ai���`a ���aoa+���`a ���bmia1���`a:���`a]���`a[���`a:���`gnpoints���`a]���`a]���`a)���`a
���`d    ���`ai���`a ���aoa+���aoa=���`a ���`gnpoints���`a ���aoa+���`a ���bmia1���`a
���`hvertices���`a ���aoa=���`a ���`bnp���aoa.���`earray���`a(���`hvertices���`a)���`a
���`hvertices���`a[���`a:���`a,���`a ���bmia1���`a]���`a ���aoa-���aoa=���`a ���bmic160���`a
���`a
���`ldolphin_path���`a ���aoa=���`a ���`dPath���`a(���`hvertices���`a,���`a ���`ecodes���`a)���`a
���`mdolphin_patch���`a ���aoa=���`a ���`iPathPatch���`a(���`ldolphin_path���`a,���`a ���`ifacecolor���aoa=���`a(���bmfc0.6���`a,���`a ���bmfc0.6���`a,���`a ���bmfc0.6���`a)���`a,���`a
���`x                          ���`iedgecolor���aoa=���`a(���bmfc0.0���`a,���`a ���bmfc0.0���`a,���`a ���bmfc0.0���`a)���`a)���`a
���`bax���aoa.���`iadd_patch���`a(���`mdolphin_patch���`a)���`a
���`a
���`hvertices���`a ���aoa=���`a ���`hAffine2D���`a(���`a)���aoa.���`jrotate_deg���`a(���bmib60���`a)���aoa.���`itransform���`a(���`hvertices���`a)���`a
���`mdolphin_path2���`a ���aoa=���`a ���`dPath���`a(���`hvertices���`a,���`a ���`ecodes���`a)���`a
���`ndolphin_patch2���`a ���aoa=���`a ���`iPathPatch���`a(���`mdolphin_path2���`a,���`a ���`ifacecolor���aoa=���`a(���bmfc0.5���`a,���`a ���bmfc0.5���`a,���`a ���bmfc0.5���`a)���`a,���`a
���`x                           ���`iedgecolor���aoa=���`a(���bmfc0.0���`a,���`a ���bmfc0.0���`a,���`a ���bmfc0.0���`a)���`a)���`a
���`bax���aoa.���`iadd_patch���`a(���`ndolphin_patch2���`a)���`a
���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
���`a
���bc1xM#############################################################################���`a
���bc1a#���`a
���bc1x# .. admonition:: References���`a
���bc1a#���`a
���bc1xN#    The use of the following functions, methods, classes and modules is shown���`a
���bc1u#    in this example:���`a
���bc1a#���`a
���bc1x#    - `matplotlib.path`���`a
���bc1x#    - `matplotlib.path.Path`���`a
���bc1x#    - `matplotlib.patches`���`a
���bc1x%#    - `matplotlib.patches.PathPatch`���`a
���bc1x"#    - `matplotlib.patches.Circle`���`a
���bc1x'#    - `matplotlib.axes.Axes.add_patch`���`a
���bc1x#    - `matplotlib.transforms`���`a
���bc1x'#    - `matplotlib.transforms.Affine2D`���`a
���bc1x2#    - `matplotlib.transforms.Affine2D.rotate_deg`���`a
`dNone�