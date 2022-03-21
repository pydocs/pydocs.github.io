����jAttributes�����pExtended Summary�����������wCall signatures::      ����x`plot([x], y, [fmt], *, data=None, **kwargs)
plot([x], y, [fmt], [x2], y2, [fmt2], ..., **kwargs)�������x9The coordinates of the points or line nodes are given by ������ax���b, ������ay���a.��������wThe optional parameter ������cfmt���x� is a convenient way for defining basic formatting like color, marker and linestyle. It's a shortcut string notation described in the ������eNotes���o section below.����x�>>> plot(x, y)        # plot x and y using default line style and color
>>> plot(x, y, 'bo')  # plot x and y using blue circle markers
>>> plot(y)           # plot y using x as index array 0..N-1
>>> plot(y, 'r+')     # ditto, but with red plusses�������lYou can use ���g.Line2D���jmatplotlibe3.5.1fmodulewmatplotlib.lines.Line2Dfmodule����xY properties as keyword arguments for more control on the appearance. Line properties and ������cfmt���x? can be mixed. The following two calls yield identical results:����x�>>> plot(x, y, 'go--', linewidth=2, markersize=12)
>>> plot(x, y, color='green', marker='o', linestyle='dashed',
...      linewidth=2, markersize=12)�������vWhen conflicting with ������cfmt���x$, keyword arguments take precedence.�����������vPlotting labelled data��������xjThere's a convenient way for plotting objects with labelled data (i.e. data that can be accessed by index ����hobj['y']���x!). Instead of giving the data in ������ax���e and ������ay���x$, you can provide the object in the ������ddata���x( parameter and just give the labels for ������ax���e and ������ay���b  ����x&>>> plot('xlabel', 'ylabel', data=obj)�������x:All indexable objects are supported. This could e.g. be a ���ddict�����d, a ���ppandas.DataFrame���fpandasa*capixpandas.core.frame.DataFramefmodule����x or a structured numpy array.�����������xPlotting multiple sets of data��������x5There are various ways to plot multiple sets of data.��ȁ��������x.The most straight forward way is just to call ���dplot�����x multiple times.   Example:����x->>> plot(x1, y1, 'bo')
>>> plot(x2, y2, 'go')�ȁ��������cIf ������ax���h and/or ������ay���xM are 2D arrays a separate data set will be drawn   for every column. If both ������ax���e and ������ay���x� are 2D, they must have the   same shape. If only one of them is 2D with shape (N, m) the other   must have length N and will be used for every data set m.��������hExample:����xK>>> x = [1, 2, 3]
>>> y = np.array([[1, 2], [3, 4], [5, 6]])
>>> plot(x, y)�������qis equivalent to:����x<>>> for col in range(y.shape[1]):
...     plot(x, y[:, col])�ȁ��������x-The third way is to specify multiple sets of ������c[x]���b, ������ay���b, ������e[fmt]���o   groups::    ����x$>>> plot(x1, y1, 'g^', x2, y2, 'g-')�������xvIn this case, any additional keyword argument applies to all   datasets. Also this syntax cannot be combined with the ������ddata���m   parameter.��������xVBy default, each line is assigned a different style specified by a 'style cycle'. The ������cfmt���x� and line property parameters are only necessary if you want explicit deviations from these defaults. Alternatively, you can also change the style cycle using ���oaxes.prop_cycle�brc���a.��gMethods�����eNotes��������������nFormat Strings��������xEA format string consists of a part for color, marker and line::      ����xfmt = '[marker][line][color]'�������xaEach of them is optional. If not provided, the value from the style cycle is used. Exception: If ����dline���r is given, but no ����fmarker���x*, the data will be a line without markers.��������xOther combinations such as ����u[color][marker][line]���xB are also supported, but note that their parsing may be ambiguous.�����������gMarkers�����3���x|=============   =============================== character       description =============   =============================== ����c'.'���v         point marker ����c','���v         pixel marker ����c'o'���w         circle marker ����c'v'���x         triangle_down marker ����c'^'���x         triangle_up marker ����c'<'���x         triangle_left marker ����c'>'���x         triangle_right marker ����c'1'���x         tri_down marker ����c'2'���w         tri_up marker ����c'3'���x         tri_left marker ����c'4'���x         tri_right marker ����c'8'���x         octagon marker ����c's'���w         square marker ����c'p'���x         pentagon marker ����c'P'���x         plus (filled) marker ����c'*'���u         star marker ����c'h'���x         hexagon1 marker ����c'H'���x         hexagon2 marker ����c'+'���u         plus marker ����c'x'���r         x marker ����c'X'���x         x (filled) marker ����c'D'���x         diamond marker ����c'd'���x         thin_diamond marker ����c'|'���v         vline marker ����c'_'���xE         hline marker =============   ===============================�����������kLine Styles��������x=============    =============================== character        description =============    =============================== ����c'-'���x          solid line style ����d'--'���x         dashed line style ����d'-.'���x         dash-dot line style ����c':'���xL          dotted line style =============    ===============================��������xExample format strings::      ����x�'b'    # blue markers with default shape
'or'   # red circles
'-g'   # green solid line
'--'   # dashed line with default color
'^k:'  # black triangle_up markers connected by a dotted line����������fColors��������x=The supported color abbreviations are the single letter codes��������xy=============    =============================== character        color =============    =============================== ����c'b'���o          blue ����c'g'���p          green ����c'r'���n          red ����c'c'���o          cyan ����c'm'���r          magenta ����c'y'���q          yellow ����c'k'���p          black ����c'w'���x@          white =============    ===============================��������hand the ����d'CN'���x3 colors that index into the default property cycle.��������xRIf the color is the only part of the format string, you can additionally use any  ���qmatplotlib.colors���jmatplotlibe3.5.1fmoduleqmatplotlib.colorsfmodule����x spec, e.g. full names (����g'green'���r) or hex strings (����i'#008000'���b).��pOther Parameters�������nscalex, scaleysbool, default: True��������xjThese parameters determine if the view limits are adapted to the data limits. The values are passed on to ���nautoscale_view���jmatplotlibe3.5.1fmodulex.matplotlib.axes._base._AxesBase.autoscale_viewfmodule����a.����h**kwargsx`.Line2D` properties, optional�����������fkwargs���x} are used to specify properties like a line label (for auto legends), linewidth, antialiasing, marker face color. Example::  ����xw>>> plot([1, 2, 3], [1, 2, 3], 'go-', label='line 1', linewidth=2)
>>> plot([1, 2, 3], [1, 4, 9], 'rs', label='line 2')�������x�If you specify multiple lines with one plot call, the kwargs apply to all those lines. In case the label object is iterable, each element is used as labels for each set of data.��������xHere is a list of available ���g.Line2D���jmatplotlibe3.5.1fmodulewmatplotlib.lines.Line2Dfmodule����l properties:��������x�Properties: agg_filter: a filter function, which takes a (m, n, 3) float array and a dpi value, and returns a (m, n, 3) array alpha: scalar or None animated: bool antialiased or aa: bool clip_box: ���e.Bbox���jmatplotlibe3.5.1fmodulexmatplotlib.transforms.Bboxfmodule����x^ clip_on: bool clip_path: Patch or (Path, Transform) or None color or c: color dash_capstyle: ���i.CapStyle���jmatplotlibe3.5.1fmodulexmatplotlib._enums.CapStylefmodule����x4 or {'butt', 'projecting', 'round'} dash_joinstyle: ���j.JoinStyle���jmatplotlibe3.5.1fmodulexmatplotlib._enums.JoinStylefmodule����x� or {'miter', 'round', 'bevel'} dashes: sequence of floats (on/off ink in points) or (None, None) data: (2, N) array or two 1D arrays drawstyle or ds: {'default', 'steps', 'steps-pre', 'steps-mid', 'steps-post'}, default: 'default' figure: ���g.Figure���jmatplotlibe3.5.1fmodulexmatplotlib.figure.Figurefmodule����x� fillstyle: {'full', 'left', 'right', 'bottom', 'top', 'none'} gid: str in_layout: bool label: object linestyle or ls: {'-', '--', '-.', ':', '', (offset, on-off-seq), ...} linewidth or lw: float marker: marker style string, ���k~.path.Path���jmatplotlibe3.5.1fmoduletmatplotlib.path.Pathfmodule����d or ���u~.markers.MarkerStyle���jmatplotlibe3.5.1fmodulexmatplotlib.markers.MarkerStylefmodule����y	 markeredgecolor or mec: color markeredgewidth or mew: float markerfacecolor or mfc: color markerfacecoloralt or mfcalt: color markersize or ms: float markevery: None or int or (int, int) or slice or list[int] or float or (float, float) or list[bool] path_effects: ���s.AbstractPathEffect�����x� picker: float or callable[[Artist, Event], tuple[bool, dict]] pickradius: float rasterized: bool sketch_params: (scale: float, length: float, randomness: float) snap: bool or None solid_capstyle: ���i.CapStyle���jmatplotlibe3.5.1fmodulexmatplotlib._enums.CapStylefmodule����x5 or {'butt', 'projecting', 'round'} solid_joinstyle: ���j.JoinStyle���jmatplotlibe3.5.1fmodulexmatplotlib._enums.JoinStylefmodule����xw or {'miter', 'round', 'bevel'} transform: unknown url: str visible: bool xdata: 1D array ydata: 1D array zorder: float��jParameters�������dx, ytarray-like or scalar��������x:The horizontal / vertical coordinates of the data points. ������ax���x$ values are optional and default to ����mrange(len(y))���a.��������x)Commonly, these parameters are 1D arrays.��������xfThey can also be scalars, or two-dimensional (in that case, the columns represent separate data sets).��������x-These arguments cannot be passed as keywords.����cfmtmstr, optional��������x4A format string, e.g. 'ro' for red circles. See the ������eNotes���x6 section for a full description of the format strings.��������x�Format strings are just an abbreviation for quickly setting basic line properties. All of these and more can also be controlled by keyword arguments.��������x*This argument cannot be passed as keyword.����ddataxindexable object, optional��������xKAn object with labelled data. If given, provide the label names to plot in ������ax���e and ������ay���a.��ƃdnote`��������yfTechnically there ' s a slight ambiguity in calls where the second label is a valid *fmt*. ``plot ( ' n ' , ' o ' , data=obj)`` could be ``plt ( x, y)`` or ``plt ( y, fmt)``. In such cases, the former interpretation is chosen, but a warning is issued. You may suppress the warning by adding an empty format string ``plot ( ' n ' , ' o ' , ' ' , data=obj)``. ��fRaises�����hReceives�����gReturns�������`qlist of `.Line2D`��������x.A list of lines representing the plotted data.��gSummary�����������x(Plot y versus x as lines and/or markers.��hWarnings�����eWarns�����fYields������gSummarypExtended SummaryjParametersgReturnspOther ParametershSee AlsoeNotesx/matplotlib/axes/_axes.pylr<class 'function'>�xmatplotlib.pyplot.Axes.plot������������gscatterx"matplotlib.axes._axes.Axes.scatter���������x`XY scatter plot with markers of varying size and/or color ( sometimes also called bubble chart).��e3.5.1���x@plot(self, *args, scalex=True, scaley=True, data=None, **kwargs)�xmatplotlib.axes._axes.Axes.plot�