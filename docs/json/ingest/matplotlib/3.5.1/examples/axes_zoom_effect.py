������������bsdx;"""
================
Axes Zoom Effect
================

"""���`a
���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���`a
���bkndfrom���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnjtransforms���`a ���bknfimport���`a ���`a(���`a
���`d    ���`dBbox���`a,���`a ���`oTransformedBbox���`a,���`a ���`xblended_transform_factory���`a)���`a
���bkndfrom���`a ���bnnlmpl_toolkits���bnna.���bnnjaxes_grid1���bnna.���bnnminset_locator���`a ���bknfimport���`a ���`a(���`a
���`d    ���`iBboxPatch���`a,���`a ���`mBboxConnector���`a,���`a ���`rBboxConnectorPatch���`a)���`a
���`a
���`a
���akcdef���`a ���bnflconnect_bbox���`a(���`ebbox1���`a,���`a ���`ebbox2���`a,���`a
���`q                 ���`eloc1a���`a,���`a ���`eloc2a���`a,���`a ���`eloc1b���`a,���`a ���`eloc2b���`a,���`a
���`q                 ���`jprop_lines���`a,���`a ���`lprop_patches���aoa=���bkcdNone���`a)���`a:���`a
���`d    ���akbif���`a ���`lprop_patches���`a ���bowbis���`a ���bkcdNone���`a:���`a
���`h        ���`lprop_patches���`a ���aoa=���`a ���`a{���`a
���`l            ���aoa*���aoa*���`jprop_lines���`a,���`a
���`l            ���bs2a"���bs2ealpha���bs2a"���`a:���`a ���`jprop_lines���aoa.���`cget���`a(���bs2a"���bs2ealpha���bs2a"���`a,���`a ���bmia1���`a)���`a ���aoa*���`a ���bmfc0.2���`a,���`a
���`l            ���bs2a"���bs2gclip_on���bs2a"���`a:���`a ���bkceFalse���`a,���`a
���`h        ���`a}���`a
���`a
���`d    ���`bc1���`a ���aoa=���`a ���`mBboxConnector���`a(���`a
���`h        ���`ebbox1���`a,���`a ���`ebbox2���`a,���`a ���`dloc1���aoa=���`eloc1a���`a,���`a ���`dloc2���aoa=���`eloc2a���`a,���`a ���`gclip_on���aoa=���bkceFalse���`a,���`a ���aoa*���aoa*���`jprop_lines���`a)���`a
���`d    ���`bc2���`a ���aoa=���`a ���`mBboxConnector���`a(���`a
���`h        ���`ebbox1���`a,���`a ���`ebbox2���`a,���`a ���`dloc1���aoa=���`eloc1b���`a,���`a ���`dloc2���aoa=���`eloc2b���`a,���`a ���`gclip_on���aoa=���bkceFalse���`a,���`a ���aoa*���aoa*���`jprop_lines���`a)���`a
���`a
���`d    ���`kbbox_patch1���`a ���aoa=���`a ���`iBboxPatch���`a(���`ebbox1���`a,���`a ���aoa*���aoa*���`lprop_patches���`a)���`a
���`d    ���`kbbox_patch2���`a ���aoa=���`a ���`iBboxPatch���`a(���`ebbox2���`a,���`a ���aoa*���aoa*���`lprop_patches���`a)���`a
���`a
���`d    ���`ap���`a ���aoa=���`a ���`rBboxConnectorPatch���`a(���`ebbox1���`a,���`a ���`ebbox2���`a,���`a
���`x                           ���bc1x%# loc1a=3, loc2a=2, loc1b=4, loc2b=1,���`a
���`x                           ���`eloc1a���aoa=���`eloc1a���`a,���`a ���`eloc2a���aoa=���`eloc2a���`a,���`a ���`eloc1b���aoa=���`eloc1b���`a,���`a ���`eloc2b���aoa=���`eloc2b���`a,���`a
���`x                           ���`gclip_on���aoa=���bkceFalse���`a,���`a
���`x                           ���aoa*���aoa*���`lprop_patches���`a)���`a
���`a
���`d    ���akfreturn���`a ���`bc1���`a,���`a ���`bc2���`a,���`a ���`kbbox_patch1���`a,���`a ���`kbbox_patch2���`a,���`a ���`ap���`a
���`a
���`a
���akcdef���`a ���bnfmzoom_effect01���`a(���`cax1���`a,���`a ���`cax2���`a,���`a ���`dxmin���`a,���`a ���`dxmax���`a,���`a ���aoa*���aoa*���`fkwargs���`a)���`a:���`a
���`d    ���bsdyL"""
    Connect *ax1* and *ax2*. The *xmin*-to-*xmax* range in both axes will
    be marked.

    Parameters
    ----------
    ax1
        The main axes.
    ax2
        The zoomed axes.
    xmin, xmax
        The limits of the colored area in both plot axes.
    **kwargs
        Arguments passed to the patch constructor.
    """���`a
���`a
���`d    ���`dbbox���`a ���aoa=���`a ���`dBbox���aoa.���`lfrom_extents���`a(���`dxmin���`a,���`a ���bmia0���`a,���`a ���`dxmax���`a,���`a ���bmia1���`a)���`a
���`a
���`d    ���`gmybbox1���`a ���aoa=���`a ���`oTransformedBbox���`a(���`dbbox���`a,���`a ���`cax1���aoa.���`sget_xaxis_transform���`a(���`a)���`a)���`a
���`d    ���`gmybbox2���`a ���aoa=���`a ���`oTransformedBbox���`a(���`dbbox���`a,���`a ���`cax2���aoa.���`sget_xaxis_transform���`a(���`a)���`a)���`a
���`a
���`d    ���`lprop_patches���`a ���aoa=���`a ���`a{���aoa*���aoa*���`fkwargs���`a,���`a ���bs2a"���bs2bec���bs2a"���`a:���`a ���bs2a"���bs2dnone���bs2a"���`a,���`a ���bs2a"���bs2ealpha���bs2a"���`a:���`a ���bmfc0.2���`a}���`a
���`a
���`d    ���`bc1���`a,���`a ���`bc2���`a,���`a ���`kbbox_patch1���`a,���`a ���`kbbox_patch2���`a,���`a ���`ap���`a ���aoa=���`a ���`lconnect_bbox���`a(���`a
���`h        ���`gmybbox1���`a,���`a ���`gmybbox2���`a,���`a
���`h        ���`eloc1a���aoa=���bmia3���`a,���`a ���`eloc2a���aoa=���bmia2���`a,���`a ���`eloc1b���aoa=���bmia4���`a,���`a ���`eloc2b���aoa=���bmia1���`a,���`a
���`h        ���`jprop_lines���aoa=���`fkwargs���`a,���`a ���`lprop_patches���aoa=���`lprop_patches���`a)���`a
���`a
���`d    ���`cax1���aoa.���`iadd_patch���`a(���`kbbox_patch1���`a)���`a
���`d    ���`cax2���aoa.���`iadd_patch���`a(���`kbbox_patch2���`a)���`a
���`d    ���`cax2���aoa.���`iadd_patch���`a(���`bc1���`a)���`a
���`d    ���`cax2���aoa.���`iadd_patch���`a(���`bc2���`a)���`a
���`d    ���`cax2���aoa.���`iadd_patch���`a(���`ap���`a)���`a
���`a
���`d    ���akfreturn���`a ���`bc1���`a,���`a ���`bc2���`a,���`a ���`kbbox_patch1���`a,���`a ���`kbbox_patch2���`a,���`a ���`ap���`a
���`a
���`a
���akcdef���`a ���bnfmzoom_effect02���`a(���`cax1���`a,���`a ���`cax2���`a,���`a ���aoa*���aoa*���`fkwargs���`a)���`a:���`a
���`d    ���bsdx�"""
    ax1 : the main axes
    ax1 : the zoomed axes

    Similar to zoom_effect01.  The xmin & xmax will be taken from the
    ax1.viewLim.
    """���`a
���`a
���`d    ���`btt���`a ���aoa=���`a ���`cax1���aoa.���`jtransScale���`a ���aoa+���`a ���`a(���`cax1���aoa.���`ktransLimits���`a ���aoa+���`a ���`cax2���aoa.���`itransAxes���`a)���`a
���`d    ���`etrans���`a ���aoa=���`a ���`xblended_transform_factory���`a(���`cax2���aoa.���`itransData���`a,���`a ���`btt���`a)���`a
���`a
���`d    ���`gmybbox1���`a ���aoa=���`a ���`cax1���aoa.���`dbbox���`a
���`d    ���`gmybbox2���`a ���aoa=���`a ���`oTransformedBbox���`a(���`cax1���aoa.���`gviewLim���`a,���`a ���`etrans���`a)���`a
���`a
���`d    ���`lprop_patches���`a ���aoa=���`a ���`a{���aoa*���aoa*���`fkwargs���`a,���`a ���bs2a"���bs2bec���bs2a"���`a:���`a ���bs2a"���bs2dnone���bs2a"���`a,���`a ���bs2a"���bs2ealpha���bs2a"���`a:���`a ���bmfc0.2���`a}���`a
���`a
���`d    ���`bc1���`a,���`a ���`bc2���`a,���`a ���`kbbox_patch1���`a,���`a ���`kbbox_patch2���`a,���`a ���`ap���`a ���aoa=���`a ���`lconnect_bbox���`a(���`a
���`h        ���`gmybbox1���`a,���`a ���`gmybbox2���`a,���`a
���`h        ���`eloc1a���aoa=���bmia3���`a,���`a ���`eloc2a���aoa=���bmia2���`a,���`a ���`eloc1b���aoa=���bmia4���`a,���`a ���`eloc2b���aoa=���bmia1���`a,���`a
���`h        ���`jprop_lines���aoa=���`fkwargs���`a,���`a ���`lprop_patches���aoa=���`lprop_patches���`a)���`a
���`a
���`d    ���`cax1���aoa.���`iadd_patch���`a(���`kbbox_patch1���`a)���`a
���`d    ���`cax2���aoa.���`iadd_patch���`a(���`kbbox_patch2���`a)���`a
���`d    ���`cax2���aoa.���`iadd_patch���`a(���`bc1���`a)���`a
���`d    ���`cax2���aoa.���`iadd_patch���`a(���`bc2���`a)���`a
���`d    ���`cax2���aoa.���`iadd_patch���`a(���`ap���`a)���`a
���`a
���`d    ���akfreturn���`a ���`bc1���`a,���`a ���`bc2���`a,���`a ���`kbbox_patch1���`a,���`a ���`kbbox_patch2���`a,���`a ���`ap���`a
���`a
���`a
���`caxs���`a ���aoa=���`a ���`cplt���aoa.���`ffigure���`a(���`a)���aoa.���`nsubplot_mosaic���`a(���`a[���`a
���`d    ���`a[���bs2a"���bs2ezoom1���bs2a"���`a,���`a ���bs2a"���bs2ezoom2���bs2a"���`a]���`a,���`a
���`d    ���`a[���bs2a"���bs2dmain���bs2a"���`a,���`a ���bs2a"���bs2dmain���bs2a"���`a]���`a,���`a
���`a]���`a)���`a
���`a
���`caxs���`a[���bs2a"���bs2dmain���bs2a"���`a]���aoa.���`cset���`a(���`dxlim���aoa=���`a(���bmia0���`a,���`a ���bmia5���`a)���`a)���`a
���`mzoom_effect01���`a(���`caxs���`a[���bs2a"���bs2ezoom1���bs2a"���`a]���`a,���`a ���`caxs���`a[���bs2a"���bs2dmain���bs2a"���`a]���`a,���`a ���bmfc0.2���`a,���`a ���bmfc0.8���`a)���`a
���`caxs���`a[���bs2a"���bs2ezoom2���bs2a"���`a]���aoa.���`cset���`a(���`dxlim���aoa=���`a(���bmia2���`a,���`a ���bmia3���`a)���`a)���`a
���`mzoom_effect02���`a(���`caxs���`a[���bs2a"���bs2ezoom2���bs2a"���`a]���`a,���`a ���`caxs���`a[���bs2a"���bs2dmain���bs2a"���`a]���`a)���`a
���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
`dNone�