ŸØÇÅŸ¥Éô5Ÿ±Çbsdx≥"""
=========
Hat graph
=========
This example shows how to create a `hat graph`_ and how to annotate it with
labels.

.. _hat graph: https://doi.org/10.1186/s41235-019-0182-3
"""Ÿ±Ç`a
Ÿ±ÇbknfimportŸ±Ç`a Ÿ±ÇbnnŸ¢ÑenumpyŸ†Ñenumpyf1.22.3fmoduleenumpyfmoduleıŸ±Ç`a Ÿ±ÇakbasŸ±Ç`a Ÿ±ÇbnnbnpŸ±Ç`a
Ÿ±ÇbknfimportŸ±Ç`a Ÿ±ÇbnnŸ¢ÑjmatplotlibŸ†Ñjmatplotlibe3.5.1fmodulejmatplotlibfmoduleıŸ±Çbnna.Ÿ±ÇbnnfpyplotŸ±Ç`a Ÿ±ÇakbasŸ±Ç`a Ÿ±ÇbnncpltŸ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±ÇakcdefŸ±Ç`a Ÿ±Çbnfihat_graphŸ±Ç`a(Ÿ±Ç`baxŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`gxlabelsŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`fvaluesŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`lgroup_labelsŸ±Ç`a)Ÿ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Çbsdy """
    Create a hat graph.

    Parameters
    ----------
    ax : matplotlib.axes.Axes
        The Axes to plot into.
    xlabels : list of str
        The category names to be displayed on the x-axis.
    values : (M, N) array-like
        The data values.
        Rows are the groups (len(group_labels) == M).
        Columns are the categories (len(xlabels) == N).
    group_labels : list of str
        The group labels displayed in the legend.
    """Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±ÇakcdefŸ±Ç`a Ÿ±Çbnfjlabel_barsŸ±Ç`a(Ÿ±Ç`gheightsŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`erectsŸ±Ç`a)Ÿ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±Çbsdx-"""Attach a text label on top of each bar."""Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±ÇakcforŸ±Ç`a Ÿ±Ç`fheightŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`drectŸ±Ç`a Ÿ±ÇbowbinŸ±Ç`a Ÿ±ÇbnbczipŸ±Ç`a(Ÿ±Ç`gheightsŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`erectsŸ±Ç`a)Ÿ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`l            Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`hannotateŸ±Ç`a(Ÿ±ÇbsaafŸ±Çbs1a'Ÿ±Çbsia{Ÿ±Ç`fheightŸ±Çbsia}Ÿ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`x                        Ÿ±Ç`bxyŸ±Çaoa=Ÿ±Ç`a(Ÿ±Ç`drectŸ±Çaoa.Ÿ±Ç`eget_xŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a Ÿ±Çaoa+Ÿ±Ç`a Ÿ±Ç`drectŸ±Çaoa.Ÿ±Ç`iget_widthŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a Ÿ±Çaoa/Ÿ±Ç`a Ÿ±Çbmia2Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`fheightŸ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`x                        Ÿ±Ç`fxytextŸ±Çaoa=Ÿ±Ç`a(Ÿ±Çbmia0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia4Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`b  Ÿ±Çbc1x# 4 points vertical offset.Ÿ±Ç`a
Ÿ±Ç`x                        Ÿ±Ç`jtextcoordsŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1moffset pointsŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`x                        Ÿ±Ç`bhaŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1fcenterŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`bvaŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1fbottomŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`fvaluesŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`gasarrayŸ±Ç`a(Ÿ±Ç`fvaluesŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`axŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`farangeŸ±Ç`a(Ÿ±Ç`fvaluesŸ±Çaoa.Ÿ±Ç`eshapeŸ±Ç`a[Ÿ±Çbmia1Ÿ±Ç`a]Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`jset_xticksŸ±Ç`a(Ÿ±Ç`axŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`flabelsŸ±Çaoa=Ÿ±Ç`gxlabelsŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`gspacingŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Çbmfc0.3Ÿ±Ç`b  Ÿ±Çbc1x# spacing between hat groupsŸ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`ewidthŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`a(Ÿ±Çbmia1Ÿ±Ç`a Ÿ±Çaoa-Ÿ±Ç`a Ÿ±Ç`gspacingŸ±Ç`a)Ÿ±Ç`a Ÿ±Çaoa/Ÿ±Ç`a Ÿ±Ç`fvaluesŸ±Çaoa.Ÿ±Ç`eshapeŸ±Ç`a[Ÿ±Çbmia0Ÿ±Ç`a]Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`hheights0Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`fvaluesŸ±Ç`a[Ÿ±Çbmia0Ÿ±Ç`a]Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±ÇakcforŸ±Ç`a Ÿ±Ç`aiŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`a(Ÿ±Ç`gheightsŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`kgroup_labelŸ±Ç`a)Ÿ±Ç`a Ÿ±ÇbowbinŸ±Ç`a Ÿ±ÇbnbienumerateŸ±Ç`a(Ÿ±ÇbnbczipŸ±Ç`a(Ÿ±Ç`fvaluesŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`lgroup_labelsŸ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±Ç`estyleŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`a{Ÿ±Çbs1a'Ÿ±Çbs1dfillŸ±Çbs1a'Ÿ±Ç`a:Ÿ±Ç`a Ÿ±ÇbkceFalseŸ±Ç`a}Ÿ±Ç`a Ÿ±ÇakbifŸ±Ç`a Ÿ±Ç`aiŸ±Ç`a Ÿ±Çaob==Ÿ±Ç`a Ÿ±Çbmia0Ÿ±Ç`a Ÿ±ÇakdelseŸ±Ç`a Ÿ±Ç`a{Ÿ±Çbs1a'Ÿ±Çbs1iedgecolorŸ±Çbs1a'Ÿ±Ç`a:Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1eblackŸ±Çbs1a'Ÿ±Ç`a}Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±Ç`erectsŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`cbarŸ±Ç`a(Ÿ±Ç`axŸ±Ç`a Ÿ±Çaoa-Ÿ±Ç`a Ÿ±Ç`gspacingŸ±Çaoa/Ÿ±Çbmia2Ÿ±Ç`a Ÿ±Çaoa+Ÿ±Ç`a Ÿ±Ç`aiŸ±Ç`a Ÿ±Çaoa*Ÿ±Ç`a Ÿ±Ç`ewidthŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`gheightsŸ±Ç`a Ÿ±Çaoa-Ÿ±Ç`a Ÿ±Ç`hheights0Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`w                       Ÿ±Ç`ewidthŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`fbottomŸ±Çaoa=Ÿ±Ç`hheights0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`elabelŸ±Çaoa=Ÿ±Ç`kgroup_labelŸ±Ç`a,Ÿ±Ç`a Ÿ±Çaoa*Ÿ±Çaoa*Ÿ±Ç`estyleŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±Ç`jlabel_barsŸ±Ç`a(Ÿ±Ç`gheightsŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`erectsŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1x8# initialise labels and a numpy array make sure you haveŸ±Ç`a
Ÿ±Çbc1x-# N labels of N number of values in the arrayŸ±Ç`a
Ÿ±Ç`gxlabelsŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`a[Ÿ±Çbs1a'Ÿ±Çbs1aIŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1bIIŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1cIIIŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1bIVŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1aVŸ±Çbs1a'Ÿ±Ç`a]Ÿ±Ç`a
Ÿ±Ç`gplayerAŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`earrayŸ±Ç`a(Ÿ±Ç`a[Ÿ±Çbmia5Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmib15Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmib22Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmib20Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmib25Ÿ±Ç`a]Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`gplayerBŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`earrayŸ±Ç`a(Ÿ±Ç`a[Ÿ±Çbmib25Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmib32Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmib34Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmib30Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmib27Ÿ±Ç`a]Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`cfigŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`baxŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`hsubplotsŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`ihat_graphŸ±Ç`a(Ÿ±Ç`baxŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`gxlabelsŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`a[Ÿ±Ç`gplayerAŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`gplayerBŸ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`a[Ÿ±Çbs1a'Ÿ±Çbs1hPlayer AŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1hPlayer BŸ±Çbs1a'Ÿ±Ç`a]Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1xE# Add some text for labels, title and custom x-axis tick labels, etc.Ÿ±Ç`a
Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`jset_xlabelŸ±Ç`a(Ÿ±Çbs1a'Ÿ±Çbs1eGamesŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`jset_ylabelŸ±Ç`a(Ÿ±Çbs1a'Ÿ±Çbs1eScoreŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`hset_ylimŸ±Ç`a(Ÿ±Çbmia0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmib60Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`iset_titleŸ±Ç`a(Ÿ±Çbs1a'Ÿ±Çbs1x$Scores by number of game and playersŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`flegendŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`cfigŸ±Çaoa.Ÿ±Ç`ltight_layoutŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`dshowŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Çbc1xM#############################################################################Ÿ±Ç`a
Ÿ±Çbc1a#Ÿ±Ç`a
Ÿ±Çbc1x# .. admonition:: ReferencesŸ±Ç`a
Ÿ±Çbc1a#Ÿ±Ç`a
Ÿ±Çbc1xN#    The use of the following functions, methods, classes and modules is shownŸ±Ç`a
Ÿ±Çbc1u#    in this example:Ÿ±Ç`a
Ÿ±Çbc1a#Ÿ±Ç`a
Ÿ±Çbc1x;#    - `matplotlib.axes.Axes.bar` / `matplotlib.pyplot.bar`Ÿ±Ç`a
Ÿ±Çbc1xE#    - `matplotlib.axes.Axes.annotate` / `matplotlib.pyplot.annotate`Ÿ±Ç`a
`dNoneˆ