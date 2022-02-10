{
  "_content": {
    "Attributes": {
      "children": [],
      "title": null
    },
    "Extended Summary": {
      "children": [],
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
      "children": [
        {
          "type": "Param",
          "data": {
            "param": "year",
            "type_": "int, optional",
            "desc": []
          }
        },
        {
          "type": "Param",
          "data": {
            "param": "month",
            "type_": "int, optional",
            "desc": []
          }
        },
        {
          "type": "Param",
          "data": {
            "param": "day",
            "type_": "int, optional",
            "desc": []
          }
        },
        {
          "type": "Param",
          "data": {
            "param": "hour",
            "type_": "int, optional",
            "desc": []
          }
        },
        {
          "type": "Param",
          "data": {
            "param": "minute",
            "type_": "int, optional",
            "desc": []
          }
        },
        {
          "type": "Param",
          "data": {
            "param": "second",
            "type_": "int, optional",
            "desc": []
          }
        },
        {
          "type": "Param",
          "data": {
            "param": "microsecond",
            "type_": "int, optional",
            "desc": []
          }
        },
        {
          "type": "Param",
          "data": {
            "param": "nanosecond",
            "type_": "int, optional",
            "desc": []
          }
        },
        {
          "type": "Param",
          "data": {
            "param": "tzinfo",
            "type_": "tz-convertible, optional",
            "desc": []
          }
        },
        {
          "type": "Param",
          "data": {
            "param": "fold",
            "type_": "int, optional",
            "desc": []
          }
        }
      ],
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
      "children": [
        {
          "type": "Param",
          "data": {
            "param": "",
            "type_": "Timestamp with fields replaced",
            "desc": []
          }
        }
      ],
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
                  "value": "Implements datetime.replace, handles nanoseconds."
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
  "refs": [
    {
      "module": "pandas",
      "version": "1.4.0",
      "kind": "module",
      "path": "pandas.compat._optional.import_optional_dependency"
    },
    {
      "module": "pandas",
      "version": "1.4.0",
      "kind": "module",
      "path": "pandas._libs.tslibs.timestamps.Timestamp"
    },
    {
      "module": "pandas",
      "version": "1.4.0",
      "kind": "module",
      "path": "pandas._libs.tslibs.nattype.NaTType"
    }
  ],
  "ordered_sections": [
    "Summary",
    "Parameters",
    "Returns",
    "Examples"
  ],
  "item_file": null,
  "item_line": null,
  "item_type": "<class 'cython_function_or_method'>",
  "aliases": [
    "pandas._libs.NaTType.date",
    "pandas._libs.NaTType.to_pydatetime",
    "pandas._libs.NaTType.now",
    "pandas._libs.NaTType.today",
    "pandas._libs.NaTType.round",
    "pandas._libs.NaTType.floor",
    "pandas._libs.NaTType.ceil",
    "pandas._libs.NaTType.tz_convert",
    "pandas._libs.NaTType.tz_localize",
    "pandas._libs.NaTType.replace"
  ],
  "example_section_data": {
    "children": [
      {
        "type": "Paragraph",
        "data": {
          "inline": [
            {
              "type": "Words",
              "data": {
                "value": "Create a timestamp object:"
              }
            }
          ],
          "inner": []
        }
      },
      {
        "type": "Code2",
        "data": {
          "entries": [
            {
              "type": "",
              "link": {
                "type": "str",
                "data": "ts"
              }
            },
            {
              "type": "",
              "link": {
                "type": "str",
                "data": " "
              }
            },
            {
              "type": "o",
              "link": {
                "type": "str",
                "data": "="
              }
            },
            {
              "type": "",
              "link": {
                "type": "str",
                "data": " "
              }
            },
            {
              "type": "",
              "link": {
                "type": "str",
                "data": "pd"
              }
            },
            {
              "type": "o",
              "link": {
                "type": "str",
                "data": "."
              }
            },
            {
              "type": "",
              "link": {
                "type": "Link",
                "data": {
                  "value": "Timestamp",
                  "reference": {
                    "module": "pandas",
                    "version": "1.4.0",
                    "kind": "module",
                    "path": "pandas._libs.tslibs.timestamps.Timestamp"
                  },
                  "kind": "module",
                  "exists": true
                }
              }
            },
            {
              "type": "",
              "link": {
                "type": "str",
                "data": "("
              }
            },
            {
              "type": "s1",
              "link": {
                "type": "str",
                "data": "'"
              }
            },
            {
              "type": "s1",
              "link": {
                "type": "str",
                "data": "2020-03-14T15:32:52.192548651"
              }
            },
            {
              "type": "s1",
              "link": {
                "type": "str",
                "data": "'"
              }
            },
            {
              "type": "",
              "link": {
                "type": "str",
                "data": ","
              }
            },
            {
              "type": "",
              "link": {
                "type": "str",
                "data": " "
              }
            },
            {
              "type": "",
              "link": {
                "type": "str",
                "data": "tz"
              }
            },
            {
              "type": "o",
              "link": {
                "type": "str",
                "data": "="
              }
            },
            {
              "type": "s1",
              "link": {
                "type": "str",
                "data": "'"
              }
            },
            {
              "type": "s1",
              "link": {
                "type": "str",
                "data": "UTC"
              }
            },
            {
              "type": "s1",
              "link": {
                "type": "str",
                "data": "'"
              }
            },
            {
              "type": "",
              "link": {
                "type": "str",
                "data": ")"
              }
            },
            {
              "type": "",
              "link": {
                "type": "str",
                "data": "\n"
              }
            },
            {
              "type": "",
              "link": {
                "type": "str",
                "data": "ts"
              }
            }
          ],
          "out": "Timestamp('2020-03-14 15:32:52.192548651+0000', tz='UTC')",
          "ce_status": "compiled"
        }
      },
      {
        "type": "Paragraph",
        "data": {
          "inline": [
            {
              "type": "Words",
              "data": {
                "value": "Replace year and the hour:"
              }
            }
          ],
          "inner": []
        }
      },
      {
        "type": "Code2",
        "data": {
          "entries": [
            {
              "type": "",
              "link": {
                "type": "str",
                "data": "ts"
              }
            },
            {
              "type": "o",
              "link": {
                "type": "str",
                "data": "."
              }
            },
            {
              "type": "",
              "link": {
                "type": "str",
                "data": "replace"
              }
            },
            {
              "type": "",
              "link": {
                "type": "str",
                "data": "("
              }
            },
            {
              "type": "",
              "link": {
                "type": "str",
                "data": "year"
              }
            },
            {
              "type": "o",
              "link": {
                "type": "str",
                "data": "="
              }
            },
            {
              "type": "mi",
              "link": {
                "type": "str",
                "data": "1999"
              }
            },
            {
              "type": "",
              "link": {
                "type": "str",
                "data": ","
              }
            },
            {
              "type": "",
              "link": {
                "type": "str",
                "data": " "
              }
            },
            {
              "type": "",
              "link": {
                "type": "str",
                "data": "hour"
              }
            },
            {
              "type": "o",
              "link": {
                "type": "str",
                "data": "="
              }
            },
            {
              "type": "mi",
              "link": {
                "type": "str",
                "data": "10"
              }
            },
            {
              "type": "",
              "link": {
                "type": "str",
                "data": ")"
              }
            }
          ],
          "out": "Timestamp('1999-03-14 10:32:52.192548651+0000', tz='UTC')",
          "ce_status": "compiled"
        }
      },
      {
        "type": "Paragraph",
        "data": {
          "inline": [
            {
              "type": "Words",
              "data": {
                "value": "Replace timezone (not a conversion):"
              }
            }
          ],
          "inner": []
        }
      },
      {
        "type": "Code2",
        "data": {
          "entries": [
            {
              "type": "kn",
              "link": {
                "type": "Link",
                "data": {
                  "value": "import",
                  "reference": {
                    "module": "pandas",
                    "version": "1.4.0",
                    "kind": "module",
                    "path": "pandas.compat._optional.import_optional_dependency"
                  },
                  "kind": "module",
                  "exists": true
                }
              }
            },
            {
              "type": "",
              "link": {
                "type": "str",
                "data": " "
              }
            },
            {
              "type": "nn",
              "link": {
                "type": "str",
                "data": "pytz"
              }
            },
            {
              "type": "",
              "link": {
                "type": "str",
                "data": "\n"
              }
            },
            {
              "type": "",
              "link": {
                "type": "str",
                "data": "ts"
              }
            },
            {
              "type": "o",
              "link": {
                "type": "str",
                "data": "."
              }
            },
            {
              "type": "",
              "link": {
                "type": "str",
                "data": "replace"
              }
            },
            {
              "type": "",
              "link": {
                "type": "str",
                "data": "("
              }
            },
            {
              "type": "",
              "link": {
                "type": "str",
                "data": "tzinfo"
              }
            },
            {
              "type": "o",
              "link": {
                "type": "str",
                "data": "="
              }
            },
            {
              "type": "",
              "link": {
                "type": "str",
                "data": "pytz"
              }
            },
            {
              "type": "o",
              "link": {
                "type": "str",
                "data": "."
              }
            },
            {
              "type": "",
              "link": {
                "type": "str",
                "data": "timezone"
              }
            },
            {
              "type": "",
              "link": {
                "type": "str",
                "data": "("
              }
            },
            {
              "type": "s1",
              "link": {
                "type": "str",
                "data": "'"
              }
            },
            {
              "type": "s1",
              "link": {
                "type": "str",
                "data": "US/Pacific"
              }
            },
            {
              "type": "s1",
              "link": {
                "type": "str",
                "data": "'"
              }
            },
            {
              "type": "",
              "link": {
                "type": "str",
                "data": ")"
              }
            },
            {
              "type": "",
              "link": {
                "type": "str",
                "data": ")"
              }
            }
          ],
          "out": "Timestamp('2020-03-14 15:32:52.192548651-0700', tz='US/Pacific')",
          "ce_status": "compiled"
        }
      },
      {
        "type": "Paragraph",
        "data": {
          "inline": [
            {
              "type": "Words",
              "data": {
                "value": "Analogous for "
              }
            },
            {
              "type": "Verbatim",
              "data": {
                "value": [
                  "pd.NaT"
                ]
              }
            },
            {
              "type": "Words",
              "data": {
                "value": ":"
              }
            }
          ],
          "inner": []
        }
      },
      {
        "type": "Code2",
        "data": {
          "entries": [
            {
              "type": "",
              "link": {
                "type": "str",
                "data": "pd"
              }
            },
            {
              "type": "o",
              "link": {
                "type": "str",
                "data": "."
              }
            },
            {
              "type": "",
              "link": {
                "type": "Link",
                "data": {
                  "value": "NaT",
                  "reference": {
                    "module": "pandas",
                    "version": "1.4.0",
                    "kind": "module",
                    "path": "pandas._libs.tslibs.nattype.NaTType"
                  },
                  "kind": "module",
                  "exists": true
                }
              }
            },
            {
              "type": "o",
              "link": {
                "type": "str",
                "data": "."
              }
            },
            {
              "type": "",
              "link": {
                "type": "str",
                "data": "replace"
              }
            },
            {
              "type": "",
              "link": {
                "type": "str",
                "data": "("
              }
            },
            {
              "type": "",
              "link": {
                "type": "str",
                "data": "tzinfo"
              }
            },
            {
              "type": "o",
              "link": {
                "type": "str",
                "data": "="
              }
            },
            {
              "type": "",
              "link": {
                "type": "str",
                "data": "pytz"
              }
            },
            {
              "type": "o",
              "link": {
                "type": "str",
                "data": "."
              }
            },
            {
              "type": "",
              "link": {
                "type": "str",
                "data": "timezone"
              }
            },
            {
              "type": "",
              "link": {
                "type": "str",
                "data": "("
              }
            },
            {
              "type": "s1",
              "link": {
                "type": "str",
                "data": "'"
              }
            },
            {
              "type": "s1",
              "link": {
                "type": "str",
                "data": "US/Pacific"
              }
            },
            {
              "type": "s1",
              "link": {
                "type": "str",
                "data": "'"
              }
            },
            {
              "type": "",
              "link": {
                "type": "str",
                "data": ")"
              }
            },
            {
              "type": "",
              "link": {
                "type": "str",
                "data": ")"
              }
            }
          ],
          "out": "NaT",
          "ce_status": "compiled"
        }
      }
    ],
    "title": null
  },
  "see_also": [],
  "version": "1.4.0",
  "signature": "f(*args, **kwargs)",
  "references": null,
  "logo": "logo.png",
  "qa": "pandas._libs.tslibs.nattype._make_nat_func.<locals>.f",
  "arbitrary": []
}