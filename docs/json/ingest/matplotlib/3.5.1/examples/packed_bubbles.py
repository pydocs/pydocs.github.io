�����������bsdy�"""
===================
Packed-bubble chart
===================

Create a packed-bubble chart to represent scalar data.
The presented algorithm tries to move all bubbles as close to the center of
mass as possible while avoiding some collisions by moving around colliding
objects. In this example we plot the market share of different desktop
browsers.
(source: https://gs.statcounter.com/browser-market-share/desktop/worldwidev)
"""���`a
���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���`a
���`tbrowser_market_share���`a ���aoa=���`a ���`a{���`a
���`d    ���bs1a'���bs1hbrowsers���bs1a'���`a:���`a ���`a[���bs1a'���bs1gfirefox���bs1a'���`a,���`a ���bs1a'���bs1fchrome���bs1a'���`a,���`a ���bs1a'���bs1fsafari���bs1a'���`a,���`a ���bs1a'���bs1dedge���bs1a'���`a,���`a ���bs1a'���bs1bie���bs1a'���`a,���`a ���bs1a'���bs1eopera���bs1a'���`a]���`a,���`a
���`d    ���bs1a'���bs1lmarket_share���bs1a'���`a:���`a ���`a[���bmfd8.61���`a,���`a ���bmfe69.55���`a,���`a ���bmfd8.36���`a,���`a ���bmfd4.12���`a,���`a ���bmfd2.76���`a,���`a ���bmfd2.43���`a]���`a,���`a
���`d    ���bs1a'���bs1ecolor���bs1a'���`a:���`a ���`a[���bs1a'���bs1g#5A69AF���bs1a'���`a,���`a ���bs1a'���bs1g#579E65���bs1a'���`a,���`a ���bs1a'���bs1g#F9C784���bs1a'���`a,���`a ���bs1a'���bs1g#FC944A���bs1a'���`a,���`a ���bs1a'���bs1g#F24C00���bs1a'���`a,���`a ���bs1a'���bs1g#00B825���bs1a'���`a]���`a
���`a}���`a
���`a
���`a
���akeclass���`a ���bnckBubbleChart���`a:���`a
���`d    ���akcdef���`a ���bfmh__init__���`a(���bbpdself���`a,���`a ���`darea���`a,���`a ���`nbubble_spacing���aoa=���bmia0���`a)���`a:���`a
���`h        ���bsdyU"""
        Setup for bubble collapse.

        Parameters
        ----------
        area : array-like
            Area of the bubbles.
        bubble_spacing : float, default: 0
            Minimal spacing between bubbles after collapsing.

        Notes
        -----
        If "area" is sorted, the results might look weird.
        """���`a
���`h        ���`darea���`a ���aoa=���`a ���`bnp���aoa.���`gasarray���`a(���`darea���`a)���`a
���`h        ���`ar���`a ���aoa=���`a ���`bnp���aoa.���`dsqrt���`a(���`darea���`a ���aoa/���`a ���`bnp���aoa.���`bpi���`a)���`a
���`a
���`h        ���bbpdself���aoa.���`nbubble_spacing���`a ���aoa=���`a ���`nbubble_spacing���`a
���`h        ���bbpdself���aoa.���`gbubbles���`a ���aoa=���`a ���`bnp���aoa.���`dones���`a(���`a(���bnbclen���`a(���`darea���`a)���`a,���`a ���bmia4���`a)���`a)���`a
���`h        ���bbpdself���aoa.���`gbubbles���`a[���`a:���`a,���`a ���bmia2���`a]���`a ���aoa=���`a ���`ar���`a
���`h        ���bbpdself���aoa.���`gbubbles���`a[���`a:���`a,���`a ���bmia3���`a]���`a ���aoa=���`a ���`darea���`a
���`h        ���bbpdself���aoa.���`gmaxstep���`a ���aoa=���`a ���bmia2���`a ���aoa*���`a ���bbpdself���aoa.���`gbubbles���`a[���`a:���`a,���`a ���bmia2���`a]���aoa.���`cmax���`a(���`a)���`a ���aoa+���`a ���bbpdself���aoa.���`nbubble_spacing���`a
���`h        ���bbpdself���aoa.���`istep_dist���`a ���aoa=���`a ���bbpdself���aoa.���`gmaxstep���`a ���aoa/���`a ���bmia2���`a
���`a
���`h        ���bc1x+# calculate initial grid layout for bubbles���`a
���`h        ���`flength���`a ���aoa=���`a ���`bnp���aoa.���`dceil���`a(���`bnp���aoa.���`dsqrt���`a(���bnbclen���`a(���bbpdself���aoa.���`gbubbles���`a)���`a)���`a)���`a
���`h        ���`dgrid���`a ���aoa=���`a ���`bnp���aoa.���`farange���`a(���`flength���`a)���`a ���aoa*���`a ���bbpdself���aoa.���`gmaxstep���`a
���`h        ���`bgx���`a,���`a ���`bgy���`a ���aoa=���`a ���`bnp���aoa.���`hmeshgrid���`a(���`dgrid���`a,���`a ���`dgrid���`a)���`a
���`h        ���bbpdself���aoa.���`gbubbles���`a[���`a:���`a,���`a ���bmia0���`a]���`a ���aoa=���`a ���`bgx���aoa.���`gflatten���`a(���`a)���`a[���`a:���bnbclen���`a(���bbpdself���aoa.���`gbubbles���`a)���`a]���`a
���`h        ���bbpdself���aoa.���`gbubbles���`a[���`a:���`a,���`a ���bmia1���`a]���`a ���aoa=���`a ���`bgy���aoa.���`gflatten���`a(���`a)���`a[���`a:���bnbclen���`a(���bbpdself���aoa.���`gbubbles���`a)���`a]���`a
���`a
���`h        ���bbpdself���aoa.���`ccom���`a ���aoa=���`a ���bbpdself���aoa.���`ncenter_of_mass���`a(���`a)���`a
���`a
���`d    ���akcdef���`a ���bnfncenter_of_mass���`a(���bbpdself���`a)���`a:���`a
���`h        ���akfreturn���`a ���`bnp���aoa.���`gaverage���`a(���`a
���`l            ���bbpdself���aoa.���`gbubbles���`a[���`a:���`a,���`a ���`a:���bmia2���`a]���`a,���`a ���`daxis���aoa=���bmia0���`a,���`a ���`gweights���aoa=���bbpdself���aoa.���`gbubbles���`a[���`a:���`a,���`a ���bmia3���`a]���`a
���`h        ���`a)���`a
���`a
���`d    ���akcdef���`a ���bnfocenter_distance���`a(���bbpdself���`a,���`a ���`fbubble���`a,���`a ���`gbubbles���`a)���`a:���`a
���`h        ���akfreturn���`a ���`bnp���aoa.���`ehypot���`a(���`fbubble���`a[���bmia0���`a]���`a ���aoa-���`a ���`gbubbles���`a[���`a:���`a,���`a ���bmia0���`a]���`a,���`a
���`x                        ���`fbubble���`a[���bmia1���`a]���`a ���aoa-���`a ���`gbubbles���`a[���`a:���`a,���`a ���bmia1���`a]���`a)���`a
���`a
���`d    ���akcdef���`a ���bnfpoutline_distance���`a(���bbpdself���`a,���`a ���`fbubble���`a,���`a ���`gbubbles���`a)���`a:���`a
���`h        ���`ocenter_distance���`a ���aoa=���`a ���bbpdself���aoa.���`ocenter_distance���`a(���`fbubble���`a,���`a ���`gbubbles���`a)���`a
���`h        ���akfreturn���`a ���`ocenter_distance���`a ���aoa-���`a ���`fbubble���`a[���bmia2���`a]���`a ���aoa-���`a ���`b\
���`l            ���`gbubbles���`a[���`a:���`a,���`a ���bmia2���`a]���`a ���aoa-���`a ���bbpdself���aoa.���`nbubble_spacing���`a
���`a
���`d    ���akcdef���`a ���bnfpcheck_collisions���`a(���bbpdself���`a,���`a ���`fbubble���`a,���`a ���`gbubbles���`a)���`a:���`a
���`h        ���`hdistance���`a ���aoa=���`a ���bbpdself���aoa.���`poutline_distance���`a(���`fbubble���`a,���`a ���`gbubbles���`a)���`a
���`h        ���akfreturn���`a ���bnbclen���`a(���`hdistance���`a[���`hdistance���`a ���aoa<���`a ���bmia0���`a]���`a)���`a
���`a
���`d    ���akcdef���`a ���bnfmcollides_with���`a(���bbpdself���`a,���`a ���`fbubble���`a,���`a ���`gbubbles���`a)���`a:���`a
���`h        ���`hdistance���`a ���aoa=���`a ���bbpdself���aoa.���`poutline_distance���`a(���`fbubble���`a,���`a ���`gbubbles���`a)���`a
���`h        ���`gidx_min���`a ���aoa=���`a ���`bnp���aoa.���`fargmin���`a(���`hdistance���`a)���`a
���`h        ���akfreturn���`a ���`gidx_min���`a ���akbif���`a ���bnbdtype���`a(���`gidx_min���`a)���`a ���aob==���`a ���`bnp���aoa.���`gndarray���`a ���akdelse���`a ���`a[���`gidx_min���`a]���`a
���`a
���`d    ���akcdef���`a ���bnfhcollapse���`a(���bbpdself���`a,���`a ���`ln_iterations���aoa=���bmib50���`a)���`a:���`a
���`h        ���bsdx�"""
        Move bubbles to the center of mass.

        Parameters
        ----------
        n_iterations : int, default: 50
            Number of moves to perform.
        """���`a
���`h        ���akcfor���`a ���`b_i���`a ���bowbin���`a ���bnberange���`a(���`ln_iterations���`a)���`a:���`a
���`l            ���`emoves���`a ���aoa=���`a ���bmia0���`a
���`l            ���akcfor���`a ���`ai���`a ���bowbin���`a ���bnberange���`a(���bnbclen���`a(���bbpdself���aoa.���`gbubbles���`a)���`a)���`a:���`a
���`p                ���`hrest_bub���`a ���aoa=���`a ���`bnp���aoa.���`fdelete���`a(���bbpdself���aoa.���`gbubbles���`a,���`a ���`ai���`a,���`a ���bmia0���`a)���`a
���`p                ���bc1x1# try to move directly towards the center of mass���`a
���`p                ���bc1x4# direction vector from bubble to the center of mass���`a
���`p                ���`gdir_vec���`a ���aoa=���`a ���bbpdself���aoa.���`ccom���`a ���aoa-���`a ���bbpdself���aoa.���`gbubbles���`a[���`ai���`a,���`a ���`a:���bmia2���`a]���`a
���`a
���`p                ���bc1x.# shorten direction vector to have length of 1���`a
���`p                ���`gdir_vec���`a ���aoa=���`a ���`gdir_vec���`a ���aoa/���`a ���`bnp���aoa.���`dsqrt���`a(���`gdir_vec���aoa.���`cdot���`a(���`gdir_vec���`a)���`a)���`a
���`a
���`p                ���bc1x# calculate new bubble position���`a
���`p                ���`inew_point���`a ���aoa=���`a ���bbpdself���aoa.���`gbubbles���`a[���`ai���`a,���`a ���`a:���bmia2���`a]���`a ���aoa+���`a ���`gdir_vec���`a ���aoa*���`a ���bbpdself���aoa.���`istep_dist���`a
���`p                ���`jnew_bubble���`a ���aoa=���`a ���`bnp���aoa.���`fappend���`a(���`inew_point���`a,���`a ���bbpdself���aoa.���`gbubbles���`a[���`ai���`a,���`a ���bmia2���`a:���bmia4���`a]���`a)���`a
���`a
���`p                ���bc1x6# check whether new bubble collides with other bubbles���`a
���`p                ���akbif���`a ���bowcnot���`a ���bbpdself���aoa.���`pcheck_collisions���`a(���`jnew_bubble���`a,���`a ���`hrest_bub���`a)���`a:���`a
���`t                    ���bbpdself���aoa.���`gbubbles���`a[���`ai���`a,���`a ���`a:���`a]���`a ���aoa=���`a ���`jnew_bubble���`a
���`t                    ���bbpdself���aoa.���`ccom���`a ���aoa=���`a ���bbpdself���aoa.���`ncenter_of_mass���`a(���`a)���`a
���`t                    ���`emoves���`a ���aoa+���aoa=���`a ���bmia1���`a
���`p                ���akdelse���`a:���`a
���`t                    ���bc1x3# try to move around a bubble that you collide with���`a
���`t                    ���bc1w# find colliding bubble���`a
���`t                    ���akcfor���`a ���`icolliding���`a ���bowbin���`a ���bbpdself���aoa.���`mcollides_with���`a(���`jnew_bubble���`a,���`a ���`hrest_bub���`a)���`a:���`a
���`x                        ���bc1x# calculate direction vector���`a
���`x                        ���`gdir_vec���`a ���aoa=���`a ���`hrest_bub���`a[���`icolliding���`a,���`a ���`a:���bmia2���`a]���`a ���aoa-���`a ���bbpdself���aoa.���`gbubbles���`a[���`ai���`a,���`a ���`a:���bmia2���`a]���`a
���`x                        ���`gdir_vec���`a ���aoa=���`a ���`gdir_vec���`a ���aoa/���`a ���`bnp���aoa.���`dsqrt���`a(���`gdir_vec���aoa.���`cdot���`a(���`gdir_vec���`a)���`a)���`a
���`x                        ���bc1x# calculate orthogonal vector���`a
���`x                        ���`dorth���`a ���aoa=���`a ���`bnp���aoa.���`earray���`a(���`a[���`gdir_vec���`a[���bmia1���`a]���`a,���`a ���aoa-���`gdir_vec���`a[���bmia0���`a]���`a]���`a)���`a
���`x                        ���bc1x# test which direction to go���`a
���`x                        ���`jnew_point1���`a ���aoa=���`a ���`a(���bbpdself���aoa.���`gbubbles���`a[���`ai���`a,���`a ���`a:���bmia2���`a]���`a ���aoa+���`a ���`dorth���`a ���aoa*���`a
���`x&                                      ���bbpdself���aoa.���`istep_dist���`a)���`a
���`x                        ���`jnew_point2���`a ���aoa=���`a ���`a(���bbpdself���aoa.���`gbubbles���`a[���`ai���`a,���`a ���`a:���bmia2���`a]���`a ���aoa-���`a ���`dorth���`a ���aoa*���`a
���`x&                                      ���bbpdself���aoa.���`istep_dist���`a)���`a
���`x                        ���`edist1���`a ���aoa=���`a ���bbpdself���aoa.���`ocenter_distance���`a(���`a
���`x                            ���bbpdself���aoa.���`ccom���`a,���`a ���`bnp���aoa.���`earray���`a(���`a[���`jnew_point1���`a]���`a)���`a)���`a
���`x                        ���`edist2���`a ���aoa=���`a ���bbpdself���aoa.���`ocenter_distance���`a(���`a
���`x                            ���bbpdself���aoa.���`ccom���`a,���`a ���`bnp���aoa.���`earray���`a(���`a[���`jnew_point2���`a]���`a)���`a)���`a
���`x                        ���`inew_point���`a ���aoa=���`a ���`jnew_point1���`a ���akbif���`a ���`edist1���`a ���aoa<���`a ���`edist2���`a ���akdelse���`a ���`jnew_point2���`a
���`x                        ���`jnew_bubble���`a ���aoa=���`a ���`bnp���aoa.���`fappend���`a(���`inew_point���`a,���`a ���bbpdself���aoa.���`gbubbles���`a[���`ai���`a,���`a ���bmia2���`a:���bmia4���`a]���`a)���`a
���`x                        ���akbif���`a ���bowcnot���`a ���bbpdself���aoa.���`pcheck_collisions���`a(���`jnew_bubble���`a,���`a ���`hrest_bub���`a)���`a:���`a
���`x                            ���bbpdself���aoa.���`gbubbles���`a[���`ai���`a,���`a ���`a:���`a]���`a ���aoa=���`a ���`jnew_bubble���`a
���`x                            ���bbpdself���aoa.���`ccom���`a ���aoa=���`a ���bbpdself���aoa.���`ncenter_of_mass���`a(���`a)���`a
���`a
���`l            ���akbif���`a ���`emoves���`a ���aoa/���`a ���bnbclen���`a(���bbpdself���aoa.���`gbubbles���`a)���`a ���aoa<���`a ���bmfc0.1���`a:���`a
���`p                ���bbpdself���aoa.���`istep_dist���`a ���aoa=���`a ���bbpdself���aoa.���`istep_dist���`a ���aoa/���`a ���bmia2���`a
���`a
���`d    ���akcdef���`a ���bnfdplot���`a(���bbpdself���`a,���`a ���`bax���`a,���`a ���`flabels���`a,���`a ���`fcolors���`a)���`a:���`a
���`h        ���bsdx�"""
        Draw the bubble plot.

        Parameters
        ----------
        ax : matplotlib.axes.Axes
        labels : list
            Labels of the bubbles.
        colors : list
            Colors of the bubbles.
        """���`a
���`h        ���akcfor���`a ���`ai���`a ���bowbin���`a ���bnberange���`a(���bnbclen���`a(���bbpdself���aoa.���`gbubbles���`a)���`a)���`a:���`a
���`l            ���`dcirc���`a ���aoa=���`a ���`cplt���aoa.���`fCircle���`a(���`a
���`p                ���bbpdself���aoa.���`gbubbles���`a[���`ai���`a,���`a ���`a:���bmia2���`a]���`a,���`a ���bbpdself���aoa.���`gbubbles���`a[���`ai���`a,���`a ���bmia2���`a]���`a,���`a ���`ecolor���aoa=���`fcolors���`a[���`ai���`a]���`a)���`a
���`l            ���`bax���aoa.���`iadd_patch���`a(���`dcirc���`a)���`a
���`l            ���`bax���aoa.���`dtext���`a(���aoa*���bbpdself���aoa.���`gbubbles���`a[���`ai���`a,���`a ���`a:���bmia2���`a]���`a,���`a ���`flabels���`a[���`ai���`a]���`a,���`a
���`t                    ���`shorizontalalignment���aoa=���bs1a'���bs1fcenter���bs1a'���`a,���`a ���`qverticalalignment���aoa=���bs1a'���bs1fcenter���bs1a'���`a)���`a
���`a
���`a
���`lbubble_chart���`a ���aoa=���`a ���`kBubbleChart���`a(���`darea���aoa=���`tbrowser_market_share���`a[���bs1a'���bs1lmarket_share���bs1a'���`a]���`a,���`a
���`x                           ���`nbubble_spacing���aoa=���bmfc0.1���`a)���`a
���`a
���`lbubble_chart���aoa.���`hcollapse���`a(���`a)���`a
���`a
���`cfig���`a,���`a ���`bax���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`jsubplot_kw���aoa=���bnbddict���`a(���`faspect���aoa=���bs2a"���bs2eequal���bs2a"���`a)���`a)���`a
���`lbubble_chart���aoa.���`dplot���`a(���`a
���`d    ���`bax���`a,���`a ���`tbrowser_market_share���`a[���bs1a'���bs1hbrowsers���bs1a'���`a]���`a,���`a ���`tbrowser_market_share���`a[���bs1a'���bs1ecolor���bs1a'���`a]���`a)���`a
���`bax���aoa.���`daxis���`a(���bs2a"���bs2coff���bs2a"���`a)���`a
���`bax���aoa.���`erelim���`a(���`a)���`a
���`bax���aoa.���`nautoscale_view���`a(���`a)���`a
���`bax���aoa.���`iset_title���`a(���bs1a'���bs1tBrowser market share���bs1a'���`a)���`a
���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
`dNone�