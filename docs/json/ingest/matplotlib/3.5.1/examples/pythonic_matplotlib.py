ŸØÇÅŸ¥Éò›Ÿ±Çbsdy """
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
"""Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±ÇbknfimportŸ±Ç`a Ÿ±ÇbnnŸ¢ÑjmatplotlibŸ†Ñjmatplotlibe3.5.1fmodulejmatplotlibfmoduleıŸ±Çbnna.Ÿ±ÇbnnfpyplotŸ±Ç`a Ÿ±ÇakbasŸ±Ç`a Ÿ±ÇbnncpltŸ±Ç`a
Ÿ±ÇbknfimportŸ±Ç`a Ÿ±ÇbnnŸ¢ÑenumpyŸ†Ñenumpyf1.22.3fmoduleenumpyfmoduleıŸ±Ç`a Ÿ±ÇakbasŸ±Ç`a Ÿ±ÇbnnbnpŸ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`atŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`farangeŸ±Ç`a(Ÿ±Çbmfc0.0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfc1.0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd0.01Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`cfigŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`a(Ÿ±Ç`cax1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`cax2Ÿ±Ç`a)Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`hsubplotsŸ±Ç`a(Ÿ±Çbmia2Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`cax1Ÿ±Çaoa.Ÿ±Ç`dplotŸ±Ç`a(Ÿ±Ç`atŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`csinŸ±Ç`a(Ÿ±Çbmia2Ÿ±Çaoa*Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`bpiŸ±Ç`a Ÿ±Çaoa*Ÿ±Ç`a Ÿ±Ç`atŸ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cax1Ÿ±Çaoa.Ÿ±Ç`dgridŸ±Ç`a(Ÿ±ÇbkcdTrueŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cax1Ÿ±Çaoa.Ÿ±Ç`hset_ylimŸ±Ç`a(Ÿ±Ç`a(Ÿ±Çaoa-Ÿ±Çbmia2Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia2Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cax1Ÿ±Çaoa.Ÿ±Ç`jset_ylabelŸ±Ç`a(Ÿ±Çbs1a'Ÿ±Çbs1d1 HzŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cax1Ÿ±Çaoa.Ÿ±Ç`iset_titleŸ±Ç`a(Ÿ±Çbs1a'Ÿ±Çbs1rA sine wave or twoŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`cax1Ÿ±Çaoa.Ÿ±Ç`exaxisŸ±Çaoa.Ÿ±Ç`oset_tick_paramsŸ±Ç`a(Ÿ±Ç`jlabelcolorŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1arŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`cax2Ÿ±Çaoa.Ÿ±Ç`dplotŸ±Ç`a(Ÿ±Ç`atŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`csinŸ±Ç`a(Ÿ±Çbmia2Ÿ±Ç`a Ÿ±Çaoa*Ÿ±Ç`a Ÿ±Çbmia2Ÿ±Çaoa*Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`bpiŸ±Ç`a Ÿ±Çaoa*Ÿ±Ç`a Ÿ±Ç`atŸ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cax2Ÿ±Çaoa.Ÿ±Ç`dgridŸ±Ç`a(Ÿ±ÇbkcdTrueŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cax2Ÿ±Çaoa.Ÿ±Ç`hset_ylimŸ±Ç`a(Ÿ±Ç`a(Ÿ±Çaoa-Ÿ±Çbmia2Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia2Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`alŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cax2Ÿ±Çaoa.Ÿ±Ç`jset_xlabelŸ±Ç`a(Ÿ±Çbs1a'Ÿ±Çbs1fHi momŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`alŸ±Çaoa.Ÿ±Ç`iset_colorŸ±Ç`a(Ÿ±Çbs1a'Ÿ±Çbs1agŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`alŸ±Çaoa.Ÿ±Ç`lset_fontsizeŸ±Ç`a(Ÿ±Çbs1a'Ÿ±Çbs1elargeŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`dshowŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
`dNoneˆ