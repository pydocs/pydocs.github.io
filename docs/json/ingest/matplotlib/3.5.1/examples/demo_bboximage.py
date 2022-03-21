��������&���bsdy"""
==============
BboxImage Demo
==============

A `~matplotlib.image.BboxImage` can be used to position an image according to
a bounding box. This demo shows how to show an image inside a `.text.Text`'s
bounding box as well as how to manually create a bounding box for the image.
"""���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���bkndfrom���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnneimage���`a ���bknfimport���`a ���`iBboxImage���`a
���bkndfrom���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnjtransforms���`a ���bknfimport���`a ���`dBbox���`a,���`a ���`oTransformedBbox���`a
���`a
���`a
���`cfig���`a,���`a ���`a(���`cax1���`a,���`a ���`cax2���`a)���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`encols���aoa=���bmia2���`a)���`a
���`a
���bc1x# ----------------------------���`a
���bc1x# Create a BboxImage with Text���`a
���bc1x# ----------------------------���`a
���`ctxt���`a ���aoa=���`a ���`cax1���aoa.���`dtext���`a(���bmfc0.5���`a,���`a ���bmfc0.5���`a,���`a ���bs2a"���bs2dtest���bs2a"���`a,���`a ���`dsize���aoa=���bmib30���`a,���`a ���`bha���aoa=���bs2a"���bs2fcenter���bs2a"���`a,���`a ���`ecolor���aoa=���bs2a"���bs2aw���bs2a"���`a)���`a
���`fkwargs���`a ���aoa=���`a ���bnbddict���`a(���`a)���`a
���`a
���`jbbox_image���`a ���aoa=���`a ���`iBboxImage���`a(���`ctxt���aoa.���`qget_window_extent���`a,���`a
���`w                       ���`dnorm���aoa=���bkcdNone���`a,���`a
���`w                       ���`forigin���aoa=���bkcdNone���`a,���`a
���`w                       ���`gclip_on���aoa=���bkceFalse���`a,���`a
���`w                       ���aoa*���aoa*���`fkwargs���`a
���`w                       ���`a)���`a
���`aa���`a ���aoa=���`a ���`bnp���aoa.���`farange���`a(���bmic256���`a)���aoa.���`greshape���`a(���bmia1���`a,���`a ���bmic256���`a)���aoa/���bmfd256.���`a
���`jbbox_image���aoa.���`hset_data���`a(���`aa���`a)���`a
���`cax1���aoa.���`jadd_artist���`a(���`jbbox_image���`a)���`a
���`a
���bc1x&# ------------------------------------���`a
���bc1x&# Create a BboxImage for each colormap���`a
���bc1x&# ------------------------------------���`a
���`aa���`a ���aoa=���`a ���`bnp���aoa.���`hlinspace���`a(���bmia0���`a,���`a ���bmia1���`a,���`a ���bmic256���`a)���aoa.���`greshape���`a(���bmia1���`a,���`a ���aoa-���bmia1���`a)���`a
���`aa���`a ���aoa=���`a ���`bnp���aoa.���`fvstack���`a(���`a(���`aa���`a,���`a ���`aa���`a)���`a)���`a
���`a
���bc1x1# List of all colormaps; skip reversed colormaps.���`a
���`jcmap_names���`a ���aoa=���`a ���bnbfsorted���`a(���`am���`a ���akcfor���`a ���`am���`a ���bowbin���`a ���`cplt���aoa.���`icolormaps���`a ���akbif���`a ���bowcnot���`a ���`am���aoa.���`hendswith���`a(���bs2a"���bs2b_r���bs2a"���`a)���`a)���`a
���`a
���`dncol���`a ���aoa=���`a ���bmia2���`a
���`dnrow���`a ���aoa=���`a ���bnbclen���`a(���`jcmap_names���`a)���`a ���aoa/���aoa/���`a ���`dncol���`a ���aoa+���`a ���bmia1���`a
���`a
���`mxpad_fraction���`a ���aoa=���`a ���bmfc0.3���`a
���`bdx���`a ���aoa=���`a ���bmia1���`a ���aoa/���`a ���`a(���`dncol���`a ���aoa+���`a ���`mxpad_fraction���`a ���aoa*���`a ���`a(���`dncol���`a ���aoa-���`a ���bmia1���`a)���`a)���`a
���`a
���`mypad_fraction���`a ���aoa=���`a ���bmfc0.3���`a
���`bdy���`a ���aoa=���`a ���bmia1���`a ���aoa/���`a ���`a(���`dnrow���`a ���aoa+���`a ���`mypad_fraction���`a ���aoa*���`a ���`a(���`dnrow���`a ���aoa-���`a ���bmia1���`a)���`a)���`a
���`a
���akcfor���`a ���`ai���`a,���`a ���`icmap_name���`a ���bowbin���`a ���bnbienumerate���`a(���`jcmap_names���`a)���`a:���`a
���`d    ���`bix���`a,���`a ���`biy���`a ���aoa=���`a ���bnbfdivmod���`a(���`ai���`a,���`a ���`dnrow���`a)���`a
���`a
���`d    ���`ebbox0���`a ���aoa=���`a ���`dBbox���aoa.���`kfrom_bounds���`a(���`bix���aoa*���`bdx���aoa*���`a(���bmia1���`a ���aoa+���`a ���`mxpad_fraction���`a)���`a,���`a
���`x                             ���bmfb1.���`a ���aoa-���`a ���`biy���aoa*���`bdy���aoa*���`a(���bmia1���`a ���aoa+���`a ���`mypad_fraction���`a)���`a ���aoa-���`a ���`bdy���`a,���`a
���`x                             ���`bdx���`a,���`a ���`bdy���`a)���`a
���`d    ���`dbbox���`a ���aoa=���`a ���`oTransformedBbox���`a(���`ebbox0���`a,���`a ���`cax2���aoa.���`itransAxes���`a)���`a
���`a
���`d    ���`jbbox_image���`a ���aoa=���`a ���`iBboxImage���`a(���`dbbox���`a,���`a
���`x                           ���`dcmap���aoa=���`icmap_name���`a,���`a
���`x                           ���`dnorm���aoa=���bkcdNone���`a,���`a
���`x                           ���`forigin���aoa=���bkcdNone���`a,���`a
���`x                           ���aoa*���aoa*���`fkwargs���`a
���`x                           ���`a)���`a
���`a
���`d    ���`jbbox_image���aoa.���`hset_data���`a(���`aa���`a)���`a
���`d    ���`cax2���aoa.���`jadd_artist���`a(���`jbbox_image���`a)���`a
���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
���`a
���bc1xM#############################################################################���`a
���bc1a#���`a
���bc1x# .. admonition:: References���`a
���bc1a#���`a
���bc1xN#    The use of the following functions, methods, classes and modules is shown���`a
���bc1u#    in this example:���`a
���bc1a#���`a
���bc1x##    - `matplotlib.image.BboxImage`���`a
���bc1x##    - `matplotlib.transforms.Bbox`���`a
���bc1x.#    - `matplotlib.transforms.TransformedBbox`���`a
���bc1x#    - `matplotlib.text.Text`���`a
`dNone�