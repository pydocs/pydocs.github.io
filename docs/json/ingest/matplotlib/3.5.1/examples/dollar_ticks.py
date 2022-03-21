������������bsdx}"""
============
Dollar Ticks
============

Use a `~.ticker.FormatStrFormatter` to prepend dollar signs on y axis labels.
"""���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���`a
���bc1x)# Fixing random state for reproducibility���`a
���`bnp���aoa.���`frandom���aoa.���`dseed���`a(���bmih19680801���`a)���`a
���`a
���`cfig���`a,���`a ���`bax���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`a)���`a
���`bax���aoa.���`dplot���`a(���bmic100���aoa*���`bnp���aoa.���`frandom���aoa.���`drand���`a(���bmib20���`a)���`a)���`a
���`a
���bc1x"# Use automatic StrMethodFormatter���`a
���`bax���aoa.���`eyaxis���aoa.���`sset_major_formatter���`a(���bs1a'���bs1a$���bsih{x:1.2f}���bs1a'���`a)���`a
���`a
���`bax���aoa.���`eyaxis���aoa.���`oset_tick_params���`a(���`ewhich���aoa=���bs1a'���bs1emajor���bs1a'���`a,���`a ���`jlabelcolor���aoa=���bs1a'���bs1egreen���bs1a'���`a,���`a
���`x                         ���`ilabelleft���aoa=���bkceFalse���`a,���`a ���`jlabelright���aoa=���bkcdTrue���`a)���`a
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
���bc1x##    - `matplotlib.pyplot.subplots`���`a
���bc1x1#    - `matplotlib.axis.Axis.set_major_formatter`���`a
���bc1x-#    - `matplotlib.axis.Axis.set_tick_params`���`a
���bc1x#    - `matplotlib.axis.Tick`���`a
���bc1x-#    - `matplotlib.ticker.StrMethodFormatter`���`a
`dNone�