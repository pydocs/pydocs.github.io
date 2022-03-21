������������bsdy"""
================
The Bayes update
================

This animation displays the posterior estimate updates as it is refitted when
new data arrives.
The vertical line represents the theoretical value to which the plotted
distribution should converge.
"""���`a
���`a
���bknfimport���`a ���bnndmath���`a
���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���bkndfrom���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnianimation���`a ���bknfimport���`a ���`mFuncAnimation���`a
���`a
���`a
���akcdef���`a ���bnfhbeta_pdf���`a(���`ax���`a,���`a ���`aa���`a,���`a ���`ab���`a)���`a:���`a
���`d    ���akfreturn���`a ���`a(���`ax���aoa*���aoa*���`a(���`aa���aoa-���bmia1���`a)���`a ���aoa*���`a ���`a(���bmia1���aoa-���`ax���`a)���aoa*���aoa*���`a(���`ab���aoa-���bmia1���`a)���`a ���aoa*���`a ���`dmath���aoa.���`egamma���`a(���`aa���`a ���aoa+���`a ���`ab���`a)���`a
���`l            ���aoa/���`a ���`a(���`dmath���aoa.���`egamma���`a(���`aa���`a)���`a ���aoa*���`a ���`dmath���aoa.���`egamma���`a(���`ab���`a)���`a)���`a)���`a
���`a
���`a
���akeclass���`a ���bncjUpdateDist���`a:���`a
���`d    ���akcdef���`a ���bfmh__init__���`a(���bbpdself���`a,���`a ���`bax���`a,���`a ���`dprob���aoa=���bmfc0.5���`a)���`a:���`a
���`h        ���bbpdself���aoa.���`gsuccess���`a ���aoa=���`a ���bmia0���`a
���`h        ���bbpdself���aoa.���`dprob���`a ���aoa=���`a ���`dprob���`a
���`h        ���bbpdself���aoa.���`dline���`a,���`a ���aoa=���`a ���`bax���aoa.���`dplot���`a(���`a[���`a]���`a,���`a ���`a[���`a]���`a,���`a ���bs1a'���bs1bk-���bs1a'���`a)���`a
���`h        ���bbpdself���aoa.���`ax���`a ���aoa=���`a ���`bnp���aoa.���`hlinspace���`a(���bmia0���`a,���`a ���bmia1���`a,���`a ���bmic200���`a)���`a
���`h        ���bbpdself���aoa.���`bax���`a ���aoa=���`a ���`bax���`a
���`a
���`h        ���bc1x# Set up plot parameters���`a
���`h        ���bbpdself���aoa.���`bax���aoa.���`hset_xlim���`a(���bmia0���`a,���`a ���bmia1���`a)���`a
���`h        ���bbpdself���aoa.���`bax���aoa.���`hset_ylim���`a(���bmia0���`a,���`a ���bmib10���`a)���`a
���`h        ���bbpdself���aoa.���`bax���aoa.���`dgrid���`a(���bkcdTrue���`a)���`a
���`a
���`h        ���bc1x9# This vertical line represents the theoretical value, to���`a
���`h        ���bc1x1# which the plotted distribution should converge.���`a
���`h        ���bbpdself���aoa.���`bax���aoa.���`gaxvline���`a(���`dprob���`a,���`a ���`ilinestyle���aoa=���bs1a'���bs1b--���bs1a'���`a,���`a ���`ecolor���aoa=���bs1a'���bs1eblack���bs1a'���`a)���`a
���`a
���`d    ���akcdef���`a ���bfmh__call__���`a(���bbpdself���`a,���`a ���`ai���`a)���`a:���`a
���`h        ���bc1x9# This way the plot can continuously run and we just keep���`a
���`h        ���bc1x*# watching new realizations of the process���`a
���`h        ���akbif���`a ���`ai���`a ���aob==���`a ���bmia0���`a:���`a
���`l            ���bbpdself���aoa.���`gsuccess���`a ���aoa=���`a ���bmia0���`a
���`l            ���bbpdself���aoa.���`dline���aoa.���`hset_data���`a(���`a[���`a]���`a,���`a ���`a[���`a]���`a)���`a
���`l            ���akfreturn���`a ���bbpdself���aoa.���`dline���`a,���`a
���`a
���`h        ���bc1x@# Choose success based on exceed a threshold with a uniform pick���`a
���`h        ���akbif���`a ���`bnp���aoa.���`frandom���aoa.���`drand���`a(���bmia1���`a,���`a)���`a ���aoa<���`a ���bbpdself���aoa.���`dprob���`a:���`a
���`l            ���bbpdself���aoa.���`gsuccess���`a ���aoa+���aoa=���`a ���bmia1���`a
���`h        ���`ay���`a ���aoa=���`a ���`hbeta_pdf���`a(���bbpdself���aoa.���`ax���`a,���`a ���bbpdself���aoa.���`gsuccess���`a ���aoa+���`a ���bmia1���`a,���`a ���`a(���`ai���`a ���aoa-���`a ���bbpdself���aoa.���`gsuccess���`a)���`a ���aoa+���`a ���bmia1���`a)���`a
���`h        ���bbpdself���aoa.���`dline���aoa.���`hset_data���`a(���bbpdself���aoa.���`ax���`a,���`a ���`ay���`a)���`a
���`h        ���akfreturn���`a ���bbpdself���aoa.���`dline���`a,���`a
���`a
���bc1x)# Fixing random state for reproducibility���`a
���`bnp���aoa.���`frandom���aoa.���`dseed���`a(���bmih19680801���`a)���`a
���`a
���`a
���`cfig���`a,���`a ���`bax���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`a)���`a
���`bud���`a ���aoa=���`a ���`jUpdateDist���`a(���`bax���`a,���`a ���`dprob���aoa=���bmfc0.7���`a)���`a
���`danim���`a ���aoa=���`a ���`mFuncAnimation���`a(���`cfig���`a,���`a ���`bud���`a,���`a ���`fframes���aoa=���bmic100���`a,���`a ���`hinterval���aoa=���bmic100���`a,���`a ���`dblit���aoa=���bkcdTrue���`a)���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
`dNone�