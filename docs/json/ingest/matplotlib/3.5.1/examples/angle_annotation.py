ŸØÇÅŸ¥ÉôºŸ±Çbsdy\"""
===========================
Scale invariant angle label
===========================

This example shows how to create a scale invariant angle annotation. It is
often useful to mark angles between lines or inside shapes with a circular arc.
While Matplotlib provides an `~.patches.Arc`, an inherent problem when directly
using it for such purposes is that an arc being circular in data space is not
necessarily circular in display space. Also, the arc's radius is often best
defined in a coordinate system which is independent of the actual data
coordinates - at least if you want to be able to freely zoom into your plot
without the annotation growing to infinity.

This calls for a solution where the arc's center is defined in data space, but
its radius in a physical unit like points or pixels, or as a ratio of the Axes
dimension. The following ``AngleAnnotation`` class provides such solution.

The example below serves two purposes:

* It provides a ready-to-use solution for the problem of easily drawing angles
  in graphs.
* It shows how to subclass a Matplotlib artist to enhance its functionality, as
  well as giving a hands-on example on how to use Matplotlib's :doc:`transform
  system </tutorials/advanced/transforms_tutorial>`.

If mainly interested in the former, you may copy the below class and jump to
the :ref:`angle-annotation-usage` section.
"""Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1xI#########################################################################Ÿ±Ç`a
Ÿ±Çbc1w# AngleAnnotation classŸ±Ç`a
Ÿ±Çbc1w# ~~~~~~~~~~~~~~~~~~~~~Ÿ±Ç`a
Ÿ±Çbc1xN# The essential idea here is to subclass `~.patches.Arc` and set its transformŸ±Ç`a
Ÿ±Çbc1xK# to the `~.transforms.IdentityTransform`, making the parameters of the arcŸ±Ç`a
Ÿ±Çbc1x# defined in pixel space.Ÿ±Ç`a
Ÿ±Çbc1xD# We then override the ``Arc``'s attributes ``_center``, ``theta1``,Ÿ±Ç`a
Ÿ±Çbc1xL# ``theta2``, ``width`` and ``height`` and make them properties, coupling toŸ±Ç`a
Ÿ±Çbc1xI# internal methods that calculate the respective parameters each time theŸ±Ç`a
Ÿ±Çbc1xN# attribute is accessed and thereby ensuring that the arc in pixel space staysŸ±Ç`a
Ÿ±Çbc1x.# synchronized with the input points and size.Ÿ±Ç`a
Ÿ±Çbc1xM# For example, each time the arc's drawing method would query its ``_center``Ÿ±Ç`a
Ÿ±Çbc1xI# attribute, instead of receiving the same number all over again, it willŸ±Ç`a
Ÿ±Çbc1xN# instead receive the result of the ``get_center_in_pixels`` method we definedŸ±Ç`a
Ÿ±Çbc1xK# in the subclass. This method transforms the center in data coordinates toŸ±Ç`a
Ÿ±Çbc1xM# pixels via the Axes transform ``ax.transData``. The size and the angles areŸ±Ç`a
Ÿ±Çbc1xF# calculated in a similar fashion, such that the arc changes its shapeŸ±Ç`a
Ÿ±Çbc1x;# automatically when e.g. zooming or panning interactively.Ÿ±Ç`a
Ÿ±Çbc1a#Ÿ±Ç`a
Ÿ±Çbc1xN# The functionality of this class allows to annotate the arc with a text. ThisŸ±Ç`a
Ÿ±Çbc1xJ# text is a `~.text.Annotation` stored in an attribute ``text``. Since theŸ±Ç`a
Ÿ±Çbc1xL# arc's position and radius are defined only at draw time, we need to updateŸ±Ç`a
Ÿ±Çbc1xO# the text's position accordingly. This is done by reimplementing the ``Arc``'sŸ±Ç`a
Ÿ±Çbc1xC# ``draw()`` method to let it call an updating method for the text.Ÿ±Ç`a
Ÿ±Çbc1a#Ÿ±Ç`a
Ÿ±Çbc1xN# The arc and the text will be added to the provided Axes at instantiation: itŸ±Ç`a
Ÿ±Çbc1x<# is hence not strictly necessary to keep a reference to it.Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±ÇbknfimportŸ±Ç`a Ÿ±ÇbnnŸ¢ÑenumpyŸ†Ñenumpyf1.22.3fmoduleenumpyfmoduleıŸ±Ç`a Ÿ±ÇakbasŸ±Ç`a Ÿ±ÇbnnbnpŸ±Ç`a
Ÿ±ÇbknfimportŸ±Ç`a Ÿ±ÇbnnŸ¢ÑjmatplotlibŸ†Ñjmatplotlibe3.5.1fmodulejmatplotlibfmoduleıŸ±Çbnna.Ÿ±ÇbnnfpyplotŸ±Ç`a Ÿ±ÇakbasŸ±Ç`a Ÿ±ÇbnncpltŸ±Ç`a
Ÿ±ÇbkndfromŸ±Ç`a Ÿ±ÇbnnŸ¢ÑjmatplotlibŸ†Ñjmatplotlibe3.5.1fmodulejmatplotlibfmoduleıŸ±Çbnna.Ÿ±ÇbnngpatchesŸ±Ç`a Ÿ±ÇbknfimportŸ±Ç`a Ÿ±Ç`cArcŸ±Ç`a
Ÿ±ÇbkndfromŸ±Ç`a Ÿ±ÇbnnŸ¢ÑjmatplotlibŸ†Ñjmatplotlibe3.5.1fmodulejmatplotlibfmoduleıŸ±Çbnna.Ÿ±ÇbnnjtransformsŸ±Ç`a Ÿ±ÇbknfimportŸ±Ç`a Ÿ±Ç`qIdentityTransformŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`oTransformedBboxŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dBboxŸ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±ÇakeclassŸ±Ç`a Ÿ±ÇbncoAngleAnnotationŸ±Ç`a(Ÿ±Ç`cArcŸ±Ç`a)Ÿ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±ÇbsdxY"""
    Draws an arc between two vectors which appears circular in display space.
    """Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±ÇakcdefŸ±Ç`a Ÿ±Çbfmh__init__Ÿ±Ç`a(Ÿ±ÇbbpdselfŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`bxyŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`bp1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`bp2Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dsizeŸ±Çaoa=Ÿ±Çbmib75Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dunitŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2fpointsŸ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`baxŸ±Çaoa=Ÿ±ÇbkcdNoneŸ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`q                 Ÿ±Ç`dtextŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ltextpositionŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2finsideŸ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`gtext_kwŸ±Çaoa=Ÿ±ÇbkcdNoneŸ±Ç`a,Ÿ±Ç`a Ÿ±Çaoa*Ÿ±Çaoa*Ÿ±Ç`fkwargsŸ±Ç`a)Ÿ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±Çbsdy~"""
        Parameters
        ----------
        xy, p1, p2 : tuple or array of two floats
            Center position and two points. Angle annotation is drawn between
            the two vectors connecting *p1* and *p2* with *xy*, respectively.
            Units are data coordinates.

        size : float
            Diameter of the angle annotation in units specified by *unit*.

        unit : str
            One of the following strings to specify the unit of *size*:

            * "pixels": pixels
            * "points": points, use points instead of pixels to not have a
              dependence on the DPI
            * "axes width", "axes height": relative units of Axes width, height
            * "axes min", "axes max": minimum or maximum of relative Axes
              width, height

        ax : `matplotlib.axes.Axes`
            The Axes to add the angle annotation to.

        text : str
            The text to mark the angle with.

        textposition : {"inside", "outside", "edge"}
            Whether to show the text in- or outside the arc. "edge" can be used
            for custom positions anchored at the arc's edge.

        text_kw : dict
            Dictionary of arguments passed to the Annotation.

        **kwargs
            Further parameters are passed to `matplotlib.patches.Arc`. Use this
            to specify, color, linewidth etc. of the arc.

        """Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±ÇbbpdselfŸ±Çaoa.Ÿ±Ç`baxŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`baxŸ±Ç`a Ÿ±ÇbowborŸ±Ç`a Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`cgcaŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±ÇbbpdselfŸ±Çaoa.Ÿ±Ç`g_xydataŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bxyŸ±Ç`b  Ÿ±Çbc1u# in data coordinatesŸ±Ç`a
Ÿ±Ç`h        Ÿ±ÇbbpdselfŸ±Çaoa.Ÿ±Ç`dvec1Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bp1Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±ÇbbpdselfŸ±Çaoa.Ÿ±Ç`dvec2Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bp2Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±ÇbbpdselfŸ±Çaoa.Ÿ±Ç`dsizeŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`dsizeŸ±Ç`a
Ÿ±Ç`h        Ÿ±ÇbbpdselfŸ±Çaoa.Ÿ±Ç`dunitŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`dunitŸ±Ç`a
Ÿ±Ç`h        Ÿ±ÇbbpdselfŸ±Çaoa.Ÿ±Ç`ltextpositionŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`ltextpositionŸ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±ÇbnbesuperŸ±Ç`a(Ÿ±Ç`a)Ÿ±Çaoa.Ÿ±Çbfmh__init__Ÿ±Ç`a(Ÿ±ÇbbpdselfŸ±Çaoa.Ÿ±Ç`g_xydataŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dsizeŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dsizeŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`eangleŸ±Çaoa=Ÿ±Çbmfc0.0Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`x                         Ÿ±Ç`ftheta1Ÿ±Çaoa=Ÿ±ÇbbpdselfŸ±Çaoa.Ÿ±Ç`ftheta1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ftheta2Ÿ±Çaoa=Ÿ±ÇbbpdselfŸ±Çaoa.Ÿ±Ç`ftheta2Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çaoa*Ÿ±Çaoa*Ÿ±Ç`fkwargsŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±ÇbbpdselfŸ±Çaoa.Ÿ±Ç`mset_transformŸ±Ç`a(Ÿ±Ç`qIdentityTransformŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±ÇbbpdselfŸ±Çaoa.Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`iadd_patchŸ±Ç`a(Ÿ±ÇbbpdselfŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±ÇbbpdselfŸ±Çaoa.Ÿ±Ç`bkwŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±ÇbnbddictŸ±Ç`a(Ÿ±Ç`bhaŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2fcenterŸ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`bvaŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2fcenterŸ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`w                       Ÿ±Ç`hxycoordsŸ±Çaoa=Ÿ±Ç`qIdentityTransformŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`w                       Ÿ±Ç`fxytextŸ±Çaoa=Ÿ±Ç`a(Ÿ±Çbmia0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia0Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`jtextcoordsŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2moffset pointsŸ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`w                       Ÿ±Ç`oannotation_clipŸ±Çaoa=Ÿ±ÇbkcdTrueŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±ÇbbpdselfŸ±Çaoa.Ÿ±Ç`bkwŸ±Çaoa.Ÿ±Ç`fupdateŸ±Ç`a(Ÿ±Ç`gtext_kwŸ±Ç`a Ÿ±ÇbowborŸ±Ç`a Ÿ±Ç`a{Ÿ±Ç`a}Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±ÇbbpdselfŸ±Çaoa.Ÿ±Ç`dtextŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`hannotateŸ±Ç`a(Ÿ±Ç`dtextŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`bxyŸ±Çaoa=Ÿ±ÇbbpdselfŸ±Çaoa.Ÿ±Ç`g_centerŸ±Ç`a,Ÿ±Ç`a Ÿ±Çaoa*Ÿ±Çaoa*Ÿ±ÇbbpdselfŸ±Çaoa.Ÿ±Ç`bkwŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±ÇakcdefŸ±Ç`a Ÿ±Çbnfhget_sizeŸ±Ç`a(Ÿ±ÇbbpdselfŸ±Ç`a)Ÿ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±Ç`ffactorŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Çbmfb1.Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±ÇakbifŸ±Ç`a Ÿ±ÇbbpdselfŸ±Çaoa.Ÿ±Ç`dunitŸ±Ç`a Ÿ±Çaob==Ÿ±Ç`a Ÿ±Çbs2a"Ÿ±Çbs2fpointsŸ±Çbs2a"Ÿ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`l            Ÿ±Ç`ffactorŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±ÇbbpdselfŸ±Çaoa.Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`ffigureŸ±Çaoa.Ÿ±Ç`cdpiŸ±Ç`a Ÿ±Çaoa/Ÿ±Ç`a Ÿ±Çbmfc72.Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±ÇakdelifŸ±Ç`a Ÿ±ÇbbpdselfŸ±Çaoa.Ÿ±Ç`dunitŸ±Ç`a[Ÿ±Ç`a:Ÿ±Çbmia4Ÿ±Ç`a]Ÿ±Ç`a Ÿ±Çaob==Ÿ±Ç`a Ÿ±Çbs2a"Ÿ±Çbs2daxesŸ±Çbs2a"Ÿ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`l            Ÿ±Ç`abŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`oTransformedBboxŸ±Ç`a(Ÿ±Ç`dBboxŸ±Çaoa.Ÿ±Ç`kfrom_boundsŸ±Ç`a(Ÿ±Çbmia0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia1Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`x                                 Ÿ±ÇbbpdselfŸ±Çaoa.Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`itransAxesŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`l            Ÿ±Ç`cdicŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`a{Ÿ±Çbs2a"Ÿ±Çbs2cmaxŸ±Çbs2a"Ÿ±Ç`a:Ÿ±Ç`a Ÿ±ÇbnbcmaxŸ±Ç`a(Ÿ±Ç`abŸ±Çaoa.Ÿ±Ç`ewidthŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`abŸ±Çaoa.Ÿ±Ç`fheightŸ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`s                   Ÿ±Çbs2a"Ÿ±Çbs2cminŸ±Çbs2a"Ÿ±Ç`a:Ÿ±Ç`a Ÿ±ÇbnbcminŸ±Ç`a(Ÿ±Ç`abŸ±Çaoa.Ÿ±Ç`ewidthŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`abŸ±Çaoa.Ÿ±Ç`fheightŸ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`s                   Ÿ±Çbs2a"Ÿ±Çbs2ewidthŸ±Çbs2a"Ÿ±Ç`a:Ÿ±Ç`a Ÿ±Ç`abŸ±Çaoa.Ÿ±Ç`ewidthŸ±Ç`a,Ÿ±Ç`a Ÿ±Çbs2a"Ÿ±Çbs2fheightŸ±Çbs2a"Ÿ±Ç`a:Ÿ±Ç`a Ÿ±Ç`abŸ±Çaoa.Ÿ±Ç`fheightŸ±Ç`a}Ÿ±Ç`a
Ÿ±Ç`l            Ÿ±Ç`ffactorŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cdicŸ±Ç`a[Ÿ±ÇbbpdselfŸ±Çaoa.Ÿ±Ç`dunitŸ±Ç`a[Ÿ±Çbmia5Ÿ±Ç`a:Ÿ±Ç`a]Ÿ±Ç`a]Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±ÇakfreturnŸ±Ç`a Ÿ±ÇbbpdselfŸ±Çaoa.Ÿ±Ç`dsizeŸ±Ç`a Ÿ±Çaoa*Ÿ±Ç`a Ÿ±Ç`ffactorŸ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±ÇakcdefŸ±Ç`a Ÿ±Çbnfhset_sizeŸ±Ç`a(Ÿ±ÇbbpdselfŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dsizeŸ±Ç`a)Ÿ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±ÇbbpdselfŸ±Çaoa.Ÿ±Ç`dsizeŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`dsizeŸ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±ÇakcdefŸ±Ç`a Ÿ±Çbnftget_center_in_pixelsŸ±Ç`a(Ÿ±ÇbbpdselfŸ±Ç`a)Ÿ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±Çbsdx"""return center in pixels"""Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±ÇakfreturnŸ±Ç`a Ÿ±ÇbbpdselfŸ±Çaoa.Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`itransDataŸ±Çaoa.Ÿ±Ç`itransformŸ±Ç`a(Ÿ±ÇbbpdselfŸ±Çaoa.Ÿ±Ç`g_xydataŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±ÇakcdefŸ±Ç`a Ÿ±Çbnfjset_centerŸ±Ç`a(Ÿ±ÇbbpdselfŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`bxyŸ±Ç`a)Ÿ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±Çbsdx$"""set center in data coordinates"""Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±ÇbbpdselfŸ±Çaoa.Ÿ±Ç`g_xydataŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bxyŸ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±ÇakcdefŸ±Ç`a Ÿ±Çbnfiget_thetaŸ±Ç`a(Ÿ±ÇbbpdselfŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`cvecŸ±Ç`a)Ÿ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±Ç`mvec_in_pixelsŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±ÇbbpdselfŸ±Çaoa.Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`itransDataŸ±Çaoa.Ÿ±Ç`itransformŸ±Ç`a(Ÿ±Ç`cvecŸ±Ç`a)Ÿ±Ç`a Ÿ±Çaoa-Ÿ±Ç`a Ÿ±ÇbbpdselfŸ±Çaoa.Ÿ±Ç`g_centerŸ±Ç`a
Ÿ±Ç`h        Ÿ±ÇakfreturnŸ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`grad2degŸ±Ç`a(Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`garctan2Ÿ±Ç`a(Ÿ±Ç`mvec_in_pixelsŸ±Ç`a[Ÿ±Çbmia1Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`mvec_in_pixelsŸ±Ç`a[Ÿ±Çbmia0Ÿ±Ç`a]Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±ÇakcdefŸ±Ç`a Ÿ±Çbnfjget_theta1Ÿ±Ç`a(Ÿ±ÇbbpdselfŸ±Ç`a)Ÿ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±ÇakfreturnŸ±Ç`a Ÿ±ÇbbpdselfŸ±Çaoa.Ÿ±Ç`iget_thetaŸ±Ç`a(Ÿ±ÇbbpdselfŸ±Çaoa.Ÿ±Ç`dvec1Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±ÇakcdefŸ±Ç`a Ÿ±Çbnfjget_theta2Ÿ±Ç`a(Ÿ±ÇbbpdselfŸ±Ç`a)Ÿ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±ÇakfreturnŸ±Ç`a Ÿ±ÇbbpdselfŸ±Çaoa.Ÿ±Ç`iget_thetaŸ±Ç`a(Ÿ±ÇbbpdselfŸ±Çaoa.Ÿ±Ç`dvec2Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±ÇakcdefŸ±Ç`a Ÿ±Çbnfiset_thetaŸ±Ç`a(Ÿ±ÇbbpdselfŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`eangleŸ±Ç`a)Ÿ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±ÇakdpassŸ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Çbc1xE# Redefine attributes of the Arc to always give values in pixel spaceŸ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`g_centerŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±ÇbnbhpropertyŸ±Ç`a(Ÿ±Ç`tget_center_in_pixelsŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`jset_centerŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`ftheta1Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±ÇbnbhpropertyŸ±Ç`a(Ÿ±Ç`jget_theta1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`iset_thetaŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`ftheta2Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±ÇbnbhpropertyŸ±Ç`a(Ÿ±Ç`jget_theta2Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`iset_thetaŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`ewidthŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±ÇbnbhpropertyŸ±Ç`a(Ÿ±Ç`hget_sizeŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`hset_sizeŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`fheightŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±ÇbnbhpropertyŸ±Ç`a(Ÿ±Ç`hget_sizeŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`hset_sizeŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Çbc1xC# The following two methods are needed to update the text position.Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±ÇakcdefŸ±Ç`a Ÿ±ÇbnfddrawŸ±Ç`a(Ÿ±ÇbbpdselfŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`hrendererŸ±Ç`a)Ÿ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±ÇbbpdselfŸ±Çaoa.Ÿ±Ç`kupdate_textŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±ÇbnbesuperŸ±Ç`a(Ÿ±Ç`a)Ÿ±Çaoa.Ÿ±Ç`ddrawŸ±Ç`a(Ÿ±Ç`hrendererŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±ÇakcdefŸ±Ç`a Ÿ±Çbnfkupdate_textŸ±Ç`a(Ÿ±ÇbbpdselfŸ±Ç`a)Ÿ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±Ç`acŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±ÇbbpdselfŸ±Çaoa.Ÿ±Ç`g_centerŸ±Ç`a
Ÿ±Ç`h        Ÿ±Ç`asŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±ÇbbpdselfŸ±Çaoa.Ÿ±Ç`hget_sizeŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±Ç`jangle_spanŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`a(Ÿ±ÇbbpdselfŸ±Çaoa.Ÿ±Ç`ftheta2Ÿ±Ç`a Ÿ±Çaoa-Ÿ±Ç`a Ÿ±ÇbbpdselfŸ±Çaoa.Ÿ±Ç`ftheta1Ÿ±Ç`a)Ÿ±Ç`a Ÿ±Çaoa%Ÿ±Ç`a Ÿ±Çbmic360Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±Ç`eangleŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`gdeg2radŸ±Ç`a(Ÿ±ÇbbpdselfŸ±Çaoa.Ÿ±Ç`ftheta1Ÿ±Ç`a Ÿ±Çaoa+Ÿ±Ç`a Ÿ±Ç`jangle_spanŸ±Ç`a Ÿ±Çaoa/Ÿ±Ç`a Ÿ±Çbmia2Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±Ç`arŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`asŸ±Ç`a Ÿ±Çaoa/Ÿ±Ç`a Ÿ±Çbmia2Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±ÇakbifŸ±Ç`a Ÿ±ÇbbpdselfŸ±Çaoa.Ÿ±Ç`ltextpositionŸ±Ç`a Ÿ±Çaob==Ÿ±Ç`a Ÿ±Çbs2a"Ÿ±Çbs2finsideŸ±Çbs2a"Ÿ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`l            Ÿ±Ç`arŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`asŸ±Ç`a Ÿ±Çaoa/Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`finterpŸ±Ç`a(Ÿ±Ç`jangle_spanŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`a[Ÿ±Çbmib60Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmib90Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmic135Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmic180Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`x*                                          Ÿ±Ç`a[Ÿ±Çbmfc3.3Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfc3.5Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfc3.8Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia4Ÿ±Ç`a]Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±ÇbbpdselfŸ±Çaoa.Ÿ±Ç`dtextŸ±Çaoa.Ÿ±Ç`bxyŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`acŸ±Ç`a Ÿ±Çaoa+Ÿ±Ç`a Ÿ±Ç`arŸ±Ç`a Ÿ±Çaoa*Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`earrayŸ±Ç`a(Ÿ±Ç`a[Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`ccosŸ±Ç`a(Ÿ±Ç`eangleŸ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`csinŸ±Ç`a(Ÿ±Ç`eangleŸ±Ç`a)Ÿ±Ç`a]Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±ÇakbifŸ±Ç`a Ÿ±ÇbbpdselfŸ±Çaoa.Ÿ±Ç`ltextpositionŸ±Ç`a Ÿ±Çaob==Ÿ±Ç`a Ÿ±Çbs2a"Ÿ±Çbs2goutsideŸ±Çbs2a"Ÿ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`l            Ÿ±ÇakcdefŸ±Ç`a Ÿ±ÇbnfcR90Ÿ±Ç`a(Ÿ±Ç`aaŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`arŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`awŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ahŸ±Ç`a)Ÿ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`p                Ÿ±ÇakbifŸ±Ç`a Ÿ±Ç`aaŸ±Ç`a Ÿ±Çaoa<Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`farctanŸ±Ç`a(Ÿ±Ç`ahŸ±Çaoa/Ÿ±Çbmia2Ÿ±Çaoa/Ÿ±Ç`a(Ÿ±Ç`arŸ±Çaoa+Ÿ±Ç`awŸ±Çaoa/Ÿ±Çbmia2Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`t                    Ÿ±ÇakfreturnŸ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`dsqrtŸ±Ç`a(Ÿ±Ç`a(Ÿ±Ç`arŸ±Çaoa+Ÿ±Ç`awŸ±Çaoa/Ÿ±Çbmia2Ÿ±Ç`a)Ÿ±Çaoa*Ÿ±Çaoa*Ÿ±Çbmia2Ÿ±Ç`a Ÿ±Çaoa+Ÿ±Ç`a Ÿ±Ç`a(Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`ctanŸ±Ç`a(Ÿ±Ç`aaŸ±Ç`a)Ÿ±Çaoa*Ÿ±Ç`a(Ÿ±Ç`arŸ±Çaoa+Ÿ±Ç`awŸ±Çaoa/Ÿ±Çbmia2Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Çaoa*Ÿ±Çaoa*Ÿ±Çbmia2Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`p                Ÿ±ÇakdelseŸ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`t                    Ÿ±Ç`acŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`dsqrtŸ±Ç`a(Ÿ±Ç`a(Ÿ±Ç`awŸ±Çaoa/Ÿ±Çbmia2Ÿ±Ç`a)Ÿ±Çaoa*Ÿ±Çaoa*Ÿ±Çbmia2Ÿ±Çaoa+Ÿ±Ç`a(Ÿ±Ç`ahŸ±Çaoa/Ÿ±Çbmia2Ÿ±Ç`a)Ÿ±Çaoa*Ÿ±Çaoa*Ÿ±Çbmia2Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`t                    Ÿ±Ç`aTŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`farcsinŸ±Ç`a(Ÿ±Ç`acŸ±Ç`a Ÿ±Çaoa*Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`ccosŸ±Ç`a(Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`bpiŸ±Çaoa/Ÿ±Çbmia2Ÿ±Ç`a Ÿ±Çaoa-Ÿ±Ç`a Ÿ±Ç`aaŸ±Ç`a Ÿ±Çaoa+Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`farcsinŸ±Ç`a(Ÿ±Ç`ahŸ±Çaoa/Ÿ±Çbmia2Ÿ±Çaoa/Ÿ±Ç`acŸ±Ç`a)Ÿ±Ç`a)Ÿ±Çaoa/Ÿ±Ç`arŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`t                    Ÿ±Ç`bxyŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`arŸ±Ç`a Ÿ±Çaoa*Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`earrayŸ±Ç`a(Ÿ±Ç`a[Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`ccosŸ±Ç`a(Ÿ±Ç`aaŸ±Ç`a Ÿ±Çaoa+Ÿ±Ç`a Ÿ±Ç`aTŸ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`csinŸ±Ç`a(Ÿ±Ç`aaŸ±Ç`a Ÿ±Çaoa+Ÿ±Ç`a Ÿ±Ç`aTŸ±Ç`a)Ÿ±Ç`a]Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`t                    Ÿ±Ç`bxyŸ±Ç`a Ÿ±Çaoa+Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`earrayŸ±Ç`a(Ÿ±Ç`a[Ÿ±Ç`awŸ±Çaoa/Ÿ±Çbmia2Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ahŸ±Çaoa/Ÿ±Çbmia2Ÿ±Ç`a]Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`t                    Ÿ±ÇakfreturnŸ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`dsqrtŸ±Ç`a(Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`csumŸ±Ç`a(Ÿ±Ç`bxyŸ±Çaoa*Ÿ±Çaoa*Ÿ±Çbmia2Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`l            Ÿ±ÇakcdefŸ±Ç`a Ÿ±ÇbnfaRŸ±Ç`a(Ÿ±Ç`aaŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`arŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`awŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ahŸ±Ç`a)Ÿ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`p                Ÿ±Ç`baaŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`a(Ÿ±Ç`aaŸ±Ç`a Ÿ±Çaoa%Ÿ±Ç`a Ÿ±Ç`a(Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`bpiŸ±Çaoa/Ÿ±Çbmia4Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Çaoa*Ÿ±Ç`a(Ÿ±Ç`a(Ÿ±Ç`aaŸ±Ç`a Ÿ±Çaoa%Ÿ±Ç`a Ÿ±Ç`a(Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`bpiŸ±Çaoa/Ÿ±Çbmia2Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a Ÿ±Çaoa<Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`bpiŸ±Çaoa/Ÿ±Çbmia4Ÿ±Ç`a)Ÿ±Ç`a Ÿ±Çaoa+Ÿ±Ç`a Ÿ±Ç`b\
Ÿ±Ç`u                     Ÿ±Ç`a(Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`bpiŸ±Çaoa/Ÿ±Çbmia4Ÿ±Ç`a Ÿ±Çaoa-Ÿ±Ç`a Ÿ±Ç`a(Ÿ±Ç`aaŸ±Ç`a Ÿ±Çaoa%Ÿ±Ç`a Ÿ±Ç`a(Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`bpiŸ±Çaoa/Ÿ±Çbmia4Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Çaoa*Ÿ±Ç`a(Ÿ±Ç`a(Ÿ±Ç`aaŸ±Ç`a Ÿ±Çaoa%Ÿ±Ç`a Ÿ±Ç`a(Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`bpiŸ±Çaoa/Ÿ±Çbmia2Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a Ÿ±Çaoa>Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`bpiŸ±Çaoa/Ÿ±Çbmia4Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`p                Ÿ±ÇakfreturnŸ±Ç`a Ÿ±Ç`cR90Ÿ±Ç`a(Ÿ±Ç`baaŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`arŸ±Ç`a,Ÿ±Ç`a Ÿ±Çaoa*Ÿ±Ç`a[Ÿ±Ç`awŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ahŸ±Ç`a]Ÿ±Ç`a[Ÿ±Ç`a:Ÿ±Ç`a:Ÿ±ÇbnbcintŸ±Ç`a(Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`dsignŸ±Ç`a(Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`ccosŸ±Ç`a(Ÿ±Çbmia2Ÿ±Çaoa*Ÿ±Ç`aaŸ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a]Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`l            Ÿ±Ç`dbboxŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±ÇbbpdselfŸ±Çaoa.Ÿ±Ç`dtextŸ±Çaoa.Ÿ±Ç`qget_window_extentŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`l            Ÿ±Ç`aXŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`aRŸ±Ç`a(Ÿ±Ç`eangleŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`arŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dbboxŸ±Çaoa.Ÿ±Ç`ewidthŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dbboxŸ±Çaoa.Ÿ±Ç`fheightŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`l            Ÿ±Ç`etransŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±ÇbbpdselfŸ±Çaoa.Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`ffigureŸ±Çaoa.Ÿ±Ç`odpi_scale_transŸ±Çaoa.Ÿ±Ç`hinvertedŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`l            Ÿ±Ç`doffsŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`etransŸ±Çaoa.Ÿ±Ç`itransformŸ±Ç`a(Ÿ±Ç`a(Ÿ±Ç`a(Ÿ±Ç`aXŸ±Çaoa-Ÿ±Ç`asŸ±Çaoa/Ÿ±Çbmia2Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia0Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a[Ÿ±Çbmia0Ÿ±Ç`a]Ÿ±Ç`a Ÿ±Çaoa*Ÿ±Ç`a Ÿ±Çbmib72Ÿ±Ç`a
Ÿ±Ç`l            Ÿ±ÇbbpdselfŸ±Çaoa.Ÿ±Ç`dtextŸ±Çaoa.Ÿ±Ç`lset_positionŸ±Ç`a(Ÿ±Ç`a[Ÿ±Ç`doffsŸ±Çaoa*Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`ccosŸ±Ç`a(Ÿ±Ç`eangleŸ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`doffsŸ±Çaoa*Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`csinŸ±Ç`a(Ÿ±Ç`eangleŸ±Ç`a)Ÿ±Ç`a]Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1xI#########################################################################Ÿ±Ç`a
Ÿ±Çbc1x# .. _angle-annotation-usage:Ÿ±Ç`a
Ÿ±Çbc1a#Ÿ±Ç`a
Ÿ±Çbc1g# UsageŸ±Ç`a
Ÿ±Çbc1g# ~~~~~Ÿ±Ç`a
Ÿ±Çbc1a#Ÿ±Ç`a
Ÿ±Çbc1xL# Required arguments to ``AngleAnnotation`` are the center of the arc, *xy*,Ÿ±Ç`a
Ÿ±Çbc1xL# and two points, such that the arc spans between the two vectors connectingŸ±Ç`a
Ÿ±Çbc1xM# *p1* and *p2* with *xy*, respectively. Those are given in data coordinates.Ÿ±Ç`a
Ÿ±Çbc1xM# Further arguments are the *size* of the arc and its *unit*. Additionally, aŸ±Ç`a
Ÿ±Çbc1xO# *text* can be specified, that will be drawn either in- or outside of the arc,Ÿ±Ç`a
Ÿ±Çbc1xM# according to the value of *textposition*. Usage of those arguments is shownŸ±Ç`a
Ÿ±Çbc1h# below.Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`cfigŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`baxŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`hsubplotsŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cfigŸ±Çaoa.Ÿ±Ç`fcanvasŸ±Çaoa.Ÿ±Ç`ddrawŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`b  Ÿ±Çbc1x,# Need to draw the figure to define rendererŸ±Ç`a
Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`iset_titleŸ±Ç`a(Ÿ±Çbs2a"Ÿ±Çbs2rAngleLabel exampleŸ±Çbs2a"Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1xJ# Plot two crossing lines and label each angle between them with the aboveŸ±Ç`a
Ÿ±Çbc1x# ``AngleAnnotation`` tool.Ÿ±Ç`a
Ÿ±Ç`fcenterŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`a(Ÿ±Çbmfc4.5Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmic650Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`bp1Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`a[Ÿ±Ç`a(Ÿ±Çbmfc2.5Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmic710Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`a(Ÿ±Çbmfc6.0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmic605Ÿ±Ç`a)Ÿ±Ç`a]Ÿ±Ç`a
Ÿ±Ç`bp2Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`a[Ÿ±Ç`a(Ÿ±Çbmfc3.0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmic275Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`a(Ÿ±Çbmfc5.5Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmic900Ÿ±Ç`a)Ÿ±Ç`a]Ÿ±Ç`a
Ÿ±Ç`eline1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`dplotŸ±Ç`a(Ÿ±Çaoa*Ÿ±ÇbnbczipŸ±Ç`a(Ÿ±Çaoa*Ÿ±Ç`bp1Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`eline2Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`dplotŸ±Ç`a(Ÿ±Çaoa*Ÿ±ÇbnbczipŸ±Ç`a(Ÿ±Çaoa*Ÿ±Ç`bp2Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`epointŸ±Ç`a,Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`dplotŸ±Ç`a(Ÿ±Çaoa*Ÿ±Ç`fcenterŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`fmarkerŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2aoŸ±Çbs2a"Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`cam1Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`oAngleAnnotationŸ±Ç`a(Ÿ±Ç`fcenterŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`bp1Ÿ±Ç`a[Ÿ±Çbmia1Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`bp2Ÿ±Ç`a[Ÿ±Çbmia1Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`baxŸ±Çaoa=Ÿ±Ç`baxŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dsizeŸ±Çaoa=Ÿ±Çbmib75Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dtextŸ±Çaoa=Ÿ±ÇbsaarŸ±Çbs2a"Ÿ±Çbs2a$Ÿ±Çbs2a\Ÿ±Çbs2falpha$Ÿ±Çbs2a"Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cam2Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`oAngleAnnotationŸ±Ç`a(Ÿ±Ç`fcenterŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`bp2Ÿ±Ç`a[Ÿ±Çbmia1Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`bp1Ÿ±Ç`a[Ÿ±Çbmia0Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`baxŸ±Çaoa=Ÿ±Ç`baxŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dsizeŸ±Çaoa=Ÿ±Çbmib35Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dtextŸ±Çaoa=Ÿ±ÇbsaarŸ±Çbs2a"Ÿ±Çbs2a$Ÿ±Çbs2a\Ÿ±Çbs2ebeta$Ÿ±Çbs2a"Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cam3Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`oAngleAnnotationŸ±Ç`a(Ÿ±Ç`fcenterŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`bp1Ÿ±Ç`a[Ÿ±Çbmia0Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`bp2Ÿ±Ç`a[Ÿ±Çbmia0Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`baxŸ±Çaoa=Ÿ±Ç`baxŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dsizeŸ±Çaoa=Ÿ±Çbmib75Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dtextŸ±Çaoa=Ÿ±ÇbsaarŸ±Çbs2a"Ÿ±Çbs2a$Ÿ±Çbs2a\Ÿ±Çbs2fgamma$Ÿ±Çbs2a"Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cam4Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`oAngleAnnotationŸ±Ç`a(Ÿ±Ç`fcenterŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`bp2Ÿ±Ç`a[Ÿ±Çbmia0Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`bp1Ÿ±Ç`a[Ÿ±Çbmia1Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`baxŸ±Çaoa=Ÿ±Ç`baxŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dsizeŸ±Çaoa=Ÿ±Çbmib35Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dtextŸ±Çaoa=Ÿ±ÇbsaarŸ±Çbs2a"Ÿ±Çbs2a$Ÿ±Çbs2a\Ÿ±Çbs2ftheta$Ÿ±Çbs2a"Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1xG# Showcase some styling options for the angle arc, as well as the text.Ÿ±Ç`a
Ÿ±Ç`apŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`a[Ÿ±Ç`a(Ÿ±Çbmfc6.0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmic400Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`a(Ÿ±Çbmfc5.3Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmic410Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`a(Ÿ±Çbmfc5.6Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmic300Ÿ±Ç`a)Ÿ±Ç`a]Ÿ±Ç`a
Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`dplotŸ±Ç`a(Ÿ±Çaoa*Ÿ±ÇbnbczipŸ±Ç`a(Ÿ±Çaoa*Ÿ±Ç`apŸ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cam5Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`oAngleAnnotationŸ±Ç`a(Ÿ±Ç`apŸ±Ç`a[Ÿ±Çbmia1Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`apŸ±Ç`a[Ÿ±Çbmia0Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`apŸ±Ç`a[Ÿ±Çbmia2Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`baxŸ±Çaoa=Ÿ±Ç`baxŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dsizeŸ±Çaoa=Ÿ±Çbmib40Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dtextŸ±Çaoa=Ÿ±ÇbsaarŸ±Çbs2a"Ÿ±Çbs2a$Ÿ±Çbs2a\Ÿ±Çbs2dPhi$Ÿ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`v                      Ÿ±Ç`ilinestyleŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2b--Ÿ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ecolorŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2dgrayŸ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ltextpositionŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2goutsideŸ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`v                      Ÿ±Ç`gtext_kwŸ±Çaoa=Ÿ±ÇbnbddictŸ±Ç`a(Ÿ±Ç`hfontsizeŸ±Çaoa=Ÿ±Çbmib16Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ecolorŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2dgrayŸ±Çbs2a"Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1xI#########################################################################Ÿ±Ç`a
Ÿ±Çbc1x# ``AngleLabel`` optionsŸ±Ç`a
Ÿ±Çbc1x# ~~~~~~~~~~~~~~~~~~~~~~Ÿ±Ç`a
Ÿ±Çbc1a#Ÿ±Ç`a
Ÿ±Çbc1xK# The *textposition* and *unit* keyword arguments may be used to modify theŸ±Ç`a
Ÿ±Çbc1x-# location of the text label, as shown below:Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1x'# Helper function to draw angle easily.Ÿ±Ç`a
Ÿ±ÇakcdefŸ±Ç`a Ÿ±Çbnfjplot_angleŸ±Ç`a(Ÿ±Ç`baxŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`cposŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`eangleŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`flengthŸ±Çaoa=Ÿ±Çbmfd0.95Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dacolŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2bC0Ÿ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çaoa*Ÿ±Çaoa*Ÿ±Ç`fkwargsŸ±Ç`a)Ÿ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`dvec2Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`earrayŸ±Ç`a(Ÿ±Ç`a[Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`ccosŸ±Ç`a(Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`gdeg2radŸ±Ç`a(Ÿ±Ç`eangleŸ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`csinŸ±Ç`a(Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`gdeg2radŸ±Ç`a(Ÿ±Ç`eangleŸ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a]Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`bxyŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`bc_Ÿ±Ç`a[Ÿ±Ç`a[Ÿ±Ç`flengthŸ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia0Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`a[Ÿ±Çbmia0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia0Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dvec2Ÿ±Çaoa*Ÿ±Ç`flengthŸ±Ç`a]Ÿ±Çaoa.Ÿ±Ç`aTŸ±Ç`a Ÿ±Çaoa+Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`earrayŸ±Ç`a(Ÿ±Ç`cposŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`dplotŸ±Ç`a(Ÿ±Çaoa*Ÿ±Ç`bxyŸ±Çaoa.Ÿ±Ç`aTŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ecolorŸ±Çaoa=Ÿ±Ç`dacolŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±ÇakfreturnŸ±Ç`a Ÿ±Ç`oAngleAnnotationŸ±Ç`a(Ÿ±Ç`cposŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`bxyŸ±Ç`a[Ÿ±Çbmia0Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`bxyŸ±Ç`a[Ÿ±Çbmia2Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`baxŸ±Çaoa=Ÿ±Ç`baxŸ±Ç`a,Ÿ±Ç`a Ÿ±Çaoa*Ÿ±Çaoa*Ÿ±Ç`fkwargsŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`cfigŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`a(Ÿ±Ç`cax1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`cax2Ÿ±Ç`a)Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`hsubplotsŸ±Ç`a(Ÿ±Ç`enrowsŸ±Çaoa=Ÿ±Çbmia2Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`fsharexŸ±Çaoa=Ÿ±ÇbkcdTrueŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cfigŸ±Çaoa.Ÿ±Ç`hsuptitleŸ±Ç`a(Ÿ±Çbs2a"Ÿ±Çbs2xAngleLabel keyword argumentsŸ±Çbs2a"Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cfigŸ±Çaoa.Ÿ±Ç`fcanvasŸ±Çaoa.Ÿ±Ç`ddrawŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`b  Ÿ±Çbc1x,# Need to draw the figure to define rendererŸ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1x$# Showcase different text positions.Ÿ±Ç`a
Ÿ±Ç`cax1Ÿ±Çaoa.Ÿ±Ç`gmarginsŸ±Ç`a(Ÿ±Ç`ayŸ±Çaoa=Ÿ±Çbmfc0.4Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cax1Ÿ±Çaoa.Ÿ±Ç`iset_titleŸ±Ç`a(Ÿ±Çbs2a"Ÿ±Çbs2ltextpositionŸ±Çbs2a"Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`bkwŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±ÇbnbddictŸ±Ç`a(Ÿ±Ç`dsizeŸ±Çaoa=Ÿ±Çbmib75Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dunitŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2fpointsŸ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dtextŸ±Çaoa=Ÿ±ÇbsaarŸ±Çbs2a"Ÿ±Çbs2f$60¬∞$Ÿ±Çbs2a"Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`cam6Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`jplot_angleŸ±Ç`a(Ÿ±Ç`cax1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`a(Ÿ±Çbmfc2.0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia0Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmib60Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ltextpositionŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2finsideŸ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çaoa*Ÿ±Çaoa*Ÿ±Ç`bkwŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cam7Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`jplot_angleŸ±Ç`a(Ÿ±Ç`cax1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`a(Ÿ±Çbmfc3.5Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia0Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmib60Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ltextpositionŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2goutsideŸ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çaoa*Ÿ±Çaoa*Ÿ±Ç`bkwŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cam8Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`jplot_angleŸ±Ç`a(Ÿ±Ç`cax1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`a(Ÿ±Çbmfc5.0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia0Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmib60Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ltextpositionŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2dedgeŸ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`q                 Ÿ±Ç`gtext_kwŸ±Çaoa=Ÿ±ÇbnbddictŸ±Ç`a(Ÿ±Ç`dbboxŸ±Çaoa=Ÿ±ÇbnbddictŸ±Ç`a(Ÿ±Ç`hboxstyleŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2eroundŸ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`bfcŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2awŸ±Çbs2a"Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çaoa*Ÿ±Çaoa*Ÿ±Ç`bkwŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cam9Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`jplot_angleŸ±Ç`a(Ÿ±Ç`cax1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`a(Ÿ±Çbmfc6.5Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia0Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmib60Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ltextpositionŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2dedgeŸ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`q                 Ÿ±Ç`gtext_kwŸ±Çaoa=Ÿ±ÇbnbddictŸ±Ç`a(Ÿ±Ç`fxytextŸ±Çaoa=Ÿ±Ç`a(Ÿ±Çbmib30Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmib20Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`jarrowpropsŸ±Çaoa=Ÿ±ÇbnbddictŸ±Ç`a(Ÿ±Ç`jarrowstyleŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2b->Ÿ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`x                              Ÿ±Ç`oconnectionstyleŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2marc3,rad=-0.2Ÿ±Çbs2a"Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çaoa*Ÿ±Çaoa*Ÿ±Ç`bkwŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±ÇakcforŸ±Ç`a Ÿ±Ç`axŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dtextŸ±Ç`a Ÿ±ÇbowbinŸ±Ç`a Ÿ±ÇbnbczipŸ±Ç`a(Ÿ±Ç`a[Ÿ±Çbmfc2.0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfc3.5Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfc5.0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfc6.5Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`a[Ÿ±Çbs1a'Ÿ±Çbs1a"Ÿ±Çbs1finsideŸ±Çbs1a"Ÿ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1a"Ÿ±Çbs1goutsideŸ±Çbs1a"Ÿ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1a"Ÿ±Çbs1dedgeŸ±Çbs1a"Ÿ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`x*                                          Ÿ±Çbs1a'Ÿ±Çbs1a"Ÿ±Çbs1dedgeŸ±Çbs1a"Ÿ±Çbs1n, custom arrowŸ±Çbs1a'Ÿ±Ç`a]Ÿ±Ç`a)Ÿ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`cax1Ÿ±Çaoa.Ÿ±Ç`hannotateŸ±Ç`a(Ÿ±Ç`dtextŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`bxyŸ±Çaoa=Ÿ±Ç`a(Ÿ±Ç`axŸ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia0Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`hxycoordsŸ±Çaoa=Ÿ±Ç`cax1Ÿ±Çaoa.Ÿ±Ç`sget_xaxis_transformŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`q                 Ÿ±Ç`dbboxŸ±Çaoa=Ÿ±ÇbnbddictŸ±Ç`a(Ÿ±Ç`hboxstyleŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2eroundŸ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`bfcŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2awŸ±Çbs2a"Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`bhaŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2dleftŸ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`hfontsizeŸ±Çaoa=Ÿ±Çbmia8Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`q                 Ÿ±Ç`oannotation_clipŸ±Çaoa=Ÿ±ÇbkcdTrueŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1xH# Showcase different size units. The effect of this can best be observedŸ±Ç`a
Ÿ±Çbc1x+# by interactively changing the figure sizeŸ±Ç`a
Ÿ±Ç`cax2Ÿ±Çaoa.Ÿ±Ç`gmarginsŸ±Ç`a(Ÿ±Ç`ayŸ±Çaoa=Ÿ±Çbmfc0.4Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cax2Ÿ±Çaoa.Ÿ±Ç`iset_titleŸ±Ç`a(Ÿ±Çbs2a"Ÿ±Çbs2dunitŸ±Çbs2a"Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`bkwŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±ÇbnbddictŸ±Ç`a(Ÿ±Ç`dtextŸ±Çaoa=Ÿ±ÇbsaarŸ±Çbs2a"Ÿ±Çbs2f$60¬∞$Ÿ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ltextpositionŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2goutsideŸ±Çbs2a"Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`dam10Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`jplot_angleŸ±Ç`a(Ÿ±Ç`cax2Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`a(Ÿ±Çbmfc2.0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia0Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmib60Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dsizeŸ±Çaoa=Ÿ±Çbmib50Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dunitŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2fpixelsŸ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çaoa*Ÿ±Çaoa*Ÿ±Ç`bkwŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`dam11Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`jplot_angleŸ±Ç`a(Ÿ±Ç`cax2Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`a(Ÿ±Çbmfc3.5Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia0Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmib60Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dsizeŸ±Çaoa=Ÿ±Çbmib50Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dunitŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2fpointsŸ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çaoa*Ÿ±Çaoa*Ÿ±Ç`bkwŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`dam12Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`jplot_angleŸ±Ç`a(Ÿ±Ç`cax2Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`a(Ÿ±Çbmfc5.0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia0Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmib60Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dsizeŸ±Çaoa=Ÿ±Çbmfd0.25Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dunitŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2haxes minŸ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çaoa*Ÿ±Çaoa*Ÿ±Ç`bkwŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`dam13Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`jplot_angleŸ±Ç`a(Ÿ±Ç`cax2Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`a(Ÿ±Çbmfc6.5Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia0Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmib60Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dsizeŸ±Çaoa=Ÿ±Çbmfd0.25Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dunitŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2haxes maxŸ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çaoa*Ÿ±Çaoa*Ÿ±Ç`bkwŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±ÇakcforŸ±Ç`a Ÿ±Ç`axŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dtextŸ±Ç`a Ÿ±ÇbowbinŸ±Ç`a Ÿ±ÇbnbczipŸ±Ç`a(Ÿ±Ç`a[Ÿ±Çbmfc2.0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfc3.5Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfc5.0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfc6.5Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`a[Ÿ±Çbs1a'Ÿ±Çbs1a"Ÿ±Çbs1fpixelsŸ±Çbs1a"Ÿ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1a"Ÿ±Çbs1fpointsŸ±Çbs1a"Ÿ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`x*                                          Ÿ±Çbs1a'Ÿ±Çbs1a"Ÿ±Çbs1haxes minŸ±Çbs1a"Ÿ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1a"Ÿ±Çbs1haxes maxŸ±Çbs1a"Ÿ±Çbs1a'Ÿ±Ç`a]Ÿ±Ç`a)Ÿ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`cax2Ÿ±Çaoa.Ÿ±Ç`hannotateŸ±Ç`a(Ÿ±Ç`dtextŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`bxyŸ±Çaoa=Ÿ±Ç`a(Ÿ±Ç`axŸ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia0Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`hxycoordsŸ±Çaoa=Ÿ±Ç`cax2Ÿ±Çaoa.Ÿ±Ç`sget_xaxis_transformŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`q                 Ÿ±Ç`dbboxŸ±Çaoa=Ÿ±ÇbnbddictŸ±Ç`a(Ÿ±Ç`hboxstyleŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2eroundŸ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`bfcŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2awŸ±Çbs2a"Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`bhaŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2dleftŸ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`hfontsizeŸ±Çaoa=Ÿ±Çbmia8Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`q                 Ÿ±Ç`oannotation_clipŸ±Çaoa=Ÿ±ÇbkcdTrueŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`dshowŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1xM#############################################################################Ÿ±Ç`a
Ÿ±Çbc1a#Ÿ±Ç`a
Ÿ±Çbc1x# .. admonition:: ReferencesŸ±Ç`a
Ÿ±Çbc1a#Ÿ±Ç`a
Ÿ±Çbc1xN#    The use of the following functions, methods, classes and modules is shownŸ±Ç`a
Ÿ±Çbc1u#    in this example:Ÿ±Ç`a
Ÿ±Çbc1a#Ÿ±Ç`a
Ÿ±Çbc1x#    - `matplotlib.patches.Arc`Ÿ±Ç`a
Ÿ±Çbc1xE#    - `matplotlib.axes.Axes.annotate` / `matplotlib.pyplot.annotate`Ÿ±Ç`a
Ÿ±Çbc1x##    - `matplotlib.text.Annotation`Ÿ±Ç`a
Ÿ±Çbc1x0#    - `matplotlib.transforms.IdentityTransform`Ÿ±Ç`a
Ÿ±Çbc1x.#    - `matplotlib.transforms.TransformedBbox`Ÿ±Ç`a
Ÿ±Çbc1x##    - `matplotlib.transforms.Bbox`Ÿ±Ç`a
`dNoneˆ