������������bsdy�"""
============================
Colorbar with `.AxesDivider`
============================

The `.axes_divider.make_axes_locatable` function takes an existing axes, adds
it to a new `.AxesDivider` and returns the `.AxesDivider`.  The `.append_axes`
method of the `.AxesDivider` can then be used to create a new axes on a given
side ("top", "right", "bottom", or "left") of the original axes. This example
uses `.append_axes` to add colorbars next to axes.
"""���`a
���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���bkndfrom���`a ���bnnlmpl_toolkits���bnna.���bnnjaxes_grid1���bnna.���bnnlaxes_divider���`a ���bknfimport���`a ���`smake_axes_locatable���`a
���`a
���`cfig���`a,���`a ���`a(���`cax1���`a,���`a ���`cax2���`a)���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���bmia1���`a,���`a ���bmia2���`a)���`a
���`cfig���aoa.���`osubplots_adjust���`a(���`fwspace���aoa=���bmfc0.5���`a)���`a
���`a
���`cim1���`a ���aoa=���`a ���`cax1���aoa.���`fimshow���`a(���`a[���`a[���bmia1���`a,���`a ���bmia2���`a]���`a,���`a ���`a[���bmia3���`a,���`a ���bmia4���`a]���`a]���`a)���`a
���`kax1_divider���`a ���aoa=���`a ���`smake_axes_locatable���`a(���`cax1���`a)���`a
���bc1x,# Add an axes to the right of the main axes.���`a
���`dcax1���`a ���aoa=���`a ���`kax1_divider���aoa.���`kappend_axes���`a(���bs2a"���bs2eright���bs2a"���`a,���`a ���`dsize���aoa=���bs2a"���bs2a7���bs2a%���bs2a"���`a,���`a ���`cpad���aoa=���bs2a"���bs2a2���bs2a%���bs2a"���`a)���`a
���`ccb1���`a ���aoa=���`a ���`cfig���aoa.���`hcolorbar���`a(���`cim1���`a,���`a ���`ccax���aoa=���`dcax1���`a)���`a
���`a
���`cim2���`a ���aoa=���`a ���`cax2���aoa.���`fimshow���`a(���`a[���`a[���bmia1���`a,���`a ���bmia2���`a]���`a,���`a ���`a[���bmia3���`a,���`a ���bmia4���`a]���`a]���`a)���`a
���`kax2_divider���`a ���aoa=���`a ���`smake_axes_locatable���`a(���`cax2���`a)���`a
���bc1x"# Add an axes above the main axes.���`a
���`dcax2���`a ���aoa=���`a ���`kax2_divider���aoa.���`kappend_axes���`a(���bs2a"���bs2ctop���bs2a"���`a,���`a ���`dsize���aoa=���bs2a"���bs2a7���bs2a%���bs2a"���`a,���`a ���`cpad���aoa=���bs2a"���bs2a2���bs2a%���bs2a"���`a)���`a
���`ccb2���`a ���aoa=���`a ���`cfig���aoa.���`hcolorbar���`a(���`cim2���`a,���`a ���`ccax���aoa=���`dcax2���`a,���`a ���`korientation���aoa=���bs2a"���bs2jhorizontal���bs2a"���`a)���`a
���bc1xM# Change tick position to top (with the default tick position "bottom", ticks���`a
���bc1u# overlap the image).���`a
���`dcax2���aoa.���`exaxis���aoa.���`rset_ticks_position���`a(���bs2a"���bs2ctop���bs2a"���`a)���`a
���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
`dNone�