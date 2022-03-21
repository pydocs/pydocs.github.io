��������v���bsdy�"""
===============================
Resizing axes with tight layout
===============================

`~.figure.Figure.tight_layout` attempts to resize subplots in
a figure so that there are no overlaps between axes objects and labels
on the axes.

See :doc:`/tutorials/intermediate/tight_layout_guide` for more details and
:doc:`/tutorials/intermediate/constrainedlayout_guide` for an alternative.

"""���`a
���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���bknfimport���`a ���bnniitertools���`a
���bknfimport���`a ���bnnhwarnings���`a
���`a
���`a
���`ifontsizes���`a ���aoa=���`a ���`iitertools���aoa.���`ecycle���`a(���`a[���bmia8���`a,���`a ���bmib16���`a,���`a ���bmib24���`a,���`a ���bmib32���`a]���`a)���`a
���`a
���`a
���akcdef���`a ���bnflexample_plot���`a(���`bax���`a)���`a:���`a
���`d    ���`bax���aoa.���`dplot���`a(���`a[���bmia1���`a,���`a ���bmia2���`a]���`a)���`a
���`d    ���`bax���aoa.���`jset_xlabel���`a(���bs1a'���bs1gx-label���bs1a'���`a,���`a ���`hfontsize���aoa=���bnbdnext���`a(���`ifontsizes���`a)���`a)���`a
���`d    ���`bax���aoa.���`jset_ylabel���`a(���bs1a'���bs1gy-label���bs1a'���`a,���`a ���`hfontsize���aoa=���bnbdnext���`a(���`ifontsizes���`a)���`a)���`a
���`d    ���`bax���aoa.���`iset_title���`a(���bs1a'���bs1eTitle���bs1a'���`a,���`a ���`hfontsize���aoa=���bnbdnext���`a(���`ifontsizes���`a)���`a)���`a
���`a
���`a
���bc1xO###############################################################################���`a
���`a
���`cfig���`a,���`a ���`bax���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`a)���`a
���`lexample_plot���`a(���`bax���`a)���`a
���`cfig���aoa.���`ltight_layout���`a(���`a)���`a
���`a
���bc1xO###############################################################################���`a
���`a
���`cfig���`a,���`a ���`a(���`a(���`cax1���`a,���`a ���`cax2���`a)���`a,���`a ���`a(���`cax3���`a,���`a ���`cax4���`a)���`a)���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`enrows���aoa=���bmia2���`a,���`a ���`encols���aoa=���bmia2���`a)���`a
���`lexample_plot���`a(���`cax1���`a)���`a
���`lexample_plot���`a(���`cax2���`a)���`a
���`lexample_plot���`a(���`cax3���`a)���`a
���`lexample_plot���`a(���`cax4���`a)���`a
���`cfig���aoa.���`ltight_layout���`a(���`a)���`a
���`a
���bc1xO###############################################################################���`a
���`a
���`cfig���`a,���`a ���`a(���`cax1���`a,���`a ���`cax2���`a)���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`enrows���aoa=���bmia2���`a,���`a ���`encols���aoa=���bmia1���`a)���`a
���`lexample_plot���`a(���`cax1���`a)���`a
���`lexample_plot���`a(���`cax2���`a)���`a
���`cfig���aoa.���`ltight_layout���`a(���`a)���`a
���`a
���bc1xO###############################################################################���`a
���`a
���`cfig���`a,���`a ���`a(���`cax1���`a,���`a ���`cax2���`a)���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`enrows���aoa=���bmia1���`a,���`a ���`encols���aoa=���bmia2���`a)���`a
���`lexample_plot���`a(���`cax1���`a)���`a
���`lexample_plot���`a(���`cax2���`a)���`a
���`cfig���aoa.���`ltight_layout���`a(���`a)���`a
���`a
���bc1xO###############################################################################���`a
���`a
���`cfig���`a,���`a ���`caxs���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`enrows���aoa=���bmia3���`a,���`a ���`encols���aoa=���bmia3���`a)���`a
���akcfor���`a ���`bax���`a ���bowbin���`a ���`caxs���aoa.���`dflat���`a:���`a
���`d    ���`lexample_plot���`a(���`bax���`a)���`a
���`cfig���aoa.���`ltight_layout���`a(���`a)���`a
���`a
���bc1xO###############################################################################���`a
���`a
���`cplt���aoa.���`ffigure���`a(���`a)���`a
���`cax1���`a ���aoa=���`a ���`cplt���aoa.���`gsubplot���`a(���bmic221���`a)���`a
���`cax2���`a ���aoa=���`a ���`cplt���aoa.���`gsubplot���`a(���bmic223���`a)���`a
���`cax3���`a ���aoa=���`a ���`cplt���aoa.���`gsubplot���`a(���bmic122���`a)���`a
���`lexample_plot���`a(���`cax1���`a)���`a
���`lexample_plot���`a(���`cax2���`a)���`a
���`lexample_plot���`a(���`cax3���`a)���`a
���`cplt���aoa.���`ltight_layout���`a(���`a)���`a
���`a
���bc1xO###############################################################################���`a
���`a
���`cplt���aoa.���`ffigure���`a(���`a)���`a
���`cax1���`a ���aoa=���`a ���`cplt���aoa.���`lsubplot2grid���`a(���`a(���bmia3���`a,���`a ���bmia3���`a)���`a,���`a ���`a(���bmia0���`a,���`a ���bmia0���`a)���`a)���`a
���`cax2���`a ���aoa=���`a ���`cplt���aoa.���`lsubplot2grid���`a(���`a(���bmia3���`a,���`a ���bmia3���`a)���`a,���`a ���`a(���bmia0���`a,���`a ���bmia1���`a)���`a,���`a ���`gcolspan���aoa=���bmia2���`a)���`a
���`cax3���`a ���aoa=���`a ���`cplt���aoa.���`lsubplot2grid���`a(���`a(���bmia3���`a,���`a ���bmia3���`a)���`a,���`a ���`a(���bmia1���`a,���`a ���bmia0���`a)���`a,���`a ���`gcolspan���aoa=���bmia2���`a,���`a ���`growspan���aoa=���bmia2���`a)���`a
���`cax4���`a ���aoa=���`a ���`cplt���aoa.���`lsubplot2grid���`a(���`a(���bmia3���`a,���`a ���bmia3���`a)���`a,���`a ���`a(���bmia1���`a,���`a ���bmia2���`a)���`a,���`a ���`growspan���aoa=���bmia2���`a)���`a
���`lexample_plot���`a(���`cax1���`a)���`a
���`lexample_plot���`a(���`cax2���`a)���`a
���`lexample_plot���`a(���`cax3���`a)���`a
���`lexample_plot���`a(���`cax4���`a)���`a
���`cplt���aoa.���`ltight_layout���`a(���`a)���`a
���`a
���bc1xO###############################################################################���`a
���`a
���`cfig���`a ���aoa=���`a ���`cplt���aoa.���`ffigure���`a(���`a)���`a
���`a
���`cgs1���`a ���aoa=���`a ���`cfig���aoa.���`ladd_gridspec���`a(���bmia3���`a,���`a ���bmia1���`a)���`a
���`cax1���`a ���aoa=���`a ���`cfig���aoa.���`kadd_subplot���`a(���`cgs1���`a[���bmia0���`a]���`a)���`a
���`cax2���`a ���aoa=���`a ���`cfig���aoa.���`kadd_subplot���`a(���`cgs1���`a[���bmia1���`a]���`a)���`a
���`cax3���`a ���aoa=���`a ���`cfig���aoa.���`kadd_subplot���`a(���`cgs1���`a[���bmia2���`a]���`a)���`a
���`lexample_plot���`a(���`cax1���`a)���`a
���`lexample_plot���`a(���`cax2���`a)���`a
���`lexample_plot���`a(���`cax3���`a)���`a
���`cgs1���aoa.���`ltight_layout���`a(���`cfig���`a,���`a ���`drect���aoa=���`a[���bkcdNone���`a,���`a ���bkcdNone���`a,���`a ���bmfd0.45���`a,���`a ���bkcdNone���`a]���`a)���`a
���`a
���`cgs2���`a ���aoa=���`a ���`cfig���aoa.���`ladd_gridspec���`a(���bmia2���`a,���`a ���bmia1���`a)���`a
���`cax4���`a ���aoa=���`a ���`cfig���aoa.���`kadd_subplot���`a(���`cgs2���`a[���bmia0���`a]���`a)���`a
���`cax5���`a ���aoa=���`a ���`cfig���aoa.���`kadd_subplot���`a(���`cgs2���`a[���bmia1���`a]���`a)���`a
���`lexample_plot���`a(���`cax4���`a)���`a
���`lexample_plot���`a(���`cax5���`a)���`a
���akdwith���`a ���`hwarnings���aoa.���`ncatch_warnings���`a(���`a)���`a:���`a
���`d    ���bc1xE# gs2.tight_layout cannot handle the subplots from the first gridspec���`a
���`d    ���bc1xH# (gs1), so it will raise a warning. We are going to match the gridspecs���`a
���`d    ���bc1x-# manually so we can filter the warning away.���`a
���`d    ���`hwarnings���aoa.���`lsimplefilter���`a(���bs2a"���bs2fignore���bs2a"���`a,���`a ���bnekUserWarning���`a)���`a
���`d    ���`cgs2���aoa.���`ltight_layout���`a(���`cfig���`a,���`a ���`drect���aoa=���`a[���bmfd0.45���`a,���`a ���bkcdNone���`a,���`a ���bkcdNone���`a,���`a ���bkcdNone���`a]���`a)���`a
���`a
���bc1x0# now match the top and bottom of two gridspecs.���`a
���`ctop���`a ���aoa=���`a ���bnbcmin���`a(���`cgs1���aoa.���`ctop���`a,���`a ���`cgs2���aoa.���`ctop���`a)���`a
���`fbottom���`a ���aoa=���`a ���bnbcmax���`a(���`cgs1���aoa.���`fbottom���`a,���`a ���`cgs2���aoa.���`fbottom���`a)���`a
���`a
���`cgs1���aoa.���`fupdate���`a(���`ctop���aoa=���`ctop���`a,���`a ���`fbottom���aoa=���`fbottom���`a)���`a
���`cgs2���aoa.���`fupdate���`a(���`ctop���aoa=���`ctop���`a,���`a ���`fbottom���aoa=���`fbottom���`a)���`a
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
���bc1x0#    - `matplotlib.figure.Figure.tight_layout` /���`a
���bc1x'#      `matplotlib.pyplot.tight_layout`���`a
���bc1x.#    - `matplotlib.figure.Figure.add_gridspec`���`a
���bc1x-#    - `matplotlib.figure.Figure.add_subplot`���`a
���bc1x'#    - `matplotlib.pyplot.subplot2grid`���`a
`dNone�