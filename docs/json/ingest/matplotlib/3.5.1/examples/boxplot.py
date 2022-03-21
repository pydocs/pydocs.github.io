������������bsdy�"""
=================================
Artist customization in box plots
=================================

This example demonstrates how to use the various keyword arguments to fully
customize box plots. The first figure demonstrates how to remove and add
individual components (note that the mean is the only value not shown by
default). The second figure demonstrates how the styles of the artists can be
customized. It also demonstrates how to set the limit of the whiskers to
specific percentiles (lower right axes)

A good general reference on boxplots and their history can be found here:
https://vita.had.co.nz/papers/boxplots.pdf

"""���`a
���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���`a
���bc1k# fake data���`a
���`bnp���aoa.���`frandom���aoa.���`dseed���`a(���bmih19680801���`a)���`a
���`ddata���`a ���aoa=���`a ���`bnp���aoa.���`frandom���aoa.���`ilognormal���`a(���`dsize���aoa=���`a(���bmib37���`a,���`a ���bmia4���`a)���`a,���`a ���`dmean���aoa=���bmfc1.5���`a,���`a ���`esigma���aoa=���bmfd1.75���`a)���`a
���`flabels���`a ���aoa=���`a ���bnbdlist���`a(���bs1a'���bs1dABCD���bs1a'���`a)���`a
���`bfs���`a ���aoa=���`a ���bmib10���`b  ���bc1j# fontsize���`a
���`a
���bc1xO###############################################################################���`a
���bc1x># Demonstrate how to toggle the display of different elements:���`a
���`a
���`cfig���`a,���`a ���`caxs���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`enrows���aoa=���bmia2���`a,���`a ���`encols���aoa=���bmia3���`a,���`a ���`gfigsize���aoa=���`a(���bmia6���`a,���`a ���bmia6���`a)���`a,���`a ���`fsharey���aoa=���bkcdTrue���`a)���`a
���`caxs���`a[���bmia0���`a,���`a ���bmia0���`a]���aoa.���`gboxplot���`a(���`ddata���`a,���`a ���`flabels���aoa=���`flabels���`a)���`a
���`caxs���`a[���bmia0���`a,���`a ���bmia0���`a]���aoa.���`iset_title���`a(���bs1a'���bs1gDefault���bs1a'���`a,���`a ���`hfontsize���aoa=���`bfs���`a)���`a
���`a
���`caxs���`a[���bmia0���`a,���`a ���bmia1���`a]���aoa.���`gboxplot���`a(���`ddata���`a,���`a ���`flabels���aoa=���`flabels���`a,���`a ���`ishowmeans���aoa=���bkcdTrue���`a)���`a
���`caxs���`a[���bmia0���`a,���`a ���bmia1���`a]���aoa.���`iset_title���`a(���bs1a'���bs1nshowmeans=True���bs1a'���`a,���`a ���`hfontsize���aoa=���`bfs���`a)���`a
���`a
���`caxs���`a[���bmia0���`a,���`a ���bmia2���`a]���aoa.���`gboxplot���`a(���`ddata���`a,���`a ���`flabels���aoa=���`flabels���`a,���`a ���`ishowmeans���aoa=���bkcdTrue���`a,���`a ���`hmeanline���aoa=���bkcdTrue���`a)���`a
���`caxs���`a[���bmia0���`a,���`a ���bmia2���`a]���aoa.���`iset_title���`a(���bs1a'���bs1oshowmeans=True,���bseb\n���bs1mmeanline=True���bs1a'���`a,���`a ���`hfontsize���aoa=���`bfs���`a)���`a
���`a
���`caxs���`a[���bmia1���`a,���`a ���bmia0���`a]���aoa.���`gboxplot���`a(���`ddata���`a,���`a ���`flabels���aoa=���`flabels���`a,���`a ���`gshowbox���aoa=���bkceFalse���`a,���`a ���`hshowcaps���aoa=���bkceFalse���`a)���`a
���`ktufte_title���`a ���aoa=���`a ���bs1a'���bs1lTufte Style ���bseb\n���bs1o(showbox=False,���bseb\n���bs1oshowcaps=False)���bs1a'���`a
���`caxs���`a[���bmia1���`a,���`a ���bmia0���`a]���aoa.���`iset_title���`a(���`ktufte_title���`a,���`a ���`hfontsize���aoa=���`bfs���`a)���`a
���`a
���`caxs���`a[���bmia1���`a,���`a ���bmia1���`a]���aoa.���`gboxplot���`a(���`ddata���`a,���`a ���`flabels���aoa=���`flabels���`a,���`a ���`enotch���aoa=���bkcdTrue���`a,���`a ���`ibootstrap���aoa=���bmie10000���`a)���`a
���`caxs���`a[���bmia1���`a,���`a ���bmia1���`a]���aoa.���`iset_title���`a(���bs1a'���bs1knotch=True,���bseb\n���bs1obootstrap=10000���bs1a'���`a,���`a ���`hfontsize���aoa=���`bfs���`a)���`a
���`a
���`caxs���`a[���bmia1���`a,���`a ���bmia2���`a]���aoa.���`gboxplot���`a(���`ddata���`a,���`a ���`flabels���aoa=���`flabels���`a,���`a ���`jshowfliers���aoa=���bkceFalse���`a)���`a
���`caxs���`a[���bmia1���`a,���`a ���bmia2���`a]���aoa.���`iset_title���`a(���bs1a'���bs1pshowfliers=False���bs1a'���`a,���`a ���`hfontsize���aoa=���`bfs���`a)���`a
���`a
���akcfor���`a ���`bax���`a ���bowbin���`a ���`caxs���aoa.���`dflat���`a:���`a
���`d    ���`bax���aoa.���`jset_yscale���`a(���bs1a'���bs1clog���bs1a'���`a)���`a
���`d    ���`bax���aoa.���`oset_yticklabels���`a(���`a[���`a]���`a)���`a
���`a
���`cfig���aoa.���`osubplots_adjust���`a(���`fhspace���aoa=���bmfc0.4���`a)���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
���`a
���`a
���bc1xO###############################################################################���`a
���bc1x># Demonstrate how to customize the display different elements:���`a
���`a
���`hboxprops���`a ���aoa=���`a ���bnbddict���`a(���`ilinestyle���aoa=���bs1a'���bs1b--���bs1a'���`a,���`a ���`ilinewidth���aoa=���bmia3���`a,���`a ���`ecolor���aoa=���bs1a'���bs1mdarkgoldenrod���bs1a'���`a)���`a
���`jflierprops���`a ���aoa=���`a ���bnbddict���`a(���`fmarker���aoa=���bs1a'���bs1ao���bs1a'���`a,���`a ���`omarkerfacecolor���aoa=���bs1a'���bs1egreen���bs1a'���`a,���`a ���`jmarkersize���aoa=���bmib12���`a,���`a
���`r                  ���`omarkeredgecolor���aoa=���bs1a'���bs1dnone���bs1a'���`a)���`a
���`kmedianprops���`a ���aoa=���`a ���bnbddict���`a(���`ilinestyle���aoa=���bs1a'���bs1b-.���bs1a'���`a,���`a ���`ilinewidth���aoa=���bmfc2.5���`a,���`a ���`ecolor���aoa=���bs1a'���bs1ifirebrick���bs1a'���`a)���`a
���`nmeanpointprops���`a ���aoa=���`a ���bnbddict���`a(���`fmarker���aoa=���bs1a'���bs1aD���bs1a'���`a,���`a ���`omarkeredgecolor���aoa=���bs1a'���bs1eblack���bs1a'���`a,���`a
���`v                      ���`omarkerfacecolor���aoa=���bs1a'���bs1ifirebrick���bs1a'���`a)���`a
���`mmeanlineprops���`a ���aoa=���`a ���bnbddict���`a(���`ilinestyle���aoa=���bs1a'���bs1b--���bs1a'���`a,���`a ���`ilinewidth���aoa=���bmfc2.5���`a,���`a ���`ecolor���aoa=���bs1a'���bs1fpurple���bs1a'���`a)���`a
���`a
���`cfig���`a,���`a ���`caxs���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`enrows���aoa=���bmia2���`a,���`a ���`encols���aoa=���bmia3���`a,���`a ���`gfigsize���aoa=���`a(���bmia6���`a,���`a ���bmia6���`a)���`a,���`a ���`fsharey���aoa=���bkcdTrue���`a)���`a
���`caxs���`a[���bmia0���`a,���`a ���bmia0���`a]���aoa.���`gboxplot���`a(���`ddata���`a,���`a ���`hboxprops���aoa=���`hboxprops���`a)���`a
���`caxs���`a[���bmia0���`a,���`a ���bmia0���`a]���aoa.���`iset_title���`a(���bs1a'���bs1oCustom boxprops���bs1a'���`a,���`a ���`hfontsize���aoa=���`bfs���`a)���`a
���`a
���`caxs���`a[���bmia0���`a,���`a ���bmia1���`a]���aoa.���`gboxplot���`a(���`ddata���`a,���`a ���`jflierprops���aoa=���`jflierprops���`a,���`a ���`kmedianprops���aoa=���`kmedianprops���`a)���`a
���`caxs���`a[���bmia0���`a,���`a ���bmia1���`a]���aoa.���`iset_title���`a(���bs1a'���bs1rCustom medianprops���bseb\n���bs1nand flierprops���bs1a'���`a,���`a ���`hfontsize���aoa=���`bfs���`a)���`a
���`a
���`caxs���`a[���bmia0���`a,���`a ���bmia2���`a]���aoa.���`gboxplot���`a(���`ddata���`a,���`a ���`dwhis���aoa=���`a(���bmia0���`a,���`a ���bmic100���`a)���`a)���`a
���`caxs���`a[���bmia0���`a,���`a ���bmia2���`a]���aoa.���`iset_title���`a(���bs1a'���bs1mwhis=(0, 100)���bs1a'���`a,���`a ���`hfontsize���aoa=���`bfs���`a)���`a
���`a
���`caxs���`a[���bmia1���`a,���`a ���bmia0���`a]���aoa.���`gboxplot���`a(���`ddata���`a,���`a ���`imeanprops���aoa=���`nmeanpointprops���`a,���`a ���`hmeanline���aoa=���bkceFalse���`a,���`a
���`r                  ���`ishowmeans���aoa=���bkcdTrue���`a)���`a
���`caxs���`a[���bmia1���`a,���`a ���bmia0���`a]���aoa.���`iset_title���`a(���bs1a'���bs1kCustom mean���bseb\n���bs1has point���bs1a'���`a,���`a ���`hfontsize���aoa=���`bfs���`a)���`a
���`a
���`caxs���`a[���bmia1���`a,���`a ���bmia1���`a]���aoa.���`gboxplot���`a(���`ddata���`a,���`a ���`imeanprops���aoa=���`mmeanlineprops���`a,���`a ���`hmeanline���aoa=���bkcdTrue���`a,���`a
���`r                  ���`ishowmeans���aoa=���bkcdTrue���`a)���`a
���`caxs���`a[���bmia1���`a,���`a ���bmia1���`a]���aoa.���`iset_title���`a(���bs1a'���bs1kCustom mean���bseb\n���bs1gas line���bs1a'���`a,���`a ���`hfontsize���aoa=���`bfs���`a)���`a
���`a
���`caxs���`a[���bmia1���`a,���`a ���bmia2���`a]���aoa.���`gboxplot���`a(���`ddata���`a,���`a ���`dwhis���aoa=���`a[���bmib15���`a,���`a ���bmib85���`a]���`a)���`a
���`caxs���`a[���bmia1���`a,���`a ���bmia2���`a]���aoa.���`iset_title���`a(���bs1a'���bs1mwhis=[15, 85]���bseb\n���bs1l#percentiles���bs1a'���`a,���`a ���`hfontsize���aoa=���`bfs���`a)���`a
���`a
���akcfor���`a ���`bax���`a ���bowbin���`a ���`caxs���aoa.���`dflat���`a:���`a
���`d    ���`bax���aoa.���`jset_yscale���`a(���bs1a'���bs1clog���bs1a'���`a)���`a
���`d    ���`bax���aoa.���`oset_yticklabels���`a(���`a[���`a]���`a)���`a
���`a
���`cfig���aoa.���`hsuptitle���`a(���bs2a"���bs2qI never said they���bs2a'���bs2kd be pretty���bs2a"���`a)���`a
���`cfig���aoa.���`osubplots_adjust���`a(���`fhspace���aoa=���bmfc0.4���`a)���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
���`a
���bc1xM#############################################################################���`a
���bc1a#���`a
���bc1x# .. admonition:: References���`a
���bc1a#���`a
���bc1xN#    The use of the following functions, methods, classes and modules is shown���`a
���bc1u#    in this example:���`a
���bc1a#���`a
���bc1xC#    - `matplotlib.axes.Axes.boxplot` / `matplotlib.pyplot.boxplot`���`a
`dNone�