��������T���bsdy"""
================
Pick Event Demo2
================

Compute the mean (mu) and standard deviation (sigma) of 100 data sets and plot
mu vs. sigma.  When you click on one of the (mu, sigma) points, plot the raw
data from the dataset that generated this point.
"""���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���`a
���`a
���bc1x)# Fixing random state for reproducibility���`a
���`bnp���aoa.���`frandom���aoa.���`dseed���`a(���bmih19680801���`a)���`a
���`a
���`aX���`a ���aoa=���`a ���`bnp���aoa.���`frandom���aoa.���`drand���`a(���bmic100���`a,���`a ���bmid1000���`a)���`a
���`bxs���`a ���aoa=���`a ���`bnp���aoa.���`dmean���`a(���`aX���`a,���`a ���`daxis���aoa=���bmia1���`a)���`a
���`bys���`a ���aoa=���`a ���`bnp���aoa.���`cstd���`a(���`aX���`a,���`a ���`daxis���aoa=���bmia1���`a)���`a
���`a
���`cfig���`a,���`a ���`bax���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`a)���`a
���`bax���aoa.���`iset_title���`a(���bs1a'���bs1x"click on point to plot time series���bs1a'���`a)���`a
���`dline���`a,���`a ���aoa=���`a ���`bax���aoa.���`dplot���`a(���`bxs���`a,���`a ���`bys���`a,���`a ���bs1a'���bs1ao���bs1a'���`a,���`a ���`fpicker���aoa=���bkcdTrue���`a,���`a ���`jpickradius���aoa=���bmia5���`a)���`a
���`a
���`a
���akcdef���`a ���bnffonpick���`a(���`eevent���`a)���`a:���`a
���`a
���`d    ���akbif���`a ���`eevent���aoa.���`fartist���`a ���aob!=���`a ���`dline���`a:���`a
���`h        ���akfreturn���`a ���bkcdTrue���`a
���`a
���`d    ���`aN���`a ���aoa=���`a ���bnbclen���`a(���`eevent���aoa.���`cind���`a)���`a
���`d    ���akbif���`a ���bowcnot���`a ���`aN���`a:���`a
���`h        ���akfreturn���`a ���bkcdTrue���`a
���`a
���`d    ���`dfigi���`a,���`a ���`caxs���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`aN���`a,���`a ���`gsqueeze���aoa=���bkceFalse���`a)���`a
���`d    ���akcfor���`a ���`bax���`a,���`a ���`gdataind���`a ���bowbin���`a ���bnbczip���`a(���`caxs���aoa.���`dflat���`a,���`a ���`eevent���aoa.���`cind���`a)���`a:���`a
���`h        ���`bax���aoa.���`dplot���`a(���`aX���`a[���`gdataind���`a]���`a)���`a
���`h        ���`bax���aoa.���`dtext���`a(���bmfc.05���`a,���`a ���bmfb.9���`a,���`a ���bs1a'���bs1cmu=���bsie%1.3f���bseb\n���bs1fsigma=���bsie%1.3f���bs1a'���`a ���aoa%���`a ���`a(���`bxs���`a[���`gdataind���`a]���`a,���`a ���`bys���`a[���`gdataind���`a]���`a)���`a,���`a
���`p                ���`itransform���aoa=���`bax���aoa.���`itransAxes���`a,���`a ���`bva���aoa=���bs1a'���bs1ctop���bs1a'���`a)���`a
���`h        ���`bax���aoa.���`hset_ylim���`a(���aoa-���bmfc0.5���`a,���`a ���bmfc1.5���`a)���`a
���`d    ���`dfigi���aoa.���`dshow���`a(���`a)���`a
���`d    ���akfreturn���`a ���bkcdTrue���`a
���`a
���`cfig���aoa.���`fcanvas���aoa.���`kmpl_connect���`a(���bs1a'���bs1jpick_event���bs1a'���`a,���`a ���`fonpick���`a)���`a
���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
`dNone�