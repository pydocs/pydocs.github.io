������������bsda
���`x`"""
===========
Symlog Demo
===========

Example use of symlog (symmetric log) axis scaling.
"""���bkna
���`fimport���bnna ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���`fpyplot���aka ���`bas���bnna ���`cplt���bkna
���`fimport���bnna ���`���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����aka ���`bas���bnna ���`bnp���`a
���`a
���`bdt���aoa ���`a=���bmfa ���`d0.01���`a
���`ax���aoa ���`a=���`a ���aobnp���`a.���`farange���aoa(���bmfa-���`d50.0���`a,���bmfa ���`d50.0���`a,���`a ���`bdt���`a)���`a
���`ay���aoa ���`a=���`a ���aobnp���`a.���`farange���bmia(���`a0���`a,���bmfa ���`e100.0���`a,���`a ���`bdt���`a)���`a
���`a
���`cfig���`a,���`a ���`a(���`cax0���`a,���`a ���`cax1���`a,���`a ���`cax2���`a)���aoa ���`a=���`a ���aocplt���`a.���`hsubplots���`a(���aoenrows���bmia=���`a3���`a)���`a
���`a
���aocax0���`a.���`dplot���`a(���`ax���`a,���`a ���`ay���`a)���`a
���aocax0���`a.���`jset_xscale���bs1a(���bs1a'���bs1fsymlog���`a'���`a)���`a
���aocax0���`a.���`jset_ylabel���bs1a(���bs1a'���bs1gsymlogx���`a'���`a)���`a
���aocax0���`a.���`dgrid���`a(���`a)���`a
���aocax0���`a.���aoexaxis���`a.���`dgrid���`a(���aoewhich���bs1a=���bs1a'���bs1eminor���`a'���`a)���bc1b  ���`s# minor grid on too���`a
���`a
���aocax1���`a.���`dplot���`a(���`ay���`a,���`a ���`ax���`a)���`a
���aocax1���`a.���`jset_yscale���bs1a(���bs1a'���bs1fsymlog���`a'���`a)���`a
���aocax1���`a.���`jset_ylabel���bs1a(���bs1a'���bs1gsymlogy���`a'���`a)���`a
���`a
���aocax2���`a.���`dplot���`a(���`ax���`a,���`a ���aobnp���`a.���`csin���`a(���`ax���aoa ���`a/���bmfa ���`c3.0���`a)���`a)���`a
���aocax2���`a.���`jset_xscale���bs1a(���bs1a'���bs1fsymlog���`a'���`a)���`a
���aocax2���`a.���`jset_yscale���bs1a(���bs1a'���bs1fsymlog���`a'���`a,���`a ���aoilinthresh���bmfa=���`e0.015���`a)���`a
���aocax2���`a.���`dgrid���`a(���`a)���`a
���aocax2���`a.���`jset_ylabel���bs1a(���bs1a'���bs1ksymlog both���`a'���`a)���`a
���`a
���aocfig���`a.���`ltight_layout���`a(���`a)���`a
���aocplt���`a.���`dshow���`a(���`a)`dNone�