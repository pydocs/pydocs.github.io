{
  "_content": {
    "Attributes": {
      "children": [],
      "title": null
    },
    "Extended Summary": {
      "children": [
        {
          "type": "Paragraph",
          "data": {
            "inline": [
              {
                "type": "Words",
                "data": {
                  "value": "DEPRECATED. Suboptimal, retained for backwards compatibility."
                }
              }
            ],
            "inner": []
          }
        },
        {
          "type": "Paragraph",
          "data": {
            "inline": [
              {
                "type": "Words",
                "data": {
                  "value": "You should use the form 'var = !command' instead. Example:"
                }
              }
            ],
            "inner": []
          }
        },
        {
          "type": "BlockQuote",
          "data": {
            "value": [
              "\"%sc -l myfiles = ls ~\" should now be written as",
              "",
              "\"myfiles = !ls ~\""
            ]
          }
        },
        {
          "type": "Paragraph",
          "data": {
            "inline": [
              {
                "type": "Words",
                "data": {
                  "value": "myfiles.s, myfiles.l and myfiles.n still apply as documented below."
                }
              }
            ],
            "inner": []
          }
        },
        {
          "type": "Paragraph",
          "data": {
            "inline": [
              {
                "type": "Words",
                "data": {
                  "value": "-- %sc [options] varname=command"
                }
              }
            ],
            "inner": []
          }
        },
        {
          "type": "Paragraph",
          "data": {
            "inline": [
              {
                "type": "Words",
                "data": {
                  "value": "IPython will run the given command using commands.getoutput(), and will then update the user's interactive namespace with a variable called varname, containing the value of the call.  Your command can contain shell wildcards, pipes, etc."
                }
              }
            ],
            "inner": []
          }
        },
        {
          "type": "Paragraph",
          "data": {
            "inline": [
              {
                "type": "Words",
                "data": {
                  "value": "The '=' sign in the syntax is mandatory, and the variable name you supply must follow Python's standard conventions for valid names."
                }
              }
            ],
            "inner": []
          }
        },
        {
          "type": "Paragraph",
          "data": {
            "inline": [
              {
                "type": "Words",
                "data": {
                  "value": "(A special format without variable name exists for internal use)"
                }
              }
            ],
            "inner": []
          }
        },
        {
          "type": "Paragraph",
          "data": {
            "inline": [
              {
                "type": "Words",
                "data": {
                  "value": "Options:"
                }
              }
            ],
            "inner": []
          }
        },
        {
          "type": "BlockQuote",
          "data": {
            "value": [
              "-l: list output.  Split the output on newlines into a list before",
              "assigning it to the given variable.  By default the output is stored",
              "as a single string.",
              "",
              "-v: verbose.  Print the contents of the variable."
            ]
          }
        },
        {
          "type": "Paragraph",
          "data": {
            "inline": [
              {
                "type": "Words",
                "data": {
                  "value": "In most cases you should not need to split as a list, because the returned value is a special type of string which can automatically provide its contents either as a list (split on newlines) or as a space-separated string.  These are convenient, respectively, either for sequential processing or to be passed to a shell command."
                }
              }
            ],
            "inner": []
          }
        },
        {
          "type": "Paragraph",
          "data": {
            "inline": [
              {
                "type": "Words",
                "data": {
                  "value": "For example::      "
                }
              }
            ],
            "inner": []
          }
        },
        {
          "type": "BlockVerbatim",
          "data": {
            "lines": {
              "_lines": [
                {
                  "_line": "# Capture into variable a",
                  "_number": 0,
                  "_offset": 0
                },
                {
                  "_line": "In [1]: sc a=ls *py",
                  "_number": 1,
                  "_offset": 0
                },
                {
                  "_line": "",
                  "_number": 2,
                  "_offset": 0
                },
                {
                  "_line": "# a is a string with embedded newlines",
                  "_number": 3,
                  "_offset": 0
                },
                {
                  "_line": "In [2]: a",
                  "_number": 4,
                  "_offset": 0
                },
                {
                  "_line": "Out[2]: 'setup.py\\nwin32_manual_post_install.py'",
                  "_number": 5,
                  "_offset": 0
                },
                {
                  "_line": "",
                  "_number": 6,
                  "_offset": 0
                },
                {
                  "_line": "# which can be seen as a list:",
                  "_number": 7,
                  "_offset": 0
                },
                {
                  "_line": "In [3]: a.l",
                  "_number": 8,
                  "_offset": 0
                },
                {
                  "_line": "Out[3]: ['setup.py', 'win32_manual_post_install.py']",
                  "_number": 9,
                  "_offset": 0
                },
                {
                  "_line": "",
                  "_number": 10,
                  "_offset": 0
                },
                {
                  "_line": "# or as a whitespace-separated string:",
                  "_number": 11,
                  "_offset": 0
                },
                {
                  "_line": "In [4]: a.s",
                  "_number": 12,
                  "_offset": 0
                },
                {
                  "_line": "Out[4]: 'setup.py win32_manual_post_install.py'",
                  "_number": 13,
                  "_offset": 0
                },
                {
                  "_line": "",
                  "_number": 14,
                  "_offset": 0
                },
                {
                  "_line": "# a.s is useful to pass as a single command line:",
                  "_number": 15,
                  "_offset": 0
                },
                {
                  "_line": "In [5]: !wc -l $a.s",
                  "_number": 16,
                  "_offset": 0
                },
                {
                  "_line": "  146 setup.py",
                  "_number": 17,
                  "_offset": 0
                },
                {
                  "_line": "  130 win32_manual_post_install.py",
                  "_number": 18,
                  "_offset": 0
                },
                {
                  "_line": "  276 total",
                  "_number": 19,
                  "_offset": 0
                },
                {
                  "_line": "",
                  "_number": 20,
                  "_offset": 0
                },
                {
                  "_line": "# while the list form is useful to loop over:",
                  "_number": 21,
                  "_offset": 0
                },
                {
                  "_line": "In [6]: for f in a.l:",
                  "_number": 22,
                  "_offset": 0
                },
                {
                  "_line": "   ...:      !wc -l $f",
                  "_number": 23,
                  "_offset": 0
                },
                {
                  "_line": "   ...:",
                  "_number": 24,
                  "_offset": 0
                },
                {
                  "_line": "146 setup.py",
                  "_number": 25,
                  "_offset": 0
                },
                {
                  "_line": "130 win32_manual_post_install.py",
                  "_number": 26,
                  "_offset": 0
                }
              ]
            }
          }
        },
        {
          "type": "Paragraph",
          "data": {
            "inline": [
              {
                "type": "Words",
                "data": {
                  "value": "Similarly, the lists returned by the -l option are also special, in the sense that you can equally invoke the .s attribute on them to automatically get a whitespace-separated string from their contents::      "
                }
              }
            ],
            "inner": []
          }
        },
        {
          "type": "BlockVerbatim",
          "data": {
            "lines": {
              "_lines": [
                {
                  "_line": "In [7]: sc -l b=ls *py",
                  "_number": 0,
                  "_offset": 0
                },
                {
                  "_line": "",
                  "_number": 1,
                  "_offset": 0
                },
                {
                  "_line": "In [8]: b",
                  "_number": 2,
                  "_offset": 0
                },
                {
                  "_line": "Out[8]: ['setup.py', 'win32_manual_post_install.py']",
                  "_number": 3,
                  "_offset": 0
                },
                {
                  "_line": "",
                  "_number": 4,
                  "_offset": 0
                },
                {
                  "_line": "In [9]: b.s",
                  "_number": 5,
                  "_offset": 0
                },
                {
                  "_line": "Out[9]: 'setup.py win32_manual_post_install.py'",
                  "_number": 6,
                  "_offset": 0
                }
              ]
            }
          }
        },
        {
          "type": "Paragraph",
          "data": {
            "inline": [
              {
                "type": "Words",
                "data": {
                  "value": "In summary, both the lists and strings used for output capture have the following special attributes::      "
                }
              }
            ],
            "inner": []
          }
        },
        {
          "type": "BlockVerbatim",
          "data": {
            "lines": {
              "_lines": [
                {
                  "_line": ".l (or .list) : value as list.",
                  "_number": 0,
                  "_offset": 0
                },
                {
                  "_line": ".n (or .nlstr): value as newline-separated string.",
                  "_number": 1,
                  "_offset": 0
                },
                {
                  "_line": ".s (or .spstr): value as space-separated string.",
                  "_number": 2,
                  "_offset": 0
                }
              ]
            }
          }
        }
      ],
      "title": null
    },
    "Methods": {
      "children": [],
      "title": null
    },
    "Notes": {
      "children": [],
      "title": null
    },
    "Other Parameters": {
      "children": [],
      "title": null
    },
    "Parameters": {
      "children": [],
      "title": null
    },
    "Raises": {
      "children": [],
      "title": null
    },
    "Receives": {
      "children": [],
      "title": null
    },
    "Returns": {
      "children": [],
      "title": null
    },
    "Summary": {
      "children": [
        {
          "type": "Paragraph",
          "data": {
            "inline": [
              {
                "type": "Words",
                "data": {
                  "value": "Shell capture - run shell command and capture output (DEPRECATED use !)."
                }
              }
            ],
            "inner": []
          }
        }
      ],
      "title": null
    },
    "Warnings": {
      "children": [],
      "title": null
    },
    "Warns": {
      "children": [],
      "title": null
    },
    "Yields": {
      "children": [],
      "title": null
    }
  },
  "refs": [],
  "ordered_sections": [
    "Summary",
    "Extended Summary"
  ],
  "item_file": "/dev/ipython/IPython/core/magics/osm.py",
  "item_line": 565,
  "item_type": "<class 'function'>",
  "aliases": [
    "IPython.core.magics.OSMagics.sc"
  ],
  "example_section_data": {
    "children": [],
    "title": null
  },
  "see_also": [],
  "version": "8.0.0.dev",
  "signature": "sc(self, parameter_s='')",
  "references": null,
  "logo": "logo.png",
  "qa": "IPython.core.magics.osm.OSMagics.sc",
  "arbitrary": []
}