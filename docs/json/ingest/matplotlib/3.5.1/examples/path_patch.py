��������e���bsaar���bsdx�"""
================
PathPatch object
================

This example shows how to create `~.path.Path` and `~.patches.PathPatch`
objects through Matplotlib's API.
"""���`a
���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnndpath���`a ���akbas���`a ���bnnempath���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnngpatches���`a ���akbas���`a ���bnnhmpatches���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���`a
���`cfig���`a,���`a ���`bax���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`a)���`a
���`a
���`dPath���`a ���aoa=���`a ���`empath���aoa.���`dPath���`a
���`ipath_data���`a ���aoa=���`a ���`a[���`a
���`d    ���`a(���`dPath���aoa.���`fMOVETO���`a,���`a ���`a(���bmfd1.58���`a,���`a ���aoa-���bmfd2.57���`a)���`a)���`a,���`a
���`d    ���`a(���`dPath���aoa.���`fCURVE4���`a,���`a ���`a(���bmfd0.35���`a,���`a ���aoa-���bmfc1.1���`a)���`a)���`a,���`a
���`d    ���`a(���`dPath���aoa.���`fCURVE4���`a,���`a ���`a(���aoa-���bmfd1.75���`a,���`a ���bmfc2.0���`a)���`a)���`a,���`a
���`d    ���`a(���`dPath���aoa.���`fCURVE4���`a,���`a ���`a(���bmfe0.375���`a,���`a ���bmfc2.0���`a)���`a)���`a,���`a
���`d    ���`a(���`dPath���aoa.���`fLINETO���`a,���`a ���`a(���bmfd0.85���`a,���`a ���bmfd1.15���`a)���`a)���`a,���`a
���`d    ���`a(���`dPath���aoa.���`fCURVE4���`a,���`a ���`a(���bmfc2.2���`a,���`a ���bmfc3.2���`a)���`a)���`a,���`a
���`d    ���`a(���`dPath���aoa.���`fCURVE4���`a,���`a ���`a(���bmia3���`a,���`a ���bmfd0.05���`a)���`a)���`a,���`a
���`d    ���`a(���`dPath���aoa.���`fCURVE4���`a,���`a ���`a(���bmfc2.0���`a,���`a ���aoa-���bmfc0.5���`a)���`a)���`a,���`a
���`d    ���`a(���`dPath���aoa.���`iCLOSEPOLY���`a,���`a ���`a(���bmfd1.58���`a,���`a ���aoa-���bmfd2.57���`a)���`a)���`a,���`a
���`d    ���`a]���`a
���`ecodes���`a,���`a ���`everts���`a ���aoa=���`a ���bnbczip���`a(���aoa*���`ipath_data���`a)���`a
���`dpath���`a ���aoa=���`a ���`empath���aoa.���`dPath���`a(���`everts���`a,���`a ���`ecodes���`a)���`a
���`epatch���`a ���aoa=���`a ���`hmpatches���aoa.���`iPathPatch���`a(���`dpath���`a,���`a ���`ifacecolor���aoa=���bs1a'���bs1ar���bs1a'���`a,���`a ���`ealpha���aoa=���bmfc0.5���`a)���`a
���`bax���aoa.���`iadd_patch���`a(���`epatch���`a)���`a
���`a
���bc1x*# plot control points and connecting lines���`a
���`ax���`a,���`a ���`ay���`a ���aoa=���`a ���bnbczip���`a(���aoa*���`dpath���aoa.���`hvertices���`a)���`a
���`dline���`a,���`a ���aoa=���`a ���`bax���aoa.���`dplot���`a(���`ax���`a,���`a ���`ay���`a,���`a ���bs1a'���bs1cgo-���bs1a'���`a)���`a
���`a
���`bax���aoa.���`dgrid���`a(���`a)���`a
���`bax���aoa.���`daxis���`a(���bs1a'���bs1eequal���bs1a'���`a)���`a
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
���bc1x'#    - `matplotlib.axes.Axes.add_patch`���`a
`dNone�