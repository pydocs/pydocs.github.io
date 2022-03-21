������������bsaar���bsdx�"""
=================
Custom box styles
=================

This example demonstrates the implementation of a custom `.BoxStyle`.
Custom `.ConnectionStyle`\s and `.ArrowStyle`\s can be similarly defined.
"""���`a
���`a
���bkndfrom���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnngpatches���`a ���bknfimport���`a ���`hBoxStyle���`a
���bkndfrom���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnndpath���`a ���bknfimport���`a ���`dPath���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���`a
���`a
���bc1xO###############################################################################���`a
���bc1xI# Custom box styles can be implemented as a function that takes arguments���`a
���bc1xE# specifying both a rectangular box and the amount of "mutation", and���`a
���bc1xC# returns the "mutated" path.  The specific signature is the one of���`a
���bc1x# ``custom_box_style`` below.���`a
���bc1a#���`a
���bc1xK# Here, we return a new path which adds an "arrow" shape on the left of the���`a
���bc1f# box.���`a
���bc1a#���`a
���bc1x2# The custom box style can then be used by passing���`a
���bc1x@# ``bbox=dict(boxstyle=custom_box_style, ...)`` to `.Axes.text`.���`a
���`a
���`a
���akcdef���`a ���bnfpcustom_box_style���`a(���`bx0���`a,���`a ���`by0���`a,���`a ���`ewidth���`a,���`a ���`fheight���`a,���`a ���`mmutation_size���`a)���`a:���`a
���`d    ���bsdyI"""
    Given the location and size of the box, return the path of the box around
    it.

    Rotation is automatically taken care of.

    Parameters
    ----------
    x0, y0, width, height : float
        Box location and size.
    mutation_size : float
        Mutation reference scale, typically the text font size.
    """���`a
���`d    ���bc1i# padding���`a
���`d    ���`emypad���`a ���aoa=���`a ���bmfc0.3���`a
���`d    ���`cpad���`a ���aoa=���`a ���`mmutation_size���`a ���aoa*���`a ���`emypad���`a
���`d    ���bc1x&# width and height with padding added.���`a
���`d    ���`ewidth���`a ���aoa=���`a ���`ewidth���`a ���aoa+���`a ���bmia2���`a ���aoa*���`a ���`cpad���`a
���`d    ���`fheight���`a ���aoa=���`a ���`fheight���`a ���aoa+���`a ���bmia2���`a ���aoa*���`a ���`cpad���`a
���`d    ���bc1x# boundary of the padded box���`a
���`d    ���`bx0���`a,���`a ���`by0���`a ���aoa=���`a ���`bx0���`a ���aoa-���`a ���`cpad���`a,���`a ���`by0���`a ���aoa-���`a ���`cpad���`a
���`d    ���`bx1���`a,���`a ���`by1���`a ���aoa=���`a ���`bx0���`a ���aoa+���`a ���`ewidth���`a,���`a ���`by0���`a ���aoa+���`a ���`fheight���`a
���`d    ���bc1u# return the new path���`a
���`d    ���akfreturn���`a ���`dPath���`a(���`a[���`a(���`bx0���`a,���`a ���`by0���`a)���`a,���`a
���`q                 ���`a(���`bx1���`a,���`a ���`by0���`a)���`a,���`a ���`a(���`bx1���`a,���`a ���`by1���`a)���`a,���`a ���`a(���`bx0���`a,���`a ���`by1���`a)���`a,���`a
���`q                 ���`a(���`bx0���aoa-���`cpad���`a,���`a ���`a(���`by0���aoa+���`by1���`a)���aoa/���bmia2���`a)���`a,���`a ���`a(���`bx0���`a,���`a ���`by0���`a)���`a,���`a
���`q                 ���`a(���`bx0���`a,���`a ���`by0���`a)���`a]���`a,���`a
���`p                ���`fclosed���aoa=���bkcdTrue���`a)���`a
���`a
���`a
���`cfig���`a,���`a ���`bax���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`gfigsize���aoa=���`a(���bmia3���`a,���`a ���bmia3���`a)���`a)���`a
���`bax���aoa.���`dtext���`a(���bmfc0.5���`a,���`a ���bmfc0.5���`a,���`a ���bs2a"���bs2dTest���bs2a"���`a,���`a ���`dsize���aoa=���bmib30���`a,���`a ���`bva���aoa=���bs2a"���bs2fcenter���bs2a"���`a,���`a ���`bha���aoa=���bs2a"���bs2fcenter���bs2a"���`a,���`a ���`hrotation���aoa=���bmib30���`a,���`a
���`h        ���`dbbox���aoa=���bnbddict���`a(���`hboxstyle���aoa=���`pcustom_box_style���`a,���`a ���`ealpha���aoa=���bmfc0.2���`a)���`a)���`a
���`a
���`a
���bc1xO###############################################################################���`a
���bc1xJ# Likewise, custom box styles can be implemented as classes that implement���`a
���bc1o# ``__call__``.���`a
���bc1a#���`a
���bc1xL# The classes can then be registered into the ``BoxStyle._style_list`` dict,���`a
���bc1x4# which allows specifying the box style as a string,���`a
���bc1xA# ``bbox=dict(boxstyle="registered_name,param=value,...", ...)``.���`a
���bc1xJ# Note that this registration relies on internal APIs and is therefore not���`a
���bc1w# officially supported.���`a
���`a
���`a
���akeclass���`a ���bncgMyStyle���`a:���`a
���`d    ���bsds"""A simple box."""���`a
���`a
���`d    ���akcdef���`a ���bfmh__init__���`a(���bbpdself���`a,���`a ���`cpad���aoa=���bmfc0.3���`a)���`a:���`a
���`h        ���bsdx�"""
        The arguments must be floats and have default values.

        Parameters
        ----------
        pad : float
            amount of padding
        """���`a
���`h        ���bbpdself���aoa.���`cpad���`a ���aoa=���`a ���`cpad���`a
���`h        ���bnbesuper���`a(���`a)���aoa.���bfmh__init__���`a(���`a)���`a
���`a
���`d    ���akcdef���`a ���bfmh__call__���`a(���bbpdself���`a,���`a ���`bx0���`a,���`a ���`by0���`a,���`a ���`ewidth���`a,���`a ���`fheight���`a,���`a ���`mmutation_size���`a)���`a:���`a
���`h        ���bsdyy"""
        Given the location and size of the box, return the path of the box
        around it.

        Rotation is automatically taken care of.

        Parameters
        ----------
        x0, y0, width, height : float
            Box location and size.
        mutation_size : float
            Reference scale for the mutation, typically the text font size.
        """���`a
���`h        ���bc1i# padding���`a
���`h        ���`cpad���`a ���aoa=���`a ���`mmutation_size���`a ���aoa*���`a ���bbpdself���aoa.���`cpad���`a
���`h        ���bc1x%# width and height with padding added���`a
���`h        ���`ewidth���`a ���aoa=���`a ���`ewidth���`a ���aoa+���`a ���bmfb2.���aoa*���`cpad���`a
���`h        ���`fheight���`a ���aoa=���`a ���`fheight���`a ���aoa+���`a ���bmfb2.���aoa*���`cpad���`a
���`h        ���bc1x# boundary of the padded box���`a
���`h        ���`bx0���`a,���`a ���`by0���`a ���aoa=���`a ���`bx0���`a ���aoa-���`a ���`cpad���`a,���`a ���`by0���`a ���aoa-���`a ���`cpad���`a
���`h        ���`bx1���`a,���`a ���`by1���`a ���aoa=���`a ���`bx0���`a ���aoa+���`a ���`ewidth���`a,���`a ���`by0���`a ���aoa+���`a ���`fheight���`a
���`h        ���bc1u# return the new path���`a
���`h        ���akfreturn���`a ���`dPath���`a(���`a[���`a(���`bx0���`a,���`a ���`by0���`a)���`a,���`a
���`u                     ���`a(���`bx1���`a,���`a ���`by0���`a)���`a,���`a ���`a(���`bx1���`a,���`a ���`by1���`a)���`a,���`a ���`a(���`bx0���`a,���`a ���`by1���`a)���`a,���`a
���`u                     ���`a(���`bx0���aoa-���`cpad���`a,���`a ���`a(���`by0���aoa+���`by1���`a)���aoa/���bmfb2.���`a)���`a,���`a ���`a(���`bx0���`a,���`a ���`by0���`a)���`a,���`a
���`u                     ���`a(���`bx0���`a,���`a ���`by0���`a)���`a]���`a,���`a
���`t                    ���`fclosed���aoa=���bkcdTrue���`a)���`a
���`a
���`a
���`hBoxStyle���aoa.���`k_style_list���`a[���bs2a"���bs2fangled���bs2a"���`a]���`a ���aoa=���`a ���`gMyStyle���`b  ���bc1x# Register the custom style.���`a
���`a
���`cfig���`a,���`a ���`bax���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`gfigsize���aoa=���`a(���bmia3���`a,���`a ���bmia3���`a)���`a)���`a
���`bax���aoa.���`dtext���`a(���bmfc0.5���`a,���`a ���bmfc0.5���`a,���`a ���bs2a"���bs2dTest���bs2a"���`a,���`a ���`dsize���aoa=���bmib30���`a,���`a ���`bva���aoa=���bs2a"���bs2fcenter���bs2a"���`a,���`a ���`bha���aoa=���bs2a"���bs2fcenter���bs2a"���`a,���`a ���`hrotation���aoa=���bmib30���`a,���`a
���`h        ���`dbbox���aoa=���bnbddict���`a(���`hboxstyle���aoa=���bs2a"���bs2nangled,pad=0.5���bs2a"���`a,���`a ���`ealpha���aoa=���bmfc0.2���`a)���`a)���`a
���`a
���akcdel���`a ���`hBoxStyle���aoa.���`k_style_list���`a[���bs2a"���bs2fangled���bs2a"���`a]���`b  ���bc1p# Unregister it.���`a
���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
`dNone�