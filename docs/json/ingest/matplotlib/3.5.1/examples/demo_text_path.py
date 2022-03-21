ŸØÇÅŸ¥ÉôaŸ±Çbsdxı"""
======================
Using a text as a Path
======================

`~matplotlib.textpath.TextPath` creates a `.Path` that is the outline of the
characters of a text. The resulting path can be employed e.g. as a clip path
for an image.
"""Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±ÇbknfimportŸ±Ç`a Ÿ±ÇbnnŸ¢ÑjmatplotlibŸ†Ñjmatplotlibe3.5.1fmodulejmatplotlibfmoduleıŸ±Çbnna.Ÿ±ÇbnnfpyplotŸ±Ç`a Ÿ±ÇakbasŸ±Ç`a Ÿ±ÇbnncpltŸ±Ç`a
Ÿ±ÇbkndfromŸ±Ç`a Ÿ±ÇbnnŸ¢ÑjmatplotlibŸ†Ñjmatplotlibe3.5.1fmodulejmatplotlibfmoduleıŸ±Çbnna.Ÿ±ÇbnnecbookŸ±Ç`a Ÿ±ÇbknfimportŸ±Ç`a Ÿ±Ç`oget_sample_dataŸ±Ç`a
Ÿ±ÇbkndfromŸ±Ç`a Ÿ±ÇbnnŸ¢ÑjmatplotlibŸ†Ñjmatplotlibe3.5.1fmodulejmatplotlibfmoduleıŸ±Çbnna.Ÿ±ÇbnneimageŸ±Ç`a Ÿ±ÇbknfimportŸ±Ç`a Ÿ±Ç`iBboxImageŸ±Ç`a
Ÿ±ÇbkndfromŸ±Ç`a Ÿ±ÇbnnŸ¢ÑjmatplotlibŸ†Ñjmatplotlibe3.5.1fmodulejmatplotlibfmoduleıŸ±Çbnna.Ÿ±ÇbnnioffsetboxŸ±Ç`a Ÿ±ÇbknfimportŸ±Ç`a Ÿ±Ç`a(Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`nAnnotationBboxŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`qAnchoredOffsetboxŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`oAuxTransformBoxŸ±Ç`a)Ÿ±Ç`a
Ÿ±ÇbkndfromŸ±Ç`a Ÿ±ÇbnnŸ¢ÑjmatplotlibŸ†Ñjmatplotlibe3.5.1fmodulejmatplotlibfmoduleıŸ±Çbnna.Ÿ±ÇbnngpatchesŸ±Ç`a Ÿ±ÇbknfimportŸ±Ç`a Ÿ±Ç`iPathPatchŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`fShadowŸ±Ç`a
Ÿ±ÇbkndfromŸ±Ç`a Ÿ±ÇbnnŸ¢ÑjmatplotlibŸ†Ñjmatplotlibe3.5.1fmodulejmatplotlibfmoduleıŸ±Çbnna.Ÿ±ÇbnndtextŸ±Ç`a Ÿ±ÇbknfimportŸ±Ç`a Ÿ±Ç`hTextPathŸ±Ç`a
Ÿ±ÇbkndfromŸ±Ç`a Ÿ±ÇbnnŸ¢ÑjmatplotlibŸ†Ñjmatplotlibe3.5.1fmodulejmatplotlibfmoduleıŸ±Çbnna.Ÿ±ÇbnnjtransformsŸ±Ç`a Ÿ±ÇbknfimportŸ±Ç`a Ÿ±Ç`qIdentityTransformŸ±Ç`a
Ÿ±ÇbknfimportŸ±Ç`a Ÿ±ÇbnnŸ¢ÑenumpyŸ†Ñenumpyf1.22.3fmoduleenumpyfmoduleıŸ±Ç`a Ÿ±ÇakbasŸ±Ç`a Ÿ±ÇbnnbnpŸ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±ÇakeclassŸ±Ç`a Ÿ±ÇbncuPathClippedImagePatchŸ±Ç`a(Ÿ±Ç`iPathPatchŸ±Ç`a)Ÿ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Çbsdx…"""
    The given image is used to draw the face of the patch. Internally,
    it uses BboxImage whose clippath set to the path of the patch.

    FIXME : The result is currently dpi dependent.
    """Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±ÇakcdefŸ±Ç`a Ÿ±Çbfmh__init__Ÿ±Ç`a(Ÿ±ÇbbpdselfŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dpathŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`jbbox_imageŸ±Ç`a,Ÿ±Ç`a Ÿ±Çaoa*Ÿ±Çaoa*Ÿ±Ç`fkwargsŸ±Ç`a)Ÿ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±ÇbnbesuperŸ±Ç`a(Ÿ±Ç`a)Ÿ±Çaoa.Ÿ±Çbfmh__init__Ÿ±Ç`a(Ÿ±Ç`dpathŸ±Ç`a,Ÿ±Ç`a Ÿ±Çaoa*Ÿ±Çaoa*Ÿ±Ç`fkwargsŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±ÇbbpdselfŸ±Çaoa.Ÿ±Ç`jbbox_imageŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`iBboxImageŸ±Ç`a(Ÿ±Ç`a
Ÿ±Ç`l            Ÿ±ÇbbpdselfŸ±Çaoa.Ÿ±Ç`qget_window_extentŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dnormŸ±Çaoa=Ÿ±ÇbkcdNoneŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`foriginŸ±Çaoa=Ÿ±ÇbkcdNoneŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±ÇbbpdselfŸ±Çaoa.Ÿ±Ç`jbbox_imageŸ±Çaoa.Ÿ±Ç`hset_dataŸ±Ç`a(Ÿ±Ç`jbbox_imageŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±ÇakcdefŸ±Ç`a Ÿ±Çbnfmset_facecolorŸ±Ç`a(Ÿ±ÇbbpdselfŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ecolorŸ±Ç`a)Ÿ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±Çbsdx"""Simply ignore facecolor."""Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±ÇbnbesuperŸ±Ç`a(Ÿ±Ç`a)Ÿ±Çaoa.Ÿ±Ç`mset_facecolorŸ±Ç`a(Ÿ±Çbs2a"Ÿ±Çbs2dnoneŸ±Çbs2a"Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±ÇakcdefŸ±Ç`a Ÿ±ÇbnfddrawŸ±Ç`a(Ÿ±ÇbbpdselfŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`hrendererŸ±Çaoa=Ÿ±ÇbkcdNoneŸ±Ç`a)Ÿ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±Çbc1x=# the clip path must be updated every draw. any solution? -JJŸ±Ç`a
Ÿ±Ç`h        Ÿ±ÇbbpdselfŸ±Çaoa.Ÿ±Ç`jbbox_imageŸ±Çaoa.Ÿ±Ç`mset_clip_pathŸ±Ç`a(Ÿ±ÇbbpdselfŸ±Çaoa.Ÿ±Ç`e_pathŸ±Ç`a,Ÿ±Ç`a Ÿ±ÇbbpdselfŸ±Çaoa.Ÿ±Ç`mget_transformŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±ÇbbpdselfŸ±Çaoa.Ÿ±Ç`jbbox_imageŸ±Çaoa.Ÿ±Ç`ddrawŸ±Ç`a(Ÿ±Ç`hrendererŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±ÇbnbesuperŸ±Ç`a(Ÿ±Ç`a)Ÿ±Çaoa.Ÿ±Ç`ddrawŸ±Ç`a(Ÿ±Ç`hrendererŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±ÇakbifŸ±Ç`a Ÿ±Çbvmh__name__Ÿ±Ç`a Ÿ±Çaob==Ÿ±Ç`a Ÿ±Çbs2a"Ÿ±Çbs2h__main__Ÿ±Çbs2a"Ÿ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`fusetexŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`hrcParamsŸ±Ç`a[Ÿ±Çbs2a"Ÿ±Çbs2ktext.usetexŸ±Çbs2a"Ÿ±Ç`a]Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`cfigŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`a(Ÿ±Ç`cax1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`cax2Ÿ±Ç`a)Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`hsubplotsŸ±Ç`a(Ÿ±Çbmia2Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Çbc1k# EXAMPLE 1Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`carrŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`fimreadŸ±Ç`a(Ÿ±Ç`oget_sample_dataŸ±Ç`a(Ÿ±Çbs2a"Ÿ±Çbs2pgrace_hopper.jpgŸ±Çbs2a"Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`itext_pathŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`hTextPathŸ±Ç`a(Ÿ±Ç`a(Ÿ±Çbmia0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia0Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs2a"Ÿ±Çbs2b!?Ÿ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dsizeŸ±Çaoa=Ÿ±Çbmic150Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`apŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`uPathClippedImagePatchŸ±Ç`a(Ÿ±Ç`itext_pathŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`carrŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`becŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2akŸ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`x                              Ÿ±Ç`itransformŸ±Çaoa=Ÿ±Ç`qIdentityTransformŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Çbc1q# make offset boxŸ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`ioffsetboxŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`oAuxTransformBoxŸ±Ç`a(Ÿ±Ç`qIdentityTransformŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`ioffsetboxŸ±Çaoa.Ÿ±Ç`jadd_artistŸ±Ç`a(Ÿ±Ç`apŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Çbc1x# make anchored offset boxŸ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`baoŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`qAnchoredOffsetboxŸ±Ç`a(Ÿ±Ç`clocŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1jupper leftŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`echildŸ±Çaoa=Ÿ±Ç`ioffsetboxŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`gframeonŸ±Çaoa=Ÿ±ÇbkcdTrueŸ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`x                           Ÿ±Ç`iborderpadŸ±Çaoa=Ÿ±Çbmfc0.2Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`cax1Ÿ±Çaoa.Ÿ±Ç`jadd_artistŸ±Ç`a(Ÿ±Ç`baoŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Çbc1n# another textŸ±Ç`a
Ÿ±Ç`d    Ÿ±ÇbkndfromŸ±Ç`a Ÿ±ÇbnnŸ¢ÑjmatplotlibŸ†Ñjmatplotlibe3.5.1fmodulejmatplotlibfmoduleıŸ±Çbnna.Ÿ±ÇbnngpatchesŸ±Ç`a Ÿ±ÇbknfimportŸ±Ç`a Ÿ±Ç`iPathPatchŸ±Ç`a
Ÿ±Ç`d    Ÿ±ÇakbifŸ±Ç`a Ÿ±Ç`fusetexŸ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±Ç`arŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±ÇbsaarŸ±Çbs2a"Ÿ±Çbs2a\Ÿ±Çbs2dmboxŸ±Çbs2a{Ÿ±Çbs2xtextpath supports mathtext Ÿ±Çbs2a\Ÿ±Çbs2b& Ÿ±Çbs2a\Ÿ±Çbs2dTeX}Ÿ±Çbs2a"Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±ÇakdelseŸ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±Ç`arŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±ÇbsaarŸ±Çbs2a"Ÿ±Çbs2x textpath supports mathtext & TeXŸ±Çbs2a"Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`itext_pathŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`hTextPathŸ±Ç`a(Ÿ±Ç`a(Ÿ±Çbmia0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia0Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`arŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dsizeŸ±Çaoa=Ÿ±Çbmib20Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`fusetexŸ±Çaoa=Ÿ±Ç`fusetexŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`bp1Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`iPathPatchŸ±Ç`a(Ÿ±Ç`itext_pathŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`becŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2awŸ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`blwŸ±Çaoa=Ÿ±Çbmia3Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`bfcŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2awŸ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ealphaŸ±Çaoa=Ÿ±Çbmfc0.9Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`s                   Ÿ±Ç`itransformŸ±Çaoa=Ÿ±Ç`qIdentityTransformŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`bp2Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`iPathPatchŸ±Ç`a(Ÿ±Ç`itext_pathŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`becŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2dnoneŸ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`bfcŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2akŸ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`s                   Ÿ±Ç`itransformŸ±Çaoa=Ÿ±Ç`qIdentityTransformŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`joffsetbox2Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`oAuxTransformBoxŸ±Ç`a(Ÿ±Ç`qIdentityTransformŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`joffsetbox2Ÿ±Çaoa.Ÿ±Ç`jadd_artistŸ±Ç`a(Ÿ±Ç`bp1Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`joffsetbox2Ÿ±Çaoa.Ÿ±Ç`jadd_artistŸ±Ç`a(Ÿ±Ç`bp2Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`babŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`nAnnotationBboxŸ±Ç`a(Ÿ±Ç`joffsetbox2Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`a(Ÿ±Çbmfd0.95Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd0.05Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`x                        Ÿ±Ç`hxycoordsŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1maxes fractionŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`x                        Ÿ±Ç`iboxcoordsŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2moffset pointsŸ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`x                        Ÿ±Ç`mbox_alignmentŸ±Çaoa=Ÿ±Ç`a(Ÿ±Çbmfb1.Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfb0.Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`x                        Ÿ±Ç`gframeonŸ±Çaoa=Ÿ±ÇbkceFalseŸ±Ç`a
Ÿ±Ç`x                        Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`cax1Ÿ±Çaoa.Ÿ±Ç`jadd_artistŸ±Ç`a(Ÿ±Ç`babŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`cax1Ÿ±Çaoa.Ÿ±Ç`fimshowŸ±Ç`a(Ÿ±Ç`a[Ÿ±Ç`a[Ÿ±Çbmia0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia2Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`a[Ÿ±Çbmia1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia2Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia3Ÿ±Ç`a]Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dcmapŸ±Çaoa=Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`bcmŸ±Çaoa.Ÿ±Ç`kgist_gray_rŸ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`o               Ÿ±Ç`minterpolationŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2hbilinearŸ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`faspectŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2dautoŸ±Çbs2a"Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Çbc1k# EXAMPLE 2Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`carrŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`farangeŸ±Ç`a(Ÿ±Çbmic256Ÿ±Ç`a)Ÿ±Çaoa.Ÿ±Ç`greshapeŸ±Ç`a(Ÿ±Çbmia1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmic256Ÿ±Ç`a)Ÿ±Ç`a Ÿ±Çaoa/Ÿ±Ç`a Ÿ±Çbmic256Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±ÇakbifŸ±Ç`a Ÿ±Ç`fusetexŸ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±Ç`asŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`a(Ÿ±ÇbsaarŸ±Çbs2a"Ÿ±Çbs2a$Ÿ±Çbs2a\Ÿ±Çbs2ldisplaystyleŸ±Çbs2a\Ÿ±Çbs2eleft[Ÿ±Çbs2a\Ÿ±Çbs2dsum_Ÿ±Çbs2a{Ÿ±Çbs2en=1}^Ÿ±Çbs2a\Ÿ±Çbs2einftyŸ±Çbs2a"Ÿ±Ç`a
Ÿ±Ç`m             Ÿ±ÇbsaarŸ±Çbs2a"Ÿ±Çbs2a\Ÿ±Çbs2dfracŸ±Çbs2a{Ÿ±Çbs2c-e^Ÿ±Çbs2a{Ÿ±Çbs2aiŸ±Çbs2a\Ÿ±Çbs2dpi}}Ÿ±Çbs2a{Ÿ±Çbs2d2^n}Ÿ±Çbs2a\Ÿ±Çbs2hright]$!Ÿ±Çbs2a"Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±ÇakdelseŸ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±Ç`asŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±ÇbsaarŸ±Çbs2a"Ÿ±Çbs2a$Ÿ±Çbs2a\Ÿ±Çbs2eleft[Ÿ±Çbs2a\Ÿ±Çbs2dsum_Ÿ±Çbs2a{Ÿ±Çbs2en=1}^Ÿ±Çbs2a\Ÿ±Çbs2einftyŸ±Çbs2a\Ÿ±Çbs2dfracŸ±Çbs2a{Ÿ±Çbs2c-e^Ÿ±Çbs2a{Ÿ±Çbs2aiŸ±Çbs2a\Ÿ±Çbs2dpi}}Ÿ±Çbs2a{Ÿ±Çbs2d2^n}Ÿ±Çbs2a\Ÿ±Çbs2hright]$!Ÿ±Çbs2a"Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`itext_pathŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`hTextPathŸ±Ç`a(Ÿ±Ç`a(Ÿ±Çbmia0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia0Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`asŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dsizeŸ±Çaoa=Ÿ±Çbmib40Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`fusetexŸ±Çaoa=Ÿ±Ç`fusetexŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`jtext_patchŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`uPathClippedImagePatchŸ±Ç`a(Ÿ±Ç`itext_pathŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`carrŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`becŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2dnoneŸ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`x'                                       Ÿ±Ç`itransformŸ±Çaoa=Ÿ±Ç`qIdentityTransformŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`gshadow1Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`fShadowŸ±Ç`a(Ÿ±Ç`jtext_patchŸ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çaoa-Ÿ±Çbmia1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`bfcŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2dnoneŸ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`becŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2c0.6Ÿ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`blwŸ±Çaoa=Ÿ±Çbmia3Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`gshadow2Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`fShadowŸ±Ç`a(Ÿ±Ç`jtext_patchŸ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çaoa-Ÿ±Çbmia1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`bfcŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2c0.3Ÿ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`becŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2dnoneŸ±Çbs2a"Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Çbc1q# make offset boxŸ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`ioffsetboxŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`oAuxTransformBoxŸ±Ç`a(Ÿ±Ç`qIdentityTransformŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`ioffsetboxŸ±Çaoa.Ÿ±Ç`jadd_artistŸ±Ç`a(Ÿ±Ç`gshadow1Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`ioffsetboxŸ±Çaoa.Ÿ±Ç`jadd_artistŸ±Ç`a(Ÿ±Ç`gshadow2Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`ioffsetboxŸ±Çaoa.Ÿ±Ç`jadd_artistŸ±Ç`a(Ÿ±Ç`jtext_patchŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Çbc1x4# place the anchored offset box using AnnotationBboxŸ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`babŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`nAnnotationBboxŸ±Ç`a(Ÿ±Ç`ioffsetboxŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`a(Ÿ±Çbmfc0.5Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfc0.5Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`x                        Ÿ±Ç`hxycoordsŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1ddataŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`x                        Ÿ±Ç`iboxcoordsŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2moffset pointsŸ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`x                        Ÿ±Ç`mbox_alignmentŸ±Çaoa=Ÿ±Ç`a(Ÿ±Çbmfc0.5Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfc0.5Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`x                        Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`cax2Ÿ±Çaoa.Ÿ±Ç`jadd_artistŸ±Ç`a(Ÿ±Ç`babŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`cax2Ÿ±Çaoa.Ÿ±Ç`hset_xlimŸ±Ç`a(Ÿ±Çbmia0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia1Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`cax2Ÿ±Çaoa.Ÿ±Ç`hset_ylimŸ±Ç`a(Ÿ±Çbmia0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia1Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`dshowŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
`dNoneˆ