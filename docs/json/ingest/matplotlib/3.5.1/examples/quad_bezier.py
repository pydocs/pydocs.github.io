������������bsdx�"""
============
Bezier Curve
============

This example showcases the `~.patches.PathPatch` object to create a Bezier
polycurve path patch.
"""���`a
���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnndpath���`a ���akbas���`a ���bnnempath���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnngpatches���`a ���akbas���`a ���bnnhmpatches���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���`a
���`dPath���`a ���aoa=���`a ���`empath���aoa.���`dPath���`a
���`a
���`cfig���`a,���`a ���`bax���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`a)���`a
���`cpp1���`a ���aoa=���`a ���`hmpatches���aoa.���`iPathPatch���`a(���`a
���`d    ���`dPath���`a(���`a[���`a(���bmia0���`a,���`a ���bmia0���`a)���`a,���`a ���`a(���bmia1���`a,���`a ���bmia0���`a)���`a,���`a ���`a(���bmia1���`a,���`a ���bmia1���`a)���`a,���`a ���`a(���bmia0���`a,���`a ���bmia0���`a)���`a]���`a,���`a
���`i         ���`a[���`dPath���aoa.���`fMOVETO���`a,���`a ���`dPath���aoa.���`fCURVE3���`a,���`a ���`dPath���aoa.���`fCURVE3���`a,���`a ���`dPath���aoa.���`iCLOSEPOLY���`a]���`a)���`a,���`a
���`d    ���`bfc���aoa=���bs2a"���bs2dnone���bs2a"���`a,���`a ���`itransform���aoa=���`bax���aoa.���`itransData���`a)���`a
���`a
���`bax���aoa.���`iadd_patch���`a(���`cpp1���`a)���`a
���`bax���aoa.���`dplot���`a(���`a[���bmfd0.75���`a]���`a,���`a ���`a[���bmfd0.25���`a]���`a,���`a ���bs2a"���bs2bro���bs2a"���`a)���`a
���`bax���aoa.���`iset_title���`a(���bs1a'���bs1x#The red point should be on the path���bs1a'���`a)���`a
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
���bc1x'#    - `matplotlib.axes.Axes.add_patch`���`a
`dNone�