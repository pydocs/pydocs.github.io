��������%���bsdy�"""
============================
Affine transform of an image
============================


Prepending an affine transformation (`~.transforms.Affine2D`) to the :ref:`data
transform <data-coords>` of an image allows to manipulate the image's shape and
orientation.  This is an example of the concept of :ref:`transform chaining
<transformation-pipeline>`.

The image of the output should have its boundary match the dashed yellow
rectangle.
"""���`a
���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnjtransforms���`a ���akbas���`a ���bnnkmtransforms���`a
���`a
���`a
���akcdef���`a ���bnfiget_image���`a(���`a)���`a:���`a
���`d    ���`edelta���`a ���aoa=���`a ���bmfd0.25���`a
���`d    ���`ax���`a ���aoa=���`a ���`ay���`a ���aoa=���`a ���`bnp���aoa.���`farange���`a(���aoa-���bmfc3.0���`a,���`a ���bmfc3.0���`a,���`a ���`edelta���`a)���`a
���`d    ���`aX���`a,���`a ���`aY���`a ���aoa=���`a ���`bnp���aoa.���`hmeshgrid���`a(���`ax���`a,���`a ���`ay���`a)���`a
���`d    ���`bZ1���`a ���aoa=���`a ���`bnp���aoa.���`cexp���`a(���aoa-���`aX���aoa*���aoa*���bmia2���`a ���aoa-���`a ���`aY���aoa*���aoa*���bmia2���`a)���`a
���`d    ���`bZ2���`a ���aoa=���`a ���`bnp���aoa.���`cexp���`a(���aoa-���`a(���`aX���`a ���aoa-���`a ���bmia1���`a)���aoa*���aoa*���bmia2���`a ���aoa-���`a ���`a(���`aY���`a ���aoa-���`a ���bmia1���`a)���aoa*���aoa*���bmia2���`a)���`a
���`d    ���`aZ���`a ���aoa=���`a ���`a(���`bZ1���`a ���aoa-���`a ���`bZ2���`a)���`a
���`d    ���akfreturn���`a ���`aZ���`a
���`a
���`a
���akcdef���`a ���bnfgdo_plot���`a(���`bax���`a,���`a ���`aZ���`a,���`a ���`itransform���`a)���`a:���`a
���`d    ���`bim���`a ���aoa=���`a ���`bax���aoa.���`fimshow���`a(���`aZ���`a,���`a ���`minterpolation���aoa=���bs1a'���bs1dnone���bs1a'���`a,���`a
���`s                   ���`forigin���aoa=���bs1a'���bs1elower���bs1a'���`a,���`a
���`s                   ���`fextent���aoa=���`a[���aoa-���bmia2���`a,���`a ���bmia4���`a,���`a ���aoa-���bmia3���`a,���`a ���bmia2���`a]���`a,���`a ���`gclip_on���aoa=���bkcdTrue���`a)���`a
���`a
���`d    ���`jtrans_data���`a ���aoa=���`a ���`itransform���`a ���aoa+���`a ���`bax���aoa.���`itransData���`a
���`d    ���`bim���aoa.���`mset_transform���`a(���`jtrans_data���`a)���`a
���`a
���`d    ���bc1x&# display intended extent of the image���`a
���`d    ���`bx1���`a,���`a ���`bx2���`a,���`a ���`by1���`a,���`a ���`by2���`a ���aoa=���`a ���`bim���aoa.���`jget_extent���`a(���`a)���`a
���`d    ���`bax���aoa.���`dplot���`a(���`a[���`bx1���`a,���`a ���`bx2���`a,���`a ���`bx2���`a,���`a ���`bx1���`a,���`a ���`bx1���`a]���`a,���`a ���`a[���`by1���`a,���`a ���`by1���`a,���`a ���`by2���`a,���`a ���`by2���`a,���`a ���`by1���`a]���`a,���`a ���bs2a"���bs2cy--���bs2a"���`a,���`a
���`l            ���`itransform���aoa=���`jtrans_data���`a)���`a
���`d    ���`bax���aoa.���`hset_xlim���`a(���aoa-���bmia5���`a,���`a ���bmia5���`a)���`a
���`d    ���`bax���aoa.���`hset_ylim���`a(���aoa-���bmia4���`a,���`a ���bmia4���`a)���`a
���`a
���`a
���bc1x# prepare image and figure���`a
���`cfig���`a,���`a ���`a(���`a(���`cax1���`a,���`a ���`cax2���`a)���`a,���`a ���`a(���`cax3���`a,���`a ���`cax4���`a)���`a)���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���bmia2���`a,���`a ���bmia2���`a)���`a
���`aZ���`a ���aoa=���`a ���`iget_image���`a(���`a)���`a
���`a
���bc1p# image rotation���`a
���`gdo_plot���`a(���`cax1���`a,���`a ���`aZ���`a,���`a ���`kmtransforms���aoa.���`hAffine2D���`a(���`a)���aoa.���`jrotate_deg���`a(���bmib30���`a)���`a)���`a
���`a
���bc1l# image skew���`a
���`gdo_plot���`a(���`cax2���`a,���`a ���`aZ���`a,���`a ���`kmtransforms���aoa.���`hAffine2D���`a(���`a)���aoa.���`hskew_deg���`a(���bmib30���`a,���`a ���bmib15���`a)���`a)���`a
���`a
���bc1v# scale and reflection���`a
���`gdo_plot���`a(���`cax3���`a,���`a ���`aZ���`a,���`a ���`kmtransforms���aoa.���`hAffine2D���`a(���`a)���aoa.���`escale���`a(���aoa-���bmia1���`a,���`a ���bmfb.5���`a)���`a)���`a
���`a
���bc1x# everything and a translation���`a
���`gdo_plot���`a(���`cax4���`a,���`a ���`aZ���`a,���`a ���`kmtransforms���aoa.���`hAffine2D���`a(���`a)���aoa.���`a
���`h        ���`jrotate_deg���`a(���bmib30���`a)���aoa.���`hskew_deg���`a(���bmib30���`a,���`a ���bmib15���`a)���aoa.���`escale���`a(���aoa-���bmia1���`a,���`a ���bmfb.5���`a)���aoa.���`itranslate���`a(���bmfb.5���`a,���`a ���aoa-���bmia1���`a)���`a)���`a
���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
���`a
���`a
���bc1xM#############################################################################���`a
���bc1a#���`a
���bc1x# .. admonition:: References���`a
���bc1a#���`a
���bc1xN#    The use of the following functions, methods, classes and modules is shown���`a
���bc1u#    in this example:���`a
���bc1a#���`a
���bc1xA#    - `matplotlib.axes.Axes.imshow` / `matplotlib.pyplot.imshow`���`a
���bc1x'#    - `matplotlib.transforms.Affine2D`���`a
`dNone�