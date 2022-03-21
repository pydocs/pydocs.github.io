������������bsdy`"""
========================
3D plot projection types
========================

Demonstrates the different camera projections for 3D plots, and the effects of
changing the focal length for a perspective projection. Note that Matplotlib
corrects for the 'zoom' effect of changing the focal length.

The default focal length of 1 corresponds to a Field of View (FOV) of 90 deg.
An increased focal length between 1 and infinity "flattens" the image, while a
decreased focal length between 1 and 0 exaggerates the perspective and gives
the image more apparent depth. In the limiting case, a focal length of
infinity corresponds to an orthographic projection after correction of the
zoom effect.

You can calculate focal length from a FOV via the equation:

.. mathmpl::

    1 / \tan (FOV / 2)

Or vice versa:

.. mathmpl::

    FOV = 2 * \atan (1 / focal length)

"""���`a
���`a
���bkndfrom���`a ���bnnlmpl_toolkits���bnna.���bnngmplot3d���`a ���bknfimport���`a ���`faxes3d���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���`a
���`a
���`cfig���`a,���`a ���`caxs���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���bmia1���`a,���`a ���bmia3���`a,���`a ���`jsubplot_kw���aoa=���`a{���bs1a'���bs1jprojection���bs1a'���`a:���`a ���bs1a'���bs1b3d���bs1a'���`a}���`a)���`a
���`a
���bc1s# Get the test data���`a
���`aX���`a,���`a ���`aY���`a,���`a ���`aZ���`a ���aoa=���`a ���`faxes3d���aoa.���`mget_test_data���`a(���bmfd0.05���`a)���`a
���`a
���bc1o# Plot the data���`a
���akcfor���`a ���`bax���`a ���bowbin���`a ���`caxs���`a:���`a
���`d    ���`bax���aoa.���`nplot_wireframe���`a(���`aX���`a,���`a ���`aY���`a,���`a ���`aZ���`a,���`a ���`grstride���aoa=���bmib10���`a,���`a ���`gcstride���aoa=���bmib10���`a)���`a
���`a
���bc1x"# Set the orthographic projection.���`a
���`caxs���`a[���bmia0���`a]���aoa.���`mset_proj_type���`a(���bs1a'���bs1eortho���bs1a'���`a)���`b  ���bc1m# FOV = 0 deg���`a
���`caxs���`a[���bmia0���`a]���aoa.���`iset_title���`a(���bs2a"���bs2a'���bs2eortho���bs2a'���bseb\n���bs2rfocal_length = ∞���bs2a"���`a,���`a ���`hfontsize���aoa=���bmib10���`a)���`a
���`a
���bc1x!# Set the perspective projections���`a
���`caxs���`a[���bmia1���`a]���aoa.���`mset_proj_type���`a(���bs1a'���bs1epersp���bs1a'���`a)���`b  ���bc1n# FOV = 90 deg���`a
���`caxs���`a[���bmia1���`a]���aoa.���`iset_title���`a(���bs2a"���bs2a'���bs2epersp���bs2a'���bseb\n���bs2xfocal_length = 1 (default)���bs2a"���`a,���`a ���`hfontsize���aoa=���bmib10���`a)���`a
���`a
���`caxs���`a[���bmia2���`a]���aoa.���`mset_proj_type���`a(���bs1a'���bs1epersp���bs1a'���`a,���`a ���`lfocal_length���aoa=���bmfc0.2���`a)���`b  ���bc1q# FOV = 157.4 deg���`a
���`caxs���`a[���bmia2���`a]���aoa.���`iset_title���`a(���bs2a"���bs2a'���bs2epersp���bs2a'���bseb\n���bs2rfocal_length = 0.2���bs2a"���`a,���`a ���`hfontsize���aoa=���bmib10���`a)���`a
���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
`dNone�