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
            "param": "locale",
            "type_": "str, default None (English locale)",
            "desc": [
              {
                "type": "Paragraph",
                "data": {
                  "inline": [
                    {
                      "type": "Words",
                      "data": {
                        "value": "Locale determining the language in which to return the day name."
                      }
                    }
                  ],
                  "inner": []
                }
              }
            ]
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
            "type_": "str",
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
                  "value": "Return the day name of the Timestamp with specified locale."
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
      "path": "pandas._libs.tslibs.nattype.NaTType"
    },
    {
      "module": "pandas",
      "version": "1.4.0",
      "kind": "module",
      "path": "pandas.core.arrays.datetimes.DatetimeArray.day_name"
    },
    {
      "module": "pandas",
      "version": "1.4.0",
      "kind": "module",
      "path": "pandas._libs.tslibs.timestamps.Timestamp"
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
    "pandas._libs.NaTType.weekday",
    "pandas._libs.NaTType.isoweekday",
    "pandas._libs.NaTType.total_seconds",
    "pandas._libs.NaTType.month_name",
    "pandas._libs.NaTType.day_name"
  ],
  "example_section_data": {
    "children": [
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
                  "value": "day_name",
                  "reference": {
                    "module": "pandas",
                    "version": "1.4.0",
                    "kind": "module",
                    "path": "pandas.core.arrays.datetimes.DatetimeArray.day_name"
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
              "type": "",
              "link": {
                "type": "str",
                "data": ")"
              }
            }
          ],
          "out": "'Saturday'",
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
                "type": "Link",
                "data": {
                  "value": "day_name",
                  "reference": {
                    "module": "pandas",
                    "version": "1.4.0",
                    "kind": "module",
                    "path": "pandas.core.arrays.datetimes.DatetimeArray.day_name"
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
              "type": "",
              "link": {
                "type": "str",
                "data": ")"
              }
            }
          ],
          "out": "nan",
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
  "qa": "pandas._libs.tslibs.nattype._make_nan_func.<locals>.f",
  "arbitrary": []
}