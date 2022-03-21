Ùª­jAttributesÙ¯‚€öpExtended SummaryÙ¯‚‘Ù¹‚Ù§x=DEPRECATED. Suboptimal, retained for backwards compatibility.€Ù¹‚Ù§x:You should use the form 'var = !command' instead. Example:€Ù·ƒx0"%sc -l myfiles = ls ~" should now be written as`q"myfiles = !ls ~"Ù¹‚Ù§xCmyfiles.s, myfiles.l and myfiles.n still apply as documented below.€Ù¹‚Ù§x -- %sc [options] varname=command€Ù¹‚Ù§xíIPython will run the given command using commands.getoutput(), and will then update the user's interactive namespace with a variable called varname, containing the value of the call.  Your command can contain shell wildcards, pipes, etc.€Ù¹‚Ù§x„The '=' sign in the syntax is mandatory, and the variable name you supply must follow Python's standard conventions for valid names.€Ù¹‚Ù§x@(A special format without variable name exists for internal use)€Ù¹‚Ù§hOptions:€Ù·…xA-l: list output.  Split the output on newlines into a list beforexDassigning it to the given variable.  By default the output is storedsas a single string.`x1-v: verbose.  Print the contents of the variable.Ù¹‚Ù§yHIn most cases you should not need to split as a list, because the returned value is a special type of string which can automatically provide its contents either as a list (split on newlines) or as a space-separated string.  These are convenient, respectively, either for sequential processing or to be passed to a shell command.€Ù¹‚Ù§sFor example::      €ÙÀyl# Capture into variable a
In [1]: sc a=ls *py

# a is a string with embedded newlines
In [2]: a
Out[2]: 'setup.py\nwin32_manual_post_install.py'

# which can be seen as a list:
In [3]: a.l
Out[3]: ['setup.py', 'win32_manual_post_install.py']

# or as a whitespace-separated string:
In [4]: a.s
Out[4]: 'setup.py win32_manual_post_install.py'

# a.s is useful to pass as a single command line:
In [5]: !wc -l $a.s
  146 setup.py
  130 win32_manual_post_install.py
  276 total

# while the list form is useful to loop over:
In [6]: for f in a.l:
   ...:      !wc -l $f
   ...:
146 setup.py
130 win32_manual_post_install.pyÙ¹‚Ù§xÑSimilarly, the lists returned by the -l option are also special, in the sense that you can equally invoke the .s attribute on them to automatically get a whitespace-separated string from their contents::      €ÙÀx“In [7]: sc -l b=ls *py

In [8]: b
Out[8]: ['setup.py', 'win32_manual_post_install.py']

In [9]: b.s
Out[9]: 'setup.py win32_manual_post_install.py'Ù¹‚Ù§xlIn summary, both the lists and strings used for output capture have the following special attributes::      €ÙÀx‚.l (or .list) : value as list.
.n (or .nlstr): value as newline-separated string.
.s (or .spstr): value as space-separated string.ögMethodsÙ¯‚€öeNotesÙ¯‚€öpOther ParametersÙ¯‚€öjParametersÙ¯‚€öfRaisesÙ¯‚€öhReceivesÙ¯‚€ögReturnsÙ¯‚€ögSummaryÙ¯‚Ù¹‚Ù§xHShell capture - run shell command and capture output (DEPRECATED use !).€öhWarningsÙ¯‚€öeWarnsÙ¯‚€öfYieldsÙ¯‚€ö‚gSummarypExtended Summaryx'/dev/ipython/IPython/core/magics/osm.py3r<class 'function'>xIPython.core.magics.OSMagics.scÙ¯‚€ö€i8.2.0.devÙ«xsc(self, parameter_s='')öx#IPython.core.magics.osm.OSMagics.sc€