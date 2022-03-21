������������bsdx�"""
======
Timers
======

Simple example of using general timer objects. This is used to update
the time placed in the title of the figure.
"""���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���bkndfrom���`a ���bnnhdatetime���`a ���bknfimport���`a ���`hdatetime���`a
���`a
���`a
���akcdef���`a ���bnflupdate_title���`a(���`daxes���`a)���`a:���`a
���`d    ���`daxes���aoa.���`iset_title���`a(���`hdatetime���aoa.���`cnow���`a(���`a)���`a)���`a
���`d    ���`daxes���aoa.���`ffigure���aoa.���`fcanvas���aoa.���`ddraw���`a(���`a)���`a
���`a
���`cfig���`a,���`a ���`bax���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`a)���`a
���`a
���`ax���`a ���aoa=���`a ���`bnp���aoa.���`hlinspace���`a(���aoa-���bmia3���`a,���`a ���bmia3���`a)���`a
���`bax���aoa.���`dplot���`a(���`ax���`a,���`a ���`ax���`a ���aoa*���aoa*���`a ���bmia2���`a)���`a
���`a
���bc1xA# Create a new timer object. Set the interval to 100 milliseconds���`a
���bc1xF# (1000 is default) and tell the timer what function should be called.���`a
���`etimer���`a ���aoa=���`a ���`cfig���aoa.���`fcanvas���aoa.���`inew_timer���`a(���`hinterval���aoa=���bmic100���`a)���`a
���`etimer���aoa.���`ladd_callback���`a(���`lupdate_title���`a,���`a ���`bax���`a)���`a
���`etimer���aoa.���`estart���`a(���`a)���`a
���`a
���bc1x0# Or could start the timer on first figure draw:���`a
���bc1x# def start_timer(event):���`a
���bc1s#     timer.start()���`a
���bc1x'#     fig.canvas.mpl_disconnect(drawid)���`a
���bc1x<# drawid = fig.canvas.mpl_connect('draw_event', start_timer)���`a
���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
`dNone�