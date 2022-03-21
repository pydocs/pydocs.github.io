��������C���bsdx�"""
==================
Animated histogram
==================

Use histogram's `.BarContainer` to draw a bunch of rectangles for an animated
histogram.
"""���`a
���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnianimation���`a ���akbas���`a ���bnnianimation���`a
���`a
���bc1x)# Fixing random state for reproducibility���`a
���`bnp���aoa.���`frandom���aoa.���`dseed���`a(���bmih19680801���`a)���`a
���bc1r# Fixing bin edges���`a
���`iHIST_BINS���`a ���aoa=���`a ���`bnp���aoa.���`hlinspace���`a(���aoa-���bmia4���`a,���`a ���bmia4���`a,���`a ���bmic100���`a)���`a
���`a
���bc1x# histogram our data with numpy���`a
���`ddata���`a ���aoa=���`a ���`bnp���aoa.���`frandom���aoa.���`erandn���`a(���bmid1000���`a)���`a
���`an���`a,���`a ���`a_���`a ���aoa=���`a ���`bnp���aoa.���`ihistogram���`a(���`ddata���`a,���`a ���`iHIST_BINS���`a)���`a
���`a
���bc1xO###############################################################################���`a
���bc1xL# To animate the histogram, we need an ``animate`` function, which generates���`a
���bc1xM# a random set of numbers and updates the heights of rectangles. We utilize a���`a
���bc1xK# python closure to track an instance of `.BarContainer` whose `.Rectangle`���`a
���bc1x# patches we shall update.���`a
���`a
���`a
���akcdef���`a ���bnfqprepare_animation���`a(���`mbar_container���`a)���`a:���`a
���`a
���`d    ���akcdef���`a ���bnfganimate���`a(���`lframe_number���`a)���`a:���`a
���`h        ���bc1x# simulate new data coming in���`a
���`h        ���`ddata���`a ���aoa=���`a ���`bnp���aoa.���`frandom���aoa.���`erandn���`a(���bmid1000���`a)���`a
���`h        ���`an���`a,���`a ���`a_���`a ���aoa=���`a ���`bnp���aoa.���`ihistogram���`a(���`ddata���`a,���`a ���`iHIST_BINS���`a)���`a
���`h        ���akcfor���`a ���`ecount���`a,���`a ���`drect���`a ���bowbin���`a ���bnbczip���`a(���`an���`a,���`a ���`mbar_container���aoa.���`gpatches���`a)���`a:���`a
���`l            ���`drect���aoa.���`jset_height���`a(���`ecount���`a)���`a
���`h        ���akfreturn���`a ���`mbar_container���aoa.���`gpatches���`a
���`d    ���akfreturn���`a ���`ganimate���`a
���`a
���bc1xO###############################################################################���`a
���bc1xG# Using :func:`~matplotlib.pyplot.hist` allows us to get an instance of���`a
���bc1xK# `.BarContainer`, which is a collection of `.Rectangle` instances. Calling���`a
���bc1xN# ``prepare_animation`` will define ``animate`` function working with supplied���`a
���bc1x># `.BarContainer`, all this is used to setup `.FuncAnimation`.���`a
���`a
���`cfig���`a,���`a ���`bax���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`a)���`a
���`a_���`a,���`a ���`a_���`a,���`a ���`mbar_container���`a ���aoa=���`a ���`bax���aoa.���`dhist���`a(���`ddata���`a,���`a ���`iHIST_BINS���`a,���`a ���`blw���aoa=���bmia1���`a,���`a
���`x                              ���`bec���aoa=���bs2a"���bs2fyellow���bs2a"���`a,���`a ���`bfc���aoa=���bs2a"���bs2egreen���bs2a"���`a,���`a ���`ealpha���aoa=���bmfc0.5���`a)���`a
���`bax���aoa.���`hset_ylim���`a(���`ctop���aoa=���bmib55���`a)���`b  ���bc1x4# set safe limit to ensure that all data is visible.���`a
���`a
���`cani���`a ���aoa=���`a ���`ianimation���aoa.���`mFuncAnimation���`a(���`cfig���`a,���`a ���`qprepare_animation���`a(���`mbar_container���`a)���`a,���`a ���bmib50���`a,���`a
���`x                              ���`frepeat���aoa=���bkceFalse���`a,���`a ���`dblit���aoa=���bkcdTrue���`a)���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
`dNone�