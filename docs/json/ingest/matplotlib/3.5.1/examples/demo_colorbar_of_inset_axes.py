�����������bsdxg"""
===============================
Adding a colorbar to inset axes
===============================
"""���`a
���`a
���bkndfrom���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����`a ���bknfimport���`a ���`ecbook���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���bkndfrom���`a ���bnnlmpl_toolkits���bnna.���bnnjaxes_grid1���bnna.���bnnminset_locator���`a ���bknfimport���`a ���`jinset_axes���`a,���`a ���`qzoomed_inset_axes���`a
���`a
���`a
���`cfig���`a,���`a ���`bax���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`gfigsize���aoa=���`a[���bmia5���`a,���`a ���bmia4���`a]���`a)���`a
���`bax���aoa.���`cset���`a(���`faspect���aoa=���bmia1���`a,���`a ���`dxlim���aoa=���`a(���aoa-���bmib15���`a,���`a ���bmib15���`a)���`a,���`a ���`dylim���aoa=���`a(���aoa-���bmib20���`a,���`a ���bmia5���`a)���`a)���`a
���`a
���`aZ���`a ���aoa=���`a ���`ecbook���aoa.���`oget_sample_data���`a(���bs2a"���bs2xaxes_grid/bivariate_normal.npy���bs2a"���`a,���`a ���`gnp_load���aoa=���bkcdTrue���`a)���`a
���`fextent���`a ���aoa=���`a ���`a(���aoa-���bmia3���`a,���`a ���bmia4���`a,���`a ���aoa-���bmia4���`a,���`a ���bmia3���`a)���`a
���`a
���`eaxins���`a ���aoa=���`a ���`qzoomed_inset_axes���`a(���`bax���`a,���`a ���`dzoom���aoa=���bmia2���`a,���`a ���`cloc���aoa=���bs1a'���bs1jupper left���bs1a'���`a)���`a
���`eaxins���aoa.���`cset���`a(���`fxticks���aoa=���`a[���`a]���`a,���`a ���`fyticks���aoa=���`a[���`a]���`a)���`a
���`bim���`a ���aoa=���`a ���`eaxins���aoa.���`fimshow���`a(���`aZ���`a,���`a ���`fextent���aoa=���`fextent���`a,���`a ���`forigin���aoa=���bs2a"���bs2elower���bs2a"���`a)���`a
���`a
���bc1j# colorbar���`a
���`ccax���`a ���aoa=���`a ���`jinset_axes���`a(���`eaxins���`a,���`a
���`q                 ���`ewidth���aoa=���bs2a"���bs2a5���bs2a%���bs2a"���`a,���`b  ���bc1x"# width = 10% of parent_bbox width���`a
���`q                 ���`fheight���aoa=���bs2a"���bs2c100���bs2a%���bs2a"���`a,���`b  ���bc1n# height : 50%���`a
���`q                 ���`cloc���aoa=���bs1a'���bs1jlower left���bs1a'���`a,���`a
���`q                 ���`nbbox_to_anchor���aoa=���`a(���bmfd1.05���`a,���`a ���bmfb0.���`a,���`a ���bmia1���`a,���`a ���bmia1���`a)���`a,���`a
���`q                 ���`nbbox_transform���aoa=���`eaxins���aoa.���`itransAxes���`a,���`a
���`q                 ���`iborderpad���aoa=���bmia0���`a,���`a
���`q                 ���`a)���`a
���`cfig���aoa.���`hcolorbar���`a(���`bim���`a,���`a ���`ccax���aoa=���`ccax���`a)���`a
���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
`dNone�