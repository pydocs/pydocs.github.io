�����������bsdx�"""
======================================
Long chain of connections using Sankey
======================================

Demonstrate/test the Sankey class by producing a long chain of connections.
"""���`a
���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���bkndfrom���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfsankey���`a ���bknfimport���`a ���`fSankey���`a
���`a
���`nlinks_per_side���`a ���aoa=���`a ���bmia6���`a
���`a
���`a
���akcdef���`a ���bnfdside���`a(���`fsankey���`a,���`a ���`an���aoa=���bmia1���`a)���`a:���`a
���`d    ���bsdx"""Generate a side chain."""���`a
���`d    ���`eprior���`a ���aoa=���`a ���bnbclen���`a(���`fsankey���aoa.���`hdiagrams���`a)���`a
���`d    ���akcfor���`a ���`ai���`a ���bowbin���`a ���bnberange���`a(���bmia0���`a,���`a ���bmia2���aoa*���`an���`a,���`a ���bmia2���`a)���`a:���`a
���`h        ���`fsankey���aoa.���`cadd���`a(���`eflows���aoa=���`a[���bmia1���`a,���`a ���aoa-���bmia1���`a]���`a,���`a ���`lorientations���aoa=���`a[���aoa-���bmia1���`a,���`a ���aoa-���bmia1���`a]���`a,���`a
���`s                   ���`jpatchlabel���aoa=���bnbcstr���`a(���`eprior���`a ���aoa+���`a ���`ai���`a)���`a,���`a
���`s                   ���`eprior���aoa=���`eprior���`a ���aoa+���`a ���`ai���`a ���aoa-���`a ���bmia1���`a,���`a ���`gconnect���aoa=���`a(���bmia1���`a,���`a ���bmia0���`a)���`a,���`a ���`ealpha���aoa=���bmfc0.5���`a)���`a
���`h        ���`fsankey���aoa.���`cadd���`a(���`eflows���aoa=���`a[���bmia1���`a,���`a ���aoa-���bmia1���`a]���`a,���`a ���`lorientations���aoa=���`a[���bmia1���`a,���`a ���bmia1���`a]���`a,���`a
���`s                   ���`jpatchlabel���aoa=���bnbcstr���`a(���`eprior���`a ���aoa+���`a ���`ai���`a ���aoa+���`a ���bmia1���`a)���`a,���`a
���`s                   ���`eprior���aoa=���`eprior���`a ���aoa+���`a ���`ai���`a,���`a ���`gconnect���aoa=���`a(���bmia1���`a,���`a ���bmia0���`a)���`a,���`a ���`ealpha���aoa=���bmfc0.5���`a)���`a
���`a
���`a
���akcdef���`a ���bnffcorner���`a(���`fsankey���`a)���`a:���`a
���`d    ���bsdx"""Generate a corner link."""���`a
���`d    ���`eprior���`a ���aoa=���`a ���bnbclen���`a(���`fsankey���aoa.���`hdiagrams���`a)���`a
���`d    ���`fsankey���aoa.���`cadd���`a(���`eflows���aoa=���`a[���bmia1���`a,���`a ���aoa-���bmia1���`a]���`a,���`a ���`lorientations���aoa=���`a[���bmia0���`a,���`a ���bmia1���`a]���`a,���`a
���`o               ���`jpatchlabel���aoa=���bnbcstr���`a(���`eprior���`a)���`a,���`a ���`ifacecolor���aoa=���bs1a'���bs1ak���bs1a'���`a,���`a
���`o               ���`eprior���aoa=���`eprior���`a ���aoa-���`a ���bmia1���`a,���`a ���`gconnect���aoa=���`a(���bmia1���`a,���`a ���bmia0���`a)���`a,���`a ���`ealpha���aoa=���bmfc0.5���`a)���`a
���`a
���`a
���`cfig���`a ���aoa=���`a ���`cplt���aoa.���`ffigure���`a(���`a)���`a
���`bax���`a ���aoa=���`a ���`cfig���aoa.���`kadd_subplot���`a(���bmia1���`a,���`a ���bmia1���`a,���`a ���bmia1���`a,���`a ���`fxticks���aoa=���`a[���`a]���`a,���`a ���`fyticks���aoa=���`a[���`a]���`a,���`a
���`u                     ���`etitle���aoa=���bs2a"���bs2xWhy would you want to do this?���bseb\n���bs2p(But you could.)���bs2a"���`a)���`a
���`fsankey���`a ���aoa=���`a ���`fSankey���`a(���`bax���aoa=���`bax���`a,���`a ���`dunit���aoa=���bkcdNone���`a)���`a
���`fsankey���aoa.���`cadd���`a(���`eflows���aoa=���`a[���bmia1���`a,���`a ���aoa-���bmia1���`a]���`a,���`a ���`lorientations���aoa=���`a[���bmia0���`a,���`a ���bmia1���`a]���`a,���`a
���`k           ���`jpatchlabel���aoa=���bs2a"���bs2a0���bs2a"���`a,���`a ���`ifacecolor���aoa=���bs1a'���bs1ak���bs1a'���`a,���`a
���`k           ���`hrotation���aoa=���bmib45���`a)���`a
���`dside���`a(���`fsankey���`a,���`a ���`an���aoa=���`nlinks_per_side���`a)���`a
���`fcorner���`a(���`fsankey���`a)���`a
���`dside���`a(���`fsankey���`a,���`a ���`an���aoa=���`nlinks_per_side���`a)���`a
���`fcorner���`a(���`fsankey���`a)���`a
���`dside���`a(���`fsankey���`a,���`a ���`an���aoa=���`nlinks_per_side���`a)���`a
���`fcorner���`a(���`fsankey���`a)���`a
���`dside���`a(���`fsankey���`a,���`a ���`an���aoa=���`nlinks_per_side���`a)���`a
���`fsankey���aoa.���`ffinish���`a(���`a)���`a
���bc1i# Notice:���`a
���bc1xE# 1. The alignment doesn't drift significantly (if at all; with 16007���`a
���bc1x)#    subdiagrams there is still closure).���`a
���bc1xK# 2. The first diagram is rotated 45 deg, so all other diagrams are rotated���`a
���bc1q#    accordingly.���`a
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
���bc1x#    - `matplotlib.sankey`���`a
���bc1x!#    - `matplotlib.sankey.Sankey`���`a
���bc1x%#    - `matplotlib.sankey.Sankey.add`���`a
���bc1x(#    - `matplotlib.sankey.Sankey.finish`���`a
`dNone�