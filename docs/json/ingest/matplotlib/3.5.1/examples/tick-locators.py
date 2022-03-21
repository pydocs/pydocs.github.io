������������bsdx�"""
=============
Tick locators
=============

Tick locators define the position of the ticks.

This example illustrates the usage and effect of the most common locators.
"""���`a
���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfticker���`a ���akbas���`a ���bnnfticker���`a
���`a
���`a
���akcdef���`a ���bnfesetup���`a(���`bax���`a,���`a ���`etitle���`a)���`a:���`a
���`d    ���bsdx;"""Set up common parameters for the Axes in the example."""���`a
���`d    ���bc1x# only show the bottom spine���`a
���`d    ���`bax���aoa.���`eyaxis���aoa.���`qset_major_locator���`a(���`fticker���aoa.���`kNullLocator���`a(���`a)���`a)���`a
���`d    ���`bax���aoa.���`fspines���aoa.���`eright���aoa.���`iset_color���`a(���bs1a'���bs1dnone���bs1a'���`a)���`a
���`d    ���`bax���aoa.���`fspines���aoa.���`dleft���aoa.���`iset_color���`a(���bs1a'���bs1dnone���bs1a'���`a)���`a
���`d    ���`bax���aoa.���`fspines���aoa.���`ctop���aoa.���`iset_color���`a(���bs1a'���bs1dnone���bs1a'���`a)���`a
���`a
���`d    ���`bax���aoa.���`exaxis���aoa.���`rset_ticks_position���`a(���bs1a'���bs1fbottom���bs1a'���`a)���`a
���`d    ���`bax���aoa.���`ktick_params���`a(���`ewhich���aoa=���bs1a'���bs1emajor���bs1a'���`a,���`a ���`ewidth���aoa=���bmfd1.00���`a,���`a ���`flength���aoa=���bmia5���`a)���`a
���`d    ���`bax���aoa.���`ktick_params���`a(���`ewhich���aoa=���bs1a'���bs1eminor���bs1a'���`a,���`a ���`ewidth���aoa=���bmfd0.75���`a,���`a ���`flength���aoa=���bmfc2.5���`a)���`a
���`d    ���`bax���aoa.���`hset_xlim���`a(���bmia0���`a,���`a ���bmia5���`a)���`a
���`d    ���`bax���aoa.���`hset_ylim���`a(���bmia0���`a,���`a ���bmia1���`a)���`a
���`d    ���`bax���aoa.���`dtext���`a(���bmfc0.0���`a,���`a ���bmfc0.2���`a,���`a ���`etitle���`a,���`a ���`itransform���aoa=���`bax���aoa.���`itransAxes���`a,���`a
���`l            ���`hfontsize���aoa=���bmib14���`a,���`a ���`hfontname���aoa=���bs1a'���bs1iMonospace���bs1a'���`a,���`a ���`ecolor���aoa=���bs1a'���bs1htab:blue���bs1a'���`a)���`a
���`a
���`a
���`cfig���`a,���`a ���`caxs���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���bmia8���`a,���`a ���bmia1���`a,���`a ���`gfigsize���aoa=���`a(���bmia8���`a,���`a ���bmia6���`a)���`a)���`a
���`a
���bc1n# Null Locator���`a
���`esetup���`a(���`caxs���`a[���bmia0���`a]���`a,���`a ���`etitle���aoa=���bs2a"���bs2mNullLocator()���bs2a"���`a)���`a
���`caxs���`a[���bmia0���`a]���aoa.���`exaxis���aoa.���`qset_major_locator���`a(���`fticker���aoa.���`kNullLocator���`a(���`a)���`a)���`a
���`caxs���`a[���bmia0���`a]���aoa.���`exaxis���aoa.���`qset_minor_locator���`a(���`fticker���aoa.���`kNullLocator���`a(���`a)���`a)���`a
���`a
���bc1r# Multiple Locator���`a
���`esetup���`a(���`caxs���`a[���bmia1���`a]���`a,���`a ���`etitle���aoa=���bs2a"���bs2tMultipleLocator(0.5)���bs2a"���`a)���`a
���`caxs���`a[���bmia1���`a]���aoa.���`exaxis���aoa.���`qset_major_locator���`a(���`fticker���aoa.���`oMultipleLocator���`a(���bmfc0.5���`a)���`a)���`a
���`caxs���`a[���bmia1���`a]���aoa.���`exaxis���aoa.���`qset_minor_locator���`a(���`fticker���aoa.���`oMultipleLocator���`a(���bmfc0.1���`a)���`a)���`a
���`a
���bc1o# Fixed Locator���`a
���`esetup���`a(���`caxs���`a[���bmia2���`a]���`a,���`a ���`etitle���aoa=���bs2a"���bs2wFixedLocator([0, 1, 5])���bs2a"���`a)���`a
���`caxs���`a[���bmia2���`a]���aoa.���`exaxis���aoa.���`qset_major_locator���`a(���`fticker���aoa.���`lFixedLocator���`a(���`a[���bmia0���`a,���`a ���bmia1���`a,���`a ���bmia5���`a]���`a)���`a)���`a
���`caxs���`a[���bmia2���`a]���aoa.���`exaxis���aoa.���`qset_minor_locator���`a(���`fticker���aoa.���`lFixedLocator���`a(���`bnp���aoa.���`hlinspace���`a(���bmfc0.2���`a,���`a ���bmfc0.8���`a,���`a ���bmia4���`a)���`a)���`a)���`a
���`a
���bc1p# Linear Locator���`a
���`esetup���`a(���`caxs���`a[���bmia3���`a]���`a,���`a ���`etitle���aoa=���bs2a"���bs2xLinearLocator(numticks=3)���bs2a"���`a)���`a
���`caxs���`a[���bmia3���`a]���aoa.���`exaxis���aoa.���`qset_major_locator���`a(���`fticker���aoa.���`mLinearLocator���`a(���bmia3���`a)���`a)���`a
���`caxs���`a[���bmia3���`a]���aoa.���`exaxis���aoa.���`qset_minor_locator���`a(���`fticker���aoa.���`mLinearLocator���`a(���bmib31���`a)���`a)���`a
���`a
���bc1o# Index Locator���`a
���`esetup���`a(���`caxs���`a[���bmia4���`a]���`a,���`a ���`etitle���aoa=���bs2a"���bs2x#IndexLocator(base=0.5, offset=0.25)���bs2a"���`a)���`a
���`caxs���`a[���bmia4���`a]���aoa.���`dplot���`a(���bnberange���`a(���bmia0���`a,���`a ���bmia5���`a)���`a,���`a ���`a[���bmia0���`a]���aoa*���bmia5���`a,���`a ���`ecolor���aoa=���bs1a'���bs1ewhite���bs1a'���`a)���`a
���`caxs���`a[���bmia4���`a]���aoa.���`exaxis���aoa.���`qset_major_locator���`a(���`fticker���aoa.���`lIndexLocator���`a(���`dbase���aoa=���bmfc0.5���`a,���`a ���`foffset���aoa=���bmfd0.25���`a)���`a)���`a
���`a
���bc1n# Auto Locator���`a
���`esetup���`a(���`caxs���`a[���bmia5���`a]���`a,���`a ���`etitle���aoa=���bs2a"���bs2mAutoLocator()���bs2a"���`a)���`a
���`caxs���`a[���bmia5���`a]���aoa.���`exaxis���aoa.���`qset_major_locator���`a(���`fticker���aoa.���`kAutoLocator���`a(���`a)���`a)���`a
���`caxs���`a[���bmia5���`a]���aoa.���`exaxis���aoa.���`qset_minor_locator���`a(���`fticker���aoa.���`pAutoMinorLocator���`a(���`a)���`a)���`a
���`a
���bc1n# MaxN Locator���`a
���`esetup���`a(���`caxs���`a[���bmia6���`a]���`a,���`a ���`etitle���aoa=���bs2a"���bs2pMaxNLocator(n=4)���bs2a"���`a)���`a
���`caxs���`a[���bmia6���`a]���aoa.���`exaxis���aoa.���`qset_major_locator���`a(���`fticker���aoa.���`kMaxNLocator���`a(���bmia4���`a)���`a)���`a
���`caxs���`a[���bmia6���`a]���aoa.���`exaxis���aoa.���`qset_minor_locator���`a(���`fticker���aoa.���`kMaxNLocator���`a(���bmib40���`a)���`a)���`a
���`a
���bc1m# Log Locator���`a
���`esetup���`a(���`caxs���`a[���bmia7���`a]���`a,���`a ���`etitle���aoa=���bs2a"���bs2x LogLocator(base=10, numticks=15)���bs2a"���`a)���`a
���`caxs���`a[���bmia7���`a]���aoa.���`hset_xlim���`a(���bmib10���aoa*���aoa*���bmia3���`a,���`a ���bmib10���aoa*���aoa*���bmib10���`a)���`a
���`caxs���`a[���bmia7���`a]���aoa.���`jset_xscale���`a(���bs1a'���bs1clog���bs1a'���`a)���`a
���`caxs���`a[���bmia7���`a]���aoa.���`exaxis���aoa.���`qset_major_locator���`a(���`fticker���aoa.���`jLogLocator���`a(���`dbase���aoa=���bmib10���`a,���`a ���`hnumticks���aoa=���bmib15���`a)���`a)���`a
���`a
���`cplt���aoa.���`ltight_layout���`a(���`a)���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
`dNone�