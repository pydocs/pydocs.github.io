������������bsdyb"""
=====================
Fixing too many ticks
=====================

One common cause for unexpected tick behavior is passing a list of strings
instead of numbers or datetime objects. This can easily happen without notice
when reading in a comma-delimited text file. Matplotlib treats lists of strings
as *categorical* variables
(:doc:`/gallery/lines_bars_and_markers/categorical_variables`), and by default
puts one tick per category, and plots them in the order in which they are
supplied.  If this is not desired, the solution is to convert the strings to
a numeric type as in the following examples.

"""���`a
���`a
���bc1xL############################################################################���`a
���bc1xD# Example 1: Strings can lead to an unexpected order of number ticks���`a
���bc1xD# ------------------------------------------------------------------���`a
���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���`a
���`cfig���`a,���`a ���`bax���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���bmia1���`a,���`a ���bmia2���`a,���`a ���`rconstrained_layout���aoa=���bkcdTrue���`a,���`a ���`gfigsize���aoa=���`a(���bmia6���`a,���`a ���bmfc2.5���`a)���`a)���`a
���`ax���`a ���aoa=���`a ���`a[���bs1a'���bs1a1���bs1a'���`a,���`a ���bs1a'���bs1a5���bs1a'���`a,���`a ���bs1a'���bs1a2���bs1a'���`a,���`a ���bs1a'���bs1a3���bs1a'���`a]���`a
���`ay���`a ���aoa=���`a ���`a[���bmia1���`a,���`a ���bmia4���`a,���`a ���bmia2���`a,���`a ���bmia3���`a]���`a
���`bax���`a[���bmia0���`a]���aoa.���`dplot���`a(���`ax���`a,���`a ���`ay���`a,���`a ���bs1a'���bs1ad���bs1a'���`a)���`a
���`bax���`a[���bmia0���`a]���aoa.���`ktick_params���`a(���`daxis���aoa=���bs1a'���bs1ax���bs1a'���`a,���`a ���`ecolor���aoa=���bs1a'���bs1ar���bs1a'���`a,���`a ���`jlabelcolor���aoa=���bs1a'���bs1ar���bs1a'���`a)���`a
���`bax���`a[���bmia0���`a]���aoa.���`jset_xlabel���`a(���bs1a'���bs1jCategories���bs1a'���`a)���`a
���`bax���`a[���bmia0���`a]���aoa.���`iset_title���`a(���bs1a'���bs1x#Ticks seem out of order / misplaced���bs1a'���`a)���`a
���`a
���bc1u# convert to numbers:���`a
���`ax���`a ���aoa=���`a ���`bnp���aoa.���`gasarray���`a(���`ax���`a,���`a ���`edtype���aoa=���bs1a'���bs1efloat���bs1a'���`a)���`a
���`bax���`a[���bmia1���`a]���aoa.���`dplot���`a(���`ax���`a,���`a ���`ay���`a,���`a ���bs1a'���bs1ad���bs1a'���`a)���`a
���`bax���`a[���bmia1���`a]���aoa.���`jset_xlabel���`a(���bs1a'���bs1fFloats���bs1a'���`a)���`a
���`bax���`a[���bmia1���`a]���aoa.���`iset_title���`a(���bs1a'���bs1qTicks as expected���bs1a'���`a)���`a
���`a
���bc1xL############################################################################���`a
���bc1x0# Example 2: Strings can lead to very many ticks���`a
���bc1x0# ----------------------------------------------���`a
���bc1xK# If *x* has 100 elements, all strings, then we would have 100 (unreadable)���`a
���bc1xD# ticks, and again the solution is to convert the strings to floats:���`a
���`a
���`cfig���`a,���`a ���`bax���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���bmia1���`a,���`a ���bmia2���`a,���`a ���`gfigsize���aoa=���`a(���bmia6���`a,���`a ���bmfc2.5���`a)���`a)���`a
���`ax���`a ���aoa=���`a ���`a[���bsaaf���bs1a'���bsia{���`bxx���bsia}���bs1a'���`a ���akcfor���`a ���`bxx���`a ���bowbin���`a ���`bnp���aoa.���`farange���`a(���bmic100���`a)���`a]���`a
���`ay���`a ���aoa=���`a ���`bnp���aoa.���`farange���`a(���bmic100���`a)���`a
���`bax���`a[���bmia0���`a]���aoa.���`dplot���`a(���`ax���`a,���`a ���`ay���`a)���`a
���`bax���`a[���bmia0���`a]���aoa.���`ktick_params���`a(���`daxis���aoa=���bs1a'���bs1ax���bs1a'���`a,���`a ���`ecolor���aoa=���bs1a'���bs1ar���bs1a'���`a,���`a ���`jlabelcolor���aoa=���bs1a'���bs1ar���bs1a'���`a)���`a
���`bax���`a[���bmia0���`a]���aoa.���`iset_title���`a(���bs1a'���bs1nToo many ticks���bs1a'���`a)���`a
���`bax���`a[���bmia0���`a]���aoa.���`jset_xlabel���`a(���bs1a'���bs1jCategories���bs1a'���`a)���`a
���`a
���`bax���`a[���bmia1���`a]���aoa.���`dplot���`a(���`bnp���aoa.���`gasarray���`a(���`ax���`a,���`a ���bnbefloat���`a)���`a,���`a ���`ay���`a)���`a
���`bax���`a[���bmia1���`a]���aoa.���`iset_title���`a(���bs1a'���bs1vx converted to numbers���bs1a'���`a)���`a
���`bax���`a[���bmia1���`a]���aoa.���`jset_xlabel���`a(���bs1a'���bs1fFloats���bs1a'���`a)���`a
���`a
���bc1xL############################################################################���`a
���bc1xF# Example 3: Strings can lead to an unexpected order of datetime ticks���`a
���bc1xF# --------------------------------------------------------------------���`a
���bc1xG# A common case is when dates are read from a CSV file, they need to be���`a
���bc1xL# converted from strings to datetime objects to get the proper date locators���`a
���bc1q# and formatters.���`a
���`a
���`cfig���`a,���`a ���`bax���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���bmia1���`a,���`a ���bmia2���`a,���`a ���`rconstrained_layout���aoa=���bkcdTrue���`a,���`a ���`gfigsize���aoa=���`a(���bmia6���`a,���`a ���bmfd2.75���`a)���`a)���`a
���`ax���`a ���aoa=���`a ���`a[���bs1a'���bs1j2021-10-01���bs1a'���`a,���`a ���bs1a'���bs1j2021-11-02���bs1a'���`a,���`a ���bs1a'���bs1j2021-12-03���bs1a'���`a,���`a ���bs1a'���bs1j2021-09-01���bs1a'���`a]���`a
���`ay���`a ���aoa=���`a ���`a[���bmia0���`a,���`a ���bmia2���`a,���`a ���bmia3���`a,���`a ���bmia1���`a]���`a
���`bax���`a[���bmia0���`a]���aoa.���`dplot���`a(���`ax���`a,���`a ���`ay���`a,���`a ���bs1a'���bs1ad���bs1a'���`a)���`a
���`bax���`a[���bmia0���`a]���aoa.���`ktick_params���`a(���`daxis���aoa=���bs1a'���bs1ax���bs1a'���`a,���`a ���`mlabelrotation���aoa=���bmib90���`a,���`a ���`ecolor���aoa=���bs1a'���bs1ar���bs1a'���`a,���`a ���`jlabelcolor���aoa=���bs1a'���bs1ar���bs1a'���`a)���`a
���`bax���`a[���bmia0���`a]���aoa.���`iset_title���`a(���bs1a'���bs1rDates out of order���bs1a'���`a)���`a
���`a
���bc1w# convert to datetime64���`a
���`ax���`a ���aoa=���`a ���`bnp���aoa.���`gasarray���`a(���`ax���`a,���`a ���`edtype���aoa=���bs1a'���bs1mdatetime64[s]���bs1a'���`a)���`a
���`bax���`a[���bmia1���`a]���aoa.���`dplot���`a(���`ax���`a,���`a ���`ay���`a,���`a ���bs1a'���bs1ad���bs1a'���`a)���`a
���`bax���`a[���bmia1���`a]���aoa.���`ktick_params���`a(���`daxis���aoa=���bs1a'���bs1ax���bs1a'���`a,���`a ���`mlabelrotation���aoa=���bmib90���`a)���`a
���`bax���`a[���bmia1���`a]���aoa.���`iset_title���`a(���bs1a'���bs1xx converted to datetimes���bs1a'���`a)���`a
���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
`dNone�