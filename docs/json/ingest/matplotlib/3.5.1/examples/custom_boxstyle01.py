ŸØÇÅŸ¥Éô◊Ÿ±ÇbsaarŸ±ÇbsdxŒ"""
=================
Custom box styles
=================

This example demonstrates the implementation of a custom `.BoxStyle`.
Custom `.ConnectionStyle`\s and `.ArrowStyle`\s can be similarly defined.
"""Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±ÇbkndfromŸ±Ç`a Ÿ±ÇbnnŸ¢ÑjmatplotlibŸ†Ñjmatplotlibe3.5.1fmodulejmatplotlibfmoduleıŸ±Çbnna.Ÿ±ÇbnngpatchesŸ±Ç`a Ÿ±ÇbknfimportŸ±Ç`a Ÿ±Ç`hBoxStyleŸ±Ç`a
Ÿ±ÇbkndfromŸ±Ç`a Ÿ±ÇbnnŸ¢ÑjmatplotlibŸ†Ñjmatplotlibe3.5.1fmodulejmatplotlibfmoduleıŸ±Çbnna.Ÿ±ÇbnndpathŸ±Ç`a Ÿ±ÇbknfimportŸ±Ç`a Ÿ±Ç`dPathŸ±Ç`a
Ÿ±ÇbknfimportŸ±Ç`a Ÿ±ÇbnnŸ¢ÑjmatplotlibŸ†Ñjmatplotlibe3.5.1fmodulejmatplotlibfmoduleıŸ±Çbnna.Ÿ±ÇbnnfpyplotŸ±Ç`a Ÿ±ÇakbasŸ±Ç`a Ÿ±ÇbnncpltŸ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1xO###############################################################################Ÿ±Ç`a
Ÿ±Çbc1xI# Custom box styles can be implemented as a function that takes argumentsŸ±Ç`a
Ÿ±Çbc1xE# specifying both a rectangular box and the amount of "mutation", andŸ±Ç`a
Ÿ±Çbc1xC# returns the "mutated" path.  The specific signature is the one ofŸ±Ç`a
Ÿ±Çbc1x# ``custom_box_style`` below.Ÿ±Ç`a
Ÿ±Çbc1a#Ÿ±Ç`a
Ÿ±Çbc1xK# Here, we return a new path which adds an "arrow" shape on the left of theŸ±Ç`a
Ÿ±Çbc1f# box.Ÿ±Ç`a
Ÿ±Çbc1a#Ÿ±Ç`a
Ÿ±Çbc1x2# The custom box style can then be used by passingŸ±Ç`a
Ÿ±Çbc1x@# ``bbox=dict(boxstyle=custom_box_style, ...)`` to `.Axes.text`.Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±ÇakcdefŸ±Ç`a Ÿ±Çbnfpcustom_box_styleŸ±Ç`a(Ÿ±Ç`bx0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`by0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ewidthŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`fheightŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`mmutation_sizeŸ±Ç`a)Ÿ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±ÇbsdyI"""
    Given the location and size of the box, return the path of the box around
    it.

    Rotation is automatically taken care of.

    Parameters
    ----------
    x0, y0, width, height : float
        Box location and size.
    mutation_size : float
        Mutation reference scale, typically the text font size.
    """Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Çbc1i# paddingŸ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`emypadŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Çbmfc0.3Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`cpadŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`mmutation_sizeŸ±Ç`a Ÿ±Çaoa*Ÿ±Ç`a Ÿ±Ç`emypadŸ±Ç`a
Ÿ±Ç`d    Ÿ±Çbc1x&# width and height with padding added.Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`ewidthŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`ewidthŸ±Ç`a Ÿ±Çaoa+Ÿ±Ç`a Ÿ±Çbmia2Ÿ±Ç`a Ÿ±Çaoa*Ÿ±Ç`a Ÿ±Ç`cpadŸ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`fheightŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`fheightŸ±Ç`a Ÿ±Çaoa+Ÿ±Ç`a Ÿ±Çbmia2Ÿ±Ç`a Ÿ±Çaoa*Ÿ±Ç`a Ÿ±Ç`cpadŸ±Ç`a
Ÿ±Ç`d    Ÿ±Çbc1x# boundary of the padded boxŸ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`bx0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`by0Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bx0Ÿ±Ç`a Ÿ±Çaoa-Ÿ±Ç`a Ÿ±Ç`cpadŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`by0Ÿ±Ç`a Ÿ±Çaoa-Ÿ±Ç`a Ÿ±Ç`cpadŸ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`bx1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`by1Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bx0Ÿ±Ç`a Ÿ±Çaoa+Ÿ±Ç`a Ÿ±Ç`ewidthŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`by0Ÿ±Ç`a Ÿ±Çaoa+Ÿ±Ç`a Ÿ±Ç`fheightŸ±Ç`a
Ÿ±Ç`d    Ÿ±Çbc1u# return the new pathŸ±Ç`a
Ÿ±Ç`d    Ÿ±ÇakfreturnŸ±Ç`a Ÿ±Ç`dPathŸ±Ç`a(Ÿ±Ç`a[Ÿ±Ç`a(Ÿ±Ç`bx0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`by0Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`q                 Ÿ±Ç`a(Ÿ±Ç`bx1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`by0Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`a(Ÿ±Ç`bx1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`by1Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`a(Ÿ±Ç`bx0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`by1Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`q                 Ÿ±Ç`a(Ÿ±Ç`bx0Ÿ±Çaoa-Ÿ±Ç`cpadŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`a(Ÿ±Ç`by0Ÿ±Çaoa+Ÿ±Ç`by1Ÿ±Ç`a)Ÿ±Çaoa/Ÿ±Çbmia2Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`a(Ÿ±Ç`bx0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`by0Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`q                 Ÿ±Ç`a(Ÿ±Ç`bx0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`by0Ÿ±Ç`a)Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`p                Ÿ±Ç`fclosedŸ±Çaoa=Ÿ±ÇbkcdTrueŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`cfigŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`baxŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`hsubplotsŸ±Ç`a(Ÿ±Ç`gfigsizeŸ±Çaoa=Ÿ±Ç`a(Ÿ±Çbmia3Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia3Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`dtextŸ±Ç`a(Ÿ±Çbmfc0.5Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfc0.5Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs2a"Ÿ±Çbs2dTestŸ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dsizeŸ±Çaoa=Ÿ±Çbmib30Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`bvaŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2fcenterŸ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`bhaŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2fcenterŸ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`hrotationŸ±Çaoa=Ÿ±Çbmib30Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±Ç`dbboxŸ±Çaoa=Ÿ±ÇbnbddictŸ±Ç`a(Ÿ±Ç`hboxstyleŸ±Çaoa=Ÿ±Ç`pcustom_box_styleŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ealphaŸ±Çaoa=Ÿ±Çbmfc0.2Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1xO###############################################################################Ÿ±Ç`a
Ÿ±Çbc1xJ# Likewise, custom box styles can be implemented as classes that implementŸ±Ç`a
Ÿ±Çbc1o# ``__call__``.Ÿ±Ç`a
Ÿ±Çbc1a#Ÿ±Ç`a
Ÿ±Çbc1xL# The classes can then be registered into the ``BoxStyle._style_list`` dict,Ÿ±Ç`a
Ÿ±Çbc1x4# which allows specifying the box style as a string,Ÿ±Ç`a
Ÿ±Çbc1xA# ``bbox=dict(boxstyle="registered_name,param=value,...", ...)``.Ÿ±Ç`a
Ÿ±Çbc1xJ# Note that this registration relies on internal APIs and is therefore notŸ±Ç`a
Ÿ±Çbc1w# officially supported.Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±ÇakeclassŸ±Ç`a Ÿ±ÇbncgMyStyleŸ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Çbsds"""A simple box."""Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±ÇakcdefŸ±Ç`a Ÿ±Çbfmh__init__Ÿ±Ç`a(Ÿ±ÇbbpdselfŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`cpadŸ±Çaoa=Ÿ±Çbmfc0.3Ÿ±Ç`a)Ÿ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±Çbsdx¶"""
        The arguments must be floats and have default values.

        Parameters
        ----------
        pad : float
            amount of padding
        """Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±ÇbbpdselfŸ±Çaoa.Ÿ±Ç`cpadŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cpadŸ±Ç`a
Ÿ±Ç`h        Ÿ±ÇbnbesuperŸ±Ç`a(Ÿ±Ç`a)Ÿ±Çaoa.Ÿ±Çbfmh__init__Ÿ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±ÇakcdefŸ±Ç`a Ÿ±Çbfmh__call__Ÿ±Ç`a(Ÿ±ÇbbpdselfŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`bx0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`by0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ewidthŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`fheightŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`mmutation_sizeŸ±Ç`a)Ÿ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±Çbsdyy"""
        Given the location and size of the box, return the path of the box
        around it.

        Rotation is automatically taken care of.

        Parameters
        ----------
        x0, y0, width, height : float
            Box location and size.
        mutation_size : float
            Reference scale for the mutation, typically the text font size.
        """Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±Çbc1i# paddingŸ±Ç`a
Ÿ±Ç`h        Ÿ±Ç`cpadŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`mmutation_sizeŸ±Ç`a Ÿ±Çaoa*Ÿ±Ç`a Ÿ±ÇbbpdselfŸ±Çaoa.Ÿ±Ç`cpadŸ±Ç`a
Ÿ±Ç`h        Ÿ±Çbc1x%# width and height with padding addedŸ±Ç`a
Ÿ±Ç`h        Ÿ±Ç`ewidthŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`ewidthŸ±Ç`a Ÿ±Çaoa+Ÿ±Ç`a Ÿ±Çbmfb2.Ÿ±Çaoa*Ÿ±Ç`cpadŸ±Ç`a
Ÿ±Ç`h        Ÿ±Ç`fheightŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`fheightŸ±Ç`a Ÿ±Çaoa+Ÿ±Ç`a Ÿ±Çbmfb2.Ÿ±Çaoa*Ÿ±Ç`cpadŸ±Ç`a
Ÿ±Ç`h        Ÿ±Çbc1x# boundary of the padded boxŸ±Ç`a
Ÿ±Ç`h        Ÿ±Ç`bx0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`by0Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bx0Ÿ±Ç`a Ÿ±Çaoa-Ÿ±Ç`a Ÿ±Ç`cpadŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`by0Ÿ±Ç`a Ÿ±Çaoa-Ÿ±Ç`a Ÿ±Ç`cpadŸ±Ç`a
Ÿ±Ç`h        Ÿ±Ç`bx1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`by1Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bx0Ÿ±Ç`a Ÿ±Çaoa+Ÿ±Ç`a Ÿ±Ç`ewidthŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`by0Ÿ±Ç`a Ÿ±Çaoa+Ÿ±Ç`a Ÿ±Ç`fheightŸ±Ç`a
Ÿ±Ç`h        Ÿ±Çbc1u# return the new pathŸ±Ç`a
Ÿ±Ç`h        Ÿ±ÇakfreturnŸ±Ç`a Ÿ±Ç`dPathŸ±Ç`a(Ÿ±Ç`a[Ÿ±Ç`a(Ÿ±Ç`bx0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`by0Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`u                     Ÿ±Ç`a(Ÿ±Ç`bx1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`by0Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`a(Ÿ±Ç`bx1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`by1Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`a(Ÿ±Ç`bx0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`by1Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`u                     Ÿ±Ç`a(Ÿ±Ç`bx0Ÿ±Çaoa-Ÿ±Ç`cpadŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`a(Ÿ±Ç`by0Ÿ±Çaoa+Ÿ±Ç`by1Ÿ±Ç`a)Ÿ±Çaoa/Ÿ±Çbmfb2.Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`a(Ÿ±Ç`bx0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`by0Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`u                     Ÿ±Ç`a(Ÿ±Ç`bx0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`by0Ÿ±Ç`a)Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`t                    Ÿ±Ç`fclosedŸ±Çaoa=Ÿ±ÇbkcdTrueŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`hBoxStyleŸ±Çaoa.Ÿ±Ç`k_style_listŸ±Ç`a[Ÿ±Çbs2a"Ÿ±Çbs2fangledŸ±Çbs2a"Ÿ±Ç`a]Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`gMyStyleŸ±Ç`b  Ÿ±Çbc1x# Register the custom style.Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`cfigŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`baxŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`hsubplotsŸ±Ç`a(Ÿ±Ç`gfigsizeŸ±Çaoa=Ÿ±Ç`a(Ÿ±Çbmia3Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia3Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`dtextŸ±Ç`a(Ÿ±Çbmfc0.5Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfc0.5Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs2a"Ÿ±Çbs2dTestŸ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dsizeŸ±Çaoa=Ÿ±Çbmib30Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`bvaŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2fcenterŸ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`bhaŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2fcenterŸ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`hrotationŸ±Çaoa=Ÿ±Çbmib30Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±Ç`dbboxŸ±Çaoa=Ÿ±ÇbnbddictŸ±Ç`a(Ÿ±Ç`hboxstyleŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2nangled,pad=0.5Ÿ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ealphaŸ±Çaoa=Ÿ±Çbmfc0.2Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±ÇakcdelŸ±Ç`a Ÿ±Ç`hBoxStyleŸ±Çaoa.Ÿ±Ç`k_style_listŸ±Ç`a[Ÿ±Çbs2a"Ÿ±Çbs2fangledŸ±Çbs2a"Ÿ±Ç`a]Ÿ±Ç`b  Ÿ±Çbc1p# Unregister it.Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`dshowŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
`dNoneˆ