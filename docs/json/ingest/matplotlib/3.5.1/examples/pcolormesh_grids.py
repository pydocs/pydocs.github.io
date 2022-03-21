Ù¯‚Ù´ƒ™[Ù±‚bsdyg"""
============================
pcolormesh grids and shading
============================

`.axes.Axes.pcolormesh` and `~.axes.Axes.pcolor` have a few options for
how grids are laid out and the shading between the grid points.

Generally, if *Z* has shape *(M, N)* then the grid *X* and *Y* can be
specified with either shape *(M+1, N+1)* or *(M, N)*, depending on the
argument for the ``shading`` keyword argument.  Note that below we specify
vectors *x* as either length N or N+1 and *y* as length M or M+1, and
`~.axes.Axes.pcolormesh` internally makes the mesh matrices *X* and *Y* from
the input vectors.

"""Ù±‚`a
Ù±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnnfpyplotÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnncpltÙ±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„enumpyÙ „enumpyf1.22.3fmoduleenumpyfmoduleõÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnnbnpÙ±‚`a
Ù±‚`a
Ù±‚bc1xO###############################################################################Ù±‚`a
Ù±‚bc1n# Flat ShadingÙ±‚`a
Ù±‚bc1n# ------------Ù±‚`a
Ù±‚bc1a#Ù±‚`a
Ù±‚bc1xI# The grid specification with the least assumptions is ``shading='flat'``Ù±‚`a
Ù±‚bc1xO# and if the grid is one larger than the data in each dimension, i.e. has shapeÙ±‚`a
Ù±‚bc1xO# *(M+1, N+1)*.  In that case *X* and *Y* specify the corners of quadrilateralsÙ±‚`a
Ù±‚bc1xK# that are colored with the values in *Z*. Here we specify the edges of theÙ±‚`a
Ù±‚bc1x=# *(3, 5)* quadrilaterals with *X* and *Y* that are *(4, 6)*.Ù±‚`a
Ù±‚`a
Ù±‚`enrowsÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bmia3Ù±‚`a
Ù±‚`encolsÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bmia5Ù±‚`a
Ù±‚`aZÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`farangeÙ±‚`a(Ù±‚`enrowsÙ±‚`a Ù±‚aoa*Ù±‚`a Ù±‚`encolsÙ±‚`a)Ù±‚aoa.Ù±‚`greshapeÙ±‚`a(Ù±‚`enrowsÙ±‚`a,Ù±‚`a Ù±‚`encolsÙ±‚`a)Ù±‚`a
Ù±‚`axÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`farangeÙ±‚`a(Ù±‚`encolsÙ±‚`a Ù±‚aoa+Ù±‚`a Ù±‚bmia1Ù±‚`a)Ù±‚`a
Ù±‚`ayÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`farangeÙ±‚`a(Ù±‚`enrowsÙ±‚`a Ù±‚aoa+Ù±‚`a Ù±‚bmia1Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`cfigÙ±‚`a,Ù±‚`a Ù±‚`baxÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cpltÙ±‚aoa.Ù±‚`hsubplotsÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`jpcolormeshÙ±‚`a(Ù±‚`axÙ±‚`a,Ù±‚`a Ù±‚`ayÙ±‚`a,Ù±‚`a Ù±‚`aZÙ±‚`a,Ù±‚`a Ù±‚`gshadingÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1dflatÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`dvminÙ±‚aoa=Ù±‚`aZÙ±‚aoa.Ù±‚`cminÙ±‚`a(Ù±‚`a)Ù±‚`a,Ù±‚`a Ù±‚`dvmaxÙ±‚aoa=Ù±‚`aZÙ±‚aoa.Ù±‚`cmaxÙ±‚`a(Ù±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚akcdefÙ±‚`a Ù±‚bnfi_annotateÙ±‚`a(Ù±‚`baxÙ±‚`a,Ù±‚`a Ù±‚`axÙ±‚`a,Ù±‚`a Ù±‚`ayÙ±‚`a,Ù±‚`a Ù±‚`etitleÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`d    Ù±‚bc1x# this all gets repeated below:Ù±‚`a
Ù±‚`d    Ù±‚`aXÙ±‚`a,Ù±‚`a Ù±‚`aYÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`hmeshgridÙ±‚`a(Ù±‚`axÙ±‚`a,Ù±‚`a Ù±‚`ayÙ±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`baxÙ±‚aoa.Ù±‚`dplotÙ±‚`a(Ù±‚`aXÙ±‚aoa.Ù±‚`dflatÙ±‚`a,Ù±‚`a Ù±‚`aYÙ±‚aoa.Ù±‚`dflatÙ±‚`a,Ù±‚`a Ù±‚bs1a'Ù±‚bs1aoÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`ecolorÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1amÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`baxÙ±‚aoa.Ù±‚`hset_xlimÙ±‚`a(Ù±‚aoa-Ù±‚bmfc0.7Ù±‚`a,Ù±‚`a Ù±‚bmfc5.2Ù±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`baxÙ±‚aoa.Ù±‚`hset_ylimÙ±‚`a(Ù±‚aoa-Ù±‚bmfc0.7Ù±‚`a,Ù±‚`a Ù±‚bmfc3.2Ù±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`baxÙ±‚aoa.Ù±‚`iset_titleÙ±‚`a(Ù±‚`etitleÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`i_annotateÙ±‚`a(Ù±‚`baxÙ±‚`a,Ù±‚`a Ù±‚`axÙ±‚`a,Ù±‚`a Ù±‚`ayÙ±‚`a,Ù±‚`a Ù±‚bs2a"Ù±‚bs2hshading=Ù±‚bs2a'Ù±‚bs2dflatÙ±‚bs2a'Ù±‚bs2a"Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚bc1xO###############################################################################Ù±‚`a
Ù±‚bc1x# Flat Shading, same shape gridÙ±‚`a
Ù±‚bc1x# -----------------------------Ù±‚`a
Ù±‚bc1a#Ù±‚`a
Ù±‚bc1xL# Often, however, data is provided where *X* and *Y* match the shape of *Z*.Ù±‚`a
Ù±‚bc1xO# While this makes sense for other ``shading`` types, it is no longer permittedÙ±‚`a
Ù±‚bc1xN# when ``shading='flat'`` (and will raise a MatplotlibDeprecationWarning as ofÙ±‚`a
Ù±‚bc1xN# Matplotlib v3.3). Historically, Matplotlib silently dropped the last row andÙ±‚`a
Ù±‚bc1xM# column of *Z* in this case, to match Matlab's behavior. If this behavior isÙ±‚`a
Ù±‚bc1x># still desired, simply drop the last row and column manually:Ù±‚`a
Ù±‚`a
Ù±‚`axÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`farangeÙ±‚`a(Ù±‚`encolsÙ±‚`a)Ù±‚`b  Ù±‚bc1x # note *not* ncols + 1 as beforeÙ±‚`a
Ù±‚`ayÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`farangeÙ±‚`a(Ù±‚`enrowsÙ±‚`a)Ù±‚`a
Ù±‚`cfigÙ±‚`a,Ù±‚`a Ù±‚`baxÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cpltÙ±‚aoa.Ù±‚`hsubplotsÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`jpcolormeshÙ±‚`a(Ù±‚`axÙ±‚`a,Ù±‚`a Ù±‚`ayÙ±‚`a,Ù±‚`a Ù±‚`aZÙ±‚`a[Ù±‚`a:Ù±‚aoa-Ù±‚bmia1Ù±‚`a,Ù±‚`a Ù±‚`a:Ù±‚aoa-Ù±‚bmia1Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`gshadingÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1dflatÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`dvminÙ±‚aoa=Ù±‚`aZÙ±‚aoa.Ù±‚`cminÙ±‚`a(Ù±‚`a)Ù±‚`a,Ù±‚`a Ù±‚`dvmaxÙ±‚aoa=Ù±‚`aZÙ±‚aoa.Ù±‚`cmaxÙ±‚`a(Ù±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`i_annotateÙ±‚`a(Ù±‚`baxÙ±‚`a,Ù±‚`a Ù±‚`axÙ±‚`a,Ù±‚`a Ù±‚`ayÙ±‚`a,Ù±‚`a Ù±‚bs2a"Ù±‚bs2hshading=Ù±‚bs2a'Ù±‚bs2dflatÙ±‚bs2a'Ù±‚bs2t: X, Y, C same shapeÙ±‚bs2a"Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚bc1xO###############################################################################Ù±‚`a
Ù±‚bc1x"# Nearest Shading, same shape gridÙ±‚`a
Ù±‚bc1x"# --------------------------------Ù±‚`a
Ù±‚bc1a#Ù±‚`a
Ù±‚bc1xL# Usually, dropping a row and column of data is not what the user means whenÙ±‚`a
Ù±‚bc1xK# they make *X*, *Y* and *Z* all the same shape.  For this case, MatplotlibÙ±‚`a
Ù±‚bc1xL# allows ``shading='nearest'`` and centers the colored quadrilaterals on theÙ±‚`a
Ù±‚bc1n# grid points.Ù±‚`a
Ù±‚bc1a#Ù±‚`a
Ù±‚bc1xN# If a grid that is not the correct shape is passed with ``shading='nearest'``Ù±‚`a
Ù±‚bc1u# an error is raised.Ù±‚`a
Ù±‚`a
Ù±‚`cfigÙ±‚`a,Ù±‚`a Ù±‚`baxÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cpltÙ±‚aoa.Ù±‚`hsubplotsÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`jpcolormeshÙ±‚`a(Ù±‚`axÙ±‚`a,Ù±‚`a Ù±‚`ayÙ±‚`a,Ù±‚`a Ù±‚`aZÙ±‚`a,Ù±‚`a Ù±‚`gshadingÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1gnearestÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`dvminÙ±‚aoa=Ù±‚`aZÙ±‚aoa.Ù±‚`cminÙ±‚`a(Ù±‚`a)Ù±‚`a,Ù±‚`a Ù±‚`dvmaxÙ±‚aoa=Ù±‚`aZÙ±‚aoa.Ù±‚`cmaxÙ±‚`a(Ù±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`i_annotateÙ±‚`a(Ù±‚`baxÙ±‚`a,Ù±‚`a Ù±‚`axÙ±‚`a,Ù±‚`a Ù±‚`ayÙ±‚`a,Ù±‚`a Ù±‚bs2a"Ù±‚bs2hshading=Ù±‚bs2a'Ù±‚bs2gnearestÙ±‚bs2a'Ù±‚bs2a"Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚bc1xO###############################################################################Ù±‚`a
Ù±‚bc1n# Auto ShadingÙ±‚`a
Ù±‚bc1n# ------------Ù±‚`a
Ù±‚bc1a#Ù±‚`a
Ù±‚bc1xO# It's possible that the user would like the code to automatically choose whichÙ±‚`a
Ù±‚bc1xN# to use, in this case ``shading='auto'`` will decide whether to use 'flat' orÙ±‚`a
Ù±‚bc1x<# 'nearest' shading based on the shapes of *X*, *Y* and *Z*.Ù±‚`a
Ù±‚`a
Ù±‚`cfigÙ±‚`a,Ù±‚`a Ù±‚`caxsÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cpltÙ±‚aoa.Ù±‚`hsubplotsÙ±‚`a(Ù±‚bmia2Ù±‚`a,Ù±‚`a Ù±‚bmia1Ù±‚`a,Ù±‚`a Ù±‚`rconstrained_layoutÙ±‚aoa=Ù±‚bkcdTrueÙ±‚`a)Ù±‚`a
Ù±‚`baxÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`caxsÙ±‚`a[Ù±‚bmia0Ù±‚`a]Ù±‚`a
Ù±‚`axÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`farangeÙ±‚`a(Ù±‚`encolsÙ±‚`a)Ù±‚`a
Ù±‚`ayÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`farangeÙ±‚`a(Ù±‚`enrowsÙ±‚`a)Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`jpcolormeshÙ±‚`a(Ù±‚`axÙ±‚`a,Ù±‚`a Ù±‚`ayÙ±‚`a,Ù±‚`a Ù±‚`aZÙ±‚`a,Ù±‚`a Ù±‚`gshadingÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1dautoÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`dvminÙ±‚aoa=Ù±‚`aZÙ±‚aoa.Ù±‚`cminÙ±‚`a(Ù±‚`a)Ù±‚`a,Ù±‚`a Ù±‚`dvmaxÙ±‚aoa=Ù±‚`aZÙ±‚aoa.Ù±‚`cmaxÙ±‚`a(Ù±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`i_annotateÙ±‚`a(Ù±‚`baxÙ±‚`a,Ù±‚`a Ù±‚`axÙ±‚`a,Ù±‚`a Ù±‚`ayÙ±‚`a,Ù±‚`a Ù±‚bs2a"Ù±‚bs2hshading=Ù±‚bs2a'Ù±‚bs2dautoÙ±‚bs2a'Ù±‚bs2x; X, Y, Z: same shape (nearest)Ù±‚bs2a"Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`baxÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`caxsÙ±‚`a[Ù±‚bmia1Ù±‚`a]Ù±‚`a
Ù±‚`axÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`farangeÙ±‚`a(Ù±‚`encolsÙ±‚`a Ù±‚aoa+Ù±‚`a Ù±‚bmia1Ù±‚`a)Ù±‚`a
Ù±‚`ayÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`farangeÙ±‚`a(Ù±‚`enrowsÙ±‚`a Ù±‚aoa+Ù±‚`a Ù±‚bmia1Ù±‚`a)Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`jpcolormeshÙ±‚`a(Ù±‚`axÙ±‚`a,Ù±‚`a Ù±‚`ayÙ±‚`a,Ù±‚`a Ù±‚`aZÙ±‚`a,Ù±‚`a Ù±‚`gshadingÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1dautoÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`dvminÙ±‚aoa=Ù±‚`aZÙ±‚aoa.Ù±‚`cminÙ±‚`a(Ù±‚`a)Ù±‚`a,Ù±‚`a Ù±‚`dvmaxÙ±‚aoa=Ù±‚`aZÙ±‚aoa.Ù±‚`cmaxÙ±‚`a(Ù±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`i_annotateÙ±‚`a(Ù±‚`baxÙ±‚`a,Ù±‚`a Ù±‚`axÙ±‚`a,Ù±‚`a Ù±‚`ayÙ±‚`a,Ù±‚`a Ù±‚bs2a"Ù±‚bs2hshading=Ù±‚bs2a'Ù±‚bs2dautoÙ±‚bs2a'Ù±‚bs2x; X, Y one larger than Z (flat)Ù±‚bs2a"Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚bc1xO###############################################################################Ù±‚`a
Ù±‚bc1q# Gouraud ShadingÙ±‚`a
Ù±‚bc1q# ---------------Ù±‚`a
Ù±‚bc1a#Ù±‚`a
Ù±‚bc1xM# `Gouraud shading <https://en.wikipedia.org/wiki/Gouraud_shading>`_ can alsoÙ±‚`a
Ù±‚bc1xN# be specified, where the color in the quadrilaterals is linearly interpolatedÙ±‚`a
Ù±‚bc1xI# between the grid points.  The shapes of *X*, *Y*, *Z* must be the same.Ù±‚`a
Ù±‚`a
Ù±‚`cfigÙ±‚`a,Ù±‚`a Ù±‚`baxÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cpltÙ±‚aoa.Ù±‚`hsubplotsÙ±‚`a(Ù±‚`rconstrained_layoutÙ±‚aoa=Ù±‚bkcdTrueÙ±‚`a)Ù±‚`a
Ù±‚`axÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`farangeÙ±‚`a(Ù±‚`encolsÙ±‚`a)Ù±‚`a
Ù±‚`ayÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`farangeÙ±‚`a(Ù±‚`enrowsÙ±‚`a)Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`jpcolormeshÙ±‚`a(Ù±‚`axÙ±‚`a,Ù±‚`a Ù±‚`ayÙ±‚`a,Ù±‚`a Ù±‚`aZÙ±‚`a,Ù±‚`a Ù±‚`gshadingÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1ggouraudÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`dvminÙ±‚aoa=Ù±‚`aZÙ±‚aoa.Ù±‚`cminÙ±‚`a(Ù±‚`a)Ù±‚`a,Ù±‚`a Ù±‚`dvmaxÙ±‚aoa=Ù±‚`aZÙ±‚aoa.Ù±‚`cmaxÙ±‚`a(Ù±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`i_annotateÙ±‚`a(Ù±‚`baxÙ±‚`a,Ù±‚`a Ù±‚`axÙ±‚`a,Ù±‚`a Ù±‚`ayÙ±‚`a,Ù±‚`a Ù±‚bs2a"Ù±‚bs2hshading=Ù±‚bs2a'Ù±‚bs2ggouraudÙ±‚bs2a'Ù±‚bs2v; X, Y same shape as ZÙ±‚bs2a"Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`cpltÙ±‚aoa.Ù±‚`dshowÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚bc1xM#############################################################################Ù±‚`a
Ù±‚bc1a#Ù±‚`a
Ù±‚bc1x# .. admonition:: ReferencesÙ±‚`a
Ù±‚bc1a#Ù±‚`a
Ù±‚bc1xN#    The use of the following functions, methods, classes and modules is shownÙ±‚`a
Ù±‚bc1u#    in this example:Ù±‚`a
Ù±‚bc1a#Ù±‚`a
Ù±‚bc1xI#    - `matplotlib.axes.Axes.pcolormesh` / `matplotlib.pyplot.pcolormesh`Ù±‚`a
`dNoneö