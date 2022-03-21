��������"���bsdxm"""
=============
Scatter Demo2
=============

Demo of scatter plot with varying marker colors and sizes.
"""���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnecbook���`a ���akbas���`a ���bnnecbook���`a
���`a
���bc1xN# Load a numpy record array from yahoo csv data with fields date, open, close,���`a
���bc1xI# volume, adj_close from the mpl-data/example directory. The record array���`a
���bc1xO# stores the date as an np.datetime64 with a day unit ('D') in the date column.���`a
���`jprice_data���`a ���aoa=���`a ���`a(���`ecbook���aoa.���`oget_sample_data���`a(���bs1a'���bs1hgoog.npz���bs1a'���`a,���`a ���`gnp_load���aoa=���bkcdTrue���`a)���`a[���bs1a'���bs1jprice_data���bs1a'���`a]���`a
���`n              ���aoa.���`dview���`a(���`bnp���aoa.���`hrecarray���`a)���`a)���`a
���`jprice_data���`a ���aoa=���`a ���`jprice_data���`a[���aoa-���bmic250���`a:���`a]���`b  ���bc1x&# get the most recent 250 trading days���`a
���`a
���`fdelta1���`a ���aoa=���`a ���`bnp���aoa.���`ddiff���`a(���`jprice_data���aoa.���`iadj_close���`a)���`a ���aoa/���`a ���`jprice_data���aoa.���`iadj_close���`a[���`a:���aoa-���bmia1���`a]���`a
���`a
���bc1x"# Marker size in units of points^2���`a
���`fvolume���`a ���aoa=���`a ���`a(���bmib15���`a ���aoa*���`a ���`jprice_data���aoa.���`fvolume���`a[���`a:���aoa-���bmia2���`a]���`a ���aoa/���`a ���`jprice_data���aoa.���`fvolume���`a[���bmia0���`a]���`a)���aoa*���aoa*���bmia2���`a
���`eclose���`a ���aoa=���`a ���bmfe0.003���`a ���aoa*���`a ���`jprice_data���aoa.���`eclose���`a[���`a:���aoa-���bmia2���`a]���`a ���aoa/���`a ���bmfe0.003���`a ���aoa*���`a ���`jprice_data���aoa.���`dopen���`a[���`a:���aoa-���bmia2���`a]���`a
���`a
���`cfig���`a,���`a ���`bax���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`a)���`a
���`bax���aoa.���`gscatter���`a(���`fdelta1���`a[���`a:���aoa-���bmia1���`a]���`a,���`a ���`fdelta1���`a[���bmia1���`a:���`a]���`a,���`a ���`ac���aoa=���`eclose���`a,���`a ���`as���aoa=���`fvolume���`a,���`a ���`ealpha���aoa=���bmfc0.5���`a)���`a
���`a
���`bax���aoa.���`jset_xlabel���`a(���bsaar���bs1a'���bs1a$���bs1a\���bs1hDelta_i$���bs1a'���`a,���`a ���`hfontsize���aoa=���bmib15���`a)���`a
���`bax���aoa.���`jset_ylabel���`a(���bsaar���bs1a'���bs1a$���bs1a\���bs1fDelta_���bs1a{���bs1ei+1}$���bs1a'���`a,���`a ���`hfontsize���aoa=���bmib15���`a)���`a
���`bax���aoa.���`iset_title���`a(���bs1a'���bs1xVolume and percent change���bs1a'���`a)���`a
���`a
���`bax���aoa.���`dgrid���`a(���bkcdTrue���`a)���`a
���`cfig���aoa.���`ltight_layout���`a(���`a)���`a
���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
`dNone�