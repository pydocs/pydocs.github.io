������������bsdy�"""
Placing text boxes
==================

When decorating axes with text boxes, two useful tricks are to place the text
in axes coordinates (see :doc:`/tutorials/advanced/transforms_tutorial`),
so the text doesn't move around with changes in x or y limits.  You
can also use the ``bbox`` property of text to surround the text with a
`~matplotlib.patches.Patch` instance -- the ``bbox`` keyword argument takes a
dictionary with keys that are Patch properties.
"""���`a
���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���`a
���`bnp���aoa.���`frandom���aoa.���`dseed���`a(���bmih19680801���`a)���`a
���`a
���`cfig���`a,���`a ���`bax���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`a)���`a
���`ax���`a ���aoa=���`a ���bmib30���aoa*���`bnp���aoa.���`frandom���aoa.���`erandn���`a(���bmie10000���`a)���`a
���`bmu���`a ���aoa=���`a ���`ax���aoa.���`dmean���`a(���`a)���`a
���`fmedian���`a ���aoa=���`a ���`bnp���aoa.���`fmedian���`a(���`ax���`a)���`a
���`esigma���`a ���aoa=���`a ���`ax���aoa.���`cstd���`a(���`a)���`a
���`gtextstr���`a ���aoa=���`a ���bs1a'���bseb\n���bs1a'���aoa.���`djoin���`a(���`a(���`a
���`d    ���bsaar���bs1a'���bs1a$���bs1a\���bs1cmu=���bsid%.2f���bs1a$���bs1a'���`a ���aoa%���`a ���`a(���`bmu���`a,���`a ���`a)���`a,���`a
���`d    ���bsaar���bs1a'���bs1a$���bs1a\���bs1fmathrm���bsih{median}���bs1a=���bsid%.2f���bs1a$���bs1a'���`a ���aoa%���`a ���`a(���`fmedian���`a,���`a ���`a)���`a,���`a
���`d    ���bsaar���bs1a'���bs1a$���bs1a\���bs1fsigma=���bsid%.2f���bs1a$���bs1a'���`a ���aoa%���`a ���`a(���`esigma���`a,���`a ���`a)���`a)���`a)���`a
���`a
���`bax���aoa.���`dhist���`a(���`ax���`a,���`a ���bmib50���`a)���`a
���bc1x-# these are matplotlib.patch.Patch properties���`a
���`eprops���`a ���aoa=���`a ���bnbddict���`a(���`hboxstyle���aoa=���bs1a'���bs1eround���bs1a'���`a,���`a ���`ifacecolor���aoa=���bs1a'���bs1ewheat���bs1a'���`a,���`a ���`ealpha���aoa=���bmfc0.5���`a)���`a
���`a
���bc1x/# place a text box in upper left in axes coords���`a
���`bax���aoa.���`dtext���`a(���bmfd0.05���`a,���`a ���bmfd0.95���`a,���`a ���`gtextstr���`a,���`a ���`itransform���aoa=���`bax���aoa.���`itransAxes���`a,���`a ���`hfontsize���aoa=���bmib14���`a,���`a
���`h        ���`qverticalalignment���aoa=���bs1a'���bs1ctop���bs1a'���`a,���`a ���`dbbox���aoa=���`eprops���`a)���`a
���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
`dNone�