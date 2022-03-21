�����������bsdy�"""
=============================================
Figure labels: suptitle, supxlabel, supylabel
=============================================

Each axes can have a title (or actually three - one each with *loc* "left",
"center", and "right"), but is sometimes desirable to give a whole figure
(or `.SubFigure`) an overall title, using `.FigureBase.suptitle`.

We can also add figure-level x- and y-labels using `.FigureBase.supxlabel` and
`.FigureBase.supylabel`.
"""���`a
���bkndfrom���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnecbook���`a ���bknfimport���`a ���`oget_sample_data���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���`a
���`a
���`ax���`a ���aoa=���`a ���`bnp���aoa.���`hlinspace���`a(���bmfc0.0���`a,���`a ���bmfc5.0���`a,���`a ���bmic501���`a)���`a
���`a
���`cfig���`a,���`a ���`a(���`cax1���`a,���`a ���`cax2���`a)���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���bmia1���`a,���`a ���bmia2���`a,���`a ���`rconstrained_layout���aoa=���bkcdTrue���`a,���`a ���`fsharey���aoa=���bkcdTrue���`a)���`a
���`cax1���aoa.���`dplot���`a(���`ax���`a,���`a ���`bnp���aoa.���`ccos���`a(���bmia6���aoa*���`ax���`a)���`a ���aoa*���`a ���`bnp���aoa.���`cexp���`a(���aoa-���`ax���`a)���`a)���`a
���`cax1���aoa.���`iset_title���`a(���bs1a'���bs1fdamped���bs1a'���`a)���`a
���`cax1���aoa.���`jset_xlabel���`a(���bs1a'���bs1htime (s)���bs1a'���`a)���`a
���`cax1���aoa.���`jset_ylabel���`a(���bs1a'���bs1iamplitude���bs1a'���`a)���`a
���`a
���`cax2���aoa.���`dplot���`a(���`ax���`a,���`a ���`bnp���aoa.���`ccos���`a(���bmia6���aoa*���`ax���`a)���`a)���`a
���`cax2���aoa.���`jset_xlabel���`a(���bs1a'���bs1htime (s)���bs1a'���`a)���`a
���`cax2���aoa.���`iset_title���`a(���bs1a'���bs1hundamped���bs1a'���`a)���`a
���`a
���`cfig���aoa.���`hsuptitle���`a(���bs1a'���bs1xDifferent types of oscillations���bs1a'���`a,���`a ���`hfontsize���aoa=���bmib16���`a)���`a
���`a
���bc1xN##############################################################################���`a
���bc1xI# A global x- or y-label can be set using the `.FigureBase.supxlabel` and���`a
���bc1x"# `.FigureBase.supylabel` methods.���`a
���`a
���`cfig���`a,���`a ���`caxs���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���bmia3���`a,���`a ���bmia5���`a,���`a ���`gfigsize���aoa=���`a(���bmia8���`a,���`a ���bmia5���`a)���`a,���`a ���`rconstrained_layout���aoa=���bkcdTrue���`a,���`a
���`x                        ���`fsharex���aoa=���bkcdTrue���`a,���`a ���`fsharey���aoa=���bkcdTrue���`a)���`a
���`a
���`efname���`a ���aoa=���`a ���`oget_sample_data���`a(���bs1a'���bs1x'percent_bachelors_degrees_women_usa.csv���bs1a'���`a,���`a
���`x                        ���`iasfileobj���aoa=���bkceFalse���`a)���`a
���`rgender_degree_data���`a ���aoa=���`a ���`bnp���aoa.���`jgenfromtxt���`a(���`efname���`a,���`a ���`idelimiter���aoa=���bs1a'���bs1a,���bs1a'���`a,���`a ���`enames���aoa=���bkcdTrue���`a)���`a
���`a
���`fmajors���`a ���aoa=���`a ���`a[���bs1a'���bs1rHealth Professions���bs1a'���`a,���`a ���bs1a'���bs1uPublic Administration���bs1a'���`a,���`a ���bs1a'���bs1iEducation���bs1a'���`a,���`a
���`j          ���bs1a'���bs1jPsychology���bs1a'���`a,���`a ���bs1a'���bs1qForeign Languages���bs1a'���`a,���`a ���bs1a'���bs1gEnglish���bs1a'���`a,���`a
���`j          ���bs1a'���bs1sArt and Performance���bs1a'���`a,���`a ���bs1a'���bs1gBiology���bs1a'���`a,���`a
���`j          ���bs1a'���bs1kAgriculture���bs1a'���`a,���`a ���bs1a'���bs1hBusiness���bs1a'���`a,���`a
���`j          ���bs1a'���bs1sMath and Statistics���bs1a'���`a,���`a ���bs1a'���bs1lArchitecture���bs1a'���`a,���`a ���bs1a'���bs1qPhysical Sciences���bs1a'���`a,���`a
���`j          ���bs1a'���bs1pComputer Science���bs1a'���`a,���`a ���bs1a'���bs1kEngineering���bs1a'���`a]���`a
���`a
���akcfor���`a ���`bnn���`a,���`a ���`bax���`a ���bowbin���`a ���bnbienumerate���`a(���`caxs���aoa.���`dflat���`a)���`a:���`a
���`d    ���`bax���aoa.���`hset_xlim���`a(���bmff1969.5���`a,���`a ���bmff2011.1���`a)���`a
���`d    ���`fcolumn���`a ���aoa=���`a ���`fmajors���`a[���`bnn���`a]���`a
���`d    ���`ocolumn_rec_name���`a ���aoa=���`a ���`fcolumn���aoa.���`greplace���`a(���bs1a'���bseb\n���bs1a'���`a,���`a ���bs1a'���bs1a_���bs1a'���`a)���aoa.���`greplace���`a(���bs1a'���bs1a ���bs1a'���`a,���`a ���bs1a'���bs1a_���bs1a'���`a)���`a
���`a
���`d    ���`dline���`a,���`a ���aoa=���`a ���`bax���aoa.���`dplot���`a(���bs1a'���bs1dYear���bs1a'���`a,���`a ���`ocolumn_rec_name���`a,���`a ���`ddata���aoa=���`rgender_degree_data���`a,���`a
���`t                    ���`blw���aoa=���bmfc2.5���`a)���`a
���`d    ���`bax���aoa.���`iset_title���`a(���`fcolumn���`a,���`a ���`hfontsize���aoa=���bs1a'���bs1esmall���bs1a'���`a,���`a ���`cloc���aoa=���bs1a'���bs1dleft���bs1a'���`a)���`a
���`d    ���`bax���aoa.���`hset_ylim���`a(���`a[���bmia0���`a,���`a ���bmic100���`a]���`a)���`a
���`d    ���`bax���aoa.���`dgrid���`a(���`a)���`a
���`cfig���aoa.���`isupxlabel���`a(���bs1a'���bs1dYear���bs1a'���`a)���`a
���`cfig���aoa.���`isupylabel���`a(���bs1a'���bs1x Percent Degrees Awarded To Women���bs1a'���`a)���`a
���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
`dNone�