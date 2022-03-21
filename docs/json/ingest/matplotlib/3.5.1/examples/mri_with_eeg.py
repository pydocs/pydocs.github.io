������������bsdx�"""
============
MRI With EEG
============

Displays a set of subplots with an MRI image, its intensity
histogram and some EEG traces.
"""���`a
���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnecbook���`a ���akbas���`a ���bnnecbook���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnbcm���`a ���akbas���`a ���bnnbcm���`a
���`a
���bkndfrom���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnkcollections���`a ���bknfimport���`a ���`nLineCollection���`a
���bkndfrom���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfticker���`a ���bknfimport���`a ���`oMultipleLocator���`a
���`a
���`cfig���`a ���aoa=���`a ���`cplt���aoa.���`ffigure���`a(���bs2a"���bs2lMRI_with_EEG���bs2a"���`a)���`a
���`a
���bc1x-# Load the MRI data (256x256 16 bit integers)���`a
���akdwith���`a ���`ecbook���aoa.���`oget_sample_data���`a(���bs1a'���bs1ls1045.ima.gz���bs1a'���`a)���`a ���akbas���`a ���`edfile���`a:���`a
���`d    ���`bim���`a ���aoa=���`a ���`bnp���aoa.���`jfrombuffer���`a(���`edfile���aoa.���`dread���`a(���`a)���`a,���`a ���`bnp���aoa.���`fuint16���`a)���aoa.���`greshape���`a(���`a(���bmic256���`a,���`a ���bmic256���`a)���`a)���`a
���`a
���bc1t# Plot the MRI image���`a
���`cax0���`a ���aoa=���`a ���`cfig���aoa.���`kadd_subplot���`a(���bmia2���`a,���`a ���bmia2���`a,���`a ���bmia1���`a)���`a
���`cax0���aoa.���`fimshow���`a(���`bim���`a,���`a ���`dcmap���aoa=���`bcm���aoa.���`dgray���`a)���`a
���`cax0���aoa.���`daxis���`a(���bs1a'���bs1coff���bs1a'���`a)���`a
���`a
���bc1x%# Plot the histogram of MRI intensity���`a
���`cax1���`a ���aoa=���`a ���`cfig���aoa.���`kadd_subplot���`a(���bmia2���`a,���`a ���bmia2���`a,���`a ���bmia2���`a)���`a
���`bim���`a ���aoa=���`a ���`bnp���aoa.���`eravel���`a(���`bim���`a)���`a
���`bim���`a ���aoa=���`a ���`bim���`a[���`bnp���aoa.���`gnonzero���`a(���`bim���`a)���`a]���`b  ���bc1w# Ignore the background���`a
���`bim���`a ���aoa=���`a ���`bim���`a ���aoa/���`a ���`a(���bmia2���aoa*���aoa*���bmib16���`a ���aoa-���`a ���bmia1���`a)���`b  ���bc1k# Normalize���`a
���`cax1���aoa.���`dhist���`a(���`bim���`a,���`a ���`dbins���aoa=���bmic100���`a)���`a
���`cax1���aoa.���`exaxis���aoa.���`qset_major_locator���`a(���`oMultipleLocator���`a(���bmfc0.4���`a)���`a)���`a
���`cax1���aoa.���`mminorticks_on���`a(���`a)���`a
���`cax1���aoa.���`jset_yticks���`a(���`a[���`a]���`a)���`a
���`cax1���aoa.���`jset_xlabel���`a(���bs1a'���bs1pIntensity (a.u.)���bs1a'���`a)���`a
���`cax1���aoa.���`jset_ylabel���`a(���bs1a'���bs1kMRI density���bs1a'���`a)���`a
���`a
���bc1s# Load the EEG data���`a
���`in_samples���`a,���`a ���`fn_rows���`a ���aoa=���`a ���bmic800���`a,���`a ���bmia4���`a
���akdwith���`a ���`ecbook���aoa.���`oget_sample_data���`a(���bs1a'���bs1geeg.dat���bs1a'���`a)���`a ���akbas���`a ���`geegfile���`a:���`a
���`d    ���`ddata���`a ���aoa=���`a ���`bnp���aoa.���`hfromfile���`a(���`geegfile���`a,���`a ���`edtype���aoa=���bnbefloat���`a)���aoa.���`greshape���`a(���`a(���`in_samples���`a,���`a ���`fn_rows���`a)���`a)���`a
���`at���`a ���aoa=���`a ���bmib10���`a ���aoa*���`a ���`bnp���aoa.���`farange���`a(���`in_samples���`a)���`a ���aoa/���`a ���`in_samples���`a
���`a
���bc1n# Plot the EEG���`a
���`hticklocs���`a ���aoa=���`a ���`a[���`a]���`a
���`cax2���`a ���aoa=���`a ���`cfig���aoa.���`kadd_subplot���`a(���bmia2���`a,���`a ���bmia1���`a,���`a ���bmia2���`a)���`a
���`cax2���aoa.���`hset_xlim���`a(���bmia0���`a,���`a ���bmib10���`a)���`a
���`cax2���aoa.���`jset_xticks���`a(���`bnp���aoa.���`farange���`a(���bmib10���`a)���`a)���`a
���`ddmin���`a ���aoa=���`a ���`ddata���aoa.���`cmin���`a(���`a)���`a
���`ddmax���`a ���aoa=���`a ���`ddata���aoa.���`cmax���`a(���`a)���`a
���`bdr���`a ���aoa=���`a ���`a(���`ddmax���`a ���aoa-���`a ���`ddmin���`a)���`a ���aoa*���`a ���bmfc0.7���`b  ���bc1s# Crowd them a bit.���`a
���`by0���`a ���aoa=���`a ���`ddmin���`a
���`by1���`a ���aoa=���`a ���`a(���`fn_rows���`a ���aoa-���`a ���bmia1���`a)���`a ���aoa*���`a ���`bdr���`a ���aoa+���`a ���`ddmax���`a
���`cax2���aoa.���`hset_ylim���`a(���`by0���`a,���`a ���`by1���`a)���`a
���`a
���`dsegs���`a ���aoa=���`a ���`a[���`a]���`a
���akcfor���`a ���`ai���`a ���bowbin���`a ���bnberange���`a(���`fn_rows���`a)���`a:���`a
���`d    ���`dsegs���aoa.���`fappend���`a(���`bnp���aoa.���`lcolumn_stack���`a(���`a(���`at���`a,���`a ���`ddata���`a[���`a:���`a,���`a ���`ai���`a]���`a)���`a)���`a)���`a
���`d    ���`hticklocs���aoa.���`fappend���`a(���`ai���`a ���aoa*���`a ���`bdr���`a)���`a
���`a
���`goffsets���`a ���aoa=���`a ���`bnp���aoa.���`ezeros���`a(���`a(���`fn_rows���`a,���`a ���bmia2���`a)���`a,���`a ���`edtype���aoa=���bnbefloat���`a)���`a
���`goffsets���`a[���`a:���`a,���`a ���bmia1���`a]���`a ���aoa=���`a ���`hticklocs���`a
���`a
���`elines���`a ���aoa=���`a ���`nLineCollection���`a(���`dsegs���`a,���`a ���`goffsets���aoa=���`goffsets���`a,���`a ���`ktransOffset���aoa=���bkcdNone���`a)���`a
���`cax2���aoa.���`nadd_collection���`a(���`elines���`a)���`a
���`a
���bc1x6# Set the yticks to use axes coordinates on the y axis���`a
���`cax2���aoa.���`jset_yticks���`a(���`hticklocs���`a,���`a ���`flabels���aoa=���`a[���bs1a'���bs1cPG3���bs1a'���`a,���`a ���bs1a'���bs1cPG5���bs1a'���`a,���`a ���bs1a'���bs1cPG7���bs1a'���`a,���`a ���bs1a'���bs1cPG9���bs1a'���`a]���`a)���`a
���`a
���`cax2���aoa.���`jset_xlabel���`a(���bs1a'���bs1hTime (s)���bs1a'���`a)���`a
���`a
���`a
���`cplt���aoa.���`ltight_layout���`a(���`a)���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
`dNone�