��������F���bsdxe"""
============
Findobj Demo
============

Recursively find all objects that match some criteria
"""���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnndtext���`a ���akbas���`a ���bnndtext���`a
���`a
���`aa���`a ���aoa=���`a ���`bnp���aoa.���`farange���`a(���bmia0���`a,���`a ���bmia3���`a,���`a ���bmfc.02���`a)���`a
���`ab���`a ���aoa=���`a ���`bnp���aoa.���`farange���`a(���bmia0���`a,���`a ���bmia3���`a,���`a ���bmfc.02���`a)���`a
���`ac���`a ���aoa=���`a ���`bnp���aoa.���`cexp���`a(���`aa���`a)���`a
���`ad���`a ���aoa=���`a ���`ac���`a[���`a:���`a:���aoa-���bmia1���`a]���`a
���`a
���`cfig���`a,���`a ���`bax���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`a)���`a
���`cplt���aoa.���`dplot���`a(���`aa���`a,���`a ���`ac���`a,���`a ���bs1a'���bs1ck--���bs1a'���`a,���`a ���`aa���`a,���`a ���`ad���`a,���`a ���bs1a'���bs1bk:���bs1a'���`a,���`a ���`aa���`a,���`a ���`ac���`a ���aoa+���`a ���`ad���`a,���`a ���bs1a'���bs1ak���bs1a'���`a)���`a
���`cplt���aoa.���`flegend���`a(���`a(���bs1a'���bs1lModel length���bs1a'���`a,���`a ���bs1a'���bs1kData length���bs1a'���`a,���`a ���bs1a'���bs1tTotal message length���bs1a'���`a)���`a,���`a
���`k           ���`cloc���aoa=���bs1a'���bs1lupper center���bs1a'���`a,���`a ���`fshadow���aoa=���bkcdTrue���`a)���`a
���`cplt���aoa.���`dylim���`a(���`a[���aoa-���bmia1���`a,���`a ���bmib20���`a]���`a)���`a
���`cplt���aoa.���`dgrid���`a(���bkceFalse���`a)���`a
���`cplt���aoa.���`fxlabel���`a(���bs1a'���bs1uModel complexity --->���bs1a'���`a)���`a
���`cplt���aoa.���`fylabel���`a(���bs1a'���bs1sMessage length --->���bs1a'���`a)���`a
���`cplt���aoa.���`etitle���`a(���bs1a'���bs1vMinimum Message Length���bs1a'���`a)���`a
���`a
���`a
���bc1x# match on arbitrary function���`a
���akcdef���`a ���bnffmyfunc���`a(���`ax���`a)���`a:���`a
���`d    ���akfreturn���`a ���bnbghasattr���`a(���`ax���`a,���`a ���bs1a'���bs1iset_color���bs1a'���`a)���`a ���bowcand���`a ���bowcnot���`a ���bnbghasattr���`a(���`ax���`a,���`a ���bs1a'���bs1mset_facecolor���bs1a'���`a)���`a
���`a
���`a
���akcfor���`a ���`ao���`a ���bowbin���`a ���`cfig���aoa.���`gfindobj���`a(���`fmyfunc���`a)���`a:���`a
���`d    ���`ao���aoa.���`iset_color���`a(���bs1a'���bs1dblue���bs1a'���`a)���`a
���`a
���bc1x# match on class instances���`a
���akcfor���`a ���`ao���`a ���bowbin���`a ���`cfig���aoa.���`gfindobj���`a(���`dtext���aoa.���`dText���`a)���`a:���`a
���`d    ���`ao���aoa.���`mset_fontstyle���`a(���bs1a'���bs1fitalic���bs1a'���`a)���`a
���`a
���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
`dNone�