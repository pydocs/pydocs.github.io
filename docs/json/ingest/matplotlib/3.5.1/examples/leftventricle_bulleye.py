��������d���bsdx�"""
=======================
Left ventricle bullseye
=======================

This example demonstrates how to create the 17 segment model for the left
ventricle recommended by the American Heart Association (AHA).
"""���`a
���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����`a ���akbas���`a ���bnncmpl���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���`a
���`a
���akcdef���`a ���bnfmbullseye_plot���`a(���`bax���`a,���`a ���`ddata���`a,���`a ���`hseg_bold���aoa=���bkcdNone���`a,���`a ���`dcmap���aoa=���bkcdNone���`a,���`a ���`dnorm���aoa=���bkcdNone���`a)���`a:���`a
���`d    ���bsdy�"""
    Bullseye representation for the left ventricle.

    Parameters
    ----------
    ax : axes
    data : list of int and float
        The intensity values for each of the 17 segments
    seg_bold : list of int, optional
        A list with the segments to highlight
    cmap : ColorMap or None, optional
        Optional argument to set the desired colormap
    norm : Normalize or None, optional
        Optional argument to normalize data into the [0.0, 1.0] range

    Notes
    -----
    This function creates the 17 segment model for the left ventricle according
    to the American Heart Association (AHA) [1]_

    References
    ----------
    .. [1] M. D. Cerqueira, N. J. Weissman, V. Dilsizian, A. K. Jacobs,
        S. Kaul, W. K. Laskey, D. J. Pennell, J. A. Rumberger, T. Ryan,
        and M. S. Verani, "Standardized myocardial segmentation and
        nomenclature for tomographic imaging of the heart",
        Circulation, vol. 105, no. 4, pp. 539-542, 2002.
    """���`a
���`d    ���akbif���`a ���`hseg_bold���`a ���bowbis���`a ���bkcdNone���`a:���`a
���`h        ���`hseg_bold���`a ���aoa=���`a ���`a[���`a]���`a
���`a
���`d    ���`ilinewidth���`a ���aoa=���`a ���bmia2���`a
���`d    ���`ddata���`a ���aoa=���`a ���`bnp���aoa.���`eravel���`a(���`ddata���`a)���`a
���`a
���`d    ���akbif���`a ���`dcmap���`a ���bowbis���`a ���bkcdNone���`a:���`a
���`h        ���`dcmap���`a ���aoa=���`a ���`cplt���aoa.���`bcm���aoa.���`gviridis���`a
���`a
���`d    ���akbif���`a ���`dnorm���`a ���bowbis���`a ���bkcdNone���`a:���`a
���`h        ���`dnorm���`a ���aoa=���`a ���`cmpl���aoa.���`fcolors���aoa.���`iNormalize���`a(���`dvmin���aoa=���`ddata���aoa.���`cmin���`a(���`a)���`a,���`a ���`dvmax���aoa=���`ddata���aoa.���`cmax���`a(���`a)���`a)���`a
���`a
���`d    ���`etheta���`a ���aoa=���`a ���`bnp���aoa.���`hlinspace���`a(���bmia0���`a,���`a ���bmia2���`a ���aoa*���`a ���`bnp���aoa.���`bpi���`a,���`a ���bmic768���`a)���`a
���`d    ���`ar���`a ���aoa=���`a ���`bnp���aoa.���`hlinspace���`a(���bmfc0.2���`a,���`a ���bmia1���`a,���`a ���bmia4���`a)���`a
���`a
���`d    ���bc1x%# Create the bound for the segment 17���`a
���`d    ���akcfor���`a ���`ai���`a ���bowbin���`a ���bnberange���`a(���`ar���aoa.���`eshape���`a[���bmia0���`a]���`a)���`a:���`a
���`h        ���`bax���aoa.���`dplot���`a(���`etheta���`a,���`a ���`bnp���aoa.���`frepeat���`a(���`ar���`a[���`ai���`a]���`a,���`a ���`etheta���aoa.���`eshape���`a)���`a,���`a ���bs1a'���bs1b-k���bs1a'���`a,���`a ���`blw���aoa=���`ilinewidth���`a)���`a
���`a
���`d    ���bc1x)# Create the bounds for the segments 1-12���`a
���`d    ���akcfor���`a ���`ai���`a ���bowbin���`a ���bnberange���`a(���bmia6���`a)���`a:���`a
���`h        ���`gtheta_i���`a ���aoa=���`a ���`bnp���aoa.���`gdeg2rad���`a(���`ai���`a ���aoa*���`a ���bmib60���`a)���`a
���`h        ���`bax���aoa.���`dplot���`a(���`a[���`gtheta_i���`a,���`a ���`gtheta_i���`a]���`a,���`a ���`a[���`ar���`a[���bmia1���`a]���`a,���`a ���bmia1���`a]���`a,���`a ���bs1a'���bs1b-k���bs1a'���`a,���`a ���`blw���aoa=���`ilinewidth���`a)���`a
���`a
���`d    ���bc1x*# Create the bounds for the segments 13-16���`a
���`d    ���akcfor���`a ���`ai���`a ���bowbin���`a ���bnberange���`a(���bmia4���`a)���`a:���`a
���`h        ���`gtheta_i���`a ���aoa=���`a ���`bnp���aoa.���`gdeg2rad���`a(���`ai���`a ���aoa*���`a ���bmib90���`a ���aoa-���`a ���bmib45���`a)���`a
���`h        ���`bax���aoa.���`dplot���`a(���`a[���`gtheta_i���`a,���`a ���`gtheta_i���`a]���`a,���`a ���`a[���`ar���`a[���bmia0���`a]���`a,���`a ���`ar���`a[���bmia1���`a]���`a]���`a,���`a ���bs1a'���bs1b-k���bs1a'���`a,���`a ���`blw���aoa=���`ilinewidth���`a)���`a
���`a
���`d    ���bc1w# Fill the segments 1-6���`a
���`d    ���`br0���`a ���aoa=���`a ���`ar���`a[���bmia2���`a:���bmia4���`a]���`a
���`d    ���`br0���`a ���aoa=���`a ���`bnp���aoa.���`frepeat���`a(���`br0���`a[���`a:���`a,���`a ���`bnp���aoa.���`gnewaxis���`a]���`a,���`a ���bmic128���`a,���`a ���`daxis���aoa=���bmia1���`a)���aoa.���`aT���`a
���`d    ���akcfor���`a ���`ai���`a ���bowbin���`a ���bnberange���`a(���bmia6���`a)���`a:���`a
���`h        ���bc1x## First segment start at 60 degrees���`a
���`h        ���`ftheta0���`a ���aoa=���`a ���`etheta���`a[���`ai���`a ���aoa*���`a ���bmic128���`a:���`ai���`a ���aoa*���`a ���bmic128���`a ���aoa+���`a ���bmic128���`a]���`a ���aoa+���`a ���`bnp���aoa.���`gdeg2rad���`a(���bmib60���`a)���`a
���`h        ���`ftheta0���`a ���aoa=���`a ���`bnp���aoa.���`frepeat���`a(���`ftheta0���`a[���`a:���`a,���`a ���`bnp���aoa.���`gnewaxis���`a]���`a,���`a ���bmia2���`a,���`a ���`daxis���aoa=���bmia1���`a)���`a
���`h        ���`az���`a ���aoa=���`a ���`bnp���aoa.���`dones���`a(���`a(���bmic128���`a,���`a ���bmia2���`a)���`a)���`a ���aoa*���`a ���`ddata���`a[���`ai���`a]���`a
���`h        ���`bax���aoa.���`jpcolormesh���`a(���`ftheta0���`a,���`a ���`br0���`a,���`a ���`az���`a,���`a ���`dcmap���aoa=���`dcmap���`a,���`a ���`dnorm���aoa=���`dnorm���`a,���`a ���`gshading���aoa=���bs1a'���bs1dauto���bs1a'���`a)���`a
���`h        ���akbif���`a ���`ai���`a ���aoa+���`a ���bmia1���`a ���bowbin���`a ���`hseg_bold���`a:���`a
���`l            ���`bax���aoa.���`dplot���`a(���`ftheta0���`a,���`a ���`br0���`a,���`a ���bs1a'���bs1b-k���bs1a'���`a,���`a ���`blw���aoa=���`ilinewidth���`a ���aoa+���`a ���bmia2���`a)���`a
���`l            ���`bax���aoa.���`dplot���`a(���`ftheta0���`a[���bmia0���`a]���`a,���`a ���`a[���`ar���`a[���bmia2���`a]���`a,���`a ���`ar���`a[���bmia3���`a]���`a]���`a,���`a ���bs1a'���bs1b-k���bs1a'���`a,���`a ���`blw���aoa=���`ilinewidth���`a ���aoa+���`a ���bmia1���`a)���`a
���`l            ���`bax���aoa.���`dplot���`a(���`ftheta0���`a[���aoa-���bmia1���`a]���`a,���`a ���`a[���`ar���`a[���bmia2���`a]���`a,���`a ���`ar���`a[���bmia3���`a]���`a]���`a,���`a ���bs1a'���bs1b-k���bs1a'���`a,���`a ���`blw���aoa=���`ilinewidth���`a ���aoa+���`a ���bmia1���`a)���`a
���`a
���`d    ���bc1x# Fill the segments 7-12���`a
���`d    ���`br0���`a ���aoa=���`a ���`ar���`a[���bmia1���`a:���bmia3���`a]���`a
���`d    ���`br0���`a ���aoa=���`a ���`bnp���aoa.���`frepeat���`a(���`br0���`a[���`a:���`a,���`a ���`bnp���aoa.���`gnewaxis���`a]���`a,���`a ���bmic128���`a,���`a ���`daxis���aoa=���bmia1���`a)���aoa.���`aT���`a
���`d    ���akcfor���`a ���`ai���`a ���bowbin���`a ���bnberange���`a(���bmia6���`a)���`a:���`a
���`h        ���bc1x## First segment start at 60 degrees���`a
���`h        ���`ftheta0���`a ���aoa=���`a ���`etheta���`a[���`ai���`a ���aoa*���`a ���bmic128���`a:���`ai���`a ���aoa*���`a ���bmic128���`a ���aoa+���`a ���bmic128���`a]���`a ���aoa+���`a ���`bnp���aoa.���`gdeg2rad���`a(���bmib60���`a)���`a
���`h        ���`ftheta0���`a ���aoa=���`a ���`bnp���aoa.���`frepeat���`a(���`ftheta0���`a[���`a:���`a,���`a ���`bnp���aoa.���`gnewaxis���`a]���`a,���`a ���bmia2���`a,���`a ���`daxis���aoa=���bmia1���`a)���`a
���`h        ���`az���`a ���aoa=���`a ���`bnp���aoa.���`dones���`a(���`a(���bmic128���`a,���`a ���bmia2���`a)���`a)���`a ���aoa*���`a ���`ddata���`a[���`ai���`a ���aoa+���`a ���bmia6���`a]���`a
���`h        ���`bax���aoa.���`jpcolormesh���`a(���`ftheta0���`a,���`a ���`br0���`a,���`a ���`az���`a,���`a ���`dcmap���aoa=���`dcmap���`a,���`a ���`dnorm���aoa=���`dnorm���`a,���`a ���`gshading���aoa=���bs1a'���bs1dauto���bs1a'���`a)���`a
���`h        ���akbif���`a ���`ai���`a ���aoa+���`a ���bmia7���`a ���bowbin���`a ���`hseg_bold���`a:���`a
���`l            ���`bax���aoa.���`dplot���`a(���`ftheta0���`a,���`a ���`br0���`a,���`a ���bs1a'���bs1b-k���bs1a'���`a,���`a ���`blw���aoa=���`ilinewidth���`a ���aoa+���`a ���bmia2���`a)���`a
���`l            ���`bax���aoa.���`dplot���`a(���`ftheta0���`a[���bmia0���`a]���`a,���`a ���`a[���`ar���`a[���bmia1���`a]���`a,���`a ���`ar���`a[���bmia2���`a]���`a]���`a,���`a ���bs1a'���bs1b-k���bs1a'���`a,���`a ���`blw���aoa=���`ilinewidth���`a ���aoa+���`a ���bmia1���`a)���`a
���`l            ���`bax���aoa.���`dplot���`a(���`ftheta0���`a[���aoa-���bmia1���`a]���`a,���`a ���`a[���`ar���`a[���bmia1���`a]���`a,���`a ���`ar���`a[���bmia2���`a]���`a]���`a,���`a ���bs1a'���bs1b-k���bs1a'���`a,���`a ���`blw���aoa=���`ilinewidth���`a ���aoa+���`a ���bmia1���`a)���`a
���`a
���`d    ���bc1x# Fill the segments 13-16���`a
���`d    ���`br0���`a ���aoa=���`a ���`ar���`a[���bmia0���`a:���bmia2���`a]���`a
���`d    ���`br0���`a ���aoa=���`a ���`bnp���aoa.���`frepeat���`a(���`br0���`a[���`a:���`a,���`a ���`bnp���aoa.���`gnewaxis���`a]���`a,���`a ���bmic192���`a,���`a ���`daxis���aoa=���bmia1���`a)���aoa.���`aT���`a
���`d    ���akcfor���`a ���`ai���`a ���bowbin���`a ���bnberange���`a(���bmia4���`a)���`a:���`a
���`h        ���bc1x## First segment start at 45 degrees���`a
���`h        ���`ftheta0���`a ���aoa=���`a ���`etheta���`a[���`ai���`a ���aoa*���`a ���bmic192���`a:���`ai���`a ���aoa*���`a ���bmic192���`a ���aoa+���`a ���bmic192���`a]���`a ���aoa+���`a ���`bnp���aoa.���`gdeg2rad���`a(���bmib45���`a)���`a
���`h        ���`ftheta0���`a ���aoa=���`a ���`bnp���aoa.���`frepeat���`a(���`ftheta0���`a[���`a:���`a,���`a ���`bnp���aoa.���`gnewaxis���`a]���`a,���`a ���bmia2���`a,���`a ���`daxis���aoa=���bmia1���`a)���`a
���`h        ���`az���`a ���aoa=���`a ���`bnp���aoa.���`dones���`a(���`a(���bmic192���`a,���`a ���bmia2���`a)���`a)���`a ���aoa*���`a ���`ddata���`a[���`ai���`a ���aoa+���`a ���bmib12���`a]���`a
���`h        ���`bax���aoa.���`jpcolormesh���`a(���`ftheta0���`a,���`a ���`br0���`a,���`a ���`az���`a,���`a ���`dcmap���aoa=���`dcmap���`a,���`a ���`dnorm���aoa=���`dnorm���`a,���`a ���`gshading���aoa=���bs1a'���bs1dauto���bs1a'���`a)���`a
���`h        ���akbif���`a ���`ai���`a ���aoa+���`a ���bmib13���`a ���bowbin���`a ���`hseg_bold���`a:���`a
���`l            ���`bax���aoa.���`dplot���`a(���`ftheta0���`a,���`a ���`br0���`a,���`a ���bs1a'���bs1b-k���bs1a'���`a,���`a ���`blw���aoa=���`ilinewidth���`a ���aoa+���`a ���bmia2���`a)���`a
���`l            ���`bax���aoa.���`dplot���`a(���`ftheta0���`a[���bmia0���`a]���`a,���`a ���`a[���`ar���`a[���bmia0���`a]���`a,���`a ���`ar���`a[���bmia1���`a]���`a]���`a,���`a ���bs1a'���bs1b-k���bs1a'���`a,���`a ���`blw���aoa=���`ilinewidth���`a ���aoa+���`a ���bmia1���`a)���`a
���`l            ���`bax���aoa.���`dplot���`a(���`ftheta0���`a[���aoa-���bmia1���`a]���`a,���`a ���`a[���`ar���`a[���bmia0���`a]���`a,���`a ���`ar���`a[���bmia1���`a]���`a]���`a,���`a ���bs1a'���bs1b-k���bs1a'���`a,���`a ���`blw���aoa=���`ilinewidth���`a ���aoa+���`a ���bmia1���`a)���`a
���`a
���`d    ���bc1v# Fill the segments 17���`a
���`d    ���akbif���`a ���`ddata���aoa.���`dsize���`a ���aob==���`a ���bmib17���`a:���`a
���`h        ���`br0���`a ���aoa=���`a ���`bnp���aoa.���`earray���`a(���`a[���bmia0���`a,���`a ���`ar���`a[���bmia0���`a]���`a]���`a)���`a
���`h        ���`br0���`a ���aoa=���`a ���`bnp���aoa.���`frepeat���`a(���`br0���`a[���`a:���`a,���`a ���`bnp���aoa.���`gnewaxis���`a]���`a,���`a ���`etheta���aoa.���`dsize���`a,���`a ���`daxis���aoa=���bmia1���`a)���aoa.���`aT���`a
���`h        ���`ftheta0���`a ���aoa=���`a ���`bnp���aoa.���`frepeat���`a(���`etheta���`a[���`a:���`a,���`a ���`bnp���aoa.���`gnewaxis���`a]���`a,���`a ���bmia2���`a,���`a ���`daxis���aoa=���bmia1���`a)���`a
���`h        ���`az���`a ���aoa=���`a ���`bnp���aoa.���`dones���`a(���`a(���`etheta���aoa.���`dsize���`a,���`a ���bmia2���`a)���`a)���`a ���aoa*���`a ���`ddata���`a[���bmib16���`a]���`a
���`h        ���`bax���aoa.���`jpcolormesh���`a(���`ftheta0���`a,���`a ���`br0���`a,���`a ���`az���`a,���`a ���`dcmap���aoa=���`dcmap���`a,���`a ���`dnorm���aoa=���`dnorm���`a,���`a ���`gshading���aoa=���bs1a'���bs1dauto���bs1a'���`a)���`a
���`h        ���akbif���`a ���bmib17���`a ���bowbin���`a ���`hseg_bold���`a:���`a
���`l            ���`bax���aoa.���`dplot���`a(���`ftheta0���`a,���`a ���`br0���`a,���`a ���bs1a'���bs1b-k���bs1a'���`a,���`a ���`blw���aoa=���`ilinewidth���`a ���aoa+���`a ���bmia2���`a)���`a
���`a
���`d    ���`bax���aoa.���`hset_ylim���`a(���`a[���bmia0���`a,���`a ���bmia1���`a]���`a)���`a
���`d    ���`bax���aoa.���`oset_yticklabels���`a(���`a[���`a]���`a)���`a
���`d    ���`bax���aoa.���`oset_xticklabels���`a(���`a[���`a]���`a)���`a
���`a
���`a
���bc1v# Create the fake data���`a
���`ddata���`a ���aoa=���`a ���`bnp���aoa.���`farange���`a(���bmib17���`a)���`a ���aoa+���`a ���bmia1���`a
���`a
���`a
���bc1x4# Make a figure and axes with dimensions as desired.���`a
���`cfig���`a,���`a ���`bax���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`gfigsize���aoa=���`a(���bmib12���`a,���`a ���bmia8���`a)���`a,���`a ���`enrows���aoa=���bmia1���`a,���`a ���`encols���aoa=���bmia3���`a,���`a
���`w                       ���`jsubplot_kw���aoa=���bnbddict���`a(���`jprojection���aoa=���bs1a'���bs1epolar���bs1a'���`a)���`a)���`a
���`cfig���aoa.���`fcanvas���aoa.���`gmanager���aoa.���`pset_window_title���`a(���bs1a'���bs1xLeft Ventricle Bulls Eyes (AHA)���bs1a'���`a)���`a
���`a
���bc1x## Create the axis for the colorbars���`a
���`caxl���`a ���aoa=���`a ���`cfig���aoa.���`hadd_axes���`a(���`a[���bmfd0.14���`a,���`a ���bmfd0.15���`a,���`a ���bmfc0.2���`a,���`a ���bmfd0.05���`a]���`a)���`a
���`daxl2���`a ���aoa=���`a ���`cfig���aoa.���`hadd_axes���`a(���`a[���bmfd0.41���`a,���`a ���bmfd0.15���`a,���`a ���bmfc0.2���`a,���`a ���bmfd0.05���`a]���`a)���`a
���`daxl3���`a ���aoa=���`a ���`cfig���aoa.���`hadd_axes���`a(���`a[���bmfd0.69���`a,���`a ���bmfd0.15���`a,���`a ���bmfc0.2���`a,���`a ���bmfd0.05���`a]���`a)���`a
���`a
���`a
���bc1x?# Set the colormap and norm to correspond to the data for which���`a
���bc1x# the colorbar will be used.���`a
���`dcmap���`a ���aoa=���`a ���`cmpl���aoa.���`bcm���aoa.���`gviridis���`a
���`dnorm���`a ���aoa=���`a ���`cmpl���aoa.���`fcolors���aoa.���`iNormalize���`a(���`dvmin���aoa=���bmia1���`a,���`a ���`dvmax���aoa=���bmib17���`a)���`a
���bc1xI# Create an empty ScalarMappable to set the colorbar's colormap and norm.���`a
���bc1xH# The following gives a basic continuous colorbar with ticks and labels.���`a
���`cfig���aoa.���`hcolorbar���`a(���`cmpl���aoa.���`bcm���aoa.���`nScalarMappable���`a(���`dcmap���aoa=���`dcmap���`a,���`a ���`dnorm���aoa=���`dnorm���`a)���`a,���`a
���`m             ���`ccax���aoa=���`caxl���`a,���`a ���`korientation���aoa=���bs1a'���bs1jhorizontal���bs1a'���`a,���`a ���`elabel���aoa=���bs1a'���bs1jSome Units���bs1a'���`a)���`a
���`a
���`a
���bc1x$# And again for the second colorbar.���`a
���`ecmap2���`a ���aoa=���`a ���`cmpl���aoa.���`bcm���aoa.���`dcool���`a
���`enorm2���`a ���aoa=���`a ���`cmpl���aoa.���`fcolors���aoa.���`iNormalize���`a(���`dvmin���aoa=���bmia1���`a,���`a ���`dvmax���aoa=���bmib17���`a)���`a
���`cfig���aoa.���`hcolorbar���`a(���`cmpl���aoa.���`bcm���aoa.���`nScalarMappable���`a(���`dcmap���aoa=���`ecmap2���`a,���`a ���`dnorm���aoa=���`enorm2���`a)���`a,���`a
���`m             ���`ccax���aoa=���`daxl2���`a,���`a ���`korientation���aoa=���bs1a'���bs1jhorizontal���bs1a'���`a,���`a ���`elabel���aoa=���bs1a'���bs1pSome other units���bs1a'���`a)���`a
���`a
���`a
���bc1x?# The second example illustrates the use of a ListedColormap, a���`a
���bc1x@# BoundaryNorm, and extended ends to show the "over" and "under"���`a
���bc1o# value colors.���`a
���`ecmap3���`a ���aoa=���`a ���`a(���`cmpl���aoa.���`fcolors���aoa.���`nListedColormap���`a(���`a[���bs1a'���bs1ar���bs1a'���`a,���`a ���bs1a'���bs1ag���bs1a'���`a,���`a ���bs1a'���bs1ab���bs1a'���`a,���`a ���bs1a'���bs1ac���bs1a'���`a]���`a)���`a
���`i         ���aoa.���`mwith_extremes���`a(���`dover���aoa=���bs1a'���bs1d0.35���bs1a'���`a,���`a ���`eunder���aoa=���bs1a'���bs1d0.75���bs1a'���`a)���`a)���`a
���bc1xE# If a ListedColormap is used, the length of the bounds array must be���`a
���bc1xD# one greater than the length of the color list.  The bounds must be���`a
���bc1x# monotonically increasing.���`a
���`fbounds���`a ���aoa=���`a ���`a[���bmia2���`a,���`a ���bmia3���`a,���`a ���bmia7���`a,���`a ���bmia9���`a,���`a ���bmib15���`a]���`a
���`enorm3���`a ���aoa=���`a ���`cmpl���aoa.���`fcolors���aoa.���`lBoundaryNorm���`a(���`fbounds���`a,���`a ���`ecmap3���aoa.���`aN���`a)���`a
���`cfig���aoa.���`hcolorbar���`a(���`cmpl���aoa.���`bcm���aoa.���`nScalarMappable���`a(���`dcmap���aoa=���`ecmap3���`a,���`a ���`dnorm���aoa=���`enorm3���`a)���`a,���`a
���`m             ���`ccax���aoa=���`daxl3���`a,���`a
���`m             ���bc1x9# to use 'extend', you must specify two extra boundaries:���`a
���`m             ���`jboundaries���aoa=���`a[���bmia0���`a]���`a ���aoa+���`a ���`fbounds���`a ���aoa+���`a ���`a[���bmib18���`a]���`a,���`a
���`m             ���`fextend���aoa=���bs1a'���bs1dboth���bs1a'���`a,���`a
���`m             ���`eticks���aoa=���`fbounds���`a,���`b  ���bc1j# optional���`a
���`m             ���`gspacing���aoa=���bs1a'���bs1lproportional���bs1a'���`a,���`a
���`m             ���`korientation���aoa=���bs1a'���bs1jhorizontal���bs1a'���`a,���`a
���`m             ���`elabel���aoa=���bs1a'���bs1x$Discrete intervals, some other units���bs1a'���`a)���`a
���`a
���`a
���bc1x# Create the 17 segment model���`a
���`mbullseye_plot���`a(���`bax���`a[���bmia0���`a]���`a,���`a ���`ddata���`a,���`a ���`dcmap���aoa=���`dcmap���`a,���`a ���`dnorm���aoa=���`dnorm���`a)���`a
���`bax���`a[���bmia0���`a]���aoa.���`iset_title���`a(���bs1a'���bs1oBulls Eye (AHA)���bs1a'���`a)���`a
���`a
���`mbullseye_plot���`a(���`bax���`a[���bmia1���`a]���`a,���`a ���`ddata���`a,���`a ���`dcmap���aoa=���`ecmap2���`a,���`a ���`dnorm���aoa=���`enorm2���`a)���`a
���`bax���`a[���bmia1���`a]���aoa.���`iset_title���`a(���bs1a'���bs1oBulls Eye (AHA)���bs1a'���`a)���`a
���`a
���`mbullseye_plot���`a(���`bax���`a[���bmia2���`a]���`a,���`a ���`ddata���`a,���`a ���`hseg_bold���aoa=���`a[���bmia3���`a,���`a ���bmia5���`a,���`a ���bmia6���`a,���`a ���bmib11���`a,���`a ���bmib12���`a,���`a ���bmib16���`a]���`a,���`a
���`n              ���`dcmap���aoa=���`ecmap3���`a,���`a ���`dnorm���aoa=���`enorm3���`a)���`a
���`bax���`a[���bmia2���`a]���aoa.���`iset_title���`a(���bs1a'���bs1x&Segments [3, 5, 6, 11, 12, 16] in bold���bs1a'���`a)���`a
���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
`dNone�