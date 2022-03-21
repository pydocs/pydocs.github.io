������������bsdyI"""
========================================
Bayesian Methods for Hackers style sheet
========================================

This example demonstrates the style used in the Bayesian Methods for Hackers
[1]_ online book.

.. [1] http://camdavidsonpilon.github.io/Probabilistic-Programming-and-Bayesian-Methods-for-Hackers/

"""���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���`a
���`a
���bc1x)# Fixing random state for reproducibility���`a
���`bnp���aoa.���`frandom���aoa.���`dseed���`a(���bmih19680801���`a)���`a
���`a
���`cplt���aoa.���`estyle���aoa.���`cuse���`a(���bs1a'���bs1cbmh���bs1a'���`a)���`a
���`a
���`a
���akcdef���`a ���bnfnplot_beta_hist���`a(���`bax���`a,���`a ���`aa���`a,���`a ���`ab���`a)���`a:���`a
���`d    ���`bax���aoa.���`dhist���`a(���`bnp���aoa.���`frandom���aoa.���`dbeta���`a(���`aa���`a,���`a ���`ab���`a,���`a ���`dsize���aoa=���bmie10000���`a)���`a,���`a
���`l            ���`hhisttype���aoa=���bs2a"���bs2jstepfilled���bs2a"���`a,���`a ���`dbins���aoa=���bmib25���`a,���`a ���`ealpha���aoa=���bmfc0.8���`a,���`a ���`gdensity���aoa=���bkcdTrue���`a)���`a
���`a
���`a
���`cfig���`a,���`a ���`bax���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`a)���`a
���`nplot_beta_hist���`a(���`bax���`a,���`a ���bmib10���`a,���`a ���bmib10���`a)���`a
���`nplot_beta_hist���`a(���`bax���`a,���`a ���bmia4���`a,���`a ���bmib12���`a)���`a
���`nplot_beta_hist���`a(���`bax���`a,���`a ���bmib50���`a,���`a ���bmib12���`a)���`a
���`nplot_beta_hist���`a(���`bax���`a,���`a ���bmia6���`a,���`a ���bmib55���`a)���`a
���`bax���aoa.���`iset_title���`a(���bs2a"���bs2a'���bs2cbmh���bs2a'���bs2l style sheet���bs2a"���`a)���`a
���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
`dNone�