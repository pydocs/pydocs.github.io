������������bsdy\"""
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
"""���`a
���`a
���bc1xI#########################################################################���`a
���bc1w# AngleAnnotation class���`a
���bc1w# ~~~~~~~~~~~~~~~~~~~~~���`a
���bc1xN# The essential idea here is to subclass `~.patches.Arc` and set its transform���`a
���bc1xK# to the `~.transforms.IdentityTransform`, making the parameters of the arc���`a
���bc1x# defined in pixel space.���`a
���bc1xD# We then override the ``Arc``'s attributes ``_center``, ``theta1``,���`a
���bc1xL# ``theta2``, ``width`` and ``height`` and make them properties, coupling to���`a
���bc1xI# internal methods that calculate the respective parameters each time the���`a
���bc1xN# attribute is accessed and thereby ensuring that the arc in pixel space stays���`a
���bc1x.# synchronized with the input points and size.���`a
���bc1xM# For example, each time the arc's drawing method would query its ``_center``���`a
���bc1xI# attribute, instead of receiving the same number all over again, it will���`a
���bc1xN# instead receive the result of the ``get_center_in_pixels`` method we defined���`a
���bc1xK# in the subclass. This method transforms the center in data coordinates to���`a
���bc1xM# pixels via the Axes transform ``ax.transData``. The size and the angles are���`a
���bc1xF# calculated in a similar fashion, such that the arc changes its shape���`a
���bc1x;# automatically when e.g. zooming or panning interactively.���`a
���bc1a#���`a
���bc1xN# The functionality of this class allows to annotate the arc with a text. This���`a
���bc1xJ# text is a `~.text.Annotation` stored in an attribute ``text``. Since the���`a
���bc1xL# arc's position and radius are defined only at draw time, we need to update���`a
���bc1xO# the text's position accordingly. This is done by reimplementing the ``Arc``'s���`a
���bc1xC# ``draw()`` method to let it call an updating method for the text.���`a
���bc1a#���`a
���bc1xN# The arc and the text will be added to the provided Axes at instantiation: it���`a
���bc1x<# is hence not strictly necessary to keep a reference to it.���`a
���`a
���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���bkndfrom���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnngpatches���`a ���bknfimport���`a ���`cArc���`a
���bkndfrom���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnjtransforms���`a ���bknfimport���`a ���`qIdentityTransform���`a,���`a ���`oTransformedBbox���`a,���`a ���`dBbox���`a
���`a
���`a
���akeclass���`a ���bncoAngleAnnotation���`a(���`cArc���`a)���`a:���`a
���`d    ���bsdxY"""
    Draws an arc between two vectors which appears circular in display space.
    """���`a
���`d    ���akcdef���`a ���bfmh__init__���`a(���bbpdself���`a,���`a ���`bxy���`a,���`a ���`bp1���`a,���`a ���`bp2���`a,���`a ���`dsize���aoa=���bmib75���`a,���`a ���`dunit���aoa=���bs2a"���bs2fpoints���bs2a"���`a,���`a ���`bax���aoa=���bkcdNone���`a,���`a
���`q                 ���`dtext���aoa=���bs2a"���bs2a"���`a,���`a ���`ltextposition���aoa=���bs2a"���bs2finside���bs2a"���`a,���`a ���`gtext_kw���aoa=���bkcdNone���`a,���`a ���aoa*���aoa*���`fkwargs���`a)���`a:���`a
���`h        ���bsdy~"""
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

        """���`a
���`h        ���bbpdself���aoa.���`bax���`a ���aoa=���`a ���`bax���`a ���bowbor���`a ���`cplt���aoa.���`cgca���`a(���`a)���`a
���`h        ���bbpdself���aoa.���`g_xydata���`a ���aoa=���`a ���`bxy���`b  ���bc1u# in data coordinates���`a
���`h        ���bbpdself���aoa.���`dvec1���`a ���aoa=���`a ���`bp1���`a
���`h        ���bbpdself���aoa.���`dvec2���`a ���aoa=���`a ���`bp2���`a
���`h        ���bbpdself���aoa.���`dsize���`a ���aoa=���`a ���`dsize���`a
���`h        ���bbpdself���aoa.���`dunit���`a ���aoa=���`a ���`dunit���`a
���`h        ���bbpdself���aoa.���`ltextposition���`a ���aoa=���`a ���`ltextposition���`a
���`a
���`h        ���bnbesuper���`a(���`a)���aoa.���bfmh__init__���`a(���bbpdself���aoa.���`g_xydata���`a,���`a ���`dsize���`a,���`a ���`dsize���`a,���`a ���`eangle���aoa=���bmfc0.0���`a,���`a
���`x                         ���`ftheta1���aoa=���bbpdself���aoa.���`ftheta1���`a,���`a ���`ftheta2���aoa=���bbpdself���aoa.���`ftheta2���`a,���`a ���aoa*���aoa*���`fkwargs���`a)���`a
���`a
���`h        ���bbpdself���aoa.���`mset_transform���`a(���`qIdentityTransform���`a(���`a)���`a)���`a
���`h        ���bbpdself���aoa.���`bax���aoa.���`iadd_patch���`a(���bbpdself���`a)���`a
���`a
���`h        ���bbpdself���aoa.���`bkw���`a ���aoa=���`a ���bnbddict���`a(���`bha���aoa=���bs2a"���bs2fcenter���bs2a"���`a,���`a ���`bva���aoa=���bs2a"���bs2fcenter���bs2a"���`a,���`a
���`w                       ���`hxycoords���aoa=���`qIdentityTransform���`a(���`a)���`a,���`a
���`w                       ���`fxytext���aoa=���`a(���bmia0���`a,���`a ���bmia0���`a)���`a,���`a ���`jtextcoords���aoa=���bs2a"���bs2moffset points���bs2a"���`a,���`a
���`w                       ���`oannotation_clip���aoa=���bkcdTrue���`a)���`a
���`h        ���bbpdself���aoa.���`bkw���aoa.���`fupdate���`a(���`gtext_kw���`a ���bowbor���`a ���`a{���`a}���`a)���`a
���`h        ���bbpdself���aoa.���`dtext���`a ���aoa=���`a ���`bax���aoa.���`hannotate���`a(���`dtext���`a,���`a ���`bxy���aoa=���bbpdself���aoa.���`g_center���`a,���`a ���aoa*���aoa*���bbpdself���aoa.���`bkw���`a)���`a
���`a
���`d    ���akcdef���`a ���bnfhget_size���`a(���bbpdself���`a)���`a:���`a
���`h        ���`ffactor���`a ���aoa=���`a ���bmfb1.���`a
���`h        ���akbif���`a ���bbpdself���aoa.���`dunit���`a ���aob==���`a ���bs2a"���bs2fpoints���bs2a"���`a:���`a
���`l            ���`ffactor���`a ���aoa=���`a ���bbpdself���aoa.���`bax���aoa.���`ffigure���aoa.���`cdpi���`a ���aoa/���`a ���bmfc72.���`a
���`h        ���akdelif���`a ���bbpdself���aoa.���`dunit���`a[���`a:���bmia4���`a]���`a ���aob==���`a ���bs2a"���bs2daxes���bs2a"���`a:���`a
���`l            ���`ab���`a ���aoa=���`a ���`oTransformedBbox���`a(���`dBbox���aoa.���`kfrom_bounds���`a(���bmia0���`a,���`a ���bmia0���`a,���`a ���bmia1���`a,���`a ���bmia1���`a)���`a,���`a
���`x                                 ���bbpdself���aoa.���`bax���aoa.���`itransAxes���`a)���`a
���`l            ���`cdic���`a ���aoa=���`a ���`a{���bs2a"���bs2cmax���bs2a"���`a:���`a ���bnbcmax���`a(���`ab���aoa.���`ewidth���`a,���`a ���`ab���aoa.���`fheight���`a)���`a,���`a
���`s                   ���bs2a"���bs2cmin���bs2a"���`a:���`a ���bnbcmin���`a(���`ab���aoa.���`ewidth���`a,���`a ���`ab���aoa.���`fheight���`a)���`a,���`a
���`s                   ���bs2a"���bs2ewidth���bs2a"���`a:���`a ���`ab���aoa.���`ewidth���`a,���`a ���bs2a"���bs2fheight���bs2a"���`a:���`a ���`ab���aoa.���`fheight���`a}���`a
���`l            ���`ffactor���`a ���aoa=���`a ���`cdic���`a[���bbpdself���aoa.���`dunit���`a[���bmia5���`a:���`a]���`a]���`a
���`h        ���akfreturn���`a ���bbpdself���aoa.���`dsize���`a ���aoa*���`a ���`ffactor���`a
���`a
���`d    ���akcdef���`a ���bnfhset_size���`a(���bbpdself���`a,���`a ���`dsize���`a)���`a:���`a
���`h        ���bbpdself���aoa.���`dsize���`a ���aoa=���`a ���`dsize���`a
���`a
���`d    ���akcdef���`a ���bnftget_center_in_pixels���`a(���bbpdself���`a)���`a:���`a
���`h        ���bsdx"""return center in pixels"""���`a
���`h        ���akfreturn���`a ���bbpdself���aoa.���`bax���aoa.���`itransData���aoa.���`itransform���`a(���bbpdself���aoa.���`g_xydata���`a)���`a
���`a
���`d    ���akcdef���`a ���bnfjset_center���`a(���bbpdself���`a,���`a ���`bxy���`a)���`a:���`a
���`h        ���bsdx$"""set center in data coordinates"""���`a
���`h        ���bbpdself���aoa.���`g_xydata���`a ���aoa=���`a ���`bxy���`a
���`a
���`d    ���akcdef���`a ���bnfiget_theta���`a(���bbpdself���`a,���`a ���`cvec���`a)���`a:���`a
���`h        ���`mvec_in_pixels���`a ���aoa=���`a ���bbpdself���aoa.���`bax���aoa.���`itransData���aoa.���`itransform���`a(���`cvec���`a)���`a ���aoa-���`a ���bbpdself���aoa.���`g_center���`a
���`h        ���akfreturn���`a ���`bnp���aoa.���`grad2deg���`a(���`bnp���aoa.���`garctan2���`a(���`mvec_in_pixels���`a[���bmia1���`a]���`a,���`a ���`mvec_in_pixels���`a[���bmia0���`a]���`a)���`a)���`a
���`a
���`d    ���akcdef���`a ���bnfjget_theta1���`a(���bbpdself���`a)���`a:���`a
���`h        ���akfreturn���`a ���bbpdself���aoa.���`iget_theta���`a(���bbpdself���aoa.���`dvec1���`a)���`a
���`a
���`d    ���akcdef���`a ���bnfjget_theta2���`a(���bbpdself���`a)���`a:���`a
���`h        ���akfreturn���`a ���bbpdself���aoa.���`iget_theta���`a(���bbpdself���aoa.���`dvec2���`a)���`a
���`a
���`d    ���akcdef���`a ���bnfiset_theta���`a(���bbpdself���`a,���`a ���`eangle���`a)���`a:���`a
���`h        ���akdpass���`a
���`a
���`d    ���bc1xE# Redefine attributes of the Arc to always give values in pixel space���`a
���`d    ���`g_center���`a ���aoa=���`a ���bnbhproperty���`a(���`tget_center_in_pixels���`a,���`a ���`jset_center���`a)���`a
���`d    ���`ftheta1���`a ���aoa=���`a ���bnbhproperty���`a(���`jget_theta1���`a,���`a ���`iset_theta���`a)���`a
���`d    ���`ftheta2���`a ���aoa=���`a ���bnbhproperty���`a(���`jget_theta2���`a,���`a ���`iset_theta���`a)���`a
���`d    ���`ewidth���`a ���aoa=���`a ���bnbhproperty���`a(���`hget_size���`a,���`a ���`hset_size���`a)���`a
���`d    ���`fheight���`a ���aoa=���`a ���bnbhproperty���`a(���`hget_size���`a,���`a ���`hset_size���`a)���`a
���`a
���`d    ���bc1xC# The following two methods are needed to update the text position.���`a
���`d    ���akcdef���`a ���bnfddraw���`a(���bbpdself���`a,���`a ���`hrenderer���`a)���`a:���`a
���`h        ���bbpdself���aoa.���`kupdate_text���`a(���`a)���`a
���`h        ���bnbesuper���`a(���`a)���aoa.���`ddraw���`a(���`hrenderer���`a)���`a
���`a
���`d    ���akcdef���`a ���bnfkupdate_text���`a(���bbpdself���`a)���`a:���`a
���`h        ���`ac���`a ���aoa=���`a ���bbpdself���aoa.���`g_center���`a
���`h        ���`as���`a ���aoa=���`a ���bbpdself���aoa.���`hget_size���`a(���`a)���`a
���`h        ���`jangle_span���`a ���aoa=���`a ���`a(���bbpdself���aoa.���`ftheta2���`a ���aoa-���`a ���bbpdself���aoa.���`ftheta1���`a)���`a ���aoa%���`a ���bmic360���`a
���`h        ���`eangle���`a ���aoa=���`a ���`bnp���aoa.���`gdeg2rad���`a(���bbpdself���aoa.���`ftheta1���`a ���aoa+���`a ���`jangle_span���`a ���aoa/���`a ���bmia2���`a)���`a
���`h        ���`ar���`a ���aoa=���`a ���`as���`a ���aoa/���`a ���bmia2���`a
���`h        ���akbif���`a ���bbpdself���aoa.���`ltextposition���`a ���aob==���`a ���bs2a"���bs2finside���bs2a"���`a:���`a
���`l            ���`ar���`a ���aoa=���`a ���`as���`a ���aoa/���`a ���`bnp���aoa.���`finterp���`a(���`jangle_span���`a,���`a ���`a[���bmib60���`a,���`a ���bmib90���`a,���`a ���bmic135���`a,���`a ���bmic180���`a]���`a,���`a
���`x*                                          ���`a[���bmfc3.3���`a,���`a ���bmfc3.5���`a,���`a ���bmfc3.8���`a,���`a ���bmia4���`a]���`a)���`a
���`h        ���bbpdself���aoa.���`dtext���aoa.���`bxy���`a ���aoa=���`a ���`ac���`a ���aoa+���`a ���`ar���`a ���aoa*���`a ���`bnp���aoa.���`earray���`a(���`a[���`bnp���aoa.���`ccos���`a(���`eangle���`a)���`a,���`a ���`bnp���aoa.���`csin���`a(���`eangle���`a)���`a]���`a)���`a
���`h        ���akbif���`a ���bbpdself���aoa.���`ltextposition���`a ���aob==���`a ���bs2a"���bs2goutside���bs2a"���`a:���`a
���`l            ���akcdef���`a ���bnfcR90���`a(���`aa���`a,���`a ���`ar���`a,���`a ���`aw���`a,���`a ���`ah���`a)���`a:���`a
���`p                ���akbif���`a ���`aa���`a ���aoa<���`a ���`bnp���aoa.���`farctan���`a(���`ah���aoa/���bmia2���aoa/���`a(���`ar���aoa+���`aw���aoa/���bmia2���`a)���`a)���`a:���`a
���`t                    ���akfreturn���`a ���`bnp���aoa.���`dsqrt���`a(���`a(���`ar���aoa+���`aw���aoa/���bmia2���`a)���aoa*���aoa*���bmia2���`a ���aoa+���`a ���`a(���`bnp���aoa.���`ctan���`a(���`aa���`a)���aoa*���`a(���`ar���aoa+���`aw���aoa/���bmia2���`a)���`a)���aoa*���aoa*���bmia2���`a)���`a
���`p                ���akdelse���`a:���`a
���`t                    ���`ac���`a ���aoa=���`a ���`bnp���aoa.���`dsqrt���`a(���`a(���`aw���aoa/���bmia2���`a)���aoa*���aoa*���bmia2���aoa+���`a(���`ah���aoa/���bmia2���`a)���aoa*���aoa*���bmia2���`a)���`a
���`t                    ���`aT���`a ���aoa=���`a ���`bnp���aoa.���`farcsin���`a(���`ac���`a ���aoa*���`a ���`bnp���aoa.���`ccos���`a(���`bnp���aoa.���`bpi���aoa/���bmia2���`a ���aoa-���`a ���`aa���`a ���aoa+���`a ���`bnp���aoa.���`farcsin���`a(���`ah���aoa/���bmia2���aoa/���`ac���`a)���`a)���aoa/���`ar���`a)���`a
���`t                    ���`bxy���`a ���aoa=���`a ���`ar���`a ���aoa*���`a ���`bnp���aoa.���`earray���`a(���`a[���`bnp���aoa.���`ccos���`a(���`aa���`a ���aoa+���`a ���`aT���`a)���`a,���`a ���`bnp���aoa.���`csin���`a(���`aa���`a ���aoa+���`a ���`aT���`a)���`a]���`a)���`a
���`t                    ���`bxy���`a ���aoa+���aoa=���`a ���`bnp���aoa.���`earray���`a(���`a[���`aw���aoa/���bmia2���`a,���`a ���`ah���aoa/���bmia2���`a]���`a)���`a
���`t                    ���akfreturn���`a ���`bnp���aoa.���`dsqrt���`a(���`bnp���aoa.���`csum���`a(���`bxy���aoa*���aoa*���bmia2���`a)���`a)���`a
���`a
���`l            ���akcdef���`a ���bnfaR���`a(���`aa���`a,���`a ���`ar���`a,���`a ���`aw���`a,���`a ���`ah���`a)���`a:���`a
���`p                ���`baa���`a ���aoa=���`a ���`a(���`aa���`a ���aoa%���`a ���`a(���`bnp���aoa.���`bpi���aoa/���bmia4���`a)���`a)���aoa*���`a(���`a(���`aa���`a ���aoa%���`a ���`a(���`bnp���aoa.���`bpi���aoa/���bmia2���`a)���`a)���`a ���aoa<���aoa=���`a ���`bnp���aoa.���`bpi���aoa/���bmia4���`a)���`a ���aoa+���`a ���`b\
���`u                     ���`a(���`bnp���aoa.���`bpi���aoa/���bmia4���`a ���aoa-���`a ���`a(���`aa���`a ���aoa%���`a ���`a(���`bnp���aoa.���`bpi���aoa/���bmia4���`a)���`a)���`a)���aoa*���`a(���`a(���`aa���`a ���aoa%���`a ���`a(���`bnp���aoa.���`bpi���aoa/���bmia2���`a)���`a)���`a ���aoa>���aoa=���`a ���`bnp���aoa.���`bpi���aoa/���bmia4���`a)���`a
���`p                ���akfreturn���`a ���`cR90���`a(���`baa���`a,���`a ���`ar���`a,���`a ���aoa*���`a[���`aw���`a,���`a ���`ah���`a]���`a[���`a:���`a:���bnbcint���`a(���`bnp���aoa.���`dsign���`a(���`bnp���aoa.���`ccos���`a(���bmia2���aoa*���`aa���`a)���`a)���`a)���`a]���`a)���`a
���`a
���`l            ���`dbbox���`a ���aoa=���`a ���bbpdself���aoa.���`dtext���aoa.���`qget_window_extent���`a(���`a)���`a
���`l            ���`aX���`a ���aoa=���`a ���`aR���`a(���`eangle���`a,���`a ���`ar���`a,���`a ���`dbbox���aoa.���`ewidth���`a,���`a ���`dbbox���aoa.���`fheight���`a)���`a
���`l            ���`etrans���`a ���aoa=���`a ���bbpdself���aoa.���`bax���aoa.���`ffigure���aoa.���`odpi_scale_trans���aoa.���`hinverted���`a(���`a)���`a
���`l            ���`doffs���`a ���aoa=���`a ���`etrans���aoa.���`itransform���`a(���`a(���`a(���`aX���aoa-���`as���aoa/���bmia2���`a)���`a,���`a ���bmia0���`a)���`a)���`a[���bmia0���`a]���`a ���aoa*���`a ���bmib72���`a
���`l            ���bbpdself���aoa.���`dtext���aoa.���`lset_position���`a(���`a[���`doffs���aoa*���`bnp���aoa.���`ccos���`a(���`eangle���`a)���`a,���`a ���`doffs���aoa*���`bnp���aoa.���`csin���`a(���`eangle���`a)���`a]���`a)���`a
���`a
���`a
���bc1xI#########################################################################���`a
���bc1x# .. _angle-annotation-usage:���`a
���bc1a#���`a
���bc1g# Usage���`a
���bc1g# ~~~~~���`a
���bc1a#���`a
���bc1xL# Required arguments to ``AngleAnnotation`` are the center of the arc, *xy*,���`a
���bc1xL# and two points, such that the arc spans between the two vectors connecting���`a
���bc1xM# *p1* and *p2* with *xy*, respectively. Those are given in data coordinates.���`a
���bc1xM# Further arguments are the *size* of the arc and its *unit*. Additionally, a���`a
���bc1xO# *text* can be specified, that will be drawn either in- or outside of the arc,���`a
���bc1xM# according to the value of *textposition*. Usage of those arguments is shown���`a
���bc1h# below.���`a
���`a
���`cfig���`a,���`a ���`bax���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`a)���`a
���`cfig���aoa.���`fcanvas���aoa.���`ddraw���`a(���`a)���`b  ���bc1x,# Need to draw the figure to define renderer���`a
���`bax���aoa.���`iset_title���`a(���bs2a"���bs2rAngleLabel example���bs2a"���`a)���`a
���`a
���bc1xJ# Plot two crossing lines and label each angle between them with the above���`a
���bc1x# ``AngleAnnotation`` tool.���`a
���`fcenter���`a ���aoa=���`a ���`a(���bmfc4.5���`a,���`a ���bmic650���`a)���`a
���`bp1���`a ���aoa=���`a ���`a[���`a(���bmfc2.5���`a,���`a ���bmic710���`a)���`a,���`a ���`a(���bmfc6.0���`a,���`a ���bmic605���`a)���`a]���`a
���`bp2���`a ���aoa=���`a ���`a[���`a(���bmfc3.0���`a,���`a ���bmic275���`a)���`a,���`a ���`a(���bmfc5.5���`a,���`a ���bmic900���`a)���`a]���`a
���`eline1���`a,���`a ���aoa=���`a ���`bax���aoa.���`dplot���`a(���aoa*���bnbczip���`a(���aoa*���`bp1���`a)���`a)���`a
���`eline2���`a,���`a ���aoa=���`a ���`bax���aoa.���`dplot���`a(���aoa*���bnbczip���`a(���aoa*���`bp2���`a)���`a)���`a
���`epoint���`a,���`a ���aoa=���`a ���`bax���aoa.���`dplot���`a(���aoa*���`fcenter���`a,���`a ���`fmarker���aoa=���bs2a"���bs2ao���bs2a"���`a)���`a
���`a
���`cam1���`a ���aoa=���`a ���`oAngleAnnotation���`a(���`fcenter���`a,���`a ���`bp1���`a[���bmia1���`a]���`a,���`a ���`bp2���`a[���bmia1���`a]���`a,���`a ���`bax���aoa=���`bax���`a,���`a ���`dsize���aoa=���bmib75���`a,���`a ���`dtext���aoa=���bsaar���bs2a"���bs2a$���bs2a\���bs2falpha$���bs2a"���`a)���`a
���`cam2���`a ���aoa=���`a ���`oAngleAnnotation���`a(���`fcenter���`a,���`a ���`bp2���`a[���bmia1���`a]���`a,���`a ���`bp1���`a[���bmia0���`a]���`a,���`a ���`bax���aoa=���`bax���`a,���`a ���`dsize���aoa=���bmib35���`a,���`a ���`dtext���aoa=���bsaar���bs2a"���bs2a$���bs2a\���bs2ebeta$���bs2a"���`a)���`a
���`cam3���`a ���aoa=���`a ���`oAngleAnnotation���`a(���`fcenter���`a,���`a ���`bp1���`a[���bmia0���`a]���`a,���`a ���`bp2���`a[���bmia0���`a]���`a,���`a ���`bax���aoa=���`bax���`a,���`a ���`dsize���aoa=���bmib75���`a,���`a ���`dtext���aoa=���bsaar���bs2a"���bs2a$���bs2a\���bs2fgamma$���bs2a"���`a)���`a
���`cam4���`a ���aoa=���`a ���`oAngleAnnotation���`a(���`fcenter���`a,���`a ���`bp2���`a[���bmia0���`a]���`a,���`a ���`bp1���`a[���bmia1���`a]���`a,���`a ���`bax���aoa=���`bax���`a,���`a ���`dsize���aoa=���bmib35���`a,���`a ���`dtext���aoa=���bsaar���bs2a"���bs2a$���bs2a\���bs2ftheta$���bs2a"���`a)���`a
���`a
���`a
���bc1xG# Showcase some styling options for the angle arc, as well as the text.���`a
���`ap���`a ���aoa=���`a ���`a[���`a(���bmfc6.0���`a,���`a ���bmic400���`a)���`a,���`a ���`a(���bmfc5.3���`a,���`a ���bmic410���`a)���`a,���`a ���`a(���bmfc5.6���`a,���`a ���bmic300���`a)���`a]���`a
���`bax���aoa.���`dplot���`a(���aoa*���bnbczip���`a(���aoa*���`ap���`a)���`a)���`a
���`cam5���`a ���aoa=���`a ���`oAngleAnnotation���`a(���`ap���`a[���bmia1���`a]���`a,���`a ���`ap���`a[���bmia0���`a]���`a,���`a ���`ap���`a[���bmia2���`a]���`a,���`a ���`bax���aoa=���`bax���`a,���`a ���`dsize���aoa=���bmib40���`a,���`a ���`dtext���aoa=���bsaar���bs2a"���bs2a$���bs2a\���bs2dPhi$���bs2a"���`a,���`a
���`v                      ���`ilinestyle���aoa=���bs2a"���bs2b--���bs2a"���`a,���`a ���`ecolor���aoa=���bs2a"���bs2dgray���bs2a"���`a,���`a ���`ltextposition���aoa=���bs2a"���bs2goutside���bs2a"���`a,���`a
���`v                      ���`gtext_kw���aoa=���bnbddict���`a(���`hfontsize���aoa=���bmib16���`a,���`a ���`ecolor���aoa=���bs2a"���bs2dgray���bs2a"���`a)���`a)���`a
���`a
���`a
���bc1xI#########################################################################���`a
���bc1x# ``AngleLabel`` options���`a
���bc1x# ~~~~~~~~~~~~~~~~~~~~~~���`a
���bc1a#���`a
���bc1xK# The *textposition* and *unit* keyword arguments may be used to modify the���`a
���bc1x-# location of the text label, as shown below:���`a
���`a
���`a
���bc1x'# Helper function to draw angle easily.���`a
���akcdef���`a ���bnfjplot_angle���`a(���`bax���`a,���`a ���`cpos���`a,���`a ���`eangle���`a,���`a ���`flength���aoa=���bmfd0.95���`a,���`a ���`dacol���aoa=���bs2a"���bs2bC0���bs2a"���`a,���`a ���aoa*���aoa*���`fkwargs���`a)���`a:���`a
���`d    ���`dvec2���`a ���aoa=���`a ���`bnp���aoa.���`earray���`a(���`a[���`bnp���aoa.���`ccos���`a(���`bnp���aoa.���`gdeg2rad���`a(���`eangle���`a)���`a)���`a,���`a ���`bnp���aoa.���`csin���`a(���`bnp���aoa.���`gdeg2rad���`a(���`eangle���`a)���`a)���`a]���`a)���`a
���`d    ���`bxy���`a ���aoa=���`a ���`bnp���aoa.���`bc_���`a[���`a[���`flength���`a,���`a ���bmia0���`a]���`a,���`a ���`a[���bmia0���`a,���`a ���bmia0���`a]���`a,���`a ���`dvec2���aoa*���`flength���`a]���aoa.���`aT���`a ���aoa+���`a ���`bnp���aoa.���`earray���`a(���`cpos���`a)���`a
���`d    ���`bax���aoa.���`dplot���`a(���aoa*���`bxy���aoa.���`aT���`a,���`a ���`ecolor���aoa=���`dacol���`a)���`a
���`d    ���akfreturn���`a ���`oAngleAnnotation���`a(���`cpos���`a,���`a ���`bxy���`a[���bmia0���`a]���`a,���`a ���`bxy���`a[���bmia2���`a]���`a,���`a ���`bax���aoa=���`bax���`a,���`a ���aoa*���aoa*���`fkwargs���`a)���`a
���`a
���`a
���`cfig���`a,���`a ���`a(���`cax1���`a,���`a ���`cax2���`a)���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`enrows���aoa=���bmia2���`a,���`a ���`fsharex���aoa=���bkcdTrue���`a)���`a
���`cfig���aoa.���`hsuptitle���`a(���bs2a"���bs2xAngleLabel keyword arguments���bs2a"���`a)���`a
���`cfig���aoa.���`fcanvas���aoa.���`ddraw���`a(���`a)���`b  ���bc1x,# Need to draw the figure to define renderer���`a
���`a
���bc1x$# Showcase different text positions.���`a
���`cax1���aoa.���`gmargins���`a(���`ay���aoa=���bmfc0.4���`a)���`a
���`cax1���aoa.���`iset_title���`a(���bs2a"���bs2ltextposition���bs2a"���`a)���`a
���`bkw���`a ���aoa=���`a ���bnbddict���`a(���`dsize���aoa=���bmib75���`a,���`a ���`dunit���aoa=���bs2a"���bs2fpoints���bs2a"���`a,���`a ���`dtext���aoa=���bsaar���bs2a"���bs2f$60°$���bs2a"���`a)���`a
���`a
���`cam6���`a ���aoa=���`a ���`jplot_angle���`a(���`cax1���`a,���`a ���`a(���bmfc2.0���`a,���`a ���bmia0���`a)���`a,���`a ���bmib60���`a,���`a ���`ltextposition���aoa=���bs2a"���bs2finside���bs2a"���`a,���`a ���aoa*���aoa*���`bkw���`a)���`a
���`cam7���`a ���aoa=���`a ���`jplot_angle���`a(���`cax1���`a,���`a ���`a(���bmfc3.5���`a,���`a ���bmia0���`a)���`a,���`a ���bmib60���`a,���`a ���`ltextposition���aoa=���bs2a"���bs2goutside���bs2a"���`a,���`a ���aoa*���aoa*���`bkw���`a)���`a
���`cam8���`a ���aoa=���`a ���`jplot_angle���`a(���`cax1���`a,���`a ���`a(���bmfc5.0���`a,���`a ���bmia0���`a)���`a,���`a ���bmib60���`a,���`a ���`ltextposition���aoa=���bs2a"���bs2dedge���bs2a"���`a,���`a
���`q                 ���`gtext_kw���aoa=���bnbddict���`a(���`dbbox���aoa=���bnbddict���`a(���`hboxstyle���aoa=���bs2a"���bs2eround���bs2a"���`a,���`a ���`bfc���aoa=���bs2a"���bs2aw���bs2a"���`a)���`a)���`a,���`a ���aoa*���aoa*���`bkw���`a)���`a
���`cam9���`a ���aoa=���`a ���`jplot_angle���`a(���`cax1���`a,���`a ���`a(���bmfc6.5���`a,���`a ���bmia0���`a)���`a,���`a ���bmib60���`a,���`a ���`ltextposition���aoa=���bs2a"���bs2dedge���bs2a"���`a,���`a
���`q                 ���`gtext_kw���aoa=���bnbddict���`a(���`fxytext���aoa=���`a(���bmib30���`a,���`a ���bmib20���`a)���`a,���`a ���`jarrowprops���aoa=���bnbddict���`a(���`jarrowstyle���aoa=���bs2a"���bs2b->���bs2a"���`a,���`a
���`x                              ���`oconnectionstyle���aoa=���bs2a"���bs2marc3,rad=-0.2���bs2a"���`a)���`a)���`a,���`a ���aoa*���aoa*���`bkw���`a)���`a
���`a
���akcfor���`a ���`ax���`a,���`a ���`dtext���`a ���bowbin���`a ���bnbczip���`a(���`a[���bmfc2.0���`a,���`a ���bmfc3.5���`a,���`a ���bmfc5.0���`a,���`a ���bmfc6.5���`a]���`a,���`a ���`a[���bs1a'���bs1a"���bs1finside���bs1a"���bs1a'���`a,���`a ���bs1a'���bs1a"���bs1goutside���bs1a"���bs1a'���`a,���`a ���bs1a'���bs1a"���bs1dedge���bs1a"���bs1a'���`a,���`a
���`x*                                          ���bs1a'���bs1a"���bs1dedge���bs1a"���bs1n, custom arrow���bs1a'���`a]���`a)���`a:���`a
���`d    ���`cax1���aoa.���`hannotate���`a(���`dtext���`a,���`a ���`bxy���aoa=���`a(���`ax���`a,���`a ���bmia0���`a)���`a,���`a ���`hxycoords���aoa=���`cax1���aoa.���`sget_xaxis_transform���`a(���`a)���`a,���`a
���`q                 ���`dbbox���aoa=���bnbddict���`a(���`hboxstyle���aoa=���bs2a"���bs2eround���bs2a"���`a,���`a ���`bfc���aoa=���bs2a"���bs2aw���bs2a"���`a)���`a,���`a ���`bha���aoa=���bs2a"���bs2dleft���bs2a"���`a,���`a ���`hfontsize���aoa=���bmia8���`a,���`a
���`q                 ���`oannotation_clip���aoa=���bkcdTrue���`a)���`a
���`a
���bc1xH# Showcase different size units. The effect of this can best be observed���`a
���bc1x+# by interactively changing the figure size���`a
���`cax2���aoa.���`gmargins���`a(���`ay���aoa=���bmfc0.4���`a)���`a
���`cax2���aoa.���`iset_title���`a(���bs2a"���bs2dunit���bs2a"���`a)���`a
���`bkw���`a ���aoa=���`a ���bnbddict���`a(���`dtext���aoa=���bsaar���bs2a"���bs2f$60°$���bs2a"���`a,���`a ���`ltextposition���aoa=���bs2a"���bs2goutside���bs2a"���`a)���`a
���`a
���`dam10���`a ���aoa=���`a ���`jplot_angle���`a(���`cax2���`a,���`a ���`a(���bmfc2.0���`a,���`a ���bmia0���`a)���`a,���`a ���bmib60���`a,���`a ���`dsize���aoa=���bmib50���`a,���`a ���`dunit���aoa=���bs2a"���bs2fpixels���bs2a"���`a,���`a ���aoa*���aoa*���`bkw���`a)���`a
���`dam11���`a ���aoa=���`a ���`jplot_angle���`a(���`cax2���`a,���`a ���`a(���bmfc3.5���`a,���`a ���bmia0���`a)���`a,���`a ���bmib60���`a,���`a ���`dsize���aoa=���bmib50���`a,���`a ���`dunit���aoa=���bs2a"���bs2fpoints���bs2a"���`a,���`a ���aoa*���aoa*���`bkw���`a)���`a
���`dam12���`a ���aoa=���`a ���`jplot_angle���`a(���`cax2���`a,���`a ���`a(���bmfc5.0���`a,���`a ���bmia0���`a)���`a,���`a ���bmib60���`a,���`a ���`dsize���aoa=���bmfd0.25���`a,���`a ���`dunit���aoa=���bs2a"���bs2haxes min���bs2a"���`a,���`a ���aoa*���aoa*���`bkw���`a)���`a
���`dam13���`a ���aoa=���`a ���`jplot_angle���`a(���`cax2���`a,���`a ���`a(���bmfc6.5���`a,���`a ���bmia0���`a)���`a,���`a ���bmib60���`a,���`a ���`dsize���aoa=���bmfd0.25���`a,���`a ���`dunit���aoa=���bs2a"���bs2haxes max���bs2a"���`a,���`a ���aoa*���aoa*���`bkw���`a)���`a
���`a
���akcfor���`a ���`ax���`a,���`a ���`dtext���`a ���bowbin���`a ���bnbczip���`a(���`a[���bmfc2.0���`a,���`a ���bmfc3.5���`a,���`a ���bmfc5.0���`a,���`a ���bmfc6.5���`a]���`a,���`a ���`a[���bs1a'���bs1a"���bs1fpixels���bs1a"���bs1a'���`a,���`a ���bs1a'���bs1a"���bs1fpoints���bs1a"���bs1a'���`a,���`a
���`x*                                          ���bs1a'���bs1a"���bs1haxes min���bs1a"���bs1a'���`a,���`a ���bs1a'���bs1a"���bs1haxes max���bs1a"���bs1a'���`a]���`a)���`a:���`a
���`d    ���`cax2���aoa.���`hannotate���`a(���`dtext���`a,���`a ���`bxy���aoa=���`a(���`ax���`a,���`a ���bmia0���`a)���`a,���`a ���`hxycoords���aoa=���`cax2���aoa.���`sget_xaxis_transform���`a(���`a)���`a,���`a
���`q                 ���`dbbox���aoa=���bnbddict���`a(���`hboxstyle���aoa=���bs2a"���bs2eround���bs2a"���`a,���`a ���`bfc���aoa=���bs2a"���bs2aw���bs2a"���`a)���`a,���`a ���`bha���aoa=���bs2a"���bs2dleft���bs2a"���`a,���`a ���`hfontsize���aoa=���bmia8���`a,���`a
���`q                 ���`oannotation_clip���aoa=���bkcdTrue���`a)���`a
���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
���`a
���`a
���bc1xM#############################################################################���`a
���bc1a#���`a
���bc1x# .. admonition:: References���`a
���bc1a#���`a
���bc1xN#    The use of the following functions, methods, classes and modules is shown���`a
���bc1u#    in this example:���`a
���bc1a#���`a
���bc1x#    - `matplotlib.patches.Arc`���`a
���bc1xE#    - `matplotlib.axes.Axes.annotate` / `matplotlib.pyplot.annotate`���`a
���bc1x##    - `matplotlib.text.Annotation`���`a
���bc1x0#    - `matplotlib.transforms.IdentityTransform`���`a
���bc1x.#    - `matplotlib.transforms.TransformedBbox`���`a
���bc1x##    - `matplotlib.transforms.Bbox`���`a
`dNone�