������������bsdxP"""
=======
Log Bar
=======

Plotting a bar chart with a logarithmic y-axis.
"""���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���`a
���`ddata���`a ���aoa=���`a ���`a(���`a(���bmia3���`a,���`a ���bmid1000���`a)���`a,���`a ���`a(���bmib10���`a,���`a ���bmia3���`a)���`a,���`a ���`a(���bmic100���`a,���`a ���bmib30���`a)���`a,���`a ���`a(���bmic500���`a,���`a ���bmic800���`a)���`a,���`a ���`a(���bmib50���`a,���`a ���bmia1���`a)���`a)���`a
���`a
���`cdim���`a ���aoa=���`a ���bnbclen���`a(���`ddata���`a[���bmia0���`a]���`a)���`a
���`aw���`a ���aoa=���`a ���bmfd0.75���`a
���`ddimw���`a ���aoa=���`a ���`aw���`a ���aoa/���`a ���`cdim���`a
���`a
���`cfig���`a,���`a ���`bax���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`a)���`a
���`ax���`a ���aoa=���`a ���`bnp���aoa.���`farange���`a(���bnbclen���`a(���`ddata���`a)���`a)���`a
���akcfor���`a ���`ai���`a ���bowbin���`a ���bnberange���`a(���bnbclen���`a(���`ddata���`a[���bmia0���`a]���`a)���`a)���`a:���`a
���`d    ���`ay���`a ���aoa=���`a ���`a[���`ad���`a[���`ai���`a]���`a ���akcfor���`a ���`ad���`a ���bowbin���`a ���`ddata���`a]���`a
���`d    ���`ab���`a ���aoa=���`a ���`bax���aoa.���`cbar���`a(���`ax���`a ���aoa+���`a ���`ai���`a ���aoa*���`a ���`ddimw���`a,���`a ���`ay���`a,���`a ���`ddimw���`a,���`a ���`fbottom���aoa=���bmfe0.001���`a)���`a
���`a
���`bax���aoa.���`jset_xticks���`a(���`ax���`a ���aoa+���`a ���`ddimw���`a ���aoa/���`a ���bmia2���`a,���`a ���`flabels���aoa=���bnbcmap���`a(���bnbcstr���`a,���`a ���`ax���`a)���`a)���`a
���`bax���aoa.���`jset_yscale���`a(���bs1a'���bs1clog���bs1a'���`a)���`a
���`a
���`bax���aoa.���`jset_xlabel���`a(���bs1a'���bs1ax���bs1a'���`a)���`a
���`bax���aoa.���`jset_ylabel���`a(���bs1a'���bs1ay���bs1a'���`a)���`a
���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
`dNone�