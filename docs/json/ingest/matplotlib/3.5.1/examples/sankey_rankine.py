������������bsdx�"""
===================
Rankine power cycle
===================

Demonstrate the Sankey class with a practical example of a Rankine power cycle.
"""���`a
���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���`a
���bkndfrom���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfsankey���`a ���bknfimport���`a ���`fSankey���`a
���`a
���`cfig���`a ���aoa=���`a ���`cplt���aoa.���`ffigure���`a(���`gfigsize���aoa=���`a(���bmia8���`a,���`a ���bmia9���`a)���`a)���`a
���`bax���`a ���aoa=���`a ���`cfig���aoa.���`kadd_subplot���`a(���bmia1���`a,���`a ���bmia1���`a,���`a ���bmia1���`a,���`a ���`fxticks���aoa=���`a[���`a]���`a,���`a ���`fyticks���aoa=���`a[���`a]���`a,���`a
���`u                     ���`etitle���aoa=���bs2a"���bs2x0Rankine Power Cycle: Example 8.6 from Moran and ���bs2a"���`a
���`u                     ���bs2a"���bs2gShapiro���bseb\n���bsed\x22���bs2x+Fundamentals of Engineering Thermodynamics ���bs2a"���`a
���`u                     ���bs2a"���bsed\x22���bs2o, 6th ed., 2008���bs2a"���`a)���`a
���`dHdot���`a ���aoa=���`a ���`a[���bmfg260.431���`a,���`a ���bmff35.078���`a,���`a ���bmfg180.794���`a,���`a ���bmfg221.115���`a,���`a ���bmff22.700���`a,���`a
���`h        ���bmfg142.361���`a,���`a ���bmff10.193���`a,���`a ���bmff10.210���`a,���`a ���bmff43.670���`a,���`a ���bmff44.312���`a,���`a
���`h        ���bmff68.631���`a,���`a ���bmff10.758���`a,���`a ���bmff10.758���`a,���`a ���bmfe0.017���`a,���`a ���bmfe0.642���`a,���`a
���`h        ���bmfg232.121���`a,���`a ���bmff44.559���`a,���`a ���bmfg100.613���`a,���`a ���bmfg132.168���`a]���`b  ���bc1d# MW���`a
���`fsankey���`a ���aoa=���`a ���`fSankey���`a(���`bax���aoa=���`bax���`a,���`a ���bnbfformat���aoa=���bs1a'���bsid%.3G���bs1a'���`a,���`a ���`dunit���aoa=���bs1a'���bs1c MW���bs1a'���`a,���`a ���`cgap���aoa=���bmfc0.5���`a,���`a ���`escale���aoa=���bmfc1.0���aoa/���`dHdot���`a[���bmia0���`a]���`a)���`a
���`fsankey���aoa.���`cadd���`a(���`jpatchlabel���aoa=���bs1a'���bseb\n���bseb\n���bs1fPump 1���bs1a'���`a,���`a ���`hrotation���aoa=���bmib90���`a,���`a ���`ifacecolor���aoa=���bs1a'���bs1g#37c959���bs1a'���`a,���`a
���`k           ���`eflows���aoa=���`a[���`dHdot���`a[���bmib13���`a]���`a,���`a ���`dHdot���`a[���bmia6���`a]���`a,���`a ���aoa-���`dHdot���`a[���bmia7���`a]���`a]���`a,���`a
���`k           ���`flabels���aoa=���`a[���bs1a'���bs1kShaft power���bs1a'���`a,���`a ���bs1a'���bs1a'���`a,���`a ���bkcdNone���`a]���`a,���`a
���`k           ���`kpathlengths���aoa=���`a[���bmfc0.4���`a,���`a ���bmfe0.883���`a,���`a ���bmfd0.25���`a]���`a,���`a
���`k           ���`lorientations���aoa=���`a[���bmia1���`a,���`a ���aoa-���bmia1���`a,���`a ���bmia0���`a]���`a)���`a
���`fsankey���aoa.���`cadd���`a(���`jpatchlabel���aoa=���bs1a'���bseb\n���bseb\n���bs1dOpen���bseb\n���bs1fheater���bs1a'���`a,���`a ���`ifacecolor���aoa=���bs1a'���bs1g#37c959���bs1a'���`a,���`a
���`k           ���`eflows���aoa=���`a[���`dHdot���`a[���bmib11���`a]���`a,���`a ���`dHdot���`a[���bmia7���`a]���`a,���`a ���`dHdot���`a[���bmia4���`a]���`a,���`a ���aoa-���`dHdot���`a[���bmia8���`a]���`a]���`a,���`a
���`k           ���`flabels���aoa=���`a[���bkcdNone���`a,���`a ���bs1a'���bs1a'���`a,���`a ���bkcdNone���`a,���`a ���bkcdNone���`a]���`a,���`a
���`k           ���`kpathlengths���aoa=���`a[���bmfd0.25���`a,���`a ���bmfd0.25���`a,���`a ���bmfd1.93���`a,���`a ���bmfd0.25���`a]���`a,���`a
���`k           ���`lorientations���aoa=���`a[���bmia1���`a,���`a ���bmia0���`a,���`a ���aoa-���bmia1���`a,���`a ���bmia0���`a]���`a,���`a ���`eprior���aoa=���bmia0���`a,���`a ���`gconnect���aoa=���`a(���bmia2���`a,���`a ���bmia1���`a)���`a)���`a
���`fsankey���aoa.���`cadd���`a(���`jpatchlabel���aoa=���bs1a'���bseb\n���bseb\n���bs1fPump 2���bs1a'���`a,���`a ���`ifacecolor���aoa=���bs1a'���bs1g#37c959���bs1a'���`a,���`a
���`k           ���`eflows���aoa=���`a[���`dHdot���`a[���bmib14���`a]���`a,���`a ���`dHdot���`a[���bmia8���`a]���`a,���`a ���aoa-���`dHdot���`a[���bmia9���`a]���`a]���`a,���`a
���`k           ���`flabels���aoa=���`a[���bs1a'���bs1kShaft power���bs1a'���`a,���`a ���bs1a'���bs1a'���`a,���`a ���bkcdNone���`a]���`a,���`a
���`k           ���`kpathlengths���aoa=���`a[���bmfc0.4���`a,���`a ���bmfd0.25���`a,���`a ���bmfd0.25���`a]���`a,���`a
���`k           ���`lorientations���aoa=���`a[���bmia1���`a,���`a ���bmia0���`a,���`a ���bmia0���`a]���`a,���`a ���`eprior���aoa=���bmia1���`a,���`a ���`gconnect���aoa=���`a(���bmia3���`a,���`a ���bmia1���`a)���`a)���`a
���`fsankey���aoa.���`cadd���`a(���`jpatchlabel���aoa=���bs1a'���bs1fClosed���bseb\n���bs1fheater���bs1a'���`a,���`a ���`ktrunklength���aoa=���bmfe2.914���`a,���`a ���`bfc���aoa=���bs1a'���bs1g#37c959���bs1a'���`a,���`a
���`k           ���`eflows���aoa=���`a[���`dHdot���`a[���bmia9���`a]���`a,���`a ���`dHdot���`a[���bmia1���`a]���`a,���`a ���aoa-���`dHdot���`a[���bmib11���`a]���`a,���`a ���aoa-���`dHdot���`a[���bmib10���`a]���`a]���`a,���`a
���`k           ���`kpathlengths���aoa=���`a[���bmfd0.25���`a,���`a ���bmfe1.543���`a,���`a ���bmfd0.25���`a,���`a ���bmfd0.25���`a]���`a,���`a
���`k           ���`flabels���aoa=���`a[���bs1a'���bs1a'���`a,���`a ���bs1a'���bs1a'���`a,���`a ���bkcdNone���`a,���`a ���bkcdNone���`a]���`a,���`a
���`k           ���`lorientations���aoa=���`a[���bmia0���`a,���`a ���aoa-���bmia1���`a,���`a ���bmia1���`a,���`a ���aoa-���bmia1���`a]���`a,���`a ���`eprior���aoa=���bmia2���`a,���`a ���`gconnect���aoa=���`a(���bmia2���`a,���`a ���bmia0���`a)���`a)���`a
���`fsankey���aoa.���`cadd���`a(���`jpatchlabel���aoa=���bs1a'���bs1dTrap���bs1a'���`a,���`a ���`ifacecolor���aoa=���bs1a'���bs1g#37c959���bs1a'���`a,���`a ���`ktrunklength���aoa=���bmfe5.102���`a,���`a
���`k           ���`eflows���aoa=���`a[���`dHdot���`a[���bmib11���`a]���`a,���`a ���aoa-���`dHdot���`a[���bmib12���`a]���`a]���`a,���`a
���`k           ���`flabels���aoa=���`a[���bs1a'���bseb\n���bs1a'���`a,���`a ���bkcdNone���`a]���`a,���`a
���`k           ���`kpathlengths���aoa=���`a[���bmfc1.0���`a,���`a ���bmfd1.01���`a]���`a,���`a
���`k           ���`lorientations���aoa=���`a[���bmia1���`a,���`a ���bmia1���`a]���`a,���`a ���`eprior���aoa=���bmia3���`a,���`a ���`gconnect���aoa=���`a(���bmia2���`a,���`a ���bmia0���`a)���`a)���`a
���`fsankey���aoa.���`cadd���`a(���`jpatchlabel���aoa=���bs1a'���bs1eSteam���bseb\n���bs1igenerator���bs1a'���`a,���`a ���`ifacecolor���aoa=���bs1a'���bs1g#ff5555���bs1a'���`a,���`a
���`k           ���`eflows���aoa=���`a[���`dHdot���`a[���bmib15���`a]���`a,���`a ���`dHdot���`a[���bmib10���`a]���`a,���`a ���`dHdot���`a[���bmia2���`a]���`a,���`a ���aoa-���`dHdot���`a[���bmia3���`a]���`a,���`a ���aoa-���`dHdot���`a[���bmia0���`a]���`a]���`a,���`a
���`k           ���`flabels���aoa=���`a[���bs1a'���bs1iHeat rate���bs1a'���`a,���`a ���bs1a'���bs1a'���`a,���`a ���bs1a'���bs1a'���`a,���`a ���bkcdNone���`a,���`a ���bkcdNone���`a]���`a,���`a
���`k           ���`kpathlengths���aoa=���bmfd0.25���`a,���`a
���`k           ���`lorientations���aoa=���`a[���bmia1���`a,���`a ���bmia0���`a,���`a ���aoa-���bmia1���`a,���`a ���aoa-���bmia1���`a,���`a ���aoa-���bmia1���`a]���`a,���`a ���`eprior���aoa=���bmia3���`a,���`a ���`gconnect���aoa=���`a(���bmia3���`a,���`a ���bmia1���`a)���`a)���`a
���`fsankey���aoa.���`cadd���`a(���`jpatchlabel���aoa=���bs1a'���bseb\n���bseb\n���bseb\n���bs1iTurbine 1���bs1a'���`a,���`a ���`ifacecolor���aoa=���bs1a'���bs1g#37c959���bs1a'���`a,���`a
���`k           ���`eflows���aoa=���`a[���`dHdot���`a[���bmia0���`a]���`a,���`a ���aoa-���`dHdot���`a[���bmib16���`a]���`a,���`a ���aoa-���`dHdot���`a[���bmia1���`a]���`a,���`a ���aoa-���`dHdot���`a[���bmia2���`a]���`a]���`a,���`a
���`k           ���`flabels���aoa=���`a[���bs1a'���bs1a'���`a,���`a ���bkcdNone���`a,���`a ���bkcdNone���`a,���`a ���bkcdNone���`a]���`a,���`a
���`k           ���`kpathlengths���aoa=���`a[���bmfd0.25���`a,���`a ���bmfe0.153���`a,���`a ���bmfe1.543���`a,���`a ���bmfd0.25���`a]���`a,���`a
���`k           ���`lorientations���aoa=���`a[���bmia0���`a,���`a ���bmia1���`a,���`a ���aoa-���bmia1���`a,���`a ���aoa-���bmia1���`a]���`a,���`a ���`eprior���aoa=���bmia5���`a,���`a ���`gconnect���aoa=���`a(���bmia4���`a,���`a ���bmia0���`a)���`a)���`a
���`fsankey���aoa.���`cadd���`a(���`jpatchlabel���aoa=���bs1a'���bseb\n���bseb\n���bseb\n���bs1fReheat���bs1a'���`a,���`a ���`ifacecolor���aoa=���bs1a'���bs1g#37c959���bs1a'���`a,���`a
���`k           ���`eflows���aoa=���`a[���`dHdot���`a[���bmia2���`a]���`a,���`a ���aoa-���`dHdot���`a[���bmia2���`a]���`a]���`a,���`a
���`k           ���`flabels���aoa=���`a[���bkcdNone���`a,���`a ���bkcdNone���`a]���`a,���`a
���`k           ���`kpathlengths���aoa=���`a[���bmfe0.725���`a,���`a ���bmfd0.25���`a]���`a,���`a
���`k           ���`lorientations���aoa=���`a[���aoa-���bmia1���`a,���`a ���bmia0���`a]���`a,���`a ���`eprior���aoa=���bmia6���`a,���`a ���`gconnect���aoa=���`a(���bmia3���`a,���`a ���bmia0���`a)���`a)���`a
���`fsankey���aoa.���`cadd���`a(���`jpatchlabel���aoa=���bs1a'���bs1iTurbine 2���bs1a'���`a,���`a ���`ktrunklength���aoa=���bmfe3.212���`a,���`a ���`ifacecolor���aoa=���bs1a'���bs1g#37c959���bs1a'���`a,���`a
���`k           ���`eflows���aoa=���`a[���`dHdot���`a[���bmia3���`a]���`a,���`a ���`dHdot���`a[���bmib16���`a]���`a,���`a ���aoa-���`dHdot���`a[���bmia5���`a]���`a,���`a ���aoa-���`dHdot���`a[���bmia4���`a]���`a,���`a ���aoa-���`dHdot���`a[���bmib17���`a]���`a]���`a,���`a
���`k           ���`flabels���aoa=���`a[���bkcdNone���`a,���`a ���bs1a'���bs1kShaft power���bs1a'���`a,���`a ���bkcdNone���`a,���`a ���bs1a'���bs1a'���`a,���`a ���bs1a'���bs1kShaft power���bs1a'���`a]���`a,���`a
���`k           ���`kpathlengths���aoa=���`a[���bmfe0.751���`a,���`a ���bmfd0.15���`a,���`a ���bmfd0.25���`a,���`a ���bmfd1.93���`a,���`a ���bmfd0.25���`a]���`a,���`a
���`k           ���`lorientations���aoa=���`a[���bmia0���`a,���`a ���aoa-���bmia1���`a,���`a ���bmia0���`a,���`a ���aoa-���bmia1���`a,���`a ���bmia1���`a]���`a,���`a ���`eprior���aoa=���bmia6���`a,���`a ���`gconnect���aoa=���`a(���bmia1���`a,���`a ���bmia1���`a)���`a)���`a
���`fsankey���aoa.���`cadd���`a(���`jpatchlabel���aoa=���bs1a'���bs1iCondenser���bs1a'���`a,���`a ���`ifacecolor���aoa=���bs1a'���bs1g#58b1fa���bs1a'���`a,���`a ���`ktrunklength���aoa=���bmfe1.764���`a,���`a
���`k           ���`eflows���aoa=���`a[���`dHdot���`a[���bmia5���`a]���`a,���`a ���aoa-���`dHdot���`a[���bmib18���`a]���`a,���`a ���aoa-���`dHdot���`a[���bmia6���`a]���`a]���`a,���`a
���`k           ���`flabels���aoa=���`a[���bs1a'���bs1a'���`a,���`a ���bs1a'���bs1iHeat rate���bs1a'���`a,���`a ���bkcdNone���`a]���`a,���`a
���`k           ���`kpathlengths���aoa=���`a[���bmfd0.45���`a,���`a ���bmfd0.25���`a,���`a ���bmfe0.883���`a]���`a,���`a
���`k           ���`lorientations���aoa=���`a[���aoa-���bmia1���`a,���`a ���bmia1���`a,���`a ���bmia0���`a]���`a,���`a ���`eprior���aoa=���bmia8���`a,���`a ���`gconnect���aoa=���`a(���bmia2���`a,���`a ���bmia0���`a)���`a)���`a
���`hdiagrams���`a ���aoa=���`a ���`fsankey���aoa.���`ffinish���`a(���`a)���`a
���akcfor���`a ���`gdiagram���`a ���bowbin���`a ���`hdiagrams���`a:���`a
���`d    ���`gdiagram���aoa.���`dtext���aoa.���`nset_fontweight���`a(���bs1a'���bs1dbold���bs1a'���`a)���`a
���`d    ���`gdiagram���aoa.���`dtext���aoa.���`lset_fontsize���`a(���bs1a'���bs1b10���bs1a'���`a)���`a
���`d    ���akcfor���`a ���`dtext���`a ���bowbin���`a ���`gdiagram���aoa.���`etexts���`a:���`a
���`h        ���`dtext���aoa.���`lset_fontsize���`a(���bs1a'���bs1b10���bs1a'���`a)���`a
���bc1xI# Notice that the explicit connections are handled automatically, but the���`a
���bc1xK# implicit ones currently are not.  The lengths of the paths and the trunks���`a
���bc1x6# must be adjusted manually, and that is a bit tricky.���`a
���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
���`a
���`a
���bc1xM#############################################################################���`a
���bc1a#���`a
���bc1x# .. admonition:: References���`a
���bc1a#���`a
���bc1xN#    The use of the following functions, methods, classes and modules is shown���`a
���bc1u#    in this example:���`a
���bc1a#���`a
���bc1x#    - `matplotlib.sankey`���`a
���bc1x!#    - `matplotlib.sankey.Sankey`���`a
���bc1x%#    - `matplotlib.sankey.Sankey.add`���`a
���bc1x(#    - `matplotlib.sankey.Sankey.finish`���`a
`dNone�