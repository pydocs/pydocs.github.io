��������H���bsdy1"""
==========
Evans test
==========

A mockup "Foo" units class which supports conversion and different tick
formatting depending on the "unit".  Here the "unit" is just a scalar
conversion factor, but this example shows that Matplotlib is entirely agnostic
to what kind of units client packages use.
"""���`a
���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnneunits���`a ���akbas���`a ���bnneunits���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfticker���`a ���akbas���`a ���bnnfticker���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���`a
���`a
���akeclass���`a ���bnccFoo���`a:���`a
���`d    ���akcdef���`a ���bfmh__init__���`a(���bbpdself���`a,���`a ���`cval���`a,���`a ���`dunit���aoa=���bmfc1.0���`a)���`a:���`a
���`h        ���bbpdself���aoa.���`dunit���`a ���aoa=���`a ���`dunit���`a
���`h        ���bbpdself���aoa.���`d_val���`a ���aoa=���`a ���`cval���`a ���aoa*���`a ���`dunit���`a
���`a
���`d    ���akcdef���`a ���bnfevalue���`a(���bbpdself���`a,���`a ���`dunit���`a)���`a:���`a
���`h        ���akbif���`a ���`dunit���`a ���bowbis���`a ���bkcdNone���`a:���`a
���`l            ���`dunit���`a ���aoa=���`a ���bbpdself���aoa.���`dunit���`a
���`h        ���akfreturn���`a ���bbpdself���aoa.���`d_val���`a ���aoa/���`a ���`dunit���`a
���`a
���`a
���akeclass���`a ���bnclFooConverter���`a(���`eunits���aoa.���`sConversionInterface���`a)���`a:���`a
���`d    ���bndm@staticmethod���`a
���`d    ���akcdef���`a ���bnfhaxisinfo���`a(���`dunit���`a,���`a ���`daxis���`a)���`a:���`a
���`h        ���bsdx"""Return the Foo AxisInfo."""���`a
���`h        ���akbif���`a ���`dunit���`a ���aob==���`a ���bmfc1.0���`a ���bowbor���`a ���`dunit���`a ���aob==���`a ���bmfc2.0���`a:���`a
���`l            ���akfreturn���`a ���`eunits���aoa.���`hAxisInfo���`a(���`a
���`p                ���`fmajloc���aoa=���`fticker���aoa.���`lIndexLocator���`a(���bmia8���`a,���`a ���bmia0���`a)���`a,���`a
���`p                ���`fmajfmt���aoa=���`fticker���aoa.���`rFormatStrFormatter���`a(���bs2a"���bs2eVAL: ���bsib%s���bs2a"���`a)���`a,���`a
���`p                ���`elabel���aoa=���bs1a'���bs1cfoo���bs1a'���`a,���`a
���`p                ���`a)���`a
���`a
���`h        ���akdelse���`a:���`a
���`l            ���akfreturn���`a ���bkcdNone���`a
���`a
���`d    ���bndm@staticmethod���`a
���`d    ���akcdef���`a ���bnfgconvert���`a(���`cobj���`a,���`a ���`dunit���`a,���`a ���`daxis���`a)���`a:���`a
���`h        ���bsdxs"""
        Convert *obj* using *unit*.

        If *obj* is a sequence, return the converted sequence.
        """���`a
���`h        ���akbif���`a ���`bnp���aoa.���`hiterable���`a(���`cobj���`a)���`a:���`a
���`l            ���akfreturn���`a ���`a[���`ao���aoa.���`evalue���`a(���`dunit���`a)���`a ���akcfor���`a ���`ao���`a ���bowbin���`a ���`cobj���`a]���`a
���`h        ���akdelse���`a:���`a
���`l            ���akfreturn���`a ���`cobj���aoa.���`evalue���`a(���`dunit���`a)���`a
���`a
���`d    ���bndm@staticmethod���`a
���`d    ���akcdef���`a ���bnfmdefault_units���`a(���`ax���`a,���`a ���`daxis���`a)���`a:���`a
���`h        ���bsdx."""Return the default unit for *x* or None."""���`a
���`h        ���akbif���`a ���`bnp���aoa.���`hiterable���`a(���`ax���`a)���`a:���`a
���`l            ���akcfor���`a ���`ethisx���`a ���bowbin���`a ���`ax���`a:���`a
���`p                ���akfreturn���`a ���`ethisx���aoa.���`dunit���`a
���`h        ���akdelse���`a:���`a
���`l            ���akfreturn���`a ���`ax���aoa.���`dunit���`a
���`a
���`a
���`eunits���aoa.���`hregistry���`a[���`cFoo���`a]���`a ���aoa=���`a ���`lFooConverter���`a(���`a)���`a
���`a
���bc1r# create some Foos���`a
���`ax���`a ���aoa=���`a ���`a[���`cFoo���`a(���`cval���`a,���`a ���bmfc1.0���`a)���`a ���akcfor���`a ���`cval���`a ���bowbin���`a ���bnberange���`a(���bmia0���`a,���`a ���bmib50���`a,���`a ���bmia2���`a)���`a]���`a
���bc1x# and some arbitrary y data���`a
���`ay���`a ���aoa=���`a ���`a[���`ai���`a ���akcfor���`a ���`ai���`a ���bowbin���`a ���bnberange���`a(���bnbclen���`a(���`ax���`a)���`a)���`a]���`a
���`a
���`cfig���`a,���`a ���`a(���`cax1���`a,���`a ���`cax2���`a)���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���bmia1���`a,���`a ���bmia2���`a)���`a
���`cfig���aoa.���`hsuptitle���`a(���bs2a"���bs2lCustom units���bs2a"���`a)���`a
���`cfig���aoa.���`osubplots_adjust���`a(���`fbottom���aoa=���bmfc0.2���`a)���`a
���`a
���bc1w# plot specifying units���`a
���`cax2���aoa.���`dplot���`a(���`ax���`a,���`a ���`ay���`a,���`a ���bs1a'���bs1ao���bs1a'���`a,���`a ���`fxunits���aoa=���bmfc2.0���`a)���`a
���`cax2���aoa.���`iset_title���`a(���bs2a"���bs2lxunits = 2.0���bs2a"���`a)���`a
���`cplt���aoa.���`dsetp���`a(���`cax2���aoa.���`oget_xticklabels���`a(���`a)���`a,���`a ���`hrotation���aoa=���bmib30���`a,���`a ���`bha���aoa=���bs1a'���bs1eright���bs1a'���`a)���`a
���`a
���bc1xF# plot without specifying units; will use the None branch for axisinfo���`a
���`cax1���aoa.���`dplot���`a(���`ax���`a,���`a ���`ay���`a)���`b  ���bc1t# uses default units���`a
���`cax1���aoa.���`iset_title���`a(���bs1a'���bs1mdefault units���bs1a'���`a)���`a
���`cplt���aoa.���`dsetp���`a(���`cax1���aoa.���`oget_xticklabels���`a(���`a)���`a,���`a ���`hrotation���aoa=���bmib30���`a,���`a ���`bha���aoa=���bs1a'���bs1eright���bs1a'���`a)���`a
���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
`dNone�