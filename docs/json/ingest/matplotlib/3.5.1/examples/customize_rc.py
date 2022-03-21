������������bsdyE"""
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
"""���`a
���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���`a
���`cplt���aoa.���`gsubplot���`a(���bmic311���`a)���`a
���`cplt���aoa.���`dplot���`a(���`a[���bmia1���`a,���`a ���bmia2���`a,���`a ���bmia3���`a]���`a)���`a
���`a
���bc1x?# the axes attributes need to be set before the call to subplot���`a
���`cplt���aoa.���`hrcParams���aoa.���`fupdate���`a(���`a{���`a
���`d    ���bs2a"���bs2kfont.weight���bs2a"���`a:���`a ���bs2a"���bs2dbold���bs2a"���`a,���`a
���`d    ���bs2a"���bs2pxtick.major.size���bs2a"���`a:���`a ���bmia5���`a,���`a
���`d    ���bs2a"���bs2oxtick.major.pad���bs2a"���`a:���`a ���bmia7���`a,���`a
���`d    ���bs2a"���bs2oxtick.labelsize���bs2a"���`a:���`a ���bmib15���`a,���`a
���`d    ���bs2a"���bs2jgrid.color���bs2a"���`a:���`a ���bs2a"���bs2c0.5���bs2a"���`a,���`a
���`d    ���bs2a"���bs2ngrid.linestyle���bs2a"���`a:���`a ���bs2a"���bs2a-���bs2a"���`a,���`a
���`d    ���bs2a"���bs2ngrid.linewidth���bs2a"���`a:���`a ���bmia5���`a,���`a
���`d    ���bs2a"���bs2olines.linewidth���bs2a"���`a:���`a ���bmia2���`a,���`a
���`d    ���bs2a"���bs2klines.color���bs2a"���`a:���`a ���bs2a"���bs2ag���bs2a"���`a,���`a
���`a}���`a)���`a
���`cplt���aoa.���`gsubplot���`a(���bmic312���`a)���`a
���`cplt���aoa.���`dplot���`a(���`a[���bmia1���`a,���`a ���bmia2���`a,���`a ���bmia3���`a]���`a)���`a
���`cplt���aoa.���`dgrid���`a(���bkcdTrue���`a)���`a
���`a
���`cplt���aoa.���`jrcdefaults���`a(���`a)���`a
���`cplt���aoa.���`gsubplot���`a(���bmic313���`a)���`a
���`cplt���aoa.���`dplot���`a(���`a[���bmia1���`a,���`a ���bmia2���`a,���`a ���bmia3���`a]���`a)���`a
���`cplt���aoa.���`dgrid���`a(���bkcdTrue���`a)���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
`dNone�