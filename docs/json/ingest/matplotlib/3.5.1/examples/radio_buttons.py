������������bsdy!"""
=============
Radio Buttons
=============

Using radio buttons to choose properties of your plot.

Radio buttons let you choose between multiple options in a visualization.
In this case, the buttons let the user choose one of the three different sine
waves to be shown in the plot.
"""���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���bkndfrom���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnngwidgets���`a ���bknfimport���`a ���`lRadioButtons���`a
���`a
���`at���`a ���aoa=���`a ���`bnp���aoa.���`farange���`a(���bmfc0.0���`a,���`a ���bmfc2.0���`a,���`a ���bmfd0.01���`a)���`a
���`bs0���`a ���aoa=���`a ���`bnp���aoa.���`csin���`a(���bmia2���aoa*���`bnp���aoa.���`bpi���aoa*���`at���`a)���`a
���`bs1���`a ���aoa=���`a ���`bnp���aoa.���`csin���`a(���bmia4���aoa*���`bnp���aoa.���`bpi���aoa*���`at���`a)���`a
���`bs2���`a ���aoa=���`a ���`bnp���aoa.���`csin���`a(���bmia8���aoa*���`bnp���aoa.���`bpi���aoa*���`at���`a)���`a
���`a
���`cfig���`a,���`a ���`bax���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`a)���`a
���`al���`a,���`a ���aoa=���`a ���`bax���aoa.���`dplot���`a(���`at���`a,���`a ���`bs0���`a,���`a ���`blw���aoa=���bmia2���`a,���`a ���`ecolor���aoa=���bs1a'���bs1cred���bs1a'���`a)���`a
���`cplt���aoa.���`osubplots_adjust���`a(���`dleft���aoa=���bmfc0.3���`a)���`a
���`a
���`gaxcolor���`a ���aoa=���`a ���bs1a'���bs1tlightgoldenrodyellow���bs1a'���`a
���`crax���`a ���aoa=���`a ���`cplt���aoa.���`daxes���`a(���`a[���bmfd0.05���`a,���`a ���bmfc0.7���`a,���`a ���bmfd0.15���`a,���`a ���bmfd0.15���`a]���`a,���`a ���`ifacecolor���aoa=���`gaxcolor���`a)���`a
���`eradio���`a ���aoa=���`a ���`lRadioButtons���`a(���`crax���`a,���`a ���`a(���bs1a'���bs1d2 Hz���bs1a'���`a,���`a ���bs1a'���bs1d4 Hz���bs1a'���`a,���`a ���bs1a'���bs1d8 Hz���bs1a'���`a)���`a)���`a
���`a
���`a
���akcdef���`a ���bnffhzfunc���`a(���`elabel���`a)���`a:���`a
���`d    ���`fhzdict���`a ���aoa=���`a ���`a{���bs1a'���bs1d2 Hz���bs1a'���`a:���`a ���`bs0���`a,���`a ���bs1a'���bs1d4 Hz���bs1a'���`a:���`a ���`bs1���`a,���`a ���bs1a'���bs1d8 Hz���bs1a'���`a:���`a ���`bs2���`a}���`a
���`d    ���`eydata���`a ���aoa=���`a ���`fhzdict���`a[���`elabel���`a]���`a
���`d    ���`al���aoa.���`iset_ydata���`a(���`eydata���`a)���`a
���`d    ���`cplt���aoa.���`ddraw���`a(���`a)���`a
���`eradio���aoa.���`jon_clicked���`a(���`fhzfunc���`a)���`a
���`a
���`crax���`a ���aoa=���`a ���`cplt���aoa.���`daxes���`a(���`a[���bmfd0.05���`a,���`a ���bmfc0.4���`a,���`a ���bmfd0.15���`a,���`a ���bmfd0.15���`a]���`a,���`a ���`ifacecolor���aoa=���`gaxcolor���`a)���`a
���`fradio2���`a ���aoa=���`a ���`lRadioButtons���`a(���`crax���`a,���`a ���`a(���bs1a'���bs1cred���bs1a'���`a,���`a ���bs1a'���bs1dblue���bs1a'���`a,���`a ���bs1a'���bs1egreen���bs1a'���`a)���`a)���`a
���`a
���`a
���akcdef���`a ���bnficolorfunc���`a(���`elabel���`a)���`a:���`a
���`d    ���`al���aoa.���`iset_color���`a(���`elabel���`a)���`a
���`d    ���`cplt���aoa.���`ddraw���`a(���`a)���`a
���`fradio2���aoa.���`jon_clicked���`a(���`icolorfunc���`a)���`a
���`a
���`crax���`a ���aoa=���`a ���`cplt���aoa.���`daxes���`a(���`a[���bmfd0.05���`a,���`a ���bmfc0.1���`a,���`a ���bmfd0.15���`a,���`a ���bmfd0.15���`a]���`a,���`a ���`ifacecolor���aoa=���`gaxcolor���`a)���`a
���`fradio3���`a ���aoa=���`a ���`lRadioButtons���`a(���`crax���`a,���`a ���`a(���bs1a'���bs1a-���bs1a'���`a,���`a ���bs1a'���bs1b--���bs1a'���`a,���`a ���bs1a'���bs1b-.���bs1a'���`a,���`a ���bs1a'���bs1esteps���bs1a'���`a,���`a ���bs1a'���bs1a:���bs1a'���`a)���`a)���`a
���`a
���`a
���akcdef���`a ���bnfistylefunc���`a(���`elabel���`a)���`a:���`a
���`d    ���`al���aoa.���`mset_linestyle���`a(���`elabel���`a)���`a
���`d    ���`cplt���aoa.���`ddraw���`a(���`a)���`a
���`fradio3���aoa.���`jon_clicked���`a(���`istylefunc���`a)���`a
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
���bc1x(#    - `matplotlib.widgets.RadioButtons`���`a
`dNone�