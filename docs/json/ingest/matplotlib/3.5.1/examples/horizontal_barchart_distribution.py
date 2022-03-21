ŸØÇÅŸ¥Éô`Ÿ±Çbsdy"""
=============================================
Discrete distribution as horizontal bar chart
=============================================

Stacked bar charts can be used to visualize discrete distributions.

This example visualizes the result of a survey in which people could rate
their agreement to questions on a five-element scale.

The horizontal stacking is achieved by calling `~.Axes.barh()` for each
category and passing the starting point as the cumulative sum of the
already drawn bars via the parameter ``left``.
"""Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±ÇbknfimportŸ±Ç`a Ÿ±ÇbnnŸ¢ÑenumpyŸ†Ñenumpyf1.22.3fmoduleenumpyfmoduleıŸ±Ç`a Ÿ±ÇakbasŸ±Ç`a Ÿ±ÇbnnbnpŸ±Ç`a
Ÿ±ÇbknfimportŸ±Ç`a Ÿ±ÇbnnŸ¢ÑjmatplotlibŸ†Ñjmatplotlibe3.5.1fmodulejmatplotlibfmoduleıŸ±Çbnna.Ÿ±ÇbnnfpyplotŸ±Ç`a Ÿ±ÇakbasŸ±Ç`a Ÿ±ÇbnncpltŸ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`ncategory_namesŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`a[Ÿ±Çbs1a'Ÿ±Çbs1qStrongly disagreeŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1hDisagreeŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`r                  Ÿ±Çbs1a'Ÿ±Çbs1xNeither agree nor disagreeŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1eAgreeŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1nStrongly agreeŸ±Çbs1a'Ÿ±Ç`a]Ÿ±Ç`a
Ÿ±Ç`gresultsŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`a{Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Çbs1a'Ÿ±Çbs1jQuestion 1Ÿ±Çbs1a'Ÿ±Ç`a:Ÿ±Ç`a Ÿ±Ç`a[Ÿ±Çbmib10Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmib15Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmib17Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmib32Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmib26Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Çbs1a'Ÿ±Çbs1jQuestion 2Ÿ±Çbs1a'Ÿ±Ç`a:Ÿ±Ç`a Ÿ±Ç`a[Ÿ±Çbmib26Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmib22Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmib29Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmib10Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmib13Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Çbs1a'Ÿ±Çbs1jQuestion 3Ÿ±Çbs1a'Ÿ±Ç`a:Ÿ±Ç`a Ÿ±Ç`a[Ÿ±Çbmib35Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmib37Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia7Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia2Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmib19Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Çbs1a'Ÿ±Çbs1jQuestion 4Ÿ±Çbs1a'Ÿ±Ç`a:Ÿ±Ç`a Ÿ±Ç`a[Ÿ±Çbmib32Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmib11Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia9Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmib15Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmib33Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Çbs1a'Ÿ±Çbs1jQuestion 5Ÿ±Çbs1a'Ÿ±Ç`a:Ÿ±Ç`a Ÿ±Ç`a[Ÿ±Çbmib21Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmib29Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia5Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia5Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmib40Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Çbs1a'Ÿ±Çbs1jQuestion 6Ÿ±Çbs1a'Ÿ±Ç`a:Ÿ±Ç`a Ÿ±Ç`a[Ÿ±Çbmia8Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmib19Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia5Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmib30Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmib38Ÿ±Ç`a]Ÿ±Ç`a
Ÿ±Ç`a}Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±ÇakcdefŸ±Ç`a Ÿ±ÇbnffsurveyŸ±Ç`a(Ÿ±Ç`gresultsŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ncategory_namesŸ±Ç`a)Ÿ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±ÇbsdyC"""
    Parameters
    ----------
    results : dict
        A mapping from question labels to a list of answers per category.
        It is assumed all lists contain the same number of entries and that
        it matches the length of *category_names*.
    category_names : list of str
        The category labels.
    """Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`flabelsŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±ÇbnbdlistŸ±Ç`a(Ÿ±Ç`gresultsŸ±Çaoa.Ÿ±Ç`dkeysŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`ddataŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`earrayŸ±Ç`a(Ÿ±ÇbnbdlistŸ±Ç`a(Ÿ±Ç`gresultsŸ±Çaoa.Ÿ±Ç`fvaluesŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`hdata_cumŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`ddataŸ±Çaoa.Ÿ±Ç`fcumsumŸ±Ç`a(Ÿ±Ç`daxisŸ±Çaoa=Ÿ±Çbmia1Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`ocategory_colorsŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`icolormapsŸ±Ç`a[Ÿ±Çbs1a'Ÿ±Çbs1fRdYlGnŸ±Çbs1a'Ÿ±Ç`a]Ÿ±Ç`a(Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`hlinspaceŸ±Ç`a(Ÿ±Çbmfd0.15Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd0.85Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ddataŸ±Çaoa.Ÿ±Ç`eshapeŸ±Ç`a[Ÿ±Çbmia1Ÿ±Ç`a]Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`cfigŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`baxŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`hsubplotsŸ±Ç`a(Ÿ±Ç`gfigsizeŸ±Çaoa=Ÿ±Ç`a(Ÿ±Çbmfc9.2Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia5Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`linvert_yaxisŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`exaxisŸ±Çaoa.Ÿ±Ç`kset_visibleŸ±Ç`a(Ÿ±ÇbkceFalseŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`hset_xlimŸ±Ç`a(Ÿ±Çbmia0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`csumŸ±Ç`a(Ÿ±Ç`ddataŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`daxisŸ±Çaoa=Ÿ±Çbmia1Ÿ±Ç`a)Ÿ±Çaoa.Ÿ±Ç`cmaxŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±ÇakcforŸ±Ç`a Ÿ±Ç`aiŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`a(Ÿ±Ç`gcolnameŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ecolorŸ±Ç`a)Ÿ±Ç`a Ÿ±ÇbowbinŸ±Ç`a Ÿ±ÇbnbienumerateŸ±Ç`a(Ÿ±ÇbnbczipŸ±Ç`a(Ÿ±Ç`ncategory_namesŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ocategory_colorsŸ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±Ç`fwidthsŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`ddataŸ±Ç`a[Ÿ±Ç`a:Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`aiŸ±Ç`a]Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±Ç`fstartsŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`hdata_cumŸ±Ç`a[Ÿ±Ç`a:Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`aiŸ±Ç`a]Ÿ±Ç`a Ÿ±Çaoa-Ÿ±Ç`a Ÿ±Ç`fwidthsŸ±Ç`a
Ÿ±Ç`h        Ÿ±Ç`erectsŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`dbarhŸ±Ç`a(Ÿ±Ç`flabelsŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`fwidthsŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dleftŸ±Çaoa=Ÿ±Ç`fstartsŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`fheightŸ±Çaoa=Ÿ±Çbmfc0.5Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`x                        Ÿ±Ç`elabelŸ±Çaoa=Ÿ±Ç`gcolnameŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ecolorŸ±Çaoa=Ÿ±Ç`ecolorŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±Ç`arŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`agŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`abŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`a_Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`ecolorŸ±Ç`a
Ÿ±Ç`h        Ÿ±Ç`jtext_colorŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1ewhiteŸ±Çbs1a'Ÿ±Ç`a Ÿ±ÇakbifŸ±Ç`a Ÿ±Ç`arŸ±Ç`a Ÿ±Çaoa*Ÿ±Ç`a Ÿ±Ç`agŸ±Ç`a Ÿ±Çaoa*Ÿ±Ç`a Ÿ±Ç`abŸ±Ç`a Ÿ±Çaoa<Ÿ±Ç`a Ÿ±Çbmfc0.5Ÿ±Ç`a Ÿ±ÇakdelseŸ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1hdarkgreyŸ±Çbs1a'Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`ibar_labelŸ±Ç`a(Ÿ±Ç`erectsŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`jlabel_typeŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1fcenterŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ecolorŸ±Çaoa=Ÿ±Ç`jtext_colorŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`flegendŸ±Ç`a(Ÿ±Ç`dncolŸ±Çaoa=Ÿ±ÇbnbclenŸ±Ç`a(Ÿ±Ç`ncategory_namesŸ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`nbbox_to_anchorŸ±Çaoa=Ÿ±Ç`a(Ÿ±Çbmia0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia1Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`n              Ÿ±Ç`clocŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1jlower leftŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`hfontsizeŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1esmallŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±ÇakfreturnŸ±Ç`a Ÿ±Ç`cfigŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`baxŸ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`fsurveyŸ±Ç`a(Ÿ±Ç`gresultsŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ncategory_namesŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`dshowŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1xM#############################################################################Ÿ±Ç`a
Ÿ±Çbc1a#Ÿ±Ç`a
Ÿ±Çbc1x# .. admonition:: ReferencesŸ±Ç`a
Ÿ±Çbc1a#Ÿ±Ç`a
Ÿ±Çbc1xN#    The use of the following functions, methods, classes and modules is shownŸ±Ç`a
Ÿ±Çbc1u#    in this example:Ÿ±Ç`a
Ÿ±Çbc1a#Ÿ±Ç`a
Ÿ±Çbc1x=#    - `matplotlib.axes.Axes.barh` / `matplotlib.pyplot.barh`Ÿ±Ç`a
Ÿ±Çbc1xG#    - `matplotlib.axes.Axes.bar_label` / `matplotlib.pyplot.bar_label`Ÿ±Ç`a
Ÿ±Çbc1xA#    - `matplotlib.axes.Axes.legend` / `matplotlib.pyplot.legend`Ÿ±Ç`a
`dNoneˆ