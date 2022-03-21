ŸØÇÅŸ¥Éô2Ÿ±Çbsdx{"""
================
The Sankey class
================

Demonstrate the Sankey class by producing three basic diagrams.
"""Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±ÇbknfimportŸ±Ç`a Ÿ±ÇbnnŸ¢ÑjmatplotlibŸ†Ñjmatplotlibe3.5.1fmodulejmatplotlibfmoduleıŸ±Çbnna.Ÿ±ÇbnnfpyplotŸ±Ç`a Ÿ±ÇakbasŸ±Ç`a Ÿ±ÇbnncpltŸ±Ç`a
Ÿ±Ç`a
Ÿ±ÇbkndfromŸ±Ç`a Ÿ±ÇbnnŸ¢ÑjmatplotlibŸ†Ñjmatplotlibe3.5.1fmodulejmatplotlibfmoduleıŸ±Çbnna.Ÿ±ÇbnnfsankeyŸ±Ç`a Ÿ±ÇbknfimportŸ±Ç`a Ÿ±Ç`fSankeyŸ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1xO###############################################################################Ÿ±Ç`a
Ÿ±Çbc1x# Example 1 -- Mostly defaultsŸ±Ç`a
Ÿ±Çbc1a#Ÿ±Ç`a
Ÿ±Çbc1xL# This demonstrates how to create a simple diagram by implicitly calling theŸ±Ç`a
Ÿ±Çbc1xI# Sankey.add() method and by appending finish() to the call to the class.Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`fSankeyŸ±Ç`a(Ÿ±Ç`eflowsŸ±Çaoa=Ÿ±Ç`a[Ÿ±Çbmfd0.25Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd0.15Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd0.60Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çaoa-Ÿ±Çbmfd0.20Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çaoa-Ÿ±Çbmfd0.15Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çaoa-Ÿ±Çbmfd0.05Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çaoa-Ÿ±Çbmfd0.50Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çaoa-Ÿ±Çbmfd0.10Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`g       Ÿ±Ç`flabelsŸ±Çaoa=Ÿ±Ç`a[Ÿ±Çbs1a'Ÿ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1eFirstŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1fSecondŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1eThirdŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1fFourthŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1eFifthŸ±Çbs1a'Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`g       Ÿ±Ç`lorientationsŸ±Çaoa=Ÿ±Ç`a[Ÿ±Çaoa-Ÿ±Çbmia1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çaoa-Ÿ±Çbmia1Ÿ±Ç`a]Ÿ±Ç`a)Ÿ±Çaoa.Ÿ±Ç`ffinishŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`etitleŸ±Ç`a(Ÿ±Çbs2a"Ÿ±Çbs2x1The default settings produce a diagram like this.Ÿ±Çbs2a"Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1xO###############################################################################Ÿ±Ç`a
Ÿ±Çbc1i# Notice:Ÿ±Ç`a
Ÿ±Çbc1a#Ÿ±Ç`a
Ÿ±Çbc1xG# 1. Axes weren't provided when Sankey() was instantiated, so they wereŸ±Ç`a
Ÿ±Çbc1x#    created automatically.Ÿ±Ç`a
Ÿ±Çbc1xC# 2. The scale argument wasn't necessary since the data was alreadyŸ±Ç`a
Ÿ±Çbc1p#    normalized.Ÿ±Ç`a
Ÿ±Çbc1x8# 3. By default, the lengths of the paths are justified.Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1xO###############################################################################Ÿ±Ç`a
Ÿ±Çbc1k# Example 2Ÿ±Ç`a
Ÿ±Çbc1a#Ÿ±Ç`a
Ÿ±Çbc1t# This demonstrates:Ÿ±Ç`a
Ÿ±Çbc1a#Ÿ±Ç`a
Ÿ±Çbc1x,# 1. Setting one path longer than the othersŸ±Ç`a
Ÿ±Çbc1x1# 2. Placing a label in the middle of the diagramŸ±Ç`a
Ÿ±Çbc1x4# 3. Using the scale argument to normalize the flowsŸ±Ç`a
Ÿ±Çbc1x8# 4. Implicitly passing keyword arguments to PathPatch()Ÿ±Ç`a
Ÿ±Çbc1x*# 5. Changing the angle of the arrow headsŸ±Ç`a
Ÿ±Çbc1xG# 6. Changing the offset between the tips of the paths and their labelsŸ±Ç`a
Ÿ±Çbc1xF# 7. Formatting the numbers in the path labels and the associated unitŸ±Ç`a
Ÿ±Çbc1xL# 8. Changing the appearance of the patch and the labels after the figure isŸ±Ç`a
Ÿ±Çbc1l#    createdŸ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`cfigŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`ffigureŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`baxŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cfigŸ±Çaoa.Ÿ±Ç`kadd_subplotŸ±Ç`a(Ÿ±Çbmia1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`fxticksŸ±Çaoa=Ÿ±Ç`a[Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`fyticksŸ±Çaoa=Ÿ±Ç`a[Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`u                     Ÿ±Ç`etitleŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2xFlow Diagram of a WidgetŸ±Çbs2a"Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`fsankeyŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`fSankeyŸ±Ç`a(Ÿ±Ç`baxŸ±Çaoa=Ÿ±Ç`baxŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`escaleŸ±Çaoa=Ÿ±Çbmfd0.01Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`foffsetŸ±Çaoa=Ÿ±Çbmfc0.2Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`jhead_angleŸ±Çaoa=Ÿ±Çbmic180Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`p                Ÿ±ÇbnbfformatŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbsid%.0fŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dunitŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1a%Ÿ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`fsankeyŸ±Çaoa.Ÿ±Ç`caddŸ±Ç`a(Ÿ±Ç`eflowsŸ±Çaoa=Ÿ±Ç`a[Ÿ±Çbmib25Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmib60Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çaoa-Ÿ±Çbmib10Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çaoa-Ÿ±Çbmib20Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çaoa-Ÿ±Çbmia5Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çaoa-Ÿ±Çbmib15Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çaoa-Ÿ±Çbmib10Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çaoa-Ÿ±Çbmib40Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`k           Ÿ±Ç`flabelsŸ±Çaoa=Ÿ±Ç`a[Ÿ±Çbs1a'Ÿ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1eFirstŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1fSecondŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1eThirdŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1fFourthŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`s                   Ÿ±Çbs1a'Ÿ±Çbs1eFifthŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1gHurray!Ÿ±Çbs1a'Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`k           Ÿ±Ç`lorientationsŸ±Çaoa=Ÿ±Ç`a[Ÿ±Çaoa-Ÿ±Çbmia1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çaoa-Ÿ±Çbmia1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çaoa-Ÿ±Çbmia1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia0Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`k           Ÿ±Ç`kpathlengthsŸ±Çaoa=Ÿ±Ç`a[Ÿ±Çbmfd0.25Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd0.25Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd0.25Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd0.25Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd0.25Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfc0.6Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd0.25Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd0.25Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`x                        Ÿ±Çbmfd0.25Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`k           Ÿ±Ç`jpatchlabelŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2fWidgetŸ±Çbseb\nŸ±Çbs2aAŸ±Çbs2a"Ÿ±Ç`a)Ÿ±Ç`b  Ÿ±Çbc1x+# Arguments to matplotlib.patches.PathPatchŸ±Ç`a
Ÿ±Ç`hdiagramsŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`fsankeyŸ±Çaoa.Ÿ±Ç`ffinishŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`hdiagramsŸ±Ç`a[Ÿ±Çbmia0Ÿ±Ç`a]Ÿ±Çaoa.Ÿ±Ç`etextsŸ±Ç`a[Ÿ±Çaoa-Ÿ±Çbmia1Ÿ±Ç`a]Ÿ±Çaoa.Ÿ±Ç`iset_colorŸ±Ç`a(Ÿ±Çbs1a'Ÿ±Çbs1arŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`hdiagramsŸ±Ç`a[Ÿ±Çbmia0Ÿ±Ç`a]Ÿ±Çaoa.Ÿ±Ç`dtextŸ±Çaoa.Ÿ±Ç`nset_fontweightŸ±Ç`a(Ÿ±Çbs1a'Ÿ±Çbs1dboldŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1xO###############################################################################Ÿ±Ç`a
Ÿ±Çbc1i# Notice:Ÿ±Ç`a
Ÿ±Çbc1a#Ÿ±Ç`a
Ÿ±Çbc1xH# 1. Since the sum of the flows is nonzero, the width of the trunk isn'tŸ±Ç`a
Ÿ±Çbc1xJ#    uniform.  The matplotlib logging system logs this at the DEBUG level.Ÿ±Ç`a
Ÿ±Çbc1xN# 2. The second flow doesn't appear because its value is zero.  Again, this isŸ±Ç`a
Ÿ±Çbc1x#    logged at the DEBUG level.Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1xO###############################################################################Ÿ±Ç`a
Ÿ±Çbc1k# Example 3Ÿ±Ç`a
Ÿ±Çbc1a#Ÿ±Ç`a
Ÿ±Çbc1t# This demonstrates:Ÿ±Ç`a
Ÿ±Çbc1a#Ÿ±Ç`a
Ÿ±Çbc1x# 1. Connecting two systemsŸ±Ç`a
Ÿ±Çbc1x-# 2. Turning off the labels of the quantitiesŸ±Ç`a
Ÿ±Çbc1t# 3. Adding a legendŸ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`cfigŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`ffigureŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`baxŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cfigŸ±Çaoa.Ÿ±Ç`kadd_subplotŸ±Ç`a(Ÿ±Çbmia1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`fxticksŸ±Çaoa=Ÿ±Ç`a[Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`fyticksŸ±Çaoa=Ÿ±Ç`a[Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`etitleŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2kTwo SystemsŸ±Çbs2a"Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`eflowsŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`a[Ÿ±Çbmfd0.25Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd0.15Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd0.60Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çaoa-Ÿ±Çbmfd0.10Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çaoa-Ÿ±Çbmfd0.05Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çaoa-Ÿ±Çbmfd0.25Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çaoa-Ÿ±Çbmfd0.15Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çaoa-Ÿ±Çbmfd0.10Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çaoa-Ÿ±Çbmfd0.35Ÿ±Ç`a]Ÿ±Ç`a
Ÿ±Ç`fsankeyŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`fSankeyŸ±Ç`a(Ÿ±Ç`baxŸ±Çaoa=Ÿ±Ç`baxŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dunitŸ±Çaoa=Ÿ±ÇbkcdNoneŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`fsankeyŸ±Çaoa.Ÿ±Ç`caddŸ±Ç`a(Ÿ±Ç`eflowsŸ±Çaoa=Ÿ±Ç`eflowsŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`elabelŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1coneŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`k           Ÿ±Ç`lorientationsŸ±Çaoa=Ÿ±Ç`a[Ÿ±Çaoa-Ÿ±Çbmia1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çaoa-Ÿ±Çbmia1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çaoa-Ÿ±Çbmia1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia0Ÿ±Ç`a]Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`fsankeyŸ±Çaoa.Ÿ±Ç`caddŸ±Ç`a(Ÿ±Ç`eflowsŸ±Çaoa=Ÿ±Ç`a[Ÿ±Çaoa-Ÿ±Çbmfd0.25Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd0.15Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfc0.1Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`elabelŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1ctwoŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`k           Ÿ±Ç`lorientationsŸ±Çaoa=Ÿ±Ç`a[Ÿ±Çaoa-Ÿ±Çbmia1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çaoa-Ÿ±Çbmia1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çaoa-Ÿ±Çbmia1Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`epriorŸ±Çaoa=Ÿ±Çbmia0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`gconnectŸ±Çaoa=Ÿ±Ç`a(Ÿ±Çbmia0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia0Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`hdiagramsŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`fsankeyŸ±Çaoa.Ÿ±Ç`ffinishŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`hdiagramsŸ±Ç`a[Ÿ±Çaoa-Ÿ±Çbmia1Ÿ±Ç`a]Ÿ±Çaoa.Ÿ±Ç`epatchŸ±Çaoa.Ÿ±Ç`iset_hatchŸ±Ç`a(Ÿ±Çbs1a'Ÿ±Çbs1a/Ÿ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`flegendŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1xO###############################################################################Ÿ±Ç`a
Ÿ±Çbc1xF# Notice that only one connection is specified, but the systems form aŸ±Ç`a
Ÿ±Çbc1xG# circuit since: (1) the lengths of the paths are justified and (2) theŸ±Ç`a
Ÿ±Çbc1x4# orientation and ordering of the flows is mirrored.Ÿ±Ç`a
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
Ÿ±Çbc1x#    - `matplotlib.sankey`Ÿ±Ç`a
Ÿ±Çbc1x!#    - `matplotlib.sankey.Sankey`Ÿ±Ç`a
Ÿ±Çbc1x%#    - `matplotlib.sankey.Sankey.add`Ÿ±Ç`a
Ÿ±Çbc1x(#    - `matplotlib.sankey.Sankey.finish`Ÿ±Ç`a
`dNoneˆ