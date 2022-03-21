Ù¯‚Ù´ƒ˜ÒÙ±‚bsdyE"""
============
Customize Rc
============

I'm not trying to make a good looking figure here, but just to show
some examples of customizing `.rcParams` on the fly.

If you like to work interactively, and need to create different sets
of defaults for figures (e.g., one set of defaults for publication, one
set for interactive exploration), you may want to define some
functions in a custom module that set the defaults, e.g.,::

    def set_pub():
        rcParams.update({
            "font.weight": "bold",  # bold fonts
            "tick.labelsize": 15,   # large tick labels
            "lines.linewidth": 1,   # thick lines
            "lines.color": "k",     # black lines
            "grid.color": "0.5",    # gray gridlines
            "grid.linestyle": "-",  # solid gridlines
            "grid.linewidth": 0.5,  # thin gridlines
            "savefig.dpi": 300,     # higher resolution output.
        })

Then as you are working interactively, you just need to do::

    >>> set_pub()
    >>> plot([1, 2, 3])
    >>> savefig('myfig')
    >>> rcdefaults()  # restore the defaults
"""Ù±‚`a
Ù±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnnfpyplotÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnncpltÙ±‚`a
Ù±‚`a
Ù±‚`cpltÙ±‚aoa.Ù±‚`gsubplotÙ±‚`a(Ù±‚bmic311Ù±‚`a)Ù±‚`a
Ù±‚`cpltÙ±‚aoa.Ù±‚`dplotÙ±‚`a(Ù±‚`a[Ù±‚bmia1Ù±‚`a,Ù±‚`a Ù±‚bmia2Ù±‚`a,Ù±‚`a Ù±‚bmia3Ù±‚`a]Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚bc1x?# the axes attributes need to be set before the call to subplotÙ±‚`a
Ù±‚`cpltÙ±‚aoa.Ù±‚`hrcParamsÙ±‚aoa.Ù±‚`fupdateÙ±‚`a(Ù±‚`a{Ù±‚`a
Ù±‚`d    Ù±‚bs2a"Ù±‚bs2kfont.weightÙ±‚bs2a"Ù±‚`a:Ù±‚`a Ù±‚bs2a"Ù±‚bs2dboldÙ±‚bs2a"Ù±‚`a,Ù±‚`a
Ù±‚`d    Ù±‚bs2a"Ù±‚bs2pxtick.major.sizeÙ±‚bs2a"Ù±‚`a:Ù±‚`a Ù±‚bmia5Ù±‚`a,Ù±‚`a
Ù±‚`d    Ù±‚bs2a"Ù±‚bs2oxtick.major.padÙ±‚bs2a"Ù±‚`a:Ù±‚`a Ù±‚bmia7Ù±‚`a,Ù±‚`a
Ù±‚`d    Ù±‚bs2a"Ù±‚bs2oxtick.labelsizeÙ±‚bs2a"Ù±‚`a:Ù±‚`a Ù±‚bmib15Ù±‚`a,Ù±‚`a
Ù±‚`d    Ù±‚bs2a"Ù±‚bs2jgrid.colorÙ±‚bs2a"Ù±‚`a:Ù±‚`a Ù±‚bs2a"Ù±‚bs2c0.5Ù±‚bs2a"Ù±‚`a,Ù±‚`a
Ù±‚`d    Ù±‚bs2a"Ù±‚bs2ngrid.linestyleÙ±‚bs2a"Ù±‚`a:Ù±‚`a Ù±‚bs2a"Ù±‚bs2a-Ù±‚bs2a"Ù±‚`a,Ù±‚`a
Ù±‚`d    Ù±‚bs2a"Ù±‚bs2ngrid.linewidthÙ±‚bs2a"Ù±‚`a:Ù±‚`a Ù±‚bmia5Ù±‚`a,Ù±‚`a
Ù±‚`d    Ù±‚bs2a"Ù±‚bs2olines.linewidthÙ±‚bs2a"Ù±‚`a:Ù±‚`a Ù±‚bmia2Ù±‚`a,Ù±‚`a
Ù±‚`d    Ù±‚bs2a"Ù±‚bs2klines.colorÙ±‚bs2a"Ù±‚`a:Ù±‚`a Ù±‚bs2a"Ù±‚bs2agÙ±‚bs2a"Ù±‚`a,Ù±‚`a
Ù±‚`a}Ù±‚`a)Ù±‚`a
Ù±‚`cpltÙ±‚aoa.Ù±‚`gsubplotÙ±‚`a(Ù±‚bmic312Ù±‚`a)Ù±‚`a
Ù±‚`cpltÙ±‚aoa.Ù±‚`dplotÙ±‚`a(Ù±‚`a[Ù±‚bmia1Ù±‚`a,Ù±‚`a Ù±‚bmia2Ù±‚`a,Ù±‚`a Ù±‚bmia3Ù±‚`a]Ù±‚`a)Ù±‚`a
Ù±‚`cpltÙ±‚aoa.Ù±‚`dgridÙ±‚`a(Ù±‚bkcdTrueÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`cpltÙ±‚aoa.Ù±‚`jrcdefaultsÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`cpltÙ±‚aoa.Ù±‚`gsubplotÙ±‚`a(Ù±‚bmic313Ù±‚`a)Ù±‚`a
Ù±‚`cpltÙ±‚aoa.Ù±‚`dplotÙ±‚`a(Ù±‚`a[Ù±‚bmia1Ù±‚`a,Ù±‚`a Ù±‚bmia2Ù±‚`a,Ù±‚`a Ù±‚bmia3Ù±‚`a]Ù±‚`a)Ù±‚`a
Ù±‚`cpltÙ±‚aoa.Ù±‚`dgridÙ±‚`a(Ù±‚bkcdTrueÙ±‚`a)Ù±‚`a
Ù±‚`cpltÙ±‚aoa.Ù±‚`dshowÙ±‚`a(Ù±‚`a)Ù±‚`a
`dNoneö