��������n���bsdx["""
===========================
Stackplots and streamgraphs
===========================
"""���`a
���`a
���bc1xN##############################################################################���`a
���bc1l# Stackplots���`a
���bc1l# ----------���`a
���bc1a#���`a
���bc1xH# Stackplots draw multiple datasets as vertically stacked areas. This is���`a
���bc1xJ# useful when the individual data values and additionally their cumulative���`a
���bc1x# value are of interest.���`a
���`a
���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���`a
���bc1xE# data from United Nations World Population Prospects (Revision 2019)���`a
���bc1x8# https://population.un.org/wpp/, license: CC BY 3.0 IGO���`a
���`dyear���`a ���aoa=���`a ���`a[���bmid1950���`a,���`a ���bmid1960���`a,���`a ���bmid1970���`a,���`a ���bmid1980���`a,���`a ���bmid1990���`a,���`a ���bmid2000���`a,���`a ���bmid2010���`a,���`a ���bmid2018���`a]���`a
���`wpopulation_by_continent���`a ���aoa=���`a ���`a{���`a
���`d    ���bs1a'���bs1fafrica���bs1a'���`a:���`a ���`a[���bmic228���`a,���`a ���bmic284���`a,���`a ���bmic365���`a,���`a ���bmic477���`a,���`a ���bmic631���`a,���`a ���bmic814���`a,���`a ���bmid1044���`a,���`a ���bmid1275���`a]���`a,���`a
���`d    ���bs1a'���bs1hamericas���bs1a'���`a:���`a ���`a[���bmic340���`a,���`a ���bmic425���`a,���`a ���bmic519���`a,���`a ���bmic619���`a,���`a ���bmic727���`a,���`a ���bmic840���`a,���`a ���bmic943���`a,���`a ���bmid1006���`a]���`a,���`a
���`d    ���bs1a'���bs1dasia���bs1a'���`a:���`a ���`a[���bmid1394���`a,���`a ���bmid1686���`a,���`a ���bmid2120���`a,���`a ���bmid2625���`a,���`a ���bmid3202���`a,���`a ���bmid3714���`a,���`a ���bmid4169���`a,���`a ���bmid4560���`a]���`a,���`a
���`d    ���bs1a'���bs1feurope���bs1a'���`a:���`a ���`a[���bmic220���`a,���`a ���bmic253���`a,���`a ���bmic276���`a,���`a ���bmic295���`a,���`a ���bmic310���`a,���`a ���bmic303���`a,���`a ���bmic294���`a,���`a ���bmic293���`a]���`a,���`a
���`d    ���bs1a'���bs1goceania���bs1a'���`a:���`a ���`a[���bmib12���`a,���`a ���bmib15���`a,���`a ���bmib19���`a,���`a ���bmib22���`a,���`a ���bmib26���`a,���`a ���bmib31���`a,���`a ���bmib36���`a,���`a ���bmib39���`a]���`a,���`a
���`a}���`a
���`a
���`cfig���`a,���`a ���`bax���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`a)���`a
���`bax���aoa.���`istackplot���`a(���`dyear���`a,���`a ���`wpopulation_by_continent���aoa.���`fvalues���`a(���`a)���`a,���`a
���`m             ���`flabels���aoa=���`wpopulation_by_continent���aoa.���`dkeys���`a(���`a)���`a,���`a ���`ealpha���aoa=���bmfc0.8���`a)���`a
���`bax���aoa.���`flegend���`a(���`cloc���aoa=���bs1a'���bs1jupper left���bs1a'���`a)���`a
���`bax���aoa.���`iset_title���`a(���bs1a'���bs1pWorld population���bs1a'���`a)���`a
���`bax���aoa.���`jset_xlabel���`a(���bs1a'���bs1dYear���bs1a'���`a)���`a
���`bax���aoa.���`jset_ylabel���`a(���bs1a'���bs1xNumber of people (millions)���bs1a'���`a)���`a
���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
���`a
���bc1xN##############################################################################���`a
���bc1n# Streamgraphs���`a
���bc1n# ------------���`a
���bc1a#���`a
���bc1xL# Using the *baseline* parameter, you can turn an ordinary stacked area plot���`a
���bc1x&# with baseline 0 into a stream graph.���`a
���`a
���`a
���bc1x)# Fixing random state for reproducibility���`a
���`bnp���aoa.���`frandom���aoa.���`dseed���`a(���bmih19680801���`a)���`a
���`a
���`a
���akcdef���`a ���bnfpgaussian_mixture���`a(���`ax���`a,���`a ���`an���aoa=���bmia5���`a)���`a:���`a
���`d    ���bsdxK"""Return a random mixture of *n* Gaussians, evaluated at positions *x*."""���`a
���`d    ���akcdef���`a ���bnfsadd_random_gaussian���`a(���`aa���`a)���`a:���`a
���`h        ���`iamplitude���`a ���aoa=���`a ���bmia1���`a ���aoa/���`a ���`a(���bmfb.1���`a ���aoa+���`a ���`bnp���aoa.���`frandom���aoa.���`frandom���`a(���`a)���`a)���`a
���`h        ���`bdx���`a ���aoa=���`a ���`ax���`a[���aoa-���bmia1���`a]���`a ���aoa-���`a ���`ax���`a[���bmia0���`a]���`a
���`h        ���`bx0���`a ���aoa=���`a ���`a(���bmia2���`a ���aoa*���`a ���`bnp���aoa.���`frandom���aoa.���`frandom���`a(���`a)���`a ���aoa-���`a ���bmfb.5���`a)���`a ���aoa*���`a ���`bdx���`a
���`h        ���`az���`a ���aoa=���`a ���bmib10���`a ���aoa/���`a ���`a(���bmfb.1���`a ���aoa+���`a ���`bnp���aoa.���`frandom���aoa.���`frandom���`a(���`a)���`a)���`a ���aoa/���`a ���`bdx���`a
���`h        ���`aa���`a ���aoa+���aoa=���`a ���`iamplitude���`a ���aoa*���`a ���`bnp���aoa.���`cexp���`a(���aoa-���`a(���`az���`a ���aoa*���`a ���`a(���`ax���`a ���aoa-���`a ���`bx0���`a)���`a)���aoa*���aoa*���bmia2���`a)���`a
���`d    ���`aa���`a ���aoa=���`a ���`bnp���aoa.���`jzeros_like���`a(���`ax���`a)���`a
���`d    ���akcfor���`a ���`aj���`a ���bowbin���`a ���bnberange���`a(���`an���`a)���`a:���`a
���`h        ���`sadd_random_gaussian���`a(���`aa���`a)���`a
���`d    ���akfreturn���`a ���`aa���`a
���`a
���`a
���`ax���`a ���aoa=���`a ���`bnp���aoa.���`hlinspace���`a(���bmia0���`a,���`a ���bmic100���`a,���`a ���bmic101���`a)���`a
���`bys���`a ���aoa=���`a ���`a[���`pgaussian_mixture���`a(���`ax���`a)���`a ���akcfor���`a ���`a_���`a ���bowbin���`a ���bnberange���`a(���bmia3���`a)���`a]���`a
���`a
���`cfig���`a,���`a ���`bax���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`a)���`a
���`bax���aoa.���`istackplot���`a(���`ax���`a,���`a ���`bys���`a,���`a ���`hbaseline���aoa=���bs1a'���bs1fwiggle���bs1a'���`a)���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
`dNone�