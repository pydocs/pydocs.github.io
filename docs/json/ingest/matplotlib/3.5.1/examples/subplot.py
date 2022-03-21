��������;���bsdx�"""
=================
Multiple subplots
=================

Simple demo with multiple subplots.

For more options, see :doc:`/gallery/subplots_axes_and_figures/subplots_demo`.

.. redirect-from:: /gallery/subplots_axes_and_figures/subplot_demo
"""���`a
���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���`a
���bc1x# Create some fake data.���`a
���`bx1���`a ���aoa=���`a ���`bnp���aoa.���`hlinspace���`a(���bmfc0.0���`a,���`a ���bmfc5.0���`a)���`a
���`by1���`a ���aoa=���`a ���`bnp���aoa.���`ccos���`a(���bmia2���`a ���aoa*���`a ���`bnp���aoa.���`bpi���`a ���aoa*���`a ���`bx1���`a)���`a ���aoa*���`a ���`bnp���aoa.���`cexp���`a(���aoa-���`bx1���`a)���`a
���`bx2���`a ���aoa=���`a ���`bnp���aoa.���`hlinspace���`a(���bmfc0.0���`a,���`a ���bmfc2.0���`a)���`a
���`by2���`a ���aoa=���`a ���`bnp���aoa.���`ccos���`a(���bmia2���`a ���aoa*���`a ���`bnp���aoa.���`bpi���`a ���aoa*���`a ���`bx2���`a)���`a
���`a
���bc1xO###############################################################################���`a
���bc1xL# `~.pyplot.subplots()` is the recommended method to generate simple subplot���`a
���bc1o# arrangements:���`a
���`a
���`cfig���`a,���`a ���`a(���`cax1���`a,���`a ���`cax2���`a)���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���bmia2���`a,���`a ���bmia1���`a)���`a
���`cfig���aoa.���`hsuptitle���`a(���bs1a'���bs1tA tale of 2 subplots���bs1a'���`a)���`a
���`a
���`cax1���aoa.���`dplot���`a(���`bx1���`a,���`a ���`by1���`a,���`a ���bs1a'���bs1bo-���bs1a'���`a)���`a
���`cax1���aoa.���`jset_ylabel���`a(���bs1a'���bs1rDamped oscillation���bs1a'���`a)���`a
���`a
���`cax2���aoa.���`dplot���`a(���`bx2���`a,���`a ���`by2���`a,���`a ���bs1a'���bs1b.-���bs1a'���`a)���`a
���`cax2���aoa.���`jset_xlabel���`a(���bs1a'���bs1htime (s)���bs1a'���`a)���`a
���`cax2���aoa.���`jset_ylabel���`a(���bs1a'���bs1hUndamped���bs1a'���`a)���`a
���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
���`a
���bc1xO###############################################################################���`a
���bc1xJ# Subplots can also be generated one at a time using `~.pyplot.subplot()`:���`a
���`a
���`cplt���aoa.���`gsubplot���`a(���bmia2���`a,���`a ���bmia1���`a,���`a ���bmia1���`a)���`a
���`cplt���aoa.���`dplot���`a(���`bx1���`a,���`a ���`by1���`a,���`a ���bs1a'���bs1bo-���bs1a'���`a)���`a
���`cplt���aoa.���`etitle���`a(���bs1a'���bs1tA tale of 2 subplots���bs1a'���`a)���`a
���`cplt���aoa.���`fylabel���`a(���bs1a'���bs1rDamped oscillation���bs1a'���`a)���`a
���`a
���`cplt���aoa.���`gsubplot���`a(���bmia2���`a,���`a ���bmia1���`a,���`a ���bmia2���`a)���`a
���`cplt���aoa.���`dplot���`a(���`bx2���`a,���`a ���`by2���`a,���`a ���bs1a'���bs1b.-���bs1a'���`a)���`a
���`cplt���aoa.���`fxlabel���`a(���bs1a'���bs1htime (s)���bs1a'���`a)���`a
���`cplt���aoa.���`fylabel���`a(���bs1a'���bs1hUndamped���bs1a'���`a)���`a
���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
`dNone�