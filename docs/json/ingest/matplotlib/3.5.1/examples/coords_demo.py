������������bsdx�"""
===========================
Mouse move and click events
===========================

An example of how to interact with the plotting canvas by connecting to move
and click events.
"""���`a
���`a
���bkndfrom���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnmbackend_bases���`a ���bknfimport���`a ���`kMouseButton���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���`a
���`at���`a ���aoa=���`a ���`bnp���aoa.���`farange���`a(���bmfc0.0���`a,���`a ���bmfc1.0���`a,���`a ���bmfd0.01���`a)���`a
���`as���`a ���aoa=���`a ���`bnp���aoa.���`csin���`a(���bmia2���`a ���aoa*���`a ���`bnp���aoa.���`bpi���`a ���aoa*���`a ���`at���`a)���`a
���`cfig���`a,���`a ���`bax���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`a)���`a
���`bax���aoa.���`dplot���`a(���`at���`a,���`a ���`as���`a)���`a
���`a
���`a
���akcdef���`a ���bnfgon_move���`a(���`eevent���`a)���`a:���`a
���`d    ���bc1x# get the x and y pixel coords���`a
���`d    ���`ax���`a,���`a ���`ay���`a ���aoa=���`a ���`eevent���aoa.���`ax���`a,���`a ���`eevent���aoa.���`ay���`a
���`d    ���akbif���`a ���`eevent���aoa.���`finaxes���`a:���`a
���`h        ���`bax���`a ���aoa=���`a ���`eevent���aoa.���`finaxes���`b  ���bc1s# the axes instance���`a
���`h        ���bnbeprint���`a(���bs1a'���bs1ldata coords ���bsib%f���bs1a ���bsib%f���bs1a'���`a ���aoa%���`a ���`a(���`eevent���aoa.���`exdata���`a,���`a ���`eevent���aoa.���`eydata���`a)���`a)���`a
���`a
���`a
���akcdef���`a ���bnfhon_click���`a(���`eevent���`a)���`a:���`a
���`d    ���akbif���`a ���`eevent���aoa.���`fbutton���`a ���bowbis���`a ���`kMouseButton���aoa.���`dLEFT���`a:���`a
���`h        ���bnbeprint���`a(���bs1a'���bs1vdisconnecting callback���bs1a'���`a)���`a
���`h        ���`cplt���aoa.���`jdisconnect���`a(���`jbinding_id���`a)���`a
���`a
���`a
���`jbinding_id���`a ���aoa=���`a ���`cplt���aoa.���`gconnect���`a(���bs1a'���bs1smotion_notify_event���bs1a'���`a,���`a ���`gon_move���`a)���`a
���`cplt���aoa.���`gconnect���`a(���bs1a'���bs1rbutton_press_event���bs1a'���`a,���`a ���`hon_click���`a)���`a
���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
`dNone�