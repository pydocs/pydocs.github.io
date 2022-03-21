��������W���bsaar���bsdx�"""
=============
Mmh Donuts!!!
=============

Draw donuts (miam!) using `~.path.Path`\s and `~.patches.PathPatch`\es.
This example shows the effect of the path's orientations in a compound path.
"""���`a
���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnndpath���`a ���akbas���`a ���bnnempath���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnngpatches���`a ���akbas���`a ���bnnhmpatches���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���`a
���`a
���akcdef���`a ���bnfdwise���`a(���`av���`a)���`a:���`a
���`d    ���akbif���`a ���`av���`a ���aob==���`a ���bmia1���`a:���`a
���`h        ���akfreturn���`a ���bs2a"���bs2cCCW���bs2a"���`a
���`d    ���akdelse���`a:���`a
���`h        ���akfreturn���`a ���bs2a"���bs2bCW���bs2a"���`a
���`a
���`a
���akcdef���`a ���bnfkmake_circle���`a(���`ar���`a)���`a:���`a
���`d    ���`at���`a ���aoa=���`a ���`bnp���aoa.���`farange���`a(���bmia0���`a,���`a ���`bnp���aoa.���`bpi���`a ���aoa*���`a ���bmfc2.0���`a,���`a ���bmfd0.01���`a)���`a
���`d    ���`at���`a ���aoa=���`a ���`at���aoa.���`greshape���`a(���`a(���bnbclen���`a(���`at���`a)���`a,���`a ���bmia1���`a)���`a)���`a
���`d    ���`ax���`a ���aoa=���`a ���`ar���`a ���aoa*���`a ���`bnp���aoa.���`ccos���`a(���`at���`a)���`a
���`d    ���`ay���`a ���aoa=���`a ���`ar���`a ���aoa*���`a ���`bnp���aoa.���`csin���`a(���`at���`a)���`a
���`d    ���akfreturn���`a ���`bnp���aoa.���`fhstack���`a(���`a(���`ax���`a,���`a ���`ay���`a)���`a)���`a
���`a
���`dPath���`a ���aoa=���`a ���`empath���aoa.���`dPath���`a
���`a
���`cfig���`a,���`a ���`bax���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`a)���`a
���`a
���`oinside_vertices���`a ���aoa=���`a ���`kmake_circle���`a(���bmfc0.5���`a)���`a
���`poutside_vertices���`a ���aoa=���`a ���`kmake_circle���`a(���bmfc1.0���`a)���`a
���`ecodes���`a ���aoa=���`a ���`bnp���aoa.���`dones���`a(���`a
���`d    ���bnbclen���`a(���`oinside_vertices���`a)���`a,���`a ���`edtype���aoa=���`empath���aoa.���`dPath���aoa.���`icode_type���`a)���`a ���aoa*���`a ���`empath���aoa.���`dPath���aoa.���`fLINETO���`a
���`ecodes���`a[���bmia0���`a]���`a ���aoa=���`a ���`empath���aoa.���`dPath���aoa.���`fMOVETO���`a
���`a
���akcfor���`a ���`ai���`a,���`a ���`a(���`finside���`a,���`a ���`goutside���`a)���`a ���bowbin���`a ���bnbienumerate���`a(���`a(���`a(���bmia1���`a,���`a ���bmia1���`a)���`a,���`a ���`a(���bmia1���`a,���`a ���aoa-���bmia1���`a)���`a,���`a ���`a(���aoa-���bmia1���`a,���`a ���bmia1���`a)���`a,���`a ���`a(���aoa-���bmia1���`a,���`a ���aoa-���bmia1���`a)���`a)���`a)���`a:���`a
���`d    ���bc1xF# Concatenate the inside and outside subpaths together, changing their���`a
���`d    ���bc1q# order as needed���`a
���`d    ���`hvertices���`a ���aoa=���`a ���`bnp���aoa.���`kconcatenate���`a(���`a(���`poutside_vertices���`a[���`a:���`a:���`goutside���`a]���`a,���`a
���`x                               ���`oinside_vertices���`a[���`a:���`a:���`finside���`a]���`a)���`a)���`a
���`d    ���bc1p# Shift the path���`a
���`d    ���`hvertices���`a[���`a:���`a,���`a ���bmia0���`a]���`a ���aoa+���aoa=���`a ���`ai���`a ���aoa*���`a ���bmfc2.5���`a
���`d    ���bc1xF# The codes will be all "LINETO" commands, except for "MOVETO"s at the���`a
���`d    ���bc1x# beginning of each subpath���`a
���`d    ���`iall_codes���`a ���aoa=���`a ���`bnp���aoa.���`kconcatenate���`a(���`a(���`ecodes���`a,���`a ���`ecodes���`a)���`a)���`a
���`d    ���bc1x# Create the Path object���`a
���`d    ���`dpath���`a ���aoa=���`a ���`empath���aoa.���`dPath���`a(���`hvertices���`a,���`a ���`iall_codes���`a)���`a
���`d    ���bc1m# Add plot it���`a
���`d    ���`epatch���`a ���aoa=���`a ���`hmpatches���aoa.���`iPathPatch���`a(���`dpath���`a,���`a ���`ifacecolor���aoa=���bs1a'���bs1g#885500���bs1a'���`a,���`a ���`iedgecolor���aoa=���bs1a'���bs1eblack���bs1a'���`a)���`a
���`d    ���`bax���aoa.���`iadd_patch���`a(���`epatch���`a)���`a
���`a
���`d    ���`bax���aoa.���`hannotate���`a(���bs2a"���bs2hOutside ���bsib%s���bs2a,���bseb\n���bs2gInside ���bsib%s���bs2a"���`a ���aoa%���`a ���`a(���`dwise���`a(���`goutside���`a)���`a,���`a ���`dwise���`a(���`finside���`a)���`a)���`a,���`a
���`p                ���`a(���`ai���`a ���aoa*���`a ���bmfc2.5���`a,���`a ���aoa-���bmfc1.5���`a)���`a,���`a ���`bva���aoa=���bs2a"���bs2ctop���bs2a"���`a,���`a ���`bha���aoa=���bs2a"���bs2fcenter���bs2a"���`a)���`a
���`a
���`bax���aoa.���`hset_xlim���`a(���aoa-���bmia2���`a,���`a ���bmib10���`a)���`a
���`bax���aoa.���`hset_ylim���`a(���aoa-���bmia3���`a,���`a ���bmia2���`a)���`a
���`bax���aoa.���`iset_title���`a(���bs1a'���bs1lMmm, donuts!���bs1a'���`a)���`a
���`bax���aoa.���`jset_aspect���`a(���bmfc1.0���`a)���`a
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
���bc1x&#    - `matplotlib.axes.Axes.annotate`���`a
���bc1x(#    - `matplotlib.axes.Axes.set_aspect`���`a
���bc1x&#    - `matplotlib.axes.Axes.set_xlim`���`a
���bc1x&#    - `matplotlib.axes.Axes.set_ylim`���`a
���bc1x'#    - `matplotlib.axes.Axes.set_title`���`a
`dNone�