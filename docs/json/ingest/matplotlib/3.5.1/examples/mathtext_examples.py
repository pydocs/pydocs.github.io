Ù¯‚Ù´ƒ™Ù±‚bsdxw"""
=================
Mathtext Examples
=================

Selected features of Matplotlib's math rendering engine.
"""Ù±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnbreÙ±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnjsubprocessÙ±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnncsysÙ±‚`a
Ù±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnnfpyplotÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnncpltÙ±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚bc1xN# Selection of features following "Writing mathematical expressions" tutorial,Ù±‚`a
Ù±‚bc1x # with randomly picked examples.Ù±‚`a
Ù±‚`nmathtext_demosÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`a{Ù±‚`a
Ù±‚`d    Ù±‚bs2a"Ù±‚bs2kHeader demoÙ±‚bs2a"Ù±‚`a:Ù±‚`a
Ù±‚`h        Ù±‚bsaarÙ±‚bs2a"Ù±‚bs2c$W^Ù±‚bs2a{Ù±‚bs2a3Ù±‚bs2a\Ù±‚bs2fbeta}_Ù±‚bs2a{Ù±‚bs2a\Ù±‚bs2hdelta_1 Ù±‚bs2a\Ù±‚bs2frho_1 Ù±‚bs2a\Ù±‚bs2ksigma_2} = Ù±‚bs2a"Ù±‚`a
Ù±‚`h        Ù±‚bsaarÙ±‚bs2a"Ù±‚bs2bU^Ù±‚bs2a{Ù±‚bs2a3Ù±‚bs2a\Ù±‚bs2fbeta}_Ù±‚bs2a{Ù±‚bs2a\Ù±‚bs2hdelta_1 Ù±‚bs2a\Ù±‚bs2irho_1} + Ù±‚bs2a\Ù±‚bs2dfracÙ±‚bsic{1}Ù±‚bs2a{Ù±‚bs2b8 Ù±‚bs2a\Ù±‚bs2fpi 2} Ù±‚bs2a"Ù±‚`a
Ù±‚`h        Ù±‚bsaarÙ±‚bs2a"Ù±‚bs2a\Ù±‚bs2dint^Ù±‚bs2a{Ù±‚bs2a\Ù±‚bs2ialpha_2}_Ù±‚bs2a{Ù±‚bs2a\Ù±‚bs2kalpha_2} d Ù±‚bs2a\Ù±‚bs2falpha^Ù±‚bs2a\Ù±‚bs2hprime_2 Ù±‚bs2a\Ù±‚bs2eleft[Ù±‚bs2a\Ù±‚bs2dfracÙ±‚bs2a{Ù±‚bs2a Ù±‚bs2a"Ù±‚`a
Ù±‚`h        Ù±‚bsaarÙ±‚bs2a"Ù±‚bs2bU^Ù±‚bs2a{Ù±‚bs2a2Ù±‚bs2a\Ù±‚bs2fbeta}_Ù±‚bs2a{Ù±‚bs2a\Ù±‚bs2hdelta_1 Ù±‚bs2a\Ù±‚bs2irho_1} - Ù±‚bs2a\Ù±‚bs2falpha^Ù±‚bs2a\Ù±‚bs2iprime_2U^Ù±‚bs2a{Ù±‚bs2a1Ù±‚bs2a\Ù±‚bs2fbeta}_Ù±‚bs2a"Ù±‚`a
Ù±‚`h        Ù±‚bsaarÙ±‚bs2a"Ù±‚bs2a{Ù±‚bs2a\Ù±‚bs2frho_1 Ù±‚bs2a\Ù±‚bs2jsigma_2} }Ù±‚bs2a{Ù±‚bs2bU^Ù±‚bs2a{Ù±‚bs2a0Ù±‚bs2a\Ù±‚bs2fbeta}_Ù±‚bs2a{Ù±‚bs2a\Ù±‚bs2frho_1 Ù±‚bs2a\Ù±‚bs2isigma_2}}Ù±‚bs2a\Ù±‚bs2gright]$Ù±‚bs2a"Ù±‚`a,Ù±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚bs2a"Ù±‚bs2xSubscripts and superscriptsÙ±‚bs2a"Ù±‚`a:Ù±‚`a
Ù±‚`h        Ù±‚bsaarÙ±‚bs2a"Ù±‚bs2a$Ù±‚bs2a\Ù±‚bs2jalpha_i > Ù±‚bs2a\Ù±‚bs2gbeta_i,Ù±‚bs2a\Ù±‚bs2a Ù±‚bs2a"Ù±‚`a
Ù±‚`h        Ù±‚bsaarÙ±‚bs2a"Ù±‚bs2a\Ù±‚bs2falpha_Ù±‚bs2a{Ù±‚bs2ii+1}^j = Ù±‚bs2a{Ù±‚bs2a\Ù±‚bs2irm sin}(2Ù±‚bs2a\Ù±‚bs2npi f_j t_i) e^Ù±‚bs2a{Ù±‚bs2g-5 t_i/Ù±‚bs2a\Ù±‚bs2etau},Ù±‚bs2a\Ù±‚bs2a Ù±‚bs2a"Ù±‚`a
Ù±‚`h        Ù±‚bsaarÙ±‚bs2a"Ù±‚bs2a\Ù±‚bs2fldots$Ù±‚bs2a"Ù±‚`a,Ù±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚bs2a"Ù±‚bs2x(Fractions, binomials and stacked numbersÙ±‚bs2a"Ù±‚`a:Ù±‚`a
Ù±‚`h        Ù±‚bsaarÙ±‚bs2a"Ù±‚bs2a$Ù±‚bs2a\Ù±‚bs2dfracÙ±‚bsic{3}Ù±‚bsic{4}Ù±‚bs2a,Ù±‚bs2a\Ù±‚bs2a Ù±‚bs2a\Ù±‚bs2ebinomÙ±‚bsic{3}Ù±‚bsic{4}Ù±‚bs2a,Ù±‚bs2a\Ù±‚bs2a Ù±‚bs2a\Ù±‚bs2ggenfracÙ±‚bsib{}Ù±‚bsib{}Ù±‚bsic{0}Ù±‚bsib{}Ù±‚bsic{3}Ù±‚bsic{4}Ù±‚bs2a,Ù±‚bs2a\Ù±‚bs2a Ù±‚bs2a"Ù±‚`a
Ù±‚`h        Ù±‚bsaarÙ±‚bs2a"Ù±‚bs2a\Ù±‚bs2eleft(Ù±‚bs2a\Ù±‚bs2dfracÙ±‚bs2a{Ù±‚bs2d5 - Ù±‚bs2a\Ù±‚bs2dfracÙ±‚bsic{1}Ù±‚bsic{x}Ù±‚bs2a}Ù±‚bsic{4}Ù±‚bs2a\Ù±‚bs2gright),Ù±‚bs2a\Ù±‚bs2a Ù±‚bs2a\Ù±‚bs2fldots$Ù±‚bs2a"Ù±‚`a,Ù±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚bs2a"Ù±‚bs2hRadicalsÙ±‚bs2a"Ù±‚`a:Ù±‚`a
Ù±‚`h        Ù±‚bsaarÙ±‚bs2a"Ù±‚bs2a$Ù±‚bs2a\Ù±‚bs2dsqrtÙ±‚bsic{2}Ù±‚bs2a,Ù±‚bs2a\Ù±‚bs2a Ù±‚bs2a\Ù±‚bs2gsqrt[3]Ù±‚bsic{x}Ù±‚bs2a,Ù±‚bs2a\Ù±‚bs2a Ù±‚bs2a\Ù±‚bs2fldots$Ù±‚bs2a"Ù±‚`a,Ù±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚bs2a"Ù±‚bs2eFontsÙ±‚bs2a"Ù±‚`a:Ù±‚`a
Ù±‚`h        Ù±‚bsaarÙ±‚bs2a"Ù±‚bs2a$Ù±‚bs2a\Ù±‚bs2fmathrmÙ±‚bsig{Roman}Ù±‚bs2a\Ù±‚bs2c , Ù±‚bs2a\Ù±‚bs2a Ù±‚bs2a\Ù±‚bs2fmathitÙ±‚bsih{Italic}Ù±‚bs2a\Ù±‚bs2c , Ù±‚bs2a\Ù±‚bs2a Ù±‚bs2a\Ù±‚bs2fmathttÙ±‚bsil{Typewriter}Ù±‚bs2a Ù±‚bs2a\Ù±‚bs2a Ù±‚bs2a"Ù±‚`a
Ù±‚`h        Ù±‚bsaarÙ±‚bs2a"Ù±‚bs2a\Ù±‚bs2fmathrmÙ±‚bsid{or}Ù±‚bs2a\Ù±‚bs2a Ù±‚bs2a\Ù±‚bs2gmathcalÙ±‚bsim{CALLIGRAPHY}Ù±‚bs2a$Ù±‚bs2a"Ù±‚`a,Ù±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚bs2a"Ù±‚bs2gAccentsÙ±‚bs2a"Ù±‚`a:Ù±‚`a
Ù±‚`h        Ù±‚bsaarÙ±‚bs2a"Ù±‚bs2a$Ù±‚bs2a\Ù±‚bs2hacute a,Ù±‚bs2a\Ù±‚bs2a Ù±‚bs2a\Ù±‚bs2fbar a,Ù±‚bs2a\Ù±‚bs2a Ù±‚bs2a\Ù±‚bs2hbreve a,Ù±‚bs2a\Ù±‚bs2a Ù±‚bs2a\Ù±‚bs2fdot a,Ù±‚bs2a\Ù±‚bs2a Ù±‚bs2a\Ù±‚bs2hddot a, Ù±‚bs2a\Ù±‚bs2a Ù±‚bs2a\Ù±‚bs2igrave a, Ù±‚bs2a\Ù±‚bs2a Ù±‚bs2a"Ù±‚`a
Ù±‚`h        Ù±‚bsaarÙ±‚bs2a"Ù±‚bs2a\Ù±‚bs2fhat a,Ù±‚bs2a\Ù±‚bs2a Ù±‚bs2a\Ù±‚bs2htilde a,Ù±‚bs2a\Ù±‚bs2a Ù±‚bs2a\Ù±‚bs2fvec a,Ù±‚bs2a\Ù±‚bs2a Ù±‚bs2a\Ù±‚bs2gwidehatÙ±‚bsie{xyz}Ù±‚bs2a,Ù±‚bs2a\Ù±‚bs2a Ù±‚bs2a\Ù±‚bs2iwidetildeÙ±‚bsie{xyz}Ù±‚bs2a,Ù±‚bs2a\Ù±‚bs2a Ù±‚bs2a"Ù±‚`a
Ù±‚`h        Ù±‚bsaarÙ±‚bs2a"Ù±‚bs2a\Ù±‚bs2fldots$Ù±‚bs2a"Ù±‚`a,Ù±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚bs2a"Ù±‚bs2mGreek, HebrewÙ±‚bs2a"Ù±‚`a:Ù±‚`a
Ù±‚`h        Ù±‚bsaarÙ±‚bs2a"Ù±‚bs2a$Ù±‚bs2a\Ù±‚bs2falpha,Ù±‚bs2a\Ù±‚bs2a Ù±‚bs2a\Ù±‚bs2ebeta,Ù±‚bs2a\Ù±‚bs2a Ù±‚bs2a\Ù±‚bs2dchi,Ù±‚bs2a\Ù±‚bs2a Ù±‚bs2a\Ù±‚bs2fdelta,Ù±‚bs2a\Ù±‚bs2a Ù±‚bs2a\Ù±‚bs2glambda,Ù±‚bs2a\Ù±‚bs2a Ù±‚bs2a\Ù±‚bs2cmu,Ù±‚bs2a\Ù±‚bs2a Ù±‚bs2a"Ù±‚`a
Ù±‚`h        Ù±‚bsaarÙ±‚bs2a"Ù±‚bs2a\Ù±‚bs2fDelta,Ù±‚bs2a\Ù±‚bs2a Ù±‚bs2a\Ù±‚bs2fGamma,Ù±‚bs2a\Ù±‚bs2a Ù±‚bs2a\Ù±‚bs2fOmega,Ù±‚bs2a\Ù±‚bs2a Ù±‚bs2a\Ù±‚bs2dPhi,Ù±‚bs2a\Ù±‚bs2a Ù±‚bs2a\Ù±‚bs2cPi,Ù±‚bs2a\Ù±‚bs2a Ù±‚bs2a\Ù±‚bs2hUpsilon,Ù±‚bs2a\Ù±‚bs2a Ù±‚bs2a\Ù±‚bs2fnabla,Ù±‚bs2a\Ù±‚bs2a Ù±‚bs2a"Ù±‚`a
Ù±‚`h        Ù±‚bsaarÙ±‚bs2a"Ù±‚bs2a\Ù±‚bs2faleph,Ù±‚bs2a\Ù±‚bs2a Ù±‚bs2a\Ù±‚bs2ebeth,Ù±‚bs2a\Ù±‚bs2a Ù±‚bs2a\Ù±‚bs2gdaleth,Ù±‚bs2a\Ù±‚bs2a Ù±‚bs2a\Ù±‚bs2fgimel,Ù±‚bs2a\Ù±‚bs2a Ù±‚bs2a\Ù±‚bs2fldots$Ù±‚bs2a"Ù±‚`a,Ù±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚bs2a"Ù±‚bs2x!Delimiters, functions and SymbolsÙ±‚bs2a"Ù±‚`a:Ù±‚`a
Ù±‚`h        Ù±‚bsaarÙ±‚bs2a"Ù±‚bs2a$Ù±‚bs2a\Ù±‚bs2gcoprod,Ù±‚bs2a\Ù±‚bs2a Ù±‚bs2a\Ù±‚bs2dint,Ù±‚bs2a\Ù±‚bs2a Ù±‚bs2a\Ù±‚bs2eoint,Ù±‚bs2a\Ù±‚bs2a Ù±‚bs2a\Ù±‚bs2eprod,Ù±‚bs2a\Ù±‚bs2a Ù±‚bs2a\Ù±‚bs2dsum,Ù±‚bs2a\Ù±‚bs2a Ù±‚bs2a"Ù±‚`a
Ù±‚`h        Ù±‚bsaarÙ±‚bs2a"Ù±‚bs2a\Ù±‚bs2dlog,Ù±‚bs2a\Ù±‚bs2a Ù±‚bs2a\Ù±‚bs2dsin,Ù±‚bs2a\Ù±‚bs2a Ù±‚bs2a\Ù±‚bs2gapprox,Ù±‚bs2a\Ù±‚bs2a Ù±‚bs2a\Ù±‚bs2foplus,Ù±‚bs2a\Ù±‚bs2a Ù±‚bs2a\Ù±‚bs2estar,Ù±‚bs2a\Ù±‚bs2a Ù±‚bs2a\Ù±‚bs2jvarpropto,Ù±‚bs2a\Ù±‚bs2a Ù±‚bs2a"Ù±‚`a
Ù±‚`h        Ù±‚bsaarÙ±‚bs2a"Ù±‚bs2a\Ù±‚bs2finfty,Ù±‚bs2a\Ù±‚bs2a Ù±‚bs2a\Ù±‚bs2hpartial,Ù±‚bs2a\Ù±‚bs2a Ù±‚bs2a\Ù±‚bs2cRe,Ù±‚bs2a\Ù±‚bs2a Ù±‚bs2a\Ù±‚bs2uleftrightsquigarrow, Ù±‚bs2a\Ù±‚bs2a Ù±‚bs2a\Ù±‚bs2fldots$Ù±‚bs2a"Ù±‚`a,Ù±‚`a
Ù±‚`a}Ù±‚`a
Ù±‚`gn_linesÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bnbclenÙ±‚`a(Ù±‚`nmathtext_demosÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚akcdefÙ±‚`a Ù±‚bnfedoallÙ±‚`a(Ù±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`d    Ù±‚bc1x1# Colors used in Matplotlib online documentation.Ù±‚`a
Ù±‚`d    Ù±‚`lmpl_grey_rgbÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`a(Ù±‚bmib51Ù±‚`a Ù±‚aoa/Ù±‚`a Ù±‚bmic255Ù±‚`a,Ù±‚`a Ù±‚bmib51Ù±‚`a Ù±‚aoa/Ù±‚`a Ù±‚bmic255Ù±‚`a,Ù±‚`a Ù±‚bmib51Ù±‚`a Ù±‚aoa/Ù±‚`a Ù±‚bmic255Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚bc1x# Creating figure and axis.Ù±‚`a
Ù±‚`d    Ù±‚`cfigÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cpltÙ±‚aoa.Ù±‚`ffigureÙ±‚`a(Ù±‚`gfigsizeÙ±‚aoa=Ù±‚`a(Ù±‚bmia7Ù±‚`a,Ù±‚`a Ù±‚bmia7Ù±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`baxÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cfigÙ±‚aoa.Ù±‚`hadd_axesÙ±‚`a(Ù±‚`a[Ù±‚bmfd0.01Ù±‚`a,Ù±‚`a Ù±‚bmfd0.01Ù±‚`a,Ù±‚`a Ù±‚bmfd0.98Ù±‚`a,Ù±‚`a Ù±‚bmfd0.90Ù±‚`a]Ù±‚`a,Ù±‚`a
Ù±‚`v                      Ù±‚`ifacecolorÙ±‚aoa=Ù±‚bs2a"Ù±‚bs2ewhiteÙ±‚bs2a"Ù±‚`a,Ù±‚`a Ù±‚`gframeonÙ±‚aoa=Ù±‚bkcdTrueÙ±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`baxÙ±‚aoa.Ù±‚`hset_xlimÙ±‚`a(Ù±‚bmia0Ù±‚`a,Ù±‚`a Ù±‚bmia1Ù±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`baxÙ±‚aoa.Ù±‚`hset_ylimÙ±‚`a(Ù±‚bmia0Ù±‚`a,Ù±‚`a Ù±‚bmia1Ù±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`baxÙ±‚aoa.Ù±‚`iset_titleÙ±‚`a(Ù±‚bs2a"Ù±‚bs2jMatplotlibÙ±‚bs2a'Ù±‚bs2ws math rendering engineÙ±‚bs2a"Ù±‚`a,Ù±‚`a
Ù±‚`q                 Ù±‚`ecolorÙ±‚aoa=Ù±‚`lmpl_grey_rgbÙ±‚`a,Ù±‚`a Ù±‚`hfontsizeÙ±‚aoa=Ù±‚bmib14Ù±‚`a,Ù±‚`a Ù±‚`fweightÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1dboldÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`baxÙ±‚aoa.Ù±‚`jset_xticksÙ±‚`a(Ù±‚`a[Ù±‚`a]Ù±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`baxÙ±‚aoa.Ù±‚`jset_yticksÙ±‚`a(Ù±‚`a[Ù±‚`a]Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚bc1x"# Gap between lines in axes coordsÙ±‚`a
Ù±‚`d    Ù±‚`mline_axesfracÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bmia1Ù±‚`a Ù±‚aoa/Ù±‚`a Ù±‚`gn_linesÙ±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚bc1x$# Plot header demonstration formula.Ù±‚`a
Ù±‚`d    Ù±‚`ifull_demoÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`nmathtext_demosÙ±‚`a[Ù±‚bs1a'Ù±‚bs1kHeader demoÙ±‚bs1a'Ù±‚`a]Ù±‚`a
Ù±‚`d    Ù±‚`baxÙ±‚aoa.Ù±‚`hannotateÙ±‚`a(Ù±‚`ifull_demoÙ±‚`a,Ù±‚`a
Ù±‚`p                Ù±‚`bxyÙ±‚aoa=Ù±‚`a(Ù±‚bmfc0.5Ù±‚`a,Ù±‚`a Ù±‚bmfb1.Ù±‚`a Ù±‚aoa-Ù±‚`a Ù±‚bmfd0.59Ù±‚`a Ù±‚aoa*Ù±‚`a Ù±‚`mline_axesfracÙ±‚`a)Ù±‚`a,Ù±‚`a
Ù±‚`p                Ù±‚`ecolorÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1jtab:orangeÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`bhaÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1fcenterÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`hfontsizeÙ±‚aoa=Ù±‚bmib20Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚bc1x&# Plot feature demonstration formulae.Ù±‚`a
Ù±‚`d    Ù±‚akcforÙ±‚`a Ù±‚`fi_lineÙ±‚`a,Ù±‚`a Ù±‚`a(Ù±‚`etitleÙ±‚`a,Ù±‚`a Ù±‚`ddemoÙ±‚`a)Ù±‚`a Ù±‚bowbinÙ±‚`a Ù±‚bnbienumerateÙ±‚`a(Ù±‚`nmathtext_demosÙ±‚aoa.Ù±‚`eitemsÙ±‚`a(Ù±‚`a)Ù±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`h        Ù±‚bnbeprintÙ±‚`a(Ù±‚`fi_lineÙ±‚`a,Ù±‚`a Ù±‚`ddemoÙ±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚akbifÙ±‚`a Ù±‚`fi_lineÙ±‚`a Ù±‚aob==Ù±‚`a Ù±‚bmia0Ù±‚`a:Ù±‚`a
Ù±‚`l            Ù±‚akhcontinueÙ±‚`a
Ù±‚`a
Ù±‚`h        Ù±‚`hbaselineÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bmia1Ù±‚`a Ù±‚aoa-Ù±‚`a Ù±‚`fi_lineÙ±‚`a Ù±‚aoa*Ù±‚`a Ù±‚`mline_axesfracÙ±‚`a
Ù±‚`h        Ù±‚`mbaseline_nextÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`hbaselineÙ±‚`a Ù±‚aoa-Ù±‚`a Ù±‚`mline_axesfracÙ±‚`a
Ù±‚`h        Ù±‚`jfill_colorÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`a[Ù±‚bs1a'Ù±‚bs1ewhiteÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚bs1a'Ù±‚bs1htab:blueÙ±‚bs1a'Ù±‚`a]Ù±‚`a[Ù±‚`fi_lineÙ±‚`a Ù±‚aoa%Ù±‚`a Ù±‚bmia2Ù±‚`a]Ù±‚`a
Ù±‚`h        Ù±‚`baxÙ±‚aoa.Ù±‚`lfill_betweenÙ±‚`a(Ù±‚`a[Ù±‚bmia0Ù±‚`a,Ù±‚`a Ù±‚bmia1Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`a[Ù±‚`hbaselineÙ±‚`a,Ù±‚`a Ù±‚`hbaselineÙ±‚`a]Ù±‚`a,Ù±‚`a
Ù±‚`x                        Ù±‚`a[Ù±‚`mbaseline_nextÙ±‚`a,Ù±‚`a Ù±‚`mbaseline_nextÙ±‚`a]Ù±‚`a,Ù±‚`a
Ù±‚`x                        Ù±‚`ecolorÙ±‚aoa=Ù±‚`jfill_colorÙ±‚`a,Ù±‚`a Ù±‚`ealphaÙ±‚aoa=Ù±‚bmfc0.2Ù±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚`baxÙ±‚aoa.Ù±‚`hannotateÙ±‚`a(Ù±‚bsaafÙ±‚bs1a'Ù±‚bsia{Ù±‚`etitleÙ±‚bsia}Ù±‚bs1a:Ù±‚bs1a'Ù±‚`a,Ù±‚`a
Ù±‚`t                    Ù±‚`bxyÙ±‚aoa=Ù±‚`a(Ù±‚bmfd0.06Ù±‚`a,Ù±‚`a Ù±‚`hbaselineÙ±‚`a Ù±‚aoa-Ù±‚`a Ù±‚bmfc0.3Ù±‚`a Ù±‚aoa*Ù±‚`a Ù±‚`mline_axesfracÙ±‚`a)Ù±‚`a,Ù±‚`a
Ù±‚`t                    Ù±‚`ecolorÙ±‚aoa=Ù±‚`lmpl_grey_rgbÙ±‚`a,Ù±‚`a Ù±‚`fweightÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1dboldÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚`baxÙ±‚aoa.Ù±‚`hannotateÙ±‚`a(Ù±‚`ddemoÙ±‚`a,Ù±‚`a
Ù±‚`t                    Ù±‚`bxyÙ±‚aoa=Ù±‚`a(Ù±‚bmfd0.04Ù±‚`a,Ù±‚`a Ù±‚`hbaselineÙ±‚`a Ù±‚aoa-Ù±‚`a Ù±‚bmfd0.75Ù±‚`a Ù±‚aoa*Ù±‚`a Ù±‚`mline_axesfracÙ±‚`a)Ù±‚`a,Ù±‚`a
Ù±‚`t                    Ù±‚`ecolorÙ±‚aoa=Ù±‚`lmpl_grey_rgbÙ±‚`a,Ù±‚`a Ù±‚`hfontsizeÙ±‚aoa=Ù±‚bmib16Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚`cpltÙ±‚aoa.Ù±‚`dshowÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚akbifÙ±‚`a Ù±‚bs1a'Ù±‚bs1g--latexÙ±‚bs1a'Ù±‚`a Ù±‚bowbinÙ±‚`a Ù±‚`csysÙ±‚aoa.Ù±‚`dargvÙ±‚`a:Ù±‚`a
Ù±‚`d    Ù±‚bc1x*# Run: python mathtext_examples.py --latexÙ±‚`a
Ù±‚`d    Ù±‚bc1x$# Need amsmath and amssymb packages.Ù±‚`a
Ù±‚`d    Ù±‚akdwithÙ±‚`a Ù±‚bnbdopenÙ±‚`a(Ù±‚bs2a"Ù±‚bs2umathtext_examples.ltxÙ±‚bs2a"Ù±‚`a,Ù±‚`a Ù±‚bs2a"Ù±‚bs2awÙ±‚bs2a"Ù±‚`a)Ù±‚`a Ù±‚akbasÙ±‚`a Ù±‚`bfdÙ±‚`a:Ù±‚`a
Ù±‚`h        Ù±‚`bfdÙ±‚aoa.Ù±‚`ewriteÙ±‚`a(Ù±‚bs2a"Ù±‚bseb\\Ù±‚bs2mdocumentclassÙ±‚bsii{article}Ù±‚bseb\nÙ±‚bs2a"Ù±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚`bfdÙ±‚aoa.Ù±‚`ewriteÙ±‚`a(Ù±‚bs2a"Ù±‚bseb\\Ù±‚bs2jusepackageÙ±‚bs2a{Ù±‚bs2qamsmath, amssymb}Ù±‚bseb\nÙ±‚bs2a"Ù±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚`bfdÙ±‚aoa.Ù±‚`ewriteÙ±‚`a(Ù±‚bs2a"Ù±‚bseb\\Ù±‚bs2ebeginÙ±‚bsij{document}Ù±‚bseb\nÙ±‚bs2a"Ù±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚`bfdÙ±‚aoa.Ù±‚`ewriteÙ±‚`a(Ù±‚bs2a"Ù±‚bseb\\Ù±‚bs2ebeginÙ±‚bsik{enumerate}Ù±‚bseb\nÙ±‚bs2a"Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`h        Ù±‚akcforÙ±‚`a Ù±‚`asÙ±‚`a Ù±‚bowbinÙ±‚`a Ù±‚`nmathtext_demosÙ±‚aoa.Ù±‚`fvaluesÙ±‚`a(Ù±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`l            Ù±‚`asÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`breÙ±‚aoa.Ù±‚`csubÙ±‚`a(Ù±‚bsaarÙ±‚bs2a"Ù±‚bs2d(?<!Ù±‚bseb\\Ù±‚bs2a)Ù±‚bs2a\Ù±‚bs2a$Ù±‚bs2a"Ù±‚`a,Ù±‚`a Ù±‚bs2a"Ù±‚bs2b$$Ù±‚bs2a"Ù±‚`a,Ù±‚`a Ù±‚`asÙ±‚`a)Ù±‚`a
Ù±‚`l            Ù±‚`bfdÙ±‚aoa.Ù±‚`ewriteÙ±‚`a(Ù±‚bs2a"Ù±‚bseb\\Ù±‚bs2eitem Ù±‚bsib%sÙ±‚bseb\nÙ±‚bs2a"Ù±‚`a Ù±‚aoa%Ù±‚`a Ù±‚`asÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`h        Ù±‚`bfdÙ±‚aoa.Ù±‚`ewriteÙ±‚`a(Ù±‚bs2a"Ù±‚bseb\\Ù±‚bs2cendÙ±‚bsik{enumerate}Ù±‚bseb\nÙ±‚bs2a"Ù±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚`bfdÙ±‚aoa.Ù±‚`ewriteÙ±‚`a(Ù±‚bs2a"Ù±‚bseb\\Ù±‚bs2cendÙ±‚bsij{document}Ù±‚bseb\nÙ±‚bs2a"Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚`jsubprocessÙ±‚aoa.Ù±‚`dcallÙ±‚`a(Ù±‚`a[Ù±‚bs2a"Ù±‚bs2hpdflatexÙ±‚bs2a"Ù±‚`a,Ù±‚`a Ù±‚bs2a"Ù±‚bs2umathtext_examples.ltxÙ±‚bs2a"Ù±‚`a]Ù±‚`a)Ù±‚`a
Ù±‚akdelseÙ±‚`a:Ù±‚`a
Ù±‚`d    Ù±‚`edoallÙ±‚`a(Ù±‚`a)Ù±‚`a
`dNoneö