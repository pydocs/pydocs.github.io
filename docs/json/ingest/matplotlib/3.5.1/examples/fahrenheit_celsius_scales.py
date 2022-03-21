������������bsdx�"""
=================================
Different scales on the same axes
=================================

Demo of how to display two scales on the left and right y axis.

This example uses the Fahrenheit and Celsius scales.
"""���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���`a
���`a
���akcdef���`a ���bnfrfahrenheit2celsius���`a(���`dtemp���`a)���`a:���`a
���`d    ���bsdxL"""
    Returns temperature in Celsius given Fahrenheit temperature.
    """���`a
���`d    ���akfreturn���`a ���`a(���bmfb5.���`a ���aoa/���`a ���bmfb9.���`a)���`a ���aoa*���`a ���`a(���`dtemp���`a ���aoa-���`a ���bmib32���`a)���`a
���`a
���`a
���akcdef���`a ���bnfimake_plot���`a(���`a)���`a:���`a
���`a
���`d    ���bc1x5# Define a closure function to register as a callback���`a
���`d    ���akcdef���`a ���bnfwconvert_ax_c_to_celsius���`a(���`dax_f���`a)���`a:���`a
���`h        ���bsdxE"""
        Update second axis according with first axis.
        """���`a
���`h        ���`by1���`a,���`a ���`by2���`a ���aoa=���`a ���`dax_f���aoa.���`hget_ylim���`a(���`a)���`a
���`h        ���`dax_c���aoa.���`hset_ylim���`a(���`rfahrenheit2celsius���`a(���`by1���`a)���`a,���`a ���`rfahrenheit2celsius���`a(���`by2���`a)���`a)���`a
���`h        ���`dax_c���aoa.���`ffigure���aoa.���`fcanvas���aoa.���`ddraw���`a(���`a)���`a
���`a
���`d    ���`cfig���`a,���`a ���`dax_f���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`a)���`a
���`d    ���`dax_c���`a ���aoa=���`a ���`dax_f���aoa.���`etwinx���`a(���`a)���`a
���`a
���`d    ���bc1x<# automatically update ylim of ax2 when ylim of ax1 changes.���`a
���`d    ���`dax_f���aoa.���`icallbacks���aoa.���`gconnect���`a(���bs2a"���bs2lylim_changed���bs2a"���`a,���`a ���`wconvert_ax_c_to_celsius���`a)���`a
���`d    ���`dax_f���aoa.���`dplot���`a(���`bnp���aoa.���`hlinspace���`a(���aoa-���bmib40���`a,���`a ���bmic120���`a,���`a ���bmic100���`a)���`a)���`a
���`d    ���`dax_f���aoa.���`hset_xlim���`a(���bmia0���`a,���`a ���bmic100���`a)���`a
���`a
���`d    ���`dax_f���aoa.���`iset_title���`a(���bs1a'���bs1x"Two scales: Fahrenheit and Celsius���bs1a'���`a)���`a
���`d    ���`dax_f���aoa.���`jset_ylabel���`a(���bs1a'���bs1jFahrenheit���bs1a'���`a)���`a
���`d    ���`dax_c���aoa.���`jset_ylabel���`a(���bs1a'���bs1gCelsius���bs1a'���`a)���`a
���`a
���`d    ���`cplt���aoa.���`dshow���`a(���`a)���`a
���`a
���`imake_plot���`a(���`a)���`a
`dNone�