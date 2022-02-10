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
            "value": "# Capture into variable a\nIn [1]: sc a=ls *py\n\n# a is a string with embedded newlines\nIn [2]: a\nOut[2]: 'setup.py\\nwin32_manual_post_install.py'\n\n# which can be seen as a list:\nIn [3]: a.l\nOut[3]: ['setup.py', 'win32_manual_post_install.py']\n\n# or as a whitespace-separated string:\nIn [4]: a.s\nOut[4]: 'setup.py win32_manual_post_install.py'\n\n# a.s is useful to pass as a single command line:\nIn [5]: !wc -l $a.s\n  146 setup.py\n  130 win32_manual_post_install.py\n  276 total\n\n# while the list form is useful to loop over:\nIn [6]: for f in a.l:\n   ...:      !wc -l $f\n   ...:\n146 setup.py\n130 win32_manual_post_install.py"
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
            "value": "In [7]: sc -l b=ls *py\n\nIn [8]: b\nOut[8]: ['setup.py', 'win32_manual_post_install.py']\n\nIn [9]: b.s\nOut[9]: 'setup.py win32_manual_post_install.py'"
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
            "value": ".l (or .list) : value as list.\n.n (or .nlstr): value as newline-separated string.\n.s (or .spstr): value as space-separated string."
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
  "item_line": 563,
  "item_type": "<class 'function'>",
  "aliases": [
    "IPython.core.magics.OSMagics.sc"
  ],
  "example_section_data": {
    "children": [],
    "title": null
  },
  "see_also": [],
  "version": "8.1.0.dev",
  "signature": "sc(self, parameter_s='')",
  "references": null,
  "logo": "logo.png",
  "qa": "IPython.core.magics.osm.OSMagics.sc",
  "arbitrary": []
}