������������bsaar���bsdy)"""
==========================
Multiple Yaxis With Spines
==========================

Create multiple y axes with a shared x axis. This is done by creating
a `~.axes.Axes.twinx` axes, turning all spines but the right one invisible
and offset its position using `~.spines.Spine.set_position`.

Note that this approach uses `matplotlib.axes.Axes` and their
`~matplotlib.spines.Spine`\s. An alternative approach for parasite
axes is shown in the :doc:`/gallery/axisartist/demo_parasite_axes` and
:doc:`/gallery/axisartist/demo_parasite_axes2` examples.
"""���`a
���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���`a
���`a
���`cfig���`a,���`a ���`bax���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`a)���`a
���`cfig���aoa.���`osubplots_adjust���`a(���`eright���aoa=���bmfd0.75���`a)���`a
���`a
���`etwin1���`a ���aoa=���`a ���`bax���aoa.���`etwinx���`a(���`a)���`a
���`etwin2���`a ���aoa=���`a ���`bax���aoa.���`etwinx���`a(���`a)���`a
���`a
���bc1xI# Offset the right spine of twin2.  The ticks and label have already been���`a
���bc1x%# placed on the right by twinx above.���`a
���`etwin2���aoa.���`fspines���aoa.���`eright���aoa.���`lset_position���`a(���`a(���bs2a"���bs2daxes���bs2a"���`a,���`a ���bmfc1.2���`a)���`a)���`a
���`a
���`bp1���`a,���`a ���aoa=���`a ���`bax���aoa.���`dplot���`a(���`a[���bmia0���`a,���`a ���bmia1���`a,���`a ���bmia2���`a]���`a,���`a ���`a[���bmia0���`a,���`a ���bmia1���`a,���`a ���bmia2���`a]���`a,���`a ���bs2a"���bs2bb-���bs2a"���`a,���`a ���`elabel���aoa=���bs2a"���bs2gDensity���bs2a"���`a)���`a
���`bp2���`a,���`a ���aoa=���`a ���`etwin1���aoa.���`dplot���`a(���`a[���bmia0���`a,���`a ���bmia1���`a,���`a ���bmia2���`a]���`a,���`a ���`a[���bmia0���`a,���`a ���bmia3���`a,���`a ���bmia2���`a]���`a,���`a ���bs2a"���bs2br-���bs2a"���`a,���`a ���`elabel���aoa=���bs2a"���bs2kTemperature���bs2a"���`a)���`a
���`bp3���`a,���`a ���aoa=���`a ���`etwin2���aoa.���`dplot���`a(���`a[���bmia0���`a,���`a ���bmia1���`a,���`a ���bmia2���`a]���`a,���`a ���`a[���bmib50���`a,���`a ���bmib30���`a,���`a ���bmib15���`a]���`a,���`a ���bs2a"���bs2bg-���bs2a"���`a,���`a ���`elabel���aoa=���bs2a"���bs2hVelocity���bs2a"���`a)���`a
���`a
���`bax���aoa.���`hset_xlim���`a(���bmia0���`a,���`a ���bmia2���`a)���`a
���`bax���aoa.���`hset_ylim���`a(���bmia0���`a,���`a ���bmia2���`a)���`a
���`etwin1���aoa.���`hset_ylim���`a(���bmia0���`a,���`a ���bmia4���`a)���`a
���`etwin2���aoa.���`hset_ylim���`a(���bmia1���`a,���`a ���bmib65���`a)���`a
���`a
���`bax���aoa.���`jset_xlabel���`a(���bs2a"���bs2hDistance���bs2a"���`a)���`a
���`bax���aoa.���`jset_ylabel���`a(���bs2a"���bs2gDensity���bs2a"���`a)���`a
���`etwin1���aoa.���`jset_ylabel���`a(���bs2a"���bs2kTemperature���bs2a"���`a)���`a
���`etwin2���aoa.���`jset_ylabel���`a(���bs2a"���bs2hVelocity���bs2a"���`a)���`a
���`a
���`bax���aoa.���`eyaxis���aoa.���`elabel���aoa.���`iset_color���`a(���`bp1���aoa.���`iget_color���`a(���`a)���`a)���`a
���`etwin1���aoa.���`eyaxis���aoa.���`elabel���aoa.���`iset_color���`a(���`bp2���aoa.���`iget_color���`a(���`a)���`a)���`a
���`etwin2���aoa.���`eyaxis���aoa.���`elabel���aoa.���`iset_color���`a(���`bp3���aoa.���`iget_color���`a(���`a)���`a)���`a
���`a
���`ctkw���`a ���aoa=���`a ���bnbddict���`a(���`dsize���aoa=���bmia4���`a,���`a ���`ewidth���aoa=���bmfc1.5���`a)���`a
���`bax���aoa.���`ktick_params���`a(���`daxis���aoa=���bs1a'���bs1ay���bs1a'���`a,���`a ���`fcolors���aoa=���`bp1���aoa.���`iget_color���`a(���`a)���`a,���`a ���aoa*���aoa*���`ctkw���`a)���`a
���`etwin1���aoa.���`ktick_params���`a(���`daxis���aoa=���bs1a'���bs1ay���bs1a'���`a,���`a ���`fcolors���aoa=���`bp2���aoa.���`iget_color���`a(���`a)���`a,���`a ���aoa*���aoa*���`ctkw���`a)���`a
���`etwin2���aoa.���`ktick_params���`a(���`daxis���aoa=���bs1a'���bs1ay���bs1a'���`a,���`a ���`fcolors���aoa=���`bp3���aoa.���`iget_color���`a(���`a)���`a,���`a ���aoa*���aoa*���`ctkw���`a)���`a
���`bax���aoa.���`ktick_params���`a(���`daxis���aoa=���bs1a'���bs1ax���bs1a'���`a,���`a ���aoa*���aoa*���`ctkw���`a)���`a
���`a
���`bax���aoa.���`flegend���`a(���`ghandles���aoa=���`a[���`bp1���`a,���`a ���`bp2���`a,���`a ���`bp3���`a]���`a)���`a
���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
`dNone�