������������bsdy """
==========================
The default tick formatter
==========================

The example shows use of the default `.ScalarFormatter` with different
settings.

Example 1 : Default

Example 2 : With no Numerical Offset

Example 3 : With Mathtext
"""���`a
���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���`a
���bc1xO###############################################################################���`a
���bc1k# Example 1���`a
���`a
���`ax���`a ���aoa=���`a ���`bnp���aoa.���`farange���`a(���bmia0���`a,���`a ���bmia1���`a,���`a ���bmfc.01���`a)���`a
���`cfig���`a,���`a ���`a[���`a[���`cax1���`a,���`a ���`cax2���`a]���`a,���`a ���`a[���`cax3���`a,���`a ���`cax4���`a]���`a]���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���bmia2���`a,���`a ���bmia2���`a,���`a ���`gfigsize���aoa=���`a(���bmia6���`a,���`a ���bmia6���`a)���`a)���`a
���`cfig���aoa.���`dtext���`a(���bmfc0.5���`a,���`a ���bmfe0.975���`a,���`a ���bs1a'���bs1pDefault settings���bs1a'���`a,���`a
���`i         ���`shorizontalalignment���aoa=���bs1a'���bs1fcenter���bs1a'���`a,���`a
���`i         ���`qverticalalignment���aoa=���bs1a'���bs1ctop���bs1a'���`a)���`a
���`a
���`cax1���aoa.���`dplot���`a(���`ax���`a ���aoa*���`a ���bmfc1e5���`a ���aoa+���`a ���bmfd1e10���`a,���`a ���`ax���`a ���aoa*���`a ���bmfe1e-10���`a ���aoa+���`a ���bmfd1e-5���`a)���`a
���`a
���`cax2���aoa.���`dplot���`a(���`ax���`a ���aoa*���`a ���bmfc1e5���`a,���`a ���`ax���`a ���aoa*���`a ���bmfd1e-4���`a)���`a
���`a
���`cax3���aoa.���`dplot���`a(���aoa-���`ax���`a ���aoa*���`a ���bmfc1e5���`a ���aoa-���`a ���bmfd1e10���`a,���`a ���aoa-���`ax���`a ���aoa*���`a ���bmfd1e-5���`a ���aoa-���`a ���bmfe1e-10���`a)���`a
���`a
���`cax4���aoa.���`dplot���`a(���aoa-���`ax���`a ���aoa*���`a ���bmfc1e5���`a,���`a ���aoa-���`ax���`a ���aoa*���`a ���bmfd1e-4���`a)���`a
���`a
���`cfig���aoa.���`osubplots_adjust���`a(���`fwspace���aoa=���bmfc0.7���`a,���`a ���`fhspace���aoa=���bmfc0.6���`a)���`a
���`a
���bc1xO###############################################################################���`a
���bc1k# Example 2���`a
���`a
���`ax���`a ���aoa=���`a ���`bnp���aoa.���`farange���`a(���bmia0���`a,���`a ���bmia1���`a,���`a ���bmfc.01���`a)���`a
���`cfig���`a,���`a ���`a[���`a[���`cax1���`a,���`a ���`cax2���`a]���`a,���`a ���`a[���`cax3���`a,���`a ���`cax4���`a]���`a]���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���bmia2���`a,���`a ���bmia2���`a,���`a ���`gfigsize���aoa=���`a(���bmia6���`a,���`a ���bmia6���`a)���`a)���`a
���`cfig���aoa.���`dtext���`a(���bmfc0.5���`a,���`a ���bmfe0.975���`a,���`a ���bs1a'���bs1sNo numerical offset���bs1a'���`a,���`a
���`i         ���`shorizontalalignment���aoa=���bs1a'���bs1fcenter���bs1a'���`a,���`a
���`i         ���`qverticalalignment���aoa=���bs1a'���bs1ctop���bs1a'���`a)���`a
���`a
���`cax1���aoa.���`dplot���`a(���`ax���`a ���aoa*���`a ���bmfc1e5���`a ���aoa+���`a ���bmfd1e10���`a,���`a ���`ax���`a ���aoa*���`a ���bmfe1e-10���`a ���aoa+���`a ���bmfd1e-5���`a)���`a
���`cax1���aoa.���`pticklabel_format���`a(���`iuseOffset���aoa=���bkceFalse���`a)���`a
���`a
���`cax2���aoa.���`dplot���`a(���`ax���`a ���aoa*���`a ���bmfc1e5���`a,���`a ���`ax���`a ���aoa*���`a ���bmfd1e-4���`a)���`a
���`cax2���aoa.���`pticklabel_format���`a(���`iuseOffset���aoa=���bkceFalse���`a)���`a
���`a
���`cax3���aoa.���`dplot���`a(���aoa-���`ax���`a ���aoa*���`a ���bmfc1e5���`a ���aoa-���`a ���bmfd1e10���`a,���`a ���aoa-���`ax���`a ���aoa*���`a ���bmfd1e-5���`a ���aoa-���`a ���bmfe1e-10���`a)���`a
���`cax3���aoa.���`pticklabel_format���`a(���`iuseOffset���aoa=���bkceFalse���`a)���`a
���`a
���`cax4���aoa.���`dplot���`a(���aoa-���`ax���`a ���aoa*���`a ���bmfc1e5���`a,���`a ���aoa-���`ax���`a ���aoa*���`a ���bmfd1e-4���`a)���`a
���`cax4���aoa.���`pticklabel_format���`a(���`iuseOffset���aoa=���bkceFalse���`a)���`a
���`a
���`cfig���aoa.���`osubplots_adjust���`a(���`fwspace���aoa=���bmfc0.7���`a,���`a ���`fhspace���aoa=���bmfc0.6���`a)���`a
���`a
���bc1xO###############################################################################���`a
���bc1k# Example 3���`a
���`a
���`ax���`a ���aoa=���`a ���`bnp���aoa.���`farange���`a(���bmia0���`a,���`a ���bmia1���`a,���`a ���bmfc.01���`a)���`a
���`cfig���`a,���`a ���`a[���`a[���`cax1���`a,���`a ���`cax2���`a]���`a,���`a ���`a[���`cax3���`a,���`a ���`cax4���`a]���`a]���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���bmia2���`a,���`a ���bmia2���`a,���`a ���`gfigsize���aoa=���`a(���bmia6���`a,���`a ���bmia6���`a)���`a)���`a
���`cfig���aoa.���`dtext���`a(���bmfc0.5���`a,���`a ���bmfe0.975���`a,���`a ���bs1a'���bs1mWith mathtext���bs1a'���`a,���`a
���`i         ���`shorizontalalignment���aoa=���bs1a'���bs1fcenter���bs1a'���`a,���`a
���`i         ���`qverticalalignment���aoa=���bs1a'���bs1ctop���bs1a'���`a)���`a
���`a
���`cax1���aoa.���`dplot���`a(���`ax���`a ���aoa*���`a ���bmfc1e5���`a ���aoa+���`a ���bmfd1e10���`a,���`a ���`ax���`a ���aoa*���`a ���bmfe1e-10���`a ���aoa+���`a ���bmfd1e-5���`a)���`a
���`cax1���aoa.���`pticklabel_format���`a(���`kuseMathText���aoa=���bkcdTrue���`a)���`a
���`a
���`cax2���aoa.���`dplot���`a(���`ax���`a ���aoa*���`a ���bmfc1e5���`a,���`a ���`ax���`a ���aoa*���`a ���bmfd1e-4���`a)���`a
���`cax2���aoa.���`pticklabel_format���`a(���`kuseMathText���aoa=���bkcdTrue���`a)���`a
���`a
���`cax3���aoa.���`dplot���`a(���aoa-���`ax���`a ���aoa*���`a ���bmfc1e5���`a ���aoa-���`a ���bmfd1e10���`a,���`a ���aoa-���`ax���`a ���aoa*���`a ���bmfd1e-5���`a ���aoa-���`a ���bmfe1e-10���`a)���`a
���`cax3���aoa.���`pticklabel_format���`a(���`kuseMathText���aoa=���bkcdTrue���`a)���`a
���`a
���`cax4���aoa.���`dplot���`a(���aoa-���`ax���`a ���aoa*���`a ���bmfc1e5���`a,���`a ���aoa-���`ax���`a ���aoa*���`a ���bmfd1e-4���`a)���`a
���`cax4���aoa.���`pticklabel_format���`a(���`kuseMathText���aoa=���bkcdTrue���`a)���`a
���`a
���`cfig���aoa.���`osubplots_adjust���`a(���`fwspace���aoa=���bmfc0.7���`a,���`a ���`fhspace���aoa=���bmfc0.6���`a)���`a
���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
`dNone�