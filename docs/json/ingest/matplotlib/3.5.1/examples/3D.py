��������l���bsdxy"""
====================
Frontpage 3D example
====================

This example reproduces the frontpage 3D example.
"""���`a
���`a
���bkndfrom���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����`a ���bknfimport���`a ���`ecbook���`a
���bkndfrom���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����`a ���bknfimport���`a ���`bcm���`a
���bkndfrom���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfcolors���`a ���bknfimport���`a ���`kLightSource���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���`a
���`cdem���`a ���aoa=���`a ���`ecbook���aoa.���`oget_sample_data���`a(���bs1a'���bs1wjacksboro_fault_dem.npz���bs1a'���`a,���`a ���`gnp_load���aoa=���bkcdTrue���`a)���`a
���`az���`a ���aoa=���`a ���`cdem���`a[���bs1a'���bs1ielevation���bs1a'���`a]���`a
���`enrows���`a,���`a ���`encols���`a ���aoa=���`a ���`az���aoa.���`eshape���`a
���`ax���`a ���aoa=���`a ���`bnp���aoa.���`hlinspace���`a(���`cdem���`a[���bs1a'���bs1dxmin���bs1a'���`a]���`a,���`a ���`cdem���`a[���bs1a'���bs1dxmax���bs1a'���`a]���`a,���`a ���`encols���`a)���`a
���`ay���`a ���aoa=���`a ���`bnp���aoa.���`hlinspace���`a(���`cdem���`a[���bs1a'���bs1dymin���bs1a'���`a]���`a,���`a ���`cdem���`a[���bs1a'���bs1dymax���bs1a'���`a]���`a,���`a ���`enrows���`a)���`a
���`ax���`a,���`a ���`ay���`a ���aoa=���`a ���`bnp���aoa.���`hmeshgrid���`a(���`ax���`a,���`a ���`ay���`a)���`a
���`a
���`fregion���`a ���aoa=���`a ���`bnp���aoa.���`bs_���`a[���bmia5���`a:���bmib50���`a,���`a ���bmia5���`a:���bmib50���`a]���`a
���`ax���`a,���`a ���`ay���`a,���`a ���`az���`a ���aoa=���`a ���`ax���`a[���`fregion���`a]���`a,���`a ���`ay���`a[���`fregion���`a]���`a,���`a ���`az���`a[���`fregion���`a]���`a
���`a
���`cfig���`a,���`a ���`bax���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`jsubplot_kw���aoa=���bnbddict���`a(���`jprojection���aoa=���bs1a'���bs1b3d���bs1a'���`a)���`a)���`a
���`a
���`bls���`a ���aoa=���`a ���`kLightSource���`a(���bmic270���`a,���`a ���bmib45���`a)���`a
���bc1xJ# To use a custom hillshading mode, override the built-in shading and pass���`a
���bc1xB# in the rgb colors of the shaded surface calculated from "shade".���`a
���`crgb���`a ���aoa=���`a ���`bls���aoa.���`eshade���`a(���`az���`a,���`a ���`dcmap���aoa=���`bcm���aoa.���`jgist_earth���`a,���`a ���`ivert_exag���aoa=���bmfc0.1���`a,���`a ���`jblend_mode���aoa=���bs1a'���bs1dsoft���bs1a'���`a)���`a
���`dsurf���`a ���aoa=���`a ���`bax���aoa.���`lplot_surface���`a(���`ax���`a,���`a ���`ay���`a,���`a ���`az���`a,���`a ���`grstride���aoa=���bmia1���`a,���`a ���`gcstride���aoa=���bmia1���`a,���`a ���`jfacecolors���aoa=���`crgb���`a,���`a
���`w                       ���`ilinewidth���aoa=���bmia0���`a,���`a ���`kantialiased���aoa=���bkceFalse���`a,���`a ���`eshade���aoa=���bkceFalse���`a)���`a
���`bax���aoa.���`jset_xticks���`a(���`a[���`a]���`a)���`a
���`bax���aoa.���`jset_yticks���`a(���`a[���`a]���`a)���`a
���`bax���aoa.���`jset_zticks���`a(���`a[���`a]���`a)���`a
���`cfig���aoa.���`gsavefig���`a(���bs2a"���bs2wsurface3d_frontpage.png���bs2a"���`a,���`a ���`cdpi���aoa=���bmib25���`a)���`b  ���bc1x# results in 160x120 px image���`a
`dNone�