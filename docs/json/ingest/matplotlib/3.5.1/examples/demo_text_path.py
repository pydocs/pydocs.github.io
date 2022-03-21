��������a���bsdx�"""
======================
Using a text as a Path
======================

`~matplotlib.textpath.TextPath` creates a `.Path` that is the outline of the
characters of a text. The resulting path can be employed e.g. as a clip path
for an image.
"""���`a
���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���bkndfrom���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnecbook���`a ���bknfimport���`a ���`oget_sample_data���`a
���bkndfrom���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnneimage���`a ���bknfimport���`a ���`iBboxImage���`a
���bkndfrom���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnioffsetbox���`a ���bknfimport���`a ���`a(���`a
���`d    ���`nAnnotationBbox���`a,���`a ���`qAnchoredOffsetbox���`a,���`a ���`oAuxTransformBox���`a)���`a
���bkndfrom���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnngpatches���`a ���bknfimport���`a ���`iPathPatch���`a,���`a ���`fShadow���`a
���bkndfrom���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnndtext���`a ���bknfimport���`a ���`hTextPath���`a
���bkndfrom���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnjtransforms���`a ���bknfimport���`a ���`qIdentityTransform���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���`a
���`a
���akeclass���`a ���bncuPathClippedImagePatch���`a(���`iPathPatch���`a)���`a:���`a
���`d    ���bsdx�"""
    The given image is used to draw the face of the patch. Internally,
    it uses BboxImage whose clippath set to the path of the patch.

    FIXME : The result is currently dpi dependent.
    """���`a
���`a
���`d    ���akcdef���`a ���bfmh__init__���`a(���bbpdself���`a,���`a ���`dpath���`a,���`a ���`jbbox_image���`a,���`a ���aoa*���aoa*���`fkwargs���`a)���`a:���`a
���`h        ���bnbesuper���`a(���`a)���aoa.���bfmh__init__���`a(���`dpath���`a,���`a ���aoa*���aoa*���`fkwargs���`a)���`a
���`h        ���bbpdself���aoa.���`jbbox_image���`a ���aoa=���`a ���`iBboxImage���`a(���`a
���`l            ���bbpdself���aoa.���`qget_window_extent���`a,���`a ���`dnorm���aoa=���bkcdNone���`a,���`a ���`forigin���aoa=���bkcdNone���`a)���`a
���`h        ���bbpdself���aoa.���`jbbox_image���aoa.���`hset_data���`a(���`jbbox_image���`a)���`a
���`a
���`d    ���akcdef���`a ���bnfmset_facecolor���`a(���bbpdself���`a,���`a ���`ecolor���`a)���`a:���`a
���`h        ���bsdx"""Simply ignore facecolor."""���`a
���`h        ���bnbesuper���`a(���`a)���aoa.���`mset_facecolor���`a(���bs2a"���bs2dnone���bs2a"���`a)���`a
���`a
���`d    ���akcdef���`a ���bnfddraw���`a(���bbpdself���`a,���`a ���`hrenderer���aoa=���bkcdNone���`a)���`a:���`a
���`h        ���bc1x=# the clip path must be updated every draw. any solution? -JJ���`a
���`h        ���bbpdself���aoa.���`jbbox_image���aoa.���`mset_clip_path���`a(���bbpdself���aoa.���`e_path���`a,���`a ���bbpdself���aoa.���`mget_transform���`a(���`a)���`a)���`a
���`h        ���bbpdself���aoa.���`jbbox_image���aoa.���`ddraw���`a(���`hrenderer���`a)���`a
���`h        ���bnbesuper���`a(���`a)���aoa.���`ddraw���`a(���`hrenderer���`a)���`a
���`a
���`a
���akbif���`a ���bvmh__name__���`a ���aob==���`a ���bs2a"���bs2h__main__���bs2a"���`a:���`a
���`a
���`d    ���`fusetex���`a ���aoa=���`a ���`cplt���aoa.���`hrcParams���`a[���bs2a"���bs2ktext.usetex���bs2a"���`a]���`a
���`a
���`d    ���`cfig���`a,���`a ���`a(���`cax1���`a,���`a ���`cax2���`a)���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���bmia2���`a)���`a
���`a
���`d    ���bc1k# EXAMPLE 1���`a
���`a
���`d    ���`carr���`a ���aoa=���`a ���`cplt���aoa.���`fimread���`a(���`oget_sample_data���`a(���bs2a"���bs2pgrace_hopper.jpg���bs2a"���`a)���`a)���`a
���`a
���`d    ���`itext_path���`a ���aoa=���`a ���`hTextPath���`a(���`a(���bmia0���`a,���`a ���bmia0���`a)���`a,���`a ���bs2a"���bs2b!?���bs2a"���`a,���`a ���`dsize���aoa=���bmic150���`a)���`a
���`d    ���`ap���`a ���aoa=���`a ���`uPathClippedImagePatch���`a(���`itext_path���`a,���`a ���`carr���`a,���`a ���`bec���aoa=���bs2a"���bs2ak���bs2a"���`a,���`a
���`x                              ���`itransform���aoa=���`qIdentityTransform���`a(���`a)���`a)���`a
���`a
���`d    ���bc1q# make offset box���`a
���`d    ���`ioffsetbox���`a ���aoa=���`a ���`oAuxTransformBox���`a(���`qIdentityTransform���`a(���`a)���`a)���`a
���`d    ���`ioffsetbox���aoa.���`jadd_artist���`a(���`ap���`a)���`a
���`a
���`d    ���bc1x# make anchored offset box���`a
���`d    ���`bao���`a ���aoa=���`a ���`qAnchoredOffsetbox���`a(���`cloc���aoa=���bs1a'���bs1jupper left���bs1a'���`a,���`a ���`echild���aoa=���`ioffsetbox���`a,���`a ���`gframeon���aoa=���bkcdTrue���`a,���`a
���`x                           ���`iborderpad���aoa=���bmfc0.2���`a)���`a
���`d    ���`cax1���aoa.���`jadd_artist���`a(���`bao���`a)���`a
���`a
���`d    ���bc1n# another text���`a
���`d    ���bkndfrom���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnngpatches���`a ���bknfimport���`a ���`iPathPatch���`a
���`d    ���akbif���`a ���`fusetex���`a:���`a
���`h        ���`ar���`a ���aoa=���`a ���bsaar���bs2a"���bs2a\���bs2dmbox���bs2a{���bs2xtextpath supports mathtext ���bs2a\���bs2b& ���bs2a\���bs2dTeX}���bs2a"���`a
���`d    ���akdelse���`a:���`a
���`h        ���`ar���`a ���aoa=���`a ���bsaar���bs2a"���bs2x textpath supports mathtext & TeX���bs2a"���`a
���`a
���`d    ���`itext_path���`a ���aoa=���`a ���`hTextPath���`a(���`a(���bmia0���`a,���`a ���bmia0���`a)���`a,���`a ���`ar���`a,���`a ���`dsize���aoa=���bmib20���`a,���`a ���`fusetex���aoa=���`fusetex���`a)���`a
���`a
���`d    ���`bp1���`a ���aoa=���`a ���`iPathPatch���`a(���`itext_path���`a,���`a ���`bec���aoa=���bs2a"���bs2aw���bs2a"���`a,���`a ���`blw���aoa=���bmia3���`a,���`a ���`bfc���aoa=���bs2a"���bs2aw���bs2a"���`a,���`a ���`ealpha���aoa=���bmfc0.9���`a,���`a
���`s                   ���`itransform���aoa=���`qIdentityTransform���`a(���`a)���`a)���`a
���`d    ���`bp2���`a ���aoa=���`a ���`iPathPatch���`a(���`itext_path���`a,���`a ���`bec���aoa=���bs2a"���bs2dnone���bs2a"���`a,���`a ���`bfc���aoa=���bs2a"���bs2ak���bs2a"���`a,���`a
���`s                   ���`itransform���aoa=���`qIdentityTransform���`a(���`a)���`a)���`a
���`a
���`d    ���`joffsetbox2���`a ���aoa=���`a ���`oAuxTransformBox���`a(���`qIdentityTransform���`a(���`a)���`a)���`a
���`d    ���`joffsetbox2���aoa.���`jadd_artist���`a(���`bp1���`a)���`a
���`d    ���`joffsetbox2���aoa.���`jadd_artist���`a(���`bp2���`a)���`a
���`a
���`d    ���`bab���`a ���aoa=���`a ���`nAnnotationBbox���`a(���`joffsetbox2���`a,���`a ���`a(���bmfd0.95���`a,���`a ���bmfd0.05���`a)���`a,���`a
���`x                        ���`hxycoords���aoa=���bs1a'���bs1maxes fraction���bs1a'���`a,���`a
���`x                        ���`iboxcoords���aoa=���bs2a"���bs2moffset points���bs2a"���`a,���`a
���`x                        ���`mbox_alignment���aoa=���`a(���bmfb1.���`a,���`a ���bmfb0.���`a)���`a,���`a
���`x                        ���`gframeon���aoa=���bkceFalse���`a
���`x                        ���`a)���`a
���`d    ���`cax1���aoa.���`jadd_artist���`a(���`bab���`a)���`a
���`a
���`d    ���`cax1���aoa.���`fimshow���`a(���`a[���`a[���bmia0���`a,���`a ���bmia1���`a,���`a ���bmia2���`a]���`a,���`a ���`a[���bmia1���`a,���`a ���bmia2���`a,���`a ���bmia3���`a]���`a]���`a,���`a ���`dcmap���aoa=���`cplt���aoa.���`bcm���aoa.���`kgist_gray_r���`a,���`a
���`o               ���`minterpolation���aoa=���bs2a"���bs2hbilinear���bs2a"���`a,���`a ���`faspect���aoa=���bs2a"���bs2dauto���bs2a"���`a)���`a
���`a
���`d    ���bc1k# EXAMPLE 2���`a
���`a
���`d    ���`carr���`a ���aoa=���`a ���`bnp���aoa.���`farange���`a(���bmic256���`a)���aoa.���`greshape���`a(���bmia1���`a,���`a ���bmic256���`a)���`a ���aoa/���`a ���bmic256���`a
���`a
���`d    ���akbif���`a ���`fusetex���`a:���`a
���`h        ���`as���`a ���aoa=���`a ���`a(���bsaar���bs2a"���bs2a$���bs2a\���bs2ldisplaystyle���bs2a\���bs2eleft[���bs2a\���bs2dsum_���bs2a{���bs2en=1}^���bs2a\���bs2einfty���bs2a"���`a
���`m             ���bsaar���bs2a"���bs2a\���bs2dfrac���bs2a{���bs2c-e^���bs2a{���bs2ai���bs2a\���bs2dpi}}���bs2a{���bs2d2^n}���bs2a\���bs2hright]$!���bs2a"���`a)���`a
���`d    ���akdelse���`a:���`a
���`h        ���`as���`a ���aoa=���`a ���bsaar���bs2a"���bs2a$���bs2a\���bs2eleft[���bs2a\���bs2dsum_���bs2a{���bs2en=1}^���bs2a\���bs2einfty���bs2a\���bs2dfrac���bs2a{���bs2c-e^���bs2a{���bs2ai���bs2a\���bs2dpi}}���bs2a{���bs2d2^n}���bs2a\���bs2hright]$!���bs2a"���`a
���`d    ���`itext_path���`a ���aoa=���`a ���`hTextPath���`a(���`a(���bmia0���`a,���`a ���bmia0���`a)���`a,���`a ���`as���`a,���`a ���`dsize���aoa=���bmib40���`a,���`a ���`fusetex���aoa=���`fusetex���`a)���`a
���`d    ���`jtext_patch���`a ���aoa=���`a ���`uPathClippedImagePatch���`a(���`itext_path���`a,���`a ���`carr���`a,���`a ���`bec���aoa=���bs2a"���bs2dnone���bs2a"���`a,���`a
���`x'                                       ���`itransform���aoa=���`qIdentityTransform���`a(���`a)���`a)���`a
���`a
���`d    ���`gshadow1���`a ���aoa=���`a ���`fShadow���`a(���`jtext_patch���`a,���`a ���bmia1���`a,���`a ���aoa-���bmia1���`a,���`a ���`bfc���aoa=���bs2a"���bs2dnone���bs2a"���`a,���`a ���`bec���aoa=���bs2a"���bs2c0.6���bs2a"���`a,���`a ���`blw���aoa=���bmia3���`a)���`a
���`d    ���`gshadow2���`a ���aoa=���`a ���`fShadow���`a(���`jtext_patch���`a,���`a ���bmia1���`a,���`a ���aoa-���bmia1���`a,���`a ���`bfc���aoa=���bs2a"���bs2c0.3���bs2a"���`a,���`a ���`bec���aoa=���bs2a"���bs2dnone���bs2a"���`a)���`a
���`a
���`d    ���bc1q# make offset box���`a
���`d    ���`ioffsetbox���`a ���aoa=���`a ���`oAuxTransformBox���`a(���`qIdentityTransform���`a(���`a)���`a)���`a
���`d    ���`ioffsetbox���aoa.���`jadd_artist���`a(���`gshadow1���`a)���`a
���`d    ���`ioffsetbox���aoa.���`jadd_artist���`a(���`gshadow2���`a)���`a
���`d    ���`ioffsetbox���aoa.���`jadd_artist���`a(���`jtext_patch���`a)���`a
���`a
���`d    ���bc1x4# place the anchored offset box using AnnotationBbox���`a
���`d    ���`bab���`a ���aoa=���`a ���`nAnnotationBbox���`a(���`ioffsetbox���`a,���`a ���`a(���bmfc0.5���`a,���`a ���bmfc0.5���`a)���`a,���`a
���`x                        ���`hxycoords���aoa=���bs1a'���bs1ddata���bs1a'���`a,���`a
���`x                        ���`iboxcoords���aoa=���bs2a"���bs2moffset points���bs2a"���`a,���`a
���`x                        ���`mbox_alignment���aoa=���`a(���bmfc0.5���`a,���`a ���bmfc0.5���`a)���`a,���`a
���`x                        ���`a)���`a
���`a
���`d    ���`cax2���aoa.���`jadd_artist���`a(���`bab���`a)���`a
���`a
���`d    ���`cax2���aoa.���`hset_xlim���`a(���bmia0���`a,���`a ���bmia1���`a)���`a
���`d    ���`cax2���aoa.���`hset_ylim���`a(���bmia0���`a,���`a ���bmia1���`a)���`a
���`a
���`d    ���`cplt���aoa.���`dshow���`a(���`a)���`a
`dNone�