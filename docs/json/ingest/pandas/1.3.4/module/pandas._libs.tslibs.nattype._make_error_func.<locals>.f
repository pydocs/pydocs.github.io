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
            "param": "ordinal",
            "type_": "int",
            "desc": [
              {
                "type": "Paragraph",
                "data": {
                  "inline": [
                    {
                      "type": "Words",
                      "data": {
                        "value": "Date corresponding to a proleptic Gregorian ordinal."
                      }
                    }
                  ],
                  "inner": []
                }
              }
            ]
          }
        },
        {
          "type": "Param",
          "data": {
            "param": "freq",
            "type_": "str, DateOffset",
            "desc": [
              {
                "type": "Paragraph",
                "data": {
                  "inline": [
                    {
                      "type": "Words",
                      "data": {
                        "value": "Offset to apply to the Timestamp."
                      }
                    }
                  ],
                  "inner": []
                }
              }
            ]
          }
        },
        {
          "type": "Param",
          "data": {
            "param": "tz",
            "type_": "str, pytz.timezone, dateutil.tz.tzfile or None",
            "desc": [
              {
                "type": "Paragraph",
                "data": {
                  "inline": [
                    {
                      "type": "Words",
                      "data": {
                        "value": "Time zone for the Timestamp."
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
                  "value": "Passed an ordinal, translate and convert to a ts. Note: by definition there cannot be any tz info on the ordinal itself."
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
      "version": "1.3.4",
      "kind": "module",
      "path": "pandas._libs.tslibs.timestamps.Timestamp"
    }
  ],
  "ordered_sections": [
    "Signature",
    "Summary",
    "Parameters",
    "Examples"
  ],
  "item_file": null,
  "item_line": null,
  "item_type": "<class 'cython_function_or_method'>",
  "aliases": [
    "pandas._libs.NaTType.utctimetuple",
    "pandas._libs.NaTType.timetz",
    "pandas._libs.NaTType.timetuple",
    "pandas._libs.NaTType.isocalendar",
    "pandas._libs.NaTType.dst",
    "pandas._libs.NaTType.ctime",
    "pandas._libs.NaTType.time",
    "pandas._libs.NaTType.toordinal",
    "pandas._libs.NaTType.tzname",
    "pandas._libs.NaTType.utcoffset",
    "pandas._libs.NaTType.fromisocalendar",
    "pandas._libs.NaTType.strftime",
    "pandas._libs.NaTType.strptime",
    "pandas._libs.NaTType.utcfromtimestamp",
    "pandas._libs.NaTType.fromtimestamp",
    "pandas._libs.NaTType.combine",
    "pandas._libs.NaTType.utcnow",
    "pandas._libs.NaTType.timestamp",
    "pandas._libs.NaTType.astimezone",
    "pandas._libs.NaTType.fromordinal"
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
                    "version": "1.3.4",
                    "kind": "module",
                    "path": "pandas._libs.tslibs.timestamps.Timestamp"
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
                "data": "fromordinal"
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
              "type": "mi",
              "link": {
                "type": "str",
                "data": "737425"
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
          "out": "Timestamp('2020-01-01 00:00:00')",
          "ce_status": "exception_in_exec"
        }
      }
    ],
    "title": null
  },
  "see_also": [],
  "version": "1.3.4",
  "signature": "Timestamp.fromordinal(ordinal, freq=None, tz=None)",
  "references": null,
  "logo": "logo.png",
  "qa": "pandas._libs.tslibs.nattype._make_error_func.<locals>.f",
  "arbitrary": []
}