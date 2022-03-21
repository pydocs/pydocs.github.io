��������k���bsdxq"""
===================
`.HBoxDivider` demo
===================

Using an `.HBoxDivider` to arrange subplots.
"""���`a
���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���bkndfrom���`a ���bnnlmpl_toolkits���bnna.���bnnjaxes_grid1���bnna.���bnnlaxes_divider���`a ���bknfimport���`a ���`kHBoxDivider���`a
���bknfimport���`a ���bnnlmpl_toolkits���bnna.���bnnjaxes_grid1���bnna.���bnniaxes_size���`a ���akbas���`a ���bnndSize���`a
���`a
���`a
���akcdef���`a ���bnfrmake_heights_equal���`a(���`cfig���`a,���`a ���`drect���`a,���`a ���`cax1���`a,���`a ���`cax2���`a,���`a ���`cpad���`a)���`a:���`a
���`d    ���bc1o# pad in inches���`a
���`d    ���`gdivider���`a ���aoa=���`a ���`kHBoxDivider���`a(���`a
���`h        ���`cfig���`a,���`a ���`drect���`a,���`a
���`h        ���`jhorizontal���aoa=���`a[���`dSize���aoa.���`eAxesX���`a(���`cax1���`a)���`a,���`a ���`dSize���aoa.���`eFixed���`a(���`cpad���`a)���`a,���`a ���`dSize���aoa.���`eAxesX���`a(���`cax2���`a)���`a]���`a,���`a
���`h        ���`hvertical���aoa=���`a[���`dSize���aoa.���`eAxesY���`a(���`cax1���`a)���`a,���`a ���`dSize���aoa.���`fScaled���`a(���bmia1���`a)���`a,���`a ���`dSize���aoa.���`eAxesY���`a(���`cax2���`a)���`a]���`a)���`a
���`d    ���`cax1���aoa.���`pset_axes_locator���`a(���`gdivider���aoa.���`knew_locator���`a(���bmia0���`a)���`a)���`a
���`d    ���`cax2���aoa.���`pset_axes_locator���`a(���`gdivider���aoa.���`knew_locator���`a(���bmia2���`a)���`a)���`a
���`a
���`a
���akbif���`a ���bvmh__name__���`a ���aob==���`a ���bs2a"���bs2h__main__���bs2a"���`a:���`a
���`a
���`d    ���`darr1���`a ���aoa=���`a ���`bnp���aoa.���`farange���`a(���bmib20���`a)���aoa.���`greshape���`a(���`a(���bmia4���`a,���`a ���bmia5���`a)���`a)���`a
���`d    ���`darr2���`a ���aoa=���`a ���`bnp���aoa.���`farange���`a(���bmib20���`a)���aoa.���`greshape���`a(���`a(���bmia5���`a,���`a ���bmia4���`a)���`a)���`a
���`a
���`d    ���`cfig���`a,���`a ���`a(���`cax1���`a,���`a ���`cax2���`a)���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���bmia1���`a,���`a ���bmia2���`a)���`a
���`d    ���`cax1���aoa.���`fimshow���`a(���`darr1���`a)���`a
���`d    ���`cax2���aoa.���`fimshow���`a(���`darr2���`a)���`a
���`a
���`d    ���`rmake_heights_equal���`a(���`cfig���`a,���`a ���bmic111���`a,���`a ���`cax1���`a,���`a ���`cax2���`a,���`a ���`cpad���aoa=���bmfc0.5���`a)���`a
���`a
���`d    ���`cfig���aoa.���`dtext���`a(���bmfb.5���`a,���`a ���bmfb.5���`a,���`a
���`m             ���bs2a"���bs2iBoth axes���bs2a'���bs2v location are adjusted���bseb\n���bs2a"���`a
���`m             ���bs2a"���bs2xso that they have equal heights���bseb\n���bs2a"���`a
���`m             ���bs2a"���bs2x%while maintaining their aspect ratios���bs2a"���`a,���`a
���`m             ���`bva���aoa=���bs2a"���bs2fcenter���bs2a"���`a,���`a ���`bha���aoa=���bs2a"���bs2fcenter���bs2a"���`a,���`a
���`m             ���`dbbox���aoa=���bnbddict���`a(���`hboxstyle���aoa=���bs2a"���bs2lround, pad=1���bs2a"���`a,���`a ���`ifacecolor���aoa=���bs2a"���bs2aw���bs2a"���`a)���`a)���`a
���`a
���`d    ���`cplt���aoa.���`dshow���`a(���`a)���`a
`dNone�