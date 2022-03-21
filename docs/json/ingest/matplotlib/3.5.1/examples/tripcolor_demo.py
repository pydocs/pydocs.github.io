������������bsdxi"""
==============
Tripcolor Demo
==============

Pseudocolor plots of unstructured triangular grids.
"""���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnctri���`a ���akbas���`a ���bnnctri���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���`a
���bc1xO###############################################################################���`a
���bc1xJ# Creating a Triangulation without specifying the triangles results in the���`a
���bc1x'# Delaunay triangulation of the points.���`a
���`a
���bc1x5# First create the x and y coordinates of the points.���`a
���`hn_angles���`a ���aoa=���`a ���bmib36���`a
���`gn_radii���`a ���aoa=���`a ���bmia8���`a
���`jmin_radius���`a ���aoa=���`a ���bmfd0.25���`a
���`eradii���`a ���aoa=���`a ���`bnp���aoa.���`hlinspace���`a(���`jmin_radius���`a,���`a ���bmfd0.95���`a,���`a ���`gn_radii���`a)���`a
���`a
���`fangles���`a ���aoa=���`a ���`bnp���aoa.���`hlinspace���`a(���bmia0���`a,���`a ���bmia2���`a ���aoa*���`a ���`bnp���aoa.���`bpi���`a,���`a ���`hn_angles���`a,���`a ���`hendpoint���aoa=���bkceFalse���`a)���`a
���`fangles���`a ���aoa=���`a ���`bnp���aoa.���`frepeat���`a(���`fangles���`a[���aoa.���aoa.���aoa.���`a,���`a ���`bnp���aoa.���`gnewaxis���`a]���`a,���`a ���`gn_radii���`a,���`a ���`daxis���aoa=���bmia1���`a)���`a
���`fangles���`a[���`a:���`a,���`a ���bmia1���`a:���`a:���bmia2���`a]���`a ���aoa+���aoa=���`a ���`bnp���aoa.���`bpi���`a ���aoa/���`a ���`hn_angles���`a
���`a
���`ax���`a ���aoa=���`a ���`a(���`eradii���`a ���aoa*���`a ���`bnp���aoa.���`ccos���`a(���`fangles���`a)���`a)���aoa.���`gflatten���`a(���`a)���`a
���`ay���`a ���aoa=���`a ���`a(���`eradii���`a ���aoa*���`a ���`bnp���aoa.���`csin���`a(���`fangles���`a)���`a)���aoa.���`gflatten���`a(���`a)���`a
���`az���`a ���aoa=���`a ���`a(���`bnp���aoa.���`ccos���`a(���`eradii���`a)���`a ���aoa*���`a ���`bnp���aoa.���`ccos���`a(���bmia3���`a ���aoa*���`a ���`fangles���`a)���`a)���aoa.���`gflatten���`a(���`a)���`a
���`a
���bc1xK# Create the Triangulation; no triangles so Delaunay triangulation created.���`a
���`ftriang���`a ���aoa=���`a ���`ctri���aoa.���`mTriangulation���`a(���`ax���`a,���`a ���`ay���`a)���`a
���`a
���bc1x# Mask off unwanted triangles.���`a
���`ftriang���aoa.���`hset_mask���`a(���`bnp���aoa.���`ehypot���`a(���`ax���`a[���`ftriang���aoa.���`itriangles���`a]���aoa.���`dmean���`a(���`daxis���aoa=���bmia1���`a)���`a,���`a
���`x                         ���`ay���`a[���`ftriang���aoa.���`itriangles���`a]���aoa.���`dmean���`a(���`daxis���aoa=���bmia1���`a)���`a)���`a
���`p                ���aoa<���`a ���`jmin_radius���`a)���`a
���`a
���bc1xO###############################################################################���`a
���bc1q# tripcolor plot.���`a
���`a
���`dfig1���`a,���`a ���`cax1���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`a)���`a
���`cax1���aoa.���`jset_aspect���`a(���bs1a'���bs1eequal���bs1a'���`a)���`a
���`ctpc���`a ���aoa=���`a ���`cax1���aoa.���`itripcolor���`a(���`ftriang���`a,���`a ���`az���`a,���`a ���`gshading���aoa=���bs1a'���bs1dflat���bs1a'���`a)���`a
���`dfig1���aoa.���`hcolorbar���`a(���`ctpc���`a)���`a
���`cax1���aoa.���`iset_title���`a(���bs1a'���bs1x1tripcolor of Delaunay triangulation, flat shading���bs1a'���`a)���`a
���`a
���bc1xO###############################################################################���`a
���bc1x# Illustrate Gouraud shading.���`a
���`a
���`dfig2���`a,���`a ���`cax2���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`a)���`a
���`cax2���aoa.���`jset_aspect���`a(���bs1a'���bs1eequal���bs1a'���`a)���`a
���`ctpc���`a ���aoa=���`a ���`cax2���aoa.���`itripcolor���`a(���`ftriang���`a,���`a ���`az���`a,���`a ���`gshading���aoa=���bs1a'���bs1ggouraud���bs1a'���`a)���`a
���`dfig2���aoa.���`hcolorbar���`a(���`ctpc���`a)���`a
���`cax2���aoa.���`iset_title���`a(���bs1a'���bs1x4tripcolor of Delaunay triangulation, gouraud shading���bs1a'���`a)���`a
���`a
���`a
���bc1xO###############################################################################���`a
���bc1xG# You can specify your own triangulation rather than perform a Delaunay���`a
���bc1xM# triangulation of the points, where each triangle is given by the indices of���`a
���bc1xN# the three points that make up the triangle, ordered in either a clockwise or���`a
���bc1w# anticlockwise manner.���`a
���`a
���`bxy���`a ���aoa=���`a ���`bnp���aoa.���`gasarray���`a(���`a[���`a
���`d    ���`a[���aoa-���bmfe0.101���`a,���`a ���bmfe0.872���`a]���`a,���`a ���`a[���aoa-���bmfe0.080���`a,���`a ���bmfe0.883���`a]���`a,���`a ���`a[���aoa-���bmfe0.069���`a,���`a ���bmfe0.888���`a]���`a,���`a ���`a[���aoa-���bmfe0.054���`a,���`a ���bmfe0.890���`a]���`a,���`a
���`d    ���`a[���aoa-���bmfe0.045���`a,���`a ���bmfe0.897���`a]���`a,���`a ���`a[���aoa-���bmfe0.057���`a,���`a ���bmfe0.895���`a]���`a,���`a ���`a[���aoa-���bmfe0.073���`a,���`a ���bmfe0.900���`a]���`a,���`a ���`a[���aoa-���bmfe0.087���`a,���`a ���bmfe0.898���`a]���`a,���`a
���`d    ���`a[���aoa-���bmfe0.090���`a,���`a ���bmfe0.904���`a]���`a,���`a ���`a[���aoa-���bmfe0.069���`a,���`a ���bmfe0.907���`a]���`a,���`a ���`a[���aoa-���bmfe0.069���`a,���`a ���bmfe0.921���`a]���`a,���`a ���`a[���aoa-���bmfe0.080���`a,���`a ���bmfe0.919���`a]���`a,���`a
���`d    ���`a[���aoa-���bmfe0.073���`a,���`a ���bmfe0.928���`a]���`a,���`a ���`a[���aoa-���bmfe0.052���`a,���`a ���bmfe0.930���`a]���`a,���`a ���`a[���aoa-���bmfe0.048���`a,���`a ���bmfe0.942���`a]���`a,���`a ���`a[���aoa-���bmfe0.062���`a,���`a ���bmfe0.949���`a]���`a,���`a
���`d    ���`a[���aoa-���bmfe0.054���`a,���`a ���bmfe0.958���`a]���`a,���`a ���`a[���aoa-���bmfe0.069���`a,���`a ���bmfe0.954���`a]���`a,���`a ���`a[���aoa-���bmfe0.087���`a,���`a ���bmfe0.952���`a]���`a,���`a ���`a[���aoa-���bmfe0.087���`a,���`a ���bmfe0.959���`a]���`a,���`a
���`d    ���`a[���aoa-���bmfe0.080���`a,���`a ���bmfe0.966���`a]���`a,���`a ���`a[���aoa-���bmfe0.085���`a,���`a ���bmfe0.973���`a]���`a,���`a ���`a[���aoa-���bmfe0.087���`a,���`a ���bmfe0.965���`a]���`a,���`a ���`a[���aoa-���bmfe0.097���`a,���`a ���bmfe0.965���`a]���`a,���`a
���`d    ���`a[���aoa-���bmfe0.097���`a,���`a ���bmfe0.975���`a]���`a,���`a ���`a[���aoa-���bmfe0.092���`a,���`a ���bmfe0.984���`a]���`a,���`a ���`a[���aoa-���bmfe0.101���`a,���`a ���bmfe0.980���`a]���`a,���`a ���`a[���aoa-���bmfe0.108���`a,���`a ���bmfe0.980���`a]���`a,���`a
���`d    ���`a[���aoa-���bmfe0.104���`a,���`a ���bmfe0.987���`a]���`a,���`a ���`a[���aoa-���bmfe0.102���`a,���`a ���bmfe0.993���`a]���`a,���`a ���`a[���aoa-���bmfe0.115���`a,���`a ���bmfe1.001���`a]���`a,���`a ���`a[���aoa-���bmfe0.099���`a,���`a ���bmfe0.996���`a]���`a,���`a
���`d    ���`a[���aoa-���bmfe0.101���`a,���`a ���bmfe1.007���`a]���`a,���`a ���`a[���aoa-���bmfe0.090���`a,���`a ���bmfe1.010���`a]���`a,���`a ���`a[���aoa-���bmfe0.087���`a,���`a ���bmfe1.021���`a]���`a,���`a ���`a[���aoa-���bmfe0.069���`a,���`a ���bmfe1.021���`a]���`a,���`a
���`d    ���`a[���aoa-���bmfe0.052���`a,���`a ���bmfe1.022���`a]���`a,���`a ���`a[���aoa-���bmfe0.052���`a,���`a ���bmfe1.017���`a]���`a,���`a ���`a[���aoa-���bmfe0.069���`a,���`a ���bmfe1.010���`a]���`a,���`a ���`a[���aoa-���bmfe0.064���`a,���`a ���bmfe1.005���`a]���`a,���`a
���`d    ���`a[���aoa-���bmfe0.048���`a,���`a ���bmfe1.005���`a]���`a,���`a ���`a[���aoa-���bmfe0.031���`a,���`a ���bmfe1.005���`a]���`a,���`a ���`a[���aoa-���bmfe0.031���`a,���`a ���bmfe0.996���`a]���`a,���`a ���`a[���aoa-���bmfe0.040���`a,���`a ���bmfe0.987���`a]���`a,���`a
���`d    ���`a[���aoa-���bmfe0.045���`a,���`a ���bmfe0.980���`a]���`a,���`a ���`a[���aoa-���bmfe0.052���`a,���`a ���bmfe0.975���`a]���`a,���`a ���`a[���aoa-���bmfe0.040���`a,���`a ���bmfe0.973���`a]���`a,���`a ���`a[���aoa-���bmfe0.026���`a,���`a ���bmfe0.968���`a]���`a,���`a
���`d    ���`a[���aoa-���bmfe0.020���`a,���`a ���bmfe0.954���`a]���`a,���`a ���`a[���aoa-���bmfe0.006���`a,���`a ���bmfe0.947���`a]���`a,���`a ���`a[���`a ���bmfe0.003���`a,���`a ���bmfe0.935���`a]���`a,���`a ���`a[���`a ���bmfe0.006���`a,���`a ���bmfe0.926���`a]���`a,���`a
���`d    ���`a[���`a ���bmfe0.005���`a,���`a ���bmfe0.921���`a]���`a,���`a ���`a[���`a ���bmfe0.022���`a,���`a ���bmfe0.923���`a]���`a,���`a ���`a[���`a ���bmfe0.033���`a,���`a ���bmfe0.912���`a]���`a,���`a ���`a[���`a ���bmfe0.029���`a,���`a ���bmfe0.905���`a]���`a,���`a
���`d    ���`a[���`a ���bmfe0.017���`a,���`a ���bmfe0.900���`a]���`a,���`a ���`a[���`a ���bmfe0.012���`a,���`a ���bmfe0.895���`a]���`a,���`a ���`a[���`a ���bmfe0.027���`a,���`a ���bmfe0.893���`a]���`a,���`a ���`a[���`a ���bmfe0.019���`a,���`a ���bmfe0.886���`a]���`a,���`a
���`d    ���`a[���`a ���bmfe0.001���`a,���`a ���bmfe0.883���`a]���`a,���`a ���`a[���aoa-���bmfe0.012���`a,���`a ���bmfe0.884���`a]���`a,���`a ���`a[���aoa-���bmfe0.029���`a,���`a ���bmfe0.883���`a]���`a,���`a ���`a[���aoa-���bmfe0.038���`a,���`a ���bmfe0.879���`a]���`a,���`a
���`d    ���`a[���aoa-���bmfe0.057���`a,���`a ���bmfe0.881���`a]���`a,���`a ���`a[���aoa-���bmfe0.062���`a,���`a ���bmfe0.876���`a]���`a,���`a ���`a[���aoa-���bmfe0.078���`a,���`a ���bmfe0.876���`a]���`a,���`a ���`a[���aoa-���bmfe0.087���`a,���`a ���bmfe0.872���`a]���`a,���`a
���`d    ���`a[���aoa-���bmfe0.030���`a,���`a ���bmfe0.907���`a]���`a,���`a ���`a[���aoa-���bmfe0.007���`a,���`a ���bmfe0.905���`a]���`a,���`a ���`a[���aoa-���bmfe0.057���`a,���`a ���bmfe0.916���`a]���`a,���`a ���`a[���aoa-���bmfe0.025���`a,���`a ���bmfe0.933���`a]���`a,���`a
���`d    ���`a[���aoa-���bmfe0.077���`a,���`a ���bmfe0.990���`a]���`a,���`a ���`a[���aoa-���bmfe0.059���`a,���`a ���bmfe0.993���`a]���`a]���`a)���`a
���`ax���`a,���`a ���`ay���`a ���aoa=���`a ���`bnp���aoa.���`grad2deg���`a(���`bxy���`a)���aoa.���`aT���`a
���`a
���`itriangles���`a ���aoa=���`a ���`bnp���aoa.���`gasarray���`a(���`a[���`a
���`d    ���`a[���bmib67���`a,���`a ���bmib66���`a,���`b  ���bmia1���`a]���`a,���`a ���`a[���bmib65���`a,���`b  ���bmia2���`a,���`a ���bmib66���`a]���`a,���`a ���`a[���`a ���bmia1���`a,���`a ���bmib66���`a,���`b  ���bmia2���`a]���`a,���`a ���`a[���bmib64���`a,���`b  ���bmia2���`a,���`a ���bmib65���`a]���`a,���`a ���`a[���bmib63���`a,���`b  ���bmia3���`a,���`a ���bmib64���`a]���`a,���`a
���`d    ���`a[���bmib60���`a,���`a ���bmib59���`a,���`a ���bmib57���`a]���`a,���`a ���`a[���`a ���bmia2���`a,���`a ���bmib64���`a,���`b  ���bmia3���`a]���`a,���`a ���`a[���`a ���bmia3���`a,���`a ���bmib63���`a,���`b  ���bmia4���`a]���`a,���`a ���`a[���`a ���bmia0���`a,���`a ���bmib67���`a,���`b  ���bmia1���`a]���`a,���`a ���`a[���bmib62���`a,���`b  ���bmia4���`a,���`a ���bmib63���`a]���`a,���`a
���`d    ���`a[���bmib57���`a,���`a ���bmib59���`a,���`a ���bmib56���`a]���`a,���`a ���`a[���bmib59���`a,���`a ���bmib58���`a,���`a ���bmib56���`a]���`a,���`a ���`a[���bmib61���`a,���`a ���bmib60���`a,���`a ���bmib69���`a]���`a,���`a ���`a[���bmib57���`a,���`a ���bmib69���`a,���`a ���bmib60���`a]���`a,���`a ���`a[���`a ���bmia4���`a,���`a ���bmib62���`a,���`a ���bmib68���`a]���`a,���`a
���`d    ���`a[���`a ���bmia6���`a,���`b  ���bmia5���`a,���`b  ���bmia9���`a]���`a,���`a ���`a[���bmib61���`a,���`a ���bmib68���`a,���`a ���bmib62���`a]���`a,���`a ���`a[���bmib69���`a,���`a ���bmib68���`a,���`a ���bmib61���`a]���`a,���`a ���`a[���`a ���bmia9���`a,���`b  ���bmia5���`a,���`a ���bmib70���`a]���`a,���`a ���`a[���`a ���bmia6���`a,���`b  ���bmia8���`a,���`b  ���bmia7���`a]���`a,���`a
���`d    ���`a[���`a ���bmia4���`a,���`a ���bmib70���`a,���`b  ���bmia5���`a]���`a,���`a ���`a[���`a ���bmia8���`a,���`b  ���bmia6���`a,���`b  ���bmia9���`a]���`a,���`a ���`a[���bmib56���`a,���`a ���bmib69���`a,���`a ���bmib57���`a]���`a,���`a ���`a[���bmib69���`a,���`a ���bmib56���`a,���`a ���bmib52���`a]���`a,���`a ���`a[���bmib70���`a,���`a ���bmib10���`a,���`b  ���bmia9���`a]���`a,���`a
���`d    ���`a[���bmib54���`a,���`a ���bmib53���`a,���`a ���bmib55���`a]���`a,���`a ���`a[���bmib56���`a,���`a ���bmib55���`a,���`a ���bmib53���`a]���`a,���`a ���`a[���bmib68���`a,���`a ���bmib70���`a,���`b  ���bmia4���`a]���`a,���`a ���`a[���bmib52���`a,���`a ���bmib56���`a,���`a ���bmib53���`a]���`a,���`a ���`a[���bmib11���`a,���`a ���bmib10���`a,���`a ���bmib12���`a]���`a,���`a
���`d    ���`a[���bmib69���`a,���`a ���bmib71���`a,���`a ���bmib68���`a]���`a,���`a ���`a[���bmib68���`a,���`a ���bmib13���`a,���`a ���bmib70���`a]���`a,���`a ���`a[���bmib10���`a,���`a ���bmib70���`a,���`a ���bmib13���`a]���`a,���`a ���`a[���bmib51���`a,���`a ���bmib50���`a,���`a ���bmib52���`a]���`a,���`a ���`a[���bmib13���`a,���`a ���bmib68���`a,���`a ���bmib71���`a]���`a,���`a
���`d    ���`a[���bmib52���`a,���`a ���bmib71���`a,���`a ���bmib69���`a]���`a,���`a ���`a[���bmib12���`a,���`a ���bmib10���`a,���`a ���bmib13���`a]���`a,���`a ���`a[���bmib71���`a,���`a ���bmib52���`a,���`a ���bmib50���`a]���`a,���`a ���`a[���bmib71���`a,���`a ���bmib14���`a,���`a ���bmib13���`a]���`a,���`a ���`a[���bmib50���`a,���`a ���bmib49���`a,���`a ���bmib71���`a]���`a,���`a
���`d    ���`a[���bmib49���`a,���`a ���bmib48���`a,���`a ���bmib71���`a]���`a,���`a ���`a[���bmib14���`a,���`a ���bmib16���`a,���`a ���bmib15���`a]���`a,���`a ���`a[���bmib14���`a,���`a ���bmib71���`a,���`a ���bmib48���`a]���`a,���`a ���`a[���bmib17���`a,���`a ���bmib19���`a,���`a ���bmib18���`a]���`a,���`a ���`a[���bmib17���`a,���`a ���bmib20���`a,���`a ���bmib19���`a]���`a,���`a
���`d    ���`a[���bmib48���`a,���`a ���bmib16���`a,���`a ���bmib14���`a]���`a,���`a ���`a[���bmib48���`a,���`a ���bmib47���`a,���`a ���bmib16���`a]���`a,���`a ���`a[���bmib47���`a,���`a ���bmib46���`a,���`a ���bmib16���`a]���`a,���`a ���`a[���bmib16���`a,���`a ���bmib46���`a,���`a ���bmib45���`a]���`a,���`a ���`a[���bmib23���`a,���`a ���bmib22���`a,���`a ���bmib24���`a]���`a,���`a
���`d    ���`a[���bmib21���`a,���`a ���bmib24���`a,���`a ���bmib22���`a]���`a,���`a ���`a[���bmib17���`a,���`a ���bmib16���`a,���`a ���bmib45���`a]���`a,���`a ���`a[���bmib20���`a,���`a ���bmib17���`a,���`a ���bmib45���`a]���`a,���`a ���`a[���bmib21���`a,���`a ���bmib25���`a,���`a ���bmib24���`a]���`a,���`a ���`a[���bmib27���`a,���`a ���bmib26���`a,���`a ���bmib28���`a]���`a,���`a
���`d    ���`a[���bmib20���`a,���`a ���bmib72���`a,���`a ���bmib21���`a]���`a,���`a ���`a[���bmib25���`a,���`a ���bmib21���`a,���`a ���bmib72���`a]���`a,���`a ���`a[���bmib45���`a,���`a ���bmib72���`a,���`a ���bmib20���`a]���`a,���`a ���`a[���bmib25���`a,���`a ���bmib28���`a,���`a ���bmib26���`a]���`a,���`a ���`a[���bmib44���`a,���`a ���bmib73���`a,���`a ���bmib45���`a]���`a,���`a
���`d    ���`a[���bmib72���`a,���`a ���bmib45���`a,���`a ���bmib73���`a]���`a,���`a ���`a[���bmib28���`a,���`a ���bmib25���`a,���`a ���bmib29���`a]���`a,���`a ���`a[���bmib29���`a,���`a ���bmib25���`a,���`a ���bmib31���`a]���`a,���`a ���`a[���bmib43���`a,���`a ���bmib73���`a,���`a ���bmib44���`a]���`a,���`a ���`a[���bmib73���`a,���`a ���bmib43���`a,���`a ���bmib40���`a]���`a,���`a
���`d    ���`a[���bmib72���`a,���`a ���bmib73���`a,���`a ���bmib39���`a]���`a,���`a ���`a[���bmib72���`a,���`a ���bmib31���`a,���`a ���bmib25���`a]���`a,���`a ���`a[���bmib42���`a,���`a ���bmib40���`a,���`a ���bmib43���`a]���`a,���`a ���`a[���bmib31���`a,���`a ���bmib30���`a,���`a ���bmib29���`a]���`a,���`a ���`a[���bmib39���`a,���`a ���bmib73���`a,���`a ���bmib40���`a]���`a,���`a
���`d    ���`a[���bmib42���`a,���`a ���bmib41���`a,���`a ���bmib40���`a]���`a,���`a ���`a[���bmib72���`a,���`a ���bmib33���`a,���`a ���bmib31���`a]���`a,���`a ���`a[���bmib32���`a,���`a ���bmib31���`a,���`a ���bmib33���`a]���`a,���`a ���`a[���bmib39���`a,���`a ���bmib38���`a,���`a ���bmib72���`a]���`a,���`a ���`a[���bmib33���`a,���`a ���bmib72���`a,���`a ���bmib38���`a]���`a,���`a
���`d    ���`a[���bmib33���`a,���`a ���bmib38���`a,���`a ���bmib34���`a]���`a,���`a ���`a[���bmib37���`a,���`a ���bmib35���`a,���`a ���bmib38���`a]���`a,���`a ���`a[���bmib34���`a,���`a ���bmib38���`a,���`a ���bmib35���`a]���`a,���`a ���`a[���bmib35���`a,���`a ���bmib37���`a,���`a ���bmib36���`a]���`a]���`a)���`a
���`a
���`dxmid���`a ���aoa=���`a ���`ax���`a[���`itriangles���`a]���aoa.���`dmean���`a(���`daxis���aoa=���bmia1���`a)���`a
���`dymid���`a ���aoa=���`a ���`ay���`a[���`itriangles���`a]���aoa.���`dmean���`a(���`daxis���aoa=���bmia1���`a)���`a
���`bx0���`a ���aoa=���`a ���aoa-���bmia5���`a
���`by0���`a ���aoa=���`a ���bmib52���`a
���`fzfaces���`a ���aoa=���`a ���`bnp���aoa.���`cexp���`a(���aoa-���bmfd0.01���`a ���aoa*���`a ���`a(���`a(���`dxmid���`a ���aoa-���`a ���`bx0���`a)���`a ���aoa*���`a ���`a(���`dxmid���`a ���aoa-���`a ���`bx0���`a)���`a ���aoa+���`a
���`x                         ���`a(���`dymid���`a ���aoa-���`a ���`by0���`a)���`a ���aoa*���`a ���`a(���`dymid���`a ���aoa-���`a ���`by0���`a)���`a)���`a)���`a
���`a
���bc1xO###############################################################################���`a
���bc1xO# Rather than create a Triangulation object, can simply pass x, y and triangles���`a
���bc1xJ# arrays to tripcolor directly.  It would be better to use a Triangulation���`a
���bc1xH# object if the same triangulation was to be used more than once to save���`a
���bc1x# duplicated calculations.���`a
���bc1xM# Can specify one color value per face rather than one per point by using the���`a
���bc1x # *facecolors* keyword argument.���`a
���`a
���`dfig3���`a,���`a ���`cax3���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`a)���`a
���`cax3���aoa.���`jset_aspect���`a(���bs1a'���bs1eequal���bs1a'���`a)���`a
���`ctpc���`a ���aoa=���`a ���`cax3���aoa.���`itripcolor���`a(���`ax���`a,���`a ���`ay���`a,���`a ���`itriangles���`a,���`a ���`jfacecolors���aoa=���`fzfaces���`a,���`a ���`jedgecolors���aoa=���bs1a'���bs1ak���bs1a'���`a)���`a
���`dfig3���aoa.���`hcolorbar���`a(���`ctpc���`a)���`a
���`cax3���aoa.���`iset_title���`a(���bs1a'���bs1x)tripcolor of user-specified triangulation���bs1a'���`a)���`a
���`cax3���aoa.���`jset_xlabel���`a(���bs1a'���bs1sLongitude (degrees)���bs1a'���`a)���`a
���`cax3���aoa.���`jset_ylabel���`a(���bs1a'���bs1rLatitude (degrees)���bs1a'���`a)���`a
���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
���`a
���bc1xM#############################################################################���`a
���bc1a#���`a
���bc1x# .. admonition:: References���`a
���bc1a#���`a
���bc1xN#    The use of the following functions, methods, classes and modules is shown���`a
���bc1u#    in this example:���`a
���bc1a#���`a
���bc1xG#    - `matplotlib.axes.Axes.tripcolor` / `matplotlib.pyplot.tripcolor`���`a
���bc1w#    - `matplotlib.tri`���`a
���bc1x%#    - `matplotlib.tri.Triangulation`���`a
`dNone�