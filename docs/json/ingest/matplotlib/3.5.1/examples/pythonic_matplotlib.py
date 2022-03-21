������������bsdy�"""
===================
Pythonic Matplotlib
===================

Some people prefer to write more pythonic, object-oriented code
rather than use the pyplot interface to matplotlib.  This example shows
you how.

Unless you are an application developer, I recommend using part of the
pyplot interface, particularly the figure, close, subplot, axes, and
show commands.  These hide a lot of complexity from you that you don't
need to see in normal figure creation, like instantiating DPI
instances, managing the bounding boxes of the figure elements,
creating and realizing GUI windows and embedding figures in them.

If you are an application developer and want to embed matplotlib in
your application, follow the lead of examples/embedding_in_wx.py,
examples/embedding_in_gtk.py or examples/embedding_in_tk.py.  In this
case you will want to control the creation of all your figures,
embedding them in application windows, etc.

If you are a web application developer, you may want to use the
example in webapp_demo.py, which shows how to use the backend agg
figure canvas directly, with none of the globals (current figure,
current axes) that are present in the pyplot interface.  Note that
there is no reason why the pyplot interface won't work for web
application developers, however.

If you see an example in the examples dir written in pyplot interface,
and you want to emulate that using the true python method calls, there
is an easy mapping.  Many of those examples use 'set' to control
figure properties.  Here's how to map those commands onto instance
methods

The syntax of set is::

    plt.setp(object or sequence, somestring, attribute)

if called with an object, set calls::

    object.set_somestring(attribute)

if called with a sequence, set does::

    for object in sequence:
       object.set_somestring(attribute)

So for your example, if a is your axes object, you can do::

    a.set_xticklabels([])
    a.set_yticklabels([])
    a.set_xticks([])
    a.set_yticks([])
"""���`a
���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���`a
���`at���`a ���aoa=���`a ���`bnp���aoa.���`farange���`a(���bmfc0.0���`a,���`a ���bmfc1.0���`a,���`a ���bmfd0.01���`a)���`a
���`a
���`cfig���`a,���`a ���`a(���`cax1���`a,���`a ���`cax2���`a)���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���bmia2���`a)���`a
���`a
���`cax1���aoa.���`dplot���`a(���`at���`a,���`a ���`bnp���aoa.���`csin���`a(���bmia2���aoa*���`bnp���aoa.���`bpi���`a ���aoa*���`a ���`at���`a)���`a)���`a
���`cax1���aoa.���`dgrid���`a(���bkcdTrue���`a)���`a
���`cax1���aoa.���`hset_ylim���`a(���`a(���aoa-���bmia2���`a,���`a ���bmia2���`a)���`a)���`a
���`cax1���aoa.���`jset_ylabel���`a(���bs1a'���bs1d1 Hz���bs1a'���`a)���`a
���`cax1���aoa.���`iset_title���`a(���bs1a'���bs1rA sine wave or two���bs1a'���`a)���`a
���`a
���`cax1���aoa.���`exaxis���aoa.���`oset_tick_params���`a(���`jlabelcolor���aoa=���bs1a'���bs1ar���bs1a'���`a)���`a
���`a
���`cax2���aoa.���`dplot���`a(���`at���`a,���`a ���`bnp���aoa.���`csin���`a(���bmia2���`a ���aoa*���`a ���bmia2���aoa*���`bnp���aoa.���`bpi���`a ���aoa*���`a ���`at���`a)���`a)���`a
���`cax2���aoa.���`dgrid���`a(���bkcdTrue���`a)���`a
���`cax2���aoa.���`hset_ylim���`a(���`a(���aoa-���bmia2���`a,���`a ���bmia2���`a)���`a)���`a
���`al���`a ���aoa=���`a ���`cax2���aoa.���`jset_xlabel���`a(���bs1a'���bs1fHi mom���bs1a'���`a)���`a
���`al���aoa.���`iset_color���`a(���bs1a'���bs1ag���bs1a'���`a)���`a
���`al���aoa.���`lset_fontsize���`a(���bs1a'���bs1elarge���bs1a'���`a)���`a
���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
`dNone�