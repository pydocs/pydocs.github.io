������������bsdx;"""
================
Parasite Simple2
================

"""���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnjtransforms���`a ���akbas���`a ���bnnkmtransforms���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���bkndfrom���`a ���bnnlmpl_toolkits���bnna.���bnnjaxes_grid1���bnna.���bnnmparasite_axes���`a ���bknfimport���`a ���`hHostAxes���`a
���`a
���`cobs���`a ���aoa=���`a ���`a[���`a[���bs2a"���bs2e01_S1���bs2a"���`a,���`a ���bmfd3.88���`a,���`a ���bmfd0.14���`a,���`a ���bmid1970���`a,���`a ���bmib63���`a]���`a,���`a
���`g       ���`a[���bs2a"���bs2e01_S4���bs2a"���`a,���`a ���bmfc5.6���`a,���`a ���bmfd0.82���`a,���`a ���bmid1622���`a,���`a ���bmic150���`a]���`a,���`a
���`g       ���`a[���bs2a"���bs2e02_S1���bs2a"���`a,���`a ���bmfc2.4���`a,���`a ���bmfd0.54���`a,���`a ���bmid1570���`a,���`a ���bmib40���`a]���`a,���`a
���`g       ���`a[���bs2a"���bs2e03_S1���bs2a"���`a,���`a ���bmfc4.1���`a,���`a ���bmfd0.62���`a,���`a ���bmid2380���`a,���`a ���bmic170���`a]���`a]���`a
���`a
���`a
���`cfig���`a ���aoa=���`a ���`cplt���aoa.���`ffigure���`a(���`a)���`a
���`a
���`fax_kms���`a ���aoa=���`a ���`cfig���aoa.���`kadd_subplot���`a(���`jaxes_class���aoa=���`hHostAxes���`a,���`a ���`faspect���aoa=���bmia1���`a)���`a
���`a
���bc1xI# angular proper motion("/yr) to linear velocity(km/s) at distance=2.3kpc���`a
���`ipm_to_kms���`a ���aoa=���`a ���bmfb1.���aoa/���bmfg206265.���aoa*���bmid2300���aoa*���bmfh3.085e18���aoa/���bmff3.15e7���aoa/���bmfd1.e5���`a
���`a
���`iaux_trans���`a ���aoa=���`a ���`kmtransforms���aoa.���`hAffine2D���`a(���`a)���aoa.���`escale���`a(���`ipm_to_kms���`a,���`a ���bmfb1.���`a)���`a
���`eax_pm���`a ���aoa=���`a ���`fax_kms���aoa.���`dtwin���`a(���`iaux_trans���`a)���`a
���`a
���akcfor���`a ���`an���`a,���`a ���`bds���`a,���`a ���`cdse���`a,���`a ���`aw���`a,���`a ���`bwe���`a ���bowbin���`a ���`cobs���`a:���`a
���`d    ���`dtime���`a ���aoa=���`a ���`a(���`a(���bmid2007���`a ���aoa+���`a ���`a(���bmfc10.���`a ���aoa+���`a ���bmia4���aoa/���bmfc30.���`a)���aoa/���bmib12���`a)���`a ���aoa-���`a ���bmff1988.5���`a)���`a
���`d    ���`av���`a ���aoa=���`a ���`bds���`a ���aoa/���`a ���`dtime���`a ���aoa*���`a ���`ipm_to_kms���`a
���`d    ���`bve���`a ���aoa=���`a ���`cdse���`a ���aoa/���`a ���`dtime���`a ���aoa*���`a ���`ipm_to_kms���`a
���`d    ���`fax_kms���aoa.���`herrorbar���`a(���`a[���`av���`a]���`a,���`a ���`a[���`aw���`a]���`a,���`a ���`dxerr���aoa=���`a[���`bve���`a]���`a,���`a ���`dyerr���aoa=���`a[���`bwe���`a]���`a,���`a ���`ecolor���aoa=���bs2a"���bs2ak���bs2a"���`a)���`a
���`a
���`a
���`fax_kms���aoa.���`daxis���`a[���bs2a"���bs2fbottom���bs2a"���`a]���aoa.���`iset_label���`a(���bs2a"���bs2x!Linear velocity at 2.3 kpc [km/s]���bs2a"���`a)���`a
���`fax_kms���aoa.���`daxis���`a[���bs2a"���bs2dleft���bs2a"���`a]���aoa.���`iset_label���`a(���bs2a"���bs2kFWHM [km/s]���bs2a"���`a)���`a
���`eax_pm���aoa.���`daxis���`a[���bs2a"���bs2ctop���bs2a"���`a]���aoa.���`iset_label���`a(���bsaar���bs2a"���bs2pProper Motion [$���bs2a'���bs2a'���bs2e$/yr]���bs2a"���`a)���`a
���`eax_pm���aoa.���`daxis���`a[���bs2a"���bs2ctop���bs2a"���`a]���aoa.���`elabel���aoa.���`kset_visible���`a(���bkcdTrue���`a)���`a
���`eax_pm���aoa.���`daxis���`a[���bs2a"���bs2eright���bs2a"���`a]���aoa.���`pmajor_ticklabels���aoa.���`kset_visible���`a(���bkceFalse���`a)���`a
���`a
���`fax_kms���aoa.���`hset_xlim���`a(���bmic950���`a,���`a ���bmid3700���`a)���`a
���`fax_kms���aoa.���`hset_ylim���`a(���bmic950���`a,���`a ���bmid3100���`a)���`a
���bc1x9# xlim and ylim of ax_pms will be automatically adjusted.���`a
���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
`dNone�