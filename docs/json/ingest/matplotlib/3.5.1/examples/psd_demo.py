������������bsdy'"""
========
Psd Demo
========

Plotting Power Spectral Density (PSD) in Matplotlib.

The PSD is a common plot in the field of signal processing. NumPy has
many useful libraries for computing a PSD. Below we demo a few examples
of how this can be accomplished and visualized with Matplotlib.
"""���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnndmlab���`a ���akbas���`a ���bnndmlab���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnhgridspec���`a ���akbas���`a ���bnnhgridspec���`a
���`a
���bc1x)# Fixing random state for reproducibility���`a
���`bnp���aoa.���`frandom���aoa.���`dseed���`a(���bmih19680801���`a)���`a
���`a
���`bdt���`a ���aoa=���`a ���bmfd0.01���`a
���`at���`a ���aoa=���`a ���`bnp���aoa.���`farange���`a(���bmia0���`a,���`a ���bmib10���`a,���`a ���`bdt���`a)���`a
���`cnse���`a ���aoa=���`a ���`bnp���aoa.���`frandom���aoa.���`erandn���`a(���bnbclen���`a(���`at���`a)���`a)���`a
���`ar���`a ���aoa=���`a ���`bnp���aoa.���`cexp���`a(���aoa-���`at���`a ���aoa/���`a ���bmfd0.05���`a)���`a
���`a
���`dcnse���`a ���aoa=���`a ���`bnp���aoa.���`hconvolve���`a(���`cnse���`a,���`a ���`ar���`a)���`a ���aoa*���`a ���`bdt���`a
���`dcnse���`a ���aoa=���`a ���`dcnse���`a[���`a:���bnbclen���`a(���`at���`a)���`a]���`a
���`as���`a ���aoa=���`a ���bmfc0.1���`a ���aoa*���`a ���`bnp���aoa.���`csin���`a(���bmia2���`a ���aoa*���`a ���`bnp���aoa.���`bpi���`a ���aoa*���`a ���`at���`a)���`a ���aoa+���`a ���`dcnse���`a
���`a
���`cfig���`a,���`a ���`a(���`cax0���`a,���`a ���`cax1���`a)���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���bmia2���`a,���`a ���bmia1���`a)���`a
���`cax0���aoa.���`dplot���`a(���`at���`a,���`a ���`as���`a)���`a
���`cax1���aoa.���`cpsd���`a(���`as���`a,���`a ���bmic512���`a,���`a ���bmia1���`a ���aoa/���`a ���`bdt���`a)���`a
���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
���`a
���bc1xO###############################################################################���`a
���bc1xM# Compare this with the equivalent Matlab code to accomplish the same thing::���`a
���bc1a#���`a
���bc1p#     dt = 0.01;���`a
���bc1t#     t = [0:dt:10];���`a
���bc1x#     nse = randn(size(t));���`a
���bc1w#     r = exp(-t/0.05);���`a
���bc1x#     cnse = conv(nse, r)*dt;���`a
���bc1x#     cnse = cnse(1:length(t));���`a
���bc1x!#     s = 0.1*sin(2*pi*t) + cnse;���`a
���bc1a#���`a
���bc1r#     subplot(211)���`a
���bc1p#     plot(t, s)���`a
���bc1r#     subplot(212)���`a
���bc1w#     psd(s, 512, 1/dt)���`a
���bc1a#���`a
���bc1xD# Below we'll show a slightly more complex example that demonstrates���`a
���bc1x(# how padding affects the resulting PSD.���`a
���`a
���`bdt���`a ���aoa=���`a ���`bnp���aoa.���`bpi���`a ���aoa/���`a ���bmfd100.���`a
���`bfs���`a ���aoa=���`a ���bmfb1.���`a ���aoa/���`a ���`bdt���`a
���`at���`a ���aoa=���`a ���`bnp���aoa.���`farange���`a(���bmia0���`a,���`a ���bmia8���`a,���`a ���`bdt���`a)���`a
���`ay���`a ���aoa=���`a ���bmfc10.���`a ���aoa*���`a ���`bnp���aoa.���`csin���`a(���bmia2���`a ���aoa*���`a ���`bnp���aoa.���`bpi���`a ���aoa*���`a ���bmia4���`a ���aoa*���`a ���`at���`a)���`a ���aoa+���`a ���bmfb5.���`a ���aoa*���`a ���`bnp���aoa.���`csin���`a(���bmia2���`a ���aoa*���`a ���`bnp���aoa.���`bpi���`a ���aoa*���`a ���bmfd4.25���`a ���aoa*���`a ���`at���`a)���`a
���`ay���`a ���aoa=���`a ���`ay���`a ���aoa+���`a ���`bnp���aoa.���`frandom���aoa.���`erandn���`a(���aoa*���`at���aoa.���`eshape���`a)���`a
���`a
���bc1x# Plot the raw time series���`a
���`cfig���`a ���aoa=���`a ���`cplt���aoa.���`ffigure���`a(���`rconstrained_layout���aoa=���bkcdTrue���`a)���`a
���`bgs���`a ���aoa=���`a ���`hgridspec���aoa.���`hGridSpec���`a(���bmia2���`a,���`a ���bmia3���`a,���`a ���`ffigure���aoa=���`cfig���`a)���`a
���`bax���`a ���aoa=���`a ���`cfig���aoa.���`kadd_subplot���`a(���`bgs���`a[���bmia0���`a,���`a ���`a:���`a]���`a)���`a
���`bax���aoa.���`dplot���`a(���`at���`a,���`a ���`ay���`a)���`a
���`bax���aoa.���`jset_xlabel���`a(���bs1a'���bs1htime [s]���bs1a'���`a)���`a
���`bax���aoa.���`jset_ylabel���`a(���bs1a'���bs1fsignal���bs1a'���`a)���`a
���`a
���bc1xK# Plot the PSD with different amounts of zero padding. This uses the entire���`a
���bc1u# time series at once���`a
���`cax2���`a ���aoa=���`a ���`cfig���aoa.���`kadd_subplot���`a(���`bgs���`a[���bmia1���`a,���`a ���bmia0���`a]���`a)���`a
���`cax2���aoa.���`cpsd���`a(���`ay���`a,���`a ���`dNFFT���aoa=���bnbclen���`a(���`at���`a)���`a,���`a ���`fpad_to���aoa=���bnbclen���`a(���`at���`a)���`a,���`a ���`bFs���aoa=���`bfs���`a)���`a
���`cax2���aoa.���`cpsd���`a(���`ay���`a,���`a ���`dNFFT���aoa=���bnbclen���`a(���`at���`a)���`a,���`a ���`fpad_to���aoa=���bnbclen���`a(���`at���`a)���`a ���aoa*���`a ���bmia2���`a,���`a ���`bFs���aoa=���`bfs���`a)���`a
���`cax2���aoa.���`cpsd���`a(���`ay���`a,���`a ���`dNFFT���aoa=���bnbclen���`a(���`at���`a)���`a,���`a ���`fpad_to���aoa=���bnbclen���`a(���`at���`a)���`a ���aoa*���`a ���bmia4���`a,���`a ���`bFs���aoa=���`bfs���`a)���`a
���`cax2���aoa.���`iset_title���`a(���bs1a'���bs1lzero padding���bs1a'���`a)���`a
���`a
���bc1xH# Plot the PSD with different block sizes, Zero pad to the length of the���`a
���bc1x# original data sequence.���`a
���`cax3���`a ���aoa=���`a ���`cfig���aoa.���`kadd_subplot���`a(���`bgs���`a[���bmia1���`a,���`a ���bmia1���`a]���`a,���`a ���`fsharex���aoa=���`cax2���`a,���`a ���`fsharey���aoa=���`cax2���`a)���`a
���`cax3���aoa.���`cpsd���`a(���`ay���`a,���`a ���`dNFFT���aoa=���bnbclen���`a(���`at���`a)���`a,���`a ���`fpad_to���aoa=���bnbclen���`a(���`at���`a)���`a,���`a ���`bFs���aoa=���`bfs���`a)���`a
���`cax3���aoa.���`cpsd���`a(���`ay���`a,���`a ���`dNFFT���aoa=���bnbclen���`a(���`at���`a)���`a ���aoa/���aoa/���`a ���bmia2���`a,���`a ���`fpad_to���aoa=���bnbclen���`a(���`at���`a)���`a,���`a ���`bFs���aoa=���`bfs���`a)���`a
���`cax3���aoa.���`cpsd���`a(���`ay���`a,���`a ���`dNFFT���aoa=���bnbclen���`a(���`at���`a)���`a ���aoa/���aoa/���`a ���bmia4���`a,���`a ���`fpad_to���aoa=���bnbclen���`a(���`at���`a)���`a,���`a ���`bFs���aoa=���`bfs���`a)���`a
���`cax3���aoa.���`jset_ylabel���`a(���bs1a'���bs1a'���`a)���`a
���`cax3���aoa.���`iset_title���`a(���bs1a'���bs1jblock size���bs1a'���`a)���`a
���`a
���bc1x?# Plot the PSD with different amounts of overlap between blocks���`a
���`cax4���`a ���aoa=���`a ���`cfig���aoa.���`kadd_subplot���`a(���`bgs���`a[���bmia1���`a,���`a ���bmia2���`a]���`a,���`a ���`fsharex���aoa=���`cax2���`a,���`a ���`fsharey���aoa=���`cax2���`a)���`a
���`cax4���aoa.���`cpsd���`a(���`ay���`a,���`a ���`dNFFT���aoa=���bnbclen���`a(���`at���`a)���`a ���aoa/���aoa/���`a ���bmia2���`a,���`a ���`fpad_to���aoa=���bnbclen���`a(���`at���`a)���`a,���`a ���`hnoverlap���aoa=���bmia0���`a,���`a ���`bFs���aoa=���`bfs���`a)���`a
���`cax4���aoa.���`cpsd���`a(���`ay���`a,���`a ���`dNFFT���aoa=���bnbclen���`a(���`at���`a)���`a ���aoa/���aoa/���`a ���bmia2���`a,���`a ���`fpad_to���aoa=���bnbclen���`a(���`at���`a)���`a,���`a
���`h        ���`hnoverlap���aoa=���bnbcint���`a(���bmfd0.05���`a ���aoa*���`a ���bnbclen���`a(���`at���`a)���`a ���aoa/���`a ���bmfb2.���`a)���`a,���`a ���`bFs���aoa=���`bfs���`a)���`a
���`cax4���aoa.���`cpsd���`a(���`ay���`a,���`a ���`dNFFT���aoa=���bnbclen���`a(���`at���`a)���`a ���aoa/���aoa/���`a ���bmia2���`a,���`a ���`fpad_to���aoa=���bnbclen���`a(���`at���`a)���`a,���`a
���`h        ���`hnoverlap���aoa=���bnbcint���`a(���bmfc0.2���`a ���aoa*���`a ���bnbclen���`a(���`at���`a)���`a ���aoa/���`a ���bmfb2.���`a)���`a,���`a ���`bFs���aoa=���`bfs���`a)���`a
���`cax4���aoa.���`jset_ylabel���`a(���bs1a'���bs1a'���`a)���`a
���`cax4���aoa.���`iset_title���`a(���bs1a'���bs1goverlap���bs1a'���`a)���`a
���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
���`a
���`a
���bc1xO###############################################################################���`a
���bc1x># This is a ported version of a MATLAB example from the signal���`a
���bc1xD# processing toolbox that showed some difference at one time between���`a
���bc1x/# Matplotlib's and MATLAB's scaling of the PSD.���`a
���`a
���`bfs���`a ���aoa=���`a ���bmid1000���`a
���`at���`a ���aoa=���`a ���`bnp���aoa.���`hlinspace���`a(���bmia0���`a,���`a ���bmfc0.3���`a,���`a ���bmic301���`a)���`a
���`aA���`a ���aoa=���`a ���`bnp���aoa.���`earray���`a(���`a[���bmia2���`a,���`a ���bmia8���`a]���`a)���aoa.���`greshape���`a(���aoa-���bmia1���`a,���`a ���bmia1���`a)���`a
���`af���`a ���aoa=���`a ���`bnp���aoa.���`earray���`a(���`a[���bmic150���`a,���`a ���bmic140���`a]���`a)���aoa.���`greshape���`a(���aoa-���bmia1���`a,���`a ���bmia1���`a)���`a
���`bxn���`a ���aoa=���`a ���`a(���`aA���`a ���aoa*���`a ���`bnp���aoa.���`csin���`a(���bmia2���`a ���aoa*���`a ���`bnp���aoa.���`bpi���`a ���aoa*���`a ���`af���`a ���aoa*���`a ���`at���`a)���`a)���aoa.���`csum���`a(���`daxis���aoa=���bmia0���`a)���`a
���`bxn���`a ���aoa+���aoa=���`a ���bmia5���`a ���aoa*���`a ���`bnp���aoa.���`frandom���aoa.���`erandn���`a(���aoa*���`at���aoa.���`eshape���`a)���`a
���`a
���`cfig���`a,���`a ���`a(���`cax0���`a,���`a ���`cax1���`a)���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`encols���aoa=���bmia2���`a,���`a ���`rconstrained_layout���aoa=���bkcdTrue���`a)���`a
���`a
���`fyticks���`a ���aoa=���`a ���`bnp���aoa.���`farange���`a(���aoa-���bmib50���`a,���`a ���bmib30���`a,���`a ���bmib10���`a)���`a
���`fyrange���`a ���aoa=���`a ���`a(���`fyticks���`a[���bmia0���`a]���`a,���`a ���`fyticks���`a[���aoa-���bmia1���`a]���`a)���`a
���`fxticks���`a ���aoa=���`a ���`bnp���aoa.���`farange���`a(���bmia0���`a,���`a ���bmic550���`a,���`a ���bmic100���`a)���`a
���`a
���`cax0���aoa.���`cpsd���`a(���`bxn���`a,���`a ���`dNFFT���aoa=���bmic301���`a,���`a ���`bFs���aoa=���`bfs���`a,���`a ���`fwindow���aoa=���`dmlab���aoa.���`kwindow_none���`a,���`a ���`fpad_to���aoa=���bmid1024���`a,���`a
���`h        ���`mscale_by_freq���aoa=���bkcdTrue���`a)���`a
���`cax0���aoa.���`iset_title���`a(���bs1a'���bs1kPeriodogram���bs1a'���`a)���`a
���`cax0���aoa.���`jset_yticks���`a(���`fyticks���`a)���`a
���`cax0���aoa.���`jset_xticks���`a(���`fxticks���`a)���`a
���`cax0���aoa.���`dgrid���`a(���bkcdTrue���`a)���`a
���`cax0���aoa.���`hset_ylim���`a(���`fyrange���`a)���`a
���`a
���`cax1���aoa.���`cpsd���`a(���`bxn���`a,���`a ���`dNFFT���aoa=���bmic150���`a,���`a ���`bFs���aoa=���`bfs���`a,���`a ���`fwindow���aoa=���`dmlab���aoa.���`kwindow_none���`a,���`a ���`fpad_to���aoa=���bmic512���`a,���`a ���`hnoverlap���aoa=���bmib75���`a,���`a
���`h        ���`mscale_by_freq���aoa=���bkcdTrue���`a)���`a
���`cax1���aoa.���`iset_title���`a(���bs1a'���bs1eWelch���bs1a'���`a)���`a
���`cax1���aoa.���`jset_xticks���`a(���`fxticks���`a)���`a
���`cax1���aoa.���`jset_yticks���`a(���`fyticks���`a)���`a
���`cax1���aoa.���`jset_ylabel���`a(���bs1a'���bs1a'���`a)���`b  ���bc1x&# overwrite the y-label added by `psd`���`a
���`cax1���aoa.���`dgrid���`a(���bkcdTrue���`a)���`a
���`cax1���aoa.���`hset_ylim���`a(���`fyrange���`a)���`a
���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
���`a
���bc1xO###############################################################################���`a
���bc1x># This is a ported version of a MATLAB example from the signal���`a
���bc1xD# processing toolbox that showed some difference at one time between���`a
���bc1x/# Matplotlib's and MATLAB's scaling of the PSD.���`a
���bc1a#���`a
���bc1xJ# It uses a complex signal so we can see that complex PSD's work properly.���`a
���`a
���`dprng���`a ���aoa=���`a ���`bnp���aoa.���`frandom���aoa.���`kRandomState���`a(���bmih19680801���`a)���`b  ���bc1x# to ensure reproducibility���`a
���`a
���`bfs���`a ���aoa=���`a ���bmid1000���`a
���`at���`a ���aoa=���`a ���`bnp���aoa.���`hlinspace���`a(���bmia0���`a,���`a ���bmfc0.3���`a,���`a ���bmic301���`a)���`a
���`aA���`a ���aoa=���`a ���`bnp���aoa.���`earray���`a(���`a[���bmia2���`a,���`a ���bmia8���`a]���`a)���aoa.���`greshape���`a(���aoa-���bmia1���`a,���`a ���bmia1���`a)���`a
���`af���`a ���aoa=���`a ���`bnp���aoa.���`earray���`a(���`a[���bmic150���`a,���`a ���bmic140���`a]���`a)���aoa.���`greshape���`a(���aoa-���bmia1���`a,���`a ���bmia1���`a)���`a
���`bxn���`a ���aoa=���`a ���`a(���`aA���`a ���aoa*���`a ���`bnp���aoa.���`cexp���`a(���bmia2���`aj���`a ���aoa*���`a ���`bnp���aoa.���`bpi���`a ���aoa*���`a ���`af���`a ���aoa*���`a ���`at���`a)���`a)���aoa.���`csum���`a(���`daxis���aoa=���bmia0���`a)���`a ���aoa+���`a ���bmia5���`a ���aoa*���`a ���`dprng���aoa.���`erandn���`a(���aoa*���`at���aoa.���`eshape���`a)���`a
���`a
���`cfig���`a,���`a ���`a(���`cax0���`a,���`a ���`cax1���`a)���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`encols���aoa=���bmia2���`a,���`a ���`rconstrained_layout���aoa=���bkcdTrue���`a)���`a
���`a
���`fyticks���`a ���aoa=���`a ���`bnp���aoa.���`farange���`a(���aoa-���bmib50���`a,���`a ���bmib30���`a,���`a ���bmib10���`a)���`a
���`fyrange���`a ���aoa=���`a ���`a(���`fyticks���`a[���bmia0���`a]���`a,���`a ���`fyticks���`a[���aoa-���bmia1���`a]���`a)���`a
���`fxticks���`a ���aoa=���`a ���`bnp���aoa.���`farange���`a(���aoa-���bmic500���`a,���`a ���bmic550���`a,���`a ���bmic200���`a)���`a
���`a
���`cax0���aoa.���`cpsd���`a(���`bxn���`a,���`a ���`dNFFT���aoa=���bmic301���`a,���`a ���`bFs���aoa=���`bfs���`a,���`a ���`fwindow���aoa=���`dmlab���aoa.���`kwindow_none���`a,���`a ���`fpad_to���aoa=���bmid1024���`a,���`a
���`h        ���`mscale_by_freq���aoa=���bkcdTrue���`a)���`a
���`cax0���aoa.���`iset_title���`a(���bs1a'���bs1kPeriodogram���bs1a'���`a)���`a
���`cax0���aoa.���`jset_yticks���`a(���`fyticks���`a)���`a
���`cax0���aoa.���`jset_xticks���`a(���`fxticks���`a)���`a
���`cax0���aoa.���`dgrid���`a(���bkcdTrue���`a)���`a
���`cax0���aoa.���`hset_ylim���`a(���`fyrange���`a)���`a
���`a
���`cax1���aoa.���`cpsd���`a(���`bxn���`a,���`a ���`dNFFT���aoa=���bmic150���`a,���`a ���`bFs���aoa=���`bfs���`a,���`a ���`fwindow���aoa=���`dmlab���aoa.���`kwindow_none���`a,���`a ���`fpad_to���aoa=���bmic512���`a,���`a ���`hnoverlap���aoa=���bmib75���`a,���`a
���`h        ���`mscale_by_freq���aoa=���bkcdTrue���`a)���`a
���`cax1���aoa.���`iset_title���`a(���bs1a'���bs1eWelch���bs1a'���`a)���`a
���`cax1���aoa.���`jset_xticks���`a(���`fxticks���`a)���`a
���`cax1���aoa.���`jset_yticks���`a(���`fyticks���`a)���`a
���`cax1���aoa.���`jset_ylabel���`a(���bs1a'���bs1a'���`a)���`b  ���bc1x&# overwrite the y-label added by `psd`���`a
���`cax1���aoa.���`dgrid���`a(���bkcdTrue���`a)���`a
���`cax1���aoa.���`hset_ylim���`a(���`fyrange���`a)���`a
���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
`dNone�