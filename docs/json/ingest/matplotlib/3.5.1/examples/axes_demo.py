��������s���bsdyn"""
=========
Axes Demo
=========

Example use of ``fig.add_axes`` to create inset axes within the main plot axes.

Please see also the :ref:`axes_grid_examples` section, and the following three
examples:

- :doc:`/gallery/subplots_axes_and_figures/zoom_inset_axes`
- :doc:`/gallery/axes_grid1/inset_locator_demo`
- :doc:`/gallery/axes_grid1/inset_locator_demo2`
"""���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���`a
���`bnp���aoa.���`frandom���aoa.���`dseed���`a(���bmih19680801���`a)���`b  ���bc1x*# Fixing random state for reproducibility.���`a
���`a
���bc1x&# create some data to use for the plot���`a
���`bdt���`a ���aoa=���`a ���bmfe0.001���`a
���`at���`a ���aoa=���`a ���`bnp���aoa.���`farange���`a(���bmfc0.0���`a,���`a ���bmfd10.0���`a,���`a ���`bdt���`a)���`a
���`ar���`a ���aoa=���`a ���`bnp���aoa.���`cexp���`a(���aoa-���`at���`a[���`a:���bmid1000���`a]���`a ���aoa/���`a ���bmfd0.05���`a)���`b  ���bc1r# impulse response���`a
���`ax���`a ���aoa=���`a ���`bnp���aoa.���`frandom���aoa.���`erandn���`a(���bnbclen���`a(���`at���`a)���`a)���`a
���`as���`a ���aoa=���`a ���`bnp���aoa.���`hconvolve���`a(���`ax���`a,���`a ���`ar���`a)���`a[���`a:���bnbclen���`a(���`ax���`a)���`a]���`a ���aoa*���`a ���`bdt���`b  ���bc1o# colored noise���`a
���`a
���`cfig���`a,���`a ���`gmain_ax���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`a)���`a
���`gmain_ax���aoa.���`dplot���`a(���`at���`a,���`a ���`as���`a)���`a
���`gmain_ax���aoa.���`hset_xlim���`a(���bmia0���`a,���`a ���bmia1���`a)���`a
���`gmain_ax���aoa.���`hset_ylim���`a(���bmfc1.1���`a ���aoa*���`a ���`bnp���aoa.���`cmin���`a(���`as���`a)���`a,���`a ���bmia2���`a ���aoa*���`a ���`bnp���aoa.���`cmax���`a(���`as���`a)���`a)���`a
���`gmain_ax���aoa.���`jset_xlabel���`a(���bs1a'���bs1htime (s)���bs1a'���`a)���`a
���`gmain_ax���aoa.���`jset_ylabel���`a(���bs1a'���bs1lcurrent (nA)���bs1a'���`a)���`a
���`gmain_ax���aoa.���`iset_title���`a(���bs1a'���bs1vGaussian colored noise���bs1a'���`a)���`a
���`a
���bc1x*# this is an inset axes over the main axes���`a
���`nright_inset_ax���`a ���aoa=���`a ���`cfig���aoa.���`hadd_axes���`a(���`a[���bmfc.65���`a,���`a ���bmfb.6���`a,���`a ���bmfb.2���`a,���`a ���bmfb.2���`a]���`a,���`a ���`ifacecolor���aoa=���bs1a'���bs1ak���bs1a'���`a)���`a
���`nright_inset_ax���aoa.���`dhist���`a(���`as���`a,���`a ���bmic400���`a,���`a ���`gdensity���aoa=���bkcdTrue���`a)���`a
���`nright_inset_ax���aoa.���`cset���`a(���`etitle���aoa=���bs1a'���bs1kProbability���bs1a'���`a,���`a ���`fxticks���aoa=���`a[���`a]���`a,���`a ���`fyticks���aoa=���`a[���`a]���`a)���`a
���`a
���bc1x/# this is another inset axes over the main axes���`a
���`mleft_inset_ax���`a ���aoa=���`a ���`cfig���aoa.���`hadd_axes���`a(���`a[���bmfb.2���`a,���`a ���bmfb.6���`a,���`a ���bmfb.2���`a,���`a ���bmfb.2���`a]���`a,���`a ���`ifacecolor���aoa=���bs1a'���bs1ak���bs1a'���`a)���`a
���`mleft_inset_ax���aoa.���`dplot���`a(���`at���`a[���`a:���bnbclen���`a(���`ar���`a)���`a]���`a,���`a ���`ar���`a)���`a
���`mleft_inset_ax���aoa.���`cset���`a(���`etitle���aoa=���bs1a'���bs1pImpulse response���bs1a'���`a,���`a ���`dxlim���aoa=���`a(���bmia0���`a,���`a ���bmfb.2���`a)���`a,���`a ���`fxticks���aoa=���`a[���`a]���`a,���`a ���`fyticks���aoa=���`a[���`a]���`a)���`a
���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
`dNone�