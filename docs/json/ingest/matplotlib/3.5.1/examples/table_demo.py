�����������bsdxb"""
==========
Table Demo
==========

Demo of table function to display a table within a plot.
"""���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���`a
���`a
���`ddata���`a ���aoa=���`a ���`a[���`a[���`a ���bmie66386���`a,���`a ���bmif174296���`a,���`b  ���bmie75131���`a,���`a ���bmif577908���`a,���`b  ���bmie32015���`a]���`a,���`a
���`h        ���`a[���`a ���bmie58230���`a,���`a ���bmif381139���`a,���`b  ���bmie78045���`a,���`b  ���bmie99308���`a,���`a ���bmif160454���`a]���`a,���`a
���`h        ���`a[���`a ���bmie89135���`a,���`b  ���bmie80552���`a,���`a ���bmif152558���`a,���`a ���bmif497981���`a,���`a ���bmif603535���`a]���`a,���`a
���`h        ���`a[���`a ���bmie78415���`a,���`b  ���bmie81858���`a,���`a ���bmif150656���`a,���`a ���bmif193263���`a,���`b  ���bmie69638���`a]���`a,���`a
���`h        ���`a[���bmif139361���`a,���`a ���bmif331509���`a,���`a ���bmif343164���`a,���`a ���bmif781380���`a,���`b  ���bmie52269���`a]���`a]���`a
���`a
���`gcolumns���`a ���aoa=���`a ���`a(���bs1a'���bs1fFreeze���bs1a'���`a,���`a ���bs1a'���bs1dWind���bs1a'���`a,���`a ���bs1a'���bs1eFlood���bs1a'���`a,���`a ���bs1a'���bs1eQuake���bs1a'���`a,���`a ���bs1a'���bs1dHail���bs1a'���`a)���`a
���`drows���`a ���aoa=���`a ���`a[���bs1a'���bsib%d���bs1e year���bs1a'���`a ���aoa%���`a ���`ax���`a ���akcfor���`a ���`ax���`a ���bowbin���`a ���`a(���bmic100���`a,���`a ���bmib50���`a,���`a ���bmib20���`a,���`a ���bmib10���`a,���`a ���bmia5���`a)���`a]���`a
���`a
���`fvalues���`a ���aoa=���`a ���`bnp���aoa.���`farange���`a(���bmia0���`a,���`a ���bmid2500���`a,���`a ���bmic500���`a)���`a
���`ovalue_increment���`a ���aoa=���`a ���bmid1000���`a
���`a
���bc1x'# Get some pastel shades for the colors���`a
���`fcolors���`a ���aoa=���`a ���`cplt���aoa.���`bcm���aoa.���`dBuPu���`a(���`bnp���aoa.���`hlinspace���`a(���bmia0���`a,���`a ���bmfc0.5���`a,���`a ���bnbclen���`a(���`drows���`a)���`a)���`a)���`a
���`fn_rows���`a ���aoa=���`a ���bnbclen���`a(���`ddata���`a)���`a
���`a
���`eindex���`a ���aoa=���`a ���`bnp���aoa.���`farange���`a(���bnbclen���`a(���`gcolumns���`a)���`a)���`a ���aoa+���`a ���bmfc0.3���`a
���`ibar_width���`a ���aoa=���`a ���bmfc0.4���`a
���`a
���bc1x;# Initialize the vertical-offset for the stacked bar chart.���`a
���`hy_offset���`a ���aoa=���`a ���`bnp���aoa.���`ezeros���`a(���bnbclen���`a(���`gcolumns���`a)���`a)���`a
���`a
���bc1x0# Plot bars and create text labels for the table���`a
���`icell_text���`a ���aoa=���`a ���`a[���`a]���`a
���akcfor���`a ���`crow���`a ���bowbin���`a ���bnberange���`a(���`fn_rows���`a)���`a:���`a
���`d    ���`cplt���aoa.���`cbar���`a(���`eindex���`a,���`a ���`ddata���`a[���`crow���`a]���`a,���`a ���`ibar_width���`a,���`a ���`fbottom���aoa=���`hy_offset���`a,���`a ���`ecolor���aoa=���`fcolors���`a[���`crow���`a]���`a)���`a
���`d    ���`hy_offset���`a ���aoa=���`a ���`hy_offset���`a ���aoa+���`a ���`ddata���`a[���`crow���`a]���`a
���`d    ���`icell_text���aoa.���`fappend���`a(���`a[���bs1a'���bsie%1.1f���bs1a'���`a ���aoa%���`a ���`a(���`ax���`a ���aoa/���`a ���bmff1000.0���`a)���`a ���akcfor���`a ���`ax���`a ���bowbin���`a ���`hy_offset���`a]���`a)���`a
���bc1xF# Reverse colors and text labels to display the last value at the top.���`a
���`fcolors���`a ���aoa=���`a ���`fcolors���`a[���`a:���`a:���aoa-���bmia1���`a]���`a
���`icell_text���aoa.���`greverse���`a(���`a)���`a
���`a
���bc1x'# Add a table at the bottom of the axes���`a
���`ithe_table���`a ���aoa=���`a ���`cplt���aoa.���`etable���`a(���`hcellText���aoa=���`icell_text���`a,���`a
���`v                      ���`irowLabels���aoa=���`drows���`a,���`a
���`v                      ���`jrowColours���aoa=���`fcolors���`a,���`a
���`v                      ���`icolLabels���aoa=���`gcolumns���`a,���`a
���`v                      ���`cloc���aoa=���bs1a'���bs1fbottom���bs1a'���`a)���`a
���`a
���bc1x+# Adjust layout to make room for the table:���`a
���`cplt���aoa.���`osubplots_adjust���`a(���`dleft���aoa=���bmfc0.2���`a,���`a ���`fbottom���aoa=���bmfc0.2���`a)���`a
���`a
���`cplt���aoa.���`fylabel���`a(���bs2a"���bs2iLoss in $���bsic{0}���bs2a'���bs2as���bs2a"���aoa.���`fformat���`a(���`ovalue_increment���`a)���`a)���`a
���`cplt���aoa.���`fyticks���`a(���`fvalues���`a ���aoa*���`a ���`ovalue_increment���`a,���`a ���`a[���bs1a'���bsib%d���bs1a'���`a ���aoa%���`a ���`cval���`a ���akcfor���`a ���`cval���`a ���bowbin���`a ���`fvalues���`a]���`a)���`a
���`cplt���aoa.���`fxticks���`a(���`a[���`a]���`a)���`a
���`cplt���aoa.���`etitle���`a(���bs1a'���bs1pLoss by Disaster���bs1a'���`a)���`a
���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
`dNone�