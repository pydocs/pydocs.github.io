��������%���bsdy%"""
==========
AGG filter
==========

Most pixel-based backends in Matplotlib use `Anti-Grain Geometry (AGG)`_ for
rendering. You can modify the rendering of Artists by applying a filter via
`.Artist.set_agg_filter`.

.. _Anti-Grain Geometry (AGG): http://agg.sourceforge.net/antigrain.com
"""���`a
���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnbcm���`a ���akbas���`a ���bnnbcm���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnjtransforms���`a ���akbas���`a ���bnnkmtransforms���`a
���bkndfrom���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfcolors���`a ���bknfimport���`a ���`kLightSource���`a
���bkndfrom���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfartist���`a ���bknfimport���`a ���`fArtist���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���`a
���`a
���akcdef���`a ���bnfhsmooth1d���`a(���`ax���`a,���`a ���`jwindow_len���`a)���`a:���`a
���`d    ���bc1xK# copied from https://scipy-cookbook.readthedocs.io/items/SignalSmooth.html���`a
���`d    ���`as���`a ���aoa=���`a ���`bnp���aoa.���`br_���`a[���bmia2���aoa*���`ax���`a[���bmia0���`a]���`a ���aoa-���`a ���`ax���`a[���`jwindow_len���`a:���bmia1���`a:���aoa-���bmia1���`a]���`a,���`a ���`ax���`a,���`a ���bmia2���aoa*���`ax���`a[���aoa-���bmia1���`a]���`a ���aoa-���`a ���`ax���`a[���aoa-���bmia1���`a:���aoa-���`jwindow_len���`a:���aoa-���bmia1���`a]���`a]���`a
���`d    ���`aw���`a ���aoa=���`a ���`bnp���aoa.���`ghanning���`a(���`jwindow_len���`a)���`a
���`d    ���`ay���`a ���aoa=���`a ���`bnp���aoa.���`hconvolve���`a(���`aw���aoa/���`aw���aoa.���`csum���`a(���`a)���`a,���`a ���`as���`a,���`a ���`dmode���aoa=���bs1a'���bs1dsame���bs1a'���`a)���`a
���`d    ���akfreturn���`a ���`ay���`a[���`jwindow_len���aoa-���bmia1���`a:���aoa-���`jwindow_len���aoa+���bmia1���`a]���`a
���`a
���`a
���akcdef���`a ���bnfhsmooth2d���`a(���`aA���`a,���`a ���`esigma���aoa=���bmia3���`a)���`a:���`a
���`d    ���`jwindow_len���`a ���aoa=���`a ���bnbcmax���`a(���bnbcint���`a(���`esigma���`a)���`a,���`a ���bmia3���`a)���`a ���aoa*���`a ���bmia2���`a ���aoa+���`a ���bmia1���`a
���`d    ���`aA���`a ���aoa=���`a ���`bnp���aoa.���`papply_along_axis���`a(���`hsmooth1d���`a,���`a ���bmia0���`a,���`a ���`aA���`a,���`a ���`jwindow_len���`a)���`a
���`d    ���`aA���`a ���aoa=���`a ���`bnp���aoa.���`papply_along_axis���`a(���`hsmooth1d���`a,���`a ���bmia1���`a,���`a ���`aA���`a,���`a ���`jwindow_len���`a)���`a
���`d    ���akfreturn���`a ���`aA���`a
���`a
���`a
���akeclass���`a ���bncjBaseFilter���`a:���`a
���`a
���`d    ���akcdef���`a ���bnfgget_pad���`a(���bbpdself���`a,���`a ���`cdpi���`a)���`a:���`a
���`h        ���akfreturn���`a ���bmia0���`a
���`a
���`d    ���akcdef���`a ���bnfmprocess_image���`a(���`jpadded_src���`a,���`a ���`cdpi���`a)���`a:���`a
���`h        ���akeraise���`a ���bnesNotImplementedError���`a(���bs2a"���bs2x"Should be overridden by subclasses���bs2a"���`a)���`a
���`a
���`d    ���akcdef���`a ���bfmh__call__���`a(���bbpdself���`a,���`a ���`bim���`a,���`a ���`cdpi���`a)���`a:���`a
���`h        ���`cpad���`a ���aoa=���`a ���bbpdself���aoa.���`gget_pad���`a(���`cdpi���`a)���`a
���`h        ���`jpadded_src���`a ���aoa=���`a ���`bnp���aoa.���`cpad���`a(���`bim���`a,���`a ���`a[���`a(���`cpad���`a,���`a ���`cpad���`a)���`a,���`a ���`a(���`cpad���`a,���`a ���`cpad���`a)���`a,���`a ���`a(���bmia0���`a,���`a ���bmia0���`a)���`a]���`a,���`a ���bs2a"���bs2hconstant���bs2a"���`a)���`a
���`h        ���`itgt_image���`a ���aoa=���`a ���bbpdself���aoa.���`mprocess_image���`a(���`jpadded_src���`a,���`a ���`cdpi���`a)���`a
���`h        ���akfreturn���`a ���`itgt_image���`a,���`a ���aoa-���`cpad���`a,���`a ���aoa-���`cpad���`a
���`a
���`a
���akeclass���`a ���bnclOffsetFilter���`a(���`jBaseFilter���`a)���`a:���`a
���`a
���`d    ���akcdef���`a ���bfmh__init__���`a(���bbpdself���`a,���`a ���`goffsets���aoa=���`a(���bmia0���`a,���`a ���bmia0���`a)���`a)���`a:���`a
���`h        ���bbpdself���aoa.���`goffsets���`a ���aoa=���`a ���`goffsets���`a
���`a
���`d    ���akcdef���`a ���bnfgget_pad���`a(���bbpdself���`a,���`a ���`cdpi���`a)���`a:���`a
���`h        ���akfreturn���`a ���bnbcint���`a(���bnbcmax���`a(���bbpdself���aoa.���`goffsets���`a)���`a ���aoa/���`a ���bmib72���`a ���aoa*���`a ���`cdpi���`a)���`a
���`a
���`d    ���akcdef���`a ���bnfmprocess_image���`a(���bbpdself���`a,���`a ���`jpadded_src���`a,���`a ���`cdpi���`a)���`a:���`a
���`h        ���`box���`a,���`a ���`boy���`a ���aoa=���`a ���bbpdself���aoa.���`goffsets���`a
���`h        ���`ba1���`a ���aoa=���`a ���`bnp���aoa.���`droll���`a(���`jpadded_src���`a,���`a ���bnbcint���`a(���`box���`a ���aoa/���`a ���bmib72���`a ���aoa*���`a ���`cdpi���`a)���`a,���`a ���`daxis���aoa=���bmia1���`a)���`a
���`h        ���`ba2���`a ���aoa=���`a ���`bnp���aoa.���`droll���`a(���`ba1���`a,���`a ���aoa-���bnbcint���`a(���`boy���`a ���aoa/���`a ���bmib72���`a ���aoa*���`a ���`cdpi���`a)���`a,���`a ���`daxis���aoa=���bmia0���`a)���`a
���`h        ���akfreturn���`a ���`ba2���`a
���`a
���`a
���akeclass���`a ���bncnGaussianFilter���`a(���`jBaseFilter���`a)���`a:���`a
���`d    ���bsdx"""Simple Gaussian filter."""���`a
���`a
���`d    ���akcdef���`a ���bfmh__init__���`a(���bbpdself���`a,���`a ���`esigma���`a,���`a ���`ealpha���aoa=���bmfc0.5���`a,���`a ���`ecolor���aoa=���`a(���bmia0���`a,���`a ���bmia0���`a,���`a ���bmia0���`a)���`a)���`a:���`a
���`h        ���bbpdself���aoa.���`esigma���`a ���aoa=���`a ���`esigma���`a
���`h        ���bbpdself���aoa.���`ealpha���`a ���aoa=���`a ���`ealpha���`a
���`h        ���bbpdself���aoa.���`ecolor���`a ���aoa=���`a ���`ecolor���`a
���`a
���`d    ���akcdef���`a ���bnfgget_pad���`a(���bbpdself���`a,���`a ���`cdpi���`a)���`a:���`a
���`h        ���akfreturn���`a ���bnbcint���`a(���bbpdself���aoa.���`esigma���aoa*���bmia3���`a ���aoa/���`a ���bmib72���`a ���aoa*���`a ���`cdpi���`a)���`a
���`a
���`d    ���akcdef���`a ���bnfmprocess_image���`a(���bbpdself���`a,���`a ���`jpadded_src���`a,���`a ���`cdpi���`a)���`a:���`a
���`h        ���`itgt_image���`a ���aoa=���`a ���`bnp���aoa.���`jempty_like���`a(���`jpadded_src���`a)���`a
���`h        ���`itgt_image���`a[���`a:���`a,���`a ���`a:���`a,���`a ���`a:���bmia3���`a]���`a ���aoa=���`a ���bbpdself���aoa.���`ecolor���`a
���`h        ���`itgt_image���`a[���`a:���`a,���`a ���`a:���`a,���`a ���bmia3���`a]���`a ���aoa=���`a ���`hsmooth2d���`a(���`jpadded_src���`a[���`a:���`a,���`a ���`a:���`a,���`a ���bmia3���`a]���`a ���aoa*���`a ���bbpdself���aoa.���`ealpha���`a,���`a
���`x&                                      ���bbpdself���aoa.���`esigma���`a ���aoa/���`a ���bmib72���`a ���aoa*���`a ���`cdpi���`a)���`a
���`h        ���akfreturn���`a ���`itgt_image���`a
���`a
���`a
���akeclass���`a ���bncpDropShadowFilter���`a(���`jBaseFilter���`a)���`a:���`a
���`a
���`d    ���akcdef���`a ���bfmh__init__���`a(���bbpdself���`a,���`a ���`esigma���`a,���`a ���`ealpha���aoa=���bmfc0.3���`a,���`a ���`ecolor���aoa=���`a(���bmia0���`a,���`a ���bmia0���`a,���`a ���bmia0���`a)���`a,���`a ���`goffsets���aoa=���`a(���bmia0���`a,���`a ���bmia0���`a)���`a)���`a:���`a
���`h        ���bbpdself���aoa.���`lgauss_filter���`a ���aoa=���`a ���`nGaussianFilter���`a(���`esigma���`a,���`a ���`ealpha���`a,���`a ���`ecolor���`a)���`a
���`h        ���bbpdself���aoa.���`moffset_filter���`a ���aoa=���`a ���`lOffsetFilter���`a(���`goffsets���`a)���`a
���`a
���`d    ���akcdef���`a ���bnfgget_pad���`a(���bbpdself���`a,���`a ���`cdpi���`a)���`a:���`a
���`h        ���akfreturn���`a ���bnbcmax���`a(���bbpdself���aoa.���`lgauss_filter���aoa.���`gget_pad���`a(���`cdpi���`a)���`a,���`a
���`s                   ���bbpdself���aoa.���`moffset_filter���aoa.���`gget_pad���`a(���`cdpi���`a)���`a)���`a
���`a
���`d    ���akcdef���`a ���bnfmprocess_image���`a(���bbpdself���`a,���`a ���`jpadded_src���`a,���`a ���`cdpi���`a)���`a:���`a
���`h        ���`bt1���`a ���aoa=���`a ���bbpdself���aoa.���`lgauss_filter���aoa.���`mprocess_image���`a(���`jpadded_src���`a,���`a ���`cdpi���`a)���`a
���`h        ���`bt2���`a ���aoa=���`a ���bbpdself���aoa.���`moffset_filter���aoa.���`mprocess_image���`a(���`bt1���`a,���`a ���`cdpi���`a)���`a
���`h        ���akfreturn���`a ���`bt2���`a
���`a
���`a
���akeclass���`a ���bnckLightFilter���`a(���`jBaseFilter���`a)���`a:���`a
���`a
���`d    ���akcdef���`a ���bfmh__init__���`a(���bbpdself���`a,���`a ���`esigma���`a,���`a ���`hfraction���aoa=���bmfc0.5���`a)���`a:���`a
���`h        ���bbpdself���aoa.���`lgauss_filter���`a ���aoa=���`a ���`nGaussianFilter���`a(���`esigma���`a,���`a ���`ealpha���aoa=���bmia1���`a)���`a
���`h        ���bbpdself���aoa.���`llight_source���`a ���aoa=���`a ���`kLightSource���`a(���`a)���`a
���`h        ���bbpdself���aoa.���`hfraction���`a ���aoa=���`a ���`hfraction���`a
���`a
���`d    ���akcdef���`a ���bnfgget_pad���`a(���bbpdself���`a,���`a ���`cdpi���`a)���`a:���`a
���`h        ���akfreturn���`a ���bbpdself���aoa.���`lgauss_filter���aoa.���`gget_pad���`a(���`cdpi���`a)���`a
���`a
���`d    ���akcdef���`a ���bnfmprocess_image���`a(���bbpdself���`a,���`a ���`jpadded_src���`a,���`a ���`cdpi���`a)���`a:���`a
���`h        ���`bt1���`a ���aoa=���`a ���bbpdself���aoa.���`lgauss_filter���aoa.���`mprocess_image���`a(���`jpadded_src���`a,���`a ���`cdpi���`a)���`a
���`h        ���`ielevation���`a ���aoa=���`a ���`bt1���`a[���`a:���`a,���`a ���`a:���`a,���`a ���bmia3���`a]���`a
���`h        ���`crgb���`a ���aoa=���`a ���`jpadded_src���`a[���`a:���`a,���`a ���`a:���`a,���`a ���`a:���bmia3���`a]���`a
���`h        ���`ealpha���`a ���aoa=���`a ���`jpadded_src���`a[���`a:���`a,���`a ���`a:���`a,���`a ���bmia3���`a:���`a]���`a
���`h        ���`drgb2���`a ���aoa=���`a ���bbpdself���aoa.���`llight_source���aoa.���`ishade_rgb���`a(���`crgb���`a,���`a ���`ielevation���`a,���`a
���`x+                                           ���`hfraction���aoa=���bbpdself���aoa.���`hfraction���`a)���`a
���`h        ���akfreturn���`a ���`bnp���aoa.���`kconcatenate���`a(���`a[���`drgb2���`a,���`a ���`ealpha���`a]���`a,���`a ���aoa-���bmia1���`a)���`a
���`a
���`a
���akeclass���`a ���bncjGrowFilter���`a(���`jBaseFilter���`a)���`a:���`a
���`d    ���bsdw"""Enlarge the area."""���`a
���`a
���`d    ���akcdef���`a ���bfmh__init__���`a(���bbpdself���`a,���`a ���`fpixels���`a,���`a ���`ecolor���aoa=���`a(���bmia1���`a,���`a ���bmia1���`a,���`a ���bmia1���`a)���`a)���`a:���`a
���`h        ���bbpdself���aoa.���`fpixels���`a ���aoa=���`a ���`fpixels���`a
���`h        ���bbpdself���aoa.���`ecolor���`a ���aoa=���`a ���`ecolor���`a
���`a
���`d    ���akcdef���`a ���bfmh__call__���`a(���bbpdself���`a,���`a ���`bim���`a,���`a ���`cdpi���`a)���`a:���`a
���`h        ���`ealpha���`a ���aoa=���`a ���`bnp���aoa.���`cpad���`a(���`bim���`a[���aoa.���aoa.���aoa.���`a,���`a ���bmia3���`a]���`a,���`a ���bbpdself���aoa.���`fpixels���`a,���`a ���bs2a"���bs2hconstant���bs2a"���`a)���`a
���`h        ���`falpha2���`a ���aoa=���`a ���`bnp���aoa.���`dclip���`a(���`hsmooth2d���`a(���`ealpha���`a,���`a ���bbpdself���aoa.���`fpixels���`a ���aoa/���`a ���bmib72���`a ���aoa*���`a ���`cdpi���`a)���`a ���aoa*���`a ���bmia5���`a,���`a ���bmia0���`a,���`a ���bmia1���`a)���`a
���`h        ���`fnew_im���`a ���aoa=���`a ���`bnp���aoa.���`eempty���`a(���`a(���aoa*���`falpha2���aoa.���`eshape���`a,���`a ���bmia4���`a)���`a)���`a
���`h        ���`fnew_im���`a[���`a:���`a,���`a ���`a:���`a,���`a ���`a:���bmia3���`a]���`a ���aoa=���`a ���bbpdself���aoa.���`ecolor���`a
���`h        ���`fnew_im���`a[���`a:���`a,���`a ���`a:���`a,���`a ���bmia3���`a]���`a ���aoa=���`a ���`falpha2���`a
���`h        ���`goffsetx���`a,���`a ���`goffsety���`a ���aoa=���`a ���aoa-���bbpdself���aoa.���`fpixels���`a,���`a ���aoa-���bbpdself���aoa.���`fpixels���`a
���`h        ���akfreturn���`a ���`fnew_im���`a,���`a ���`goffsetx���`a,���`a ���`goffsety���`a
���`a
���`a
���akeclass���`a ���bncrFilteredArtistList���`a(���`fArtist���`a)���`a:���`a
���`d    ���bsdx<"""A simple container to filter multiple artists at once."""���`a
���`a
���`d    ���akcdef���`a ���bfmh__init__���`a(���bbpdself���`a,���`a ���`kartist_list���`a,���`a ���bnbffilter���`a)���`a:���`a
���`h        ���bnbesuper���`a(���`a)���aoa.���bfmh__init__���`a(���`a)���`a
���`h        ���bbpdself���aoa.���`l_artist_list���`a ���aoa=���`a ���`kartist_list���`a
���`h        ���bbpdself���aoa.���`g_filter���`a ���aoa=���`a ���bnbffilter���`a
���`a
���`d    ���akcdef���`a ���bnfddraw���`a(���bbpdself���`a,���`a ���`hrenderer���`a)���`a:���`a
���`h        ���`hrenderer���aoa.���`qstart_rasterizing���`a(���`a)���`a
���`h        ���`hrenderer���aoa.���`lstart_filter���`a(���`a)���`a
���`h        ���akcfor���`a ���`aa���`a ���bowbin���`a ���bbpdself���aoa.���`l_artist_list���`a:���`a
���`l            ���`aa���aoa.���`ddraw���`a(���`hrenderer���`a)���`a
���`h        ���`hrenderer���aoa.���`kstop_filter���`a(���bbpdself���aoa.���`g_filter���`a)���`a
���`h        ���`hrenderer���aoa.���`pstop_rasterizing���`a(���`a)���`a
���`a
���`a
���akcdef���`a ���bnfmfiltered_text���`a(���`bax���`a)���`a:���`a
���`d    ���bc1x$# mostly copied from contour_demo.py���`a
���`a
���`d    ���bc1o# prepare image���`a
���`d    ���`edelta���`a ���aoa=���`a ���bmfe0.025���`a
���`d    ���`ax���`a ���aoa=���`a ���`bnp���aoa.���`farange���`a(���aoa-���bmfc3.0���`a,���`a ���bmfc3.0���`a,���`a ���`edelta���`a)���`a
���`d    ���`ay���`a ���aoa=���`a ���`bnp���aoa.���`farange���`a(���aoa-���bmfc2.0���`a,���`a ���bmfc2.0���`a,���`a ���`edelta���`a)���`a
���`d    ���`aX���`a,���`a ���`aY���`a ���aoa=���`a ���`bnp���aoa.���`hmeshgrid���`a(���`ax���`a,���`a ���`ay���`a)���`a
���`d    ���`bZ1���`a ���aoa=���`a ���`bnp���aoa.���`cexp���`a(���aoa-���`aX���aoa*���aoa*���bmia2���`a ���aoa-���`a ���`aY���aoa*���aoa*���bmia2���`a)���`a
���`d    ���`bZ2���`a ���aoa=���`a ���`bnp���aoa.���`cexp���`a(���aoa-���`a(���`aX���`a ���aoa-���`a ���bmia1���`a)���aoa*���aoa*���bmia2���`a ���aoa-���`a ���`a(���`aY���`a ���aoa-���`a ���bmia1���`a)���aoa*���aoa*���bmia2���`a)���`a
���`d    ���`aZ���`a ���aoa=���`a ���`a(���`bZ1���`a ���aoa-���`a ���`bZ2���`a)���`a ���aoa*���`a ���bmia2���`a
���`a
���`d    ���bc1f# draw���`a
���`d    ���`bax���aoa.���`fimshow���`a(���`aZ���`a,���`a ���`minterpolation���aoa=���bs1a'���bs1hbilinear���bs1a'���`a,���`a ���`forigin���aoa=���bs1a'���bs1elower���bs1a'���`a,���`a
���`n              ���`dcmap���aoa=���`bcm���aoa.���`dgray���`a,���`a ���`fextent���aoa=���`a(���aoa-���bmia3���`a,���`a ���bmia3���`a,���`a ���aoa-���bmia2���`a,���`a ���bmia2���`a)���`a,���`a ���`faspect���aoa=���bs1a'���bs1dauto���bs1a'���`a)���`a
���`d    ���`flevels���`a ���aoa=���`a ���`bnp���aoa.���`farange���`a(���aoa-���bmfc1.2���`a,���`a ���bmfc1.6���`a,���`a ���bmfc0.2���`a)���`a
���`d    ���`bCS���`a ���aoa=���`a ���`bax���aoa.���`gcontour���`a(���`aZ���`a,���`a ���`flevels���`a,���`a
���`t                    ���`forigin���aoa=���bs1a'���bs1elower���bs1a'���`a,���`a
���`t                    ���`jlinewidths���aoa=���bmia2���`a,���`a
���`t                    ���`fextent���aoa=���`a(���aoa-���bmia3���`a,���`a ���bmia3���`a,���`a ���aoa-���bmia2���`a,���`a ���bmia2���`a)���`a)���`a
���`a
���`d    ���bc1o# contour label���`a
���`d    ���`bcl���`a ���aoa=���`a ���`bax���aoa.���`fclabel���`a(���`bCS���`a,���`a ���`flevels���`a[���bmia1���`a:���`a:���bmia2���`a]���`a,���`b  ���bc1x# label every second level���`a
���`s                   ���`finline���aoa=���bkcdTrue���`a,���`a
���`s                   ���`cfmt���aoa=���bs1a'���bsie%1.1f���bs1a'���`a,���`a
���`s                   ���`hfontsize���aoa=���bmib11���`a)���`a
���`a
���`d    ���bc1x# change clabel color to black���`a
���`d    ���bkndfrom���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnkpatheffects���`a ���bknfimport���`a ���`fNormal���`a
���`d    ���akcfor���`a ���`at���`a ���bowbin���`a ���`bcl���`a:���`a
���`h        ���`at���aoa.���`iset_color���`a(���bs2a"���bs2ak���bs2a"���`a)���`a
���`h        ���bc1x5# to force TextPath (i.e., same font in all backends)���`a
���`h        ���`at���aoa.���`pset_path_effects���`a(���`a[���`fNormal���`a(���`a)���`a]���`a)���`a
���`a
���`d    ���bc1x2# Add white glows to improve visibility of labels.���`a
���`d    ���`kwhite_glows���`a ���aoa=���`a ���`rFilteredArtistList���`a(���`bcl���`a,���`a ���`jGrowFilter���`a(���bmia3���`a)���`a)���`a
���`d    ���`bax���aoa.���`jadd_artist���`a(���`kwhite_glows���`a)���`a
���`d    ���`kwhite_glows���aoa.���`jset_zorder���`a(���`bcl���`a[���bmia0���`a]���aoa.���`jget_zorder���`a(���`a)���`a ���aoa-���`a ���bmfc0.1���`a)���`a
���`a
���`d    ���`bax���aoa.���`exaxis���aoa.���`kset_visible���`a(���bkceFalse���`a)���`a
���`d    ���`bax���aoa.���`eyaxis���aoa.���`kset_visible���`a(���bkceFalse���`a)���`a
���`a
���`a
���akcdef���`a ���bnfpdrop_shadow_line���`a(���`bax���`a)���`a:���`a
���`d    ���bc1x.# copied from examples/misc/svg_filter_line.py���`a
���`a
���`d    ���bc1l# draw lines���`a
���`d    ���`bl1���`a,���`a ���aoa=���`a ���`bax���aoa.���`dplot���`a(���`a[���bmfc0.1���`a,���`a ���bmfc0.5���`a,���`a ���bmfc0.9���`a]���`a,���`a ���`a[���bmfc0.1���`a,���`a ���bmfc0.9���`a,���`a ���bmfc0.5���`a]���`a,���`a ���bs2a"���bs2cbo-���bs2a"���`a)���`a
���`d    ���`bl2���`a,���`a ���aoa=���`a ���`bax���aoa.���`dplot���`a(���`a[���bmfc0.1���`a,���`a ���bmfc0.5���`a,���`a ���bmfc0.9���`a]���`a,���`a ���`a[���bmfc0.5���`a,���`a ���bmfc0.2���`a,���`a ���bmfc0.7���`a]���`a,���`a ���bs2a"���bs2cro-���bs2a"���`a)���`a
���`a
���`d    ���`egauss���`a ���aoa=���`a ���`pDropShadowFilter���`a(���bmia4���`a)���`a
���`a
���`d    ���akcfor���`a ���`al���`a ���bowbin���`a ���`a[���`bl1���`a,���`a ���`bl2���`a]���`a:���`a
���`a
���`h        ���bc1x2# draw shadows with same lines with slight offset.���`a
���`h        ���`bxx���`a ���aoa=���`a ���`al���aoa.���`iget_xdata���`a(���`a)���`a
���`h        ���`byy���`a ���aoa=���`a ���`al���aoa.���`iget_ydata���`a(���`a)���`a
���`h        ���`fshadow���`a,���`a ���aoa=���`a ���`bax���aoa.���`dplot���`a(���`bxx���`a,���`a ���`byy���`a)���`a
���`h        ���`fshadow���aoa.���`kupdate_from���`a(���`al���`a)���`a
���`a
���`h        ���bc1r# offset transform���`a
���`h        ���`bot���`a ���aoa=���`a ���`kmtransforms���aoa.���`koffset_copy���`a(���`al���aoa.���`mget_transform���`a(���`a)���`a,���`a ���`bax���aoa.���`ffigure���`a,���`a
���`x%                                     ���`ax���aoa=���bmfc4.0���`a,���`a ���`ay���aoa=���aoa-���bmfc6.0���`a,���`a ���`eunits���aoa=���bs1a'���bs1fpoints���bs1a'���`a)���`a
���`a
���`h        ���`fshadow���aoa.���`mset_transform���`a(���`bot���`a)���`a
���`a
���`h        ���bc1xA# adjust zorder of the shadow lines so that it is drawn below the���`a
���`h        ���bc1p# original lines���`a
���`h        ���`fshadow���aoa.���`jset_zorder���`a(���`al���aoa.���`jget_zorder���`a(���`a)���`a ���aoa-���`a ���bmfc0.5���`a)���`a
���`h        ���`fshadow���aoa.���`nset_agg_filter���`a(���`egauss���`a)���`a
���`h        ���`fshadow���aoa.���`nset_rasterized���`a(���bkcdTrue���`a)���`b  ���bc1x!# to support mixed-mode renderers���`a
���`a
���`d    ���`bax���aoa.���`hset_xlim���`a(���bmfb0.���`a,���`a ���bmfb1.���`a)���`a
���`d    ���`bax���aoa.���`hset_ylim���`a(���bmfb0.���`a,���`a ���bmfb1.���`a)���`a
���`a
���`d    ���`bax���aoa.���`exaxis���aoa.���`kset_visible���`a(���bkceFalse���`a)���`a
���`d    ���`bax���aoa.���`eyaxis���aoa.���`kset_visible���`a(���bkceFalse���`a)���`a
���`a
���`a
���akcdef���`a ���bnfsdrop_shadow_patches���`a(���`bax���`a)���`a:���`a
���`d    ���bc1x# Copied from barchart_demo.py���`a
���`d    ���`aN���`a ���aoa=���`a ���bmia5���`a
���`d    ���`imen_means���`a ���aoa=���`a ���`a[���bmib20���`a,���`a ���bmib35���`a,���`a ���bmib30���`a,���`a ���bmib35���`a,���`a ���bmib27���`a]���`a
���`a
���`d    ���`cind���`a ���aoa=���`a ���`bnp���aoa.���`farange���`a(���`aN���`a)���`b  ���bc1x # the x locations for the groups���`a
���`d    ���`ewidth���`a ���aoa=���`a ���bmfd0.35���`b  ���bc1w# the width of the bars���`a
���`a
���`d    ���`frects1���`a ���aoa=���`a ���`bax���aoa.���`cbar���`a(���`cind���`a,���`a ���`imen_means���`a,���`a ���`ewidth���`a,���`a ���`ecolor���aoa=���bs1a'���bs1ar���bs1a'���`a,���`a ���`bec���aoa=���bs2a"���bs2aw���bs2a"���`a,���`a ���`blw���aoa=���bmia2���`a)���`a
���`a
���`d    ���`kwomen_means���`a ���aoa=���`a ���`a[���bmib25���`a,���`a ���bmib32���`a,���`a ���bmib34���`a,���`a ���bmib20���`a,���`a ���bmib25���`a]���`a
���`d    ���`frects2���`a ���aoa=���`a ���`bax���aoa.���`cbar���`a(���`cind���`a ���aoa+���`a ���`ewidth���`a ���aoa+���`a ���bmfc0.1���`a,���`a ���`kwomen_means���`a,���`a ���`ewidth���`a,���`a
���`t                    ���`ecolor���aoa=���bs1a'���bs1ay���bs1a'���`a,���`a ���`bec���aoa=���bs2a"���bs2aw���bs2a"���`a,���`a ���`blw���aoa=���bmia2���`a)���`a
���`a
���`d    ���bc1x-# gauss = GaussianFilter(1.5, offsets=(1, 1))���`a
���`d    ���`egauss���`a ���aoa=���`a ���`pDropShadowFilter���`a(���bmia5���`a,���`a ���`goffsets���aoa=���`a(���bmia1���`a,���`a ���bmia1���`a)���`a)���`a
���`d    ���`fshadow���`a ���aoa=���`a ���`rFilteredArtistList���`a(���`frects1���`a ���aoa+���`a ���`frects2���`a,���`a ���`egauss���`a)���`a
���`d    ���`bax���aoa.���`jadd_artist���`a(���`fshadow���`a)���`a
���`d    ���`fshadow���aoa.���`jset_zorder���`a(���`frects1���`a[���bmia0���`a]���aoa.���`jget_zorder���`a(���`a)���`a ���aoa-���`a ���bmfc0.1���`a)���`a
���`a
���`d    ���`bax���aoa.���`hset_ylim���`a(���bmia0���`a,���`a ���bmib40���`a)���`a
���`a
���`d    ���`bax���aoa.���`exaxis���aoa.���`kset_visible���`a(���bkceFalse���`a)���`a
���`d    ���`bax���aoa.���`eyaxis���aoa.���`kset_visible���`a(���bkceFalse���`a)���`a
���`a
���`a
���akcdef���`a ���bnfplight_filter_pie���`a(���`bax���`a)���`a:���`a
���`d    ���`efracs���`a ���aoa=���`a ���`a[���bmib15���`a,���`a ���bmib30���`a,���`a ���bmib45���`a,���`a ���bmib10���`a]���`a
���`d    ���`gexplode���`a ���aoa=���`a ���`a(���bmia0���`a,���`a ���bmfd0.05���`a,���`a ���bmia0���`a,���`a ���bmia0���`a)���`a
���`d    ���`dpies���`a ���aoa=���`a ���`bax���aoa.���`cpie���`a(���`efracs���`a,���`a ���`gexplode���aoa=���`gexplode���`a)���`a
���`a
���`d    ���`llight_filter���`a ���aoa=���`a ���`kLightFilter���`a(���bmia9���`a)���`a
���`d    ���akcfor���`a ���`ap���`a ���bowbin���`a ���`dpies���`a[���bmia0���`a]���`a:���`a
���`h        ���`ap���aoa.���`nset_agg_filter���`a(���`llight_filter���`a)���`a
���`h        ���`ap���aoa.���`nset_rasterized���`a(���bkcdTrue���`a)���`b  ���bc1x!# to support mixed-mode renderers���`a
���`h        ���`ap���aoa.���`cset���`a(���`bec���aoa=���bs2a"���bs2dnone���bs2a"���`a,���`a
���`n              ���`blw���aoa=���bmia2���`a)���`a
���`a
���`d    ���`egauss���`a ���aoa=���`a ���`pDropShadowFilter���`a(���bmia9���`a,���`a ���`goffsets���aoa=���`a(���bmia3���`a,���`a ���bmia4���`a)���`a,���`a ���`ealpha���aoa=���bmfc0.7���`a)���`a
���`d    ���`fshadow���`a ���aoa=���`a ���`rFilteredArtistList���`a(���`dpies���`a[���bmia0���`a]���`a,���`a ���`egauss���`a)���`a
���`d    ���`bax���aoa.���`jadd_artist���`a(���`fshadow���`a)���`a
���`d    ���`fshadow���aoa.���`jset_zorder���`a(���`dpies���`a[���bmia0���`a]���`a[���bmia0���`a]���aoa.���`jget_zorder���`a(���`a)���`a ���aoa-���`a ���bmfc0.1���`a)���`a
���`a
���`a
���akbif���`a ���bvmh__name__���`a ���aob==���`a ���bs2a"���bs2h__main__���bs2a"���`a:���`a
���`a
���`d    ���`cfix���`a,���`a ���`caxs���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���bmia2���`a,���`a ���bmia2���`a)���`a
���`a
���`d    ���`mfiltered_text���`a(���`caxs���`a[���bmia0���`a,���`a ���bmia0���`a]���`a)���`a
���`d    ���`pdrop_shadow_line���`a(���`caxs���`a[���bmia0���`a,���`a ���bmia1���`a]���`a)���`a
���`d    ���`sdrop_shadow_patches���`a(���`caxs���`a[���bmia1���`a,���`a ���bmia0���`a]���`a)���`a
���`d    ���`plight_filter_pie���`a(���`caxs���`a[���bmia1���`a,���`a ���bmia1���`a]���`a)���`a
���`d    ���`caxs���`a[���bmia1���`a,���`a ���bmia1���`a]���aoa.���`lset_frame_on���`a(���bkcdTrue���`a)���`a
���`a
���`d    ���`cplt���aoa.���`dshow���`a(���`a)���`a
`dNone�