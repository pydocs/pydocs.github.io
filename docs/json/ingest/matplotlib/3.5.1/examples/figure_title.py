ŸØÇÅŸ¥ÉôŸ±Çbsdy”"""
=============================================
Figure labels: suptitle, supxlabel, supylabel
=============================================

Each axes can have a title (or actually three - one each with *loc* "left",
"center", and "right"), but is sometimes desirable to give a whole figure
(or `.SubFigure`) an overall title, using `.FigureBase.suptitle`.

We can also add figure-level x- and y-labels using `.FigureBase.supxlabel` and
`.FigureBase.supylabel`.
"""Ÿ±Ç`a
Ÿ±ÇbkndfromŸ±Ç`a Ÿ±ÇbnnŸ¢ÑjmatplotlibŸ†Ñjmatplotlibe3.5.1fmodulejmatplotlibfmoduleıŸ±Çbnna.Ÿ±ÇbnnecbookŸ±Ç`a Ÿ±ÇbknfimportŸ±Ç`a Ÿ±Ç`oget_sample_dataŸ±Ç`a
Ÿ±ÇbknfimportŸ±Ç`a Ÿ±ÇbnnŸ¢ÑjmatplotlibŸ†Ñjmatplotlibe3.5.1fmodulejmatplotlibfmoduleıŸ±Çbnna.Ÿ±ÇbnnfpyplotŸ±Ç`a Ÿ±ÇakbasŸ±Ç`a Ÿ±ÇbnncpltŸ±Ç`a
Ÿ±Ç`a
Ÿ±ÇbknfimportŸ±Ç`a Ÿ±ÇbnnŸ¢ÑenumpyŸ†Ñenumpyf1.22.3fmoduleenumpyfmoduleıŸ±Ç`a Ÿ±ÇakbasŸ±Ç`a Ÿ±ÇbnnbnpŸ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`axŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`hlinspaceŸ±Ç`a(Ÿ±Çbmfc0.0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfc5.0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmic501Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`cfigŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`a(Ÿ±Ç`cax1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`cax2Ÿ±Ç`a)Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`hsubplotsŸ±Ç`a(Ÿ±Çbmia1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia2Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`rconstrained_layoutŸ±Çaoa=Ÿ±ÇbkcdTrueŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`fshareyŸ±Çaoa=Ÿ±ÇbkcdTrueŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cax1Ÿ±Çaoa.Ÿ±Ç`dplotŸ±Ç`a(Ÿ±Ç`axŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`ccosŸ±Ç`a(Ÿ±Çbmia6Ÿ±Çaoa*Ÿ±Ç`axŸ±Ç`a)Ÿ±Ç`a Ÿ±Çaoa*Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`cexpŸ±Ç`a(Ÿ±Çaoa-Ÿ±Ç`axŸ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cax1Ÿ±Çaoa.Ÿ±Ç`iset_titleŸ±Ç`a(Ÿ±Çbs1a'Ÿ±Çbs1fdampedŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cax1Ÿ±Çaoa.Ÿ±Ç`jset_xlabelŸ±Ç`a(Ÿ±Çbs1a'Ÿ±Çbs1htime (s)Ÿ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cax1Ÿ±Çaoa.Ÿ±Ç`jset_ylabelŸ±Ç`a(Ÿ±Çbs1a'Ÿ±Çbs1iamplitudeŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`cax2Ÿ±Çaoa.Ÿ±Ç`dplotŸ±Ç`a(Ÿ±Ç`axŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`ccosŸ±Ç`a(Ÿ±Çbmia6Ÿ±Çaoa*Ÿ±Ç`axŸ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cax2Ÿ±Çaoa.Ÿ±Ç`jset_xlabelŸ±Ç`a(Ÿ±Çbs1a'Ÿ±Çbs1htime (s)Ÿ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cax2Ÿ±Çaoa.Ÿ±Ç`iset_titleŸ±Ç`a(Ÿ±Çbs1a'Ÿ±Çbs1hundampedŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`cfigŸ±Çaoa.Ÿ±Ç`hsuptitleŸ±Ç`a(Ÿ±Çbs1a'Ÿ±Çbs1xDifferent types of oscillationsŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`hfontsizeŸ±Çaoa=Ÿ±Çbmib16Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1xN##############################################################################Ÿ±Ç`a
Ÿ±Çbc1xI# A global x- or y-label can be set using the `.FigureBase.supxlabel` andŸ±Ç`a
Ÿ±Çbc1x"# `.FigureBase.supylabel` methods.Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`cfigŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`caxsŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`hsubplotsŸ±Ç`a(Ÿ±Çbmia3Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia5Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`gfigsizeŸ±Çaoa=Ÿ±Ç`a(Ÿ±Çbmia8Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia5Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`rconstrained_layoutŸ±Çaoa=Ÿ±ÇbkcdTrueŸ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`x                        Ÿ±Ç`fsharexŸ±Çaoa=Ÿ±ÇbkcdTrueŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`fshareyŸ±Çaoa=Ÿ±ÇbkcdTrueŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`efnameŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`oget_sample_dataŸ±Ç`a(Ÿ±Çbs1a'Ÿ±Çbs1x'percent_bachelors_degrees_women_usa.csvŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`x                        Ÿ±Ç`iasfileobjŸ±Çaoa=Ÿ±ÇbkceFalseŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`rgender_degree_dataŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`jgenfromtxtŸ±Ç`a(Ÿ±Ç`efnameŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`idelimiterŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1a,Ÿ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`enamesŸ±Çaoa=Ÿ±ÇbkcdTrueŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`fmajorsŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`a[Ÿ±Çbs1a'Ÿ±Çbs1rHealth ProfessionsŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1uPublic AdministrationŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1iEducationŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`j          Ÿ±Çbs1a'Ÿ±Çbs1jPsychologyŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1qForeign LanguagesŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1gEnglishŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`j          Ÿ±Çbs1a'Ÿ±Çbs1sArt and PerformanceŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1gBiologyŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`j          Ÿ±Çbs1a'Ÿ±Çbs1kAgricultureŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1hBusinessŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`j          Ÿ±Çbs1a'Ÿ±Çbs1sMath and StatisticsŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1lArchitectureŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1qPhysical SciencesŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`j          Ÿ±Çbs1a'Ÿ±Çbs1pComputer ScienceŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1kEngineeringŸ±Çbs1a'Ÿ±Ç`a]Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±ÇakcforŸ±Ç`a Ÿ±Ç`bnnŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`baxŸ±Ç`a Ÿ±ÇbowbinŸ±Ç`a Ÿ±ÇbnbienumerateŸ±Ç`a(Ÿ±Ç`caxsŸ±Çaoa.Ÿ±Ç`dflatŸ±Ç`a)Ÿ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`hset_xlimŸ±Ç`a(Ÿ±Çbmff1969.5Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmff2011.1Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`fcolumnŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`fmajorsŸ±Ç`a[Ÿ±Ç`bnnŸ±Ç`a]Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`ocolumn_rec_nameŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`fcolumnŸ±Çaoa.Ÿ±Ç`greplaceŸ±Ç`a(Ÿ±Çbs1a'Ÿ±Çbseb\nŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1a_Ÿ±Çbs1a'Ÿ±Ç`a)Ÿ±Çaoa.Ÿ±Ç`greplaceŸ±Ç`a(Ÿ±Çbs1a'Ÿ±Çbs1a Ÿ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1a_Ÿ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`dlineŸ±Ç`a,Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`dplotŸ±Ç`a(Ÿ±Çbs1a'Ÿ±Çbs1dYearŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ocolumn_rec_nameŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ddataŸ±Çaoa=Ÿ±Ç`rgender_degree_dataŸ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`t                    Ÿ±Ç`blwŸ±Çaoa=Ÿ±Çbmfc2.5Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`iset_titleŸ±Ç`a(Ÿ±Ç`fcolumnŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`hfontsizeŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1esmallŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`clocŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1dleftŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`hset_ylimŸ±Ç`a(Ÿ±Ç`a[Ÿ±Çbmia0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmic100Ÿ±Ç`a]Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`dgridŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cfigŸ±Çaoa.Ÿ±Ç`isupxlabelŸ±Ç`a(Ÿ±Çbs1a'Ÿ±Çbs1dYearŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cfigŸ±Çaoa.Ÿ±Ç`isupylabelŸ±Ç`a(Ÿ±Çbs1a'Ÿ±Çbs1x Percent Degrees Awarded To WomenŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`dshowŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
`dNoneˆ